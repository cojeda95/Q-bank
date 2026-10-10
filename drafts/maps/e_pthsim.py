# Calcium & PTH Lab Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The parathyroid glands and their Ca²⁺-sensing receptor, and PTH's three targets — bone, the kidney (proximal
# phosphate reabsorption, distal Ca²⁺ reabsorption, 1α-hydroxylase) and, through calcitriol, the gut. One `one`
# switch picks a disorder; the glands, the targets and the particles change, and five readouts give the lab
# pattern exams ask for: serum Ca²⁺, PO₄³⁻, PTH, calcitriol and urine Ca²⁺.
# No new cards: every fact restates the pinned cards (hyperpara1, hyperpara2, renalod, hypopara, pha, fhh, hcmalig,
# vitddef, sarcoid, pthaction, calcitriol, ckdphos — fact-checked against the corpus) with the First Aid pages they
# cite. Arrows left "–" where those cards give no direction. Anything inferred is marked UNVERIFIED.
# Sources: First Aid 2025 pp. 336–337, 348–349, 361, 621–622 · Costanzo ch 9 · Guyton ch 80 · Katzung ch 42 · Robbins ch 24.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ9, GY80, KZ42, RB24 = full('Costanzo', 9), full('Guyton', 80), full('Katzung', 42), full('Robbins', 24)

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
Z = lambda *k: ['dz:' + x for x in k]
HIPTH = Z('p1', 'p2', 'p3', 'vd', 'pha')      # PTH high
LOPTH = Z('hp', 'mal', 'sarc')                # PTH low
HICA, LOCA = Z('p1', 'p3', 'fhh', 'mal', 'sarc'), Z('p2', 'vd', 'hp', 'pha')
CKD = Z('p2', 'p3')
ALL = HICA + LOCA

# ════════ 1. the parathyroid glands ════════
box(160, 130, 860, 740)
text('Parathyroid glands', 180, 166, 'dyn-big')
text('four, behind the thyroid · chief cells make PTH', 180, 186, 'dyn-cap')
add('<ellipse cx="400" cy="420" rx="110" ry="190" class="dyn-cell" style="opacity:.5"/><ellipse cx="640" cy="420" rx="110" ry="190" class="dyn-cell" style="opacity:.5"/>'
    '<rect x="470" y="440" width="100" height="60" rx="20" class="dyn-cell" style="opacity:.5"/>')
