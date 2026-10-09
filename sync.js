'use strict';
/**
 * sync.js — PIN-based cross-device sync for the OCOM Question Hub.
 *
 * No accounts, no login. A PIN is just a shared "room code": whoever has it
 * can read/write the same cloud documents. They hold every block's
 * localStorage progress (flags, scores, attempts, settings), synced across
 * all blocks in one action since they all share this origin's localStorage
 * already.
 *
 * Layout: one document per block, syncs/{PIN}_{block}. Firestore caps a
 * document at 1 MiB. The first version kept everything in one document,
 * syncs/{PIN}, and with every answer carrying its objective text that filled
 * up after roughly 2,800 answers across all blocks (first hit in Oct 2026).
 * Now each block has its own document, and the cloud copy of each answer
 * leaves out its SDL title and objective text, which the question bank
 * looks up from data.js instead; a block at MAX_ATTEMPTS_STORED answers stays
 * well under the cap. The old syncs/{PIN} document is still read and merged
 * in, so nothing in it is lost, and once a push has written every block's
 * document it is emptied to a marker. A device still running an older copy
 * of this script may write it again; the next push from this one folds that
 * back in.
 *
 * Storage: Cloud Firestore, accessed directly via its REST API (no SDK load,
 * stays consistent with the rest of this site being plain vanilla JS).
 *
 * Push and Pull are both NON-DESTRUCTIVE: each one computes a union merge of
 * local + remote data first, so neither action can silently lose progress.
 * Push writes the merged result to the cloud. Pull writes the merged result
 * to this device. Running either one repeatedly is safe/idempotent.
 */

// ---- Fill these in from your Firebase project (see setup instructions) ----
const FIREBASE_CONFIG = {
  projectId: 'q-bank-cache',
  apiKey: 'AIzaSyAvYYQ5gAjcRN4W52ulCZ5nuA9BsuvNqN4',
};
// ----------------------------------------------------------------------

const BLOCK_KEYS = ['neuro', 'pulm', 'eent', 'endocrine', 'ortho', 'rheum', 'psych', 'nephro', 'omm'];
const SUFFIXES = ['flags_v1', 'progress_v1', 'attempts_v1', 'settings_v1'];
// The Lesion Atlas keeps its review progress (reviewed marks, quiz record and the
// spaced-review schedule, including question-bank misses) under one key, synced in
// its own cloud document, syncs/{PIN}_atlas.
const ATLAS_KEY = 'mla-progress';
const ATLAS_DOC = 'atlas';
const LS_PIN = 'qbank_sync_pin';
const LS_LAST_SYNC = 'qbank_sync_last';
const MAX_ATTEMPTS_STORED = 5000;
const MAX_SCORE_HISTORY = 20; // same cap as recordScore() in shared/app.js
// Firestore rejects a document over 1,048,576 bytes. Stay below it with room
// for the document name and per-field overhead it also counts.
const DOC_BYTE_BUDGET = 1000000;

function allSyncKeys() {
  const keys = [];
  BLOCK_KEYS.forEach(b => SUFFIXES.forEach(s => keys.push(`${b}_${s}`)));
  keys.push(ATLAS_KEY);
  return keys;
}

function readLocalBlob() {
  const blob = {};
  allSyncKeys().forEach(k => {
    const v = localStorage.getItem(k);
    if (v !== null) blob[k] = v;
  });
  return blob;
}

function safeParse(str, fallback) {
  if (str == null) return fallback;
  try { return JSON.parse(str); } catch (e) { return fallback; }
}

// ---- Per-field-type merge logic ----
function mergeFlags(a, b) {
  return Object.assign({}, a || {}, b || {});
}

// A score's `history` is its run list behind Analytics' Score Trend chart.
// Both sides' runs are kept, oldest first, so a sync never shortens it.
function mergeScoreHistory(a, b) {
  const seen = new Set();
  return (a || []).concat(b || [])
    .filter(r => {
      if (!r) return false;
      const k = `${r.date}|${r.correct}|${r.total}`;
      if (seen.has(k)) return false;
      seen.add(k);
      return true;
    })
    .sort((x, y) => (Date.parse(x.date) || 0) - (Date.parse(y.date) || 0))
    .slice(-MAX_SCORE_HISTORY);
}

