# Electrolytes & the ECG (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A lead II strip redrawn for each electrolyte change — low K⁺ (flat T, ST depression, U waves), high K⁺ in its
# order of progression (peaked T → wide QRS with P waves lost → sine wave), high and low Ca²⁺ (short / long QT) and
# low Mg²⁺ (torsades) — over a muscle cell holding most of the body's K⁺ and the routes K⁺ leaves the body.
# A second switch treats hyperkalemia in First Aid's order: stabilize (IV calcium), shift in (insulin + glucose,
# β₂-agonist, bicarbonate), remove (loop diuretic, binder, dialysis).
# No new cards: the facts restate the pinned cards (ecglytes, hyperk, hypok, kinsulin, khandling, hypopara,
# hyperpara1, mgpo4 — fact-checked against the corpus) with the First Aid pages they cite. Waveforms are drawn
# schematically (not to a real mV scale). Anything resting on memory is marked UNVERIFIED.
# Sources: First Aid 2025 pp. 298, 348–349, 608–609 · Costanzo ch 6 · Katzung ch 14–15 · Guyton ch 80.
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ6, KZ14, KZ15, GY80 = full('Costanzo', 6), full('Katzung', 14), full('Katzung', 15), full('Guyton', 80)

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

TAG = 'nf-l2 dyn-tag'
L = lambda *k: ['ly:' + x for x in k]
R = lambda *k: ['rx:' + x for x in k]
HK = L('hk1', 'hk2', 'hk3')
SHIFT, REMOVE = R('ins', 'b2', 'bic'), R('loop', 'binder', 'dial')
LYTES = L('lok', 'hk1', 'hk2', 'hk3', 'hica', 'loca', 'lomg')

# ════════ 1. the ECG strip ════════
box(160, 130, 2340, 760)
text('Lead II — what the ECG shows', 180, 166, 'dyn-big')
text('drawn schematically: the shape changes, not a real millivolt scale', 180, 186, 'dyn-cap')
GX0, GX1, GY0, GY1 = 200, 2300, 220, 720
add(''.join(f'<path d="M{x} {GY0} V{GY1}" class="dyn-line" style="opacity:.12"/>' for x in range(GX0, GX1 + 1, 50))
    + ''.join(f'<path d="M{GX0} {y} H{GX1}" class="dyn-line" style="opacity:.12"/>' for y in range(GY0, GY1 + 1, 50)))
BASE, MV = 500, 150                 # baseline y, px per unit of deflection

def gauss(x, c, w, a):              # a smooth bump of height a, centre c, half-width w
    return a * math.exp(-((x - c) / (w / 2.2)) ** 2)

def beat_y(x, p):
    """deflection at x within one beat (x from 0); p = waveform parameters"""
    y = 0.0
    y += gauss(x, 60, p['pw'], p['pa'])                                  # P
    q0 = 170                                                             # QRS start
    qw = p['qrs']
    y += gauss(x, q0 + qw * 0.15, qw * 0.25, -0.12)                      # Q
    y += gauss(x, q0 + qw * 0.45, qw * 0.35, p['ra'])                    # R
    y += gauss(x, q0 + qw * 0.8, qw * 0.3, -0.28)                        # S
    st0 = q0 + qw
    if st0 < x < st0 + p['st']:                                          # ST segment
        y += p['std'] * min(1, (x - st0) / 20)
    tc = st0 + p['st'] + p['tw'] / 2
    y += gauss(x, tc, p['tw'], p['ta'])                                  # T
    if p['ua']:
        y += gauss(x, tc + p['tw'] / 2 + 60, 70, p['ua'])                # U
    return y

NORMAL = dict(pa=0.15, pw=70, qrs=60, ra=1.15, st=90, std=0, ta=0.32, tw=150, ua=0)
WAVES = dict(
    norm=NORMAL,
    lok=dict(NORMAL, ta=0.07, std=-0.1, ua=0.2),                         # flat T, ST depression, U wave
    hk1=dict(NORMAL, ta=0.95, tw=110),                                   # peaked T
    hk2=dict(NORMAL, pa=0.0, qrs=150, ra=0.8, ta=0.85, tw=130),          # P gone, wide QRS
    hica=dict(NORMAL, st=15),                                            # short QT
    loca=dict(NORMAL, st=230),                                           # long QT
)
BEAT = 700
def strip(p):
    pts = []
    for X in range(GX0, GX1 + 1, 3):
        x = (X - GX0 - 20) % BEAT
        pts.append(f'{X} {round(BASE - MV * beat_y(x, p), 1)}')
    return 'M' + ' L'.join(pts)
