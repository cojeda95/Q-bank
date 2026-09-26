'use strict';
/* Board-prep Question Bank — vanilla JS app, shared across all blocks. No frameworks, no build step. */

/* ── Global state ─────────────────────────────────────────────────────── */
let DATA = null;               // parsed data.json
let SDL_INDEX = new Map();     // sdlNumber -> {sdl, examNumber}
let session = null;            // active quiz/exam session object
const main = document.getElementById('main');
const homeBtn = document.getElementById('homeBtn');

// Per-block config, set by a small inline <script> in each block's index.html
// BEFORE data.js/app.js load. Falls back to the original Neuro Block keys so
// existing localStorage progress is never lost if a page forgets to set it.
const QUIZ_CONFIG = window.QUIZ_CONFIG || { title: 'Neuro Block Question Bank', storageKey: 'neuro' };
const LS_FLAGS = QUIZ_CONFIG.storageKey + '_flags_v1';
const LS_PROGRESS = QUIZ_CONFIG.storageKey + '_progress_v1';
const LS_ATTEMPTS = QUIZ_CONFIG.storageKey + '_attempts_v1';
const LS_SETTINGS = QUIZ_CONFIG.storageKey + '_settings_v1';
const LS_EXAM_SESSION = QUIZ_CONFIG.storageKey + '_examsession_v1';
const LS_PRACTICE_SESSION = QUIZ_CONFIG.storageKey + '_practicesession_v1';
// Site-wide, not per block: turning the wrong-answer flash off in one block
// turns it off everywhere.
const LS_WRONG_FLASH = 'qbank_wrongflash_v1';
const MAX_ATTEMPTS_STORED = 5000;

/* ── Lesion Atlas links ─────────────────────────────────────────────────
   resources/atlas-terms.js (written by tools/build-atlas.py) lists every atlas
   card with its name and curated match terms, already normalized by the same
   rules as atlasNorm() below — keep the two in step. Once a question is
   answered, a card is linked when one of its terms appears as a whole phrase in
   the correct answer or the first sentence of the explanation — the part that
   explains the answer. Later sentences and the board-prep note were tested and
   left out: they mostly discuss the wrong choices and differentials, and linked
   the wrong cards. The file loads lazily; if it is missing, questions simply
   show no atlas links. */
const APP_SRC = (document.currentScript && document.currentScript.src) || '';
const ATLAS_URL = APP_SRC ? new URL('../resources/metabolic-atlas.html', APP_SRC).href : '';
let ATLAS_INDEX = null;
(function loadAtlasTerms() {
  if (!APP_SRC) return;
  const s = document.createElement('script');
  s.src = new URL('../resources/atlas-terms.js', APP_SRC).href;
  s.async = true;
  s.onload = () => {
    const d = window.ATLAS_TERMS;
    if (d && Array.isArray(d.cards)) ATLAS_INDEX = d.cards.map(([id, n, k, t]) => ({ id, n, k, t }));
  };
  document.head.appendChild(s);
})();
const ATLAS_GREEK = { 'α': ' alpha ', 'β': ' beta ', 'γ': ' gamma ', 'δ': ' delta ', 'κ': ' kappa ', 'ε': ' epsilon ', 'μ': ' mu ' };
const ATLAS_DIGITS = { '₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9',
  '⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9','⁺':'+','⁻':'-' };
