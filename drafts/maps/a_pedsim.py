# Pedigree Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# One three-generation family drawn as a pedigree (squares male, circles female; filled = affected, dot = carrier). A `steps`
# switch picks the inheritance pattern — autosomal dominant, autosomal recessive, X-linked recessive, X-linked dominant,
# mitochondrial — and the family fills in to match; a second `steps` switch (auto) reveals the generations one at a time
# while the mutant allele travels down the lines from the parent who passes it. 3 readouts. Facts from the pinned cards;
# FA pages in `fa`. The family itself is an illustration — one possible family for each pattern. No new cards.
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

PANY = 1180
MODES = ['ad', 'ar', 'xlr', 'xld', 'mito']
GENS = ['g1', 'g2', 'g3']
SEE = dict(I=['g1', 'g2', 'g3'], II=['g2', 'g3'], III=['g3'])
def W(mode, gen): return [f'mode:{mode}&gen:{g}' for g in SEE[gen]]
def WA(gen): return [f'gen:{g}' for g in SEE[gen]]
Y = dict(I=420, II=760, III=1100)
S = 64
# id: (x, gen, sex)
P = {'I1': (760, 'I', 'm'), 'I2': (1060, 'I', 'f'),
     'II1': (460, 'II', 'm'), 'II2': (760, 'II', 'f'), 'H2': (960, 'II', 'm'), 'II3': (1260, 'II', 'm'), 'W3': (1460, 'II', 'f'),
     'III1': (660, 'III', 'm'), 'III2': (860, 'III', 'f'), 'III3': (1060, 'III', 'm'),
     'III4': (1260, 'III', 'm'), 'III5': (1460, 'III', 'f'), 'III6': (1660, 'III', 'f')}
ST = dict(   # A affected, C carrier, N normal
  ad=dict(I1='A', II1='A', II2='A', III1='A', III2='A'),
  ar=dict(I1='C', I2='C', II1='A', II2='C', H2='C', III1='A', III2='C'),
  xlr=dict(I2='C', II1='A', II2='C', III1='A', III2='C'),
  xld=dict(I1='A', II2='A', III1='A', III2='A'),
  mito=dict(I2='A', II1='A', II2='A', II3='A', III1='A', III2='A', III3='A'))
PASS = dict(  # parent → child edges the mutant allele travels
  ad=[('I1', 'II1'), ('I1', 'II2'), ('II2', 'III1'), ('II2', 'III2')],
  ar=[('I1', 'II1'), ('I2', 'II1'), ('I1', 'II2'), ('II2', 'III1'), ('H2', 'III1'), ('H2', 'III2')],
  xlr=[('I2', 'II1'), ('I2', 'II2'), ('II2', 'III1'), ('II2', 'III2')],
  xld=[('I1', 'II2'), ('II2', 'III1'), ('II2', 'III2')],
  mito=[('I2', 'II1'), ('I2', 'II2'), ('I2', 'II3'), ('II2', 'III1'), ('II2', 'III2'), ('II2', 'III3')])
COUPLE = {'II': [('I1', 'I2')], 'III': [('II2', 'H2'), ('II3', 'W3')]}
KIDS = {('I1', 'I2'): ['II1', 'II2', 'II3'], ('II2', 'H2'): ['III1', 'III2', 'III3'], ('II3', 'W3'): ['III4', 'III5', 'III6']}

text('Pedigree simulator — pick a pattern, watch the family fill in', 180, 150, 'dyn-big')
text('□ male · ○ female · filled = affected · dot = carrier · one possible family for each pattern', 180, 176, 'dyn-cap')
for g, y in Y.items(): text(g, 300, y + 10, 'nf-h', 'middle', when=WA(g))

# ════════ lines ════════
def sym(x, y, sex, style):
    if sex == 'm': return f'<rect x="{x - S // 2}" y="{y - S // 2}" width="{S}" height="{S}" rx="4" style="{style}"/>'
    return f'<circle cx="{x}" cy="{y}" r="{S // 2}" style="{style}"/>'