function mergeProgress(a, b) {
  const out = Object.assign({}, a || {});
  Object.keys(b || {}).forEach(key => {
    const rb = b[key];
    if (!out[key]) { out[key] = rb; return; }
    const ra = out[key];
    const merged = { last: ra.last, best: ra.best };
    if (rb.last && (!ra.last || new Date(rb.last.date) > new Date(ra.last.date))) {
      merged.last = rb.last;
    }
    const ratio = (s) => (s && s.total) ? s.correct / s.total : -1;
    if (ratio(rb.best) > ratio(ra.best)) merged.best = rb.best;
    const history = mergeScoreHistory(ra.history, rb.history);
    if (history.length) merged.history = history;
    out[key] = merged;
  });
  return out;
}

function mergeAttempts(a, b) {
  const combined = (a || []).concat(b || []);
  const seen = new Set();
  const deduped = [];
  combined.forEach(rec => {
    const k = `${rec.id}|${rec.ts}|${rec.mode}`;
    if (seen.has(k)) return;
    seen.add(k);
    deduped.push(rec);
  });
  deduped.sort((x, y) => (x.ts || 0) - (y.ts || 0));
  return deduped.slice(-MAX_ATTEMPTS_STORED);
}

function mergeSettings(a, b, preferRemote) {
  // Low-stakes toggle, not worth fancy merging — just prefer whichever side
  // the caller says is more authoritative for this direction of sync.
  return preferRemote ? Object.assign({}, a || {}, b || {}) : Object.assign({}, b || {}, a || {});
}

// Atlas progress. Reviewed marks: union, latest time. Answer counts: the larger
// count per card, so syncing again never inflates them. Review schedule: per card,
// the side whose last schedule change (`at`) is newer wins; with no timestamps on
// either side (progress saved before they existed), the card stays due on the
// sooner date.
function mergeAtlas(a, b) {
  a = a || {}; b = b || {};
  const part = (o, k) => (o[k] && typeof o[k] === 'object') ? o[k] : {};
  const out = { rev: {}, ok: {}, miss: {}, qok: {}, qmiss: {}, box: {}, due: {}, at: {}, known: {}, star: {}, nit: {}, prd: {}, nitm: {} };
  [a, b].forEach(src => Object.entries(part(src, 'rev')).forEach(([id, t]) => {
    out.rev[id] = Math.max(+out.rev[id] || 0, +t || 0) || t;
  }));
  // "I know this" and starred cards: marked = the time, unmarked = minus the time, so
  // the device that acted last wins either way
  ['known', 'star'].forEach(k => [a, b].forEach(src => Object.entries(part(src, k)).forEach(([id, t]) => {
    t = +t || 0;
    if (t && (!(id in out[k]) || Math.abs(t) > Math.abs(out[k][id]))) out[k][id] = t;
  })));
  ['ok', 'miss', 'qok', 'qmiss'].forEach(k => [a, b].forEach(src => Object.entries(part(src, k)).forEach(([id, n]) => {
    out[k][id] = Math.max(out[k][id] || 0, +n || 0);
  })));
  // moving maps: Name-it and Predict scores per map ([right, asked], the larger of each), and the Name-it options
  // missed and not yet put right (the larger count; one named right on either device clears it there, and the
  // other device's copy comes back until it is answered there too)
  ['nit', 'prd'].forEach(k => [a, b].forEach(src => Object.entries(part(src, k)).forEach(([v, r]) => {
    if (!Array.isArray(r)) return;
    const c = out[k][v] || [0, 0]; out[k][v] = [Math.max(c[0], +r[0] || 0), Math.max(c[1], +r[1] || 0)];
  })));
  [a, b].forEach(src => Object.entries(part(src, 'nitm')).forEach(([id, n]) => { out.nitm[id] = Math.max(out.nitm[id] || 0, +n || 0); }));
  const ids = new Set([a, b].flatMap(src => Object.keys(part(src, 'box')).concat(Object.keys(part(src, 'at')))));
  ids.forEach(id => {
    const ta = +part(a, 'at')[id] || 0, tb = +part(b, 'at')[id] || 0;
    const inA = id in part(a, 'box'), inB = id in part(b, 'box');
    if (ta !== tb) {
      const w = ta > tb ? a : b;
      if (id in part(w, 'box')) { out.box[id] = part(w, 'box')[id]; out.due[id] = part(w, 'due')[id] || 0; }
    } else if (inA && inB) {
      out.box[id] = Math.min(part(a, 'box')[id], part(b, 'box')[id]);
      out.due[id] = Math.min(part(a, 'due')[id] || 0, part(b, 'due')[id] || 0);
    } else if (inA || inB) {
      const w = inA ? a : b;
      out.box[id] = part(w, 'box')[id]; out.due[id] = part(w, 'due')[id] || 0;
    }
    const t = Math.max(ta, tb);
    if (t) out.at[id] = t;
  });
  return out;
}