function atlasNorm(t) {
  return String(t || '').toLowerCase()
    .replace(/[αβγδκεμ]/g, c => ATLAS_GREEK[c])
    .replace(/[₀-₉⁰¹²³⁴-⁹⁺⁻]/g, c => ATLAS_DIGITS[c] || c)
    .replace(/<[^>]+>/g, ' ')
    .replace(/['’‘`]/g, '')
    .replace(/[‐‑‒–—―\-\/]/g, ' ')
    .replace(/[^a-z0-9+ ]/g, ' ')
    .replace(/\s+/g, ' ').trim();
}
function atlasLinksFor(q) {
  if (!ATLAS_INDEX || !q) return [];
  const lead = (String(q.explanation || '').match(/[^.!?]+[.!?]+/g) || [q.explanation || ''])[0];
  const zones = [q.choices && q.choices[q.correct], lead];
  const found = new Map();
  zones.forEach((z, zone) => {
    if (!z) return;
    const text = ' ' + atlasNorm(z) + ' ';
    for (const c of ATLAS_INDEX) {
      if (found.has(c.id)) continue;
      const hit = c.t.find(t => text.includes(' ' + t + ' ') || text.includes(' ' + t + 's ') || text.includes(' ' + t + 'es '));
      if (hit) found.set(c.id, { c, zone, len: hit.length });
    }
  });
  return [...found.values()].sort((a, b) => a.zone - b.zone || b.len - a.len).slice(0, 3).map(x => x.c);
}
function atlasLinksHtml(q) {
  const cards = atlasLinksFor(q);
  if (!cards.length || !ATLAS_URL) return '';
  return `<div class="info-block atlas"><b>On the Lesion Atlas</b>${cards.map(c =>
    `<a class="atlas-link k-${c.k}" href="${ATLAS_URL}#${encodeURIComponent(c.id)}" target="_blank" rel="noopener"><span class="dot"></span>${escapeHtml(c.n)}</a>`).join('')}</div>`;
}

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
  const date = new Date().toISOString();
  entry.last = { correct, total, date };
  if (!entry.best || correct / total > entry.best.correct / entry.best.total) {
    entry.best = { correct, total };
  }
  // Capped run history — powers the Score Trend chart in Analytics. Only
  // exam-simulation scores are recorded here (this is the only caller of
  // recordScore), so this never touches per-question attempt data.
  entry.history = (entry.history || []).concat([{ correct, total, date }]).slice(-20);
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
  const defaults = { hyOnly: false, examInstantFeedback: false };
  try { return Object.assign({}, defaults, JSON.parse(localStorage.getItem(LS_SETTINGS)) || {}); }
  catch (e) { return Object.assign({}, defaults); }
}
function saveSettings(s) {
  localStorage.setItem(LS_SETTINGS, JSON.stringify(s));
}
// On unless the user has switched it off.
function wrongFlashEnabled() {
  try { return localStorage.getItem(LS_WRONG_FLASH) !== 'off'; }
  catch (e) { return true; }
}
function setWrongFlashEnabled(on) {
  try { localStorage.setItem(LS_WRONG_FLASH, on ? 'on' : 'off'); }
  catch (e) { /* non-fatal */ }
}

/* ── In-progress exam session snapshot (powers "Resume" on the home screen) ─
   Saved on every question transition/answer while an exam simulation is in
   progress, so a closed tab, accidental navigation, or refresh doesn't lose
   the run. Cleared as soon as the exam is submitted (or time runs out). */
function saveExamSessionSnapshot() {
  if (!session || session.mode !== 'exam' || session.submitted) return;
  try {
    localStorage.setItem(LS_EXAM_SESSION, JSON.stringify({
      examNumber: session.examNumber,
      isFinal: !!session.isFinal,
      presetId: session.presetId || null,
      timed: session.timed,
      totalSeconds: session.totalSeconds,
      deadlineAt: session.deadlineAt || null,
      questions: session.questions,
      index: session.index,
      answers: session.answers,
      timeSpentMs: session.timeSpentMs || [],
      savedAt: Date.now(),
    }));
  } catch (e) { /* storage full/blocked — resume just won't be offered */ }
}
function loadExamSessionSnapshot() {
  try { return JSON.parse(localStorage.getItem(LS_EXAM_SESSION)); }
  catch (e) { return null; }
}
function clearExamSessionSnapshot() {
  localStorage.removeItem(LS_EXAM_SESSION);
}

/* ── In-progress PRACTICE session snapshot (mirrors the exam one above) ──
   Solves the exact complaint that motivated this: an accidental refresh (or
   closed tab) mid-SDL used to lose all progress, forcing a full restart of
   the batch. Saved on every question render while a practice run is active,
   keyed by sdlNumber+scoreKey (so only one in-progress practice run is
   tracked at a time, same single-slot model as the exam snapshot). Cleared
   as soon as the batch is finished (Finish button) or explicitly discarded. */
function savePracticeSessionSnapshot() {
  if (!session || session.mode !== 'practice') return;
  try {
    localStorage.setItem(LS_PRACTICE_SESSION, JSON.stringify({
      sdlNumber: session.sdlNumber,
      examNumber: session.examNumber,
      scoreKey: session.scoreKey,
      isBloom: session.isBloom,
      questions: session.questions,
      index: session.index,
      records: session.records,
      struck: session.struck || {},
      savedAt: Date.now(),
    }));
  } catch (e) { /* storage full/blocked — resume just won't be offered */ }
}
function loadPracticeSessionSnapshot() {
  try { return JSON.parse(localStorage.getItem(LS_PRACTICE_SESSION)); }
  catch (e) { return null; }
}
function clearPracticeSessionSnapshot() {
  localStorage.removeItem(LS_PRACTICE_SESSION);
}
// Maps a practice scoreKey (`sdl-N`, `sdl-N-b1`, `sdl-N-b2`, `sdl-N-b3`) back
// to the batch URL segment used to reach it via #practice/<sdl>/<batch> —
// the same derivation the Retry button already used inline; pulled out here
// so the new home-screen resume card can reuse it too.
function batchParamFromScoreKey(scoreKey) {
  return scoreKey.includes('-b') ? scoreKey.slice(-1) : 'all';
}
// Returns an SDL's questions filtered to high-yield-only if that mode is on.
function visibleQuestions(sdl) {
  const s = loadSettings();
  return s.hyOnly ? sdl.questions.filter(q => q.isHighYield) : sdl.questions;
}

/* ── Wrong-answer flash ───────────────────────────────────────────────── */
// A translucent-red screen wash plus an iMessage "Echo"-style burst: many copies
// of BOTH meme images launch from the centre in staggered waves, scatter across
// the viewport at random angles, sizes and rotations, then fade. Fires once per
// incorrect submission across every quiz mode (Practice, Flagged Review,
// Toughest-Questions Review, Exam Simulation with Instant Feedback on).
// Purely decorative — appended to <body> (not #main) so it survives the
// immediate innerHTML re-render that reveals the answer, pointer-events:none so
// it never blocks input, and it removes itself when the animation finishes.
const WRONG_FLASH_IMAGES = ['../shared/images/wrong-flash-1.png', '../shared/images/wrong-flash-2.png'];
const WRONG_FLASH_MS = 3000;     // total on-screen time
const ECHO_WAVES = 5;            // Echo arrives in bursts, not one even spray
const ECHO_PER_WAVE = 11;

// Warm the cache so the first wrong answer of a session is not the one that
// misses its own animation window.
(function preloadWrongFlash() {
  try { WRONG_FLASH_IMAGES.forEach(src => { const i = new Image(); i.src = src; }); }
  catch (e) { /* non-fatal */ }
})();

function triggerWrongFlash() {
  if (!wrongFlashEnabled()) return;
  const overlay = document.createElement('div');
  overlay.className = 'wrong-flash-overlay';

  const wash = document.createElement('div');
  wash.className = 'wrong-flash-wash';
  overlay.appendChild(wash);

  // Honour a reduced-motion preference: keep the wash, skip the swarm.
  let reduced = false;
  try { reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

  if (!reduced) {
    const vw = window.innerWidth, vh = window.innerHeight;
    const reach = Math.hypot(vw, vh) / 2;
    const total = ECHO_WAVES * ECHO_PER_WAVE;
    for (let i = 0; i < total; i++) {
      const wave = Math.floor(i / ECHO_PER_WAVE);
      const img = document.createElement('img');
      img.className = 'wrong-flash-echo';
      img.src = WRONG_FLASH_IMAGES[i % WRONG_FLASH_IMAGES.length];   // alternate, so both appear
      img.alt = '';
      img.decoding = 'async';
      const angle = Math.random() * Math.PI * 2;
      const dist = reach * (0.18 + Math.random() * 0.92);
      const size = 64 + Math.random() * 104;
      img.style.setProperty('--dx', (Math.cos(angle) * dist).toFixed(0) + 'px');
      img.style.setProperty('--dy', (Math.sin(angle) * dist).toFixed(0) + 'px');
      img.style.setProperty('--rot', (Math.random() * 64 - 32).toFixed(1) + 'deg');
      img.style.setProperty('--sc', (0.72 + Math.random() * 0.55).toFixed(2));
      img.style.setProperty('--size', size.toFixed(0) + 'px');
      img.style.setProperty('--delay', (wave * 0.34 + Math.random() * 0.2).toFixed(2) + 's');
      img.style.setProperty('--dur', (1.25 + Math.random() * 0.55).toFixed(2) + 's');
      overlay.appendChild(img);
    }
  }

  document.body.appendChild(overlay);
  setTimeout(() => overlay.remove(), WRONG_FLASH_MS + 250);
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

// Pools every question from every exam block BEFORE examNumber — not just the single
// immediately-preceding exam. Real exam structure carries "prior weeks" content forward
// from any earlier week, not specifically the last exam's content, so the Custom Exam
// Builder's 30% "prior" bucket must be able to draw from Exam 1, Exam 2, etc., all the way
// up to (but not including) the exam currently being built. Each returned question keeps
// track of which exam it actually came from via `_srcExam`, since a single "prior" bucket
// can now legitimately span multiple different source exams at once.
function allQuestionsForExamsBefore(examNumber) {
  let qs = [];
  DATA.exams.forEach(e => {
    if (e.examNumber < examNumber) {
      qs = qs.concat(allQuestionsForExam(e.examNumber).map(q => Object.assign({}, q, { _srcExam: e.examNumber })));
    }
  });
  return qs;
}

function formatTime(seconds) {
  seconds = Math.max(0, Math.round(seconds));
  const m = Math.floor(seconds / 60);
  const s = seconds % 60;
  return `${m}:${String(s).padStart(2, '0')}`;
}

function findQuestionById(id) {
  for (const exam of DATA.exams) {
    for (const sdl of exam.sdls) {
      for (const q of sdl.questions) {
        if (q.id === id) return Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: exam.examNumber });
      }
    }
  }
  return null;
}

// Tiny dependency-free sparkline — just enough to show a score trend inline.
function sparklineSvg(values, width, height) {
  width = width || 130; height = height || 30;
  if (values.length < 2) return '';
  const stepX = width / (values.length - 1);
  const y = (v) => height - (Math.max(0, Math.min(100, v)) / 100) * height;
  const points = values.map((v, i) => `${(i * stepX).toFixed(1)},${y(v).toFixed(1)}`).join(' ');
  const lastX = ((values.length - 1) * stepX).toFixed(1);
  const lastY = y(values[values.length - 1]).toFixed(1);
  return `<svg width="${width}" height="${height}" viewBox="0 0 ${width} ${height}" style="display:block; overflow:visible;">
    <polyline points="${points}" fill="none" stroke="var(--navy)" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
    <circle cx="${lastX}" cy="${lastY}" r="3" fill="var(--navy)"/>
  </svg>`;
}

/* ── Router ───────────────────────────────────────────────────────────── */
function setRoute(hash) {
  window.location.hash = hash;
}

window.addEventListener('hashchange', render);

function render() {
  // Guard: leaving an active timed exam mid-way just abandons the timer.
  if (session && session.timerId && !window.location.hash.startsWith('#exam/') && !window.location.hash.startsWith('#resume-exam')) {
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
    // A trailing /new segment (used by the Retry/Choose-Different-Batch
    // buttons) forces a fresh session even if a matching in-progress
    // snapshot exists — otherwise Retry would just resume the old one.
    renderPracticeStart(parseInt(parts[1], 10), parts[2], parts[3] === 'new');
  } else if (parts[0] === 'examsetup' && parts[1]) {
    renderExamSetup(parseInt(parts[1], 10));
  } else if (parts[0] === 'final-examsetup') {
    renderFinalExamSetup();
  } else if (parts[0] === 'resume-exam') {
    resumeExamSession();
  } else if (parts[0] === 'exam' && parts[1]) {
    renderExamSimStart(parseInt(parts[1], 10));
  } else if (parts[0] === 'flagged') {
    renderFlaggedReview();
  } else if (parts[0] === 'review') {
    renderReviewQueue();
  } else if (parts[0] === 'toughest') {
    renderToughestQueue();
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
        <div class="exam-label">${e.sdls.length} SDLs · ${qCount ? `${qCount} questions` : 'questions coming soon'}</div>
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

  // A block can be published as a skeleton (every SDL titled, no questions yet),
  // so the final needs questions in the last exam, not just more than one exam.
  const showFinalExamCard = DATA.exams.length > 1 && allQuestionsForExam(lastExamNumber()).length > 0;

  const resumeSnap = loadExamSessionSnapshot();
  const resumeHtml = resumeSnap ? `
    <div class="action-card" id="resumeExamCard" style="border-color: var(--navy); border-width: 2px;">
      <span class="icon">▶️</span>
      <div>
        <div class="sdl-title">Resume In-Progress Exam</div>
        <div class="action-label">${escapeHtml(examSessionLabel(resumeSnap))} — question ${resumeSnap.index + 1} of ${resumeSnap.questions.length}, ${resumeSnap.answers.filter(a => a !== null).length} answered${resumeSnap.timed ? (resumeSnap.deadlineAt - Date.now() <= 0 ? ' · time expired' : ` · ${formatTime((resumeSnap.deadlineAt - Date.now()) / 1000)} left`) : ' · untimed'}
          <button class="link-btn-inline" id="discardResumeBtn" style="margin-left:8px; background:none; border:1px solid var(--grey-border, #ccc); border-radius:6px; padding:2px 8px; cursor:pointer; font-size:0.78rem;">Discard</button>
        </div>
      </div>
    </div>
  ` : '';

  // Same idea as the exam resume card above, but for an in-progress SDL
  // practice run — this is the direct fix for "I refresh by accident and
  // have to redo the whole SDL." A refresh alone doesn't even need this card
  // (the #practice/<sdl>/<batch> hash survives and auto-resumes on its own),
  // but this covers the closed-tab/came-back-later case, and gives an
  // explicit Discard so an abandoned run doesn't linger forever.
  const practiceSnap = loadPracticeSessionSnapshot();
  const practiceSdl = practiceSnap ? findSdl(practiceSnap.sdlNumber) : null;
  const practiceResumeHtml = (practiceSnap && practiceSdl) ? `
    <div class="action-card" id="resumePracticeCard" style="border-color: var(--navy); border-width: 2px;">
      <span class="icon">▶️</span>
      <div>
        <div class="sdl-title">Resume In-Progress Practice</div>
        <div class="action-label">${escapeHtml(practiceSdl.sdl.title)} — question ${practiceSnap.index + 1} of ${practiceSnap.questions.length}, ${(practiceSnap.records || []).filter(r => r).length} answered
          <button class="link-btn-inline" id="discardPracticeResumeBtn" style="margin-left:8px; background:none; border:1px solid var(--grey-border, #ccc); border-radius:6px; padding:2px 8px; cursor:pointer; font-size:0.78rem;">Discard</button>
        </div>
      </div>
    </div>
  ` : '';

  main.innerHTML = `
    <h1>${escapeHtml(QUIZ_CONFIG.title)}</h1>
    <p class="subtitle">Choose an exam block to practice by SDL or run a full timed simulation.${settings.hyOnly ? ' <strong>⚡ High-Yield Only Mode is ON.</strong>' : ''}</p>
    ${resumeHtml}
    ${practiceResumeHtml}
    <div class="exam-grid">${examCards}</div>

    ${showFinalExamCard ? `
    <div class="action-card" id="finalExamCard">
      <span class="icon">&#127937;</span>
      <div>
        <div class="sdl-title">Final Exam Simulation</div>
        <div class="action-label">Cumulative — 50% Exam ${lastExamNumber()}, 50% pooled from every earlier exam block</div>
      </div>
    </div>
    ${finalPresetCardsHtml(`timed at 1.5 min each${settings.examInstantFeedback ? ' · 📝 Instant Feedback is ON' : ''}`)}
    ` : ''}

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
    <label class="radio-option" style="cursor:pointer; margin-top:8px;">
      <input type="checkbox" id="instantFeedbackToggle" ${settings.examInstantFeedback ? 'checked' : ''}>
      <span>📝 Show Answers After Each Question (Exam Simulation) — reveal correct/incorrect + explanation right after you answer, same as Practice mode, instead of waiting until you submit the whole exam</span>
    </label>
    <label class="radio-option" style="cursor:pointer; margin-top:8px;">
      <input type="checkbox" id="wrongFlashToggle" ${wrongFlashEnabled() ? 'checked' : ''}>
      <span>💥 Wrong-Answer Flash — red screen flash and image burst when you miss a question (applies to every block)</span>
    </label>
  `;

  main.querySelectorAll('.exam-card').forEach(card => {
    card.addEventListener('click', () => setRoute(`exam-sdls/${card.dataset.exam}`));
  });
  const finalExamCard = document.getElementById('finalExamCard');
  if (finalExamCard) finalExamCard.addEventListener('click', () => setRoute('final-examsetup'));
  main.querySelectorAll('.final-preset-card').forEach(card => {
    card.addEventListener('click', () => {
      const preset = findFinalPreset(card.dataset.preset);
      if (preset) startFinalPreset(preset);
    });
  });
  const resumeExamCard = document.getElementById('resumeExamCard');
  if (resumeExamCard) resumeExamCard.addEventListener('click', () => setRoute('resume-exam'));
  const discardResumeBtn = document.getElementById('discardResumeBtn');
  if (discardResumeBtn) discardResumeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (confirm('Discard the in-progress exam? This cannot be undone.')) {
      clearExamSessionSnapshot();
      renderHome();
    }
  });
  const resumePracticeCard = document.getElementById('resumePracticeCard');
  if (resumePracticeCard) resumePracticeCard.addEventListener('click', () => {
    setRoute(`practice/${practiceSnap.sdlNumber}/${batchParamFromScoreKey(practiceSnap.scoreKey)}`);
  });
  const discardPracticeResumeBtn = document.getElementById('discardPracticeResumeBtn');
  if (discardPracticeResumeBtn) discardPracticeResumeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (confirm('Discard the in-progress practice run? This cannot be undone.')) {
      clearPracticeSessionSnapshot();
      renderHome();
    }
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
  document.getElementById('instantFeedbackToggle').addEventListener('change', (e) => {
    const s = loadSettings();
    s.examInstantFeedback = e.target.checked;
    saveSettings(s);
    renderHome();
  });
  document.getElementById('wrongFlashToggle').addEventListener('change', (e) => {
    setWrongFlashEnabled(e.target.checked);
  });
}

