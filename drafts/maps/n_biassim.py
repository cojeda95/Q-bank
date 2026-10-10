# Bias in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A drawn study pipeline — target population → who gets in → the groups → measuring the outcome → the answer — with
# people flowing through it. One `one` switch picks a bias: the stage where it enters lights up and its mechanism is
# drawn (a skewed sample, dropouts, a distorted measurement, a confounder linked to both sides, a screening
# timeline for lead-time and length-time bias), with the fix underneath. No readouts — the answers are stages and
# fixes, not arrows. Facts from the pinned cards (selectionbias, infobias, confounding, screenbias, rct); their FA
# pages are in `fa`. No new cards.
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


SW = 'bias'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 700

# ════════ the pipeline ════════
box(160, 130, 2340, 1310)
text('A study, start to finish — where does the bias get in?', 190, 170, 'dyn-big')
text('people flow left to right; the stage a bias enters lights up', 190, 196, 'dyn-cap')
STG = [('pop', 'Target population', 'who the answer is for'), ('smp', 'Who gets in', 'sampling · allocation'),
       ('grp', 'The groups', 'followed over time'), ('mea', 'Measuring', 'exposure and outcome'), ('ans', 'The answer', 'RR · OR · survival')]
SX = {k: 200 + i * 430 for i, (k, *_) in enumerate(STG)}
HIT = dict(sel=['smp'], attr=['grp'], recall=['mea'], meas=['mea'], hawth=['grp'], pyg=['mea'], conf=['ans'], lead=['ans'], length=['smp'])
for k, lab, sub in STG:
    x = SX[k]
    add(f'<rect x="{x}" y="300" width="360" height="260" rx="22" class="dyn-soft"/>')
    who = [b for b, ks in HIT.items() if k in ks]
    if who:
        add(f'<rect x="{x}" y="300" width="360" height="260" rx="22" style="fill:var(--accent);fill-opacity:.14;stroke:var(--accent);stroke-width:5"/>', when=O(*who))
    text(lab, x + 24, 340, 'nf-l1'); text(sub, x + 24, 364, 'nf-l2')
for i in range(4):
    x = SX[STG[i][0]] + 360
    add(f'<path d="M{x + 8} 430 H{x + 62}" class="dyn-line" marker-end="url(#ah-bsFlow)"/>')

# selection: a skewed sample (Berkson: hospital patients are sicker)
add(f'<path d="M{SX["smp"] + 40} 480 L{SX["smp"] + 320} 420" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:10 8"/>', when=O('sel'))
text('only the easiest to enroll, or hospital patients (Berkson)', SX['smp'], 610, 'nf-l1 dyn-tag', when=O('sel'))
# attrition: people lost to follow-up
add(f'<rect x="{SX["grp"] + 60}" y="660" width="240" height="70" rx="14" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:3"/>', when=O('attr'))
text('lost to follow-up', SX['grp'] + 180, 702, 'nf-l1', 'middle', when=O('attr'))
text('those who drop out have a different prognosis', SX['grp'], 770, 'nf-l2', when=O('attr'))
# measurement-stage biases
MEA = dict(recall=('cases remember exposures differently', 'knowing the diagnosis changes recall — case-control studies'),
           meas=('the data are systematically distorted', 'e.g., a faulty blood pressure cuff'),
           pyg=('the researcher’s belief changes the result', 'observer-expectancy (Pygmalion) bias'))
for k, (a, b) in MEA.items():
    text(a, SX['mea'], 610, 'nf-l1 dyn-tag', when=O(k)); text(b, SX['mea'], 636, 'nf-l2', when=O(k))
text('being watched changes behavior (Hawthorne effect)', SX['grp'], 610, 'nf-l1 dyn-tag', when=O('hawth'))
# confounding: coffee and lung cancer, both linked to smoking
add(f'<ellipse cx="{SX["mea"] + 180}" cy="760" rx="170" ry="54" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>', when=O('conf'))
text('Smoking', SX['mea'] + 180, 766, 'nf-l1', 'middle', when=O('conf'))
add(f'<path d="M{SX["mea"] + 30} 740 Q{SX["grp"] + 200} 680 {SX["grp"] + 180} 580" style="fill:none;stroke:var(--dk5);stroke-width:4" marker-end="url(#ah-bsFlow)"/>'
    f'<path d="M{SX["mea"] + 330} 740 Q{SX["ans"] + 120} 680 {SX["ans"] + 180} 580" style="fill:none;stroke:var(--dk5);stroke-width:4" marker-end="url(#ah-bsFlow)"/>', when=O('conf'))
