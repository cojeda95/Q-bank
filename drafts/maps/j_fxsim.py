# Growth Plates & Arm Injuries in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Left: the end of a child's long bone — epiphysis, physis, metaphysis — with a `sh` switch drawing Salter-Harris types I–V
# where each card line says the fracture runs. Right: a front view of the left upper limb with the nerves that lie on the
# bone (axillary at the surgical neck, radial in the groove, median at the distal humerus, ulnar at the medial epicondyle);
# an `inj` switch breaks or dislocates it — clavicle (SCM lifts the medial fragment, the arm's weight drops the shoulder),
# anterior shoulder dislocation, supracondylar fracture, posterior elbow dislocation, medial epicondyle avulsion, Colles,
# Monteggia, Galeazzi, Little League shoulder — and lights the nerve the card puts at risk. 3 readouts. Facts from the
# pinned cards; FA pages in `fa`. No new cards.
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

S = lambda *k: [f'sh:{x}' for x in k]
I = lambda *k: [f'inj:{x}' for x in k]
PANY = 1180

text('Growth plates & arm injuries — where the line runs, and which nerve is next to it', 180, 150, 'dyn-big')
text('left: Salter-Harris on a child’s bone end · right: front view of the left arm, lateral to your right', 180, 176, 'dyn-cap')

# ════════ Salter-Harris ════════
add('<path d="M450 440 C450 300 750 300 750 440 Z" style="fill:var(--dk6);fill-opacity:.15;stroke:var(--dk6);stroke-width:4"/>'); text('epiphysis', 780, 380, 'nf-l2')
add('<rect x="450" y="440" width="300" height="24" style="fill:var(--dk9);fill-opacity:.35"/>'); text('physis (growth plate)', 780, 458, 'nf-l2')
add('<path d="M450 464 L470 700 L730 700 L750 464 Z" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>'); text('metaphysis', 780, 580, 'nf-l2')
add('<path d="M470 700 V1000 M730 700 V1000" style="stroke:var(--dk6);stroke-width:4"/>'); text('diaphysis', 780, 860, 'nf-l2')
text('joint surface', 600, 290, 'nf-l2', 'middle')
SH = {'1': 'M450 452 H750', '2': 'M450 452 H620 L740 640', '3': 'M750 452 H620 L600 318', '4': 'M590 318 L640 660'}
for k, d in SH.items():
    add(f'<path d="{d}" style="fill:none;stroke:var(--bad);stroke-width:8;stroke-linejoin:round"/>', when=S(k))
