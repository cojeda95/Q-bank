# The Aorta in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Heart → ascending aorta → arch (brachiocephalic, left carotid, left subclavian with the vertebral to the brain) →
# descending thoracic → diaphragm → renal arteries → infrarenal abdominal aorta → iliacs and legs, with blood moving, and an
# artery-wall inset where a `steps` switch (auto) builds a plaque: endothelial dysfunction → foam cells → fatty streak →
# fibrous plaque → complicated atheroma. A `one` switch shows AAA, thoracic aneurysm, dissection type A and B, subclavian
# steal, peripheral artery disease, cholesterol emboli and Mönckeberg. 5 readouts. Facts from the pinned cards; FA pages
# in `fa`. No new cards.
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

O = lambda *k: [f'dx:{x}' for x in k]
PL = lambda *k: [f'pl:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def box(x0, y0, x1, y1, lab):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="20" class="dyn-cell"/>'); text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')
VS = 'fill:none;stroke:var(--nf-blood);stroke-linecap:round;stroke-linejoin:round;opacity:.35'

text('The aorta — branches, aneurysms, dissection, steal and plaque', 180, 150, 'dyn-big')
text('schematic, front view · the patient’s left is on the right', 180, 176, 'dyn-cap')

# ════════ the aorta ════════
AO = 'M650 670 V520 C650 420 760 400 850 400 C960 400 1050 440 1050 540 V1500'
box(650, 250, 1150, 320, 'Brain'); box(300, 430, 480, 490, 'Right arm'); box(1300, 430, 1480, 490, 'Left arm')
add('<circle cx="650" cy="760" r="90" class="dyn-cell"/>'); text('Heart', 650, 766, 'nf-l1', 'middle')
add(f'<path d="{AO}" style="{VS};stroke-width:46"/>')
add(f'<path d="M1050 1500 L950 1640 M1050 1500 L1150 1640" style="{VS};stroke-width:26"/>')
text('legs', 1050, 1690, 'nf-l1', 'middle')
BR = dict(rsub='M720 410 V360 C650 360 560 390 480 455', rcar='M720 360 V320', lcar='M850 400 V320',
          lsub='M960 405 V380 C1100 380 1200 400 1300 455', lvert='M1080 384 V320')
for d in BR.values(): add(f'<path d="{d}" style="{VS};stroke-width:16"/>')
text('vertebral', 1100, 350, 'nf-l2')
add('<path d="M800 1000 H1300" style="stroke:var(--ink-3);stroke-width:3;stroke-dasharray:10 8"/>'); text('diaphragm', 1310, 1006, 'nf-l2')
add(f'<path d="M1050 1140 H1200 M1050 1140 H900" style="{VS};stroke-width:16"/>')
box(1200, 1110, 1340, 1170, 'Kidney'); box(760, 1110, 900, 1170, 'Kidney')
text('ascending', 610, 600, 'nf-l2', 'end'); text('descending thoracic', 1080, 800, 'nf-l2'); text('infrarenal', 1080, 1300, 'nf-l2')

