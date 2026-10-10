# Urea Cycle in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A hepatocyte with its mitochondrion: NH₃ + CO₂ → carbamoyl phosphate (CPS-1, needs N-acetylglutamate) → citrulline
# (OTC) → out to the cytosol → argininosuccinate (ASS) → arginine (ASL) → urea + ornithine (arginase), ornithine back in.
# Below, gut → liver → brain: ammonia that escapes reaches an astrocyte, which makes glutamine and swells. One `one`
# switch blocks a step (CPS-1/NAGS, OTC, ASS, ASL, arginase), shunts the liver (hepatic encephalopathy) or shows the
# look-alike (hereditary orotic aciduria). 5 readouts. Facts from the pinned cards (cps1, otc, ureaother, ammonia,
# oroticaciduria, hepenceph, osmolax); FA pages in `fa`. No new cards.
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


SW = 'def'
O = lambda *k: [f'{SW}:{x}' for x in k]
UC = ['cps', 'otc', 'ass', 'asl', 'arg']
PANY = 720
def X(cx, cy, s=22): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(lab, x, y, w=280):
    add(f'<rect x="{x - w // 2}" y="{y - 26}" width="{w}" height="52" rx="26" class="dyn-soft"/>')
    text(lab, x, y + 6, 'nf-l1', 'middle')

text('The urea cycle — nitrogen’s way out', 180, 150, 'dyn-big')
text('half in the mitochondrion, half in the cytosol of the hepatocyte', 180, 176, 'dyn-cap')
box(160, 200, 2340, 1160)
add('<rect x="200" y="240" width="900" height="880" rx="110" style="fill:var(--dk3);fill-opacity:.07;stroke:var(--dk3);stroke-width:6"/>')
text('Mitochondrion', 240, 290, 'nf-l1')
text('Cytosol', 2300, 250, 'nf-l1', 'end')

P = dict(nh3=(470, 360), cp=(470, 620), orn=(800, 950), cit=(1350, 450), asa=(1950, 450), arg=(2050, 760), urea=(2050, 1040), orn2=(1350, 950))
node('NH₃ + CO₂', *P['nh3']); node('Carbamoyl phosphate', *P['cp'], w=320); node('Ornithine', *P['orn'])
node('Citrulline', *P['cit']); node('Argininosuccinate', *P['asa'], w=320); node('Arginine', *P['arg']); node('Urea → kidney', *P['urea'], w=300)
node('Ornithine', *P['orn2'])
# UNVERIFIED: aspartate entering at ASS and fumarate leaving at ASL are standard teaching, not on the pinned cards
text('+ aspartate', 1650, 420, 'nf-l2', 'middle')
text('fumarate → TCA', 2300, 640, 'nf-l2', 'end')
EDGES = ['M470 386 V594', 'M600 640 C760 700 820 800 800 924', 'M630 610 C900 520 1100 450 1210 450', 'M1490 450 H1790',
         'M1980 476 L2040 734', 'M2050 786 V1014', 'M1900 1040 C1700 1040 1500 990 1480 950', 'M1210 950 H930']
for d in EDGES:
    add(f'<path d="{d}" class="dyn-line"/>')
# the cycle, run as one loop for the moving nitrogen
LOOP = 'M800 924 C820 800 760 700 600 640 C900 520 1100 450 1210 450 H1790 L2040 734 V1014 C1700 1040 1500 990 1480 950 H930 L800 924'

# blocks
XS = dict(cps=(470, 490), otc=(700, 760), ass=(1640, 450), asl=(2010, 600), arg=(2050, 900))
for k, (x, y) in XS.items():
    add(X(x, y), when=O(k))
# orotic acid spill (OTC)
node('Orotic acid', 1350, 300, 260)
add('<path d="M560 600 C800 380 1000 300 1220 300" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:10 6"/>', when=O('otc'))
text('carbamoyl phosphate spills into the pyrimidine pathway', 1350, 260, 'nf-l2', 'middle', when=O('otc'))
add(X(1500, 300, 16), when=O('oro'))
text('UMP synthase blocked: orotic acid → UMP fails', 1350, 260, 'nf-l1 dyn-tag', 'middle', when=O('oro'))
text('N-acetylglutamate switches CPS-1 on', 520, 500, 'nf-l2')

