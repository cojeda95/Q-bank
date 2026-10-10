# m39 — dynamic maps: the brief for every map writer

You are building **drawn, moving maps** for the Lesion Atlas (a med-school study site, COMLEX 1 / Step 1).
The model is **Nephron in Motion**: a drawn nephron with every transporter on the wall, ions moving across it,
and switches (ADH, aldosterone, a diuretic, NSAID / ACE inhibitor / ANP / sympathetic) that change what moves,
block transporters with a ✕, narrow vessels, and read out GFR / RPF / FF ↑↓. Your maps work the same way.

**Never edit** anything outside drafts/maps/ (read the rest of the repo only). If the kit lacks something you need, work around it with
plain SVG shapes and say so in your report — don't change the kit.

## Read first
1. The kit's documentation and code: drafts/tools/kit.js (the comment at the
   top defines every field of `m.dyn`; the code shows exactly how each is drawn).
2. The worked example: drafts/examples/a_ironflow.py — the whole nephron as kit data
   (`sites`, `flows`, `MODS`, `shapes`, `dyn`, notes, readouts). Copy its style.
3. Card format and sourcing rules: drafts/CARD_SPEC.md (sources, `card()`,
   link terms). Everything there applies to any new card you write.

## Your module (one file per map, e.g. `a_nmjflow.py`)
```python
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full          # only if you write new cards
KZ = {c: full('Katzung', c) for c in (6, 7, 27)}

MAP = dict(
  id='nmjflow', title='Neuromuscular Junction in Motion', topic='neuro', after='synapse',
  sub='<one line: what moves and what the switches do — ends with "Tap a receptor for its card">',
  w=3500, h=2100,                        # canvas px; the drawing on the left, the switches on the right
  fa='255–256, 252', src=[KZ[6], KZ[27]],   # FA 2025 pages + full() textbook titles you checked against
  lanes=[('nmPre', 'Presynaptic terminal', 'glycolysis'), …],   # 2–5; node colours, and the sidebar filter
  comps=[(140, 100, 2140, 700, 'Presynaptic terminal'), …],     # optional shaded regions (x, y, w, h, label)
  nodes=[('nm1', 'Choline acetyltransferase', 600, 220, 'nmPre', 'makes ACh', ['cardid', …]), …],
          # (id, label ≤ 26 chars, x, y, lane, subtitle or '', [card ids it pins], optional 'hub')
          # nodes are the map's card pins: put one beside each structure, pinning the cards about it
  panels=[(2420, 1240, 1000, 'Drugs at the junction (Katzung ch 27)', [('Succinylcholine', 'depolarizing …'), …])],
          # (x, y, w, title naming its source, [(key, value), …]) — 3–8 rows, every row sourced
  dyn=dict(kinds=…, groups=…, switches=…, notes=…, shapes=…, flows=…, sites=…, readouts=…,
           panel=dict(x=2420, y=110, w=1000), src='First Aid pp. 252–256 · Katzung ch 6–7, 27'),
)
```
Lane colours: glycolysis (blue), tca (red), gluconeo (green), ppp (purple), glycogen (orange), sugars (teal).
Lane keys: short camelCase starting with your map's 2-letter code, unique.

## Tools — use them, loop until clean
- `python3 -I drafts/tools/check.py a_nmjflow`
  → PROBLEMs (must fix: unknown cards, bad conditions, unknown sources…) and warnings (estimated text overlaps,
  state by state, and things outside the map). Get it to **0 problems and no overlap warnings** (a warning you've
  checked on a screenshot and know is false may stay — say so in your report).
