'use strict';
/**
 * live.js — in-person, Kahoot-style live question sessions for the
 * OCOM Question Hub. One person hosts from a laptop/projector;
 * everyone else joins from their own phone with a short room code and taps
 * A–E. The host controls when the answer is revealed and when the group
 * moves to the next question.
 *
 * No accounts, same throwaway-room-code philosophy as sync.js — built on
 * the same Firestore project, called directly via REST (no SDK).
 *
 * Firestore layout (collection `live_sessions`, separate from `syncs` so
 * it can't collide with the progress-sync feature):
 *
 *   live_sessions/{code}                        session state — HOST writes this doc
 *   live_sessions/{code}/participants/{pid}      one doc per responder — only THAT responder writes it
 *   live_sessions/{code}/answers/{qIdx}_{pid}    one doc per (question, responder) — only THAT responder writes it
 *
 * Every document has exactly one writer, so plain overwrite PATCHes are
 * safe — there's no scenario where two different people race on the same
 * doc and clobber each other, even though everyone is polling/writing the
 * same Firestore project concurrently during a session.
 */

// ---- Same Firebase project as sync.js ----
const FIREBASE_CONFIG = {
  projectId: 'q-bank-cache',
  apiKey: 'AIzaSyAvYYQ5gAjcRN4W52ulCZ5nuA9BsuvNqN4',
};

const BLOCKS = [
  { key: 'psych', label: 'Psychiatry' },
  { key: 'neuro', label: 'Neuro' },
  { key: 'endocrine', label: 'Endocrine' },
  { key: 'eent', label: 'EENT' },
  { key: 'pulm', label: 'Pulmonology' },
  { key: 'ortho', label: 'Orthopedics' },
  { key: 'rheum', label: 'Rheumatology' },
];

const POLL_MS = 2000;
const CODE_ALPHABET = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'; // no 0/O/1/I

// ============================== Firestore REST ==============================

function baseUrl() {
  return `https://firestore.googleapis.com/v1/projects/${FIREBASE_CONFIG.projectId}/databases/(default)/documents`;
}
function withKey(url) {
  return url + (url.includes('?') ? '&' : '?') + `key=${FIREBASE_CONFIG.apiKey}`;
}

function encodeValue(v) {
  if (v === null || v === undefined) return { nullValue: null };
  if (typeof v === 'boolean') return { booleanValue: v };
  if (typeof v === 'number') return Number.isInteger(v) ? { integerValue: String(v) } : { doubleValue: v };
  if (Array.isArray(v)) return { arrayValue: { values: v.map(encodeValue) } };
  return { stringValue: String(v) };
}
function decodeValue(fv) {
  if (!fv) return null;
  if ('stringValue' in fv) return fv.stringValue;
  if ('integerValue' in fv) return parseInt(fv.integerValue, 10);
  if ('doubleValue' in fv) return fv.doubleValue;
  if ('booleanValue' in fv) return fv.booleanValue;
  if ('arrayValue' in fv) return (fv.arrayValue.values || []).map(decodeValue);
  if ('nullValue' in fv) return null;
  return null;
}
function toFields(obj) {
  const fields = {};
  Object.keys(obj).forEach(k => { fields[k] = encodeValue(obj[k]); });
  return { fields };
}
function fromDoc(doc) {
  const out = {};
  const fields = (doc && doc.fields) || {};
  Object.keys(fields).forEach(k => { out[k] = decodeValue(fields[k]); });
  return out;
}

async function getDoc(path) {
  const res = await fetch(withKey(`${baseUrl()}/${path}`));
  if (res.status === 404) return null;
  if (!res.ok) throw new Error(`Firestore read failed (HTTP ${res.status})`);
  return fromDoc(await res.json());
}
// Full-document overwrite. Safe here because every path we ever call this
// on has exactly one writer (see layout note above).
async function putDoc(path, obj) {
  const res = await fetch(withKey(`${baseUrl()}/${path}`), {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(toFields(obj)),
  });
  if (!res.ok) throw new Error(`Firestore write failed (HTTP ${res.status})`);
  return res.json();
}
async function listDocs(path) {
  const res = await fetch(withKey(`${baseUrl()}/${path}?pageSize=300`));
  if (res.status === 404) return [];
  if (!res.ok) throw new Error(`Firestore list failed (HTTP ${res.status})`);
  const json = await res.json();
  return (json.documents || []).map(d => {
    const row = fromDoc(d);
    row._id = d.name.split('/').pop();
    return row;
  });
}
async function deleteDoc(path) {
  await fetch(withKey(`${baseUrl()}/${path}`), { method: 'DELETE' }).catch(() => {});
}
// Server-side filtered query (cheaper than listDocs+filter: only the matching
// docs count as reads, instead of the whole collection every poll tick).
async function queryEquals(parentPath, collectionId, fieldPath, value) {
  const res = await fetch(withKey(`${baseUrl()}/${parentPath}:runQuery`), {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      structuredQuery: {
        from: [{ collectionId }],
        where: { fieldFilter: { field: { fieldPath }, op: 'EQUAL', value: encodeValue(value) } },
      },
    }),
  });
  if (!res.ok) throw new Error(`Firestore query failed (HTTP ${res.status})`);
  const rows = await res.json();
  return rows.filter(r => r.document).map(r => {
    const row = fromDoc(r.document);
    row._id = r.document.name.split('/').pop();
    return row;
  });
}
// Deletes an entire session and its subcollections. Best-effort — used when
// a host explicitly ends/cancels a room so rooms don't pile up in Firestore.
async function deleteSessionTree(code) {
  const [participants, answers] = await Promise.all([
    listDocs(`live_sessions/${code}/participants`).catch(() => []),
    listDocs(`live_sessions/${code}/answers`).catch(() => []),
  ]);
  await Promise.all([
    ...participants.map(p => deleteDoc(`live_sessions/${code}/participants/${p._id}`)),
    ...answers.map(a => deleteDoc(`live_sessions/${code}/answers/${a._id}`)),
  ]);
  await deleteDoc(`live_sessions/${code}`);
}

