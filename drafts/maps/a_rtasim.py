# Renal Tubular Acidosis Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Where each RTA breaks the kidney's acid excretion, side by side with diarrhea (a gut loss of HCO₃⁻):
# the proximal tubule cell (NHE3, brush-border carbonic anhydrase, basolateral Na⁺–HCO₃⁻ cotransport, NH₄⁺ from
# glutamine), the collecting duct's α-intercalated cell (H⁺-ATPase, Cl⁻–HCO₃⁻ exchange) and principal cell (ENaC,
# ROMK, the aldosterone receptor), the colon, and two urine tests drawn as scales — urine pH against 5.5 and the
# urinary anion gap. One `one` switch picks a type (1, 2, 4), diarrhea, or a cause (amphotericin B, acetazolamide,
# Fanconi syndrome, spironolactone). No new cards: every fact here is one the pinned cards already carry
# (rta, drta, uag, nagma, newhco3, hco3reabs, acetazolamide, fanconisyn — fact-checked against the corpus), with the
# First Aid pages they cite; checked against FA 2025 (type 4 urine pH is "variable" there).
# Sources: First Aid 2025 pp. 604, 610–611, 617 · Costanzo ch 7 · Guyton ch 31 · Katzung ch 15 · Robbins ch 20.
# m51 upgrade (2026-10-18): 15 more causes grouped by type with `sections`, two more readouts (urine pH, urine anion gap), the stone
# and rickets drawings extended to every cause that leads there, and a "How it gets there" line per cause. Added sources:
# FA 2025 pp. 250, 402, 440, 445, 560 · Robbins ch 6 (Sjögren) · Kaplan & Sadock ch 21 (lithium) · Katzung ch 24 (topiramate),
# ch 36 (NSAID hyperkalemia), ch 46 (trimethoprim hyperkalemia) · Bootcamp Nephrology RTA slides (Sjögren, heavy metals,
# topiramate) · Batlle 1988 N Engl J Med (urinary anion gap — the ref already on the uag and drta cards).
# Every old shape/flow/site keeps its index (m47 assemble patches by index); new shapes are appended in section 5b.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ7, GY31, KZ15, RB20 = full('Costanzo', 7), full('Guyton', 31), full('Katzung', 15), full('Robbins', 20)
RB6, KS21, KZ24, KZ36, KZ46 = full('Robbins', 6), full('Kaplan & Sadock', 21), full('Katzung', 24), full('Katzung', 36), full('Katzung', 46)
BCN = 'Bootcamp.com Nephrology — Acid-Base Physiology'

