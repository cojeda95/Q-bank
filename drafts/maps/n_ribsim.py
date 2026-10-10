# Rib Motion in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Four drawn panels breathe in and out on a `steps` switch (auto): pump-handle ribs (side view — the front of the
# rib rises and the chest deepens), bucket-handle ribs (front view — the side lifts and the chest widens), caliper
# ribs 11–12 (top view — posterior-lateral on inhalation) and a stack of ribs 1–12. A `one` switch makes ribs 4–6
# an inhaled or exhaled group and marks the key rib (BITE); a second `one` switch picks an exhaled rib level and
# names the muscle its muscle-energy technique uses. 2 readouts. Facts from the pinned cards (ribmotion, ribresp,
# ribstruct, met, csrib, ribraise), sourced to Foundations ch 31/35, the Atlas of Osteopathic Techniques ch 9–10
# and the OCOM OMM course texts; no First Aid pages. No new cards.
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


BR = 'br'
INH, EXH = ['br:inh'], ['br:exh']
D = lambda *k: [f'dys:{x}' for x in k]
PANY = 760
FND35, FND31 = 'Foundations of Osteopathic Medicine ch 35 — Rib Cage', 'Foundations of Osteopathic Medicine ch 31 — Osteopathic Segmental Examination'
ATL10, ATL9 = 'Atlas of Osteopathic Techniques ch 10 — Muscle Energy Techniques', 'Atlas of Osteopathic Techniques ch 9 — Counterstrain Techniques'
OCOM_SG, OCOM_PULM = 'OCOM OMM — OMS2 written midterm study guide', 'OCOM OMM — Pulmonary OMM lab slides'

