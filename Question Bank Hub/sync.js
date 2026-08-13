'use strict';
/**
 * sync.js — PIN-based cross-device sync for the Board Prep Question Bank Hub.
 *
 * No accounts, no login. A PIN is just a shared "room code": whoever has it
 * can read/write the same small cloud document. That document holds every
 * block's localStorage progress (flags, scores, attempts, settings), synced
 * across all 6 blocks in one action since they all share this origin's
 * localStorage already.
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

const BLOCK_KEYS = ['neuro', 'pulm', 'eent', 'endocrine', 'ortho', 'rheum'];
const SUFFIXES = ['flags_v1', 'progress_v1', 'attempts_v1', 'settings_v1'];
const LS_PIN = 'qbank_sync_pin';
const LS_LAST_SYNC = 'qbank_sync_last';
const MAX_ATTEMPTS_STORED = 5000;

function allSyncKeys() {
  const keys = [];
  BLOCK_KEYS.forEach(b => SUFFIXES.forEach(s => keys.push(`${b}_${s}`)));
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
  return out;
}

function writeBlobToLocal(blob) {
  Object.keys(blob).forEach(k => localStorage.setItem(k, blob[k]));
}

// ---- Firestore REST helpers ----
function docUrl(pin) {
  return `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents/syncs/${encodeURIComponent(pin)}?key=${FIREBASE_CONFIG.apiKey}`;
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

async function fetchRemoteBlob(pin) {
  const res = await fetch(docUrl(pin));
  if (res.status === 404) return {}; // no cloud data yet for this PIN
  if (!res.ok) throw new Error(`Cloud fetch failed (HTTP ${res.status})`);
  const doc = await res.json();
  return fromFirestoreFields(doc);
}

async function writeRemoteBlob(pin, blob) {
  const res = await fetch(docUrl(pin), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(toFirestoreFields(blob)),
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`Cloud write failed (HTTP ${res.status}) ${text}`);
  }
}

// ---- Public actions ----
async function pushToCloud(pin) {
  const local = readLocalBlob();
  const remote = await fetchRemoteBlob(pin);
  const merged = mergeBlobs(local, remote);
  await writeRemoteBlob(pin, merged);
  return merged;
}

async function pullFromCloud(pin) {
  const remote = await fetchRemoteBlob(pin);
  const local = readLocalBlob();
  const merged = mergeBlobs(local, remote);
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
          <p class="sync-hint">Sync your progress (flags, scores, missed questions) across devices with a PIN — no account needed.</p>
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
window.__syncInternals = { mergeFlags, mergeProgress, mergeAttempts, mergeBlobs, readLocalBlob };

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initSyncUI);
} else {
  initSyncUI();
}
