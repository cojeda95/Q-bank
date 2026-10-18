# Calcium & PTH Lab Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The parathyroid glands and their Ca²⁺-sensing receptor, and PTH's three targets — bone, the kidney (proximal
# phosphate reabsorption, distal Ca²⁺ reabsorption, 1α-hydroxylase) and, through calcitriol, the gut. One `one`
# switch picks a disorder; the glands, the targets and the particles change, and five readouts give the lab
# pattern exams ask for: serum Ca²⁺, PO₄³⁻, PTH, calcitriol and urine Ca²⁺.
# No new cards: every fact restates the pinned cards (hyperpara1, hyperpara2, renalod, hypopara, pha, fhh, hcmalig,
# vitddef, sarcoid, pthaction, calcitriol, ckdphos — fact-checked against the corpus) with the First Aid pages they
# cite, checked against Costanzo Table 9.17 and Robbins ch 24 (Causes of hypercalcemia). Arrows left "–" where no source gives one.
# Sources: First Aid 2025 pp. 224, 336–337, 348–349, 361, 621–622, 695 · Costanzo ch 9 · Guyton ch 80 · Katzung ch 42 · Robbins ch 20, 24.
# m52 upgrade (2026-10-18): 13 more causes grouped with `sections` (by serum Ca²⁺ and what PTH does), two more readouts
# (urine cAMP, alkaline phosphatase), and calcitriol ↓ for the PTHrP route. Option keys of the 9 old disorders unchanged
# (p1 p2 p3 vd hp pha fhh mal sarc); only their order changed. Every old shape/flow/site keeps its index (flows 0, 1, 5 carry
# guide tracks in m47 tracks.json); new shapes are appended in section 7b, new flows after flow 5. Old shapes/sites only had
# their when/unless/boost/low lists widened to the new keys.
# Added sources: First Aid 2025 pp. 68 (vitamin D excess), 205 + 404 (pancreatitis: Ca²⁺ soaps), 213 (granulomas), 406 (milk-alkali),
# 434 (citrate), 436 (myeloma CRAB), 440 (tumor lysis), 592 (lithium), 609 (Mg²⁺), 621 (myoglobinuria), 626–627 (loop, thiazide) ·
# Robbins ch 24 Table 24.5 (PTH ↓: malignancy, vitamin D toxicity, immobilization, thiazides, granulomatous disease) · Robbins ch 2
# (immobilization, milk-alkali) · Guyton ch 80 (excess dietary Ca²⁺, vitamin D, disuse → parathyroids suppressed) · Katzung ch 42
# (hyperphosphatemia in vitamin D intoxication; Mg²⁺ deficiency inhibits PTH secretion and response; citrated blood) · Katzung ch 15
# (loops: hypercalciuria, serum Ca²⁺ seldom falls) · Costanzo ch 7 Table 7.5 (milk-alkali alkalosis) · Kaplan & Sadock ch 21
# (lithium: hyperparathyroidism) · Bootcamp Nephrology Electrolytes (TLS, rhabdomyolysis: PO₄³⁻ released, precipitates Ca²⁺) ·
# Stewart AF et al. N Engl J Med 1980;303:1377–83, PMID 6253785 (humoral cancer hypercalcemia: 1,25-(OH)₂D markedly reduced vs
# primary hyperparathyroidism, means 20 vs 83 pg/mL; nephrogenous cAMP elevated) · Schilling T et al. J Clin Endocrinol Metab
# 1993;76:801–3, PMID 8445039 (1,25-(OH)₂D suppressed or low-normal in hypercalcemia of malignancy, PTHrP does not raise it).
# NOTE for the owner: Costanzo Table 9.17 prints 1,25-(OH)₂D ↑ for humoral hypercalcemia of malignancy (by analogy with PTH);
# the measured data above contradict it, so the map follows the papers. Cut for lack of a corpus source: hungry bone syndrome.
# Not added as options (already covered): CKD (p2/p3). Other granulomatous diseases are folded into sarc (FA pp. 68, 213).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ9, GY80, KZ42, RB24, RB20 = full('Costanzo', 9), full('Guyton', 80), full('Katzung', 42), full('Robbins', 24), full('Robbins', 20)
CZ7, KZ15, RB2, KS21 = full('Costanzo', 7), full('Katzung', 15), full('Robbins', 2), full('Kaplan & Sadock', 21)
BCE = 'Bootcamp.com Nephrology — Electrolytes'

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
# m52 keys: li lithium · lym lymphoma · mm myeloma/lytic metastases · vdx vitamin D excess · milk milk-alkali · thz thiazide ·
# imm immobilization · mg severe hypomagnesemia · panc pancreatitis · tx massive transfusion · tls tumor lysis · rhab rhabdomyolysis · loop
SUPPN = Z('lym', 'mm', 'vdx', 'milk', 'thz', 'imm')   # m52: high Ca²⁺ from outside the glands — PTH ↓ (Robbins Table 24.5, FA p. 348, Guyton ch 80)
SUPP = Z('mal', 'sarc') + SUPPN
HIPTH = Z('p1', 'p2', 'p3', 'vd', 'pha', 'li')         # PTH high
LOPTH = Z('hp', 'mal', 'sarc') + SUPPN + Z('mg')        # PTH low
HICA = Z('p1', 'p3', 'fhh', 'mal', 'sarc', 'li') + SUPPN
LOCA = Z('p2', 'vd', 'hp', 'pha', 'mg', 'panc', 'tx', 'tls', 'rhab')
CKD = Z('p2', 'p3')
ALL = HICA + LOCA + Z('loop')

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
add(gl(GL, 34), unless=Z('p1', 'p2', 'p3', 'hp', 'mg') + SUPP)
add(gl(GL[:1], 62) + gl(GL[1:], 30), when=Z('p1'))                       # one adenoma
add(gl(GL, 52), when=CKD)                                                  # all four enlarged
add(gl(GL, 30, 'dyn-soft dyn-dim'), when=Z('hp', 'mg'))                    # removed / not working · m52: no Mg²⁺ to release PTH
add(gl(GL, 24), when=SUPP)                                                 # suppressed
text('one adenoma — autonomous PTH', 180, 700, TAG, when=Z('p1'))
text('all four enlarged — responding to low Ca²⁺ and high PO₄³⁻', 180, 700, TAG, when=Z('p2'))
text('autonomous after years of stimulation', 180, 700, TAG, when=Z('p3'))
text('removed at thyroidectomy, autoimmune, or DiGeorge', 180, 700, TAG, when=Z('hp'))
text('the glands work — the targets cannot respond', 180, 700, TAG, when=Z('pha'))
text('suppressed by the high Ca²⁺', 180, 700, TAG, when=SUPP)
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
text('kidney blind to PTH (Gs-α defect) — PO₄³⁻ kept, urine cAMP ↓', 1660, 700, TAG, when=Z('pha'))
text('no PTH — PO₄³⁻ kept, less Ca²⁺ reabsorbed', 1660, 700, TAG, when=Z('hp'))
text('PTHrP acts like PTH — PO₄³⁻ and Ca²⁺ spill (high filtered load)', 1660, 700, TAG, when=Z('mal'))
text('more Ca²⁺ in the urine — high filtered load', 1660, 700, TAG, when=Z('sarc'))

