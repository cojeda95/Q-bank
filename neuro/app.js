'use strict';
/* Neuro Block Question Bank — vanilla JS app. No frameworks, no build step. */

/* ── Global state ─────────────────────────────────────────────────────── */
let DATA = null;               // parsed data.json
let SDL_INDEX = new Map();     // sdlNumber -> {sdl, examNumber}
let session = null;            // active quiz/exam session object
const main = document.getElementById('main');
const homeBtn = document.getElementById('homeBtn');

const LS_FLAGS = 'neuro_flags_v1';
const LS_PROGRESS = 'neuro_progress_v1';
const LS_ATTEMPTS = 'neuro_attempts_v1';
const LS_SETTINGS = 'neuro_settings_v1';
const MAX_ATTEMPTS_STORED = 5000;

/* ── localStorage helpers ────────────────────────────────────────────── */
function loadFlags() {
  try { return JSON.parse(localStorage.getItem(LS_FLAGS)) || {}; }
  catch (e) { return {}; }
}
function saveFlags(flags) {
  localStorage.setItem(LS_FLAGS, JSON.stringify(flags));
}
function isFlagged(id) {
  const flags = loadFlags();
  return !!flags[id];
}
function toggleFlag(id) {
  const flags = loadFlags();
  if (flags[id]) delete flags[id]; else flags[id] = true;
  saveFlags(flags);
  return !!flags[id];
}

function loadProgress() {
  try { return JSON.parse(localStorage.getItem(LS_PROGRESS)) || {}; }
  catch (e) { return {}; }
}
function saveProgress(progress) {
  localStorage.setItem(LS_PROGRESS, JSON.stringify(progress));
}
function recordScore(key, correct, total) {
  const progress = loadProgress();
  const prev = progress[key] || {};
  const entry = prev;
  entry.last = { correct, total, date: new Date().toISOString() };
  if (!entry.best || correct / total > entry.best.correct / entry.best.total) {
    entry.best = { correct, total };
  }
  progress[key] = entry;
  saveProgress(progress);
}
function getScore(key) {
  const progress = loadProgress();
  return progress[key] || null;
}

/* ── Attempt log (powers Analytics + Review Due) ─────────────────────── */
function loadAttempts() {
  try { return JSON.parse(localStorage.getItem(LS_ATTEMPTS)) || []; }
  catch (e) { return []; }
}
function saveAttempts(list) {
  // Cap growth so localStorage never bloats over a semester of use.
  localStorage.setItem(LS_ATTEMPTS, JSON.stringify(list.slice(-MAX_ATTEMPTS_STORED)));
}
function logAttempt(rec) {
  const list = loadAttempts();
  list.push(rec);
  saveAttempts(list);
}
function lastAttemptMap() {
  // Later entries overwrite earlier ones, so this reflects the most recent
  // outcome per question — a question you missed once but have since
  // answered correctly no longer counts as "missed."
  const list = loadAttempts();
  const map = {};
  list.forEach(a => { map[a.id] = a; });
  return map;
}

/* ── Settings (High-Yield Only mode) ─────────────────────────────────── */
function loadSettings() {
  try { return Object.assign({ hyOnly: false }, JSON.parse(localStorage.getItem(LS_SETTINGS)) || {}); }
  catch (e) { return { hyOnly: false }; }
}
function saveSettings(s) {
  localStorage.setItem(LS_SETTINGS, JSON.stringify(s));
}
// Returns an SDL's questions filtered to high-yield-only if that mode is on.
function visibleQuestions(sdl) {
  const s = loadSettings();
  return s.hyOnly ? sdl.questions.filter(q => q.isHighYield) : sdl.questions;
}

/* ── Utilities ────────────────────────────────────────────────────────── */
function escapeHtml(str) {
  if (str == null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function findSdl(sdlNumber) {
  return SDL_INDEX.get(sdlNumber);
}

function allQuestionsForExam(examNumber) {
  // Excludes batch 3 (Bloom Batch) — that's an opt-in experimental trial, not part of
  // the standard question pool used for exam totals, Full Exam Simulation, or the
  // Custom Exam Builder's current/prior blend. Also respects High-Yield Only mode.
  const settings = loadSettings();
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) return [];
  let qs = [];
  exam.sdls.forEach(sdl => {
    sdl.questions.forEach(q => {
      if (q.batch === 3) return;
      if (settings.hyOnly && !q.isHighYield) return;
      qs.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title }));
    });
  });
  return qs;
}

