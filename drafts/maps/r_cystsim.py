# Kidney Cysts in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A kidney in section — cortex, medullary pyramids, papillae, pelvis — beside an inset of one tubular cell whose primary
# cilium senses flow and sends a Ca²⁺ signal that restrains proliferation (the ciliopathy model). A `one` switch places
# each cystic disease where its card puts it and sizes the kidney: ADPKD (cysts in cortex and medulla, big), ARPKD
# (dilated collecting ducts, big, Potter), medullary cystic kidney disease (small, fibrotic, no visible cysts), nephronophthisis
# (corticomedullary cysts, small), medullary sponge kidney (dilated papillary ducts, stones), multicystic dysplasia, and simple
# vs complex cysts. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

import math
D = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
KX, KY = 900, 760
BIG, SMALL = D('adpkd', 'arpkd', 'mcdk'), D('adtkd', 'nphp')

text('Kidney cysts — where each disease puts them, and what the kidney does', 180, 150, 'dyn-big')
text('kidney in section, hilum to the right · inset: the primary cilium of one tubular cell', 180, 176, 'dyn-cap')

def bean(rx, ry, when=None, unless=None, col='--dk10'):
    add(f'<path d="M{KX + rx * .55} {KY - ry * .25} C{KX + rx * .9} {KY - ry} {KX - rx} {KY - ry * 1.05} {KX - rx} {KY} '
        f'C{KX - rx} {KY + ry * 1.05} {KX + rx * .9} {KY + ry} {KX + rx * .55} {KY + ry * .25} '
        f'C{KX + rx * .35} {KY + ry * .1} {KX + rx * .35} {KY - ry * .1} {KX + rx * .55} {KY - ry * .25} Z" '
        f'style="fill:var({col});fill-opacity:.1;stroke:var({col});stroke-width:5"/>', when=when, unless=unless)
bean(380, 480, unless=BIG + SMALL); bean(470, 580, when=BIG); bean(290, 370, when=SMALL)
bean(300, 390, unless=BIG + SMALL + D('mcdk'), col='--dk3')
text('cortex', KX - 360, KY - 420, 'nf-l2')
PYR = [(-60, 0), (-20, -260), (-25, 260), (40, -140), (40, 140)]
for i, ang in enumerate((-60, -25, 0, 25, 60)):
    a = math.radians(180 + ang)
    bx, by = KX + 280 * math.cos(a), KY + 360 * math.sin(a)
    tx_, ty_ = KX + 60 * math.cos(a), KY + 80 * math.sin(a)
    add(f'<path d="M{bx - 50 * math.sin(a):.0f} {by + 50 * math.cos(a):.0f} L{bx + 50 * math.sin(a):.0f} {by - 50 * math.cos(a):.0f} L{tx_:.0f} {ty_:.0f} Z" '
        f'style="fill:var(--dk5);fill-opacity:.15;stroke:var(--dk5);stroke-width:2"/>', unless=D('mcdk'))
    for j in range(3):
        f = .35 + .2 * j
        add(f'<ellipse cx="{bx + (tx_ - bx) * f:.0f}" cy="{by + (ty_ - by) * f:.0f}" rx="12" ry="26" '
            f'transform="rotate({ang} {bx + (tx_ - bx) * f:.0f} {by + (ty_ - by) * f:.0f})" style="fill:var(--nf-h2o);fill-opacity:.7;stroke:var(--dk9);stroke-width:2"/>', when=D('arpkd'))
    add(f'<circle cx="{tx_ + 20 * math.cos(a):.0f}" cy="{ty_ + 20 * math.sin(a):.0f}" r="16" style="fill:var(--nf-h2o);fill-opacity:.7;stroke:var(--dk9);stroke-width:2"/>', when=D('msk'))
    add(f'<circle cx="{tx_ + 4 * math.cos(a):.0f}" cy="{ty_ + 4 * math.sin(a):.0f}" r="8" style="fill:var(--ink)"/>', when=D('msk'))
    cm = (KX + 230 * math.cos(a), KY + 290 * math.sin(a))
    add(f'<circle cx="{cm[0]:.0f}" cy="{cm[1]:.0f}" r="12" style="fill:var(--nf-h2o);fill-opacity:.7;stroke:var(--dk9);stroke-width:2"/>', when=D('nphp'))