# ════════ gut → liver → brain ════════
text('Where the ammonia goes when it isn’t made into urea', 180, 1220, 'dyn-big')
box(160, 1250, 2340, 1560)
node('Gut bacteria — NH₃', 420, 1400, 300)
add('<rect x="900" y="1330" width="420" height="140" rx="60" style="fill:var(--dk5);fill-opacity:.18;stroke:var(--dk5);stroke-width:4"/>')
text('Liver — urea cycle', 1110, 1406, 'nf-l1', 'middle')
add('<path d="M570 1400 H900" class="dyn-line"/>')
add('<path d="M1320 1400 H1720" class="dyn-line"/>')
add('<ellipse cx="1950" cy="1400" rx="160" ry="90" class="dyn-cell"/>', unless=O(*UC, 'hep'))
add('<ellipse cx="1950" cy="1400" rx="210" ry="120" style="fill:var(--bad);fill-opacity:.14;stroke:var(--bad);stroke-width:4"/>', when=O(*UC, 'hep'))
text('Astrocyte', 1950, 1394, 'nf-l1', 'middle')
text('NH₃ + glutamate → glutamine', 1950, 1418, 'nf-l2', 'middle')
text('swells — cerebral edema', 1950, 1540, 'nf-l1 dyn-tag', 'middle', when=O(*UC, 'hep'))
add('<path d="M570 1360 C900 1280 1500 1280 1760 1350" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:10 6"/>', when=O('hep'))
text('portosystemic shunt — the liver is bypassed', 1160, 1300, 'nf-l1 dyn-tag', 'middle', when=O('hep'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=LOOP, len=3600, speed=170, r=7, base=dict(n=10), mods=[m(O(*UC), set=dict(n=2)), m(O('hep'), set=dict(n=3))]),
  dict(d='M470 240 V330', len=90, speed=50, r=7, base=dict(nh3=2), mods=[m(O(*UC), set=dict(nh3=5))]),
  dict(d='M570 1400 H900', len=330, speed=100, r=7, base=dict(nh3=3), mods=[m(O('hep'), set=dict(nh3=1))]),
  dict(d='M1320 1400 H1720', len=400, speed=100, r=7, base=dict(), mods=[m(O(*UC), set=dict(nh3=6))]),
  dict(d='M570 1360 C900 1280 1500 1280 1760 1350', len=1260, speed=140, r=7, base=dict(), when=O('hep'), mods=[m(O('hep'), set=dict(nh3=8))]),
  dict(d='M2050 1066 V1150', len=84, speed=60, r=7, base=dict(urea=2), mods=[m(O(*UC), set=dict(urea=0))]),
  dict(d='M560 600 C800 380 1000 300 1220 300', len=760, speed=110, r=7, base=dict(), when=O('otc'), mods=[m(O('otc'), set=dict(oro=5))]),
]
sites = [
  dict(x=470, y=490, n=[-1, 0], w=20, t='md', l='CPS-1', s='rate-limiting', c='cps1', ions=[], block=O('cps'), lx=430, ly=480, la='end'),
  dict(x=700, y=760, n=[-1, 0], w=20, t='md', l='OTC', s='X-linked', c='otc', ions=[], block=O('otc'), lx=660, ly=780, la='end'),
  dict(x=1640, y=450, n=[0, 1], w=20, t='md', l='ASS', s='', c='ureaother', ions=[], block=O('ass'), lx=1640, ly=520, la='middle'),
  dict(x=2010, y=600, n=[1, 0], w=20, t='md', l='ASL', s='', c='ureaother', ions=[], block=O('asl'), lx=2060, ly=600, la='start'),
  dict(x=2050, y=900, n=[1, 0], w=20, t='md', l='Arginase', s='', c='ureaother', ions=[], block=O('arg'), lx=2100, ly=905, la='start'),
]

readouts = [
  dict(l='Ammonia', mods=[dict(when=O(*UC, 'hep'), d=1), dict(when=O('oro'), d=0)]),
  dict(l='BUN', mods=[dict(when=O(*UC), d=-1)]),
  dict(l='Orotic acid', mods=[dict(when=O('otc', 'oro'), d=1)]),
  dict(l='Citrulline', mods=[dict(when=O('ass'), d=1)]),
  dict(l='MCV (megaloblastic)', mods=[dict(when=O('oro'), d=1), dict(when=O('otc'), d=0)]),
]