def sine():
    return 'M' + ' L'.join(f'{X} {round(BASE - MV * 0.75 * math.sin((X - GX0) / 380 * 2 * math.pi), 1)}' for X in range(GX0, GX1 + 1, 4))
def torsades():
    pts = []
    for X in range(GX0, GX1 + 1, 3):
        t = (X - GX0)
        env = 0.25 + 0.75 * abs(math.sin(t / 700 * math.pi))           # the amplitude waxes and wanes — "twisting"
        pts.append(f'{X} {round(BASE - MV * 1.1 * env * math.sin(t / 95 * 2 * math.pi), 1)}')
    return 'M' + ' L'.join(pts)
TR = 'class="dyn-trace" style="stroke:var(--dk11);stroke-width:4;fill:none"'
add(f'<path d="{strip(WAVES["norm"])}" {TR}/>', unless=LYTES)
for k in ('lok', 'hk1', 'hk2', 'hica', 'loca'):
    add(f'<path d="{strip(WAVES[k])}" {TR}/>', when=L(k))
add(f'<path d="{sine()}" {TR}/>', when=L('hk3'))
add(f'<path d="{torsades()}" {TR}/>', when=L('lomg'))

# labels on the second beat (it starts at x = GX0 + 20 + BEAT = 920)
B2 = GX0 + 20 + BEAT
def at(p, part):
    st0 = 170 + p['qrs']
    return dict(p=B2 + 60, r=B2 + 170 + p['qrs'] * 0.45, t=B2 + st0 + p['st'] + p['tw'] / 2,
                u=B2 + st0 + p['st'] + p['tw'] + 60, qt0=B2 + 170, qt1=B2 + st0 + p['st'] + p['tw'])[part]