function formatTime(seconds) {
  seconds = Math.max(0, Math.round(seconds));
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${String(s).padStart(2, '0')}`;
}

/* ── Router ───────────────────────────────────────────────────────────── */
function setRoute(hash) {
  window.location.hash = hash;
}

window.addEventListener('hashchange', render);

function render() {
  // Guard: leaving an active timed exam mid-way just abandons the timer.
  if (session && session.timerId && !window.location.hash.startsWith('#exam/')) {
    clearInterval(session.timerId);
  }
  const hash = window.location.hash.replace(/^#/, '');
  const parts = hash.split('/').filter(Boolean);

  homeBtn.hidden = parts.length === 0;

  if (parts.length === 0) {
    renderHome();
  } else if (parts[0] === 'exam-sdls' && parts[1]) {
    renderExamSdlList(parseInt(parts[1], 10));
  } else if (parts[0] === 'practice' && parts[1] && !parts[2]) {
    renderBatchPicker(parseInt(parts[1], 10));
  } else if (parts[0] === 'practice' && parts[1] && parts[2]) {
    renderPracticeStart(parseInt(parts[1], 10), parts[2]);
  } else if (parts[0] === 'examsetup' && parts[1]) {
    renderExamSetup(parseInt(parts[1], 10));
  } else if (parts[0] === 'exam' && parts[1]) {
    renderExamSimStart(parseInt(parts[1], 10));
  } else if (parts[0] === 'flagged') {
    renderFlaggedReview();
  } else if (parts[0] === 'review') {
    renderReviewQueue();
  } else if (parts[0] === 'analytics') {
    renderAnalytics();
  } else if (parts[0] === 'studysheet') {
    renderStudySheet();
  } else {
    renderHome();
  }
}

homeBtn.addEventListener('click', () => setRoute(''));

/* ── Home screen ──────────────────────────────────────────────────────── */
function renderHome() {
  const examCards = DATA.exams.map(e => {
    const qCount = e.sdls.reduce((s, sdl) => s + sdl.questions.length, 0);
    return `
      <div class="exam-card" data-exam="${e.examNumber}">
        <div class="exam-num">Exam ${e.examNumber}</div>
        <div class="exam-label">${e.sdls.length} SDLs · ${qCount} questions</div>
      </div>`;
  }).join('');

  const flagCount = Object.keys(loadFlags()).length;
  const attempts = loadAttempts();

  const map = lastAttemptMap();
  const reviewIds = new Set();
  Object.keys(map).forEach(id => { if (!map[id].correct) reviewIds.add(id); });
  Object.keys(loadFlags()).forEach(id => reviewIds.add(id));
  const reviewCount = reviewIds.size;

  const settings = loadSettings();

  main.innerHTML = `
    <h1>Neuro Block Question Bank</h1>
    <p class="subtitle">Choose an exam block to practice by SDL or run a full timed simulation.${settings.hyOnly ? ' <strong>⚡ High-Yield Only Mode is ON.</strong>' : ''}</p>
    <div class="exam-grid">${examCards}</div>

    <div class="section-label">Study Tools</div>
    <div class="action-card" id="analyticsCard">
      <span class="icon">📊</span>
      <div>
        <div class="sdl-title">Performance Analytics</div>
        <div class="action-label">${attempts.length ? `${attempts.length} answers logged — see your weakest objectives` : 'Answer some questions to unlock this'}</div>
      </div>
    </div>
    <div class="action-card" id="reviewCard">
      <span class="icon">🔁</span>
      <div>
        <div class="sdl-title">Review Due (Missed + Flagged)</div>
        <div class="action-label">${reviewCount} question${reviewCount === 1 ? '' : 's'} to revisit</div>
      </div>
    </div>
    <div class="action-card" id="sheetCard">
      <span class="icon">📄</span>
      <div>
        <div class="sdl-title">Export Study Sheet</div>
        <div class="action-label">Printable list of missed + flagged questions, with explanations</div>
      </div>
    </div>
    <div class="action-card" id="flaggedCard">
      <span class="icon">&#9733;</span>
      <div>
        <div class="sdl-title">Review Flagged Only</div>
        <div class="action-label">${flagCount} question${flagCount === 1 ? '' : 's'} currently flagged, across all SDLs</div>
      </div>
    </div>

    <div class="section-label">Settings</div>
    <label class="radio-option" style="cursor:pointer;">
      <input type="checkbox" id="hyToggle" ${settings.hyOnly ? 'checked' : ''}>
      <span>⚡ High-Yield Only Mode — restrict Practice and Exam Simulation to questions tagged high-yield</span>
    </label>
  `;

  main.querySelectorAll('.exam-card').forEach(card => {
    card.addEventListener('click', () => setRoute(`exam-sdls/${card.dataset.exam}`));
  });
  document.getElementById('flaggedCard').addEventListener('click', () => setRoute('flagged'));
  document.getElementById('reviewCard').addEventListener('click', () => setRoute('review'));
  document.getElementById('analyticsCard').addEventListener('click', () => setRoute('analytics'));
  document.getElementById('sheetCard').addEventListener('click', () => setRoute('studysheet'));
  document.getElementById('hyToggle').addEventListener('change', (e) => {
    const s = loadSettings();
    s.hyOnly = e.target.checked;
    saveSettings(s);
    renderHome();
  });
}

/* ── Per-exam SDL selection screen ───────────────────────────────────── */
function renderExamSdlList(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }

  const settings = loadSettings();
  const totalQ = exam.sdls.reduce((s, sdl) => s + visibleQuestions(sdl).filter(q => q.batch !== 3).length, 0);
  const estMinutes = Math.round(totalQ * 90 / 60);

  const rows = exam.sdls.map(sdl => {
    const key = `sdl-${sdl.sdlNumber}`;
    const score = getScore(key);
    const visible = visibleQuestions(sdl);
    const regularCount = visible.filter(q => q.batch !== 3).length;
    const bloomCount = visible.filter(q => q.batch === 3).length;
    const scoreHtml = score
      ? `<div class="sdl-score">Last: ${score.last.correct}/${score.last.total}${score.best.correct === score.last.correct && score.best.total === score.last.total ? '' : ` · Best: ${score.best.correct}/${score.best.total}`}</div>`
      : `<div class="sdl-score none">Not attempted</div>`;
    return `
      <div class="sdl-row" data-sdl="${sdl.sdlNumber}">
        <div>
          <div class="sdl-title">${escapeHtml(sdl.title)}</div>
          <div class="sdl-meta">${regularCount} questions${bloomCount ? ` &middot; 🧠 ${bloomCount} Bloom Batch` : ''}</div>
        </div>
        ${scoreHtml}
      </div>`;
  }).join('');

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; All Exams</button>
    <h1>Exam ${examNumber}</h1>
    <p class="subtitle">${exam.sdls.length} SDLs · ${totalQ} total questions${settings.hyOnly ? ' · <strong>⚡ High-Yield Only Mode is ON</strong>' : ''}</p>
    <div class="action-card" id="fullSimCard">
      <span class="icon">&#9201;</span>
      <div>
        <div class="sdl-title">Full Exam Simulation</div>
        <div class="action-label">All ${totalQ} questions, timed (~${estMinutes} min budget), no immediate answer reveal</div>
      </div>
    </div>
    <div class="section-label">Practice by SDL</div>
    <div class="sdl-list">${rows}</div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('fullSimCard').addEventListener('click', () => setRoute(`examsetup/${examNumber}`));
  main.querySelectorAll('.sdl-row').forEach(row => {
    row.addEventListener('click', () => setRoute(`practice/${row.dataset.sdl}`));
  });
}

/* ── Custom Exam Builder (weighted current/prior content + batch mix) ── */
function renderExamSetup(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }

  const priorExam = DATA.exams.find(e => e.examNumber === examNumber - 1);
  const hasPrior = !!priorExam;

  const currentAllCount = allQuestionsForExam(examNumber).length;
  const priorAllCount = hasPrior ? allQuestionsForExam(examNumber - 1).length : 0;

  // Sensible defaults, recalculated client-side as controls change.
  const defaultPct = 70;
  const defaultBatch = 'mix';
  const defaultTotal = currentAllCount;

  main.innerHTML = `
    <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
    <h1>Build a Practice Exam</h1>
    <p class="subtitle">Mirror the real exam's structure, or customize the mix.</p>
    <div class="setup-card">

      ${hasPrior ? `
      <div class="setup-row">
        <div class="setup-label-row">
          <label for="pctSlider">Content Source</label>
          <span id="pctReadout" class="setup-readout">${defaultPct}% Exam ${examNumber} · ${100 - defaultPct}% Exam ${examNumber - 1}</span>
        </div>
        <input type="range" id="pctSlider" min="0" max="100" step="5" value="${defaultPct}">
        <div class="setup-hint">Real exam structure: ~70% this week's material (Exam ${examNumber}), ~30% carried over from Exam ${examNumber - 1}. Drag to change the mix.</div>
      </div>
      ` : `
      <div class="setup-row">
        <div class="setup-hint">Exam 1 has no prior exam to blend in — this simulation will draw 100% from Exam 1 content.</div>
      </div>
      `}

      <div class="setup-row">
        <div class="setup-label-row"><label>Batch Mix</label></div>
        <div class="radio-group" id="batchGroup">
          <label class="radio-option"><input type="radio" name="batchMode" value="mix" ${defaultBatch === 'mix' ? 'checked' : ''}> Mix Both Batches</label>
          <label class="radio-option"><input type="radio" name="batchMode" value="1"> Batch 1 Only — Quick Recall</label>
          <label class="radio-option"><input type="radio" name="batchMode" value="2"> Batch 2 Only — Deep Vignettes</label>
        </div>
      </div>

      <div class="setup-row">
        <div class="setup-label-row"><label for="totalInput">Total Questions</label></div>
        <input type="number" id="totalInput" class="number-input" min="1" max="${Math.max(1, currentAllCount + priorAllCount)}" step="1" value="${defaultTotal}">
        <div class="setup-hint" id="poolHint"></div>
        <div class="setup-hint" id="totalError" style="color: var(--red); display: none;"></div>
      </div>

      <button class="btn" id="startSetupBtn" style="width:100%; margin-top:10px;">Start Simulation</button>
    </div>
  `;

  document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${examNumber}`));

  const pctSlider = document.getElementById('pctSlider');
  const pctReadout = document.getElementById('pctReadout');
  const totalInput = document.getElementById('totalInput');
  const poolHint = document.getElementById('poolHint');
  const totalError = document.getElementById('totalError');

  function currentSettings() {
    const pctCurrent = hasPrior && pctSlider ? Number(pctSlider.value) : 100;
    const batchMode = document.querySelector('input[name="batchMode"]:checked').value;
    const total = Number(totalInput.value);
    return { pctCurrent, batchMode, total };
  }

  function poolSizes(batchMode) {
    const filterBatch = (qs) => batchMode === 'mix' ? qs : qs.filter(q => q.batch === Number(batchMode));
    const curPool = filterBatch(allQuestionsForExam(examNumber)).length;
    const priorPool = hasPrior ? filterBatch(allQuestionsForExam(examNumber - 1)).length : 0;
    return { curPool, priorPool };
  }

  function updatePoolHint() {
    const { batchMode } = currentSettings();
    const { curPool, priorPool } = poolSizes(batchMode);
    poolHint.textContent = `Available with this batch filter: ${curPool} from Exam ${examNumber}${hasPrior ? `, ${priorPool} from Exam ${examNumber - 1}` : ''} (combined max ${curPool + priorPool}).`;
  }

  if (pctSlider) {
    pctSlider.addEventListener('input', () => {
      pctReadout.textContent = `${pctSlider.value}% Exam ${examNumber} · ${100 - pctSlider.value}% Exam ${examNumber - 1}`;
    });
  }
  document.querySelectorAll('input[name="batchMode"]').forEach(radio => {
    radio.addEventListener('change', updatePoolHint);
  });
  updatePoolHint();

  document.getElementById('startSetupBtn').addEventListener('click', () => {
    const { pctCurrent, batchMode, total } = currentSettings();
    if (!Number.isFinite(total) || total < 1) {
      totalError.textContent = 'Enter a valid number of questions (at least 1).';
      totalError.style.display = 'block';
      return;
    }
    const { curPool, priorPool } = poolSizes(batchMode);
    if (total > curPool + priorPool) {
      totalError.textContent = `Only ${curPool + priorPool} questions are available with this batch filter — you asked for ${total}. Lower the count or switch to "Mix Both Batches."`;
      totalError.style.display = 'block';
      return;
    }
    totalError.style.display = 'none';
    const composed = buildCustomExamQuestions(examNumber, { pctCurrent, batchMode, total, hasPrior });
    beginExamSession(examNumber, composed.questions);
  });
}