/* ── Per-exam SDL selection screen ───────────────────────────────────── */
// An SDL can be attempted several ways (Both Batches, Batch 1 only, Batch 2
// only, Bloom Batch) and each writes its score under a different key. The
// list view should count the SDL as attempted if ANY of those keys has a
// score, showing whichever was attempted most recently.
function scoreKeysForSdl(sdlNumber) {
  return [
    { key: `sdl-${sdlNumber}`, label: 'Both Batches' },
    { key: `sdl-${sdlNumber}-b1`, label: 'Batch 1' },
    { key: `sdl-${sdlNumber}-b2`, label: 'Batch 2' },
    { key: `sdl-${sdlNumber}-b3`, label: 'Bloom Batch' },
  ];
}
function bestScoreForSdl(sdlNumber) {
  const options = scoreKeysForSdl(sdlNumber)
    .map(o => ({ label: o.label, score: getScore(o.key) }))
    .filter(o => o.score);
  if (options.length === 0) return null;
  options.sort((a, b) => new Date(b.score.last.date) - new Date(a.score.last.date));
  return options[0];
}

function renderExamSdlList(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }

  const settings = loadSettings();
  const totalQ = exam.sdls.reduce((s, sdl) => s + visibleQuestions(sdl).filter(q => q.batch !== 3).length, 0);
  const estMinutes = Math.round(totalQ * 90 / 60);

  const rows = exam.sdls.map(sdl => {
    const best = bestScoreForSdl(sdl.sdlNumber);
    const visible = visibleQuestions(sdl);
    const regularCount = visible.filter(q => q.batch !== 3).length;
    const bloomCount = visible.filter(q => q.batch === 3).length;
    if (!sdl.questions.length) return `
      <div class="sdl-row pending">
        <div>
          <div class="sdl-title">${escapeHtml(sdl.title)}</div>
          <div class="sdl-meta">Questions coming soon</div>
        </div>
      </div>`;
    const scoreHtml = best
      ? `<div class="sdl-score">${escapeHtml(best.label)} — Last: ${best.score.last.correct}/${best.score.last.total}${best.score.best.correct === best.score.last.correct && best.score.best.total === best.score.last.total ? '' : ` · Best: ${best.score.best.correct}/${best.score.best.total}`}</div>`
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
    <p class="subtitle">${exam.sdls.length} SDLs · ${totalQ ? `${totalQ} total questions` : 'questions coming soon'}${settings.hyOnly ? ' · <strong>⚡ High-Yield Only Mode is ON</strong>' : ''}</p>
    ${totalQ ? `<div class="action-card" id="fullSimCard">
      <span class="icon">&#9201;</span>
      <div>
        <div class="sdl-title">Full Exam Simulation</div>
        <div class="action-label">All ${totalQ} questions, timed (~${estMinutes} min budget)${settings.examInstantFeedback ? ' · 📝 Instant Feedback is ON' : ', no immediate answer reveal'}</div>
      </div>
    </div>` : ''}
    <div class="section-label">Practice by SDL</div>
    <div class="sdl-list">${rows}</div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  const fullSimCard = document.getElementById('fullSimCard');
  if (fullSimCard) fullSimCard.addEventListener('click', () => setRoute(`examsetup/${examNumber}`));
  main.querySelectorAll('.sdl-row:not(.pending)').forEach(row => {
    row.addEventListener('click', () => setRoute(`practice/${row.dataset.sdl}`));
  });
}

/* ── Custom Exam Builder (weighted current/prior content + batch mix) ── */
function renderExamSetup(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }

  const priorPoolAll = examNumber > 1 ? allQuestionsForExamsBefore(examNumber) : [];
  const hasPrior = priorPoolAll.length > 0;
  const priorRangeLabel = examNumber > 2 ? `Exams 1–${examNumber - 1}` : `Exam 1`;

  const currentAllCount = allQuestionsForExam(examNumber).length;
  const priorAllCount = priorPoolAll.length;

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
          <span id="pctReadout" class="setup-readout">${defaultPct}% Exam ${examNumber} · ${100 - defaultPct}% ${priorRangeLabel}</span>
        </div>
        <input type="range" id="pctSlider" min="0" max="100" step="5" value="${defaultPct}">
        <div class="setup-hint">Real exam structure: ~70% this week's material (Exam ${examNumber}), ~30% carried over from prior weeks' content across ${priorRangeLabel}, not just the immediately-preceding exam. Drag to change the mix.</div>
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

      <div class="setup-row">
        <div class="setup-label-row"><label>Timer</label></div>
        <label class="radio-option" style="cursor:pointer;">
          <input type="checkbox" id="timerToggle" checked>
          <span>&#9201; Timed — default 1.5 min per question</span>
        </label>
        <div id="timerMinutesRow" style="margin-top:8px;">
          <div class="setup-label-row">
            <label for="minutesPerQInput">Minutes per question</label>
            <span id="timerReadout" class="setup-readout"></span>
          </div>
          <input type="number" id="minutesPerQInput" class="number-input" min="0.5" max="30" step="0.5" value="1.5">
        </div>
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
  const timerToggle = document.getElementById('timerToggle');
  const minutesPerQInput = document.getElementById('minutesPerQInput');
  const timerMinutesRow = document.getElementById('timerMinutesRow');
  const timerReadout = document.getElementById('timerReadout');

  function updateTimerReadout() {
    const timed = timerToggle.checked;
    timerMinutesRow.style.opacity = timed ? '1' : '0.45';
    minutesPerQInput.disabled = !timed;
    if (!timed) { timerReadout.textContent = 'No time limit'; return; }
    const total = Number(totalInput.value) || 0;
    const minutesPerQ = Number(minutesPerQInput.value) || 1.5;
    timerReadout.textContent = `~${Math.round(total * minutesPerQ)} min total`;
  }
  timerToggle.addEventListener('change', updateTimerReadout);
  minutesPerQInput.addEventListener('input', updateTimerReadout);
  totalInput.addEventListener('input', updateTimerReadout);
  updateTimerReadout();

  function currentSettings() {
    const pctCurrent = hasPrior && pctSlider ? Number(pctSlider.value) : 100;
    const batchMode = document.querySelector('input[name="batchMode"]:checked').value;
    const total = Number(totalInput.value);
    const timed = timerToggle.checked;
    const minutesPerQuestion = Number(minutesPerQInput.value) || 1.5;
    return { pctCurrent, batchMode, total, timed, minutesPerQuestion };
  }

  function poolSizes(batchMode) {
    const filterBatch = (qs) => batchMode === 'mix' ? qs : qs.filter(q => q.batch === Number(batchMode));
    const curPool = filterBatch(allQuestionsForExam(examNumber)).length;
    const priorPool = hasPrior ? filterBatch(allQuestionsForExamsBefore(examNumber)).length : 0;
    return { curPool, priorPool };
  }

  function updatePoolHint() {
    const { batchMode } = currentSettings();
    const { curPool, priorPool } = poolSizes(batchMode);
    poolHint.textContent = `Available with this batch filter: ${curPool} from Exam ${examNumber}${hasPrior ? `, ${priorPool} from ${priorRangeLabel}` : ''} (combined max ${curPool + priorPool}).`;
  }

  if (pctSlider) {
    pctSlider.addEventListener('input', () => {
      pctReadout.textContent = `${pctSlider.value}% Exam ${examNumber} · ${100 - pctSlider.value}% ${priorRangeLabel}`;
    });
  }
  document.querySelectorAll('input[name="batchMode"]').forEach(radio => {
    radio.addEventListener('change', updatePoolHint);
  });
  updatePoolHint();

  document.getElementById('startSetupBtn').addEventListener('click', () => {
    const { pctCurrent, batchMode, total, timed, minutesPerQuestion } = currentSettings();
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
    beginExamSession(examNumber, composed.questions, { timed, secondsPerQuestion: minutesPerQuestion * 60 });
  });
}

