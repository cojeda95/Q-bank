# The Papez Circuit in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A midline schematic of the limbic loop — subiculum/hippocampus → postcommissural fornix → medial mammillary nucleus →
# mammillothalamic tract → anterior thalamic nucleus → cingulate gyrus → cingulum → entorhinal cortex → back — with an inset of
# the hippocampal circuit (entorhinal → dentate → CA3 → CA1 → subiculum), the amygdala → hypothalamus fear output, septal
# nuclei, and VTA dopamine → nucleus accumbens. A `one` switch cuts a link (Korsakoff, mammillothalamic tract, anterior
# thalamic infarct, bilateral hippocampi, CA1 anoxia, anterior cingulate, Klüver-Bucy, accumbens, septal) and the signal
# stops there. Positions are schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
P = dict(hip=(1320, 960), mam=(860, 980), ath=(980, 720), cing=(1000, 430), ent=(1180, 1060),
         amy=(1080, 1080), sep=(760, 720), acc=(700, 900), vta=(980, 1160), hyp=(820, 1060))
FORNIX = 'M1320 960 C1420 800 1300 560 1060 560 C900 560 840 720 860 980'
MTT = 'M860 980 C900 880 940 800 980 720'
TC = 'M980 720 C990 620 1000 520 1000 430'
CINGULUM = 'M1000 430 C1300 400 1500 600 1460 860 C1420 980 1300 1040 1180 1060'
ENT_HIP = 'M1180 1060 C1240 1040 1290 1000 1320 960'

text('The Papez circuit — the limbic loop that makes new memories', 180, 150, 'dyn-big')
text('midline view, face to the left · positions schematic', 180, 176, 'dyn-cap')

add('<path d="M420 760 C380 460 640 280 960 280 C1300 280 1560 440 1560 760 C1560 1000 1380 1180 1100 1220 C800 1240 480 1080 420 760 Z" '
    'style="fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:4"/>')
add('<path d="M640 560 C780 480 1220 480 1360 560" style="fill:none;stroke:var(--dk6);stroke-width:18;opacity:.35"/>')
text('corpus callosum', 1380, 540, 'nf-l2')
for d, w in ((FORNIX, 14), (MTT, 10), (TC, 10), (CINGULUM, 10), (ENT_HIP, 10)):
    add(f'<path d="{d}" style="fill:none;stroke:var(--dk9);stroke-width:{w};opacity:.3"/>')
add('<path d="M640 420 C800 360 1200 360 1360 420" style="fill:none;stroke:var(--dk4);stroke-width:40;opacity:.25;stroke-linecap:round"/>',
    unless=D('cing'))
add('<path d="M640 420 C800 360 1200 360 1360 420" style="fill:none;stroke:var(--bad);stroke-width:40;opacity:.35;stroke-linecap:round"/>', when=D('cing'))
LB = dict(hip='hippocampus / subiculum', mam='mammillary body', ath='anterior thalamus', cing='cingulate gyrus', ent='entorhinal cortex',
          amy='amygdala', sep='septal nuclei', acc='nucleus accumbens', vta='VTA', hyp='hypothalamus')
for k, (x, y) in P.items():
    if k == 'cing': continue
    add(f'<circle cx="{x}" cy="{y}" r="30" style="fill:var(--dk4);fill-opacity:.3;stroke:var(--dk4);stroke-width:3"/>')
    text(LB[k], x + (40 if k in ('hip', 'ent', 'amy', 'vta') else -40), y + 6, 'nf-l2', None if k in ('hip', 'ent', 'amy', 'vta') else 'end')
text(LB['cing'], 1000, 340, 'nf-l1', 'middle')
text('fornix', 1380, 700, 'nf-l2'); text('mammillothalamic tract', 860, 840, 'nf-l2', 'end'); text('cingulum', 1480, 760, 'nf-l2')
# lesions
LES = dict(kors=[P['mam'], P['ath']], mtt=[(920, 850)], athal=[P['ath']], hippo=[P['hip']], kb=[P['amy']], acc=[P['acc']], sep=[P['sep']])
for k, pts in LES.items():
    for x, y in pts: add(f'<path d="M{x - 26} {y - 26} L{x + 26} {y + 26} M{x + 26} {y - 26} L{x - 26} {y + 26}" class="nf-x"/>', when=D(k))
TAG = dict(kors='Korsakoff (thiamine) — mammillary bodies and anterior thalamus destroyed · confabulation',
           mtt='mammillothalamic tract cut — new memories fail', athal='anterior thalamic infarct — new memories fail',
           hippo='both hippocampi removed — no new declarative memory beyond minutes; old memories and skills spared',
           ca1='anoxia (arrest, drowning, hypoglycemia) — CA1 Sommer sector dies first',
           cing='bilateral anterior cingulate — blunted emotion, akinetic mutism',
           kb='Klüver-Bucy (bilateral amygdala: trauma, surgery, HSV-1) — placid, hyperoral, hypersexual',
           acc='accumbens lesion — addiction and impulsive behavior', sep='septal infarct — rage behavior in a few patients')
