# CSF Flow in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A sagittal sketch of the brain and spinal canal: choroid plexus → lateral ventricles → foramina of Monro → third
# ventricle → cerebral aqueduct → fourth ventricle → foramina of Luschka and Magendie → subarachnoid space, over the
# convexity to the arachnoid granulations in the superior sagittal sinus, and down around the cord to the lumbar cistern
# (the cord ends at the conus, L1–L2; the cauda equina below; LP at L3–L4 or L4–L5). One `one` switch blocks a site —
# everything upstream dilates, everything downstream stays small — or shows the look-alikes (NPH, ex vacuo, IIH, choroid
# plexus papilloma) and the lesions low in the canal (syrinx with Chiari I, conus medullaris, cauda equina). 5 readouts.
# Facts from the pinned cards (csfflow, ventwalls, hydroceph, nph, iih, chiari, syringomyelia, caudaequina, lpcsf, ntd);
# FA pages in `fa`. No new cards.
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


SW = 'blk'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 800
LAT_BIG = ['monro', 'aque', 'dw', 'comm', 'nph', 'exvac', 'cpp']
THIRD_BIG = ['aque', 'dw', 'comm', 'nph', 'exvac', 'cpp']
FOURTH_BIG = ['dw', 'comm', 'nph', 'exvac', 'cpp']
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'

text('CSF — made in the ventricles, absorbed into the venous sinus', 1540, 330, 'dyn-big')
text('a block dilates everything upstream of it;', 1540, 358, 'dyn-cap')
text('scarred granulations dilate every ventricle', 1540, 382, 'dyn-cap')

# ════════ the head ════════
BX, BY = 820, 560
add(f'<ellipse cx="{BX}" cy="{BY}" rx="660" ry="400" style="fill:none;stroke:var(--nf-h2o);stroke-width:3;stroke-dasharray:10 8"/>')
add(f'<ellipse cx="{BX}" cy="{BY}" rx="620" ry="360" class="dyn-soft"/>')
text('subarachnoid space', BX - 560, BY + 330, 'nf-l2', 'end')
# superior sagittal sinus + granulations
add(f'<path d="M{BX - 420} 196 Q{BX} 120 {BX + 420} 196" style="fill:none;stroke:var(--dk1);stroke-width:22;stroke-linecap:round;opacity:.7"/>')
for dx in (-240, -80, 80, 240):
    add(f'<circle cx="{BX + dx}" cy="{168 if abs(dx) < 100 else 180}" r="12" style="fill:var(--nf-h2o);opacity:.8"/>')
