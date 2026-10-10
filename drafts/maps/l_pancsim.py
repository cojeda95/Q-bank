# Pancreatitis in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A drawn duodenum, ampulla, pancreatic duct and acini, with the common bile duct and gallbladder above. Normally
# zymogens (trypsinogen) travel down the duct and are switched on only in the duodenum by enterokinase; with a
# cause of acute pancreatitis the enzymes are activated inside the gland (red particles), fat necrosis forms
# calcium soaps, and a gallstone at the ampulla stops bile and juice. Chronic pancreatitis draws fibrosis and
# calcifications with little juice. One `one` switch (cause) and 6 readouts. Facts from the pinned cards
# (acutepanc, chronicpanc, pancsec, gallstones, hypertg, pancins); their FA pages are in `fa`. No new cards.
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


SW = 'cause'
PANY = 660
O = lambda *k: [f'{SW}:{x}' for x in k]
ACUTE = O('stone', 'etoh', 'tg', 'ca')

# ════════ the drawing ════════
text('The pancreas, its duct and the duodenum', 180, 150, 'dyn-big')
text('trypsinogen should stay inactive until enterokinase in the duodenum switches it on', 180, 176, 'dyn-cap')
# gallbladder + common bile duct
add('<ellipse cx="930" cy="300" rx="120" ry="64" class="dyn-cell"/>')
text('Gallbladder', 1070, 300, 'nf-l1')
shapes.append(dict(tube='M840 340 C760 430 660 540 598 742', w=20, color='--dk5'))
text('Common bile duct', 760, 520, 'nf-l2')
# duodenum
shapes.append(dict(tube='M520 230 V1330', w=110, color='--dk3'))
text('Duodenum', 520, 210, 'nf-l1', 'middle')
# gland outline
add('<path d="M640 600 C760 540 1000 560 1240 590 C1500 620 1800 600 2080 640 C2230 660 2250 860 2090 900 '
    'C1800 960 1500 930 1240 950 C1000 970 760 980 640 900 C590 860 590 640 640 600 Z" class="dyn-soft"/>')
