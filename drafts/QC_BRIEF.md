# m39 QC — independent fact-check of the dynamic maps

Other agents wrote these maps; you are the independent checker. Nobody has verified their facts yet. A medical
student will study from them for COMLEX 1 / Step 1, so a wrong arrow or a wrong side is worse than a missing one.

Read first: drafts/SPEC_DYN.md (the map format and the rules the writers
followed), the top comment of drafts/tools/kit.js (what each field does), and
the "Sources" section of drafts/CARD_SPEC.md (where the corpus is).

## What to check, for each module you're given — every item, not a sample
1. **Notes** (`dyn.notes`): every sentence, for every key — mechanism, side effects, lab patterns, eponyms, numbers.
2. **Readouts**: for every option, does each ↑ / ↓ / ↔ (`mods` d = 1 / -1 / 0) match the sources? A readout with no
   mod shows "–"; that's fine where no source gives a direction. A wrong arrow is a must-fix.
3. **What each switch does to the drawing**: `block` (a drug hits it directly), `stop`, `low`, `boost`, `need`,
   flow `mods`, `shapes` with `when`. Is the right transporter/receptor/factor/tract hit, and nothing wrong hit?
   Is the direction of every ion/particle right (`ions` "in"/"out" relative to the label side `n`; `cross`)?
   Are structures in the right place (e.g. a receptor on the right membrane, a tract in the right column, the right
   side of a lesion's deficits, the right half of a visual field going dark)?
4. **Labels**: site labels/sublabels, node labels/subtitles, shape texts, panel rows and titles.
5. **New cards** written with card() in the module: every field, the fa pages, the link terms (no generic words).
6. **Sources**: the `fa` pages really cover the topic; `src` titles exist; panel titles name a real source.

Verify against the corpus the writers used: First Aid 2025 (the corpus (not on this branch) —
search ALL of FA, not just the cited page, before calling something unsupported; FA's text drops ↑/↓ arrows, so
never read a direction from FA text alone — confirm directions in a textbook), textbooks under corpus/, Bootcamp decks
(corpus/bootcamp), OCOM course texts (corpus/ and for OMM (OCOM drive, not on this branch) OMS 2/OMS2 Semester 1/OMM/_pipeline_midterm/sources/).
Where sources disagree, the writer may pick one and say so in the note — that's acceptable if the note says it.

## Fixing
- Edit the module file IN PLACE, minimally: fix wrong facts, wrong arrows, wrong targets/directions/sides; reword
  overstatements; delete what no source supports (or keep it if you found real support — cite it in `src`/`fa`).
- Don't redesign, rename ids, move things around or restyle. Keep text about the same length where you can.
- After editing, run `python3 -I drafts/tools/check.py <module>` — it must stay
  at 0 problems with no overlap warnings. If you changed what a state draws, `python3 -I drafts/tools/shot.py <module> --dyn <key>
  --look x0,y0,x1,y1` and look at it.
- Never edit anything outside your modules in drafts/maps/.

## Report (final message, under 400 words)
Per module: each change (where → what → why, with the source), anything you could not verify and left, anything that
looks wrong but you weren't sure enough to change. End with each module's final check.py line.