text('P', at(NORMAL, 'p'), 460, 'nf-l1', 'middle', unless=LYTES)
text('QRS', at(NORMAL, 'r'), 300, 'nf-l1', 'middle', unless=LYTES)
text('T', at(NORMAL, 't'), 430, 'nf-l1', 'middle', unless=LYTES)
text('flattened T', at(WAVES['lok'], 't'), 440, TAG, 'middle', when=L('lok'))
text('U wave', at(WAVES['lok'], 'u') + 40, 440, TAG, 'middle', when=L('lok'))
text('ST depression', at(WAVES['lok'], 't') - 90, 560, TAG, 'middle', when=L('lok'))
text('peaked T wave', at(WAVES['hk1'], 't'), 330, TAG, 'middle', when=L('hk1'))
text('P waves gone', at(WAVES['hk2'], 'p'), 470, TAG, 'middle', when=L('hk2'))
text('wide QRS', at(WAVES['hk2'], 'r'), 320, TAG, 'middle', when=L('hk2'))
text('sine wave — the last stage', 1250, 330, TAG, 'middle', when=L('hk3'))
text('torsades de pointes — the QRS twists around the baseline', 1250, 300, TAG, 'middle', when=L('lomg'))
# the QT interval bracket
def qt(p, lab, when=None, unless=None):
    x0, x1 = round(at(p, 'qt0')), round(at(p, 'qt1'))
    add(f'<path d="M{x0} 640 V660 H{x1} V640" class="dyn-line" style="stroke:var(--accent);stroke-width:3;fill:none"/>', when, unless)
    text(lab, (x0 + x1) // 2, 690, 'nf-l1' if lab == 'QT' else TAG, 'middle', when, unless)
qt(NORMAL, 'QT', unless=LYTES)
qt(WAVES['hica'], 'short QT', when=L('hica'))
qt(WAVES['loca'], 'long QT', when=L('loca'))

# ════════ 2. a muscle cell: where K⁺ lives ════════
box(160, 800, 1180, 1460)
text('A muscle cell — where K⁺ lives', 180, 836, 'dyn-big')
text('about 98% of the body’s K⁺ is inside cells', 180, 856, 'dyn-cap')
add('<ellipse cx="560" cy="1130" rx="300" ry="190" class="dyn-cell"/>')
shapes.append(dict(membrane='M260 1130 A300 190 0 1 1 860 1130 A300 190 0 1 1 260 1130 Z', w=20))
text('inside: K⁺ about 150 mEq/L', 560, 1110, 'nf-l1', 'middle')
text('blood: K⁺ about 4.5 mEq/L', 980, 1290, 'nf-l1', 'middle')
text('K⁺ high outside — the membrane is less negative, Na⁺ channels inactivate', 180, 1400, TAG, when=HK)
text('K⁺ low outside — weakness, cramps, ileus', 180, 1400, TAG, when=L('lok'))
text('the heart is protected — the K⁺ is unchanged', 180, 1430, TAG, when=R('cag'))
text('K⁺ moved into cells — still in the body', 180, 1430, TAG, when=SHIFT)
text('K⁺ removed from the body', 180, 1430, TAG, when=REMOVE)

# ════════ 3. where K⁺ leaves the body ════════
box(1220, 800, 2340, 1460)
text('Getting K⁺ out of the body', 1240, 836, 'dyn-big')
text('a shift buys time; only removal lowers the body’s total K⁺', 1240, 856, 'dyn-cap')
shapes.append(dict(vessel='M1260 960 H2300', w=40, color='--dk12'))
text('blood', 2300, 930, 'dyn-cap', 'end')
ROUTES = [(1450, 'Kidney — urine', 'loop', 'loop diuretics'), (1780, 'Gut — stool', 'binder', 'binders (patiromer)'),
          (2110, 'Dialysis', 'dial', 'dialysis')]
for x, lab, key, how in ROUTES:
    add(f'<path d="M{x} 990 V1180" class="dyn-line" style="stroke-width:3"/><rect x="{x - 110}" y="1180" width="220" height="80" rx="18" class="dyn-soft"/>')
    add(f'<rect x="{x - 110}" y="1180" width="220" height="80" rx="18" class="dyn-hl" style="fill:none"/>', when=R(key))
    text(lab, x, 1216, 'nf-l1', 'middle')
    text(how, x, 1240, 'nf-l2', 'middle')
# UNVERIFIED: that patiromer works in the gut (binds K⁺ there) — the hyperk card only names "binders (patiromer)"
text('pick a High K⁺ change, then a treatment', 1240, 1330, 'dyn-cap', unless=['rx:*'])

# ════════ 4. what the patient shows ════════
box(160, 1500, 2340, 1700)
text('What the patient shows', 180, 1536, 'dyn-big')
text('pick a change to see its signs', 180, 1570, 'dyn-cap', unless=LYTES)
text('muscle weakness, cramps, ileus, rhabdomyolysis · nephrogenic diabetes insipidus · arrhythmias', 180, 1570, TAG, when=L('lok'))
text('muscle weakness · arrhythmias · cardiac arrest', 180, 1570, TAG, when=HK)
text('stones, bones, groans, thrones and psychiatric overtones', 180, 1570, TAG, when=L('hica'))
text('tetany, perioral numbness · Chvostek and Trousseau signs', 180, 1570, TAG, when=L('loca'))
text('torsades · often with low K⁺ and low Ca²⁺ — they won’t correct until Mg²⁺ is replaced', 180, 1570, TAG, when=L('lomg'))
text('rule out pseudohyperkalemia (a hemolyzed sample) first', 180, 1600, 'nf-l2', when=HK)

# ════════ 5. motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  # K⁺ in the blood outside the cell
  dict(d='M300 1340 Q560 1400 840 1340', len=600, speed=90, r=6, base=dict(k=3), mods=[m(HK, set=dict(k=7)), m(L('lok'), set=dict(k=1)),
       m(SHIFT + REMOVE, set=dict(k=3))]),
  # K⁺ along the vessel, then out by the chosen route
  dict(d='M1270 960 H2290', len=1020, speed=120, r=6, base=dict(k=3), mods=[m(HK, set=dict(k=7)), m(L('lok'), set=dict(k=1)),
       m(REMOVE, set=dict(k=3))]),
  dict(d='M1450 990 V1170', len=180, speed=80, r=6, base=dict(), mods=[m(R('loop'), set=dict(k=4))]),
  dict(d='M1780 990 V1170', len=180, speed=80, r=6, base=dict(), mods=[m(R('binder'), set=dict(k=4))]),
  dict(d='M2110 990 V1170', len=180, speed=80, r=6, base=dict(), mods=[m(R('dial'), set=dict(k=4))]),
]

# ════════ 6. sites ════════
sites = [
  dict(x=560, y=941, n=[0, 1], w=20, t='pump', l='Na⁺/K⁺-ATPase', s='3 Na⁺ out · 2 K⁺ in', reach=40, cross=True,
       ions=[['k', 'out', 2], ['na', 'in', 1]], c='kinsulin', boost=R('ins', 'b2'), lx=560, ly=1000, la='middle'),
  dict(x=860, y=1130, n=[-1, 0], w=20, t='ch', l='K⁺ channel', s='K⁺ leaks out', reach=40, cross=True,
       ions=[['k', 'in', 1]], c='khandling', lx=760, ly=1190, la='end'),
  dict(x=330, y=1030, n=[1, 1], w=20, t='rec', l='Calcium gluconate', s='steadies the heart first', ions=[],
       c='hyperk', need=R('cag'), closed='not given', lx=380, ly=1040, la='start'),
]

