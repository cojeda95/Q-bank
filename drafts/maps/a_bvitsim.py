# B Vitamins & Zinc in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Each vitamin is drawn becoming its coenzyme and feeding the enzymes its card names: B2 → FAD/FMN (succinate dehydrogenase,
# acyl-CoA dehydrogenase, glutathione reductase), B3 → NAD⁺/NADP⁺ (also made from tryptophan with B6), B5 → CoA (acyl
# transfer, fatty-acid synthase), B7 → biotin carboxylases (pyruvate, acetyl-CoA, propionyl-CoA), zinc → zinc fingers and
# metalloenzymes. A `def` switch removes one — its enzymes stall and its signs light on a body; a `cause` switch shows the
# card-named ways to lose niacin (corn diet, Hartnup, carcinoid, isoniazid) or biotin (raw egg whites, antibiotics). Layout
# schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

D = lambda *k: [f'def:{x}' for x in k]
C = lambda *k: [f'cause:{x}' for x in k]
PANY = 1180
NIA_LOSS = D('b3') + C('corn', 'hartnup', 'carcinoid', 'inh')
BIO_LOSS = D('b7') + C('egg', 'abx')
LOST = dict(b2=D('b2'), b3=NIA_LOSS, b5=D('b5'), b7=BIO_LOSS, zn=D('zn'))
VIT = dict(b2=(300, 360, 'B2 riboflavin', 'FAD · FMN', '--dk4'), b3=(300, 600, 'B3 niacin', 'NAD⁺ · NADP⁺', '--dk9'),
           b5=(300, 840, 'B5 pantothenate', 'CoA', '--dk5'), b7=(300, 1080, 'B7 biotin', 'carboxylases', '--dk10'),
           zn=(300, 1320, 'zinc', 'zinc fingers', '--dk7'))
ENZ = dict(b2=('succinate dehydrogenase', 'acyl-CoA dehydrogenase', 'glutathione reductase'), b3=('redox (NAD⁺ / NADP⁺)',),
           b5=('acyl transfer — TCA, fatty-acid oxidation', 'fatty-acid synthase (ACP)'),
           b7=('pyruvate carboxylase', 'acetyl-CoA carboxylase', 'propionyl-CoA carboxylase'), zn=('transcription factors', 'metalloenzymes'))
SIGN = dict(b2='cheilosis · corneal vascularization · magenta tongue', b3='3 D’s: diarrhea, dermatitis (Casal necklace), dementia · glossitis',
            b5='dermatitis, enteritis, alopecia · adrenal insufficiency · burning feet', b7='dermatitis, alopecia, enteritis',
            zn='periorificial rash, hair loss, diarrhea · poor wound healing, low immunity, hypogonadism, taste and smell loss')

text('B vitamins & zinc — what each becomes, what it runs, what fails without it', 180, 150, 'dyn-big')
text('vitamin → coenzyme → enzymes · remove one to see what stalls · schematic', 180, 176, 'dyn-cap')
for k, (x, y, l, co, c) in VIT.items():
    add(f'<rect x="{x - 120}" y="{y - 40}" width="240" height="80" rx="20" style="fill:var({c});fill-opacity:.2;stroke:var({c});stroke-width:3"/>', unless=LOST[k])
    add(f'<rect x="{x - 120}" y="{y - 40}" width="240" height="80" rx="20" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 6"/>', when=LOST[k])
    text(l, x, y + 8, 'nf-l1', 'middle')
    add(f'<circle cx="{x + 330}" cy="{y}" r="44" style="fill:var({c});fill-opacity:.3;stroke:var({c});stroke-width:3"/>', unless=LOST[k])
    add(f'<circle cx="{x + 330}" cy="{y}" r="44" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:6 6"/>', when=LOST[k])
    text(co, x + 330, y + 70, 'nf-l2', 'middle')
    for i, e in enumerate(ENZ[k]):
        ey = y - 50 + i * 50 if len(ENZ[k]) > 1 else y
        add(f'<rect x="880" y="{ey - 20}" width="440" height="40" rx="12" style="fill:var(--surface);stroke:var({c});stroke-width:3"/>', unless=LOST[k])
        add(f'<rect x="880" y="{ey - 20}" width="440" height="40" rx="12" style="fill:var(--bad);fill-opacity:.15;stroke:var(--bad);stroke-width:3"/>', when=LOST[k])
        text(e, 900, ey + 6, 'nf-l2')
        add(f'<path d="M1300 {ey - 12} l20 24 M1320 {ey - 12} l-20 24" class="nf-x"/>', when=LOST[k])
