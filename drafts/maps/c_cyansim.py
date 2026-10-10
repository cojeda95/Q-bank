# Cyanotic Heart Disease in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A four-chamber heart between the lungs (top) and the body (bottom), with blue (deoxygenated), red (oxygenated) and purple
# (mixed) blood moving. A `one` switch rebuilds it as truncus arteriosus, tricuspid atresia, TAPVR, Ebstein anomaly,
# tetralogy of Fallot or d-TGA; toggles squat (TOF) and keep the PDA open with alprostadil (d-TGA). Only shunts the cards
# name are drawn. 3 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
ALL = ('truncus', 'tria', 'tapvr', 'ebstein', 'tof', 'tga')

text('Cyanotic heart disease — where blue blood sneaks to the body', 180, 150, 'dyn-big')
text('lungs on top, body below · blue = deoxygenated, red = oxygenated, purple = mixed', 180, 176, 'dyn-cap')

# ════════ anatomy ════════
add('<rect x="820" y="240" width="560" height="160" rx="60" style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>')
text('lungs', 1100, 330, 'nf-l1', 'middle')
add('<rect x="760" y="1380" width="680" height="160" rx="60" style="fill:var(--nf-blood);fill-opacity:.06;stroke:var(--dk3);stroke-width:4"/>')
text('body', 1100, 1470, 'nf-l1', 'middle')
CH = dict(RA=(820, 690), LA=(1120, 690), RV=(820, 880), LV=(1120, 880))
for k, (x, y) in CH.items():
    add(f'<rect x="{x}" y="{y}" width="260" height="170" rx="30" style="fill:var(--surface);stroke:var(--dk3);stroke-width:4"/>')
    text(k, x + 130, y + 95, 'nf-l1', 'middle')
add('<rect x="1060" y="700" width="40" height="40" rx="8" style="fill:var(--bad);opacity:.5"/>', when=D('tria', 'tapvr'))
text('ASD', 1080, 680, 'nf-l2', 'middle', when=D('tria', 'tapvr'))
add('<rect x="1060" y="900" width="40" height="50" rx="8" style="fill:var(--bad);opacity:.5"/>', when=D('truncus', 'tria', 'tof'))
text('VSD', 1080, 980, 'nf-l2', 'middle', when=D('truncus', 'tria', 'tof'))
add('<path d="M840 860 h220" class="nf-x"/>', when=D('tria'))
add('<path d="M830 850 L860 860 M840 870 L1060 870" style="stroke:var(--bad);stroke-width:10"/>', when=D('tria'))
text('no tricuspid valve', 950, 1080, 'nf-l1 dyn-tag', 'middle', when=D('tria'))
add('<path d="M830 950 C900 930 980 960 1070 940" style="fill:none;stroke:var(--bad);stroke-width:8"/>', when=D('ebstein'))
text('leaflets displaced down — part of the RV acts as atrium', 950, 1100, 'nf-l1 dyn-tag', 'middle', when=D('ebstein'))
# great vessels
NORM_PA = 'M900 880 C900 700 960 520 1000 400'
NORM_AO = 'M1240 880 C1240 700 1230 580 1280 540 H1700 V1380 C1700 1430 1600 1460 1440 1460'
TGA_AO = 'M900 880 C860 700 860 560 900 520 H1700 V1380 C1700 1430 1600 1460 1440 1460'
TGA_PA = 'M1240 880 C1240 700 1200 520 1180 400'
TRUNK = 'M1080 900 V520'
for d, w in ((NORM_PA, D('truncus', 'tga')), (NORM_AO, D('truncus', 'tga'))):
    add(f'<path d="{d}" style="fill:none;stroke:var(--dk2);stroke-width:30;opacity:.18"/>', unless=w)
add(f'<path d="{TGA_AO}" style="fill:none;stroke:var(--dk2);stroke-width:30;opacity:.18"/>', when=D('tga'))
add(f'<path d="{TGA_PA}" style="fill:none;stroke:var(--dk2);stroke-width:30;opacity:.18"/>', when=D('tga'))
add(f'<path d="{TRUNK} M1080 520 C1060 470 1020 430 1000 400 M1080 520 H1700 V1380" style="fill:none;stroke:var(--dk2);stroke-width:36;opacity:.22"/>', when=D('truncus'))
add('<path d="M905 760 C915 700 925 650 935 610" style="stroke:var(--bad);stroke-width:12"/>', when=D('tof'))
text('pulmonary stenosis', 860, 640, 'nf-l2', 'end', when=D('tof'))
text('overriding aorta', 1260, 640, 'nf-l2', when=D('tof'))
add('<path d="M1000 470 C1100 480 1200 500 1300 530" style="stroke:var(--accent);stroke-width:12;opacity:.7"/>', when=['dx:tga&pda'])
text('PDA (alprostadil)', 1150, 460, 'nf-l2', 'middle', when=['dx:tga&pda'])
text('aorta from RV, pulmonary trunk from LV — two parallel circuits', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('tga'))
text('one trunk over a VSD carries mixed blood to lungs and body', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('truncus'))
text('pulmonary veins drain to the right heart — only an ASD reaches the left', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('tapvr'))
text('blood must cross an ASD, then reach the lungs through a VSD or PDA', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('tria'))
text('tricuspid regurgitation · right heart failure · WPW · lithium in pregnancy', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('ebstein'))
text('PROVe — stenosis decides how much shunts right to left', 1100, 1620, 'nf-l1 dyn-tag', 'middle', when=D('tof'))
text('squatting ↑ SVR → less right-to-left shunt', 1100, 1660, 'nf-l1', 'middle', when=['dx:tof&squat'])