text('Pancreas', 2120, 560, 'dyn-big', 'end')
# main duct
shapes.append(dict(tube='M2020 760 H600', w=18, color='--dk9'))
text('Main pancreatic duct', 1420, 728, 'nf-l2', 'middle')
# acini + ductules
ACINI = [(880, 660), (1180, 660), (1480, 670), (1780, 670), (880, 860), (1180, 860), (1480, 860), (1780, 860)]
for x, y in ACINI:
    add(f'<path d="M{x} {y + (30 if y < 760 else -30)} V760" class="dyn-line"/>')
    add(f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" class="dyn-cell"/>', unless=O('chr'))
    add(f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" class="dyn-cell dyn-dim"/>', when=O('chr'))
text('Acinar cells — make the enzymes', 880, 610, 'nf-l2', 'middle')
# ampulla label
text('Ampulla', 640, 800, 'nf-l1')

# a gallstone at the ampulla
add('<ellipse cx="588" cy="752" rx="34" ry="24" style="fill:var(--ink-2);stroke:var(--surface);stroke-width:3"/>', when=O('stone'))
text('Gallstone blocks the ampulla', 420, 690, 'nf-l1 dyn-tag', 'end', when=O('stone'))
text('bile and juice back up', 420, 714, 'nf-l2', 'end', when=O('stone'))

# enzymes switched on inside the gland (acute causes)
for x, y in ACINI[:4] + ACINI[4:]:
    add(f'<ellipse cx="{x}" cy="{y}" rx="70" ry="42" style="fill:var(--bad);fill-opacity:.18;stroke:var(--bad);stroke-width:3"/>', when=ACUTE)
text('trypsin switched on inside the gland — autodigestion', 1430, 1000, 'nf-l1 dyn-tag', 'middle', when=ACUTE)

# fat necrosis: calcium soaps (acute)
SOAPS = [(760, 1060), (1060, 1080), (1360, 1070), (1660, 1080), (1960, 1050), (2160, 760)]
for x, y in SOAPS:
    add(f'<circle cx="{x}" cy="{y}" r="22" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3;stroke-dasharray:4 3"/>', when=ACUTE)
text('fat necrosis: fatty acids bind Ca²⁺ — calcium soaps', 1360, 1130, 'nf-l2', 'middle', when=ACUTE)

# chronic: fibrosis + calcifications + beaded duct
for x, y in [(980, 760), (1330, 760), (1630, 760), (1030, 900), (1630, 640), (1330, 900), (1930, 820)]:
    add(f'<path d="M{x - 9} {y + 7} L{x} {y - 10} L{x + 10} {y + 5} Z" style="fill:var(--ink-2)"/>', when=O('chr'))
add('<path d="M640 600 C760 540 1000 560 1240 590 C1500 620 1800 600 2080 640 C2230 660 2250 860 2090 900 '
    'C1800 960 1500 930 1240 950 C1000 970 760 980 640 900 C590 860 590 640 640 600 Z" '
    'style="fill:var(--ink-3);fill-opacity:.12;stroke:none"/>', when=O('chr'))
text('fibrosis and calcifications replace acini and islets', 1430, 1000, 'nf-l1 dyn-tag', 'middle', when=O('chr'))

# the blood: triglycerides or calcium high
shapes.append(dict(vessel='M680 1230 H2240', w=50, color='--dk1'))
text('Blood', 2240, 1196, 'nf-l1', 'end')
text('triglycerides over 1000 mg/dL', 1460, 1300, 'nf-l1 dyn-tag', 'middle', when=O('tg'))
text('hypercalcemia', 1460, 1300, 'nf-l1 dyn-tag', 'middle', when=O('ca'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  # zymogens down the main duct
  dict(d='M2000 760 H610', len=1390, speed=150, r=7, base=dict(zym=8), mods=[m(O('stone'), set=dict(zym=3), speed=0.4), m(O('chr'), set=dict(zym=2))]),
  # activated trypsin in the duodenum (after enterokinase)
  dict(d='M520 790 V1300', len=510, speed=140, r=7, base=dict(tryp=4), mods=[m(O('stone'), set=dict(tryp=0)), m(O('chr'), set=dict(tryp=1))]),
  # bile down the CBD
  dict(d='M840 340 C760 430 660 540 598 742', len=460, speed=120, r=6, base=dict(bile=4), mods=[m(O('stone'), set=dict(bile=0))]),
  # chyme down the duodenum from above
  dict(d='M520 250 V720', len=470, speed=110, r=6, base=dict(chyme=3)),
  # lipid / calcium in the blood
  dict(d='M690 1230 H2230', len=1540, speed=120, r=7, base=dict(), mods=[m(O('tg'), set=dict(tg=10)), m(O('ca'), set=dict(ca=10))]),
]
# trypsin loose inside the gland: a small loop around each acinus
for x, y in ACINI:
    flows.append(dict(d=f'M{x - 60} {y} A60 34 0 1 1 {x + 60} {y} A60 34 0 1 1 {x - 60} {y}', len=300, speed=70, r=6,
                      base=dict(), when=ACUTE, mods=[m(ACUTE, set=dict(tryp=2))]))

sites = [
  dict(x=465, y=860, n=[-1, 0], w=110, t='md', l='Enterokinase', s='trypsinogen → trypsin', c='pancsec', lx=300, ly=860, la='end'),
  dict(x=1780, y=670, n=[0, -1], w=84, t='rec', l='', aria='Acinar cell', c='acutepanc', ions=[]),
]

# ════════ readouts ════════
readouts = [
  dict(l='Lipase', mods=[dict(when=ACUTE, d=1)]),
  dict(l='Serum Ca²⁺', mods=[dict(when=O('stone', 'etoh', 'tg'), d=-1), dict(when=O('ca'), d=1)]),
  dict(l='ALP · direct bilirubin', mods=[dict(when=O('stone'), d=1)]),
  dict(l='Triglycerides', mods=[dict(when=O('tg'), d=1)]),
  dict(l='Fecal elastase', mods=[dict(when=O('chr'), d=-1)]),
  dict(l='Glucose', mods=[dict(when=O('chr'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Normal: acinar cells send zymogens (trypsinogen and the rest) down the duct; enterokinase on the duodenal brush border '
      'makes trypsin, which then activates the others. Pancreatitis is that activation happening inside the gland.',
  'cause:stone': 'A gallstone at the ampulla is one of the two commonest causes. Bile and pancreatic juice back up, enzymes activate '
                 'inside the gland, and the stone in the duct raises ALP and direct bilirubin. Treat with cholecystectomy.',
  'cause:etoh': 'Alcohol is the other common cause of acute pancreatitis — epigastric pain to the back, nausea and vomiting, with '
                'lipase over 3× normal. Repeated attacks lead to chronic pancreatitis.',
  'cause:tg': 'Triglycerides over 1000 mg/dL can cause acute pancreatitis — the H of I GET SMASHED (hypercalcemia or '
              'hypertriglyceridemia).',
  'cause:ca': 'Hypercalcemia is on the I GET SMASHED list of causes, beside hypertriglyceridemia.',
  'cause:chr': 'Chronic pancreatitis: fibrosis and calcifications replace acini and islets. Steatorrhea and diabetes follow once '
               'function falls below about 10%; lipase may be normal, fecal elastase is low.',
}

dyn = dict(
  kinds=dict(zym=['enz', '--dk9'], tryp=['enz', '--bad'], bile=['bile', '--dk5'], chyme=['bile', '--dk4'],
             tg=['blood', '--dk2'], ca=['blood', '--nf-ca']),
  groups=[['enz', 'Enzymes'], ['bile', 'Bile & chyme'], ['blood', 'Blood']],
  switches=[dict(id=SW, label='Cause', type='one', options=[
    ['stone', 'Gallstone', 'gallstones'], ['etoh', 'Alcohol', 'acutepanc'], ['tg', 'Hypertriglyceridemia', 'hypertg'],
    ['ca', 'Hypercalcemia', 'acutepanc'], ['chr', 'Chronic pancreatitis', 'chronicpanc']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 92, 380, 388, 403–404 · Robbins ch 19')

MAP = dict(
  id='pancsim', title='Pancreatitis in Motion', topic='gi', after='liver',
  sub='Zymogens travel down the duct and switch on only in the duodenum — pick a cause and watch them activate inside the '
      'gland, calcium soaps form and a stone stop the flow; chronic disease leaves fibrosis and calcifications. Tap a structure for its card',
  w=3500, h=1720,
  fa='92, 205, 380, 388, 403–404',
  src=[full('Robbins', 19), full('Robbins', 18), full('Costanzo', 8), full('Guyton', 65)],
  lanes=[('pnPhys', 'Normal secretion', 'glycolysis'), ('pnAcute', 'Acute', 'tca'), ('pnChronic', 'Chronic', 'gluconeo')],
  nodes=[
    ('pn1', 'Pancreatic secretions', 330, 1460, 'pnPhys', 'zymogens · bicarbonate', ['pancsec', 'cck'], 'hub'),
    ('pn2', 'Acute pancreatitis', 780, 1460, 'pnAcute', 'I GET SMASHED', ['acutepanc']),
    ('pn3', 'Gallstones', 1200, 1460, 'pnAcute', 'the ampulla', ['gallstones']),
    ('pn4', 'Hypertriglyceridemia', 1620, 1460, 'pnAcute', 'over 1000 mg/dL', ['hypertg']),
    ('pn5', 'Chronic pancreatitis', 330, 1590, 'pnChronic', 'calcifications', ['chronicpanc']),
    ('pn6', 'Pancreatic insufficiency', 780, 1590, 'pnChronic', 'steatorrhea', ['pancins']),
    ('pn7', 'Pancreatic cancer', 1200, 1590, 'pnChronic', 'a late risk', ['pancca'])],
  panels=[
    (2420, PANY, 1000, 'Causes — I GET SMASHED (First Aid p. 404)', [
      ('I · G · E', 'idiopathic · gallstones · ethanol'),
      ('T · S · M', 'trauma · steroids · mumps'),
      ('A · S · H', 'autoimmune · scorpion sting · hypercalcemia or TG > 1000'),
      ('E · D', 'ERCP · drugs (sulfa, NRTIs, protease inhibitors)')]),
    (2420, PANY + 200, 1000, 'Complications (First Aid p. 404)', [
      ('Pseudocyst', 'granulation tissue, no epithelium'),
      ('Systemic', 'ARDS · shock · renal failure'),
      ('Local', 'necrosis · abscess · hemorrhage'),
      ('Hypocalcemia', 'calcium soaps')])],
  dyn=dyn)