text('thyroid (seen from behind)', 520, 650, 'dyn-cap', 'middle')
GL = [(380, 300), (660, 300), (380, 540), (660, 540)]
gl = lambda pts, r, cls='dyn-soft', style='stroke:var(--dk9);stroke-width:3': ''.join(
    f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{round(r * .7)}" class="{cls}" style="{style}"/>' for x, y in pts)
add(gl(GL, 34), unless=Z('p1', 'p2', 'p3', 'hp', 'mal', 'sarc'))
add(gl(GL[:1], 62) + gl(GL[1:], 30), when=Z('p1'))                       # one adenoma
add(gl(GL, 52), when=CKD)                                                  # all four enlarged
add(gl(GL, 30, 'dyn-soft dyn-dim'), when=Z('hp'))                          # removed or not working
add(gl(GL, 24), when=Z('mal', 'sarc'))                                     # suppressed
text('one adenoma — autonomous PTH', 180, 700, TAG, when=Z('p1'))
text('all four enlarged — responding to low Ca²⁺ and high PO₄³⁻', 180, 700, TAG, when=Z('p2'))
text('autonomous after years of stimulation', 180, 700, TAG, when=Z('p3'))
text('removed at thyroidectomy, autoimmune, or DiGeorge', 180, 700, TAG, when=Z('hp'))
text('the glands work — the targets cannot respond', 180, 700, TAG, when=Z('pha'))
text('suppressed by the high Ca²⁺', 180, 700, TAG, when=Z('mal', 'sarc'))
text('the Ca²⁺ sensor is set too high', 180, 700, TAG, when=Z('fhh'))

# ════════ 2. bone ════════
box(900, 130, 1600, 740)
text('Bone', 920, 166, 'dyn-big')
text('PTH → RANKL on osteoblasts → osteoclasts resorb', 920, 186, 'dyn-cap')
add('<rect x="960" y="300" width="580" height="260" rx="40" class="dyn-cell" style="stroke:var(--dk7)"/>')
text('Ca²⁺ and PO₄³⁻ stored as mineral', 1250, 600, 'nf-l2', 'middle')
text('more resorption — Ca²⁺ and PO₄³⁻ released', 920, 700, TAG, when=Z('p1', 'p3', 'mal'))
text('PTHrP acts on the same PTH receptor', 920, 724, TAG, when=Z('mal'))
text('osteitis fibrosa cystica · brown tumors', 920, 724, TAG, when=Z('p1'))
text('renal osteodystrophy · subperiosteal thinning', 920, 700, TAG, when=Z('p2'))
text('poor mineralization — rickets / osteomalacia', 920, 700, TAG, when=Z('vd'))

# ════════ 3. kidney ════════
box(1640, 130, 2340, 740)
text('Kidney', 1660, 166, 'dyn-big')
text('PTH keeps Ca²⁺, dumps PO₄³⁻, makes calcitriol', 1660, 186, 'dyn-cap')
add('<rect x="1860" y="587" width="260" height="70" rx="20" class="dyn-cell"/>')
text('proximal tubule cell', 1990, 630, 'nf-l2', 'middle')
shapes.append(dict(tube='M1700 300 H2280', w=60))
text('proximal tubule', 1720, 270, 'dyn-cap')
text('distal tubule', 2260, 270, 'dyn-cap', 'end')
text('urine', 2290, 350, 'dyn-cap', 'end')
text('more Ca²⁺ and PO₄³⁻ in the urine', 1660, 700, TAG, when=Z('p1'))
text('Ca²⁺ held back — urine Ca²⁺ low', 1660, 700, TAG, when=Z('fhh'))
text('too few nephrons to filter PO₄³⁻ — it is retained', 1660, 700, TAG, when=CKD)
text('little calcitriol made', 1660, 724, TAG, when=Z('p2', 'hp'))
text('kidney blind to PTH (Gs-α defect)', 1660, 700, TAG, when=Z('pha'))

# ════════ 4. blood ════════
shapes.append(dict(vessel='M180 790 H2320', w=40, color='--dk12'))
text('blood', 2320, 764, 'dyn-cap', 'end')

# ════════ 5. gut ════════
box(160, 840, 1180, 1290)
text('Gut', 180, 876, 'dyn-big')
text('calcitriol builds calbindin — Ca²⁺ and PO₄³⁻ absorbed', 180, 896, 'dyn-cap')
shapes.append(dict(tube='M200 1100 H1140', w=80, color='--dk5'))
text('more Ca²⁺ absorbed', 180, 1250, TAG, when=Z('p1', 'sarc'))
text('less Ca²⁺ absorbed', 180, 1250, TAG, when=Z('p2', 'vd', 'hp'))

# ════════ 6. where the extra comes from ════════
box(1220, 840, 2340, 1290)
text('The feedback loop', 1240, 876, 'dyn-big')
text('low Ca²⁺ → more PTH · high Ca²⁺ → the Ca²⁺-sensing receptor shuts PTH off', 1240, 900, 'nf-l2')
text('calcitriol also feeds back to limit PTH synthesis', 1240, 924, 'nf-l2')
add('<path d="M1460 1030 Q1600 960 1740 1030" class="dyn-line" marker-end="url(#ah-ptGland)"/>'
    '<path d="M1740 1100 Q1600 1170 1460 1100" class="dyn-line" marker-end="url(#ah-ptGland)"/>')
text('serum Ca²⁺', 1400, 1070, 'nf-l1', 'middle')
text('PTH', 1800, 1070, 'nf-l1', 'middle')
TUMOR = '<path d="M1950 1150 q40 -60 90 -20 q50 -40 80 20 q30 60 -40 80 q-60 30 -100 -10 q-50 -20 -30 -70 Z" class="dyn-soft" style="stroke:var(--bad);stroke-width:3"/>'
add(TUMOR, when=Z('mal'))
text('tumor — PTHrP', 2040, 1260, TAG, 'middle', when=Z('mal'))
GRAN = ''.join(f'<circle cx="{x}" cy="{y}" r="22" class="dyn-soft" style="stroke:var(--dk3);stroke-width:3"/>' for x, y in [(1990, 1130), (2040, 1110), (2080, 1150), (2030, 1170)])
add(GRAN, when=Z('sarc'))
text('granuloma macrophages make calcitriol', 2040, 1250, TAG, 'middle', when=Z('sarc'))
text('the loop runs high: PTH rises to fight a low Ca²⁺', 1240, 1250, TAG, when=Z('p2', 'vd', 'pha'))
text('PTH high although Ca²⁺ is high — the loop is broken', 1240, 1250, TAG, when=Z('p1', 'p3'))

# ════════ 7. what the patient shows ════════
box(160, 1330, 2340, 1700)
text('What the patient shows', 180, 1366, 'dyn-big')
text('pick a disorder to see its signs', 180, 1400, 'dyn-cap', unless=ALL)
SIGNS = dict(
  p1=['stones, bones, groans, thrones and psychiatric overtones — often found on a routine calcium', 'short QT interval'],
  p2=['chronic kidney disease · renal osteodystrophy', 'calcium phosphate deposits in soft tissues'],
  p3=['high Ca²⁺ in a long-term dialysis patient', 'treated by parathyroidectomy'],
  vd=['rickets (bow legs, rachitic rosary) or osteomalacia (bone pain, pseudofractures)', 'hypocalcemic tetany'],
  hp=['perioral numbness, carpopedal spasm, tetany · Chvostek and Trousseau signs', 'long QT interval · check Mg²⁺'],
  pha=['short 4th and 5th metacarpals (knuckle dimples), short stature, round face', 'high PTH with low Ca²⁺ is the giveaway'],
  fhh=['mild hypercalcemia with low urinary Ca²⁺', 'observation — not surgery'],
  mal=['squamous cell carcinoma (lung, head and neck), renal, bladder, breast, ovarian carcinoma', 'high Ca²⁺ with suppressed PTH = malignancy until proven otherwise'],
  sarc=['bilateral hilar adenopathy, erythema nodosum', 'hypercalcemia from granuloma 1α-hydroxylase'])
for k, (a, b) in SIGNS.items():
    text(a, 180, 1400, TAG, when=Z(k))
    text(b, 180, 1426, 'nf-l2', when=Z(k))

# ════════ 8. motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M720 790 H2300', len=1580, speed=130, r=6, base=dict(pth=3),
       mods=[m(Z('p1', 'p2', 'vd', 'pha'), set=dict(pth=6)), m(Z('p3'), set=dict(pth=8)), m(LOPTH, set=dict(pth=0)),
             m(Z('mal'), set=dict(pthrp=4))]),
  dict(d='M200 790 H2300', len=2100, speed=100, r=6, base=dict(ca=4),
       mods=[m(HICA, set=dict(ca=8)), m(LOCA, set=dict(ca=2))]),
  dict(d='M1460 560 V770', len=210, speed=70, r=6, base=dict(ca=1, po4=1),
       mods=[m(Z('p1', 'p3', 'mal'), set=dict(ca=3, po4=2))]),
  dict(d='M1710 300 H2270', len=560, speed=110, r=6, base=dict(po4=2, ca=1),
       mods=[m(Z('p1'), set=dict(po4=4, ca=3)), m(Z('mal'), set=dict(po4=4, ca=1)), m(CKD, set=dict(po4=1, ca=1)),
             m(Z('fhh'), set=dict(ca=0, po4=2))]),
  dict(d='M210 1100 H1130', len=920, speed=110, r=6, base=dict(ca=2),
       mods=[m(Z('p1', 'sarc'), set=dict(ca=5)), m(Z('p2', 'vd', 'hp'), set=dict(ca=1))]),
  dict(d='M2040 1140 Q2040 960 2040 810', len=330, speed=90, r=6, base=dict(), mods=[m(Z('mal'), set=dict(pthrp=3)), m(Z('sarc'), set=dict(vd=3))]),
]

