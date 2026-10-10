# UTI & Incontinence in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Urethra → bladder (detrusor, outlet) → ureters → kidneys, with urine flowing down and, when infected, bacteria climbing up.
# A `one` switch shows acute cystitis, acute pyelonephritis, chronic pyelonephritis (reflux, scars), malakoplakia and the
# three incontinences (stress, urgency, overflow) — where the bacteria stop, what lights up, what leaks. 5 readouts. Facts
# from the pinned cards; FA pages in `fa`. No new cards.
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

O = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
INF = O('cyst', 'pyelo', 'chron', 'malako')
UP = O('pyelo', 'chron')

text('Urinary tract — infection climbs up, urine comes down', 180, 150, 'dyn-big')
text('red dots = bacteria ascending · blue = urine', 180, 176, 'dyn-cap')
# kidneys
for cx in (700, 1700):
    add(f'<ellipse cx="{cx}" cy="420" rx="170" ry="220" style="fill:var(--dk1);fill-opacity:.12;stroke:var(--dk1);stroke-width:4"/>')
    add(f'<ellipse cx="{cx}" cy="420" rx="170" ry="220" style="fill:var(--bad);fill-opacity:.15;stroke:var(--bad);stroke-width:6"/>', when=UP)
text('kidney', 700, 670, 'nf-l1', 'middle'); text('kidney', 1700, 670, 'nf-l1', 'middle')
for (x, y) in ((600, 300), (790, 540)):
    add(f'<path d="M{x - 30} {y} l20 -20 l20 20 l20 -20" style="fill:none;stroke:var(--ink-2);stroke-width:6"/>', when=O('chron'))
text('coarse polar scars, blunted calyces — thyroidization', 1200, 260, 'nf-l1 dyn-tag', 'middle', when=O('chron'))
text('neutrophils in the interstitium — WBC casts', 1200, 260, 'nf-l1 dyn-tag', 'middle', when=O('pyelo'))
# ureters and bladder
add('<path d="M780 600 C900 800 1050 860 1120 960 M1620 600 C1500 800 1350 860 1280 960" style="fill:none;stroke:var(--dk3);stroke-width:18;opacity:.5"/>')
text('ureter', 880, 790, 'nf-l2', 'end')
add('<path d="M980 960 C960 1200 1440 1200 1420 960 Z" style="fill:var(--nf-h2o);fill-opacity:.15;stroke:var(--dk7);stroke-width:8"/>')
add('<path d="M980 960 C960 1200 1440 1200 1420 960 Z" style="fill:var(--nf-h2o);fill-opacity:.35"/>', when=O('over'))
text('bladder · detrusor', 1200, 1050, 'nf-l1', 'middle')
add('<path d="M980 960 C960 1200 1440 1200 1420 960 Z" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:6"/>', when=O('cyst'))
for (x, y) in ((1100, 1110), (1300, 1100)):
    add(f'<circle cx="{x}" cy="{y}" r="34" style="fill:var(--dk10);fill-opacity:.6"/>', when=O('malako'))
