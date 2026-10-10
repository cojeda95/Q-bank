# Blisters — Where the Skin Splits (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A drawn cross-section of skin (corneum, granulosum, spinosum, basale, basement membrane, dermis with papillae).
# One `one` switch picks the disease and draws its blister at the level where the skin splits, with the
# immunofluorescence pattern underneath: SSSS (granulosum), pemphigus vulgaris (spinosum — acantholysis,
# tombstones, net-like IgG), bullous pemphigoid (below the basale — linear IgG/C3, eosinophils), dermatitis
# herpetiformis (IgA at the papillary tips), SJS/TEN (the whole epidermis). 4 readouts (↑ present · ↓ absent).
# Facts from the pinned cards (pemphigus, pemphigoid, dh, ssss, sjs, skinlayers, dermmicro, celiac, hs2); their FA
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


SW = 'dz'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 700

# ════════ the skin ════════
box(160, 130, 2340, 1370)
text('Skin in cross-section — where does it split?', 190, 170, 'dyn-big')
text('the deeper the split, the thicker and tenser the blister roof', 190, 196, 'dyn-cap')
X0, X1 = 380, 2240
L = [('corneum', 'Stratum corneum', 300, 340, '--dk4'), ('gran', 'Stratum granulosum', 340, 384, '--dk5'),
     ('spin', 'Stratum spinosum', 384, 530, '--dk3'), ('bas', 'Stratum basale', 530, 600, '--dk9')]
