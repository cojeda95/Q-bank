# Amyloid in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A precursor protein leaves its source cell, misfolds into a β-pleated sheet fibril and deposits in the organs that
# type of amyloid targets. One `one` switch (the amyloid type: AL, AA, β2-microglobulin, Aβ, calcitonin, amylin)
# changes the source cell, the particles and the organs lit up; a toggle (Congo red under polarized light) turns
# the deposit apple-green. 5 readouts. Facts from the pinned cards (amyloidosis, myeloma, acutephase, carpaltunnel,
# alzheimer, ich, medullary, t2dm, rcm, macroglos, nephrotic); their FA pages are in `fa`. No new cards.
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


SW = 'typ'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 700

# ════════ 1. the source cell ════════
box(160, 130, 760, 1180)
text('1 · The precursor', 190, 170, 'dyn-big')
text('where the protein is made', 190, 196, 'dyn-cap')
add('<ellipse cx="460" cy="560" rx="200" ry="150" class="dyn-cell"/>')
add('<circle cx="430" cy="560" r="56" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:3"/>')
SRC = dict(
  al=('Plasma cell (clonal)', 'immunoglobulin light chains', 'myeloma · MGUS'),
  aa=('Liver (acute-phase response)', 'serum amyloid A', 'RA · IBD · chronic infection · FMF'),
  b2m=('Long-term dialysis', 'β2-microglobulin', 'dialysis-related amyloid'),
  ab=('Neuron', 'amyloid β, cleaved from APP', 'APP gene is on chromosome 21'),
  cal=('Parafollicular C cell', 'calcitonin', 'medullary thyroid carcinoma'),
  amy=('Islet β cell', 'amylin, co-secreted with insulin', 'type 2 diabetes'),
)
for k, (a, b, c) in SRC.items():
    text(a, 460, 770, 'nf-l1', 'middle', when=O(k)); text(b, 460, 794, 'nf-l2', 'middle', when=O(k)); text(c, 460, 818, 'dyn-cap', 'middle', when=O(k))
text('pick an amyloid type', 460, 780, 'nf-l1', 'middle', unless=[f'{SW}:*'])

# ════════ 2. misfolding → β-pleated sheet fibril ════════
box(800, 130, 1380, 1180)
text('2 · Misfolding', 830, 170, 'dyn-big')
text('insoluble β-pleated sheets', 830, 196, 'dyn-cap')
zig = ' '.join(f'L{880 + i * 40} {500 + (0 if i % 2 else 40)}' for i in range(12))
for dy in (0, 70, 140):
    add(f'<path d="M880 {540 + dy} {zig.replace("500", str(500 + dy)).replace("540", str(540 + dy))}" style="fill:none;stroke:var(--dk11);stroke-width:5;stroke-linejoin:round"/>')
text('fibrils of stacked β strands', 1090, 760, 'nf-l1', 'middle')
# Congo red view
add('<circle cx="1090" cy="960" r="140" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>')
for i in range(5):
    y = 900 + i * 28
    add(f'<path d="M{990 + i * 6} {y} Q1090 {y - 26} {1190 - i * 6} {y}" style="fill:none;stroke:var(--bad);stroke-width:9;opacity:.55;stroke-linecap:round"/>', unless=['congo'])
    add(f'<path d="M{990 + i * 6} {y} Q1090 {y - 26} {1190 - i * 6} {y}" style="fill:none;stroke:var(--ok);stroke-width:9;stroke-linecap:round"/>', when=['congo'])
# UNVERIFIED: salmon-pink under ordinary light is standard teaching but not on the amyloidosis card
text('Congo red, ordinary light: salmon pink', 1090, 1130, 'nf-l2', 'middle', unless=['congo'])
text('polarized light: apple-green birefringence', 1090, 1130, 'nf-l1', 'middle', when=['congo'])

