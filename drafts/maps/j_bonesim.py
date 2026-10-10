# Bones & Kids by Age in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A long bone (epiphysis, growth plate, metaphysis, diaphysis; cortex and medulla), a child's hip and a forearm. An `age`
# switch (steps, auto) runs newborn → under 5 → 5–7 → adolescent → young adult → older adult and lights what the cards tie
# to that age; a `one` switch picks a tumor or a condition and lights where it sits with its x-ray sign: osteosarcoma, Ewing,
# giant cell tumor, osteochondroma, osteoid osteoma, chondrosarcoma, enchondroma, DDH, Legg-Calvé-Perthes, SCFE,
# Osgood-Schlatter, nursemaid's elbow, greenstick, torus and bowing fractures. 3 readouts. Facts from the pinned cards; FA
# pages in `fa`. No new cards.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

# ── drawing helpers ──
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

D = lambda *k: [f'dx:{x}' for x in k]
A = lambda *k: [f'age:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def ring(x, y, rx, ry, when): add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" style="fill:var(--bad);fill-opacity:.18;stroke:var(--bad);stroke-width:5"/>', when=when)
# UNVERIFIED: Ewing (card: 'boy') and osteochondroma (card: 'young male') are placed in the adolescent band; the cards give no age range
AGE = dict(new=['ddh'], u5=['nurse', 'green', 'torus', 'bow'], s57=['lcp'], ado=['osteo', 'ewing', 'ochon', 'scfe', 'osgood'],
           ya=['gct', 'ench'], old=['chondro'])
def lit(*k): return D(*k) + [f'age:{a}' for a, ks in AGE.items() if any(x in ks for x in k)]

text('Bones and kids — where it sits, and at what age', 180, 150, 'dyn-big')
text('a red ring = where the card places it · the age switch lights everything the cards tie to that age', 180, 176, 'dyn-cap')

# ════════ long bone (around the knee: distal femur) ════════
BX = 700
add(f'<path d="M{BX - 70} 260 V860 C{BX - 70} 960 {BX - 200} 980 {BX - 200} 1080 C{BX - 200} 1220 {BX + 200} 1220 {BX + 200} 1080 '
    f'C{BX + 200} 980 {BX + 70} 960 {BX + 70} 860 V260 Z" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:6"/>')
add(f'<path d="M{BX - 40} 260 V860 M{BX + 40} 260 V860" style="stroke:var(--dk10);stroke-width:2;stroke-dasharray:8 8"/>')
add(f'<path d="M{BX - 190} 1060 H{BX + 190}" style="stroke:var(--dk7);stroke-width:8"/>', unless=A('ya', 'old'))
add(f'<path d="M{BX - 190} 1060 H{BX + 190}" style="stroke:var(--ink-3);stroke-width:3;stroke-dasharray:6 6"/>', when=A('ya', 'old'))
for y, lab in ((500, 'diaphysis'), (940, 'metaphysis'), (1060, 'growth plate (physis)'), (1150, 'epiphysis')):
    text(lab, BX + 240, y + 6, 'nf-l2')
text('medulla', BX, 600, 'nf-l2', 'middle'); text('cortex', BX - 110, 380, 'nf-l2', 'end')
text('distal femur · knee', BX, 1270, 'nf-l1', 'middle')
ring(BX, 940, 150, 70, lit('osteo'))
ring(BX, 500, 90, 160, lit('ewing'))
ring(BX, 1150, 170, 60, lit('gct'))
add(f'<path d="M{BX + 120} 960 L{BX + 260} 880 L{BX + 280} 900 L{BX + 150} 990 Z" style="fill:var(--dk10);fill-opacity:.4;stroke:var(--bad);stroke-width:5"/>', when=lit('ochon'))
ring(BX - 70, 400, 30, 30, D('ooid'))
SIGN = dict(osteo='metaphysis near the knee · Codman triangle, sunburst', ewing='diaphysis · onion-skin · small round blue cells t(11;22)',
            gct='epiphysis after plates close · soap-bubble lytic lesion', ochon='metaphyseal stalk with a cartilage cap pointing away from the joint',
            ooid='small cortical nidus — night pain relieved by NSAIDs', chondro='pelvis, proximal femur, humerus medulla · ring-and-arc calcification',
            ench='medulla of hand and foot bones · commonest tumor of the hand')