# ════════ A · pump handle (side view) ════════
box(160, 130, 1220, 760)
text('Pump handle — ribs 2–4, side view', 190, 170, 'dyn-big')
text('axis nearly coronal: the front of the rib rises and the chest deepens front to back', 190, 196, 'dyn-cap')
add('<rect x="270" y="360" width="70" height="200" rx="12" class="dyn-cell"/>')
text('vertebra', 305, 590, 'nf-l2', 'middle')
add('<circle cx="340" cy="430" r="10" style="fill:var(--ink)"/>')
text('axis', 340, 410, 'nf-l2', 'middle')
for (y0, dy) in ((430, 0), (470, 40)):
    add(f'<path d="M340 {y0} Q700 {y0 + 40} 1030 {560 + dy}" style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=EXH)
    add(f'<path d="M340 {y0} Q720 {y0 - 10} 1070 {470 + dy}" style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=INH)
add('<rect x="1030" y="480" width="34" height="200" rx="10" style="fill:var(--dk9);fill-opacity:.4"/>', when=EXH)
add('<rect x="1070" y="390" width="34" height="200" rx="10" style="fill:var(--dk9);fill-opacity:.4"/>', when=INH)
text('sternum', 1047, 710, 'nf-l2', 'middle', when=EXH)
text('the front of the rib rises', 1120, 380, 'nf-l1 dyn-tag', 'end', when=INH)
add('<path d="M340 680 H1030" style="stroke:var(--ink-3);stroke-width:3" marker-end="url(#ah-rbMove)"/>', when=EXH)
add('<path d="M340 680 H1070" style="stroke:var(--accent);stroke-width:5" marker-end="url(#ah-rbMove)"/>', when=INH)
text('front-to-back depth', 360, 670, 'nf-l2')

# ════════ B · bucket handle (front view) ════════
box(1260, 130, 2320, 760)
text('Bucket handle — ribs 8–10, front view', 1290, 170, 'dyn-big')
text('axis swings toward sagittal: the side of the rib lifts outward and the chest widens', 1290, 196, 'dyn-cap')
add('<rect x="1774" y="270" width="34" height="400" rx="10" style="fill:var(--dk9);fill-opacity:.4"/>')
for side in (-1, 1):
    sx = lambda x: round(1791 + side * x)
    add(f'<path d="M{sx(0)} 320 C{sx(260)} 330 {sx(390)} 470 {sx(360)} 560 C{sx(330)} 640 {sx(150)} 640 {sx(0)} 610" '
        f'style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=EXH)
    add(f'<path d="M{sx(0)} 320 C{sx(300)} 320 {sx(460)} 420 {sx(440)} 500 C{sx(420)} 590 {sx(170)} 620 {sx(0)} 610" '
        f'style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=INH)
add('<path d="M1430 700 H2152" style="stroke:var(--ink-3);stroke-width:3"/>', when=EXH)
add('<path d="M1350 700 H2232" style="stroke:var(--accent);stroke-width:5"/>', when=INH)
text('side-to-side width', 1791, 735, 'nf-l2', 'middle')

# ════════ C · caliper (top view) ════════
box(160, 800, 1220, 1320)
text('Caliper — ribs 11–12, top view', 190, 840, 'dyn-big')
text('no front attachment: posterior and lateral on inhalation, anterior and medial on exhalation', 190, 866, 'dyn-cap')
add('<circle cx="690" cy="1130" r="60" class="dyn-cell"/>')
text('vertebra', 690, 1136, 'nf-l2', 'middle')
text('anterior ↑', 690, 930, 'nf-l1', 'middle')
for side in (-1, 1):
    add(f'<path d="M{690 + side * 60} 1120 Q{690 + side * 260} 1100 {690 + side * 380} 1010" style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=EXH)
    add(f'<path d="M{690 + side * 60} 1120 Q{690 + side * 300} 1140 {690 + side * 450} 1100" style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-linecap:round"/>', when=INH)

# ════════ D · ribs 1–12 and their dysfunctions ════════
box(1260, 800, 2320, 1320)
text('Ribs 1–12 — inhaled and exhaled groups', 1290, 840, 'dyn-big')
text('an inhaled rib won’t go down; an exhaled rib won’t go up', 1290, 866, 'dyn-cap')
RY = lambda i: 910 + (i - 1) * 34
GROUP = (4, 5, 6)
for i in range(1, 13):
    y = RY(i)
    text(str(i), 1470, y + 5, 'nf-l2', 'end')
    if i in GROUP:
        up = ['br:inh&!dys:exh', 'dys:inh']; down = ['br:exh&!dys:inh', 'dys:exh']
    else:
        up, down = INH, EXH
    add(f'<path d="M1500 {y} H1860" style="stroke:var(--dk4);stroke-width:12;stroke-linecap:round"/>', when=down)
    add(f'<path d="M1500 {y} L1860 {y - 12}" style="stroke:var(--dk4);stroke-width:12;stroke-linecap:round"/>', when=up)
add(f'<rect x="1488" y="{RY(4) - 22}" width="384" height="{RY(6) - RY(4) + 40}" rx="10" style="fill:none;stroke:var(--bad);stroke-width:3;stroke-dasharray:8 6"/>', when=D('inh', 'exh'))
add(f'<path d="M1500 {RY(6)} L1860 {RY(6) - 12}" style="stroke:var(--bad);stroke-width:16;stroke-linecap:round"/>', when=D('inh'))
add(f'<path d="M1500 {RY(4)} H1860" style="stroke:var(--bad);stroke-width:16;stroke-linecap:round"/>', when=D('exh'))
text('ribs 4–6 stuck up — key rib: the BOTTOM one (6)', 1900, RY(6) + 5, 'nf-l1 dyn-tag', when=D('inh'))
text('ribs 4–6 stuck down — key rib: the TOP one (4)', 1900, RY(4) + 5, 'nf-l1 dyn-tag', when=D('exh'))
# muscle energy for an exhaled rib: the muscle that lifts it
MET = dict(r1=((1,), 'anterior and middle scalenes'), r2=((2,), 'posterior scalene'), r35=((3, 4, 5), 'pectoralis minor'),
           r69=((6, 7, 8, 9), 'serratus anterior'), r1011=((10, 11), 'latissimus dorsi'), r12=((12,), 'quadratus lumborum'))
for k, (ribs, mus) in MET.items():
    a, b = ribs[0], ribs[-1]
    add(f'<rect x="1488" y="{RY(a) - 20}" width="384" height="{RY(b) - RY(a) + 36}" rx="10" style="fill:var(--accent);fill-opacity:.16;stroke:var(--accent);stroke-width:3"/>', when=[f'met:{k}'])
    text(f'MET for an exhaled rib: {mus}', 1900, RY(b) + 30 if b < 12 else RY(b) - 20, 'nf-l1', when=[f'met:{k}'])

# breath in and out (the trachea in panel A)
flows = [dict(d='M700 150 V330', len=180, speed=80, r=6, base=dict(air=3), when=INH),
         dict(d='M720 330 V150', len=180, speed=80, r=6, base=dict(air=3), when=EXH)]
add('<path d="M700 140 V330 M720 140 V330" style="stroke:var(--line-2);stroke-width:3"/>')
text('air', 740, 250, 'nf-l2')

sites = [dict(x=305, y=360, n=[0, -1], w=10, t='rec', l='', aria='Rib motion — the axis', c='ribmotion', ions=[]),
         dict(x=1860, y=RY(5), n=[1, 0], w=10, t='rec', l='', aria='Inhaled and exhaled ribs', c='ribresp', ions=[])]

readouts = [
  dict(l='Front-to-back depth', mods=[dict(when=INH, d=1), dict(when=EXH, d=-1)]),
  dict(l='Side-to-side width', mods=[dict(when=INH, d=1), dict(when=EXH, d=-1)]),
]

notes = {
  '': 'Each rib turns about an axis through its costovertebral and costotransverse joints. Upper ribs move like a pump handle, '
      'lower ribs like a bucket handle, and the floating ribs 11–12 like a caliper.',
  'br:inh': 'Inhalation: the pump-handle ribs lift their front ends (the chest deepens), the bucket-handle ribs lift their sides '
            '(the chest widens), and ribs 11–12 swing posterior and lateral.',
  'br:exh': 'Exhalation: everything reverses — pump-handle fronts drop, bucket-handle sides fall, and ribs 11–12 move anterior and '
            'medial.',
  'dys:inh': 'An inhaled rib moves freely up but is restricted coming down — it stops first on exhalation. In a group the key rib '
             'is the BOTTOM one (BITE: Bottom Inhaled, Top Exhaled); treat it and the group releases.',
  'dys:exh': 'An exhaled rib moves freely down but is restricted going up — it stops first on inhalation. The key rib of an '
             'exhaled group is the TOP one. Treat with muscle energy using the muscle that lifts that rib.',
  'met:r1': 'Exhaled rib 1: muscle energy uses the anterior and middle scalenes (course slides).',
  'met:r2': 'Exhaled rib 2: muscle energy uses the posterior scalene.',
  'met:r35': 'Exhaled ribs 3–5: muscle energy uses pectoralis minor.',
  'met:r69': 'Exhaled ribs 6–9: muscle energy uses serratus anterior.',
  'met:r1011': 'Exhaled ribs 10–11: muscle energy uses latissimus dorsi.',
  'met:r12': 'Exhaled rib 12: muscle energy uses quadratus lumborum.',
}

dyn = dict(
  kinds=dict(air=['air', '--nf-h2o']), groups=[['air', 'Air']],
  switches=[dict(id=BR, label='Breath', type='steps', auto=3, options=[['exh', 'Exhale'], ['inh', 'Inhale']]),
            dict(id='dys', label='Respiratory rib dysfunction (ribs 4–6)', type='one', options=[['inh', 'Inhaled group', 'ribresp'], ['exh', 'Exhaled group', 'ribresp']]),
            dict(id='met', label='Muscle energy for an exhaled rib', type='one', options=[
              ['r1', 'Rib 1', 'ribresp'], ['r2', 'Rib 2', 'ribresp'], ['r35', 'Ribs 3–5', 'ribresp'], ['r69', 'Ribs 6–9', 'ribresp'],
              ['r1011', 'Ribs 10–11', 'ribresp'], ['r12', 'Rib 12', 'ribresp']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Foundations of Osteopathic Medicine ch 31, 35 · Atlas of Osteopathic Techniques ch 10 · OCOM OMM course texts')

MAP = dict(
  id='ribsim', title='Rib Motion in Motion', topic='omm', after='ommmech',
  sub='Breathe in and out and watch pump-handle ribs deepen the chest, bucket-handle ribs widen it and the floating ribs swing '
      'like calipers — then make ribs 4–6 an inhaled or exhaled group, find the key rib, and name the muscle that lifts each exhaled rib',
  w=3500, h=1640,
  fa='',
  src=[FND35, FND31, ATL10, ATL9, OCOM_SG, OCOM_PULM],
  lanes=[('rbMove', 'Rib motion', 'glycolysis'), ('rbDys', 'Rib dysfunction', 'tca'), ('rbTx', 'Treatment', 'gluconeo')],
  nodes=[
    ('rb1', 'Rib motion', 330, 1420, 'rbMove', 'pump · bucket · caliper', ['ribmotion'], 'hub'),
    ('rb2', 'Inhaled vs exhaled ribs', 760, 1420, 'rbDys', 'BITE', ['ribresp']),
    ('rb3', 'Structural rib dysfunction', 1200, 1420, 'rbDys', 'subluxation · torsion', ['ribstruct']),
    ('rb4', 'Muscle energy', 1620, 1420, 'rbTx', 'patient pushes', ['met']),
    ('rb5', 'Rib counterstrain', 330, 1550, 'rbTx', 'AR · PR points', ['csrib']),
    ('rb6', 'Rib raising', 760, 1550, 'rbTx', 'sympathetic chain', ['ribraise'])],
  panels=[
    (2420, PANY, 1000, 'Which ribs move how (Foundations ch 35)', [
      ('Ribs 2–4', 'mostly pump handle'),
      ('Ribs 5–7', 'mixed'),
      ('Ribs 8–10', 'mostly bucket handle'),
      ('Ribs 11–12', 'caliper'),
      ('Key rib', 'bottom of an inhaled group, top of an exhaled one')])],
  dyn=dyn)