text('coffee drinkers', SX['grp'] + 40, 480, 'nf-l2', when=O('conf'))
text('“coffee causes lung cancer”', SX['ans'] + 24, 480, 'nf-l2', when=O('conf'))

# screening timelines (lead time, length time)
TL0, TL1 = 300, 2200
tx = lambda yrs: round(TL0 + (TL1 - TL0) * yrs / 10)
def line(y, a, b, lab, col='--ink-3', w=8):
    return f'<path d="M{tx(a)} {y} H{tx(b)}" style="stroke:var({col});stroke-width:{w};stroke-linecap:round"/>'
text('Screening, drawn on an illustrative 10-year timeline', 190, 900, 'dyn-big', when=O('lead', 'length'))
add(line(980, 0, 10, '') + f'<text class="nf-l2" x="{tx(0)}" y="960">disease begins</text>', when=O('lead'))
add(f'<circle cx="{tx(7)}" cy="980" r="14" style="fill:var(--ink)"/><circle cx="{tx(4)}" cy="1080" r="14" style="fill:var(--accent)"/>'
    f'<circle cx="{tx(10)}" cy="980" r="10" style="fill:var(--bad)"/><circle cx="{tx(10)}" cy="1080" r="10" style="fill:var(--bad)"/>'
    + line(1080, 0, 10, ''), when=O('lead'))
text('no screening: diagnosed at symptoms (year 7) → “survives 3 years”', tx(0), 1030, 'nf-l2', when=O('lead'))
text('screened: diagnosed at year 4 → “survives 6 years” — death comes at the same time', tx(0), 1130, 'nf-l1', when=O('lead'))
text('death', tx(10), 950, 'nf-l2', 'end', when=O('lead'))
for i, (a, b, lab) in enumerate(((0, 9, 'slow-growing — long detectable phase, found by the screen'), (2, 4, 'aggressive — appears and kills between screens'))):
    y = 990 + i * 110
    add(line(y, a, b, '', '--dk5' if i == 0 else '--bad', 14), when=O('length'))
    text(lab, tx(a), y + 40, 'nf-l2', when=O('length'))
for yr in (1, 5, 9):
    add(f'<path d="M{tx(yr)} 940 V1180" style="stroke:var(--accent);stroke-width:3;stroke-dasharray:8 6"/>', when=O('length'))
text('screen', tx(5), 930, 'nf-l2', 'middle', when=O('length'))

# the fix
FIX = dict(sel='Fix: randomization and the right comparison group', attr='Fix: analyze by intention-to-treat — once randomized, always analyzed',
           recall='Fix: use records, shorten the time to recall', meas='Fix: standardized, objective methods planned in advance',
           hawth='Fix: blinding, placebo, standardized methods', pyg='Fix: blinding',
           conf='Fix: randomization, matching, crossover design — or stratify (the association vanishes)',
           lead='Fix: compare back-end survival, adjusted for stage at diagnosis', length='Fix: a randomized trial of screening vs no screening')
for k, t in FIX.items():
    text(t, 190, 1260, 'nf-l1', when=O(k))
text('pick a bias on the right', 190, 1260, 'nf-l1', unless=[f'{SW}:*'])

# ════════ motion ════════
flows = [
  dict(d=f'M{SX["pop"] + 30} 470 H{SX["ans"] + 330}', len=SX['ans'] + 300 - SX['pop'], speed=170, r=7, base=dict(pp=12),
       mods=[dict(when=O('attr'), set=dict(pp=8))]),
  dict(d=f'M{SX["grp"] + 180} 500 V660', len=160, speed=70, r=7, base=dict(), when=O('attr'), mods=[dict(when=O('attr'), set=dict(pp=3))]),
]
sites = [dict(x=SX['smp'] + 180, y=300, n=[0, -1], w=40, t='rec', l='', aria='Selection bias', c='selectionbias', ions=[])]

