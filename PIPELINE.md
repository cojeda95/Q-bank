# How work reaches the live site

Live: https://cojeda95.github.io/Q-bank/

## The one rule

**This clone (`~/Developer/Q-bank`) is the only source of truth.**

The old hub paths on the external drive are now **symlinks pointing here**:

    /Volumes/OCOM/OMS 2/OMS2 Semester 1/Psych Block/Question Bank Hub  ->  ~/Developer/Q-bank
    /Volumes/OCOM/OMS 2/OMS2 Semester 1/Neuro Block/Question Bank Hub  ->  ~/Developer/Q-bank

So writing to either old path writes *here* — same file, same inode, not a copy. There is no
longer a wrong place to write. Do not replace those symlinks with real folders; a second copy
silently drifts, and git on a drive that unmounts mid-write corrupts the working tree.

`sync_hub_data.js` and `new_hub_block.js` additionally refuse to run if `HUB_ROOT` is not a
git clone, so a mistake fails loudly instead of writing questions somewhere they never
publish from.

## Where things live

| | |
|---|---|
| Question generation pipeline | `/Volumes/OCOM/OMS 2/OMS2 Semester 1/<Block>/_pipeline/` — stays on the external drive (~20 GB of PDFs, caches, generated files) |
| The website | this clone, ~21 MB |
| Handoff | `sync_hub_data.js` writes `data.js` straight into this clone |

The pipeline reads `$QBANK_HUB` (set in `~/.zshrc` to this directory). If it is ever unset,
the scripts fall back to their old relative path, so nothing breaks — it just writes to the
wrong place. Check `echo $QBANK_HUB` first if a sync seems to vanish.

## Publishing

    ./ship "what changed"     # commit everything, then push
    ./ship                    # push commits already made

Pushing to `main` triggers `.github/workflows/static.yml`, which deploys to GitHub Pages in
about 20-30 seconds. **A commit alone publishes nothing** — it has to be pushed.

### When a push says the repo is locked

A cowork session commits to this same clone, so a brief lock during a push is normal and
`./ship` just waits it out. Twice now that session has died mid-operation and left a lock
behind that nothing would ever clear, blocking every later push until it was moved by hand.

`./ship` now clears such a lock itself, but only one it can prove is abandoned — **all four**
of these must hold, or it leaves it alone and keeps waiting:

1. no `git` process is running at all
2. the lock file is **zero bytes** (git writes into a lock it is really using)
3. it is more than `STALE_AFTER` seconds old (120 by default)
4. nothing holds it open for writing — a read-only handle is Spotlight indexing, not git

Locks are **renamed, never deleted**, so even a wrong call is recoverable, and anything
cleared more than a day ago is tidied away on the next run. If you see the message about a
git process running, that is the guard doing its job: wait for the other session rather than
forcing it.

## The Lesion Atlas

`resources/metabolic-atlas.html` is a **build artifact — never hand-edit it.** It is the
standalone atlas wrapped in the hub shell: the blue "All Blocks" topbar, the site meta and
og tags, the mobile safe-area reset and the accent overrides that match the rest of the site.
Editing the deployed file directly, or copying the standalone over it, silently strips all of
that and the page loses its navigation.

The standalone source lives in the repo at **`tools/atlas-src.html`** — edit that, then rebuild:

    python3 tools/build-atlas.py

(Before 2026-09-22 the source lived only in a Claude session's temporary scratchpad, which a
reboot or a new session loses. Keep it in the repo.)

The script derives the map and lesion counts from the artifact itself, so the meta tags stay
honest. Update the matching counts on the atlas card in `index.html` by hand.

### What the build refuses

Every check below is a fault that shipped, or nearly shipped, before. They are silent at
runtime, so the build **refuses** rather than warns:

- **Markup in an escaped field.** `n`, `alias`, `enz`, `inh` and `buzz` go through `esc()`
  at render time, so a `<b>` in any of them prints as literal `<b>`. `mech`, `find`, `labs`
  and `tx` are rendered as HTML and keep their emphasis.
- **Orphan cards and dangling pins.** A card is invisible unless some node or edge pins it,
  and a pin naming a card that does not exist is a dead click.