# lesions on the aorta
add('<ellipse cx="1050" cy="1330" rx="80" ry="110" style="fill:var(--nf-blood);fill-opacity:.25;stroke:var(--bad);stroke-width:5"/>', when=O('aaa'))
text('infrarenal aneurysm — pulsatile mass', 1150, 1260, 'nf-l1 dyn-tag', when=O('aaa'))
add('<ellipse cx="650" cy="560" rx="70" ry="90" style="fill:var(--nf-blood);fill-opacity:.25;stroke:var(--bad);stroke-width:5"/>', when=O('taa'))
text('root dilation → aortic regurgitation', 540, 610, 'nf-l1 dyn-tag', 'end', when=O('taa'))
DA = 'M664 670 V520 C664 432 766 414 850 414 C950 414 1036 450 1036 540 V1400'
DB = 'M1036 560 V1400'
add(f'<path d="{DA}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=O('dissa'))
add(f'<path d="{DB}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=O('dissb'))
text('Stanford A: ascending — surgery; AR, tamponade', 540, 610, 'nf-l1 dyn-tag', 'end', when=O('dissa'))
text('Stanford B: descending only — β-blockers', 1150, 1260, 'nf-l1 dyn-tag', when=O('dissb'))
add(X(1000, 395, 14), when=O('steal'))
text('subclavian stenosis before the vertebral', 1150, 230, 'nf-l1 dyn-tag', 'middle', when=O('steal'))
add(X(1000, 1570, 14) + X(1100, 1570, 14), when=O('pad'))
text('claudication · Leriche: buttock pain, impotence', 1180, 1540, 'nf-l1 dyn-tag', when=O('pad'))
text('crystals shower downstream: blue toes, AKI — pulses intact', 1180, 1540, 'nf-l1 dyn-tag', when=O('chol'))

# ════════ the artery wall, close up ════════
IX0, IX1, IY = 1550, 2380, 560
add(f'<rect x="{IX0}" y="{IY - 220}" width="{IX1 - IX0}" height="440" rx="24" class="dyn-soft"/>')
text('artery wall, close up', IX0 + 20, IY - 186, 'nf-l1')
add(f'<rect x="{IX0 + 20}" y="{IY - 150}" width="{IX1 - IX0 - 40}" height="120" style="fill:var(--nf-blood);fill-opacity:.12"/>')
text('lumen', IX0 + 40, IY - 120, 'nf-l2')
add(f'<path d="M{IX0 + 20} {IY - 30} H{IX1 - 20}" style="stroke:var(--dk2);stroke-width:6"/>')
text('intima', IX0 + 40, IY + 4, 'nf-l2')
add(f'<rect x="{IX0 + 20}" y="{IY + 30}" width="{IX1 - IX0 - 40}" height="90" style="fill:var(--dk7);fill-opacity:.15"/>')
text('media', IX0 + 40, IY + 84, 'nf-l2')
add(f'<rect x="{IX0 + 20}" y="{IY + 30}" width="{IX1 - IX0 - 40}" height="90" style="fill:var(--ink-3);fill-opacity:.45"/>', when=O('monck'))
text('media calcified — lumen spared', 1965, IY + 160, 'nf-l1 dyn-tag', 'middle', when=O('monck'))
PX = 1965
add(f'<path d="M{PX - 160} {IY - 30} Q{PX} {IY - 70} {PX + 160} {IY - 30}" style="fill:var(--dk10);fill-opacity:.55;stroke:var(--dk10);stroke-width:2"/>', when=PL('streak'))
add(f'<path d="M{PX - 200} {IY - 30} Q{PX} {IY - 130} {PX + 200} {IY - 30}" style="fill:var(--dk10);fill-opacity:.6;stroke:var(--ink-2);stroke-width:6"/>', when=PL('fibrous', 'complex'))
add(f'<path d="M{PX - 60} {IY - 80} l30 -20 l30 20" style="fill:none;stroke:var(--bad);stroke-width:6"/><ellipse cx="{PX + 20}" cy="{IY - 110}" rx="60" ry="22" style="fill:var(--bad);fill-opacity:.6"/>', when=PL('complex'))
STG = dict(dys='endothelial dysfunction — LDL and macrophages enter the intima', streak='foam cells → fatty streak',
           fibrous='smooth muscle migrates (PDGF, FGF) → fibrous plaque', complex='complicated atheroma — calcification, thrombus')
for k, t in STG.items(): text(t, 1965, IY + 190, 'nf-l1', 'middle', when=PL(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=AO, len=1500, speed=200, r=9, base=dict(b=5), mods=[m(O('aaa', 'dissb', 'dissa'), speed=0.6)]),
  dict(d='M1050 1500 L950 1640', len=170, speed=120, r=8, base=dict(b=2), mods=[m(O('pad'), set=dict(b=0))]),
  dict(d='M1050 1500 L1150 1640', len=170, speed=120, r=8, base=dict(b=2), mods=[m(O('pad'), set=dict(b=0))]),
  dict(d=BR['rsub'], len=290, speed=110, r=8, base=dict(b=2)),
  dict(d=BR['rcar'] + ' V300', len=60, speed=50, r=8, base=dict(b=1)),
  dict(d=BR['lcar'], len=80, speed=60, r=8, base=dict(b=2)),
  dict(d=BR['lsub'], len=380, speed=120, r=8, base=dict(b=2), mods=[m(O('steal'), set=dict(b=0))]),
  dict(d=BR['lvert'], len=64, speed=50, r=8, base=dict(b=1), unless=O('steal')),
  dict(d='M1080 320 V384 C1150 390 1230 410 1300 455', len=300, speed=110, r=8, base=dict(b=3), when=O('steal')),
  dict(d='M1050 1140 H1200', len=150, speed=80, r=8, base=dict(b=2), mods=[m(O('chol'), set=dict(cr=3, b=1))]),
  dict(d='M1050 1500 L1150 1640', len=170, speed=110, r=7, base=dict(cr=3), when=O('chol')),
  dict(d=DA, len=1400, speed=140, r=7, base=dict(fl=3), when=O('dissa')),
  dict(d=DB, len=840, speed=140, r=7, base=dict(fl=3), when=O('dissb')),
  dict(d=f'M{IX0 + 40} {IY - 90} H{IX1 - 40}', len=800, speed=160, r=8, base=dict(b=3)),
  dict(d=f'M{PX - 100} {IY - 120} L{PX - 40} {IY - 20}', len=120, speed=40, r=7, base=dict(ldl=2), when=PL('dys', 'streak')),
]
sites = [dict(x=1050, y=1200, n=[1, 0], w=10, t='rec', l='', aria='Abdominal aortic aneurysm', c='aaa', ions=[]),
         dict(x=IX1 - 60, y=IY - 186, n=[0, 1], w=10, t='rec', l='', aria='Atherosclerosis', c='athero', ions=[])]

readouts = [
  dict(l='Arm BP difference', mods=[dict(when=O('dissa', 'steal'), d=1)]),
  dict(l='Brain flow', mods=[dict(when=O('steal'), d=-1)]),
  dict(l='Leg flow', mods=[dict(when=O('pad'), d=-1), dict(when=O('chol'), d=0)]),
  dict(l='Kidney function', mods=[dict(when=O('chol'), d=-1)]),
  dict(l='Aortic regurgitation', mods=[dict(when=O('taa', 'dissa'), d=1)]),
]

notes = {
  '': 'Atherosclerosis hits elastic and large and medium muscular arteries: abdominal aorta > coronary > popliteal > carotid > circle of '
      'Willis. Its complications include aneurysm, peripheral vascular disease, embolism and subclavian steal.',
  'pl:dys': 'Endothelial dysfunction: LDL and macrophages accumulate in the intima.',
  'pl:streak': 'Macrophages fill with lipid — foam cells — and form a fatty streak.',
  'pl:fibrous': 'Smooth muscle migrates in (PDGF, FGF), proliferates and lays down matrix — a fibrous plaque.',
  'pl:complex': 'Complicated atheroma: calcification (calcium content tracks complication risk), rupture and thrombosis.',
  'dx:aaa': 'Abdominal aortic aneurysm: transmural inflammation and matrix breakdown, usually infrarenal where the vasa vasorum is '
            'sparse — older male smoker, pulsatile mass; rupture: pulsatile mass + abdominal/back pain + hypotension. No abdominal OMT.',
  'dx:taa': 'Thoracic aortic aneurysm: cystic medial degeneration (hypertension, bicuspid valve, Marfan) or tertiary syphilis '
            '(vasa vasorum endarteritis) — root dilation causes aortic regurgitation.',
  'dx:dissa': 'Dissection, Stanford A: an intimal tear lets blood into the media and track along a false lumen through the ascending '
              'aorta — tearing chest pain to the back, unequal arm pressures, widened mediastinum; acute AR or tamponade. Surgery.',
  'dx:dissb': 'Dissection, Stanford B: descending aorta only, below the left subclavian — β-blockers, then vasodilators.',
  'dx:steal': 'Subclavian steal: the subclavian is narrowed before the vertebral, so the exercising arm pulls blood backward down the '
              'vertebral artery from the brain — arm pain, dizziness, vertigo, >15 mm Hg arm BP difference.',
  'dx:pad': 'Peripheral artery disease: atherosclerotic narrowing limits leg flow — claudication relieved by rest; Leriche (aortoiliac): '
            'buttock pain, impotence, weak femoral pulses. Cilostazol.',
  'dx:chol': 'Cholesterol emboli: after angiography or a graft, crystals shower from aortic plaque into small arteries — livedo, blue '
             'toes, AKI, stroke, gut ischemia — with palpable pulses.',
  'dx:monck': 'Mönckeberg medial calcific sclerosis: the media of muscular arteries calcifies but the lumen stays open — usually '
              'insignificant (over 50, renal insufficiency).',
}

dyn = dict(
  kinds=dict(b=['blood', '--nf-blood'], fl=['blood', '--bad'], cr=['emb', '--dk3'], ldl=['emb', '--dk3']),
  groups=[['blood', 'Blood'], ['emb', 'Lipid · crystals']],
  switches=[dict(id='pl', label='Plaque', type='steps', auto=4, options=[
              ['dys', 'Endothelial dysfunction'], ['streak', 'Fatty streak'], ['fibrous', 'Fibrous plaque'], ['complex', 'Complicated']]),
            dict(id='dx', label='Aorta and branches', type='one', options=[
              ['aaa', 'Abdominal aneurysm', 'aaa'], ['taa', 'Thoracic aneurysm', 'taa'], ['dissa', 'Dissection — Stanford A', 'dissection'],
              ['dissb', 'Dissection — Stanford B', 'dissection'], ['steal', 'Subclavian steal', 'subclavsteal'],
              ['pad', 'Peripheral artery disease', 'pad'], ['chol', 'Cholesterol emboli', 'cholemb'], ['monck', 'Mönckeberg', 'monckeberg']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 305–307 · Robbins ch 11')

MAP = dict(
  id='aortasim', title='The Aorta in Motion', topic='cardio', after='vasc',
  sub='Blood down the aorta and its branches, a plaque building step by step, and what goes wrong — abdominal and thoracic aneurysms, '
      'dissection A and B, subclavian steal, peripheral artery disease, cholesterol emboli and Mönckeberg',
  w=3600, h=1900,
  fa='305, 306, 307',
  src=['Robbins ch 11 — Blood vessels', 'Moore ch 5 — Abdomen', 'OCOM OMM — OMS2 written midterm study guide',
       'OCOM OMM — Week 4 lab rubric: visceral manipulation', 'Robbins ch 12 — The heart',
       'Katzung ch 12 — Vasodilators & the Treatment of Angina Pectoris & Coronary Syndromes', 'Robbins ch 20 — The kidney',
       'Moore ch 4 — Thorax', 'Bootcamp.com Cardiology — Stable angina and atherosclerosis'],
  lanes=[('aoPlq', 'Plaque', 'glycolysis'), ('aoWall', 'Aneurysm & dissection', 'tca'), ('aoFlow', 'Flow problems', 'gluconeo')],
  nodes=[
    ('ao1', 'Atherosclerosis', 330, 1760, 'aoPlq', 'streak → plaque → atheroma', ['athero'], 'hub'),
    ('ao2', 'Mönckeberg', 760, 1760, 'aoPlq', 'media, lumen spared', ['monckeberg']),
    ('ao3', 'Abdominal aortic aneurysm', 1500, 1760, 'aoWall', 'pulsatile mass', ['aaa']),
    ('ao4', 'Thoracic aortic aneurysm', 1940, 1760, 'aoWall', 'cystic medial degeneration', ['taa']),
    ('ao5', 'Aortic dissection', 2380, 1760, 'aoWall', 'tearing pain to the back', ['dissection']),
    ('ao6', 'Subclavian steal', 1500, 1620, 'aoFlow', 'dizzy using the arm', ['subclavsteal']),
    ('ao7', 'Peripheral artery disease', 1940, 1620, 'aoFlow', 'claudication', ['pad']),
    ('ao8', 'Cholesterol emboli', 2380, 1620, 'aoFlow', 'blue toes, AKI', ['cholemb'])],
  panels=[
    (2500, PANY, 1000, 'Three kinds of arteriosclerosis (First Aid p. 305)', [
      ('Atherosclerosis', 'intima — elastic + large/medium arteries'),
      ('Mönckeberg', 'media calcified, lumen open'),
      ('Arteriolosclerosis', 'hyaline (HTN, DM) · hyperplastic (onion-skin)')])],
  dyn=dyn)