text('pyramids · papillae', KX - 40, KY + 30, 'nf-l2', 'end')
add(f'<path d="M{KX + 200} {KY} H{KX + 420}" style="stroke:var(--dk5);stroke-width:30;opacity:.3"/>'); text('ureter', KX + 430, KY + 10, 'nf-l2')
for x, y, r in ((-300, -200, 60), (-150, -380, 50), (-330, 120, 70), (-120, 330, 55), (60, -440, 45), (60, 420, 50), (-60, -120, 40), (-200, 40, 45), (-60, 160, 38)):
    add(f'<circle cx="{KX + x}" cy="{KY + y}" r="{r}" style="fill:var(--nf-h2o);fill-opacity:.55;stroke:var(--dk9);stroke-width:3"/>', when=D('adpkd'))
for x, y, r in ((-250, -250, 110), (-300, 150, 130), (-50, -420, 90), (-40, 380, 100), (-100, -60, 80)):
    add(f'<circle cx="{KX + x}" cy="{KY + y}" r="{r}" style="fill:var(--nf-h2o);fill-opacity:.5;stroke:var(--dk9);stroke-width:3"/>', when=D('mcdk'))
add(f'<circle cx="{KX - 330}" cy="{KY - 120}" r="70" style="fill:var(--nf-h2o);fill-opacity:.6;stroke:var(--dk9);stroke-width:3"/>', when=D('simple', 'complex'))
add(f'<path d="M{KX - 380} {KY - 150} L{KX - 280} {KY - 90} M{KX - 330} {KY - 190} V{KY - 50}" style="stroke:var(--bad);stroke-width:6"/>', when=D('complex'))
for i in range(8):
    add(f'<path d="M{KX - 240 + i * 50} {KY - 300} l30 600" style="stroke:var(--ink-3);stroke-width:3;opacity:.5"/>', when=D('adtkd'))
TAG = dict(adpkd='ADPKD — cysts through cortex and medulla, both kidneys enlarge · PKD1 (chr 16), PKD2 (chr 4)',
           arpkd='ARPKD — dilated collecting ducts, big echogenic kidneys · infancy, Potter, hepatic fibrosis',
           adtkd='medullary cystic kidney disease — tubulointerstitial fibrosis, small kidneys, cysts usually not seen',
           nphp='nephronophthisis — small cysts at the corticomedullary junction, small kidneys · polyuria, salt wasting',
           msk='medullary sponge kidney — dilated papillary collecting ducts · hematuria, UTI, recurrent stones; function normal',
           mcdk='multicystic dysplasia — ureteric bud fails to induce the mesenchyme · unilateral: other kidney fine',
           simple='simple cyst — anechoic, incidental', complex='complex cyst — septations, enhancement, solid parts: can be RCC')