# ════════ 9. sites ════════
sites = [
  dict(x=520, y=420, n=[0, 1], w=20, t='rec', l='Ca²⁺-sensing receptor', s='high Ca²⁺ shuts PTH off', ions=[], c='pthaction',
       block=Z('fhh'), sfx=dict(block=' — set too high'), lx=520, ly=230, la='middle'),
  dict(x=700, y=790, n=[0, -1], w=40, t='pump', l='PTH out', s='from the chief cells', reach=60, cross=True,
       ions=[['pth', 'out', 2]], c='pthaction', boost=Z('p1', 'p2', 'p3', 'vd', 'pha'), low=LOPTH,
       sfx=dict(boost=' — high', low=' — low'), lx=700, ly=850, la='middle'),
  dict(x=1250, y=300, n=[0, 1], w=20, t='rec', l='PTH receptor (bone)', s='osteoblasts → RANKL', ions=[], c='pthaction',
       boost=Z('p1', 'p3', 'mal'), block=Z('pha'), sfx=dict(block=' — no response'), lx=1250, ly=360, la='middle'),
  dict(x=1820, y=300, n=[0, 1], w=60, t='co', l='Na⁺–PO₄³⁻ reabsorption', s='PTH turns it down', reach=50, cross=True,
       ions=[['po4', 'in', 1]], c='renalpo4', low=Z('p1', 'mal'), block=Z('pha'), sfx=dict(low=' — PTH holds it back', block=' — no PTH effect'),
       lx=1820, ly=410, la='middle'),
  dict(x=2150, y=300, n=[0, 1], w=60, t='ch', l='Ca²⁺ reabsorption', s='PTH turns it up', reach=50, cross=True,
       ions=[['ca', 'in', 1]], c='pthneph', boost=Z('p1', 'mal', 'fhh'), low=Z('hp'), block=Z('pha'),
       sfx=dict(block=' — no PTH effect'), lx=2150, ly=410, la='middle'),
  dict(x=1990, y=600, n=[0, -1], w=20, t='ex', l='1α-hydroxylase', s='25-OH-D → calcitriol', ions=[], c='calcitriol',
       boost=Z('p1'), low=Z('p2', 'p3', 'hp', 'pha'), stop=Z('vd'), sfx=dict(stop=' — little vitamin D to activate'),
       lx=1990, ly=540, la='middle'),
  dict(x=670, y=1060, n=[0, -1], w=80, t='co', l='Ca²⁺ absorption', s='calbindin, built by calcitriol', reach=60, cross=True,
       ions=[['ca', 'out', 1]], c='calcitriol', boost=Z('p1', 'sarc'), low=Z('p2', 'vd', 'hp'), lx=670, ly=950, la='middle'),
]

