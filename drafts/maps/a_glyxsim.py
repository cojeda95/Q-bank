# Glycolysis Odds & Ends in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Glycolysis down the middle (glucose → pyruvate), lactate on the left, pyruvate carboxylase to oxaloacetate and the TCA cycle on
# the right, with 2,3-BPG and the F-2,6-BP side branch. A `hor` stepper flips fed (insulin: PFK-2 on, F-2,6-BP up, glycolysis) and
# fasting (glucagon: FBPase-2 on, F-2,6-BP down, PEPCK carries OAA back to PEP, gluconeogenesis). An `x` switch adds one odd hit:
# red-cell hexokinase or pyruvate kinase deficiency, pyruvate carboxylase or biotin deficiency, ethanol's NADH excess, an IDH
# mutation (2-hydroxyglutarate) or an SDH mutation (succinate → HIF). Schematic. 6 readouts. Fact-checked m47 (FA, Marks, Robbins);
# the fluoride/enolase option was replaced by pyruvate kinase deficiency (no corpus source for fluoride). No new cards.
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

X = lambda *k: [f'x:{x}' for x in k]
PANY = 1180
GX = 700
STEPS = [('glucose', 300), ('glucose-6-P', 420), ('fructose-6-P', 540), ('fructose-1,6-BP', 660), ('1,3-BPG', 780),
         ('2-phosphoglycerate', 900), ('PEP', 1020), ('pyruvate', 1140)]
Y = {l: y for l, y in STEPS}
TX, TY, TR = 1500, 1000, 220

text('Glycolysis odds & ends — the switch, the poisons, the cofactor and the oncometabolites', 180, 150, 'dyn-big')
text('glycolysis down the middle · lactate left · pyruvate carboxylase and the TCA cycle right · schematic', 180, 176, 'dyn-cap')
for l, y in STEPS:
    add(f'<rect x="{GX - 120}" y="{y - 26}" width="240" height="52" rx="20" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>')
    text(l, GX, y + 6, 'nf-l1', 'middle')
for (a, ya), (b, yb) in zip(STEPS, STEPS[1:]):
    add(f'<path d="M{GX} {ya + 26} V{yb - 26}" style="stroke:var(--ink-3);stroke-width:4"/>')
text('hexokinase', GX - 140, 366, 'nf-l2', 'end'); text('PFK-1', GX - 140, 606, 'nf-l2', 'end'); text('enolase', GX - 140, 966, 'nf-l2', 'end')
# F-2,6-BP side branch
add(f'<path d="M{GX + 120} {Y["fructose-6-P"]} H{GX + 300}" style="stroke:var(--ink-3);stroke-width:4;stroke-dasharray:10 8"/>')
text('PFK-2 / FBPase-2', GX + 210, Y['fructose-6-P'] - 14, 'nf-l2', 'middle')
add(f'<circle cx="{GX + 380}" cy="{Y["fructose-6-P"]}" r="70" style="fill:var(--dk4);fill-opacity:.35;stroke:var(--dk4);stroke-width:4"/>', when=['hor:fed'])
add(f'<circle cx="{GX + 380}" cy="{Y["fructose-6-P"]}" r="30" style="fill:var(--dk4);fill-opacity:.2;stroke:var(--dk4);stroke-width:3"/>', when=['hor:fast'])
text('F-2,6-BP', GX + 380, Y['fructose-6-P'] + 100, 'nf-l1', 'middle')
add(f'<path d="M{GX + 330} {Y["fructose-6-P"] + 50} Q{GX + 250} 620 {GX + 130} 610" style="fill:none;stroke:var(--ok);stroke-width:6"/>', when=['hor:fed'])
text('+ PFK-1, − FBPase-1', GX + 160, 700, 'nf-l2', when=['hor:fed'])
# 2,3-BPG branch
add(f'<path d="M{GX - 120} {Y["1,3-BPG"]} H{GX - 330}" style="stroke:var(--ink-3);stroke-width:4;stroke-dasharray:10 8"/>')
add(f'<rect x="{GX - 520}" y="{Y["1,3-BPG"] - 26}" width="190" height="52" rx="20" style="fill:var(--surface);stroke:var(--nf-blood);stroke-width:3"/>')
text('2,3-BPG (RBC)', GX - 425, Y['1,3-BPG'] + 6, 'nf-l1', 'middle')
# lactate, OAA, TCA
add(f'<rect x="{GX - 520}" y="{Y["pyruvate"] - 26}" width="190" height="52" rx="20" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>')
text('lactate', GX - 425, Y['pyruvate'] + 6, 'nf-l1', 'middle')
add(f'<path d="M{GX - 120} {Y["pyruvate"]} H{GX - 330}" style="stroke:var(--ink-3);stroke-width:4"/>')
add(f'<path d="M{GX + 120} {Y["pyruvate"]} H{TX - TR - 10}" style="stroke:var(--ink-3);stroke-width:4"/>')
text('pyruvate carboxylase (biotin)', GX + 300, Y['pyruvate'] - 14, 'nf-l2', 'middle')
add(f'<circle cx="{TX}" cy="{TY}" r="{TR}" style="fill:none;stroke:var(--dk3);stroke-width:6;opacity:.6"/>')
text('TCA cycle', TX, TY + 6, 'nf-l1', 'middle')
# all eight intermediates, as on Core Carbon (pyruvate carboxylase feeds oxaloacetate at the left, then clockwise)
TCA = [('oxaloacetate', 180), ('citrate', 225), ('isocitrate', 270), ('α-ketoglutarate', 315), ('succinyl-CoA', 0), ('succinate', 45),
       ('fumarate', 90), ('malate', 135)]