for k, lab, y0, y1, col in L:
    add(f'<rect x="{X0}" y="{y0}" width="{X1 - X0}" height="{y1 - y0}" style="fill:var({col});fill-opacity:.22;stroke:none"/>')
    text(lab, X0 - 16, (y0 + y1) // 2 + 5, 'nf-l2', 'end')
# basement membrane with dermal papillae (bumps)
PAP = [520 + i * 240 for i in range(7)]
bm = f'M{X0} 600 ' + ' '.join(f'L{p - 70} 600 Q{p} 500 {p + 70} 600' for p in PAP) + f' L{X1} 600'
add(f'<path d="{bm} L{X1} 900 L{X0} 900 Z" style="fill:var(--dk1);fill-opacity:.16;stroke:none"/>')
add(f'<path d="{bm}" style="fill:none;stroke:var(--dk11);stroke-width:5"/>')
text('basement membrane · hemidesmosomes', X0 - 16, 606, 'nf-l2', 'end')
text('Dermis', X0 - 16, 780, 'nf-l1', 'end')
text('dermal papillae', PAP[0], 660, 'nf-l2', 'middle')
# keratinocyte outlines (desmosome junctions) in the spinosum
for x in range(X0 + 60, X1, 120):
    add(f'<path d="M{x} 392 V522" style="stroke:var(--line-2);stroke-width:2;stroke-dasharray:4 6"/>')

CX = 1300
# SSSS: split in the granulosum
add(f'<ellipse cx="{CX}" cy="350" rx="380" ry="26" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3"/>', when=O('ssss'))
text('split in the granulosum — only the upper epidermis peels', CX, 268, 'nf-l1 dyn-tag', 'middle', when=O('ssss'))
# pemphigus: suprabasal, tombstones
add(f'<path d="M{CX - 360} 528 Q{CX} 400 {CX + 360} 528 Z" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3"/>', when=O('pv'))
for i in range(-5, 6):
    add(f'<rect x="{CX + i * 56 - 16}" y="532" width="32" height="38" rx="6" style="fill:var(--dk9);fill-opacity:.55"/>', when=O('pv'))
text('acantholysis above the basale — a row of tombstones', CX, 268, 'nf-l1 dyn-tag', 'middle', when=O('pv'))
# pemphigoid: subepidermal, eosinophils
add(f'<path d="M{CX - 360} 600 Q{CX} 520 {CX + 360} 600 Q{CX} 690 {CX - 360} 600 Z" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3"/>', when=O('bp'))
for i, (dx, dy) in enumerate(((-200, 600), (-90, 630), (40, 590), (150, 640), (250, 605))):
    add(f'<circle cx="{CX + dx}" cy="{dy}" r="9" style="fill:var(--bad)"/>', when=O('bp'))
text('subepidermal — the whole epidermis is the roof · eosinophils', CX, 268, 'nf-l1 dyn-tag', 'middle', when=O('bp'))
# dermatitis herpetiformis: IgA at the papillary tips, small vesicles
for p in PAP:
    add(f'<circle cx="{p}" cy="540" r="34" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3"/>', when=O('dh'))
text('small vesicles over the dermal papillae', CX, 268, 'nf-l1 dyn-tag', 'middle', when=O('dh'))
# SJS / TEN: the whole epidermis separates
add(f'<path d="M{X0 + 80} 600 H{X1 - 80}" style="stroke:var(--surface);stroke-width:26"/>', when=O('ten'))
add(f'<rect x="{X0}" y="300" width="{X1 - X0}" height="272" style="fill:var(--ink-3);fill-opacity:.18"/>', when=O('ten'))
text('keratinocytes die along the dermal-epidermal junction — the epidermis sheets off', CX, 268, 'nf-l1 dyn-tag', 'middle', when=O('ten'))
text('pick a disease to see where the skin splits', CX, 268, 'nf-l1', 'middle', unless=[f'{SW}:*'])

# ════════ immunofluorescence ════════
text('Direct immunofluorescence', 190, 990, 'dyn-big')
add('<rect x="380" y="1030" width="900" height="280" rx="20" style="fill:var(--ink);fill-opacity:.85"/>')
# net (pemphigus)
for x in range(420, 1260, 60):
    add(f'<path d="M{x} 1050 V1290" style="stroke:var(--ok);stroke-width:3"/>', when=O('pv'))
for y in range(1060, 1300, 50):
    add(f'<path d="M400 {y} H1260" style="stroke:var(--ok);stroke-width:3"/>', when=O('pv'))
# linear (pemphigoid)
add('<path d="M400 1180 Q830 1140 1260 1180" style="fill:none;stroke:var(--ok);stroke-width:8"/>', when=O('bp'))
# granular at papillary tips (DH)
for x in range(460, 1260, 140):
    for dx, dy in ((0, 0), (14, 10), (-12, 12), (6, -12)):
        add(f'<circle cx="{x + dx}" cy="{1170 + dy}" r="6" style="fill:var(--ok)"/>', when=O('dh'))
IF = dict(pv='reticular, net-like IgG around each keratinocyte', bp='linear IgG and C3 along the dermal-epidermal junction',
          dh='granular IgA at the tips of the dermal papillae', ssss='toxin, not antibody — blisters often culture-negative',
          ten='drug reaction (or Mycoplasma, HSV) — no antibody pattern')
for k, t in IF.items():
    text(t, 1330, 1176, 'nf-l1', when=O(k))

# ════════ readouts — ↑ present · ↓ absent ════════
readouts = [
  dict(l='Nikolsky sign', mods=[dict(when=O('pv', 'ssss', 'ten'), d=1), dict(when=O('bp'), d=-1)]),
  dict(l='Oral mucosa involved', mods=[dict(when=O('pv', 'ten'), d=1), dict(when=O('bp', 'ssss'), d=-1)]),
  dict(l='Eosinophils in the blister', mods=[dict(when=O('bp'), d=1)]),
  dict(l='Anti-tTG IgA', mods=[dict(when=O('dh'), d=1)]),
]

# blister fluid moving inside each cavity
flows = [
  dict(d=f'M{CX - 300} 350 H{CX + 300} H{CX - 300}', len=1200, speed=110, r=6, base=dict(fl=8), when=O('ssss')),
  dict(d=f'M{CX - 240} 495 H{CX + 240} H{CX - 240}', len=960, speed=90, r=7, base=dict(fl=7), when=O('pv')),
  dict(d=f'M{CX - 280} 605 H{CX + 280} H{CX - 280}', len=1120, speed=90, r=7, base=dict(fl=7), when=O('bp')),
  dict(d=f'M{PAP[0]} 540 H{PAP[-1]} H{PAP[0]}', len=2 * (PAP[-1] - PAP[0]), speed=120, r=6, base=dict(fl=10), when=O('dh')),
  dict(d=f'M{X0 + 100} 600 H{X1 - 100} H{X0 + 100}', len=2 * (X1 - X0 - 200), speed=160, r=6, base=dict(fl=12), when=O('ten')),
]

sites = [
  dict(x=CX + 500, y=455, n=[0, -1], w=20, t='md', l='', aria='Desmosomes — desmoglein', c='pemphigus', ions=[]),
  dict(x=CX + 500, y=600, n=[0, 1], w=10, t='wall', l='', aria='Hemidesmosomes', c='pemphigoid', ions=[]),
]

# ════════ notes ════════
notes = {
  '': 'Blisters are named by the level of the split. Desmosomes hold keratinocytes to each other; hemidesmosomes anchor the basale '
      'to the basement membrane. In the readouts ↑ means present and ↓ absent.',
  'dz:ssss': 'Staphylococcal scalded skin syndrome: exfoliative toxin cleaves desmoglein 1 in the stratum granulosum, so only the '
             'upper epidermis peels and it heals completely. Nikolsky positive, mucosa spared.',
  'dz:pv': 'Pemphigus vulgaris: IgG against desmogleins (type II hypersensitivity) breaks desmosomes in the spinosum — acantholysis, '
           'flaccid bullae, oral involvement, Nikolsky positive, net-like IgG.',
  'dz:bp': 'Bullous pemphigoid: IgG against hemidesmosomes lifts the whole epidermis — tense blisters full of eosinophils, mucosa '
           'spared, Nikolsky negative, linear IgG and C3. Less severe than pemphigus.',
  'dz:dh': 'Dermatitis herpetiformis: granular IgA at the tips of the dermal papillae — intensely itchy vesicles on the elbows, '
           'knees and buttocks; the skin sign of celiac disease (anti-tTG).',
  'dz:ten': 'SJS and TEN: keratinocytes die along the dermal-epidermal junction, with fever, mucosal involvement and a positive '
            'Nikolsky sign — SJS under 10% of body surface, TEN over 30%. Sulfa, β-lactams, phenytoin.',
}

dyn = dict(
  kinds=dict(fl=['fl', '--nf-h2o']), groups=[['fl', 'Blister fluid']],
  switches=[dict(id=SW, label='Disease', type='one', options=[
    ['ssss', 'Staphylococcal scalded skin', 'ssss'], ['pv', 'Pemphigus vulgaris', 'pemphigus'], ['bp', 'Bullous pemphigoid', 'pemphigoid'],
    ['dh', 'Dermatitis herpetiformis', 'dh'], ['ten', 'SJS · TEN', 'sjs']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 481, 487–490 · Robbins ch 25')

MAP = dict(
  id='blistsim', title='Blisters — Where the Skin Splits', topic='msk', after='derm',
  sub='Pick a blistering disease and see the split drawn at its level — granulosum, spinosum, below the basale, the papillary '
      'tips or the whole epidermis — with its immunofluorescence pattern, Nikolsky sign and mucosal involvement',
  w=3500, h=1700,
  fa='110, 251, 388, 481, 487, 489–490',
  src=[full('Robbins', 25), full('Robbins', 8), full('Robbins', 6), full('Pawlina', 15)],
  lanes=[('blLayer', 'Skin layers', 'glycolysis'), ('blAb', 'Antibody blisters', 'tca'), ('blOther', 'Toxin & drug', 'gluconeo')],
  nodes=[
    ('bl1', 'Epidermal layers', 330, 1470, 'blLayer', 'basale to corneum', ['skinlayers', 'dermmicro'], 'hub'),
    ('bl2', 'Pemphigus vulgaris', 760, 1470, 'blAb', 'desmoglein', ['pemphigus']),
    ('bl3', 'Bullous pemphigoid', 1180, 1470, 'blAb', 'hemidesmosome', ['pemphigoid']),
    ('bl4', 'Dermatitis herpetiformis', 1600, 1470, 'blAb', 'IgA · celiac', ['dh', 'celiac']),
    ('bl5', 'Type II hypersensitivity', 2020, 1470, 'blAb', 'antibody to tissue', ['hs2']),
    ('bl6', 'Scalded skin syndrome', 330, 1600, 'blOther', 'exfoliative toxin', ['ssss']),
    ('bl7', 'EM · SJS · TEN', 760, 1600, 'blOther', 'drugs', ['sjs'])],
  panels=[
    (2420, PANY, 1000, 'Pemphigus vs pemphigoid (First Aid p. 489)', [
      ('Target', 'desmosomes · hemidesmosomes'),
      ('Split', 'intraepidermal · subepidermal'),
      ('Blister', 'flaccid · tense'),
      ('Oral mucosa', 'involved · spared'),
      ('Nikolsky', 'positive · negative'),
      ('Immunofluorescence', 'net-like · linear')])],
  dyn=dyn)