# ════════ 4. blood ════════
shapes.append(dict(vessel='M180 790 H2320', w=40, color='--dk12'))
text('blood', 2320, 764, 'dyn-cap', 'end')

# ════════ 5. gut ════════
box(160, 840, 1180, 1290)
text('Gut', 180, 876, 'dyn-big')
text('calcitriol builds calbindin — Ca²⁺ and PO₄³⁻ absorbed', 180, 896, 'dyn-cap')
shapes.append(dict(tube='M200 1100 H1140', w=80, color='--dk5'))
text('more Ca²⁺ absorbed', 180, 1250, TAG, when=Z('p1', 'sarc', 'vdx', 'lym'))
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
text('PTH high although Ca²⁺ is high — the loop is broken', 1240, 1250, TAG, when=Z('p1', 'p3', 'li'))

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

# ════════ 7b. m52 additions — appended after every older shape (keeps the old shape indices) ════════
# glands
text('lithium can cause hyperparathyroidism (Kaplan & Sadock)', 180, 700, TAG, when=Z('li'))
text('too little Mg²⁺ — PTH is not released', 180, 700, TAG, when=Z('mg'))                     # FA p. 336 · Katzung ch 42
# bone: myeloma's lytic holes; disuse
HOLES = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{round(r * .75)}" class="dyn-soft" style="stroke:var(--bad);stroke-width:3"/>'
                for x, y, r in [(1040, 470, 26), (1130, 510, 18), (1320, 495, 22), (1390, 440, 16), (1090, 400, 14)])
add(HOLES, when=Z('mm'))
text('lytic lesions — tumor cytokines (IL-1, TNF-α, RANKL) drive osteoclasts', 920, 700, TAG, when=Z('mm'))   # FA p. 436
text('disuse — bone is resorbed without any PTH push', 920, 700, TAG, when=Z('imm'))                       # Guyton ch 80 · Robbins ch 2
# kidney
text('thiazide — the distal tubule reabsorbs more Ca²⁺', 1660, 700, TAG, when=Z('thz'))               # FA p. 627
text('loop diuretic — the thick ascending limb wastes Ca²⁺', 1660, 700, TAG, when=Z('loop'))          # FA p. 626
text('more Ca²⁺ in the urine — hypercalciuria', 1660, 700, TAG, when=Z('vdx'))                        # FA p. 68
text('calcitriol low despite PTHrP (Stewart 1980)', 1660, 724, TAG, when=Z('mal'))
text('calcium phosphate and uric acid crystals — acute kidney injury', 1660, 700, TAG, when=Z('tls'))  # FA p. 440
text('myoglobin injures the tubules — acute tubular necrosis', 1660, 700, TAG, when=Z('rhab'))         # FA p. 621
# gut
text('a big Ca²⁺ and alkali load swallowed — milk, calcium carbonate', 180, 1250, TAG, when=Z('milk'))   # Robbins ch 2 · FA p. 406
# feedback loop: why PTH is off, and the source drawn at the right
text('Ca²⁺ comes from outside the glands — PTH is shut off', 1240, 1250, TAG, when=SUPPN)
text('Ca²⁺ is low, yet PTH cannot rise — its release needs Mg²⁺', 1240, 1250, TAG, when=Z('mg'))
NODE = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="34" ry="24" class="dyn-soft" style="stroke:var(--dk3);stroke-width:3"/>'
               for x, y in [(1985, 1140), (2060, 1120), (2090, 1175), (2020, 1190)])