- **Duplicate keys.** A JavaScript object keeps the *last* of two identical keys without a
  word, so a pasted-in duplicate card, map or pathway silently replaces the original.
- **Broken wiring**, found by `tools/atlas-check.js`, which the build runs under
  JavaScriptCore (`jsc`, built into macOS — no Node needed) against the real data: edges
  that end at a missing node, duplicate node ids, unknown pathway keys, ghost nodes that
  point at a missing map, maps with no tab, nodes or boxes off the canvas, unbalanced or
  stray tags in the HTML fields.
- **A card's first home moving.** A card pinned on several maps opens on its first home
  (the earliest map in `MAPS` definition order) from the Index and from `#card` links —
  including every question-bank link. **Define new maps last**, just before `const VIEWS`.
  `tools/atlas-homes.json` snapshots every card's home; if a build moves one, it stops and
  names it. Rebuild with `--accept-homes` only if the move is intended.

### Where a pin goes

A pin marks the step where a disease or drug **acts**. A drug's *side effect* goes on the
off-target mechanism that causes it, never on the drug's therapeutic target. The first
Antimicrobials map broke this — Long QT sat on the macrolide ribosome step (macrolides
prolong QT by blocking cardiac hERG channels, and clindamycin, which shares that step, does
not prolong QT at all). Those maps now carry a "Side effects — where they actually come
from" section with one node per real mechanism (hERG block, proximal tubule injury, MAO
inhibition, aldehyde dehydrogenase, UGT1A1, …) listing every drug that shares it.

### Topics in the top bar

The top bar shows broad topics (`TOPICS`, defined right after `VIEWS`); choosing one shows
its maps in a row beneath. A new map needs a `VIEWS` entry **and** a place in exactly one
topic — the build refuses a map that is in no topic or in two.

Add each new map to `NEW_MAPS` (next to `renderNav()`) with the date it goes live: for
three weeks it carries a "New" pill on its tab and a dot on its topic until the person
opens it (`mla-seen`, per device), and the Index lists it under What's new. A new feature
worth announcing gets a line in `WHATSNEW` the same way.

### Graphs on a map

A map can carry `plots:[{x,y,w,h,kind,t}]` — a schematic graph drawn by the engine, with a
row of variants (tap a chip to shift the curve). The kinds live in `PLOTS` in
`tools/atlas-src.html` (`pvloop`, `starling`, `odc`, `lungpv`, `glucose`);
`tools/atlas-check.js` keeps the same list and refuses an unknown kind or a plot off the
canvas. Every graph says on its face that it is schematic; its caption carries the sourced
facts, so check each caption against the map's sources like any card line.

### Links from the question bank

The build also writes `resources/atlas-terms.js`: each card's name, alias and its curated
`q:[...]` terms, normalized. `shared/app.js` loads it and, after a question is answered,
links the cards whose terms appear as a whole phrase in the correct answer or the first
sentence of the explanation. Later sentences and the board-prep note were tested and left
out — they mostly discuss wrong choices and differentials and linked the wrong cards.
When a card should be reachable from questions, give it a `q` list of the phrases questions
actually use (drug names, "beta blocker", "schizophrenia") and avoid broad words
("parasympathetic", "chorea", "seizures") that appear in unrelated questions. The
normalizer exists twice — `atlas_norm()` in the build and `atlasNorm()` in `app.js` — so
change both together.

Two traps found when the neuro, bone, reproduction and bacteria maps were added:

- **Parentheses in a card name become a term** when they hold capitals, so
  "Oculomotor (CN III) palsy" linked every question that mentioned CN III. Put an
  abbreviation in `alias` ("CN III palsy") instead.
- **Acronyms that mean something else elsewhere**: "egfr" is also eGFR (kidney function),
  "ctla 4" appears in every abatacept question, "gnas" covers pseudohypoparathyroidism as
  well as McCune-Albright, "jak2" is ordinary growth-hormone signaling. Use the specific
  phrase ("egfr mutation", "anti ctla 4", "jak2 v617f").

After adding cards, count which questions in every block would link to them (serve the
repo, open any block, call `atlasLinksFor(q)` over its `data.js`) and read the terms
behind the biggest counts.

### Practice buttons on atlas cards

