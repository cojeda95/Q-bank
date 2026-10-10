# Collagen Assembly in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# An assembly line built only from the steps the cards name: α-chains with the Gly-X-Y repeat → prolyl and lysyl hydroxylase
# (ascorbate, Fe²⁺) → three chains pack into the triple helix (procollagen) → N- and C-propeptides cut off by specific
# peptidases → lysyl oxidase (copper) cross-links the molecules into a fibril, with chains moving down the line. A `one`
# switch breaks a step: scurvy, osteogenesis imperfecta, kyphoscoliotic EDS, arthrochalasia and dermatosparaxis EDS, Menkes,
# vascular and classic EDS; a second shows the four collagen types and where each lives. 4 readouts. Facts from the pinned
# cards; FA pages in `fa`. Where the steps happen (inside or outside the cell) is not drawn — no card states it. No new cards.
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
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
STEPS = [(420, 'α-chains', 'Gly-X-Y repeat'), (860, 'Hydroxylation', 'prolyl · lysyl hydroxylase'), (1300, 'Triple helix', 'procollagen'),
         (1740, 'Propeptides cut', 'N- and C-peptidases'), (2180, 'Cross-linked fibril', 'lysyl oxidase')]
Y = 480
BLOCK = dict(scurvy=1, kypho=1, oi=2, arthro=3, derma=3, menkes=4)
text('Collagen — one assembly line, many ways to break it', 180, 150, 'dyn-big')
text('each step is one a card names; switch on a disease to see where the line stops', 180, 176, 'dyn-cap')
for i, (x, lab, sub) in enumerate(STEPS):
    add(f'<rect x="{x - 170}" y="{Y - 60}" width="340" height="120" rx="30" class="dyn-cell"/>')
    text(lab, x, Y - 8, 'nf-l1', 'middle'); text(sub, x, Y + 20, 'nf-l2', 'middle')
    if i: add(f'<path d="M{STEPS[i - 1][0] + 170} {Y} H{x - 170}" class="dyn-line"/>')
