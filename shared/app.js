'use strict';
/* Board-prep Question Bank — vanilla JS app, shared across all blocks. No frameworks, no build step. */

/* ── Global state ─────────────────────────────────────────────────────── */
let DATA = null;               // parsed data.json
let SDL_INDEX = new Map();     // sdlNumber -> {sdl, examNumber}
let session = null;            // active quiz/exam session object
const main = document.getElementById('main');
const homeBtn = document.getElementById('homeBtn');
/* The hub's header on every block page (design E): its brand, then the main links. The page's
   own "← All Blocks" link and title give way to it; #homeBtn stays in the bar (render() still
   shows and hides it) but each screen's breadcrumb does its job, so the stylesheet hides it.
   theme.js adds the ◐ toggle after this runs. */
const BLOCK_SHORT = { nephro: 'Nephro', psych: 'Psych', neuro: 'Neuro', endocrine: 'Endocrine', eent: 'EENT', pulm: 'Pulm',
  ortho: 'Ortho', rheum: 'Rheum', omm: 'OMM', gi: 'GI' };
(function hubHeader() {
  const bar = document.querySelector('.topbar-inner');
  if (!bar) return;
  bar.innerHTML = `<a class="hub-brand" href="../index.html">OCOM Question Hub</a>
    <nav class="hub-nav" aria-label="Main"><a href="../resources/metabolic-atlas.html">Lesion Atlas</a><a href="../index.html#blocks" aria-current="page">Blocks</a><a href="../live.html">Live Session</a><a href="../index.html#sync">Sync</a><a href="../index.html#offline">Offline</a></nav>`;
  if (homeBtn) bar.appendChild(homeBtn);
})();
// "Nephro" — the block's short name, for breadcrumbs
function blockShort() {
  return BLOCK_SHORT[blockDirName()] || QUIZ_CONFIG.title.replace(/\s*(?:Block\s*)?Question Bank$/i, '');
}
// "Nephrology / Urology / Men's Health" — the block's title without "Block Question Bank"
function blockDisplayTitle() {
  return QUIZ_CONFIG.title.replace(/\s*(?:Block\s*)?Question Bank$/i, '').replace(/\s*\/\s*/g, ' / ').trim();
}
// the batch a practice run covers, from its route segment ('1', '2', 'all', or a trial batch)
function batchLabel(b) {
  return b === '1' ? 'Batch 1' : b === '2' ? 'Batch 2' : b === 'all' ? 'Both batches'
    : (TRIAL_BATCHES[b] && TRIAL_BATCHES[b].name) || 'Practice';
}

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
// Batch 3 is the per-SDL opt-in trial slot (kept out of exam totals, simulations,
// custom exams and splits). Its wording defaults to the Neuro "Bloom Batch"; a block
// can relabel it with QUIZ_CONFIG.batch3 = { name, listLabel, icon, title, meta, hint,
// banner, afterBatch2 } (afterBatch2: list it right under Batch 2 in the batch picker).
const BATCH3 = Object.assign({
  name: 'Bloom Batch',
  listLabel: 'Bloom Batch',
  icon: '🧠',
  title: '🧠 Bloom Batch — Level 3/4 Trial',
  meta: 'experimental, board-qbank style',
  hint: 'Bloom Batch is an experimental higher-rigor trial — short single-term answer choices and board-qbank-style vignettes, kept separate from the regular batches.',
  banner: '🧠 Bloom Batch — Level 3/4 Trial (experimental, board-qbank style)',
  afterBatch2: false,
}, QUIZ_CONFIG.batch3 || {});
// Batch 4 is a second, optional trial slot with the same treatment as batch 3; it exists
// only where a block sets QUIZ_CONFIG.batch4 (same fields, plus rowClass for the picker
// row; afterBatch2 lists it right under batch 3). TRIAL_BATCHES maps batch number ->
// config, and isTrialQ() is the one test for "kept out of totals/simulation/builder/splits".
const TRIAL_BATCHES = { 3: Object.assign({ rowClass: 'bloom-row' }, BATCH3) };
if (QUIZ_CONFIG.batch4) {
  TRIAL_BATCHES[4] = Object.assign({
    name: 'Trial 2', listLabel: 'trial questions', icon: '🧪', title: '🧪 Trial', meta: 'experimental',
    hint: '', banner: '🧪 Trial (experimental)', afterBatch2: false, rowClass: 'bloom-row trial-alt-row',
  }, QUIZ_CONFIG.batch4);
}
const TRIAL_KEYS = Object.keys(TRIAL_BATCHES).map(Number).sort((a, b) => a - b);
function isTrialQ(q) { return !!TRIAL_BATCHES[q.batch]; }

/* ── Lesion Atlas links ─────────────────────────────────────────────────
   resources/atlas-terms.js (written by tools/build-atlas.py) lists every atlas
   card with its name and curated match terms, already normalized by the same
   rules as atlasNorm() below — keep the two in step. Once a question is
   answered, a card is linked when one of its terms appears as a whole phrase in
   the correct answer or the first sentence of the explanation — the part that
   explains the answer. Terms written "=term" match in the correct answer only. Later sentences and the board-prep note were tested and
   left out: they mostly discuss the wrong choices and differentials, and linked
   the wrong cards. The file loads lazily; if it is missing, questions simply
   show no atlas links. */