# tryptophan → niacin
add('<rect x="40" y="440" width="140" height="60" rx="16" style="fill:var(--dk3);fill-opacity:.15;stroke:var(--dk3);stroke-width:3"/>'); text('tryptophan', 110, 476, 'nf-l2', 'middle')
add('<path d="M180 470 C210 520 200 560 180 590" style="fill:none;stroke:var(--dk3);stroke-width:5;stroke-dasharray:8 6"/>'); text('B6 needed', 210, 540, 'nf-l2')
add('<path d="M110 440 V420" style="stroke:var(--bad);stroke-width:5"/>', when=C('carcinoid')); text('→ serotonin', 120, 410, 'nf-l2', when=C('carcinoid'))
add('<rect x="40" y="440" width="140" height="60" rx="16" style="fill:none;stroke:var(--bad);stroke-width:4"/>', when=C('hartnup'))
# body
BX, BY = 1700, 820
add(f'<circle cx="{BX}" cy="{BY - 360}" r="90" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:4"/>')
add(f'<path d="M{BX - 140} {BY - 260} H{BX + 140} L{BX + 170} {BY + 300} H{BX - 170} Z" style="fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:4"/>')
SPOT = dict(b2=[(BX - 20, BY - 330), (BX + 30, BY - 380)], b3=[(BX, BY - 250), (BX, BY)], b5=[(BX - 100, BY + 360), (BX + 100, BY + 360), (BX, BY - 120)],
            b7=[(BX, BY - 440), (BX - 80, BY - 60)], zn=[(BX - 40, BY - 320), (BX, BY - 440), (BX, BY + 120)])
for k, pts in SPOT.items():
    for x, y in pts:
        add(f'<circle cx="{x}" cy="{y}" r="30" style="fill:var(--bad);fill-opacity:.4"/>', when=LOST[k])
for k, s in SIGN.items(): text(s, BX, BY + 470, 'nf-l1 dyn-tag', 'middle', when=LOST[k])
CT = dict(corn='untreated corn diet', hartnup='Hartnup disease — tryptophan not absorbed', carcinoid='malignant carcinoid — tryptophan diverted to serotonin',
          inh='isoniazid — depletes B6', egg='raw egg whites — avidin binds biotin', abx='prolonged antibiotics')
for k, s in CT.items(): text('cause: ' + s, 1150, 1520, 'nf-l1', 'middle', when=C(k))

# ════════ motion ════════
flows = []
for k, (x, y, l, co, c) in VIT.items():
    flows.append(dict(d=f'M{x + 120} {y} H{x + 286}', len=170, speed=70, r=8, base={'v' + k: 3}, mods=[dict(when=LOST[k], set={'v' + k: 0})]))
    for i, e in enumerate(ENZ[k]):
        ey = y - 50 + i * 50 if len(ENZ[k]) > 1 else y
        flows.append(dict(d=f'M{x + 374} {y} C{x + 470} {y} 800 {ey} 880 {ey}', len=260, speed=80, r=7, base={'v' + k: 2}, mods=[dict(when=LOST[k], set={'v' + k: 0})]))
flows.append(dict(d='M110 500 C110 560 140 600 180 600', len=140, speed=60, r=7, base=dict(vb3=2), mods=[dict(when=C('hartnup', 'carcinoid', 'inh'), set=dict(vb3=0))]))
sites = [dict(x=VIT['b2'][0] - 140, y=VIT['b2'][1], n=[-1, 0], w=10, t='rec', l='', aria='Riboflavin', c='b2def', ions=[]),
         dict(x=VIT['b3'][0] - 140, y=VIT['b3'][1] + 40, n=[-1, 1], w=10, t='rec', l='', aria='Niacin', c='b3def', ions=[]),
         dict(x=VIT['b5'][0] - 140, y=VIT['b5'][1], n=[-1, 0], w=10, t='rec', l='', aria='Pantothenate', c='b5def', ions=[]),
         dict(x=VIT['b7'][0] - 140, y=VIT['b7'][1], n=[-1, 0], w=10, t='rec', l='', aria='Biotin', c='b7def', ions=[]),
         dict(x=VIT['zn'][0] - 140, y=VIT['zn'][1], n=[-1, 0], w=10, t='rec', l='', aria='Zinc', c='zinc', ions=[])]

readouts = [
  dict(l='TCA cycle flux', mods=[dict(when=LOST['b2'] + LOST['b5'], d=-1)]),
  dict(l='Gluconeogenesis', mods=[dict(when=LOST['b7'], d=-1)]),
  dict(l='Skin & hair', mods=[dict(when=LOST['b3'] + LOST['b5'] + LOST['b7'] + LOST['zn'], d=-1)]),
  dict(l='Wound healing · immunity', mods=[dict(when=LOST['zn'], d=-1)]),
]

