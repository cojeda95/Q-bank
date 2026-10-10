# Dementias Over Time (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A side view of the brain — frontal, parietal, temporal, occipital lobes, hippocampus, ventricles, midbrain, cerebellum —
# with acetylcholine from the nucleus basalis and CSF moving. A `one` switch picks the disease and `yr` (steps, auto) runs
# it early → middle → late: Alzheimer atrophy spreads out from the hippocampus, FTD takes the frontal and temporal lobes,
# PSP the midbrain, Lewy bodies stud the cortex, vascular infarcts add up step by step, CJD vacuoles fill the cortex fast,
# and NPH swells the ventricles (a `shunt` toggle drains them). The order of spread is drawn only as far as each card states
# it. 3 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
def DY(d, *y): return [f'dx:{d}&yr:{x}' for x in y]
PANY = 1180
REG = dict(front=(620, 600, 230, 200), par=(1050, 480, 210, 170), temp=(860, 880, 240, 100), occ=(1330, 680, 140, 160))

text('Dementias over time — what goes first, and how fast', 180, 150, 'dyn-big')
text('left side of the brain, face to the left · red shading = atrophy · step through early, middle, late', 180, 176, 'dyn-cap')

# ════════ brain ════════
add('<path d="M420 700 C380 420 640 260 960 270 C1260 280 1480 420 1480 680 C1480 820 1400 880 1300 880 C1220 940 1100 960 980 960 '
    'C820 980 640 960 560 880 C480 820 430 780 420 700 Z" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:5"/>')
for k, (x, y, rx, ry) in REG.items():
    add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" style="fill:none;stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 8"/>')
text('frontal', 560, 560, 'nf-l1', 'middle'); text('parietal', 1080, 440, 'nf-l1', 'middle')
text('temporal', 760, 900, 'nf-l1', 'middle'); text('occipital', 1360, 660, 'nf-l1', 'middle')
add('<ellipse cx="940" cy="860" rx="70" ry="28" style="fill:var(--dk9);fill-opacity:.3;stroke:var(--dk9);stroke-width:3"/>')
text('hippocampus', 1020, 840, 'nf-l2')
add('<path d="M800 640 C880 580 1080 580 1140 660 C1080 640 880 640 800 660 Z" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:3"/>',
    unless=['dx:nph&!shunt'])
add('<path d="M760 660 C840 520 1120 520 1200 680 C1100 720 860 720 760 660 Z" style="fill:var(--nf-h2o);fill-opacity:.55;stroke:var(--bad);stroke-width:4"/>',
    when=['dx:nph&!shunt'])
text('ventricles', 980, 600, 'nf-l2', 'middle')
add('<rect x="1040" y="930" width="90" height="300" rx="30" style="fill:var(--dk3);fill-opacity:.2;stroke:var(--dk3);stroke-width:3"/>')
text('midbrain → brainstem', 1150, 1200, 'nf-l2')
add('<ellipse cx="1310" cy="1000" rx="150" ry="90" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:3"/>'); text('cerebellum', 1310, 1120, 'nf-l2', 'middle')
add('<circle cx="760" cy="800" r="18" style="fill:var(--dk5);opacity:.8"/>'); text('nucleus basalis (ACh)', 740, 780, 'nf-l2', 'end')

# ════════ atrophy ════════
def shade(k, op, when):
    x, y, rx, ry = REG[k]
    add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" style="fill:var(--bad);fill-opacity:{op}"/>', when=when)
def hip(op, when): add(f'<ellipse cx="940" cy="860" rx="70" ry="28" style="fill:var(--bad);fill-opacity:{op}"/>', when=when)
hip(.4, DY('alz', 'e')); hip(.6, DY('alz', 'm', 'l'))
for k in ('temp', 'par'): shade(k, .3, DY('alz', 'm')); shade(k, .5, DY('alz', 'l'))
for k in ('front', 'occ'): shade(k, .4, DY('alz', 'l'))
shade('front', .35, DY('ftd', 'e')); shade('front', .55, DY('ftd', 'm', 'l')); shade('temp', .35, DY('ftd', 'm')); shade('temp', .55, DY('ftd', 'l'))
for op, y in ((.3, 'e'), (.5, 'm'), (.7, 'l')):
    add(f'<rect x="1040" y="930" width="90" height="120" rx="30" style="fill:var(--bad);fill-opacity:{op}"/>', when=DY('psp', y))
text('hummingbird sign — midbrain atrophy', 1150, 1260, 'nf-l1 dyn-tag', when=D('psp'))
LB = [(560, 520), (700, 680), (1000, 420), (1150, 560), (1330, 640), (840, 860), (650, 460), (1250, 420), (900, 480)]
for i, (x, y) in enumerate(LB):
    st = 'e' if i < 3 else ('m' if i < 6 else 'l')
    w = DY('lewy', *(('e', 'm', 'l') if st == 'e' else ('m', 'l') if st == 'm' else ('l',)))
    add(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--dk7);opacity:.85"/>', when=w)
