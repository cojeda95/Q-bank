# Hypertension in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A pressure gauge driving blood from the heart through the aorta to the arterioles of the brain, eye, heart, kidneys and
# aorta wall, with both renal arteries and the adrenals. A `bp` switch steps the pressure (normal → white-coat → stage of
# essential hypertension → urgency → emergency); a `cause` switch adds a secondary cause the cards name (atherosclerotic or
# fibromuscular renal artery stenosis, Conn syndrome) with its renin/aldosterone pattern. End-organ damage lights up only in
# an emergency, as the card lists it. 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

B = lambda *k: [f'bp:{x}' for x in k]
C = lambda *k: [f'cause:{x}' for x in k]
PANY = 1180
HX, HY = 600, 760
ORG = dict(brain=(1300, 340, 'brain — encephalopathy, stroke'), eye=(1300, 520, 'retina — hemorrhages, papilledema'),
           heart=(1300, 700, 'heart — MI, failure, LVH'), aorta=(1300, 880, 'aorta — dissection'), kidney=(1300, 1060, 'kidney — injury'),
           blood=(1300, 1240, 'blood — microangiopathic hemolysis'))
GAUGE = dict(nl=('normal', 0), wc=('high in clinic only', 1), ess=('≥ 130 / ≥ 80', 2), urg=('≥ 180 / ≥ 120, no organ damage', 3), emerg=('≥ 180 / ≥ 120 + organ damage', 4))

text('Hypertension — from white coat to emergency', 180, 150, 'dyn-big')
text('step the pressure up · add a secondary cause', 180, 176, 'dyn-cap')

# ════════ heart + gauge ════════
add(f'<path d="M{HX} {HY + 120} C{HX - 200} {HY} {HX - 180} {HY - 180} {HX - 60} {HY - 160} C{HX} {HY - 150} {HX + 20} {HY - 110} {HX + 30} {HY - 100} '
    f'C{HX + 50} {HY - 130} {HX + 120} {HY - 170} {HX + 180} {HY - 120} C{HX + 260} {HY - 40} {HX + 180} {HY + 60} {HX} {HY + 120} Z" '
    'style="fill:var(--nf-blood);fill-opacity:.15;stroke:var(--nf-blood);stroke-width:5"/>', unless=B('ess', 'urg', 'emerg'))
add(f'<path d="M{HX} {HY + 140} C{HX - 230} {HY} {HX - 210} {HY - 200} {HX - 60} {HY - 180} C{HX} {HY - 170} {HX + 20} {HY - 120} {HX + 30} {HY - 110} '
    f'C{HX + 50} {HY - 150} {HX + 130} {HY - 190} {HX + 200} {HY - 130} C{HX + 290} {HY - 40} {HX + 200} {HY + 70} {HX} {HY + 140} Z" '
    'style="fill:var(--nf-blood);fill-opacity:.2;stroke:var(--bad);stroke-width:14"/>', when=B('ess', 'urg', 'emerg'))
text('heart', HX, HY + 200, 'nf-l1', 'middle'); text('concentric LVH', HX, HY + 230, 'nf-l2', 'middle', when=B('ess', 'urg', 'emerg'))
GX, GY = 400, 420
add(f'<path d="M{GX - 150} {GY} A150 150 0 0 1 {GX + 150} {GY}" style="fill:none;stroke:var(--line-2);stroke-width:20"/>')
add(f'<path d="M{GX + 75} {GY - 130} A150 150 0 0 1 {GX + 150} {GY}" style="fill:none;stroke:var(--bad);stroke-width:20;opacity:.5"/>')
import math
for k, (l, i) in GAUGE.items():
    a = math.radians(180 - 30 - i * 30)
    add(f'<path d="M{GX} {GY} L{GX + 130 * math.cos(a):.0f} {GY - 130 * math.sin(a):.0f}" style="stroke:var(--ink);stroke-width:8;stroke-linecap:round"/>', when=B(k))
    text(l, GX, GY + 50, 'nf-l1', 'middle', when=B(k))
add(f'<circle cx="{GX}" cy="{GY}" r="12" style="fill:var(--ink)"/>'); text('blood pressure', GX, GY - 180, 'nf-l1', 'middle')
text('home or ambulatory readings are normal — confirm before diagnosing', GX + 40, GY + 90, 'nf-l1 dyn-tag', 'middle', when=B('wc'))

# ════════ arteries & organs ════════
add(f'<path d="M{HX + 30} {HY - 110} C{HX + 60} 380 900 300 1000 300 V1240" style="fill:none;stroke:var(--nf-blood);stroke-width:40;opacity:.2"/>'); text('aorta', 1020, 280, 'nf-l2')
for k, (x, y, l) in ORG.items():
    add(f'<path d="M1000 {y} H{x - 50}" style="stroke:var(--nf-blood);stroke-width:12;opacity:.3"/>')
    add(f'<circle cx="{x}" cy="{y}" r="46" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>')
    add(f'<circle cx="{x}" cy="{y}" r="46" style="fill:var(--bad);fill-opacity:.4"/>', when=B('emerg'))
    text(l, x + 64, y + 6, 'nf-l1')