/* Randomly composes a question set for a custom exam simulation, blending
   current-exam content with prior-exam content per the requested percentage,
   optionally restricted to a single batch. */
function buildCustomExamQuestions(examNumber, { pctCurrent, batchMode, total, hasPrior }) {
  const filterBatch = (qs) => batchMode === 'mix' ? qs : qs.filter(q => q.batch === Number(batchMode));

  const currentPool = filterBatch(allQuestionsForExam(examNumber));
  const priorPool = hasPrior ? filterBatch(allQuestionsForExam(examNumber - 1)) : [];

  let currentTarget, priorTarget;
  if (!hasPrior || priorPool.length === 0) {
    currentTarget = total;
    priorTarget = 0;
  } else {
    currentTarget = Math.round(total * pctCurrent / 100);
    priorTarget = total - currentTarget;
  }

  let currentTake = Math.min(currentTarget, currentPool.length);
  let priorTake = Math.min(priorTarget, priorPool.length);

  // If one pool came up short, backfill from the other pool's remaining capacity.
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

  const currentChosen = shuffle(currentPool).slice(0, currentTake)
    .map(q => Object.assign({}, q, { sourceExamNumber: examNumber, sourceTag: 'current' }));
  const priorChosen = shuffle(priorPool).slice(0, priorTake)
    .map(q => Object.assign({}, q, { sourceExamNumber: examNumber - 1, sourceTag: 'prior' }));

  return { questions: shuffle(currentChosen.concat(priorChosen)) };
}

