# Alveoli in Trouble in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Left: a small and a large alveolus joined by an airway, type II pneumocytes laying down surfactant and a macrophage
# clearing it — without surfactant, Laplace (P = 2T/r) empties the small one into the large one. Middle: both lungs, apices
# and bases, hilar nodes and pleura, where inhaled dust settles. Bottom: pulmonary artery → right ventricle. A `one` switch
# shows neonatal RDS (a `beta` toggle gives antenatal betamethasone), coal, silica, asbestos and beryllium dust, pulmonary
# alveolar proteinosis (GM-CSF, surfactant piles up) and pulmonary hypertension (RV against a high load). 5 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
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
NOSURF = ['dx:nrds&!beta']

text('Alveoli in trouble — surfactant, dust and pressure', 180, 150, 'dyn-big')
text('left: two alveoli and their surfactant · middle: where dust settles · bottom: the right heart’s load', 180, 176, 'dyn-cap')

# ════════ alveoli ════════
add('<path d="M560 700 H760" style="stroke:var(--dk5);stroke-width:30;opacity:.3"/>'); text('shared airway', 660, 680, 'nf-l2', 'middle')
add('<circle cx="480" cy="700" r="80" style="fill:var(--nf-h2o);fill-opacity:.12;stroke:var(--dk1);stroke-width:4"/>', unless=NOSURF)
add('<circle cx="480" cy="700" r="26" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:4"/>', when=NOSURF)
add('<circle cx="880" cy="700" r="130" style="fill:var(--nf-h2o);fill-opacity:.12;stroke:var(--dk1);stroke-width:4"/>', unless=NOSURF)
add('<circle cx="880" cy="700" r="160" style="fill:var(--nf-h2o);fill-opacity:.2;stroke:var(--dk1);stroke-width:4"/>', when=NOSURF)
text('small (r ↓ → P ↑)', 480, 580, 'nf-l2', 'middle'); text('large', 880, 520, 'nf-l2', 'middle')
add('<circle cx="480" cy="700" r="70" style="fill:none;stroke:var(--accent);stroke-width:8;stroke-dasharray:10 8"/>', unless=NOSURF + D('pap'))
add('<circle cx="880" cy="700" r="120" style="fill:none;stroke:var(--accent);stroke-width:8;stroke-dasharray:10 8"/>', unless=NOSURF + D('pap'))
add('<circle cx="880" cy="700" r="120" style="fill:var(--accent);fill-opacity:.45"/>', when=D('pap'))
add('<circle cx="480" cy="700" r="70" style="fill:var(--accent);fill-opacity:.45"/>', when=D('pap'))
add('<rect x="940" y="800" width="60" height="40" rx="10" style="fill:var(--dk4);fill-opacity:.5"/>'); text('type II pneumocyte', 1010, 830, 'nf-l2')
add('<circle cx="800" cy="620" r="30" style="fill:var(--dk10);fill-opacity:.4;stroke:var(--dk10);stroke-width:3"/>'); text('macrophage', 760, 580, 'nf-l2', 'end')
add('<circle cx="800" cy="620" r="30" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:6 6"/>', when=D('pap'))
text('no surfactant — small alveoli collapse into large: atelectasis, shunt', 680, 920, 'nf-l1 dyn-tag', 'middle', when=NOSURF)
text('betamethasone before delivery — surfactant made', 680, 920, 'nf-l1 dyn-tag', 'middle', when=['dx:nrds&beta'])
text('GM-CSF signaling lost — macrophages cannot clear surfactant', 680, 920, 'nf-l1 dyn-tag', 'middle', when=D('pap'))

# ════════ lungs + dust ════════
LX = 1500
for x, sgn in ((LX - 170, -1), (LX + 170, 1)):
    add(f'<path d="M{x} 360 C{x + sgn * 140} 380 {x + sgn * 180} 700 {x + sgn * 160} 980 C{x + sgn * 80} 1020 {x - sgn * 20} 1000 {x - sgn * 20} 960 V420 C{x - sgn * 20} 390 {x - sgn * 10} 360 {x} 360 Z" '
        f'style="fill:var(--nf-h2o);fill-opacity:.06;stroke:var(--dk1);stroke-width:4"/>')
text('apices', LX, 340, 'nf-l2', 'middle'); text('bases', LX, 1050, 'nf-l2', 'middle')
add(f'<circle cx="{LX - 120}" cy="640" r="20" style="fill:var(--dk6);fill-opacity:.4"/><circle cx="{LX + 120}" cy="640" r="20" style="fill:var(--dk6);fill-opacity:.4"/>')
text('hilar nodes', LX, 620, 'nf-l2', 'middle')
APX = [(LX - 230, 450), (LX - 260, 520), (LX + 230, 450), (LX + 260, 520), (LX - 200, 500), (LX + 200, 500)]
BAS = [(LX - 260, 880), (LX - 230, 940), (LX + 260, 880), (LX + 230, 940), (LX - 280, 820), (LX + 280, 820)]
for x, y in APX:
    add(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--ink);opacity:.7"/>', when=D('coal'))
    add(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--ink-3);opacity:.8"/>', when=D('silica'))
