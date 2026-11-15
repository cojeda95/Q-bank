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
 * Who can read a PIN is decided by firestore.rules: the collection cannot be
 * listed, and a document is readable only by its exact id.
 *
 * Push and Pull are both NON-DESTRUCTIVE: each one computes a union merge of
 * local + remote data first, so neither action can silently lose progress.
 * Push writes the merged result to the cloud. Pull writes the merged result
 * to this device. Running either one repeatedly is safe/idempotent.
 *
 * With a PIN saved, auto-sync (on unless this device turns it off) pulls on
 * load and when the tab is focused again, and pushes a few seconds after
 * progress, an answer, or a setting changes. The manual buttons stay. A push
 * that the rules reject, or whose precondition fails after the usual retries,
 * does not keep trying on its own.
 */

// ---- Fill these in from your Firebase project (see setup instructions) ----
const FIREBASE_CONFIG = {
  projectId: 'q-bank-cache',
  apiKey: 'AIzaSyAvYYQ5gAjcRN4W52ulCZ5nuA9BsuvNqN4',
};
// ----------------------------------------------------------------------

const BLOCK_KEYS = ['neuro', 'pulm', 'eent', 'endocrine', 'ortho', 'rheum', 'psych', 'nephro', 'gastro', 'omm', 'geriatrics', 'research'];
const SUFFIXES = ['flags_v1', 'progress_v1', 'attempts_v1', 'settings_v1'];
// The Lesion Atlas keeps its review progress (reviewed marks, quiz record and the
// spaced-review schedule, including question-bank misses) under one key, synced in
// its own cloud document, syncs/{PIN}_atlas.
const ATLAS_KEY = 'mla-progress';
const ATLAS_DOC = 'atlas';
const LS_PIN = 'qbank_sync_pin';
const LS_LAST_SYNC = 'qbank_sync_last';
// Missing key means on. '0' is the off switch for this device.
const LS_AUTO = 'qbank_sync_auto';
// Hash of the local blob last known to match a successful sync. A match skips the push.
const LS_HASH = 'qbank_sync_hash';
const AUTO_PUSH_MS = 4000;
const AUTO_PULL_MS = 30000;
const AUTO_BACKOFF_CAP = 60000;
// Same cap as shared/app.js MAX_ATTEMPTS_STORED. That name stays in app.js: both
// scripts load on a block page, and a top-level const cannot be declared twice.
const SYNC_MAX_ATTEMPTS = 5000;
const MAX_SCORE_HISTORY = 20; // same cap as recordScore() in shared/app.js
// Firestore rejects a document over 1,048,576 bytes. Stay below it with room
// for the document name and per-field overhead it also counts.
const DOC_BYTE_BUDGET = 1000000;

// True while a pull is writing the merged blob, so that write is not itself a new edit.
let applyingRemote = false;
let legacyChecked = false;
let legacyHasData = false;
const dirtyBlocks = new Set();
// '403' or 'conflict': stop automatic retries. A new edit clears a conflict hold
// (the payload changed). A 403 hold stays until a manual push/pull, toggling
// auto-sync back on, or a new page load — the same write would just be denied again.
let holdAuto = null;
let netFails = 0;
let lastPullAt = 0;
let pushTimer = null;
let syncTail = Promise.resolve();
let syncState = 'off';
const syncCounts = { gets: 0, writes: 0 };
let lifecycleBound = false;
let storageHooked = false;

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
  const seen = new Map();
  const deduped = [];
  combined.forEach(rec => {
    const k = `${rec.id}|${rec.ts}|${rec.mode}`;
    const prev = seen.get(k);
    if (prev) {
      // the same answer from both sides: keep a "why did you miss it" tag from either
      if (!prev.why && rec.why) prev.why = rec.why;
      return;
    }
    const copy = Object.assign({}, rec);
    seen.set(k, copy);
    deduped.push(copy);
  });
  deduped.sort((x, y) => (x.ts || 0) - (y.ts || 0));
  return deduped.slice(-SYNC_MAX_ATTEMPTS);
}

function mergeSettings(a, b) {
  // Toggles are saved together. The side with the newer updatedAt wins as a
  // whole, so pushing from the device that just changed a setting doesn't
  // put the stale cloud copy back. Settings saved before that stamp existed
  // tie, and the remote copy still fills in over the local one.
  if (!a || typeof a !== 'object' || Array.isArray(a)) a = {};
  if (!b || typeof b !== 'object' || Array.isArray(b)) b = {};
  const stamp = (s) => {
    const t = s.updatedAt;
    if (typeof t === 'number' && isFinite(t)) return t;
    const n = Date.parse(t);
    return isFinite(n) ? n : 0;
  };
  const ta = stamp(a), tb = stamp(b);
  if (ta > tb) return Object.assign({}, a);
  if (tb > ta) return Object.assign({}, b);
  return Object.assign({}, a, b);
}