text('soft yellow plaques: foamy macrophages, Michaelis-Gutmann bodies', 1200, 920, 'nf-l1 dyn-tag', 'middle', when=O('malako'))
add('<rect x="1170" y="1170" width="60" height="40" rx="8" style="fill:var(--dk5)"/>'); text('outlet · sphincter', 1260, 1196, 'nf-l2')
add('<path d="M1200 1210 V1400" style="stroke:var(--dk3);stroke-width:16;opacity:.5"/>'); text('urethra', 1230, 1320, 'nf-l2')
text('perineal bacteria', 1200, 1460, 'nf-l1', 'middle', when=INF)
text('reflux (children) or an obstructing stone keeps infection coming back', 1200, 880, 'nf-l1 dyn-tag', 'middle', when=O('chron'))
add(X(1200, 1190), when=O('stress'))
text('weak outlet — leaks when abdominal pressure rises', 1500, 1190, 'nf-l1 dyn-tag', when=O('stress'))
text('detrusor contracts on its own — sudden urge', 1500, 1190, 'nf-l1 dyn-tag', when=O('urge'))
text('bladder never empties — dribbles, large postvoid residual', 1500, 1190, 'nf-l1 dyn-tag', when=O('over'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
UR = ['M780 600 C900 800 1050 860 1120 960', 'M1620 600 C1500 800 1350 860 1280 960']
flows = [dict(d=d, len=480, speed=110, r=8, base=dict(u=3)) for d in UR]
flows += [
  dict(d='M1200 1210 V1400', len=190, speed=70, r=8, base=dict(u=2), mods=[m(O('over'), speed=0.3, set=dict(u=1)), m(O('stress', 'urge'), set=dict(u=5))]),
  dict(d='M1200 1400 V1150 C1150 1100 1100 1080 1080 1060', len=360, speed=90, r=8, base=dict(bac=4), when=INF),
  dict(d='M1120 960 C1050 860 900 800 780 600', len=480, speed=110, r=8, base=dict(bac=4), when=UP),
  dict(d='M1060 1100 C1150 1040 1250 1040 1340 1100', len=320, speed=180, r=8, base=dict(det=3), when=O('urge')),
]
sites = [dict(x=1200, y=1150, n=[0, -1], w=10, t='rec', l='', aria='Cystitis', c='cystitis', ions=[]),
         dict(x=870, y=420, n=[1, 0], w=10, t='rec', l='', aria='Pyelonephritis', c='pyelo', ions=[]),
         dict(x=1420, y=1100, n=[1, 0], w=10, t='rec', l='', aria='Incontinence', c='incontinence', ions=[])]

readouts = [
  dict(l='Dysuria · frequency', mods=[dict(when=O('cyst'), d=1)]),
  dict(l='Fever · flank pain', mods=[dict(when=O('pyelo'), d=1), dict(when=O('cyst'), d=0)]),
  dict(l='WBC casts', mods=[dict(when=O('pyelo'), d=1), dict(when=O('cyst'), d=0)]),
  dict(l='Postvoid residual', mods=[dict(when=O('over'), d=1), dict(when=O('stress', 'urge'), d=0)]),
  dict(l='Renal scarring', mods=[dict(when=O('chron'), d=1)]),
]

notes = {
  '': 'Urine flows from the kidneys down the ureters to the bladder and out the urethra. Infection usually goes the other way: perineal '
      'bacteria climb the short female urethra; anything that leaves urine sitting (catheter, obstruction, neurogenic bladder) helps them.',
  'dx:cyst': 'Acute cystitis: suprapubic pain, dysuria, frequency, urgency — no fever or flank pain. E coli most; S saprophyticus in '
             'sexually active young women; Proteus (ammonia smell). Leukocyte esterase ⊕, nitrites ⊕. Nitrofurantoin or TMP-SMX.',
  'dx:pyelo': 'Acute pyelonephritis: usually ascending E coli; neutrophils fill the cortical interstitium — fever, chills, flank pain, CVA '
              'tenderness; WBC casts prove the kidney. Pregnancy raises the risk. Papillary necrosis, perinephric abscess, urosepsis.',
  'dx:chron': 'Chronic pyelonephritis: recurrent infection on vesicoureteral reflux (children) or obstructing stones (adults) — coarse '
              'asymmetric polar scars, blunted calyces, thyroidization.',
  'dx:malako': 'Malakoplakia: long-standing E coli infection with defective macrophage phagolysosomes — soft yellow plaques of foamy '
               'macrophages with Michaelis-Gutmann bodies; transplant recipients.',
  'dx:stress': 'Stress incontinence: an incompetent outlet leaks with cough, sneeze, lifting — pregnancy, vaginal delivery, obesity, '
               'prostate surgery. Kegel exercises, weight loss, pessary.',
  'dx:urge': 'Urgency incontinence: the detrusor contracts on its own — UTI, stones, tumor, radiation. Bladder training; oxybutynin, mirabegron.',
  'dx:over': 'Overflow incontinence: the bladder never empties (weak detrusor or blocked outlet) — dribbling, large postvoid residual; '
             'BPH, diabetes, spinal cord injury.',
}

dyn = dict(
  kinds=dict(u=['urine', '--nf-h2o'], bac=['bug', '--bad'], det=['urine', '--dk7']), groups=[['urine', 'Urine'], ['bug', 'Bacteria']],
  switches=[dict(id='dx', label='Problem', type='one', options=[
    ['cyst', 'Acute cystitis', 'cystitis'], ['pyelo', 'Acute pyelonephritis', 'pyelo'], ['chron', 'Chronic pyelonephritis', 'chronicpyelo'],
    ['malako', 'Malakoplakia', 'malako'], ['stress', 'Stress incontinence', 'incontinence'], ['urge', 'Urgency incontinence', 'incontinence'],
    ['over', 'Overflow incontinence', 'incontinence']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 618–619 · Robbins ch 20–21')

MAP = dict(
  id='utisim', title='UTI & Incontinence in Motion', topic='renal', after='akickd',
  sub='Watch bacteria climb from urethra to bladder to kidney — cystitis, acute and chronic pyelonephritis, malakoplakia — and see the '
      'bladder leak three ways: stress, urgency and overflow incontinence',
  w=3600, h=1900,
  fa='618, 619',
  src=['Robbins ch 21 — The lower urinary tract and male genital system', 'Robbins ch 20 — The kidney',
       'Katzung ch 51 — Clinical Use of Antimicrobial Agents', 'Katzung ch 43 — Beta-Lactam & Other Cell Wall- & Membrane-Active Antibiotics',
       'Moore ch 6 — Pelvis and Perineum', 'Katzung ch 8 — Cholinoceptor-Blocking Drugs'],
  lanes=[('utInf', 'Infection', 'glycolysis'), ('utBl', 'Bladder control', 'tca')],
  nodes=[
    ('ut1', 'Acute cystitis', 330, 1660, 'utInf', 'E coli · nitrites', ['cystitis'], 'hub'),
    ('ut2', 'Acute pyelonephritis', 760, 1660, 'utInf', 'WBC casts', ['pyelo']),
    ('ut3', 'Chronic pyelonephritis', 1200, 1660, 'utInf', 'thyroidization', ['chronicpyelo']),
    ('ut4', 'Malakoplakia', 1640, 1660, 'utInf', 'Michaelis-Gutmann', ['malako']),
    ('ut5', 'Urinary incontinence', 330, 1790, 'utBl', 'stress · urge · overflow', ['incontinence'])],
  panels=[
    (2500, PANY, 1000, 'Upper or lower tract? (First Aid p. 618)', [
      ('Cystitis', 'dysuria, suprapubic pain, no fever'), ('Pyelonephritis', 'fever, flank pain, WBC casts'),
      ('Sterile pyuria', 'urethritis — gonorrhea, chlamydia'), ('Overflow', 'large postvoid residual')])],
  dyn=dyn)
