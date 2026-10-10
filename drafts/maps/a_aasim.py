# Amino Acid Disorders in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Three catabolic lines with metabolites flowing between them — phenylalanine → tyrosine (→ melanin, catecholamines and
# thyroxine, or → homogentisate → fumarylacetoacetate → fumarate + acetoacetate); leucine, isoleucine, valine → α-ketoacids
# → acyl-CoAs → propionyl-CoA → methylmalonyl-CoA → succinyl-CoA; methionine → homocysteine → cystathionine → cysteine with
# remethylation back — and a kidney tubule with the two amino-acid transporters. A `one` switch blocks one enzyme or
# transporter: the substrate piles up, spills to its tell-tale product, and the line downstream stops. 6 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
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
BW, BH = 230, 60
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(x, y, lab, cls='dyn-cell'):
    add(f'<rect x="{x - BW // 2}" y="{y - BH // 2}" width="{BW}" height="{BH}" rx="26" class="{cls}"/>')
    text(lab, x, y + 6, 'nf-l1', 'middle')
def pile(x, y, when):
    add(''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="11" style="fill:var(--dk1);opacity:.75"/>'
                for dx, dy in ((-40, -46), (-14, -52), (12, -48), (38, -44), (-26, -70), (0, -74), (26, -70))), when=when)
def outcome(x, y, lab, when):
    add(f'<rect x="{x - 150}" y="{y - 28}" width="300" height="56" rx="20" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:3"/>', when=when)
    text(lab, x, y + 6, 'nf-l1', 'middle', when=when)

text('Amino acid disorders — block an enzyme, watch the substrate pile up', 180, 150, 'dyn-big')
text('dots = metabolite flowing · a stack = what accumulates · red box = what spills out', 180, 176, 'dyn-cap')

# ════════ aromatic line ════════
YA = 420
P = dict(phe=(380, YA), tyr=(820, YA), hga=(1260, YA), faa=(1700, YA), fum=(2120, YA), mel=(820, 250), cat=(820, 590))
node(*P['phe'], 'Phenylalanine'); node(*P['tyr'], 'Tyrosine'); node(*P['hga'], 'Homogentisate')
node(*P['faa'], 'Fumarylacetoacetate'); node(*P['fum'], 'Fumarate + acetoacetate'); node(*P['mel'], 'Melanin')
node(*P['cat'], 'Dopamine · NE · thyroxine')
for (a, b, lab, lx, ly) in (('phe', 'tyr', 'PAH · BH4', 600, YA - 16), ('tyr', 'hga', '', 0, 0), ('hga', 'faa', 'HGD', 1480, YA - 16),
                            ('faa', 'fum', 'FAH', 1910, YA - 16)):
    add(f'<path d="M{P[a][0] + BW // 2} {YA} H{P[b][0] - BW // 2}" class="dyn-line"/>')
    if lab: text(lab, lx, ly, 'nf-l2', 'middle')
add(f'<path d="M820 {YA - BH // 2} V{250 + BH // 2}" class="dyn-line"/>'); text('tyrosinase', 840, 340, 'nf-l2')
add(f'<path d="M820 {YA + BH // 2} V{590 - BH // 2}" class="dyn-line"/>'); text('Tyr hydroxylase · BH4', 840, 510, 'nf-l2')
add(X(600, YA), when=O('pku', 'bh4')); add(X(820, 505), when=O('bh4')); add(X(820, 335), when=O('alb'))
add(X(1480, YA), when=O('alk')); add(X(1910, YA), when=O('tyr1'))
pile(380, YA - 30, O('pku', 'bh4')); pile(1260, YA - 30, O('alk')); pile(1700, YA - 30, O('tyr1'))
outcome(380, 600, 'phenylketones — musty odor', O('pku', 'bh4'))
outcome(1260, 600, 'black urine · ochronosis', O('alk'))
outcome(1700, 600, 'liver failure · renal Fanconi', O('tyr1'))
outcome(560, 250, 'no melanin — pale skin, hair', O('alb'))

# ════════ branched-chain and propionyl line ════════
YB = 860
Q = dict(bc=(380, YB), ka=(820, YB), acyl=(1260, YB), prop=(1700, YB), mm=(2120, YB), succ=(2120, YB + 170))
node(*Q['bc'], 'Leu · Ile · Val'); node(*Q['ka'], 'α-Ketoacids'); node(*Q['acyl'], 'Acyl-CoAs')
node(*Q['prop'], 'Propionyl-CoA'); node(*Q['mm'], 'Methylmalonyl-CoA'); node(*Q['succ'], 'Succinyl-CoA → TCA')
for (a, b, lab, lx) in (('bc', 'ka', 'transaminase · B6', 600), ('ka', 'acyl', 'BCKDH · B1', 1040), ('acyl', 'prop', 'Val, Ile', 1480),
                        ('prop', 'mm', 'PCC · biotin', 1910)):
    add(f'<path d="M{Q[a][0] + BW // 2} {YB} H{Q[b][0] - BW // 2}" class="dyn-line"/>'); text(lab, lx, YB - 16, 'nf-l2', 'middle')