shapes = []
def add(svg, when=None, unless=None):
    if when is None and unless is None: shapes.append(svg); return
    d = dict(svg=svg)
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def text(t, x, y, cls='nf-l2', anchor=None, when=None, unless=None):
    d = dict(text=t, x=x, y=y, cls=cls)
    if anchor: d['anchor'] = anchor
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def box(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')
def cell(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="30" class="dyn-cell"/>')
    shapes.append(dict(membrane=f'M{x0 + 30} {y0} H{x1 - 30} Q{x1} {y0} {x1} {y0 + 30} V{y1 - 30} Q{x1} {y1} {x1 - 30} {y1} '
                                f'H{x0 + 30} Q{x0} {y1} {x0} {y1 - 30} V{y0 + 30} Q{x0} {y0} {x0 + 30} {y0} Z', w=20))

TAG = 'nf-l2 dyn-tag'
Z = lambda *k: ['rt:' + x for x in k]
# m51: more causes, each tied to its type (First Aid 2025 p. 611 unless noted):
#   type 1 — amphotericin B, analgesic nephropathy, autoimmune disease (SLE: FA p. 611; Sjögren: Bootcamp Nephrology RTA type 1
#            slide + Robbins ch 6 "renal tubular acidosis" in Sjögren), lithium (Kaplan & Sadock ch 21: "features of distal RTA")
#   type 2 — Fanconi syndrome, multiple myeloma, carbonic anhydrase inhibitors (FA p. 611, 626); topiramate (weak CA inhibitor,
#            Katzung ch 24; Bootcamp RTA type 2 slide); Fanconi causes Wilson disease, lead, ifosfamide, cisplatin, tenofovir
#            (FA pp. 250, 402, 445, 604)
#   type 4 — low aldosterone: diabetic hyporeninism, ACE inhibitors/ARBs, NSAIDs, heparin (also FA p. 440), cyclosporine, adrenal
#            insufficiency; resistance: K⁺-sparing diuretics, TMP-SMX (FA p. 611; Katzung ch 36, 46 for the hyperkalemia)
PROX = Z('p2', 'acz', 'fan', 'topi', 'mm', 'wil', 'pb', 'ifo')   # proximal (type 2) — and its causes
DIST1 = Z('d1', 'amph', 'auto', 'li', 'anal')                      # distal (type 1)
T4 = Z('h4', 'spiro', 'dm', 'acei', 'nsaid', 'hep', 'cyc', 'add', 'tmp')   # hyperkalemic (type 4)
FANC = Z('fan', 'wil', 'pb', 'ifo')   # causes that act through Fanconi syndrome (FA p. 604)
CAI = Z('acz', 'topi')                # carbonic anhydrase inhibitors
LOWALDO = Z('h4', 'dm', 'acei', 'nsaid', 'hep', 'cyc', 'add')   # type 4 by low aldosterone production (FA p. 611)
RTA = PROX + DIST1 + T4
ALL = RTA + Z('dia')
LOWK = DIST1 + PROX + Z('dia')        # FA p. 611: serum K⁺ ↓ in types 1 and 2; diarrhea loses K⁺ in stool

# ════════ 1. proximal tubule ════════
box(160, 130, 1180, 760)
text('Proximal tubule', 180, 166, 'dyn-big')
text('reclaims filtered HCO₃⁻ · makes NH₄⁺ from glutamine', 180, 186, 'dyn-cap')
shapes.append(dict(vessel='M180 250 H1160', w=34, color='--dk12'))
text('blood', 1160, 226, 'dyn-cap', 'end')
cell(210, 290, 1130, 560)
text('Proximal tubule cell', 1110, 420, 'dyn-big', 'end')
text('CO₂ + H₂O → H⁺ + HCO₃⁻', 460, 420, 'nf-l2', 'middle')
shapes.append(dict(tube='M180 620 H1160', w=70))
text('tubular fluid — what is not reclaimed flows on to the collecting duct', 200, 700)
text('HCO₃⁻ not reclaimed — it spills on toward the urine', 200, 726, TAG, when=Z('p2', 'mm'))
text('carbonic anhydrase blocked — HCO₃⁻ stays in the lumen', 200, 726, TAG, when=Z('acz'))
text('the whole tubule fails: glucose · amino acids · phosphate · uric acid lost too', 200, 726, TAG, when=FANC)
text('high K⁺ slows NH₃ synthesis here', 200, 726, TAG, when=T4)
text('more NH₄⁺ made from glutamine — the normal answer to acidosis', 200, 726, TAG, when=Z('dia'))

# ════════ 2. collecting duct ════════
box(1220, 130, 2340, 760)
text('Collecting duct', 1240, 166, 'dyn-big')
text('α-intercalated cells secrete H⁺ · principal cells trade Na⁺ for K⁺', 1240, 186, 'dyn-cap')
shapes.append(dict(vessel='M1240 250 H2320', w=34, color='--dk12'))
text('blood', 2320, 226, 'dyn-cap', 'end')
cell(1250, 290, 1760, 560)
cell(1810, 290, 2310, 560)
text('α-intercalated cell', 1270, 420, 'dyn-big')
text('CO₂ + H₂O → H⁺ + HCO₃⁻', 1640, 420, 'nf-l2', 'middle')
text('Principal cell', 1830, 420, 'dyn-big')
shapes.append(dict(tube='M1240 620 H2320', w=70))
text('urine — NH₃ meets secreted H⁺ and is trapped as NH₄⁺', 1260, 700)
text('no H⁺ secreted → no new HCO₃⁻, little NH₄⁺', 1260, 726, TAG, when=DIST1)
text('HCO₃⁻ from the proximal tubule reaches the urine', 1260, 726, TAG, when=PROX)
text('little aldosterone signal → less K⁺ secreted', 1260, 726, TAG, when=T4)
text('brisk NH₄⁺ excretion — new HCO₃⁻ for the blood', 1260, 726, TAG, when=Z('dia'))

# ════════ 3. the colon ════════
box(160, 800, 1180, 1280)
text('Colon', 180, 836, 'dyn-big')
text('a gut loss of HCO₃⁻ looks like an RTA in the blood', 180, 856, 'dyn-cap')
shapes.append(dict(tube='M200 1000 H1140', w=90, color='--dk5'))
text('stool', 1140, 1080, 'dyn-cap', 'end')
text('diarrhea: HCO₃⁻ and K⁺ leave in the stool', 180, 1140, TAG, when=Z('dia'))
text('pick Diarrhea to compare a gut loss with the RTAs', 180, 1140, 'dyn-cap', unless=Z('dia'))

# ════════ 4. urine tests ════════
box(1220, 800, 2340, 1280)
text('Urine tests', 1240, 836, 'dyn-big')
text('markers show which side of the cut-off, not exact values', 1240, 856, 'dyn-cap')
# urine pH scale: 4.5 → 8.0
PX0, PX1, PY = 1300, 2260, 940
px = lambda ph: round(PX0 + (ph - 4.5) / 3.5 * (PX1 - PX0))
text('Urine pH', 1240, 902, 'nf-l1')
add(f'<path d="M{PX0} {PY} H{PX1}" class="dyn-line"/>'
    + ''.join(f'<path d="M{px(v)} {PY - 8} V{PY + 8}" class="dyn-line"/>'
              f'<text class="nf-l2" x="{px(v)}" y="{PY + 26}" text-anchor="middle">{v}</text>' for v in (5, 6, 7, 8))
    + f'<path d="M{px(5.5)} {PY - 30} V{PY + 12}" class="dyn-dash" style="stroke:var(--bad)"/>'
      f'<text class="nf-l1" x="{px(5.5)}" y="{PY - 36}" text-anchor="middle">5.5</text>')
def dot(ph, y, hollow=False, when=None):
    st = 'fill:var(--surface);stroke:var(--accent);stroke-width:4' if hollow else 'fill:var(--accent);stroke:var(--surface);stroke-width:3'
    add(f'<circle cx="{px(ph)}" cy="{y}" r="12" style="{st}"/>', when=when)
dot(6.6, PY, when=DIST1)
text('stays above 5.5 — the cells cannot acidify it', px(6.6), PY + 60, TAG, 'middle', when=DIST1)
dot(7.1, PY, hollow=True, when=PROX)
text('at first: HCO₃⁻ spills, urine alkaline', px(7.1), PY + 60, TAG, 'middle', when=PROX)
P2ACID = Z('p2', 'fan', 'topi', 'mm', 'wil', 'pb', 'ifo')   # every type 2 except acetazolamide, whose urine stays alkaline (FA p. 626)
dot(5.0, PY, when=P2ACID)
text('below 5.5 once serum HCO₃⁻ is under the threshold', px(5.0) - 40, PY + 86, TAG, 'start', when=P2ACID)
text('type 4: variable (First Aid 2025)', PX0, PY + 60, TAG, 'start', when=T4)
text('urine pH can run above 5.3 here — the anion gap tells it apart', PX0, PY + 60, TAG, 'start', when=Z('dia'))
# urinary anion gap scale
UY, U0 = 1150, 1780
text('Urinary anion gap = urine Na⁺ + K⁺ − Cl⁻', 1240, 1062, 'nf-l1')
add(f'<path d="M{PX0} {UY} H{PX1}" class="dyn-line"/><path d="M{U0} {UY - 10} V{UY + 10}" class="dyn-line"/>'
    f'<text class="nf-l2" x="{PX0}" y="{UY + 26}">negative</text><text class="nf-l2" x="{U0}" y="{UY + 26}" text-anchor="middle">0</text>'
    f'<text class="nf-l2" x="{PX1}" y="{UY + 26}" text-anchor="end">positive</text>')
add(f'<circle cx="1480" cy="{UY}" r="12" style="fill:var(--accent);stroke:var(--surface);stroke-width:3"/>', when=Z('dia'))
text('plenty of NH₄⁺ — the kidney is responding', 1480, UY - 24, TAG, 'middle', when=Z('dia'))
add(f'<circle cx="2080" cy="{UY}" r="12" style="fill:var(--accent);stroke:var(--surface);stroke-width:3"/>', when=DIST1 + T4)
text('little NH₄⁺ — distal acidification fails', 2080, UY - 24, TAG, 'middle', when=DIST1 + T4)
text('negative = NH₄⁺ excreted (a gut loss) · positive = little NH₄⁺ (distal or type 4 RTA)', 1240, 1236, 'dyn-cap')

# ════════ 5. what it leads to ════════
box(160, 1320, 2340, 1700)
text('What it leads to', 180, 1356, 'dyn-big')
STONE = 'M330 1480 L372 1446 L430 1458 L452 1506 L420 1552 L356 1556 L322 1520 Z'
STONES = DIST1 + CAI   # FA p. 611 (type 1), p. 626 (acetazolamide), p. 560 (topiramate: kidney stones)
add(f'<path d="{STONE}" class="dyn-soft" style="stroke:var(--dk7);stroke-width:3"/>', when=STONES)
add(f'<path d="{STONE}" class="dyn-soft dyn-dim"/>', unless=STONES)
text('Calcium phosphate stones', 490, 1490, 'nf-l1')
text('calcium phosphate precipitates in alkaline urine', 490, 1508, TAG, when=DIST1 + Z('acz'))
BONE = ('M1040 1470 a22 22 0 1 1 30 -28 L1250 1442 a22 22 0 1 1 30 28 a22 22 0 1 1 -30 28 '
        'L1070 1498 a22 22 0 1 1 -30 -28 Z')
RICKETS = Z('p2') + FANC   # FA p. 611 (in Fanconi syndrome), p. 604 (rickets/osteopenia from hypophosphatemia)
add(f'<path d="{BONE}" class="dyn-soft" style="stroke:var(--dk9);stroke-width:3"/>', when=RICKETS)
add(f'<path d="{BONE}" class="dyn-soft dyn-dim"/>', unless=RICKETS)
text('Hypophosphatemic rickets', 1040, 1580, 'nf-l1')
text('with Fanconi syndrome — phosphate lost in the urine', 1040, 1598, TAG, when=RICKETS)
add('<circle cx="1820" cy="1478" r="40" class="dyn-soft" style="stroke:var(--nf-k);stroke-width:4"/>'
    '<text class="dyn-big" x="1820" y="1484" text-anchor="middle">K⁺</text>')
text('Serum K⁺', 1880, 1470, 'nf-l1')
text('high — the only RTA with high K⁺', 1880, 1490, TAG, when=T4)
text('low', 1880, 1490, TAG, when=LOWK)
text('pick a type to see which way it goes', 1880, 1490, 'dyn-cap', unless=ALL)

# ════════ 5b. m51 additions — appended after every older shape (the live build patches shapes by index) ════════
text('carbonic anhydrase weakly inhibited — some HCO₃⁻ stays in the lumen', 200, 726, TAG, when=Z('topi'))   # Katzung ch 24
text('kidney stones — a topiramate adverse effect', 490, 1508, TAG, when=Z('topi'))                           # FA p. 560
# how each cause gets to its type — one line along the bottom of "What it leads to"
CAUSE = [
  ('d1', 'type 1 itself — pick one of its causes (amphotericin B … analgesic nephropathy) to see how it gets here'),
  ('amph', 'amphotericin B toxicity → the α-intercalated cells cannot secrete H⁺ → type 1 (First Aid p. 611)'),
  ('auto', 'autoimmune disease (Sjögren syndrome, SLE) → tubulointerstitial damage → type 1'),             # FA p. 611 · Bootcamp · Robbins ch 6
  ('li', 'lithium → occasionally features of distal (type 1) RTA (Kaplan & Sadock ch 21)'),
  ('anal', 'analgesic nephropathy → type 1 (First Aid p. 611)'),
  ('p2', 'type 2 itself — pick one of its causes (acetazolamide … ifosfamide) to see how it gets here'),
  ('acz', 'acetazolamide blocks carbonic anhydrase → type 2 (First Aid p. 626)'),
  ('topi', 'topiramate weakly inhibits carbonic anhydrase → occasionally a type 2 picture (Katzung ch 24)'),
  ('fan', 'Fanconi syndrome: the whole proximal tubule fails → type 2'),
  ('mm', 'multiple myeloma → type 2 — it can also cause full Fanconi syndrome (First Aid pp. 604, 611)'),
  ('wil', 'Wilson disease → Fanconi syndrome → type 2 (First Aid pp. 402, 604)'),
  ('pb', 'lead poisoning → Fanconi syndrome → type 2 (First Aid p. 604)'),
  ('ifo', 'ifosfamide, cisplatin, tenofovir → Fanconi syndrome → type 2 (First Aid pp. 250, 604)'),
  ('h4', 'type 4 itself — pick one of its causes (spironolactone … TMP-SMX) to see how it gets here'),
  ('spiro', 'spironolactone blocks the aldosterone receptor → aldosterone resistance → type 4'),
  ('dm', 'diabetic hyporeninism: little renin → little aldosterone → type 4 (First Aid p. 611)'),
  ('acei', 'ACE inhibitor or ARB: less angiotensin II → less aldosterone → type 4 (First Aid p. 611)'),
  ('nsaid', 'NSAIDs → less aldosterone made → type 4 (First Aid p. 611)'),
  ('hep', 'heparin → less aldosterone made → type 4 (First Aid pp. 440, 611)'),
  ('cyc', 'cyclosporine → less aldosterone made → type 4 (First Aid p. 611)'),
  ('add', 'adrenal insufficiency: no aldosterone → type 4 (First Aid p. 611)'),
  ('tmp', 'TMP-SMX → aldosterone resistance → type 4 (First Aid p. 611)'),
  ('dia', 'diarrhea is not an RTA: the gut loses HCO₃⁻ and the healthy kidney answers with NH₄⁺'),
]
text('How it gets there', 180, 1646, 'nf-l1')
for k, t in CAUSE: text(t, 180, 1672, TAG, when=Z(k))
text('pick a type or a cause', 180, 1672, 'dyn-cap', unless=ALL)

# ════════ 6. motion ════════
def m(when, **kw): return dict(when=when, **kw)
def flow(d, ln, base, mods=(), speed=110, r=6):
    return dict(d=d, len=ln, speed=speed, r=r, base=base, mods=list(mods))
flows = [
  flow('M190 250 H1150', 960, dict(hco3=4), [m(PROX, set=dict(hco3=1)), m(Z('dia'), set=dict(hco3=5))]),           # reclaimed HCO₃⁻
  flow('M190 620 H1150', 960, dict(hco3=2), [m(PROX, set=dict(hco3=7))]),                                          # filtered HCO₃⁻ left behind
  flow('M1250 250 H2310', 1060, dict(hco3=3), [m(DIST1, set=dict(hco3=0)), m(T4, set=dict(hco3=1)), m(Z('dia'), set=dict(hco3=6))]),   # new HCO₃⁻
  flow('M1250 620 H2310', 1060, dict(nh4=3, k=2), [m(DIST1, set=dict(nh4=1)), m(T4, set=dict(nh4=1, k=0)), m(Z('dia'), set=dict(nh4=7)),
                                                  m(PROX, add=dict(hco3=4))]),                                     # urine
  flow('M210 1000 H1130', 920, dict(), [m(Z('dia'), set=dict(hco3=6, k=3))], speed=150),                           # stool
]

# ════════ 7. sites ════════
sites = [
  # proximal tubule — lumen below (y 620), blood above (y 250)
  dict(x=330, y=560, n=[0, -1], w=20, t='ex', l='Na⁺–H⁺ exchanger', s='H⁺ out · Na⁺ in', reach=50, cross=True,
       ions=[['h', 'in', 1], ['na', 'out', 1]], c='hco3reabs', low=PROX, lx=330, ly=474, la='middle'),
  dict(x=600, y=560, n=[0, -1], w=20, t='ex', l='Carbonic anhydrase', s='brush border: H₂CO₃ → CO₂ + H₂O', ions=[],
       c='hco3reabs', block=Z('acz'), low=Z('topi'), sfx=dict(low=' — weakly inhibited'), lx=600, ly=474, la='middle'),
  dict(x=900, y=560, n=[0, -1], w=20, t='pump', l='Glutamine → NH₄⁺', s='NH₄⁺ into the lumen', reach=50, cross=True,
       ions=[['nh4', 'in', 1]], c='newhco3', low=T4, boost=Z('dia'), sfx=dict(low=' — slowed by high K⁺'),
       lx=900, ly=474, la='middle'),
  dict(x=460, y=290, n=[0, 1], w=20, t='co', l='Na⁺–HCO₃⁻ cotransporter', s='HCO₃⁻ back to the blood', reach=44, cross=True,
       ions=[['hco3', 'in', 2]], c='hco3reabs', low=PROX, lx=460, ly=348, la='middle'),
  dict(x=900, y=290, n=[0, 1], w=20, t='co', l='New HCO₃⁻ out', s='one for each NH₄⁺ made', reach=44, cross=True,
       ions=[['hco3', 'in', 1]], c='newhco3', low=T4, boost=Z('dia'), lx=900, ly=348, la='middle'),
  # α-intercalated cell
  dict(x=1380, y=560, n=[0, -1], w=20, t='pump', l='H⁺-ATPase', s='H⁺ into the urine', reach=50, cross=True,
       ions=[['h', 'in', 2]], c='drta', block=DIST1, boost=Z('dia'), sfx=dict(block=' — fails'), lx=1380, ly=474, la='middle'),
  dict(x=1500, y=290, n=[0, 1], w=20, t='ex', l='Cl⁻–HCO₃⁻ exchanger', s='new HCO₃⁻ to the blood', reach=44, cross=True,
       ions=[['hco3', 'in', 1], ['cl', 'out', 1]], c='newhco3', stop=DIST1, boost=Z('dia'), lx=1500, ly=348, la='middle'),
  # principal cell
  dict(x=1900, y=560, n=[0, -1], w=20, t='ch', l='ENaC', s='Na⁺ in', reach=50, cross=True,
       ions=[['na', 'out', 1]], c='aldoaction', low=T4, lx=1900, ly=474, la='middle'),
  dict(x=2090, y=560, n=[0, -1], w=20, t='ch', l='ROMK', s='K⁺ into the urine', reach=50, cross=True,
       ions=[['k', 'in', 1]], c='aldoaction', low=T4, sfx=dict(low=' — less K⁺ out'), lx=2090, ly=474, la='middle'),
  dict(x=2160, y=290, n=[0, 1], w=20, t='rec', l='Aldosterone receptor', s='turns on ENaC and ROMK', ions=[],
       c='mras', block=Z('spiro'), low=LOWALDO, sfx=dict(low=' — little signal'), lx=2160, ly=348, la='middle'),
]

# ════════ 8. readouts ════════
readouts = [
  dict(l='Serum HCO₃⁻', mods=[dict(when=ALL, d=-1)]),
  dict(l='Serum Cl⁻', mods=[dict(when=ALL, d=1)]),
  dict(l='Anion gap', mods=[dict(when=ALL, d=0)]),
  dict(l='Serum K⁺', mods=[dict(when=LOWK, d=-1), dict(when=T4, d=1)]),
  dict(l='Urine NH₄⁺', mods=[dict(when=DIST1 + T4, d=-1), dict(when=Z('dia'), d=1)]),
  # m51 — urine pH: ↑ (stays > 5.5) in type 1 (FA p. 611) and with acetazolamide (FA p. 626: high urine pH); type 2 and type 4
  # are "variable" / threshold-dependent in FA p. 611, and diarrhea can run above 5.3 (Batlle 1988) — so no arrow for those
  dict(l='Urine pH', mods=[dict(when=DIST1 + Z('acz'), d=1)]),
  # m51 — urinary anion gap (Batlle 1988, N Engl J Med, the ref on the uag/drta cards): positive in classic distal RTA, hyperkalemic
  # distal RTA and selective aldosterone deficiency; negative in diarrhea. No corpus source gives type 2 — left blank
  dict(l='Urine anion gap', mods=[dict(when=DIST1 + T4, d=1), dict(when=Z('dia'), d=-1)]),
]

# ════════ 9. notes ════════
notes = {
  '': 'The normal kidney: the proximal tubule reclaims nearly all filtered HCO₃⁻ and makes NH₄⁺ from glutamine; '
      'α-intercalated cells secrete H⁺, and every H⁺ excreted as NH₄⁺ or titratable acid returns a new HCO₃⁻ to the blood. '
      'Pick an RTA type, a cause, or diarrhea.',
  'rt:d1': 'Type 1 (distal) RTA: α-intercalated cells cannot secrete H⁺, so no new HCO₃⁻ is made and little NH₄⁺ is excreted '
           '(positive urinary anion gap). Urine pH stays above 5.5 even when serum HCO₃⁻ is very low; K⁺ falls, and calcium '
           'phosphate stones form in the alkaline urine.',
  'rt:p2': 'Type 2 (proximal) RTA: the proximal tubule cannot reabsorb HCO₃⁻, so it spills into the urine and serum HCO₃⁻ falls. '
           'Once serum HCO₃⁻ is below the threshold, urine pH drops under 5.5. K⁺ falls; with Fanconi syndrome comes '
           'hypophosphatemic rickets.',
  'rt:h4': 'Type 4 (hyperkalemic) RTA: too little aldosterone, or a kidney that resists it. Principal cells secrete less K⁺, and '
           'the high K⁺ slows NH₃ synthesis in the proximal tubule, so less NH₄⁺ is excreted (positive urinary anion gap); '
           'First Aid gives the urine pH as variable. The only RTA with high K⁺.',
  'rt:dia': 'Diarrhea: the gut, not the kidney, loses HCO₃⁻ (and K⁺) — also a normal anion gap acidosis. The healthy kidney '
            'answers by excreting more NH₄⁺, so the urinary anion gap is negative; urine pH can still run above 5.3, so the '
            'gap, not the pH, separates it from distal RTA.',
  'rt:amph': 'Amphotericin B is a classic cause of type 1 (distal) RTA: the α-intercalated cells fail to acidify the urine — '
             'urine pH above 5.5, little NH₄⁺, low K⁺.',
  'rt:acz': 'Acetazolamide blocks carbonic anhydrase, so filtered HCO₃⁻ is not reclaimed in the proximal tubule — a proximal '
            '(type 2) RTA with alkaline urine and low K⁺. The HCO₃⁻ diuresis is self-limited (once serum HCO₃⁻ falls, less is '
            'filtered), but the acidosis lasts as long as the drug. Calcium phosphate stones can form in the alkaline urine.',
  'rt:fan': 'Fanconi syndrome: the whole proximal tubule fails — HCO₃⁻ (a type 2 RTA) plus glucose, amino acids, phosphate and '
            'uric acid are lost. Glucosuria with a normal serum glucose is the giveaway; low phosphate causes rickets in children. '
            'Causes include Wilson disease, multiple myeloma, lead, tenofovir and expired tetracycline.',
  'rt:spiro': 'Spironolactone blocks the aldosterone receptor — aldosterone resistance, a cause of type 4 RTA, as are other '
              'K⁺-sparing diuretics and TMP-SMX. K⁺ secretion falls, the high K⁺ slows NH₃ synthesis, and less NH₄⁺ is excreted.',
  # ── m51 causes ──
  'rt:auto': 'Autoimmune disease is a cause of type 1 (distal) RTA — SLE in First Aid, Sjögren syndrome in Bootcamp, where Robbins ties '
             'the tubular defects to tubulointerstitial nephritis. The α-intercalated cells cannot secrete H⁺: urine pH stays above 5.5, '
             'little NH₄⁺ is excreted and K⁺ falls.',
  'rt:li': 'Lithium is occasionally associated with features of distal (type 1) RTA — urine that cannot be acidified below 5.5, little '
           'NH₄⁺, low K⁺ — on top of its better-known concentrating defect (nephrogenic diabetes insipidus).',
  'rt:anal': 'Analgesic nephropathy is a First Aid cause of type 1 (distal) RTA: the collecting duct cannot acidify the urine, so urine pH '
             'stays above 5.5, K⁺ falls and calcium phosphate stones can form.',
  'rt:topi': 'Topiramate is a weak carbonic anhydrase inhibitor; occasionally this lowers serum HCO₃⁻ — a hyperchloremic, normal anion '
             'gap acidosis of the proximal (type 2) kind. Kidney stones are a known adverse effect.',
  'rt:mm': 'Multiple myeloma is a First Aid cause of proximal (type 2) RTA, and of the full Fanconi syndrome: filtered HCO₃⁻ escapes the '
           'proximal tubule, serum HCO₃⁻ and K⁺ fall, and once HCO₃⁻ is below the threshold the urine can still drop under 5.5.',
  'rt:wil': 'Wilson disease can injure the proximal tubule into Fanconi syndrome: glucose, amino acids, phosphate and HCO₃⁻ are all lost '
            '(a type 2 RTA), K⁺ falls, and the phosphate loss brings rickets or osteopenia.',
  'rt:pb': 'Lead poisoning is a toxic cause of Fanconi syndrome: the whole proximal tubule fails, HCO₃⁻ spills (type 2 RTA) and phosphate '
           'loss brings rickets or osteopenia. Bootcamp lists mercury and cadmium with lead among the heavy-metal causes.',
  'rt:ifo': 'Ifosfamide and cisplatin — with tenofovir and expired tetracyclines — are drug causes of Fanconi syndrome: the proximal '
            'tubule loses HCO₃⁻ (type 2 RTA), glucose, amino acids and phosphate, and K⁺ falls.',
  'rt:dm': 'Diabetic hyporeninism: too little renin means too little aldosterone — a type 4 RTA. Principal cells secrete less K⁺, and the '
           'high K⁺ slows NH₃ synthesis in the proximal tubule, so less NH₄⁺ (and acid) is excreted.',
  'rt:acei': 'ACE inhibitors and ARBs take away angiotensin II’s push on the adrenal, so aldosterone falls — a First Aid cause of type 4 '
             'RTA. K⁺ rises, and the high K⁺ slows NH₃ synthesis, so less NH₄⁺ is excreted.',
  'rt:nsaid': 'NSAIDs are on First Aid’s list of causes of low aldosterone production and type 4 RTA: K⁺ rises (hyperkalemia is a listed '
              'renal NSAID effect), the high K⁺ slows NH₃ synthesis, and less NH₄⁺ is excreted.',
  'rt:hep': 'Heparin lowers aldosterone production — type 4 RTA is one of its listed adverse effects in First Aid: high K⁺, less NH₄⁺ '
            'excreted, a normal anion gap acidosis.',
  'rt:cyc': 'Cyclosporine is a First Aid cause of type 4 RTA through low aldosterone production: K⁺ rises and the high K⁺ slows NH₄⁺ '
            'excretion, giving a normal anion gap acidosis.',
  'rt:add': 'Adrenal insufficiency (Addison disease): no aldosterone, so principal cells cannot secrete K⁺ — a type 4 RTA with high K⁺ and '
            'little NH₄⁺. It is the “A” of SHARDS, the normal anion gap acidoses.',
  'rt:tmp': 'TMP-SMX causes aldosterone resistance (First Aid): the hormone is there but the collecting duct answers less, so K⁺ rises '
            'and NH₄⁺ excretion falls — a type 4 RTA. Hyperkalemia is a listed trimethoprim adverse effect.',
}

dyn = dict(
  kinds=dict(h=['h', '--nf-h'], hco3=['hco3', '--nf-hco3'], na=['ions', '--nf-na'], k=['ions', '--nf-k'], cl=['ions', '--nf-cl'],
             nh4=['nh4', '--dk4']),
  groups=[['h', 'H⁺'], ['hco3', 'HCO₃⁻'], ['ions', 'Na⁺ · K⁺ · Cl⁻'], ['nh4', 'NH₄⁺']],
  # m51: options in teaching order (each type, then its causes; diarrhea last), grouped with `sections` — keys unchanged
  switches=[dict(id='rt', label='Type or cause', type='one',
                 options=[['d1', 'Type 1 — distal', 'drta'], ['amph', 'Amphotericin B', 'amphotericin'],
                          ['auto', 'Sjögren · SLE', 'sjogren'], ['li', 'Lithium', 'lithium'], ['anal', 'Analgesic nephropathy', 'drta'],
                          ['p2', 'Type 2 — proximal', 'rta'], ['acz', 'Acetazolamide', 'acetazolamide'], ['topi', 'Topiramate', 'topiramate'],
                          ['fan', 'Fanconi syndrome', 'fanconisyn'], ['mm', 'Multiple myeloma', 'myeloma'], ['wil', 'Wilson disease', 'wilson'],
                          ['pb', 'Lead poisoning', 'lead'], ['ifo', 'Ifosfamide · cisplatin', 'cyclophos'],
                          ['h4', 'Type 4 — hyperkalemic', 'rta'], ['spiro', 'Spironolactone', 'mras'], ['dm', 'Diabetic hyporeninism', 'diabetickidney'],
                          ['acei', 'ACE inhibitor · ARB', 'acei'], ['nsaid', 'NSAIDs', 'nsaidkidney'], ['hep', 'Heparin', 'heparin'],
                          ['cyc', 'Cyclosporine', 'calcineurin'], ['add', 'Adrenal insufficiency', 'addison'], ['tmp', 'TMP-SMX', 'sulfonamides'],
                          ['dia', 'Diarrhea (gut loss)', 'diarrheaapproach']],
                 sections=[['type 1 · distal', ['d1', 'amph', 'auto', 'li', 'anal']],
                           ['type 2 · proximal', ['p2', 'acz', 'topi', 'fan', 'mm', 'wil', 'pb', 'ifo']],
                           ['type 4 · hyperkalemic', ['h4', 'spiro', 'dm', 'acei', 'nsaid', 'hep', 'cyc', 'add', 'tmp']],
                           ['not an RTA', ['dia']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 194, 250, 402, 440, 445, 560, 604, 610–611, 617, 626 · Costanzo ch 7–8 · Guyton ch 31 · Katzung ch 15, 24, 36, 46 · '
      'Robbins ch 6 · Kaplan & Sadock ch 21 · Bootcamp Nephrology · Batlle 1988')

MAP = dict(
  id='rtasim', title='Renal Tubular Acidosis Simulator', topic='renal', after='abtime',
  sub='Three ways the kidney fails to excrete acid, beside diarrhea: the proximal tubule loses filtered HCO₃⁻ (type 2), the '
      'α-intercalated cell cannot secrete H⁺ (type 1), or too little aldosterone holds K⁺ in and slows NH₄⁺ (type 4). Pick a type or '
      'a cause — amphotericin B, Sjögren, myeloma, Wilson, lead, heparin, TMP-SMX and more — to see what fails, the urine pH, the urinary '
      'anion gap and the K⁺. Tap a transporter for its card',
  w=3500, h=2160,
  fa='194, 250, 402, 440, 445, 560, 604, 610–611, 617, 626', src=[CZ7, full('Costanzo', 8), GY31, KZ15, RB20, RB6, KS21, KZ24, KZ36, KZ46, BCN],
  lanes=[('rsProx', 'Proximal tubule', 'glycolysis'), ('rsDist', 'Collecting duct', 'gluconeo'), ('rsDx', 'Labs & causes', 'tca'),
         ('rsGut', 'Gut loss', 'sugars')],
  nodes=[
    ('rs1', 'Type 1 · distal RTA', 380, 1800, 'rsDist', 'α-intercalated H⁺ fails', ['drta', 'rta']),
    ('rs2', 'Type 2 · proximal RTA', 820, 1800, 'rsProx', 'HCO₃⁻ not reclaimed', ['rta', 'hco3reabs']),
    ('rs3', 'Type 4 · hyperkalemic RTA', 1260, 1800, 'rsDist', 'aldosterone low or resisted', ['rta', 'aldoaction', 'mras']),
    ('rs4', 'Normal anion gap', 1700, 1800, 'rsDx', 'HCO₃⁻ ↓ · Cl⁻ ↑', ['nagma', 'agma']),
    ('rs5', 'Urinary anion gap', 2140, 1800, 'rsDx', 'NH₄⁺ by proxy', ['uag', 'newhco3']),
    ('rs6', 'Drug causes', 380, 1940, 'rsDx', 'amphotericin · acetazolamide', ['amphotericin', 'acetazolamide', 'ksparing', 'sulfonamides']),
    ('rs7', 'Fanconi & myeloma', 820, 1940, 'rsProx', 'the whole PCT fails', ['fanconisyn', 'myeloma', 'wilson', 'vitddef']),
    ('rs8', 'Stones & potassium', 1260, 1940, 'rsDx', 'CaPO₄ stones · K⁺ ↓ or ↑', ['calcstone', 'stones', 'hypok', 'hyperk']),
    ('rs9', 'Diarrhea', 1700, 1940, 'rsGut', 'the gut loses HCO₃⁻', ['diarrheaapproach']),
    # m51 — the cards the new causes open
    ('rs10', 'More type 1 causes', 380, 2080, 'rsDist', 'autoimmune · lithium', ['sjogren', 'sle', 'lithium']),
    ('rs11', 'More type 2 causes', 820, 2080, 'rsProx', 'lead · ifosfamide · topiramate', ['lead', 'cyclophos', 'platinum', 'topiramate']),
    ('rs12', 'More type 4 causes', 1260, 2080, 'rsDist', 'low aldosterone', ['diabetickidney', 'acei', 'arbs', 'nsaidkidney', 'heparin',
                                                                       'calcineurin', 'addison'])],
  panels=[
    (2420, 900, 1000, 'The three RTAs (First Aid p. 611)', [
      ('Type 1 · distal', 'α-intercalated cells can’t secrete H⁺ · urine pH > 5.5 · K⁺ ↓ · CaPO₄ stones'),
      ('Type 2 · proximal', 'HCO₃⁻ not reabsorbed · urine pH < 5.5 once HCO₃⁻ is low · K⁺ ↓'),
      ('Type 4 · hyperkalemic', 'aldosterone low or resisted · K⁺ ↑ → less NH₄⁺ · urine pH variable'),
      ('All three', 'normal anion gap (hyperchloremic) metabolic acidosis')]),
    (2420, 1140, 1000, 'Causes (First Aid p. 611)', [
      ('Type 1', 'amphotericin B · analgesic nephropathy · urinary obstruction · SLE'),
      ('Type 2', 'Fanconi syndrome · multiple myeloma · carbonic anhydrase inhibitors'),
      ('Type 4, low aldosterone', 'diabetic hyporeninism · ACE inhibitors, ARBs · NSAIDs · heparin · cyclosporine · adrenal insufficiency'),
      ('Type 4, resistance', 'K⁺-sparing diuretics · obstructive nephropathy · TMP-SMX')]),
    (2420, 1380, 1000, 'Urinary anion gap (Batlle 1988, N Engl J Med)', [
      ('Formula', 'urine Na⁺ + K⁺ − Cl⁻ — a rough index of NH₄⁺'),
      ('Negative', 'plenty of NH₄⁺: the kidney is responding — diarrhea'),
      ('Positive', 'little NH₄⁺: distal acidification fails — type 1 or type 4 RTA')]),
    (2420, 1620, 1000, 'More causes (First Aid pp. 440, 560, 604 · Bootcamp · Robbins · Kaplan & Sadock · Katzung)', [
      ('Type 1', 'Sjögren syndrome (Bootcamp; Robbins ch 6) · lithium, occasionally (Kaplan & Sadock ch 21)'),
      ('Type 2 via Fanconi', 'Wilson disease · lead · ifosfamide · cisplatin · tenofovir · expired tetracyclines (FA pp. 250, 604)'),
      ('Type 2, drugs', 'topiramate — a weak carbonic anhydrase inhibitor (Katzung ch 24; Bootcamp)'),
      ('Type 4', 'heparin — type 4 RTA is a listed adverse effect (FA p. 440)')])],
  dyn=dyn)
