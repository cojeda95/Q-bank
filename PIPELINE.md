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
- **An unknown source.** Every `src` entry must start with a known textbook or course
  name (`KNOWN_SRC` in the build — Robbins, Katzung, … `OCOM OMM`, `OCOM Ortho`,
  `OCOM Psych`, `Osmosis`). Add a new course's prefix there when its first card ships.
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
`tools/atlas-src.html` (`pvloop`, `starling`, `odc`, `lungpv`, `glucose`, `doseresp`, `elim`, `mm`,
`lb`, `flowvol`, `cofunc`, the action potentials `apnerve`, `apcond`, `apnodal`, `apventric`, and `wiggers`,
`menstrual`, `titration`, `lentension`, `forcevel`);
`tools/atlas-check.js` keeps the same list and refuses an unknown kind or a plot off the
canvas. Every graph says on its face that it is schematic; its caption carries the sourced
facts, so check each caption against the map's sources like any card line.

Layout (`plotSVG`): the chart takes the left ~62% of the frame (about 2.5:1, with light
gridlines at the ticks); a column on the right holds the variant chips (they wrap), the
caption (wrapped by `wrapWords`) and a legend. The chosen variant's curves get distinct
colours from `PSER` and their `lab` becomes the legend entry — label curves through `lab`,
not by placing text on the chart. Marker labels (`marks`, `drop`, `corners`, `x`/`y` lines)
carry a surface-coloured halo and flip to the left near the right edge.

A variant can also carry `bands: [[x0, x1, label]]` — shaded, numbered time windows drawn
behind the curves (alternate bands a shade darker), used for the phases of an action
potential — and `key: [[label, text]]`, rows under the caption with the label in a circle,
used to say which ions move through which channels in each numbered phase. Smooth curves
through a few keypoints come from `mono()`, a monotone cubic (Fritsch–Carlson), so a curve
never overshoots between points; the nerve, SA-node and ventricular shapes are built that
way (`AP_NERVE`, `nodal()`, `ventric()`). The key text is a sourced claim like any card line.
A key label longer than two characters ("ECG", "Vmax", "3–4") is drawn as a pill instead of a
circle.

A kind can add **strips**: `strips: [{yl, yr, h, d: V => [...]}]` — smaller charts stacked
under the main one that share its x axis (`h` px each; `yl` is a short label, about 10
characters, written in the left margin). `d(V)` gets the chosen variant and returns curves
(`{pts, lab, col}` — `col` overrides the colour, e.g. `var(--ink-2)` for an ECG) and text
(`{txt: [[x, label, y?]]}` — wave names, heart sounds). Bands span the whole stack, the x
ticks sit under the last strip, and strip curves join the legend. A variant can also carry
`events: [[x, label]]` — dashed lines through every strip, labeled at the top (valve
opening and closing on the Wiggers diagram). Place events where the drawn pressures actually
cross: the m29 batch computed them from the curves, since `mono()` smoothing moves a crossing
a little from its keypoints. Strips are used by `wiggers` (LV volume, ECG, heart sounds),
`apventric` (an ECG under the action potential, on a time axis starting at −150 ms so the P
wave shows) and `menstrual` (basal body temperature).
The Wiggers diagram shows three consecutive beats, as conventional diagrams do: each curve
is written as one 0.8-s beat of keypoints and repeated by `cyc()`; `wigMid()` moves the phase
bands and valve events onto the middle beat, and `wigEach()` repeats the ECG wave names and
heart sounds on every beat.

