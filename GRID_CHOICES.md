# Grid ("matrix") answer choices — PROTOTYPE

Branch `grid-choices-prototype` only (not on `main`, not pushed). AMBOSS-style "Which of the
following sets of findings…" items: one header row (e.g. `Serum osmolality | Urine osmolality |
Urine Na⁺`) and each choice A–E a row of `↑ / ↓ / normal` cells.

## Data schema (`<block>/data.js`, optional, backward compatible)
```json
{ "id": "…", "stem": "…",
  "grid": { "headers": ["Serum osmolality", "Urine osmolality", "Urine Na⁺"] },
  "choices": { "A": ["↓", "↓", "↓"], "B": ["↓", "↑", "↓"], "C": ["↓", "↑", "↑"], "D": ["↑", "↓", "normal"], "E": ["↑", "↑", "↓"] },
  "correct": "C", "explanation": "…", … }
```
A question without `grid` (every existing one) is untouched: `choices` stay strings and render
exactly as before (pixel-identical in the regression screenshots). A grid question's choice values
are arrays with one cell per header. Text fallback everywhere a choice is read as text: cells joined
`' / '` (`choiceText()`; results lists and the study sheet prefix each cell with its header). A soft
hyphen (`\u00AD`) in a header marks where a long word may break on a phone; it is dropped from text.

## Where it is handled
- `shared/app.js` — `isGridQ`, `choiceCells`, `choiceText`, `choiceBodyHtml`, `gridHeaderHtml`,
  `choiceListOpen`; used by the four question renderers (practice, exam simulation, flagged review,
  review/toughest/atlas queue) and by exam results, the study sheet and atlas-link matching.
  Letters, 🚫 strike-out, select/confirm, correct/incorrect highlighting, instant-feedback exams and
  dark mode are the existing code paths.
- `shared/style.css` — `.grid-choices`, `.grid-cells` (CSS grid, equal columns, `--grid-cols` set
  inline), `.grid-head-row`, `.strike-spacer`; phone tweaks under `max-width: 480px`.
  Arrow-only cells (`↑ ↓ ↔ ↑↑ ↓↓`) are wrapped in `.grid-arrow` and drawn large and bold (1.75rem,
  1.6rem on phones); `normal` and short text values keep the regular cell size.
- `live.js` / `live.html` — same rendering for host (with tally bars) and participant views.
- `tools/build-atlas.py` — joins array choices before matching atlas terms.

## Demo
`nephro/grid-demo.html` + `nephro/grid-demo-data.js` (4 Nephro items, built by the pipeline's
`blocks/nephro/grid_demo/build_demo.py`). Not linked from the hub; own storageKey
(`nephro_griddemo`), so block counts, `build-atlas.py`'s practice index (it scans only hub-linked
`<block>/data.js`), cross-device sync and Live Session never see it.

Pipeline side (schema for `questions_sdlNN.js`, checker rules): `/workspace/pipeline/rules/PIPELINE_README.md`,
section "Grid (matrix) choices — PROTOTYPE". Grid explanations refer to rows by letter
("Choice A (↓ serum osmolality, ↓ urine osmolality, ↓ urine Na⁺) is …"), never by a bare `↓ / ↓ / ↓`;
the site never reorders choices, so the letters in the data are the letters the student sees.

## Wave 1 on the Nephro site — trial batch 4 ("Trial: grid answer choices")
Ten grid questions (one each in SDLs 6, 9, 15, 18, 20, 25, 26, 28, 45, 46; ids `grid_sdlNN_q01`) live in
`nephro/data.js` as **batch 4**. No existing question was replaced. Batch 4 gets the same treatment as
the batch-3 short-stem trial:
- `shared/app.js`: `TRIAL_BATCHES` = { 3: BATCH3, 4: `QUIZ_CONFIG.batch4` (only where a block sets it) };
  `isTrialQ(q)` replaces the old `q.batch === 3` tests, so trial items stay out of exam totals, Full Exam
  Simulation, the Custom Exam Builder and objective splits. Neuro's Bloom Batch (batch 3, no batch4
  config) is unchanged.
- SDL picker: the batch-4 row (amber, `trial-alt-row`) sits right under the purple batch-3 row (or right
  under Batch 2 when an SDL has no batch 3); its own banner, hint and score key `sdl-N-b4`.
- SDL list meta: "12 questions · 🧪 3 trial questions · ▦ 1 grid trial".
- `live.js`: trial batches (≥ 3) are left out of the whole-exam id pools; batch 4 has its own label.
- Hub card: "1,122 questions + 46 trial" (36 short-stem + 10 grid).
- Pipeline source: `blocks/nephro/trial_grid/questions_grid_trial.js` → `make_grid_files.js` →
  `questions/questions_sdlNN_grid.js` (`gridQuestions`), loaded as batch 4 by `tools/lib/load_questions.js`.
The demo page (`nephro/grid-demo.html`) is kept for now; its SDL 15/20/45 items are the same
questions as `grid_sdl15/20/45_q01` under demo ids, and it can be deleted once the trial is reviewed.
