# Pancreatic Endocrine Tumors in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# An islet (α, β, δ cells, plus a VIP-secreting tumor site) beside the duodenum (gastrinoma) and the organs each hormone hits
# — liver, skin, gallbladder, gut, stomach, blood glucose. A `dx` switch grows one tumor and floods its hormone: insulinoma,
# glucagonoma, somatostatinoma (the brake stuck on — insulin, glucagon, gastrin, CCK all fall), VIPoma (WDHA) and
# gastrinoma (Zollinger-Ellison); a `men` toggle shows the MEN1 3 Ps; an `oct` toggle gives octreotide where the card lists
# it. 6 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
IX, IY = 700, 760
CELL = dict(alpha=(IX - 110, IY - 80, 'α · glucagon', '--dk4'), beta=(IX + 30, IY - 120, 'β · insulin', '--dk9'),
            delta=(IX + 120, IY + 60, 'δ · somatostatin', '--dk7'), vip=(IX - 60, IY + 120, 'VIP tumor site', '--dk10'))
OCT = ['dx:gluc&oct', 'dx:som&oct', 'dx:vip&oct']
T = dict(liver=(1500, 420, 'liver'), skin=(1500, 600, 'skin'), gb=(1500, 780, 'gallbladder'), gut=(1500, 960, 'gut'),
         stom=(1500, 1140, 'stomach'), glu=(1900, 600, 'blood glucose'))

text('Pancreatic endocrine tumors — one hormone flooding out', 180, 150, 'dyn-big')
text('an islet and the duodenum on the left · what each hormone hits on the right', 180, 176, 'dyn-cap')

add(f'<circle cx="{IX}" cy="{IY}" r="280" style="fill:var(--dk5);fill-opacity:.06;stroke:var(--dk5);stroke-width:4"/>'); text('islet', IX, IY - 300, 'nf-l1', 'middle')
for k, (x, y, l, c) in CELL.items():
    add(f'<circle cx="{x}" cy="{y}" r="40" style="fill:var({c});fill-opacity:.3;stroke:var({c});stroke-width:3"/>')
    text(l, x, y + 70, 'nf-l2', 'middle')
BIG = dict(ins='beta', gluc='alpha', som='delta', vip='vip')
for d, k in BIG.items():
    x, y, _, c = CELL[k]
    add(f'<circle cx="{x}" cy="{y}" r="90" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:5"/>', when=D(d))
add('<path d="M240 1200 C400 1150 600 1180 800 1230 C1000 1280 1100 1240 1180 1180" style="fill:none;stroke:var(--dk5);stroke-width:46;opacity:.25"/>')
text('duodenum', 360, 1270, 'nf-l1', 'middle')
add('<circle cx="700" cy="1210" r="34" style="fill:var(--dk6);fill-opacity:.3;stroke:var(--dk6);stroke-width:3"/>'); text('G cells · gastrin', 700, 1300, 'nf-l2', 'middle')
add('<circle cx="700" cy="1210" r="80" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:5"/>', when=D('zes'))
for k, (x, y, l) in T.items():
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'); text(l, x + 60, y + 6, 'nf-l1')
HIT = dict(ins=('glu',), gluc=('liver', 'skin', 'glu'), som=('gb', 'gut', 'stom', 'glu'), vip=('gut', 'stom'), zes=('stom', 'gut'))
for d, ks in HIT.items():
    for k in ks:
        x, y, _ = T[k]; add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--bad);fill-opacity:.3"/>', when=D(d), unless=[f'dx:{d}&oct'])
GL = dict(ins='low — Whipple triad', gluc='high', som='high (insulin suppressed)')
for d, s in GL.items(): text(s, 1900, 680, 'nf-l1 dyn-tag', 'middle', when=D(d))
TAG = dict(ins='insulinoma — insulin ↑ and C-peptide ↑ while glucose falls · confusion, sweating · diazoxide or resect',
           gluc='glucagonoma — 6 D’s: dermatitis (necrolytic migratory erythema), diabetes, DVT, declining weight, depression, diarrhea',
           som='somatostatinoma — the brake stuck on: diabetes, gallstones (no CCK), steatorrhea, achlorhydria (no gastrin)',
           vip='VIPoma — WDHA: watery diarrhea that continues fasting, hypokalemia, achlorhydria · “pancreatic cholera”',
           zes='gastrinoma (Zollinger-Ellison) — multiple refractory ulcers in duodenum and jejunum; gastrin rises after secretin')