add(NODE, when=Z('lym'))
text('lymphoma cells make calcitriol', 2040, 1250, TAG, 'middle', when=Z('lym'))                     # FA p. 224
LYSE = ''.join(f'<path d="M{x} {y} h50 v34 h-18 l-6 -10 l-6 10 h-20 Z" class="dyn-soft" style="stroke:var(--bad);stroke-width:3"/>'
               for x, y in [(1960, 1120), (2030, 1105), (2080, 1160), (1990, 1175)])
add(LYSE, when=Z('tls', 'rhab'))
text('tumor cells burst — K⁺, PO₄³⁻ and uric acid out', 2040, 1250, TAG, 'middle', when=Z('tls'))
text('muscle breaks down — PO₄³⁻ out', 2040, 1250, TAG, 'middle', when=Z('rhab'))
FAT = ''.join(f'<circle cx="{x}" cy="{y}" r="24" class="dyn-soft" style="stroke:var(--dk5);stroke-width:3"/>'
              for x, y in [(1990, 1130), (2045, 1115), (2095, 1150), (2040, 1170)])
add(FAT, when=Z('panc'))
text('fat necrosis — fatty acids bind Ca²⁺ as soaps', 2040, 1250, TAG, 'middle', when=Z('panc'))         # FA pp. 205, 404
add('<rect x="1990" y="1090" width="100" height="120" rx="18" class="dyn-soft" style="stroke:var(--bad);stroke-width:3"/>'
    '<path d="M2040 1090 V1060" class="dyn-line"/>', when=Z('tx'))
text('stored blood — citrate binds Ca²⁺', 2040, 1250, TAG, 'middle', when=Z('tx'))                       # FA p. 434
# signs
SIGNS2 = dict(
  li=['on lithium for bipolar disorder — mild hypercalcemia', 'also nephrogenic diabetes insipidus and thyroid effects · check calcium'],
  vdx=['hypercalcemia, hypercalciuria, loss of appetite, stupor', 'too much vitamin D — PTH suppressed'],
  milk=['large amounts of milk or calcium carbonate antacid', 'hypercalcemia with metabolic alkalosis (with renal failure)'],
  thz=['on a thiazide — hyperGLUC: glucose, lipids, uric acid and calcium up', 'the same drug treats idiopathic hypercalciuria and calcium stones'],
  imm=['prolonged bed rest or immobilization', 'disuse bone resorption — PTH falls'],
  lym=['lymphoma — the calcitriol route of hypercalcemia of malignancy', 'high Ca²⁺, low PTH, high calcitriol'],
  mm=['multiple myeloma — CRAB: hyperCalcemia, Renal insufficiency, Anemia, Bone lytic lesions', 'or bone metastases (e.g., breast)'],
  mg=['tetany, torsades de pointes, low K⁺', 'diarrhea, aminoglycosides, diuretics, alcohol use disorder · check Mg²⁺ in refractory hypocalcemia'],
  panc=['acute pancreatitis — epigastric pain radiating to the back, lipase ↑', 'hypocalcemia is a listed complication'],
  tx=['many units of stored blood given fast', 'tetany, even convulsions · K⁺ rises too'],
  tls=['days after chemotherapy for a bulky, fast tumor (lymphoma, leukemia)', 'K⁺ ↑ · PO₄³⁻ ↑ · uric acid ↑ · Ca²⁺ ↓ — acute kidney injury'],
  rhab=['crush injury, immobilization, statins — dark urine, CK ↑↑', 'PO₄³⁻ released from muscle precipitates Ca²⁺'],
  loop=['on furosemide — Loops Lose Ca²⁺', 'with saline, a treatment for hypercalcemia'])
for k, (a, b) in SIGNS2.items():
    text(a, 180, 1400, TAG, when=Z(k))
    text(b, 180, 1426, 'nf-l2', when=Z(k))