notes = {
  '': 'Bias is systematic error built into how a study is designed, run or analyzed. Ask where it got in — who was sampled, who '
      'stayed, how things were measured, or what else differed — and which design step prevents it.',
  'bias:sel': 'Selection bias: the sample does not represent the target population — convenience samples, or Berkson bias when cases '
              'or controls come from the hospital and are sicker. Randomize and pick the right comparison group.',
  'bias:attr': 'Attrition bias, a selection bias: people lost to follow-up have a different prognosis from those who stay, so the '
               'groups drift apart.',
  'bias:recall': 'Recall bias: knowing the diagnosis changes what patients remember — common in retrospective case-control studies. '
                 'Use records and shorten the gap.',
  'bias:meas': 'Measurement bias: the data are systematically distorted, as by a faulty cuff. Standardized, objective methods planned '
               'in advance prevent it.',
  'bias:hawth': 'Hawthorne effect: people change their behavior because they know they are being studied. Blinding and placebo '
                'help.',
  'bias:pyg': 'Observer-expectancy (Pygmalion) bias: the researcher’s belief changes the outcome or how it is recorded. Blinding '
              'prevents it.',
  'bias:conf': 'Confounding: a third variable linked to both exposure and outcome — coffee seems to cause lung cancer because coffee '
               'drinkers smoke. The association disappears when stratified by smoking.',
  'bias:lead': 'Lead-time bias: screening diagnoses earlier, so survival from diagnosis looks longer — but death comes at the same '
               'time. Compare back-end survival adjusted for stage.',
  'bias:length': 'Length-time bias: screening preferentially catches slow-growing disease with a long detectable phase; aggressive '
                 'disease shows up between screens. Fix with a randomized trial of screening vs none.',
}

dyn = dict(
  kinds=dict(pp=['pp', '--dk9']), groups=[['pp', 'People']],
  switches=[dict(id=SW, label='Bias', type='one', options=[
    ['sel', 'Selection (Berkson)', 'selectionbias'], ['attr', 'Attrition', 'selectionbias'], ['recall', 'Recall', 'infobias'],
    ['meas', 'Measurement', 'infobias'], ['hawth', 'Hawthorne effect', 'infobias'], ['pyg', 'Observer-expectancy', 'infobias'],
    ['conf', 'Confounding', 'confounding'], ['lead', 'Lead-time', 'screenbias'], ['length', 'Length-time', 'screenbias']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=[],
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 257, 262–263')

MAP = dict(
  id='biassim', title='Bias in Motion', topic='stats', after='biostats',
  sub='People flow through a study — sampling, groups, measurement, the answer — and each bias lights up the stage it enters, '
      'with its mechanism drawn (dropouts, a confounder, a screening timeline) and the design fix that prevents it',
  w=3500, h=1540,
  fa='257, 262–263',
  src=[],
  lanes=[('bsFlow', 'The study', 'glycolysis'), ('bsSel', 'Selection', 'tca'), ('bsInfo', 'Information & confounding', 'gluconeo')],
  nodes=[
    ('bs1', 'Clinical trials', 330, 1420, 'bsFlow', 'randomize · blind', ['rct'], 'hub'),
    ('bs2', 'Selection bias', 760, 1420, 'bsSel', 'Berkson · attrition', ['selectionbias']),
    ('bs3', 'Screening biases', 1180, 1420, 'bsSel', 'lead time · length time', ['screenbias']),
    ('bs4', 'Recall · observer bias', 1600, 1420, 'bsInfo', 'Hawthorne · Pygmalion', ['infobias']),
    ('bs5', 'Confounding', 2020, 1420, 'bsInfo', 'vs effect modification', ['confounding'])],
  panels=[
    (2420, PANY, 1000, 'Bias → prevention (First Aid pp. 262–263)', [
      ('Selection', 'randomization · right comparison group'),
      ('Recall', 'records · shorter recall time'),
      ('Observer, measurement', 'blinding · placebo · standardized methods'),
      ('Confounding', 'randomization · matching · crossover'),
      ('Lead time', 'back-end survival adjusted for stage'),
      ('Length time', 'randomized trial of screening')])],
  dyn=dyn)
