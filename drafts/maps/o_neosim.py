# Neoplasia in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A drawn epithelium on its basement membrane above a vessel. A `steps` switch (auto) walks normal → dysplasia →
# carcinoma in situ → invasive carcinoma → metastasis: nuclei enlarge, the dysplasia climbs to full thickness, the
# basement membrane is breached and tumor cells ride the vessel away. A `one` switch shows the genetics: an
# oncogene (one hit) vs a tumor suppressor (two hits, Knudson). 4 readouts. Facts from the pinned cards (neoprog,
# celladapt, hallmarks, oncogenes, tsgenes, metsites, gradestage, tumornomen, kras, p53, rb); their FA pages are in
# `fa`. No new cards.
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


ST = 'stage'
S = lambda *k: [f'{ST}:{x}' for x in k]
G = lambda *k: [f'gene:{x}' for x in k]
PANY = 720

# ════════ the epithelium ════════
box(160, 130, 2340, 1180)
text('An epithelium on its way to cancer', 190, 170, 'dyn-big')
text('the basement membrane is the line between in situ and invasive', 190, 196, 'dyn-cap')
COLS = [300 + i * 140 for i in range(14)]
BM = 720
GAP = (1150, 1330)
for x in COLS:
    for (y0, row) in ((BM - 110, 'basal'), (BM - 220, 'top')):
        add(f'<rect x="{x - 60}" y="{y0}" width="120" height="104" rx="14" class="dyn-cell"/>')
        big = S('dys', 'cis', 'inv', 'met') if row == 'basal' else S('cis', 'inv', 'met')
        cx, cy = x, y0 + 52
        add(f'<circle cx="{cx}" cy="{cy}" r="16" style="fill:var(--dk9);opacity:.75"/>', unless=big)
        rx, ry = (34, 28) if (x // 140) % 2 else (30, 34)
        add(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="fill:var(--dk9);opacity:.9"/>', when=big)
text('surface', 250, BM - 168, 'nf-l2', 'end')
text('basal', 250, BM - 58, 'nf-l2', 'end')
# basement membrane — whole, or breached
add(f'<path d="M260 {BM + 8} H2240" style="stroke:var(--dk11);stroke-width:9"/>', unless=S('inv', 'met'))
add(f'<path d="M260 {BM + 8} H{GAP[0]} M{GAP[1]} {BM + 8} H2240" style="stroke:var(--dk11);stroke-width:9"/>', when=S('inv', 'met'))
text('basement membrane', 2240, BM + 40, 'nf-l1', 'end')
# invading nest under the membrane
for (x, y) in ((1200, 790), (1290, 800), (1240, 860)):
    add(f'<rect x="{x - 40}" y="{y - 26}" width="80" height="52" rx="12" style="fill:var(--bad);fill-opacity:.2;stroke:var(--bad);stroke-width:3"/>', when=S('inv', 'met'))
text('metalloproteinases breach the membrane · E-cadherin lost', 1380, 830, 'nf-l1 dyn-tag', when=S('inv', 'met'))
# the stage caption
CAP = dict(nl='Normal: small, uniform nuclei on an intact basement membrane',
           dys='Dysplasia: pleomorphism, lost orientation, ↑ N:C ratio — often reversible',
           cis='Carcinoma in situ: severe dysplasia through the full thickness — membrane intact',
           inv='Invasive carcinoma: the basement membrane is breached',
           met='Metastasis: tumor cells enter vessels and lodge in distant organs')
for k, t in CAP.items():
    text(t, 190, 380, 'nf-l1', when=S(k))

# the vessel below
shapes.append(dict(vessel='M260 1030 H2240', w=60, color='--dk1'))
text('blood vessel or lymphatic', 260, 980, 'nf-l2')
text('→ liver · lung · bone · brain', 2240, 1110, 'nf-l1', 'end', when=S('met'))
text('carcinomas mostly by lymph, sarcomas by blood', 2240, 1136, 'nf-l2', 'end', when=S('met'))

# ════════ the genes ════════
box(160, 1220, 2340, 1560)
text('The genes behind it', 190, 1260, 'dyn-big')
for i, (x, lab) in enumerate(((420, 'allele 1'), (520, 'allele 2'))):
    add(f'<rect x="{x - 18}" y="1300" width="36" height="200" rx="18" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:3"/>')
    text(lab, x, 1530, 'nf-l2', 'middle')
add('<rect x="402" y="1380" width="36" height="26" style="fill:var(--bad)"/>', when=G('onc', 'tsg'))
add('<rect x="502" y="1380" width="36" height="26" style="fill:var(--bad)"/>', when=G('tsg'))
text('pick oncogene or tumor suppressor', 640, 1400, 'nf-l1', unless=['gene:*'])
text('Oncogene — gain of function: one hit is enough', 640, 1360, 'nf-l1', when=G('onc'))
text('RAS (KRAS) · MYC · HER2 · BCR-ABL · BRAF · RET · JAK2', 640, 1390, 'nf-l2', when=G('onc'))
text('hallmark: self-sufficiency in growth signals', 640, 1420, 'nf-l2', when=G('onc'))
text('Tumor suppressor — loss of function: both alleles must go', 640, 1360, 'nf-l1', when=G('tsg'))
text('TP53 · RB1 · APC · BRCA1/2 · PTEN · VHL · NF1', 640, 1390, 'nf-l2', when=G('tsg'))
text('Knudson two hits — inherit one bad copy and one more hit is enough', 640, 1420, 'nf-l2', when=G('tsg'))

# ════════ motion ════════
flows = [
  dict(d=f'M1240 {BM - 60} V1010', len=1010 - BM + 60, speed=60, r=8, base=dict(tum=2), when=S('inv', 'met')),
  dict(d='M1260 1030 H2230', len=970, speed=150, r=9, base=dict(tum=5), when=S('met')),
  dict(d='M270 1030 H1220', len=950, speed=150, r=6, base=dict(rbc=6)),
]
sites = [
  dict(x=1240, y=BM + 8, n=[0, 1], w=10, t='md', l='', aria='Basement membrane', c='neoprog', ions=[]),
  dict(x=470, y=1300, n=[0, -1], w=10, t='rec', l='', aria='Oncogenes and tumor suppressors', c='tsgenes', ions=[]),
]

# ════════ readouts ════════
readouts = [
  dict(l='Nuclear : cytoplasm ratio', mods=[dict(when=S('dys', 'cis', 'inv', 'met'), d=1), dict(when=S('nl'), d=0)]),
  dict(l='Basement membrane intact', mods=[dict(when=S('nl', 'dys', 'cis'), d=0), dict(when=S('inv', 'met'), d=-1)]),
  dict(l='E-cadherin', mods=[dict(when=S('inv', 'met'), d=-1), dict(when=S('nl'), d=0)]),
  dict(l='Metalloproteinase activity', mods=[dict(when=S('inv', 'met'), d=1), dict(when=S('nl'), d=0)]),
]

# ════════ notes ════════
notes = {
  '': 'A neoplasm is an uncontrolled, often monoclonal proliferation. Malignancy advances in steps, and the basement membrane is '
      'the line between in situ and invasive disease.',
  'stage:nl': 'Normal epithelium: small, uniform nuclei in an orderly layer on an intact basement membrane.',
  'stage:dys': 'Dysplasia: pleomorphism, loss of orientation and a high nuclear-to-cytoplasmic ratio — disordered precancerous '
               'growth that is often reversible.',
  'stage:cis': 'Carcinoma in situ: irreversible severe dysplasia through the full thickness of the epithelium, with the basement '
               'membrane still intact.',
  'stage:inv': 'Invasive carcinoma: metalloproteinases (collagenases, hydrolases) breach the basement membrane and E-cadherin loss '
               'loosens cell contacts; cells crawl through the matrix on laminin and fibronectin to reach vessels.',
  'stage:met': 'Metastasis: tumor cells enter lymphatics or blood — carcinomas mostly by lymph, sarcomas by blood — and lodge in '
               'liver, lung, bone or brain, where metastases outnumber primary tumors.',
  'gene:onc': 'An oncogene is a proto-oncogene with a gain-of-function mutation — one damaged allele is enough (RAS, MYC, HER2, '
              'BCR-ABL, BRAF, RET).',
  'gene:tsg': 'A tumor suppressor must lose both alleles — Knudson’s two hits. Inheriting one bad copy (Li-Fraumeni TP53, familial '
              'RB1, FAP APC) leaves only one more hit to go.',
}

dyn = dict(
  kinds=dict(tum=['cells', '--bad'], rbc=['cells', '--dk1']), groups=[['cells', 'Cells']],
  switches=[dict(id=ST, label='Stage', type='steps', auto=4, options=[
    ['nl', 'Normal'], ['dys', 'Dysplasia'], ['cis', 'Carcinoma in situ'], ['inv', 'Invasive carcinoma'], ['met', 'Metastasis']]),
    dict(id='gene', label='Genetics', type='one', options=[['onc', 'Oncogene — one hit', 'oncogenes'], ['tsg', 'Tumor suppressor — two hits', 'tsgenes']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 202, 215–220 · Robbins ch 7')

MAP = dict(
  id='neosim', title='Neoplasia in Motion', topic='path', after='neoplasia',
  sub='An epithelium steps from normal to dysplasia, carcinoma in situ, invasion and metastasis — watch the nuclei grow, the '
      'basement membrane give way and tumor cells ride a vessel away; then compare one-hit oncogenes with two-hit tumor suppressors',
  w=3500, h=1880,
  fa='202, 215–220',
  src=[full('Robbins', 7), full('Robbins', 2), full('Marks', 17)],
  lanes=[('neStep', 'Progression', 'glycolysis'), ('neGene', 'Genes', 'tca'), ('neSpread', 'Spread & staging', 'gluconeo')],
  nodes=[
    ('ne1', 'Dysplasia to metastasis', 330, 1650, 'neStep', 'the basement membrane', ['neoprog'], 'hub'),
    ('ne2', 'Cellular adaptations', 760, 1650, 'neStep', 'metaplasia → dysplasia', ['celladapt']),
    ('ne3', 'Hallmarks of cancer', 1180, 1650, 'neStep', 'what tumors gain', ['hallmarks']),
    ('ne4', 'Oncogenes', 1580, 1650, 'neGene', 'one hit', ['oncogenes', 'kras']),
    ('ne5', 'Tumor suppressors', 1980, 1650, 'neGene', 'two hits', ['tsgenes', 'p53', 'rb']),
    ('ne6', 'Where metastases go', 330, 1780, 'neSpread', 'lymph vs blood', ['metsites']),
    ('ne7', 'Grade vs stage', 760, 1780, 'neSpread', 'TNM', ['gradestage']),
    ('ne8', 'Benign vs malignant', 1180, 1780, 'neSpread', 'naming', ['tumornomen'])],
  panels=[
    (2420, PANY, 1000, 'Grade vs stage (First Aid p. 216)', [
      ('Grade', 'how the cells look — differentiation, mitoses'),
      ('Stage', 'how far it spread — TNM'),
      ('TNM weight', 'M > N > T'),
      ('Better predictor', 'stage')])],
  dyn=dyn)
