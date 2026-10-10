# Spinal Mechanics & OMT in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A thoracic column seen from behind and one vertebra from above. A `fr` switch shows Fryette Type I (neutral group curve:
# side bending and rotation to opposite sides, rotation toward the convexity — the card's T5–T8 N SRRL), Type II (a single
# flexed or extended segment, side bending and rotation to the same side — the card's T4 E SRRR) and Principle III. A motion
# barrier strip below (ease ← neutral → restrictive barrier) runs each technique — counterstrain, MET, HVLA, myofascial
# release, Still, FPR, functional — as a dot moving toward ease, toward the barrier, or through it, as the cards describe.
# 3 readouts. Facts from the pinned cards (Foundations, Atlas of Osteopathic Techniques, OCOM OMM); no First Aid pages.
# No new cards.
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

F = lambda *k: [f'fr:{x}' for x in k]
T = lambda *k: [f'tx:{x}' for x in k]
PANY = 1180
text('Spinal mechanics — Fryette’s principles, and how each technique uses the barrier', 180, 150, 'dyn-big')
text('column seen from behind · patient’s left on the left', 180, 176, 'dyn-cap')

# ════════ column from behind ════════
LV = ['T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9']
YS = [300 + i * 100 for i in range(len(LV))]
CX = 700
# neutral: straight
for lv, y in zip(LV, YS):
    add(f'<rect x="{CX - 90}" y="{y - 32}" width="180" height="64" rx="18" style="fill:var(--dk10);fill-opacity:.18;stroke:var(--dk10);stroke-width:4"/>', unless=F('t1', 't2'))
    text(lv, CX - 130, y + 6, 'nf-l2', 'end')
# Type I: T5–T8 group curve, side bent right (concave right), rotated left (toward the convexity) — N SRRL
OFF = dict(T5=-30, T6=-60, T7=-60, T8=-30)
for lv, y in zip(LV, YS):
    dx = OFF.get(lv, 0); hi = lv in OFF
    add(f'<rect x="{CX - 90 + dx}" y="{y - 32}" width="180" height="64" rx="18" style="fill:var({"--bad" if hi else "--dk10"});fill-opacity:.18;stroke:var({"--bad" if hi else "--dk10"});stroke-width:4"/>', when=F('t1'))
add('<path d="M560 470 C500 600 500 760 560 880" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:8 8"/>', when=F('t1'))
text('convex LEFT', 470, 680, 'nf-l1 dyn-tag', 'end', when=F('t1'))
text('T5–T8 N SRRL: a group, side bent right, rotated left — toward the convexity', 1200, 260, 'nf-l1 dyn-tag', 'middle', when=F('t1'))
text('long restrictor muscles hold a group curve', 1200, 290, 'nf-l2', 'middle', when=F('t1'))
# Type II: T4 single segment, extended, side bent and rotated right — E SRRR
for lv, y in zip(LV, YS):
    hi = lv == 'T4'
    add(f'<g transform="rotate({10 if hi else 0} {CX} {y})"><rect x="{CX - 90}" y="{y - 32}" width="180" height="64" rx="18" style="fill:var({"--bad" if hi else "--dk10"});fill-opacity:.18;stroke:var({"--bad" if hi else "--dk10"});stroke-width:4"/></g>', when=F('t2'))
text('T4 E SRRR: one segment, extended, side bent AND rotated right', 1200, 260, 'nf-l1 dyn-tag', 'middle', when=F('t2'))
text('short restrictor muscles · often at the top, apex or bottom of a Type I curve', 1200, 290, 'nf-l2', 'middle', when=F('t2'))
text('Principle III: motion started in one plane changes motion in the others', 1200, 260, 'nf-l1 dyn-tag', 'middle', when=F('t3'))