for x, y in BAS:
    add(f'<path d="M{x - 14} {y} h28" style="stroke:var(--dk6);stroke-width:6"/>', when=D('asbestos'))
for x in (LX - 120, LX + 120):
    add(f'<circle cx="{x}" cy="640" r="26" style="fill:none;stroke:var(--ink-2);stroke-width:5"/>', when=D('silica'))
add(f'<path d="M{LX + 330} 700 C{LX + 340} 760 {LX + 340} 820 {LX + 330} 880" style="stroke:var(--surface);stroke-width:18"/>', when=D('asbestos'))
add(f'<path d="M{LX + 330} 700 C{LX + 340} 760 {LX + 340} 820 {LX + 330} 880" style="fill:none;stroke:var(--ink-2);stroke-width:4"/>', when=D('asbestos'))
for x, y in ((LX - 230, 700), (LX + 230, 700), (LX - 200, 600)):
    add(f'<circle cx="{x}" cy="{y}" r="22" style="fill:var(--dk10);fill-opacity:.35;stroke:var(--dk10);stroke-width:3"/>', when=D('beryl'))
TAG = dict(coal='coal — upper lobes, small rounded nodules · Caplan with RA', silica='silica — upper lobes, eggshell hilar nodes · macrophages impaired → TB',
           asbestos='asbestos — lower lobes, calcified pleural plaques, ferruginous bodies · carcinoma > mesothelioma; smoking synergy',
           beryl='beryllium — noncaseating granulomas (aerospace)', nrds='preterm, grunting, retractions — ground glass · L:S ≥ 2.0 = mature',
           pap='bilateral patchy opacities · anti-GM-CSF autoantibodies (90%) · whole-lung lavage',
           ph='mean PA pressure > 20 mmHg — RV hypertrophy, parasternal heave → cor pulmonale')
