# Glycogen Storage Diseases in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A hepatocyte and a muscle fiber side by side, each with a glycogen granule and a lysosome. Fasting (liver) breaks
# glycogen down to G6P and releases glucose through glucose-6-phosphatase; exercise (muscle) burns glycogen through
# glycolysis to lactate. A `steps` switch alternates fasting / exercise; a `one` switch blocks one enzyme — von Gierke,
# Pompe, Cori, Andersen, McArdle, Hers, Tarui — with an ✕ on it and the flows and drawing changing. 6 readouts. Facts
# from the pinned cards (vongierke, pompe, cori, andersen, mcardle, hers, tarui); FA pp. 84–85. No new cards.
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


import math
SW = 'gsd'
O = lambda *k: [f'{SW}:{x}' for x in k]
FAST, EX = ['st:fast'], ['st:ex']
PANY = 720
def X(cx, cy, s=22): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(lab, x, y, w=240):
    add(f'<rect x="{x - w // 2}" y="{y - 24}" width="{w}" height="48" rx="24" class="dyn-soft"/>')
    text(lab, x, y + 6, 'nf-l1', 'middle')
def granule(cx, cy, long=False):
    """a glycogen granule drawn as a branched tree (or long unbranched chains)"""
    out = []
    if long:
        for i in range(5):
            out.append(f'<path d="M{cx - 150} {cy - 60 + i * 30} H{cx + 150}" style="stroke:var(--dk5);stroke-width:7;stroke-linecap:round"/>')
    else:
        for a in range(0, 360, 45):
            x1, y1 = cx + 70 * math.cos(math.radians(a)), cy + 70 * math.sin(math.radians(a))
            x2, y2 = cx + 130 * math.cos(math.radians(a + 20)), cy + 110 * math.sin(math.radians(a + 20))
            x3, y3 = cx + 130 * math.cos(math.radians(a - 20)), cy + 110 * math.sin(math.radians(a - 20))
            out.append(f'<path d="M{cx} {cy} L{x1:.0f} {y1:.0f} L{x2:.0f} {y2:.0f} M{x1:.0f} {y1:.0f} L{x3:.0f} {y3:.0f}" style="fill:none;stroke:var(--dk5);stroke-width:6;stroke-linecap:round"/>')
    return ''.join(out)

text('Glycogen — stored in liver for the blood, in muscle for itself', 180, 150, 'dyn-big')
text('alternate fasting and exercise, then block one enzyme', 180, 176, 'dyn-cap')