// Merge two full blobs (each a map of localStorage-key -> raw JSON string).
function mergeBlobs(localBlob, remoteBlob) {
  const out = {};
  BLOCK_KEYS.forEach(block => {
    const fKey = `${block}_flags_v1`, pKey = `${block}_progress_v1`, aKey = `${block}_attempts_v1`, sKey = `${block}_settings_v1`;
    const lf = safeParse(localBlob[fKey], {}), rf = safeParse(remoteBlob[fKey], {});
    const lp = safeParse(localBlob[pKey], {}), rp = safeParse(remoteBlob[pKey], {});
    const la = safeParse(localBlob[aKey], []), ra = safeParse(remoteBlob[aKey], []);
    const ls = safeParse(localBlob[sKey], {}), rs = safeParse(remoteBlob[sKey], {});

    out[fKey] = JSON.stringify(mergeFlags(lf, rf));
    out[pKey] = JSON.stringify(mergeProgress(lp, rp));
    out[aKey] = JSON.stringify(mergeAttempts(la, ra));
    out[sKey] = JSON.stringify(mergeSettings(ls, rs, true));
  });
  const lAtlas = safeParse(localBlob[ATLAS_KEY], null), rAtlas = safeParse(remoteBlob[ATLAS_KEY], null);
  if (lAtlas || rAtlas) out[ATLAS_KEY] = JSON.stringify(mergeAtlas(lAtlas, rAtlas));
  return out;
}

function writeBlobToLocal(blob) {
  Object.keys(blob).forEach(k => localStorage.setItem(k, blob[k]));
}

// ---- Cloud copy of one block ----
function blockDocId(pin, block) {
  return `${pin}_${block}`;
}

function isEmptyBlock(blob, block) {
  return SUFFIXES.every(s => {
    const v = safeParse(blob[`${block}_${s}`], null);
    return v == null || (Array.isArray(v) ? v.length === 0 : Object.keys(v).length === 0);
  });
}

function utf8Bytes(str) {
  return new TextEncoder().encode(str).length;
}

// One block's keys from a merged blob, as they are stored in the cloud: each
// answer without its SDL title and objective text, and if the document would
// still be too big, without its oldest answers (they stay on the devices that
// logged them). Returns null when the block has nothing to store.
function cloudBlockBlob(blob, block) {
  if (isEmptyBlock(blob, block)) return null;
  const out = {};
  SUFFIXES.forEach(s => {
    const k = `${block}_${s}`;
    if (blob[k] !== undefined) out[k] = blob[k];
  });
  const aKey = `${block}_attempts_v1`;
  let attempts = safeParse(out[aKey], []).map(a => {
    const { sdlTitle, objectiveLabel, ...rest } = a;
    return rest;
  });
  out[aKey] = JSON.stringify(attempts);
  const size = () => Object.keys(out).reduce((n, k) => n + utf8Bytes(k) + 1 + utf8Bytes(out[k]) + 1, 0);
  while (size() > DOC_BYTE_BUDGET && attempts.length) {
    attempts = attempts.slice(Math.max(1, Math.ceil(attempts.length / 10)));
    out[aKey] = JSON.stringify(attempts);
  }
  if (size() > DOC_BYTE_BUDGET) throw new Error(`${block} progress is too large to sync`);
  return out;
}