add('<rect x="450" y="446" width="300" height="12" style="fill:var(--bad);opacity:.8"/>', when=S('5'))
add('<path d="M600 250 V330 M560 270 L600 330 L640 270" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=S('5'))
SHT = {'1': 'I — straight through the plate: epiphysis separates', '2': 'II — plate, then out the metaphysis (Thurston-Holland) — commonest, ~74%',
       '3': 'III — plate, then out the epiphysis — into the joint: arthritis + growth arrest', '4': 'IV — across epiphysis, plate and metaphysis — bony bar if malreduced',
       '5': 'V — crush of the plate'}
for k, s in SHT.items(): text(s, 600, 1060, 'nf-l1 dyn-tag', 'middle', when=S(k))
text('any type can arrest growth — displacement and reduction matter more than the type', 600, 1100, 'nf-l2', 'middle', when=['sh:*'])

# ════════ arm ════════
AX = 1760
add('<path d="M1300 400 C1450 370 1600 380 1700 400" style="fill:none;stroke:var(--dk6);stroke-width:26;opacity:.4;stroke-linecap:round"/>', unless=I('clav'))
add('<path d="M1300 400 C1400 380 1460 360 1500 340" style="fill:none;stroke:var(--dk6);stroke-width:26;opacity:.5;stroke-linecap:round"/>', when=I('clav'))
add('<path d="M1530 420 C1600 430 1660 450 1700 470" style="fill:none;stroke:var(--dk6);stroke-width:26;opacity:.5;stroke-linecap:round"/>', when=I('clav'))
text('clavicle', 1360, 360, 'nf-l2')
add('<path d="M1690 420 C1660 470 1660 520 1690 560" style="fill:none;stroke:var(--dk6);stroke-width:10"/>'); text('glenoid', 1640, 500, 'nf-l2', 'end')
HEAD = '<circle cx="{x}" cy="{y}" r="58" style="fill:var(--dk6);fill-opacity:.2;stroke:var(--dk6);stroke-width:4"/>'
add(HEAD.format(x=AX - 10, y=490), unless=I('antdis'))
add(HEAD.format(x=AX - 80, y=580).replace('--dk6);stroke-width', '--bad);stroke-width'), when=I('antdis'))
add(f'<path d="M{AX} 540 V880" style="stroke:var(--dk6);stroke-width:46;opacity:.25;stroke-linecap:round"/>'); text('humerus', AX + 50, 700, 'nf-l2')
add(f'<path d="M{AX - 40} 900 H{AX + 40}" style="stroke:var(--dk6);stroke-width:30;opacity:.3;stroke-linecap:round"/>')
add(f'<circle cx="{AX - 62}" cy="900" r="16" style="fill:var(--dk6);fill-opacity:.4"/>', unless=I('medepi')); text('medial epicondyle', AX - 90, 890, 'nf-l2', 'end')
add(f'<circle cx="{AX - 100}" cy="950" r="16" style="fill:var(--bad);fill-opacity:.6"/>', when=I('medepi'))
OFF = I('postdis')
def fore(dx, when=None, unless=None):
    add(f'<path d="M{AX - 22 + dx} 930 L{AX - 26 + dx} 1300" style="stroke:var(--dk6);stroke-width:20;opacity:.3;stroke-linecap:round"/>', when=when, unless=unless)
    add(f'<path d="M{AX + 26 + dx} 930 L{AX + 34 + dx} 1300" style="stroke:var(--dk6);stroke-width:24;opacity:.3;stroke-linecap:round"/>', when=when, unless=unless)
fore(0, unless=OFF); fore(60, when=OFF)
text('ulna', AX - 90, 1150, 'nf-l2', 'end'); text('radius', AX + 70, 1150, 'nf-l2')
# fracture marks
def brk(x, y, when): add(f'<path d="M{x - 30} {y - 10} L{x + 30} {y + 10}" style="stroke:var(--bad);stroke-width:8"/>', when=when)
brk(1515, 380, I('clav')); brk(AX, 840, I('supra')); brk(AX + 32, 1270, I('colles')); brk(AX - 24, 1100, I('monteggia')); brk(AX + 30, 1100, I('galeazzi'))
add(f'<circle cx="{AX + 40}" cy="920" r="22" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=I('monteggia'))
add(f'<circle cx="{AX}" cy="1300" r="26" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=I('galeazzi'))
add(f'<path d="M{AX - 30} 520 H{AX + 30}" style="stroke:var(--bad);stroke-width:10"/>', when=I('ll'))
# nerves
NV = dict(ax=(AX + 40, 560, 'axillary'), rad=(AX + 34, 720, 'radial'), med=(AX + 10, 860, 'median'), uln=(AX - 70, 930, 'ulnar'))
for k, (x, y, l) in NV.items():
    add(f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--dk7);opacity:.7"/>'); text(l, x + (20 if k != 'uln' else -20), y + 30, 'nf-l2', None if k != 'uln' else 'end')
RISK = dict(ax=I('antdis'), med=I('supra'), uln=I('postdis', 'medepi'))
for k, w in RISK.items():
    x, y, _ = NV[k]; add(f'<circle cx="{x}" cy="{y}" r="26" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=w)
IT = dict(clav='clavicle — middle third; SCM lifts the medial piece, the arm’s weight drops the shoulder',
          antdis='anterior dislocation — head goes subcoracoid · Bankart, Hill-Sachs · axillary nerve: flat deltoid, numb patch',
          supra='supracondylar — distal fragment pulled over; median nerve or brachial vessels',
          postdis='posterior elbow dislocation — UCL tears; ulnar nerve', medepi='medial epicondyle avulsion (child) — ulnar nerve traction',
          colles='Colles — distal radius tilts dorsally: dinner fork · over 50, osteoporosis', monteggia='Monteggia — ulna fracture + radial head dislocation (missed in kids)',
          galeazzi='Galeazzi — radial shaft fracture + DRUJ disruption — needs ORIF', ll='Little League shoulder — stress injury of the proximal humeral physis in pitchers')
for k, s in IT.items(): text(s, 1700, 1420, 'nf-l1 dyn-tag', 'middle', when=I(k))

# ════════ motion ════════
flows = [
  dict(d='M1460 330 C1440 300 1420 280 1400 250', len=100, speed=50, r=9, base=dict(pull=2), when=I('clav')),
  dict(d='M1640 460 C1650 500 1660 540 1670 580', len=130, speed=50, r=9, base=dict(pull=2), when=I('clav')),
  dict(d=f'M{AX - 10} 490 C{AX - 40} 520 {AX - 60} 550 {AX - 80} 580', len=110, speed=50, r=9, base=dict(pull=2), when=I('antdis')),
  dict(d=f'M{AX + 32} 1270 C{AX + 50} 1250 {AX + 70} 1240 {AX + 90} 1235', len=70, speed=40, r=9, base=dict(pull=2), when=I('colles')),
]
sites = [dict(x=420, y=450, n=[-1, 0], w=10, t='rec', l='', aria='Salter-Harris', c='salterharris', ions=[]),
         dict(x=1300, y=440, n=[-1, 1], w=10, t='rec', l='', aria='Clavicle fracture', c='clavfx', ions=[]),
         dict(x=1640, y=620, n=[-1, 0], w=10, t='rec', l='', aria='Shoulder dislocation', c='shoulderdisloc', ions=[]),
         dict(x=AX + 90, y=900, n=[1, 0], w=10, t='rec', l='', aria='Elbow injuries', c='elbowinj', ions=[]),
         dict(x=AX + 110, y=1300, n=[1, 0], w=10, t='rec', l='', aria='Forearm fractures', c='forearmfx', ions=[]),
         dict(x=AX + 80, y=500, n=[1, -1], w=10, t='rec', l='', aria='Little League shoulder', c='littleleague', ions=[])]

readouts = [
  dict(l='Growth plate involved', mods=[dict(when=['sh:*'] + I('ll'), d=1)]),
  dict(l='Joint surface involved', mods=[dict(when=S('3'), d=1)]),
  dict(l='Nerve at risk', mods=[dict(when=I('antdis', 'supra', 'postdis', 'medepi'), d=1)]),
]

notes = {
  '': 'In children the physis is weaker than the bone and ligaments, so it breaks first. In the arm, each bony landmark carries a '
      'nerve — surgical neck: axillary · radial groove: radial · distal humerus: median · medial epicondyle: ulnar.',
  'sh:1': 'Salter-Harris I: straight through the physis — the epiphysis separates from the metaphysis.',
  'sh:2': 'Salter-Harris II: along the physis then out through the metaphysis (Thurston-Holland fragment) — commonest, ~74%.',
  'sh:3': 'Salter-Harris III: along the physis then out through the epiphysis — intra-articular: arthritis as well as growth arrest.',
  'sh:4': 'Salter-Harris IV: across epiphysis, physis and metaphysis; malreduced → transphyseal bony bar.',
  'sh:5': 'Salter-Harris V: compression crush of the physis.',
  'inj:clav': 'Clavicle: often broken (children, birth trauma, falls on the outstretched hand); weakest at the middle–lateral third '
              'junction. SCM lifts the medial fragment; the shoulder drops and the lateral fragment rotates in.',
  'inj:antdis': 'Anterior shoulder dislocation: young athletes — extension and lateral rotation drive the head inferoanteriorly to '
                'a subcoracoid spot. Bankart, Hill-Sachs; axillary nerve (flattened deltoid, numb deltoid skin).',
  'inj:supra': 'Supracondylar humerus fracture (children): the distal fragment is pulled over the proximal; median nerve or '
               'brachial vessels at risk.',
  'inj:postdis': 'Posterior elbow dislocation: fall on the hand with the elbow flexed, or hyperextension; UCL tears, radial head, '
                 'coronoid or olecranon fractures; ulnar nerve.',
  'inj:medepi': 'Medial epicondyle avulsion in children: the UCL pulls the epicondyle off before it fuses — ulnar nerve traction.',
  'inj:colles': 'Colles: distal 2 cm of the radius, over 50, osteoporosis, fall on the outstretched pronated hand — dorsal tilt, '
                'dinner fork, radial shortening; usually unites well.',
  'inj:monteggia': 'Monteggia: ulna fracture with radial head dislocation — often missed in children.',
  'inj:galeazzi': 'Galeazzi: radial shaft fracture with distal radioulnar joint disruption — unstable, ORIF.',
  'inj:ll': 'Little League shoulder: proximal humeral epiphysiolysis in pitchers — rest; pitch-count limits.',
}

dyn = dict(
  kinds=dict(pull=['mov', '--bad']), groups=[['mov', 'Displacement']],
  switches=[dict(id='sh', label='Salter-Harris', type='one', options=[
              ['1', 'Type I', 'salterharris'], ['2', 'Type II', 'salterharris'], ['3', 'Type III', 'salterharris'],
              ['4', 'Type IV', 'salterharris'], ['5', 'Type V', 'salterharris']]),
            dict(id='inj', label='Arm injury', type='one', options=[
              ['clav', 'Clavicle fracture', 'clavfx'], ['antdis', 'Anterior shoulder dislocation', 'shoulderdisloc'],
              ['supra', 'Supracondylar fracture', 'elbowinj'], ['postdis', 'Posterior elbow dislocation', 'elbowinj'],
              ['medepi', 'Medial epicondyle avulsion', 'elbowinj'], ['colles', 'Colles', 'forearmfx'],
              ['monteggia', 'Monteggia', 'forearmfx'], ['galeazzi', 'Galeazzi', 'forearmfx'], ['ll', 'Little League shoulder', 'littleleague']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Moore ch 3')

MAP = dict(
  id='fxsim', title='Growth Plates & Arm Injuries in Motion', topic='msk', after='sportsortho',
  sub='Draw Salter-Harris I–V through a child’s growth plate, then break and dislocate the arm — clavicle, shoulder, elbow, Colles, '
      'Monteggia, Galeazzi — and see which nerve sits next to each',
  w=3600, h=1900,
  fa='450, 463, 467',
  src=['Moore ch 3 — Upper Limb', 'Pawlina ch 8 — Bone'],
  lanes=[('fxPed', 'Growth plate', 'tca'), ('fxArm', 'Upper limb', 'glycolysis')],
  nodes=[
    ('fx1', 'Salter-Harris fractures', 330, 1700, 'fxPed', 'types I–V', ['salterharris'], 'hub'),
    ('fx2', 'Little League shoulder', 760, 1700, 'fxPed', 'proximal humeral physis', ['littleleague']),
    ('fx3', 'Clavicle fracture', 1200, 1700, 'fxArm', 'middle third', ['clavfx']),
    ('fx4', 'Shoulder dislocation', 1640, 1700, 'fxArm', 'anterior · axillary n.', ['shoulderdisloc']),
    ('fx5', 'Elbow fractures', 2080, 1700, 'fxArm', 'median · ulnar', ['elbowinj']),
    ('fx6', 'Forearm & wrist fractures', 2520, 1700, 'fxArm', 'Colles · Monteggia', ['forearmfx'])],
  panels=[
    (2500, PANY, 1000, 'Bone → nerve (Moore ch 3)', [
      ('Surgical neck', 'axillary'), ('Radial groove', 'radial'), ('Distal humerus', 'median'), ('Medial epicondyle', 'ulnar')])],
  dyn=dyn)
