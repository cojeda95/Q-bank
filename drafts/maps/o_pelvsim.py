# Pelvis in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A schematic pelvis from the front (ASIS, pubic tubercles) and from behind (PSIS, with the examiner's thumbs), a dysfunction
# on the patient's LEFT. A `steps` switch (auto) runs the flexion test — upright, then bending forward — and the thumb on the
# restricted side rides farther up; a `test` switch picks standing or seated. A `one` switch shows anterior and posterior
# innominate rotation, upslip and downslip, inflare and outflare, superior and inferior pubic shear, and a sacral
# (sacroiliac) dysfunction; the landmarks move as the cards say. 3 readouts. Facts from the pinned cards (Foundations of
# Osteopathic Medicine ch 31, 37–38, OCOM OMM); no First Aid pages. No new cards.
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
PANY = 1180
IS = D('ant', 'post', 'up', 'down', 'in', 'out', 'psup', 'pinf')      # iliosacral / pubic — the standing test finds them
SI = D('sac')
BEND = ['ph:bend']
POS = [f'ph:bend&test:stand&dx:{k}' for k in ('ant', 'post', 'up', 'down', 'in', 'out', 'psup', 'pinf')] + ['ph:bend&test:seat&dx:sac']
def panel(x0, y0, x1, y1, t): add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="36" class="dyn-soft"/>'); text(t, x0 + 30, y0 + 44, 'nf-l1')
BONE = 'fill:var(--dk10);fill-opacity:.18;stroke:var(--dk10);stroke-width:4'
def dot(x, y, when=None, unless=None, c='--ink-2', r=14): add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var({c})"/>', when=when, unless=unless)

text('The pelvis — flexion tests and innominate dysfunctions', 180, 150, 'dyn-big')
text('dysfunction on the patient’s LEFT · a moved landmark is red, its normal place is a hollow ring', 180, 176, 'dyn-cap')

# ════════ front view ════════
panel(300, 230, 1300, 1000, 'From the front — ASIS and pubic tubercles')
FX = 800
add(f'<path d="M{FX - 360} 380 C{FX - 420} 560 {FX - 260} 760 {FX - 60} 820 L{FX + 60} 820 C{FX + 260} 760 {FX + 420} 560 {FX + 360} 380 '
    f'C{FX + 200} 460 {FX - 200} 460 {FX - 360} 380 Z" style="{BONE}"/>')