- `python3 -I drafts/tools/shot.py a_nmjflow` → builds a scratch copy of the site with your map and screenshots it (prints a PNG
  path; open it with the Read tool). Options: `--dyn o:dz:mg,t:adh` (switch keys, comma-separated, as the chips use
  them: `o:<switch>:<option>`, `t:<toggle>`, `g:<group>`), `--look x0,y0,x1,y1` (zoom to that canvas region —
  use it, the whole-map shot is small), `--dark` (dark theme), `--nobuild` (reuse the last build for a new state).
  A build takes ~10 s. **Look at every state at least once** (zoomed), in light theme, and the default state in dark.
  Fix anything cramped, overlapping, unclear or ugly. The bar is "a student understands it in 10 seconds".

## Design rules
- **Draw the anatomy**, simply and big: membranes (`{membrane:"<path>", w:22}`), tubes, vessels, cells
  (`<rect class="dyn-cell" …>`, `<ellipse class="dyn-cell" …>`), soft regions (`class="dyn-soft"`), lines
  (`dyn-line`, `dyn-dash`), arrows (`<path class="dyn-line" marker-end="url(#ah-<one of your lane keys>)"/>` —
  a marker exists for each lane that has nodes). Text classes: `nf-l1` (13 px bold labels), `nf-l2` (12 px),
  `dyn-big` (15 px bold region titles), `dyn-cap` (italic captions). Highlights: `dyn-hl`; lesions: `dyn-lesion`;
  visual fields: `dyn-field` + `dyn-lost` for the blind part; dimmed: `dyn-dim`; traces: `dyn-trace`.
- **Colours only through CSS variables** (dark mode must work): `var(--dk1)`…`var(--dk12)`, `var(--ink)`,
  `var(--ink-2)`, `var(--ink-3)`, `var(--surface)`, `var(--surface-2)`, `var(--line-2)`, `var(--accent)`,
  `var(--ok)`, `var(--bad)`, and the ion colours `--nf-na --nf-k --nf-cl --nf-ca --nf-h2o --nf-glu --nf-h --nf-hco3
  --nf-mg --nf-urea` (use these for those ions, so every map colours Na⁺, K⁺… the same). Never a hex colour.