LINE = 'stroke:var(--ink-2);stroke-width:4;fill:none'
for (a, b), kids in KIDS.items():
    xa, ga, _ = P[a]; xb, _, _ = P[b]; y = Y[ga]
    kg = P[kids[0]][1]; ky = Y[kg]; mid = (xa + xb) // 2
    xs = [P[k][0] for k in kids]
    add(f'<path d="M{xa + S // 2} {y} H{xb - S // 2} M{mid} {y} V{(y + ky) // 2} M{min(xs)} {(y + ky) // 2} H{max(xs)} '
        + ' '.join(f'M{x} {(y + ky) // 2} V{ky - S // 2}' for x in xs) + f'" style="{LINE}"/>', when=WA(kg))
for pid, (x, g, sex) in P.items():
    add(sym(x, Y[g], sex, 'fill:var(--surface);stroke:var(--ink-2);stroke-width:4'), when=WA(g))
    for m in MODES:
        s = ST[m].get(pid, 'N')
        if s == 'A': add(sym(x, Y[g], sex, 'fill:var(--dk1);stroke:var(--ink-2);stroke-width:4'), when=W(m, g))
        if s == 'C': add(f'<circle cx="{x}" cy="{Y[g]}" r="11" style="fill:var(--dk1)"/>', when=W(m, g))
text('marries in', P['H2'][0], Y['II'] + 62, 'nf-l2', 'middle', when=WA('II'))
text('marries in', P['W3'][0], Y['II'] + 62, 'nf-l2', 'middle', when=WA('II'))

TAG = dict(ad=('Autosomal dominant: every generation, both sexes, male-to-male transmission possible', '50% risk to each child of an affected heterozygote'),
           ar=('Autosomal recessive: one generation — affected siblings, carrier parents', 'two carriers: 25% affected, 50% carriers · unaffected sibling: 2/3 carrier'),
           xlr=('X-linked recessive: affected males linked through carrier females — no male-to-male', 'sons of carrier mothers: 50% affected'),
           xld=('X-linked dominant: either sex; an affected father passes it to every daughter, no son', 'children of an affected mother: 50% each'),
           mito=('Mitochondrial: mtDNA comes only from the egg — mother to all children, father to none', 'heteroplasmy: severity varies within the family'))
EX = dict(ad='Huntington, Marfan, NF1/NF2, ADPKD, FAP, familial hypercholesterolemia, hereditary spherocytosis',
          ar='CF, sickle cell, PKU, Wilson, hemochromatosis, thalassemia, glycogen storage diseases',
          xlr='Duchenne/Becker, hemophilia A and B, G6PD, Fabry, Lesch-Nyhan, Bruton, Wiskott-Aldrich',
          xld='fragile X, Alport, hypophosphatemic rickets', mito='MELAS, MERRF, Leber hereditary optic neuropathy')
for m, (a, b) in TAG.items():
    text(a, 1060, 1300, 'nf-l1 dyn-tag', 'middle', when=[f'mode:{m}'])
    text(b, 1060, 1332, 'nf-l1', 'middle', when=[f'mode:{m}'])
    text('e.g. ' + EX[m], 1060, 1364, 'nf-l2', 'middle', when=[f'mode:{m}'])

# ════════ motion: the allele travels ════════
flows = []
for m, edges in PASS.items():
    for a, b in edges:
        xa, ga, _ = P[a]; xb, gb, _ = P[b]
        ya, yb = Y[ga], Y[gb]
        mid_y = (ya + yb) // 2
        d = f'M{xa} {ya + S // 2} V{mid_y} H{xb} V{yb - S // 2}'
        flows.append(dict(d=d, len=abs(yb - ya) + abs(xb - xa), speed=120, r=9, base=dict(al=1), when=W(m, gb)))
sites = [dict(x=1880, y=Y['I'], n=[0, 1], w=10, t='rec', l='', aria='Autosomal dominant', c='adinh', ions=[], when=['mode:ad']),
         dict(x=1880, y=Y['I'], n=[0, 1], w=10, t='rec', l='', aria='Autosomal recessive', c='arinh', ions=[], when=['mode:ar']),
         dict(x=1880, y=Y['I'], n=[0, 1], w=10, t='rec', l='', aria='X-linked recessive', c='xlrinh', ions=[], when=['mode:xlr']),
         dict(x=1880, y=Y['I'], n=[0, 1], w=10, t='rec', l='', aria='X-linked dominant', c='xldinh', ions=[], when=['mode:xld']),
         dict(x=1880, y=Y['I'], n=[0, 1], w=10, t='rec', l='', aria='Mitochondrial inheritance', c='mitoinh', ions=[], when=['mode:mito'])]
text('tap for the card', 1880, Y['I'] + 70, 'nf-l2', 'middle')

