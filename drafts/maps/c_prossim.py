# The Prostate in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A section of the prostate — transition zone around the urethra, peripheral zone at the back by the rectum, central zone,
# ejaculatory ducts from the seminal vesicles — with urine running down the urethra, DHT made in the stroma, and semen
# assembling from vas deferens, seminal vesicles and prostate. A `one` switch shows BPH (transition zone squeezes the urethra;
# toggles for an α₁-blocker and finasteride), HGPIN, prostate cancer (peripheral, palpable; Batson plexus → spine), and a
# `gl` switch draws Gleason patterns for the score. An inset compares gland lining: two layers (benign, PIN) vs no basal
# cells (cancer). Zone shapes schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
CX, CY = 900, 760

text('The prostate — zones, growth, cancer and semen', 180, 150, 'dyn-big')
text('section, front at the top, rectum below · zone shapes schematic', 180, 176, 'dyn-cap')

# ════════ prostate ════════
add(f'<ellipse cx="{CX}" cy="{CY}" rx="340" ry="280" style="fill:var(--dk9);fill-opacity:.08;stroke:var(--dk9);stroke-width:5"/>')
add(f'<path d="M{CX - 320} {CY + 60} C{CX - 300} {CY + 260} {CX + 300} {CY + 260} {CX + 320} {CY + 60} C{CX + 200} {CY + 160} {CX - 200} {CY + 160} {CX - 320} {CY + 60} Z" '
    'style="fill:var(--dk4);fill-opacity:.15;stroke:var(--dk4);stroke-width:3"/>')