/* ── Batch picker (per-SDL) ───────────────────────────────────────────── */
function renderBatchPicker(sdlNumber) {
  const found = findSdl(sdlNumber);
  if (!found) { renderHome(); return; }
  const { sdl, examNumber } = found;
  const settings = loadSettings();
  const visible = visibleQuestions(sdl);

  const batch1Count = visible.filter(q => q.batch === 1).length;
  const batch2Count = visible.filter(q => q.batch === 2).length;
  const bloomCount = visible.filter(q => q.batch === 3).length;
  const classicBoth = batch1Count > 0 && batch2Count > 0;

  // Build the list of selectable options. If there's only one, skip the picker entirely.
  const options = [];
  if (batch1Count) options.push({ key: '1', title: 'Batch 1 — Quick Recall', meta: `${batch1Count} questions`, scoreKey: `sdl-${sdlNumber}-b1` });
  if (batch2Count) options.push({ key: '2', title: 'Batch 2 — Deep Vignettes', meta: `${batch2Count} questions`, scoreKey: `sdl-${sdlNumber}-b2` });
  if (classicBoth) options.push({ key: 'all', title: 'Both Batches', meta: `${batch1Count + batch2Count} questions`, scoreKey: `sdl-${sdlNumber}` });
  if (bloomCount) options.push({ key: '3', title: '🧠 Bloom Batch — Level 3/4 Trial', meta: `${bloomCount} questions · experimental, board-qbank style`, scoreKey: `sdl-${sdlNumber}-b3`, special: true });

  if (options.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
      <h1>${escapeHtml(sdl.title)}</h1>
      <p class="empty-state">No high-yield questions in this SDL. Turn off High-Yield Only Mode on the Home screen to practice all questions here.</p>
    `;
    document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${examNumber}`));
    return;
  }
  if (options.length === 1) {
    renderPracticeStart(sdlNumber, options[0].key);
    return;
  }

  const scoreFor = (key) => {
    const s = getScore(key);
    return s ? `<div class="sdl-score">Last: ${s.last.correct}/${s.last.total}</div>` : `<div class="sdl-score none">Not attempted</div>`;
  };

  const rows = options.map(opt => `
    <div class="sdl-row ${opt.special ? 'bloom-row' : ''}" data-batch="${opt.key}">
      <div>
        <div class="sdl-title">${opt.title}</div>
        <div class="sdl-meta">${opt.meta}</div>
      </div>
      ${scoreFor(opt.scoreKey)}
    </div>`).join('');

  main.innerHTML = `
    <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
    <h1>${escapeHtml(sdl.title)}</h1>
    <p class="subtitle">Choose which batch to practice.${settings.hyOnly ? ' <strong>⚡ High-Yield Only Mode is ON</strong> — counts below are already filtered.' : ''}</p>
    <div class="sdl-list">${rows}</div>
    ${bloomCount ? '<p class="setup-hint" style="margin-top:14px;">Bloom Batch is an experimental higher-rigor trial — short single-term answer choices and board-qbank-style vignettes, kept separate from the regular batches.</p>' : ''}
  `;

  document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${examNumber}`));
  main.querySelectorAll('.sdl-row').forEach(row => {
    row.addEventListener('click', () => setRoute(`practice/${sdlNumber}/${row.dataset.batch}`));
  });
}

/* ── Practice mode (per-SDL, immediate feedback) ─────────────────────── */
function renderPracticeStart(sdlNumber, batch) {
  const found = findSdl(sdlNumber);
  if (!found) { renderHome(); return; }
  const { sdl, examNumber } = found;
  const baseQuestions = visibleQuestions(sdl);

  const batch1Count = baseQuestions.filter(q => q.batch === 1).length;
  const batch2Count = baseQuestions.filter(q => q.batch === 2).length;
  const hasClassicBatches = batch1Count > 0 && batch2Count > 0;

  let questions = baseQuestions.filter(q => q.batch !== 3); // default/"all": classic batches only, never bloom
  let scoreKey = `sdl-${sdlNumber}`;
  let isBloom = false;

  if (batch === '3') {
    questions = baseQuestions.filter(q => q.batch === 3);
    scoreKey = `sdl-${sdlNumber}-b3`;
    isBloom = true;
  } else if (hasClassicBatches && (batch === '1' || batch === '2')) {
    questions = baseQuestions.filter(q => q.batch === Number(batch));
    scoreKey = `sdl-${sdlNumber}-b${batch}`;
  }

  if (questions.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
      <h1>${escapeHtml(sdl.title)}</h1>
      <p class="empty-state">No questions match the current filters (High-Yield Only Mode is likely on). Turn it off on the Home screen, or pick a different batch.</p>
    `;
    document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${examNumber}`));
    return;
  }

  session = {
    mode: 'practice',
    sdlNumber,
    examNumber,
    scoreKey,
    isBloom,
    questions,
    index: 0,
    correctCount: 0,
    answered: null,     // letter chosen for current question, or null
    pendingLetter: null, // letter chosen but not yet confirmed with a confidence rating
    confidence: null,    // 'guessed' | 'confident' for the current question
  };
  renderPracticeQuestion();
}

function renderPracticeQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const locked = !!(session.answered || session.pendingLetter);

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    if (session.answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === session.answered) cls += ' incorrect';
    } else if (session.pendingLetter) {
      cls += ' disabled';
      if (letter === session.pendingLetter) cls += ' selected';
    }
    return `<button class="${cls}" data-letter="${letter}" ${locked ? 'disabled' : ''}>
      <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
    </button>`;
  }).join('');

  let confidenceHtml = '';
  if (session.pendingLetter && !session.answered) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer?</div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (session.answered) {
    const wasCorrect = session.answered === q.correct;
    feedbackHtml = `
      <div class="feedback-banner ${wasCorrect ? 'correct' : 'incorrect'}">
        ${wasCorrect ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${q.crossRef ? `<div class="info-block xref">${escapeHtml(q.crossRef)}</div>` : ''}
      <div class="next-row"><button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button></div>
    `;
  }

  main.innerHTML = `
    <button class="back-link" id="backExam">&larr; Exam ${session.examNumber}</button>
    ${session.isBloom ? '<div class="bloom-banner">🧠 Bloom Batch — Level 3/4 Trial (experimental, board-qbank style)</div>' : ''}
    <div class="quiz-header">
      <span class="quiz-progress">Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${session.correctCount}/${session.index + (session.answered ? 1 : 0)}</span>
    </div>
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:${(session.index / total) * 100}%"></div></div>
    <div class="q-card">
      <div class="q-meta-row">
        <span class="q-objective">Objective ${q.objective ?? ''} ${q.isHighYield ? '<span class="hy-badge">&#9889; HIGH YIELD</span>' : ''} ${q.bloomLevel ? `<span class="bloom-badge">${escapeHtml(q.bloomLevel)}</span>` : ''}</span>
        <button class="flag-btn ${flagged ? 'flagged' : ''}" id="flagBtn">${flagged ? '★ Flagged' : '☆ Flag for review'}</button>
      </div>
      <div class="q-stem">${escapeHtml(q.stem)}</div>
      <div class="choice-list">${choicesHtml}</div>
      ${confidenceHtml}
      ${feedbackHtml}
    </div>
  `;

  document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${session.examNumber}`));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderPracticeQuestion();
  });

  function finalizeAnswer(confidence) {
    session.answered = session.pendingLetter;
    session.confidence = confidence;
    const correct = session.answered === q.correct;
    if (correct) session.correctCount++;
    logAttempt({
      id: q.id, sdlNumber: session.sdlNumber, sdlTitle: findSdl(session.sdlNumber).sdl.title,
      examNumber: session.examNumber, objective: q.objective, objectiveLabel: q.objectiveLabel,
      batch: q.batch, correct, confidence, mode: 'practice', ts: Date.now(),
    });
    renderPracticeQuestion();
  }

  if (!session.pendingLetter && !session.answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderPracticeQuestion();
      });
    });
  } else if (session.pendingLetter && !session.answered) {
    document.getElementById('confGuessed').addEventListener('click', () => finalizeAnswer('guessed'));
    document.getElementById('confConfident').addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.answered = null;
          session.pendingLetter = null;
          session.confidence = null;
          renderPracticeQuestion();
        } else {
          recordScore(session.scoreKey, session.correctCount, total);
          renderPracticeComplete();
        }
      });
    }
  }
}

