# The O₂ Curve in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A schematic hemoglobin dissociation curve (saturation vs PO₂; the shapes are drawn, not plotted from measured values)
# with a dot riding it from the lungs to the tissues, a bracket for how much O₂ is unloaded, and a red cell beside it.
# A `one` switch shifts the curve right (exercise, acid and CO₂ — the Bohr effect, fever, high altitude and 2,3-BPG) or
# left (cold, fetal hemoglobin, myoglobin for comparison), or shows CO poisoning, methemoglobinemia, anemia,
# polycythemia, cyanide and sickle cell. 5 readouts (P50, SaO₂, PaO₂, O₂ content, unloading). Facts from the pinned
# cards; FA pages in `fa`. No new cards.
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

O = lambda *k: [f'sh:{x}' for x in k]
PANY = 1180
X0, Y0, XS, YS = 400, 1100, 10, 7          # chart origin; px per mm Hg, px per % saturation
def px(p): return round(X0 + p * XS)
def py(s): return round(Y0 - s * YS)
def sat(p, p50, n=2.7, top=100): return top * p ** n / (p ** n + p50 ** n) if p > 0 else 0
def curve(p50, n=2.7, top=100, p0=0, p1=120):
    pts = [(p, sat(p, p50, n, top)) for p in [p0 + i * (p1 - p0) / 60 for i in range(61)]]
    return 'M' + ' L'.join(f'{px(p)} {py(s)}' for p, s in pts)
RIGHT = O('exer', 'acid', 'fever', 'alt')
LEFT = O('cold', 'hbf')
LOWTOP = O('co', 'metb')
CURVES = {                                   # key → (p50, n, top, when, unless)
  'norm': (27, 2.7, 100, None, RIGHT + LEFT + LOWTOP + O('myo')),
  'right': (37, 2.7, 100, RIGHT, None),
  'left': (18, 2.7, 100, LEFT, None),
  'low': (18, 2.7, 55, LOWTOP, None),
  'myo': (4, 1.0, 100, O('myo'), None),
}

text('The O₂–hemoglobin curve — loading in the lungs, unloading in the tissues', 180, 150, 'dyn-big')
text('a schematic curve; right = less affinity, more unloading · left = more affinity, less unloading', 180, 176, 'dyn-cap')

# ════════ the chart ════════
add(f'<path d="M{X0} {py(100) - 30} V{Y0} H{px(125)}" style="fill:none;stroke:var(--ink-2);stroke-width:3"/>')
for p in range(0, 121, 20):
    add(f'<path d="M{px(p)} {Y0} v10" style="stroke:var(--ink-2);stroke-width:2"/>'); text(str(p), px(p), Y0 + 36, 'nf-l2', 'middle')
for s in (0, 50, 100):
    add(f'<path d="M{X0} {py(s)} h-10" style="stroke:var(--ink-2);stroke-width:2"/>'); text(f'{s}%', X0 - 20, py(s) + 5, 'nf-l2', 'end')
text('PO₂ (mm Hg)', px(60), Y0 + 76, 'nf-l1', 'middle')
text('Hb saturation', X0 - 20, py(100) - 50, 'nf-l1')
for p, lab in ((40, 'tissues'), (100, 'lungs')):
    add(f'<path d="M{px(p)} {Y0} V{py(100) - 10}" style="stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 8"/>')
    text(lab, px(p), py(100) - 24, 'nf-l1', 'middle')
add(f'<path d="{curve(27)}" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 8"/>', when=['sh:*'], unless=O('anemia', 'poly', 'cn', 'sickle'))
text('dashed = normal', px(120), Y0 - 24, 'nf-l2', 'end', when=['sh:*'], unless=O('anemia', 'poly', 'cn', 'sickle'))
for k, (p50, n, top, w, u) in CURVES.items():
    add(f'<path d="{curve(p50, n, top)}" style="fill:none;stroke:var(--nf-blood);stroke-width:6"/>', when=w, unless=u)
    s100, s40 = sat(100, p50, n, top), sat(40, p50, n, top)
    add(f'<path d="M{px(108)} {py(s100)} H{px(114)} V{py(s40)} H{px(108)}" style="fill:none;stroke:var(--accent);stroke-width:4"/>', when=w, unless=u)
text('unloaded', px(116), py(78), 'nf-l1', 'start')
# P50 marker: the shift
text('→ right shift: P50 rises', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=RIGHT)
text('← left shift: P50 falls', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=LEFT)
text('fewer hemes carry O₂, and the rest hold on tighter', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=LOWTOP)
text('myoglobin: one chain, binds tighter, not sigmoid', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=O('myo'))
text('curve unchanged — less hemoglobin, so less O₂ per dL', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=O('anemia'))
text('curve unchanged — more hemoglobin, more O₂ per dL', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=O('poly'))
text('curve and blood gas normal — the cells can’t use the O₂', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=O('cn'))
text('curve unchanged here — low O₂ in the tissues sickles the cell', px(40), py(30), 'nf-l1 dyn-tag', 'start', when=O('sickle'))