INF = [((1100, 520), ('e', 'm', 'l')), ((700, 640), ('m', 'l')), ((1300, 720), ('l',)), ((880, 860), ('l',))]
for (x, y), ys in INF:
    add(f'<circle cx="{x}" cy="{y}" r="40" style="fill:var(--ink);fill-opacity:.55"/>', when=DY('vasc', *ys))
SP_ = [(600, 560), (720, 520), (980, 400), (1120, 470), (1340, 700), (820, 880), (660, 700), (1200, 620), (900, 520), (1060, 640)]
for i, (x, y) in enumerate(SP_):
    ys = ('e', 'm', 'l') if i < 3 else ('m', 'l')
    for dx_ in (-16, 14):
        add(f'<circle cx="{x + dx_}" cy="{y}" r="11" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:2"/>', when=DY('cjd', *ys))
TAG = dict(alz='short-term memory first — plaques and tangles spread out from the hippocampus',
           ftd='personality, behavior or language before memory — Pick bodies or TDP-43',
           psp='parkinsonism + early vertical gaze palsy + cognitive decline', lewy='α-synuclein in the cortex from the start — visual hallucinations, fluctuations',
           vasc='stepwise decline — each infarct adds a step; memory late', cjd='rapid: weeks to months — startle myoclonus, ataxia, fatal',
           nph='wobbly, wacky and wet — ventricles out of proportion to the sulci')
for k, s in TAG.items(): text(s, 950, 1340, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('drained — a reversible dementia', 950, 1380, 'nf-l1', 'middle', when=['dx:nph&shunt'])
text('reversible causes to rule out first: depression, hypothyroidism, B12, neurosyphilis, NPH — check TSH, B12, RPR, imaging',
     950, 1420, 'nf-l2', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M760 800 C700 700 620 600 600 520', len=320, speed=80, r=8, base=dict(ach=3),
       mods=[m(DY('alz', 'e'), set=dict(ach=2)), m(DY('alz', 'm'), set=dict(ach=1)), m(DY('alz', 'l'), set=dict(ach=0))]),
  dict(d='M760 800 C850 650 950 520 1050 460', len=420, speed=80, r=8, base=dict(ach=3),
       mods=[m(DY('alz', 'e'), set=dict(ach=2)), m(DY('alz', 'm'), set=dict(ach=1)), m(DY('alz', 'l'), set=dict(ach=0))]),
  dict(d='M820 650 C900 610 1060 610 1120 660 C1100 760 1090 860 1085 1200', len=800, speed=70, r=8, base=dict(csf=3),
       mods=[m(['dx:nph&!shunt'], speed=0.2)]),
  dict(d='M1120 680 C1300 800 1500 1000 1600 1300', len=750, speed=110, r=8, base=dict(csf=3), when=['dx:nph&shunt']),
]
sites = [dict(x=900, y=820, n=[-1, -1], w=10, t='rec', l='', aria='Alzheimer disease', c='alzheimer', ions=[]),
         dict(x=480, y=560, n=[-1, 0], w=10, t='rec', l='', aria='Frontotemporal dementia', c='ftd', ions=[]),
         dict(x=1130, y=980, n=[1, 0], w=10, t='rec', l='', aria='Progressive supranuclear palsy', c='psp', ions=[]),
         dict(x=1250, y=380, n=[1, -1], w=10, t='rec', l='', aria='Lewy body dementia', c='lewy', ions=[]),
         dict(x=1420, y=520, n=[1, 0], w=10, t='rec', l='', aria='Vascular dementia', c='vascdementia', ions=[]),
         dict(x=640, y=380, n=[-1, -1], w=10, t='rec', l='', aria='Creutzfeldt-Jakob disease', c='cjd', ions=[]),
         dict(x=1200, y=640, n=[1, 0], w=10, t='rec', l='', aria='Normal pressure hydrocephalus', c='nph', ions=[]),
         dict(x=450, y=820, n=[-1, 0], w=10, t='rec', l='', aria='Reversible causes', c='dementiarev', ions=[])]

readouts = [
  dict(l='Memory', mods=[dict(when=D('alz', 'cjd', 'lewy'), d=-1), dict(when=['dx:nph&!shunt'], d=-1), dict(when=DY('vasc', 'l') + DY('ftd', 'l'), d=-1)]),
  dict(l='Behavior & language', mods=[dict(when=D('ftd'), d=-1), dict(when=DY('alz', 'l'), d=-1)]),
  dict(l='Movement & gait', mods=[dict(when=D('psp', 'lewy', 'cjd'), d=-1), dict(when=['dx:nph&!shunt'], d=-1)]),
]