# ════════ one vertebra from above ════════
VX, VY = 1300, 600
VERT = f'<circle cx="{VX}" cy="{VY - 40}" r="80" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/><path d="M{VX} {VY + 40} V{VY + 150}" style="stroke:var(--ink-3);stroke-width:14;stroke-linecap:round"/>'
add(VERT, unless=F('t1', 't2'))
add(f'<g transform="rotate(-18 {VX} {VY})">{VERT}</g>', when=F('t1'))
add(f'<g transform="rotate(18 {VX} {VY})">{VERT}</g>', when=F('t2'))
text('body (front)', VX, VY - 140, 'nf-l2', 'middle')
text('back', VX, VY + 190, 'nf-l2', 'middle')
text('one vertebra from above', VX, VY + 240, 'nf-l1', 'middle')
text('Type I: rotated toward the convex (left) side', VX, VY + 280, 'nf-l1 dyn-tag', 'middle', when=F('t1'))
text('Type II: rotated right, side bent right', VX, VY + 280, 'nf-l1 dyn-tag', 'middle', when=F('t2'))
text('named for the direction of ease', VX, VY + 310, 'nf-l2', 'middle', when=F('t1', 't2'))

# ════════ barrier strip ════════
BY = 1150
add(f'<path d="M400 {BY} H2300" style="stroke:var(--ink-3);stroke-width:6"/>')
for x, lab in ((500, 'ease'), (1250, 'neutral'), (1900, 'restrictive barrier')):
    add(f'<path d="M{x} {BY - 40} V{BY + 40}" style="stroke:var({"--bad" if x == 1900 else "--ink-2"});stroke-width:{6 if x == 1900 else 3}"/>')
    text(lab, x, BY + 76, 'nf-l1', 'middle')
add(f'<rect x="1900" y="{BY - 40}" width="300" height="80" rx="10" style="fill:var(--bad);fill-opacity:.1"/>'); text('restricted range', 2050, BY + 6, 'nf-l2', 'middle')
TT = dict(cs=('Counterstrain — indirect, passive', 'shorten the tissue at the tender point until tenderness drops ≥70%, hold ~90 s, return slowly'),
          met=('MET — direct, the patient works', 'isometric contraction 3–5 s against a firm counterforce, relax, take up slack to the new barrier'),
          hvla=('HVLA — direct thrust', 'a quick, short thrust through the barrier of a localized restriction'),
          mfr=('Myofascial release — direct or indirect', 'load the fascia toward the barrier or toward ease and hold until it releases'),
          still=('Still — indirect, then direct', 'to ease, add compression, then carry through neutral into the restricted range'),
          fpr=('FPR — indirect with compression', 'flatten the curve, compress, place into ease 3–5 s, return'),
          func=('Functional — indirect', 'stack every motion pair toward ease, breathe and hold 3–5 s'))
for k, (a, b) in TT.items():
    text(a, 1350, BY - 120, 'nf-l1 dyn-tag', 'middle', when=T(k)); text(b, 1350, BY - 90, 'nf-l2', 'middle', when=T(k))
for k in ('met', 'still', 'fpr'):
    add(f'<path d="M{1250 if k != "met" else 1880} {BY - 20} v-30 M{1230 if k != "met" else 1860} {BY - 30} l20 -20 l20 20" style="fill:none;stroke:var(--accent);stroke-width:4"/>', when=T(k))