# ════════ 7. readouts ════════
readouts = [
  dict(l='Serum K⁺', mods=[m(L('lok'), d=-1), m(HK, d=1)]),
  dict(l='T wave', mods=[m(L('lok'), d=-1), m(L('hk1', 'hk2'), d=1)]),
  dict(l='QRS width', mods=[m(L('hk2', 'hk3'), d=1)]),
  dict(l='QT interval', mods=[m(L('hica'), d=-1), m(L('loca'), d=1)]),
  dict(l='Serum Ca²⁺', mods=[m(L('hica'), d=1), m(L('loca', 'lomg'), d=-1)]),
  # UNVERIFIED: calcium gluconate leaves K⁺ unchanged (↔) — inferred from the hyperk card's order (stabilize, then shift, then remove)
  dict(l='K⁺ after the drug', mods=[m(R('cag'), d=0), m(SHIFT + REMOVE, d=-1)]),
]

# ════════ 8. notes ════════
notes = {
  '': 'Potassium and calcium change how the heart repolarizes, so the ECG can be the first clue to an electrolyte disorder. '
      'Pick a change to see the strip redrawn, then try treating high K⁺.',
  'ly:lok': 'Low K⁺: flattened T waves, ST depression and prominent U waves, with arrhythmias, muscle weakness, cramps and ileus. '
            'K⁺ shifts into cells with insulin, β₂-agonists and alkalosis, and is lost with diuretics, diarrhea and '
            'hyperaldosteronism. Check Mg²⁺ — low K⁺ will not correct until it is replaced.',
  'ly:hk1': 'High K⁺, early: peaked T waves. High K⁺ depolarizes the resting membrane. It shifts out of cells with insulin lack, '
            'β-blockade, acidosis, digoxin and cell lysis, and builds up when the kidney cannot secrete it (renal failure, low aldosterone).',
  'ly:hk2': 'High K⁺, worse: the QRS widens and P waves are lost. High K⁺ depolarizes the resting membrane and inactivates Na⁺ '
            'channels. Give IV calcium gluconate first.',
  'ly:hk3': 'High K⁺, severe: the strip becomes a sine wave — the last stage of the progression, with cardiac arrest the risk. '
            'Stabilize, shift and remove.',
  'ly:hica': 'High Ca²⁺: a short QT interval — a clue to hypercalcemia such as primary hyperparathyroidism, with stones, bones, '
             'groans, thrones and psychiatric overtones.',
  'ly:loca': 'Low Ca²⁺: a long QT interval, with tetany, perioral numbness and Chvostek and Trousseau signs — e.g., after '
             'accidental parathyroid removal during thyroidectomy.',
  'ly:lomg': 'Low Mg²⁺: torsades de pointes, often with low K⁺ and low Ca²⁺ — magnesium is needed for PTH release and for the '
             'kidney to hold K⁺. Torsades → give IV magnesium.',
  # UNVERIFIED: "it does not move K⁺" — see the readout note above
  'rx:cag': 'IV calcium gluconate comes first in hyperkalemia: it stabilizes the heart. It does not move K⁺ — that still has '
            'to be shifted into cells or removed.',
  'rx:ins': 'Insulin, given with glucose, stimulates the Na⁺/K⁺-ATPase and moves K⁺ into cells — fast, but the K⁺ stays in '
            'the body.',
  'rx:b2': 'A β₂-agonist also drives K⁺ into cells through the Na⁺/K⁺-ATPase — a shift, not a removal.',
  'rx:bic': 'Bicarbonate shifts K⁺ into cells — alkalosis moves K⁺ in, as acidosis moves it out.',
  'rx:loop': 'A loop diuretic removes K⁺ in the urine — total body K⁺ falls.',
  'rx:binder': 'A binder such as patiromer removes K⁺ from the body.',
  'rx:dial': 'Dialysis removes K⁺ from the blood — the route when the kidneys have failed.',
  'rx:*&!ly:hk1&!ly:hk2&!ly:hk3': 'These treatments are for high K⁺ — pick a High K⁺ change to see them act.',
}