text('needs vitamin C (ascorbate) + Fe²⁺', 860, Y + 100, 'nf-l2', 'middle')
text('needs copper', 2180, Y + 100, 'nf-l2', 'middle')
for k, i in BLOCK.items():
    x = STEPS[i][0]
    add(X(x - 150, Y - 80), when=D(k))
    add(f'<rect x="{x - 170}" y="{Y - 60}" width="340" height="120" rx="30" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D(k))
# schematic molecules
def helix(x, y, ok=True, when=None):
    c = '--dk2' if ok else '--bad'
    add(''.join(f'<path d="M{x - 120} {y + o} q30 -20 60 0 t60 0 t60 0 t60 0" style="fill:none;stroke:var({c});stroke-width:5"/>' for o in (-14, 0, 14)), when=when)
helix(1300, 760)
text('three α-chains wound together', 1300, 820, 'nf-l2', 'middle')
add('<path d="M1180 760 h-50 M1420 760 h50" style="stroke:var(--dk5);stroke-width:12"/>', unless=D('arthro', 'derma'))
add('<path d="M1180 760 h-50 M1420 760 h50" style="stroke:var(--bad);stroke-width:12"/>', when=D('arthro', 'derma'))
text('propeptides left on', 1300, 700, 'nf-l1 dyn-tag', 'middle', when=D('arthro', 'derma'))
for i in range(4):
    add(f'<rect x="{1960 + (i % 2) * 120}" y="{720 + i * 22}" width="220" height="14" rx="6" style="fill:var(--dk2);opacity:.6"/>')
for x in (2040, 2120, 2200):
    add(f'<path d="M{x} 720 V800" style="stroke:var(--dk4);stroke-width:4"/>', unless=D('menkes', 'kypho'))
text('cross-links', 2180, 840, 'nf-l2', 'middle')
TAG = dict(scurvy='no hydroxyproline — the helix can’t hydrogen-bond, collagen degrades', oi='glycine substitution — chains can’t pack; one bad chain poisons the trimer',
           kypho='PLOD1: no hydroxylysine → no cross-links', arthro='COL1A1/2 chains resist cleavage — dominant',
           derma='procollagen N-peptidase (ADAMTS2) missing — recessive', menkes='ATP7A: copper can’t reach lysyl oxidase',
           vasc='type III collagen (COL3A1) — arteries, bowel, gravid uterus rupture', classic='type V collagen (COL5A1/2) — fragile, scarring skin')
for k, t in TAG.items(): text(t, 1300, 300, 'nf-l1 dyn-tag', 'middle', when=D(k))
# collagen types panel
TY = dict(t1=('Type I — 90%', 'bone, skin, tendon, dentin, fascia, cornea, late wound repair · OI'),
          t2=('Type II', 'cartilage, vitreous, nucleus pulposus'),
          t3=('Type III — reticulin', 'skin, vessels, uterus, fetal tissue, granulation tissue · vascular EDS'),
          t4=('Type IV', 'basement membrane · Alport, Goodpasture'))
add('<rect x="300" y="980" width="2000" height="300" rx="30" class="dyn-soft"/>')
text('Collagen types', 330, 1020, 'nf-l1')
for i, (k, (a, b)) in enumerate(TY.items()):
    y = 1070 + i * 50
    text(a, 340, y, 'nf-l1'); text(b, 760, y, 'nf-l2')
    add(f'<rect x="320" y="{y - 30}" width="1960" height="44" rx="12" style="fill:var(--accent);fill-opacity:.12"/>',
        when=[f'ty:{k}'] + (D('oi') if k == 't1' else []) + (D('vasc') if k == 't3' else []))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = []
for i in range(4):
    x0, x1 = STEPS[i][0] + 170, STEPS[i + 1][0] - 170
    flows.append(dict(d=f'M{x0} {Y} H{x1}', len=x1 - x0, speed=60, r=9, base=dict(ch=3), mods=[m(D(*[k for k, b in BLOCK.items() if b <= i]), set=dict(ch=0))]))
flows.append(dict(d=f'M{STEPS[4][0] - 120} 760 H{STEPS[4][0] + 140}', len=260, speed=40, r=8, base=dict(ch=2), mods=[m(D(*BLOCK), set=dict(ch=0))]))
sites = [dict(x=860, y=Y + 60, n=[0, 1], w=10, t='rec', l='', aria='Scurvy', c='scurvy', ions=[]),
         dict(x=1300, y=Y + 60, n=[0, 1], w=10, t='rec', l='', aria='Osteogenesis imperfecta', c='oi', ions=[]),
         dict(x=1740, y=Y + 60, n=[0, 1], w=10, t='rec', l='', aria='Procollagen cleavage', c='edsproc', ions=[]),
         dict(x=2180, y=Y + 60, n=[0, 1], w=10, t='rec', l='', aria='Menkes', c='menkes', ions=[]),
         dict(x=330, y=1240, n=[0, 1], w=10, t='rec', l='', aria='Collagen types', c='collagentypes', ions=[])]

readouts = [
  dict(l='Stable collagen made', mods=[dict(when=D('scurvy', 'oi', 'kypho', 'arthro', 'derma', 'menkes'), d=-1)]),
  dict(l='Bleeding gums · bruising', mods=[dict(when=D('scurvy'), d=1)]),
  dict(l='Fractures', mods=[dict(when=D('oi'), d=1)]),
  dict(l='Vessel or organ rupture', mods=[dict(when=D('vasc'), d=1)]),
]

notes = {
  '': 'Collagen chains carry a Gly-X-Y repeat; prolyl and lysyl hydroxylase (vitamin C, Fe²⁺) add hydroxyl groups; three chains pack into '
      'a triple helix (procollagen); specific peptidases cut off the N- and C-terminal propeptides; lysyl oxidase (copper) cross-links the '
      'molecules. EDS subtypes, OI, scurvy and Menkes each break a different step.',
  'dx:scurvy': 'Scurvy: ascorbate keeps the hydroxylases’ iron reduced; without hydroxyproline the helix can’t hydrogen-bond and degrades — '
               'swollen gums, bruising, perifollicular hemorrhage, corkscrew hairs, poor wound healing; normal platelets and coags.',
  'dx:oi': 'Osteogenesis imperfecta: a glycine substitution in COL1A1/COL1A2 stops the chains packing — dominant negative. Fractures with '
           'minimal trauma, blue sclerae, hearing loss, dentinogenesis imperfecta. Bisphosphonates.',
  'dx:kypho': 'Kyphoscoliotic EDS: PLOD1 lysyl hydroxylase deficiency — no hydroxylysine, no cross-links; scoliosis, ocular fragility. Recessive.',
  'dx:arthro': 'Arthrochalasia EDS: COL1A1/2 chains resist propeptide cleavage — dominant.',
  'dx:derma': 'Dermatosparaxis EDS: procollagen N-peptidase (ADAMTS2) deficiency — recessive enzyme defect.',
  'dx:menkes': 'Menkes disease: ATP7A copper transport fails, so lysyl oxidase can’t cross-link — kinky hair, hypotonia, developmental '
               'delay, cerebral aneurysms; ↓ serum copper.',
  'dx:vasc': 'Vascular EDS: abnormal type III collagen (COL3A1) — spontaneous rupture of arteries, colon, gravid uterus; skin usually not '
             'hyperextensible.',
  'dx:classic': 'Classic EDS: type V collagen (COL5A1/2) — marked skin fragility and scarring. Hypermobile EDS is the commonest, gene unknown.',
}

dyn = dict(
  kinds=dict(ch=['chain', '--dk2']), groups=[['chain', 'Collagen chains']],
  switches=[dict(id='dx', label='What breaks', type='one', options=[
              ['scurvy', 'Scurvy', 'scurvy'], ['oi', 'Osteogenesis imperfecta', 'oi'], ['kypho', 'Kyphoscoliotic EDS', 'edskypho'],
              ['arthro', 'Arthrochalasia EDS', 'edsproc'], ['derma', 'Dermatosparaxis EDS', 'edsproc'], ['menkes', 'Menkes disease', 'menkes'],
              ['vasc', 'Vascular EDS', 'edsvasc'], ['classic', 'Classic EDS', 'edsclassic']]),
            dict(id='ty', label='Collagen type', type='one', options=[
              ['t1', 'Type I', 'collagentypes'], ['t2', 'Type II', 'collagentypes'], ['t3', 'Type III', 'collagentypes'], ['t4', 'Type IV', 'collagentypes']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 48–49, 67, 212 · Robbins ch 5 · Pawlina ch 6')

MAP = dict(
  id='colsim', title='Collagen Assembly in Motion', topic='bio', after='collagen',
  sub='Run collagen down its assembly line — Gly-X-Y chains, hydroxylation, triple helix, propeptide cleavage, cross-linking — and break '
      'each step: scurvy, osteogenesis imperfecta, the EDS subtypes and Menkes; then see where types I–IV live',
  w=3600, h=1900,
  fa='48, 49, 67, 212',
  src=['Pawlina ch 6 — Connective Tissue', 'Robbins ch 5 — Genetic disorders'],
  lanes=[('coStep', 'Synthesis defects', 'glycolysis'), ('coEds', 'Ehlers-Danlos', 'tca'), ('coType', 'Types', 'gluconeo')],
  nodes=[
    ('co1', 'Collagen types', 330, 1660, 'coType', 'I bone · II cartilage · III vessels · IV BM', ['collagentypes'], 'hub'),
    ('co2', 'Scurvy', 760, 1660, 'coStep', 'vitamin C', ['scurvy']),
    ('co3', 'Osteogenesis imperfecta', 1200, 1660, 'coStep', 'glycine · blue sclerae', ['oi']),
    ('co4', 'Menkes disease', 1640, 1660, 'coStep', 'copper', ['menkes']),
    ('co5', 'Ehlers-Danlos', 2080, 1660, 'coEds', '13 types, one theme', ['eds', 'edsclass']),
    ('co6', 'Kyphoscoliotic EDS', 330, 1790, 'coEds', 'lysyl hydroxylase', ['edskypho']),
    ('co7', 'Procollagen cleavage EDS', 760, 1790, 'coEds', 'arthrochalasia · dermatosparaxis', ['edsproc']),
    ('co8', 'Vascular · classic EDS', 1200, 1790, 'coEds', 'type III · type V', ['edsvasc', 'edsclassic']),
    ('co9', 'Hypermobile EDS', 1640, 1790, 'coEds', 'commonest, gene unknown', ['edshyper'])],
  panels=[
    (2500, PANY, 1000, 'Step → disease', [
      ('Hydroxylation (vit C, Fe²⁺)', 'scurvy · kyphoscoliotic EDS'), ('Triple helix (glycine)', 'osteogenesis imperfecta'),
      ('Propeptide cleavage', 'arthrochalasia, dermatosparaxis EDS'), ('Cross-linking (Cu)', 'Menkes'), ('Which collagen', 'vascular (III), classic (V)')])],
  dyn=dyn)