const APP_SRC = (document.currentScript && document.currentScript.src) || '';
const ATLAS_URL = APP_SRC ? new URL('../resources/metabolic-atlas.html', APP_SRC).href : '';
let ATLAS_INDEX = null;
let ATLAS_MAPS = null;   // map id -> [title, card ids], for "Practice this map"
let ATLAS_GRAPHS = null; // [map id, plot index, title, card ids] — "See it on a graph", "Graphs for this block"
let ATLAS_MOVES = null;  // [map id, "switch:option" or "", option label, map title, card ids] — "See it move"
let ATLAS_READY = Promise.resolve();   // settles once atlas-terms.js has loaded (or failed)
(function loadAtlasTerms() {
  if (!APP_SRC) return;
  ATLAS_READY = new Promise(resolve => {
    const s = document.createElement('script');
    s.src = new URL('../resources/atlas-terms.js', APP_SRC).href;
    s.async = true;
    s.onload = () => {
      const d = window.ATLAS_TERMS;
      if (d && Array.isArray(d.cards)) ATLAS_INDEX = d.cards.map(([id, n, k, t]) => ({ id, n, k, t }));
      if (d && d.maps) ATLAS_MAPS = d.maps;
      if (d && Array.isArray(d.graphs)) ATLAS_GRAPHS = d.graphs;
      if (d && Array.isArray(d.moves)) ATLAS_MOVES = d.moves;
      resolve();
    };
    s.onerror = resolve;
    document.head.appendChild(s);
  });
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
// Cards whose terms appear in the given zones (zone 0 = an answer's text, where
// "=term" also counts), best first: earlier zone, then longer matching term.
function atlasMatch(zones) {
  const found = new Map();
  zones.forEach((z, zone) => {
    if (!z) return;
    const text = ' ' + atlasNorm(z) + ' ';
    for (const c of ATLAS_INDEX) {
      if (found.has(c.id)) continue;
      // a term written "=term" is answer-only: it never matches in the explanation
      const hit = c.t.find(t => {
        if (t[0] === '=') { if (zone) return false; t = t.slice(1); }
        return text.includes(' ' + t + ' ') || text.includes(' ' + t + 's ') || text.includes(' ' + t + 'es ');
      });
      if (hit) found.set(c.id, { c, zone, len: hit.replace(/^=/, '').length });
    }
  });
  return [...found.values()].sort((a, b) => a.zone - b.zone || b.len - a.len).map(x => x.c);
}
function atlasLinksFor(q) {
  if (!ATLAS_INDEX || !q) return [];
  const lead = (String(q.explanation || '').match(/[^.!?]+[.!?]+/g) || [q.explanation || ''])[0];
  return atlasMatch([q.choices && choiceText(q, q.correct), lead]).slice(0, 3);
}
/* "You picked": after a miss, the option the person chose is matched the same way as
   a correct answer, and its best card — one not already linked for the right answer —
   is shown with a Compare link that opens it beside the correct card in the atlas
   (#cmp/<picked>/<correct>). */
// The best card for one answer option, matched on its leading phrase — what it names —
// not the reasoning that follows, which mentions other things in passing
// ("X, which …", "X because …", "X — …").
function atlasOptionCard(q, letter) {
  const head = String(choiceText(q, letter)).split(/[,;:(]| [—–-] | (?:which|because|since|due to|caused by|as|so|while|whereas|that) /i)[0];
  return atlasMatch([head])[0] || null;
}
function atlasPickedFor(q, picked, have) {
  if (!ATLAS_INDEX || !q || !q.choices || !picked || picked === q.correct) return null;
  // If the option's best card is already one linked for the right answer, the option is
  // about the same thing (a wrong statement about it) — nothing to compare.
  const top = atlasOptionCard(q, picked);
  return top && !(have || []).some(c => c.id === top.id) ? top : null;
}
/* After a miss, a table gives the atlas card for every answer choice: the right answer
   shows its top linked card, each other option its own best card (or "same card as the
   answer" when it names the same thing), and the row you picked carries the Compare
   link (#cmp/<picked>/<correct>). Single-answer questions only. */
function atlasChoicesHtml(q, picked, cards, link) {
  const letters = Object.keys(q.choices || {});
  if (letters.length < 2 || typeof picked !== 'string' || typeof q.correct !== 'string' || !letters.includes(picked)) return '';
  const short = t => { t = String(t || '').replace(/\s+/g, ' ').trim(); return t.length > 90 ? t.slice(0, 88).replace(/\s+\S*$/, '') + '…' : t; };
  const rows = letters.map(L => {
    const right = L === q.correct, mine = L === picked;
    const c = right ? cards[0] : atlasOptionCard(q, L);
    const same = !right && c && cards.some(x => x.id === c.id);
    const tag = right ? '<span class="ac-tag ok">answer</span>' : mine ? '<span class="ac-tag pick">your pick</span>' : '';
    const cmp = mine && c && !same && cards.length
      ? `<a class="atlas-cmp" href="${ATLAS_URL}#cmp/${encodeURIComponent(c.id)}/${encodeURIComponent(cards[0].id)}" target="_blank" rel="noopener">Compare</a>` : '';
    const cell = !c ? '<span class="ac-none">—</span>' : same ? '<span class="ac-none">same card as the answer</span>' : link(c) + cmp;
    return `<tr class="${right ? 'is-right' : mine ? 'is-pick' : ''}"><th scope="row">${escapeHtml(L)}</th>
      <td class="ac-opt">${escapeHtml(short(choiceText(q, L)))}${tag}</td><td class="ac-card">${cell}</td></tr>`;
  }).join('');
  return `<div class="atlas-choices"><div class="atlas-picked-lbl">Every answer choice on the atlas</div><table class="atlas-ctab"><tbody>${rows}</tbody></table></div>`;
}
function atlasLinksHtml(q, picked) {
  if (!ATLAS_URL) return '';
  const cards = atlasLinksFor(q);
  const link = c => `<a class="atlas-link k-${c.k}" href="${ATLAS_URL}#${encodeURIComponent(c.id)}" target="_blank" rel="noopener"><span class="dot"></span>${escapeHtml(c.n)}</a>`;
  const table = picked && ATLAS_INDEX && q && q.choices && picked !== q.correct ? atlasChoicesHtml(q, picked, cards, link) : '';
  // No table (e.g. a select-all question): fall back to the single "You picked" line.
  const wrong = table ? null : atlasPickedFor(q, picked, cards);
  if (!cards.length && !wrong && !table) return '';
  const pickedHtml = wrong ? `<div class="atlas-picked"><span class="atlas-picked-lbl">You picked ${escapeHtml(picked)}:</span>${link(wrong)}${cards.length
    ? `<a class="atlas-cmp" href="${ATLAS_URL}#cmp/${encodeURIComponent(wrong.id)}/${encodeURIComponent(cards[0].id)}" target="_blank" rel="noopener">Compare with ${escapeHtml(cards[0].n)}</a>` : ''}</div>` : '';
  // the first graph that illustrates one of the linked cards, best card first
  const g = ATLAS_GRAPHS && cards.map(c => ATLAS_GRAPHS.find(x => x[3].includes(c.id))).find(Boolean);
  const graphHtml = g ? `<a class="atlas-graph" href="${ATLAS_URL}#graph/${encodeURIComponent(g[0])}/${g[1]}" target="_blank" rel="noopener">See it on a graph: ${escapeHtml(g[2])}</a>` : '';
  // a moving map for the best card: with that card's switch already on if one exists, else the map itself
  const mv = ATLAS_MOVES && cards.map(c => ATLAS_MOVES.find(x => x[1] && x[4].includes(c.id)) || ATLAS_MOVES.find(x => !x[1] && x[4].includes(c.id))).find(Boolean);
  const moveHtml = mv ? `<a class="atlas-graph atlas-move" href="${ATLAS_URL}#${encodeURIComponent(mv[0])}${mv[1] ? '/~' + mv[1].split(':').map(encodeURIComponent).join(':') : ''}" target="_blank" rel="noopener">See it move: ${escapeHtml(mv[3])}${mv[2] ? ' — ' + escapeHtml(mv[2]) : ''}</a>` : '';
  // Missed it: the moving map for the right answer goes first, as a prompt to watch it.
  const missed = picked && q && picked !== q.correct && mv;
  const ctaHtml = missed ? `<a class="atlas-move-cta" href="${ATLAS_URL}#${encodeURIComponent(mv[0])}${mv[1] ? '/~' + mv[1].split(':').map(encodeURIComponent).join(':') : ''}" target="_blank" rel="noopener"><span class="amc-k">Missed it? Watch it move</span><span class="amc-t">${escapeHtml(mv[3])}${mv[2] ? ' — ' + escapeHtml(mv[2]) : ''}</span></a>` : '';
  return `<div class="info-block atlas">${ctaHtml}<b>On the Lesion Atlas</b>${cards.map(link).join('')}${graphHtml}${missed ? '' : moveHtml}${pickedHtml}${table}</div>`;
}

/* Missed questions feed the Lesion Atlas review list. The atlas keeps its
   progress in localStorage ('mla-progress') on this same site. A miss puts the
   question's top atlas card on the spaced-review schedule, due now; a right
   answer moves a card already on the schedule forward — due again in 1, 3,
   then 7 days, then off. Same rule as schedule() in tools/atlas-src.html —
   keep the two in step. */
const ATLAS_PROG_KEY = 'mla-progress';
const ATLAS_BOX_DAYS = [0, 1, 3, 7];
let QUESTION_INDEX = null;
function questionById(id) {
  if (!QUESTION_INDEX) {
    QUESTION_INDEX = {};
    ((window.QUIZ_DATA && window.QUIZ_DATA.exams) || []).forEach(e => (e.sdls || []).forEach(s =>
      (s.questions || []).forEach(q => { QUESTION_INDEX[q.id] = q; })));
  }
  return QUESTION_INDEX[id];
}
function atlasNoteAnswer(rec) {
  const q = rec && questionById(rec.id);
  if (!q) return;
  ATLAS_READY.then(() => {
    const card = atlasLinksFor(q)[0];
    if (!card) return;
    let p = {};
    try { p = JSON.parse(localStorage.getItem(ATLAS_PROG_KEY)) || {}; } catch (e) { p = {}; }
    ['qok', 'qmiss', 'box', 'due', 'at'].forEach(k => { if (!p[k] || typeof p[k] !== 'object') p[k] = {}; });
    const id = card.id, now = Date.now();
    // Counts are always kept; the review schedule only when the person has turned
    // card review on in the atlas (opt-in, same key the atlas and the hub read).
    let review = false;
    try { review = localStorage.getItem('mla-review') === 'on'; } catch (e) {}
    if (rec.correct) {
      p.qok[id] = (p.qok[id] || 0) + 1;
      if (review && id in p.box) {
        p.at[id] = now;   // when the schedule last changed — PIN sync keeps the newer side
        const b = p.box[id] + 1;
        if (b >= ATLAS_BOX_DAYS.length) { delete p.box[id]; delete p.due[id]; }
        else { p.box[id] = b; p.due[id] = now + ATLAS_BOX_DAYS[b] * 864e5; }
      }
    } else {
      p.qmiss[id] = (p.qmiss[id] || 0) + 1;
      if (review) { p.box[id] = 0; p.due[id] = now; p.at[id] = now; }
    }
    try { localStorage.setItem(ATLAS_PROG_KEY, JSON.stringify(p)); } catch (e) {}
  });
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
  atlasNoteAnswer(rec);
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
      splitId: session.splitId || null,
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
      trialBatch: session.trialBatch || 0,
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

/* ── Grid ("matrix") answer choices — PROTOTYPE ─────────────────────────
   Optional, backward-compatible: a question with
     grid: { headers: ['Serum Na⁺', 'Urine osmolality', 'ECF volume'] }
   stores each choice as an array of cell values, one per header
     choices: { A: ['↓', '↑', 'normal'], B: [...], ... }
   and is drawn as aligned rows under one header row. Questions without `grid`
   (every existing one) render exactly as before. Anything that needs plain text
   (results lists, study sheet, atlas matching, live sessions) goes through
   choiceText(), which joins the cells with ' / '. */
function isGridQ(q) {
  return !!(q && q.grid && Array.isArray(q.grid.headers) && q.grid.headers.length);
}
// Header i as plain text (drops soft hyphens, which only mark where a long header may break).
function gridHeaderText(q, i) {
  return String(q.grid.headers[i] == null ? '' : q.grid.headers[i]).replace(/\u00AD/g, '');
}
function choiceCells(q, letter) {
  const v = q && q.choices ? q.choices[letter] : null;
  if (Array.isArray(v)) return v.map(c => (c == null ? '' : String(c)));
  return v == null ? [] : String(v).split(' / ');
}
// Plain-text form of a choice. withHeaders: "Serum Na⁺ ↓ · Urine osmolality ↑ · …"
function choiceText(q, letter, withHeaders) {
  const v = q && q.choices ? q.choices[letter] : null;
  if (!Array.isArray(v)) return v == null ? '' : String(v);
  if (withHeaders && isGridQ(q)) return v.map((c, i) => `${gridHeaderText(q, i)} ${c}`.trim()).join(' · ');
  return v.join(' / ');
}
function choiceBodyHtml(q, letter) {
  if (!isGridQ(q)) return `<span>${escapeHtml(choiceText(q, letter))}</span>`;
  const cells = choiceCells(q, letter);
  const label = q.grid.headers.map((h, i) => `${gridHeaderText(q, i)}: ${cells[i] || ''}`).join('; ');
  return `<span class="grid-cells" aria-label="${escapeHtml(label)}">${q.grid.headers.map((h, i) =>
    gridCellHtml(cells[i])).join('')}</span>`;
}
// One cell. Arrow-only cells (↑ ↓ ↔ ↑↑ ↓↓) get .grid-arrow so the arrow is drawn
// large; 'normal' and short text values keep the regular cell size.
function gridCellHtml(c) {
  const t = String(c == null ? '' : c).trim();
  return /^[↑↓↔]{1,2}$/.test(t)
    ? `<span class="grid-cell is-arrow"><span class="grid-arrow">${t}</span></span>`
    : `<span class="grid-cell">${escapeHtml(t)}</span>`;
}
// Header row drawn above the choices; withStrike reserves the 🚫 column so cells line up.
function gridHeaderHtml(q, withStrike) {
  if (!isGridQ(q)) return '';
  return `<div class="choice-row grid-head" aria-hidden="true">
      <div class="grid-head-row"><span class="letter"></span><span class="grid-cells">${q.grid.headers.map(h =>
        `<span class="grid-cell">${escapeHtml(h)}</span>`).join('')}</span></div>${withStrike ? '<span class="strike-spacer"></span>' : ''}
    </div>`;
}
function choiceListOpen(q) {
  return isGridQ(q)
    ? `<div class="choice-list grid-choices" style="--grid-cols:${q.grid.headers.length}">`
    : '<div class="choice-list">';
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
  // Excludes the trial batches (isTrialQ: batch 3, Bloom Batch / nephro short-stem trial,
  // and batch 4 where QUIZ_CONFIG.batch4 exists) — opt-in experimental trials, not part of
  // the standard question pool used for exam totals, Full Exam Simulation, or the
  // Custom Exam Builder's current/prior blend. Also respects High-Yield Only mode.
  const settings = loadSettings();
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) return [];
  let qs = [];
  exam.sdls.forEach(sdl => {
    sdl.questions.forEach(q => {
      if (isTrialQ(q)) return;
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

// Answers synced from another device arrive without their SDL title and
// objective text (sync.js leaves them out of the cloud copy to stay under
// Firestore's document size limit), so Analytics looks them up here.
function sdlTitleFor(sdlNumber) {
  const found = findSdl(sdlNumber);
  return found ? found.sdl.title : `SDL ${sdlNumber}`;
}
let OBJECTIVE_LABELS = null; // "sdlNumber-objective" -> objectiveLabel, built on first use
function objectiveLabelFor(sdlNumber, objective) {
  if (!OBJECTIVE_LABELS) {
    OBJECTIVE_LABELS = new Map();
    DATA.exams.forEach(e => e.sdls.forEach(sdl => sdl.questions.forEach(q => {
      const key = `${sdl.sdlNumber}-${q.objective}`;
      if (q.objectiveLabel && !OBJECTIVE_LABELS.has(key)) OBJECTIVE_LABELS.set(key, q.objectiveLabel);
    })));
  }
  return OBJECTIVE_LABELS.get(`${sdlNumber}-${objective}`) || '';
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
  main.dataset.view = parts.length === 0 ? 'home' : (parts[0] === 'practice' && parts[2]) ? 'practice-q' : parts[0];
  // a new screen starts at the top (the block home is long now)
  if (render.lastHash !== undefined && render.lastHash !== hash) window.scrollTo(0, 0);
  render.lastHash = hash;

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
  } else if (parts[0] === 'split' && parts[1]) {
    renderSplitSetup(decodeURIComponent(parts[1]));
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
  } else if (parts[0] === 'atlas' && parts[1]) {
    renderAtlasPractice(decodeURIComponent(parts[1]), parts[2] === 'missed');
  } else if (parts[0] === 'atlasmap' && parts[1]) {
    renderAtlasMapPractice(decodeURIComponent(parts[1]), parts[2] === 'missed');
  } else if (parts[0] === 'atlascards' && parts[1]) {
    renderAtlasCardsPractice(decodeURIComponent(parts[1]).split(','), parts[2] ? decodeURIComponent(parts[2]) : '');
  } else if (parts[0] === 'sdlcards' && parts[1]) {
    renderSdlCards(parseInt(parts[1], 10));
  } else if (parts[0] === 'sdlmissed' && parts[1]) {
    renderSdlMissed(parseInt(parts[1], 10));
  } else {
    renderHome();
  }
  rememberPlace(parts);
}

/* "Continue where you left off" on the hub: the last place you were in a block is kept on
   this device ('qhub-last': block folder and title, the hash, a label, the time). The hub
   reads it — and, for SDL practice, that block's saved session — to link straight back. */
function rememberPlace(parts) {
  const save = label => { try { localStorage.setItem('qhub-last', JSON.stringify({ dir: blockDirName(), title: QUIZ_CONFIG.title,
    hash: window.location.hash, label, at: Date.now() })); } catch (e) {} };
  if (parts[0] === 'practice' && parts[1] && parts[2]) {
    const f = findSdl(parseInt(parts[1], 10)); if (f) save(f.sdl.title);
  } else if (parts[0] === 'exam-sdls' && parts[1]) save('Exam ' + parts[1] + ' — SDL list');
  else if (parts[0] === 'review') save('Review: missed & flagged');
  else if (parts[0] === 'flagged') save('Flagged questions');
  else if (parts[0] === 'toughest') save('Toughest questions');
  else if ((parts[0] === 'sdlcards' || parts[0] === 'sdlmissed') && parts[1]) {
    const f = findSdl(parseInt(parts[1], 10));
    if (f) save((parts[0] === 'sdlcards' ? 'Atlas cards: ' : 'Your misses: ') + f.sdl.title);
  }
  else if (parts[0] === 'atlascards' && parts[1]) save('Atlas practice: ' + (parts[2] ? decodeURIComponent(parts[2]) : 'a graph'));
  else if ((parts[0] === 'atlas' || parts[0] === 'atlasmap') && parts[1]) {
    const id = decodeURIComponent(parts[1]), route = window.location.hash, miss = parts[2] === 'missed' ? ' — your misses' : '';
    ATLAS_READY.then(() => {
      if (window.location.hash !== route) return;
      const name = parts[0] === 'atlasmap' ? (ATLAS_MAPS && ATLAS_MAPS[id] ? ATLAS_MAPS[id][0] : id)
        : ((ATLAS_INDEX && (ATLAS_INDEX.find(c => c.id === id) || {}).n) || id);
      save('Atlas practice: ' + name + miss);
    });
  }
}
/* Questions you got wrong on your latest try, from a list of linked questions. */
function onlyMissed(qs) {
  const last = lastAttemptMap();
  return qs.filter(q => last[q.id] && !last[q.id].correct);
}

homeBtn.addEventListener('click', () => setRoute(''));

/* ── Home screen ──────────────────────────────────────────────────────── */
/* "Maps for this block" on the block home: the atlas maps whose cards this block's
   questions link to most (counts from resources/atlas-practice.js, built by
   tools/build-atlas.py), each with a link to the map and a Practice button that runs
   those questions here (#atlasmap/<map id>). Loads lazily; absent data shows nothing. */
let ATLAS_PRACTICE_READY = null;
function loadAtlasPractice() {
  if (ATLAS_PRACTICE_READY) return ATLAS_PRACTICE_READY;
  ATLAS_PRACTICE_READY = new Promise(resolve => {
    if (window.ATLAS_PRACTICE) return resolve(window.ATLAS_PRACTICE);
    if (!APP_SRC) return resolve(null);
    const s = document.createElement('script');
    s.src = new URL('../resources/atlas-practice.js', APP_SRC).href;
    s.async = true;
    s.onload = () => resolve(window.ATLAS_PRACTICE || null);
    s.onerror = () => resolve(null);
    document.head.appendChild(s);
  });
  return ATLAS_PRACTICE_READY;
}
function blockDirName() {
  const parts = location.pathname.split('/').filter(Boolean);
  if (parts.length && /\.html?$/i.test(parts[parts.length - 1])) parts.pop();
  return parts.length ? decodeURIComponent(parts[parts.length - 1]) : '';
}
/* Your accuracy per map: each question you have answered in this block counts toward
   every map holding one of its linked atlas cards (the same rule the map's Practice run
   uses), scored on your latest try. Linked cards are worked out once per question per
   page load. */
const ATLAS_Q_CARDS = new Map();
function atlasMapAccuracy() {
  const cardMaps = {};
  Object.keys(ATLAS_MAPS || {}).forEach(m => (ATLAS_MAPS[m][1] || []).forEach(c => { (cardMaps[c] = cardMaps[c] || []).push(m); }));
  const acc = {};
  const last = lastAttemptMap();
  Object.keys(last).forEach(id => {
    const q = questionById(id);
    if (!q) return;
    if (!ATLAS_Q_CARDS.has(id)) ATLAS_Q_CARDS.set(id, atlasLinksFor(q).map(c => c.id));
    const maps = new Set();
    ATLAS_Q_CARDS.get(id).forEach(c => (cardMaps[c] || []).forEach(m => maps.add(m)));
    maps.forEach(m => { const a = acc[m] = acc[m] || { n: 0, ok: 0 }; a.n++; if (last[id].correct) a.ok++; });
  });
  return acc;
}
const AMAP_MIN = 3;   // answers on a map before it is ranked by accuracy
function fillAtlasMapsHome() {
  const el = document.getElementById('atlasMapsHome');
  if (!el || !ATLAS_URL) return;
  Promise.all([ATLAS_READY, loadAtlasPractice()]).then(([, P]) => {
    if (!document.body.contains(el) || !P || !P.maps || !ATLAS_MAPS) return;
    const bi = (P.blocks || []).findIndex(b => b[0] === blockDirName());
    if (bi < 0) return;
    const acc = atlasMapAccuracy();
    const pct = a => a.ok / a.n;
    const ranked = id => !!(acc[id] && acc[id].n >= AMAP_MIN);
    // Weakest first among maps you have answered enough of; the rest by question count.
    const rows = Object.keys(P.maps).map(id => [id, ((P.maps[id] || []).find(x => x[0] === bi) || [0, 0])[1]])
      .filter(([id, n]) => n > 0 && ATLAS_MAPS[id])
      .sort((a, b) => (ranked(b[0]) - ranked(a[0]))
        || (ranked(a[0]) ? pct(acc[a[0]]) - pct(acc[b[0]]) || acc[b[0]].n - acc[a[0]].n : 0)
        || b[1] - a[1] || ATLAS_MAPS[a[0]][0].localeCompare(ATLAS_MAPS[b[0]][0]));
    if (!rows.length) return;
    const most = Math.max(1, ...rows.map(r => r[1]));
    const row = ([id, n]) => {
      const a = acc[id], p = a ? Math.round(100 * pct(a)) : 0;
      const chip = a ? `<span class="amap-acc ${p < 60 ? 'lo' : p < 80 ? 'mid' : 'hi'}" title="Your latest try on ${a.n} of this map’s questions">${a.ok}/${a.n} · ${p}%</span>` : '';
      return `<li class="amap-row">
        <a class="amap-name" href="${ATLAS_URL}#${encodeURIComponent(id)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[id][0])}</a>
        <span class="amap-bar" aria-hidden="true"><i style="width:${Math.round(100 * n / most)}%"></i></span>
        ${chip}<span class="amap-n">${n} question${n === 1 ? '' : 's'}</span>
        ${a && a.n > a.ok ? `<a class="amap-go amap-miss" href="#atlasmap/${encodeURIComponent(id)}/missed" title="Run only the questions you missed on your latest try">Redo ${a.n - a.ok} missed</a>` : ''}
        <a class="amap-go open" href="${ATLAS_URL}#${encodeURIComponent(id)}" target="_blank" rel="noopener">Open map</a>
        <a class="amap-go" href="#atlasmap/${encodeURIComponent(id)}">Practice</a></li>`;
    };
    const anyRanked = rows.some(r => ranked(r[0]));
    const top = rows.slice(0, 8), rest = rows.slice(8);
    el.innerHTML = `<section class="bsec atlas-sec" aria-labelledby="amapH"><div class="sec-head"><h2 class="sec-h" id="amapH">This block in the Lesion Atlas</h2>
      <a href="${ATLAS_URL}" target="_blank" rel="noopener">Open the atlas →</a></div>
      <p class="amap-note">${anyRanked
        ? `Your weakest maps first — ranked by your latest answer to each question linked to the map, once you have answered ${AMAP_MIN}. The rest follow by how many of this block’s questions link to them.`
        : 'Lesion Atlas maps ranked by how many of this block’s questions link to their cards. Once you answer a few questions, your weakest maps move to the top.'} Open a map, or practice its questions here.</p>
      <ul class="amap-list">${top.map(row).join('')}</ul>
      ${rest.length ? `<details class="amap-more"><summary>All ${rows.length} maps</summary><ul class="amap-list">${rest.map(row).join('')}</ul></details>` : ''}</section>`;
  });
}

/* "Moving maps for this block" on the block home: the atlas's moving maps whose cards this block's questions
   link to most (counts from atlas-practice.js), each with the switches this block tests most — a switch link
   opens the map with it on (#<map>/~<switch>:<option>) — and a Practice button (#atlasmap/<map>). */
function fillAtlasMovesHome() {
  const el = document.getElementById('atlasMovesHome');
  if (!el || !ATLAS_URL) return;
  Promise.all([ATLAS_READY, loadAtlasPractice()]).then(([, P]) => {
    if (!document.body.contains(el) || !P || !P.maps || !ATLAS_MOVES || !ATLAS_MAPS) return;
    const bi = (P.blocks || []).findIndex(b => b[0] === blockDirName());
    if (bi < 0) return;
    const nOf = (rows) => ((rows || []).find(x => x[0] === bi) || [0, 0])[1];
    const moving = [...new Set(ATLAS_MOVES.map(x => x[0]))].filter(v => ATLAS_MAPS[v]);
    const rows = moving.map(v => [v, nOf(P.maps[v])]).filter(([, n]) => n > 0)
      .sort((a, b) => b[1] - a[1] || ATLAS_MAPS[a[0]][0].localeCompare(ATLAS_MAPS[b[0]][0]));
    if (!rows.length) return;
    let named = {}; try { named = (JSON.parse(localStorage.getItem('mla-progress') || '{}') || {}).nit || {}; } catch (e) {}   // Name-it scores, saved by the atlas
    const open = (v, sw) => `${ATLAS_URL}#${encodeURIComponent(v)}${sw ? '/~' + sw.split(':').map(encodeURIComponent).join(':') : ''}`;
    const tile = ([v, n]) => {
      const sws = ATLAS_MOVES.filter(x => x[0] === v && x[1])
        .map(x => [x, x[4].reduce((t, c) => t + nOf(P.cards && P.cards[c]), 0)]).filter(([, k]) => k > 0)
        .sort((a, b) => b[1] - a[1]).slice(0, 3);
      return `<div class="gtile mtile"><a class="gt-name" href="${open(v)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[v][0])}</a>
        <span class="gt-meta">${n} question${n === 1 ? '' : 's'} in this block${named[v] && named[v][1] ? ` · Name it ${named[v][0]}/${named[v][1]}` : ''}</span>
        ${sws.length ? `<span class="mt-sw">${sws.map(([x, k]) => `<a href="${open(v, x[1])}" target="_blank" rel="noopener" title="${k} question${k === 1 ? '' : 's'} here">${escapeHtml(x[2])}</a>`).join('')}</span>` : MOVE_GLYPH}
        <span class="gt-links"><a href="${open(v)}" target="_blank" rel="noopener">Open map</a><a href="#atlasmap/${encodeURIComponent(v)}">Practice</a></span></div>`;
    };
    const top = rows.slice(0, 6), rest = rows.slice(6);
    const hero = document.getElementById('atlasMovesHero');
    if (hero) {
      const item = ([v, n]) => {
        const sws = ATLAS_MOVES.filter(x => x[0] === v && x[1])
          .map(x => [x, x[4].reduce((t, c) => t + nOf(P.cards && P.cards[c]), 0)]).filter(([, k]) => k > 0)
          .sort((a, b) => b[1] - a[1]).slice(0, 2);
        return `<li><a class="mh-name" href="${open(v)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[v][0])}</a>
          <span class="bh-meta">${n} question${n === 1 ? '' : 's'} here${named[v] && named[v][1] ? ` · Name it ${named[v][0]}/${named[v][1]}` : ''}</span>
          ${sws.length ? `<span class="mt-sw">${sws.map(([x]) => `<a href="${open(v, x[1])}" target="_blank" rel="noopener">${escapeHtml(x[2])}</a>`).join('')}</span>` : ''}</li>`;
      };
      hero.innerHTML = `<div class="bh-card static mhero">
        <span class="kicker">Moving maps for this block</span>
        <ul class="mh-list">${rows.slice(0, 3).map(item).join('')}</ul>
        <span class="bh-actions"><a class="btn" href="${ATLAS_URL}#quiz/moving" target="_blank" rel="noopener">Moving-map mix</a>${rows.length > 3 ? `<button type="button" class="btn secondary" id="mhAll">All ${rows.length} moving maps ↓</button>` : ''}</span></div>`;
      const all = document.getElementById('mhAll');
      if (all) all.addEventListener('click', () => { const t = document.getElementById('amvH'); if (t) t.scrollIntoView({ behavior: 'smooth', block: 'start' }); });
    }
    el.innerHTML = `<section class="bsec" aria-labelledby="amvH"><h3 class="sub-h" id="amvH">Moving maps for this block</h3>
      <p class="amap-note">Lesion Atlas maps you can switch — drugs, diseases, lesions — ranked by how many of this block’s questions they cover. A switch below opens the map with it on.</p>
      <div class="gtiles">${top.map(tile).join('')}</div>
      ${rest.length ? `<details class="amap-more"><summary>All ${rows.length} moving maps</summary><div class="gtiles">${rest.map(tile).join('')}</div></details>` : ''}</section>`;
  });
}

/* "Graphs for this block" on the block home: the atlas graphs whose cards this block's questions
   link to most (counts from atlas-practice.js), each opening the graph in the atlas (#graph/<map>/<plot>)
   with a Practice button that runs those questions here (#atlascards). Absent data shows nothing. */
function fillAtlasGraphsHome() {
  const el = document.getElementById('atlasGraphsHome');
  if (!el || !ATLAS_URL) return;
  Promise.all([ATLAS_READY, loadAtlasPractice()]).then(([, P]) => {
    if (!document.body.contains(el) || !P || !P.graphs || !ATLAS_GRAPHS) return;
    const bi = (P.blocks || []).findIndex(b => b[0] === blockDirName());
    if (bi < 0) return;
    const rows = Object.keys(P.graphs).map(gi => [+gi, ((P.graphs[gi] || []).find(x => x[0] === bi) || [0, 0])[1]])
      .filter(([gi, n]) => n > 0 && ATLAS_GRAPHS[gi])
      .sort((a, b) => b[1] - a[1] || ATLAS_GRAPHS[a[0]][2].localeCompare(ATLAS_GRAPHS[b[0]][2]));
    if (!rows.length) return;
    const row = ([gi, n]) => {
      const [v, i, t, ids] = ATLAS_GRAPHS[gi], map = ATLAS_MAPS && ATLAS_MAPS[v] ? ATLAS_MAPS[v][0] : v;
      return `<li class="amap-row">
        <a class="amap-name" href="${ATLAS_URL}#graph/${encodeURIComponent(v)}/${i}" target="_blank" rel="noopener">${escapeHtml(t)}</a>
        <span class="amap-n">${escapeHtml(map)} · ${n} question${n === 1 ? '' : 's'}</span>
        <a class="amap-go" href="#atlascards/${encodeURIComponent(ids.join(','))}/${encodeURIComponent(t)}">Practice</a></li>`;
    };
    // the top six as tiles, the rest as rows
    const tile = ([gi, n]) => {
      const [v, i, t, ids] = ATLAS_GRAPHS[gi], map = ATLAS_MAPS && ATLAS_MAPS[v] ? ATLAS_MAPS[v][0] : v;
      const open = `${ATLAS_URL}#graph/${encodeURIComponent(v)}/${i}`;
      return `<div class="gtile"><a class="gt-name" href="${open}" target="_blank" rel="noopener">${escapeHtml(t)}</a>
        <span class="gt-meta">${escapeHtml(map)} · ${n} question${n === 1 ? '' : 's'}</span>${GRAPH_GLYPH}
        <span class="gt-links"><a href="${open}" target="_blank" rel="noopener">Open graph</a><a href="#atlascards/${encodeURIComponent(ids.join(','))}/${encodeURIComponent(t)}">Practice</a></span></div>`;
    };
    const top = rows.slice(0, 6), rest = rows.slice(6);
    el.innerHTML = `<section class="bsec" aria-labelledby="agH"><h3 class="sub-h" id="agH">Graphs for this block</h3>
      <p class="amap-note">Lesion Atlas graphs whose cards this block’s questions test most. Open a graph to see it and quiz yourself on its versions, or practice its questions here.</p>
      <div class="gtiles">${top.map(tile).join('')}</div>
      ${rest.length ? `<details class="amap-more"><summary>All ${rows.length} graphs</summary><ul class="amap-list">${rest.map(row).join('')}</ul></details>` : ''}</section>`;
  });
}

/* "Your weakest SDLs" on the block home: every SDL you have answered at least SDL_MIN of its
   questions in, ranked by your latest try (lastAttemptMap), weakest first — with Redo missed
   (#sdlmissed/<sdl>), Atlas cards (#sdlcards/<sdl>) and Practice. */
const SDL_MIN = 3;
function sdlAccuracy() {
  const last = lastAttemptMap(), out = [];
  DATA.exams.forEach(e => e.sdls.forEach(sdl => {
    let n = 0, ok = 0;
    sdl.questions.forEach(q => { const a = last[q.id]; if (a) { n++; if (a.correct) ok++; } });
    if (n) out.push({ sdl, examNumber: e.examNumber, n, ok, total: sdl.questions.length });
  }));
  return out;
}
function fillWeakSdlsHome() {
  const el = document.getElementById('weakSdlsHome');
  if (!el) return;
  const rows = sdlAccuracy().filter(r => r.n >= SDL_MIN)
    .sort((a, b) => a.ok / a.n - b.ok / b.n || b.n - a.n || a.sdl.sdlNumber - b.sdl.sdlNumber);
  if (!rows.length) { el.innerHTML = ''; return; }
  const row = r => {
    const p = Math.round(100 * r.ok / r.n), miss = r.n - r.ok;
    return `<li class="amap-row">
      <a class="amap-name" href="#practice/${r.sdl.sdlNumber}">${escapeHtml(r.sdl.title)}</a>
      <span class="amap-acc ${p < 60 ? 'lo' : p < 80 ? 'mid' : 'hi'}" title="Your latest try on ${r.n} of its ${r.total} questions">${r.ok}/${r.n} · ${p}%</span>
      <span class="amap-n">Exam ${r.examNumber}</span>
      ${miss ? `<a class="amap-go amap-miss" href="#sdlmissed/${r.sdl.sdlNumber}" title="Run only the questions you missed on your latest try">Redo ${miss} missed</a>` : ''}
      ${ATLAS_URL ? `<a class="amap-go" href="#sdlcards/${r.sdl.sdlNumber}" title="The atlas cards this SDL’s questions link to">Atlas cards</a>` : ''}
      <a class="amap-go" href="#practice/${r.sdl.sdlNumber}">Practice</a></li>`;
  };
  const top = rows.slice(0, 6), rest = rows.slice(6);
  el.innerHTML = `<section class="bsec" aria-labelledby="weakH"><h2 class="sec-h" id="weakH">Your weakest SDLs</h2>
    <p class="amap-note">Ranked by your latest answer to each question, once you have answered ${SDL_MIN} in an SDL — weakest first. This device only.</p>
    <ul class="amap-list">${top.map(row).join('')}</ul>
    ${rest.length ? `<details class="amap-more"><summary>All ${rows.length} SDLs you have started</summary><ul class="amap-list">${rest.map(row).join('')}</ul></details>` : ''}</section>`;
}

/* ── Block home (design H) ─────────────────────────────────────────────
   A band with the block's name, its counts and a search over its SDLs, beside
   whatever you were doing (an exam or SDL run to resume, or your progress);
   then the exams, the simulations and the block's maps and graphs on the
   Lesion Atlas, with the study tools, the block's latest announcement and the
   settings in a side column. */
function loadExamDates() {
  try { const o = JSON.parse(localStorage.getItem('qhub-examdates') || '{}'); return o && typeof o === 'object' ? o : {}; } catch (e) { return {}; }
}
// "in 5 days" for an exam date set on the hub's Exam countdown (this device only); past dates show nothing
function examWhen(s) {
  const m = typeof s === 'string' && s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (!m) return '';
  const t = new Date(+m[1], +m[2] - 1, +m[3]), now = new Date(); now.setHours(0, 0, 0, 0);
  const d = Math.round((t - now) / 86400000);
  return d < 0 ? '' : d === 0 ? 'today' : d === 1 ? 'tomorrow' : `in ${d} days`;
}
function renderHome() {
  main.dataset.view = 'home';
  const last = lastAttemptMap();
  const dates = loadExamDates();
  const examCards = DATA.exams.map(e => {
    // Regular bank only (trial batches are opt-in, as in the SDL list); trial counts follow.
    const all = e.sdls.flatMap(sdl => sdl.questions);
    const regular = all.filter(q => !isTrialQ(q));
    const qCount = regular.length;
    const trialMeta = TRIAL_KEYS.map(b => {
      const n = all.filter(q => q.batch === b).length;
      return n ? `<span class="trial-count">${TRIAL_BATCHES[b].icon} ${n} ${escapeHtml(TRIAL_BATCHES[b].listLabel)}</span>` : '';
    }).join('');
    let seen = 0, right = 0;
    regular.forEach(q => { const a = last[q.id]; if (a) { seen++; if (a.correct) right++; } });
    const seenPct = qCount ? Math.min(100, Math.round(100 * seen / qCount)) : 0;
    const when = examWhen(dates[`${blockDirName()}:${e.examNumber}`]);
    return `
      <button type="button" class="exam-card" data-exam="${e.examNumber}">
        <span class="ex-top"><span class="exam-num">Exam ${e.examNumber}</span>${when ? `<span class="ex-when">${escapeHtml(when)}</span>` : ''}</span>
        <span class="exam-label">${e.sdls.length} SDLs · ${qCount ? `${qCount} questions` : 'questions coming soon'}</span>
        ${qCount && trialMeta ? `<span class="exam-label exam-trial">${trialMeta}</span>` : ''}
        ${qCount ? `<span class="ex-bar"><i style="width:${seenPct}%"></i></span>
        <span class="ex-prog">${seen ? `${seenPct}% seen · ${Math.round(100 * right / seen)}% right` : 'Not started'}</span>` : ''}
      </button>`;
  }).join('');

  const flagCount = Object.keys(loadFlags()).length;
  const attempts = loadAttempts();

  const reviewIds = new Set();
  Object.keys(last).forEach(id => { if (!last[id].correct) reviewIds.add(id); });
  Object.keys(loadFlags()).forEach(id => reviewIds.add(id));
  const reviewCount = reviewIds.size;

  const settings = loadSettings();

  // A block can be published as a skeleton (every SDL titled, no questions yet),
  // so the final needs questions in the last exam, not just more than one exam.
  const showFinalExamCard = DATA.exams.length > 1 && allQuestionsForExam(lastExamNumber()).length > 0;

  const resumeSnap = loadExamSessionSnapshot();
  const resumeHtml = resumeSnap ? (() => {
    const done = resumeSnap.answers.filter(a => a !== null).length, n = resumeSnap.questions.length;
    return `
    <div class="bh-card" id="resumeExamCard" role="button" tabindex="0">
      <span class="kicker">Resume exam</span>
      <span class="bh-title">${escapeHtml(examSessionLabel(resumeSnap))}</span>
      <span class="bh-meta">Question ${resumeSnap.index + 1} of ${n} · ${done} answered${resumeSnap.timed ? (resumeSnap.deadlineAt - Date.now() <= 0 ? ' · time expired' : ` · ${formatTime((resumeSnap.deadlineAt - Date.now()) / 1000)} left`) : ' · untimed'}</span>
      <span class="bh-bar"><i style="width:${Math.round(100 * done / n)}%"></i></span>
      <span class="bh-actions"><span class="btn">Resume</span><button type="button" class="btn secondary" id="discardResumeBtn">Discard</button></span>
    </div>`;
  })() : '';

  // Same idea as the exam resume card above, but for an in-progress SDL
  // practice run — this is the direct fix for "I refresh by accident and
  // have to redo the whole SDL." A refresh alone doesn't even need this card
  // (the #practice/<sdl>/<batch> hash survives and auto-resumes on its own),
  // but this covers the closed-tab/came-back-later case, and gives an
  // explicit Discard so an abandoned run doesn't linger forever.
  const practiceSnap = loadPracticeSessionSnapshot();
  const practiceSdl = practiceSnap ? findSdl(practiceSnap.sdlNumber) : null;
  const practiceResumeHtml = (practiceSnap && practiceSdl) ? (() => {
    const recs = (practiceSnap.records || []).filter(r => r), n = practiceSnap.questions.length;
    return `
    <div class="bh-card" id="resumePracticeCard" role="button" tabindex="0">
      <span class="kicker">Resume practice</span>
      <span class="bh-title">${escapeHtml(practiceSdl.sdl.title)}</span>
      <span class="bh-meta">${escapeHtml(batchLabel(batchParamFromScoreKey(practiceSnap.scoreKey)))} · question ${practiceSnap.index + 1} of ${n} · ${recs.filter(r => r.correct).length} of ${recs.length} right</span>
      <span class="bh-bar"><i style="width:${Math.round(100 * recs.length / n)}%"></i></span>
      <span class="bh-actions"><span class="btn">Resume</span><button type="button" class="btn secondary" id="discardPracticeResumeBtn">Discard</button></span>
    </div>`;
  })() : '';

  // Nothing to resume: how you are doing in this block, and where to go next
  const answered = Object.keys(last).length, rightAll = Object.keys(last).filter(id => last[id].correct).length;
  const firstExam = DATA.exams.find(e => e.sdls.some(s => s.questions.length)) || DATA.exams[0];
  // Your progress: a slim bar sitting on top of the exams (the hero's side holds the moving maps)
  const progressHtml = `
    <div class="bprog" aria-label="Your progress">
      <span class="bprog-t"><span class="kicker">Your progress</span> ${answered
        ? `<b>${answered.toLocaleString()} answered · ${Math.round(100 * rightAll / answered)}% right</b> · ${reviewCount} to review — missed and flagged · this device`
        : '<b>Nothing answered yet</b> — pick an exam below, or search for an SDL.'}</span>
      <span class="bprog-act">${answered
        ? `${reviewCount ? '<a class="btn" href="#review">Review due</a>' : ''}<a class="btn${reviewCount ? ' secondary' : ''}" href="#analytics">Analytics</a>`
        : firstExam ? `<a class="btn" href="#exam-sdls/${firstExam.examNumber}">Start Exam ${firstExam.examNumber}</a>` : ''}</span>
    </div>`;

  const nSdl = DATA.exams.reduce((s, e) => s + e.sdls.length, 0);
  const allQs = DATA.exams.flatMap(e => e.sdls.flatMap(s => s.questions));
  const nReg = allQs.filter(q => !isTrialQ(q)).length, nTrial = allQs.length - nReg;

  main.innerHTML = `
    <section class="bhero bleed" aria-labelledby="bhTitle">
      <div class="bhero-in">
        <div class="bhero-main">
          <nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">All blocks</a><span aria-hidden="true">/</span><span>${escapeHtml(blockShort())}</span></nav>
          <h1 id="bhTitle">${escapeHtml(blockDisplayTitle())}</h1>
          <p class="bhero-meta">${DATA.exams.length} exam${DATA.exams.length === 1 ? '' : 's'} · ${nSdl} SDLs · ${nReg.toLocaleString()} questions${nTrial ? ` + ${nTrial} trial` : ''}${settings.hyOnly ? ' · <strong>⚡ High-yield only is on</strong>' : ''}</p>
          <form class="bsearch" id="bSearch" role="search" autocomplete="off">
            <div class="bsbox">
              <label class="sr" for="bQ">Search this block’s SDLs</label>
              <input id="bQ" type="search" placeholder="Search this block — “SDL 23” or a topic" role="combobox" aria-expanded="false" aria-controls="bRes" aria-autocomplete="list" spellcheck="false">
              <div class="bsres" id="bRes" role="listbox" aria-label="SDLs" hidden></div>
            </div>
            <button type="submit">Search</button>
          </form>
        </div>
        <div class="bhero-side">${resumeHtml}${practiceResumeHtml}<div id="atlasMovesHero"></div></div>
      </div>
    </section>
    <div class="bcols">
      <div class="bcol-main">
        <section class="bsec" aria-labelledby="exH">
          ${progressHtml}
          <h2 class="sec-h" id="exH">Exams</h2>
          <div class="exam-grid">${examCards}</div>
          <div class="sim-grid">
            ${splitCardsHtml()}
            ${showFinalExamCard ? `
            <div class="action-card" id="finalExamCard">
              <span class="icon">&#127937;</span>
              <div>
                <div class="sdl-title">Final Exam Simulation</div>
                <div class="action-label">Cumulative — 50% Exam ${lastExamNumber()}, 50% pooled from every earlier exam block</div>
              </div>
            </div>
            ${finalPresetCardsHtml(`timed at 1.5 min each${settings.examInstantFeedback ? ' · 📝 Instant Feedback is ON' : ''}`)}` : ''}
          </div>
        </section>
        <div id="weakSdlsHome"></div>
        <div id="atlasMapsHome"></div>
        <div id="atlasMovesHome"></div>
        <div id="atlasGraphsHome"></div>
      </div>
      <aside class="bcol-side" aria-label="Study tools and settings">
        <section class="side-box" aria-labelledby="toolsH">
          <h2 class="side-h" id="toolsH">Study tools</h2>
          <button type="button" class="tool-row" id="analyticsCard"><b>Performance analytics</b><span>${attempts.length ? `${attempts.length} answers logged — see your weakest objectives` : 'Answer some questions to unlock this'}</span></button>
          <button type="button" class="tool-row" id="reviewCard"><b>Review due — missed + flagged</b><span>${reviewCount} question${reviewCount === 1 ? '' : 's'} to revisit</span></button>
          <button type="button" class="tool-row" id="sheetCard"><b>Export study sheet</b><span>Printable missed + flagged, with explanations</span></button>
          <button type="button" class="tool-row" id="flaggedCard"><b>Review flagged only</b><span>${flagCount} question${flagCount === 1 ? '' : 's'} flagged, across all SDLs</span></button>
        </section>
        <div id="blockNews"></div>
        <section class="side-box" aria-labelledby="setH">
          <h2 class="side-h" id="setH">Settings</h2>
          <label class="switch-row"><span><b>High-yield only</b><span>Practice and simulations use only questions tagged high-yield</span></span>
            <input type="checkbox" class="switch" id="hyToggle" ${settings.hyOnly ? 'checked' : ''}></label>
          <label class="switch-row"><span><b>Show answers in simulations</b><span>Reveal right or wrong and the explanation after each question, as in Practice, instead of when you submit</span></span>
            <input type="checkbox" class="switch" id="instantFeedbackToggle" ${settings.examInstantFeedback ? 'checked' : ''}></label>
          <label class="switch-row"><span><b>Wrong-answer flash</b><span>Red flash and image burst when you miss (every block)</span></span>
            <input type="checkbox" class="switch" id="wrongFlashToggle" ${wrongFlashEnabled() ? 'checked' : ''}></label>
        </section>
      </aside>
    </div>
  `;
  fillWeakSdlsHome();
  fillAtlasMapsHome();
  fillAtlasMovesHome();
  fillAtlasGraphsHome();
  fillBlockNews();
  bindBlockSearch();

  main.querySelectorAll('.exam-card').forEach(card => {
    card.addEventListener('click', () => setRoute(`exam-sdls/${card.dataset.exam}`));
  });
  bindSplitCards();
  const finalExamCard = document.getElementById('finalExamCard');
  if (finalExamCard) finalExamCard.addEventListener('click', () => setRoute('final-examsetup'));
  main.querySelectorAll('.final-preset-card').forEach(card => {
    card.addEventListener('click', () => {
      const preset = findFinalPreset(card.dataset.preset);
      if (preset) startFinalPreset(preset);
    });
  });
  // the resume cards open on click or Enter / Space; their Discard buttons stop that
  const onActivate = (el, fn) => {
    el.addEventListener('click', fn);
    el.addEventListener('keydown', e => { if ((e.key === 'Enter' || e.key === ' ') && e.target === el) { e.preventDefault(); fn(); } });
  };
  const resumeExamCard = document.getElementById('resumeExamCard');
  if (resumeExamCard) onActivate(resumeExamCard, () => setRoute('resume-exam'));
  const discardResumeBtn = document.getElementById('discardResumeBtn');
  if (discardResumeBtn) discardResumeBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    if (confirm('Discard the in-progress exam? This cannot be undone.')) {
      clearExamSessionSnapshot();
      renderHome();
    }
  });
  const resumePracticeCard = document.getElementById('resumePracticeCard');
  if (resumePracticeCard) onActivate(resumePracticeCard, () => {
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

/* Search this block's SDLs from the band at the top of its home: "23" or "SDL 23" finds that
   SDL, words find titles; each result opens the SDL. The last row hands the search to the
   hub's home page, which also searches the atlas (index.html?q=…). */
function bindBlockSearch() {
  const form = document.getElementById('bSearch'), q = document.getElementById('bQ'), box = document.getElementById('bRes');
  if (!form || !q || !box) return;
  const items = DATA.exams.flatMap(e => e.sdls.map(s => ({ s, e: e.examNumber, n: atlasNorm(s.title) })));
  let opts = [], active = -1;
  function show() {
    const qn = atlasNorm(q.value);
    if (!qn) { hide(); return; }
    const num = qn.match(/^(?:sdl ?)?(\d+)$/), words = qn.split(' ');
    const hits = num ? items.filter(it => String(it.s.sdlNumber) === num[1])
      : items.map(it => {
        const sp = ' ' + it.n + ' ';
        const sc = it.n.indexOf(qn) === 0 ? 3 : sp.indexOf(' ' + qn) >= 0 ? 2 : words.every(w => sp.indexOf(' ' + w) >= 0) ? 1 : 0;
        return [sc, it];
      }).filter(x => x[0]).sort((a, b) => b[0] - a[0] || a[1].s.sdlNumber - b[1].s.sdlNumber).map(x => x[1]);
    const rows = hits.slice(0, 7).map((it, i) => `<a class="bsopt" role="option" id="bOpt${i}" href="#practice/${it.s.sdlNumber}"><b>${escapeHtml(it.s.title)}</b><span>Exam ${it.e} · ${it.s.questions.length} questions</span></a>`);
    rows.push(`<a class="bsopt hub" role="option" id="bOpt${rows.length}" href="../index.html?q=${encodeURIComponent(q.value.trim())}"><b>Search the Lesion Atlas for “${escapeHtml(q.value.trim())}”</b><span>Maps, cards, graphs and every block’s SDLs</span></a>`);
    box.innerHTML = (hits.length ? '' : '<div class="bsnone">No SDL in this block matches.</div>') + rows.join('');
    box.hidden = false; q.setAttribute('aria-expanded', 'true');
    opts = [].slice.call(box.querySelectorAll('.bsopt')); setActive(-1);
  }
  function hide() { box.hidden = true; q.setAttribute('aria-expanded', 'false'); q.removeAttribute('aria-activedescendant'); opts = []; active = -1; }
  function setActive(i) {
    opts.forEach((o, j) => { o.classList.toggle('on', j === i); o.setAttribute('aria-selected', String(j === i)); });
    active = i;
    if (i >= 0) { q.setAttribute('aria-activedescendant', opts[i].id); opts[i].scrollIntoView({ block: 'nearest' }); } else q.removeAttribute('aria-activedescendant');
  }
  q.addEventListener('input', show);
  q.addEventListener('keydown', e => {
    if (e.key === 'ArrowDown' && opts.length) { e.preventDefault(); setActive(Math.min(opts.length - 1, active + 1)); }
    else if (e.key === 'ArrowUp' && opts.length) { e.preventDefault(); setActive(Math.max(-1, active - 1)); }
    else if (e.key === 'Escape') hide();
  });
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (!q.value.trim()) { q.focus(); return; }
    show();
    const o = opts[active >= 0 ? active : 0];
    if (o) location.href = o.href;
  });
  document.addEventListener('click', e => { if (!form.contains(e.target)) hide(); });
}

/* The block's latest announcement from the hub (announcements.js, edited by hand): the newest
   entry tagged with this block, or that names it, shown in the side column. */
let BLOCK_NEWS_READY = null;
function fillBlockNews() {
  const el = document.getElementById('blockNews');
  if (!el || !APP_SRC) return;
  if (!BLOCK_NEWS_READY) BLOCK_NEWS_READY = new Promise(resolve => {
    if (window.ANNOUNCEMENTS || window.ANNOUNCEMENT) return resolve();
    const s = document.createElement('script');
    s.src = new URL('../announcements.js', APP_SRC).href;
    s.async = true; s.onload = resolve; s.onerror = resolve;
    document.head.appendChild(s);
  });
  BLOCK_NEWS_READY.then(() => {
    if (!document.body.contains(el)) return;
    const list = (Array.isArray(window.ANNOUNCEMENTS) ? window.ANNOUNCEMENTS : []).concat(window.ANNOUNCEMENT ? [window.ANNOUNCEMENT] : []);
    const short = blockShort().toLowerCase(), dir = blockDirName().toLowerCase();
    const names = [short, dir, blockDisplayTitle().split(' / ')[0].toLowerCase()];
    const a = list.find(x => x && x.text && ((x.tag && names.includes(String(x.tag).toLowerCase())) ||
      names.some(n => n && new RegExp('\\b' + n.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i').test(String(x.text).replace(/<[^>]+>/g, '')))));
    if (!a) { el.innerHTML = ''; return; }
    el.innerHTML = `<section class="side-box news-box" aria-labelledby="bnH">
      <h2 class="side-h" id="bnH">Latest for ${escapeHtml(blockShort())}${a.date ? ` · ${escapeHtml(a.date)}` : ''}</h2>
      <p>${a.text}</p><a href="../index.html#newsH">All announcements →</a></section>`;
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
  ].concat(TRIAL_KEYS.map(b => ({ key: `sdl-${sdlNumber}-b${b}`, label: TRIAL_BATCHES[b].name })));
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
  main.dataset.view = 'exam-sdls';

  const settings = loadSettings();
  const totalQ = exam.sdls.reduce((s, sdl) => s + visibleQuestions(sdl).filter(q => !isTrialQ(q)).length, 0);
  const estMinutes = Math.round(totalQ * 90 / 60);
  const snap = loadPracticeSessionSnapshot();
  const when = examWhen(loadExamDates()[`${blockDirName()}:${examNumber}`]);

  const rows = exam.sdls.map(sdl => {
    const best = bestScoreForSdl(sdl.sdlNumber);
    const visible = visibleQuestions(sdl);
    const regularCount = visible.filter(q => !isTrialQ(q)).length;
    const trialMeta = TRIAL_KEYS.map(b => {
      const n = visible.filter(q => q.batch === b).length;
      return n ? ` &middot; ${TRIAL_BATCHES[b].icon} ${n} ${escapeHtml(TRIAL_BATCHES[b].listLabel)}` : '';
    }).join('');
    // the SDL's own title without its "SDL 13 — " lead: the number sits in the badge
    const name = String(sdl.title).replace(/^SDL\s*\d+\s*(?:[—–:-]+|--)\s*/i, '');
    if (!sdl.questions.length) return `
      <div class="sdl-row pending">
        <span class="sdl-num">${sdl.sdlNumber}</span>
        <div class="sdl-body">
          <div class="sdl-title">${escapeHtml(name)}</div>
          <div class="sdl-meta">Questions coming soon</div>
        </div>
      </div>`;
    const going = snap && String(snap.sdlNumber) === String(sdl.sdlNumber);
    const scoreHtml = going
      ? `<div class="sdl-score going">In progress · question ${snap.index + 1} of ${snap.questions.length}</div>`
      : best
        ? `<div class="sdl-score">${escapeHtml(best.label)} — Last: ${best.score.last.correct}/${best.score.last.total}${best.score.best.correct === best.score.last.correct && best.score.best.total === best.score.last.total ? '' : ` · Best: ${best.score.best.correct}/${best.score.best.total}`}</div>`
        : `<div class="sdl-score none">Not attempted</div>`;
    return `
      <div class="sdl-row${going ? ' going' : ''}" data-sdl="${sdl.sdlNumber}">
        <span class="sdl-num">${sdl.sdlNumber}</span>
        <div class="sdl-body">
          <div class="sdl-title">${escapeHtml(name)}</div>
          <div class="sdl-meta">${regularCount} questions${trialMeta}${ATLAS_URL ? ` &middot; <a class="sdl-atlas" href="#sdlcards/${sdl.sdlNumber}" title="The atlas cards this SDL’s questions link to">Atlas cards</a>` : ''}</div>
          ${scoreHtml}
        </div>
        <span class="sdl-go">${going ? 'Resume' : 'Practice'}</span>
      </div>`;
  }).join('');

  main.innerHTML = `
    <section class="page-head bleed" aria-labelledby="exTitle">
      <div class="ph-in">
        <div class="ph-main">
          <nav class="crumbs" aria-label="Breadcrumb"><a href="../index.html">All blocks</a><span aria-hidden="true">/</span><a href="#">${escapeHtml(blockShort())}</a><span aria-hidden="true">/</span><span>Exam ${examNumber}</span></nav>
          <h1 id="exTitle">Exam ${examNumber}</h1>
          <p class="ph-meta">${exam.sdls.length} SDLs · ${totalQ ? `${totalQ} questions` : 'questions coming soon'}${when ? ` · <span class="ph-when">${escapeHtml(when)}</span>` : ''}${settings.hyOnly ? ' · <strong>⚡ High-yield only is on</strong>' : ''}</p>
        </div>
        ${totalQ ? `<button type="button" class="ph-cta" id="fullSimCard">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2"/><path d="M9 2h6"/></svg>
          <span><b>Full exam simulation</b><span>All ${totalQ} questions, timed (~${estMinutes} min)${settings.examInstantFeedback ? ' · answers shown as you go' : ', answers at the end'}</span></span>
        </button>` : ''}
      </div>
    </section>
    ${splitPresets().some(p => p.exam === examNumber) ? `<div class="sim-grid">${splitCardsHtml(examNumber)}</div>` : ''}
    <div class="xcols">
      <section class="xmain" aria-labelledby="sdlH">
        <h2 class="sec-h" id="sdlH">Practice by SDL</h2>
        <div class="sdl-list">${rows}</div>
      </section>
      <aside class="xside" id="examAtlas" aria-label="Exam ${examNumber} in the Lesion Atlas"></aside>
    </div>
  `;

  const fullSimCard = document.getElementById('fullSimCard');
  if (fullSimCard) fullSimCard.addEventListener('click', () => setRoute(`examsetup/${examNumber}`));
  bindSplitCards();
  main.querySelectorAll('.sdl-row:not(.pending)').forEach(row => {
    row.addEventListener('click', e => {
      if (e.target.closest('a')) return;
      const n = +row.dataset.sdl;
      if (snap && String(snap.sdlNumber) === String(n)) setRoute(`practice/${n}/${batchParamFromScoreKey(snap.scoreKey)}`);
      else setRoute(`practice/${n}`);
    });
  });
  fillExamAtlas(exam);
}

/* "Exam N in the atlas" beside the SDL list: the maps this exam's questions link to most, and
   the graph they lean on most — worked out from each question's linked cards, the same rule
   as everywhere else (atlasLinksFor). Maps open in the atlas; Practice runs the block's
   questions on that map (#atlasmap) or graph (#atlascards). */
function fillExamAtlas(exam) {
  const el = document.getElementById('examAtlas');
  if (!el || !ATLAS_URL) return;
  ATLAS_READY.then(() => new Promise(r => setTimeout(r, 0))).then(() => {
    if (!document.body.contains(el) || !ATLAS_MAPS || !ATLAS_INDEX) return;
    const cardMaps = {};
    Object.keys(ATLAS_MAPS).forEach(m => (ATLAS_MAPS[m][1] || []).forEach(c => { (cardMaps[c] = cardMaps[c] || []).push(m); }));
    const mapN = {}, graphN = {};
    exam.sdls.forEach(sdl => sdl.questions.forEach(q => {
      if (isTrialQ(q)) return;
      if (!ATLAS_Q_CARDS.has(q.id)) ATLAS_Q_CARDS.set(q.id, atlasLinksFor(q).map(c => c.id));
      const ids = ATLAS_Q_CARDS.get(q.id), maps = new Set();
      ids.forEach(c => (cardMaps[c] || []).forEach(m => maps.add(m)));
      maps.forEach(m => { mapN[m] = (mapN[m] || 0) + 1; });
      (ATLAS_GRAPHS || []).forEach((g, gi) => { if (g[3].some(c => ids.includes(c))) graphN[gi] = (graphN[gi] || 0) + 1; });
    }));
    const maps = Object.keys(mapN).sort((a, b) => mapN[b] - mapN[a] || ATLAS_MAPS[a][0].localeCompare(ATLAS_MAPS[b][0])).slice(0, 5);
    const gTop = Object.keys(graphN).sort((a, b) => graphN[b] - graphN[a])[0];
    if (!maps.length) { el.innerHTML = ''; return; }
    const g = gTop != null ? ATLAS_GRAPHS[gTop] : null;
    el.innerHTML = `<section class="side-box">
        <h2 class="side-h">Exam ${exam.examNumber} in the atlas</h2>
        <p class="side-note">The maps this exam’s questions link to most</p>
        ${maps.map(m => `<div class="xmap"><a href="${ATLAS_URL}#${encodeURIComponent(m)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[m][0])}</a>
          <span>${mapN[m]} question${mapN[m] === 1 ? '' : 's'}</span><a class="amap-go" href="#atlasmap/${encodeURIComponent(m)}">Practice</a></div>`).join('')}
      </section>
      ${g ? `<section class="side-box">
        <h2 class="side-h">Graph to know</h2>
        <a class="xgraph" href="${ATLAS_URL}#graph/${encodeURIComponent(g[0])}/${g[1]}" target="_blank" rel="noopener">${escapeHtml(g[2])}</a>
        ${GRAPH_GLYPH}
        <p class="side-note">${graphN[gTop]} of this exam’s questions · on ${escapeHtml(ATLAS_MAPS[g[0]] ? ATLAS_MAPS[g[0]][0] : g[0])}</p>
        <span class="side-links"><a href="${ATLAS_URL}#graph/${encodeURIComponent(g[0])}/${g[1]}" target="_blank" rel="noopener">Open the graph</a><a href="#atlascards/${encodeURIComponent(g[3].join(','))}/${encodeURIComponent(g[2])}">Practice its questions</a></span>
      </section>` : ''}`;
  });
}
// a small generic graph sketch for graph tiles (decorative; the real graph is in the atlas)
const MOVE_GLYPH = '<svg class="g-glyph m-glyph" viewBox="0 0 220 70" aria-hidden="true"><path class="ax" d="M10 35H210"/><circle class="c1" cx="60" cy="35" r="7"/><circle class="c2" cx="120" cy="35" r="7"/><circle class="c1" cx="180" cy="35" r="7"/></svg>';
const GRAPH_GLYPH = '<svg class="g-glyph" viewBox="0 0 220 70" aria-hidden="true"><path class="ax" d="M14 4V62H214"/><path class="c1" d="M14 50C60 50 84 14 130 12S200 10 212 10"/><path class="c2" d="M14 60C80 60 130 48 212 30"/></svg>';

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
  const splitCards = splitCardsHtml(examNumber, 'using the timer setting below');

  main.innerHTML = `
    <button class="back-link" id="backExam">&larr; Exam ${examNumber}</button>
    <h1>Build a Practice Exam</h1>
    <p class="subtitle">Mirror the real exam's structure, or customize the mix.</p>
    ${splitCards ? `
    <div class="section-label">One-Click Presets</div>
    ${splitCards}
    <div class="section-label">Custom Mix</div>` : ''}
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
  // A split card here starts right away, using this page's timer setting.
  main.querySelectorAll('.split-card').forEach(card => {
    card.addEventListener('click', () => {
      const preset = findSplitPreset(card.dataset.split);
      if (!preset) return;
      const { timed, minutesPerQuestion } = currentSettings();
      startSplit(preset, { timed, secondsPerQuestion: minutesPerQuestion * 60 });
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
  if (s.splitId) {
    const split = findSplitPreset(s.splitId);
    return split ? split.name : 'Objective Split';
  }
  const preset = s.presetId ? findFinalPreset(s.presetId) : null;
  if (s.presetId) return `Final Exam — ${preset ? preset.name : 'Preset'}`;
  return s.isFinal ? 'Final Exam Simulation' : `Exam ${s.examNumber} Simulation`;
}
function examScoreKey(s) {
  if (s.splitId) return `split-${s.splitId}`;
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

/* ── Objective splits (every objective once, configured per block) ────────
   A block can publish an exam that samples each learning objective of one exam
   in QUIZ_CONFIG.splitPresets: { id, name, exam, perObjective (default 1),
   extra (default 0) }. Every run draws `perObjective` random questions from
   each objective of each SDL in `exam`, in SDL then objective order, and puts
   `extra` more at the end, drawn at random from the rest of that exam's pool —
   or, with `extraExams: [1]`, one each from that many random objectives of those
   earlier exams (a cumulative review slice; `extraLabel` names it, e.g. "Week 1").
   Trial batches (isTrialQ) are left out as everywhere else, but High-Yield Only Mode is
   ignored: the split's size is set by the objective count, and some objectives
   have no high-yield questions at all. Blocks without splits see no change. */
function splitPresets() {
  const list = Array.isArray(QUIZ_CONFIG.splitPresets) ? QUIZ_CONFIG.splitPresets : [];
  return list.filter(p => p && p.id && p.name && DATA.exams.some(e => e.examNumber === p.exam));
}
function findSplitPreset(id) {
  return splitPresets().find(p => p.id === id) || null;
}
function splitPerObjective(preset) {
  return Number.isFinite(preset.perObjective) && preset.perObjective >= 1 ? Math.floor(preset.perObjective) : 1;
}
function splitExtra(preset) {
  return Number.isFinite(preset.extra) && preset.extra > 0 ? Math.floor(preset.extra) : 0;
}
// One group per objective that has questions: { sdl, objective, questions }.
function splitObjectiveGroups(preset) { return examObjectiveGroups(preset.exam); }
const splitExtraExams = preset => Array.isArray(preset.extraExams) && preset.extraExams.length ? preset.extraExams : null;
function examObjectiveGroups(examNumber) {
  const exam = DATA.exams.find(e => e.examNumber === examNumber);
  if (!exam) return [];
  const groups = [];
  exam.sdls.slice().sort((a, b) => a.sdlNumber - b.sdlNumber).forEach(sdl => {
    const byObjective = new Map();
    sdl.questions.forEach(q => {
      if (isTrialQ(q)) return;
      if (!byObjective.has(q.objective)) byObjective.set(q.objective, []);
      byObjective.get(q.objective).push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title }));
    });
    Array.from(byObjective.keys()).sort((a, b) => a - b).forEach(objective => {
      groups.push({ sdl, objective, questions: byObjective.get(objective) });
    });
  });
  return groups;
}
// How many objectives the split covers, and how many questions a run holds.
function splitCounts(preset) {
  const groups = splitObjectiveGroups(preset);
  const per = splitPerObjective(preset);
  const core = groups.reduce((s, g) => s + Math.min(per, g.questions.length), 0);
  const xs = splitExtraExams(preset);
  const pool = xs ? xs.reduce((s, n) => s + examObjectiveGroups(n).length, 0) + core   // one per earlier-exam objective
    : groups.reduce((s, g) => s + g.questions.length, 0);
  const extra = Math.min(splitExtra(preset), pool - core);
  return { objectives: groups.length, core, extra, total: core + extra };
}
function buildSplitQuestions(preset) {
  const per = splitPerObjective(preset);
  const core = [], rest = [];
  splitObjectiveGroups(preset).forEach(g => {
    const picked = shuffle(g.questions);
    core.push(...picked.slice(0, per));
    rest.push(...picked.slice(per));
  });
  const xs = splitExtraExams(preset);
  if (xs) return core.concat(shuffle(xs.flatMap(n => examObjectiveGroups(n))).map(g => shuffle(g.questions)[0]).slice(0, splitExtra(preset)));
  return core.concat(shuffle(rest).slice(0, splitExtra(preset)));
}
function startSplit(preset, { timed = true, secondsPerQuestion = 90 } = {}) {
  if (loadExamSessionSnapshot() && !confirm('Start a new exam? The exam you have in progress will be discarded.')) return;
  const questions = buildSplitQuestions(preset);
  if (questions.length === 0) {
    alert(`No questions are available for ${preset.name}.`);
    return;
  }
  beginExamSession(preset.exam, questions, { splitId: preset.id, timed, secondsPerQuestion });
}
// e.g. "1 question from each of Exam 1's 47 objectives + 3 random · 50 questions"
function splitSummary(preset) {
  const per = splitPerObjective(preset);
  const { objectives, extra, total } = splitCounts(preset);
  const xs = splitExtraExams(preset);
  return `${per} question${per === 1 ? '' : 's'} from each of Exam ${preset.exam}'s ${objectives} objectives${extra ? ` + ${extra} ${xs ? `${preset.extraLabel || 'Exam ' + xs.join(' & ')} review` : 'random'}` : ''} · ${total} questions`;
}
// Cards for the home screen, or for one exam's pages when examNumber is given.
// `note` is appended to the label, e.g. on the exam setup page.
function splitCardsHtml(examNumber, note) {
  return splitPresets().filter(p => examNumber == null || p.exam === examNumber).map(p => {
    const score = getScore(`split-${p.id}`);
    return `
    <div class="action-card split-card" data-split="${escapeHtml(p.id)}">
      <span class="icon">&#127919;</span>
      <div>
        <div class="sdl-title">${escapeHtml(p.name)}</div>
        <div class="action-label">${escapeHtml(splitSummary(p))}${note ? `, ${note}` : ''}${score ? ` · Last: ${score.last.correct}/${score.last.total}` : ''}</div>
      </div>
    </div>`;
  }).join('');
}
function bindSplitCards() {
  main.querySelectorAll('.split-card').forEach(card => {
    card.addEventListener('click', () => setRoute(`split/${encodeURIComponent(card.dataset.split)}`));
  });
}

function renderSplitSetup(id) {
  const preset = findSplitPreset(id);
  if (!preset) { renderHome(); return; }
  const per = splitPerObjective(preset);
  const { objectives, core, extra, total } = splitCounts(preset);
  const settings = loadSettings();
  const score = getScore(`split-${preset.id}`);

  const bySdl = new Map(); // sdlNumber -> { title, objectives, questions }
  splitObjectiveGroups(preset).forEach(g => {
    const row = bySdl.get(g.sdl.sdlNumber) || { title: g.sdl.title, objectives: 0, questions: 0 };
    row.objectives++;
    row.questions += Math.min(per, g.questions.length);
    bySdl.set(g.sdl.sdlNumber, row);
  });
  const rows = Array.from(bySdl.values())
    .map(r => `<tr><td>${escapeHtml(r.title)}</td><td>${r.objectives}</td><td>${r.questions}</td></tr>`)
    .join('');
  const extraPositions = extra === 1 ? `question ${total}` : `questions ${core + 1}–${total}`;
  const xs = splitExtraExams(preset), xName = preset.extraLabel || (xs ? `Exam ${xs.join(' & ')}` : '');
  const extraWhere = xs ? `from ${extra} different random objectives of ${xName} (Exam ${xs.join(' & ')}) — ${Math.round(100 * extra / total)}% of the run` : `at random from the rest of Exam ${preset.exam}`;

  main.innerHTML = `
    <button class="back-link" id="backHome">&larr; Home</button>
    <h1>${escapeHtml(preset.name)}</h1>
    <p class="subtitle">Every objective in Exam ${preset.exam}: ${per} random question${per === 1 ? '' : 's'} from each of its ${objectives} objectives, in SDL order (${core} questions)${extra ? `, then ${extra} more picked ${extraWhere} as ${extraPositions}` : ''}. ${total} questions in all, drawn fresh every run.</p>
    ${score ? `<p class="setup-hint">Last run: ${score.last.correct}/${score.last.total}${score.best.correct === score.last.correct && score.best.total === score.last.total ? '' : ` · Best: ${score.best.correct}/${score.best.total}`}</p>` : ''}
    ${settings.hyOnly ? '<p class="setup-hint">⚡ High-Yield Only Mode does not apply here: this split always covers every objective, including those with no high-yield questions.</p>' : ''}
    <div class="setup-card">
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
        ${settings.examInstantFeedback ? '<div class="setup-hint">📝 Instant Feedback is ON — answers are revealed after each question.</div>' : ''}
      </div>
      <button class="btn" id="startSplitBtn" style="width:100%; margin-top:10px;">Start ${escapeHtml(preset.name)}</button>
    </div>

    <div class="section-label">What Each Run Draws</div>
    <table class="breakdown-table">
      <thead><tr><th>SDL</th><th>Objectives</th><th>Questions</th></tr></thead>
      <tbody>
        ${rows}
        ${extra ? `<tr><td>${xs ? `${escapeHtml(xName)} review — one each from random Exam ${xs.join(' & ')} objectives` : `Random extras from any Exam ${preset.exam} SDL`}</td><td>—</td><td>${extra}</td></tr>` : ''}
        <tr><td><b>Total</b></td><td><b>${objectives}</b></td><td><b>${total}</b></td></tr>
      </tbody>
    </table>
  `;

  document.getElementById('backHome').addEventListener('click', () => setRoute(''));
  const timerToggle = document.getElementById('timerToggle');
  const minutesPerQInput = document.getElementById('minutesPerQInput');
  const timerMinutesRow = document.getElementById('timerMinutesRow');
  const timerReadout = document.getElementById('timerReadout');

  function updateTimerReadout() {
    const timed = timerToggle.checked;
    timerMinutesRow.style.opacity = timed ? '1' : '0.45';
    minutesPerQInput.disabled = !timed;
    if (!timed) { timerReadout.textContent = 'No time limit'; return; }
    const minutesPerQ = Number(minutesPerQInput.value) || 1.5;
    timerReadout.textContent = `~${Math.round(total * minutesPerQ)} min total`;
  }
  timerToggle.addEventListener('change', updateTimerReadout);
  minutesPerQInput.addEventListener('input', updateTimerReadout);
  updateTimerReadout();

  document.getElementById('startSplitBtn').addEventListener('click', () => {
    const minutesPerQuestion = Number(minutesPerQInput.value) || 1.5;
    startSplit(preset, { timed: timerToggle.checked, secondsPerQuestion: minutesPerQuestion * 60 });
  });
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
  const trialCounts = TRIAL_KEYS.map(b => [b, visible.filter(q => q.batch === b).length]).filter(([, n]) => n);
  const classicBoth = batch1Count > 0 && batch2Count > 0;

  // Build the list of selectable options. If there's only one, skip the picker entirely.
  const options = [];
  if (batch1Count) options.push({ key: '1', title: 'Batch 1 — Quick Recall', meta: `${batch1Count} questions`, scoreKey: `sdl-${sdlNumber}-b1` });
  if (batch2Count) options.push({ key: '2', title: 'Batch 2 — Deep Vignettes', meta: `${batch2Count} questions`, scoreKey: `sdl-${sdlNumber}-b2` });
  if (classicBoth) options.push({ key: 'all', title: 'Both Batches', meta: `${batch1Count + batch2Count} questions`, scoreKey: `sdl-${sdlNumber}` });
  // Trial rows: an afterBatch2 trial goes right under Batch 2 (after any earlier trial row
  // placed there), otherwise at the end.
  let afterB2 = 0;
  trialCounts.forEach(([b, n]) => {
    const T = TRIAL_BATCHES[b];
    const trialOpt = { key: String(b), title: escapeHtml(T.title), meta: `${n} question${n === 1 ? '' : 's'} · ${escapeHtml(T.meta)}`, scoreKey: `sdl-${sdlNumber}-b${b}`, rowClass: T.rowClass };
    const b2 = options.findIndex(o => o.key === '2');
    if (T.afterBatch2 && b2 >= 0) options.splice(b2 + 1 + afterB2++, 0, trialOpt); else options.push(trialOpt);
  });

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
    <div class="sdl-row ${opt.rowClass || ''}" data-batch="${opt.key}">
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
    ${trialCounts.map(([b]) => TRIAL_BATCHES[b].hint ? `<p class="setup-hint" style="margin-top:14px;">${escapeHtml(TRIAL_BATCHES[b].hint)}</p>` : '').join('')}
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
        trialBatch: snap.trialBatch || (snap.isBloom ? 3 : 0),
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

  let questions = baseQuestions.filter(q => !isTrialQ(q)); // default/"all": classic batches only, never a trial
  let scoreKey = `sdl-${sdlNumber}`;
  let isBloom = false;
  let trialBatch = 0;

  if (TRIAL_BATCHES[batch]) {
    trialBatch = Number(batch);
    questions = baseQuestions.filter(q => q.batch === trialBatch);
    scoreKey = `sdl-${sdlNumber}-b${trialBatch}`;
    isBloom = trialBatch === 3;
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
    trialBatch,
    questions,
    index: 0,
    records: new Array(questions.length).fill(null), // {letter, confidence, correct} once answered, per question
    struck: {},
    pendingLetter: null, // letter chosen but not yet confirmed with a confidence rating (current question only)
  };
  renderPracticeQuestion();
}

/* ── "On the Lesion Atlas" beside a practice question (design J) ─────────
   Once a question is answered, the panel shows its best linked card itself — the
   card's subtitle, the opening of its mechanism, a buzzword, its sources and First
   Aid pages (resources/atlas-cards.js, built by tools/build-atlas.py, loaded after
   the first answer) — with links to open it on its map, practice it, and the usual
   atlas links (other cards, See it on a graph, You picked / Compare). Before an
   answer it only says what will appear, so it never gives the answer away. */
let ATLAS_CARDS_READY = null;
function loadAtlasCards() {
  if (ATLAS_CARDS_READY) return ATLAS_CARDS_READY;
  ATLAS_CARDS_READY = new Promise(resolve => {
    if (window.ATLAS_CARDS) return resolve(window.ATLAS_CARDS);
    if (!APP_SRC) return resolve(null);
    const s = document.createElement('script');
    s.src = new URL('../resources/atlas-cards.js', APP_SRC).href;
    s.async = true;
    s.onload = () => resolve(window.ATLAS_CARDS || null);
    s.onerror = () => resolve(null);
    document.head.appendChild(s);
  });
  return ATLAS_CARDS_READY;
}
// the first map a card is pinned on — its home in the atlas
function atlasHomeMap(id) {
  for (const m of Object.keys(ATLAS_MAPS || {})) if ((ATLAS_MAPS[m][1] || []).includes(id)) return m;
  return null;
}
const ATLAS_KIND = { dz: 'Disease', drug: 'Drug', reg: 'Regulation', tox: 'Toxicity', org: 'Organism', gene: 'Gene', enz: 'Enzyme' };
function atlasRailHtml(q, picked) {
  if (!ATLAS_URL) return '';
  const cards = atlasLinksFor(q);
  const more = atlasLinksHtml(q, picked);
  const c = cards[0];
  if (!c) return more || `<div class="rail-wait"><span class="kicker">On the Lesion Atlas</span><p>No atlas card is linked to this question yet.</p></div>`;
  const d = window.ATLAS_CARDS && window.ATLAS_CARDS[c.id];
  const home = atlasHomeMap(c.id);
  const P = window.ATLAS_PRACTICE, bi = P ? (P.blocks || []).findIndex(b => b[0] === blockDirName()) : -1;
  const nHere = P && P.cards && P.cards[c.id] ? ((P.cards[c.id].find(x => x[0] === bi) || [0, 0])[1]) : 0;
  const href = `${ATLAS_URL}#${home ? encodeURIComponent(home) + '/' : ''}${encodeURIComponent(c.id)}`;
  return `<section class="rail-card" aria-labelledby="railCardH">
      <span class="kicker atlas-k">On the Lesion Atlas${ATLAS_KIND[c.k] ? ` · ${ATLAS_KIND[c.k]}` : ''}</span>
      <h2 id="railCardH"><a href="${href}" target="_blank" rel="noopener">${escapeHtml(c.n)}</a></h2>
      ${d && d[0] ? `<p class="rail-sub">${escapeHtml(d[0])}</p>` : ''}
      ${d && d[1] ? `<p class="rail-mech">${escapeHtml(d[1])}</p>` : ''}
      ${d && d[2] ? `<p class="rail-buzz">${escapeHtml(d[2])}</p>` : ''}
      ${d && (d[4].length || d[3]) ? `<p class="rail-src">${escapeHtml(d[4].join(' · '))}${d[3] ? `${d[4].length ? ' · ' : ''}First Aid p. ${escapeHtml(d[3])}` : ''}</p>` : ''}
      <span class="rail-actions"><a class="btn atlas" href="${href}" target="_blank" rel="noopener">Open on the map</a><a class="btn secondary" href="#atlas/${encodeURIComponent(c.id)}">Practice this card</a></span>
      <p class="rail-home">${home && ATLAS_MAPS[home] ? `Lives on <a href="${ATLAS_URL}#${encodeURIComponent(home)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[home][0])}</a>` : ''}${nHere ? `${home ? ' · ' : ''}${nHere} question${nHere === 1 ? '' : 's'} here link to it` : ''}</p>
    </section>
    ${more.replace('<b>On the Lesion Atlas</b>', '<b>Linked on the atlas</b>')}`;
}
// refill the panel once the card summaries (and the atlas terms) have loaded
function refreshRailWhenReady(q, picked) {
  Promise.all([ATLAS_READY, loadAtlasCards(), loadAtlasPractice()]).then(() => {
    const r = document.getElementById('qRail');
    if (r && r.dataset.q === String(q.id)) r.innerHTML = atlasRailHtml(q, picked);
  });
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
        <span class="letter">${letter}</span>${choiceBodyHtml(q, letter)}
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
    `;
  }

  const answeredSoFar = session.records.filter(r => r).length;
  const correctSoFar = session.records.filter(r => r && r.correct).length;
  const picked = answered && !record.correct ? record.letter : null;

  main.dataset.view = 'practice-q';
  main.innerHTML = `
    <div class="q-sub bleed">
      <div class="q-sub-in">
        <nav class="crumbs" aria-label="Breadcrumb"><a href="#">${escapeHtml(blockShort())}</a><span aria-hidden="true">/</span><a href="#exam-sdls/${session.examNumber}">Exam ${session.examNumber}</a><span aria-hidden="true">/</span><a href="#practice/${session.sdlNumber}">SDL ${session.sdlNumber}</a><span class="crumb-x">· ${escapeHtml(batchLabel(batchParamFromScoreKey(session.scoreKey || '')))}</span></nav>
        <span class="q-sub-r"><span class="quiz-progress">Question <b>${session.index + 1}</b> of ${total}</span><span class="quiz-score">Score <b>${correctSoFar}/${answeredSoFar}</b></span></span>
      </div>
      <div class="q-sub-bar"><i style="width:${(session.index / total) * 100}%"></i></div>
    </div>
    ${TRIAL_BATCHES[session.trialBatch || (session.isBloom ? 3 : 0)] ? `<div class="bloom-banner${session.trialBatch === 4 ? ' trial-alt-banner' : ''}">${escapeHtml(TRIAL_BATCHES[session.trialBatch || 3].banner)}</div>` : ''}
    <div class="qlayout${answered ? ' answered' : ''}">
      <div class="q-card">
        <div class="q-meta-row">
          <span class="q-objective">Objective ${q.objective ?? ''} ${q.isHighYield ? '<span class="hy-badge">&#9889; HIGH YIELD</span>' : ''} ${q.bloomLevel ? `<span class="bloom-badge">${escapeHtml(q.bloomLevel)}</span>` : ''}</span>
          <button class="flag-btn ${flagged ? 'flagged' : ''}" id="flagBtn">${flagged ? '★ Flagged' : '☆ Flag for review'}</button>
        </div>
        <div class="q-stem">${escapeHtml(q.stem)}</div>
        ${choiceListOpen(q)}${gridHeaderHtml(q, !answered)}${choicesHtml}</div>
        ${confidenceHtml}
        ${feedbackHtml}
      </div>
      <aside class="q-rail" id="qRail" data-q="${escapeHtml(String(q.id))}" aria-label="On the Lesion Atlas">${answered ? atlasRailHtml(q, picked)
        : '<div class="rail-wait"><span class="kicker">On the Lesion Atlas</span><p>Answer to see where this question lives on the atlas — its card, its map and its graph.</p></div>'}</aside>
      <div class="next-row q-nav">
        <button class="btn secondary" id="prevBtn" ${session.index === 0 ? 'disabled' : ''}>&larr; Previous</button>
        ${answered ? `<button class="btn" id="nextBtn">${session.index + 1 < total ? 'Next question &rarr;' : 'Finish'}</button>` : '<span></span>'}
      </div>
    </div>
  `;
  if (answered && !(window.ATLAS_CARDS && ATLAS_INDEX && window.ATLAS_PRACTICE)) refreshRailWhenReady(q, picked);

  document.getElementById('flagBtn').addEventListener('click', () => {
    toggleFlag(q.id);
    renderPracticeQuestion();
  });
  document.getElementById('prevBtn').addEventListener('click', () => {
    if (session.index > 0) {
      session.index--;
      session.pendingLetter = null;
      renderPracticeQuestion();
      window.scrollTo(0, 0);
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
          window.scrollTo(0, 0);
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
   `isFinal`, `presetId` and `splitId` just change labeling/back-navigation/score-key —
   the question composition itself is already handled by the caller
   (buildCustomExamQuestions, buildPresetExamQuestions or buildSplitQuestions). */
function beginExamSession(examNumber, questions, { isFinal, presetId = null, splitId = null, timed = true, secondsPerQuestion = 90 } = {}) {
  const totalSeconds = timed ? questions.length * secondsPerQuestion : null;
  const deadlineAt = timed ? Date.now() + totalSeconds * 1000 : null;

  session = {
    mode: 'exam',
    examNumber,
    isFinal: !!isFinal,
    presetId,
    splitId,
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
    splitId: snap.splitId || null,
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
        <span class="letter">${letter}</span>${choiceBodyHtml(q, letter)}
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
      ${atlasLinksHtml(q, isCorrect ? null : selected)}
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
      ${choiceListOpen(q)}${gridHeaderHtml(q, !locked)}${choicesHtml}</div>
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
        <div class="your-answer">Your answer: ${given ? `${given} — ${escapeHtml(choiceText(q, given, true))}` : '(no answer)'}</div>
        <div class="correct-answer">Correct answer: ${q.correct} — ${escapeHtml(choiceText(q, q.correct, true))}</div>
        <div class="info-block explanation"><b>Explanation</b>${escapeHtml(q.explanation)}</div>
        ${q.boardPrep ? `<div class="info-block boardprep"><b>Board Prep</b>${escapeHtml(q.boardPrep)}</div>` : ''}
        ${atlasLinksHtml(q, given)}
      </div>
    `).join('');

  main.innerHTML = `
    <h1>${session.splitId ? `${escapeHtml(examSessionLabel(session))} Results` : session.presetId ? escapeHtml(examSessionLabel(session).replace(/^Final Exam/, 'Final Exam Results')) : session.isFinal ? 'Final Exam Results' : `Exam ${session.examNumber} Simulation Results`}</h1>
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
      <button class="btn" id="doneBtn">${session.splitId ? `Back to ${escapeHtml(examSessionLabel(session))}` : session.isFinal ? 'Back to Home' : `Back to Exam ${session.examNumber}`}</button>
    </div>
  `;
  document.getElementById('doneBtn').addEventListener('click', () => setRoute(
    session.splitId ? `split/${encodeURIComponent(session.splitId)}` : session.isFinal ? '' : `exam-sdls/${session.examNumber}`));
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
        <span class="letter">${letter}</span>${choiceBodyHtml(q, letter)}
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
      ${atlasLinksHtml(q, record.correct ? null : record.letter)}
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
      ${choiceListOpen(q)}${gridHeaderHtml(q, !answered)}${choicesHtml}</div>
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

/* ── Practice from an atlas card ───────────────────────────────────────
   The atlas's "Practice" buttons open #atlas/<card id>. This block's questions
   that link to that card — by exactly the rule that shows atlas links under an
   answered question (atlasLinksFor) — run as a review-style session.
   tools/build-atlas.py counts them the same way for the buttons. */
function atlasPracticeQuestions(id) {
  const out = [];
  DATA.exams.forEach(e => e.sdls.forEach(sdl => sdl.questions.forEach(q => {
    if (atlasLinksFor(q).some(c => c.id === id)) {
      out.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: e.examNumber }));
    }
  })));
  return out;
}
function renderAtlasPractice(id, missedOnly) {
  const route = window.location.hash;
  main.innerHTML = `<p class="loading">Finding questions…</p>`;
  ATLAS_READY.then(() => {
    if (window.location.hash !== route) return;   // navigated away while loading
    const card = ATLAS_INDEX && ATLAS_INDEX.find(c => c.id === id);
    let qs = card ? atlasPracticeQuestions(id) : [];
    if (missedOnly && qs.length) {
      qs = onlyMissed(qs);
      if (!qs.length) {
        main.innerHTML = `
          <button class="back-link" id="backHome">&larr; Home</button>
          <h1>${escapeHtml(card.n)}</h1>
          <p class="empty-state">No misses left on this card — your latest try on each of its questions was right.</p>`;
        document.getElementById('backHome').addEventListener('click', () => setRoute(''));
        return;
      }
    }
    if (!qs.length) {
      main.innerHTML = `
        <button class="back-link" id="backHome">&larr; Home</button>
        <h1>${card ? escapeHtml(card.n) : 'Atlas practice'}</h1>
        <p class="empty-state">No questions in this block link to that atlas card yet.${ATLAS_URL && card ? ` <a href="${ATLAS_URL}#${encodeURIComponent(id)}">Back to the card</a>` : ''}</p>
      `;
      document.getElementById('backHome').addEventListener('click', () => setRoute(''));
      return;
    }
    session = {
      mode: 'review',
      queueLabel: 'Atlas — ' + card.n + (missedOnly ? ' · your misses' : ''),
      questions: shuffle(qs),
      index: 0,
      records: new Array(qs.length).fill(null),
      pendingLetter: null,
    };
    renderReviewQuestion();
  });
}

/* ── Atlas cards for one SDL ───────────────────────────────────────────
   #sdlcards/<sdl>: the atlas cards this SDL's questions link to (atlasLinksFor — the
   same rule as the links under an answered question), most-linked first, with the maps
   that hold most of them and your record on each card's questions. Read the cards, then
   drill the SDL. */
function renderSdlCards(sdlNumber) {
  const f = findSdl(sdlNumber);
  if (!f) { renderHome(); return; }
  const route = window.location.hash;
  main.innerHTML = `<p class="loading">Finding cards…</p>`;
  ATLAS_READY.then(() => {
    if (window.location.hash !== route) return;
    const qs = f.sdl.questions, last = lastAttemptMap(), tally = new Map();
    let linked = 0;
    qs.forEach(q => {
      const cs = atlasLinksFor(q);
      if (cs.length) linked++;
      cs.forEach((c, i) => {
        const t = tally.get(c.id) || { c, n: 0, top: 0, ans: 0, ok: 0 };
        t.n++; if (i === 0) t.top++;
        if (last[q.id]) { t.ans++; if (last[q.id].correct) t.ok++; }
        tally.set(c.id, t);
      });
    });
    const rows = [...tally.values()].sort((a, b) => b.top - a.top || b.n - a.n || a.c.n.localeCompare(b.c.n));
    const back = `<button class="back-link" id="backList">&larr; Exam ${f.examNumber}</button>`;
    if (!rows.length) {
      main.innerHTML = `${back}<h1>Atlas cards</h1><p class="empty-state">No atlas cards link to ${escapeHtml(f.sdl.title)} yet.</p>`;
      document.getElementById('backList').addEventListener('click', () => setRoute(`exam-sdls/${f.examNumber}`));
      return;
    }
    const mapHits = Object.keys(ATLAS_MAPS || {}).map(m => {
      const on = new Set(ATLAS_MAPS[m][1] || []);
      return [m, rows.filter(r => on.has(r.c.id)).length];
    }).filter(x => x[1] > 1).sort((a, b) => b[1] - a[1]).slice(0, 4);
    const link = c => `<a class="atlas-link k-${c.k}" href="${ATLAS_URL}#${encodeURIComponent(c.id)}" target="_blank" rel="noopener"><span class="dot"></span>${escapeHtml(c.n)}</a>`;
    main.innerHTML = `${back}
      <h1>Atlas cards</h1>
      <p class="subtitle">${escapeHtml(f.sdl.title)} — ${rows.length} card${rows.length === 1 ? '' : 's'} linked from ${linked} of its ${qs.length} questions, most-linked first. Read them, then drill the SDL.</p>
      ${mapHits.length ? `<p class="sdlc-maps">Most of them sit on: ${mapHits.map(([m, n]) => `<a href="${ATLAS_URL}#${encodeURIComponent(m)}" target="_blank" rel="noopener">${escapeHtml(ATLAS_MAPS[m][0])}</a> <span class="sdlc-n">(${n})</span>`).join(' · ')}</p>` : ''}
      <ul class="sdlc-list">${rows.map(r => `<li class="sdlc-row">${link(r.c)}
        <span class="sdlc-n">${r.n} question${r.n === 1 ? '' : 's'}</span>
        ${r.ans ? `<span class="amap-acc ${r.ok / r.ans < 0.6 ? 'lo' : r.ok / r.ans < 0.8 ? 'mid' : 'hi'}" title="Your latest try on this card’s questions in this SDL">${r.ok}/${r.ans} right</span>` : ''}</li>`).join('')}</ul>
      <p class="sdlc-actions"><a class="amap-go" href="#practice/${sdlNumber}">Practice this SDL</a></p>`;
    document.getElementById('backList').addEventListener('click', () => setRoute(`exam-sdls/${f.examNumber}`));
  });
}
/* #sdlmissed/<sdl>: the SDL's questions you got wrong on your latest try, as a review run. */
function renderSdlMissed(sdlNumber) {
  const f = findSdl(sdlNumber);
  if (!f) { renderHome(); return; }
  const qs = onlyMissed(f.sdl.questions).map(q => Object.assign({}, q, { sdlNumber, sdlTitle: f.sdl.title, examNumber: f.examNumber }));
  if (!qs.length) {
    main.innerHTML = `
      <button class="back-link" id="backHome">&larr; Home</button>
      <h1>${escapeHtml(f.sdl.title)}</h1>
      <p class="empty-state">No misses left in this SDL — your latest try on each question you answered was right.</p>`;
    document.getElementById('backHome').addEventListener('click', () => setRoute(''));
    return;
  }
  session = {
    mode: 'review',
    queueLabel: f.sdl.title + ' · your misses',
    questions: shuffle(qs),
    index: 0,
    records: new Array(qs.length).fill(null),
    pendingLetter: null,
  };
  renderReviewQuestion();
}

/* ── Practice a whole atlas map ──────────────────────────────────────────
   "Practice this map" opens #atlasmap/<map id>: every question in this block that
   links to any card pinned on that map (atlas-terms.js lists each map's cards).
   tools/build-atlas.py counts them the same way for the map's buttons. */
function renderAtlasMapPractice(mapId, missedOnly) {
  const route = window.location.hash;
  main.innerHTML = `<p class="loading">Finding questions…</p>`;
  ATLAS_READY.then(() => {
    if (window.location.hash !== route) return;
    const entry = ATLAS_MAPS && ATLAS_MAPS[mapId];
    const ids = new Set(entry ? entry[1] : []);
    const qs = [];
    if (ids.size) DATA.exams.forEach(e => e.sdls.forEach(sdl => sdl.questions.forEach(q => {
      if (atlasLinksFor(q).some(c => ids.has(c.id))) {
        qs.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: e.examNumber }));
      }
    })));
    if (missedOnly && qs.length) {
      const miss = onlyMissed(qs);
      if (!miss.length) {
        main.innerHTML = `
          <button class="back-link" id="backHome">&larr; Home</button>
          <h1>${escapeHtml(entry[0])}</h1>
          <p class="empty-state">No misses left on this map — your latest try on each of its questions was right.</p>`;
        document.getElementById('backHome').addEventListener('click', () => setRoute(''));
        return;
      }
      qs.length = 0; miss.forEach(q => qs.push(q));
    }
    if (!qs.length) {
      main.innerHTML = `
        <button class="back-link" id="backHome">&larr; Home</button>
        <h1>${entry ? escapeHtml(entry[0]) : 'Atlas practice'}</h1>
        <p class="empty-state">No questions in this block link to the cards on that map yet.${ATLAS_URL && entry ? ` <a href="${ATLAS_URL}#${encodeURIComponent(mapId)}">Back to the map</a>` : ''}</p>
      `;
      document.getElementById('backHome').addEventListener('click', () => setRoute(''));
      return;
    }
    session = {
      mode: 'review',
      queueLabel: 'Atlas — ' + entry[0] + (missedOnly ? ' · your misses' : ''),
      questions: shuffle(qs),
      index: 0,
      records: new Array(qs.length).fill(null),
      pendingLetter: null,
    };
    renderReviewQuestion();
  });
}

/* ── Practice from an atlas graph ────────────────────────────────────────
   A graph's "Questions" chips open #atlascards/<card id,card id,…>/<graph title>: every
   question in this block that links to any card the graph illustrates (the atlas counts
   them from atlas-qlinks.js, built by the same linking rule). */
function renderAtlasCardsPractice(ids, title) {
  const route = window.location.hash;
  main.innerHTML = `<p class="loading">Finding questions…</p>`;
  ATLAS_READY.then(() => {
    if (window.location.hash !== route) return;
    const want = new Set(ids), name = title || 'Atlas graph', qs = [];
    DATA.exams.forEach(e => e.sdls.forEach(sdl => sdl.questions.forEach(q => {
      if (atlasLinksFor(q).some(c => want.has(c.id))) {
        qs.push(Object.assign({}, q, { sdlNumber: sdl.sdlNumber, sdlTitle: sdl.title, examNumber: e.examNumber }));
      }
    })));
    if (!qs.length) {
      main.innerHTML = `
        <button class="back-link" id="backHome">&larr; Home</button>
        <h1>${escapeHtml(name)}</h1>
        <p class="empty-state">No questions in this block link to the cards on that graph yet.</p>`;
      document.getElementById('backHome').addEventListener('click', () => setRoute(''));
      return;
    }
    session = {
      mode: 'review',
      queueLabel: 'Atlas — ' + name,
      questions: shuffle(qs),
      index: 0,
      records: new Array(qs.length).fill(null),
      pendingLetter: null,
    };
    renderReviewQuestion();
  });
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
        <span class="letter">${letter}</span>${choiceBodyHtml(q, letter)}
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
      ${atlasLinksHtml(q, record.correct ? null : record.letter)}
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
      ${choiceListOpen(q)}${gridHeaderHtml(q, !answered)}${choicesHtml}</div>
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

    if (!bySdl[a.sdlNumber]) bySdl[a.sdlNumber] = { correct: 0, total: 0, title: a.sdlTitle || sdlTitleFor(a.sdlNumber), sdlNumber: a.sdlNumber };
    bySdl[a.sdlNumber].total++;
    if (a.correct) bySdl[a.sdlNumber].correct++;

    const objKey = `${a.sdlNumber}-${a.objective}`;
    if (!byObjective[objKey]) byObjective[objKey] = { correct: 0, total: 0, sdlNumber: a.sdlNumber, objective: a.objective, label: a.objectiveLabel || objectiveLabelFor(a.sdlNumber, a.objective) };
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
        const splitId = key.startsWith('split-') ? key.slice('split-'.length) : null;
        const label = splitId ? examSessionLabel({ splitId }) : presetId ? examSessionLabel({ presetId }) : key === 'final-exam' ? 'Final Exam' : key.replace(/^exam-/, 'Exam ');
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
      <div class="sheet-answer">Correct answer: ${q.correct} — ${escapeHtml(choiceText(q, q.correct, true))}</div>
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