for k, s in TAG.items(): text(s, 1000, 1330, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ hippocampal inset ════════
IX, IY = 1720, 900
add(f'<rect x="{IX}" y="{IY}" width="700" height="300" rx="24" class="dyn-soft"/>')
text('inside the hippocampal formation', IX + 20, IY - 16, 'nf-l1')
HS = [('EC', 0), ('DG', 1), ('CA3', 2), ('CA1', 3), ('Sub', 4)]
for lab, i in HS:
    x = IX + 80 + i * 135
    add(f'<circle cx="{x}" cy="{IY + 150}" r="40" style="fill:var(--dk9);fill-opacity:.25;stroke:var(--dk9);stroke-width:3"/>')
    text(lab, x, IY + 158, 'nf-l1', 'middle')
add(f'<path d="M{IX + 485} {IY + 120} l40 60 M{IX + 525} {IY + 120} l-40 60" class="nf-x"/>', when=D('ca1'))
text('perforant path in · dentate → CA3 → CA1 → subiculum · out via the fornix', IX + 350, IY + 260, 'nf-l2', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
CUT = D('kors', 'mtt', 'athal', 'hippo', 'ca1')
flows = [
  dict(d=FORNIX, len=1100, speed=110, r=9, base=dict(sig=4), mods=[m(D('hippo', 'ca1'), set=dict(sig=0))]),
  dict(d=MTT, len=300, speed=110, r=9, base=dict(sig=2), mods=[m(D('kors', 'mtt', 'hippo', 'ca1'), set=dict(sig=0))]),
  dict(d=TC, len=300, speed=110, r=9, base=dict(sig=2), mods=[m(CUT, set=dict(sig=0))]),
  dict(d=CINGULUM, len=900, speed=110, r=9, base=dict(sig=4), mods=[m(CUT + D('cing'), set=dict(sig=0))]),
  dict(d=ENT_HIP, len=200, speed=110, r=9, base=dict(sig=2), mods=[m(CUT + D('cing'), set=dict(sig=0))]),
  dict(d=f'M{IX + 80} {IY + 150} H{IX + 620}', len=540, speed=100, r=8, base=dict(sig=4), mods=[m(D('ca1', 'hippo'), set=dict(sig=1), speed=0.3)]),
  dict(d='M1080 1080 C1000 1100 900 1080 820 1060', len=280, speed=100, r=8, base=dict(fear=2), mods=[m(D('kb'), set=dict(fear=0))]),
  dict(d='M980 1160 C900 1100 780 1000 700 900', len=360, speed=100, r=8, base=dict(da=3), mods=[m(D('acc'), set=dict(da=0))]),
]
sites = [dict(x=1240, y=520, n=[0, -1], w=10, t='rec', l='', aria='Papez circuit', c='papez', ions=[]),
         dict(x=IX + 700, y=IY + 150, n=[1, 0], w=10, t='rec', l='', aria='Hippocampal formation', c='hippoform', ions=[]),
         dict(x=1390, y=1000, n=[1, 0], w=10, t='rec', l='', aria='Memory consolidation', c='memconsol', ions=[]),
         dict(x=900, y=1020, n=[-1, 1], w=10, t='rec', l='', aria='Amnesia and Korsakoff', c='amnesia', ions=[]),
         dict(x=1120, y=1130, n=[1, 1], w=10, t='rec', l='', aria='Amygdala', c='amygdala', ions=[]),
         dict(x=1040, y=1030, n=[1, -1], w=10, t='rec', l='', aria='Klüver-Bucy syndrome', c='kluverbucy', ions=[]),
         dict(x=650, y=930, n=[-1, 0], w=10, t='rec', l='', aria='Nucleus accumbens', c='accumbens', ions=[]),
         dict(x=720, y=690, n=[-1, -1], w=10, t='rec', l='', aria='Septal nuclei', c='septal', ions=[])]

readouts = [
  dict(l='New declarative memories', mods=[dict(when=CUT, d=-1)]),
  dict(l='Old memories', mods=[dict(when=D('kors'), d=-1)]),
  dict(l='Fear response', mods=[dict(when=D('kb'), d=-1)]),
  dict(l='Impulse control', mods=[dict(when=D('acc'), d=-1)]),
]

notes = {
  '': 'Papez circuit: subiculum → postcommissural fornix → medial mammillary nucleus → mammillothalamic tract → anterior thalamic '
      'nucleus → cingulate gyrus → cingulum → entorhinal cortex → hippocampus. Consolidating short-term into long-term '
      'declarative memory is the hippocampal formation’s job; break any link and new memory formation suffers.',
  'dx:kors': 'Korsakoff: thiamine deficiency destroys especially the mammillary bodies and anterior thalamus — anterograde more '
             'than retrograde amnesia, disorientation, confabulation. Wernicke (acute, reversible): ophthalmoplegia, ataxia, '
             'confusion — thiamine before glucose.',
  'dx:mtt': 'A cut mammillothalamic tract breaks the loop — new memory formation suffers.',
  'dx:athal': 'An anterior thalamic infarct breaks the loop — new memory formation suffers.',
  'dx:hippo': 'Bilateral hippocampal removal: old memories and short-term recall survive, but no new declarative memory lasts '
              'beyond a few minutes — anterograde amnesia. Procedural memory (cerebellum, basal ganglia, motor cortex) is spared.',
  'dx:ca1': 'CA1 — the Sommer sector — is the most anoxia-vulnerable part of the hippocampus (cardiac arrest, near drowning, '
            'severe hypoglycemia).',
  'dx:cing': 'Bilateral anterior cingulate lesions blunt emotional responses and can cause akinetic mutism — immobile, mute, '
             'unresponsive but not in coma.',
  'dx:kb': 'Klüver-Bucy: bilateral temporal lesions abolish the amygdalae — placidity, hyperorality, hyperphagia, hypersexuality, '
           'visual agnosia, hypermetamorphosis. Trauma, temporal lobe surgery, HSV-1 encephalitis.',
  'dx:acc': 'Nucleus accumbens: VTA dopamine via the medial forebrain bundle makes it a gratification center; lesions → addiction '
            'and impulsive behavior.',
  'dx:sep': 'Septal nuclei: rage behavior has been seen in a few patients with midline septal infarcts.',
}

dyn = dict(
  kinds=dict(sig=['mov', '--dk9'], fear=['mov', '--bad'], da=['mov', '--accent']),
  groups=[['mov', 'Papez signal · fear output · dopamine']],
  switches=[dict(id='dx', label='Lesion', type='one', options=[
              ['kors', 'Korsakoff', 'amnesia'], ['mtt', 'Mammillothalamic tract', 'papez'], ['athal', 'Anterior thalamus', 'papez'],
              ['hippo', 'Both hippocampi', 'memconsol'], ['ca1', 'CA1 anoxia', 'hippoform'], ['cing', 'Anterior cingulate', 'papez'],
              ['kb', 'Klüver-Bucy', 'kluverbucy'], ['acc', 'Nucleus accumbens', 'accumbens'], ['sep', 'Septal nuclei', 'septal']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Fundamental Neuroscience ch 31')

MAP = dict(
  id='papezsim', title='The Papez Circuit in Motion', topic='behav', after='limbmem',
  sub='Send a signal around the Papez loop and through the hippocampus, then cut it — Korsakoff, mammillothalamic tract, thalamus, '
      'hippocampi, CA1 anoxia, cingulate — or lesion the amygdala, accumbens or septum',
  w=3600, h=1900,
  fa='64, 505, 509, 524, 575',
  src=['Fundamental Neuroscience ch 31 — The Limbic System',
       'Guyton ch 58 — Cerebral Cortex, Intellectual Functions of the Brain, Learning, and Memory',
       'Guyton ch 59 — The Limbic System and the Hypothalamus—Behavioral and Motivational Mechanisms of the Brain'],
  lanes=[('pzMem', 'Memory loop', 'glycolysis'), ('pzEmo', 'Emotion & reward', 'tca')],
  nodes=[
    ('pz1', 'Papez circuit', 330, 1700, 'pzMem', 'fornix → thalamus → cingulate', ['papez'], 'hub'),
    ('pz2', 'Hippocampal formation', 760, 1700, 'pzMem', 'DG → CA3 → CA1', ['hippoform']),
    ('pz3', 'Memory consolidation', 1200, 1700, 'pzMem', 'short → long term', ['memconsol']),
    ('pz4', 'Amnesia & Korsakoff', 1640, 1700, 'pzMem', 'anterograde', ['amnesia']),
    ('pz5', 'Amygdala', 2080, 1700, 'pzEmo', 'fear · salience', ['amygdala']),
    ('pz6', 'Klüver-Bucy syndrome', 2520, 1700, 'pzEmo', 'placid · hyperoral', ['kluverbucy']),
    ('pz7', 'Nucleus accumbens', 2960, 1700, 'pzEmo', 'reward · addiction', ['accumbens']),
    ('pz8', 'Septal nuclei', 330, 1840, 'pzEmo', 'medial forebrain bundle', ['septal'])],
  panels=[
    (2500, PANY, 1000, 'Where the loop breaks (Fundamental Neuroscience ch 31)', [
      ('Mammillary bodies', 'thiamine — Korsakoff'), ('Mammillothalamic tract', 'new memories fail'), ('Anterior thalamus', 'infarct'),
      ('Both hippocampi', 'anterograde amnesia'), ('CA1', 'anoxia')])],
  dyn=dyn)