text('peripheral zone (posterior)', CX, CY + 230, 'nf-l1', 'middle')
add(f'<ellipse cx="{CX}" cy="{CY - 40}" rx="130" ry="100" style="fill:var(--dk5);fill-opacity:.15;stroke:var(--dk5);stroke-width:3"/>', unless=D('bph'))
add(f'<ellipse cx="{CX}" cy="{CY - 40}" rx="220" ry="170" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--bad);stroke-width:5"/>', when=D('bph'))
text('transition zone', CX, CY - 160, 'nf-l1', 'middle', unless=D('bph'))
add(f'<path d="M{CX - 60} {CY + 40} C{CX - 30} {CY + 120} {CX + 30} {CY + 120} {CX + 60} {CY + 40}" style="fill:none;stroke:var(--dk7);stroke-width:4;stroke-dasharray:8 6"/>')
text('central zone', CX + 80, CY + 100, 'nf-l2')
add(f'<circle cx="{CX}" cy="{CY - 40}" r="26" style="fill:var(--surface);stroke:var(--nf-h2o);stroke-width:6"/>', unless=D('bph'))
add(f'<ellipse cx="{CX}" cy="{CY - 40}" rx="10" ry="26" style="fill:var(--surface);stroke:var(--bad);stroke-width:6"/>', when=D('bph'))
text('urethra', CX + 40, CY - 30, 'nf-l2')
add(f'<rect x="{CX - 380}" y="{CY + 320}" width="760" height="70" rx="30" style="fill:var(--dk6);fill-opacity:.15;stroke:var(--dk6);stroke-width:3"/>'); text('rectum', CX, CY + 365, 'nf-l1', 'middle')
add(f'<circle cx="{CX + 160}" cy="{CY + 170}" r="50" style="fill:var(--bad);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=D('ca'))
add(f'<circle cx="{CX + 160}" cy="{CY + 170}" r="30" style="fill:var(--dk7);fill-opacity:.45"/>', when=D('pin'))
text('hard nodule felt on rectal exam', CX + 160, CY + 450, 'nf-l1 dyn-tag', 'middle', when=D('ca'))
add(f'<path d="M{CX + 160} {CY + 230} V{CY + 310}" style="stroke:var(--accent);stroke-width:8"/>', when=D('ca')); text('finger', CX + 180, CY + 300, 'nf-l2', when=D('ca'))
# seminal vesicles + ejaculatory ducts
for s in (-1, 1):
    add(f'<ellipse cx="{CX + s * 420}" cy="{CY - 280}" rx="110" ry="50" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>')
    add(f'<path d="M{CX + s * 330} {CY - 260} C{CX + s * 200} {CY - 200} {CX + s * 60} {CY - 100} {CX + s * 10} {CY - 40}" style="fill:none;stroke:var(--dk10);stroke-width:6;opacity:.6"/>')
text('seminal vesicle', CX - 420, CY - 350, 'nf-l2', 'middle'); text('ejaculatory duct', CX + 360, CY - 180, 'nf-l2')
# spine
add('<rect x="1500" y="360" width="140" height="760" rx="30" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:3"/>'); text('lumbar spine', 1570, 340, 'nf-l1', 'middle')
for y in (520, 700, 880):
    add(f'<circle cx="1570" cy="{y}" r="34" style="fill:var(--ink-3);fill-opacity:.7"/>', when=D('ca'))
text('osteoblastic metastases · ↑ ALP', 1570, 1170, 'nf-l1 dyn-tag', 'middle', when=D('ca'))

# ════════ gland inset ════════
IX, IY = 1820, 420
add(f'<rect x="{IX}" y="{IY}" width="560" height="380" rx="24" class="dyn-soft"/>'); text('gland lining', IX + 20, IY - 16, 'nf-l1')
add(f'<circle cx="{IX + 280}" cy="{IY + 190}" r="120" style="fill:none;stroke:var(--dk4);stroke-width:14"/>')
add(f'<circle cx="{IX + 280}" cy="{IY + 190}" r="136" style="fill:none;stroke:var(--dk9);stroke-width:10"/>', unless=D('ca'))
add(f'<circle cx="{IX + 280}" cy="{IY + 190}" r="136" style="fill:none;stroke:var(--ink-3);stroke-width:4;stroke-dasharray:6 8"/>', when=D('ca'))
text('secretory (inner) · basal (outer)', IX + 280, IY + 360, 'nf-l2', 'middle')
text('basal cells kept — benign or PIN', IX + 280, IY + 410, 'nf-l1', 'middle', unless=D('ca'))
text('no basal cells — carcinoma · AMACR ↑', IX + 280, IY + 410, 'nf-l1 dyn-tag', 'middle', when=D('ca'))
for i in range(8):
    add(f'<circle cx="{IX + 180 + (i % 4) * 60}" cy="{IY + 140 + (i // 4) * 80}" r="14" style="fill:var(--bad);opacity:.8"/>', when=D('pin'))

# ════════ Gleason ════════
GX, GY = 1820, 960
add(f'<rect x="{GX}" y="{GY}" width="560" height="300" rx="24" class="dyn-soft"/>'); text('Gleason patterns', GX + 20, GY - 16, 'nf-l1')
for i in range(6):
    add(f'<circle cx="{GX + 80 + (i % 3) * 90}" cy="{GY + 100 + (i // 3) * 100}" r="34" style="fill:none;stroke:var(--dk4);stroke-width:6"/>', when=['gl:g33', 'gl:g34'])
for i in range(4):
    add(f'<path d="M{GX + 330 + i * 50} {GY + 60} v180" style="stroke:var(--bad);stroke-width:10"/>', when=['gl:g45', 'gl:g55'])
add(f'<rect x="{GX + 60}" y="{GY + 60}" width="240" height="180" rx="10" style="fill:var(--bad);fill-opacity:.4"/>', when=['gl:g55'])
for i in range(3):
    add(f'<path d="M{GX + 330 + i * 70} {GY + 100} a30 30 0 1 0 1 0" style="fill:none;stroke:var(--dk4);stroke-width:5"/>', when=['gl:g34'])
GL = dict(g33='3 + 3 = 6 → grade group 1', g34='3 + 4 = 7 → grade group 2', g45='4 + 5 = 9 — advanced, less curable', g55='5 + 5 = 10 → grade group 5 · sheets and cords')
for k, s in GL.items(): text(s, GX + 280, GY + 290, 'nf-l1', 'middle', when=[f'gl:{k}'])

TAG = dict(bph='BPH — transition zone around the urethra: obstruction; not premalignant · up to 90% by 80',
           pin='HGPIN — atypical cells, prominent nucleoli, basal layer still there; peripheral zone',
           ca='adenocarcinoma — peripheral zone, androgen-dependent · PSA ↑ (free fraction ↓) · Batson plexus → spine')
for k, s in TAG.items(): text(s, CX, 1300, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('α₁-blocker relaxes smooth muscle — urine flows', CX, 1340, 'nf-l1', 'middle', when=['dx:bph&alpha'])
text('finasteride blocks stromal 5α-reductase — gland shrinks; PSA halves (double it)', CX, 1380, 'nf-l1', 'middle', when=['dx:bph&fin'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{CX} 360 V{CY - 40} C{CX} {CY + 200} {CX} {CY + 260} {CX + 20} 1200', len=900, speed=120, r=9, base=dict(urine=4),
       mods=[m(D('bph'), set=dict(urine=2), speed=0.25), m(['dx:bph&alpha'], speed=3)]),
  dict(d=f'M{CX - 150} {CY + 20} C{CX - 100} {CY - 20} {CX - 60} {CY - 40} {CX - 30} {CY - 40}', len=140, speed=60, r=8, base=dict(dht=3),
       mods=[m(D('bph'), set=dict(dht=5)), m(['dx:bph&fin'], set=dict(dht=0))]),
  dict(d=f'M{CX + 330} {CY - 260} C{CX + 200} {CY - 200} {CX + 60} {CY - 100} {CX + 10} {CY - 40}', len=420, speed=90, r=8, base=dict(semen=3)),
  dict(d=f'M{CX - 330} {CY - 260} C{CX - 200} {CY - 200} {CX - 60} {CY - 100} {CX - 10} {CY - 40}', len=420, speed=90, r=8, base=dict(semen=3)),
  dict(d=f'M{CX + 160} {CY + 170} C{CX + 400} {CY + 100} 1400 800 1540 700', len=700, speed=110, r=10, base=dict(met=3), when=D('ca')),
]
sites = [dict(x=CX - 360, y=CY - 40, n=[-1, 0], w=10, t='rec', l='', aria='Prostate zones', c='prozones', ions=[]),
         dict(x=CX - 230, y=CY - 160, n=[-1, -1], w=10, t='rec', l='', aria='BPH', c='bphpath', ions=[]),
         dict(x=IX + 560, y=IY + 190, n=[1, 0], w=10, t='rec', l='', aria='HGPIN', c='hgpin', ions=[]),
         dict(x=GX + 560, y=GY + 150, n=[1, 0], w=10, t='rec', l='', aria='Gleason', c='gleason', ions=[]),
         dict(x=CX + 260, y=CY + 210, n=[1, 1], w=10, t='rec', l='', aria='Prostate cancer', c='prostateca', ions=[]),
         dict(x=CX + 530, y=CY - 280, n=[1, 0], w=10, t='rec', l='', aria='Semen', c='semen', ions=[])]

readouts = [
  dict(l='Urine flow', mods=[dict(when=D('bph'), d=-1), dict(when=['dx:bph&alpha'], d=1)]),
  dict(l='Gland size', mods=[dict(when=D('bph'), d=1), dict(when=['dx:bph&fin'], d=-1)]),
  dict(l='PSA', mods=[dict(when=D('ca'), d=1), dict(when=['dx:bph&fin'], d=-1)]),
  dict(l='Alkaline phosphatase', mods=[dict(when=D('ca'), d=1)]),
]

notes = {
  '': 'Transition zone around the urethra → BPH (obstructs); peripheral zone at the back → cancer (palpable). Glands have a basal '
      'layer under secretory cells. Semen: ~60% seminal vesicle (fructose), ~30% prostate (alkaline, PSA), ~10% vas deferens.',
  'dx:bph': 'BPH: stromal type 2 5α-reductase makes DHT, which drives stroma and epithelium; the transition zone squeezes the '
            'urethra. Not premalignant. α₁-blockers relax smooth muscle; finasteride/dutasteride shrink the gland (halve PSA, '
            '↓ libido, teratogenic to male fetuses).',
  'dx:pin': 'High-grade PIN: architecturally benign branching acini with atypical cells and prominent nucleoli, still with a basal '
            'layer — a peripheral-zone precursor; present in ~80% of cancer prostates.',
  'dx:ca': 'Prostate adenocarcinoma: peripheral zone, androgen-dependent; small crowded single-layered glands, no basal cells, '
           'AMACR ↑, perineural invasion. ↑ PSA with lower free fraction; Batson plexus → osteoblastic spine metastases (↑ ALP). '
           'Grade and stage predict outcome.',
  'gl:g33': 'Gleason adds the primary and secondary patterns (2–10): 3 + 3 = 6 → grade group 1.',
  'gl:g34': '3 + 4 = 7 → grade group 2 (4 + 3 would be group 3).',
  'gl:g45': '8–10 tend to be advanced and less curable.',
  'gl:g55': 'Pattern 5: cords, sheets, solid nests infiltrating stroma — up to group 5.',
}

dyn = dict(
  kinds=dict(urine=['mov', '--nf-h2o'], dht=['mov', '--dk4'], semen=['mov', '--dk10'], met=['mov', '--bad']),
  groups=[['mov', 'Urine · DHT · semen · metastases']],
  switches=[dict(id='dx', label='Process', type='one', options=[
              ['bph', 'BPH', 'bphpath'], ['pin', 'High-grade PIN', 'hgpin'], ['ca', 'Adenocarcinoma', 'prostateca']]),
            dict(id='gl', label='Gleason', type='one', options=[
              ['g33', '3 + 3', 'gleason'], ['g34', '3 + 4', 'gleason'], ['g45', '4 + 5', 'gleason'], ['g55', '5 + 5', 'gleason']]),
            dict(id='alpha', label='Drug', type='toggle', on='α₁-blocker given', off='α₁-blocker', def_=False),
            dict(id='fin', label='Drug', type='toggle', on='Finasteride given', off='Finasteride', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 21')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='prossim', title='The Prostate in Motion', topic='devrepro', after='prosobs',
  sub='See BPH squeeze the urethra from the transition zone and cancer grow in the peripheral zone, lose the basal layer and seed '
      'the spine — then grade it with Gleason and treat BPH with an α₁-blocker or finasteride',
  w=3600, h=1900,
  fa='646, 647, 672, 673',
  src=['Robbins ch 21 — The lower urinary tract and male genital system', 'Katzung ch 40 — The Gonadal Hormones & Inhibitors',
       'Guyton ch 81 — Reproductive and Hormonal Functions of the Male (and Function of the Pineal Gland)'],
  lanes=[('prNl', 'Normal', 'glycolysis'), ('prDz', 'Disease', 'tca')],
  nodes=[
    ('pr1', 'Prostate zones', 330, 1700, 'prNl', 'transition vs peripheral', ['prozones'], 'hub'),
    ('pr2', 'Semen & accessory glands', 760, 1700, 'prNl', 'SV 60% · prostate 30%', ['semen']),
    ('pr3', 'BPH & stromal DHT', 1200, 1700, 'prDz', '5α-reductase', ['bphpath']),
    ('pr4', 'High-grade PIN', 1640, 1700, 'prDz', 'basal cells kept', ['hgpin']),
    ('pr5', 'Prostate adenocarcinoma', 2080, 1700, 'prDz', 'peripheral · Batson', ['prostateca']),
    ('pr6', 'Gleason score', 2520, 1700, 'prDz', 'primary + secondary', ['gleason'])],
  panels=[
    (2500, PANY, 1000, 'Zone → disease (Robbins ch 21)', [
      ('Transition', 'BPH — obstructs'), ('Peripheral', 'cancer, HGPIN — palpable'), ('Basal cells', 'kept: benign/PIN · lost: cancer')])],
  dyn=dyn)