add(f'<path d="M2120 {YB + BH // 2} V{YB + 170 - BH // 2}" class="dyn-line"/>'); text('mutase · B12', 2140, YB + 90, 'nf-l2')
text('+ odd-chain fatty acids, Met, Thr (VOMIT)', 1700, YB - 50, 'nf-l2', 'middle')
add(X(1040, YB), when=O('msud')); add(X(1910, YB), when=O('pa')); add(X(2120, YB + 85), when=O('mma'))
pile(820, YB - 30, O('msud')); pile(1700, YB - 30, O('pa')); pile(2120, YB - 30, O('mma'))
outcome(820, YB + 120, 'maple syrup urine — neuro decline', O('msud'))
outcome(1700, YB + 120, 'acidosis + ketosis + ↑ NH₃', O('pa', 'mma'))

# ════════ sulfur line ════════
YC = 1240
R = dict(met=(380, YC), hcy=(820, YC), cth=(1260, YC), cys=(1700, YC))
node(*R['met'], 'Methionine'); node(*R['hcy'], 'Homocysteine'); node(*R['cth'], 'Cystathionine'); node(*R['cys'], 'Cysteine')
add(f'<path d="M{380 + BW // 2} {YC} H{820 - BW // 2}" class="dyn-line"/>')
add(f'<path d="M{820 + BW // 2} {YC} H{1260 - BW // 2}" class="dyn-line"/>'); text('CBS · B6', 1040, YC - 16, 'nf-l2', 'middle')
add(f'<path d="M{1260 + BW // 2} {YC} H{1700 - BW // 2}" class="dyn-line"/>')
add(f'<path d="M820 {YC + BH // 2} C820 {YC + 140} 380 {YC + 140} 380 {YC + BH // 2}" class="dyn-line"/>')
text('methionine synthase · B12 · folate (MTHFR)', 600, YC + 140, 'nf-l2', 'middle')
add(X(1040, YC), when=O('cbs')); add(X(600, YC + 105), when=O('ms'))
pile(820, YC - 30, O('cbs', 'ms'))
outcome(1260, YC + 110, 'marfanoid · lens down-in · clots', O('cbs', 'ms'))

