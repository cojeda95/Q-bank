# How work reaches the live site

Live: https://cojeda95.github.io/Q-bank/

## The one rule

**This clone (`~/Developer/Q-bank`) is the only source of truth.**
Do not create a second clone anywhere — especially not on `/Volumes/OCOM`. Git on an
external volume corrupts when the drive unmounts mid-write, and a second copy silently
drifts from this one.

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

## Shared code

`shared/app.js` and `shared/style.css` are used by every block. A change there hits all of
them at once, so test more than one block. Each block folder holds only its `index.html`
(which sets `window.QUIZ_CONFIG`) and its own `data.js`.