// ---- Firestore REST helpers ----
function docUrl(docId) {
  return `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/syncs/${encodeURIComponent(docId)}?key=${FIREBASE_CONFIG.apiKey}`;
}

function toFirestoreFields(blob) {
  const fields = {};
  Object.keys(blob).forEach(k => { fields[k] = { stringValue: blob[k] }; });
  fields['_updatedAt'] = { timestampValue: new Date().toISOString() };
  return { fields };
}

function fromFirestoreFields(doc) {
  const blob = {};
  const fields = (doc && doc.fields) || {};
  Object.keys(fields).forEach(k => {
    if (k === '_updatedAt') return;
    if (fields[k].stringValue !== undefined) blob[k] = fields[k].stringValue;
  });
  return blob;
}

async function fetchDoc(docId) {
  const res = await fetch(docUrl(docId));
  if (res.status === 404) return null; // nothing stored there yet
  if (!res.ok) throw new Error(`Cloud fetch failed (HTTP ${res.status})`);
  return res.json();
}

async function patchDoc(docId, body) {
  const res = await fetch(docUrl(docId), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`Cloud write failed (HTTP ${res.status}) ${text}`);
  }
}

// Everything stored for a PIN: every block's document, merged over the old
// single document. `hasLegacyData` says whether the old document still holds
// progress, so a push knows to empty it.
async function fetchRemoteBlob(pin) {
  const [legacyDoc, ...blockDocs] = await Promise.all(
    [fetchDoc(pin)].concat(BLOCK_KEYS.concat([ATLAS_DOC]).map(b => fetchDoc(blockDocId(pin, b)))));
  const legacy = fromFirestoreFields(legacyDoc);
  const current = Object.assign({}, ...blockDocs.map(fromFirestoreFields));
  return { blob: mergeBlobs(legacy, current), hasLegacyData: Object.keys(legacy).length > 0 };
}

async function writeRemoteBlob(pin, blob, clearLegacy) {
  const atlas = blob[ATLAS_KEY];
  await Promise.all(BLOCK_KEYS.map(block => {
    const data = cloudBlockBlob(blob, block);
    return data ? patchDoc(blockDocId(pin, block), toFirestoreFields(data)) : null;
  }).concat(atlas && atlas.length > 2 ? [patchDoc(blockDocId(pin, ATLAS_DOC), toFirestoreFields({ [ATLAS_KEY]: atlas }))] : []));
  // Only after every block is safely stored: the old document now holds
  // nothing they don't, so empty it to stay out of the way.
  if (clearLegacy) {
    await patchDoc(pin, { fields: { _migratedAt: { timestampValue: new Date().toISOString() } } });
  }
}

// ---- Public actions ----
async function pushToCloud(pin) {
  const local = readLocalBlob();
  const remote = await fetchRemoteBlob(pin);
  const merged = mergeBlobs(local, remote.blob);
  await writeRemoteBlob(pin, merged, remote.hasLegacyData);
  return merged;
}

async function pullFromCloud(pin) {
  const remote = await fetchRemoteBlob(pin);
  const local = readLocalBlob();
  const merged = mergeBlobs(local, remote.blob);
  writeBlobToLocal(merged);
  return merged;
}

// ---- UI wiring ----
function generatePin() {
  const alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; // no 0/O/1/I to avoid confusion
  let pin = '';
  for (let i = 0; i < 6; i++) pin += alphabet[Math.floor(Math.random() * alphabet.length)];
  return pin;
}