/* Randomly composes a question set for a custom exam simulation, blending
   current-exam content with prior-weeks content per the requested percentage,
   optionally restricted to a single batch. The "prior" pool spans every exam
   block before this one (Exam 1..examNumber-1), not just the exam immediately
   before it — real exam structure carries content forward from any earlier
   week, not specifically the last exam. */
function buildCustomExamQuestions(examNumber, { pctCurrent, batchMode, total, hasPrior }) {
  const filterBatch = (qs) => batchMode === 'mix' ? qs : qs.filter(q => q.batch === Number(batchMode));

  const currentPool = filterBatch(allQuestionsForExam(examNumber));
  const priorPool = hasPrior ? filterBatch(allQuestionsForExamsBefore(examNumber)) : [];

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
  // Prior pool now spans multiple exams — preserve each question's own originating exam
  // number (`_srcExam`, set by allQuestionsForExamsBefore) rather than forcing a single
  // prior exam number, so the results breakdown can show exactly where each question came
  // from even when the 30% is drawn from more than one earlier exam block.
  const priorChosen = shuffle(priorPool).slice(0, priorTake)
    .map(q => Object.assign({}, q, { sourceExamNumber: q._srcExam, sourceTag: 'prior' }));

  return { questions: shuffle(currentChosen.concat(priorChosen)) };
}

/* ── Final Exam mode (50/50 cumulative: last exam vs. everything before it) ──
   Reuses buildCustomExamQuestions/beginExamSession exactly like the per-exam
   Custom Exam Builder, just with the "current" exam fixed to the last exam
   block in the whole dataset (not whichever exam the user is browsing) and a
   50/50 default split instead of 70/30, matching the real final's cumulative
   structure: 50% from the most recent week's material, 50% from every week
   before it, not weighted toward "just the last exam" either. */
function lastExamNumber() {
  return Math.max(...DATA.exams.map(e => e.examNumber));
}

/* ── Final Exam presets (one click, configured per block) ──────────────────
   A block can publish its real final's announced distribution in
   QUIZ_CONFIG.finalPresets. `perSdl` maps an exam number to the [min, max]
   questions drawn from EACH of that exam's SDLs, e.g. { 1: [2, 3], 4: [5, 6] };
   every run picks a count inside the range per SDL, so repeated runs vary the
   way an "approximately 2-3 per SDL" exam does. Exams missing from perSdl
   contribute nothing, and blocks without presets see no change at all. */
function finalPresets() {
  const list = Array.isArray(QUIZ_CONFIG.finalPresets) ? QUIZ_CONFIG.finalPresets : [];
  return list.filter(p => p && p.id && p.name && p.perSdl && DATA.exams.some(e => presetRange(p, e.examNumber)));
}
function findFinalPreset(id) {
  return finalPresets().find(p => p.id === id) || null;
}
function presetRange(preset, examNumber) {
  const r = preset.perSdl[examNumber];
  if (!Array.isArray(r) || r.length !== 2 || !r.every(Number.isFinite)) return null;
  return [Math.max(0, Math.min(r[0], r[1])), Math.max(0, r[0], r[1])];
}
// e.g. "2–3 per SDL from Exams 1–2 · 1–2 per SDL from Exam 3 · 5–6 per SDL from Exam 4"
function presetSummary(preset) {
  const groups = [];
  DATA.exams.slice().sort((a, b) => a.examNumber - b.examNumber).forEach(e => {
    const r = presetRange(preset, e.examNumber);
    if (!r) return;
    const key = r[0] === r[1] ? `${r[0]}` : `${r[0]}–${r[1]}`;
    const last = groups[groups.length - 1];
    if (last && last.key === key && last.exams[last.exams.length - 1] === e.examNumber - 1) last.exams.push(e.examNumber);
    else groups.push({ key, exams: [e.examNumber] });
  });
  return groups.map(g => `${g.key} per SDL from ${g.exams.length > 1 ? `Exams ${g.exams[0]}–${g.exams[g.exams.length - 1]}` : `Exam ${g.exams[0]}`}`).join(' · ');
}
// [fewest, most] questions a run can hold, capped by what each SDL actually has
// under the current filters (High-Yield Only Mode can shrink an SDL's pool).
function presetCountRange(preset) {
  let lo = 0, hi = 0;
  DATA.exams.forEach(e => {
    const r = presetRange(preset, e.examNumber);
    if (!r) return;
    const pool = allQuestionsForExam(e.examNumber);
    e.sdls.forEach(sdl => {
      const n = pool.filter(q => q.sdlNumber === sdl.sdlNumber).length;
      lo += Math.min(r[0], n);
      hi += Math.min(r[1], n);
    });
  });
  return [lo, hi];
}
function buildPresetExamQuestions(preset) {
  const finalExam = lastExamNumber();
  let chosen = [];
  DATA.exams.forEach(e => {
    const r = presetRange(preset, e.examNumber);
    if (!r) return;
    const pool = allQuestionsForExam(e.examNumber);
    e.sdls.forEach(sdl => {
      const want = r[0] + Math.floor(Math.random() * (r[1] - r[0] + 1));
      const picked = shuffle(pool.filter(q => q.sdlNumber === sdl.sdlNumber)).slice(0, want);
      chosen = chosen.concat(picked.map(q => Object.assign({}, q, {
        sourceExamNumber: e.examNumber,
        sourceTag: e.examNumber === finalExam ? 'current' : 'prior',
      })));
    });
  });
  return shuffle(chosen);
}
function startFinalPreset(preset, { timed = true, secondsPerQuestion = 90 } = {}) {
  if (loadExamSessionSnapshot() && !confirm('Start a new exam? The exam you have in progress will be discarded.')) return;
  const questions = buildPresetExamQuestions(preset);
  if (questions.length === 0) {
    alert(`No questions match ${preset.name} with the current settings.`);
    return;
  }
  beginExamSession(lastExamNumber(), questions, { isFinal: true, presetId: preset.id, timed, secondsPerQuestion });
}
// Title for an exam session or a saved snapshot of one.
function examSessionLabel(s) {
  const preset = s.presetId ? findFinalPreset(s.presetId) : null;
  if (s.presetId) return `Final Exam — ${preset ? preset.name : 'Preset'}`;
  return s.isFinal ? 'Final Exam Simulation' : `Exam ${s.examNumber} Simulation`;
}
function examScoreKey(s) {
  if (s.presetId) return `final-preset-${s.presetId}`;
  return s.isFinal ? 'final-exam' : `exam-${s.examNumber}`;
}
function finalPresetCardsHtml(note) {
  return finalPresets().map(p => {
    const [lo, hi] = presetCountRange(p);
    return `
    <div class="action-card final-preset-card" data-preset="${escapeHtml(p.id)}"${p.source ? ` title="${escapeHtml(p.source)}"` : ''}>
      <span class="icon">&#128203;</span>
      <div>
        <div class="sdl-title">${escapeHtml(p.name)}</div>
        <div class="action-label">One click: ${escapeHtml(presetSummary(p))} · ${lo === hi ? lo : `${lo}–${hi}`} questions, ${note}</div>
      </div>
    </div>`;
  }).join('');
}

