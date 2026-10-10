# Fructose, Galactose & Sorbitol in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Three short pathways with metabolites flowing: fructose → (fructokinase) F1P → (aldolase B) trioses → glycolysis;
# lactose → galactose → (galactokinase) Gal-1-P → (GALT) glucose-1-P, with aldose reductase turning spare galactose into
# galactitol in the lens; and glucose → (aldose reductase, NADPH) sorbitol → (sorbitol dehydrogenase) fructose. A `one`
# switch blocks a step: hereditary fructose intolerance, essential fructosuria, classic galactosemia, galactokinase
# deficiency, and the hyperglycemia of diabetes. 6 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
PANY = 1180
BW = 240
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(x, y, lab):
    add(f'<rect x="{x - BW // 2}" y="{y - 30}" width="{BW}" height="60" rx="26" class="dyn-cell"/>'); text(lab, x, y + 6, 'nf-l1', 'middle')
def link(x0, x1, y, lab, lx=None):
    add(f'<path d="M{x0 + BW // 2} {y} H{x1 - BW // 2}" class="dyn-line"/>')
    if lab: text(lab, lx or (x0 + x1) // 2, y - 16, 'nf-l2', 'middle')
def pile(x, y, when):
    add(''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="11" style="fill:var(--dk1);opacity:.8"/>'
                for dx, dy in ((-40, 0), (-14, -6), (12, -2), (38, 2), (-26, -24), (0, -28), (26, -24))), when=when)
def outcome(x, y, lab, when, w=330):
    add(f'<rect x="{x - w // 2}" y="{y - 28}" width="{w}" height="56" rx="20" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:3"/>', when=when)
    text(lab, x, y + 6, 'nf-l1', 'middle', when=when)

text('Fructose, galactose and sorbitol — where each block traps the sugar', 180, 150, 'dyn-big')
text('a stack = what accumulates · red box = the consequence', 180, 176, 'dyn-cap')

# fructose
YF = 400
node(400, YF, 'Fructose'); node(900, YF, 'Fructose-1-P'); node(1400, YF, 'DHAP + glyceraldehyde'); node(1900, YF, '→ glycolysis')
link(400, 900, YF, 'fructokinase'); link(900, 1400, YF, 'aldolase B'); link(1400, 1900, YF, '')
add(X(650, YF), when=O('essf')); add(X(1150, YF), when=O('hfi'))
pile(400, YF - 40, O('essf')); pile(900, YF - 40, O('hfi'))
outcome(400, YF + 120, 'fructose in the urine — benign', O('essf'))
outcome(900, YF + 120, 'Pi trapped → ATP ↓ → hypoglycemia', O('hfi'), 380)
text('at weaning: fruit, juice, honey, sucrose', 900, YF + 175, 'nf-l1 dyn-tag', 'middle', when=O('hfi'))

# galactose
YG = 760
node(400, YG, 'Lactose (milk)'); node(900, YG, 'Galactose'); node(1400, YG, 'Galactose-1-P'); node(1900, YG, 'Glucose-1-P')
link(400, 900, YG, 'lactase'); link(900, 1400, YG, 'galactokinase'); link(1400, 1900, YG, 'GALT')
node(900, YG + 200, 'Galactitol')
add(f'<path d="M900 {YG + 30} V{YG + 170}" class="dyn-line"/>'); text('aldose reductase', 920, YG + 105, 'nf-l2')
add(f'<ellipse cx="560" cy="{YG + 200}" rx="80" ry="50" style="fill:var(--nf-h2o);fill-opacity:.2;stroke:var(--dk7);stroke-width:3"/>')
text('lens', 560, YG + 206, 'nf-l1', 'middle')
add(f'<ellipse cx="560" cy="{YG + 200}" rx="80" ry="50" style="fill:var(--ink-3);fill-opacity:.5"/>', when=O('galt', 'galk', 'dm'))
add(X(1150, YG), when=O('galk')); add(X(1650, YG), when=O('galt'))
pile(900, YG - 40, O('galk', 'galt')); pile(1400, YG - 40, O('galt'))
outcome(1400, YG + 120, 'liver and kidney injury · E. coli sepsis', O('galt'), 400)
outcome(560, YG + 300, 'infantile cataracts', O('galt', 'galk'), 260)
text('cataracts only — “Kid can’t see”', 1400, YG + 120, 'nf-l1 dyn-tag', 'middle', when=O('galk'))

