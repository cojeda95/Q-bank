# Cerebellar Lesions in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The right cerebellar hemisphere's output crossing in the superior peduncle to the left VL thalamus and motor cortex, then back
# across at the pyramids to the right cord (two crossings, same side); the vermis and fastigial output to both vestibular nuclei;
# and a body on the right. A `les` switch places a lesion — right hemisphere, the vermis (alcohol, medulloblastoma), the left
# midbrain beyond the decussation, or the dorsal columns (sensory ataxia) — and an `eyes` toggle runs Romberg.
# Schematic. 5 readouts. Facts from the pinned cards (Fundamental Neuroscience ch 27, 33; Robbins ch 28); FA pages in `fa`. No new cards.
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

LS = lambda *k: [f'les:{x}' for x in k]
PANY = 1180
CX, CY = 760, 1060

text('Cerebellar lesions — two crossings make it the same side; the midline makes it the trunk', 180, 150, 'dyn-big')
text('brain on the left (patient’s left and right labeled), body on the right · eyes-closed toggle runs Romberg · schematic', 180, 176, 'dyn-cap')
# cortex, thalamus, midbrain, cerebellum, cord
for x, l in ((CX - 200, 'left motor cortex'), (CX + 200, 'right motor cortex')):
    add(f'<ellipse cx="{x}" cy="330" rx="150" ry="60" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:3"/>'); text(l, x, 336, 'nf-l2', 'middle')
for x, l in ((CX - 130, 'left VL thalamus'), (CX + 130, 'right VL thalamus')):
    add(f'<ellipse cx="{x}" cy="560" rx="90" ry="45" style="fill:var(--dk11);fill-opacity:.12;stroke:var(--dk11);stroke-width:3"/>'); text(l, x, 566, 'nf-l2', 'middle')