// ============================== helpers ==============================

function generateCode() {
  let code = '';
  for (let i = 0; i < 5; i++) code += CODE_ALPHABET[Math.floor(Math.random() * CODE_ALPHABET.length)];
  return code;
}
function randomId() {
  return Math.random().toString(36).slice(2, 10);
}
function esc(str) {
  const d = document.createElement('div');
  d.textContent = str == null ? '' : String(str);
  return d.innerHTML;
}

let loadedBlockKey = null;
function loadBlockData(blockKey) {
  return new Promise((resolve, reject) => {
    if (loadedBlockKey === blockKey && window.QUIZ_DATA) { resolve(window.QUIZ_DATA); return; }
    window.QUIZ_DATA = undefined;
    const existing = document.getElementById('blockDataScript');
    if (existing) existing.remove();
    const script = document.createElement('script');
    script.id = 'blockDataScript';
    script.src = `${blockKey}/data.js`;
    script.onload = () => {
      loadedBlockKey = blockKey;
      if (window.QUIZ_DATA) resolve(window.QUIZ_DATA);
      else reject(new Error('data.js loaded but QUIZ_DATA was not set'));
    };
    script.onerror = () => reject(new Error(`Could not load ${blockKey}/data.js`));
    document.head.appendChild(script);
  });
}
function flattenSdls(quizData) {
  const sdls = [];
  (quizData.exams || []).forEach(exam => {
    (exam.sdls || []).forEach(sdl => {
      sdls.push({ examNumber: exam.examNumber, sdlNumber: sdl.sdlNumber, title: sdl.title, questions: sdl.questions || [] });
    });
  });
  return sdls;
}
function questionById(quizData, id) {
  for (const exam of quizData.exams || []) {
    for (const sdl of exam.sdls || []) {
      for (const q of sdl.questions || []) {
        if (q.id === id) return q;
      }
    }
  }
  return null;
}
function shuffleArr(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
// Every question id in a block across both regular batches — excludes batch
// 3 (Bloom Batch), same opt-in-only exclusion the regular per-block app uses
// for its own Exam/Final Exam Simulation question pools. Pass examNumber to
// scope to just that exam; omit (or pass null) for the whole block.
function allBlockQuestionIds(quizData, examNumber) {
  const ids = [];
  (quizData.exams || []).forEach(exam => {
    if (examNumber != null && exam.examNumber !== examNumber) return;
    (exam.sdls || []).forEach(sdl => {
      (sdl.questions || []).forEach(q => { if (q.batch !== 3) ids.push(q.id); });
    });
  });
  return ids;
}
// Every question id from every exam strictly BEFORE examNumber — the "prior
// weeks" pool used to blend a per-exam mock exam the same cumulative way the
// per-block app's Full Exam Simulation does.
function blockQuestionIdsBefore(quizData, examNumber) {
  const ids = [];
  (quizData.exams || []).forEach(exam => {
    if (exam.examNumber >= examNumber) return;
    (exam.sdls || []).forEach(sdl => {
      (sdl.questions || []).forEach(q => { if (q.batch !== 3) ids.push(q.id); });
    });
  });
  return ids;
}
function joinUrl(code) {
  const here = location.origin + location.pathname;
  return `${here}?join=${code}`;
}

// ============================== app state ==============================

const root = () => document.getElementById('liveRoot');
let state = { screen: 'landing' };
let pollTimer = null;

function setState(patch) {
  state = Object.assign({}, state, patch);
  render();
}
function stopPolling() {
  if (pollTimer) { clearInterval(pollTimer); pollTimer = null; }
  clearAutoAdvanceTimer();
}
function startPolling(fn) {
  stopPolling();
  fn();
  pollTimer = setInterval(fn, POLL_MS);
}

// ============================== landing ==============================

function renderLanding() {
  root().innerHTML = `
    <div class="live-card">
      <h1>Live Session</h1>
      <p class="subtitle">An in-person, Kahoot-style round: one host controls the pace, everyone else answers A–E on their own phone.</p>
      <div class="live-actions">
        <button class="live-btn" id="hostBtn">🖥️ Host a Session</button>
        <button class="live-btn secondary" id="joinBtn">📱 Join a Session</button>
      </div>
      <details class="faq">
        <summary>❓ How this works / FAQ</summary>
        <div class="faq-body">
          <p><b>Hosting</b> — pick a block, then either pick specific SDL(s)/batch(es) to pull questions from, or use 🎯 Mock Exam to auto-build a random N-question set from the whole block in one click. You'll land in a lobby with a 5-letter room code and a QR code — share either one. Once people have joined, hit "Start Session."</p>
          <p><b>Joining</b> — go to the Live Session page, tap "Join a Session," and enter the room code plus your name. No account needed.</p>
          <p><b>Pacing</b> — by default you control it manually: Reveal Answer, then Next Question. Turning on Auto-Advance at setup reveals and moves on for you after a set number of seconds, so you don't have to babysit the host screen.</p>
          <p><b>During the round</b> — 🔓/🔒 Lock Room stops new people from joining mid-session (existing joiners are unaffected). ← Previous Question lets you back up if you moved on too fast. ⏹ End Early stops the round at any point and jumps straight to the leaderboard.</p>
          <p><b>🧹 Clean Up Room</b> — once the session ends, this permanently deletes the room, its participants, and every submitted answer from the shared database. Please do this when you're done — old rooms don't expire on their own, and leaving a lot of them around makes room codes more likely to collide with a new session. "Back without cleaning up" is there if you want to leave it a bit longer so people can screenshot the leaderboard, but circle back and clean it up afterward.</p>
          <p><b>Is anyone's personal data stored?</b> — Just whatever first name a participant types in to join, and their answers/score for that one room — all of it gets deleted the moment you clean up the room. Nothing here is tied to accounts or saved long-term.</p>
        </div>
      </details>
    </div>
  `;
  document.getElementById('hostBtn').addEventListener('click', () => setState({ screen: 'hostSetup' }));
  document.getElementById('joinBtn').addEventListener('click', () => setState({ screen: 'joinEntry', code: '' }));
}

// ============================== host: setup ==============================

function renderHostSetup() {
  const blockKey = state.blockKey || '';
  root().innerHTML = `
    <div class="live-card">
      <button class="link-btn" id="backBtn">&larr; Back</button>
      <h1>Host a Session</h1>
      <p class="subtitle">Pick a block, then pick which SDL(s) to pull questions from.</p>
      <label class="live-label">Block</label>
      <select id="blockSelect" class="live-select">
        <option value="">Choose a block…</option>
        ${BLOCKS.map(b => `<option value="${b.key}" ${b.key === blockKey ? 'selected' : ''}>${b.label}</option>`).join('')}
      </select>
      <div id="sdlPicker"></div>
    </div>
  `;
  document.getElementById('backBtn').addEventListener('click', () => setState({ screen: 'landing' }));
  document.getElementById('blockSelect').addEventListener('change', async (e) => {
    const key = e.target.value;
    if (!key) { setState({ blockKey: '', sdls: null, selectedBatches: [] }); return; }
    document.getElementById('sdlPicker').innerHTML = `<p class="loading">Loading question bank…</p>`;
    try {
      const data = await loadBlockData(key);
      setState({ blockKey: key, quizData: data, sdls: flattenSdls(data), selectedBatches: [] });
    } catch (err) {
      document.getElementById('sdlPicker').innerHTML = `<p class="live-error">${esc(err.message)}</p>`;
    }
  });
  if (state.sdls) renderSdlPicker();
}

function batchLabel(b) {
  if (b === 1) return 'Batch 1 — Quick Recall';
  if (b === 2) return 'Batch 2 — Deep Vignettes';
  if (b === 3) return 'Batch 3 — Bloom Batch';
  return `Batch ${b}`;
}

function renderSdlPicker() {
  const container = document.getElementById('sdlPicker');
  if (!container) return;
  const selected = state.selectedBatches || [];
  const examNumbers = Array.from(new Set(state.sdls.map(s => s.examNumber))).sort((a, b) => a - b);
  const examCounts = {};
  const priorCounts = {};
  examNumbers.forEach(en => {
    examCounts[en] = allBlockQuestionIds(state.quizData, en).length;
    priorCounts[en] = blockQuestionIdsBefore(state.quizData, en).length;
  });
  const blockTotal = allBlockQuestionIds(state.quizData).length;
  const mockDefault = Math.min(100, blockTotal);
  container.innerHTML = `
    <div style="border: 2px solid var(--navy); border-radius: 10px; padding: 14px 16px; margin: 14px 0;">
      <div style="font-weight:700; color:var(--navy); margin-bottom:4px;">🎯 Mock Exam</div>
      <p class="live-status" style="margin-top:0;">Skip the manual picker below — randomly build a mock exam pulling from every SDL and both batches, scoped to one exam or the whole block. Same idea as the app's Full/Final Exam Simulation, just as a live round.</p>
      <div style="display:flex; align-items:center; gap:10px; flex-wrap:wrap;">
        <label for="mockExamScope" style="font-size:0.85rem; color:var(--grey-text); font-weight:700;">Scope</label>
        <select id="mockExamScope" class="live-select" style="width:auto;">
          <option value="">All Exams (${blockTotal} questions)</option>
          ${examNumbers.map(en => `<option value="${en}">Exam ${en} only (${examCounts[en]} questions)</option>`).join('')}
        </select>
        <label for="mockExamCount" style="font-size:0.85rem; color:var(--grey-text); font-weight:700;">Questions</label>
        <input type="number" id="mockExamCount" class="live-select" style="width:90px;" min="10" max="${blockTotal}" step="5" value="${mockDefault}" ${blockTotal < 10 ? 'disabled' : ''}>
        <button class="live-btn" id="mockExamBtn" ${blockTotal < 10 ? 'disabled' : ''}>Create Mock Exam Session</button>
      </div>
      <div id="mockPctRow" style="margin-top:10px; display:none;">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <label for="mockPctSlider" style="font-size:0.85rem; color:var(--grey-text); font-weight:700;">Content Source</label>
          <span id="mockPctReadout" class="live-status" style="margin:0;"></span>
        </div>
        <input type="range" id="mockPctSlider" min="0" max="100" step="5" value="70" style="width:100%;">
      </div>
    </div>
    <label class="live-label" style="margin-top:16px;">SDLs &amp; batches to include (manual)</label>
    <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:8px;">
      ${examNumbers.map(en => `<button class="live-btn secondary" data-quick-exam="${en}" style="padding:6px 12px; font-size:0.82rem;">Select Entire Exam ${en}</button>`).join('')}
      <button class="live-btn secondary" id="clearAllBtn" style="padding:6px 12px; font-size:0.82rem;" ${selected.length ? '' : 'disabled'}>Clear All</button>
    </div>
    <p class="live-status" style="margin-top:0;">Heads up: a full exam's worth of questions runs long as a live, host-paced round (Auto-Advance below can help) — great for a big review session, just budget the time.</p>
    <div class="sdl-list">
      ${state.sdls.map((s, i) => {
        const batches = Array.from(new Set(s.questions.map(q => q.batch))).sort((a, b) => a - b);
        return `
          <div class="sdl-group">
            <div class="sdl-group-title">Exam ${s.examNumber} &middot; SDL ${s.sdlNumber} — ${esc(s.title)}</div>
            ${batches.map(b => {
              const key = `${i}-${b}`;
              const qCount = s.questions.filter(q => q.batch === b).length;
              const checked = selected.includes(key);
              return `
                <label class="sdl-row sdl-row-batch">
                  <input type="checkbox" data-key="${key}" ${checked ? 'checked' : ''}>
                  <span>${batchLabel(b)} <span class="q-count">(${qCount} questions)</span></span>
                </label>
              `;
            }).join('')}
          </div>
        `;
      }).join('')}
    </div>
    <div class="live-status" id="pickerStatus">
      ${selected.length ? `${totalQuestions()} question(s) selected` : 'Select at least one batch'}
    </div>
    <label class="live-label" style="margin-top:16px;">Pacing</label>
    <label class="sdl-row" style="cursor:pointer;">
      <input type="checkbox" id="autoAdvanceToggle" ${state.autoAdvanceOn ? 'checked' : ''}>
      <span>⏱ Auto-advance each question — reveal &amp; move on for me, no manual "Next" needed</span>
    </label>
    <div id="autoAdvanceRow" style="margin-top:8px; ${state.autoAdvanceOn ? '' : 'opacity:0.45;'}">
      <div class="setup-label-row" style="display:flex; justify-content:space-between; align-items:center;">
        <label for="autoAdvanceSecs" style="font-size:0.85rem; color:var(--grey-text); font-weight:700;">Seconds to answer before reveal</label>
      </div>
      <input type="number" id="autoAdvanceSecs" class="live-select" style="width:100px;" min="5" max="300" step="5" value="${state.autoAdvanceSecs || 20}" ${state.autoAdvanceOn ? '' : 'disabled'}>
    </div>
    <div class="live-actions" style="margin-top:14px;">
      <button class="live-btn" id="createBtn" ${selected.length ? '' : 'disabled'}>Create Session</button>
    </div>
  `;
  container.querySelectorAll('input[type=checkbox][data-key]').forEach(cb => {
    cb.addEventListener('change', () => {
      const key = cb.dataset.key;
      let sel = (state.selectedBatches || []).slice();
      if (cb.checked) sel.push(key); else sel = sel.filter(x => x !== key);
      setState({ selectedBatches: sel });
    });
  });
  container.querySelectorAll('[data-quick-exam]').forEach(btn => {
    btn.addEventListener('click', () => {
      const en = Number(btn.dataset.quickExam);
      const sel = (state.selectedBatches || []).slice();
      state.sdls.forEach((s, i) => {
        if (s.examNumber !== en) return;
        Array.from(new Set(s.questions.map(q => q.batch))).forEach(b => {
          const key = `${i}-${b}`;
          if (!sel.includes(key)) sel.push(key);
        });
      });
      setState({ selectedBatches: sel });
    });
  });
  const clearAllBtn = document.getElementById('clearAllBtn');
  if (clearAllBtn) clearAllBtn.addEventListener('click', () => setState({ selectedBatches: [] }));
  const mockExamBtn = document.getElementById('mockExamBtn');
  const mockExamCount = document.getElementById('mockExamCount');
  const mockExamScope = document.getElementById('mockExamScope');
  const mockPctRow = document.getElementById('mockPctRow');
  const mockPctSlider = document.getElementById('mockPctSlider');
  const mockPctReadout = document.getElementById('mockPctReadout');

  function scopeTotalFor(en) {
    return en == null ? blockTotal : examCounts[en] + priorCounts[en];
  }
  function updateMockPctRow() {
    const en = mockExamScope.value ? Number(mockExamScope.value) : null;
    if (en == null) { mockPctRow.style.display = 'none'; return; }
    mockPctRow.style.display = 'block';
    const hasPrior = priorCounts[en] > 0;
    mockPctSlider.disabled = !hasPrior;
    if (!hasPrior) {
      mockPctReadout.textContent = `100% Exam ${en} (no earlier exam to blend in)`;
    } else {
      mockPctReadout.textContent = `${mockPctSlider.value}% Exam ${en} · ${100 - mockPctSlider.value}% prior exams`;
    }
  }
  if (mockExamScope) mockExamScope.addEventListener('change', () => {
    const en = mockExamScope.value ? Number(mockExamScope.value) : null;
    const scopeTotal = scopeTotalFor(en);
    mockExamCount.max = scopeTotal;
    mockExamCount.value = Math.min(Number(mockExamCount.value) || mockDefault, scopeTotal);
    updateMockPctRow();
  });
  if (mockPctSlider) mockPctSlider.addEventListener('input', updateMockPctRow);
  updateMockPctRow();
  if (mockExamBtn) mockExamBtn.addEventListener('click', () => {
    const en = mockExamScope && mockExamScope.value ? Number(mockExamScope.value) : null;
    const count = Math.max(10, Number(mockExamCount.value) || mockDefault);
    const pctCurrent = en != null ? Number(mockPctSlider.value) : undefined;
    createMockExamSession(count, en, pctCurrent);
  });
  const autoAdvanceToggle = document.getElementById('autoAdvanceToggle');
  const autoAdvanceRow = document.getElementById('autoAdvanceRow');
  const autoAdvanceSecs = document.getElementById('autoAdvanceSecs');
  autoAdvanceToggle.addEventListener('change', () => {
    state.autoAdvanceOn = autoAdvanceToggle.checked;
    autoAdvanceRow.style.opacity = state.autoAdvanceOn ? '1' : '0.45';
    autoAdvanceSecs.disabled = !state.autoAdvanceOn;
  });
  autoAdvanceSecs.addEventListener('input', () => { state.autoAdvanceSecs = Number(autoAdvanceSecs.value) || 20; });
  const createBtn = document.getElementById('createBtn');
  if (createBtn) createBtn.addEventListener('click', createSession);
}

function totalQuestions() {
  return (state.selectedBatches || []).reduce((sum, key) => {
    const [i, b] = key.split('-').map(Number);
    return sum + state.sdls[i].questions.filter(q => q.batch === b).length;
  }, 0);
}

async function createSession() {
  const questionIds = [];
  (state.selectedBatches || []).forEach(key => {
    const [i, b] = key.split('-').map(Number);
    state.sdls[i].questions.filter(q => q.batch === b).forEach(q => questionIds.push(q.id));
  });
  await createSessionWithQuestionIds(questionIds);
}

// Randomly composed mock exam — pulls from every SDL and both regular
// batches, scoped to one exam or the whole block per examNumber (null =
// whole block). When a specific exam is picked, it's blended the same
// cumulative way the per-block app's Full Exam Simulation is: pctCurrent%
// from that exam, the rest pooled from every exam before it — not just
// "that exam's own questions in isolation." Whole-block scope ignores
// pctCurrent entirely since there's no single "current" exam to weight.
async function createMockExamSession(count, examNumber, pctCurrent) {
  let questionIds;

  if (examNumber == null) {
    const pool = allBlockQuestionIds(state.quizData);
    questionIds = shuffleArr(pool).slice(0, Math.min(count, pool.length));
  } else {
    const currentPool = allBlockQuestionIds(state.quizData, examNumber);
    const priorPool = blockQuestionIdsBefore(state.quizData, examNumber);
    const hasPrior = priorPool.length > 0;

    let currentTarget, priorTarget;
    if (!hasPrior) {
      currentTarget = count;
      priorTarget = 0;
    } else {
      currentTarget = Math.round(count * (pctCurrent == null ? 70 : pctCurrent) / 100);
      priorTarget = count - currentTarget;
    }

    let currentTake = Math.min(currentTarget, currentPool.length);
    let priorTake = Math.min(priorTarget, priorPool.length);

    // If one pool came up short, backfill from the other pool's remaining capacity —
    // same shortfall redistribution as the per-block app's buildCustomExamQuestions.
    let shortfall = (currentTarget - currentTake) + (priorTarget - priorTake);
    if (shortfall > 0) {
      const currentRemaining = currentPool.length - currentTake;
      const addToCurrent = Math.min(shortfall, currentRemaining);
      currentTake += addToCurrent;
      shortfall -= addToCurrent;
      const priorRemaining = priorPool.length - priorTake;
      const addToPrior = Math.min(shortfall, priorRemaining);
      priorTake += addToPrior;
    }

    questionIds = shuffleArr(shuffleArr(currentPool).slice(0, currentTake).concat(shuffleArr(priorPool).slice(0, priorTake)));
  }

  await createSessionWithQuestionIds(questionIds);
}

async function createSessionWithQuestionIds(questionIds) {
  if (!questionIds.length) return;

  const autoAdvanceSeconds = state.autoAdvanceOn ? (state.autoAdvanceSecs || 20) : 0;

  setState({ screen: 'creating' });
  let code = generateCode();
  for (let tries = 0; tries < 5; tries++) {
    const existing = await getDoc(`live_sessions/${code}`).catch(() => null);
    if (!existing) break;
    code = generateCode();
  }
  const hostToken = randomId();
  await putDoc(`live_sessions/${code}`, {
    block: state.blockKey,
    status: 'lobby',
    currentIndex: 0,
    revealed: false,
    locked: false,
    questionIds,
    autoAdvanceSeconds,
    createdAt: Date.now(),
    hostToken,
  });
  sessionStorage.setItem(`live_host_${code}`, hostToken);
  setState({ screen: 'hostRoom', code, hostToken });
  startHostPolling();
}

// ============================== host: room ==============================

function startHostPolling() {
  startPolling(async () => {
    try {
      const [session, participants] = await Promise.all([
        getDoc(`live_sessions/${state.code}`),
        listDocs(`live_sessions/${state.code}/participants`),
      ]);
      if (!session) return;
      let answers = [];
      if (session.status === 'active') {
        // Server-side filter by qIndex — only reads this question's answers,
        // not the whole answer history (which otherwise grows every question).
        answers = await queryEquals(`live_sessions/${state.code}`, 'answers', 'qIndex', session.currentIndex);
      }
      setState({ session, participants, answers });
    } catch (err) {
      setState({ pollError: err.message });
    }
  });
}

function renderHostRoom() {
  const s = state.session;
  if (!s) { root().innerHTML = `<div class="live-card"><p class="loading">Loading session…</p></div>`; return; }

  const participants = state.participants || [];
  const url = joinUrl(state.code);

  if (s.status === 'lobby') {
    clearAutoAdvanceTimer();
    root().innerHTML = `
      <div class="live-card">
        <h1>Room Code</h1>
        <div class="room-code">${state.code}</div>
        <div id="qrCode" class="qr-wrap"></div>
        <p class="subtitle">Have everyone go to <span class="join-url">${esc(url)}</span> and enter this code, or just scan the QR code above.</p>
        <div class="live-actions">
          <button class="live-btn secondary" id="copyBtn">Copy join link</button>
          <button class="live-btn secondary" id="lockBtn">${s.locked ? '🔒 Room Locked' : '🔓 Lock Room'}</button>
        </div>
        ${s.locked ? `<p class="live-status">New people can't join while locked. Unlock to let more people in.</p>` : ''}
        <h2 style="margin-top:24px;">Joined (${participants.length})</h2>
        <div class="participant-chips">
          ${participants.map(p => `<span class="chip">${esc(p.name)}</span>`).join('') || '<span class="live-status">Waiting for people to join…</span>'}
        </div>
        <div class="live-actions" style="margin-top:20px;">
          <button class="live-btn" id="startBtn" ${participants.length ? '' : 'disabled'}>Start Session</button>
          <button class="live-btn secondary" id="cancelBtn">Cancel</button>
        </div>
      </div>
    `;
    document.getElementById('copyBtn').addEventListener('click', () => {
      navigator.clipboard.writeText(url).then(() => {
        document.getElementById('copyBtn').textContent = 'Copied!';
        setTimeout(() => { const b = document.getElementById('copyBtn'); if (b) b.textContent = 'Copy join link'; }, 1500);
      }).catch(() => {});
    });
    document.getElementById('lockBtn').addEventListener('click', () => hostPatch({ locked: !s.locked }));
    const startBtn = document.getElementById('startBtn');
    if (startBtn) startBtn.addEventListener('click', () => hostPatch({ status: 'active', currentIndex: 0, revealed: false }));
    document.getElementById('cancelBtn').addEventListener('click', endSessionAndExit);
    // Best-effort — if the QR library didn't load (offline, CDN blocked), the
    // room code and copy-link button above still work fine on their own.
    const qrEl = document.getElementById('qrCode');
    if (qrEl && window.QRCode) {
      try {
        new QRCode(qrEl, { text: url, width: 160, height: 160, colorDark: '#1f4e79', colorLight: '#ffffff', correctLevel: QRCode.CorrectLevel.M });
      } catch (e) { /* ignore — degrade to code + link only */ }
    }
    return;
  }

  if (s.status === 'active') {
    const q = questionById(state.quizData, s.questionIds[s.currentIndex]);
    const answers = state.answers || [];
    const tally = {};
    answers.forEach(a => { tally[a.choice] = (tally[a.choice] || 0) + 1; });
    const maxTally = Math.max(1, ...Object.values(tally));
    const isLast = s.currentIndex >= s.questionIds.length - 1;

    root().innerHTML = `
      <div class="live-card">
        <div class="host-meta">
          Room <b>${state.code}</b> &middot; Question ${s.currentIndex + 1} of ${s.questionIds.length} &middot; ${participants.length} joined &middot; ${answers.length} answered${s.autoAdvanceSeconds ? ` &middot; ⏱ Auto-pacing on (${s.autoAdvanceSeconds}s/question)` : ''}
          <button class="link-btn-inline" id="lockBtn">${s.locked ? '🔒 Locked' : '🔓 Lock room'}</button>
          <button class="link-btn-inline" id="endEarlyBtn">⏹ End Early</button>
        </div>
        <h2 class="q-stem">${esc(q ? q.stem : '(question not found)')}</h2>
        <div class="choice-list">
          ${q ? Object.keys(q.choices).sort().map(letter => {
            const count = tally[letter] || 0;
            const pct = Math.round((count / maxTally) * 100);
            const isCorrect = s.revealed && letter === q.correct;
            return `
              <div class="choice host-choice ${isCorrect ? 'correct' : ''}">
                <span class="letter">${letter}.</span>
                <span class="choice-text">${esc(q.choices[letter])}</span>
                ${s.revealed ? `
                  <span class="tally-bar-wrap"><span class="tally-bar" style="width:${count ? pct : 0}%"></span></span>
                  <span class="tally-count">${count}</span>
                ` : ''}
              </div>
            `;
          }).join('') : ''}
        </div>
        ${s.revealed && q ? `
          <div class="info-block explanation" style="margin-top:14px;"><b>Explanation</b>${esc(q.explanation || '')}</div>
          ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${esc(q.boardPrep)}</div>` : ''}
          ${q.crossRef ? `<div class="info-block xref">${esc(q.crossRef)}</div>` : ''}
        ` : ''}
        <div class="live-actions" style="margin-top:20px;">
          <button class="live-btn secondary" id="prevBtn" ${s.currentIndex <= 0 ? 'disabled' : ''}>&larr; Previous Question</button>
          ${!s.revealed ? `<button class="live-btn" id="revealBtn">Reveal Answer</button>` : ''}
          <button class="live-btn ${s.revealed ? '' : 'secondary'}" id="nextBtn">${isLast ? 'End Session' : 'Next Question'}</button>
        </div>
      </div>
    `;
    document.getElementById('lockBtn').addEventListener('click', () => hostPatch({ locked: !s.locked }));
    document.getElementById('endEarlyBtn').addEventListener('click', () => {
      if (confirm(`End the session now at question ${s.currentIndex + 1} of ${s.questionIds.length}? Everyone will see the final leaderboard.`)) {
        clearAutoAdvanceTimer();
        hostPatch({ status: 'ended' });
      }
    });
    const revealBtn = document.getElementById('revealBtn');
    if (revealBtn) revealBtn.addEventListener('click', () => { clearAutoAdvanceTimer(); hostPatch({ revealed: true }); });
    const prevBtn = document.getElementById('prevBtn');
    if (prevBtn) prevBtn.addEventListener('click', () => {
      if (s.currentIndex > 0) { clearAutoAdvanceTimer(); hostPatch({ currentIndex: s.currentIndex - 1, revealed: false }); }
    });
    document.getElementById('nextBtn').addEventListener('click', () => {
      clearAutoAdvanceTimer();
      if (isLast) hostPatch({ status: 'ended' });
      else hostPatch({ currentIndex: s.currentIndex + 1, revealed: false });
    });
    scheduleAutoAdvance(s);
    return;
  }

  if (s.status === 'ended') {
    clearAutoAdvanceTimer();
    stopPolling();
    const sorted = participants.slice().sort((a, b) => (b.score || 0) - (a.score || 0));
    root().innerHTML = `
      <div class="live-card">
        <h1>Session Ended</h1>
        <h2>Leaderboard</h2>
        <ol class="leaderboard">
          ${sorted.map(p => `<li><span>${esc(p.name)}</span><span class="lb-score">${p.score || 0}</span></li>`).join('') || '<li>No participants.</li>'}
        </ol>
        <p class="live-status" id="cleanupStatus">Everyone's had a chance to see this? Clean up the room so it doesn't sit around in the database.</p>
        <div class="live-actions" style="margin-top:8px;">
          <button class="live-btn secondary" id="doneBtn">Back without cleaning up</button>
          <button class="live-btn" id="cleanupBtn">🧹 Clean Up Room</button>
        </div>
      </div>
    `;
    document.getElementById('doneBtn').addEventListener('click', () => setState({ screen: 'landing', code: null, session: null }));
    document.getElementById('cleanupBtn').addEventListener('click', async () => {
      const btn = document.getElementById('cleanupBtn');
      btn.disabled = true;
      btn.textContent = 'Cleaning up…';
      await deleteSessionTree(state.code).catch(() => {});
      setState({ screen: 'landing', code: null, session: null });
    });
  }
}

async function hostPatch(patch) {
  const merged = Object.assign({}, state.session, patch);
  await putDoc(`live_sessions/${state.code}`, {
    block: merged.block,
    status: merged.status,
    currentIndex: merged.currentIndex,
    revealed: merged.revealed,
    locked: !!merged.locked,
    questionIds: merged.questionIds,
    autoAdvanceSeconds: merged.autoAdvanceSeconds || 0,
    createdAt: merged.createdAt,
    hostToken: merged.hostToken,
  });
  setState({ session: merged });
}

// ============================== host: auto-advance ==============================
// When the host set a per-question time limit at setup, the host's own tab
// drives pacing locally (via hostPatch, same as a manual click) so every
// participant sees it through the normal 2s poll — no separate schema needed.
function clearAutoAdvanceTimer() {
  if (state._autoTimer) { clearTimeout(state._autoTimer); state._autoTimer = null; }
  state._autoKey = null;
}
function scheduleAutoAdvance(s) {
  const secs = s && s.autoAdvanceSeconds;
  if (!secs || s.status !== 'active') { clearAutoAdvanceTimer(); return; }
  const key = `${s.currentIndex}:${s.revealed}`;
  if (state._autoKey === key) return; // already scheduled for this exact question/reveal state
  clearAutoAdvanceTimer();
  state._autoKey = key;
  const isLast = s.currentIndex >= s.questionIds.length - 1;
  if (!s.revealed) {
    state._autoTimer = setTimeout(() => { hostPatch({ revealed: true }); }, secs * 1000);
  } else {
    // Brief pause to let everyone see the reveal, then move on automatically.
    const revealPause = Math.min(10, Math.max(4, Math.round(secs / 3)));
    state._autoTimer = setTimeout(() => {
      if (isLast) hostPatch({ status: 'ended' });
      else hostPatch({ currentIndex: s.currentIndex + 1, revealed: false });
    }, revealPause * 1000);
  }
}

async function endSessionAndExit() {
  // Cancelled straight out of the lobby — nobody's mid-question, so it's
  // safe to just delete the room outright instead of leaving it as "ended".
  clearAutoAdvanceTimer();
  stopPolling();
  await deleteSessionTree(state.code).catch(() => {});
  setState({ screen: 'landing', code: null, session: null });
}

// ============================== join: entry ==============================

function renderJoinEntry() {
  root().innerHTML = `
    <div class="live-card">
      <button class="link-btn" id="backBtn">&larr; Back</button>
      <h1>Join a Session</h1>
      <label class="live-label">Room Code</label>
      <input type="text" id="codeInput" class="live-select" maxlength="5" style="text-transform:uppercase;" value="${esc(state.code || '')}" placeholder="e.g. K7QRT">
      <label class="live-label" style="margin-top:12px;">Your Name</label>
      <input type="text" id="nameInput" class="live-select" maxlength="30" placeholder="First name is fine">
      <div class="live-status" id="joinStatus"></div>
      <div class="live-actions" style="margin-top:16px;">
        <button class="live-btn" id="joinSubmitBtn">Join</button>
      </div>
    </div>
  `;
  document.getElementById('backBtn').addEventListener('click', () => setState({ screen: 'landing' }));
  document.getElementById('joinSubmitBtn').addEventListener('click', submitJoin);
}

async function submitJoin() {
  const code = document.getElementById('codeInput').value.trim().toUpperCase();
  const name = document.getElementById('nameInput').value.trim();
  const statusEl = document.getElementById('joinStatus');
  if (!code || !name) { statusEl.textContent = 'Enter both a code and your name.'; return; }
  statusEl.textContent = 'Joining…';
  try {
    const session = await getDoc(`live_sessions/${code}`);
    if (!session) { statusEl.textContent = `No session found for code ${code}.`; return; }
    if (session.status === 'ended') { statusEl.textContent = 'That session has already ended.'; return; }

    let pid = localStorage.getItem(`live_pid_${code}`);
    const existingP = pid ? await getDoc(`live_sessions/${code}/participants/${pid}`) : null;

    if (session.locked && !existingP) {
      statusEl.textContent = '🔒 This room is locked. Ask the host to unlock it before you can join.';
      return;
    }

    if (!pid) { pid = randomId(); localStorage.setItem(`live_pid_${code}`, pid); }
    localStorage.setItem(`live_name_${code}`, name);

    await putDoc(`live_sessions/${code}/participants/${pid}`, {
      name,
      score: existingP ? (existingP.score || 0) : 0,
      joinedAt: existingP ? existingP.joinedAt : Date.now(),
    });

    const data = await loadBlockData(session.block);
    setState({
      screen: 'joinRoom', code, pid, name, quizData: data,
      session, answeredThisQ: null, scoredIndexes: loadScoredIndexes(code),
      myAnswers: {}, showBreakdown: false,
    });
    startJoinPolling();
  } catch (err) {
    statusEl.textContent = `Error: ${err.message}`;
  }
}

function scoredKey(code) { return `live_scored_${code}`; }
function loadScoredIndexes(code) {
  try { return JSON.parse(localStorage.getItem(scoredKey(code)) || '[]'); } catch (e) { return []; }
}
function markScored(code, idx) {
  const list = loadScoredIndexes(code);
  if (!list.includes(idx)) { list.push(idx); localStorage.setItem(scoredKey(code), JSON.stringify(list)); }
}

// ============================== join: room ==============================

function startJoinPolling() {
  startPolling(async () => {
    try {
      const session = await getDoc(`live_sessions/${state.code}`);
      if (!session) return;
      let answeredThisQ = state.answeredThisQ;
      if (session.status === 'active') {
        if (!state._lastIndex || state._lastIndex !== session.currentIndex) {
          const own = await getDoc(`live_sessions/${state.code}/answers/${session.currentIndex}_${state.pid}`);
          answeredThisQ = own ? own.choice : null;
          // Keep a running local record of this participant's own answer per
          // question — powers the "Your Answers" breakdown once the session
          // ends. It's only ever this device's own answers, never anyone else's.
          if (own) state.myAnswers = Object.assign({}, state.myAnswers, { [session.currentIndex]: own.choice });
        }
      }
      setState({ session, answeredThisQ, _lastIndex: session.currentIndex });

      // Score exactly once per question, right after reveal, from this device.
      if (session.status === 'active' && session.revealed && answeredThisQ) {
        const scored = loadScoredIndexes(state.code);
        if (!scored.includes(session.currentIndex)) {
          const q = questionById(state.quizData, session.questionIds[session.currentIndex]);
          if (q && answeredThisQ === q.correct) {
            const me = await getDoc(`live_sessions/${state.code}/participants/${state.pid}`);
            await putDoc(`live_sessions/${state.code}/participants/${state.pid}`, {
              name: state.name,
              score: (me && me.score ? me.score : 0) + 1,
              joinedAt: me ? me.joinedAt : Date.now(),
            });
          }
          markScored(state.code, session.currentIndex);
        }
      }
    } catch (err) {
      setState({ pollError: err.message });
    }
  });
}

function renderJoinRoom() {
  const s = state.session;
  if (!s) { root().innerHTML = `<div class="live-card"><p class="loading">Loading…</p></div>`; return; }

  if (s.status === 'lobby') {
    root().innerHTML = `
      <div class="live-card">
        <h1>You're in, ${esc(state.name)} 👋</h1>
        <p class="subtitle">Waiting for the host to start room <b>${state.code}</b>…</p>
      </div>
    `;
    return;
  }

  if (s.status === 'active') {
    const q = questionById(state.quizData, s.questionIds[s.currentIndex]);
    const mine = state.answeredThisQ;
    root().innerHTML = `
      <div class="live-card">
        <div class="host-meta">Room ${state.code} &middot; Question ${s.currentIndex + 1} of ${s.questionIds.length}</div>
        <h2 class="q-stem">${esc(q ? q.stem : '')}</h2>
        <div class="choice-list">
          ${q ? Object.keys(q.choices).sort().map(letter => {
            let cls = 'choice';
            if (mine === letter) cls += ' selected';
            if (s.revealed) {
              cls += ' disabled';
              if (letter === q.correct) cls += ' correct';
              else if (letter === mine) cls += ' incorrect';
            }
            return `
              <button class="${cls}" data-letter="${letter}" ${s.revealed ? 'disabled' : ''}>
                <span class="letter">${letter}.</span>
                <span>${esc(q.choices[letter])}</span>
              </button>
            `;
          }).join('') : ''}
        </div>
        ${!mine && !s.revealed ? '' : (s.revealed ? `
          <div class="feedback-banner ${mine === (q && q.correct) ? 'correct' : 'incorrect'}">
            ${mine === (q && q.correct) ? '✅ Correct!' : `❌ Correct answer: ${q ? q.correct : ''}`}
          </div>
          ${q && q.explanation ? `<div class="info-block explanation"><b>Explanation</b>${esc(q.explanation)}</div>` : ''}
          ${q && q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${esc(q.boardPrep)}</div>` : ''}
          ${q && q.crossRef ? `<div class="info-block xref">${esc(q.crossRef)}</div>` : ''}
        ` : `<p class="live-status">Answer selected — tap another choice to change it, or wait for the host to reveal.</p>`)}
      </div>
    `;
    if (!s.revealed) {
      root().querySelectorAll('.choice').forEach(btn => {
        btn.addEventListener('click', () => submitAnswer(btn.dataset.letter));
      });
    }
    return;
  }

  if (s.status === 'ended') {
    stopPolling();
    const myAnswers = state.myAnswers || {};
    const showBreakdown = !!state.showBreakdown;
    let correctCount = 0;
    const rows = s.questionIds.map((qid, i) => {
      const q = questionById(state.quizData, qid);
      const mine = myAnswers[i];
      const isCorrect = q && mine === q.correct;
      if (isCorrect) correctCount++;
      if (!q) return '';
      return `
        <div class="q-card" style="margin-top:12px;">
          <div class="host-meta">Question ${i + 1} of ${s.questionIds.length}</div>
          <div class="q-stem" style="font-weight:600;">${esc(q.stem)}</div>
          <div class="feedback-banner ${isCorrect ? 'correct' : 'incorrect'}" style="margin-top:8px;">
            ${mine ? (isCorrect ? '✅ You answered correctly' : `❌ You answered ${mine} — correct answer: ${q.correct}`) : `⚠️ Not answered — correct answer: ${q.correct}`}
          </div>
          ${q.explanation ? `<div class="info-block explanation"><b>Explanation</b>${esc(q.explanation)}</div>` : ''}
          ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${esc(q.boardPrep)}</div>` : ''}
          ${q.crossRef ? `<div class="info-block xref">${esc(q.crossRef)}</div>` : ''}
        </div>
      `;
    }).join('');

    root().innerHTML = `
      <div class="live-card">
        <h1>Session Ended</h1>
        <p class="subtitle">Thanks for playing, ${esc(state.name)}! You got ${correctCount} of ${s.questionIds.length} correct.</p>
        <div class="live-actions" style="margin-top:16px;">
          <button class="live-btn secondary" id="toggleBreakdownBtn">${showBreakdown ? 'Hide' : 'Show'} Your Answers</button>
          <button class="live-btn" id="doneBtn">Back to Live Session home</button>
        </div>
        ${showBreakdown ? rows : ''}
      </div>
    `;
    document.getElementById('doneBtn').addEventListener('click', () => setState({ screen: 'landing', code: null, session: null, myAnswers: {} }));
    document.getElementById('toggleBreakdownBtn').addEventListener('click', () => setState({ showBreakdown: !showBreakdown }));
  }
}

async function submitAnswer(letter) {
  setState({ answeredThisQ: letter, myAnswers: Object.assign({}, state.myAnswers, { [state.session.currentIndex]: letter }) });
  try {
    await putDoc(`live_sessions/${state.code}/answers/${state.session.currentIndex}_${state.pid}`, {
      choice: letter,
      qIndex: state.session.currentIndex,
      ts: Date.now(),
    });
  } catch (err) {
    setState({ answeredThisQ: null, pollError: err.message });
  }
}

// ============================== dispatch ==============================

function render() {
  if (state.screen === 'landing') renderLanding();
  else if (state.screen === 'hostSetup') renderHostSetup();
  else if (state.screen === 'creating') { root().innerHTML = `<div class="live-card"><p class="loading">Creating session…</p></div>`; }
  else if (state.screen === 'hostRoom') renderHostRoom();
  else if (state.screen === 'joinEntry') renderJoinEntry();
  else if (state.screen === 'joinRoom') renderJoinRoom();
}

function boot() {
  const params = new URLSearchParams(location.search);
  const join = params.get('join');
  if (join) setState({ screen: 'joinEntry', code: join.toUpperCase() });
  else render();
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();