# ════════ kidney: the transporters ════════
add('<rect x="1950" y="1180" width="450" height="70" rx="30" style="fill:var(--nf-h2o);fill-opacity:.12;stroke:var(--dk3);stroke-width:4"/>')
text('proximal tubule (and gut)', 2175, 1160, 'nf-l1', 'middle')
text('urine →', 2400, 1300, 'nf-l2', 'end')
outcome(2175, 1380, 'Trp lost → niacin ↓ → pellagra', O('hartnup'))
outcome(2175, 1380, 'cystine stones — hexagonal', O('cyst'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def seg(d, n, stop=None, low=None, when=None, k='aa'):
    f = dict(d=d, len=220, speed=70, r=8, base={k: n})
    mods = []
    if low: mods.append(m(low, set={k: 1}))
    if stop: mods.append(m(stop, set={k: 0}))
    if mods: f['mods'] = mods
    if when: f['when'] = when
    return f
flows = [
  seg(f'M495 {YA} H705', 3, stop=O('pku', 'bh4')),
  seg(f'M935 {YA} H1145', 3, low=O('pku', 'bh4')),
  seg(f'M820 {YA - 30} V280', 2, stop=O('alb'), low=O('pku', 'bh4')),
  seg(f'M820 {YA + 30} V560', 2, stop=O('bh4'), low=O('pku')),
  seg(f'M1375 {YA} H1585', 3, stop=O('alk'), low=O('pku', 'bh4')),
  seg(f'M1815 {YA} H2005', 3, stop=O('alk', 'tyr1'), low=O('pku', 'bh4')),
  seg(f'M380 {YA + 30} V572', 4, when=O('pku', 'bh4'), k='bad'),
  seg(f'M1260 {YA + 30} V572', 4, when=O('alk'), k='bad'),
  seg(f'M1700 {YA + 30} V572', 4, when=O('tyr1'), k='bad'),
  seg(f'M495 {YB} H705', 3),
  seg(f'M935 {YB} H1145', 3, stop=O('msud')),
  seg(f'M1375 {YB} H1585', 3, stop=O('msud')),
  seg(f'M1815 {YB} H2005', 3, stop=O('msud', 'pa')),
  seg(f'M2120 {YB + 30} V{YB + 140}', 3, stop=O('msud', 'pa', 'mma')),
  seg(f'M820 {YB + 30} V{YB + 92}', 4, when=O('msud'), k='bad'),
  seg(f'M1700 {YB + 30} V{YB + 92}', 4, when=O('pa'), k='bad'),
  seg(f'M2120 {YB + 30} C2000 {YB + 90} 1900 {YB + 120} 1850 {YB + 120}', 4, when=O('mma'), k='bad'),
  seg(f'M495 {YC} H705', 3),
  seg(f'M935 {YC} H1145', 3, stop=O('cbs')),
  seg(f'M1375 {YC} H1585', 3, stop=O('cbs')),
  seg(f'M820 {YC + 30} C820 {YC + 140} 380 {YC + 140} 380 {YC + 30}', 3, stop=O('ms')),
  seg(f'M820 {YC + 30} C900 {YC + 100} 1100 {YC + 110} 1110 {YC + 110}', 4, when=O('cbs', 'ms'), k='bad'),
  seg('M1970 1215 H2400', 3, k='aa'),
]
sites = [
  dict(x=2050, y=1250, n=[0, 1], w=8, t='co', l='neutral AA', s='Trp', c='hartnup', ions=[['aa', 'out', 1]], block=O('hartnup'),
       la='middle', lx=2050, ly=1300),
  dict(x=2280, y=1250, n=[0, 1], w=8, t='co', l='COLA', s='cystine', c='cystinuria', ions=[['aa', 'out', 1]], block=O('cyst'),
       la='middle', lx=2280, ly=1300),
  dict(x=600, y=860, n=[0, 1], w=10, t='rec', l='', aria='Pyridoxine (B6)', c='b6', ions=[]),
]

readouts = [
  dict(l='Phenylalanine', mods=[dict(when=O('pku', 'bh4'), d=1)]),
  dict(l='Tyrosine', mods=[dict(when=O('pku'), d=-1)]),
  dict(l='Leu · Ile · Val', mods=[dict(when=O('msud'), d=1)]),
  dict(l='Anion-gap acidosis · NH₃', mods=[dict(when=O('pa', 'mma'), d=1)]),
  dict(l='Homocysteine', mods=[dict(when=O('cbs', 'ms'), d=1)]),
  dict(l='Methionine', mods=[dict(when=O('cbs'), d=1), dict(when=O('ms'), d=-1)]),
]

notes = {
  '': 'Each catabolic line runs an amino acid down to TCA intermediates or ketone bodies. Block one enzyme (all autosomal recessive '
      'here) and the substrate piles up and spills into a product that names the disease; everything downstream stops.',
  'dx:pku': 'PKU: phenylalanine hydroxylase is missing, so Phe accumulates and is shunted to phenylketones (musty odor); tyrosine '
            'becomes essential, starving melanin, dopamine and thyroxine. Newborn screen; low-Phe diet, avoid aspartame.',
  'dx:bh4': 'BH4 (cofactor) deficiency: phenylalanine hydroxylase fails as in PKU, and so do tyrosine and tryptophan hydroxylases — '
            'adding a catecholamine and serotonin deficit. BH4 supplementation.',
  'dx:alb': 'Albinism: melanocytes are present but tyrosinase can’t turn tyrosine into melanin — pale skin and hair, more skin cancer.',
  'dx:alk': 'Alkaptonuria: homogentisate dioxygenase is missing; homogentisic acid polymerizes to a blue-black pigment that binds '
            'collagen (ochronosis) — urine that blackens in air, arthralgias. Usually benign. Nitisinone.',
  'dx:tyr1': 'Tyrosinemia type I: fumarylacetoacetate hydrolase, the last step, is missing — fumarylacetoacetate accumulates and the '
             'liver fails; chronic cirrhosis, hepatocellular carcinoma, renal Fanconi. Nitisinone.',
  'dx:msud': 'Maple syrup urine disease: the branched-chain α-ketoacids can’t be decarboxylated (BCKDH, a thiamine enzyme) — ↑ Leu, Ile, '
             'Val; sweet urine, vomiting, neurologic decline. Restrict BCAAs; thiamine.',
  'dx:pa': 'Propionic acidemia (propionyl-CoA carboxylase, biotin): organic acids build up and inhibit gluconeogenesis and the urea '
           'cycle — anion-gap acidosis with ketosis, hyperammonemia, low fasting glucose.',
  'dx:mma': 'Methylmalonic acidemia (methylmalonyl-CoA mutase, B12): the same picture one step later, with ↑ methylmalonic acid.',
  'dx:cbs': 'Homocystinuria (cystathionine β-synthase, B6): homocysteine can’t go on to cystathionine — ↑ homocysteine and ↑ methionine; '
            'marfanoid habitus, lens down and in, intellectual disability, thrombosis. B6, cysteine; restrict methionine.',
  'dx:ms': 'Homocystinuria from failed remethylation (methionine synthase / B12, MTHFR / folate): ↑ homocysteine with LOW methionine.',
  'dx:hartnup': 'Hartnup disease: the neutral amino-acid transporter (kidney and gut) fails; tryptophan is lost in the urine, and '
                'tryptophan makes niacin — pellagra from a transport defect. High-protein diet, nicotinic acid.',
  'dx:cyst': 'Cystinuria: reabsorption of Cystine, Ornithine, Lysine, Arginine (COLA) fails; cystine precipitates in acidic urine — '
             'hexagonal crystals, stones from childhood. Hydration, urinary alkalinization.',
}

dyn = dict(
  kinds=dict(aa=['flow', '--dk2'], bad=['spill', '--bad']), groups=[['flow', 'Metabolite flow'], ['spill', 'What spills out']],
  switches=[dict(id='dx', label='Block', type='one', options=[
    ['pku', 'PKU (phenylalanine hydroxylase)', 'pku'], ['bh4', 'BH4 deficiency', 'pku'], ['alb', 'Albinism (tyrosinase)', 'albinism'],
    ['alk', 'Alkaptonuria', 'alkapton'], ['tyr1', 'Tyrosinemia type I', 'tyrosinemia'], ['msud', 'Maple syrup urine disease', 'msud'],
    ['pa', 'Propionic acidemia', 'organicacid'], ['mma', 'Methylmalonic acidemia', 'organicacid'],
    ['cbs', 'Homocystinuria — CBS', 'homocyst'], ['ms', 'Homocystinuria — remethylation', 'homocyst'],
    ['hartnup', 'Hartnup disease', 'hartnup'], ['cyst', 'Cystinuria', 'cystinuria']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 64–66, 81–83, 88 · Marks ch 37')

MAP = dict(
  id='aasim', title='Amino Acid Disorders in Motion', topic='bio', after='nitrogen',
  sub='Run phenylalanine, the branched-chain amino acids and methionine down their pathways, then block one enzyme or transporter — '
      'PKU, BH4, albinism, alkaptonuria, tyrosinemia, MSUD, propionic and methylmalonic acidemia, homocystinuria, Hartnup, cystinuria',
  w=3600, h=1900,
  fa='59, 64, 65, 66, 81, 82, 83, 88, 115, 425, 484, 604, 617',
  src=['Marks ch 37 — Synthesis and Degradation of Amino Acids', 'Robbins ch 5 — Genetic disorders', 'Pawlina ch 15 — Integumentary System',
       'Marks ch 46 — Metabolism of the Nervous System', 'Marks ch 23 — Tricarboxylic Acid Cycle', 'Marks ch 8 — Enzymes as Catalysts',
       'Robbins ch 18 — Liver and gallbladder', 'Marks ch 30 — Oxidation of Fatty Acids and Ketone Bodies',
       'Marks ch 35 — Protein Digestion and Amino Acid Absorption', 'Costanzo ch 8 — Gastrointestinal physiology', 'Robbins ch 20 — The kidney'],
  lanes=[('aaArom', 'Phenylalanine & tyrosine', 'glycolysis'), ('aaBc', 'Branched-chain & propionyl', 'tca'), ('aaSul', 'Sulfur & transport', 'gluconeo')],
  nodes=[
    ('aa1', 'B6 — transamination', 330, 1620, 'aaBc', 'PLP cofactor', ['b6'], 'hub'),
    ('aa2', 'Phenylketonuria', 760, 1620, 'aaArom', 'musty odor', ['pku']),
    ('aa3', 'Alkaptonuria · albinism', 1200, 1620, 'aaArom', 'black urine · no melanin', ['alkapton', 'albinism']),
    ('aa4', 'Tyrosinemia type I', 1640, 1620, 'aaArom', 'liver failure', ['tyrosinemia']),
    ('aa5', 'Maple syrup urine disease', 2080, 1620, 'aaBc', 'I Love Vermont', ['msud']),
    ('aa6', 'Propionic · methylmalonic', 330, 1760, 'aaBc', 'VOMIT · acidosis', ['organicacid']),
    ('aa7', 'Homocystinuria', 760, 1760, 'aaSul', 'lens down and in', ['homocyst']),
    ('aa8', 'Hartnup · cystinuria', 1200, 1760, 'aaSul', 'transport defects', ['hartnup', 'cystinuria'])],
  panels=[
    (2500, PANY, 1000, 'Cofactors to remember', [
      ('BH4', 'Phe, Tyr and Trp hydroxylases'),
      ('B1 (thiamine)', 'BCKDH — also PDH and α-KGDH'),
      ('Biotin', 'propionyl-CoA carboxylase'),
      ('B12', 'methylmalonyl-CoA mutase, methionine synthase'),
      ('B6', 'transaminases, cystathionine β-synthase')])],
  dyn=dyn)
