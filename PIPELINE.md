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

Edit the standalone, then rebuild:

    python3 tools/build-atlas.py /path/to/standalone.html

The script derives the map and lesion counts from the artifact itself, so the meta tags stay
honest. Update the matching counts on the atlas card in `index.html` by hand.

The build **refuses** rather than warns if it finds either of the two faults that have
shipped before, so you cannot deploy them by accident:

- **Markup in an escaped field.** `n`, `alias`, `enz`, `inh` and `buzz` go through `esc()`
  at render time, so a `<b>` in any of them prints as literal `<b>` in the side rail and on
  the card. `mech`, `find`, `labs` and `tx` are rendered as HTML and keep their emphasis.
  This one shipped once and affected 19 cards before anyone noticed.
- **Orphan cards and dangling pins.** A lesion card is invisible unless some node or edge
  pins it, and a pin naming a card that does not exist is a dead click.

Layout is still checked by hand — open the page and run the DOM audit in the console for
overlapping boxes, text overflowing its node, arrowheads buried under chips and pin fills.
The trap there: **`document.querySelector('svg')` grabs a toolbar icon, not the map.** The
map is `#svg`. An audit rooted on the wrong element finds zero nodes and reports "clean" for
every map, which it silently did for several sessions. Assert the node count is non-zero
before believing a clean result.

## Shared code

`shared/app.js` and `shared/style.css` are used by every block. A change there hits all of
them at once, so test more than one block. Each block folder holds only its `index.html`
(which sets `window.QUIZ_CONFIG`) and its own `data.js`.