A kind can name its x ticks with `xtl: [...]` (one label per entry of `xt`) for a category
axis — the oxygen cascade's Air · Trachea · Alveoli · Arteries · Tissue fluid · Cells — or for
ends of a distance axis ("afferent end", "efferent end"). The m30 kinds: `glomcap` (Starling
pressures along the glomerular capillary from `glomP()`, Costanzo's 45/10/19→35 mm Hg, with
efferent and afferent constriction, more plasma flow, low plasma protein and obstruction),
`ecglytes` (one ECG beat from `ecgB()` for normal, high and low K⁺, high and low Ca²⁺, with
`events` marking the QRS start and T end), `pregweeks` (hCG, estrogens, progesterone and hCS by
week, plus corpus luteum vs placental progesterone), `vco2` and `vo2` (Guyton's ventilation
response curves), `o2cascade` (PO₂ from air to the cell at sea level, 20,000 ft and 30,000 ft —
points joined by straight lines, no `mono()`), `pthca` (PTH and calcitonin against plasma
calcium, Guyton Fig 80.14, with FHH, primary hyperparathyroidism and hypoparathyroidism) and
`hcvsero` (HCV RNA, ALT and anti-HCV after infection: clears, chronic, chronic then cured).

### Search abbreviations

`ABBR` in `tools/atlas-src.html` holds First Aid 2025's abbreviation list (pp. 747–757),
kept only where some card uses the meaning (the m23 batch script built it). A search that
is exactly one of them ("mi", "dka") matches the abbreviation as a whole word or any of its
meanings. Where First Aid defines an abbreviation differently from common use (RA = right
atrium), the list follows First Aid; add entries by hand only with a source.

### Per-device switches

`mla-hy` (High-yield only), `mla-hideknown`, `mla-seen` (New marks), `mla-streak`
(Daily mix: last finished day and streak length), `mla-text` (Aa text size), `mla-mini`
(overview map turned off), `mla-review` and `mla-recent` (the last 12 cards opened, newest
first — **Recently viewed** in the rail and on the Index) live in localStorage on each device
and are not synced; `mla-progress` (with `known` and `star`) syncs by PIN.

### Search inside the maps

Besides cards, a search lists matching **map boxes** (node label and caption) and **panel
rows** (`boxIndex`/`boxMatches`; word starts, whole words for three letters or fewer),
current map first. `goBox` opens the map, centres the spot and rings it (panel rows get a
highlight band). Panels render `data-panel`/`data-row` for this.

### Practice this map

`tools/build-atlas.py` writes each map's pinned card ids into `resources/atlas-terms.js`
(`maps: id -> [title, card ids]`) and, in `resources/atlas-practice.js`, how many questions
per block link to any card on the map (`maps: id -> [[block, n]]`, each question once). The
side panel and the Info sheet show a button per block that opens
`<block>/index.html#atlasmap/<map id>`, run by `renderAtlasMapPractice` in `shared/app.js`
with the same linking rule, so the counts match.