import math
P = {}
for l, a in TCA:
    x, y = TX + TR * math.cos(math.radians(a)), TY + TR * math.sin(math.radians(a)); P[l] = (x, y)
    add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" style="fill:var(--dk3);opacity:.7"/>')
    text(l, x + (24 if x >= TX else -24), y + (36 if y > TY + 50 else -20 if y < TY - 50 else 6), 'nf-l2', 'start' if x >= TX else 'end')
text('IDH', P['isocitrate'][0] + 60, (P['isocitrate'][1] + P['α-ketoglutarate'][1]) / 2, 'nf-l2')
text('SDH = complex II', TX + 150, TY + 300, 'nf-l2', 'middle')
mx, my = P['malate']
add(f'<circle cx="{mx:.0f}" cy="{my:.0f}" r="34" style="fill:var(--dk10);fill-opacity:.4"/>', when=X('etoh'))   # NADH pushes OAA → malate
# hits
add(f'<path d="M{GX - 30} 340 l60 40 m0 -40 l-60 40" style="stroke:var(--bad);stroke-width:10"/>', when=X('hk'))
add(f'<path d="M{GX - 30} 1060 l60 40 m0 -40 l-60 40" style="stroke:var(--bad);stroke-width:10"/>', when=X('pk'))
add(f'<rect x="{GX - 540}" y="{Y["1,3-BPG"] - 46}" width="230" height="92" rx="30" class="dyn-hl" style="fill:none"/>', when=X('pk'))
text('2,3-BPG ↑ 2–3× → right shift', GX - 425, Y['1,3-BPG'] + 76, 'nf-l2', 'middle', when=X('pk'))
text('pyruvate kinase', GX - 140, 1086, 'nf-l2', 'end')
# fasting: PEPCK carries oxaloacetate back to PEP (the bypass of pyruvate kinase)
PEPCK = f'M{TX - TR} {TY} C{TX - TR - 30} 1070 1000 1060 {GX + 120} {Y["PEP"] + 10}'
add(f'<path d="{PEPCK}" style="fill:none;stroke:var(--dk4);stroke-width:4;stroke-dasharray:10 8"/>', when=['hor:fast'])
text('PEPCK (OAA → PEP)', 1060, 1038, 'nf-l2', 'middle', when=['hor:fast'])
add(f'<path d="M{GX + 270} {Y["pyruvate"] - 30} l60 60 m0 -60 l-60 60" style="stroke:var(--bad);stroke-width:10"/>', when=X('pc'))
add(f'<rect x="{GX - 560}" y="1300" width="260" height="70" rx="24" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--dk10);stroke-width:3"/>', when=X('etoh'))
text('ethanol → acetaldehyde → acetate', GX - 430, 1342, 'nf-l2', 'middle', when=X('etoh'))
text('NADH ↑ : NAD⁺', GX - 430, 1410, 'nf-l1', 'middle', when=X('etoh'))
ax, ay = P['α-ketoglutarate']
add(f'<circle cx="{ax + 220:.0f}" cy="{ay:.0f}" r="50" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=X('idh'))
text('2-HG', ax + 220, ay + 6, 'nf-l1', 'middle', when=X('idh'))
sx, sy = P['succinate']
add(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="40" style="fill:var(--bad);fill-opacity:.45"/>', when=X('sdh'))
add(f'<rect x="{sx + 150:.0f}" y="{sy + 140:.0f}" width="180" height="60" rx="20" style="fill:var(--bad);fill-opacity:.2;stroke:var(--bad);stroke-width:3"/>', when=X('sdh'))
text('HIF-1α → VEGF', sx + 240, sy + 178, 'nf-l2', 'middle', when=X('sdh'))
HTAG = dict(fed='fed — insulin → phosphatase → PFK-2 on → F-2,6-BP up → PFK-1 on, FBPase-1 off → glycolysis',
            fast='fasting — glucagon → cAMP → PKA → FBPase-2 on → F-2,6-BP down → gluconeogenesis')
for k, s in HTAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=[f'hor:{k}'])
XTAG = dict(hk='hexokinase deficiency (RBC) — everything downstream falls, 2,3-BPG too: hemolysis with a left-shifted O₂ curve',
            pk='pyruvate kinase deficiency (RBC) — ↓ ATP, rigid RBCs, hemolysis; intermediates back up, 2,3-BPG ↑: right-shifted O₂ curve',
            pc='pyruvate carboxylase or biotin deficiency — no oxaloacetate: lactic acidosis, hypoglycemia (raw egg whites: avidin)',
            etoh='ethanol — NADH excess turns pyruvate → lactate, OAA → malate: fasting hypoglycemia, lactic acidosis, gout, fatty liver',
            idh='IDH1/2 mutant — α-KG → 2-hydroxyglutarate blocks TET2: glioma (better prognosis), AML, cholangiocarcinoma',
            sdh='SDH mutant — succinate blocks HIF’s proline hydroxylation, HIF stays on: familial paraganglioma, pheochromocytoma')
for k, s in XTAG.items(): text(s, 1100, 1520, 'nf-l1', 'middle', when=X(k))

# ════════ motion ════════
GLY_ON = 'hor:fed&!x:hk&!x:pk'
flows = [dict(d=f'M{GX - 50} 300 V{Y["pyruvate"]}', len=840, speed=130, r=8, base=dict(c=4), when=[GLY_ON]),
         dict(d=f'M{GX - 50} 300 V{Y["PEP"]}', len=720, speed=90, r=8, base=dict(c=2), when=['hor:fed&x:pk']),
         dict(d=f'{PEPCK} L{GX + 50} {Y["PEP"] + 10} V320', len=1480, speed=130, r=8, base=dict(c=3), when=['hor:fast&!x:pc&!x:etoh']),
         dict(d=f'M{GX + 120} {Y["pyruvate"] + 10} H{TX - TR - 10}', len=560, speed=110, r=8, base=dict(c=3), when=['!x:pc']),
         dict(d=f'M{GX - 120} {Y["pyruvate"] + 10} H{GX - 330}', len=210, speed=90, r=8, base=dict(c=3), when=X('pc', 'etoh')),
         dict(d=f'M{GX - 120} {Y["1,3-BPG"] + 10} H{GX - 330}', len=210, speed=80, r=7, base=dict(c=2), when=['!x:hk'],
              mods=[dict(when=X('pk'), set=dict(c=5))]),
         dict(d=f'M{TX - TR} {TY} A{TR} {TR} 0 1 1 {TX + TR} {TY} A{TR} {TR} 0 1 1 {TX - TR} {TY}', len=1380, speed=120, r=7, base=dict(c=3),
              when=['!x:sdh']),
         dict(d=f'M{ax:.0f} {ay:.0f} H{ax + 170:.0f}', len=170, speed=60, r=8, base=dict(onc=3), when=X('idh')),
         dict(d=f'M{sx:.0f} {sy:.0f} L{sx + 150:.0f} {sy + 160:.0f}', len=220, speed=60, r=8, base=dict(onc=3), when=X('sdh')),
         dict(d=f'M{GX - 430} 1300 C{GX - 430} 1240 {GX - 425} 1200 {GX - 425} {Y["pyruvate"] + 26}', len=160, speed=60, r=7,
              base=dict(nadh=3), when=X('etoh'))]
sites = [dict(x=GX - 330, y=330, n=[-1, -1], w=10, t='rec', l='', aria='Hexokinase deficiency', c='hkdef', ions=[]),
         dict(x=GX + 330, y=1080, n=[1, 1], w=10, t='rec', l='', aria='Pyruvate kinase deficiency', c='pkdef', ions=[]),
         dict(x=GX + 500, y=Y['fructose-6-P'] - 60, n=[1, -1], w=10, t='rec', l='', aria='Fructose-2,6-bisphosphate', c='f26bp', ions=[]),
         dict(x=GX + 420, y=Y['pyruvate'] + 60, n=[1, 1], w=10, t='rec', l='', aria='Pyruvate carboxylase deficiency', c='pyrcarb', ions=[]),
         dict(x=GX - 600, y=1240, n=[-1, 1], w=10, t='rec', l='', aria='Ethanol metabolism', c='ethanol', ions=[]),
         dict(x=TX + 330, y=TY - 120, n=[1, -1], w=10, t='rec', l='', aria='IDH mutation', c='idhmut', ions=[]),
         dict(x=TX - 60, y=TY + 330, n=[-1, 1], w=10, t='rec', l='', aria='SDH mutation', c='sdhmut', ions=[])]

readouts = [
  dict(l='Glycolysis', mods=[dict(when=[GLY_ON], d=1), dict(when=['hor:fast', 'x:hk', 'x:pk'], d=-1)]),
  dict(l='Gluconeogenesis', mods=[dict(when=['hor:fast&!x:pc&!x:etoh'], d=1), dict(when=['hor:fed', 'x:pc', 'x:etoh'], d=-1)]),
  dict(l='Blood glucose', mods=[dict(when=['x:pc', 'x:etoh&hor:fast'], d=-1)]),
  dict(l='Lactate', mods=[dict(when=X('pc', 'etoh'), d=1)]),
  dict(l='2,3-BPG', mods=[dict(when=X('hk'), d=-1), dict(when=X('pk'), d=1)]),
  dict(l='Oncometabolite', mods=[dict(when=X('idh', 'sdh'), d=1)]),
]

notes = {
  '': 'Glycolysis runs glucose to pyruvate; pyruvate goes to lactate, or through pyruvate carboxylase to oxaloacetate for gluconeogenesis '
      'and the TCA cycle. F-2,6-BP is not an intermediate: made from F-6-P, it only switches PFK-1 on and FBPase-1 off.',
  'hor:fed': 'Fed: insulin activates a phosphatase; the bifunctional enzyme is dephosphorylated, PFK-2 is active, F-2,6-BP rises, PFK-1 '
             'runs and FBPase-1 is held off — no futile cycle. PFK-1 is also inhibited by ATP and citrate, activated by AMP.',
  'hor:fast': 'Fasting: glucagon → cAMP → PKA phosphorylates the enzyme; FBPase-2 is active, F-2,6-BP falls and gluconeogenesis runs — '
              'pyruvate carboxylase makes OAA and PEPCK turns it back into PEP, bypassing pyruvate kinase.',
  'x:hk': 'Hexokinase deficiency (red cell): a glycolytic-enzyme hemolytic anemia. A block at the first step lowers the intermediates below it, '
          '2,3-BPG included, so the O₂ curve shifts left — the mirror image of pyruvate kinase deficiency (inferred from Marks ch 42).',
  'x:pk': 'Pyruvate kinase deficiency: red-cell ATP falls (by up to half), ion pumps fail, rigid cells hemolyze (burr cells; hemolytic anemia '
          'in a newborn). PEP → pyruvate is blocked, so 2,3-BPG rises 2–3× and the O₂ curve shifts right — the anemia is better tolerated.',
  'x:pc': 'Pyruvate carboxylase (biotin, ATP) makes oxaloacetate. Deficiency: lactic acidemia and delayed development (Leigh-type), and '
          'gluconeogenesis fails → hypoglycemia. Biotin serves every carboxylase; deficiency (raw egg whites, long antibiotics) gives '
          'dermatitis, enteritis, alopecia.',
  'x:etoh': 'Alcohol and aldehyde dehydrogenases both make NADH. Excess NADH drives pyruvate → lactate and OAA → malate, starving '
            'gluconeogenesis: fasting hypoglycemia in a binge drinker, lactic acidosis (lactate cuts urate excretion → gout), ketoacidosis, '
            'steatosis. Give thiamine before dextrose.',
  'x:idh': 'Neomorphic IDH1/IDH2: α-ketoglutarate → 2-hydroxyglutarate, which inhibits α-KG–dependent enzymes such as TET2 → abnormal DNA '
           'methylation. IDH-mutant glioma (better prognosis than glioblastoma; IDH1 R132H stain), AML, cholangiocarcinoma, enchondroma.',
  'x:sdh': 'SDH (also complex II of the ETC): succinate accumulates and blocks the proline hydroxylation that tags HIF for destruction, '
           'so HIF stays active → hypoxia genes on. Germline SDHB/SDHD: familial paraganglioma/pheochromocytoma; also renal cell carcinoma.',
}

dyn = dict(
  kinds=dict(c=['mov', '--dk3'], onc=['bad', '--bad'], nadh=['bad', '--dk10']),
  groups=[['mov', 'Carbon flow'], ['bad', 'Oncometabolite · NADH']],
  switches=[dict(id='hor', label='State', type='steps', options=[['fed', 'Fed (insulin)', 'f26bp'], ['fast', 'Fasting (glucagon)', 'f26bp']]),
            dict(id='x', label='Odd hit', type='one', options=[
              ['hk', 'Hexokinase deficiency', 'hkdef'], ['pk', 'Pyruvate kinase deficiency', 'pkdef'], ['pc', 'Pyruvate carboxylase / biotin', 'pyrcarb'],
              ['etoh', 'Ethanol', 'ethanol'], ['idh', 'IDH mutation', 'idhmut'], ['sdh', 'SDH mutation', 'sdhmut']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 64–66, 70, 74–76, 428 · Marks ch 22–23, 25, 28, 33–34, 42 · Robbins ch 7, 14, 24, 28')

MAP = dict(
  id='glyxsim', title='Glycolysis Odds & Ends in Motion', topic='bio', after='core',
  sub='Flip F-2,6-BP between fed and fasting, then hit glycolysis with hexokinase or pyruvate kinase deficiency, a missing pyruvate carboxylase, '
      'ethanol’s NADH, or an IDH or SDH mutation',
  w=3600, h=1900,
  fa='64, 66, 70, 74, 75, 76, 428',
  src=['Marks ch 22 — Generation of Adenosine Triphosphate from Glucose, Fructose, and Galactose: Glycolysis',
       'Marks ch 28 — Gluconeogenesis and Maintenance of Blood Glucose Levels', 'Marks ch 33 — Metabolism of Ethanol',
       'Marks ch 34 — Integration of Carbohydrate and Lipid Metabolism', 'Robbins ch 7 — Neoplasia',
       'Marks ch 23 — Tricarboxylic Acid Cycle', 'Marks ch 25 — Oxygen Toxicity and Free-Radical Injury',
       'Marks ch 42 — The Biochemistry of Erythrocytes and Other Blood Cells', 'Robbins ch 14 — Red blood cell and bleeding disorders',
       'Robbins ch 24 — The endocrine system', 'Robbins ch 28 — The central nervous system'],
  lanes=[('gxGly', 'Glycolysis & its switch', 'glycolysis'), ('gxNeo', 'Gluconeogenesis & TCA', 'tca')],
  nodes=[
    ('gx1', 'Hexokinase deficiency', 240, 1720, 'gxGly', 'RBC · ↓2,3-BPG', ['hkdef']),
    ('gx2', 'Pyruvate kinase deficiency', 560, 1720, 'gxGly', 'RBC · ↑2,3-BPG', ['pkdef']),
    ('gx3', 'F-2,6-BP switch', 880, 1720, 'gxGly', 'insulin vs glucagon', ['f26bp'], 'hub'),
    ('gx4', 'Pyruvate carboxylase', 1200, 1720, 'gxNeo', 'biotin', ['pyrcarb']),
    ('gx5', 'Ethanol & NADH', 1520, 1720, 'gxNeo', 'lactate · hypoglycemia', ['ethanol']),
    ('gx6', 'IDH mutation', 1840, 1720, 'gxNeo', '2-hydroxyglutarate', ['idhmut']),
    ('gx7', 'SDH mutation', 2160, 1720, 'gxNeo', 'succinate → HIF', ['sdhmut'])],
  panels=[
    (2500, PANY, 1000, 'Odd hits (Marks · First Aid)', [
      ('Hexokinase', 'hemolysis, left shift'), ('Pyruvate kinase', 'hemolysis, right shift'), ('Pyruvate carboxylase', 'biotin, lactate'),
      ('Ethanol', 'NADH → hypoglycemia'), ('IDH / SDH', '2-HG / succinate')])],
  dyn=dyn)