- Layout: drawing in x 140 → (panel.x − 80); the switches at `panel` (x ≈ w − 1080, y 110, w 1000); info `panels`
  in the same column **below** the switches and notes (check.py's overlap warning tells you where the notes end).
  Labels ≥ 30 px clear of other labels and of lines they don't belong to. Nothing outside 0…w, 0…h.
- Motion: `flows` = particles along a path (`len` = the path's length in px — add straight segments, estimate
  curves; `speed` px/s, default 140). `sites` = a receptor / channel / transporter / enzyme on a wall with particles
  crossing (`cross:true` sends them right through a membrane). Keep it calm: ≤ ~120 moving particles in any state.
- **Every switch must change the picture** — a ✕ on what it blocks (`block`), a channel that stays shut
  (`need` + `closed:"…"`), fewer/more particles (`low`/`boost`, flow `mods`), a vessel or airway narrowing
  (`vessel`/`tube` `mods`), a highlighted or added shape (`shapes` with `when`) — **and** show a note saying what
  happened and why, in 1–3 plain sentences with the exam-relevant consequence. Add `readouts` (↑ ↓ ↔) where the
  exam asks for directions (e.g. PT/PTT, TSH/T4, PaO₂/A–a gradient, QRS/QT, serum urate).
- Switch kinds: `toggle` (on/off: a hormone present), `one` (pick at most one: a drug, a disease, a lesion site),
  `steps` (phases of a cycle, always one, `auto: 3` steps through them by itself — for action-potential phases,
  a cascade's stages…). Conditions: `"adh"`, `"!adh"`, `"drug:loop"`, `"drug:*"`, `"a&b"`.
- Lesion simulators: a `one` switch of lesion sites; each option draws its ✕ on the pathway (shape with `when`)
  and its deficit (e.g. the two visual-field circles with the lost part dark), and a note naming the deficit and
  the classic cause. Readouts are optional there.
- Tap targets: every site has `c` (the card it opens); nodes pin cards. Every card a site opens must also be
  pinned on a node.

## Sources and cards
- Every fact in notes, panels, labels, readouts and new cards must be supported by a source you actually read in
  the corpus (FA 2025 pages in the corpus (NOT on this branch — see drafts/HANDOFF.md), textbook chapters,
  Bootcamp decks, OCOM course texts under corpus/ — see m37/SPEC.md). Put the FA pages in `fa`, the textbook titles
  (`full('<Book>', ch)`) in `src`, and a short human source line in `dyn.src`. Panel titles name their source.
  If you can't find support for something, leave it out.
- **Pin existing cards** — grep atlas-src.html (`grep -n '^<id>:{n:'`, `grep -i` names and synonyms on lines
  starting `xxx:{n:"`) and use what's there. Write a **new card** only for a real gap the map needs (sourced, per
  m37/SPEC.md, `p` = one of your lanes), and pin it on a node. Never duplicate an existing card.
- Never copy Bootcamp practice questions (their stems or choices). Write in your own words.

## Report (final message, under 350 words)
Per map: id, the switches and what each changes, new cards (id + name), existing cards pinned (count), sources,
anything dropped for lack of support, anything you're unsure of, check.py's final line, and the PNGs you looked at.

## m40/m41 addendum — read this too
- **Worked examples now exist** — read at least one before you start: drafts/examples/ (d_coagflow.py, …) 
  d_coagflow.py (lab-pattern readouts: PT/PTT/bleeding time per drug and disorder), c_visfield.py (a lesion simulator),
  e_alvflow.py (readouts + a graph drawn with shapes), f_follflow.py (a cell with transporters). They passed an
  independent fact-check; copy their structure and style.
- **Every `one` option names its card**: write options as `[key, "label", "cardid"]` — the existing (or your new) card
  that option is about (e.g. `["hema", "Hemophilia A", "hemophilia"]`). The site uses it for "See it move" links from
  practice questions and for search ("hemophilia" → this map with that switch on). check.py verifies the card exists.
  Leave the third element off only when no card fits.
- **Readouts drive a new "Predict it" mode**: students hide the arrows, guess ↑ ↓ ↔ for each readout, then check.
  So give every option the readout arrows the exam asks about (sourced), and keep "–" only where no source gives a
  direction. 3–6 readouts per map.
- **Map ids must not equal a card id** (check.py enforces it): `#<id>` links open a map before a card.
- New maps go into the atlas as it is now (all m39 maps are in it) — re-grep atlas-src.html for existing cards first.
- m41: the atlas now has 27 moving maps (e.g. drafts/examples/a_ironflow.py,
  b_glomsim.py are good recent examples). The kit (m42/kit.js) adds a phone sheet and "Predict the arrows" on its
  own — you don't build those. Draw anything that changes with a switch as `shapes` with `when`, including
  graphs/traces (see m39/d_cardap.py and e_alvflow.py for drawn traces that change per option).

## m42 addendum
- The atlas now has 34 moving maps, all in base-src.html. The best recent examples (all passed an independent fact-check):
  drafts/examples/a_pvflow.py (a loop graph redrawn per option + heart sounds),
  a_misim.py (territory + ECG leads per option), c_plexsim.py (nerve lesion simulator with shaded skin and drawn signs),
  b_edemaflow.py (force arrows + readouts), d_mensflow.py (an axis with feedback + a drawn hormone graph).
- Static maps already covering parts of your topic are listed in your task; pin their cards, don't duplicate them.
- Keep generic phrases out of new cards' link terms (m41 lost "luteal phase", "proliferative phase", "lymphatic obstruction"
  because they pulled unrelated questions). A link term must name the card's own subject.
- Guided tours: every moving map will get a "Tour" that steps through the switches in order (default state, then each
  option) and shows that state's note as narration. So order each switch's options in teaching order, and make every
  option's note stand on its own (one clear point, 1–3 sentences).