# polyol
YP = 1240
node(400, YP, 'Glucose'); node(900, YP, 'Sorbitol'); node(1400, YP, 'Fructose')
link(400, 900, YP, 'aldose reductase · NADPH'); link(900, 1400, YP, 'sorbitol dehydrogenase')
add(f'<rect x="1700" y="{YP - 60}" width="520" height="120" rx="24" class="dyn-soft"/>')
text('Schwann cells · lens · retina · kidney', 1960, YP - 10, 'nf-l1', 'middle')
text('little or no sorbitol dehydrogenase', 1960, YP + 20, 'nf-l2', 'middle')
add(X(1150, YP), when=O('dm'))
pile(900, YP - 40, O('dm'))
outcome(900, YP + 120, 'osmotic damage: neuropathy, cataracts, retinopathy', O('dm'), 500)

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def fl(x0, x1, y, n, stop=None, when=None, k='s', boost=None):
    f = dict(d=f'M{x0} {y} H{x1}', len=abs(x1 - x0), speed=70, r=8, base={k: n}, mods=[])
    if boost: f['mods'].append(m(boost, set={k: 6}))
    if stop: f['mods'].append(m(stop, set={k: 0}))
    if when: f['when'] = when
    return f
flows = [
  fl(520, 780, YF, 3, stop=O('essf')), fl(1020, 1280, YF, 3, stop=O('essf', 'hfi')), fl(1520, 1780, YF, 3, stop=O('essf', 'hfi')),
  dict(d=f'M400 {YF + 30} V{YF + 92}', len=62, speed=40, r=8, base=dict(bad=3), when=O('essf')),
  fl(520, 780, YG, 3), fl(1020, 1280, YG, 3, stop=O('galk')), fl(1520, 1780, YG, 3, stop=O('galk', 'galt')),
  dict(d=f'M900 {YG + 30} V{YG + 170}', len=140, speed=60, r=8, base=dict(s=1), mods=[m(O('galt', 'galk'), set=dict(s=5))]),
  dict(d=f'M780 {YG + 200} H640', len=140, speed=50, r=8, base=dict(bad=3), when=O('galt', 'galk')),
  fl(520, 780, YP, 1, boost=O('dm')), fl(1020, 1280, YP, 1, stop=O('dm')),
]
sites = [dict(x=1210, y=YF, n=[0, 1], w=10, t='rec', l='', aria='Aldolase B', c='hfi', ions=[]),
         dict(x=1710, y=YG, n=[0, 1], w=10, t='rec', l='', aria='GALT', c='galactosemia', ions=[]),
         dict(x=710, y=YP, n=[0, 1], w=10, t='rec', l='', aria='Aldose reductase', c='polyol', ions=[])]

readouts = [
  dict(l='Blood glucose', mods=[dict(when=O('hfi'), d=-1), dict(when=O('dm'), d=1)]),
  dict(l='Urine reducing substances', mods=[dict(when=O('hfi', 'essf', 'galt', 'galk'), d=1)]),
  dict(l='Blood phosphate', mods=[dict(when=O('hfi'), d=-1)]),
  dict(l='Uric acid', mods=[dict(when=O('hfi'), d=1)]),
  dict(l='Liver injury', mods=[dict(when=O('hfi', 'galt'), d=1), dict(when=O('galk', 'essf'), d=0)]),
  dict(l='Cataracts', mods=[dict(when=O('galt', 'galk', 'dm'), d=1)]),
]