# ════════ 8. motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M720 790 H2300', len=1580, speed=130, r=6, base=dict(pth=3),
       mods=[m(Z('p1', 'p2', 'vd', 'pha', 'li'), set=dict(pth=6)), m(Z('p3'), set=dict(pth=8)), m(LOPTH, set=dict(pth=0)),
             m(Z('mal'), set=dict(pthrp=4))]),
  dict(d='M200 790 H2300', len=2100, speed=100, r=6, base=dict(ca=4),
       mods=[m(HICA, set=dict(ca=8)), m(LOCA, set=dict(ca=2))]),
  dict(d='M1460 560 V770', len=210, speed=70, r=6, base=dict(ca=1, po4=1),
       mods=[m(Z('p1', 'p3', 'mal'), set=dict(ca=3, po4=2)), m(Z('mm', 'imm'), set=dict(ca=3))]),
  dict(d='M1710 300 H2270', len=560, speed=110, r=6, base=dict(po4=2, ca=1),
       mods=[m(Z('p1'), set=dict(po4=4, ca=3)), m(Z('mal'), set=dict(po4=4, ca=3)), m(Z('hp', 'pha'), set=dict(po4=1, ca=1)), m(CKD, set=dict(po4=1, ca=1)),
             m(Z('fhh', 'thz'), set=dict(ca=0, po4=2)), m(Z('loop', 'vdx'), set=dict(ca=3))]),
  dict(d='M210 1100 H1130', len=920, speed=110, r=6, base=dict(ca=2),
       mods=[m(Z('p1', 'sarc', 'vdx', 'lym', 'milk'), set=dict(ca=5)), m(Z('p2', 'vd', 'hp'), set=dict(ca=1))]),
  dict(d='M2040 1140 Q2040 960 2040 810', len=330, speed=90, r=6, base=dict(), mods=[m(Z('mal'), set=dict(pthrp=3)), m(Z('sarc', 'lym'), set=dict(vd=3))]),
  # m52 — flow 6: phosphate out of dying cells into the blood (tumor lysis, rhabdomyolysis)
  dict(d='M2040 1140 Q2040 960 2040 810', len=330, speed=90, r=6, base=dict(), mods=[m(Z('tls', 'rhab'), set=dict(po4=3))]),
  # m52 — flow 7: Ca²⁺ pulled out of the blood (bound as soaps in pancreatitis, by citrate in transfused blood)
  dict(d='M2000 810 Q2000 960 2000 1110', len=300, speed=80, r=6, base=dict(), mods=[m(Z('panc', 'tx'), set=dict(ca=3))]),
]

# ════════ 9. sites ════════
sites = [
  dict(x=520, y=420, n=[0, 1], w=20, t='rec', l='Ca²⁺-sensing receptor', s='high Ca²⁺ shuts PTH off', ions=[], c='pthaction',
       block=Z('fhh'), sfx=dict(block=' — set too high'), lx=520, ly=230, la='middle'),
  dict(x=700, y=790, n=[0, -1], w=40, t='pump', l='PTH out', s='from the chief cells', reach=60, cross=True,
       ions=[['pth', 'out', 2]], c='pthaction', boost=Z('p1', 'p2', 'p3', 'vd', 'pha', 'li'), low=LOPTH,
       sfx=dict(boost=' — high', low=' — low'), lx=700, ly=850, la='middle'),
  dict(x=1250, y=300, n=[0, 1], w=20, t='rec', l='PTH receptor (bone)', s='osteoblasts → RANKL', ions=[], c='pthaction',
       boost=Z('p1', 'p3', 'mal'), block=Z('pha'), sfx=dict(block=' — no response'), lx=1250, ly=360, la='middle'),
  dict(x=1820, y=300, n=[0, 1], w=60, t='co', l='Na⁺–PO₄³⁻ reabsorption', s='PTH turns it down', reach=50, cross=True,
       ions=[['po4', 'in', 1]], c='renalpo4', low=Z('p1', 'mal'), boost=Z('hp', 'pha'), sfx=dict(low=' — PTH holds it back', boost=' — no PTH brake'),
       lx=1820, ly=410, la='middle'),
  dict(x=2150, y=300, n=[0, 1], w=60, t='ch', l='Ca²⁺ reabsorption', s='PTH turns it up', reach=50, cross=True,
       ions=[['ca', 'in', 1]], c='pthneph', boost=Z('p1', 'mal', 'fhh', 'thz'), low=Z('hp', 'pha'),
       sfx=dict(low=' — little PTH effect'), lx=2150, ly=410, la='middle'),
  # m52: mal joins the "low" list — calcitriol is low in humoral hypercalcemia of malignancy (Stewart 1980; Schilling 1993)
  dict(x=1990, y=600, n=[0, -1], w=20, t='ex', l='1α-hydroxylase', s='25-OH-D → calcitriol', ions=[], c='calcitriol',
       boost=Z('p1'), low=Z('p2', 'p3', 'hp', 'pha', 'mal'), stop=Z('vd'), sfx=dict(stop=' — little vitamin D to activate'),
       lx=1990, ly=540, la='middle'),
  dict(x=670, y=1060, n=[0, -1], w=80, t='co', l='Ca²⁺ absorption', s='calbindin, built by calcitriol', reach=60, cross=True,
       ions=[['ca', 'out', 1]], c='calcitriol', boost=Z('p1', 'sarc', 'vdx', 'lym', 'milk'), low=Z('p2', 'vd', 'hp'), lx=670, ly=950, la='middle'),
]