# ════════ motion ════════
VEN = 'M760 1460 C640 1300 620 820 820 760'
TAPV = 'M1200 400 C1300 500 700 480 700 600 C700 680 760 720 820 740'
PV = 'M1200 400 C1240 520 1240 620 1240 690'
def fl(d, n, k, when=None, unless=None, speed=110, mods=None):
    f = dict(d=d, len=900, speed=speed, r=10, base={k: n})
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    return f
flows = [
  fl(VEN, 4, 'blue'),
  fl('M900 760 V940', 2, 'blue', unless=D('tria', 'tapvr'), mods=[dict(when=D('ebstein'), set=dict(blue=1))]),
  fl('M960 940 V770', 2, 'blue', when=D('ebstein'), speed=70),
  fl(NORM_PA, 3, 'blue', unless=D('truncus', 'tga', 'tria', 'tapvr'), mods=[dict(when=D('tof'), set=dict(blue=1), speed=0.5)]),
  fl(PV, 3, 'red', unless=D('tapvr')),
  fl('M1200 760 V940', 3, 'red', unless=D('tria', 'tapvr')),
  fl(NORM_AO, 4, 'red', unless=D('truncus', 'tga', 'tria', 'tapvr', 'tof')),
  # tetralogy: RV → VSD → aorta
  fl('M940 940 C1000 940 1060 930 1100 920 C1200 900 1240 800 1240 700 C1230 580 1280 540 1320 540 H1700 V1380', 3, 'mix', when=D('tof'),
     mods=[dict(when=['dx:tof&squat'], set=dict(mix=1))]),
  fl(NORM_AO, 2, 'red', when=D('tof')),
  # truncus
  fl('M940 960 H1080 V520 H1700 V1380', 4, 'mix', when=D('truncus')),
  fl('M1080 520 C1060 470 1020 430 1000 400', 3, 'mix', when=D('truncus')),
  # tricuspid atresia: RA → ASD → LA → LV → aorta and VSD → RV → PA
  fl('M900 720 H1200 V940', 4, 'mix', when=D('tria', 'tapvr')),
  fl(NORM_AO, 4, 'mix', when=D('tria', 'tapvr')),
  fl('M1150 940 H900 ' + NORM_PA[NORM_PA.index('C'):].replace('C900 700', 'C900 700'), 2, 'mix', when=D('tria')),
  # TAPVR
  fl(TAPV, 3, 'red', when=D('tapvr')),
  fl('M900 760 V940 ' + NORM_PA.replace('M900 880', 'L900 880'), 2, 'mix', when=D('tapvr')),
  # d-TGA
  fl(TGA_AO, 4, 'blue', when=D('tga'), mods=[dict(when=['dx:tga&pda'], set=dict(blue=3))]),
  fl(TGA_PA, 3, 'red', when=D('tga')),
  fl('M1000 470 C1100 480 1200 500 1300 530', 2, 'mix', when=['dx:tga&pda']),
]
sites = [dict(x=1080, y=500, n=[0, -1], w=10, t='rec', l='', aria='Truncus arteriosus', c='truncus', ions=[]),
         dict(x=800, y=860, n=[-1, 0], w=10, t='rec', l='', aria='Tricuspid atresia', c='triatresia', ions=[]),
         dict(x=700, y=560, n=[-1, 0], w=10, t='rec', l='', aria='TAPVR', c='tapvr', ions=[]),
         dict(x=800, y=990, n=[-1, 0], w=10, t='rec', l='', aria='Ebstein anomaly', c='ebstein', ions=[]),
         dict(x=1400, y=900, n=[1, 0], w=10, t='rec', l='', aria='Tetralogy of Fallot', c='tof', ions=[]),
         dict(x=1720, y=700, n=[1, 0], w=10, t='rec', l='', aria='d-TGA', c='dtga', ions=[])]

readouts = [
  dict(l='Systemic O₂ saturation', mods=[dict(when=D('truncus', 'tria', 'tapvr', 'tof', 'tga'), d=-1)]),
  dict(l='Pulmonary blood flow', mods=[dict(when=D('tof'), d=-1)]),
  dict(l='Right-heart failure', mods=[dict(when=D('ebstein'), d=1)]),
]