# ════════ 3. where it deposits ════════
box(1420, 130, 2340, 1180)
text('3 · Where it deposits', 1450, 170, 'dyn-big')
ORG = [('kid', 'Kidney', 'mesangium → nephrotic syndrome'), ('hrt', 'Heart', 'restrictive · low-voltage ECG'),
       ('tng', 'Tongue', 'macroglossia'), ('nrv', 'Median nerve', 'carpal tunnel · neuropathy'),
       ('brn', 'Brain', 'plaques · lobar hemorrhage'), ('thy', 'Thyroid', 'amyloid stroma of the tumor'),
       ('isl', 'Pancreatic islet', 'islet amyloid')]
HIT = dict(al=['kid', 'hrt', 'tng', 'nrv'], aa=['kid'], b2m=['nrv'], ab=['brn'], cal=['thy'], amy=['isl'])
OY = {o[0]: 250 + i * 130 for i, o in enumerate(ORG)}
for k, lab, sub in ORG:
    y = OY[k]; who = [t for t, hs in HIT.items() if k in hs]
    add(f'<rect x="1700" y="{y - 40}" width="600" height="80" rx="14" class="dyn-soft"/>')
    add(f'<rect x="1700" y="{y - 40}" width="600" height="80" rx="14" style="fill:var(--accent);fill-opacity:.14;stroke:var(--accent);stroke-width:4"/>', when=O(*who))
    text(lab, 1730, y - 4, 'nf-l1'); text(sub, 1730, y + 20, 'nf-l2')
    add(f'<rect x="1700" y="{y - 40}" width="600" height="80" rx="14" style="fill:var(--surface);fill-opacity:.55;stroke:none"/>', when=[f'{SW}:{t}' for t in HIT if k not in HIT[t]])

# ════════ motion ════════
flows = [dict(d='M640 560 H880', len=240, speed=90, r=8, base=dict(), mods=[dict(when=O(*SRC), set=dict(prot=4))])]
for t, hs in HIT.items():
    for k in hs:
        y = OY[k]
        flows.append(dict(d=f'M1340 680 C1500 680 1560 {y} 1700 {y}', len=round(380 + abs(y - 680) * 0.8), speed=110, r=8,
                          base=dict(fib=3), when=O(t)))

sites = [
  dict(x=460, y=410, n=[0, -1], w=40, t='rec', l='', aria='The precursor protein', c='amyloidosis', ions=[]),
  dict(x=1090, y=820, n=[0, -1], w=40, t='rec', l='', aria='Congo red stain', c='amyloidosis', ions=[]),
]