# ════════ 10. readouts ════════
readouts = [
  dict(l='Serum Ca²⁺', mods=[m(HICA, d=1), m(LOCA, d=-1)]),
  # p3: PO₄³⁻ ↑ rests on ckdphos (late CKD keeps phosphate high despite high PTH)
  dict(l='Serum PO₄³⁻', mods=[m(Z('p1', 'vd', 'mal'), d=-1), m(Z('p2', 'p3', 'hp', 'pha'), d=1)]),
  # fhh: "PTH normal or minimally elevated" → ↔ · sarc: PTH ↓ — UNVERIFIED, inferred from the high Ca²⁺ (no card states it)
  dict(l='PTH', mods=[m(HIPTH + Z('p3'), d=1), m(LOPTH, d=-1), m(Z('fhh'), d=0)]),
  dict(l='Calcitriol', mods=[m(Z('p1', 'sarc'), d=1), m(Z('p2', 'hp'), d=-1)]),
  dict(l='Urine Ca²⁺', mods=[m(Z('p1'), d=1), m(Z('fhh'), d=-1)]),
]

# ════════ 11. notes ════════
notes = {
  '': 'PTH from the chief cells raises Ca²⁺: it releases Ca²⁺ from bone (via RANKL on osteoblasts), holds Ca²⁺ in the distal '
      'tubule, dumps phosphate in the urine and turns on renal 1α-hydroxylase, so calcitriol pulls Ca²⁺ and PO₄³⁻ from the gut. '
      'Pick a disorder to see the lab pattern.',
  'dz:p1': 'Primary hyperparathyroidism — usually one adenoma secreting PTH on its own: Ca²⁺ ↑, PO₄³⁻ ↓, PTH ↑ (or '
           'inappropriately normal) and urine Ca²⁺ ↑ — the high urine Ca²⁺ separates it from FHH. Most are found on a routine '
           'calcium; brown tumors and stones, bones, groans when advanced.',
  'dz:p2': 'Secondary hyperparathyroidism of chronic kidney disease: failing 1α-hydroxylase lowers calcitriol and phosphate '
           'is retained, so Ca²⁺ falls and all four glands hypertrophy — Ca²⁺ ↓, PO₄³⁻ ↑, PTH ↑, calcitriol ↓. Low Ca²⁺ with '
           'HIGH phosphate = kidney; with LOW phosphate = vitamin D.',
  'dz:p3': 'Tertiary hyperparathyroidism: after long stimulation in kidney disease a gland becomes autonomous — Ca²⁺ and PTH '
           'both high, PTH very high. Think of it in a long-term dialysis patient with high Ca²⁺; treated by parathyroidectomy.',
  'dz:vd': 'Vitamin D deficiency: less Ca²⁺ and PO₄³⁻ absorbed, so Ca²⁺ ↓, PO₄³⁻ ↓, PTH ↑ and alkaline phosphatase ↑ — '
           'rickets in children, osteomalacia in adults. Order 25-OH-D, the storage form, not calcitriol.',
  'dz:hp': 'Hypoparathyroidism: without PTH the kidney stops reabsorbing Ca²⁺ and making calcitriol while phosphate is retained — '
           'Ca²⁺ ↓, PO₄³⁻ ↑, PTH ↓. Tetany, Chvostek and Trousseau signs, long QT; often after a thyroidectomy. Check Mg²⁺.',
  'dz:pha': 'Pseudohypoparathyroidism type 1A: the glands work, but a Gs-α defect leaves kidney and bone blind to PTH — '
            'Ca²⁺ ↓, PO₄³⁻ ↑ with PTH ↑, the giveaway. Albright hereditary osteodystrophy: short 4th and 5th metacarpals, '
            'short stature, round face; maternally inherited.',
  'dz:fhh': 'Familial hypocalciuric hypercalcemia: an inactivating Ca²⁺-sensing receptor mutation makes the glands and tubule '
            'read Ca²⁺ as low — mild Ca²⁺ ↑, PTH normal or slightly ↑, and LOW urine Ca²⁺ (unlike primary '
            'hyperparathyroidism). Observation only.',
  'dz:mal': 'Hypercalcemia of malignancy, PTHrP route — squamous cell carcinomas (lung, head and neck) and renal, bladder, '
            'breast and ovarian carcinoma make PTHrP, which acts on the PTH receptor: Ca²⁺ ↑, PO₄³⁻ ↓ and PTH ↓. High Ca²⁺ '
            'with suppressed PTH = malignancy until proven otherwise.',
  # UNVERIFIED: PTH ↓ in sarcoidosis — inferred from the hypercalcemia; the sarcoid card does not state it
  'dz:sarc': 'Sarcoidosis: granuloma macrophages carry 1α-hydroxylase and make calcitriol, so the gut absorbs more Ca²⁺ — '
             'Ca²⁺ ↑ and calcitriol ↑ while PTH is suppressed.',
}

