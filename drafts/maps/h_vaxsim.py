# Vaccines in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Injection site → antigen-presenting cell → helper T cell and cytotoxic T cell (cellular) → B cell → plasma cells and
# antibodies (humoral) → memory, with the antigen and the signals moving. A `one` switch gives the vaccine type — live
# attenuated, inactivated, subunit/recombinant, conjugate, plain polysaccharide, toxoid, mRNA — and the arms it uses light up
# or go quiet: a plain polysaccharide reaches the B cell with no T-cell help, a conjugate brings the helper T cell in, a
# toxoid's antibodies neutralize a toxin, a live vaccine replicates briefly. 5 readouts. Facts from the pinned cards; FA
# pages in `fa`. No new cards.
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

O = lambda *k: [f'vx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def cell(x, y, r, lab, sub, c):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var({c});fill-opacity:.18;stroke:var({c});stroke-width:4"/>')
    text(lab, x, y + 2, 'nf-l1', 'middle'); text(sub, x, y + 26, 'nf-l2', 'middle')
CELL = O('live', 'mrna')                     # both arms, strong cellular
TDEP = O('live', 'killed', 'sub', 'conj', 'toxoid', 'mrna')
TIND = O('ps')

text('Vaccines — which arms of immunity each type switches on', 180, 150, 'dyn-big')
text('pick a vaccine type and follow the antigen', 180, 176, 'dyn-cap')

add('<rect x="300" y="300" width="300" height="200" rx="30" class="dyn-soft"/>'); text('Injection site', 450, 340, 'nf-l1', 'middle')
cell(800, 400, 90, 'APC', 'presents antigen', '--dk2')
cell(1200, 300, 80, 'Helper T', 'T-cell help', '--dk5')
cell(1200, 560, 80, 'Cytotoxic T', 'cellular immunity', '--dk1')
cell(1600, 420, 80, 'B cell', '', '--dk7')
cell(2000, 300, 70, 'Plasma cell', 'antibodies', '--dk4')
cell(2000, 560, 70, 'Memory', '', '--dk9')
add('<rect x="1850" y="760" width="400" height="140" rx="30" class="dyn-soft"/>'); text('Toxin', 2050, 800, 'nf-l1', 'middle')
text('antibodies neutralize the toxin', 2050, 870, 'nf-l1 dyn-tag', 'middle', when=O('toxoid'))
add(X(1270, 240, 14) + X(1270, 500, 14), when=TIND)
text('polysaccharide can’t be presented to T cells — T-cell–independent', 1200, 200, 'nf-l1 dyn-tag', 'middle', when=TIND)
text('carrier protein brings in T-cell help — T-cell–dependent', 1200, 200, 'nf-l1 dyn-tag', 'middle', when=O('conj'))
text('replicates briefly — can revert to a virulent form', 450, 540, 'nf-l1 dyn-tag', 'middle', when=O('live'))
text('lipid nanoparticle → your cells make the protein', 450, 540, 'nf-l1 dyn-tag', 'middle', when=O('mrna'))
text('inactivated — can’t revert; boosters usually needed', 450, 540, 'nf-l1 dyn-tag', 'middle', when=O('killed'))
text('chosen antigens only — fewer reactions, weaker response', 450, 540, 'nf-l1 dyn-tag', 'middle', when=O('sub'))
text('denatured toxin, receptor-binding site intact', 450, 540, 'nf-l1 dyn-tag', 'middle', when=O('toxoid'))
EX = dict(live='MMR, varicella, yellow fever, rotavirus, oral polio, intranasal flu, BCG, oral typhoid · NOT in pregnancy or immunodeficiency',
          killed='hepatitis A, typhoid (Vi, IM), rabies, IM influenza, Salk polio — “A TRIP could Kill you”',
          sub='hepatitis B (HBsAg), HPV, recombinant zoster, acellular pertussis',
          conj='PCV13/15/20, Hib, meningococcal ACWY (on diphtheria toxoid) — infants at 2, 4, 6 months',
          ps='PPSV23 — pneumococcal polysaccharide, 23 serotypes', toxoid='tetanus, diphtheria — Td/Tdap every 10 years; Tdap each pregnancy',
          mrna='SARS-CoV-2 — safe in pregnancy; rare myocarditis in young males')