# ════════ the red cell ════════
RX, RY = 2050, 640
add(f'<ellipse cx="{RX}" cy="{RY}" rx="230" ry="150" style="fill:var(--nf-blood);fill-opacity:.18;stroke:var(--nf-blood);stroke-width:4"/>', unless=O('sickle'))
add(f'<path d="M{RX - 250} {RY + 40} Q{RX - 60} {RY - 200} {RX + 250} {RY - 20} Q{RX + 40} {RY - 90} {RX - 250} {RY + 40} Z" style="fill:var(--nf-blood);fill-opacity:.25;stroke:var(--bad);stroke-width:4"/>', when=O('sickle'))
text('red cell', RX, RY - 170, 'nf-l1', 'middle')
TAG = dict(exer='exercise shifts the curve right', acid='Bohr effect: H⁺ and CO₂ lower the affinity',
           fever='↑ temperature', alt='chronic altitude: ↑ 2,3-BPG and ↑ EPO', cold='↓ temperature',
           hbf='HbF (α₂γ₂) binds 2,3-BPG poorly — pulls O₂ across the placenta', myo='myoglobin stores O₂ in muscle',
           co='CO binds Hb with >200× the affinity of O₂', metb='Fe³⁺ heme can’t bind O₂ — chocolate-brown blood',
           anemia='fewer red cells, normal SaO₂ and PaO₂', poly='more red cells', cn='cyanide blocks complex IV',
           sickle='deoxy-HbS polymerizes (Glu6Val); acidosis, dehydration promote it')
