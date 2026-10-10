# Emboli in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A whole-body circulation: leg veins, femur marrow, uterus and a neck central line feed the IVC/SVC → right heart →
# pulmonary artery → lungs → left heart → aorta → brain, skin, kidney and legs, with a knee joint. A `one` switch sends one
# kind of embolus on its route — DVT → PE, fat (long-bone fracture → lungs, brain, skin), iatrogenic air (central line),
# decompression bubbles (joints, lungs, nerves), amniotic fluid (→ lungs, DIC), left-atrial mural thrombus (→ brain, kidney,
# legs) — and a `pfo` toggle lets a DVT cross into the left heart (paradoxical embolism). 5 readouts. Facts from the pinned
# cards; FA pages in `fa`. No new cards.
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
PX = dict(dvt='M560 1600 C700 1500 900 1350 1000 1200 V880', fat='M500 1380 C650 1330 850 1290 1000 1200 V880',
          afe='M780 1280 C860 1260 940 1240 1000 1200 V880', air='M820 300 C900 400 980 600 1000 860')
PA = 'M1000 880 V1040 C1060 900 1100 700 1100 600 C1080 540 1000 500 930 470'
PV = 'M1270 470 C1250 600 1220 750 1200 880'
BRAIN = 'M1200 880 V1020 C1300 950 1450 700 1500 500 C1520 400 1560 330 1600 300'
SKIN = 'M1200 1020 C1400 950 1650 800 1900 720'
KID = 'M1200 1020 C1350 1050 1550 1050 1700 1020'
LEG = 'M1200 1020 C1350 1150 1450 1350 1500 1550'
PFO = 'M1000 880 H1200 V1020 C1300 950 1450 700 1500 500 C1520 400 1560 330 1600 300'

text('Emboli — where each one starts, and where it lodges', 180, 150, 'dyn-big')
text('veins and right heart on the left, lungs on top, left heart and arteries on the right · an embolus moves like a FAT BAT', 180, 176, 'dyn-cap')

# ════════ body ════════
for x in (900, 1300):
    add(f'<ellipse cx="{x}" cy="460" rx="170" ry="130" style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>')
text('lungs', 1100, 300, 'nf-l1', 'middle')
add('<rect x="940" y="820" width="320" height="260" rx="40" style="fill:var(--nf-blood);fill-opacity:.06;stroke:var(--dk3);stroke-width:4"/>')
add('<path d="M1100 820 V1080" style="stroke:var(--dk3);stroke-width:4"/>')
text('RA / RV', 1020, 1110, 'nf-l2', 'middle'); text('LA / LV', 1180, 1110, 'nf-l2', 'middle')
add('<path d="M1000 1200 V1080 M1000 820 V300" style="stroke:var(--nf-h2o);stroke-width:22;opacity:.25"/>')
text('IVC', 1020, 1180, 'nf-l2'); text('SVC', 1020, 760, 'nf-l2')
add('<ellipse cx="1600" cy="300" rx="130" ry="90" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--dk2);stroke-width:4"/>'); text('brain', 1600, 190, 'nf-l1', 'middle')
add('<rect x="1880" y="660" width="120" height="120" rx="20" style="fill:var(--dk9);fill-opacity:.12;stroke:var(--dk9);stroke-width:3"/>'); text('skin', 1940, 820, 'nf-l2', 'middle')
add('<ellipse cx="1730" cy="1020" rx="40" ry="60" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--dk10);stroke-width:3"/>'); text('kidney', 1800, 1030, 'nf-l2')
text('legs', 1500, 1600, 'nf-l2', 'middle')
add('<circle cx="1900" cy="1450" r="60" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:3"/>'); text('joint', 1900, 1540, 'nf-l2', 'middle')
add(f'<path d="{PX["dvt"]}" style="fill:none;stroke:var(--nf-h2o);stroke-width:14;opacity:.3"/>'); text('deep leg veins', 560, 1640, 'nf-l2', 'middle')
add('<rect x="440" y="1250" width="60" height="280" rx="24" style="fill:var(--dk6);fill-opacity:.2;stroke:var(--dk6);stroke-width:3"/>'); text('femur', 470, 1230, 'nf-l2', 'middle')
add('<path d="M430 1420 L510 1380" style="stroke:var(--bad);stroke-width:6"/>', when=D('fat'))
add('<ellipse cx="780" cy="1280" rx="70" ry="50" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'); text('uterus', 780, 1360, 'nf-l2', 'middle')
add('<path d="M760 260 L830 310" style="stroke:var(--ink-2);stroke-width:8"/>'); text('central line', 750, 250, 'nf-l2', 'end')
add('<circle cx="1220" cy="860" r="22" style="fill:var(--bad);opacity:.85"/>', when=D('mural'))
add('<path d="M1000 860 H1200" style="stroke:var(--bad);stroke-width:6;stroke-dasharray:8 6"/>', when=['pfo'])
text('PFO', 1100, 845, 'nf-l1', 'middle', when=['pfo'])
# lodged emboli
for x, y, w in ((920, 470, D('dvt', 'fat', 'air', 'afe')), (1600, 300, D('fat', 'mural', 'dcs') + ['dx:dvt&pfo']), (1940, 720, D('fat')),
                (1730, 1020, D('mural')), (1500, 1550, D('mural')), (1900, 1450, D('dcs')), (1300, 460, D('dcs'))):
    add(f'<circle cx="{x}" cy="{y}" r="26" style="fill:var(--bad);fill-opacity:.6;stroke:var(--bad);stroke-width:4"/>', when=w)