for k, t in EX.items(): text(t, 1275, 1060, 'nf-l1', 'middle', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def f(d, L, k, n, when=None, low=None, stop=None):
    x = dict(d=d, len=L, speed=110, r=9, base={k: n}, mods=[])
    if low: x['mods'].append(m(low, set={k: 1}))
    if stop: x['mods'].append(m(stop, set={k: 0}))
    if when: x['when'] = when
    return x
flows = [
  f('M600 400 H710', 110, 'ag', 3, when=['vx:*'], stop=TIND),
  f('M600 440 C900 700 1300 700 1530 470', 1000, 'ag', 3, when=TIND),
  f('M880 360 L1120 310', 250, 'sig', 3, when=TDEP),
  f('M880 440 L1120 540', 260, 'sig', 3, when=TDEP, low=O('killed', 'sub', 'conj', 'toxoid')),
  f('M1280 320 L1520 400', 250, 'sig', 3, when=TDEP),
  f('M1680 400 L1930 310', 270, 'ab', 3, when=['vx:*']),
  f('M1680 440 L1930 550', 270, 'ab', 3, when=TDEP),
  f('M2070 300 H2300', 230, 'ab', 4, when=['vx:*'], low=O('sub')),
  f('M2050 370 V760', 390, 'ab', 4, when=O('toxoid')),
  f('M450 300 C420 220 520 220 500 300', 240, 'ag', 3, when=O('live')),
]
sites = [dict(x=800, y=490, n=[0, 1], w=10, t='rec', l='', aria='Live vaccines', c='vxlive', ions=[]),
         dict(x=1600, y=500, n=[0, 1], w=10, t='rec', l='', aria='Conjugate vaccines', c='vxconj', ions=[]),
         dict(x=2050, y=900, n=[0, 1], w=10, t='rec', l='', aria='Toxoids', c='vxtoxoid', ions=[])]

readouts = [
  dict(l='Humoral (antibody)', mods=[dict(when=['vx:*'], d=1)]),
  dict(l='Cell-mediated', mods=[dict(when=CELL, d=1), dict(when=O('killed', 'ps'), d=-1)]),
  dict(l='T-cell help', mods=[dict(when=O('conj', 'live', 'mrna'), d=1), dict(when=TIND, d=-1)]),
  dict(l='Boosters needed', mods=[dict(when=O('killed', 'toxoid'), d=1)]),
  dict(l='OK in immunodeficiency', mods=[dict(when=O('live'), d=-1)]),
]

notes = {
  '': 'A vaccine shows the immune system an antigen so memory is ready before the real infection. What is injected decides which arms '
      'respond: humoral (B cells, antibodies) and cell-mediated (T cells).',
  'vx:live': 'Live attenuated: a nonpathogenic organism that still grows briefly — strong, often lifelong cellular and humoral immunity, '
             'but it can revert. Contraindicated in pregnancy and immunodeficiency (MMR and varicella allowed in HIV with CD4 ≥ 200).',
  'vx:killed': 'Inactivated: heat or chemicals keep the surface epitopes — mainly humoral, weaker cell-mediated, boosters usually needed; '
               'can’t revert.',
  'vx:sub': 'Subunit/recombinant: only the antigens that best stimulate immunity — fewer adverse reactions, but costlier and weaker.',
  'vx:conj': 'Conjugate: a capsular polysaccharide joined to a carrier protein brings in T-cell help — a T-cell–dependent response. '
             'Hib, PCV, meningococcal ACWY.',
  'vx:ps': 'Plain polysaccharide (PPSV23): the capsule can’t be presented to T cells, so the response is mainly T-cell–independent.',
  'vx:toxoid': 'Toxoid: a toxin denatured but with its receptor-binding site intact — antibodies against the toxin; antitoxin wanes, '
               'so boosters every 10 years and after a wound if > 5 years.',
  'vx:mrna': 'mRNA: a lipid nanoparticle delivers mRNA and the patient’s cells make the protein (spike) — cellular and humoral immunity.',
}

dyn = dict(
  kinds=dict(ag=['ag', '--dk3'], sig=['sig', '--dk5'], ab=['ab', '--dk4']),
  groups=[['ag', 'Antigen'], ['sig', 'T-cell signals'], ['ab', 'Antibodies']],
  switches=[dict(id='vx', label='Vaccine type', type='one', options=[
    ['live', 'Live attenuated', 'vxlive'], ['killed', 'Inactivated', 'vxkilled'], ['sub', 'Subunit / recombinant', 'vxsub'],
    ['conj', 'Conjugate', 'vxconj'], ['ps', 'Polysaccharide only', 'vxconj'], ['toxoid', 'Toxoid', 'vxtoxoid'], ['mrna', 'mRNA', 'vxmrna']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 109, 114, 116, 125 · Katzung Appendix 1')

MAP = dict(
  id='vaxsim', title='Vaccines in Motion', topic='immuno', after='vaccines',
  sub='Follow the antigen from the injection site to APCs, T cells and B cells and see which arms each vaccine type uses — live, '
      'inactivated, subunit, conjugate vs polysaccharide, toxoid and mRNA',
  w=3600, h=1900,
  fa='109, 114, 116, 125',
  src=['Katzung Appendix 1 — Vaccines, Immune Globulins, & Other Complex Biologic Products'],
  lanes=[('vxWhole', 'Whole organism', 'glycolysis'), ('vxPart', 'Parts of it', 'tca'), ('vxGene', 'Genetic', 'gluconeo')],
  nodes=[
    ('vx1', 'Live attenuated', 330, 1660, 'vxWhole', 'strong, can revert', ['vxlive'], 'hub'),
    ('vx2', 'Inactivated', 760, 1660, 'vxWhole', 'A TRIP could Kill you', ['vxkilled']),
    ('vx3', 'Subunit · recombinant', 1200, 1660, 'vxPart', 'HBV, HPV, zoster', ['vxsub']),
    ('vx4', 'Conjugate vs polysaccharide', 1640, 1660, 'vxPart', 'T-cell help', ['vxconj']),
    ('vx5', 'Toxoid', 2080, 1660, 'vxPart', 'tetanus, diphtheria', ['vxtoxoid']),
    ('vx6', 'mRNA', 330, 1790, 'vxGene', 'your cells make it', ['vxmrna'])],
  panels=[
    (2500, PANY, 1000, 'Vaccine types (First Aid p. 109)', [
      ('Live attenuated', 'cellular + humoral; not in pregnancy/immunodeficiency'),
      ('Inactivated', 'mainly humoral; boosters'), ('Conjugate', 'T-cell–dependent'),
      ('Polysaccharide', 'T-cell–independent'), ('Toxoid', 'anti-toxin antibodies')])],
  dyn=dyn)