Links also run the other way. The build writes `resources/atlas-practice.js`: for every
card, how many questions in each block link to it, counted by a Python copy of
`atlasLinksFor()` (the same zones, the same top-3 rule). Each card's drawer shows a
**Practice** section with one button per block ("Rheum · 30"); a button opens
`<block>/index.html#atlas/<card id>`, where `app.js` finds those questions with
`atlasLinksFor()` itself and runs them as a review session. The counts only refresh when
the build runs, so **re-run `python3 tools/build-atlas.py` after syncing new questions**
and ship `resources/atlas-practice.js` with them — a stale count is harmless (the session
always uses the live questions) but reads wrong. Blocks are discovered from the hub's
block links; give a new block a short label in `SHORT` in the build. The standalone
`tools/atlas-src.html` has no practice file, so it shows no Practice section.

If `atlas_norm()`/`atlasNorm()` or the linking rule changes, change the build's
`links_for()` too; the check is to count per card in every block in the browser and
compare with `atlas-practice.js` — they matched exactly (0 of 8 blocks off) when this
was added.

Deep links work anywhere: `metabolic-atlas.html#abx` opens a map,
`#abx/vancomycin` a card on that map, `#vancomycin` a card on its first home.

### Layout

Layout is still checked in the browser. Serve the repo (`python3 -m http.server`), open the
atlas, and load the auditor from the console:

    (0,eval)(await (await fetch('/tools/atlas-audit.js')).text()); __auditAll()

It reports overlapping boxes, text overflowing its node, arrowheads buried under chips,
labels sitting nearer another edge than their own, pin fills and off-canvas items, for every
map in both themes. The trap: **`document.querySelector('svg')` grabs a toolbar icon, not
the map.** The map is `#svg`. An audit rooted on the wrong element finds zero nodes and
reports "clean" for every map, which it silently did for several sessions — the auditor now
refuses a zero-node result.

## Shared code

`shared/app.js` and `shared/style.css` are used by every block. A change there hits all of
them at once, so test more than one block. Each block folder holds only its `index.html`
(which sets `window.QUIZ_CONFIG`) and its own `data.js`.

### Dark mode

`shared/theme.js` and `shared/theme.css` give every page a ◐ light/dark toggle in its top
bar. The choice is saved under the Lesion Atlas's key (`mla-theme`), so one switch covers
the hub, every block, Live Session, the OMM explorer and the atlas; light is the default.
Every page needs both in its `<head>`, after its own stylesheet — a new block's
`index.html` included:

    <link rel="stylesheet" href="../shared/theme.css">
    <script src="../shared/theme.js"></script>

Colours in page CSS must come from the variables (`--text`, `--card-bg`, `--input-bg`,
`--navy`, `--navy-fill` for filled buttons, and so on — the full list is at the top of
`theme.css`), never hard-coded hex, or they will not change in dark mode. White text on the
top bar and on filled buttons is the exception. Dark applies on screen only, so printing
stays light.

### Final exam presets

A block can add one-click Final Exam presets that follow a real exam's announced
distribution. They go in that block's `QUIZ_CONFIG.finalPresets` in its `index.html`,
not in `app.js`, so other blocks are unaffected:

    finalPresets: [{
      id: 'williams',                       // score-history key: final-preset-williams
      name: "Dr. Williams' Distribution",
      source: 'where the numbers came from', // shown as the card's tooltip
      perSdl: { 1: [2, 3], 2: [2, 3], 3: [1, 2], 4: [5, 6] }
    }]

`perSdl` maps an exam number to the [min, max] questions drawn from **each** SDL in that
exam; every run picks a count in the range per SDL, and exams left out contribute nothing.
The card appears under Final Exam Simulation on the block's home page (one click, timed at
1.5 min per question) and at the top of the Final Exam page (using that page's timer
setting). Runs are scored and trended separately from the custom final. Psych's preset
comes from the course email of 2026-09-24; its Exams 1-4 are
weekly exams, so week N is Exam N.

### Objective splits