for k in ('brain', 'heart', 'kidney', 'eye'):
    x, y, _ = ORG[k]; add(f'<circle cx="{x}" cy="{y}" r="46" style="fill:var(--bad);fill-opacity:.15"/>', when=B('ess', 'urg'))
text('arterioles: hyaline (essential) · hyperplastic “onion skin” (severe) · fibrinoid necrosis (emergency)', 1300, 1380, 'nf-l2', 'middle')
# renal arteries + adrenal
RA = (900, 1150)
add(f'<path d="M1000 {RA[1]} H{RA[0] - 120}" style="stroke:var(--nf-blood);stroke-width:14;opacity:.35"/>')
add(f'<ellipse cx="{RA[0] - 190}" cy="{RA[1]}" rx="60" ry="90" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>', unless=C('athero', 'fmd'))
add(f'<ellipse cx="{RA[0] - 190}" cy="{RA[1]}" rx="44" ry="70" style="fill:var(--dk10);fill-opacity:.25;stroke:var(--bad);stroke-width:4"/>', when=C('athero', 'fmd'))
text('kidney (JG cells)', RA[0] - 190, RA[1] + 120, 'nf-l2', 'middle')
add(f'<path d="M{RA[0] - 30} {RA[1] - 14} v28" style="stroke:var(--bad);stroke-width:16"/>', when=C('athero'))
for i in range(4):
    add(f'<circle cx="{RA[0] - 40 - i * 18}" cy="{RA[1]}" r="10" style="fill:none;stroke:var(--bad);stroke-width:4"/>', when=C('fmd'))
add(f'<ellipse cx="{RA[0] - 190}" cy="{RA[1] - 130}" rx="40" ry="22" style="fill:var(--dk4);fill-opacity:.2;stroke:var(--dk4);stroke-width:3"/>', unless=C('conn'))
add(f'<ellipse cx="{RA[0] - 190}" cy="{RA[1] - 130}" rx="60" ry="34" style="fill:var(--dk4);fill-opacity:.4;stroke:var(--bad);stroke-width:4"/>', when=C('conn'))
text('adrenal', RA[0] - 270, RA[1] - 130, 'nf-l2', 'end')
CT = dict(athero='atherosclerotic stenosis — proximal third, older male smokers · renin ↑ aldosterone ↑',
          fmd='fibromuscular dysplasia — “string of beads”, distal two-thirds, young women · renin ↑ aldosterone ↑',
          conn='Conn — aldosterone ↑, renin ↓ · hypokalemia, metabolic alkalosis, no edema')