// Atlas progress. Reviewed marks: union, latest time. Answer counts: the larger
// count per card, so syncing again never inflates them. Review schedule: per card,
// the side whose last schedule change (`at`) is newer wins; with no timestamps on
// either side (progress saved before they existed), the card stays due on the
// sooner date.
function mergeAtlas(a, b) {
  a = a || {}; b = b || {};
  const part = (o, k) => (o[k] && typeof o[k] === 'object') ? o[k] : {};
  const out = { rev: {}, ok: {}, miss: {}, qok: {}, qmiss: {}, box: {}, due: {}, at: {}, known: {}, star: {}, nit: {}, prd: {}, nitm: {}, cas: {}, note: {} };
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
  // moving maps: Name-it, Predict and Case scores per map ([right, asked], the larger of each), and the Name-it options
  // missed and not yet put right (the larger count; one named right on either device clears it there, and the
  // other device's copy comes back until it is answered there too)
  ['nit', 'prd', 'cas'].forEach(k => [a, b].forEach(src => Object.entries(part(src, k)).forEach(([v, r]) => {
    if (!Array.isArray(r)) return;
    const c = out[k][v] || [0, 0]; out[k][v] = [Math.max(c[0], +r[0] || 0), Math.max(c[1], +r[1] || 0)];
  })));
  [a, b].forEach(src => Object.entries(part(src, 'nitm')).forEach(([id, n]) => { out.nitm[id] = Math.max(out.nitm[id] || 0, +n || 0); }));
  // personal notes on cards ({t: last edit, text}; an emptied note keeps its time, so the deletion syncs too):
  // the newest edit wins, card by card. The atlas also keeps a copy in mla-notes on each device.
  [a, b].forEach(src => Object.entries(part(src, 'note')).forEach(([id, n]) => {
    if (!n || typeof n !== 'object' || typeof n.text !== 'string') return;
    const t = +n.t || 0;
    if (!(id in out.note) || t > out.note[id].t) out.note[id] = { t, text: n.text.slice(0, 1000) };
  }));
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
function mergeBlobs(localBlob, remoteBlob, blocks) {
  const out = {};
  (blocks || BLOCK_KEYS).forEach(block => {
    const fKey = `${block}_flags_v1`, pKey = `${block}_progress_v1`, aKey = `${block}_attempts_v1`, sKey = `${block}_settings_v1`;
    const lf = safeParse(localBlob[fKey], {}), rf = safeParse(remoteBlob[fKey], {});
    const lp = safeParse(localBlob[pKey], {}), rp = safeParse(remoteBlob[pKey], {});
    const la = safeParse(localBlob[aKey], []), ra = safeParse(remoteBlob[aKey], []);
    const ls = safeParse(localBlob[sKey], {}), rs = safeParse(remoteBlob[sKey], {});

    out[fKey] = JSON.stringify(mergeFlags(lf, rf));
    out[pKey] = JSON.stringify(mergeProgress(lp, rp));
    out[aKey] = JSON.stringify(mergeAttempts(la, ra));
    out[sKey] = JSON.stringify(mergeSettings(ls, rs));
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
// Same opt-in as live.js. Production hostnames never use the emulator.
// http://localhost:<port>/index.html?emulator=1 with the Firestore emulator on port 8080.
function useFirestoreEmulator() {
  try {
    const host = location.hostname;
    const local = host === 'localhost' || host === '127.0.0.1' || host === '::1';
    if (!local) return false;
    if (new URLSearchParams(location.search).get('emulator') === '1') {
      localStorage.setItem('qbank_firestore_emulator', '1');
      return true;
    }
    return localStorage.getItem('qbank_firestore_emulator') === '1';
  } catch (e) {
    return false;
  }
}
function docUrl(docId) {
  const origin = useFirestoreEmulator()
    ? `http://${location.hostname === '::1' ? '127.0.0.1' : location.hostname}:8080`
    : 'https://firestore.googleapis.com';
  return `${origin}/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/syncs/${encodeURIComponent(docId)}?key=${FIREBASE_CONFIG.apiKey}`;
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

function httpError(message, status) {
  const err = new Error(message);
  err.status = status;
  return err;
}

// keepalive lets a flush started as the page hides finish after it unloads.
// Chrome caps a keepalive body around 64KB; a larger write goes out as a normal fetch.
function fetchOpts(opts, extra) {
  const o = Object.assign({}, extra || {});
  if (opts && opts.keepalive) {
    const body = o.body || '';
    if (!body || utf8Bytes(body) < 60000) o.keepalive = true;
  }
  return o;
}

async function fetchDoc(docId, opts) {
  syncCounts.gets += 1;
  let res;
  try {
    res = await fetch(docUrl(docId), fetchOpts(opts, { cache: 'no-store' }));
  } catch (err) {
    // A browser that rejects keepalive still has a hidden-but-alive page on visibilitychange.
    if (!(opts && opts.keepalive)) throw err;
    syncCounts.gets += 1;
    res = await fetch(docUrl(docId), { cache: 'no-store' });
  }
  if (res.status === 404) return null; // nothing stored there yet
  if (!res.ok) throw httpError(`Cloud fetch failed (HTTP ${res.status})`, res.status);
  return res.json();
}

function conflictError(status) {
  const err = new Error(`Cloud write conflict (HTTP ${status})`);
  err.conflict = true;
  err.status = status;
  return err;
}

// updateTime is the document's updateTime from the last read. The write is a
// commit with that precondition so a concurrent push fails instead of
// overwriting that device's attempts. A missing time means we observed no
// document, so the write may only create one. The precondition is in the
// commit body: a timestamp query parameter on PATCH is not applied by the
// emulator (it becomes "version 0" and every update fails).
async function patchDoc(docId, body, updateTime, opts) {
  const origin = useFirestoreEmulator()
    ? `http://${location.hostname === '::1' ? '127.0.0.1' : location.hostname}:8080`
    : 'https://firestore.googleapis.com';
  const url = `${origin}/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents:commit?key=${FIREBASE_CONFIG.apiKey}`;
  const write = {
    update: {
      name: `projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/syncs/${docId}`,
      fields: body.fields,
    },
    currentDocument: updateTime ? { updateTime } : { exists: false },
  };
  const payload = JSON.stringify({ writes: [write] });
  syncCounts.writes += 1;
  let res;
  try {
    res = await fetch(url, fetchOpts(opts, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: payload,
    }));
  } catch (err) {
    if (!(opts && opts.keepalive)) throw err;
    syncCounts.writes += 1;
    res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: payload,
    });
  }
  if (res.ok) return;
  const text = await res.text().catch(() => '');
  if (res.status === 409 || res.status === 412 || /ABORTED|FAILED_PRECONDITION|ALREADY_EXISTS/.test(text)) throw conflictError(res.status);
  throw httpError(`Cloud write failed (HTTP ${res.status}) ${text}`, res.status);
}

// Everything stored for a PIN: every block's document, merged over the old
// single document. `hasLegacyData` says whether the old document still holds
// progress, so a push knows to empty it.
async function fetchRemoteBlob(pin, opts) {
  const ids = [pin].concat(BLOCK_KEYS.concat([ATLAS_DOC]).map(b => blockDocId(pin, b)));
  const docs = await Promise.all(ids.map(id => fetchDoc(id, opts)));
  const versions = {};
  ids.forEach((id, i) => { versions[id] = (docs[i] && docs[i].updateTime) || null; });
  const legacy = fromFirestoreFields(docs[0]);
  const current = Object.assign({}, ...docs.slice(1).map(fromFirestoreFields));
  return { blob: mergeBlobs(legacy, current), hasLegacyData: Object.keys(legacy).length > 0, versions };
}

async function writeRemoteBlob(pin, blob, clearLegacy, versions, opts) {
  versions = versions || {};
  const atlas = blob[ATLAS_KEY];
  const writes = BLOCK_KEYS.map(block => {
    const data = cloudBlockBlob(blob, block);
    if (!data) return null;
    const id = blockDocId(pin, block);
    return patchDoc(id, toFirestoreFields(data), versions[id], opts);
  });
  if (atlas && atlas.length > 2) {
    const id = blockDocId(pin, ATLAS_DOC);
    writes.push(patchDoc(id, toFirestoreFields({ [ATLAS_KEY]: atlas }), versions[id], opts));
  }
  await Promise.all(writes);
  // Only after every block is safely stored: the old document now holds
  // nothing they don't, so empty it to stay out of the way.
  if (clearLegacy) {
    await patchDoc(pin, { fields: { _migratedAt: { timestampValue: new Date().toISOString() } } }, versions[pin], opts);
  }
}

// ---- Public actions ----
const PUSH_ATTEMPTS = 4;
async function pushToCloud(pin, opts) {
  let lastErr;
  for (let attempt = 0; attempt < PUSH_ATTEMPTS; attempt++) {
    const local = readLocalBlob();
    const remote = await fetchRemoteBlob(pin, opts);
    const merged = mergeBlobs(local, remote.blob);
    try {
      await writeRemoteBlob(pin, merged, remote.hasLegacyData, remote.versions, opts);
      legacyChecked = true;
      legacyHasData = false;
      return merged;
    } catch (err) {
      lastErr = err;
      if (!err.conflict || attempt === PUSH_ATTEMPTS - 1) throw err;
    }
  }
  throw lastErr;
}

// Read remote, union it with whatever is local NOW (after the fetch, so an
// answer logged while the request was in flight is included), and store that.
async function pullMerged(pin, opts) {
  const remote = await fetchRemoteBlob(pin, opts);
  legacyChecked = true;
  legacyHasData = !!remote.hasLegacyData;
  const local = readLocalBlob();
  const merged = mergeBlobs(local, remote.blob);
  applyingRemote = true;
  try { writeBlobToLocal(merged); }
  finally { applyingRemote = false; }
  const stored = readLocalBlob();
  const need = legacyHasData ? nonEmptyBlocks(stored) : blocksNeedingPush(stored, remote.blob);
  return { merged, remote, need };
}

async function pullFromCloud(pin) {
  const { merged } = await pullMerged(pin);
  return merged;
}

// ---- UI wiring ----
function generatePin() {
  const alphabet = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; // no 0/O/1/I to avoid confusion
  const buf = new Uint32Array(1);
  const limit = 0x100000000 - (0x100000000 % alphabet.length);
  let pin = '';
  for (let i = 0; i < 6; i++) {
    let n;
    do { crypto.getRandomValues(buf); n = buf[0]; } while (n >= limit);
    pin += alphabet[n % alphabet.length];
  }
  return pin;
}

function getSavedPin() {
  return localStorage.getItem(LS_PIN) || '';
}
function savePin(pin) {
  const prev = localStorage.getItem(LS_PIN) || '';
  if (prev !== pin) {
    try { localStorage.removeItem(LS_HASH); } catch (e) {}
    dirtyBlocks.clear();
    holdAuto = null;
    legacyChecked = false;
    legacyHasData = false;
  }
  localStorage.setItem(LS_PIN, pin);
}
function recordLastSync() {
  localStorage.setItem(LS_LAST_SYNC, new Date().toISOString());
}
function getLastSync() {
  const v = localStorage.getItem(LS_LAST_SYNC);
  return v ? new Date(v).toLocaleString() : null;
}

/* ── Backup file (no PIN needed) ─────────────────────────────────────────
   Progress lives in this browser's local storage whether or not a PIN is used. "Download my progress" saves every
   block's flags, scores, attempts and settings, plus the Lesion Atlas progress and hub preferences, as one JSON file;
   "Restore" MERGES a file into this browser with the same rules as PIN sync, so an older file never erases newer work. */
const BACKUP_FORMAT = 'ocom-qhub-backup-v1';
const BLOCK_KEY_RE = /^([a-z0-9]+)_(flags|progress|attempts|settings)_v1$/;
function backupKeys() {
  const out = [];
  for (let i = 0; i < localStorage.length; i++) {
    const k = localStorage.key(i);
    if (BLOCK_KEY_RE.test(k) || k === ATLAS_KEY || /^(mla-|qhub-)/.test(k)) out.push(k);
  }
  return out.sort();
}
function downloadBackup() {
  const data = {};
  backupKeys().forEach(k => { data[k] = localStorage.getItem(k); });
  const blob = new Blob([JSON.stringify({ format: BACKUP_FORMAT, saved: new Date().toISOString(), data })], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `ocom-qhub-progress-${new Date().toISOString().slice(0, 10)}.json`;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 2000);
}
function restoreBackup(text) {
  const file = JSON.parse(text);
  if (!file || file.format !== BACKUP_FORMAT || typeof file.data !== 'object') throw new Error('not a Question Hub progress file');
  const incoming = {}, other = {};
  Object.keys(file.data).forEach(k => {
    const v = file.data[k];
    if (typeof v !== 'string') return;
    if (BLOCK_KEY_RE.test(k) || k === ATLAS_KEY) incoming[k] = v; else if (/^(mla-|qhub-)/.test(k)) other[k] = v;
  });
  const blocks = [...new Set(Object.keys(incoming).map(k => (k.match(BLOCK_KEY_RE) || [])[1]).filter(Boolean))];
  const local = {};
  Object.keys(incoming).forEach(k => { const v = localStorage.getItem(k); if (v !== null) local[k] = v; });
  if (localStorage.getItem(ATLAS_KEY) !== null) local[ATLAS_KEY] = localStorage.getItem(ATLAS_KEY);
  const merged = mergeBlobs(local, incoming, blocks);
  Object.keys(merged).forEach(k => { if (k in incoming || k in local) localStorage.setItem(k, merged[k]); });
  Object.keys(other).forEach(k => { if (localStorage.getItem(k) === null) localStorage.setItem(k, other[k]); });   // never overwrite this browser's own preferences
  let answers = 0;
  blocks.forEach(b => { try { answers += (JSON.parse(localStorage.getItem(`${b}_attempts_v1`)) || []).length; } catch (e) {} });
  return { blocks: blocks.length, answers };
}
function backupCardHtml() {
  return `
      <div class="sync-card" style="margin-top:12px">
        <p class="sync-hint"><b>No PIN? Back up with a file.</b> Your progress is saved in this browser. Clearing browsing data, a private window, or (on iPhone) not visiting for about a week can erase it — download a copy now and then, and restore it here on any device.</p>
        <div class="sync-actions">
          <button class="sync-btn" id="backupBtn">⬇ Download my progress</button>
          <button class="sync-btn secondary" id="restoreBtn">⬆ Restore from a file</button>
          <input type="file" id="restoreFile" accept="application/json,.json" hidden>
        </div>
        <div class="sync-status" id="backupStatus"></div>
      </div>`;
}
function bindBackupCard() {
  const st = () => document.getElementById('backupStatus');
  const b = document.getElementById('backupBtn'), r = document.getElementById('restoreBtn'), f = document.getElementById('restoreFile');
  if (!b) return;
  b.addEventListener('click', () => { try { downloadBackup(); st().textContent = '✅ Saved — keep the file somewhere safe (Files, Drive, email to yourself).'; } catch (e) { st().textContent = `❌ ${e.message}`; } });
  r.addEventListener('click', () => f.click());
  f.addEventListener('change', () => {
    const file = f.files && f.files[0]; if (!file) return;
    file.text().then(t => {
      const res = restoreBackup(t);
      st().textContent = `✅ Restored and merged: ${res.blocks} block${res.blocks === 1 ? '' : 's'}, ${res.answers.toLocaleString()} answers on this device now. Reload any open block to see it.`;
    }).catch(e => { st().textContent = `❌ Couldn't restore: ${e.message}`; }).finally(() => { f.value = ''; });
  });
}
/* Ask the browser to keep this site's storage (so it isn't cleared automatically under storage pressure). */
function requestPersistentStorage() {
  try { if (navigator.storage && navigator.storage.persist) navigator.storage.persisted().then(p => { if (!p) navigator.storage.persist(); }); } catch (e) {}
}
requestPersistentStorage();

// ---- Automatic sync -------------------------------------------------------
// One pull or push at a time. Calls from a timer or a button queue behind it;
// nothing here calls runExclusive while it already holds the queue.
function runExclusive(fn) {
  const run = syncTail.then(() => fn(), () => fn());
  syncTail = run.then(() => {}, () => {});
  return run;
}

function firebaseConfigured() {
  return FIREBASE_CONFIG.projectId !== 'YOUR_PROJECT_ID' && FIREBASE_CONFIG.apiKey !== 'YOUR_API_KEY';
}
function autoSyncEnabled() {
  try { return localStorage.getItem(LS_AUTO) !== '0'; }
  catch (e) { return true; }
}
function canAuto() {
  return firebaseConfigured() && !!getSavedPin() && autoSyncEnabled();
}
function blockOfKey(key) {
  if (key === ATLAS_KEY) return ATLAS_DOC;
  const m = /^([a-z0-9]+)_(?:flags|progress|attempts|settings)_v1$/.exec(key);
  return m && BLOCK_KEYS.indexOf(m[1]) !== -1 ? m[1] : null;
}
function hashBlob(blob) {
  const keys = Object.keys(blob).sort();
  let h1 = 0x811c9dc5;
  let h2 = 0x811c9dc5 ^ 0x01000193;
  const feed = (s) => {
    for (let i = 0; i < s.length; i++) {
      const c = s.charCodeAt(i);
      h1 = Math.imul(h1 ^ c, 0x01000193);
      h2 = Math.imul(h2 ^ (c + 1), 0x01000193);
    }
  };
  keys.forEach(k => { feed(k); feed('\0'); feed(String(blob[k])); feed('\0'); });
  return (h1 >>> 0).toString(16).padStart(8, '0') + (h2 >>> 0).toString(16).padStart(8, '0');
}
function canon(v) {
  if (Array.isArray(v)) return '[' + v.map(canon).join(',') + ']';
  if (v && typeof v === 'object') {
    return '{' + Object.keys(v).sort().map(k => JSON.stringify(k) + ':' + canon(v[k])).join(',') + '}';
  }
  return JSON.stringify(v);
}
function canonField(key, str) {
  if (key.endsWith('_attempts_v1')) {
    const arr = safeParse(str, []);
    const stripped = (Array.isArray(arr) ? arr : []).map(a => {
      if (!a || typeof a !== 'object' || Array.isArray(a)) return a;
      const { sdlTitle, objectiveLabel, ...rest } = a;
      return rest;
    });
    return canon(stripped);
  }
  return canon(safeParse(str, null));
}
// Semantic cloud form of one block (or the atlas). Attempts are compared without
// the SDL title and objective text, which the cloud copy always drops.
function blockCloudCanon(blob, block) {
  if (block === ATLAS_DOC) {
    const raw = blob[ATLAS_KEY];
    if (!raw || raw.length <= 2) return '';
    return canon(safeParse(raw, null));
  }
  let data;
  try { data = cloudBlockBlob(blob, block); }
  catch (e) { return 'TOO_BIG'; }
  if (!data) return '';
  return SUFFIXES.map(s => {
    const k = `${block}_${s}`;
    return k in data ? canonField(k, data[k]) : '';
  }).join('\n');
}
function blocksNeedingPush(localBlob, remoteBlob) {
  const out = [];
  BLOCK_KEYS.forEach(block => {
    if (blockCloudCanon(localBlob, block) !== blockCloudCanon(remoteBlob, block)) out.push(block);
  });
  if (blockCloudCanon(localBlob, ATLAS_DOC) !== blockCloudCanon(remoteBlob, ATLAS_DOC)) out.push(ATLAS_DOC);
  return out;
}
function nonEmptyBlocks(blob) {
  const out = [];
  BLOCK_KEYS.forEach(b => { if (!isEmptyBlock(blob, b)) out.push(b); });
  if (blob[ATLAS_KEY] && blob[ATLAS_KEY].length > 2) out.push(ATLAS_DOC);
  return out;
}
function pickBlock(blob, block) {
  const out = {};
  SUFFIXES.forEach(s => {
    const k = `${block}_${s}`;
    if (blob[k] !== undefined) out[k] = blob[k];
  });
  return out;
}
function noteLocalChange(key) {
  if (applyingRemote) return;
  const block = blockOfKey(key);
  if (!block) return;
  dirtyBlocks.add(block);
  if (holdAuto === 'conflict') holdAuto = null;
  if (!canAuto() || holdAuto) return;
  if (!navigator.onLine) { setStatus('offline'); return; }
  schedulePush(AUTO_PUSH_MS);
}
function installStorageHook() {
  if (storageHooked) return;
  storageHooked = true;
  const nativeSet = Storage.prototype.setItem;
  const nativeRemove = Storage.prototype.removeItem;
  Storage.prototype.setItem = function (k, v) {
    nativeSet.call(this, k, v);
    if (this === localStorage) { try { noteLocalChange(k); } catch (e) {} }
  };
  Storage.prototype.removeItem = function (k) {
    nativeRemove.call(this, k);
    if (this === localStorage) { try { noteLocalChange(k); } catch (e) {} }
  };
}
function isNetworkError(err) {
  if (!navigator.onLine) return true;
  if (!err) return false;
  if (err.name === 'TypeError') return true;
  return !err.status && /fetch|network|offline/i.test(String(err.message || ''));
}
// 403 and a precondition miss (after pushToCloud / pushBlocks already retried)
// stop here. Network failures wait, then try again, and the online event resumes sooner.
function handleSyncError(err) {
  if (!navigator.onLine) { setStatus('offline'); return; }
  if (err && err.conflict) { holdAuto = 'conflict'; setStatus('error'); return; }
  if (err && (err.status === 403 || err.status === 401)) { holdAuto = '403'; setStatus('error'); return; }
  if (err && err.status >= 400 && err.status < 500 && err.status !== 408 && err.status !== 429) {
    holdAuto = '403';
    setStatus('error');
    return;
  }
  if (err && !isNetworkError(err)) { holdAuto = '403'; setStatus('error'); return; }
  netFails += 1;
  setStatus('error');
  if (!autoSyncEnabled()) return;
  const delay = Math.min(AUTO_BACKOFF_CAP, 2000 * Math.pow(2, netFails));
  clearTimeout(pushTimer);
  pushTimer = setTimeout(() => {
    pushTimer = null;
    if (!canAuto() || holdAuto) return;
    if (!navigator.onLine) { setStatus('offline'); return; }
    if (dirtyBlocks.size) runExclusive(() => runPush(false));
    else runExclusive(() => doPull());
  }, delay);
}
function schedulePush(delay) {
  if (!canAuto() || holdAuto) return;
  clearTimeout(pushTimer);
  if (!navigator.onLine) { setStatus('offline'); return; }
  setStatus('syncing');
  pushTimer = setTimeout(() => {
    pushTimer = null;
    runExclusive(() => runPush(false));
  }, delay == null ? AUTO_PUSH_MS : delay);
}
function flushSoon() {
  if (!canAuto() || holdAuto) return;
  const hash = hashBlob(readLocalBlob());
  if (!dirtyBlocks.size && hash === localStorage.getItem(LS_HASH)) return;
  if (!dirtyBlocks.size) nonEmptyBlocks(readLocalBlob()).forEach(b => dirtyBlocks.add(b));
  if (!dirtyBlocks.size) return;
  clearTimeout(pushTimer);
  pushTimer = null;
  if (!navigator.onLine) { setStatus('offline'); return; }
  runExclusive(() => runPush(true));
}
async function pushOneBlock(pin, block, opts) {
  const local = readLocalBlob();
  const id = blockDocId(pin, block);
  const doc = await fetchDoc(id, opts);
  const remoteBlob = fromFirestoreFields(doc);
  const updateTime = (doc && doc.updateTime) || null;
  if (block === ATLAS_DOC) {
    const merged = mergeBlobs({ [ATLAS_KEY]: local[ATLAS_KEY] }, { [ATLAS_KEY]: remoteBlob[ATLAS_KEY] }, []);
    if (blockCloudCanon(merged, ATLAS_DOC) === blockCloudCanon(remoteBlob, ATLAS_DOC)) return;
    const atlas = merged[ATLAS_KEY];
    if (!atlas || atlas.length <= 2) return;
    await patchDoc(id, toFirestoreFields({ [ATLAS_KEY]: atlas }), updateTime, opts);
    return;
  }
  const merged = mergeBlobs(pickBlock(local, block), remoteBlob, [block]);
  if (blockCloudCanon(merged, block) === blockCloudCanon(remoteBlob, block)) return;
  const data = cloudBlockBlob(merged, block);
  if (!data) return;
  await patchDoc(id, toFirestoreFields(data), updateTime, opts);
}
async function pushBlocks(pin, blocks, opts) {
  if (!legacyChecked) {
    const doc = await fetchDoc(pin, opts);
    legacyChecked = true;
    legacyHasData = Object.keys(fromFirestoreFields(doc)).length > 0;
  }
  // The old single document still holds progress: the full push folds it in and clears it.
  if (legacyHasData) {
    await pushToCloud(pin, opts);
    return;
  }
  let pending = blocks.slice();
  let lastErr;
  for (let attempt = 0; attempt < PUSH_ATTEMPTS && pending.length; attempt++) {
    const next = [];
    await Promise.all(pending.map(async block => {
      try {
        await pushOneBlock(pin, block, opts);
      } catch (err) {
        if (!err.conflict) throw err;
        next.push(block);
        lastErr = err;
      }
    }));
    pending = next;
  }
  if (pending.length) throw lastErr || conflictError(409);
}
async function runPush(keepalive) {
  if (!canAuto() || holdAuto) return;
  const pin = getSavedPin();
  if (!pin) return;
  if (!navigator.onLine) { setStatus('offline'); return; }
  const hashNow = hashBlob(readLocalBlob());
  if (!dirtyBlocks.size && hashNow === localStorage.getItem(LS_HASH)) {
    setStatus('synced');
    return;
  }
  if (!dirtyBlocks.size) nonEmptyBlocks(readLocalBlob()).forEach(b => dirtyBlocks.add(b));
  if (!dirtyBlocks.size) {
    try { localStorage.setItem(LS_HASH, hashNow); } catch (e) {}
    setStatus('synced');
    return;
  }
  setStatus('syncing');
  const blocks = [...dirtyBlocks];
  const hashAtStart = hashBlob(readLocalBlob());
  try {
    await pushBlocks(pin, blocks, { keepalive: !!keepalive });
    if (hashBlob(readLocalBlob()) === hashAtStart) {
      blocks.forEach(b => dirtyBlocks.delete(b));
      if (!dirtyBlocks.size) {
        try { localStorage.setItem(LS_HASH, hashAtStart); } catch (e) {}
      }
    }
    netFails = 0;
    recordLastSync();
    if (dirtyBlocks.size) schedulePush(AUTO_PUSH_MS);
    else setStatus('synced');
  } catch (err) {
    handleSyncError(err);
  }
}
async function doPull() {
  if (!canAuto() || holdAuto) return;
  const pin = getSavedPin();
  if (!pin) return;
  if (!navigator.onLine) { setStatus('offline'); return; }
  setStatus('syncing');
  try {
    const { need } = await pullMerged(pin);
    lastPullAt = Date.now();
    if (legacyHasData) need.forEach(b => dirtyBlocks.add(b));
    else {
      const keep = new Set(need);
      [...dirtyBlocks].forEach(b => { if (!keep.has(b)) dirtyBlocks.delete(b); });
      need.forEach(b => dirtyBlocks.add(b));
    }
    netFails = 0;
    recordLastSync();
    if (!dirtyBlocks.size) {
      try { localStorage.setItem(LS_HASH, hashBlob(readLocalBlob())); } catch (e) {}
      setStatus('synced');
    } else schedulePush(1000);
  } catch (err) {
    handleSyncError(err);
  }
}
function requestPull(force) {
  if (!canAuto() || holdAuto) return;
  if (!navigator.onLine) { setStatus('offline'); return; }
  const now = Date.now();
  if (!force && now - lastPullAt < AUTO_PULL_MS) return;
  lastPullAt = now;
  return runExclusive(() => doPull());
}
function bindLifecycle() {
  if (lifecycleBound) return;
  lifecycleBound = true;
  document.addEventListener('visibilitychange', () => {
    if (!canAuto()) return;
    if (document.visibilityState === 'hidden') flushSoon();
    else requestPull(false);
  });
  window.addEventListener('focus', () => requestPull(false));
  window.addEventListener('pageshow', () => requestPull(false));
  window.addEventListener('pagehide', () => flushSoon());
  window.addEventListener('online', () => {
    if (!canAuto() || holdAuto) return;
    netFails = 0;
    clearTimeout(pushTimer);
    pushTimer = null;
    if (dirtyBlocks.size) runExclusive(() => runPush(false));
    else runExclusive(() => doPull());
  });
  window.addEventListener('offline', () => {
    if (!getSavedPin() || !autoSyncEnabled()) return;
    clearTimeout(pushTimer);
    pushTimer = null;
    setStatus('offline');
  });
}
function bootAuto() {
  placeHeaderStatus();
  if (!firebaseConfigured() || !getSavedPin()) { setStatus('off'); return; }
  if (!autoSyncEnabled()) { setStatus('off'); return; }
  if (!navigator.onLine) {
    if (hashBlob(readLocalBlob()) !== localStorage.getItem(LS_HASH)) {
      nonEmptyBlocks(readLocalBlob()).forEach(b => dirtyBlocks.add(b));
    }
    setStatus('offline');
    return;
  }
  requestPull(true);
}
function forgetPin() {
  try { localStorage.removeItem(LS_PIN); } catch (e) {}
  try { localStorage.removeItem(LS_HASH); } catch (e) {}
  dirtyBlocks.clear();
  holdAuto = null;
  legacyChecked = false;
  legacyHasData = false;
  clearTimeout(pushTimer);
  pushTimer = null;
  setStatus('off');
}

const SYNC_LABELS = { synced: 'Synced', syncing: 'Syncing…', offline: 'Offline', error: 'Sync error' };
function injectSyncStyle() {
  if (document.getElementById('syncLiveStyle')) return;
  const style = document.createElement('style');
  style.id = 'syncLiveStyle';
  style.textContent = [
    '.sync-live{display:inline-flex;align-items:center;gap:6px;margin:0 0 8px;min-height:32px;padding:0;font-size:.8rem;font-weight:600;line-height:1.2;color:var(--grey-text,#5b5f58)}',
    '.sync-live[hidden]{display:none !important}',
    '.sync-live::before{content:"";width:7px;height:7px;border-radius:50%;background:currentColor;flex:none}',
    '.sync-live[data-state="synced"]{color:var(--green,#2e7d32)}',
    '.sync-live[data-state="syncing"]{color:var(--navy,#1f4e79)}',
    '.sync-live[data-state="offline"]{color:var(--amber-ink,#8a5a00)}',
    '.sync-live[data-state="error"]{color:var(--red,#c0392b)}',
    '.sync-auto{display:flex;align-items:center;gap:8px;margin:0 0 10px;min-height:44px;font-size:.9rem;cursor:pointer}',
    '.sync-auto input{width:20px;height:20px;margin:0;flex:none}',
    '.topbar-actions .sync-live,.ocom-topbar-inner>.sync-live,.topbar-inner>.sync-live{margin:0 0 0 2px}',
    '@media (max-width:640px){.sync-live{font-size:.75rem}}',
  ].join('\n');
  (document.head || document.documentElement).appendChild(style);
}
function applyStatusEl(el) {
  if (!el) return;
  const text = SYNC_LABELS[syncState] || '';
  const show = !!text && !!getSavedPin() && firebaseConfigured();
  if (el.textContent !== text) el.textContent = text;
  if ((el.dataset.state || '') !== (syncState || '')) el.dataset.state = syncState || '';
  el.hidden = !show;
}
function applyAllStatus() {
  document.querySelectorAll('[data-sync-live]').forEach(applyStatusEl);
}
function setStatus(state) {
  syncState = state;
  applyAllStatus();
  const lastEl = document.getElementById('syncLast');
  if (lastEl && state === 'synced') {
    const last = getLastSync();
    if (last) lastEl.textContent = `Last synced: ${last}.`;
  }
}
function placeHeaderStatus() {
  const host = document.querySelector('.topbar-actions')
    || document.querySelector('.ocom-topbar-inner')
    || document.querySelector('.topbar-inner');
  if (!host) return;
  let el = document.getElementById('syncLiveHeader');
  if (!el) {
    // span, not p: the theme button's group is itself a span, and a p would split it.
    el = document.createElement('span');
    el.id = 'syncLiveHeader';
    el.className = 'sync-live';
    el.setAttribute('data-sync-live', '');
    el.setAttribute('role', 'status');
    el.setAttribute('aria-live', 'polite');
  }
  if (el.parentNode !== host) host.appendChild(el);
  applyStatusEl(el);
}

function initSyncUI() {
  injectSyncStyle();
  installStorageHook();
  bindLifecycle();
  const root = document.getElementById('syncSection');
  const configured = firebaseConfigured();

  function render(status) {
    if (!root) return;
    const pin = getSavedPin();
    const lastSync = getLastSync();
    if (!configured) {
      root.innerHTML = `<p class="sync-hint">Cross-device sync isn't set up yet on this deployment.</p>${backupCardHtml()}`;
      bindBackupCard(render);
      placeHeaderStatus();
      return;
    }
    root.innerHTML = `
      <div class="sync-card">
        ${pin ? `
          <div class="sync-pin-display">Your sync PIN: <span class="sync-pin">${pin}</span></div>
          <p class="sync-live" id="syncLiveCard" data-sync-live role="status" aria-live="polite"></p>
          <p class="sync-hint">Enter this same PIN on your other device. Auto-sync pulls when you open the site or come back to it, and pushes a few seconds after you answer. <span id="syncLast">${lastSync ? `Last synced: ${lastSync}.` : 'Not synced yet on this device.'}</span></p>
          <label class="sync-auto"><input type="checkbox" id="autoSyncToggle"${autoSyncEnabled() ? ' checked' : ''}> Auto-sync</label>
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
            <label class="sr" for="pinInput">Sync PIN</label>
            <input type="text" id="pinInput" class="sync-pin-input" maxlength="6" placeholder="Have a PIN? Enter it">
            <button class="sync-btn secondary" id="usePinBtn">Link Device</button>
          </div>
        `}
        <div class="sync-status" id="syncStatus">${status || ''}</div>
      </div>
      ${backupCardHtml()}
    `;
    bindBackupCard(render);
    placeHeaderStatus();
    applyAllStatus();

    if (pin) {
      document.getElementById('pushBtn').addEventListener('click', () => doAction('push', pin));
      document.getElementById('pullBtn').addEventListener('click', () => doAction('pull', pin));
      document.getElementById('forgetPinBtn').addEventListener('click', () => {
        forgetPin();
        render('');
      });
      const autoBox = document.getElementById('autoSyncToggle');
      if (autoBox) autoBox.addEventListener('change', () => {
        try { localStorage.setItem(LS_AUTO, autoBox.checked ? '1' : '0'); } catch (e) {}
        if (autoBox.checked) {
          holdAuto = null;
          netFails = 0;
          requestPull(true);
        } else {
          clearTimeout(pushTimer);
          pushTimer = null;
          setStatus('off');
        }
      });
    } else {
      document.getElementById('newPinBtn').addEventListener('click', () => {
        const newPin = generatePin();
        savePin(newPin);
        doAction('push', newPin);
      });
      document.getElementById('usePinBtn').addEventListener('click', () => {
        const val = document.getElementById('pinInput').value.trim().toUpperCase();
        if (!/^[A-Z0-9]{6}$/.test(val)) {
          render('❌ A PIN is 6 letters or numbers.');
          return;
        }
        savePin(val);
        doAction('pull', val);
      });
    }
  }

  async function doAction(kind, pin) {
    holdAuto = null;
    netFails = 0;
    clearTimeout(pushTimer);
    pushTimer = null;
    setStatus('syncing');
    const statusEl = () => document.getElementById('syncStatus');
    if (statusEl()) statusEl().textContent = kind === 'push' ? 'Pushing…' : 'Pulling…';
    try {
      await runExclusive(async () => {
        if (kind === 'push') {
          const hashAtStart = hashBlob(readLocalBlob());
          await pushToCloud(pin);
          // An answer that landed while the write was in flight is still dirty.
          if (hashBlob(readLocalBlob()) === hashAtStart) {
            dirtyBlocks.clear();
            try { localStorage.setItem(LS_HASH, hashAtStart); } catch (e) {}
          }
        } else {
          const { need } = await pullMerged(pin);
          if (autoSyncEnabled()) {
            if (!legacyHasData) {
              const keep = new Set(need);
              [...dirtyBlocks].forEach(b => { if (!keep.has(b)) dirtyBlocks.delete(b); });
            }
            need.forEach(b => dirtyBlocks.add(b));
          } else dirtyBlocks.clear();
          if (!dirtyBlocks.size) {
            try { localStorage.setItem(LS_HASH, hashBlob(readLocalBlob())); } catch (e) {}
          }
        }
        recordLastSync();
        lastPullAt = Date.now();
      });
      const follow = dirtyBlocks.size && autoSyncEnabled();
      if (!follow) setStatus(navigator.onLine ? 'synced' : 'offline');
      render(kind === 'push' ? '✅ Synced to cloud.' : '✅ Synced from cloud.');
      if (follow) schedulePush(1000);
    } catch (err) {
      handleSyncError(err);
      render(`❌ Sync failed: ${err.message}`);
    }
  }

  if (root) render('');
  bootAuto();
  setTimeout(() => { placeHeaderStatus(); applyAllStatus(); }, 0);
  document.addEventListener('DOMContentLoaded', () => { placeHeaderStatus(); applyAllStatus(); });
}

// Exposed on window: used by index.html's inline boot script, and handy for testing/debugging.
window.pushToCloud = pushToCloud;
window.pullFromCloud = pullFromCloud;
window.getSavedPin = getSavedPin;
window.__syncInternals = { mergeFlags, mergeProgress, mergeScoreHistory, mergeAttempts, mergeAtlas, mergeSettings, mergeBlobs, readLocalBlob, cloudBlockBlob, fetchRemoteBlob, writeRemoteBlob, patchDoc, hashBlob, syncCounts };

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSyncUI);
} else {
  initSyncUI();
}