text('compression', 1150, BY - 40, 'nf-l2', 'middle', when=T('still', 'fpr'))
text('patient contracts', 1780, BY - 40, 'nf-l2', 'middle', when=T('met'))
text('contraindicated over severe osteoporosis, acute radiculopathy, spondylolisthesis, stenosis, inflamed joints', 1350, BY + 130, 'nf-l2', 'middle', when=T('hvla'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
PATH = dict(cs=(f'M1250 {BY} H520', 730, 80), met=(f'M1250 {BY} H1890', 640, 90), hvla=(f'M1880 {BY} H2050', 170, 420),
            mfr=(f'M1250 {BY} H1880', 630, 50), still=(f'M1250 {BY} H560 M560 {BY} H2050', 1600, 200), fpr=(f'M1250 {BY} H560', 690, 160),
            func=(f'M1250 {BY} H600', 650, 70))
flows = [dict(d=d, len=L, speed=sp, r=14, base=dict(seg=1), when=T(k)) for k, (d, L, sp) in PATH.items()]
flows += [dict(d=f'M{CX + 140} 300 V900', len=600, speed=90, r=8, base=dict(mv=3), when=F('t1', 't3'))]
sites = [dict(x=CX + 100, y=YS[3], n=[1, 0], w=10, t='rec', l='', aria='Fryette principles', c='fryette', ions=[]),
         dict(x=500, y=BY, n=[0, -1], w=10, t='rec', l='', aria='Counterstrain', c='counterstrain', ions=[]),
         dict(x=2250, y=BY, n=[0, -1], w=10, t='rec', l='', aria='HVLA', c='hvla', ions=[]),
         dict(x=1250, y=BY, n=[0, -1], w=10, t='rec', l='', aria='Still technique', c='stilltech', ions=[])]

readouts = [
  dict(l='Toward the barrier (direct)', mods=[dict(when=T('met', 'hvla'), d=1), dict(when=T('cs', 'fpr', 'func'), d=-1), dict(when=T('mfr', 'still'), d=0)]),
  dict(l='Patient active', mods=[dict(when=T('met'), d=1), dict(when=T('cs', 'hvla', 'fpr', 'still'), d=-1)]),
  dict(l='Segments involved', mods=[dict(when=F('t1'), d=1), dict(when=F('t2'), d=-1)]),
]

notes = {
  '': 'Fryette I (neutral): side bending and rotation go to opposite sides, rotation toward the convexity, across a group. Fryette II '
      '(flexed or extended): same side, one segment. Fryette III: motion in one plane modifies the others. Dysfunctions are named for '
      'their ease. Techniques either go toward ease (indirect), toward the barrier (direct), or both.',
  'fr:t1': 'Type I dysfunction: a group curve such as T5–T8 N SRRL, held by long restrictor muscles.',
  'fr:t2': 'Type II dysfunction: one segment, flexed or extended, such as T4 E SRRR — short restrictors; usually at the top, apex or bottom '
           'of a Type I curve. The cervical spine was left out: OA is Type I, AA mostly rotation, C2–C7 Type II.',
  'fr:t3': 'Principle III (Nelson): starting motion in one plane modifies motion in the others.',
  'tx:cs': 'Counterstrain: passive, indirect — shorten the tissue around the tender point until tenderness drops by about 70%, hold about '
           '90 seconds, return slowly. Good for acute flares and frail patients.',
  'tx:met': 'Muscle energy: the patient contracts isometrically 3–5 s against an unyielding counterforce, relaxes, and the physician takes '
            'up slack to the new barrier (Golgi tendon organ inhibition). Type II FRS/ERS, sacral torsions.',
  'tx:hvla': 'HVLA: a quick, short thrust through the barrier of a localized (often Type II) restriction. Avoid with severe osteoporosis, '
             'acute disc herniation with radiculopathy, spondylolisthesis, stenosis, inflamed joints.',
  'tx:mfr': 'Myofascial release: engage the fascia toward the barrier (direct) or toward ease (indirect) and hold until it releases.',
  'tx:still': 'Still technique: into ease, add a compression, then carry through neutral into the previously restricted range and back.',
  'tx:fpr': 'Facilitated positional release: flatten the curve, compress, place into ease for 3–5 s — gentle and quick; unlike Still it '
            'doesn’t go through the barrier.',
  'tx:func': 'Functional technique (Johnston): stack every motion pair — including translations and the breath — toward ease, hold 3–5 s.',
}

dyn = dict(
  kinds=dict(seg=['seg', '--accent'], mv=['seg', '--dk2']), groups=[['seg', 'Segment motion']],
  switches=[dict(id='fr', label='Fryette', type='one', options=[
              ['t1', 'Type I — neutral group', 'fryette'], ['t2', 'Type II — single segment', 'fryette'], ['t3', 'Principle III', 'fryette']]),
            dict(id='tx', label='Technique', type='one', options=[
              ['cs', 'Counterstrain', 'counterstrain'], ['met', 'Muscle energy', 'met'], ['hvla', 'HVLA', 'hvla'], ['mfr', 'Myofascial release', 'mfr'],
              ['still', 'Still technique', 'stilltech'], ['fpr', 'FPR', 'fpr'], ['func', 'Functional', 'functech']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Foundations of Osteopathic Medicine ch 31, 43, 56 · Atlas of Osteopathic Techniques ch 5, 10 · OCOM OMM')

MAP = dict(
  id='frysim', title='Spinal Mechanics & OMT in Motion', topic='omm', after='omt',
  sub='See a Type I group curve and a Type II single segment couple side bending and rotation, then run each technique along the barrier — '
      'counterstrain, muscle energy, HVLA, myofascial release, Still, FPR and functional',
  w=3600, h=1900,
  fa='',
  src=['Foundations of Osteopathic Medicine ch 31 — Osteopathic Segmental Examination', 'Atlas of Osteopathic Techniques ch 5 — Intersegmental Motion Testing',
       'OCOM OMM — OMS2 written midterm study guide', 'OCOM OMM — Thoracic OMT review lab rubric',
       'Foundations of Osteopathic Medicine ch 43 — Clinical Assessment: Viscerosomatic, Somatosomatic, Somatovisceral Reflexes; Counterstrain Points, Myofascial Trigger Points, and Chapman Reflexes',
       'Foundations of Osteopathic Medicine ch 93 — Osteopathic Considerations in the Patient With Low Back Pain',
       'OCOM OMM — Pulmonology and rib OMT lab rubric', 'OCOM OMM — Week 9 lab rubric: upper and lower crossed syndromes',
       'Atlas of Osteopathic Techniques ch 10 — Muscle Energy Techniques', 'Foundations of Osteopathic Medicine (4e) ch 42 — Acute Low Back Pain',
       'OCOM OMM — Lab rubric: Still technique and FPR',
       'Foundations of Osteopathic Medicine ch 56 — Still Technique: A Facilitated Indirect Then Direct Method'],
  lanes=[('fyMech', 'Spinal mechanics', 'glycolysis'), ('fyDir', 'Direct', 'tca'), ('fyInd', 'Indirect', 'gluconeo')],
  nodes=[
    ('fy1', 'Fryette principles', 330, 1660, 'fyMech', 'I group · II segment', ['fryette'], 'hub'),
    ('fy2', 'Muscle energy', 760, 1660, 'fyDir', 'patient contracts', ['met']),
    ('fy3', 'HVLA', 1200, 1660, 'fyDir', 'thrust', ['hvla']),
    ('fy4', 'Myofascial release', 1640, 1660, 'fyDir', 'direct or indirect', ['mfr']),
    ('fy5', 'Counterstrain', 330, 1790, 'fyInd', 'tender point · 90 s', ['counterstrain']),
    ('fy6', 'Still · FPR', 760, 1790, 'fyInd', 'compression', ['stilltech', 'fpr']),
    ('fy7', 'Functional technique', 1200, 1790, 'fyInd', 'stack ease', ['functech'])],
  panels=[
    (2500, PANY, 1000, 'Fryette at a glance', [
      ('Type I (neutral)', 'group · SB and R opposite · R toward convexity'), ('Type II (F or E)', 'one segment · SB and R same side'),
      ('Principle III', 'one plane modifies the others'), ('Cervical', 'OA Type I · AA rotation · C2–C7 Type II')])],
  dyn=dyn)