for k, s in TAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('octreotide (a somatostatin analogue) quiets the tumor’s hormone', 1100, 1520, 'nf-l1', 'middle', when=OCT)
for x, y, l in ((300, 360, 'pituitary'), (300, 520, 'parathyroids')):
    add(f'<circle cx="{x}" cy="{y}" r="40" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/>', when=['men'])
    text(l, x + 56, y + 6, 'nf-l1', when=['men'])
text('MEN1 — the 3 Ps: parathyroid, pituitary, pancreas (gastrinoma, insulinoma)', 640, 270, 'nf-l1 dyn-tag', 'middle', when=['men'])

# ════════ motion ════════
def go(src, tgt, kind, d, n=4):
    (x0, y0), (x1, y1) = src, T[tgt][:2]
    return dict(d=f'M{x0} {y0} C{(x0 + x1) / 2:.0f} {y0} {(x0 + x1) / 2:.0f} {y1} {x1 - 44} {y1}', len=900, speed=130, r=9,
                base={kind: n}, when=D(d), mods=[dict(when=[f'dx:{d}&oct'], set={kind: 1})])
B = lambda k: CELL[k][:2]
flows = [go(B('beta'), 'glu', 'ins', 'ins'), go(B('alpha'), 'liver', 'glc', 'gluc'), go(B('alpha'), 'skin', 'glc', 'gluc', 2),
         go(B('delta'), 'gb', 'som', 'som'), go(B('delta'), 'stom', 'som', 'som', 2), go(B('delta'), 'gut', 'som', 'som', 2),
         go(B('vip'), 'gut', 'vipk', 'vip'), go(B('vip'), 'stom', 'vipk', 'vip', 2), go((700, 1210), 'stom', 'gas', 'zes'),
         dict(d='M1544 960 C1600 1000 1620 1060 1640 1120', len=200, speed=140, r=9, base=dict(h2o=4), when=D('vip'),
              mods=[dict(when=['dx:vip&oct'], set=dict(h2o=1))]),
         dict(d=f'M{IX} {IY} C{IX + 150} {IY - 100} {IX + 200} {IY - 50} {IX + 250} {IY}', len=300, speed=60, r=7, base=dict(blood=3), unless=['dx:*'])]
sites = [dict(x=IX + 90, y=IY - 170, n=[1, -1], w=10, t='rec', l='', aria='Insulinoma', c='insulinoma', ions=[]),
         dict(x=IX - 170, y=IY - 130, n=[-1, -1], w=10, t='rec', l='', aria='Glucagonoma', c='glucagonoma', ions=[]),
         dict(x=IX + 180, y=IY + 100, n=[1, 1], w=10, t='rec', l='', aria='Somatostatinoma', c='somatostatinoma', ions=[]),
         dict(x=IX - 120, y=IY + 180, n=[-1, 1], w=10, t='rec', l='', aria='VIPoma', c='vipoma', ions=[]),
         dict(x=780, y=1180, n=[1, -1], w=10, t='rec', l='', aria='Zollinger-Ellison', c='zes', ions=[]),
         dict(x=240, y=440, n=[-1, 0], w=10, t='rec', l='', aria='MEN', c='men', ions=[])]

readouts = [
  dict(l='Blood glucose', mods=[dict(when=D('ins'), d=-1), dict(when=D('gluc', 'som'), d=1)]),
  dict(l='C-peptide', mods=[dict(when=D('ins'), d=1)]),
  dict(l='Gastric acid', mods=[dict(when=D('zes'), d=1), dict(when=D('som', 'vip'), d=-1)]),
  dict(l='Stool volume', mods=[dict(when=D('vip', 'zes', 'som', 'gluc'), d=1)]),
  dict(l='Serum K⁺', mods=[dict(when=D('vip'), d=-1)]),
  dict(l='Gallstones', mods=[dict(when=D('som'), d=1)]),
]