function renderPracticeComplete() {
  const total = session.questions.length;
  const pct = Math.round((session.correctCount / total) * 100);
  main.innerHTML = `
    <div class="result-summary">
      <div class="big-pct">${pct}%</div>
      <div class="sub">${session.correctCount} / ${total} correct</div>
    </div>
    <div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
      <button class="btn secondary" id="retryBtn">Retry This Batch</button>
      <button class="btn secondary" id="backBatchBtn">Choose Different Batch</button>
      <button class="btn" id="doneBtn">Back to Exam ${session.examNumber}</button>
    </div>
  `;
  document.getElementById('retryBtn').addEventListener('click', () => setRoute(`practice/${session.sdlNumber}/${session.scoreKey.includes('-b') ? session.scoreKey.slice(-1) : 'all'}`));
  document.getElementById('backBatchBtn').addEventListener('click', () => setRoute(`practice/${session.sdlNumber}`));
  document.getElementById('doneBtn').addEventListener('click', () => setRoute(`exam-sdls/${session.examNumber}`));
}

/* ── Full Exam Simulation mode (timed, no immediate feedback) ────────── */
function renderExamSimStart(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }
  const questions = shuffleExamQuestions(allQuestionsForExam(examNumber));
  if (questions.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
      <p class="empty-state">No questions match High-Yield Only Mode for this exam. Turn it off on the Home screen to run a full simulation.</p>
    `;
    document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${examNumber}`));
    return;
  }
  beginExamSession(examNumber, questions);
}

/* Shared by both the default (100% current exam) and the Custom Exam
   Builder's weighted/batch-filtered simulations. */
function beginExamSession(examNumber, questions) {
  const totalSeconds = questions.length * 90;

  session = {
    mode: 'exam',
    examNumber,
    questions,
    index: 0,
    answers: new Array(questions.length).fill(null), // letter chosen, or null
    totalSeconds,
    remainingSeconds: totalSeconds,
    timerId: null,
    submitted: false,
  };

  session.timerId = setInterval(() => {
    session.remainingSeconds--;
    if (session.remainingSeconds <= 0) {
      session.remainingSeconds = 0;
      clearInterval(session.timerId);
      finishExamSim(true);
      return;
    }
    updateTimerDisplay();
  }, 1000);

  renderExamQuestion();
}

function shuffleExamQuestions(qs) {
  // Keep deterministic order (by SDL/objective) is also fine, but a shuffle
  // gives a more realistic "exam" feel. Simple: keep as-is (grouped by SDL).
  return qs;
}

function updateTimerDisplay() {
  const el = document.getElementById('examTimer');
  if (!el) return;
  el.textContent = formatTime(session.remainingSeconds);
  el.classList.toggle('low', session.remainingSeconds <= 60);
}

function renderExamQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const selected = session.answers[session.index];

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    if (selected === letter) cls += ' selected';
    return `<button class="${cls}" data-letter="${letter}">
      <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
    </button>`;
  }).join('');

  const answeredCount = session.answers.filter(a => a !== null).length;

  main.innerHTML = `
    <div class="quiz-header">
      <span class="quiz-progress">Exam ${session.examNumber} Simulation — Question ${session.index + 1} of ${total}</span>
      <span id="examTimer" class="timer">${formatTime(session.remainingSeconds)}</span>
    </div>
    <div class="quiz-header">
      <span class="quiz-progress">${q.sdlTitle}</span>
      <span class="quiz-score">Answered: ${answeredCount}/${total}</span>
    </div>
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:${(session.index / total) * 100}%"></div></div>
    <div class="q-card">
      <div class="q-meta-row">
        <span class="q-objective">Objective ${q.objective ?? ''}</span>
        <button class="flag-btn ${flagged ? 'flagged' : ''}" id="flagBtn">${flagged ? '★ Flagged' : '☆ Flag for later'}</button>
      </div>
      <div class="q-stem">${escapeHtml(q.stem)}</div>
      <div class="choice-list">${choicesHtml}</div>
      <div class="next-row" style="justify-content: space-between;">
        <button class="btn secondary" id="prevBtn" ${session.index === 0 ? 'disabled' : ''}>Previous</button>
        <div style="display:flex; gap:10px;">
          ${session.index + 1 < total
            ? '<button class="btn" id="nextBtn">Next</button>'
            : '<button class="btn" id="submitBtn">Submit Exam</button>'}
        </div>
      </div>
    </div>
  `;

  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderExamQuestion();
  });
  main.querySelectorAll('.choice').forEach(btn => {
    btn.addEventListener('click', () => {
      session.answers[session.index] = btn.dataset.letter;
      renderExamQuestion();
    });
  });
  const prevBtn = document.getElementById('prevBtn');
  if (prevBtn) prevBtn.addEventListener('click', () => {
    if (session.index > 0) { session.index--; renderExamQuestion(); }
  });
  const nextBtn = document.getElementById('nextBtn');
  if (nextBtn) nextBtn.addEventListener('click', () => {
    if (session.index + 1 < total) { session.index++; renderExamQuestion(); }
  });
  const submitBtn = document.getElementById('submitBtn');
  if (submitBtn) submitBtn.addEventListener('click', () => {
    if (answeredCount < total) {
      if (!confirm(`You have ${total - answeredCount} unanswered question(s). Submit anyway?`)) return;
    }
    finishExamSim(false);
  });
}