function renderFinalExamSetup() {
  const examNumber = lastExamNumber();
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) { renderHome(); return; }

  const priorPoolAll = allQuestionsForExamsBefore(examNumber);
  const hasPrior = priorPoolAll.length > 0;
  const priorRangeLabel = examNumber > 2 ? `Exams 1–${examNumber - 1}` : `Exam 1`;

  const currentAllCount = allQuestionsForExam(examNumber).length;
  const priorAllCount = priorPoolAll.length;

  const defaultPct = 50;
  const defaultBatch = 'mix';
  const defaultTotal = currentAllCount + priorAllCount;

  if (!hasPrior) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Final Exam Simulation</h1>
      <p class="empty-state">Final Exam mode needs at least two exam blocks — only Exam ${examNumber} exists so far. Come back once an earlier exam's content is available to blend in.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <h1>Final Exam Simulation</h1>
    <p class="subtitle">Cumulative structure: ~50% Exam ${examNumber} (the most recent week's material), ~50% pooled from every week before it (${priorRangeLabel}) — not weighted toward just the last exam.</p>
    ${finalPresets().length ? `
    <div class="section-label">One-Click Presets</div>
    ${finalPresetCardsHtml('using the timer setting below')}
    <div class="section-label">Custom Mix</div>` : ''}
    <div class="setup-card">

      <div class="setup-row">
        <div class="setup-label-row">
          <label for="pctSlider">Content Source</label>
          <span id="pctReadout" class="setup-readout">${defaultPct}% Exam ${examNumber} · ${100 - defaultPct}% ${priorRangeLabel}</span>
        </div>
        <input type="range" id="pctSlider" min="0" max="100" step="5" value="${defaultPct}">
        <div class="setup-hint">Real final exam structure: ~50% the most recent week (Exam ${examNumber}), ~50% carried over from any earlier week across ${priorRangeLabel}. Drag to change the mix.</div>
      </div>

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

      <div class="setup-row">
        <div class="setup-label-row"><label>Timer</label></div>
        <label class="radio-option" style="cursor:pointer;">
          <input type="checkbox" id="timerToggle" checked>
          <span>&#9201; Timed — default 1.5 min per question</span>
        </label>
        <div id="timerMinutesRow" style="margin-top:8px;">
          <div class="setup-label-row">
            <label for="minutesPerQInput">Minutes per question</label>
            <span id="timerReadout" class="setup-readout"></span>
          </div>
          <input type="number" id="minutesPerQInput" class="number-input" min="0.5" max="30" step="0.5" value="1.5">
        </div>
      </div>

      <button class="btn" id="startSetupBtn" style="width:100%; margin-top:10px;">Start Final Exam Simulation</button>
    </div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));

  const pctSlider = document.getElementById('pctSlider');
  const pctReadout = document.getElementById('pctReadout');
  const totalInput = document.getElementById('totalInput');
  const poolHint = document.getElementById('poolHint');
  const totalError = document.getElementById('totalError');
  const timerToggle = document.getElementById('timerToggle');
  const minutesPerQInput = document.getElementById('minutesPerQInput');
  const timerMinutesRow = document.getElementById('timerMinutesRow');
  const timerReadout = document.getElementById('timerReadout');

  function updateTimerReadout() {
    const timed = timerToggle.checked;
    timerMinutesRow.style.opacity = timed ? '1' : '0.45';
    minutesPerQInput.disabled = !timed;
    if (!timed) { timerReadout.textContent = 'No time limit'; return; }
    const total = Number(totalInput.value) || 0;
    const minutesPerQ = Number(minutesPerQInput.value) || 1.5;
    timerReadout.textContent = `~${Math.round(total * minutesPerQ)} min total`;
  }
  timerToggle.addEventListener('change', updateTimerReadout);
  minutesPerQInput.addEventListener('input', updateTimerReadout);
  totalInput.addEventListener('input', updateTimerReadout);
  updateTimerReadout();

  function currentSettings() {
    const pctCurrent = Number(pctSlider.value);
    const batchMode = document.querySelector('input[name="batchMode"]:checked').value;
    const total = Number(totalInput.value);
    const timed = timerToggle.checked;
    const minutesPerQuestion = Number(minutesPerQInput.value) || 1.5;
    return { pctCurrent, batchMode, total, timed, minutesPerQuestion };
  }

  function poolSizes(batchMode) {
    const filterBatch = (qs) => batchMode === 'mix' ? qs : qs.filter(q => q.batch === Number(batchMode));
    const curPool = filterBatch(allQuestionsForExam(examNumber)).length;
    const priorPool = filterBatch(allQuestionsForExamsBefore(examNumber)).length;
    return { curPool, priorPool };
  }

  function updatePoolHint() {
    const { batchMode } = currentSettings();
    const { curPool, priorPool } = poolSizes(batchMode);
    poolHint.textContent = `Available with this batch filter: ${curPool} from Exam ${examNumber}, ${priorPool} from ${priorRangeLabel} (combined max ${curPool + priorPool}).`;
  }

  pctSlider.addEventListener('input', () => {
    pctReadout.textContent = `${pctSlider.value}% Exam ${examNumber} · ${100 - pctSlider.value}% ${priorRangeLabel}`;
  });
  main.querySelectorAll('.final-preset-card').forEach(card => {
    card.addEventListener('click', () => {
      const preset = findFinalPreset(card.dataset.preset);
      if (!preset) return;
      const { timed, minutesPerQuestion } = currentSettings();
      startFinalPreset(preset, { timed, secondsPerQuestion: minutesPerQuestion * 60 });
    });
  });
  document.querySelectorAll('input[name="batchMode"]').forEach(radio => {
    radio.addEventListener('change', updatePoolHint);
  });
  updatePoolHint();

  document.getElementById('startSetupBtn').addEventListener('click', () => {
    const { pctCurrent, batchMode, total, timed, minutesPerQuestion } = currentSettings();
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
    beginExamSession(examNumber, composed.questions, { isFinal: true, timed, secondsPerQuestion: minutesPerQuestion * 60 });
  });
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
function renderPracticeStart(sdlNumber, batch, forceNew) {
  const found = findSdl(sdlNumber);
  if (!found) { renderHome(); return; }
  const { sdl, examNumber } = found;

  // Resume path: if there's an in-progress snapshot for this exact SDL+batch
  // (saved on every question render — see savePracticeSessionSnapshot),
  // rebuild the session from it instead of starting over. This is what makes
  // an accidental refresh (or closed tab, or clicking away and back) land
  // right back where you left off rather than restarting the batch — the
  // hash for this route already encodes sdlNumber+batch, so a refresh just
  // re-runs this same function with the same params. `forceNew` (set by the
  // Retry / Choose Different Batch buttons via a trailing /new) skips this
  // and always starts fresh.
  if (!forceNew) {
    const snap = loadPracticeSessionSnapshot();
    if (snap && snap.sdlNumber === sdlNumber && batchParamFromScoreKey(snap.scoreKey) === batch
        && Array.isArray(snap.questions) && snap.questions.length > 0) {
      session = {
        mode: 'practice',
        sdlNumber: snap.sdlNumber,
        examNumber: snap.examNumber,
        scoreKey: snap.scoreKey,
        isBloom: !!snap.isBloom,
        questions: snap.questions,
        index: Math.min(snap.index || 0, snap.questions.length - 1),
        records: Array.isArray(snap.records) && snap.records.length === snap.questions.length
          ? snap.records
          : new Array(snap.questions.length).fill(null),
        struck: snap.struck || {},
        pendingLetter: null,
      };
      renderPracticeQuestion();
      return;
    }
    // No matching snapshot for this SDL+batch — if a DIFFERENT one is
    // sitting around (e.g. the last thing you had open before navigating
    // here fresh), it's now orphaned, so clear it rather than let it
    // silently resurface the wrong batch later.
    if (snap) clearPracticeSessionSnapshot();
  }

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
      <p class="empty-state">${sdl.questions.length ? 'No questions match the current filters (High-Yield Only Mode is likely on). Turn it off on the Home screen, or pick a different batch.' : 'Questions for this SDL are coming soon.'}</p>
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
    records: new Array(questions.length).fill(null), // {letter, confidence, correct} once answered, per question
    struck: {},
    pendingLetter: null, // letter chosen but not yet confirmed with a confidence rating (current question only)
  };
  renderPracticeQuestion();
}

function renderPracticeQuestion() {
  savePracticeSessionSnapshot();
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const record = session.records[session.index];
  const answered = !!record;
  if (!session.struck) session.struck = {};
  const struckArr = session.struck[session.index] || [];

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    const isStruck = struckArr.includes(letter);
    if (isStruck && !answered) cls += ' struck';
    if (answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === record.letter) cls += ' incorrect';
    } else if (session.pendingLetter === letter) {
      cls += ' selected';
    }
    const strikeBtn = !answered ? `<button class="strike-btn ${isStruck ? 'active' : ''}" data-strike-letter="${letter}" title="Cross out this choice" aria-label="Cross out choice ${letter}">🚫</button>` : '';
    return `<div class="choice-row">
      <button class="${cls}" data-letter="${letter}" ${answered ? 'disabled' : ''}>
        <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
      </button>${strikeBtn}
    </div>`;
  }).join('');

  let confidenceHtml = '';
  if (!answered && session.pendingLetter) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer? <span style="font-weight:400; color:var(--grey-text);">(tap a different choice to change it)</span></div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (answered) {
    feedbackHtml = `
      <div class="feedback-banner ${record.correct ? 'correct' : 'incorrect'}">
        ${record.correct ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${q.crossRef ? `<div class="info-block xref">${escapeHtml(q.crossRef)}</div>` : ''}
      ${atlasLinksHtml(q)}
    `;
  }

  const answeredSoFar = session.records.filter(r => r).length;
  const correctSoFar = session.records.filter(r => r && r.correct).length;

  main.innerHTML = `
    <button class="back-link" id="backExam">&larr; Exam ${session.examNumber}</button>
    ${session.isBloom ? '<div class="bloom-banner">🧠 Bloom Batch — Level 3/4 Trial (experimental, board-qbank style)</div>' : ''}
    <div class="quiz-header">
      <span class="quiz-progress">Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${correctSoFar}/${answeredSoFar}</span>
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
      <div class="next-row" style="justify-content: space-between;">
        <button class="btn secondary" id="prevBtn" ${session.index === 0 ? 'disabled' : ''}>&larr; Previous</button>
        ${answered ? `<button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button>` : '<span></span>'}
      </div>
    </div>
  `;

  document.getElementById('backExam').addEventListener('click', () => setRoute(`exam-sdls/${session.examNumber}`));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderPracticeQuestion();
  });
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (session.index > 0) {
      session.index--;
      session.pendingLetter = null;
      renderPracticeQuestion();
    }
  });

  function finalizeAnswer(confidence) {
    const letter = session.pendingLetter;
    const correct = letter === q.correct;
    session.records[session.index] = { letter, confidence, correct };
    session.pendingLetter = null;
    if (!correct) triggerWrongFlash();
    logAttempt({
      id: q.id, sdlNumber: session.sdlNumber, sdlTitle: findSdl(session.sdlNumber).sdl.title,
      examNumber: session.examNumber, objective: q.objective, objectiveLabel: q.objectiveLabel,
      batch: q.batch, correct, confidence, mode: 'practice', ts: Date.now(),
    });
    renderPracticeQuestion();
  }

  if (!answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderPracticeQuestion();
      });
    });
    main.querySelectorAll('.strike-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const letter = btn.dataset.strikeLetter;
        const arr = session.struck[session.index] || [];
        const i = arr.indexOf(letter);
        if (i === -1) arr.push(letter); else arr.splice(i, 1);
        session.struck[session.index] = arr;
        renderPracticeQuestion();
      });
    });
    const confGuessed = document.getElementById('confGuessed');
    const confConfident = document.getElementById('confConfident');
    if (confGuessed) confGuessed.addEventListener('click', () => finalizeAnswer('guessed'));
    if (confConfident) confConfident.addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.pendingLetter = null;
          renderPracticeQuestion();
        } else {
          recordScore(session.scoreKey, correctSoFar, total);
          clearPracticeSessionSnapshot();
          renderPracticeComplete();
        }
      });
    }
  }
}