readouts = [
  dict(l='Both sexes affected', mods=[dict(when=['mode:ad', 'mode:ar', 'mode:xld', 'mode:mito'], d=1), dict(when=['mode:xlr'], d=-1)]),
  dict(l='Male-to-male transmission', mods=[dict(when=['mode:ad'], d=1), dict(when=['mode:xlr', 'mode:xld', 'mode:mito'], d=-1)]),
  dict(l='Every generation', mods=[dict(when=['mode:ad'], d=1), dict(when=['mode:ar', 'mode:xlr'], d=-1)]),
]

notes = {
  '': 'Read a pedigree by asking three questions: is every generation affected, are both sexes affected, and does an affected father '
      'ever pass it to a son?',
  'mode:ad': 'Autosomal dominant: one mutant allele is enough — often structural genes, pleiotropic and variably expressive. Vertical '
             'transmission in both sexes; male-to-male transmission rules out X-linkage.',
  'mode:ar': 'Autosomal recessive: both alleles lost — usually enzyme deficiencies, severe, in childhood. Horizontal: affected siblings of '
             'unaffected carrier parents; consanguinity raises the risk.',
  'mode:xlr': 'X-linked recessive: males with one mutant X are affected; it skips generations through carrier females. Females are '
              'affected only if homozygous, 45,X, or with skewed lyonization.',
  'mode:xld': 'X-linked dominant: one mutant X causes disease in either sex. Affected father → all daughters, no sons; affected mother → '
              '50% of children.',
  'mode:mito': 'Mitochondrial: mtDNA comes only from the egg, so an affected mother can pass it to all her children and an affected father '
               'to none. Heteroplasmy varies severity; brain and muscle suffer most (ragged red fibers).',
  'gen:g1': 'Generation I — the founders.', 'gen:g2': 'Generation II — the children, and two people who marry in.',
  'gen:g3': 'Generation III — the grandchildren.',
}

dyn = dict(
  kinds=dict(al=['allele', '--bad']), groups=[['allele', 'Mutant allele']],
  switches=[dict(id='mode', label='Pattern', type='steps', options=[
              ['ad', 'Autosomal dominant'], ['ar', 'Autosomal recessive'], ['xlr', 'X-linked recessive'],
              ['xld', 'X-linked dominant'], ['mito', 'Mitochondrial']]),
            dict(id='gen', label='Generations', type='steps', auto=3, options=[['g1', 'I'], ['g2', 'I–II'], ['g3', 'I–III']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 57–60 · Robbins ch 5')

MAP = dict(
  id='pedsim', title='Pedigree Simulator', topic='bio', after='genetics',
  sub='One family, five inheritance patterns: pick autosomal dominant, autosomal recessive, X-linked recessive, X-linked dominant or '
      'mitochondrial and watch the generations fill in as the mutant allele passes down',
  w=3600, h=1900,
  fa='55, 57, 58, 59, 60',
  src=['Robbins ch 5 — Genetic disorders', 'Marks ch 18 — An Introduction to Human Genetics',
       'Marks ch 24 — Oxidative Phosphorylation and Mitochondrial Function'],
  lanes=[('pdAuto', 'Autosomal', 'glycolysis'), ('pdX', 'X-linked', 'tca'), ('pdMito', 'Mitochondrial', 'gluconeo')],
  nodes=[
    ('pd1', 'Autosomal dominant', 330, 1620, 'pdAuto', 'every generation', ['adinh'], 'hub'),
    ('pd2', 'Autosomal recessive', 760, 1620, 'pdAuto', 'siblings, carrier parents', ['arinh']),
    ('pd3', 'X-linked recessive', 1200, 1620, 'pdX', 'no male-to-male', ['xlrinh']),
    ('pd4', 'X-linked dominant', 1640, 1620, 'pdX', 'dad → all daughters', ['xldinh']),
    ('pd5', 'Mitochondrial', 2080, 1620, 'pdMito', 'mother → all', ['mitoinh'])],
  panels=[
    (2500, PANY, 1000, 'Three questions (First Aid pp. 57–60)', [
      ('Every generation?', 'yes: dominant · no: recessive'),
      ('Mostly males?', 'X-linked recessive'),
      ('Father → son?', 'rules out X-linked and mitochondrial'),
      ('Only through the mother?', 'mitochondrial')])],
  dyn=dyn)