notes = {
  '': 'Normal: blue blood returns to the right heart and goes to the lungs; red blood returns to the left heart and goes to the '
      'body. Cyanotic lesions let blue blood bypass the lungs. Pick a lesion.',
  'dx:truncus': 'Truncus arteriosus: neural crest cells never build the aorticopulmonary septum — one trunk over a VSD carries '
                'mixed blood to body and lungs. Early cyanosis; DiGeorge (22q11).',
  'dx:tria': 'Tricuspid atresia: no tricuspid valve, hypoplastic RV — blood crosses an ASD to the left heart and reaches the lungs '
             'through a VSD or PDA. ECG: tall P waves, left axis deviation.',
  'dx:tapvr': 'TAPVR: all pulmonary veins drain to systemic veins (SVC, coronary sinus); oxygenated blood reaches the left heart '
              'only through an ASD (sometimes a PDA).',
  'dx:ebstein': 'Ebstein anomaly: tricuspid leaflets attach low in the RV, so part of the RV acts as atrium and the valve leaks — '
                'tricuspid regurgitation, right heart failure, accessory pathways (WPW). Prenatal lithium.',
  'dx:tof': 'Tetralogy of Fallot: anterosuperior displacement of the infundibular septum → pulmonary stenosis, RVH, overriding '
            'aorta, VSD. The stenosis decides the right-to-left shunt. Tet spells; boot-shaped heart.',
  'dx:tga': 'd-TGA: the aorticopulmonary septum fails to spiral — aorta from the RV, pulmonary trunk from the LV, two parallel '
            'circuits. Profound cyanosis in the first days; egg on a string; maternal diabetes. Life depends on mixing (VSD, PDA, '
            'PFO).',
  'squat': 'Squatting (or knee-to-chest in a tet spell) raises systemic vascular resistance and reduces right-to-left shunting.',
  'pda': 'Alprostadil keeps the PDA open for mixing; balloon atrial septostomy in the first days of life.',
}

dyn = dict(
  kinds=dict(blue=['mov', '--nf-h2o'], red=['mov', '--nf-blood'], mix=['mov', '--dk7']),
  groups=[['mov', 'Blue · red · mixed blood']],
  switches=[dict(id='dx', label='Lesion', type='one', options=[
              ['truncus', 'Truncus arteriosus', 'truncus'], ['tria', 'Tricuspid atresia', 'triatresia'], ['tapvr', 'TAPVR', 'tapvr'],
              ['ebstein', 'Ebstein anomaly', 'ebstein'], ['tof', 'Tetralogy of Fallot', 'tof'], ['tga', 'd-TGA', 'dtga']]),
            dict(id='squat', label='Maneuver', type='toggle', on='Squatting', off='Squat (TOF)', def_=False),
            dict(id='pda', label='Drug', type='toggle', on='PDA kept open', off='Alprostadil (TGA)', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 12')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='cyansim', title='Cyanotic Heart Disease in Motion', topic='cardio', after='chd',
  sub='Watch blue and red blood keep apart in a normal heart, then rebuild it as truncus, tricuspid atresia, TAPVR, Ebstein, '
      'tetralogy or d-TGA — squat a tet spell and open a PDA',
  w=3600, h=1900,
  fa='285, 302',
  src=['Robbins ch 12 — The heart', 'Langman ch 13 — Cardiovascular System'],
  lanes=[('cyR2L', 'Right-to-left & mixing', 'tca'), ('cyValve', 'Valve', 'glycolysis')],
  nodes=[
    ('cy1', 'Tetralogy of Fallot', 330, 1780, 'cyR2L', 'PROVe · squat', ['tof'], 'hub'),
    ('cy2', 'd-TGA', 760, 1780, 'cyR2L', 'parallel circuits', ['dtga']),
    ('cy3', 'Truncus arteriosus', 1200, 1780, 'cyR2L', 'one trunk · 22q11', ['truncus']),
    ('cy4', 'Tricuspid atresia', 1640, 1780, 'cyR2L', 'ASD + VSD/PDA', ['triatresia']),
    ('cy5', 'TAPVR', 2080, 1780, 'cyR2L', 'veins to right heart', ['tapvr']),
    ('cy6', 'Ebstein anomaly', 2520, 1780, 'cyValve', 'lithium · WPW', ['ebstein'])],
  panels=[
    (2500, PANY, 1000, 'Mixing each lesion needs (Robbins ch 12)', [
      ('Truncus', 'VSD'), ('Tricuspid atresia', 'ASD + VSD or PDA'), ('TAPVR', 'ASD (± PDA)'), ('d-TGA', 'VSD, PDA or PFO')])],
  dyn=dyn)