notes = {
  '': 'Fructose is trapped by fructokinase and split by aldolase B; galactose by galactokinase and GALT; glucose can be reduced to '
      'sorbitol by aldose reductase. Which enzyme is missing decides whether the trapped sugar is harmless or toxic.',
  'dx:hfi': 'Hereditary fructose intolerance (aldolase B): fructokinase still makes fructose-1-P, which can’t be split. F1P sequesters '
            'phosphate, ATP falls, glycogenolysis and gluconeogenesis stop — vomiting and hypoglycemia at weaning; ↓ phosphate, ↑ uric '
            'acid, liver failure, Fanconi. Remove fructose, sucrose and sorbitol.',
  'dx:essf': 'Essential fructosuria (fructokinase): fructose is never phosphorylated, nothing toxic builds up — it simply spills into '
             'the urine. Benign.',
  'dx:galt': 'Classic galactosemia (GALT): galactose-1-P is toxic to liver and kidney, and spare galactose becomes galactitol in the lens '
             '— vomiting, jaundice, hepatomegaly, infantile cataracts, E. coli sepsis in a newborn on milk. Exclude lactose.',
  'dx:galk': 'Galactokinase deficiency: galactose piles up and becomes galactitol, but with no galactose-1-P there is no liver or kidney '
             'injury — infantile cataracts only.',
  'dx:dm': 'Hyperglycemia (diabetes): aldose reductase turns glucose into sorbitol, using NADPH. Schwann cells, lens, retina and kidney '
           'have little sorbitol dehydrogenase, so sorbitol is trapped — osmotic damage: neuropathy, cataracts, retinopathy, nephropathy.',
}

dyn = dict(
  kinds=dict(s=['sugar', '--dk2'], bad=['spill', '--bad']), groups=[['sugar', 'Sugar flow'], ['spill', 'Where it ends up']],
  switches=[dict(id='dx', label='Block', type='one', options=[
    ['hfi', 'Hereditary fructose intolerance', 'hfi'], ['essf', 'Essential fructosuria', 'essfruct'],
    ['galt', 'Classic galactosemia (GALT)', 'galactosemia'], ['galk', 'Galactokinase deficiency', 'galactokinase'],
    ['dm', 'Hyperglycemia (polyol pathway)', 'polyol']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 78–79 · Marks ch 22')

MAP = dict(
  id='sugarsim', title='Fructose & Galactose in Motion', topic='bio', after='core',
  sub='Send fructose, galactose and glucose down their side pathways and block a step — hereditary fructose intolerance vs essential '
      'fructosuria, classic galactosemia vs galactokinase deficiency, and sorbitol trapped in the lens and nerves in diabetes',
  w=3600, h=1900,
  fa='78, 79, 709',
  src=['Marks ch 22 — Generation of Adenosine Triphosphate from Glucose, Fructose, and Galactose: Glycolysis',
       'Robbins ch 10 — Diseases of infancy and childhood'],
  lanes=[('sgFru', 'Fructose', 'glycolysis'), ('sgGal', 'Galactose', 'tca'), ('sgPol', 'Polyol pathway', 'gluconeo')],
  nodes=[
    ('sg1', 'Fructose intolerance (HFI)', 330, 1620, 'sgFru', 'aldolase B', ['hfi'], 'hub'),
    ('sg2', 'Essential fructosuria', 760, 1620, 'sgFru', 'benign', ['essfruct']),
    ('sg3', 'Classic galactosemia', 1200, 1620, 'sgGal', 'GALT · E. coli sepsis', ['galactosemia']),
    ('sg4', 'Galactokinase deficiency', 1640, 1620, 'sgGal', 'cataracts only', ['galactokinase']),
    ('sg5', 'Polyol pathway', 2080, 1620, 'sgPol', 'sorbitol trapped', ['polyol'])],
  panels=[
    (2500, PANY, 1000, 'Kinase vs the next enzyme (First Aid p. 78)', [
      ('Fructokinase', 'essential fructosuria — benign'),
      ('Aldolase B', 'hereditary fructose intolerance — toxic'),
      ('Galactokinase', 'cataracts only'),
      ('GALT', 'liver, kidney, brain + cataracts')])],
  dyn=dyn)