dyn = dict(
  kinds=dict(pth=['pth', '--dk9'], pthrp=['pth', '--bad'], ca=['ca', '--nf-ca'], po4=['po4', '--dk6'], vd=['vd', '--dk10']),
  groups=[['pth', 'PTH · PTHrP'], ['ca', 'Ca²⁺'], ['po4', 'PO₄³⁻'], ['vd', 'Calcitriol']],
  switches=[dict(id='dz', label='Pick a disorder', type='one',
                 options=[['p1', 'Primary hyperparathyroidism', 'hyperpara1'], ['p2', 'Secondary (kidney disease)', 'hyperpara2'],
                          ['p3', 'Tertiary', 'renalod'], ['vd', 'Vitamin D deficiency', 'vitddef'], ['hp', 'Hypoparathyroidism', 'hypopara'],
                          ['pha', 'Pseudohypoparathyroidism', 'pha'], ['fhh', 'FHH', 'fhh'], ['mal', 'Malignancy — PTHrP', 'hcmalig'],
                          ['sarc', 'Sarcoidosis', 'sarcoid']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 336–337, 348–349, 361, 621–622 · Costanzo ch 9 · Guyton ch 80 · Katzung ch 42 · Robbins ch 24')

MAP = dict(
  id='pthsim', title='Calcium & PTH Lab Simulator', topic='endo', after='hormones',
  sub='The parathyroids, their Ca²⁺ sensor, and PTH’s three targets — bone, kidney and (through calcitriol) gut. Pick a '
      'disorder to see what the glands and targets do and the lab pattern: Ca²⁺, PO₄³⁻, PTH, calcitriol and urine Ca²⁺. '
      'Tap a receptor or transporter for its card',
  w=3500, h=2100,
  fa='336–337, 348–349, 361, 621–622', src=[CZ9, GY80, KZ42, RB24],
  lanes=[('ptGland', 'Parathyroid', 'glycolysis'), ('ptTarget', 'Bone, kidney & gut', 'gluconeo'), ('ptDz', 'Disorders', 'tca')],
  nodes=[
    ('pt1', 'PTH actions & control', 380, 1800, 'ptGland', 'raise Ca²⁺, trash PO₄³⁻', ['pthaction', 'casr']),
    ('pt2', 'Vitamin D', 820, 1800, 'ptTarget', 'skin → liver 25 → kidney 1α', ['calcitriol', 'vitddef']),
    ('pt3', 'PTH on the nephron', 1260, 1800, 'ptTarget', 'phosphaturic · hypocalciuric', ['pthneph', 'renalpo4']),
    ('pt4', 'Hyperparathyroidism', 1700, 1800, 'ptDz', 'primary · secondary · tertiary', ['hyperpara1', 'hyperpara2', 'renalod']),
    ('pt5', 'Low PTH or no response', 2140, 1800, 'ptDz', 'hypo · pseudohypo', ['hypopara', 'pha']),
    ('pt6', 'High Ca²⁺, low PTH', 380, 1940, 'ptDz', 'malignancy · granulomas', ['hcmalig', 'sarcoid']),
    ('pt7', 'FHH', 820, 1940, 'ptDz', 'the sensor set too high', ['fhh']),
    ('pt8', 'Kidney disease', 1260, 1940, 'ptDz', 'phosphate retained', ['ckdphos', 'ckd']),
    ('pt9', 'Treatment', 1700, 1940, 'ptDz', 'bisphosphonates · cinacalcet', ['calciumdrugs'])],
  panels=[
    (2420, 880, 1000, 'The lab patterns (First Aid pp. 348–349)', [
      ('Primary hyperparathyroidism', 'Ca²⁺ ↑ · PO₄³⁻ ↓ · PTH ↑ · urine Ca²⁺ ↑'),
      ('Secondary (CKD)', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↑ · calcitriol ↓'),
      ('Tertiary', 'Ca²⁺ ↑ · PTH ↑↑'),
      ('Vitamin D deficiency', 'Ca²⁺ ↓ · PO₄³⁻ ↓ · PTH ↑ · ALP ↑'),
      ('Hypoparathyroidism', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↓'),
      ('Pseudohypoparathyroidism', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↑'),
      ('FHH', 'Ca²⁺ ↑ · PTH normal or slightly ↑ · urine Ca²⁺ ↓'),
      ('Malignancy (PTHrP)', 'Ca²⁺ ↑ · PO₄³⁻ ↓ · PTH ↓')]),
    (2420, 1180, 1000, 'Telling them apart (First Aid p. 349)', [
      ('Low Ca²⁺, high PO₄³⁻', 'kidney disease, hypoparathyroidism or pseudohypoparathyroidism'),
      ('Low Ca²⁺, low PO₄³⁻', 'vitamin D deficiency'),
      ('High Ca²⁺, urine Ca²⁺ high', 'primary hyperparathyroidism'),
      ('High Ca²⁺, urine Ca²⁺ low', 'FHH'),
      ('High Ca²⁺, PTH low', 'malignancy · granulomas · vitamin D excess')])],
  dyn=dyn)