Each block's home page also lists **Maps for this block** (`fillAtlasMapsHome` in
`shared/app.js`), each with a link to the map and a Practice button for the same
`#atlasmap/<map id>` session. Every map also shows **your accuracy** on it
(`atlasMapAccuracy`): each question you have answered in the block counts toward every map
that holds one of its linked cards — the Practice rule again — scored on your latest try
(`lastAttemptMap`). Maps with at least `AMAP_MIN` (3) answers come first, weakest first;
the rest follow by that block's question count in `atlas-practice.js`. The block is read
from the page's folder name, which must match the block's first entry in `blocks` of
`atlas-practice.js` (the build takes it from the hub's block links).

A map you have missed questions on also gets **Redo N missed**, which opens
`#atlasmap/<map id>/missed`: the same linked questions, filtered to the ones whose latest
try was wrong (`onlyMissed` in `shared/app.js`). `#atlas/<card id>/missed` does the same
for one card. Both show an empty state when nothing is missed.

The block's SDL list (Exam N) gives every SDL an **Atlas cards** link to `#sdlcards/<sdl>`
(`renderSdlCards`): the cards its questions link to (`atlasLinksFor`, the same rule as the
links under an answer), most often top-linked first, with the maps holding several of them
and your latest-try record on each card's questions; a Practice button follows. The block
home shows **Your weakest SDLs** (`fillWeakSdlsHome`) above Maps for this block: every SDL
with at least `SDL_MIN` (3) answers, weakest first, each with Redo N missed
(`#sdlmissed/<sdl>`, `renderSdlMissed` — the SDL's questions wrong on your latest try, as a
review run), Atlas cards and Practice. Both routes have Continue-card labels in
`rememberPlace`.

### Taking the reader to a pin

`flashPins` → `centerOn` is the one path every search result, link and "Same pathway"
button uses. A pin on a node sits inside the node's own `translate()`, so its position is
read with `pinXY` (the transform chain up to the camera), never from the pin's transform
attribute — that mistake centred most searches near the map's top-left corner. `centerOn`
centres in `clearRect()` (the map left of the card panel on a wide screen, above the bottom
sheet on a phone) and zooms until pins are readable (`readScale`, larger with the Aa text
size). Several pins of one card on a map are framed together when they fit. The overview
map (`drawMini`/`miniView`, top right) appears only while zoomed in.

Text size (Aa) scales the card panel, side panel, Index, walk and quiz bars with CSS `zoom`.
Map labels do not scale: node boxes are sized from character counts, and enlarging the text
inside them collided on ten maps at +15% (115 findings at +30%) in the layout audit.

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

**The card's name base is always a term** (the part before " — "). A card named
"Insulin — receptor & metabolic effects" linked every answer containing "insulin"; name it
"Insulin receptor & metabolic effects" instead, so the whole phrase is the term.

**Link sweeps.** To raise an SDL's coverage without new cards, list its unlinked questions with
the cards whose text overlaps the answer most, then add an answer-only term (`"=…"`, a phrase
from the correct answer) only where the card already states that fact — or add a find line
from a source the card cites first. Answer-only phrases cannot pull in questions that merely
mention the topic. The m30 sweep (Chapman points, osteoarthritis and JIA, cortisol actions,
surfactant and ventilation, prostate, visual fields and pupils, fractures) linked 45 more
questions. A card with an empty `q:[]` takes the first term without a leading comma — the
build's JSON parse fails on `[,"…"]`.

**You picked.** After a miss, `atlasLinksHtml(q, picked)` also matches the option the person
chose (`atlasPickedFor`): only its leading phrase — the text before the first comma, colon,
dash, "which", "because" and similar — so the reasoning in a long distractor does not pull
in passing mentions. If that option's best card is one already linked for the right answer,
nothing is shown (the option is a wrong statement about the same thing). Otherwise the card
appears under the links with **Compare with …**, which opens
`metabolic-atlas.html#cmp/<picked card>/<correct card>`: the atlas opens on the correct
card's home map with both cards side by side (`readHash` → `openCompare`). About one wrong
option in five gets a card.

**Every answer choice.** On single-answer questions the "You picked" line is replaced by a
table (`atlasChoicesHtml`) giving the card for every option: the right answer shows its top
linked card; each other option its own best card from its leading phrase
(`atlasOptionCard`, the same matching), or "same card as the answer" when that card is
already linked for the right answer; the row you picked carries the Compare link.
Select-all and grid questions keep the single "You picked" line.

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

The build also writes `resources/atlas-qlinks.js` (`window.ATLAS_QLINKS`): for every card,
the ids of the questions linked to it, per block. The atlas reads it with each block's
`<folder>_attempts_v1` on this device (`qbRecord` in `tools/atlas-src.html`) to show
**Your record** in the card's Practice section — "X of N right on your latest try" — a
per-block "a/b right" on each button, and **Redo n missed** linking to
`<block>/index.html#atlas/<card id>/missed`. The ids go stale the same way the counts do,
so ship `atlas-qlinks.js` with every rebuild. It is in `CORE` in `sw.js` and in the hub's
atlas file lists (Save all, the atlas tile's Save button and its offline check).

If `atlas_norm()`/`atlasNorm()` or the linking rule changes, change the build's
`links_for()` too; the check is to count per card in every block in the browser and
compare with `atlas-practice.js` — they matched exactly (0 of 8 blocks off) when this
was added.

Deep links work anywhere: `metabolic-atlas.html#abx` opens a map,
`#abx/vancomycin` a card on that map, `#vancomycin` a card on its first home, and
`#cmp/<a>/<b>` two cards side by side.

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

The hub's **Use Offline → Save all** button fetches every block's `index.html` and `data.js`
(from the hub's block links), the atlas files and `shared/`, and puts them straight into the
service worker's cache with the Cache API — so it works even on a first visit, before the
worker controls the tab. The cache name is written in the hub's script too: **if `CACHE` in
`sw.js` changes, change it in `index.html` as well**, or the saved copies land in a cache the
worker no longer reads (and its activate step deletes). The time of the last full save is
kept per device under `qhub-offline-at`. Pages needing a CDN (the sacral explorer's three.js)
are left out — they cannot work offline anyway.

**Block tiles** on the hub show, per device, your progress (questions answered and % right on
your latest try, read from each block's `<folder>_attempts_v1` — so a block's `storageKey`
must equal its folder name) and its offline status: *Saved offline* when its `index.html`
and `data.js` are in the cache (the atlas tile checks the three atlas files), *Not saved
offline* otherwise, and *Newer version online* when a saved file's size differs from the copy
online. Online size comes from a `HEAD` request — the size half of GitHub Pages'
`"mtime-size"` ETag, or `Content-Length` — because the mtime half (and `Last-Modified`)
changes for every file on every deploy. An edit that keeps a file's byte size identical is
not flagged. The same script fills the summary line under Save all, and reruns after a
save. It has its own copy of `CACHE` too.

Each tile also gets a **Save offline** button (`saveBtn` in the hub's script) when the block
is not saved or a newer version is online, and the device is online. It caches that block's
`index.html` and `data.js` (or the atlas files) plus `SHARED` — the hub, `shared/` and the
two atlas link files every block page loads — then re-runs the status check, so the chip
turns to *Saved offline* without saving every block.

**Exam readiness.** Under the progress chip, each tile shows one chip per exam you have
started: "Exam N · X% seen · Y% right" — questions answered (latest try per question, read
from the same attempt log; every attempt record carries `examNumber`) over that exam's
regular questions, and the share right. Totals come from `resources/qbank-counts.js`
(`window.QBANK_COUNTS`), written by `tools/build-atlas.py` from every block's `data.js`:
per block, the trial batches (3 always; 4 where the block's `index.html` defines `batch4`,
as `isTrialQ` does) and each exam's count of non-trial questions — they match the block's
exam cards. Re-run the build after syncing questions, as for `atlas-practice.js`. The file is
in `CORE` in `sw.js` and in the hub's Save all list.

**Exam countdown.** A collapsible card under Continue (`#countdownCard`) has one date field per
exam, built from `QBANK_COUNTS`; dates are kept on this device in `qhub-examdates`
(`{"<folder>:<exam>": "YYYY-MM-DD"}`). Each tile then shows "Exam N in D days · U new left ·
P/day" (amber `.bm.cd` chip, placed before the offline chips): U is the exam's regular
questions not yet answered on this device, P = ⌈U ÷ D⌉. Past dates show nothing; the card's
summary names the nearest upcoming exam.

**Continue where you left off.** Every block page records where you are (`rememberPlace`
at the end of `render()` in `shared/app.js`) under `qhub-last` in localStorage: the block
folder, its title, the hash and a readable label (the SDL title, "Exam N", review modes, or
"Atlas practice: <card or map>"). The hub's Continue card (`showContinue`) shows it with
how long ago it was, adds "question i of n" from `<folder>_practicesession_v1` when the saved
session matches, and links back to `<folder>/index.html<hash>`. It checks the folder against
the hub's tiles and the hash against a pattern before using either, and stays hidden when
nothing is saved.

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