text('superior sagittal sinus', BX + 440, 190, 'nf-l1')
text('arachnoid granulations — one-way into venous blood', BX + 440, 214, 'nf-l2')
add(X(BX - 80, 168, 22) + X(BX + 80, 168, 22), when=O('comm'))
text('scarred after meningitis — CSF can’t get out', BX, 248, 'nf-l1 dyn-tag', 'middle', when=O('comm'))
# cerebellum
add('<path d="M980 760 Q1150 700 1290 800 Q1300 900 1140 930 Q1000 930 960 860 Z" style="fill:var(--dk4);fill-opacity:.18;stroke:var(--dk4);stroke-width:2"/>')
text('cerebellum', 1140, 884, 'nf-l2', 'middle')
# ventricles
LAT = 'M560 420 C700 320 1000 320 1120 420 C1150 480 1080 520 1000 480 C900 440 760 440 680 500 C620 540 560 500 560 420 Z'
add(f'<path d="{LAT}" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--nf-h2o);stroke-width:3"/>', unless=O(*LAT_BIG))
add(f'<path d="{LAT}" transform="translate(850 440) scale(1.4) translate(-850 -440)" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=O(*LAT_BIG))
text('lateral ventricles', 700, 380, 'nf-l1', 'middle')
add('<rect x="834" y="520" width="34" height="120" rx="12" style="fill:var(--nf-h2o);fill-opacity:.4;stroke:var(--nf-h2o);stroke-width:3"/>', unless=O(*THIRD_BIG))
add('<rect x="805" y="505" width="92" height="150" rx="24" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=O(*THIRD_BIG))
text('third', 760, 600, 'nf-l2', 'end')
add('<path d="M866 640 L930 730" style="stroke:var(--nf-h2o);stroke-width:7"/>')
text('aqueduct', 880, 700, 'nf-l2', 'end')
add('<path d="M925 735 L1000 790 L935 830 Z" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:3"/>', unless=O(*FOURTH_BIG))
add('<path d="M900 715 L1060 800 L910 880 Z" style="fill:var(--nf-h2o);fill-opacity:.5;stroke:var(--bad);stroke-width:4"/>', when=O(*FOURTH_BIG))
text('fourth', 1010, 760, 'nf-l2')
# the only exits: Magendie (midline, one) and Luschka (lateral, paired) — drawn schematically
# UNVERIFIED: midline/lateral is from the neuro question explanations (SDL 08), not the csfflow card, which names only the foramina
add('<path d="M942 822 L962 892" style="fill:none;stroke:var(--nf-h2o);stroke-width:10;stroke-linecap:round"/>')
add('<path d="M996 786 L1072 768 M996 792 L1072 812" style="fill:none;stroke:var(--nf-h2o);stroke-width:8;stroke-linecap:round"/>')
text('Magendie — midline', 930, 905, 'nf-l2', 'end')
text('Luschka ×2 — lateral', 1080, 842, 'nf-l2')
# choroid plexus
for (x, y) in ((900, 400), (950, 790)):
    add(f'<path d="M{x - 30} {y} q10 -14 20 0 q10 14 20 0 q10 -14 20 0" style="fill:none;stroke:var(--dk5);stroke-width:5"/>')
text('choroid plexus', 960, 360, 'nf-l2')
add('<circle cx="900" cy="400" r="34" style="fill:var(--dk5);fill-opacity:.4;stroke:var(--dk5);stroke-width:3"/>', when=O('cpp'))
# block marks
add(X(800, 490), when=O('monro')); text('colloid cyst at the foramen of Monro', 560, 300, 'nf-l1 dyn-tag', 'middle', when=O('monro'))
add(X(898, 686), when=O('aque')); text('aqueductal stenosis', 600, 720, 'nf-l1 dyn-tag', 'end', when=O('aque'))
add(X(955, 862, 14) + X(1060, 772, 12) + X(1060, 810, 12), when=O('dw')); text('fourth-ventricle outlet — Dandy-Walker cyst', 1280, 960, 'nf-l1 dyn-tag', 'middle', when=O('dw'))
text('brain atrophy — ventricles fill the space', BX, BY + 300, 'nf-l1 dyn-tag', 'middle', when=O('exvac'))
text('ventricles normal — pressure high', BX, BY + 300, 'nf-l1 dyn-tag', 'middle', when=O('iih'))
text('too much CSF made', 960, 320, 'nf-l1 dyn-tag', 'middle', when=O('cpp'))

# ════════ the spinal canal ════════
SX = 960
LV = dict(fm=960, c7=1140, t12=1440, conus=1530, l3=1640, l5=1760, s2=1860)
add(f'<rect x="{SX - 70}" y="{LV["fm"]}" width="140" height="{LV["s2"] - LV["fm"]}" rx="50" style="fill:none;stroke:var(--nf-h2o);stroke-width:3;stroke-dasharray:10 8"/>')
add(f'<path d="M{SX - 26} {LV["fm"]} V{LV["conus"] - 40} Q{SX} {LV["conus"] + 20} {SX + 26} {LV["conus"] - 40} V{LV["fm"]} Z" class="dyn-cell"/>')
for i in range(-3, 4):
    add(f'<path d="M{SX + i * 6} {LV["conus"]} Q{SX + i * 16} {LV["l5"]} {SX + i * 20} {LV["s2"] - 20}" style="fill:none;stroke:var(--dk9);stroke-width:2"/>')
for k, lab in (('fm', 'foramen magnum'), ('c7', 'C7'), ('t12', 'T12'), ('conus', 'L1–L2 · conus medullaris'), ('l3', 'L3–L4'), ('l5', 'L5'), ('s2', 'S2 · end of the dural sac')):
    text(lab, SX - 100, LV[k] + 5, 'nf-l2', 'end')
text('cauda equina', SX + 100, LV['l3'], 'nf-l1')
text('lumbar cistern — LP here', SX + 100, LV['l3'] + 26, 'nf-l2')
add(f'<path d="M{SX + 260} {LV["l3"] + 60} L{SX + 40} {LV["l3"] + 40}" style="stroke:var(--ink-2);stroke-width:5"/>')
# syrinx (Chiari I)
add(f'<ellipse cx="{SX}" cy="{LV["c7"]}" rx="12" ry="120" style="fill:var(--nf-h2o);stroke:var(--bad);stroke-width:3"/>', when=O('syr'))
add('<path d="M960 900 L940 990 L980 990 Z" style="fill:var(--dk4);fill-opacity:.6"/>', when=O('syr'))
text('Chiari I tonsils + syrinx (C2–T9)', SX + 100, LV['c7'], 'nf-l1 dyn-tag', when=O('syr'))
# conus / cauda lesions
add(f'<ellipse cx="{SX}" cy="{LV["conus"]}" rx="70" ry="40" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:3"/>', when=O('conus'))
text('conus medullaris — symmetric weakness, UMN signs', SX + 100, LV['conus'] - 30, 'nf-l1 dyn-tag', when=O('conus'))
add(f'<ellipse cx="{SX - 40}" cy="{LV["l5"] - 40}" rx="60" ry="50" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/>', when=O('cauda'))
text('central disc compresses the roots — LMN, saddle anesthesia', SX + 100, LV['l5'], 'nf-l1 dyn-tag', when=O('cauda'))

# ════════ the clue box ════════
box(1500, 1040, 2340, 1900)
text('What dilates, what to expect', 1530, 1080, 'dyn-big')
CL = dict(
  monro=('Noncommunicating — at the foramen of Monro', 'the lateral ventricles balloon; third and fourth stay small'),
  aque=('Noncommunicating — aqueductal stenosis', 'lateral + third ventricles dilate; the fourth stays small'),
  dw=('Noncommunicating — Dandy-Walker', 'absent vermis, cystic fourth ventricle, hydrocephalus'),
  comm=('Communicating — granulations scarred', 'every ventricle dilates · ↑ ICP, papilledema, herniation'),
  nph=('Normal pressure hydrocephalus', 'ventricles big, pressure only episodic · wobbly, wacky, wet'),
  exvac=('Ex vacuo ventriculomegaly', 'atrophy — normal ICP, no triad (Alzheimer, HIV, FTD, Huntington)'),
  iih=('Idiopathic intracranial hypertension', 'normal ventricles, high opening pressure, papilledema, CN VI'),
  cpp=('Choroid plexus papilloma', 'too much CSF → raised pressure; mostly children, 4th ventricle'),
  syr=('Chiari I with syringomyelia', 'cape-like loss of pain and temperature; anterior horn signs later'),
  conus=('Conus medullaris syndrome', 'symmetric leg weakness with UMN signs (cauda equina card)'),
  cauda=('Cauda equina syndrome', 'saddle anesthesia, bladder and bowel, asymmetric LMN weakness, absent ankle jerks'),
)
for k, (a, b) in CL.items():
    text(a, 1530, 1130, 'nf-l1', when=O(k))
    cut = b.rfind(' ', 0, 52) if len(b) > 52 else len(b)
    text(b[:cut], 1530, 1160, 'nf-l2', when=O(k)); 
    if cut < len(b): text(b[cut + 1:], 1530, 1184, 'nf-l2', when=O(k))
text('pick a block or a lesion', 1530, 1130, 'nf-l1', unless=[f'{SW}:*'])
text('CSF: 120–140 mL in the adult, 400–500 mL made a day', 1530, 1260, 'nf-l2')
text('LP opening pressure 80–180 mm H₂O', 1530, 1290, 'nf-l2')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
UP_MONRO = O('monro'); UP_AQ = O('monro', 'aque'); UP_4 = O('monro', 'aque', 'dw')
flows = [
  dict(d='M900 400 C860 440 830 470 840 520', len=140, speed=60, r=7, base=dict(c=3), mods=[m(UP_MONRO, set=dict(c=0)), m(O('cpp'), set=dict(c=6))]),
  dict(d='M851 530 V640 L930 730', len=230, speed=70, r=7, base=dict(c=3), mods=[m(UP_AQ, set=dict(c=0))]),
  dict(d='M945 800 L962 892 C1100 930 1250 900 1380 700 C1460 520 1400 300 1240 210', len=1000, speed=110, r=7, base=dict(c=5),
       mods=[m(UP_4, set=dict(c=0)), m(O('comm'), speed=0.3)]),
  dict(d='M985 790 H1072 C1220 770 1340 760 1380 700 C1460 520 1400 300 1240 210', len=980, speed=110, r=7, base=dict(c=4),
       mods=[m(UP_4, set=dict(c=0)), m(O('comm'), speed=0.3)]),
  dict(d='M1240 210 Q1000 140 900 168', len=360, speed=80, r=7, base=dict(c=3), mods=[m(UP_4 + O('comm'), set=dict(c=0))]),
  dict(d=f'M{SX + 50} 980 V{LV["s2"] - 30}', len=870, speed=110, r=7, base=dict(c=5), mods=[m(UP_4, set=dict(c=0))]),
]
sites = [
  dict(x=SX, y=LV['conus'], n=[1, 0], w=40, t='rec', l='', aria='Conus medullaris / cauda equina', c='caudaequina', ions=[]),
  dict(x=840, y=520, n=[-1, 0], w=30, t='md', l='', aria='CSF flow', c='csfflow', ions=[]),
  dict(x=SX + 260, y=LV['l3'] + 60, n=[1, 0], w=10, t='rec', l='', aria='Lumbar puncture', c='lpcsf', ions=[]),
]

readouts = [
  dict(l='Intracranial pressure', mods=[dict(when=O('monro', 'aque', 'dw', 'comm', 'cpp', 'iih'), d=1), dict(when=O('nph', 'exvac'), d=0)]),
  dict(l='Lateral ventricle size', mods=[dict(when=O(*LAT_BIG), d=1), dict(when=O('iih'), d=0)]),
  dict(l='Papilledema', mods=[dict(when=O('comm', 'iih'), d=1)]),
  dict(l='Leg reflexes', mods=[dict(when=O('cauda'), d=-1), dict(when=O('conus'), d=1)]),
  dict(l='Saddle anesthesia · bladder', mods=[dict(when=O('cauda'), d=1)]),
]

notes = {
  '': 'Choroid plexus makes CSF in the lateral, third and fourth ventricles. It runs lateral → foramina of Monro → third → aqueduct → '
      'fourth → foramina of Luschka and Magendie (the only exits) → subarachnoid space → arachnoid granulations into the superior '
      'sagittal sinus — and down around the cord to the lumbar cistern.',
  'blk:monro': 'A colloid cyst at the foramen of Monro is a noncommunicating block: only the lateral ventricles upstream of it dilate.',
  'blk:aque': 'Aqueductal stenosis: the lateral and third ventricles dilate behind the block while the fourth ventricle stays small — '
              'noncommunicating hydrocephalus.',
  'blk:dw': 'Dandy-Walker malformation: the vermis is absent and the fourth ventricle is a large cyst filling the posterior fossa, '
            'with hydrocephalus and often spina bifida.',
  'blk:comm': 'Communicating hydrocephalus: the ventricles all connect, but scarred arachnoid granulations (after meningitis) can’t '
              'absorb CSF — every ventricle dilates, with raised ICP, papilledema and herniation risk.',
  'blk:nph': 'Normal pressure hydrocephalus: pressure rises only episodically, but the enlarged ventricles stretch the corona radiata — '
             'gait apraxia, dementia and incontinence; a reversible dementia.',
  'blk:exvac': 'Ex vacuo ventriculomegaly mimics hydrocephalus: brain atrophy (Alzheimer, HIV, FTD, Huntington) leaves big ventricles '
               'with normal pressure and no triad.',
  'blk:iih': 'Idiopathic intracranial hypertension: raised ICP with normal imaging — headache, pulsatile tinnitus, CN VI palsy, '
             'papilledema; a lumbar puncture shows a high opening pressure and relieves the headache.',
  'blk:cpp': 'Choroid plexus papilloma: overproduction of CSF raises the pressure; mostly children under 10, half or more in the '
             'fourth ventricle; resect.',
  'blk:syr': 'Chiari I: cerebellar tonsils below the foramen magnum, often with a syrinx (C2–T9) that cuts the crossing spinothalamic '
             'fibers — cape-like loss of pain and temperature with touch spared.',
  'blk:conus': 'The cord ends at the conus medullaris (L1–L2). Conus medullaris syndrome gives symmetric leg weakness with upper motor '
               'neuron signs (the contrast drawn on the cauda equina card).',
  'blk:cauda': 'Cauda equina syndrome: a central disc, tumor or abscess compresses the free roots below L1–L2 — saddle anesthesia, '
               'bladder and bowel loss, asymmetric flaccid weakness, absent ankle jerks. Emergency MRI and decompression.',
}

dyn = dict(
  kinds=dict(c=['csf', '--nf-h2o']), groups=[['csf', 'CSF']],
  switches=[dict(id=SW, label='Block or lesion', type='one', options=[
    ['monro', 'Foramen of Monro (colloid cyst)', 'hydroceph'], ['aque', 'Aqueductal stenosis', 'hydroceph'], ['dw', 'Dandy-Walker', 'chiari'],
    ['comm', 'Scarred granulations (communicating)', 'hydroceph'], ['nph', 'Normal pressure hydrocephalus', 'nph'],
    ['exvac', 'Ex vacuo ventriculomegaly', 'hydroceph'], ['iih', 'Pseudotumor cerebri (IIH)', 'iih'], ['cpp', 'Choroid plexus papilloma', 'csfflow'],
    ['syr', 'Chiari I + syringomyelia', 'syringomyelia'], ['conus', 'Conus medullaris syndrome', 'caudaequina'], ['cauda', 'Cauda equina syndrome', 'caudaequina']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 501–502, 515, 520, 536 · Fundamental Neuroscience ch 6–7')

MAP = dict(
  id='csfsim', title='CSF Flow in Motion', topic='neuro', after='meninges',
  sub='CSF from the choroid plexus through the ventricles to the subarachnoid space, the venous sinus and down the spinal canal — '
      'block it at Monro, the aqueduct, the fourth-ventricle outlets or the granulations and watch what dilates, then compare NPH, '
      'pseudotumor, syrinx, conus medullaris and cauda equina',
  w=3500, h=2160,
  fa='501–502, 506, 515, 520, 536',
  src=[full('Fundamental Neuroscience', 6), full('Fundamental Neuroscience', 7), full('Fundamental Neuroscience', 9), full('Robbins', 28), full('Moore', 2)],
  lanes=[('cfFlow', 'CSF flow', 'glycolysis'), ('cfHydro', 'Hydrocephalus & pressure', 'tca'), ('cfCanal', 'Spinal canal', 'gluconeo')],
  nodes=[
    ('cf1', 'CSF production & flow', 330, 1990, 'cfFlow', 'plexus → sinus', ['csfflow', 'ventwalls'], 'hub'),
    ('cf2', 'Hydrocephalus', 760, 1990, 'cfHydro', 'communicating or not', ['hydroceph']),
    ('cf3', 'NPH · pseudotumor', 1160, 1990, 'cfHydro', 'wobbly, wacky, wet · TOAD', ['nph', 'iih']),
    ('cf4', 'Chiari · Dandy-Walker', 1580, 1990, 'cfHydro', 'posterior fossa', ['chiari']),
    ('cf5', 'Syringomyelia', 330, 2110, 'cfCanal', 'cape-like loss', ['syringomyelia']),
    ('cf6', 'Cauda equina · conus', 760, 2110, 'cfCanal', 'below L1–L2', ['caudaequina']),
    ('cf7', 'Lumbar puncture', 1160, 2110, 'cfCanal', 'L3–L4 or L4–L5', ['lpcsf', 'ntd'])],
  panels=[
    (2420, PANY, 1000, 'Which ventricles dilate (First Aid p. 536)', [
      ('Foramen of Monro', 'lateral only'),
      ('Aqueduct', 'lateral + third'),
      ('Fourth-ventricle outlets', 'all four'),
      ('Arachnoid granulations', 'all four — communicating'),
      ('Ex vacuo', 'big ventricles, normal pressure')])],
  dyn=dyn)