# ════════ 10. readouts ════════
readouts = [
  # m52 — high: lithium (FA p. 592), vitamin D excess (FA p. 68), milk-alkali (FA p. 406), thiazides (FA p. 627), immobilization and
  # granulomas (Katzung ch 42; Robbins Table 24.5), lymphoma (FA p. 224), myeloma (FA p. 436). Low: severe hypomagnesemia (FA p. 609),
  # pancreatitis (FA p. 404), massive transfusion (FA p. 434), tumor lysis (FA p. 440), rhabdomyolysis (Bootcamp; rhabdo card).
  # Loop diuretics: no arrow — Katzung ch 15 says they "do not generally cause hypocalcemia" (at most mild)
  dict(l='Serum Ca²⁺', mods=[m(HICA, d=1), m(LOCA, d=-1)]),
  # p3: PO₄³⁻ ↑ — ckdphos and FA p. 622 (late CKD keeps phosphate high despite high PTH)
  # m52 — ↑ in vitamin D intoxication (Katzung ch 42 "Hyperphosphatemia … vitamin D intoxication"; vitddef card), tumor lysis (FA p. 440),
  # rhabdomyolysis (Bootcamp Electrolytes)
  dict(l='Serum PO₄³⁻', mods=[m(Z('p1', 'vd', 'mal'), d=-1), m(Z('p2', 'p3', 'hp', 'pha', 'vdx', 'tls', 'rhab'), d=1)]),
  # fhh: "PTH normal or minimally elevated" → ↔ · sarc: PTH ↓ — Robbins ch 24 Table (granulomatous disease under "Decreased PTH")
  # m52 — li ↑ (Kaplan & Sadock ch 21: hyperparathyroidism); ↓ for vitamin D toxicity, immobilization, thiazides (Robbins Table 24.5),
  # excess Ca²⁺ intake and cancer (FA p. 348 figure: PTH-independent hypercalcemia; Guyton ch 80), lymphoma (hcmalig card),
  # severe hypomagnesemia (FA p. 336 "↓↓ serum Mg²⁺ → ↓ PTH secretion"; Katzung ch 42)
  dict(l='PTH', mods=[m(HIPTH + Z('p3'), d=1), m(LOPTH, d=-1), m(Z('fhh'), d=0)]),
  # Costanzo Table 9.17: 1,25-(OH)₂D ↑ in primary, ↓ in hypo-, pseudohypo- and CKD. Lymphoma ↑ (FA p. 224).
  # m52 — mal ↓: measured 1,25-(OH)₂D markedly reduced in humoral cancer hypercalcemia (Stewart 1980, PMID 6253785) and suppressed or
  # low-normal (Schilling 1993, PMID 8445039). Costanzo Table 9.17 prints ↑ here; the audit (m52 F2) ruled that unsupported.
  dict(l='Calcitriol', mods=[m(Z('p1', 'sarc', 'lym'), d=1), m(Z('p2', 'hp', 'pha', 'mal'), d=-1)]),
  # urine Ca²⁺ ↑ from the high filtered load: primary and malignancy (Costanzo Table 9.17), sarcoidosis (Robbins ch 20)
  # m52 — ↑ vitamin D excess (FA p. 68 hypercalciuria), loop diuretics (FA p. 626 "↑ Ca²⁺ excretion"); ↓ thiazides (FA p. 627)
  dict(l='Urine Ca²⁺', mods=[m(Z('p1', 'mal', 'sarc', 'vdx', 'loop'), d=1), m(Z('fhh', 'thz'), d=-1)]),
  # m52 — urine cAMP: ↑ primary (FA p. 349; Costanzo Table 9.17) and PTHrP (Costanzo Table 9.17; nephrogenous cAMP high, Stewart 1980);
  # ↓ surgical hypoparathyroidism and pseudohypoparathyroidism (Costanzo Table 9.17)
  dict(l='Urine cAMP', mods=[m(Z('p1', 'mal'), d=1), m(Z('hp', 'pha'), d=-1)]),
  # m52 — alkaline phosphatase: ↑ primary (FA p. 349), secondary of CKD (FA pp. 348–349), vitamin D deficiency and pseudohypo-
  # parathyroidism (FA p. 348 table); "—" (normal) in hypoparathyroidism (FA p. 348 table); ↑ in Costanzo Box 9.5 (PTHrP lung cancer)
  dict(l='ALP', mods=[m(Z('p1', 'p2', 'vd', 'pha', 'mal'), d=1), m(Z('hp'), d=0)]),
]