# ════════ readouts ════════
readouts = [
  dict(l='Serum light chains (κ or λ)', mods=[dict(when=O('al'), d=1)]),
  dict(l='Serum amyloid A · CRP', mods=[dict(when=O('aa'), d=1)]),
  dict(l='Urine protein', mods=[dict(when=O('al', 'aa'), d=1)]),
  dict(l='ECG voltage', mods=[dict(when=O('al'), d=-1)]),
  dict(l='Calcitonin', mods=[dict(when=O('cal'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Amyloid is any protein that misfolds into insoluble β-pleated sheets and deposits in tissue. The type is named for the '
      'precursor, and the precursor decides which organs fill up. Congo red shows it.',
  'typ:al': 'AL amyloid comes from immunoglobulin light chains made by a clonal plasma cell (myeloma, MGUS): nephrotic syndrome, '
            'restrictive cardiomyopathy with a low-voltage ECG, macroglossia, carpal tunnel and neuropathy.',
  'typ:aa': 'AA amyloid comes from serum amyloid A, an acute-phase reactant, in chronic inflammation — RA, IBD, chronic infection, '
            'familial Mediterranean fever. The kidney is the organ most often involved.',
  'typ:b2m': 'Dialysis-related amyloid is made of β2-microglobulin; long-term dialysis is a cause of carpal tunnel syndrome.',
  'typ:ab': 'Amyloid β, cleaved from APP, forms the extracellular plaques of Alzheimer disease; in vessel walls it causes cerebral '
            'amyloid angiopathy — recurrent lobar hemorrhages in older adults.',
  'typ:cal': 'Medullary thyroid carcinoma: the C cells’ calcitonin forms amyloid in the tumor stroma, which stains with Congo red. '
             'Serum calcitonin rises.',
  'typ:amy': 'In type 2 diabetes, amylin co-secreted with insulin deposits as islet amyloid as the β cells fail.',
  'congo': 'Congo red–stained amyloid shows apple-green birefringence under polarized light — the diagnostic stain.',
}

dyn = dict(
  kinds=dict(prot=['prot', '--dk9'], fib=['prot', '--dk11']), groups=[['prot', 'Protein']],
  switches=[dict(id=SW, label='Amyloid type', type='one', options=[
    ['al', 'AL — light chains', 'amyloidosis'], ['aa', 'AA — serum amyloid A', 'amyloidosis'], ['b2m', 'β2-microglobulin — dialysis', 'carpaltunnel'],
    ['ab', 'Aβ — Alzheimer', 'alzheimer'], ['cal', 'Calcitonin — medullary thyroid', 'medullary'], ['amy', 'Amylin — type 2 diabetes', 't2dm']]),
    dict(id='congo', label='Stain', type='toggle', on='Polarized light', off='Ordinary light', **{'def': False})],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 208, 315, 345, 351, 436, 453, 528, 534 · Robbins ch 6')

MAP = dict(
  id='amylsim', title='Amyloid in Motion', topic='path', after='genpath',
  sub='A precursor protein misfolds into β-pleated sheets and deposits where its type goes — pick AL, AA, β2-microglobulin, '
      'Aβ, calcitonin or amylin to see the source cell and the organs fill, and turn on polarized light for apple-green birefringence',
  w=3500, h=1560,
  fa='106, 208–209, 315, 345, 351, 356, 436, 453, 463, 528, 534, 613',
  src=[full('Robbins', 6), full('Robbins', 20), full('Robbins', 13), full('Robbins', 12), full('Robbins', 28), full('Robbins', 24)],
  lanes=[('amSys', 'Systemic amyloid', 'glycolysis'), ('amLoc', 'Localized amyloid', 'tca'), ('amOrg', 'Organ damage', 'gluconeo')],
  nodes=[
    ('am1', 'Amyloidosis', 330, 1300, 'amSys', 'AL · AA · Congo red', ['amyloidosis'], 'hub'),
    ('am2', 'Multiple myeloma', 760, 1300, 'amSys', 'light chains', ['myeloma']),
    ('am3', 'Acute-phase response', 1180, 1300, 'amSys', 'serum amyloid A', ['acutephase']),
    ('am4', 'Alzheimer · amyloid angiopathy', 1640, 1300, 'amLoc', 'Aβ', ['alzheimer', 'ich']),
    ('am5', 'Medullary thyroid carcinoma', 2120, 1300, 'amLoc', 'calcitonin', ['medullary']),
    ('am6', 'Type 2 diabetes', 330, 1430, 'amLoc', 'islet amylin', ['t2dm']),
    ('am7', 'Restrictive cardiomyopathy', 780, 1430, 'amOrg', 'low-voltage ECG', ['rcm']),
    ('am8', 'Nephrotic syndrome', 1220, 1430, 'amOrg', 'mesangial deposits', ['nephrotic']),
    ('am9', 'Carpal tunnel · macroglossia', 1660, 1430, 'amOrg', 'dialysis · AL', ['carpaltunnel', 'macroglos'])],
  panels=[
    (2420, PANY, 1000, 'Precursor → disease (cards)', [
      ('Light chains (AL)', 'myeloma, MGUS'),
      ('Serum amyloid A (AA)', 'chronic inflammation'),
      ('β2-microglobulin', 'long-term dialysis'),
      ('Amyloid β', 'Alzheimer · amyloid angiopathy'),
      ('Calcitonin', 'medullary thyroid carcinoma'),
      ('Amylin', 'type 2 diabetes islets')])],
  dyn=dyn)