notes = {
  '': 'Each islet cell makes one hormone: α glucagon, β insulin, δ somatostatin (the universal brake); G cells in the duodenum '
      'make gastrin. A tumor of one floods its hormone. Pick one.',
  'dx:ins': 'Insulinoma: insulin secreted whatever the glucose — Whipple triad; insulin ↑, C-peptide ↑, proinsulin ↑ (injected '
            'insulin: C-peptide ↓; a sulfonylurea screen separates the drug). ~10% MEN1. Resect; diazoxide.',
  'dx:gluc': 'Glucagonoma: α-cell glucagon drives glycogenolysis and gluconeogenesis — 6 D’s: necrolytic migratory erythema, '
             'diabetes, DVT, declining weight, depression, diarrhea; anemia. Resect; octreotide.',
  'dx:som': 'Somatostatinoma: the brake stuck on — insulin, glucagon, gastrin, CCK, secretin and enzymes all suppressed: diabetes, '
            'gallstones, steatorrhea, achlorhydria. Resect; octreotide.',
  'dx:vip': 'VIPoma: VIP raises cAMP in the gut epithelium (like cholera) and inhibits acid — WDHA: watery diarrhea that continues '
            'fasting, hypokalemia, achlorhydria; flushing. Octreotide, fluids and K⁺; resect.',
  'dx:zes': 'Zollinger-Ellison: a gastrinoma (duodenum, else pancreas) drives relentless acid — multiple refractory ulcers, '
            'diarrhea, steatorrhea (acid inactivates enzymes). Gastrin rises after secretin. PPIs. MEN1.',
  'men': 'MEN1 (menin, chromosome 11): Parathyroid, Pituitary (prolactinoma), Pancreas (gastrinoma, insulinoma). MEN2A/2B are RET.',
}

dyn = dict(
  kinds=dict(ins=['mov', '--dk9'], glc=['mov', '--dk4'], som=['mov', '--dk7'], vipk=['mov', '--dk10'], gas=['mov', '--dk6'],
             h2o=['mov', '--nf-h2o'], blood=['mov', '--nf-blood']),
  groups=[['mov', 'Hormones · water']],
  switches=[dict(id='dx', label='Tumor', type='one', options=[
              ['ins', 'Insulinoma', 'insulinoma'], ['gluc', 'Glucagonoma', 'glucagonoma'], ['som', 'Somatostatinoma', 'somatostatinoma'],
              ['vip', 'VIPoma', 'vipoma'], ['zes', 'Gastrinoma (ZES)', 'zes']]),
            dict(id='men', label='Syndrome', type='toggle', on='MEN1 shown', off='Show MEN1', def_=False),
            dict(id='oct', label='Drug', type='toggle', on='Octreotide given', off='Octreotide', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 24')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='netsim', title='Pancreatic Endocrine Tumors in Motion', topic='endo', after='pancreas',
  sub='Grow an insulinoma, glucagonoma, somatostatinoma, VIPoma or gastrinoma and watch its one hormone flood the liver, skin, '
      'gut, stomach and blood glucose — then show MEN1 and give octreotide',
  w=3600, h=1900,
  fa='338, 356, 357, 378',
  src=['Robbins ch 24 — The endocrine system', 'Katzung ch 62 — Drugs Used in the Treatment of Gastrointestinal Diseases'],
  lanes=[('ntIslet', 'Islet tumors', 'tca'), ('ntGut', 'Gut & syndrome', 'glycolysis')],
  nodes=[
    ('nt1', 'Insulinoma', 330, 1720, 'ntIslet', 'C-peptide ↑', ['insulinoma'], 'hub'),
    ('nt2', 'Glucagonoma', 760, 1720, 'ntIslet', '6 D’s', ['glucagonoma']),
    ('nt3', 'Somatostatinoma', 1200, 1720, 'ntIslet', 'brake stuck on', ['somatostatinoma']),
    ('nt4', 'VIPoma', 1640, 1720, 'ntIslet', 'WDHA', ['vipoma']),
    ('nt5', 'Zollinger-Ellison', 2080, 1720, 'ntGut', 'gastrin · secretin', ['zes']),
    ('nt6', 'Multiple endocrine neoplasia', 2520, 1720, 'ntGut', 'MEN1 3 Ps', ['men'])],
  panels=[
    (2500, PANY, 1000, 'Tumor → hormone → clue (Robbins ch 24)', [
      ('Insulinoma', 'insulin — hypoglycemia, C-peptide ↑'), ('Glucagonoma', 'glucagon — migratory erythema'),
      ('Somatostatinoma', 'somatostatin — gallstones, steatorrhea'), ('VIPoma', 'VIP — WDHA'), ('Gastrinoma', 'gastrin — ulcers')])],
  dyn=dyn)