for k, t in SIGN.items(): text(t, 1300, 1420, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ hip ════════
HX, HY = 1500, 560
add(f'<path d="M{HX - 200} 300 C{HX - 60} 340 {HX + 60} 420 {HX + 40} 520" style="fill:none;stroke:var(--dk10);stroke-width:30;opacity:.4"/>')
text('acetabulum', HX - 220, 300, 'nf-l2', 'end')
add(f'<circle cx="{HX}" cy="{HY}" r="90" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--dk10);stroke-width:5"/>', unless=D('lcp', 'scfe', 'ddh'))
add(f'<path d="M{HX - 90} {HY + 10} C{HX - 90} {HY - 60} {HX + 90} {HY - 60} {HX + 90} {HY + 10} Z" style="fill:var(--ink-3);fill-opacity:.5;stroke:var(--bad);stroke-width:5"/>', when=D('lcp'))
add(f'<circle cx="{HX - 20}" cy="{HY + 40}" r="90" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--bad);stroke-width:5"/>', when=D('scfe'))
add(f'<circle cx="{HX + 130}" cy="{HY + 110}" r="90" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--bad);stroke-width:5"/>', when=D('ddh'))
add(f'<path d="M{HX + 50} {HY + 60} L{HX + 260} {HY + 420} L{HX + 360} {HY + 380} L{HX + 120} {HY + 20}" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:5"/>')
text('femoral head · neck', HX + 260, HY - 30, 'nf-l2')
HIP = dict(ddh='newborn: acetabulum underdeveloped — Ortolani/Barlow clunk; ultrasound',
           lcp='5–7, boys: avascular femoral head flattens and fragments; first x-ray often normal',
           scfe='obese young adolescent: epiphysis slips off the neck — hip or knee pain')
for k, t in HIP.items(): text(t, 1300, 1420, 'nf-l1 dyn-tag', 'middle', when=D(k))
ring(HX, HY, 140, 140, A('new', 's57') + ['age:ado&dx:scfe'])

# ════════ knee tuberosity, elbow, forearm ════════
add('<rect x="1950" y="260" width="380" height="300" rx="30" class="dyn-soft"/>'); text('Tibial tuberosity', 2140, 300, 'nf-l1', 'middle')
ring(2140, 430, 80, 60, lit('osgood'))
text('repetitive avulsion after a growth spurt', 2140, 520, 'nf-l2', 'middle', when=lit('osgood'))
add('<rect x="1950" y="620" width="380" height="300" rx="30" class="dyn-soft"/>'); text('Elbow', 2140, 660, 'nf-l1', 'middle')
ring(2140, 790, 80, 60, lit('nurse'))
text('annular ligament slips over the radial head', 2140, 880, 'nf-l2', 'middle', when=lit('nurse'))
add('<rect x="1300" y="1000" width="1030" height="300" rx="30" class="dyn-soft"/>'); text('Child’s forearm', 1330, 1040, 'nf-l1')
add('<path d="M1360 1160 H2280" style="stroke:var(--dk10);stroke-width:40;opacity:.35;stroke-linecap:round"/>', unless=D('green', 'torus', 'bow'))
add('<path d="M1360 1180 Q1820 1080 2280 1180" style="fill:none;stroke:var(--dk10);stroke-width:40;opacity:.35;stroke-linecap:round"/>', when=D('bow', 'green'))
add('<path d="M1820 1110 l-10 30 l20 10" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('green'))
add('<path d="M1360 1160 H2280" style="stroke:var(--dk10);stroke-width:40;opacity:.35;stroke-linecap:round"/><path d="M2160 1130 q15 30 0 60" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('torus'))
FX = dict(bow='bowing: bends, cortex intact — ulna or fibula', green='greenstick: bending — fails on the tension (convex) side only',
          torus='torus (buckle): axial force — cortex buckles on the compression side, distal radius')
for k, t in FX.items(): text(t, 1820, 1270, 'nf-l1 dyn-tag', 'middle', when=D(k))
AGES = dict(new='newborn: DDH', u5='under 5: nursemaid’s elbow; immature bone bends and buckles', s57='5–7: Legg-Calvé-Perthes',
            ado='adolescent: osteosarcoma, Ewing, osteochondroma, SCFE, Osgood-Schlatter', ya='young adult (plates closed): giant cell tumor; 20–50 enchondroma',
            old='older adult: chondrosarcoma; osteosarcoma secondary to Paget, radiation')
for k, t in AGES.items(): text(t, 1300, 1460, 'nf-l2', 'middle', when=A(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{BX - 260} 400 C{BX - 200} 700 {BX - 150} 900 {BX - 60} 1000', len=640, speed=110, r=8, base=dict(bl=2)),
  dict(d=f'M{HX + 200} {HY + 300} C{HX + 120} {HY + 160} {HX + 60} {HY + 80} {HX} {HY}', len=360, speed=90, r=8, base=dict(bl=3), mods=[m(D('lcp'), set=dict(bl=0))]),
  dict(d=f'M{HX} {HY} L{HX - 20} {HY + 40}', len=45, speed=15, r=12, base=dict(f=1), when=D('scfe')),
  dict(d=f'M{HX + 40} {HY + 20} L{HX + 130} {HY + 110}', len=130, speed=40, r=12, base=dict(f=1), when=D('ddh')),
  dict(d='M1820 1000 V1110', len=110, speed=50, r=10, base=dict(f=2), when=D('bow', 'green')),
  dict(d='M2330 1160 H2190', len=140, speed=50, r=10, base=dict(f=2), when=D('torus')),
  dict(d='M2300 790 H2200', len=100, speed=30, r=10, base=dict(f=1), when=D('nurse')),
]
sites = [dict(x=BX, y=940, n=[0, 1], w=10, t='rec', l='', aria='Osteosarcoma', c='osteosarcoma', ions=[]),
         dict(x=BX, y=500, n=[1, 0], w=10, t='rec', l='', aria='Ewing sarcoma', c='ewing', ions=[]),
         dict(x=HX, y=HY - 100, n=[0, -1], w=10, t='rec', l='', aria='Legg-Calvé-Perthes', c='lcp', ions=[]),
         dict(x=1360, y=1160, n=[-1, 0], w=10, t='rec', l='', aria='Greenstick and torus fractures', c='pedsfx', ions=[])]

readouts = [
  dict(l='Malignant', mods=[dict(when=D('osteo', 'ewing', 'chondro'), d=1), dict(when=D('gct', 'ochon', 'ooid', 'ench'), d=-1)]),
  dict(l='Growth plate open', mods=[dict(when=A('new', 'u5', 's57', 'ado'), d=1), dict(when=A('ya', 'old'), d=-1)]),
  dict(l='Femoral head blood flow', mods=[dict(when=D('lcp'), d=-1)]),
]

notes = {
  '': 'Location on a long bone and age narrow the list: metaphysis (osteosarcoma, osteochondroma), diaphysis (Ewing), epiphysis after '
      'the plates close (giant cell tumor). Children’s bone is flexible — it bends and buckles instead of snapping.',
  'dx:osteo': 'Osteosarcoma: malignant osteoblasts making osteoid in the metaphysis near the knee — teenager; Codman triangle, sunburst; '
              'RB1, Li-Fraumeni, Paget. Surgery and chemotherapy.',
  'dx:ewing': 'Ewing sarcoma: small round blue cells, t(11;22) EWS-FLI1, diaphysis of long bones and pelvis — a boy with pain, swelling, '
              'fever (mimics osteomyelitis); onion-skin periosteum. Responds to chemotherapy.',
  'dx:gct': 'Giant cell tumor: locally aggressive benign, in the epiphysis after the plates close, around the knee — soap bubble; stromal '
            'cells express RANKL. Curettage, denosumab.',
  'dx:ochon': 'Osteochondroma: the most common benign bone tumor — a metaphyseal stalk continuous with the marrow, cartilage cap pointing '
              'away from the joint; rarely becomes chondrosarcoma.',
  'dx:ooid': 'Osteoid osteoma: a small cortical nidus making prostaglandins — night pain relieved by NSAIDs.',
  'dx:chondro': 'Chondrosarcoma: malignant cartilage in the medulla of the pelvis, proximal femur and humerus of older adults — ring-and-arc '
                'calcification.',
  'dx:ench': 'Enchondroma: benign hyaline cartilage in the medulla of the small hand and foot bones, ages 20–50; IDH1/2. Ollier, Maffucci.',
  'dx:ddh': 'Developmental dysplasia of the hip: the acetabulum develops abnormally — Ortolani and Barlow clunk; ultrasound (x-ray not '
            'useful until 4–6 months).',
  'dx:lcp': 'Legg-Calvé-Perthes: idiopathic avascular necrosis of the femoral head at 5–7, boys 4:1; creeping substitution, collapse and '
            'flattening, then remodeling.',
  'dx:scfe': 'Slipped capital femoral epiphysis: axial force slips the epiphysis off the neck — obese young adolescent with hip or knee pain.',
  'dx:osgood': 'Osgood-Schlatter: repetitive avulsion of the tibial tuberosity ossification center after a growth spurt — running, jumping.',
  'dx:nurse': 'Radial head subluxation: a sudden pull slips the immature annular ligament over the radial head — under 5, arm flexed and pronated.',
  'dx:green': 'Greenstick: bending stress breaks only the tension side.', 'dx:torus': 'Torus (buckle): axial force buckles the compression side.',
  'dx:bow': 'Bowing fracture: the bone bends without breaking the cortex — ulna or fibula. Splint or cast.',
}

dyn = dict(
  kinds=dict(bl=['flow', '--nf-blood'], f=['flow', '--bad']), groups=[['flow', 'Blood supply · force']],
  switches=[dict(id='age', label='Age', type='steps', auto=4, options=[['new', 'Newborn'], ['u5', 'Under 5'], ['s57', '5–7'],
                                                                        ['ado', 'Adolescent'], ['ya', 'Young adult'], ['old', 'Older adult']]),
            dict(id='dx', label='Tumor or condition', type='one', options=[
              ['osteo', 'Osteosarcoma', 'osteosarcoma'], ['ewing', 'Ewing sarcoma', 'ewing'], ['gct', 'Giant cell tumor', 'gct'],
              ['ochon', 'Osteochondroma', 'osteochondroma'], ['ooid', 'Osteoid osteoma', 'osteoidosteoma'], ['chondro', 'Chondrosarcoma', 'chondrosarcoma'],
              ['ench', 'Enchondroma', 'enchondroma'], ['ddh', 'DDH', 'ddh'], ['lcp', 'Legg-Calvé-Perthes', 'lcp'], ['scfe', 'SCFE', 'scfe'],
              ['osgood', 'Osgood-Schlatter', 'osgood'], ['nurse', 'Nursemaid’s elbow', 'nursemaid'], ['green', 'Greenstick fracture', 'pedsfx'],
              ['torus', 'Torus fracture', 'pedsfx'], ['bow', 'Bowing fracture', 'bowingfx']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 466–467, 470–471 · Robbins ch 26')

MAP = dict(
  id='bonesim', title='Bones & Kids by Age in Motion', topic='msk', after='bone',
  sub='Run the ages from newborn to older adult and see what lights up — then place each bone tumor on the long bone (metaphysis, '
      'diaphysis, epiphysis) and watch the child’s hip, elbow and forearm: DDH, Perthes, SCFE, Osgood-Schlatter, nursemaid’s elbow, '
      'greenstick, torus and bowing fractures',
  w=3600, h=1900,
  fa='466, 467, 470, 471',
  src=['Robbins ch 26 — Bones, joints, and soft tissue tumors', 'Bootcamp.com MSK — Primary bone tumors', 'Moore ch 7 — Lower Limb',
       'Langman ch 12 — Limbs', 'OCOM Ortho — SDL 9 reading: Pediatric orthopedic surgery (Current Diagnosis & Treatment in Orthopedics 6e ch 12)',
       'Moore ch 3 — Upper Limb', 'Moore ch 1 — Overview and Basic Concepts',
       'OCOM Ortho — SDL 9 reading: Fracture management (Practical Office Orthopedics ch 8)', 'Bootcamp.com MSK — Childhood musculoskeletal pathology'],
  lanes=[('boTum', 'Bone tumors', 'glycolysis'), ('boHip', 'Pediatric hip & knee', 'tca'), ('boFx', 'Pediatric fractures', 'gluconeo')],
  nodes=[
    ('bo1', 'Osteosarcoma', 330, 1660, 'boTum', 'metaphysis · knee', ['osteosarcoma'], 'hub'),
    ('bo2', 'Ewing sarcoma', 760, 1660, 'boTum', 'diaphysis · t(11;22)', ['ewing']),
    ('bo3', 'Giant cell · osteochondroma', 1200, 1660, 'boTum', 'epiphysis · stalk', ['gct', 'osteochondroma']),
    ('bo4', 'Osteoid osteoma', 1640, 1660, 'boTum', 'NSAID-relieved', ['osteoidosteoma']),
    ('bo5', 'Chondrosarcoma · enchondroma', 2080, 1660, 'boTum', 'cartilage', ['chondrosarcoma', 'enchondroma']),
    ('bo6', 'DDH · Perthes · SCFE', 330, 1790, 'boHip', 'by age', ['ddh', 'lcp', 'scfe']),
    ('bo7', 'Osgood-Schlatter', 760, 1790, 'boHip', 'tibial tuberosity', ['osgood']),
    ('bo8', 'Nursemaid’s elbow', 1200, 1790, 'boFx', 'under 5', ['nursemaid']),
    ('bo9', 'Greenstick · torus · bowing', 1640, 1790, 'boFx', 'bends, buckles', ['pedsfx', 'bowingfx'])],
  panels=[
    (2500, PANY, 1000, 'Location on the long bone (First Aid p. 470)', [
      ('Epiphysis', 'giant cell tumor (plates closed)'), ('Metaphysis', 'osteosarcoma, osteochondroma'),
      ('Diaphysis', 'Ewing sarcoma'), ('Medulla, hands and feet', 'enchondroma')])],
  dyn=dyn)
