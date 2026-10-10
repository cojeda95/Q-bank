# Acute Kidney Injury in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Aorta → renal artery → afferent arteriole → glomerulus → efferent arteriole, and filtrate → tubule → loop → collecting duct
# → ureter → bladder → urethra past the prostate. A `one` switch breaks it before, inside or after the kidney: hypovolemia,
# NSAID (afferent), ACE inhibitor/ARB (efferent), ATN (oliguric and recovery phases), AIN, glomerulonephritis, BPH
# obstruction. Sodium reabsorption, casts and back-pressure move; a lab strip and 4 readouts show BUN:Cr, FENa, urine
# osmolality and creatinine with the card cut-offs. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
PRE, INTR = ('hypo', 'nsaid', 'acei'), ('atn', 'atnrec', 'ain', 'gn')
PANY = 1180
GX, GY = 900, 560

text('Acute kidney injury — before, inside or after the kidney', 180, 150, 'dyn-big')
text('blood in from the left, urine out to the bladder · sodium pulled back into the blood in teal', 180, 176, 'dyn-cap')

# ════════ plumbing ════════
add('<path d="M300 260 V1300" style="stroke:var(--nf-blood);stroke-width:60;opacity:.25"/>'); text('aorta', 300, 240, 'nf-l1', 'middle')
add(f'<path d="M330 {GY} H{GX - 70}" style="stroke:var(--nf-blood);stroke-width:26;opacity:.35"/>', unless=D('nsaid'))
add(f'<path d="M330 {GY} H{GX - 260}" style="stroke:var(--nf-blood);stroke-width:26;opacity:.35"/>', when=D('nsaid'))
add(f'<path d="M{GX - 260} {GY} H{GX - 70}" style="stroke:var(--bad);stroke-width:10"/>', when=D('nsaid'))
text('afferent', GX - 200, GY - 30, 'nf-l2', 'middle')
add(f'<path d="M{GX + 70} {GY} H1140" style="stroke:var(--nf-blood);stroke-width:18;opacity:.35"/>', unless=D('acei'))
add(f'<path d="M{GX + 70} {GY} H1140" style="stroke:var(--nf-blood);stroke-width:36;opacity:.35"/>', when=D('acei'))
text('efferent', GX + 140, GY - 30, 'nf-l2', 'middle')
add(f'<circle cx="{GX}" cy="{GY}" r="70" style="fill:var(--nf-blood);fill-opacity:.15;stroke:var(--dk1);stroke-width:4"/>', unless=D('gn'))
add(f'<circle cx="{GX}" cy="{GY}" r="78" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:5"/>', when=D('gn'))
text('glomerulus', GX, GY - 100, 'nf-l1', 'middle')
TUB = f'M{GX} {GY + 70} C{GX} {GY + 160} 1100 {GY + 160} 1100 {GY + 260} V1060 C1100 1120 1200 1120 1200 1060 V{GY + 240} H1420 V1120'
add(f'<path d="{TUB}" style="fill:none;stroke:var(--dk5);stroke-width:34;opacity:.25;stroke-linejoin:round"/>')
text('proximal tubule', 1000, GY + 190, 'nf-l2', 'end'); text('loop', 1150, 1150, 'nf-l2', 'middle'); text('collecting duct', 1450, 900, 'nf-l2')
add('<path d="M1420 1120 C1420 1200 1560 1240 1640 1260" style="fill:none;stroke:var(--dk5);stroke-width:20;opacity:.3"/>', unless=D('post'))
add('<path d="M1420 1120 C1420 1200 1560 1240 1640 1260" style="fill:none;stroke:var(--dk5);stroke-width:40;opacity:.4"/>', when=D('post'))
text('ureter', 1520, 1270, 'nf-l2', 'end')
add('<ellipse cx="1780" cy="1300" rx="140" ry="90" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:4"/>', unless=D('post'))
add('<ellipse cx="1780" cy="1260" rx="200" ry="150" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--bad);stroke-width:5"/>', when=D('post'))
text('bladder', 1780, 1130, 'nf-l1', 'middle', unless=D('post'))
add('<path d="M1780 1390 V1560" style="stroke:var(--dk5);stroke-width:14;opacity:.4"/>')
add('<ellipse cx="1780" cy="1450" rx="60" ry="40" style="fill:var(--dk9);fill-opacity:.25;stroke:var(--dk9);stroke-width:3"/>', unless=D('post'))
add('<ellipse cx="1780" cy="1450" rx="110" ry="60" style="fill:var(--dk9);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=D('post'))
text('prostate', 1910, 1460, 'nf-l2')
text('distended bladder · hydronephrosis', 1780, 1060, 'nf-l1 dyn-tag', 'middle', when=D('post'))
# interstitium / casts
for x, y in ((1040, 900), (1260, 820), (1300, 1000), (1000, 1020)):
    add(f'<circle cx="{x}" cy="{y}" r="16" style="fill:var(--dk4);fill-opacity:.7"/>', when=D('ain'))
for y in (900, 960, 1020):
    add(f'<rect x="1088" y="{y}" width="24" height="44" rx="10" style="fill:var(--dk6);opacity:.9"/>', when=D('atn'))
    add(f'<rect x="1408" y="{y}" width="24" height="44" rx="10" style="fill:var(--dk4);opacity:.9"/>', when=D('ain'))
    add(f'<rect x="1408" y="{y}" width="24" height="44" rx="10" style="fill:var(--nf-blood);opacity:.9"/>', when=D('gn'))
TAG = dict(hypo='hemorrhage, vomiting, diarrhea, burns, over-diuresis — or heart failure, cirrhosis, sepsis',
           nsaid='NSAID — afferent arteriole constricts', acei='ACE inhibitor / ARB — efferent arteriole relaxes',
           atn='ATN — dead tubular cells slough into muddy brown casts', atnrec='ATN recovery — polyuric, hypokalemia',
           ain='AIN — drug hypersensitivity: WBC casts, urine eosinophils', gn='glomerulonephritis — RBC casts, dysmorphic red cells',
           post='BPH obstruction — back-pressure opposes filtration')
for k, s in TAG.items(): text(s, 1100, 300, 'nf-l1 dyn-tag', 'middle', when=D(k))
LAB = dict(pre='BUN:Cr > 20 · FENa < 1% · urine Na⁺ < 20 · Uosm > 500 · bland or hyaline',
           intr='BUN:Cr < 15 · FENa > 2% · urine Na⁺ > 40 · Uosm < 350 · active sediment',
           post='hydronephrosis on ultrasound · indices vary with duration · type 4 RTA possible')
text(LAB['pre'], 1100, 1640, 'nf-l1', 'middle', when=D(*PRE))
text(LAB['intr'], 1100, 1640, 'nf-l1', 'middle', when=D('atn', 'ain', 'gn'))
text(LAB['post'], 1100, 1640, 'nf-l1', 'middle', when=D('post'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M300 300 V{GY} H{GX - 70}', len=860, speed=140, r=9, base=dict(bl=4),
       mods=[m(D('hypo', 'nsaid'), set=dict(bl=1), speed=0.4)]),
  dict(d=f'M{GX + 70} {GY} H1140', len=200, speed=140, r=8, base=dict(bl=2), mods=[m(D('hypo', 'nsaid'), set=dict(bl=1), speed=0.4)]),
  dict(d=TUB, len=1700, speed=150, r=8, base=dict(fil=5),
       mods=[m(D(*PRE), set=dict(fil=1), speed=0.4), m(D('atn', 'ain', 'gn'), set=dict(fil=2), speed=0.5),
             m(D('atnrec'), set=dict(fil=9), speed=1.4), m(D('post'), set=dict(fil=2), speed=0.1)]),
  dict(d='M1420 1120 C1420 1200 1560 1240 1640 1260', len=280, speed=120, r=8, base=dict(fil=2), unless=D('post')),
  dict(d='M1640 1260 C1560 1240 1420 1200 1420 1120 V900', len=500, speed=60, r=8, base=dict(bp=4), when=D('post')),
  dict(d=f'M1100 820 C1060 760 1100 700 1140 {GY + 20}', len=320, speed=100, r=8, base=dict(na=3),
       mods=[m(D(*PRE), set=dict(na=7)), m(D('atn', 'atnrec', 'ain', 'gn'), set=dict(na=0))]),
]
sites = [dict(x=600, y=GY + 60, n=[0, 1], w=10, t='rec', l='', aria='Pre-renal AKI', c='prerenal', ions=[]),
         dict(x=1060, y=1000, n=[-1, 0], w=10, t='rec', l='', aria='Acute tubular necrosis', c='atn', ions=[]),
         dict(x=1300, y=900, n=[1, 0], w=10, t='rec', l='', aria='Intrinsic AKI', c='intrarenal', ions=[]),
         dict(x=1480, y=1040, n=[1, 0], w=10, t='rec', l='', aria='Urinary casts', c='casts', ions=[]),
         dict(x=1600, y=1460, n=[-1, 0], w=10, t='rec', l='', aria='Post-renal AKI', c='postrenal', ions=[])]

readouts = [
  dict(l='Creatinine', mods=[dict(when=D(*PRE, 'atn', 'ain', 'gn', 'post'), d=1)]),
  dict(l='BUN:Cr ratio', mods=[dict(when=D(*PRE), d=1), dict(when=D('atn', 'ain', 'gn'), d=-1)]),
  dict(l='FENa', mods=[dict(when=D(*PRE), d=-1), dict(when=D('atn', 'ain', 'gn'), d=1)]),
  dict(l='Urine osmolality', mods=[dict(when=D(*PRE), d=1), dict(when=D('atn', 'ain', 'gn'), d=-1)]),
]

notes = {
  '': 'Normal: blood filters at the glomerulus, the tubule reclaims sodium and water, and urine drains to the bladder. Break it '
      'before the kidney (perfusion), inside it (tubules, interstitium, glomeruli) or after it (obstruction).',
  'dx:hypo': 'Pre-renal: less flow, lower GFR, but intact tubules starving for sodium — under aldosterone and ADH they reabsorb '
             'sodium and water avidly and drag urea along; creatinine is not reabsorbed, so BUN:Cr > 20, FENa < 1%, Uosm > 500.',
  'dx:nsaid': 'NSAIDs constrict the afferent arteriole (uncoupling autoregulation) — a pre-renal picture. Stop the drug.',
  'dx:acei': 'ACE inhibitors / ARBs relax the efferent arteriole — filtration pressure falls; pre-renal picture. Bilateral renal '
             'artery stenosis does the same.',
  'dx:atn': 'ATN: the commonest intrinsic AKI in hospital. PCT and medullary thick ascending limb die first (highest demand, '
            'lowest O₂); sloughed cells form muddy brown casts that block the lumen and back-leak filtrate. Oliguric '
            'maintenance phase 1–3 weeks: hyperkalemia, acidosis, uremia.',
  'dx:atnrec': 'ATN recovery phase: polyuric, with hypokalemia.',
  'dx:ain': 'AIN: drug hypersensitivity in the interstitium — WBC casts, urine eosinophils, sometimes fever and rash.',
  'dx:gn': 'Glomerulonephritis: RBC casts, dysmorphic red cells, hypertension.',
  'dx:post': 'Post-renal: obstruction (BPH most often in older men; bilateral stones, tumor) pushes pressure back into Bowman’s '
             'space and opposes filtration. Creatinine rises only if bilateral or in a solitary kidney. Relieve it — catheter, '
             'stent or nephrostomy — then watch the diuresis.',
}

dyn = dict(
  kinds=dict(bl=['mov', '--nf-blood'], fil=['mov', '--nf-h2o'], na=['mov', '--dk1'], bp=['mov', '--bad']),
  groups=[['mov', 'Blood · filtrate · Na⁺ reclaimed · back-pressure']],
  switches=[dict(id='dx', label='Injury', type='one', options=[
              ['hypo', 'Hypovolemia', 'prerenal'], ['nsaid', 'NSAID', 'prerenal'], ['acei', 'ACE inhibitor / ARB', 'prerenal'],
              ['atn', 'ATN (oliguric)', 'atn'], ['atnrec', 'ATN recovery', 'atn'], ['ain', 'AIN', 'intrarenal'],
              ['gn', 'Glomerulonephritis', 'intrarenal'], ['post', 'BPH obstruction', 'postrenal']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 20')

MAP = dict(
  id='akisim', title='Acute Kidney Injury in Motion', topic='renal', after='akickd',
  sub='Starve the kidney of blood, kill its tubules, inflame its interstitium or glomeruli, or block its outflow — and watch '
      'sodium handling, casts, BUN:Cr, FENa and urine osmolality move',
  w=3600, h=1900,
  fa='597, 601, 607, 612, 618, 620, 621',
  src=['Robbins ch 20 — The kidney', 'Guyton ch 32 — Diuretics and Kidney Diseases'],
  lanes=[('akPre', 'Pre-renal', 'glycolysis'), ('akIn', 'Intrinsic', 'tca'), ('akPost', 'Post-renal', 'gluconeo')],
  nodes=[
    ('ak1', 'Pre-renal AKI', 330, 1780, 'akPre', 'BUN:Cr > 20 · FENa < 1%', ['prerenal'], 'hub'),
    ('ak2', 'Intrinsic AKI', 760, 1780, 'akIn', 'FENa > 2%', ['intrarenal']),
    ('ak3', 'Acute tubular necrosis', 1200, 1780, 'akIn', 'muddy brown casts', ['atn']),
    ('ak4', 'Urinary casts', 1640, 1780, 'akIn', 'which compartment', ['casts']),
    ('ak5', 'Post-renal AKI', 2080, 1780, 'akPost', 'BPH · hydronephrosis', ['postrenal'])],
  panels=[
    (2500, PANY, 1000, 'Cut-offs (Robbins ch 20)', [
      ('Pre-renal', 'BUN:Cr > 20 · FENa < 1% · Uosm > 500'), ('Intrinsic', 'BUN:Cr < 15 · FENa > 2% · Uosm < 350'),
      ('Post-renal', 'indices vary · hydronephrosis'), ('Casts', 'muddy brown ATN · WBC AIN · RBC GN')])],
  dyn=dyn)