function finishExamSim(timeExpired) {
  if (session.timerId) clearInterval(session.timerId);
  session.submitted = true;
  session.timeExpired = timeExpired;

  const total = session.questions.length;
  let correctCount = 0;
  const missed = [];
  const bySdl = {}; // sdlNumber -> {correct, total, title}
  const byObjective = {}; // "sdlNumber-objective" -> {correct, total, sdlNumber, objective}

  session.questions.forEach((q, i) => {
    const ans = session.answers[i];
    const isCorrect = ans === q.correct;
    if (isCorrect) correctCount++;
    else missed.push({ q, given: ans });

    if (!bySdl[q.sdlNumber]) bySdl[q.sdlNumber] = { correct: 0, total: 0, title: q.sdlTitle };
    bySdl[q.sdlNumber].total++;
    if (isCorrect) bySdl[q.sdlNumber].correct++;

    const objKey = `${q.sdlNumber}-${q.objective}`;
    if (!byObjective[objKey]) byObjective[objKey] = { correct: 0, total: 0, sdlNumber: q.sdlNumber, objective: q.objective };
    byObjective[objKey].total++;
    if (isCorrect) byObjective[objKey].correct++;
  });

  recordScore(`exam-${session.examNumber}`, correctCount, total);

  // Log every question in this simulation to the attempts history (no confidence
  // rating is collected in timed exam mode — that's reserved for practice/review).
  session.questions.forEach((q, i) => {
    const ans = session.answers[i];
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle,
      examNumber: q.sourceExamNumber || session.examNumber, objective: q.objective, objectiveLabel: q.objectiveLabel,
      batch: q.batch, correct: ans === q.correct, confidence: null, mode: 'exam', ts: Date.now(),
    });
  });

  const bySource = {}; // 'current' | 'prior' -> {correct, total, examNumber}
  session.questions.forEach((q, i) => {
    if (!q.sourceTag) return;
    const isCorrect = session.answers[i] === q.correct;
    if (!bySource[q.sourceTag]) bySource[q.sourceTag] = { correct: 0, total: 0, examNumber: q.sourceExamNumber };
    bySource[q.sourceTag].total++;
    if (isCorrect) bySource[q.sourceTag].correct++;
  });

  session.results = { correctCount, total, missed, bySdl, byObjective, bySource };
  renderExamResults();
}

