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
- `live.js` / `live.html` — same rendering for host (with tally bars) and participant views.
- `tools/build-atlas.py` — joins array choices before matching atlas terms.

## Demo
`nephro/grid-demo.html` + `nephro/grid-demo-data.js` (4 Nephro items, built by the pipeline's
`blocks/nephro/grid_demo/build_demo.py`). Not linked from the hub; own storageKey
(`nephro_griddemo`), so block counts, `build-atlas.py`'s practice index (it scans only hub-linked
`<block>/data.js`), cross-device sync and Live Session never see it.

Pipeline side (schema for `questions_sdlNN.js`, checker rules): `/workspace/pipeline/rules/PIPELINE_README.md`,
section "Grid (matrix) choices — PROTOTYPE".