notes = {
  '': 'Amino-acid nitrogen leaves the body as urea. NH₃ and CO₂ become carbamoyl phosphate in the mitochondrion (CPS-1, which needs '
      'N-acetylglutamate); OTC adds ornithine to make citrulline; the cytosol finishes the cycle and arginase releases urea.',
  'def:cps': 'CPS-1 or N-acetylglutamate synthase deficiency: carbamoyl phosphate is never made — neonatal hyperammonemic coma like '
             'OTC deficiency, but orotic acid is normal or low.',
  'def:otc': 'OTC deficiency, the commonest urea cycle disorder (X-linked): carbamoyl phosphate spills into the pyrimidine pathway, so '
             'orotic acid rises with ammonia — but no megaloblastic anemia. Limit protein; benzoate or phenylbutyrate.',
  'def:ass': 'Argininosuccinate synthetase deficiency (citrullinemia): hyperammonemia with very high citrulline — each distal block '
             'piles up its own substrate.',
  'def:asl': 'Argininosuccinate lyase deficiency (argininosuccinic aciduria): argininosuccinate accumulates, ammonia rises. Arginine '
             'supplements help when the block comes after argininosuccinate synthesis.',
  'def:arg': 'Arginase deficiency: the last step fails, so arginine accumulates and urea isn’t released.',
  'def:hep': 'Hepatic encephalopathy: portosystemic shunting and failing hepatocytes let gut ammonia reach the brain — asterixis, '
             'confusion, coma. Lactulose traps NH₄⁺ in the colon; rifaximin kills ammonia-making bacteria.',
  'def:oro': 'Hereditary orotic aciduria (UMP synthase) — the look-alike: orotic acid rises but ammonia is normal, and the missing '
             'pyrimidines cause a megaloblastic anemia that B12 and folate can’t fix. Give uridine.',
}

dyn = dict(
  kinds=dict(n=['n', '--dk9'], nh3=['nh3', '--bad'], urea=['n', '--ok'], oro=['nh3', '--dk5']),
  groups=[['n', 'Nitrogen in the cycle'], ['nh3', 'Ammonia & orotic acid']],
  switches=[dict(id=SW, label='Block or bypass', type='one', options=[
    ['cps', 'CPS-1 / NAGS deficiency', 'cps1'], ['otc', 'OTC deficiency', 'otc'], ['ass', 'Citrullinemia (ASS)', 'ureaother'],
    ['asl', 'Argininosuccinic aciduria (ASL)', 'ureaother'], ['arg', 'Arginase deficiency', 'ureaother'],
    ['hep', 'Hepatic encephalopathy', 'hepenceph'], ['oro', 'Orotic aciduria (the look-alike)', 'oroticaciduria']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 80–81, 399, 426 · Marks ch 36')

MAP = dict(
  id='ureasim', title='Urea Cycle in Motion', topic='bio', after='nitrogen',
  sub='Nitrogen runs the urea cycle from carbamoyl phosphate to urea — block CPS-1, OTC, ASS, ASL or arginase, bypass the liver, '
      'or compare orotic aciduria, and watch ammonia back up, orotic acid spill and an astrocyte swell',
  w=3500, h=1820,
  fa='80–81, 399, 408, 426',
  src=[full('Marks', 36), full('Marks', 39), full('Marks', 44), full('Robbins', 18)],
  lanes=[('urCycle', 'Urea cycle', 'glycolysis'), ('urDef', 'Defects', 'tca'), ('urBrain', 'Ammonia & the brain', 'gluconeo')],
  nodes=[
    ('ur1', 'Hyperammonemia', 330, 1640, 'urBrain', 'astrocyte glutamine', ['ammonia'], 'hub'),
    ('ur2', 'OTC deficiency', 760, 1640, 'urDef', 'orotic acid ↑', ['otc']),
    ('ur3', 'CPS-1 / NAGS deficiency', 1180, 1640, 'urDef', 'orotic acid normal', ['cps1']),
    ('ur4', 'Distal blocks', 1600, 1640, 'urDef', 'citrulline · ASA · arginine', ['ureaother']),
    ('ur5', 'Orotic aciduria', 2000, 1640, 'urDef', 'no hyperammonemia', ['oroticaciduria']),
    ('ur6', 'Hepatic encephalopathy', 330, 1760, 'urBrain', 'lactulose · rifaximin', ['hepenceph', 'osmolax'])],
  panels=[
    (2420, PANY, 1000, 'Telling them apart (First Aid pp. 80–81, 426)', [
      ('OTC deficiency', 'ammonia ↑ · orotic acid ↑ · no anemia'),
      ('CPS-1 deficiency', 'ammonia ↑ · orotic acid normal'),
      ('Orotic aciduria', 'orotic acid ↑ · ammonia normal · megaloblastic'),
      ('Citrullinemia', 'ammonia ↑ · citrulline ↑↑')])],
  dyn=dyn)
