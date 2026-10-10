# Fetal Circulation in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A schematic heart, lungs, liver, placenta and head with the blood moving: umbilical vein (the most oxygenated blood) →
# ductus venosus → IVC → right atrium → foramen ovale → left heart → aorta → brain; SVC → right ventricle → pulmonary
# artery → ductus arteriosus → descending aorta → umbilical arteries → placenta, with little going to the high-resistance
# lungs. A `steps` switch (auto) runs fetus → first breath → newborn: the lungs open, the foramen ovale and ductus close and
# the shunts become their ligaments. A `one` switch shows what goes wrong or what drugs do: PDA, PPHN, patent foramen
# ovale, D-transposition, indomethacin, alprostadil. 5 readouts. Facts from the pinned cards (fetalcirc, pda, asd, pphn,
# dtga, tof, eisenmenger, nrds); FA pages in `fa`. No new cards.
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


ST = 'st'
S = lambda *k: [f'{ST}:{x}' for x in k]
D = lambda *k: [f'dx:{x}' for x in k]
PANY = 800
FETAL = S('fetal')
AFTER = ['st:birth&!dx:pphn', 'st:newborn&!dx:pphn']
DA_OPEN = S('fetal', 'birth') + D('pda', 'pphn', 'pge1', 'dtga')
FO_OPEN = S('fetal') + D('pphn', 'pfo', 'dtga')
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def room(x0, y0, x1, y1, lab, cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="{cls}"/>')
    text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')

text('Fetal circulation — three shunts, closed at birth', 180, 150, 'dyn-big')
text('red = oxygen-rich · blue = oxygen-poor · schematic positions', 180, 176, 'dyn-cap')

# ════════ the organs ════════
room(1180, 200, 1500, 290, 'Brain · upper body')
room(300, 330, 640, 620, 'Lungs')
add('<rect x="300" y="330" width="340" height="290" rx="24" style="fill:var(--dk11);fill-opacity:.12"/>', when=FETAL)
text('fluid-filled, high resistance', 470, 600, 'nf-l2', 'middle', when=FETAL, unless=D('pphn'))
text('expanding — resistance falls', 470, 600, 'nf-l2', 'middle', when=['st:birth&!dx:pphn'])
text('vessels fail to relax', 470, 600, 'nf-l1 dyn-tag', 'middle', when=D('pphn'))
room(880, 560, 1120, 720, 'Right atrium')
room(1280, 560, 1520, 720, 'Left atrium')
room(880, 770, 1120, 940, 'Right ventricle')
room(1280, 770, 1520, 940, 'Left ventricle')
room(640, 1090, 920, 1260, '')
text('Liver', 760, 1236, 'nf-l1', 'middle')
room(300, 1360, 760, 1500, 'Placenta')
add('<rect x="300" y="1360" width="460" height="140" rx="24" style="fill:var(--surface);fill-opacity:.7"/>', unless=FETAL)
text('placenta gone', 530, 1530, 'nf-l2', 'middle', unless=FETAL)
room(1880, 1230, 2240, 1360, 'Lower body')
# vessels (drawn lines)
V = dict(
  uv='M640 1360 C640 1260 680 1200 700 1180 L860 1175',
  dv='M860 1175 H1000',
  ivc='M1000 1250 V720',
  svc='M1050 290 V560',
  fo='M1120 640 H1280',
  pa='M960 850 H760 V400 H1250',
  da='M1250 400 H1700',
  lungsbr='M760 470 H640',
  pv='M470 330 V270 H1360 V560',
  ao='M1400 770 V360 C1400 300 1460 290 1520 290 C1640 290 1700 340 1700 400 V1230',
  head='M1450 330 V290',
  ua='M1700 1240 V1300 H1880 M1700 1300 V1440 H760',
)
for k, d in V.items():
    if k in ('fo', 'da', 'dv', 'uv'): continue
    add(f'<path d="{d}" class="dyn-line"/>')
add(f'<path d="{V["da"]}" style="fill:none;stroke:var(--dk11);stroke-width:10;opacity:.5"/>', when=DA_OPEN, unless=D('indo'))
add(f'<path d="{V["da"]}" style="fill:none;stroke:var(--ink-3);stroke-width:4;stroke-dasharray:4 8"/>', unless=DA_OPEN)
add(f'<path d="{V["da"]}" style="fill:none;stroke:var(--ink-3);stroke-width:4;stroke-dasharray:4 8"/>', when=D('indo'))
text('ductus arteriosus', 1480, 360, 'nf-l1', 'middle', when=DA_OPEN, unless=D('indo'))
text('ligamentum arteriosum', 1480, 360, 'nf-l2', 'middle', unless=DA_OPEN)
text('closing — indomethacin', 1480, 360, 'nf-l1 dyn-tag', 'middle', when=D('indo'))
add(f'<path d="{V["fo"]}" style="fill:none;stroke:var(--nf-blood);stroke-width:12;opacity:.5"/>', when=FO_OPEN)
add('<path d="M1200 600 V680" style="fill:none;stroke:var(--ink-3);stroke-width:6"/>', unless=FO_OPEN)
text('foramen ovale', 1200, 545, 'nf-l1', 'middle', when=FO_OPEN)
text('fossa ovalis', 1200, 545, 'nf-l2', 'middle', unless=FO_OPEN)
add(f'<path d="{V["uv"]}" style="fill:none;stroke:var(--nf-blood);stroke-width:8"/><path d="{V["dv"]}" style="fill:none;stroke:var(--nf-blood);stroke-width:8"/>', when=FETAL)
add(f'<path d="{V["uv"]}" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:4 8"/><path d="{V["dv"]}" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:4 8"/>', unless=FETAL)
text('umbilical vein — highest O₂', 560, 1290, 'nf-l1', 'end', when=FETAL)
text('ligamentum teres', 560, 1290, 'nf-l2', 'end', unless=FETAL)
text('ductus venosus', 930, 1150, 'nf-l1', 'middle', when=FETAL)
text('ligamentum venosum', 930, 1150, 'nf-l2', 'middle', unless=FETAL)
text('umbilical arteries', 1240, 1470, 'nf-l1', 'middle', when=FETAL)
text('medial umbilical ligaments', 1240, 1470, 'nf-l2', 'middle', unless=FETAL)
text('aorta', 1720, 700, 'nf-l1')
text('pulmonary artery', 740, 700, 'nf-l1', 'end')
text('SVC', 1070, 470, 'nf-l2'); text('IVC', 1020, 1080, 'nf-l2')
# disease marks
text('aorta → pulmonary artery: continuous machinelike murmur', 1480, 460, 'nf-l1 dyn-tag', 'middle', when=D('pda'))
text('a venous clot crosses to the left — paradoxical embolus', 1200, 1000, 'nf-l1 dyn-tag', 'middle', when=D('pfo'))
text('aorta from the RV, pulmonary trunk from the LV — two parallel circuits; mixing keeps the baby alive', 1200, 1040, 'nf-l1 dyn-tag', 'middle', when=D('dtga'))
text('alprostadil (PGE₁) keeps the ductus open', 1480, 460, 'nf-l1 dyn-tag', 'middle', when=D('pge1'))
text('right-to-left through the foramen ovale and ductus — preductal sat > postductal', 1200, 1040, 'nf-l1 dyn-tag', 'middle', when=D('pphn'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FETALISH = FETAL + D('pphn')
flows = [
  dict(d=V['uv'] + ' H1000 V720', len=820, speed=120, r=7, base=dict(), when=FETAL, mods=[m(FETAL, set=dict(ox=6))]),
  dict(d=V['fo'], len=160, speed=80, r=7, base=dict(), when=FO_OPEN, mods=[m(FETAL, set=dict(ox=4)), m(D('pphn', 'pfo', 'dtga'), set=dict(dx=3))]),
  dict(d=V['ao'], len=1300, speed=140, r=7, base=dict(ox=6), mods=[m(D('pphn'), set=dict(ox=3))]),
  dict(d='M1450 330 V290', len=40, speed=40, r=6, base=dict(ox=1)),
  dict(d=V['svc'], len=270, speed=100, r=7, base=dict(dx=4)),
  dict(d='M1000 1250 V720', len=530, speed=100, r=7, base=dict(), unless=FETAL, mods=[m(['!st:fetal'], set=dict(dx=4))]),
  dict(d='M960 720 V850 H760 V400 H1250', len=1070, speed=130, r=7, base=dict(dx=5)),
  dict(d=V['da'], len=450, speed=110, r=7, base=dict(), when=DA_OPEN,
       mods=[m(FETALISH + D('pge1', 'dtga'), set=dict(dx=5)), m(D('indo'), set=dict(dx=0))]),
  dict(d='M1700 400 H1250', len=450, speed=110, r=7, base=dict(), when=D('pda'), mods=[m(D('pda'), set=dict(ox=5))]),
  dict(d=V['lungsbr'], len=120, speed=60, r=7, base=dict(dx=1), mods=[m(AFTER, set=dict(dx=6))]),
  dict(d=V['pv'], len=1300, speed=150, r=7, base=dict(ox=1), mods=[m(AFTER, set=dict(ox=7))]),
  dict(d='M1700 1240 V1440 H760', len=1150, speed=140, r=7, base=dict(), when=FETAL, mods=[m(FETAL, set=dict(dx=5))]),
  dict(d='M1700 1240 V1300 H1880', len=240, speed=80, r=7, base=dict(ox=3)),
  dict(d='M760 1250 C840 1200 900 900 1120 660', len=700, speed=110, r=8, base=dict(), when=D('pfo'), mods=[m(D('pfo'), set=dict(clot=2))]),
]
sites = [dict(x=1200, y=640, n=[0, 1], w=10, t='ch', l='', aria='Foramen ovale', c='asd', ions=[]),
         dict(x=1480, y=400, n=[0, -1], w=10, t='ch', l='', aria='Ductus arteriosus', c='pda', ions=[]),
         dict(x=930, y=1175, n=[0, 1], w=10, t='rec', l='', aria='Fetal circulation', c='fetalcirc', ions=[])]

readouts = [
  dict(l='Pulmonary vascular resistance', mods=[dict(when=AFTER, d=-1), dict(when=D('pphn'), d=1)]),
  dict(l='Pulmonary blood flow', mods=[dict(when=AFTER, d=1), dict(when=D('pphn'), d=-1)]),
  dict(l='Left atrial pressure', mods=[dict(when=AFTER, d=1)]),
  dict(l='Preductal minus postductal O₂ sat', mods=[dict(when=D('pphn'), d=1)]),
  dict(l='Continuous murmur', mods=[dict(when=D('pda'), d=1)]),
]

notes = {
  '': 'Three shunts route placental blood around the liver and lungs: the ductus venosus (umbilical vein → IVC), the foramen ovale '
      '(RA → LA → brain) and the ductus arteriosus (pulmonary artery → descending aorta), because fetal pulmonary resistance is high.',
  'st:fetal': 'Fetus: the most oxygenated blood is in the umbilical vein; it bypasses the liver (ductus venosus), crosses the foramen '
              'ovale to the left heart and the brain. SVC blood goes RV → pulmonary artery → ductus arteriosus → descending aorta.',
  'st:birth': 'First breath: the lungs expand and pulmonary resistance falls, so pulmonary blood flow rises and more blood returns to '
              'the left atrium — LA pressure exceeds RA pressure and the foramen ovale flap closes.',
  'st:newborn': 'Newborn: rising O₂ and falling prostaglandins (placenta gone) close the ductus. Remnants: ligamentum arteriosum, '
                'fossa ovalis, ligamentum venosum, ligamentum teres, medial umbilical ligaments.',
  'dx:pda': 'Patent ductus arteriosus: the ductus stays open and, with pulmonary resistance now low, flow reverses — aorta into '
            'pulmonary artery, a continuous machinelike murmur. Prematurity, congenital rubella. Close it with indomethacin.',
  'dx:pphn': 'Persistent pulmonary hypertension of the newborn (meconium aspiration, pneumonia): the pulmonary vessels don’t relax, so '
             'blood keeps shunting right to left through the foramen ovale and ductus — preductal saturation above postductal.',
  'dx:pfo': 'Patent foramen ovale: the two septa never fused, so when right pressure briefly exceeds left (lifting, Valsalva) a venous '
            'clot can cross — a paradoxical embolus and stroke.',
  'dx:dtga': 'D-transposition: the aorta leaves the RV and the pulmonary trunk the LV — two parallel circuits. Life depends on mixing '
             'through a PDA, PFO or VSD: alprostadil keeps the ductus open, then balloon atrial septostomy.',
  'dx:indo': 'Indomethacin (or ibuprofen, acetaminophen) blocks prostaglandin synthesis and closes a PDA.',
  'dx:pge1': 'Alprostadil (PGE₁) keeps the ductus open in duct-dependent lesions until surgery.',
}

dyn = dict(
  kinds=dict(ox=['blood', '--nf-blood'], dx=['blood', '--dk11'], clot=['blood', '--ink-2']), groups=[['blood', 'Blood (red = O₂-rich, blue = O₂-poor)']],
  switches=[dict(id=ST, label='When', type='steps', auto=4, options=[['fetal', 'Fetus'], ['birth', 'First breath'], ['newborn', 'Newborn']]),
            dict(id='dx', label='What goes wrong · drugs', type='one', options=[
              ['pda', 'Patent ductus arteriosus', 'pda'], ['pphn', 'PPHN', 'pphn'], ['pfo', 'Patent foramen ovale', 'asd'],
              ['dtga', 'D-transposition', 'dtga'], ['indo', 'Indomethacin', 'pda'], ['pge1', 'Alprostadil (PGE₁)', 'pda']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 287, 294, 302–304 · Langman ch 13')

MAP = dict(
  id='fetalsim', title='Fetal Circulation in Motion', topic='cardio', after='chd',
  sub='Follow placental blood through the ductus venosus, foramen ovale and ductus arteriosus, then take the first breath and watch '
      'the shunts close and become ligaments — and compare PDA, PPHN, a patent foramen ovale, transposition, indomethacin and alprostadil',
  w=3500, h=1820,
  fa='285, 287, 294, 302–304',
  src=[full('Langman', 13), full('Guyton', 23)],
  lanes=[('ftNorm', 'Fetal circulation', 'glycolysis'), ('ftDz', 'Shunt problems', 'tca'), ('ftCyan', 'Cyanotic lesions', 'gluconeo')],
  nodes=[
    ('ft1', 'Fetal circulation', 330, 1620, 'ftNorm', 'three shunts', ['fetalcirc'], 'hub'),
    ('ft2', 'Patent ductus arteriosus', 760, 1620, 'ftDz', 'machinelike murmur', ['pda']),
    ('ft3', 'ASD · patent foramen ovale', 1200, 1620, 'ftDz', 'paradoxical emboli', ['asd']),
    ('ft4', 'PPHN', 1620, 1620, 'ftDz', 'right-to-left persists', ['pphn']),
    ('ft5', 'D-transposition', 330, 1750, 'ftCyan', 'parallel circuits', ['dtga']),
    ('ft6', 'Tetralogy · Eisenmenger', 760, 1750, 'ftCyan', 'PROVe · reversal', ['tof', 'eisenmenger'])],
  panels=[
    (2420, PANY, 1000, 'Shunt → remnant (First Aid p. 287)', [
      ('Ductus venosus', 'ligamentum venosum'),
      ('Foramen ovale', 'fossa ovalis'),
      ('Ductus arteriosus', 'ligamentum arteriosum'),
      ('Umbilical vein', 'ligamentum teres'),
      ('Umbilical arteries', 'medial umbilical ligaments')])],
  dyn=dyn)