for k, s in CT.items(): text(s, 900, 1500, 'nf-l1 dyn-tag', 'middle', when=C(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FAST = [m(B('ess'), speed=1.3), m(B('urg', 'emerg'), speed=1.8, set=dict(blood=7))]
flows = [dict(d=f'M{HX + 30} {HY - 110} C{HX + 60} 380 900 300 1000 300 V1240', len=1500, speed=130, r=9, base=dict(blood=5), mods=FAST)]
flows += [dict(d=f'M1000 {y} H{x - 50}', len=300, speed=110, r=8, base=dict(blood=2), mods=FAST) for k, (x, y, _) in ORG.items()]
flows += [dict(d=f'M{RA[0] - 190} {RA[1] - 80} C{RA[0] - 300} {RA[1] - 300} 500 900 {HX - 150} {HY + 60}', len=900, speed=100, r=9, base=dict(renin=3), when=C('athero', 'fmd')),
          dict(d=f'M{RA[0] - 190} {RA[1] - 150} C{RA[0] - 300} {RA[1] - 360} 500 950 {HX - 120} {HY + 100}', len=900, speed=100, r=9, base=dict(aldo=3), when=C('athero', 'fmd', 'conn'))]
sites = [dict(x=GX + 180, y=GY - 60, n=[1, -1], w=10, t='rec', l='', aria='Essential hypertension', c='htn', ions=[]),
         dict(x=GX - 180, y=GY - 60, n=[-1, -1], w=10, t='rec', l='', aria='White-coat hypertension', c='whitecoathtn', ions=[]),
         dict(x=1380, y=250, n=[1, -1], w=10, t='rec', l='', aria='Hypertensive emergency', c='htnemerg', ions=[]),
         dict(x=RA[0] - 260, y=RA[1] + 40, n=[-1, 1], w=10, t='rec', l='', aria='Renovascular hypertension', c='renovascular', ions=[]),
         dict(x=RA[0] - 120, y=RA[1] - 160, n=[1, -1], w=10, t='rec', l='', aria='Conn syndrome', c='conn', ions=[]),
         dict(x=1360, y=1120, n=[1, 1], w=10, t='rec', l='', aria='Nephrosclerosis', c='nephrosclerosis', ions=[])]

readouts = [
  dict(l='Blood pressure', mods=[dict(when=B('wc', 'ess', 'urg', 'emerg') + C('athero', 'fmd', 'conn'), d=1)]),
  dict(l='Acute end-organ damage', mods=[dict(when=B('emerg'), d=1)]),
  dict(l='Renin', mods=[dict(when=C('athero', 'fmd'), d=1), dict(when=C('conn'), d=-1)]),
  dict(l='Aldosterone', mods=[dict(when=C('athero', 'fmd', 'conn'), d=1)]),
  dict(l='Serum K⁺', mods=[dict(when=C('conn'), d=-1)]),
]

notes = {
  '': 'Hypertension: persistent systolic ≥ 130 and/or diastolic ≥ 80 mm Hg, diagnosed from repeated readings. About 90% is '
      'essential; the rest is mostly renovascular, primary hyperaldosteronism or sleep apnea.',
  'bp:wc': 'White-coat hypertension: high in the office, normal at home — confirm with home or ambulatory readings first.',
  'bp:ess': 'Essential hypertension (≥ 130/80): raises risk of coronary disease, concentric LVH, heart failure, AF, dissection, '
            'stroke, CKD, retinopathy; hyaline arteriolosclerosis. First line: thiazide, ACEi, ARB, CCB.',
  'bp:urg': 'Hypertensive urgency: ≥ 180 / ≥ 120 without acute end-organ damage.',
  'bp:emerg': 'Hypertensive emergency: ≥ 180 / ≥ 120 with acute end-organ damage — encephalopathy, stroke, retinal hemorrhages, '
              'papilledema, MI, heart failure, dissection, kidney injury, microangiopathic hemolysis; fibrinoid necrosis.',
  'cause:athero': 'Renal artery stenosis (atherosclerotic): the kidney senses low perfusion and pours out renin — angiotensin II '
                  'raises pressure and holds that kidney’s GFR (efferent constriction), so ACEi/ARB can crash it.',
  'cause:fmd': 'Fibromuscular dysplasia: “string of beads”, distal two-thirds of the renal artery, young or middle-aged women.',
  'cause:conn': 'Conn syndrome: an adenoma or bilateral hyperplasia makes aldosterone on its own; volume expansion suppresses renin '
                '— high aldosterone:renin ratio, hypokalemia, metabolic alkalosis, no edema (escape).',
}

dyn = dict(
  kinds=dict(blood=['mov', '--nf-blood'], renin=['mov', '--dk10'], aldo=['mov', '--dk4']), groups=[['mov', 'Blood · renin · aldosterone']],
  switches=[dict(id='bp', label='Pressure', type='steps', auto=3, options=[
              ['nl', 'Normal'], ['wc', 'White coat'], ['ess', 'Essential'], ['urg', 'Urgency'], ['emerg', 'Emergency']]),
            dict(id='cause', label='Secondary cause', type='one', options=[
              ['athero', 'Atherosclerotic renal artery stenosis', 'renovascular'], ['fmd', 'Fibromuscular dysplasia', 'renovascular'],
              ['conn', 'Conn syndrome', 'conn']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 11')

MAP = dict(
  id='htnsim', title='Hypertension in Motion', topic='cardio', after='htnrx',
  sub='Step blood pressure from white coat to essential to urgency to emergency and watch the end organs, then add a renal artery '
      'stenosis or Conn syndrome and read renin and aldosterone',
  w=3600, h=1900,
  fa='304, 350, 354, 623',
  src=['Robbins ch 11 — Blood vessels', 'Katzung ch 11 — Antihypertensive Agents'],
  lanes=[('htLevel', 'Levels', 'tca'), ('htCause', 'Secondary causes', 'glycolysis')],
  nodes=[
    ('ht1', 'Essential hypertension', 330, 1720, 'htLevel', '≥ 130/80 · 90%', ['htn'], 'hub'),
    ('ht2', 'White-coat hypertension', 760, 1720, 'htLevel', 'home readings', ['whitecoathtn']),
    ('ht3', 'Hypertensive emergency', 1200, 1720, 'htLevel', 'organ damage', ['htnemerg']),
    ('ht4', 'Renovascular hypertension', 1640, 1720, 'htCause', 'renin ↑ aldo ↑', ['renovascular']),
    ('ht5', 'Conn syndrome', 2080, 1720, 'htCause', 'aldo ↑ renin ↓', ['conn']),
    ('ht6', 'Benign nephrosclerosis', 2520, 1720, 'htCause', 'hyaline arterioles', ['nephrosclerosis'])],
  panels=[
    (2500, PANY, 1000, 'Renin and aldosterone (Robbins ch 11)', [
      ('Renal artery stenosis', 'renin ↑ · aldosterone ↑'), ('Conn syndrome', 'renin ↓ · aldosterone ↑'),
      ('Urgency vs emergency', 'organ damage decides')])],
  dyn=dyn)
