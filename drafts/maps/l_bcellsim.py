# B Cells & Lymphomas in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A B cell's journey: marrow precursor (TdT) → blood → lymph node follicle (mantle zone of naive B cells, germinal center,
# marginal zone) → plasma cells and memory, with cells moving along it, plus the spleen and the brain. A `one` switch picks a
# lymphoid neoplasm and lights the place it arises or lives (where the card names it) with its marker and translocation:
# ALL, CLL, hairy cell, mantle cell, follicular, Burkitt, DLBCL, marginal zone (MALT), Hodgkin, primary CNS lymphoma. A
# 4 readouts. Facts from the pinned cards; FA pages in `fa`.
# No new cards.
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

O = lambda *k: [f'ly:{x}' for x in k]
PANY = 1180
def zone(x0, y0, x1, y1, lab, sub=''):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="30" class="dyn-soft"/>')
    text(lab, x0 + 24, y0 + 40, 'nf-l1'); 
    if sub: text(sub, x0 + 24, y0 + 66, 'nf-l2')
def hi(x0, y0, x1, y1, when): add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="30" style="fill:var(--bad);fill-opacity:.1;stroke:var(--bad);stroke-width:5"/>', when=when)

text('B cells and the lymphomas — where each one comes from', 180, 150, 'dyn-big')
text('a lit box = where the card places the tumor’s cell of origin or where it lives', 180, 176, 'dyn-cap')

zone(300, 260, 700, 640, 'Bone marrow', 'precursors · TdT')
zone(800, 260, 1150, 640, 'Blood', 'mature B cells')
# lymph node follicle
add('<rect x="1250" y="240" width="1050" height="760" rx="80" class="dyn-soft"/>'); text('Lymph node follicle', 1280, 284, 'nf-l1')
add('<circle cx="1700" cy="640" r="330" style="fill:var(--dk7);fill-opacity:.08;stroke:var(--dk7);stroke-width:3;stroke-dasharray:10 8"/>')
text('marginal zone', 1700, 330, 'nf-l2', 'middle')
add('<circle cx="1700" cy="640" r="250" style="fill:var(--dk2);fill-opacity:.12;stroke:var(--dk2);stroke-width:3"/>')
text('mantle zone — naive B cells', 1700, 420, 'nf-l2', 'middle')
add('<circle cx="1700" cy="660" r="150" style="fill:var(--dk5);fill-opacity:.2;stroke:var(--dk5);stroke-width:3"/>')
text('germinal center', 1700, 650, 'nf-l1', 'middle'); text('selection: losers die', 1700, 676, 'nf-l2', 'middle')
zone(2050, 820, 2300, 990, 'Plasma · memory')
zone(300, 760, 700, 1000, 'Spleen · liver')
zone(800, 760, 1150, 1000, 'Brain')
zone(300, 1100, 1150, 1280, 'Chronic antigen: H. pylori, Sjögren, Hashimoto')

hi(300, 260, 700, 640, O('all'))
hi(800, 260, 1150, 640, O('cll'))
hi(300, 760, 700, 1000, O('hairy', 'cll'))
add('<circle cx="1700" cy="640" r="250" style="fill:none;stroke:var(--bad);stroke-width:8"/>', when=O('mantle'))
add('<circle cx="1700" cy="660" r="150" style="fill:var(--bad);fill-opacity:.15;stroke:var(--bad);stroke-width:8"/>', when=O('foll', 'dlbcl', 'hodg'))
add('<circle cx="1700" cy="640" r="330" style="fill:none;stroke:var(--bad);stroke-width:8"/>', when=O('malt'))
hi(300, 1100, 1150, 1280, O('malt'))
hi(800, 760, 1150, 1000, O('pcnsl'))
INFO = dict(
  all=('ALL: blasts arrested early — TdT ⊕, CD10 ⊕ (pre-B)', 't(12;21) better · t(9;22) worse — add imatinib · CNS and testes'),
  cll=('CLL: mature CD5 ⊕ CD23 ⊕ B cells that won’t die — smudge cells', 'AIHA, hypogammaglobulinemia · Richter → DLBCL · ibrutinib, venetoclax'),
  hairy=('Hairy cell: marrow, spleen, liver — dry tap, massive spleen', 'BRAF V600E · TRAP ⊕ · cladribine'),
  mantle=('Mantle cell: naive mantle-zone B cells, cyclin D1 t(11;14), CD5 ⊕ CD23 ⊝', 'very aggressive · rituximab-based, bortezomib'),
  foll=('Follicular: BCL-2 t(14;18) — germinal-center cells that refuse to die', 'waxing-waning nodes · indolent · can become DLBCL'),
  burk=('Burkitt: c-MYC t(8;14) next to the IgH promoter — starry sky', 'jaw (endemic, EBV) or abdomen · tumor lysis risk'),
  dlbcl=('DLBCL: large germinal-center B cells in sheets — BCL-2, BCL-6', 'most common adult NHL · R-CHOP'),
  malt=('Marginal zone: chronic antigen keeps marginal-zone B cells dividing — t(11;18)', 'gastric MALT regresses with H. pylori eradication'),
  hodg=('Hodgkin: Reed-Sternberg cells, crippled germinal-center B cells — CD15 ⊕ CD30 ⊕', 'contiguous spread · EBV · ABVD'),
  pcnsl=('Primary CNS lymphoma: EBV-driven, usually DLBCL type — AIDS', 'single ring-enhancing lesion vs toxoplasmosis · restore immunity'))
