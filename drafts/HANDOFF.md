# Drafts branch — handoff for a cloud session

You are continuing work on the **Lesion Atlas** inside the OCOM Question Hub (a med-school study site for COMLEX 1 /
Step 1). This branch (`drafts`) exists so map modules and site features can be drafted away from the Mac that holds the
sources. **Nothing on this branch deploys** — GitHub Pages serves `main`. The owner (Alonso) pulls this branch on the Mac,
fact-checks every map against the real sources, assembles, and pushes `main` himself.

## The site in one paragraph
`tools/atlas-src.html` is the atlas: ~2,170 cards (`id:{n:"…"` lines), 241 maps (`MAPS.<id> = {…}`), and the JavaScript —
including the **dynamic-maps kit** (between `/* ── Dynamic maps kit (art:"kit")` and `const ART={ kit:kitArt };`).
`python3 -I tools/build-atlas.py` builds `resources/metabolic-atlas.html` plus `resources/dyn/<map>.js` (each moving map's
drawing, loaded lazily), `atlas-terms.js` / `atlas-home.js` / `atlas-practice.js` / `atlas-qlinks.js` / `atlas-cards.js`, and
links the question bank (each block's `data.js`) to cards by link terms. The hub is `index.html`; block pages share
`shared/app.js` + `shared/style.css`; `sync.js` is the PIN sync; `sw.js` is offline. `PIPELINE.md` documents every feature.

## Rules that always apply
1. **Sources.** Every fact on a map or card must be supported by First Aid 2025, the textbooks (Costanzo, Guyton, Robbins,
   Katzung, Marks/Lippincott, Moore, Kaplan & Sadock, Fundamental Neuroscience, Langman…), Bootcamp decks or OCOM course
   texts. The corpus is NOT on this branch, so: cite the FA 2025 pages and textbook chapters you are confident of, and add a
   `# UNVERIFIED:` comment on anything you could not pin to a source. The Mac-side fact-checker reads the real corpus and
   will cut what it can't confirm. Never invent a page number to look sourced — leave `fa=''` instead.
2. Never copy Bootcamp practice questions. Never delete cards or questions.
3. Commit to **this branch only**; never push `main`. End commit messages with
   `Co-Authored-By: Claude <model name> <noreply@anthropic.com>`.
4. Before any commit, summarize what changed and wait for the owner to say "push" (he may also say "commit").
5. Keep `drafts/maps/` for new modules; `drafts/examples/` is read-only reference.

## Writing a moving map
- Read, in order: `drafts/SPEC_DYN.md` (the writer brief, with all addenda), the comment at the top of `drafts/tools/kit.js`
  (every `m.dyn` field), `drafts/CARD_SPEC.md` (card format + link-term rules), and one or two of `drafts/examples/`:
  `a_pvflow.py` (loop graph + sounds), `c_plexsim.py` (lesion simulator), `a_ironflow.py` (transporters), `d_coagflow.py`
  (lab-pattern readouts), `a_abtime.py` (time steps + drawn traces + mixed disorders).
- One module per map in `drafts/maps/<letter>_<id>.py`. Map ids must not equal a card id. Options are `[key, label, cardid]`.
  Pin existing cards (grep `tools/atlas-src.html` for names/synonyms) — write a new card only for a real gap.
- Check from the repo root: `python3 -I drafts/tools/check.py <module>` → must end **OK · 0 warnings** (0 problems, no
  overlap/outside warnings). Screenshots (`drafts/tools/shot.py … --dyn o:sw:key --look x0,y0,x1,y1`) need Chrome/Chromium;
  if none is installed the script says so — then rely on check.py's layout estimates and keep labels ≥ 30 px apart.
- Give every map 3–6 readouts (Predict mode), order options in teaching order (the Tour walks them), make every note stand
  alone (1–3 sentences; Name it shows it after an answer). Keep generic phrases out of link terms.
- Don't touch `tools/atlas-src.html` for a map — the Mac inserts modules with `dynlib.insert`. Leave a short
  `drafts/maps/REPORT.md` entry per map: id, switches, readout logic, cards pinned/new, sources, anything unsure.

## Site features (no sourcing needed)
Edit the kit inside `tools/atlas-src.html` directly, or `shared/app.js` / `index.html` / `shared/style.css`, then run
`python3 -I tools/build-atlas.py` and open `resources/metabolic-atlas.html` if you can (a static server + browser) to test.
Keep the kit's conventions: state lives in `DYN[v]` / `st`, controls are `data-dyn` keys handled by `dynSet`, phone sheet =
`dynSheetRender`, address = `dynStateStr`/`dynApplyStr`. Note in your report that the kit changed, so the owner copies the
new kit section back into his batch tooling (`drafts/tools/kit.js` here should be updated to match).

## What exists already (don't rebuild)
241 maps, 44 moving. Moving-map features: Predict the arrows, Tour (+Play), Name it (misses come back first; scores in
`mla-progress` and PIN-synced), Compare (+Pin B), Copy link, Moving-map mix (`#quiz/moving`, can stay in one topic), keys
(← → 1–4 Enter t n p c), "See it move" on cards and questions, Moving maps for this block (block home hero), weakest moving
maps on the Index, offline saving of `resources/dyn/*`. Moving maps so far: nephron, NMJ, monoamine synapse, action
potential, basal ganglia, spinal cord / brainstem / visual pathway / glomerular / lower-limb / brachial-plexus / pupil
simulators, cardiac AP, coagulation, alveolus, asthma, HPA, β cell, thyroid follicle, cochlea, gut absorption, bone, gout,
RA joint, viscerosomatic, lymphatic pump, bilirubin, iron, acid–base, antibiotics, MI locator, PV loop, edema, HIV,
menstrual cycle, shock, baroreflex, ECG, CAH, lipoproteins, heme, nucleotides, parietal cell, acid–base timeline.

## Backlog (pick from here unless told otherwise)
Maps: renal tubular acidosis simulator · thyroid function tests · anemia work-up flow · cranial nerve reflex arcs ·
visual-field/CN simulator upgrades · hypothalamic–pituitary axes side by side.
Acid–base timeline extras: ABG calculator (type pH/PaCO₂/HCO₃⁻ → disorder, compensation check, point on the graph) ·
acute-vs-chronic magnitude readout for Name it · Davenport tie-in.
Mix: missed list at the end (buttons open each missed state) · Predict questions inside the mix · length 5/10/20 ·
3-second Undo after a Name-it tap.

## Hand-back
When done: summary of modules/features, check.py lines, sources used, `# UNVERIFIED` count, and anything that touched the
kit. The owner then fact-checks on the Mac, assembles into `main`, runs the link compare and the browser overlap sweep,
and pushes.