for k, s in TAG.items(): text(s, 1300, 1450, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ RV ════════
add('<path d="M500 1250 H1100" style="stroke:var(--nf-h2o);stroke-width:30;opacity:.3"/>', unless=D('ph')); text('pulmonary artery', 800, 1220, 'nf-l2', 'middle')
add('<path d="M500 1250 H1100" style="stroke:var(--bad);stroke-width:18;opacity:.6"/>', when=D('ph'))
add('<rect x="320" y="1180" width="180" height="150" rx="40" style="fill:var(--surface);stroke:var(--dk3);stroke-width:5"/>', unless=D('ph'))
add('<rect x="300" y="1160" width="220" height="190" rx="50" style="fill:var(--surface);stroke:var(--bad);stroke-width:14"/>', when=D('ph'))
text('RV', 410, 1265, 'nf-l1', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M480 700 H880', len=400, speed=80, r=9, base=dict(air=3), when=NOSURF),
  dict(d='M960 820 C920 780 900 760 880 740', len=110, speed=50, r=8, base=dict(surf=3), unless=NOSURF),
  dict(d='M860 700 C840 670 820 650 800 630', len=100, speed=50, r=8, base=dict(surf=2), unless=D('pap')),
  dict(d=f'M{LX} 250 C{LX - 120} 320 {LX - 220} 400 {LX - 230} 460', len=300, speed=90, r=8, base=dict(dust=3), when=D('coal', 'silica')),
  dict(d=f'M{LX} 250 C{LX + 200} 400 {LX + 280} 700 {LX + 260} 880', len=700, speed=90, r=8, base=dict(dust=3), when=D('asbestos')),
  dict(d='M500 1250 H1100', len=600, speed=120, r=9, base=dict(blood=3), mods=[m(D('ph'), speed=0.4)]),
]
sites = [dict(x=480, y=820, n=[0, 1], w=10, t='rec', l='', aria='Neonatal RDS', c='nrds', ions=[]),
         dict(x=800, y=560, n=[-1, -1], w=10, t='rec', l='', aria='Pulmonary alveolar proteinosis', c='pap', ions=[]),
         dict(x=LX + 360, y=600, n=[1, 0], w=10, t='rec', l='', aria='Pneumoconioses', c='pneumoconiosis', ions=[]),
         dict(x=1140, y=1250, n=[1, 0], w=10, t='rec', l='', aria='Pulmonary hypertension', c='pulmhtn', ions=[])]

readouts = [
  dict(l='Alveolar collapse · shunt', mods=[dict(when=NOSURF, d=1)]),
  dict(l='Fibrosis', mods=[dict(when=D('coal', 'silica', 'asbestos'), d=1)]),
  dict(l='TB risk', mods=[dict(when=D('silica'), d=1)]),
  dict(l='Lung carcinoma risk', mods=[dict(when=D('asbestos'), d=1)]),
  dict(l='Right ventricle load', mods=[dict(when=D('ph'), d=1)]),
]

notes = {
  '': 'Surfactant from type II pneumocytes lowers surface tension so small alveoli stay open (P = 2T/r); macrophages clear it and '
      'eat dust. Pick a disease.',
  'dx:nrds': 'Neonatal RDS: too little surfactant — small alveoli collapse into large: diffuse atelectasis, a big right-to-left '
             'shunt. Prematurity, maternal diabetes (fetal insulin), C-section without labor. Synthesis starts ~20 wk, mature ~35 '
             'wk. Antenatal betamethasone; surfactant; CPAP.',
  'dx:coal': 'Coal workers: upper lobes, small rounded nodules; Caplan syndrome with rheumatoid arthritis.',
  'dx:silica': 'Silicosis: sandblasting, foundries, mines — upper lobes, eggshell calcification of hilar nodes; silica impairs '
               'macrophages → TB risk; whorled collagen nodules.',
  'dx:asbestos': 'Asbestosis: shipbuilding, roofing, plumbing — lower lobes, ivory-white calcified pleural plaques, ferruginous '
                 'bodies; bronchogenic carcinoma > mesothelioma; strikingly synergistic with smoking.',
  'dx:beryl': 'Berylliosis: aerospace and manufacturing — noncaseating granulomas; sometimes steroid-responsive.',
  'dx:pap': 'Pulmonary alveolar proteinosis: GM-CSF signaling fails (autoantibodies in 90%), macrophages cannot mature and clear '
            'surfactant, which fills the alveoli. Whole-lung lavage; GM-CSF.',
  'dx:ph': 'Pulmonary hypertension: mean PA pressure > 20 mmHg; the thin-walled RV hypertrophies (parasternal heave) and fails — '
           'cor pulmonale. Groups 1–5; group 1: bosentan, sildenafil, epoprostenol, riociguat.',
  'beta': 'Maternal betamethasone before preterm delivery is the key prevention of neonatal RDS.',
}

dyn = dict(
  kinds=dict(air=['mov', '--nf-h2o'], surf=['mov', '--accent'], dust=['mov', '--ink-3'], blood=['mov', '--nf-blood']),
  groups=[['mov', 'Air · surfactant · dust · blood']],
  switches=[dict(id='dx', label='Disease', type='one', options=[
              ['nrds', 'Neonatal RDS', 'nrds'], ['coal', 'Coal', 'pneumoconiosis'], ['silica', 'Silica', 'pneumoconiosis'],
              ['asbestos', 'Asbestos', 'pneumoconiosis'], ['beryl', 'Beryllium', 'pneumoconiosis'], ['pap', 'Alveolar proteinosis', 'pap'],
              ['ph', 'Pulmonary hypertension', 'pulmhtn']]),
            dict(id='beta', label='Prevention', type='toggle', on='Betamethasone given', off='Antenatal betamethasone', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 15')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='alvdzsim', title='Alveoli in Trouble in Motion', topic='pulmo', after='lungdz',
  sub='Take surfactant away and watch small alveoli empty into large ones, fill them with surfactant that macrophages cannot '
      'clear, settle coal, silica and asbestos where each goes, and load the right ventricle',
  w=3600, h=1900,
  fa='679, 696, 698, 706',
  src=['Robbins ch 15 — The lung'],
  lanes=[('adSurf', 'Surfactant', 'tca'), ('adDust', 'Dust & vessels', 'glycolysis')],
  nodes=[
    ('ad1', 'Neonatal RDS', 330, 1720, 'adSurf', 'Laplace · L:S ratio', ['nrds'], 'hub'),
    ('ad2', 'Alveolar proteinosis', 760, 1720, 'adSurf', 'GM-CSF', ['pap']),
    ('ad3', 'Pneumoconioses', 1200, 1720, 'adDust', 'apices vs bases', ['pneumoconiosis']),
    ('ad4', 'Pulmonary hypertension', 1640, 1720, 'adDust', 'cor pulmonale', ['pulmhtn'])],
  panels=[
    (2500, PANY, 1000, 'Where dust goes (Robbins ch 15)', [
      ('Coal, silica', 'apices'), ('Asbestos', 'bases, pleural plaques'), ('Silica', 'eggshell nodes → TB'), ('Beryllium', 'granulomas')])],
  dyn=dyn)