for k, (a, b) in INFO.items():
    text(a, 1300, 1400, 'nf-l1 dyn-tag', 'middle', when=O(k)); text(b, 1300, 1432, 'nf-l2', 'middle', when=O(k))
text('Burkitt — the card names no cell of origin; MYC drives every cell to divide', 1700, 1060, 'nf-l1 dyn-tag', 'middle', when=O('burk'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FAST = O('burk', 'all')
flows = [
  dict(d='M700 450 H800', len=100, speed=60, r=10, base=dict(b=2), mods=[m(O('all'), set=dict(b=0))]),
  dict(d='M1150 450 C1250 450 1350 560 1450 600', len=330, speed=90, r=10, base=dict(b=3)),
  dict(d='M1550 660 A150 150 0 1 1 1549.9 659', len=940, speed=160, r=10, base=dict(b=3),
       mods=[m(O('burk'), set=dict(b=8), speed=2), m(O('foll'), set=dict(b=6), speed=0.5)]),
  dict(d='M1850 700 C1950 760 2050 800 2120 850', len=300, speed=90, r=10, base=dict(b=3), mods=[m(O('foll', 'dlbcl', 'hodg'), set=dict(b=1))]),
  dict(d='M500 640 V560 M500 560 V450', len=190, speed=80, r=10, base=dict(blast=4), when=O('all')),
  dict(d='M975 450 V380', len=70, speed=20, r=10, base=dict(b=5), when=O('cll')),
  dict(d='M700 1190 C1000 1150 1300 1050 1380 900', len=700, speed=120, r=8, base=dict(ag=4), when=O('malt')),
]
sites = [dict(x=1700, y=810, n=[0, 1], w=10, t='rec', l='', aria='Follicular lymphoma', c='follicular', ions=[]),
         dict(x=975, y=640, n=[0, 1], w=10, t='rec', l='', aria='CLL', c='cll', ions=[]),
         dict(x=500, y=640, n=[0, 1], w=10, t='rec', l='', aria='ALL', c='alleuk', ions=[])]

readouts = [
  dict(l='Growth rate', mods=[dict(when=O('burk', 'all', 'mantle', 'dlbcl'), d=1), dict(when=O('foll', 'cll', 'malt'), d=-1)]),
  dict(l='TdT ⊕', mods=[dict(when=O('all'), d=1), dict(when=O('cll', 'mantle', 'foll', 'burk', 'dlbcl', 'hairy'), d=-1)]),
  dict(l='CD5 ⊕', mods=[dict(when=O('cll', 'mantle'), d=1), dict(when=O('foll'), d=-1)]),
  dict(l='Tumor lysis risk', mods=[dict(when=O('burk'), d=1)]),
]

notes = {
  '': 'B cells start as precursors in the marrow (TdT, receptor rearrangement), circulate as mature naive cells, and in a lymph node '
      'follicle pass through the germinal center, where cells that fail selection should die; survivors become plasma and memory cells. '
      'Each lymphoid neoplasm is frozen at, or lives in, one of these places.',
  'ly:all': 'ALL: a precursor stops maturing as a blast — TdT ⊕, CD10 ⊕ in B-lineage; replaces the marrow, seeds CNS and testes. Children; '
            'the leukemia most responsive to therapy.',
  'ly:cll': 'CLL / SLL: small mature CD5 ⊕ B cells escape apoptosis and accumulate — lymphocytosis, smudge cells, AIHA, infections; '
            'Richter transformation to DLBCL.',
  'ly:hairy': 'Hairy cell leukemia: mature B cells home to marrow, spleen and liver; marrow fibrosis — dry tap; BRAF V600E. Cladribine.',
  'ly:mantle': 'Mantle cell lymphoma: naive mantle-zone B cells; cyclin D1 t(11;14) pushes G1 → S. CD5 ⊕ like CLL but CD23 ⊝.',
  'ly:foll': 'Follicular lymphoma: BCL-2 t(14;18) — germinal-center B cells that should die survive and accumulate; too little death, '
             'not too much division. Indolent, hard to cure.',
  'ly:burk': 'Burkitt lymphoma: c-MYC t(8;14) under the always-active IgH promoter — the fastest-growing human tumor; starry-sky '
             'macrophages eat the dead cells.',
  'ly:dlbcl': 'DLBCL: large germinal-center B cells in diffuse sheets, alone or transformed from follicular lymphoma or CLL — aggressive '
              'but potentially curable.',
  'ly:malt': 'Marginal zone lymphoma: chronic antigen stimulation keeps marginal-zone B cells dividing — H. pylori, Sjögren, Hashimoto. '
             'Early gastric MALT regresses when H. pylori is cleared.',
  'ly:hodg': 'Hodgkin lymphoma: Reed-Sternberg cells are germinal-center B cells that lost their B-cell program; most of the node is a '
             'reactive crowd. Contiguous spread, so stage predicts outcome.',
  'ly:pcnsl': 'Primary CNS lymphoma: when T-cell surveillance fails, EBV-infected B cells grow in the brain — AIDS-defining.',
}

dyn = dict(
  kinds=dict(b=['cell', '--dk7'], blast=['cell', '--bad'], ag=['cell', '--dk3']), groups=[['cell', 'B cells · antigen']],
  switches=[dict(id='ly', label='Lymphoid neoplasm', type='one', options=[
    ['all', 'ALL', 'alleuk'], ['cll', 'CLL / SLL', 'cll'], ['hairy', 'Hairy cell', 'hairycell'], ['mantle', 'Mantle cell', 'mantle'],
    ['foll', 'Follicular', 'follicular'], ['burk', 'Burkitt', 'burkitt'], ['dlbcl', 'DLBCL', 'dlbcl'], ['malt', 'Marginal zone (MALT)', 'malt'],
    ['hodg', 'Hodgkin', 'hodgkin'], ['pcnsl', 'Primary CNS lymphoma', 'pcnsl']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 434–440 · Robbins ch 13')

MAP = dict(
  id='bcellsim', title='B Cells & Lymphomas in Motion', topic='heme', after='hemeonc',
  sub='Follow a B cell from marrow to blood to the follicle’s mantle, germinal center and marginal zone, then light up where each '
      'leukemia or lymphoma comes from — ALL, CLL, hairy cell, mantle, follicular, Burkitt, DLBCL, MALT, Hodgkin and CNS lymphoma',
  w=3600, h=1900,
  fa='107, 173, 220, 223, 429, 434, 435, 437, 439, 440, 444, 446, 447',
  src=['Robbins ch 13 — Diseases of white blood cells, lymph nodes, spleen, and thymus', 'Katzung ch 54 — Cancer Chemotherapy',
       'Katzung ch 55 — Immunopharmacology', 'Robbins ch 7 — Neoplasia', 'Robbins ch 28 — The central nervous system',
       'Robbins ch 6 — Diseases of the immune system', 'Robbins ch 17 — The gastrointestinal tract'],
  lanes=[('bcLeuk', 'Leukemias', 'glycolysis'), ('bcNHL', 'Non-Hodgkin lymphomas', 'tca'), ('bcHod', 'Hodgkin & CNS', 'gluconeo')],
  nodes=[
    ('bc1', 'ALL', 330, 1660, 'bcLeuk', 'TdT ⊕', ['alleuk'], 'hub'),
    ('bc2', 'CLL', 760, 1660, 'bcLeuk', 'smudge cells', ['cll']),
    ('bc3', 'Hairy cell leukemia', 1200, 1660, 'bcLeuk', 'BRAF · dry tap', ['hairycell']),
    ('bc4', 'Mantle cell', 1640, 1660, 'bcNHL', 'cyclin D1', ['mantle']),
    ('bc5', 'Follicular', 2080, 1660, 'bcNHL', 'BCL-2', ['follicular']),
    ('bc6', 'Burkitt', 330, 1790, 'bcNHL', 'c-MYC · starry sky', ['burkitt']),
    ('bc7', 'DLBCL', 760, 1790, 'bcNHL', 'most common', ['dlbcl']),
    ('bc8', 'Marginal zone · MALT', 1200, 1790, 'bcNHL', 'H. pylori', ['malt']),
    ('bc9', 'Hodgkin · CNS lymphoma', 1640, 1790, 'bcHod', 'Reed-Sternberg · EBV', ['hodgkin', 'pcnsl'])],
  panels=[
    (2500, PANY, 1000, 'Translocations (First Aid p. 437)', [
      ('t(14;18)', 'follicular — BCL-2'), ('t(11;14)', 'mantle cell — cyclin D1'), ('t(8;14)', 'Burkitt — c-MYC'),
      ('t(11;18)', 'marginal zone'), ('t(9;22)', 'ALL — worse prognosis')])],
  dyn=dyn)