# ════════ 11. notes ════════
notes = {
  '': 'PTH from the chief cells raises Ca²⁺: it releases Ca²⁺ from bone (via RANKL on osteoblasts), holds Ca²⁺ in the distal '
      'tubule, dumps phosphate in the urine and turns on renal 1α-hydroxylase, so calcitriol pulls Ca²⁺ and PO₄³⁻ from the gut. '
      'Pick a disorder or a cause to see the lab pattern.',
  'dz:p1': 'Primary hyperparathyroidism — usually one adenoma secreting PTH on its own: Ca²⁺ ↑, PO₄³⁻ ↓, PTH ↑ (or '
           'inappropriately normal) and urine Ca²⁺ ↑ — the high urine Ca²⁺ separates it from FHH. Most are found on a routine '
           'calcium; brown tumors and stones, bones, groans when advanced.',
  'dz:p2': 'Secondary hyperparathyroidism of chronic kidney disease: failing 1α-hydroxylase lowers calcitriol and phosphate '
           'is retained, so Ca²⁺ falls and all four glands hypertrophy — Ca²⁺ ↓, PO₄³⁻ ↑, PTH ↑, calcitriol ↓. Low Ca²⁺ with '
           'HIGH phosphate = kidney; with LOW phosphate = vitamin D.',
  'dz:p3': 'Tertiary hyperparathyroidism: after long stimulation in kidney disease a gland becomes autonomous — Ca²⁺ and PTH '
           'both high, PTH very high. Think of it in a long-term dialysis patient with high Ca²⁺; treated by parathyroidectomy.',
  'dz:vd': 'Vitamin D deficiency: less Ca²⁺ and PO₄³⁻ absorbed, so Ca²⁺ and PO₄³⁻ ↓ (FA: normal or ↓ — PTH ↑ props Ca²⁺ up) '
           'and alkaline phosphatase ↑ — '
           'rickets in children, osteomalacia in adults. Order 25-OH-D, the storage form, not calcitriol.',
  'dz:hp': 'Hypoparathyroidism: without PTH the kidney reabsorbs less Ca²⁺ and makes less calcitriol while phosphate is retained — '
           'Ca²⁺ ↓, PO₄³⁻ ↑, PTH ↓. Tetany, Chvostek and Trousseau signs, long QT; often after a thyroidectomy. Check Mg²⁺.',
  'dz:pha': 'Pseudohypoparathyroidism type 1A: the glands work, but a Gs-α defect leaves kidney and bone blind to PTH — '
            'Ca²⁺ ↓, PO₄³⁻ ↑ and calcitriol ↓ with PTH ↑, the giveaway. Albright hereditary osteodystrophy: short 4th and 5th metacarpals, '
            'short stature, round face; maternally inherited.',
  'dz:fhh': 'Familial hypocalciuric hypercalcemia: an inactivating Ca²⁺-sensing receptor mutation makes the glands and tubule '
            'read Ca²⁺ as low — mild Ca²⁺ ↑, PTH normal or slightly ↑, and LOW urine Ca²⁺ (unlike primary '
            'hyperparathyroidism). Observation only.',
  'dz:mal': 'Hypercalcemia of malignancy, PTHrP route — squamous cell carcinomas (lung, head and neck) and renal, bladder, '
            'breast and ovarian carcinoma make PTHrP, which acts on the PTH receptor: Ca²⁺ ↑, PO₄³⁻ ↓, PTH ↓; like PTH it raises '
            'urine Ca²⁺ and urine cAMP (Costanzo). Calcitriol, though, is low — measured levels are far below those of primary '
            'hyperparathyroidism (Stewart 1980); high calcitriol is the lymphoma route.',
  'dz:sarc': 'Sarcoidosis: granuloma macrophages carry 1α-hydroxylase and make calcitriol, so the gut absorbs more Ca²⁺ — '
             'Ca²⁺ ↑, calcitriol ↑ and urine Ca²⁺ ↑ while PTH is suppressed (Robbins). Other granulomatous diseases do the same '
             '(First Aid); glucocorticoids shrink the granulomas.',
  # ── m52 causes ──
  'dz:li': 'Lithium can cause hyperparathyroidism (Kaplan & Sadock), so it raises Ca²⁺ with PTH up — First Aid lists mild '
           'hypercalcemia beside its nephrogenic diabetes insipidus and thyroid effects. Check calcium before and during treatment.',
  'dz:vdx': 'Vitamin D excess: the gut absorbs more Ca²⁺ and phosphate, so Ca²⁺ and PO₄³⁻ rise with hypercalciuria, and the high '
            'Ca²⁺ suppresses PTH. Loss of appetite and stupor; glucocorticoids help by cutting vitamin D–driven gut Ca²⁺ transport (Katzung).',
  'dz:milk': 'Milk-alkali syndrome: a large intake of calcium with absorbable alkali — milk or calcium carbonate antacids — raises Ca²⁺ '
             'and suppresses PTH. The alkali load, held in by renal failure, adds a metabolic alkalosis (Costanzo).',
  'dz:thz': 'Thiazides block NCC in the distal convoluted tubule, which raises Ca²⁺ reabsorption there — serum Ca²⁺ ↑, urine Ca²⁺ ↓, '
            'PTH suppressed (Robbins). The same effect makes them a treatment for idiopathic hypercalciuria and calcium stones.',
  'dz:imm': 'Immobilization: bone that is not used is resorbed without any PTH push, so Ca²⁺ rises and the parathyroids are '
            'suppressed (Guyton; Robbins). Paget disease patients are at risk of immobilization hypercalcemia (Katzung).',
  'dz:lym': 'Lymphoma is the calcitriol route of hypercalcemia of malignancy: the tumor raises 1,25-(OH)₂ vitamin D, the gut absorbs '
            'more Ca²⁺ — Ca²⁺ ↑, calcitriol ↑, PTH ↓ (First Aid p. 224). Unlike the PTHrP tumors, calcitriol is high, as in sarcoidosis.',
  'dz:mm': 'Multiple myeloma and bone metastases (e.g., breast) raise Ca²⁺ straight from bone: tumor cytokines (IL-1, TNF-α, RANKL) '
           'switch on osteoclasts and punch lytic holes, and PTH is suppressed. Myeloma is CRAB — hyperCalcemia, Renal insufficiency, '
           'Anemia, Bone lytic lesions.',
  'dz:mg': 'Severe hypomagnesemia: Mg²⁺ is needed to release PTH and for tissues to respond to it, so Ca²⁺ falls while PTH stays low '
           '(a mild Mg²⁺ dip raises PTH instead). Causes include diarrhea, aminoglycosides, diuretics and alcohol use disorder; low K⁺ '
           'and torsades come with it — check Mg²⁺ in refractory hypocalcemia.',
  'dz:panc': 'Acute pancreatitis: lipase frees fatty acids from peripancreatic fat, and they bind calcium as soaps (fat necrosis, '
             'saponification) — hypocalcemia is a listed complication. Diagnosis needs 2 of 3: epigastric pain radiating to the back, '
             'lipase or amylase ≥ 3× normal, imaging.',
  'dz:tx': 'Massive transfusion: stored blood carries citrate, which chelates Ca²⁺, so large, fast volumes lower ionized Ca²⁺ — tetany, '
           'even convulsions. Old units also bring K⁺ from lysed red cells.',
  'dz:tls': 'Tumor lysis syndrome: when a bulky, fast tumor (often a lymphoma or leukemia) dies at once — usually after treatment '
            'starts — K⁺, PO₄³⁻ and uric acid flood the blood. Phosphate sequesters Ca²⁺, so Ca²⁺ falls; calcium phosphate and uric '
            'acid crystals injure the kidney.',
  'dz:rhab': 'Rhabdomyolysis: injured muscle releases phosphate (with K⁺ and myoglobin), and the phosphate precipitates Ca²⁺ — '
             'PO₄³⁻ ↑, Ca²⁺ ↓. Dark urine, very high CK, and myoglobin injuring the tubules (acute tubular necrosis).',
  'dz:loop': 'Loop diuretics block NKCC2 and abolish the lumen-positive potential that drives Ca²⁺ reabsorption in the thick ascending '
             'limb — Loops Lose Ca²⁺, so urine Ca²⁺ rises. Serum Ca²⁺ seldom falls much, because PTH and vitamin D raise reabsorption '
             'and absorption (Katzung); with saline, loops treat hypercalcemia.',
}