for k, s in TAG.items(): text(s, KX + 100, 1460, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ cilium inset ════════
IX, IY = 1680, 560
add(f'<rect x="{IX}" y="{IY}" width="600" height="420" rx="24" class="dyn-soft"/>'); text('tubular cell — primary cilium', IX + 20, IY - 16, 'nf-l1')
add(f'<path d="M{IX + 40} {IY + 120} H{IX + 560}" style="stroke:var(--nf-h2o);stroke-width:26;opacity:.3"/>'); text('urine flow', IX + 40, IY + 90, 'nf-l2')
add(f'<rect x="{IX + 200}" y="{IY + 200}" width="200" height="160" rx="20" style="fill:var(--dk2);fill-opacity:.15;stroke:var(--dk2);stroke-width:3"/>')
add(f'<path d="M{IX + 300} {IY + 200} C{IX + 300} {IY + 160} {IX + 320} {IY + 130} {IX + 350} {IY + 110}" style="fill:none;stroke:var(--dk4);stroke-width:8"/>',
    unless=D('adpkd', 'arpkd', 'nphp'))
add(f'<path d="M{IX + 300} {IY + 200} V{IY + 150}" style="fill:none;stroke:var(--bad);stroke-width:8;stroke-dasharray:6 6"/>', when=D('adpkd', 'arpkd', 'nphp'))
text('polycystins · fibrocystin · nephrocystins sit on the cilium', IX + 300, IY + 400, 'nf-l2', 'middle')
text('signal lost → cells proliferate → cyst', IX + 300, IY + 440, 'nf-l1 dyn-tag', 'middle', when=D('adpkd', 'arpkd', 'nphp'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{IX + 40} {IY + 120} H{IX + 560}', len=520, speed=110, r=8, base=dict(urine=4)),
  dict(d=f'M{IX + 330} {IY + 120} C{IX + 320} {IY + 160} {IX + 310} {IY + 200} {IX + 300} {IY + 260}', len=150, speed=60, r=7, base=dict(ca=3),
       unless=D('adpkd', 'arpkd', 'nphp')),
  dict(d=f'M{IX + 300} {IY + 280} C{IX + 380} {IY + 300} {IX + 440} {IY + 320} {IX + 500} {IY + 330}', len=220, speed=60, r=9, base=dict(prolif=3),
       when=D('adpkd', 'arpkd', 'nphp')),
  dict(d=f'M{KX + 120} {KY} H{KX + 420}', len=300, speed=100, r=8, base=dict(urine=3), mods=[m(D('adtkd', 'nphp'), set=dict(urine=6), speed=1.5),
       m(D('mcdk'), set=dict(urine=0))]),
]
sites = [dict(x=KX - 470, y=KY - 120, n=[-1, 0], w=10, t='rec', l='', aria='ADPKD', c='adpkd', ions=[]),
         dict(x=KX - 470, y=KY + 140, n=[-1, 0], w=10, t='rec', l='', aria='ARPKD', c='arpkd', ions=[]),
         dict(x=KX + 60, y=KY - 520, n=[0, -1], w=10, t='rec', l='', aria='Medullary cystic kidney disease', c='adtkd', ions=[]),
         dict(x=KX + 60, y=KY + 520, n=[0, 1], w=10, t='rec', l='', aria='Nephronophthisis', c='nephronoph', ions=[]),
         dict(x=KX + 160, y=KY - 120, n=[1, -1], w=10, t='rec', l='', aria='Medullary sponge kidney', c='medsponge', ions=[]),
         dict(x=KX + 160, y=KY + 140, n=[1, 1], w=10, t='rec', l='', aria='Multicystic dysplasia', c='mcdk', ions=[]),
         dict(x=KX - 470, y=KY - 380, n=[-1, -1], w=10, t='rec', l='', aria='Simple vs complex cysts', c='renalcysts', ions=[]),
         dict(x=IX + 600, y=IY + 280, n=[1, 0], w=10, t='rec', l='', aria='Ciliopathy model', c='ciliopathy', ions=[])]

readouts = [
  dict(l='Kidney size', mods=[dict(when=BIG, d=1), dict(when=SMALL, d=-1)]),
  dict(l='Urine concentrating ability', mods=[dict(when=D('adtkd', 'nphp'), d=-1)]),
  dict(l='Stones · UTI', mods=[dict(when=D('msk'), d=1)]),
  dict(l='Hypertension', mods=[dict(when=D('adpkd', 'arpkd'), d=1)]),
]

notes = {
  '': 'Each tubular cell has one nonmotile primary cilium that senses flow; the polycystins, fibrocystin and nephrocystins sit '
      'on it and restrain proliferation. Pick a disease to see where its cysts form.',
  'dx:adpkd': 'ADPKD: PKD1 (chr 16) or PKD2 (chr 4); each cyst is clonal (second-hit somatic mutation). Bilateral big kidneys — '
              'flank pain, hematuria, hypertension (ischemia → renin), UTIs; failure in about half. Berry aneurysms, MVP, '
              'liver cysts, diverticulosis. ACEi/ARB.',
  'dx:arpkd': 'ARPKD: PKHD1 (fibrocystin) — collecting ducts dilate; enlarged echogenic kidneys prenatally, oligohydramnios → '
              'Potter sequence; congenital hepatic fibrosis → portal hypertension.',
  'dx:adtkd': 'Medullary cystic kidney disease: tubulointerstitial fibrosis — cannot concentrate urine; small kidneys; cysts '
              'usually not seen. Transplant.',
  'dx:nphp': 'Nephronophthisis: commonest genetic cause of ESKD in children and young adults; cysts at the corticomedullary '
             'junction (may be too small to see); small kidneys; polyuria, polydipsia, salt wasting, growth retardation, anemia.',
  'dx:msk': 'Medullary sponge kidney: dilated papillary collecting ducts in adults — hematuria, UTIs, recurrent stones; function '
            'usually normal; benign.',
  'dx:mcdk': 'Multicystic dysplasia: the ureteric bud fails to induce the metanephric mesenchyme — irregular cysts, cartilage, '
             'immature ducts; often with ureteropelvic obstruction. Unilateral: excellent prognosis; bilateral: Potter.',
  'dx:simple': 'Simple cyst: ultrafiltrate, anechoic, very common, incidental — no treatment.',
  'dx:complex': 'Complex cyst: septations, enhancement or solid components — may be renal cell carcinoma; surveil or resect.',
}

dyn = dict(
  kinds=dict(urine=['mov', '--nf-h2o'], ca=['mov', '--dk4'], prolif=['mov', '--bad']), groups=[['mov', 'Urine · Ca²⁺ signal · proliferation']],
  switches=[dict(id='dx', label='Disease', type='one', options=[
              ['adpkd', 'ADPKD', 'adpkd'], ['arpkd', 'ARPKD', 'arpkd'], ['adtkd', 'Medullary cystic kidney', 'adtkd'],
              ['nphp', 'Nephronophthisis', 'nephronoph'], ['msk', 'Medullary sponge kidney', 'medsponge'],
              ['mcdk', 'Multicystic dysplasia', 'mcdk'], ['simple', 'Simple cyst', 'renalcysts'], ['complex', 'Complex cyst', 'renalcysts']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 20')

MAP = dict(
  id='cystsim', title='Kidney Cysts in Motion', topic='renal', after='renvasc',
  sub='Place each cystic kidney disease where it lives — ADPKD, ARPKD, medullary cystic, nephronophthisis, sponge kidney, dysplasia, '
      'simple and complex cysts — and see why a broken primary cilium makes cysts',
  w=3600, h=2000,
  fa='58, 596, 597, 622',
  src=['Robbins ch 20 — The kidney', 'Langman ch 16 — Urogenital System'],
  lanes=[('kcGen', 'Genetic', 'tca'), ('kcOther', 'Acquired & developmental', 'glycolysis')],
  nodes=[
    ('kc1', 'Ciliopathy model', 330, 1720, 'kcGen', 'primary cilium', ['ciliopathy'], 'hub'),
    ('kc2', 'ADPKD', 760, 1720, 'kcGen', 'PKD1/PKD2 · big', ['adpkd']),
    ('kc3', 'ARPKD', 1200, 1720, 'kcGen', 'PKHD1 · Potter', ['arpkd']),
    ('kc4', 'Nephronophthisis', 1640, 1720, 'kcGen', 'corticomedullary', ['nephronoph']),
    ('kc5', 'Medullary cystic kidney', 2080, 1720, 'kcGen', 'small · fibrosis', ['adtkd']),
    ('kc6', 'Medullary sponge kidney', 2520, 1720, 'kcOther', 'stones · benign', ['medsponge']),
    ('kc7', 'Multicystic dysplasia', 2960, 1720, 'kcOther', 'ureteric bud', ['mcdk']),
    ('kc8', 'Simple vs complex cysts', 330, 1850, 'kcOther', 'RCC risk', ['renalcysts'])],
  panels=[
    (2500, PANY, 1000, 'Kidney size (Robbins ch 20)', [
      ('Big', 'ADPKD, ARPKD, multicystic dysplasia'), ('Small', 'medullary cystic, nephronophthisis'),
      ('Normal function', 'medullary sponge kidney')])],
  dyn=dyn)
