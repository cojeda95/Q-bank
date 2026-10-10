# Myeloid Neoplasms in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A marrow with one stem cell feeding three lanes — red cells (EPO → JAK2), the granulocyte ladder (myeloblast →
# promyelocyte → maturing granulocytes → neutrophil) and platelets (TPO → JAK2) — into the blood, with the spleen beside it.
# A `one` switch breaks it: AML (blasts ≥ 20%, maturation blocked), APL (stalled promyelocytes, DIC), MDS (full marrow, few
# cells out), CML (BCR-ABL, too many granulocytes, big spleen), CML blast crisis, polycythemia vera, essential
# thrombocythemia, myelofibrosis and Langerhans cell histiocytosis. A `drug` toggle gives each one's card-stated treatment
# (cytarabine + anthracycline, ATRA + arsenic, imatinib, ruxolitinib). Intermediate granulocyte stages are not named
# because no card names them. 6 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
def DR(k, on=True): return [f'dx:{k}&{"" if on else "!"}drug']
PANY = 1180
STEM = (300, 680)
def cell(x, y, r, col, when=None, unless=None, dash=False):
    st = f'fill:var({col});fill-opacity:.35;stroke:var({col});stroke-width:4' + (';stroke-dasharray:6 6' if dash else '')
    add(f'<circle cx="{x}" cy="{y}" r="{r}" style="{st}"/>', when=when, unless=unless)

text('Myeloid neoplasms — where the marrow’s output goes wrong', 180, 150, 'dyn-big')
text('one stem cell, three lanes, into the blood · pick a disease, then give its drug', 180, 176, 'dyn-cap')

# ════════ marrow ════════
add('<rect x="180" y="260" width="1340" height="860" rx="40" style="fill:var(--dk5);fill-opacity:.06;stroke:var(--dk5);stroke-width:5"/>')
text('bone marrow', 220, 300, 'nf-l1')
cell(*STEM, 46, '--dk7'); text('stem cell', STEM[0], STEM[1] + 80, 'nf-l2', 'middle')
add('<path d="M340 650 C420 520 500 420 600 420 H1500" style="fill:none;stroke:var(--nf-blood);stroke-width:5;opacity:.4"/>')
add('<path d="M340 710 C420 840 500 960 600 960 H1500" style="fill:none;stroke:var(--dk9);stroke-width:5;opacity:.4"/>')
add('<path d="M346 680 H1500" style="fill:none;stroke:var(--dk4);stroke-width:5;opacity:.4"/>')
text('red cells — EPO → JAK2', 640, 396, 'nf-l2'); text('platelets — TPO → JAK2', 640, 1000, 'nf-l2')
GL = [(560, 'myeloblast'), (820, 'promyelocyte'), (1080, 'maturing'), (1340, 'neutrophil')]
for x, l in GL:
    cell(x, 680, 34, '--dk4'); text(l, x, 740, 'nf-l2', 'middle')