dyn = dict(
  kinds=dict(pth=['pth', '--dk9'], pthrp=['pth', '--bad'], ca=['ca', '--nf-ca'], po4=['po4', '--dk6'], vd=['vd', '--dk10']),
  groups=[['pth', 'PTH · PTHrP'], ['ca', 'Ca²⁺'], ['po4', 'PO₄³⁻'], ['vd', 'Calcitriol']],
  # m52: options in teaching order, grouped by serum Ca²⁺ and what PTH does — the 9 old keys unchanged
  switches=[dict(id='dz', label='Pick a cause', type='one',
                 options=[['p1', 'Primary hyperparathyroidism', 'hyperpara1'], ['p3', 'Tertiary', 'renalod'], ['li', 'Lithium', 'lithium'],
                          ['fhh', 'FHH', 'fhh'],
                          ['mal', 'Malignancy — PTHrP', 'hcmalig'], ['lym', 'Lymphoma — calcitriol', 'hcmalig'],
                          ['mm', 'Myeloma · bone metastases', 'myeloma'], ['sarc', 'Sarcoidosis · granulomas', 'sarcoid'],
                          ['vdx', 'Vitamin D excess', 'vitddef'], ['milk', 'Milk-alkali syndrome', 'mucosal'], ['thz', 'Thiazide', 'thiazides'],
                          ['imm', 'Immobilization'],
                          ['p2', 'Secondary (kidney disease)', 'hyperpara2'], ['vd', 'Vitamin D deficiency', 'vitddef'],
                          ['pha', 'Pseudohypoparathyroidism', 'pha'],
                          ['hp', 'Hypoparathyroidism', 'hypopara'], ['mg', 'Severe hypomagnesemia', 'mgpo4'],
                          ['panc', 'Acute pancreatitis', 'acutepanc'], ['tx', 'Massive transfusion', 'massivetx'],
                          ['tls', 'Tumor lysis syndrome', 'tls'], ['rhab', 'Rhabdomyolysis', 'rhabdo'],
                          ['loop', 'Loop diuretic', 'loopdiuretics']],
                 sections=[['high Ca²⁺ · PTH high or normal', ['p1', 'p3', 'li', 'fhh']],
                           ['high Ca²⁺ · PTH suppressed', ['mal', 'lym', 'mm', 'sarc', 'vdx', 'milk', 'thz', 'imm']],
                           ['low Ca²⁺ · PTH high', ['p2', 'vd', 'pha']],
                           ['low Ca²⁺ · PTH low', ['hp', 'mg']],
                           ['low Ca²⁺ · Ca²⁺ bound or precipitated', ['panc', 'tx', 'tls', 'rhab']],
                           ['serum Ca²⁺ holds · urine Ca²⁺ up', ['loop']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 68, 224, 336–349, 404–406, 434–440, 592, 609, 621–627, 695 · Costanzo ch 7, 9 · Guyton ch 80 · Katzung ch 15, 42 · '
      'Robbins ch 2, 20, 24 · Kaplan & Sadock ch 21 · Bootcamp · Stewart 1980')

MAP = dict(
  id='pthsim', title='Calcium & PTH Lab Simulator', topic='endo', after='hormones',
  sub='The parathyroids, their Ca²⁺ sensor, and PTH’s three targets — bone, kidney and (through calcitriol) gut. Pick a '
      'disorder or a cause — PTH, PTHrP and lymphoma, vitamin D, thiazides and loops, lithium, milk-alkali, magnesium, tumor lysis and '
      'more — to see what the glands and targets do and the lab pattern: Ca²⁺, PO₄³⁻, PTH, calcitriol, urine Ca²⁺, urine cAMP and ALP. '
      'Tap a receptor or transporter for its card',
  w=3500, h=2180,
  fa='68, 205, 224, 336–337, 348–349, 361, 404, 406, 434, 436, 440, 592, 609, 621–622, 626–627, 695',
  src=[CZ9, GY80, KZ42, RB24, RB20, CZ7, KZ15, RB2, KS21, BCE],
  lanes=[('ptGland', 'Parathyroid', 'glycolysis'), ('ptTarget', 'Bone, kidney & gut', 'gluconeo'), ('ptDz', 'Disorders', 'tca')],
  nodes=[
    ('pt1', 'PTH actions & control', 380, 1800, 'ptGland', 'raise Ca²⁺, trash PO₄³⁻', ['pthaction', 'casr']),
    ('pt2', 'Vitamin D', 820, 1800, 'ptTarget', 'skin → liver 25 → kidney 1α', ['calcitriol', 'vitddef']),
    ('pt3', 'PTH on the nephron', 1260, 1800, 'ptTarget', 'phosphaturic · hypocalciuric', ['pthneph', 'renalpo4']),
    ('pt4', 'Hyperparathyroidism', 1700, 1800, 'ptDz', 'primary · secondary · tertiary', ['hyperpara1', 'hyperpara2', 'renalod']),
    ('pt5', 'Low PTH or no response', 2140, 1800, 'ptDz', 'hypo · pseudohypo', ['hypopara', 'pha']),
    ('pt6', 'High Ca²⁺, low PTH', 380, 1940, 'ptDz', 'malignancy · granulomas', ['hcmalig', 'sarcoid', 'myeloma']),
    ('pt7', 'FHH', 820, 1940, 'ptDz', 'the sensor set too high', ['fhh']),
    ('pt8', 'Kidney disease', 1260, 1940, 'ptDz', 'phosphate retained', ['ckdphos', 'ckd']),
    ('pt9', 'Treatment', 1700, 1940, 'ptDz', 'bisphosphonates · cinacalcet', ['calciumdrugs']),
    # m52 — the cards the new causes open
    ('pt10', 'Drug causes', 2140, 1940, 'ptDz', 'thiazide · loop · lithium · antacid', ['thiazides', 'loopdiuretics', 'lithium', 'mucosal']),
    ('pt11', 'Ca²⁺ bound or Mg²⁺ low', 380, 2080, 'ptDz', 'soaps · citrate · magnesium', ['acutepanc', 'massivetx', 'mgpo4']),
    ('pt12', 'Cells breaking down', 820, 2080, 'ptDz', 'tumor lysis · rhabdomyolysis', ['tls', 'rhabdo'])],
  panels=[
    (2420, 1040, 1000, 'The lab patterns (First Aid pp. 348–349 · Costanzo ch 9)', [
      ('Primary hyperparathyroidism', 'Ca²⁺ ↑ · PO₄³⁻ ↓ · PTH ↑ · urine Ca²⁺ ↑'),
      ('Secondary (CKD)', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↑ · calcitriol ↓'),
      ('Tertiary', 'Ca²⁺ ↑ · PTH ↑↑'),
      ('Vitamin D deficiency', 'Ca²⁺, PO₄³⁻ normal or ↓ · PTH ↑ · ALP ↑'),
      ('Hypoparathyroidism', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↓'),
      ('Pseudohypoparathyroidism', 'Ca²⁺ ↓ · PO₄³⁻ ↑ · PTH ↑'),
      ('FHH', 'Ca²⁺ ↑ · PTH normal or slightly ↑ · urine Ca²⁺ ↓'),
      ('Malignancy (PTHrP)', 'Ca²⁺ ↑ · PO₄³⁻ ↓ · PTH ↓ · calcitriol ↓ (Stewart 1980)')]),
    (2420, 1330, 1000, 'Telling them apart (First Aid pp. 224, 336, 348–349, 627 · Robbins ch 24)', [
      ('Low Ca²⁺, high PO₄³⁻', 'kidney disease, hypoparathyroidism or pseudohypoparathyroidism'),
      ('Low Ca²⁺, low PO₄³⁻', 'vitamin D deficiency'),
      ('Low Ca²⁺, PTH low', 'hypoparathyroidism · severe hypomagnesemia'),
      ('High Ca²⁺, urine Ca²⁺ high', 'primary hyperparathyroidism'),
      ('High Ca²⁺, urine Ca²⁺ low', 'FHH · thiazides'),
      ('High Ca²⁺, PTH low', 'malignancy · granulomas · vitamin D excess · thiazides · immobilization'),
      ('High Ca²⁺, calcitriol high', 'sarcoidosis and other granulomas · lymphoma')])],
  dyn=dyn)