function renderPracticeComplete() {
  const total = session.questions.length;
  const correctCount = session.records.filter(r => r && r.correct).length;
  const pct = Math.round((correctCount / total) * 100);
  main.innerHTML = `
    <div class="result-summary">
      <div class="big-pct">${pct}%</div>
      <div class="sub">${correctCount} / ${total} correct</div>
    </div>
    <div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap;">
      <button class="btn secondary" id="retryBtn">Retry This Batch</button>
      <button class="btn secondary" id="backBatchBtn">Choose Different Batch</button>
      <button class="btn" id="doneBtn">Back to Exam ${session.examNumber}</button>
    </div>
  `;
  document.getElementById('retryBtn').addEventListener('click', () => setRoute(`practice/${session.sdlNumber}/${batchParamFromScoreKey(session.scoreKey)}/new`));
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

/* Shared by the default (100% current exam), Custom Exam Builder's
   weighted/batch-filtered simulations, Final Exam mode and its one-click presets.
   `isFinal` and `presetId` just change labeling/back-navigation/score-key — the
   question composition itself is already handled by the caller
   (buildCustomExamQuestions or buildPresetExamQuestions). */
function beginExamSession(examNumber, questions, { isFinal, presetId = null, timed = true, secondsPerQuestion = 90 } = {}) {
  const totalSeconds = timed ? questions.length * secondsPerQuestion : null;
  const deadlineAt = timed ? Date.now() + totalSeconds * 1000 : null;

  session = {
    mode: 'exam',
    examNumber,
    isFinal: !!isFinal,
    presetId,
    questions,
    index: 0,
    answers: new Array(questions.length).fill(null), // letter chosen, or null
    timed,
    totalSeconds,
    deadlineAt,
    remainingSeconds: totalSeconds,
    timerId: null,
    submitted: false,
    timeSpentMs: new Array(questions.length).fill(0),
    questionShownAt: null,
  };

  if (timed) startExamTimer();

  // Reflect the active exam in the URL hash (without triggering the router,
  // since replaceState doesn't fire hashchange) so a page refresh mid-exam
  // lands back on the resume path instead of losing the run.
  history.replaceState(null, '', '#resume-exam');

  renderExamQuestion();
}

// Rebuilds `session` from a snapshot saved to localStorage by
// saveExamSessionSnapshot() — used both for the "Resume In-Progress Exam"
// home-screen card and for recovering after a page refresh (the URL hash
// stays on #resume-exam for the duration of any exam simulation).
function resumeExamSession() {
  const snap = loadExamSessionSnapshot();
  if (!snap || !Array.isArray(snap.questions) || snap.questions.length === 0) {
    clearExamSessionSnapshot();
    renderHome();
    return;
  }

  session = {
    mode: 'exam',
    examNumber: snap.examNumber,
    isFinal: !!snap.isFinal,
    presetId: snap.presetId || null,
    questions: snap.questions,
    index: Math.min(snap.index || 0, snap.questions.length - 1),
    answers: snap.answers,
    timed: snap.timed,
    totalSeconds: snap.totalSeconds,
    deadlineAt: snap.deadlineAt,
    remainingSeconds: snap.timed ? Math.max(0, Math.round((snap.deadlineAt - Date.now()) / 1000)) : null,
    timerId: null,
    submitted: false,
    timeSpentMs: Array.isArray(snap.timeSpentMs) && snap.timeSpentMs.length === snap.questions.length
      ? snap.timeSpentMs
      : new Array(snap.questions.length).fill(0),
    questionShownAt: null, // don't count any time the tab was closed/away
  };

  if (session.timed && session.remainingSeconds <= 0) {
    // Time ran out while the page was closed — score it as a time-expired submission.
    finishExamSim(true);
    return;
  }

  if (session.timed) startExamTimer();
  renderExamQuestion();
}

function startExamTimer() {
  session.timerId = setInterval(() => {
    session.remainingSeconds = Math.max(0, Math.round((session.deadlineAt - Date.now()) / 1000));
    if (session.remainingSeconds <= 0) {
      clearInterval(session.timerId);
      finishExamSim(true);
      return;
    }
    updateTimerDisplay();
  }, 1000);
}

function shuffleExamQuestions(qs) {
  // Keep deterministic order (by SDL/objective) is also fine, but a shuffle
  // gives a more realistic "exam" feel. Simple: keep as-is (grouped by SDL).
  return qs;
}

function updateTimerDisplay() {
  const el = document.getElementById('examTimer');
  if (!el) return;
  if (!session.timed) { el.textContent = 'Untimed'; el.classList.remove('low'); return; }
  el.textContent = formatTime(session.remainingSeconds);
  el.classList.toggle('low', session.remainingSeconds <= 60);
}

// Flushes elapsed viewing time for the CURRENT question into
// session.timeSpentMs before the index changes or the exam is submitted.
// Left un-flushed between calls so repeated re-renders of the same
// question (flagging it, picking an answer) don't reset the clock.
function flushQuestionTime() {
  if (!session.timeSpentMs) session.timeSpentMs = new Array(session.questions.length).fill(0);
  if (session.questionShownAt) {
    session.timeSpentMs[session.index] = (session.timeSpentMs[session.index] || 0) + (Date.now() - session.questionShownAt);
    session.questionShownAt = null;
  }
}

function renderExamQuestion() {
  if (!session.questionShownAt) session.questionShownAt = Date.now();
  saveExamSessionSnapshot();
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const selected = session.answers[session.index];
  const instantFeedback = loadSettings().examInstantFeedback;
  const locked = instantFeedback && !!selected; // answer revealed, choice no longer changeable
  if (!session.struck) session.struck = {};
  const struckArr = session.struck[session.index] || [];

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    const isStruck = struckArr.includes(letter);
    if (isStruck && !locked) cls += ' struck';
    if (locked) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === selected) cls += ' incorrect';
    } else if (selected === letter) {
      cls += ' selected';
    }
    const strikeBtn = !locked ? `<button class="strike-btn ${isStruck ? 'active' : ''}" data-strike-letter="${letter}" title="Cross out this choice" aria-label="Cross out choice ${letter}">🚫</button>` : '';
    return `<div class="choice-row">
      <button class="${cls}" data-letter="${letter}" ${locked ? 'disabled' : ''}>
        <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
      </button>${strikeBtn}
    </div>`;
  }).join('');

  let feedbackHtml = '';
  if (locked) {
    const isCorrect = selected === q.correct;
    feedbackHtml = `
      <div class="feedback-banner ${isCorrect ? 'correct' : 'incorrect'}">
        ${isCorrect ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${q.crossRef ? `<div class="info-block xref">${escapeHtml(q.crossRef)}</div>` : ''}
      ${atlasLinksHtml(q)}
    `;
  }

  const answeredCount = session.answers.filter(a => a !== null).length;

  main.innerHTML = `
    <div class="quiz-header">
      <span class="quiz-progress">${escapeHtml(examSessionLabel(session))} — Question ${session.index + 1} of ${total}${instantFeedback ? ' · 📝 Instant Feedback' : ''}</span>
      <span id="examTimer" class="timer">${session.timed ? formatTime(session.remainingSeconds) : 'Untimed'}</span>
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
      ${feedbackHtml}
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
  if (!locked) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        const letter = btn.dataset.letter;
        session.answers[session.index] = letter;
        if (instantFeedback && letter !== q.correct) triggerWrongFlash();
        renderExamQuestion();
      });
    });
    main.querySelectorAll('.strike-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const letter = btn.dataset.strikeLetter;
        const arr = session.struck[session.index] || [];
        const i = arr.indexOf(letter);
        if (i === -1) arr.push(letter); else arr.splice(i, 1);
        session.struck[session.index] = arr;
        renderExamQuestion();
      });
    });
  }
  const prevBtn = document.getElementById('prevBtn');
  if (prevBtn) prevBtn.addEventListener('click', () => {
    if (session.index > 0) { flushQuestionTime(); session.index--; renderExamQuestion(); }
  });
  const nextBtn = document.getElementById('nextBtn');
  if (nextBtn) nextBtn.addEventListener('click', () => {
    if (session.index + 1 < total) { flushQuestionTime(); session.index++; renderExamQuestion(); }
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
  flushQuestionTime();
  if (session.timerId) clearInterval(session.timerId);
  session.submitted = true;
  session.timeExpired = timeExpired;
  clearExamSessionSnapshot();

  const total = session.questions.length;
  let correctCount = 0;
  const missed = [];
  const bySdl = {}; // sdlNumber -> {correct, total, title}
  const byObjective = {}; // "sdlNumber-objective" -> {correct, total, sdlNumber, objective}
  const timeSpentMs = session.timeSpentMs || new Array(total).fill(0);

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

  recordScore(examScoreKey(session), correctCount, total);

  // Log every question in this simulation to the attempts history (no confidence
  // rating is collected in timed exam mode — that's reserved for practice/review).
  // timeMs rides along here too, purely for this device's own Pacing summary below.
  session.questions.forEach((q, i) => {
    const ans = session.answers[i];
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle,
      examNumber: q.sourceExamNumber || session.examNumber, objective: q.objective, objectiveLabel: q.objectiveLabel,
      batch: q.batch, correct: ans === q.correct, confidence: null, mode: 'exam', ts: Date.now(),
      timeMs: timeSpentMs[i] || 0,
    });
  });

  // Keyed by the question's actual source exam number (not just 'current'/'prior'),
  // since the 30% "prior" bucket can now legitimately span multiple different earlier
  // exam blocks at once — collapsing them into one 'prior' row would hide which specific
  // earlier exam's content the student is weak on.
  const bySource = {}; // examNumber -> {correct, total, examNumber, tag}
  session.questions.forEach((q, i) => {
    if (!q.sourceTag) return;
    const isCorrect = session.answers[i] === q.correct;
    const key = q.sourceExamNumber;
    if (!bySource[key]) bySource[key] = { correct: 0, total: 0, examNumber: key, tag: q.sourceTag };
    bySource[key].total++;
    if (isCorrect) bySource[key].correct++;
  });

  // Pacing: average time per question vs. the allotted time (if timed), and
  // the slowest few questions — helps spot where time actually went.
  const answeredTimes = session.questions.map((q, i) => ({ q, ms: timeSpentMs[i] || 0 })).filter(t => t.ms > 0);
  const avgMs = answeredTimes.length ? answeredTimes.reduce((s, t) => s + t.ms, 0) / answeredTimes.length : 0;
  const allottedMs = session.timed && session.totalSeconds ? (session.totalSeconds / total) * 1000 : null;
  const slowest = answeredTimes.slice().sort((a, b) => b.ms - a.ms).slice(0, 5);
  const pacing = { avgMs, allottedMs, slowest, hasData: answeredTimes.length > 0 };

  session.results = { correctCount, total, missed, bySdl, byObjective, bySource, pacing };
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
        ${sourceKeys.sort((a, b) => Number(b) - Number(a)).map(key => {
          const r = bySource[key];
          const label = r.tag === 'current' ? `Exam ${r.examNumber} (this week's material)` : `Exam ${r.examNumber} (prior weeks' carryover)`;
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

  const pacingHtml = !session.results.pacing || !session.results.pacing.hasData ? '' : (() => {
    const { avgMs, allottedMs, slowest } = session.results.pacing;
    const avgLabel = formatTime(avgMs / 1000);
    const vsAllotted = allottedMs
      ? ` &middot; allotted ${formatTime(allottedMs / 1000)}/question (${avgMs > allottedMs ? 'running slower than planned' : 'within your planned pace'})`
      : '';
    const slowRows = slowest.map(({ q, ms }) => `<tr><td>${escapeHtml(q.stem.length > 90 ? q.stem.slice(0, 90) + '…' : q.stem)}</td><td>SDL ${q.sdlNumber}</td><td>${formatTime(ms / 1000)}</td></tr>`).join('');
    return `
      <div class="section-label">Pacing</div>
      <p class="setup-hint">Average ${avgLabel}/question${vsAllotted}</p>
      <table class="breakdown-table">
        <thead><tr><th>Slowest Questions</th><th>SDL</th><th>Time</th></tr></thead>
        <tbody>${slowRows}</tbody>
      </table>
    `;
  })();

  const missedHtml = missed.length === 0
    ? '<p class="empty-state">No missed questions — perfect score.</p>'
    : missed.map(({ q, given }) => `
      <div class="missed-item">
        <div class="missed-stem">${escapeHtml(q.stem)} ${isFlagged(q.id) ? '<span class="flagged-tag">&#9733; flagged</span>' : ''}</div>
        <div class="your-answer">Your answer: ${given ? `${given} — ${escapeHtml(q.choices[given])}` : '(no answer)'}</div>
        <div class="correct-answer">Correct answer: ${q.correct} — ${escapeHtml(q.choices[q.correct])}</div>
        <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
        ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
        ${atlasLinksHtml(q)}
      </div>
    `).join('');

  main.innerHTML = `
    <h1>${session.presetId ? escapeHtml(examSessionLabel(session).replace(/^Final Exam/, 'Final Exam Results')) : session.isFinal ? 'Final Exam Results' : `Exam ${session.examNumber} Simulation Results`}</h1>
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

    ${pacingHtml}

    <div class="section-label">Missed Questions (${missed.length})</div>
    ${missedHtml}

    <div style="display:flex; gap:10px; justify-content:center; margin-top:20px;">
      <button class="btn" id="doneBtn">${session.isFinal ? 'Back to Home' : `Back to Exam ${session.examNumber}`}</button>
    </div>
  `;
  document.getElementById('doneBtn').addEventListener('click', () => setRoute(session.isFinal ? '' : `exam-sdls/${session.examNumber}`));
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
    records: new Array(flaggedQuestions.length).fill(null),
    pendingLetter: null,
  };
  renderFlaggedQuestion();
}

function renderFlaggedQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const record = session.records[session.index];
  const answered = !!record;
  if (!session.struck) session.struck = {};
  const struckArr = session.struck[session.index] || [];

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    const isStruck = struckArr.includes(letter);
    if (isStruck && !answered) cls += ' struck';
    if (answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === record.letter) cls += ' incorrect';
    } else if (session.pendingLetter === letter) {
      cls += ' selected';
    }
    const strikeBtn = !answered ? `<button class="strike-btn ${isStruck ? 'active' : ''}" data-strike-letter="${letter}" title="Cross out this choice" aria-label="Cross out choice ${letter}">🚫</button>` : '';
    return `<div class="choice-row">
      <button class="${cls}" data-letter="${letter}" ${answered ? 'disabled' : ''}>
        <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
      </button>${strikeBtn}
    </div>`;
  }).join('');

  let confidenceHtml = '';
  if (!answered && session.pendingLetter) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer? <span style="font-weight:400; color:var(--grey-text);">(tap a different choice to change it)</span></div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (answered) {
    feedbackHtml = `
      <div class="feedback-banner ${record.correct ? 'correct' : 'incorrect'}">
        ${record.correct ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${atlasLinksHtml(q)}
    `;
  }

  const answeredSoFar = session.records.filter(r => r).length;
  const correctSoFar = session.records.filter(r => r && r.correct).length;

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <div class="quiz-header">
      <span class="quiz-progress">Flagged Review — Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${correctSoFar}/${answeredSoFar}</span>
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
      <div class="next-row" style="justify-content: space-between;">
        <button class="btn secondary" id="prevBtn" ${session.index === 0 ? 'disabled' : ''}>&larr; Previous</button>
        ${answered ? `<button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button>` : '<span></span>'}
      </div>
    </div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    // Refresh this same view (item stays visible until navigating away).
    renderFlaggedQuestion();
  });
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (session.index > 0) {
      session.index--;
      session.pendingLetter = null;
      renderFlaggedQuestion();
    }
  });

  function finalizeAnswer(confidence) {
    const letter = session.pendingLetter;
    const correct = letter === q.correct;
    session.records[session.index] = { letter, confidence, correct };
    session.pendingLetter = null;
    if (!correct) triggerWrongFlash();
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle, examNumber: q.examNumber,
      objective: q.objective, objectiveLabel: q.objectiveLabel, batch: q.batch,
      correct, confidence, mode: 'flagged', ts: Date.now(),
    });
    renderFlaggedQuestion();
  }

  if (!answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderFlaggedQuestion();
      });
    });
    main.querySelectorAll('.strike-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const letter = btn.dataset.strikeLetter;
        const arr = session.struck[session.index] || [];
        const i = arr.indexOf(letter);
        if (i === -1) arr.push(letter); else arr.splice(i, 1);
        session.struck[session.index] = arr;
        renderFlaggedQuestion();
      });
    });
    const confGuessed = document.getElementById('confGuessed');
    const confConfident = document.getElementById('confConfident');
    if (confGuessed) confGuessed.addEventListener('click', () => finalizeAnswer('guessed'));
    if (confConfident) confConfident.addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.pendingLetter = null;
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
    queueLabel: 'Review Due',
    questions: shuffle(qs),
    index: 0,
    records: new Array(qs.length).fill(null),
    pendingLetter: null,
  };
  renderReviewQuestion();
}

/* ── Toughest Questions (item-level, this browser's own attempts only) ──
   Personal-only by construction: every stat here comes from LS_ATTEMPTS,
   which never leaves this device — nothing about other users is read,
   stored, or aggregated anywhere in this app. */
function attemptStatsByQuestionId() {
  const stats = {};
  loadAttempts().forEach(a => {
    if (!stats[a.id]) stats[a.id] = { id: a.id, total: 0, correct: 0 };
    stats[a.id].total++;
    if (a.correct) stats[a.id].correct++;
  });
  return stats;
}
function toughestQuestions(minAttempts, maxAccuracy, limit) {
  minAttempts = minAttempts || 2;
  maxAccuracy = maxAccuracy == null ? 1 : maxAccuracy;
  const stats = Object.values(attemptStatsByQuestionId())
    .filter(s => s.total >= minAttempts && (s.correct / s.total) <= maxAccuracy)
    .sort((a, b) => (a.correct / a.total) - (b.correct / b.total) || b.total - a.total);
  const withQ = stats.map(s => Object.assign({ accuracy: s.correct / s.total, attempts: s.total }, findQuestionById(s.id))).filter(q => q.id);
  return limit ? withQ.slice(0, limit) : withQ;
}

function renderToughestQueue() {
  const qs = toughestQuestions(2, 0.7, 30);

  if (qs.length === 0) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>Toughest Questions</h1>
      <p class="empty-state">Nothing qualifies yet — this fills in once you've answered a question at least twice and are still missing it more often than not. Keep practicing.</p>
    `;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }

  session = {
    mode: 'review',
    queueLabel: 'Toughest Questions',
    questions: qs,
    index: 0,
    records: new Array(qs.length).fill(null),
    pendingLetter: null,
  };
  renderReviewQuestion();
}