text('patient’s right', FX - 300, 960, 'nf-l2', 'middle'); text('patient’s LEFT', FX + 300, 960, 'nf-l1', 'middle')
RA, LA, Y_A = FX - 330, FX + 330, 470               # ASIS
RP, LP, Y_P = FX - 50, FX + 50, 820                 # pubic tubercles
dot(RA, Y_A); dot(RP, Y_P)
MOVE_A = dict(ant=(0, 40), post=(0, -40), up=(0, -40), down=(0, 40), **{'in': (-40, 0)}, out=(40, 0))
MOVE_P = dict(ant=(0, 30), post=(0, -30), up=(0, -24), psup=(0, -36), pinf=(0, 36))
dot(LA, Y_A, unless=D(*MOVE_A)); dot(LP, Y_P, unless=D(*MOVE_P))
for k, (dx, dy) in MOVE_A.items():
    add(f'<circle cx="{LA}" cy="{Y_A}" r="14" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=D(k)); dot(LA + dx, Y_A + dy, when=D(k), c='--bad')
for k, (dx, dy) in MOVE_P.items():
    add(f'<circle cx="{LP}" cy="{Y_P}" r="14" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=D(k)); dot(LP + dx, Y_P + dy, when=D(k), c='--bad')
text('ASIS', RA - 40, Y_A + 6, 'nf-l2', 'end'); text('pubic tubercles', FX, Y_P + 60, 'nf-l2', 'middle')

# ════════ back view ════════
panel(1350, 230, 2400, 1000, 'From behind — PSIS under the examiner’s thumbs')
BX = 1875
add(f'<path d="M{BX - 300} 420 C{BX - 360} 600 {BX - 200} 760 {BX - 80} 820 L{BX + 80} 820 C{BX + 200} 760 {BX + 360} 600 {BX + 300} 420 Z" style="{BONE}"/>')
add(f'<path d="M{BX - 80} 520 L{BX + 80} 520 L{BX + 30} 800 L{BX - 30} 800 Z" style="fill:var(--dk7);fill-opacity:.2;stroke:var(--dk7);stroke-width:3"/>')
text('sacrum', BX, 700, 'nf-l2', 'middle')
text('patient’s LEFT', BX - 280, 960, 'nf-l1', 'middle'); text('patient’s right', BX + 280, 960, 'nf-l2', 'middle')
LPS, RPS, Y_S = BX - 140, BX + 140, 560
MOVE_S = dict(ant=(0, -36), post=(0, 36), up=(0, -36), down=(0, 36), **{'in': (-36, 0)}, out=(36, 0))   # back view: left PSIS is left of BX; lateral = -x, medial = +x
# PSIS normal / moved (static, upright)
dot(RPS, Y_S, unless=BEND)
dot(LPS, Y_S, unless=D(*MOVE_S) + BEND)
for k, (dx, dy) in MOVE_S.items():
    add(f'<circle cx="{LPS}" cy="{Y_S}" r="14" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=[f'dx:{k}&ph:up'])
    dot(LPS + dx, Y_S + dy, when=[f'dx:{k}&ph:up'], c='--bad')
text('PSIS', RPS + 40, Y_S + 6, 'nf-l2')
text('upright — note where the thumbs start', BX, 300, 'nf-l1 dyn-tag', 'middle', when=['ph:up'])
text('bending forward: left thumb rides farther up — positive on the LEFT', BX, 300, 'nf-l1 dyn-tag', 'middle', when=POS)
text('bending forward: thumbs travel together — negative', BX, 300, 'nf-l1 dyn-tag', 'middle', when=BEND, unless=POS)
text('standing: legs pull on the pelvis — picks up iliosacral (innominate) problems', BX, 1060, 'nf-l1', 'middle', when=['test:stand'])
text('seated: the femurs brace the innominates — picks up sacroiliac (sacral) problems', BX, 1060, 'nf-l1', 'middle', when=['test:seat'])

TAG = dict(ant='Anterior rotation: ASIS down, PSIS up — hamstring tightness, tender iliolumbar ligament',
           post='Posterior rotation: ASIS up, PSIS down — groin or medial knee pain, tender inguinal ligament',
           up='Upslip: ASIS and PSIS both up — weight caught on one leg', down='Downslip: ASIS and PSIS both down — rare',
           **{'in': 'Inflare: ASIS medial, PSIS lateral'}, out='Outflare: ASIS lateral, PSIS medial',
           psup='Superior pubic shear: left tubercle up — tender inguinal ligament, can mimic cystitis',
           pinf='Inferior pubic shear: left tubercle down', sac='Sacral (sacroiliac) dysfunction: the seated test is the one that turns positive')
for k, t in TAG.items(): text(t, 1350, 1100, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ motion: the thumbs ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{RPS} {Y_S} V{Y_S - 120}', len=120, speed=40, r=14, base=dict(th=1), when=BEND),
  dict(d=f'M{LPS} {Y_S} V{Y_S - 120}', len=120, speed=40, r=14, base=dict(th=1), when=BEND, unless=POS),
  dict(d=f'M{LPS} {Y_S} V{Y_S - 220}', len=220, speed=73, r=14, base=dict(th=1), when=POS),
]
sites = [dict(x=BX + 420, y=Y_S - 260, n=[0, -1], w=10, t='rec', l='', aria='Flexion tests', c='flextests', ions=[]),
         dict(x=FX, y=Y_A, n=[0, 1], w=10, t='rec', l='', aria='Innominate rotation', c='innomrot', ions=[]),
         dict(x=FX, y=Y_P, n=[0, -1], w=10, t='rec', l='', aria='Pubic shear', c='pubicshear', ions=[])]

readouts = [
  dict(l='Standing flexion test (left)', mods=[dict(when=IS, d=1), dict(when=SI, d=0)]),
  dict(l='Seated flexion test (left)', mods=[dict(when=SI, d=1), dict(when=IS, d=0)]),
  dict(l='Left ASIS height', mods=[dict(when=D('post', 'up'), d=1), dict(when=D('ant', 'down'), d=-1), dict(when=D('in', 'out'), d=0)]),
]

notes = {
  '': 'Thumbs on both PSISs, the patient bends forward: the PSIS that rides farther up and forward marks the restricted side. Standing, '
      'the legs pull on the pelvis, so a positive standing test points to an iliosacral (innominate) problem; seated, the femurs brace '
      'the innominates, so a positive seated test points to a sacroiliac (sacral) problem.',
  'test:seat': 'Seated flexion test. False positives either way: tight hamstrings, quadratus lumborum, iliopsoas, a short leg — treat and retest.',
  'dx:ant': 'Anterior innominate rotation (about the inferior transverse axis): ASIS inferior, PSIS superior; tends to bring that pubic '
            'bone down. Named for the free direction, on the side of the positive standing test.',
  'dx:post': 'Posterior innominate rotation: ASIS superior, PSIS inferior; brings that pubic bone up. Groin (rectus femoris) or medial '
             'knee (sartorius) pain.',
  'dx:up': 'Superior innominate shear (upslip): nonphysiologic — ASIS and PSIS both superior, the pubic ramus may be too; slackens the '
           'sacrotuberous ligament.',
  'dx:down': 'Inferior innominate shear (downslip): ASIS and PSIS both inferior; rare, and walking tends to reduce it.',
  'dx:in': 'Inflare (about a vertical axis): ASIS medial, PSIS lateral. Treat any rotation first — until then a medial ASIS isn’t reliable.',
  'dx:out': 'Outflare: ASIS lateral, PSIS medial.',
  'dx:psup': 'Superior pubic shear: named for the side of the positive standing flexion test — a positive left test with a high left '
             'tubercle is a LEFT superior shear, not a right inferior one.',
  'dx:pinf': 'Inferior pubic shear: left tubercle low, positive standing test on the left.',
  'dx:sac': 'A sacral (sacroiliac) dysfunction turns the seated flexion test positive; the femurs brace the innominates out of the picture.',
}

dyn = dict(
  kinds=dict(th=['thumb', '--accent']), groups=[['thumb', 'Examiner’s thumbs']],
  switches=[dict(id='ph', label='Flexion test', type='steps', auto=3, options=[['up', 'Upright'], ['bend', 'Bending forward']]),
            dict(id='test', label='Position', type='steps', options=[['stand', 'Standing'], ['seat', 'Seated']]),
            dict(id='dx', label='Left-sided dysfunction', type='one', options=[
              ['ant', 'Anterior innominate', 'innomrot'], ['post', 'Posterior innominate', 'innomrot'], ['up', 'Upslip', 'innomshear'],
              ['down', 'Downslip', 'innomshear'], ['in', 'Inflare', 'innomflare'], ['out', 'Outflare', 'innomflare'],
              ['psup', 'Superior pubic shear', 'pubicshear'], ['pinf', 'Inferior pubic shear', 'pubicshear'], ['sac', 'Sacral dysfunction', 'flextests']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Foundations of Osteopathic Medicine ch 37–38 · OCOM OMM')

MAP = dict(
  id='pelvsim', title='Pelvis in Motion', topic='omm', after='cranial',
  sub='Run the standing and seated flexion tests and watch the thumb on the restricted side ride up; then see the landmarks move for '
      'anterior and posterior rotation, upslip and downslip, inflare and outflare, and pubic shears',
  w=3600, h=1900,
  fa='',
  src=['Foundations of Osteopathic Medicine ch 37 — Pelvis', 'Foundations of Osteopathic Medicine ch 38 — Functional Anatomy and Diagnosis of the Sacrum',
       'Foundations of Osteopathic Medicine ch 31 — Osteopathic Segmental Examination', 'OCOM OMM — OMS2 written midterm study guide'],
  lanes=[('pvTest', 'Flexion tests', 'glycolysis'), ('pvInn', 'Innominate', 'tca'), ('pvPub', 'Pubic symphysis', 'gluconeo')],
  nodes=[
    ('pv1', 'Standing vs seated flexion', 330, 1660, 'pvTest', 'iliosacral vs sacroiliac', ['flextests'], 'hub'),
    ('pv2', 'Anterior · posterior rotation', 760, 1660, 'pvInn', 'inferior transverse axis', ['innomrot']),
    ('pv3', 'Upslip · downslip', 1200, 1660, 'pvInn', 'vertical shear', ['innomshear']),
    ('pv4', 'Inflare · outflare', 1640, 1660, 'pvInn', 'vertical axis', ['innomflare']),
    ('pv5', 'Pubic shear', 2080, 1660, 'pvPub', 'named for the positive side', ['pubicshear'])],
  panels=[
    (2500, PANY, 1000, 'Landmarks on the involved side', [
      ('Anterior rotation', 'ASIS ↓ · PSIS ↑'), ('Posterior rotation', 'ASIS ↑ · PSIS ↓'),
      ('Upslip / downslip', 'ASIS and PSIS both ↑ / both ↓'), ('Inflare / outflare', 'ASIS medial / lateral'),
      ('Pubic shear', 'tubercle ↑ or ↓ on the positive side')])],
  dyn=dyn)