# ════════ liver ════════
box(160, 210, 1220, 1120)
text('Hepatocyte — fasting: keep the blood glucose up', 190, 250, 'nf-l1')
add(granule(470, 470), unless=O('and'))
add(granule(470, 470, long=True), when=O('and'))
text('glycogen', 470, 640, 'nf-l2', 'middle')
add('<circle cx="470" cy="470" r="150" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3;stroke-dasharray:8 6"/>', when=O('cori', 'vg', 'hers'))
text('limit dextrin — stuck at the branches', 470, 290, 'nf-l1 dyn-tag', 'middle', when=O('cori'))
text('long unbranched chains — fibrosis, infantile cirrhosis', 470, 290, 'nf-l1 dyn-tag', 'middle', when=O('and'))
node('Glucose-6-P', 470, 800)
node('Glucose → blood', 470, 1040, 260)
node('Lactate · urate · TG', 900, 900, 260)
add('<path d="M470 640 V776 M470 824 V1016 M590 810 L800 880" class="dyn-line"/>')
add('<circle cx="960" cy="440" r="80" style="fill:var(--dk11);fill-opacity:.12;stroke:var(--dk11);stroke-width:3"/>', unless=O('pompe'))
add('<circle cx="960" cy="440" r="120" style="fill:var(--dk5);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=O('pompe'))
text('lysosome', 960, 446, 'nf-l2', 'middle')
add(X(470, 920), when=O('vg')); add(X(560, 700), when=O('hers')); add(X(380, 560), when=O('cori')); add(X(620, 420), when=O('and'))
add(X(1040, 360), when=O('pompe'))

# ════════ muscle ════════
box(1260, 210, 2340, 1120)
text('Muscle fiber — exercise: fuel for itself only', 1290, 250, 'nf-l1')
add(granule(1580, 470))
text('glycogen', 1580, 640, 'nf-l2', 'middle')
node('Glucose-6-P', 1580, 800)
node('Fructose-1,6-BP', 1580, 930, 260)
node('Pyruvate → lactate', 1580, 1060, 280)
add('<path d="M1580 640 V776 M1580 824 V906 M1580 954 V1036" class="dyn-line"/>')
# UNVERIFIED: muscle lacking glucose-6-phosphatase is standard teaching; the vongierke card lists liver, kidney and gut only
text('no glucose-6-phosphatase — muscle can’t release glucose', 1900, 800, 'nf-l2', 'middle')
add('<circle cx="2080" cy="440" r="80" style="fill:var(--dk11);fill-opacity:.12;stroke:var(--dk11);stroke-width:3"/>', unless=O('pompe'))
add('<circle cx="2080" cy="440" r="120" style="fill:var(--dk5);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=O('pompe'))
text('lysosome', 2080, 446, 'nf-l2', 'middle')
add(X(1670, 700), when=O('mca')); add(X(1680, 870), when=O('tar')); add(X(2160, 360), when=O('pompe'))
text('lysosomes fill with glycogen — heart, muscle, liver', 1580, 300, 'nf-l1 dyn-tag', 'middle', when=O('pompe'))
text('cramps and myoglobinuria with exercise', 1580, 300, 'nf-l1 dyn-tag', 'middle', when=O('mca', 'tar'))

# blood
shapes.append(dict(vessel='M200 1180 H2300', w=50, color='--dk1'))
text('blood', 2300, 1150, 'nf-l1', 'end')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M470 600 V776', len=176, speed=70, r=7, base=dict(), when=FAST, mods=[m(FAST, set=dict(g=4)), m(O('hers'), set=dict(g=1)), m(O('cori'), set=dict(g=1))]),
  dict(d='M470 824 V1180 H1100', len=1000, speed=130, r=7, base=dict(), when=FAST, mods=[m(FAST, set=dict(glu=5)), m(O('vg'), set=dict(glu=0)), m(O('cori', 'hers'), set=dict(glu=2))]),
  dict(d='M590 810 L800 880', len=220, speed=70, r=7, base=dict(), when=O('vg'), mods=[m(O('vg'), set=dict(lac=5))]),
  dict(d='M1580 600 V776', len=176, speed=80, r=7, base=dict(), when=EX, mods=[m(EX, set=dict(g=5)), m(O('mca'), set=dict(g=0))]),
  dict(d='M1580 824 V1036', len=212, speed=90, r=7, base=dict(), when=EX, mods=[m(EX, set=dict(g=4)), m(O('mca', 'tar'), set=dict(g=0))]),
  dict(d='M1580 1084 V1180 H2280', len=800, speed=130, r=7, base=dict(), when=EX, mods=[m(EX, set=dict(lac=5)), m(O('mca', 'tar'), set=dict(lac=0))]),
]
sites = [
  dict(x=470, y=920, n=[1, 0], w=20, t='md', l='Glucose-6-phosphatase', s='liver, kidney · von Gierke', c='vongierke', ions=[], block=O('vg'), lx=520, ly=930, la='start'),
  dict(x=560, y=700, n=[1, 0], w=20, t='md', l='Liver phosphorylase', s='Hers', c='hers', ions=[], block=O('hers'), lx=610, ly=710, la='start'),
  dict(x=1670, y=700, n=[1, 0], w=20, t='md', l='Myophosphorylase', s='McArdle', c='mcardle', ions=[], block=O('mca'), lx=1720, ly=710, la='start'),
  dict(x=1680, y=870, n=[1, 0], w=20, t='md', l='PFK-1 (muscle)', s='Tarui', c='tarui', ions=[], block=O('tar'), lx=1730, ly=880, la='start'),
]

readouts = [
  dict(l='Fasting glucose', mods=[dict(when=O('vg', 'cori', 'hers'), d=-1), dict(when=O('pompe', 'mca'), d=0)]),
  dict(l='Lactate (at rest)', mods=[dict(when=O('vg'), d=1), dict(when=O('cori'), d=0)]),
  dict(l='Uric acid · triglycerides', mods=[dict(when=O('vg'), d=1), dict(when=O('cori'), d=0)]),
  dict(l='Liver size', mods=[dict(when=O('vg', 'cori', 'hers', 'and', 'pompe'), d=1)]),
  dict(l='Lactate rise with exercise', mods=[dict(when=O('mca', 'tar'), d=-1)]),
  dict(l='CK', mods=[dict(when=O('mca'), d=1)]),
]

notes = {
  '': 'Liver glycogen keeps the blood glucose up during fasting — it alone has glucose-6-phosphatase. Muscle glycogen fuels the '
      'muscle itself through glycolysis. Each storage disease blocks one enzyme in one of these tissues.',
  'st:fast': 'Fasting: liver phosphorylase and the debranching enzyme break glycogen to G6P, and glucose-6-phosphatase releases free '
             'glucose into the blood.',
  'st:ex': 'Exercise: myophosphorylase breaks muscle glycogen to G6P, which runs through PFK-1 and glycolysis to lactate in the '
           'early anaerobic burst.',
  'gsd:vg': 'von Gierke (GSD I, glucose-6-phosphatase): glucose can’t leave the liver, so severe fasting hypoglycemia, with G6P '
            'shunted to lactate, urate and triglycerides; huge liver and kidneys. Frequent cornstarch; avoid fructose and galactose.',
  'gsd:pompe': 'Pompe (GSD II, lysosomal acid α-1,4-glucosidase): glycogen fills lysosomes of heart, muscle and liver — infantile '
               'hypertrophic cardiomyopathy, floppy baby, macroglossia. Blood glucose is normal. Enzyme replacement.',
  'gsd:cori': 'Cori (GSD III, debranching enzyme): phosphorylase stops near the branches and limit dextrin accumulates — fasting '
              'hypoglycemia and hepatomegaly, but normal lactate and urate because gluconeogenesis works.',
  'gsd:and': 'Andersen (GSD IV, branching enzyme): long unbranched chains are poorly soluble and provoke fibrosis — infantile '
             'cirrhosis, failure to thrive, early death.',
  'gsd:mca': 'McArdle (GSD V, myophosphorylase): muscle can’t use its glycogen — cramps and myoglobinuria with brief intense '
             'exercise, a second wind, flat venous lactate with a normal ammonia rise. Blood glucose normal.',
  'gsd:hers': 'Hers (GSD VI, liver phosphorylase): glycogenolysis fails but gluconeogenesis compensates — hepatomegaly with mild '
              'hypoglycemia, the mildest hepatic GSD.',
  'gsd:tar': 'Tarui (GSD VII, muscle PFK-1): glycolysis is blocked at its committed step in muscle and red cells — McArdle-like '
             'exercise intolerance plus hemolytic anemia.',
}

dyn = dict(
  kinds=dict(g=['g', '--dk5'], glu=['g', '--nf-glu'], lac=['lac', '--bad']), groups=[['g', 'Glycogen & glucose'], ['lac', 'Lactate']],
  switches=[dict(id='st', label='The body is…', type='steps', auto=4, options=[['fast', 'Fasting (liver)'], ['ex', 'Exercising (muscle)']]),
            dict(id=SW, label='Missing enzyme', type='one', options=[
    ['vg', 'von Gierke — glucose-6-phosphatase', 'vongierke'], ['pompe', 'Pompe — acid maltase', 'pompe'], ['cori', 'Cori — debranching', 'cori'],
    ['and', 'Andersen — branching', 'andersen'], ['mca', 'McArdle — myophosphorylase', 'mcardle'], ['hers', 'Hers — liver phosphorylase', 'hers'],
    ['tar', 'Tarui — muscle PFK-1', 'tarui']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 84–85 · Marks ch 26')

MAP = dict(
  id='gsdsim', title='Glycogen Storage Diseases in Motion', topic='bio', after='core',
  sub='Liver releases glucose while fasting, muscle burns its own glycogen while exercising — block glucose-6-phosphatase, acid '
      'maltase, debranching or branching enzyme, myophosphorylase, liver phosphorylase or PFK and watch what stalls and what piles up',
  w=3500, h=1480,
  fa='84–85',
  src=[full('Marks', 26), full('Robbins', 5), full('Robbins', 27)],
  lanes=[('gsLiver', 'Liver GSDs', 'glycolysis'), ('gsMuscle', 'Muscle GSDs', 'tca'), ('gsLyso', 'Lysosomal', 'gluconeo')],
  nodes=[
    ('gs1', 'von Gierke (I)', 330, 1290, 'gsLiver', 'glucose-6-phosphatase', ['vongierke'], 'hub'),
    ('gs2', 'Cori (III)', 700, 1290, 'gsLiver', 'debranching', ['cori']),
    ('gs3', 'Andersen (IV)', 1060, 1290, 'gsLiver', 'branching', ['andersen']),
    ('gs4', 'Hers (VI)', 1420, 1290, 'gsLiver', 'liver phosphorylase', ['hers']),
    ('gs5', 'McArdle (V)', 330, 1410, 'gsMuscle', 'myophosphorylase', ['mcardle']),
    ('gs6', 'Tarui (VII)', 700, 1410, 'gsMuscle', 'muscle PFK-1', ['tarui']),
    ('gs7', 'Pompe (II)', 1060, 1410, 'gsLyso', 'acid maltase', ['pompe'])],
  panels=[
    (2420, PANY, 1000, 'Telling them apart (First Aid pp. 84–85)', [
      ('Hypoglycemia + ↑ lactate', 'von Gierke'),
      ('Hypoglycemia, normal lactate', 'Cori'),
      ('Cardiomyopathy, normal glucose', 'Pompe'),
      ('Cramps, flat lactate curve', 'McArdle'),
      ('McArdle + hemolysis', 'Tarui'),
      ('Infantile cirrhosis', 'Andersen')])],
  dyn=dyn)