function renderReviewQuestion() {
  const q = session.questions[session.index];
  const total = session.questions.length;
  const flagged = isFlagged(q.id);
  const letters = ['A', 'B', 'C', 'D', 'E'];
  const record = session.records[session.index];
  const answered = !!record;
  if (!session.struck) session.struck = {};
  const struckArr = session.struck[session.index] || [];

  const choicesHtml = letters.map(letter => {
    let cls = 'choice';
    const isStruck = struckArr.includes(letter);
    if (isStruck && !answered) cls += ' struck';
    if (answered) {
      cls += ' disabled';
      if (letter === q.correct) cls += ' correct';
      else if (letter === record.letter) cls += ' incorrect';
    } else if (session.pendingLetter === letter) {
      cls += ' selected';
    }
    const strikeBtn = !answered ? `<button class="strike-btn ${isStruck ? 'active' : ''}" data-strike-letter="${letter}" title="Cross out this choice" aria-label="Cross out choice ${letter}">🚫</button>` : '';
    return `<div class="choice-row">
      <button class="${cls}" data-letter="${letter}" ${answered ? 'disabled' : ''}>
        <span class="letter">${letter}.</span><span>${escapeHtml(q.choices[letter])}</span>
      </button>${strikeBtn}
    </div>`;
  }).join('');

  let confidenceHtml = '';
  if (!answered && session.pendingLetter) {
    confidenceHtml = `
      <div class="confidence-prompt">
        <div class="confidence-label">How confident were you in that answer? <span style="font-weight:400; color:var(--grey-text);">(tap a different choice to change it)</span></div>
        <div class="confidence-buttons">
          <button class="btn secondary" id="confGuessed">🤔 Guessed</button>
          <button class="btn" id="confConfident">💪 Confident</button>
        </div>
      </div>`;
  }

  let feedbackHtml = '';
  if (answered) {
    feedbackHtml = `
      <div class="feedback-banner ${record.correct ? 'correct' : 'incorrect'}">
        ${record.correct ? '✅ Correct' : `❌ Incorrect — correct answer is ${q.correct}`}
      </div>
      <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
      ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
      ${q.crossRef ? `<div class="info-block xref">${escapeHtml(q.crossRef)}</div>` : ''}
      ${atlasLinksHtml(q)}
    `;
  }

  const answeredSoFar = session.records.filter(r => r).length;
  const correctSoFar = session.records.filter(r => r && r.correct).length;

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <div class="quiz-header">
      <span class="quiz-progress">${escapeHtml(session.queueLabel || 'Review Due')} — Question ${session.index + 1} of ${total}</span>
      <span class="quiz-score">Score: ${correctSoFar}/${answeredSoFar}</span>
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
      <div class="next-row" style="justify-content: space-between;">
        <button class="btn secondary" id="prevBtn" ${session.index === 0 ? 'disabled' : ''}>&larr; Previous</button>
        ${answered ? `<button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next Question' : 'Finish'}</button>` : '<span></span>'}
      </div>
    </div>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderReviewQuestion();
  });
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (session.index > 0) {
      session.index--;
      session.pendingLetter = null;
      renderReviewQuestion();
    }
  });

  function finalizeAnswer(confidence) {
    const letter = session.pendingLetter;
    const correct = letter === q.correct;
    session.records[session.index] = { letter, confidence, correct };
    session.pendingLetter = null;
    if (!correct) triggerWrongFlash();
    logAttempt({
      id: q.id, sdlNumber: q.sdlNumber, sdlTitle: q.sdlTitle, examNumber: q.examNumber,
      objective: q.objective, objectiveLabel: q.objectiveLabel, batch: q.batch,
      correct, confidence, mode: 'review', ts: Date.now(),
    });
    renderReviewQuestion();
  }

  if (!answered) {
    main.querySelectorAll('.choice').forEach(btn => {
      btn.addEventListener('click', () => {
        session.pendingLetter = btn.dataset.letter;
        renderReviewQuestion();
      });
    });
    main.querySelectorAll('.strike-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const letter = btn.dataset.strikeLetter;
        const arr = session.struck[session.index] || [];
        const i = arr.indexOf(letter);
        if (i === -1) arr.push(letter); else arr.splice(i, 1);
        session.struck[session.index] = arr;
        renderReviewQuestion();
      });
    });
    const confGuessed = document.getElementById('confGuessed');
    const confConfident = document.getElementById('confConfident');
    if (confGuessed) confGuessed.addEventListener('click', () => finalizeAnswer('guessed'));
    if (confConfident) confConfident.addEventListener('click', () => finalizeAnswer('confident'));
  } else {
    const nextBtn = document.getElementById('nextBtn');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        if (session.index + 1 < total) {
          session.index++;
          session.pendingLetter = null;
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

    if (!bySdl[a.sdlNumber]) bySdl[a.sdlNumber] = { correct: 0, total: 0, title: a.sdlTitle || `SDL ${a.sdlNumber}`, sdlNumber: a.sdlNumber };
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

  // Score Trend: each exam-simulation key's run history (recordScore keeps
  // the last 20 runs per key), rendered as a tiny sparkline + the raw % sequence.
  const progress = loadProgress();
  const trendKeys = Object.keys(progress).filter(k => progress[k].history && progress[k].history.length >= 2);
  const trendHtml = trendKeys.length === 0
    ? '<p class="setup-hint">Run the same Full or Final Exam Simulation more than once to unlock a score trend here.</p>'
    : trendKeys.sort().map(key => {
        const h = progress[key].history;
        const pcts = h.map(e => Math.round((e.correct / e.total) * 100));
        const presetId = key.startsWith('final-preset-') ? key.slice('final-preset-'.length) : null;
        const label = presetId ? examSessionLabel({ presetId }) : key === 'final-exam' ? 'Final Exam' : key.replace(/^exam-/, 'Exam ');
        return `
          <div style="display:flex; align-items:center; gap:16px; margin-bottom:10px; flex-wrap:wrap;">
            <div style="min-width:100px; font-weight:700; color:var(--navy); font-size:0.92rem;">${escapeHtml(label)}</div>
            ${sparklineSvg(pcts)}
            <div style="font-size:0.85rem; color:var(--grey-text);">${pcts.join('% &rarr; ')}%</div>
          </div>
        `;
      }).join('');

  // Toughest Questions: item-level accuracy, computed only from this browser's
  // own attempt log (see attemptStatsByQuestionId) — never shared or aggregated.
  const toughest = toughestQuestions(2, 1, 8);
  const toughestHtml = toughest.length === 0
    ? '<p class="setup-hint">Answer a question two or more times to start surfacing your personal toughest questions here.</p>'
    : `
      <table class="breakdown-table">
        <thead><tr><th>Question</th><th>SDL</th><th>Your Accuracy</th></tr></thead>
        <tbody>
          ${toughest.map(q => `
            <tr>
              <td>${escapeHtml(q.stem.length > 90 ? q.stem.slice(0, 90) + '…' : q.stem)}</td>
              <td>SDL ${q.sdlNumber}</td>
              <td>${Math.round(q.accuracy * 100)}% (${q.attempts} attempt${q.attempts === 1 ? '' : 's'})</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
      <div style="margin-top:12px;">
        <button class="btn secondary" id="drillToughestBtn">Drill Toughest Questions</button>
      </div>
    `;

  // Focus areas: objectives with at least 2 attempts, worst accuracy first.
  const objList = Object.values(byObjective)
    .filter(o => o.total >= 2)
    .sort((a, b) => (a.correct / a.total) - (b.correct / b.total));
  const focusRows = objList.slice(0, 10).map(o => {
    const label = (o.label || '').replace(/^Objective\s+\d+\s*—?\s*/i, '');
    return `<tr><td>SDL ${o.sdlNumber} — ${escapeHtml(label)}</td><td>${o.correct}/${o.total}</td><td>${Math.round((o.correct / o.total) * 100)}%</td></tr>`;
  }).join('');

  // Group by-SDL rollups under their parent exam block, in exam order, so performance
  // across the whole course reads at a glance instead of one long flat table mixing
  // every exam's SDLs together. Each exam header also shows its own aggregate score.
  const byExam = {}; // examNumber -> { examNumber, correct, total, sdls: [...] }
  Object.values(bySdl).forEach(s => {
    const found = SDL_INDEX.get(s.sdlNumber);
    const examNumber = found ? found.examNumber : 0;
    if (!byExam[examNumber]) byExam[examNumber] = { examNumber, correct: 0, total: 0, sdls: [] };
    byExam[examNumber].correct += s.correct;
    byExam[examNumber].total += s.total;
    byExam[examNumber].sdls.push(s);
  });

  const examGroupsHtml = Object.values(byExam)
    .sort((a, b) => a.examNumber - b.examNumber)
    .map(group => {
      const groupPct = Math.round((group.correct / group.total) * 100);
      const rows = group.sdls
        .sort((a, b) => a.sdlNumber - b.sdlNumber)
        .map(s => `<tr><td>${escapeHtml(s.title)}</td><td>${s.correct}/${s.total}</td><td>${Math.round((s.correct / s.total) * 100)}%</td></tr>`)
        .join('');
      const title = group.examNumber === 0 ? 'Other' : `Exam ${group.examNumber}`;
      return `
        <div class="exam-group">
          <div class="exam-group-header">
            <span class="exam-group-title">${title}</span>
            <span class="exam-group-score">${group.correct}/${group.total} &middot; ${groupPct}%</span>
          </div>
          <table class="breakdown-table"><thead><tr><th>SDL</th><th>Score</th><th>%</th></tr></thead><tbody>${rows}</tbody></table>
        </div>
      `;
    }).join('');

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

    <div class="section-label">Score Trend (Exam Simulations)</div>
    ${trendHtml}

    <div class="section-label">Your Toughest Questions</div>
    <p class="setup-hint" style="margin-top:-4px;">Personal only — based purely on this browser's own answer history, never shared with anyone.</p>
    ${toughestHtml}

    <div class="section-label">Focus Areas — Weakest Objectives</div>
    ${focusRows
      ? `<table class="breakdown-table"><thead><tr><th>Objective</th><th>Score</th><th>%</th></tr></thead><tbody>${focusRows}</tbody></table>`
      : '<p class="empty-state">Not enough repeated attempts per objective yet — answer a few more questions in each SDL.</p>'}

    <div class="section-label">By Exam / SDL</div>
    ${examGroupsHtml}

    <div class="section-label">Confidence Calibration</div>
    ${calibrationHtml}
  `;
  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  const drillToughestBtn = document.getElementById('drillToughestBtn');
  if (drillToughestBtn) drillToughestBtn.addEventListener('click', () => setRoute('toughest'));
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
  if (!window.QUIZ_DATA) throw new Error('data.js did not define window.QUIZ_DATA — make sure data.js is loaded before app.js in index.html.');
  DATA = window.QUIZ_DATA;
  DATA.exams.forEach(exam => {
    exam.sdls.forEach(sdl => {
      SDL_INDEX.set(sdl.sdlNumber, { sdl, examNumber: exam.examNumber });
    });
  });
  render();
} catch (err) {
  main.innerHTML = `<p class="empty-state">Could not load question bank: ${escapeHtml(err.message)}</p>`;
}