# blocks
for i in range(7):
    cell(500 + (i % 4) * 40, 600 - (i // 4) * 50, 22, '--bad', when=D('aml', 'blast'), unless=['dx:aml&drug'])
for i in range(7):
    cell(760 + (i % 4) * 40, 600 - (i // 4) * 50, 22, '--bad', when=DR('apl', False))
text('maturation blocked — blasts pile up', 640, 520, 'nf-l1 dyn-tag', 'middle', when=D('aml'), unless=['dx:aml&drug'])
text('stalled as promyelocytes — granules full of procoagulant → DIC', 820, 520, 'nf-l1 dyn-tag', 'middle', when=DR('apl', False))
text('ATRA + arsenic: promyelocytes mature into neutrophils', 820, 520, 'nf-l1 dyn-tag', 'middle', when=DR('apl'))
text('blast crisis — AML or ALL', 640, 520, 'nf-l1 dyn-tag', 'middle', when=D('blast'))
text('full marrow, daughters die before release — fewer than 20% blasts', 850, 1080, 'nf-l1 dyn-tag', 'middle', when=D('mds'))
for x in (620, 900, 1180):
    add(f'<path d="M{x - 20} {660} l40 40 M{x + 20} {660} l-40 40" class="nf-x"/>', when=D('mds'))
text('BCR-ABL kinase always on — t(9;22)', 1210, 620, 'nf-l1 dyn-tag', 'middle', when=DR('cml', False))
text('imatinib switches the kinase off', 1210, 620, 'nf-l1 dyn-tag', 'middle', when=DR('cml'))
text('JAK2 V617F — on without EPO', 1000, 360, 'nf-l1 dyn-tag', 'middle', when=D('pv'))
text('JAK2 on without TPO', 1000, 1050, 'nf-l1 dyn-tag', 'middle', when=D('et'))
for i in range(9):
    add(f'<path d="M{260 + i * 140} 300 l100 780" style="stroke:var(--ink-3);stroke-width:3;opacity:.5"/>', when=D('mf'))
text('fibrosis — dry tap', 850, 1080, 'nf-l1 dyn-tag', 'middle', when=D('mf'))

# ════════ blood + spleen ════════
add('<path d="M1600 300 V1100" style="stroke:var(--nf-blood);stroke-width:90;opacity:.12;stroke-linecap:round"/>')
text('blood', 1600, 270, 'nf-l1', 'middle')
add('<ellipse cx="2050" cy="700" rx="120" ry="80" style="fill:var(--dk10);fill-opacity:.25;stroke:var(--dk10);stroke-width:4"/>', unless=D('cml', 'mf', 'blast'))
add('<ellipse cx="2050" cy="700" rx="230" ry="160" style="fill:var(--dk10);fill-opacity:.25;stroke:var(--bad);stroke-width:5"/>', when=D('cml', 'mf', 'blast'))
text('spleen', 2050, 900, 'nf-l1', 'middle')
text('Auer rods (MPO ⊕) in the blasts', 1600, 1180, 'nf-l1', 'middle', when=D('aml', 'apl'))
text('DIC — low fibrinogen, long PT and PTT', 1600, 1220, 'nf-l1 dyn-tag', 'middle', when=DR('apl', False))
text('bilobed (duet) neutrophils — pseudo-Pelger-Huët', 1600, 1180, 'nf-l1', 'middle', when=D('mds'))
text('basophilia · low LAP score', 1600, 1180, 'nf-l1', 'middle', when=D('cml'))
text('teardrop cells', 1600, 1180, 'nf-l1', 'middle', when=D('mf'))
text('high hematocrit, low EPO · itch after a warm shower', 1600, 1180, 'nf-l1', 'middle', when=D('pv'))
text('bleeding and thrombosis', 1600, 1180, 'nf-l1', 'middle', when=D('et'))
# LCH
add('<path d="M2000 1000 C2000 940 2200 940 2200 1000 V1080 H2000 Z" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:4"/>')
text('skull & skin', 2100, 1110, 'nf-l2', 'middle')
add('<circle cx="2100" cy="990" r="22" style="fill:var(--surface);stroke:var(--bad);stroke-width:4"/>', when=D('lch'))
text('lytic lesion — Langerhans cells, CD1a ⊕, S-100 ⊕, Birbeck granules', 2100, 920, 'nf-l1 dyn-tag', 'middle', when=D('lch'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
LOW = D('aml', 'apl', 'mds', 'blast', 'mf')
flows = [
  dict(d='M340 650 C420 520 500 420 600 420 H1580', len=1300, speed=120, r=8, base=dict(rbc=3),
       mods=[m(LOW, set=dict(rbc=1)), m(D('pv'), set=dict(rbc=8)), m(['dx:pv&drug', 'dx:aml&drug'], set=dict(rbc=3))]),
  dict(d='M340 710 C420 840 500 960 600 960 H1580', len=1300, speed=120, r=7, base=dict(plt=3),
       mods=[m(LOW, set=dict(plt=1)), m(D('et'), set=dict(plt=8)), m(['dx:aml&drug'], set=dict(plt=3))]),
  dict(d='M346 680 H1580', len=1240, speed=120, r=8, base=dict(neu=3),
       mods=[m(D('aml', 'blast', 'mds', 'mf'), set=dict(neu=1)), m(DR('apl', False), set=dict(neu=0)), m(DR('apl'), set=dict(neu=5)),
             m(D('cml'), set=dict(neu=9)), m(['dx:cml&drug', 'dx:aml&drug'], set=dict(neu=3))]),
  dict(d='M600 600 C900 560 1300 560 1580 600', len=1000, speed=100, r=9, base=dict(blast=6), when=D('aml', 'blast'), unless=['dx:aml&drug']),
]
sites = [dict(x=560, y=780, n=[0, 1], w=10, t='rec', l='', aria='AML', c='aml', ions=[]),
         dict(x=820, y=780, n=[0, 1], w=10, t='rec', l='', aria='APL', c='apl', ions=[]),
         dict(x=300, y=600, n=[0, -1], w=10, t='rec', l='', aria='Myelodysplastic syndromes', c='mds', ions=[]),
         dict(x=1340, y=780, n=[0, 1], w=10, t='rec', l='', aria='CML', c='cml', ions=[]),
         dict(x=1500, y=420, n=[0, -1], w=10, t='rec', l='', aria='JAK2 neoplasms', c='jak2', ions=[]),
         dict(x=2200, y=1040, n=[1, 0], w=10, t='rec', l='', aria='Langerhans cell histiocytosis', c='lch', ions=[])]

readouts = [
  dict(l='Blasts in blood', mods=[dict(when=D('aml', 'blast'), d=1), dict(when=['dx:aml&drug'], d=-1)]),
  dict(l='Neutrophils', mods=[dict(when=D('aml', 'blast', 'mds'), d=-1), dict(when=DR('apl', False), d=-1), dict(when=DR('cml', False), d=1)]),
  dict(l='Hematocrit', mods=[dict(when=D('aml', 'apl', 'mds', 'blast'), d=-1), dict(when=DR('pv', False), d=1)]),
  dict(l='Platelets', mods=[dict(when=D('aml', 'apl', 'mds', 'blast'), d=-1), dict(when=D('et'), d=1)]),
  dict(l='Spleen size', mods=[dict(when=D('cml', 'mf', 'blast'), d=1)]),
  dict(l='DIC', mods=[dict(when=DR('apl', False), d=1)]),
]

notes = {
  '': 'One stem cell feeds three lanes: red cells and platelets (EPO and TPO signal through JAK2) and the granulocyte ladder from '
      'myeloblast to neutrophil. Pick a disease to see which lane fails or floods.',
  'dx:aml': 'AML: mutations block maturation; myeloblasts fill the marrow (≥ 20%) and spill into the blood, crowding out red '
            'cells, neutrophils and platelets. MPO ⊕, TdT ⊝, Auer rods. Median onset ≈ 65.',
  'dx:apl': 'APL: t(15;17) PML-RARα keeps maturation genes off — cells stall as promyelocytes packed with Auer rods; their '
            'procoagulant granules set off DIC.',
  'dx:mds': 'MDS: a clone fills the marrow but its daughters mature badly and die before release — cytopenias with a cellular '
            'marrow, fewer than 20% blasts; pseudo-Pelger-Huët cells, ringed sideroblasts; risk of AML.',
  'dx:cml': 'CML: t(9;22) BCR-ABL kinase always on — mature and maturing granulocytes, basophilia, splenomegaly, low LAP score.',
  'dx:blast': 'Untreated CML progresses to blast crisis — AML or ALL.',
  'dx:pv': 'Polycythemia vera: JAK2 V617F (> 95%) turns JAK2 on without EPO — high hematocrit with low EPO, itching after a warm '
           'shower, erythromelalgia, Budd-Chiari, DVT/PE.',
  'dx:et': 'Essential thrombocythemia: JAK2-driven platelet excess — bleeding and thrombosis.',
  'dx:mf': 'Myelofibrosis: teardrop cells, dry tap, massive splenomegaly.',
  'dx:lch': 'Langerhans cell histiocytosis: a clone of immature Langerhans (dendritic) cells, often BRAF V600E — child with lytic '
            'skull lesions and rash; S-100 ⊕, CD1a ⊕, Birbeck granules (tennis rackets).',
  'drug': 'Treatment from the cards — AML: cytarabine + an anthracycline · APL: all-trans retinoic acid + arsenic trioxide '
          '(differentiation) · CML: imatinib · PV: phlebotomy, hydroxyurea, ruxolitinib.',
}

dyn = dict(
  kinds=dict(rbc=['mov', '--nf-blood'], plt=['mov', '--dk9'], neu=['mov', '--dk4'], blast=['mov', '--bad']),
  groups=[['mov', 'Red cells · platelets · neutrophils · blasts']],
  switches=[dict(id='dx', label='Disease', type='one', options=[
              ['aml', 'AML', 'aml'], ['apl', 'APL t(15;17)', 'apl'], ['mds', 'MDS', 'mds'], ['cml', 'CML t(9;22)', 'cml'],
              ['blast', 'CML blast crisis', 'cml'], ['pv', 'Polycythemia vera', 'jak2'], ['et', 'Essential thrombocythemia', 'jak2'],
              ['mf', 'Myelofibrosis', 'jak2'], ['lch', 'Langerhans cell histiocytosis', 'lch']]),
            dict(id='drug', label='Treat', type='toggle', on='Drug given', off='Give the drug', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 13')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='myelsim', title='Myeloid Neoplasms in Motion', topic='heme', after='hemeonc',
  sub='Watch one marrow stem cell feed red cells, granulocytes and platelets into the blood — then block it (AML, APL, MDS), flood '
      'it (CML, polycythemia vera, thrombocythemia), scar it (myelofibrosis) and give each disease its drug',
  w=3600, h=1900,
  fa='436, 437, 438, 439, 440, 447',
  src=['Robbins ch 13 — Diseases of white blood cells, lymph nodes, spleen, and thymus', 'Katzung ch 54 — Cancer Chemotherapy'],
  lanes=[('myAcute', 'Acute & dysplastic', 'tca'), ('myMpn', 'Myeloproliferative & histiocytic', 'glycolysis')],
  nodes=[
    ('my1', 'AML', 330, 1660, 'myAcute', '≥ 20% blasts · Auer rods', ['aml'], 'hub'),
    ('my2', 'APL', 760, 1660, 'myAcute', 't(15;17) · DIC · ATRA', ['apl']),
    ('my3', 'Myelodysplastic syndromes', 1200, 1660, 'myAcute', '< 20% blasts', ['mds']),
    ('my4', 'CML & BCR-ABL inhibitors', 1640, 1660, 'myMpn', 't(9;22) · imatinib', ['cml']),
    ('my5', 'JAK2 V617F neoplasms', 2080, 1660, 'myMpn', 'PV · ET · myelofibrosis', ['jak2']),
    ('my6', 'Langerhans cell histiocytosis', 2520, 1660, 'myMpn', 'Birbeck granules', ['lch'])],
  panels=[
    (2500, PANY, 1000, 'Marker → disease (Robbins ch 13)', [
      ('t(15;17) PML-RARα', 'APL'), ('t(9;22) BCR-ABL', 'CML'), ('JAK2 V617F', 'PV, ET, myelofibrosis'),
      ('Blasts ≥ 20%', 'AML (< 20%: MDS)'), ('CD1a, S-100', 'LCH')])],
  dyn=dyn)