function renderExamResults() {
  const { correctCount, total, missed, bySdl, byObjective, bySource } = session.results;
  const pct = Math.round((correctCount / total) * 100);

  const sourceKeys = Object.keys(bySource || {});
  const sourceHtml = sourceKeys.length === 0 ? '' : `
    <div class="section-label">Content Source Breakdown</div>
    <table class="breakdown-table">
      <thead><tr><th>Source</th><th>Score</th><th>%</th></tr></thead>
      <tbody>
        ${sourceKeys.sort().reverse().map(tag => {
          const r = bySource[tag];
          const label = tag === 'current' ? `Exam ${r.examNumber} (this week's material)` : `Exam ${r.examNumber} (prior exam carryover)`;
          return `<tr><td>${label}</td><td>${r.correct}/${r.total}</td><td>${Math.round((r.correct / r.total) * 100)}%</td></tr>`;
        }).join('')}
      </tbody>
    </table>
  `;

  const sdlRows = Object.keys(bySdl).sort((a, b) => a - b).map(sdlNum => {
    const r = bySdl[sdlNum];
    return `<tr><td>${escapeHtml(r.title)}</td><td>${r.correct}/${r.total}</td><td>${Math.round((r.correct / r.total) * 100)}%</td></tr>`;
  }).join('');

  const objRows = Object.keys(byObjective).sort((a, b) => {
    const ra = byObjective[a], rb = byObjective[b];
    return ra.sdlNumber - rb.sdlNumber || ra.objective - rb.objective;
  }).map(k => {
    const r = byObjective[k];
    return `<tr><td>SDL ${r.sdlNumber}, Obj ${r.objective ?? '—'}</td><td>${r.correct}/${r.total}</td><td>${Math.round((r.correct / r.total) * 100)}%</td></tr>`;
  }).join('');

  const missedHtml = missed.length === 0
    ? '<p class="empty-state">No missed questions — perfect score.</p>'
    : missed.map(({ q, given }) => `
      <div class="missed-item">
        <div class="missed-stem">${escapeHtml(q.stem)} ${isFlagged(q.id) ? '<span class="flagged-tag">&#9733; flagged</span>' : ''}</div>
        <div class="your-answer">Your answer: ${given ? `${given} — ${escapeHtml(q.choices[given])}` : '(no answer)'}</div>
        <div class="correct-answer">Correct answer: ${q.correct} — ${escapeHtml(q.choices[q.correct])}</div>
        <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
        ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      </div>
    `).join('');

  main.innerHTML = `
    <h1>Exam ${session.examNumber} Simulation Results</h1>
    ${session.timeExpired ? '<p class="subtitle">Time expired — exam auto-submitted.</p>' : ''}
    <div class="result-summary">
      <div class="big-pct">${pct}%</div>
      <div class="sub">${correctCount} / ${total} correct</div>
    </div>

    ${sourceHtml}

    <div class="section-label">Per-SDL Breakdown</div>
    <table class="breakdown-table">
      <thead><tr><th>SDL</th><th>Score</th><th>%</th></tr></thead>
      <tbody>${sdlRows}</tbody>
    </table>

    <div class="section-label">Per-Objective Breakdown</div>
    <table class="breakdown-table">
      <thead><tr><th>Objective</th><th>Score</th><th>%</th></tr></thead>
      <tbody>${objRows}</tbody>
    </table>

    <div class="section-label">Missed Questions (${missed.length})</div>
    ${missedHtml}

    <div style="display:flex; gap:10px; justify-content:center; margin-top:20px;">
      <button class="btn" id="doneBtn">Back to Exam ${session.examNumber}</button>
    </div>
  `;
  document.getElementById('doneBtn').addEventListener('click', () => setRoute(`exam-sdls/${session.examNumber}`));
}

/* ── Review Flagged Questions ─────────────────────────────────────────── */
function renderFlaggedReview() {
  const flags = loadFlags();
  const ids = Object.keys(flags);
  const flaggedQuestions = [];

  DATA.exams.forEach(exam => {
    exam.sdls.forEach(sdl => {
      sdl.questions.forEach(q => {
        if (flags[q.id]) {
          flaggedQuestions.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: exam.examNumber }));
        }
      });
    });
  });

  if (flaggedQuestions.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Review Flagged Questions</h1>
      <p class="empty-state">No questions are currently flagged. While practicing, tap "Flag for review" on any question to save it here.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  session = {
    mode: 'flagged',
    questions: flaggedQuestions,
    index: 0,
    correctCount: 0,
    answered: null,
    pendingLetter: null,
    confidence: null,
  };
  renderFlaggedQuestion();
}

function renderFlaggedQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const locked = !!(session.answered || session.pendingLetter);

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    if (session.answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === session.answered) cls += ' incorrect';
    } else if (session.pendingLetter) {
      cls += ' disabled';
      if (letter === session.pendingLetter) cls += ' selected';
    }
    return `<button class="${cls}" data-letter="${letter}" ${locked ? 'disabled' : ''}>
      <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
    </button>`;
  }).join('');

  let confidenceHtml = '';
  if (session.pendingLetter && !session.answered) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer?</div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (session.answered) {
    const wasCorrect = session.answered === q.correct;
    feedbackHtml = `
      <div class="feedback-banner ${wasCorrect ? 'correct' : 'incorrect'}">
        ${wasCorrect ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      <div class="next-row"><button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button></div>
    `;
  }

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <div class="quiz-header">
      <span class="quiz-progress">Flagged Review — Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${session.correctCount}/${session.index + (session.answered ? 1 : 0)}</span>
    </div>
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:${(session.index / total) * 100}%"></div></div>
    <div class="q-card">
      <div class="q-meta-row">
        <span class="q-objective">${escapeHtml(q.sdlTitle)} · Objective ${q.objective ?? ''} ${q.isHighYield ? '<span class="hy-badge">&#9889; HIGH YIELD</span>' : ''}</span>
        <button class="flag-btn flagged" id="flagBtn">&#9733; Flagged</button>
      </div>
      <div class="q-stem">${escapeHtml(q.stem)}</div>
      <div class="choice-list">${choicesHtml}</div>
      ${confidenceHtml}
      ${feedbackHtml}
    </div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    // Refresh this same view (item stays visible until navigating away).
    renderFlaggedQuestion();
  });

  function finalizeAnswer(confidence) {
    session.answered = session.pendingLetter;
    session.confidence = confidence;
    const correct = session.answered === q.correct;
    if (correct) session.correctCount++;
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle, examNumber: q.examNumber,
      objective: q.objective, objectiveLabel: q.objectiveLabel, batch: q.batch,
      correct, confidence, mode: 'flagged', ts: Date.now(),
    });
    renderFlaggedQuestion();
  }

  if (!session.pendingLetter && !session.answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderFlaggedQuestion();
      });
    });
  } else if (session.pendingLetter && !session.answered) {
    document.getElementById('confGuessed').addEventListener('click', () => finalizeAnswer('guessed'));
    document.getElementById('confConfident').addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.answered = null;
          session.pendingLetter = null;
          session.confidence = null;
          renderFlaggedQuestion();
        } else {
          setRoute('');
        }
      });
    }
  }
}

/* ── Review Due (missed + flagged, combined) ─────────────────────────── */
function reviewDueIds() {
  const map = lastAttemptMap();
  const ids = new Set();
  Object.keys(map).forEach(id => { if (!map[id].correct) ids.add(id); });
  Object.keys(loadFlags()).forEach(id => ids.add(id));
  return ids;
}

function reviewDueQuestions() {
  const ids = reviewDueIds();
  const qs = [];
  DATA.exams.forEach(exam => {
    exam.sdls.forEach(sdl => {
      sdl.questions.forEach(q => {
        if (ids.has(q.id)) {
          qs.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: exam.examNumber }));
        }
      });
    });
  });
  return qs;
}

function renderReviewQueue() {
  const qs = reviewDueQuestions();

  if (qs.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Review Due</h1>
      <p class="empty-state">Nothing missed or flagged right now — you're all caught up. Keep practicing and this will fill in automatically.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  session = {
    mode: 'review',
    questions: shuffle(qs),
    index: 0,
    correctCount: 0,
    answered: null,
    pendingLetter: null,
    confidence: null,
  };
  renderReviewQuestion();
}

function renderReviewQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const locked = !!(session.answered || session.pendingLetter);

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    if (session.answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === session.answered) cls += ' incorrect';
    } else if (session.pendingLetter) {
      cls += ' disabled';
      if (letter === session.pendingLetter) cls += ' selected';
    }
    return `<button class="${cls}" data-letter="${letter}" ${locked ? 'disabled' : ''}>
      <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
    </button>`;
  }).join('');

  let confidenceHtml = '';
  if (session.pendingLetter && !session.answered) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer?</div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (session.answered) {
    const wasCorrect = session.answered === q.correct;
    feedbackHtml = `
      <div class="feedback-banner ${wasCorrect ? 'correct' : 'incorrect'}">
        ${wasCorrect ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${q.crossRef ? `<div class="info-block xref">${escapeHtml(q.crossRef)}</div>` : ''}
      <div class="next-row"><button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button></div>
    `;
  }

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <div class="quiz-header">
      <span class="quiz-progress">Review Due — Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${session.correctCount}/${session.index + (session.answered ? 1 : 0)}</span>
    </div>
    <div class="progress-bar-outer"><div class="progress-bar-inner" style="width:${(session.index / total) * 100}%"></div></div>
    <div class="q-card">
      <div class="q-meta-row">
        <span class="q-objective">${escapeHtml(q.sdlTitle)} · Objective ${q.objective ?? ''} ${q.isHighYield ? '<span class="hy-badge">&#9889; HIGH YIELD</span>' : ''}</span>
        <button class="flag-btn ${flagged ? 'flagged' : ''}" id="flagBtn">${flagged ? '★ Flagged' : '☆ Flag for review'}</button>
      </div>
      <div class="q-stem">${escapeHtml(q.stem)}</div>
      <div class="choice-list">${choicesHtml}</div>
      ${confidenceHtml}
      ${feedbackHtml}
    </div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderReviewQuestion();
  });

  function finalizeAnswer(confidence) {
    session.answered = session.pendingLetter;
    session.confidence = confidence;
    const correct = session.answered === q.correct;
    if (correct) session.correctCount++;
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle, examNumber: q.examNumber,
      objective: q.objective, objectiveLabel: q.objectiveLabel, batch: q.batch,
      correct, confidence, mode: 'review', ts: Date.now(),
    });
    renderReviewQuestion();
  }

  if (!session.pendingLetter && !session.answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderReviewQuestion();
      });
    });
  } else if (session.pendingLetter && !session.answered) {
    document.getElementById('confGuessed').addEventListener('click', () => finalizeAnswer('guessed'));
    document.getElementById('confConfident').addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.answered = null;
          session.pendingLetter = null;
          session.confidence = null;
          renderReviewQuestion();
        } else {
          setRoute('');
        }
      });
    }
  }
}

/* ── Performance Analytics ───────────────────────────────────────────── */
function renderAnalytics() {
  const attempts = loadAttempts();

  if (attempts.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Performance Analytics</h1>
      <p class="empty-state">No attempts logged yet. Answer some practice or exam questions and check back here.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  const bySdl = {};       // sdlNumber -> {correct, total, title}
  const byObjective = {}; // "sdlNumber-objective" -> {correct, total, sdlNumber, objective, label}
  let totalCorrect = 0;
  let confConfidentTotal = 0, confConfidentWrong = 0;
  let confGuessedTotal = 0, confGuessedRight = 0;

  attempts.forEach(a => {
    if (a.correct) totalCorrect++;

    if (!bySdl[a.sdlNumber]) bySdl[a.sdlNumber] = { correct: 0, total: 0, title: a.sdlTitle || `SDL ${a.sdlNumber}` };
    bySdl[a.sdlNumber].total++;
    if (a.correct) bySdl[a.sdlNumber].correct++;

    const objKey = `${a.sdlNumber}-${a.objective}`;
    if (!byObjective[objKey]) byObjective[objKey] = { correct: 0, total: 0, sdlNumber: a.sdlNumber, objective: a.objective, label: a.objectiveLabel };
    byObjective[objKey].total++;
    if (a.correct) byObjective[objKey].correct++;

    if (a.confidence === 'confident') {
      confConfidentTotal++;
      if (!a.correct) confConfidentWrong++;
    } else if (a.confidence === 'guessed') {
      confGuessedTotal++;
      if (a.correct) confGuessedRight++;
    }
  });

  const overallPct = Math.round((totalCorrect / attempts.length) * 100);

  // Focus areas: objectives with at least 2 attempts, worst accuracy first.
  const objList = Object.values(byObjective)
    .filter(o => o.total >= 2)
    .sort((a, b) => (a.correct / a.total) - (b.correct / b.total));
  const focusRows = objList.slice(0, 10).map(o => {
    const label = (o.label || '').replace(/^Objective\s+\d+\s*—?\s*/i, '');
    return `<tr><td>SDL ${o.sdlNumber} — ${escapeHtml(label)}</td><td>${o.correct}/${o.total}</td><td>${Math.round((o.correct / o.total) * 100)}%</td></tr>`;
  }).join('');

  const sdlList = Object.values(bySdl).sort((a, b) => (a.correct / a.total) - (b.correct / b.total));
  const sdlRows = sdlList.map(s =>
    `<tr><td>${escapeHtml(s.title)}</td><td>${s.correct}/${s.total}</td><td>${Math.round((s.correct / s.total) * 100)}%</td></tr>`
  ).join('');

  const hasCalibration = (confConfidentTotal + confGuessedTotal) > 0;
  const calibrationHtml = !hasCalibration
    ? '<p class="setup-hint">Answer with a confidence rating (Guessed / Confident) during Practice, Flagged, or Review Due mode to unlock calibration stats here.</p>'
    : `
      <table class="breakdown-table">
        <thead><tr><th>Pattern</th><th>Rate</th></tr></thead>
        <tbody>
          <tr><td>Confident but wrong</td><td>${confConfidentWrong} of ${confConfidentTotal} confident answers (${confConfidentTotal ? Math.round(confConfidentWrong / confConfidentTotal * 100) : 0}%)</td></tr>
          <tr><td>Guessed but right</td><td>${confGuessedRight} of ${confGuessedTotal} guessed answers (${confGuessedTotal ? Math.round(confGuessedRight / confGuessedTotal * 100) : 0}%)</td></tr>
        </tbody>
      </table>
      <p class="setup-hint">"Confident but wrong" flags overconfidence — those concepts are worth re-reading, not just re-drilling. "Guessed but right" flags lucky hits that still need reinforcement even though they scored.</p>
    `;

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <h1>Performance Analytics</h1>
    <p class="subtitle">Based on ${attempts.length} logged answers across all practice and exam modes.</p>

    <div class="result-summary">
      <div class="big-pct">${overallPct}%</div>
      <div class="sub">${totalCorrect} / ${attempts.length} correct, all-time</div>
    </div>

    <div class="section-label">Focus Areas — Weakest Objectives</div>
    ${focusRows
      ? `<table class="breakdown-table"><thead><tr><th>Objective</th><th>Score</th><th>%</th></tr></thead><tbody>${focusRows}</tbody></table>`
      : '<p class="empty-state">Not enough repeated attempts per objective yet — answer a few more questions in each SDL.</p>'}

    <div class="section-label">By SDL / Topic</div>
    <table class="breakdown-table"><thead><tr><th>SDL</th><th>Score</th><th>%</th></tr></thead><tbody>${sdlRows}</tbody></table>

    <div class="section-label">Confidence Calibration</div>
    ${calibrationHtml}
  `;
  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
}

/* ── Printable Study Sheet (missed + flagged) ────────────────────────── */
function renderStudySheet() {
  const qs = reviewDueQuestions().sort((a, b) => a.examNumber - b.examNumber || a.sdlNumber - b.sdlNumber);
  const flags = loadFlags();

  if (qs.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Study Sheet</h1>
      <p class="empty-state">Nothing missed or flagged yet — nothing to export.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  const itemsHtml = qs.map((q, i) => `
    <div class="sheet-item">
      <div class="sheet-meta">${escapeHtml(q.sdlTitle)} · Objective ${q.objective ?? ''}${q.isHighYield ? ' · ⚡ High Yield' : ''}${flags[q.id] ? ' · ★ Flagged' : ''}</div>
      <div class="sheet-stem"><b>${i + 1}.</b> ${escapeHtml(q.stem)}</div>
      <div class="sheet-answer">Correct answer: ${q.correct} — ${escapeHtml(q.choices[q.correct])}</div>
      <div class="sheet-explanation">${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="sheet-boardprep"><b>Board Prep:</b> ${escapeHtml(q.boardPrep)}</div>` : ''}
    </div>
  `).join('');

  main.innerHTML = `
    <div class="no-print" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; flex-wrap:wrap; gap:10px;">
      <button class="back-link" id="backHome" style="margin:0;">&larr; Home</button>
      <button class="btn" id="printBtn">🖨️ Print / Save as PDF</button>
    </div>
    <h1 class="print-title">Study Sheet — Missed &amp; Flagged (${qs.length})</h1>
    <div class="sheet-list">${itemsHtml}</div>
  `;
  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('printBtn').addEventListener('click', () => window.print());
}

/* ── Boot ─────────────────────────────────────────────────────────────── */
try {
  if (!window.NEURO_QUIZ_DATA) throw new Error('data.js did not define window.NEURO_QUIZ_DATA — make sure data.js is loaded before app.js in index.html.');
  DATA = window.NEURO_QUIZ_DATA;
  DATA.exams.forEach(exam => {
    exam.sdls.forEach(sdl => {
      SDL_INDEX.set(sdl.sdlNumber, { sdl, examNumber: exam.examNumber });
    });
  });
  render();
} catch (err) {
  main.innerHTML = `<p class="empty-state">Could not load question bank: ${escapeHtml(err.message)}</p>`;
}