notes = {
  '': 'Each water-soluble vitamin becomes a coenzyme for a set of enzymes; zinc holds hundreds of enzymes and transcription '
      'factors together. Remove one to see what stalls and what shows.',
  'def:b2': 'Riboflavin → FAD and FMN for succinate dehydrogenase, acyl-CoA dehydrogenase, glutathione reductase. Deficiency: '
            'cheilosis, corneal vascularization (the 2 C’s), magenta tongue.',
  'def:b3': 'Niacin → NAD⁺ and NADP⁺; also made from tryptophan with B6. Pellagra: diarrhea, dermatitis (Casal necklace), dementia; '
            'glossitis. Excess niacin: flushing (aspirin blunts), hyperglycemia, hyperuricemia.',
  'def:b5': 'Pantothenate is the backbone of CoA (and part of fatty-acid synthase) — every acyl transfer slows: dermatitis, '
            'enteritis, alopecia, adrenal insufficiency, burning feet.',
  'def:b7': 'Biotin carries CO₂ for every carboxylase — gluconeogenesis, fatty-acid synthesis and odd-chain catabolism stall: '
            'dermatitis, alopecia, enteritis.',
  'def:zn': 'Zinc: fast-turnover tissues fail first — periorificial and acral rash, hair loss, diarrhea (acrodermatitis '
            'enteropathica), poor healing, low immunity, hypogonadism, dysgeusia, anosmia.',
  'cause:corn': 'An untreated corn diet causes pellagra.', 'cause:hartnup': 'Hartnup disease: tryptophan is not absorbed → pellagra.',
  'cause:carcinoid': 'Malignant carcinoid diverts tryptophan to serotonin → pellagra.', 'cause:inh': 'Isoniazid depletes B6, so tryptophan cannot become niacin.',
  'cause:egg': 'Raw egg whites: avidin binds biotin.', 'cause:abx': 'Prolonged antibiotic use causes biotin deficiency.',
}

dyn = dict(
  kinds=dict(vb2=['mov', '--dk4'], vb3=['mov', '--dk9'], vb5=['mov', '--dk5'], vb7=['mov', '--dk10'], vzn=['mov', '--dk7']),
  groups=[['mov', 'Coenzymes at work']],
  switches=[dict(id='def', label='Deficiency', type='one', options=[
              ['b2', 'B2 riboflavin', 'b2def'], ['b3', 'B3 niacin', 'b3def'], ['b5', 'B5 pantothenate', 'b5def'], ['b7', 'B7 biotin', 'b7def'],
              ['zn', 'Zinc', 'zinc']]),
            dict(id='cause', label='Cause', type='one', options=[
              ['corn', 'Corn diet (B3)', 'b3def'], ['hartnup', 'Hartnup (B3)', 'b3def'], ['carcinoid', 'Carcinoid (B3)', 'b3def'],
              ['inh', 'Isoniazid (B3)', 'b3def'], ['egg', 'Raw egg whites (B7)', 'b7def'], ['abx', 'Antibiotics (B7)', 'b7def']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Marks ch 23')

MAP = dict(
  id='bvitsim', title='B Vitamins & Zinc in Motion', topic='bio', after='vitamins',
  sub='Watch riboflavin, niacin, pantothenate, biotin and zinc become the coenzymes that run their enzymes — then take one away and '
      'see the enzymes stall and the deficiency show',
  w=3600, h=1900,
  fa='65, 66, 69',
  src=['Marks ch 23 — Tricarboxylic Acid Cycle', 'Robbins ch 9 — Environmental and nutritional diseases'],
  lanes=[('bvB', 'B vitamins', 'tca'), ('bvMin', 'Mineral', 'glycolysis')],
  nodes=[
    ('bv1', 'Riboflavin (B2)', 330, 1720, 'bvB', 'FAD · 2 C’s', ['b2def'], 'hub'),
    ('bv2', 'Niacin (B3) — pellagra', 760, 1720, 'bvB', '3 D’s', ['b3def']),
    ('bv3', 'Pantothenate (B5)', 1200, 1720, 'bvB', 'CoA', ['b5def']),
    ('bv4', 'Biotin (B7)', 1640, 1720, 'bvB', 'carboxylases · avidin', ['b7def']),
    ('bv5', 'Zinc deficiency', 2080, 1720, 'bvMin', 'acrodermatitis', ['zinc'])],
  panels=[
    (2500, PANY, 1000, 'Coenzyme for each (Marks)', [
      ('B2', 'FAD, FMN'), ('B3', 'NAD⁺, NADP⁺'), ('B5', 'CoA'), ('B7', 'carboxylases'), ('Zinc', 'zinc fingers, metalloenzymes')])],
  dyn=dyn)