notes = {
  '': 'Dementia is a decline in memory or executive function with a clear sensorium — unlike delirium. Pick a disease and step '
      'through time; rule out the reversible causes first.',
  'dx:alz': 'Alzheimer: β-amyloid plaques and tau tangles spread out from the entorhinal cortex and hippocampus; nucleus basalis '
            'cholinergic neurons go early, so cortical ACh falls. Memory first, then language, visuospatial, executive; '
            'personality late. APP (chr 21, Down), presenilins, APOE ε4. Donepezil, rivastigmine, galantamine; memantine.',
  'dx:ftd': 'Frontotemporal: frontal and temporal neurons go first — disinhibition, apathy, hyperorality, compulsions, or primary '
            'progressive aphasia — before memory. Pick bodies or TDP-43.',
  'dx:psp': 'PSP: tau in the midbrain and basal ganglia — parkinsonism with an early vertical gaze palsy and cognitive decline; '
            'hummingbird sign. Supportive.',
  'dx:lewy': 'Lewy body dementia: α-synuclein Lewy bodies in the cortex from the start — visual hallucinations, fluctuating '
             'cognition, REM sleep behavior disorder, parkinsonism within a year of the dementia. Severe antipsychotic '
             'sensitivity; cholinesterase inhibitors.',
  'dx:vasc': 'Vascular dementia (2nd most common): infarcts and small-vessel ischemia — stepwise decline, focal signs, memory late. '
             'Control vascular risk factors.',
  'dx:cjd': 'CJD: PrPsc refolds PrPc into β-pleated sheets — spongiform cortex without inflammation; rapidly progressive dementia '
            'over weeks to months with startle myoclonus and ataxia. Periodic sharp waves on EEG, CSF 14-3-3. Fatal.',
  'dx:nph': 'Normal pressure hydrocephalus: the ventricles enlarge and stretch corona radiata fibers to the legs and bladder — gait '
            'apraxia, cognitive dysfunction, incontinence. Reversible.',
  'shunt': 'Lumbar puncture drainage, then a ventriculoperitoneal shunt, for NPH.',
}

dyn = dict(
  kinds=dict(ach=['mov', '--dk5'], csf=['mov', '--nf-h2o']), groups=[['mov', 'Acetylcholine · CSF']],
  switches=[dict(id='dx', label='Disease', type='one', options=[
              ['alz', 'Alzheimer', 'alzheimer'], ['ftd', 'Frontotemporal', 'ftd'], ['lewy', 'Lewy body', 'lewy'],
              ['vasc', 'Vascular', 'vascdementia'], ['psp', 'PSP', 'psp'], ['cjd', 'CJD', 'cjd'], ['nph', 'NPH', 'nph']]),
            dict(id='yr', label='Time', type='steps', auto=3, options=[['e', 'Early'], ['m', 'Middle'], ['l', 'Late']]),
            dict(id='shunt', label='Treat', type='toggle', on='Shunted', off='Shunt (NPH)', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 28')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='demsim', title='Dementias Over Time', topic='neuro', after='cortex',
  sub='Run each dementia from early to late — Alzheimer spreading from the hippocampus, frontotemporal, Lewy body, stepwise '
      'vascular, PSP, rapid CJD — and shunt the reversible one, NPH',
  w=3600, h=1900,
  fa='174, 534, 535, 536',
  src=['Robbins ch 28 — The central nervous system', 'Kaplan & Sadock ch 3 — Neurocognitive Disorders'],
  lanes=[('dmNeuro', 'Neurodegenerative', 'tca'), ('dmOther', 'Vascular, prion, reversible', 'glycolysis')],
  nodes=[
    ('dm1', 'Alzheimer disease', 330, 1700, 'dmNeuro', 'hippocampus first', ['alzheimer'], 'hub'),
    ('dm2', 'Frontotemporal dementia', 760, 1700, 'dmNeuro', 'behavior first', ['ftd']),
    ('dm3', 'Lewy body dementia', 1200, 1700, 'dmNeuro', 'hallucinations', ['lewy']),
    ('dm4', 'Progressive supranuclear palsy', 1640, 1700, 'dmNeuro', 'vertical gaze', ['psp']),
    ('dm5', 'Vascular dementia', 2080, 1700, 'dmOther', 'stepwise', ['vascdementia']),
    ('dm6', 'Creutzfeldt-Jakob disease', 2520, 1700, 'dmOther', 'weeks to months', ['cjd']),
    ('dm7', 'Normal pressure hydrocephalus', 2960, 1700, 'dmOther', 'wet, wobbly, wacky', ['nph']),
    ('dm8', 'Reversible causes', 330, 1840, 'dmOther', 'TSH · B12 · RPR', ['dementiarev'])],
  panels=[
    (2500, PANY, 1000, 'What goes first (Robbins ch 28)', [
      ('Alzheimer', 'short-term memory'), ('Frontotemporal', 'behavior or language'), ('Lewy body', 'hallucinations, fluctuation'),
      ('Vascular', 'stepwise; memory late'), ('CJD', 'rapid, myoclonus'), ('NPH', 'triad: gait, cognition, incontinence')])],
  dyn=dyn)