for k, t in TAG.items(): text(t, RX, RY + 200, 'nf-l1 dyn-tag', 'middle', when=O(k))
text('Hb · 2,3-BPG · H⁺ · CO₂', RX, RY + 6, 'nf-l2', 'middle')
text('O₂ to the tissues', RX + 120, RY + 280, 'nf-l2', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = []
for k, (p50, n, top, w, u) in CURVES.items():
    d = curve(p50, n, top, 100, 40).replace('M', 'M', 1)
    f = dict(d=d, len=900, speed=160, r=12, base=dict(o2=2))
    if w: f['when'] = w
    if u: f['unless'] = u
    flows.append(f)
flows.append(dict(d=f'M{RX + 60} {RY + 120} L{RX + 160} {RY + 260}', len=180, speed=80, r=8, base=dict(o2=3),
                  mods=[m(RIGHT, set=dict(o2=5)), m(LEFT + LOWTOP + O('anemia'), set=dict(o2=1))]))
sites = [dict(x=px(70), y=Y0, n=[0, 1], w=10, t='rec', l='', aria='The dissociation curve', c='odc', ions=[]),
         dict(x=RX - 230, y=RY, n=[-1, 0], w=10, t='rec', l='', aria='Hemoglobin types', c='hbtypes', ions=[])]

readouts = [
  dict(l='P50', mods=[dict(when=RIGHT, d=1), dict(when=LEFT + LOWTOP + O('myo'), d=-1)]),
  dict(l='SaO₂', mods=[dict(when=LOWTOP, d=-1), dict(when=O('anemia', 'cn'), d=0)]),
  dict(l='PaO₂', mods=[dict(when=O('alt'), d=-1), dict(when=LOWTOP + O('anemia', 'cn'), d=0)]),
  dict(l='O₂ content', mods=[dict(when=LOWTOP + O('anemia'), d=-1), dict(when=O('poly'), d=1), dict(when=O('cn'), d=0)]),
  dict(l='O₂ unloading', mods=[dict(when=RIGHT, d=1), dict(when=LEFT + LOWTOP, d=-1)]),
]

notes = {
  '': 'Hemoglobin binds O₂ cooperatively, so the curve is sigmoid. O₂ content = 1.34 × Hb × SaO₂ + 0.003 × PaO₂. Blood loads '
      'near full in the lungs and gives some up in the tissues; shifts match unloading to what the tissue needs.',
  'sh:exer': 'Exercise shifts the curve right (↓ affinity, ↑ P50): more O₂ is unloaded to the working muscle.',
  'sh:acid': 'Bohr effect: ↑ H⁺ and CO₂ (↓ pH) shift the curve right — more unloading where metabolism is high.',
  'sh:fever': '↑ temperature shifts the curve right.',
  'sh:alt': 'High altitude: inspired PO₂ falls (hypoxemia, normal A–a gradient). Over time ↑ 2,3-BPG shifts the curve right and ↑ '
            'erythropoietin raises hemoglobin.',
  'sh:cold': '↓ temperature shifts the curve left (↑ affinity).',
  'sh:hbf': 'Fetal hemoglobin (α₂γ₂) binds 2,3-BPG poorly, so it has a higher affinity than HbA — left-shifted — and pulls O₂ across '
            'the placenta.',
  'sh:myo': 'Myoglobin is a single chain: it binds O₂ more tightly and its curve is not sigmoid.',
  'sh:co': 'CO binds hemoglobin with >200× the affinity of O₂: it removes carrying capacity and left-shifts the remaining hemes. '
           'Normal PaO₂, low SaO₂ on co-oximetry — the pulse oximeter reads falsely normal. 100% O₂, hyperbaric if severe.',
  'sh:metb': 'Methemoglobin (Fe³⁺) cannot bind O₂ and left-shifts the remaining hemes. Cyanosis that O₂ doesn’t fix, chocolate-brown '
             'blood, normal PaO₂. Nitrites, dapsone, benzocaine. Methylene blue.',
  'sh:anemia': 'Anemia: less O₂ content with a normal SaO₂ and PaO₂ — the curve is the same, there is just less hemoglobin.',
  'sh:poly': 'Polycythemia: more O₂ content.',
  'sh:cn': 'Cyanide: content, saturation and PaO₂ all normal — the block is in the mitochondria (complex IV), not the blood.',
  'sh:sickle': 'Sickle cell: Glu6Val in β-globin. Deoxygenated HbS polymerizes and bends the cell; hypoxia, dehydration and acidosis '
               'promote sickling, HbF prevents it.',
}

dyn = dict(
  kinds=dict(o2=['o2', '--nf-blood']), groups=[['o2', 'Oxygen']],
  switches=[dict(id='sh', label='Shift · poison · disease', type='one', options=[
    ['exer', 'Exercise', 'odc'], ['acid', '↑ CO₂ / ↓ pH (Bohr)', 'odc'], ['fever', '↑ Temperature', 'odc'],
    ['alt', 'High altitude (↑ 2,3-BPG)', 'altitude'], ['cold', '↓ Temperature', 'odc'], ['hbf', 'Fetal hemoglobin', 'hbtypes'],
    ['myo', 'Myoglobin', 'odc'], ['co', 'Carbon monoxide', 'cohb'], ['metb', 'Methemoglobinemia', 'methb'],
    ['anemia', 'Anemia', 'odc'], ['poly', 'Polycythemia', 'odc'], ['cn', 'Cyanide', 'cyanide'], ['sickle', 'Sickle cell', 'sickle']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 687–689 · Costanzo ch 5 · Guyton ch 41')

MAP = dict(
  id='odcsim', title='The O₂ Curve in Motion', topic='pulmo', after='gasx',
  sub='Ride the hemoglobin dissociation curve from lungs to tissues and see how much O₂ is unloaded — shift it right with exercise, '
      'acid, fever and altitude, left with cold and fetal hemoglobin, and compare CO, methemoglobin, anemia, cyanide and sickle cell',
  w=3600, h=1900,
  fa='410, 416, 425, 428, 687, 688, 689, 691',
  src=['Costanzo ch 5 — Respiratory physiology', 'Guyton ch 41 — Transport of Oxygen and Carbon Dioxide in Blood and Tissue Fluids',
       'Robbins ch 14 — Red blood cell and bleeding disorders', 'Marks ch 6 — Amino Acids in Proteins',
       'Katzung ch 33 — Agents Used in Cytopenias; Hematopoietic Growth Factors', 'Costanzo ch 7 — Acid-base physiology',
       'Guyton ch 45 — Physiology of Deep-Sea Diving and Other Hyperbaric Conditions', 'Katzung ch 58 — Management of the Poisoned Patient',
       'Katzung ch 12 — Vasodilators & the Treatment of Angina Pectoris & Coronary Syndromes'],
  lanes=[('hbNorm', 'Oxygen transport', 'glycolysis'), ('hbPois', 'Poisons', 'tca'), ('hbType', 'Hemoglobin types & disease', 'gluconeo')],
  nodes=[
    ('hb1', 'O₂ content & the curve', 330, 1620, 'hbNorm', 'left is lower (P50)', ['odc'], 'hub'),
    ('hb2', 'High altitude', 760, 1620, 'hbNorm', '↑ 2,3-BPG, ↑ EPO', ['altitude']),
    ('hb3', 'Hemoglobin as a buffer', 1200, 1620, 'hbNorm', 'deoxyHb buffers better', ['intrabuffer']),
    ('hb4', 'CO poisoning', 1640, 1620, 'hbPois', 'pulse oximeter lies', ['cohb']),
    ('hb5', 'Methemoglobinemia', 2080, 1620, 'hbPois', 'chocolate-brown blood', ['methb']),
    ('hb6', 'Cyanide', 330, 1760, 'hbPois', 'complex IV', ['cyanide']),
    ('hb7', 'Hyperbaric oxygen', 760, 1760, 'hbPois', 'dissolved O₂ soars', ['hbo']),
    ('hb8', 'Hemoglobin types · HbF', 1200, 1760, 'hbType', 'α₂γ₂ left-shifted', ['hbtypes']),
    ('hb9', 'Sickle cell disease', 1640, 1760, 'hbType', 'Glu6Val', ['sickle'])],
  panels=[
    (2500, PANY, 1000, 'Which way does it shift? (First Aid p. 688)', [
      ('Right (↑ P50, ↑ unloading)', 'exercise, ↓ pH, ↑ CO₂, ↑ temp, ↑ 2,3-BPG'),
      ('Left (↓ P50)', '↓ temp, fetal Hb, CO, methemoglobin'),
      ('↓ SaO₂ + content, normal PaO₂', 'CO, methemoglobin'),
      ('↓ content only', 'anemia'),
      ('All normal', 'cyanide')])],
  dyn=dyn)