add(f'<rect x="{CX - 160}" y="700" width="320" height="180" rx="40" style="fill:var(--dk8);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
text('midbrain', CX + 180, 720, 'nf-l2')
text('SCP decussation', CX + 180, 830, 'nf-l2')
for x in (CX - 110, CX + 110):
    add(f'<circle cx="{x}" cy="760" r="24" style="fill:var(--nf-blood);fill-opacity:.25;stroke:var(--nf-blood);stroke-width:3"/>')
text('red nuclei', CX, 745, 'nf-l2', 'middle')
for x in (CX - 140, CX + 140):
    add(f'<circle cx="{x}" cy="940" r="22" style="fill:var(--dk6);fill-opacity:.25;stroke:var(--dk6);stroke-width:3"/>')
text('vestibular nuclei', CX - 180, 945, 'nf-l2', 'end')
add(f'<ellipse cx="{CX - 190}" cy="{CY + 60}" rx="180" ry="110" style="fill:var(--dk3);fill-opacity:.1;stroke:var(--dk3);stroke-width:4"/>')
add(f'<ellipse cx="{CX + 190}" cy="{CY + 60}" rx="180" ry="110" style="fill:var(--dk3);fill-opacity:.1;stroke:var(--dk3);stroke-width:4"/>')
add(f'<rect x="{CX - 40}" y="{CY - 20}" width="80" height="170" rx="30" style="fill:var(--dk3);fill-opacity:.2;stroke:var(--dk3);stroke-width:4"/>')
text('L hemisphere', CX - 190, CY + 200, 'nf-l2', 'middle'); text('R hemisphere', CX + 190, CY + 200, 'nf-l2', 'middle'); text('vermis', CX, CY + 175, 'nf-l2', 'middle')
add(f'<circle cx="{CX + 150}" cy="{CY + 40}" r="20" style="fill:var(--dk3);opacity:.5"/>'); text('dentate', CX + 180, CY + 46, 'nf-l2')
add(f'<path d="M{CX} {CY + 260} V1440" style="stroke:var(--dk8);stroke-width:80;opacity:.08;stroke-linecap:round"/>')
text('pyramidal decussation', CX + 60, 1290, 'nf-l2'); text('spinal cord', CX + 60, 1440, 'nf-l2')
text('patient’s LEFT', CX - 360, 260, 'nf-l1', 'middle'); text('patient’s RIGHT', CX + 360, 260, 'nf-l1', 'middle')
# body
BX = 1800
add(f'<circle cx="{BX}" cy="420" r="60" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
add(f'<rect x="{BX - 80}" y="500" width="160" height="380" rx="40" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
LIMB = dict(la=f'M{BX - 100} 520 L{BX - 220} 820', ra=f'M{BX + 100} 520 L{BX + 220} 820', ll=f'M{BX - 50} 900 L{BX - 90} 1300', rl=f'M{BX + 50} 900 L{BX + 90} 1300')
for k, d in LIMB.items():
    add(f'<path d="{d}" style="stroke:var(--line-2);stroke-width:40;stroke-linecap:round;opacity:.6"/>')
text('LEFT', BX - 260, 520, 'nf-l1', 'end'); text('RIGHT', BX + 260, 520, 'nf-l1')
text('trunk', BX, 700, 'nf-l2', 'middle')
RIGHT = LS('rh', 'mb')
for k in ('ra', 'rl'):
    add(f'<path d="{LIMB[k]}" style="stroke:var(--bad);stroke-width:40;stroke-linecap:round;opacity:.5"/>', when=RIGHT)
add(f'<rect x="{BX - 80}" y="500" width="160" height="380" rx="40" style="fill:var(--bad);fill-opacity:.35"/>', when=LS('mid'))
add(f'<circle cx="{BX}" cy="420" r="60" style="fill:var(--bad);fill-opacity:.3"/>', when=LS('mid'))
for k in ('ll', 'rl'):
    add(f'<path d="{LIMB[k]}" style="stroke:var(--dk10);stroke-width:40;stroke-linecap:round;opacity:.55"/>', when=LS('dc'))
# sway
add(f'<path d="M{BX - 200} 1360 Q{BX} 1300 {BX + 200} 1360" style="fill:none;stroke:var(--bad);stroke-width:8;stroke-dasharray:16 10"/>', when=['les:mid', 'les:dc&eyes'])
text('sways, wide base', BX, 1400, 'nf-l1', 'middle', when=['les:mid', 'les:dc&eyes'])
add(f'<path d="M{BX - 30} 380 h60" style="stroke:var(--ink);stroke-width:8"/>', when=['eyes'])
text('eyes closed', BX + 80, 390, 'nf-l2', when=['eyes'])
# lesions
add(f'<ellipse cx="{CX + 190}" cy="{CY + 60}" rx="120" ry="70" style="fill:var(--bad);opacity:.45"/>', when=LS('rh'))
add(f'<rect x="{CX - 40}" y="{CY - 20}" width="80" height="120" rx="30" style="fill:var(--bad);opacity:.5"/>', when=LS('mid'))
add(f'<circle cx="{CX - 110}" cy="660" r="44" style="fill:var(--bad);opacity:.45"/>', when=LS('mb'))
add(f'<path d="M{CX - 30} 1330 V1460 M{CX + 30} 1330 V1460" style="stroke:var(--dk10);stroke-width:18"/>', when=LS('dc'))
text('dorsal columns', CX - 60, 1480, 'nf-l2', 'end', when=LS('dc'))
TAG = dict(rh='right hemisphere — right-sided dysmetria, intention tremor, dysdiadochokinesia, rebound, hypotonia; leans to the right',
           mid='vermis (alcohol: anterior superior vermis · medulloblastoma in a child) — truncal ataxia, wide base, titubation, nystagmus, both sides',
           mb='left midbrain beyond the decussation — signs on the right: opposite the lesion',
           dc='dorsal columns (B12, vitamin E, copper deficiency, tabes) — lost position & vibration sense: steady eyes open, falls eyes closed')
for k, s in TAG.items(): text(s, 1100, 1520, 'nf-l1 dyn-tag', 'middle', when=LS(k))
text('Romberg positive — vision was holding them up', 1100, 1560, 'nf-l1', 'middle', when=['les:dc&eyes'])
text('unsteady with eyes open too — not a Romberg sign', 1100, 1560, 'nf-l1', 'middle', when=['les:mid'])

# ════════ motion ════════
OUT = (f'M{CX + 150} {CY + 40} C{CX + 120} 960 {CX + 60} 880 {CX} 820 C{CX - 60} 760 {CX - 130} 680 {CX - 130} 600 '
       f'C{CX - 140} 500 {CX - 200} 440 {CX - 200} 390')
DOWN = f'M{CX - 260} 380 C{CX - 320} 600 {CX - 100} 1100 {CX - 40} 1250 C{CX} 1300 {CX + 30} 1330 {CX + 40} 1460'
flows = [dict(d=OUT, len=900, speed=140, r=8, base=dict(sig=3), when=['!les:rh&!les:mb']),
         dict(d=DOWN, len=1200, speed=140, r=8, base=dict(sig=3), when=['!les:rh&!les:mb']),
         dict(d=f'M{CX + 40} 1460 C{CX + 400} 1500 {BX - 400} 900 {BX + 100} 560', len=1300, speed=160, r=7, base=dict(sig=2), when=['!les:rh&!les:mb']),
         dict(d=OUT, len=900, speed=60, r=8, base=dict(bad=2), when=LS('rh')),
         # left midbrain lesion: the crossed output reaches the lesion and goes no further
         dict(d=f'M{CX + 150} {CY + 40} C{CX + 120} 960 {CX + 60} 880 {CX} 820 L{CX - 100} 680', len=560, speed=60, r=8, base=dict(bad=2), when=LS('mb')),
         dict(d=f'M{CX} {CY} C{CX - 60} 1000 {CX - 120} 980 {CX - 140} 940', len=200, speed=80, r=7, base=dict(sig=2), when=['!les:mid']),
         dict(d=f'M{CX} {CY} C{CX + 60} 1000 {CX + 120} 980 {CX + 140} 940', len=200, speed=80, r=7, base=dict(sig=2), when=['!les:mid']),
         dict(d=f'M{CX + 40} 1460 V1320', len=140, speed=60, r=7, base=dict(prop=2), when=['!les:dc'])]
sites = [dict(x=CX + 430, y=CY + 40, n=[1, 1], w=10, t='rec', l='', aria='The ipsilateral rule', c='cbipsi', ions=[]),
         dict(x=BX + 300, y=1200, n=[1, 1], w=10, t='rec', l='', aria='Cerebellar vs sensory ataxia', c='cbataxia', ions=[]),
         dict(x=CX - 420, y=CY + 120, n=[-1, 1], w=10, t='rec', l='', aria='Causes of cerebellar ataxia', c='cbcauses', ions=[])]

readouts = [
  dict(l='Right limb coordination', mods=[dict(when=LS('rh', 'mb'), d=-1), dict(when=LS('mid'), d=0)]),
  dict(l='Left limb coordination', mods=[dict(when=LS('rh', 'mb', 'mid'), d=0)]),
  dict(l='Trunk & gait', mods=[dict(when=['les:mid', 'les:dc&eyes'], d=-1)]),
  dict(l='Position sense', mods=[dict(when=LS('dc'), d=-1), dict(when=LS('rh', 'mid', 'mb'), d=0)]),
  dict(l='Nystagmus', mods=[dict(when=LS('mid', 'rh'), d=1)]),
]

notes = {
  '': 'The right lateral and interposed nuclei cross in the superior peduncle decussation to the left VL thalamus (→ left motor cortex) and '
      'the left red nucleus; both project back across to the right cord. Two crossings, so a hemisphere lesion shows on its own side. '
      'The vermis and fastigial nuclei reach the vestibular and reticular nuclei of both sides — the trunk.',
  'les:rh': 'Right hemisphere lesion: right-sided dysmetria (past-pointing), intention tremor worst near the target, dysdiadochokinesia, a '
            'heel-to-shin that slips off, rebound, hypotonia, scanning dysarthria, leaning or falling toward the lesion. Cerebellar '
            'nystagmus: slow drift away from the lesion.',
  'les:mid': 'Midline lesion: bilateral, trunk and axial muscles — wide-based lurching gait, cannot walk tandem, titubation, nystagmus, head '
             'tilt; unsteady even with the eyes open. Alcohol (about 1% of alcohol use disorder) loses granule then Purkinje cells in the '
             'anterior superior vermis with Bergmann gliosis; medulloblastoma grows in a child’s vermis; Dandy-Walker lacks a vermis.',
  'les:mb': 'Past the decussation the fibers already serve the other side, so a midbrain lesion there gives cerebellar signs opposite the lesion.',
  'les:dc': 'Sensory ataxia: dorsal columns or nerves (B12, vitamin E or copper deficiency, tabes dorsalis) — lost position and vibration '
            'sense. Friedreich ataxia mixes both: gait ataxia from childhood, lost position sense, low reflexes with an extensor plantar, '
            'cardiomyopathy. Spinocerebellar ataxias are dominant; many are CAG repeats.',
  'eyes': 'Romberg: feet together, eyes closed. Steady with eyes open but falling once they close means vision was replacing lost position '
          'sense. A midline cerebellar patient is unsteady with the eyes open as well.',
}

dyn = dict(
  kinds=dict(sig=['mov', '--dk7'], bad=['mov', '--bad'], prop=['mov', '--dk10']),
  groups=[['mov', 'Cerebellar output · position sense']],
  switches=[dict(id='les', label='Lesion', type='one', options=[
              ['rh', 'Right hemisphere', 'cbipsi'], ['mid', 'Vermis (midline)', 'cbcauses'], ['mb', 'Left midbrain, past the crossing', 'cbipsi'],
              ['dc', 'Dorsal columns (sensory)', 'cbataxia']]),
            dict(id='eyes', label='Romberg', type='toggle', on='Eyes closed', off='Close the eyes', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Fundamental Neuroscience ch 27, 33 · Robbins ch 28')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='cbsim', title='Cerebellar Lesions in Motion', topic='neuro', after='cerebellum',
  sub='Damage a cerebellar hemisphere, the vermis, the midbrain past the crossing or the dorsal columns, and see which side and which part '
      'of the body goes wrong — then close the eyes for Romberg',
  w=3600, h=1900,
  fa='510, 524, 544',
  src=['Fundamental Neuroscience ch 27 — The Cerebellum', 'Fundamental Neuroscience ch 33 — The Neurologic Examination',
       'Robbins ch 28 — The central nervous system'],
  lanes=[('cbRule', 'Which side', 'tca'), ('cbDz', 'Ataxia & causes', 'glycolysis')],
  nodes=[
    ('cb1', 'The ipsilateral rule', 400, 1720, 'cbRule', 'two crossings', ['cbipsi', 'cbzones', 'cerebcircuit', 'cbpeduncle', 'cbcompare'], 'hub'),
    ('cb2', 'Cerebellar vs sensory ataxia', 950, 1720, 'cbDz', 'Romberg', ['cbataxia']),
    ('cb3', 'Causes of cerebellar ataxia', 1500, 1720, 'cbDz', 'alcohol · tumors · SCA', ['cbcauses', 'cerebellar'])],
  panels=[
    (2500, PANY, 1000, 'Where is the lesion? (Fundamental Neuroscience ch 27, 33)', [
      ('Hemisphere', 'same-side limbs'), ('Vermis', 'trunk, both sides'), ('Past the SCP crossing', 'opposite side'),
      ('Falls only eyes closed', 'dorsal columns')])],
  dyn=dyn)