function getSavedPin() {
  return localStorage.getItem(LS_PIN) || '';
}
function savePin(pin) {
  localStorage.setItem(LS_PIN, pin);
}
function recordLastSync() {
  localStorage.setItem(LS_LAST_SYNC, new Date().toISOString());
}
function getLastSync() {
  const v = localStorage.getItem(LS_LAST_SYNC);
  return v ? new Date(v).toLocaleString() : null;
}

function initSyncUI() {
  const root = document.getElementById('syncSection');
  if (!root) return;

  const configured = FIREBASE_CONFIG.projectId !== 'YOUR_PROJECT_ID' && FIREBASE_CONFIG.apiKey !== 'YOUR_API_KEY';

  function render(status) {
    const pin = getSavedPin();
    const lastSync = getLastSync();
    if (!configured) {
      root.innerHTML = `<p class="sync-hint">Cross-device sync isn't set up yet on this deployment.</p>`;
      return;
    }
    root.innerHTML = `
      <div class="sync-card">
        ${pin ? `
          <div class="sync-pin-display">Your sync PIN: <span class="sync-pin">${pin}</span></div>
          <p class="sync-hint">Enter this same PIN on your other device to link it. ${lastSync ? `Last synced: ${lastSync}.` : 'Not synced yet on this device.'}</p>
          <div class="sync-actions">
            <button class="sync-btn" id="pushBtn">⬆ Push to Cloud</button>
            <button class="sync-btn" id="pullBtn">⬇ Pull from Cloud</button>
            <button class="sync-btn secondary" id="forgetPinBtn">Use a different PIN</button>
          </div>
        ` : `
          <p class="sync-hint">Sync your progress (flags, scores, missed questions, and your Lesion Atlas reviews) across devices with a PIN — no account needed.</p>
          <div class="sync-actions">
            <button class="sync-btn" id="newPinBtn">Create a New PIN</button>
          </div>
          <div class="sync-enter-row">
            <input type="text" id="pinInput" class="sync-pin-input" maxlength="6" placeholder="Have a PIN? Enter it">
            <button class="sync-btn secondary" id="usePinBtn">Link Device</button>
          </div>
        `}
        <div class="sync-status" id="syncStatus">${status || ''}</div>
      </div>
    `;

    if (pin) {
      document.getElementById('pushBtn').addEventListener('click', () => doAction('push', pin));
      document.getElementById('pullBtn').addEventListener('click', () => doAction('pull', pin));
      document.getElementById('forgetPinBtn').addEventListener('click', () => {
        localStorage.removeItem(LS_PIN);
        render('');
      });
    } else {
      document.getElementById('newPinBtn').addEventListener('click', () => {
        const newPin = generatePin();
        savePin(newPin);
        doAction('push', newPin);
      });
      document.getElementById('usePinBtn').addEventListener('click', () => {
        const val = document.getElementById('pinInput').value.trim().toUpperCase();
        if (!val) return;
        savePin(val);
        doAction('pull', val);
      });
    }
  }

  async function doAction(kind, pin) {
    const statusEl = () => document.getElementById('syncStatus');
    if (statusEl()) statusEl().textContent = kind === 'push' ? 'Pushing…' : 'Pulling…';
    try {
      if (kind === 'push') await pushToCloud(pin);
      else await pullFromCloud(pin);
      recordLastSync();
      render(kind === 'push' ? '✅ Synced to cloud.' : '✅ Synced from cloud.');
    } catch (err) {
      render(`❌ Sync failed: ${err.message}`);
    }
  }

  render('');
}

// Exposed on window: used by index.html's inline boot script, and handy for testing/debugging.
window.pushToCloud = pushToCloud;
window.pullFromCloud = pullFromCloud;
window.__syncInternals = { mergeFlags, mergeProgress, mergeScoreHistory, mergeAttempts, mergeAtlas, mergeBlobs, readLocalBlob, cloudBlockBlob, fetchRemoteBlob, writeRemoteBlob };

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSyncUI);
} else {
  initSyncUI();
}
