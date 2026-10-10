# Lysosomal Storage in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A cell: the Golgi tags lysosomal enzymes with mannose-6-phosphate and ships them to the lysosome, which digests
# substrates taken in from outside. One `one` switch removes an enzyme — Tay-Sachs, Niemann-Pick, Gaucher, Fabry,
# Krabbe, metachromatic leukodystrophy, Hurler, Hunter — and the lysosome fills with that substrate; I-cell disease
# breaks the tag instead, so the enzymes are secreted into the blood. A clue box lists where each one shows.
# 6 readouts (↑ present · ↓ absent). Facts from the pinned cards (taysachs, niemannpick, gaucher, fabry, krabbe, mld,
# hurler, hunter, icell, farber, gm1); FA pp. 45, 86. No new cards.
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
SW = 'lsd'
O = lambda *k: [f'{SW}:{x}' for x in k]
ALL = ['tay', 'np', 'gau', 'fab', 'kra', 'mld', 'hur', 'hun']
PANY = 760

text('The lysosome — the cell’s digestive bag', 180, 150, 'dyn-big')
text('each enzyme clears one substrate; lose it and that substrate fills the lysosome', 180, 176, 'dyn-cap')
add('<rect x="160" y="210" width="1500" height="980" rx="120" class="dyn-cell"/>')
text('the cell', 200, 260, 'nf-l1')
# Golgi
for i in range(4):
    add(f'<path d="M{300 + i * 8} {430 + i * 36} Q450 {390 + i * 36} {600 - i * 8} {430 + i * 36}" style="fill:none;stroke:var(--dk9);stroke-width:12;stroke-linecap:round"/>')
text('Golgi', 450, 600, 'nf-l1', 'middle')
text('tags enzymes with mannose-6-phosphate', 450, 624, 'nf-l2', 'middle')
add('<path d="M330 640 L570 680 M570 640 L330 680" class="nf-x"/>', when=O('icell'))
# the lysosome
LX, LY, LR = 1100, 700, 250
add(f'<circle cx="{LX}" cy="{LY}" r="{LR}" style="fill:var(--dk11);fill-opacity:.10;stroke:var(--dk11);stroke-width:6"/>', unless=O(*ALL, 'icell'))
add(f'<circle cx="{LX}" cy="{LY}" r="{LR + 40}" style="fill:var(--dk5);fill-opacity:.30;stroke:var(--bad);stroke-width:6"/>', when=O(*ALL, 'icell'))
text('Lysosome', LX, LY - LR - 18, 'nf-l1', 'middle', unless=O(*ALL, 'icell'))
text('Lysosome — packed with undigested substrate', LX, LY - LR - 58, 'nf-l1 dyn-tag', 'middle', when=O(*ALL, 'icell'))
# substrate entering from outside (endocytosis)
text('substrates arrive from outside', 1460, 1150, 'nf-l2', 'middle')
# I-cell: enzymes leave to the blood
add('<path d="M600 520 C800 360 1300 260 1660 300" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:10 6"/>', when=O('icell'))
text('untagged enzymes are secreted into the blood', 1100, 300, 'nf-l1 dyn-tag', 'middle', when=O('icell'))