TAG = dict(dvt='DVT → PE: ventilated, not perfused — dead space', fat='fat: 1–3 days after a long-bone fracture — hypoxemia, confusion, petechiae',
           air='air entering at central line placement', dcs='diver ascends too fast — nitrogen bubbles: bends, chokes, neurologic',
           afe='amniotic fluid in labor or postpartum → dyspnea, shock, DIC', mural='left atrial thrombus (AF) → systemic arterial emboli')
for k, s in TAG.items(): text(s, 1100, 1700, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('paradoxical: a venous clot crosses into the left heart → brain', 1100, 1740, 'nf-l1', 'middle', when=['dx:dvt&pfo'])

# ════════ motion ════════
flows = [dict(d=PX[k], len=900, speed=120, r=11, base={k: 3}, when=D(k)) for k in ('dvt', 'fat', 'afe', 'air')]
flows += [
  dict(d=PA, len=800, speed=120, r=11, base=dict(dvt=3), when=D('dvt')),
  dict(d=PA, len=800, speed=120, r=11, base=dict(fat=3), when=D('fat')),
  dict(d=PA, len=800, speed=120, r=11, base=dict(afe=3), when=D('afe')),
  dict(d=PA, len=800, speed=120, r=11, base=dict(air=3), when=D('air')),
  dict(d=PV + ' ' + BRAIN.replace('M1200 880', 'L1200 880'), len=1400, speed=120, r=9, base=dict(fat=2), when=D('fat')),
  dict(d=SKIN, len=750, speed=120, r=9, base=dict(fat=2), when=D('fat')),
  dict(d=BRAIN, len=900, speed=120, r=11, base=dict(mur=3), when=D('mural')),
  dict(d=KID, len=520, speed=120, r=11, base=dict(mur=2), when=D('mural')),
  dict(d=LEG, len=650, speed=120, r=11, base=dict(mur=2), when=D('mural')),
  dict(d=PFO, len=1100, speed=120, r=11, base=dict(dvt=3), when=['dx:dvt&pfo']),
  dict(d='M1840 1500 C1860 1460 1880 1420 1900 1400', len=120, speed=40, r=9, base=dict(air=3), when=D('dcs')),
  dict(d='M1250 520 C1270 500 1290 480 1310 460', len=90, speed=40, r=9, base=dict(air=3), when=D('dcs')),
  dict(d='M1560 340 C1580 320 1600 310 1620 290', len=90, speed=40, r=9, base=dict(air=3), when=D('dcs')),
]
flows.append(dict(d='M1000 1200 V880 ' + PA[PA.index('V1040'):], len=1000, speed=100, r=7, base=dict(blood=3), unless=['dx:*']))
sites = [dict(x=560, y=1560, n=[-1, 0], w=10, t='rec', l='', aria='DVT', c='dvt', ions=[]),
         dict(x=880, y=560, n=[-1, 1], w=10, t='rec', l='', aria='Pulmonary embolism', c='pe', ions=[]),
         dict(x=420, y=1330, n=[-1, 0], w=10, t='rec', l='', aria='Fat embolism', c='fatemb', ions=[]),
         dict(x=1960, y=1400, n=[1, 0], w=10, t='rec', l='', aria='Air embolism', c='airemb', ions=[]),
         dict(x=700, y=1260, n=[-1, 0], w=10, t='rec', l='', aria='Amniotic fluid embolism', c='afe', ions=[]),
         dict(x=1270, y=820, n=[1, -1], w=10, t='rec', l='', aria='Embolus types', c='emboli', ions=[])]

readouts = [
  dict(l='Dead space (lung)', mods=[dict(when=D('dvt', 'fat', 'air', 'afe'), d=1)]),
  dict(l='Hypoxemia', mods=[dict(when=D('dvt', 'fat', 'air', 'afe', 'dcs'), d=1)]),
  dict(l='Brain emboli', mods=[dict(when=D('fat', 'mural', 'dcs') + ['dx:dvt&pfo'], d=1)]),
  dict(l='Petechial rash', mods=[dict(when=D('fat'), d=1)]),
  dict(l='DIC', mods=[dict(when=D('afe'), d=1)]),
]

notes = {
  '': 'An embolus is material carried in the blood from where it formed to where it lodges — most are thrombi. Venous emboli stop '
      'in the lungs; left-heart emboli go to the brain, kidneys and legs. FAT BAT: fat, air, thrombus, bacteria, amniotic fluid, tumor.',
  'dx:dvt': 'DVT → PE: most PEs come from proximal deep leg veins (iliac, femoral, popliteal) — Virchow triad of stasis, '
            'hypercoagulability, endothelial damage. The lung beyond is ventilated but not perfused. Sudden dyspnea, pleuritic '
            'pain, tachycardia; CT pulmonary angiography; anticoagulate.',
  'dx:fat': 'Fat embolism: marrow fat after a long-bone fracture (or liposuction) lodges in the small vessels of the lungs, brain '
            'and skin, 1–3 days later — hypoxemia, neurologic changes, petechial rash; free fatty acids injure endothelium.',
  'dx:air': 'Iatrogenic air embolism: air enters during central line placement or other procedures.',
  'dx:dcs': 'Decompression sickness: nitrogen dissolved at depth comes out of solution on fast ascent — the bends (joints, '
            'muscles), the chokes (breathing), neurologic signs; chronic caisson disease infarcts bone (femoral heads). '
            'Hyperbaric O₂.',
  'dx:afe': 'Amniotic fluid embolism: fluid and fetal cells enter the maternal circulation in labor or postpartum — sudden '
            'dyspnea, cyanosis, shock, seizures, coma, then DIC. Fetal squames and lanugo in the maternal lungs. High mortality.',
  'dx:mural': 'About 80% of systemic arterial emboli start as intracardiac mural thrombi — after LV infarcts or with left atrial '
              'dilation and fibrillation.',
  'pfo': 'Paradoxical embolism: a venous embolus crosses an ASD, VSD or patent foramen ovale into the systemic circulation.',
}

dyn = dict(
  kinds=dict(dvt=['mov', '--bad'], fat=['mov', '--dk9'], air=['mov', '--ink-3'], afe=['mov', '--dk10'], mur=['mov', '--bad'],
             blood=['mov', '--nf-h2o']),
  groups=[['mov', 'Emboli · blood']],
  switches=[dict(id='dx', label='Embolus', type='one', options=[
              ['dvt', 'Thrombus (DVT → PE)', 'pe'], ['fat', 'Fat', 'fatemb'], ['air', 'Air (central line)', 'airemb'],
              ['dcs', 'Decompression bubbles', 'airemb'], ['afe', 'Amniotic fluid', 'afe'], ['mural', 'Left atrial thrombus', 'emboli']]),
            dict(id='pfo', label='Heart', type='toggle', on='PFO open', off='Open a PFO', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 4')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='embolsim', title='Emboli in Motion', topic='path', after='thromboemb',
  sub='Launch a thrombus, fat, air, nitrogen bubbles, amniotic fluid or a left-atrial clot and follow it to where it lodges — '
      'then open a PFO and watch a leg clot reach the brain',
  w=3600, h=2000,
  fa='284, 321, 691',
  src=['Robbins ch 4 — Hemodynamic disorders, thromboembolic disease, and shock',
       'Guyton ch 45 — Physiology of Deep-Sea Diving and Other Hyperbaric Conditions'],
  lanes=[('emVen', 'Venous → lung', 'glycolysis'), ('emArt', 'Arterial & paradoxical', 'tca')],
  nodes=[
    ('em1', 'Embolus types', 330, 1840, 'emArt', 'FAT BAT', ['emboli'], 'hub'),
    ('em2', 'Deep venous thrombosis', 760, 1840, 'emVen', 'Virchow triad', ['dvt']),
    ('em3', 'Pulmonary embolism', 1200, 1840, 'emVen', 'dead space', ['pe']),
    ('em4', 'Fat embolism syndrome', 1640, 1840, 'emVen', 'fracture · petechiae', ['fatemb']),
    ('em5', 'Air & decompression', 2080, 1840, 'emVen', 'bends · chokes', ['airemb']),
    ('em6', 'Amniotic fluid embolism', 2520, 1840, 'emVen', 'labor · DIC', ['afe'])],
  panels=[
    (2500, PANY, 1000, 'FAT BAT (Robbins ch 4)', [
      ('Fat', 'long-bone fracture, liposuction'), ('Air', 'divers, central lines'), ('Thrombus', 'deep leg veins; LA in AF'),
      ('Bacteria', 'infected vegetations'), ('Amniotic fluid', 'labor → DIC'), ('Tumor', 'blood or lymph')])],
  dyn=dyn)