dyn = dict(
  kinds=dict(k=['k', '--nf-k'], na=['na', '--nf-na']),
  groups=[['k', 'K⁺'], ['na', 'Na⁺']],
  switches=[dict(id='ly', label='Pick an electrolyte change', type='one',
                 options=[['lok', 'Low K⁺', 'hypok'], ['hk1', 'High K⁺ — early', 'hyperk'], ['hk2', 'High K⁺ — worse', 'hyperk'],
                          ['hk3', 'High K⁺ — severe', 'hyperk'], ['hica', 'High Ca²⁺', 'ecglytes'], ['loca', 'Low Ca²⁺', 'hypopara'],
                          ['lomg', 'Low Mg²⁺', 'mgpo4']]),
            dict(id='rx', label='Treat high K⁺ — stabilize, shift, remove', type='one',
                 options=[['cag', 'IV calcium gluconate', 'hyperk'], ['ins', 'Insulin + glucose', 'kinsulin'], ['b2', 'β₂-agonist', 'kinsulin'],
                          ['bic', 'Bicarbonate', 'hyperk'], ['loop', 'Loop diuretic', 'loopdiuretics'], ['binder', 'Binder (patiromer)', 'hyperk'],
                          ['dial', 'Dialysis', 'hyperk']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 298, 348–349, 608–609 · Costanzo ch 6 · Katzung ch 14–15 · Guyton ch 80')

MAP = dict(
  id='lyteecg', title='Electrolytes & the ECG', topic='cardio', after='ecgsim',
  sub='A lead II strip redrawn for low K⁺, high K⁺ as it worsens (peaked T → wide QRS → sine wave), high and low Ca²⁺ and low '
      'Mg²⁺ — then treat high K⁺ in order: stabilize, shift into cells, remove. Tap the pump or a channel for its card',
  w=3500, h=2100,
  fa='298, 348–349, 608–609', src=[CZ6, KZ14, KZ15, GY80],
  lanes=[('leK', 'Potassium', 'glycolysis'), ('leCa', 'Calcium & magnesium', 'tca'), ('leRx', 'Treating high K⁺', 'gluconeo')],
  nodes=[
    ('le1', 'Electrolytes on the ECG', 380, 1800, 'leK', 'peaked T · U wave · QT', ['ecglytes']),
    ('le2', 'High K⁺', 820, 1800, 'leK', 'causes and treatment', ['hyperk', 'tls', 'rhabdo', 'digoxin']),
    ('le3', 'Low K⁺', 1260, 1800, 'leK', 'shifts and losses', ['hypok', 'periodicpara']),
    ('le4', 'K⁺ inside cells', 1700, 1800, 'leK', 'pump, shifts, nephron', ['kinsulin', 'khandling', 'nakpump']),
    ('le5', 'Calcium & the QT', 380, 1940, 'leCa', 'short or long', ['hypopara', 'hyperpara1']),
    ('le6', 'Magnesium', 820, 1940, 'leCa', 'torsades', ['mgpo4', 'longqt']),
    ('le7', 'Removing K⁺', 1260, 1940, 'leRx', 'urine · gut · dialysis', ['loopdiuretics', 'ksparing'])],
  panels=[
    (2420, 860, 1000, 'Electrolytes on the ECG (First Aid pp. 298, 609)', [
      ('Low K⁺', 'flattened T waves, ST depression, prominent U waves'),
      ('High K⁺', 'peaked T waves → wide QRS, P waves lost → sine wave'),
      ('High Ca²⁺', 'short QT interval'),
      ('Low Ca²⁺', 'long QT interval · tetany, Chvostek and Trousseau signs'),
      ('Low Mg²⁺', 'torsades de pointes · often with low K⁺ and Ca²⁺')]),
    (2420, 1100, 1000, 'Treating high K⁺ (First Aid p. 609; Katzung ch 15)', [
      ('1 · Stabilize', 'IV calcium gluconate — the heart first'),
      ('2 · Shift in', 'insulin + glucose · β₂-agonist · bicarbonate'),
      ('3 · Remove', 'loop diuretics · binders (patiromer) · dialysis'),
      ('First', 'rule out pseudohyperkalemia — a hemolyzed sample')]),
    (2420, 1320, 1000, 'What moves K⁺ (Costanzo ch 6)', [
      ('Into cells', 'insulin · β₂-agonists · α-antagonists · alkalosis · hypo-osmolarity'),
      ('Out of cells', 'insulin lack · β-blockers · α-agonists · acidosis · hyperosmolarity · cell lysis · exercise'),
      ('Out of the body', 'the distal nephron: principal cells secrete K⁺ under aldosterone')])],
  dyn=dyn)