# ════════ the clue box ════════
C = dict(
  tay=('Tay-Sachs — β-hexosaminidase A', 'stores GM2 ganglioside · autosomal recessive', 'neurodegeneration, cherry-red macula, hyperacusis', 'NO hepatosplenomegaly'),
  np=('Niemann-Pick A/B — sphingomyelinase', 'stores sphingomyelin · autosomal recessive', 'type A: neurodegeneration + hepatosplenomegaly', 'cherry-red spot · foam cells'),
  gau=('Gaucher — β-glucocerebrosidase', 'stores glucocerebroside in macrophages · the commonest', 'hepatosplenomegaly, pancytopenia, bone crises (AVN)', '“crumpled tissue paper” Gaucher cells'),
  fab=('Fabry — α-galactosidase A', 'stores ceramide trihexoside · X-linked recessive', 'burning hands and feet, angiokeratomas, hypohidrosis', 'later renal failure and heart disease'),
  kra=('Krabbe — galactocerebrosidase', 'galactocerebroside and psychosine kill oligodendrocytes', 'optic atrophy, peripheral neuropathy, regression', 'globoid cells in white matter'),
  mld=('Metachromatic leukodystrophy — arylsulfatase A', 'stores sulfatides · central AND peripheral demyelination', 'dementia, spasticity, areflexia, ataxia', 'slowed nerve conduction'),
  hur=('Hurler (MPS I) — α-L-iduronidase', 'stores heparan and dermatan sulfate · autosomal recessive', 'corneal clouding, coarse facies, hepatosplenomegaly', 'urinary GAGs ↑ · dysostosis multiplex'),
  hun=('Hunter (MPS II) — iduronate-2-sulfatase', 'same GAGs · X-linked recessive · milder', 'NO corneal clouding · aggressive behavior', 'urinary GAGs ↑'),
  icell=('I-cell disease — GlcNAc-1-phosphotransferase', 'no mannose-6-phosphate tag: enzymes go to the blood', 'coarse facies, gingival hyperplasia, claw hand', 'plasma lysosomal enzymes ↑ · normal urine GAGs'),
)
box(1700, 210, 2340, 1190)
text('Where it shows', 1730, 250, 'dyn-big')
text('pick a disease on the right', 1730, 290, 'nf-l1', unless=[f'{SW}:*'])
for k, lines in C.items():
    for i, t in enumerate(lines):
        y = 300 + i * 64
        text(t if len(t) < 42 else t[:t.rfind(' ', 0, 42)], 1730, y, 'nf-l1' if i == 0 else 'nf-l2', when=O(k))
        if len(t) >= 42:
            text(t[t.rfind(' ', 0, 42) + 1:], 1730, y + 24, 'nf-l1' if i == 0 else 'nf-l2', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
loop = f'M{LX - 180} {LY} A180 180 0 1 1 {LX + 180} {LY} A180 180 0 1 1 {LX - 180} {LY}'
flows = [
  dict(d=f'M600 560 C750 620 800 680 {LX - LR} {LY}', len=560, speed=110, r=7, base=dict(enz=5), mods=[m(O('icell'), set=dict(enz=0))]),
  dict(d='M600 520 C800 360 1300 260 1660 300', len=1160, speed=140, r=7, base=dict(), when=O('icell'), mods=[m(O('icell'), set=dict(enz=6))]),
  dict(d=f'M1640 1100 C1500 1050 1400 950 {LX + 150} {LY + 200}', len=600, speed=90, r=8, base=dict(sub=3)),
  dict(d=loop, len=round(2 * math.pi * 180), speed=50, r=9, base=dict(sub=2), mods=[m(O(*ALL, 'icell'), set=dict(sub=16))]),
]
ENZ = [('tay', 'β-Hexosaminidase A', 'taysachs'), ('np', 'Sphingomyelinase', 'niemannpick'), ('gau', 'β-Glucocerebrosidase', 'gaucher'),
       ('fab', 'α-Galactosidase A', 'fabry'), ('kra', 'Galactocerebrosidase', 'krabbe'), ('mld', 'Arylsulfatase A', 'mld'),
       ('hur', 'α-L-Iduronidase', 'hurler'), ('hun', 'Iduronate-2-sulfatase', 'hunter')]
sites = []
for i, (k, lab, card) in enumerate(ENZ):
    a = math.radians(200 + i * 20)
    x, y = LX + LR * math.cos(a), LY + LR * math.sin(a)
    sites.append(dict(x=round(x), y=round(y), n=[round(math.cos(a), 2), round(math.sin(a), 2)], w=12, t='md', l='', aria=lab, c=card, ions=[],
                      block=O(k, 'icell')))

readouts = [
  dict(l='Hepatosplenomegaly', mods=[dict(when=O('np', 'gau', 'hur', 'hun'), d=1), dict(when=O('tay'), d=-1)]),
  dict(l='Cherry-red spot', mods=[dict(when=O('tay', 'np'), d=1), dict(when=O('gau', 'kra'), d=-1)]),
  dict(l='Corneal clouding', mods=[dict(when=O('hur', 'icell'), d=1), dict(when=O('hun'), d=-1)]),
  dict(l='Peripheral neuropathy', mods=[dict(when=O('fab', 'kra', 'mld'), d=1)]),
  dict(l='Urinary GAGs', mods=[dict(when=O('hur', 'hun'), d=1), dict(when=O('icell'), d=0)]),
  dict(l='Plasma lysosomal enzymes', mods=[dict(when=O('icell'), d=1)]),
]

notes = {
  '': 'The Golgi tags lysosomal enzymes with mannose-6-phosphate and ships them to the lysosome, which digests what the cell takes '
      'in. Lose one enzyme and its substrate accumulates. In the readouts ↑ means present and ↓ absent.',
  'lsd:tay': 'Tay-Sachs (β-hexosaminidase A): GM2 ganglioside fills neurons — neurodegeneration, a cherry-red macula, hyperacusis, '
             'death by 2–3 years. No hepatosplenomegaly, the separator from Niemann-Pick.',
  'lsd:np': 'Niemann-Pick A/B (sphingomyelinase): sphingomyelin loads neurons and macrophages — type A has neurodegeneration plus '
            'hepatosplenomegaly and a cherry-red spot; foam cells.',
  'lsd:gau': 'Gaucher (β-glucocerebrosidase), the commonest: engorged macrophages infiltrate marrow, liver and spleen — '
             'hepatosplenomegaly, pancytopenia, bone crises. Enzyme replacement.',
  'lsd:fab': 'Fabry (α-galactosidase A, X-linked): ceramide trihexoside builds up in vascular endothelium — burning hands and feet, '
             'angiokeratomas, hypohidrosis, then renal failure and heart disease.',
  'lsd:kra': 'Krabbe (galactocerebrosidase): psychosine kills oligodendrocytes — central and peripheral demyelination, optic '
             'atrophy, globoid cells. No cherry-red spot.',
  'lsd:mld': 'Metachromatic leukodystrophy (arylsulfatase A): sulfatides destabilize myelin both centrally and peripherally — '
             'dementia and spasticity with areflexia and slowed conduction.',
  'lsd:hur': 'Hurler (MPS I, α-L-iduronidase): heparan and dermatan sulfate pile up — corneal clouding, coarse facies, '
             'hepatosplenomegaly, airway obstruction; urinary GAGs rise.',
  'lsd:hun': 'Hunter (MPS II, iduronate-2-sulfatase, X-linked): the same GAGs, a milder picture in boys — and the cornea is spared. '
             'Aggressive behavior.',
  'lsd:icell': 'I-cell disease (GlcNAc-1-phosphotransferase): without the mannose-6-phosphate tag the enzymes are secreted into the '
               'blood, so every lysosome fills — high plasma enzymes, low inside cells, normal urine GAGs.',
}

dyn = dict(
  kinds=dict(enz=['enz', '--dk9'], sub=['sub', '--dk5']), groups=[['enz', 'Enzymes'], ['sub', 'Substrate']],
  switches=[dict(id=SW, label='Missing enzyme', type='one', options=[
    ['tay', 'Tay-Sachs', 'taysachs'], ['np', 'Niemann-Pick', 'niemannpick'], ['gau', 'Gaucher', 'gaucher'], ['fab', 'Fabry', 'fabry'],
    ['kra', 'Krabbe', 'krabbe'], ['mld', 'Metachromatic leukodystrophy', 'mld'], ['hur', 'Hurler (MPS I)', 'hurler'],
    ['hun', 'Hunter (MPS II)', 'hunter'], ['icell', 'I-cell disease', 'icell']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 45, 86 · Robbins ch 5')

MAP = dict(
  id='lsdsim', title='Lysosomal Storage in Motion', topic='bio', after='lysosome',
  sub='Enzymes tagged in the Golgi digest what reaches the lysosome — remove one and watch its substrate fill the lysosome, or break '
      'the tag (I-cell) and watch the enzymes leave for the blood; the readouts ask about organs, cherry-red spot, cornea and nerves',
  w=3500, h=1520,
  fa='45, 86',
  src=[full('Robbins', 5), full('Robbins', 28), full('Marks', 47), full('Pawlina', 2)],
  lanes=[('lsSphingo', 'Sphingolipidoses', 'glycolysis'), ('lsMps', 'Mucopolysaccharidoses', 'tca'), ('lsTraffic', 'Trafficking', 'gluconeo')],
  nodes=[
    ('lq1', 'Tay-Sachs · GM1', 330, 1300, 'lsSphingo', 'cherry-red, no HSM', ['taysachs', 'gm1'], 'hub'),
    ('lq2', 'Niemann-Pick · Gaucher', 760, 1300, 'lsSphingo', 'macrophages', ['niemannpick', 'gaucher']),
    ('lq3', 'Fabry', 1160, 1300, 'lsSphingo', 'X-linked', ['fabry']),
    ('lq4', 'Krabbe · MLD · Farber', 1580, 1300, 'lsSphingo', 'myelin', ['krabbe', 'mld', 'farber']),
    ('lq5', 'Hurler · Hunter', 330, 1430, 'lsMps', 'GAGs', ['hurler', 'hunter']),
    ('lq6', 'I-cell disease', 760, 1430, 'lsTraffic', 'mannose-6-phosphate', ['icell'])],
  panels=[],
  dyn=dyn)