A block can also add an exam that covers every objective of one exam once. It goes in
that block's `QUIZ_CONFIG.splitPresets`:

    splitPresets: [{
      id: 'moorjani',        // route #split/moorjani, score-history key: split-moorjani
      name: 'Moorjani Split',
      exam: 1,               // which exam's SDLs to cover
      perObjective: 1,       // random questions drawn from each objective (default 1)
      extra: 3               // more random questions from the rest of that exam (default 0)
    }]

Each run takes the objective questions in SDL and objective order, then puts the extras
last. The card appears on the block's home page and on that exam's SDL list, where it opens
a page with the timer setting and a per-SDL count of what a run draws. It also sits under
One-Click Presets on that exam's simulation setup page (Full Exam Simulation), where one
click starts it with that page's timer setting. Bloom Batch is left
out as everywhere else, but High-Yield Only Mode is ignored: the split's size is set by
the objective count, and some objectives have no high-yield questions. Nephro's Moorjani
Split covers Exam 1 (SDLs 1-12, 47 objectives), so a run is 47 + 3 = 50 questions.

### Offline mode

`sw.js`, at the site root, is a service worker that `shared/theme.js` registers on every
page that loads it; the atlas registers it itself, since it doesn't load `theme.js`. It works
network first, so online visitors always get the newest files. Every same-origin file a
visitor opens is saved as it loads, so the hub, the atlas and any block they have opened
once keep working without signal. A page never opened before shows a short "you're offline"
notice. Requests to other sites (the Firestore sync, CDNs) pass straight through.

Nothing extra is needed when you publish. If a shared file is renamed, update the `CORE`
list at the top of `sw.js`, which pre-saves the hub, `shared/` and the atlas on first visit.
To throw away everyone's saved copies, change `CACHE` (`qhub-v1` → `qhub-v2`).

## Cross-device sync

`sync.js` (on the hub page) syncs every block's flags, scores, answers and settings through
Cloud Firestore, keyed by a 6-character PIN; there are no accounts. Push and Pull both merge
the device and the cloud first, so neither loses progress.

**One document per block**: `syncs/{PIN}_{block}`, e.g. `syncs/MGVMZA_nephro`. Firestore
rejects any document over 1 MiB. Until October 2026 everything lived in one document per
PIN, `syncs/{PIN}`, and since each answer carried its full objective text, a PIN filled up
after roughly 2,800 answers across all blocks and every Push failed with "exceeds the
maximum allowed size". Now:

- the cloud copy of each answer leaves out `sdlTitle` and `objectiveLabel`. Analytics in
  `shared/app.js` looks them up from `data.js` (`sdlTitleFor`, `objectiveLabelFor`), so
  answers pulled from another device still show their text. A block at the 5,000-answer
  cap is about 0.75 MB.
- if a block's document would still pass the limit, its oldest answers are left out of
  the cloud copy (never off the device that logged them) rather than the push failing.
- the old `syncs/{PIN}` document is still read and merged on every sync. Once a push has
  written every block, it is emptied to a `_migratedAt` marker. A device still running an
  older cached `sync.js` can write it again; the next push folds that back in.

A new block needs its storage key in `BLOCK_KEYS` in `sync.js`, or its progress won't sync.

**Lesion Atlas progress** (`mla-progress`: reviewed marks, quiz record, the spaced-review
schedule and question-bank misses) syncs in its own document, `syncs/{PIN}_atlas`, through
`mergeAtlas` in `sync.js`. Counts take the larger side; the schedule takes, card by card,
the side whose `at` timestamp (when that card's schedule last changed) is newer. Both the
atlas (`schedule()` in `tools/atlas-src.html`) and `atlasNoteAnswer` in `shared/app.js`
write `at` — keep them in step with `mergeAtlas`.

**"I know this"** marks and **starred cards** live in the same blob as `known` and `star`: the time a card was marked, or
minus the time it was unmarked, so `mergeAtlas` keeps whichever device acted last (larger
absolute value). A known card sits out every atlas quiz and the due list — `isWeak()` in the
atlas and the hub's due pill both skip it. Hiding known cards from the lists
(`mla-hideknown`) is per device and not synced.

Card review is **opt-in** (`mla-review` = `"on"`, per device, not synced). While it is off,
answers are still counted but nothing is scheduled, and no "due" message appears anywhere —
not the map rings, the Due cards round, the rail lists or the hub pill.
