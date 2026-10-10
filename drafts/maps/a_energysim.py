# Energy Metabolism in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Glucose runs down glycolysis in the cytosol, pyruvate enters the mitochondrion through PDH, turns the TCA cycle, and
# NADH feeds complexes I–IV, which pump H⁺ out; H⁺ returns through ATP synthase (V). One `one` switch drops a
# poison or deficiency on its step (pyruvate kinase, PDH deficiency, thiamine, arsenic, fluoroacetate, rotenone,
# antimycin, cyanide, CO, oligomycin, an uncoupler): ✕ on the target, flow stops or reroutes to lactate, protons
# stop or leak. 6 readouts. Facts from the pinned cards (etcinhib, uncoupler, cyanide, cohb, arsenic, fluoroacetate,
# pdhdef, thiamine, pkdef, lacticmech, mito); FA pages in `fa`. No new cards.
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
SW = 'blk'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 760
ETC = ['rot', 'anti', 'cn', 'co', 'oligo']
PDHB = ['pdh', 'thia', 'ars']
DOWN = PDHB + ['fluoro'] + ETC          # anything that backs pyruvate up into lactate

text('Fuel to ATP — where each poison hits', 180, 150, 'dyn-big')
text('glycolysis in the cytosol, then PDH, the TCA cycle and the electron transport chain in the mitochondrion', 180, 176, 'dyn-cap')

# ════════ cytosol: glycolysis ════════
box(160, 210, 900, 1220)
text('Cytosol', 190, 250, 'nf-l1')
GL = [('Glucose', 300), ('Glucose-6-P', 420), ('Fructose-1,6-BP', 540), ('Glyceraldehyde-3-P', 660), ('PEP', 780), ('Pyruvate', 920)]
for lab, y in GL:
    add(f'<rect x="420" y="{y - 24}" width="300" height="48" rx="24" class="dyn-soft"/>')
    text(lab, 570, y + 6, 'nf-l1', 'middle')
add('<rect x="200" y="1076" width="200" height="48" rx="24" class="dyn-soft"/>')
text('Lactate', 300, 1100, 'nf-l1', 'middle')
text('LDH', 400, 1030, 'nf-l2')
add('<path d="M480 945 L330 1074" class="dyn-line"/>')
text('ATP made here (no O₂ needed)', 600, 860, 'nf-l2')

# ════════ mitochondrion ════════
add('<rect x="940" y="210" width="1400" height="1010" rx="120" style="fill:var(--dk3);fill-opacity:.06;stroke:var(--dk3);stroke-width:6"/>')
add('<path d="M2040 260 V1170" style="stroke:var(--dk3);stroke-width:22;stroke-linecap:round;opacity:.55"/>')
text('Mitochondrial matrix', 980, 250, 'nf-l1')
text('inner membrane', 2040, 1205, 'nf-l2', 'middle')
text('H⁺ outside', 2200, 250, 'nf-l1', 'middle')
# PDH + acetyl-CoA
add('<rect x="980" y="896" width="230" height="48" rx="24" class="dyn-soft"/>')
text('Acetyl-CoA', 1095, 926, 'nf-l1', 'middle')
add('<path d="M720 920 H980" class="dyn-line"/>')
# TCA circle
TX, TY, TR = 1480, 640, 220
add(f'<circle cx="{TX}" cy="{TY}" r="{TR}" style="fill:none;stroke:var(--dk2);stroke-width:5;stroke-dasharray:14 8"/>')
text('TCA cycle', TX, TY + 6, 'dyn-big', 'middle')
for ang, lab in ((200, 'Citrate'), (250, 'Isocitrate'), (320, 'α-Ketoglutarate'), (20, 'Succinyl-CoA'), (110, 'Oxaloacetate')):
    x = TX + TR * math.cos(math.radians(ang)); y = TY + TR * math.sin(math.radians(ang))
    add(f'<circle cx="{round(x)}" cy="{round(y)}" r="10" style="fill:var(--dk2)"/>')
    dx = -16 if 90 < ang < 270 else 16
    text(lab, round(x + dx), round(y - 14), 'nf-l2', 'end' if dx < 0 else 'start')
add(f'<path d="M1210 900 Q1260 820 {TX - TR + 10} {TY + 60}" class="dyn-line"/>')
# ETC labels on the membrane
CX = dict(I=360, III=560, IV=760, V=1000)
for k, y in CX.items():
    text('ATP synthase (V)' if k == 'V' else f'Complex {k}', 1990, y + 6, 'nf-l1', 'end')
text('O₂ → H₂O', 1880, CX['IV'] + 50, 'nf-l2', 'end')
text('ADP → ATP', 1880, CX['V'] + 50, 'nf-l2', 'end')

# ✕ marks and tags for each block
def X(cx, cy, s=22): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
add(X(840, 850), when=O('pk'))
text('pyruvate kinase deficiency — red cells run out of ATP', 600, 1180, 'nf-l1 dyn-tag', 'middle', when=O('pk'))
add(X(850, 920), when=O(*PDHB))
TAG = dict(pdh='PDH deficiency — pyruvate can’t enter: lactate and alanine pile up',
           thia='no thiamine (TPP) — PDH and α-KG dehydrogenase stall',
           ars='arsenic binds lipoic acid — PDH and α-KG dehydrogenase stall',
           fluoro='fluoroacetate → fluorocitrate blocks aconitase — citrate piles up',
           rot='rotenone blocks complex I', anti='antimycin blocks complex III',
           cn='cyanide blocks complex IV — O₂ present but unusable', co='CO blocks complex IV and grabs hemoglobin',
           oligo='oligomycin blocks ATP synthase', unc='uncoupler: H⁺ leaks back without ATP synthase — energy leaves as heat')
for k, t in TAG.items():
    if k in ('pk',): continue
    text(t, 1500, 1170, 'nf-l1 dyn-tag', 'middle', when=O(k))
akx, aky = TX + TR * math.cos(math.radians(320)), TY + TR * math.sin(math.radians(320))
add(X(round(akx) + 30, round(aky) + 30, 16), when=O('thia', 'ars'))
add(X(TX + round(TR * math.cos(math.radians(225))), TY + round(TR * math.sin(math.radians(225))), 18), when=O('fluoro'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M570 324 V756', len=432, speed=110, r=7, base=dict(glc=6)),
  dict(d='M570 804 V896', len=92, speed=80, r=7, base=dict(glc=2), mods=[m(O('pk'), set=dict(glc=0))]),
  dict(d='M480 945 L330 1074', len=200, speed=70, r=7, base=dict(lac=1), mods=[m(O(*DOWN), set=dict(lac=6))]),
  dict(d='M720 920 H980', len=260, speed=110, r=7, base=dict(glc=3), mods=[m(O(*PDHB), set=dict(glc=0)), m(O(*ETC, 'fluoro'), set=dict(glc=1))]),
  dict(d=f'M{TX - TR} {TY} A{TR} {TR} 0 1 1 {TX + TR} {TY} A{TR} {TR} 0 1 1 {TX - TR} {TY}', len=round(2 * math.pi * TR), speed=120, r=7,
       base=dict(tca=8), mods=[m(O(*PDHB), set=dict(tca=1)), m(O('fluoro'), set=dict(tca=0)), m(O(*ETC), set=dict(tca=2)), m(O('unc'), set=dict(tca=12))]),
  dict(d=f'M{TX + 120} {TY - 180} C1800 260 1900 300 2025 {CX["I"]}', len=600, speed=110, r=7, base=dict(nadh=4),
       mods=[m(O(*PDHB, 'fluoro'), set=dict(nadh=1)), m(O(*ETC), set=dict(nadh=1)), m(O('unc'), set=dict(nadh=7))]),
  dict(d=f'M1700 {CX["IV"] + 40} H2020', len=320, speed=90, r=7, base=dict(o2=3), mods=[m(O(*ETC), set=dict(o2=0)), m(O('unc'), set=dict(o2=7))]),
  dict(d=f'M2030 {CX["V"] + 30} H1700', len=330, speed=90, r=8, base=dict(atp=4), mods=[m(O(*ETC, 'unc'), set=dict(atp=0))]),
  dict(d='M2060 640 C2160 640 2200 760 2300 860', len=320, speed=120, r=8, base=dict(), when=O('unc'), mods=[m(O('unc'), set=dict(heat=6))]),
]

sites = [
  dict(x=2040, y=CX['I'], n=[1, 0], w=22, t='pump', l='', aria='Complex I', c='etcinhib', ions=[['h', 'out', 2]],
       block=O('rot'), stop=O('anti', 'cn', 'co', 'oligo')),
  dict(x=2040, y=CX['III'], n=[1, 0], w=22, t='pump', l='', aria='Complex III', c='etcinhib', ions=[['h', 'out', 2]],
       block=O('anti'), stop=O('rot', 'cn', 'co', 'oligo')),
  dict(x=2040, y=CX['IV'], n=[1, 0], w=22, t='pump', l='', aria='Complex IV — cytochrome c oxidase', c='cyanide', ions=[['h', 'out', 2]],
       block=O('cn', 'co'), stop=O('rot', 'anti', 'oligo')),
  dict(x=2040, y=CX['V'], n=[1, 0], w=22, t='ch', l='', aria='ATP synthase', c='etcinhib', ions=[['h', 'in', 3]],
       block=O('oligo'), stop=O('rot', 'anti', 'cn', 'co'), low=O('unc')),
  dict(x=2040, y=640, n=[1, 0], w=22, t='para', l='', aria='Uncoupler — proton leak', c='uncoupler', ions=[['h', 'in', 4]], when=O('unc')),
  dict(x=1095, y=880, n=[0, -1], w=40, t='md', l='', aria='Pyruvate dehydrogenase', c='pdhdef', ions=[], block=O(*PDHB)),
]

# ════════ readouts ════════
readouts = [
  dict(l='Lactate', mods=[dict(when=O(*DOWN), d=1)]),
  dict(l='O₂ consumption', mods=[dict(when=O(*ETC), d=-1), dict(when=O('unc'), d=1)]),
  dict(l='ATP', mods=[dict(when=O('pk', 'ars', *ETC, 'unc'), d=-1)]),
  dict(l='Venous O₂ saturation', mods=[dict(when=O('cn'), d=1)]),
  dict(l='Body temperature', mods=[dict(when=O('unc'), d=1)]),
  dict(l='Citrate', mods=[dict(when=O('fluoro'), d=1)]),
]

notes = {
  '': 'Glycolysis makes a little ATP without oxygen; pyruvate then enters the mitochondrion through PDH, turns the TCA cycle, and '
      'NADH drives complexes I–IV to pump H⁺ out. H⁺ flowing back through ATP synthase makes most of the ATP.',
  'blk:pk': 'Pyruvate kinase deficiency: red cells have no mitochondria and depend on glycolytic ATP, so losing the last ATP-making '
            'step leaves rigid cells the spleen removes — chronic hemolysis; 2,3-BPG builds up and right-shifts the O₂ curve.',
  'blk:pdh': 'PDH deficiency (X-linked): pyruvate can’t enter the TCA cycle, so it becomes lactate and alanine — infant neurologic '
             'impairment with an anion-gap lactic acidosis. Ketogenic diet; thiamine, lipoic acid.',
  'blk:thia': 'Thiamine (TPP) is the cofactor for PDH and α-ketoglutarate dehydrogenase (and transketolase). Brain and heart fail '
              'first — Wernicke, beriberi; pyruvate and lactate rise. Give thiamine before glucose.',
  'blk:ars': 'Arsenite binds lipoic acid and stalls PDH and α-ketoglutarate dehydrogenase; arsenate also robs the GAPDH step of its '
             'ATP. Garlic breath, rice-water diarrhea; lactate and pyruvate rise. Dimercaprol or succimer.',
  'blk:fluoro': 'Fluoroacetate is made into fluorocitrate, which blocks aconitase — the cycle stops one step past citrate. Citrate '
                'piles up (chelating calcium), with lactic acidosis, seizures and arrhythmias.',
  'blk:rot': 'Rotenone blocks complex I: no electron flow, no proton pumping, no ATP; O₂ use falls and cells fall back on '
             'anaerobic glycolysis — lactic acidosis.',
  'blk:anti': 'Antimycin blocks complex III — the same picture: the gradient collapses, ATP synthesis stops, O₂ consumption falls, '
              'lactate rises.',
  'blk:cn': 'Cyanide binds complex IV: oxygen is there but can’t be used, so venous blood stays oxygenated, with severe anion-gap '
            'lactic acidosis. Hydroxocobalamin first; nitrites plus thiosulfate.',
  'blk:co': 'Carbon monoxide blocks complex IV and binds hemoglobin over 200 times more tightly than O₂ — normal PaO₂, falsely normal '
            'pulse oximetry, high carboxyhemoglobin on co-oximetry. 100% or hyperbaric O₂.',
  'blk:oligo': 'Oligomycin blocks ATP synthase (complex V) directly: protons can’t return, so the chain backs up, O₂ use falls and '
               'ATP stops.',
  'blk:unc': 'Uncouplers (2,4-dinitrophenol, aspirin overdose, thermogenin in brown fat) let H⁺ back in without ATP synthase: '
             'electron transport races and O₂ use rises, but the energy leaves as heat — hyperthermia, low ATP.',
}

dyn = dict(
  kinds=dict(glc=['fuel', '--nf-glu'], tca=['fuel', '--dk2'], nadh=['fuel', '--dk9'], lac=['fuel', '--dk5'], o2=['o2', '--dk1'],
             atp=['atp', '--ok'], heat=['atp', '--bad'], h=['h', '--nf-h']),
  groups=[['fuel', 'Fuel & NADH'], ['o2', 'Oxygen'], ['h', 'Protons'], ['atp', 'ATP & heat']],
  switches=[dict(id=SW, label='Poison or deficiency', type='one', options=[
    ['pk', 'Pyruvate kinase deficiency', 'pkdef'], ['pdh', 'PDH deficiency', 'pdhdef'], ['thia', 'Thiamine deficiency', 'thiamine'],
    ['ars', 'Arsenic', 'arsenic'], ['fluoro', 'Fluoroacetate', 'fluoroacetate'], ['rot', 'Rotenone (complex I)', 'etcinhib'],
    ['anti', 'Antimycin (complex III)', 'etcinhib'], ['cn', 'Cyanide (complex IV)', 'cyanide'], ['co', 'Carbon monoxide', 'cohb'],
    ['oligo', 'Oligomycin (ATP synthase)', 'etcinhib'], ['unc', 'Uncoupler (2,4-DNP)', 'uncoupler']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 64, 74–76, 428, 689 · Marks ch 22–24 · Katzung ch 58')

MAP = dict(
  id='energysim', title='Energy Metabolism in Motion', topic='bio', after='core',
  sub='Glucose to pyruvate, through PDH and the TCA cycle to the electron transport chain — drop a poison or deficiency on its step '
      'and watch the flow stop, lactate rise, protons stall or leak, and O₂ use, ATP and temperature move. Tap a complex for its card',
  w=3500, h=1560,
  fa='55, 64, 73–76, 247, 428, 689',
  src=[full('Marks', 22), full('Marks', 23), full('Marks', 24), full('Katzung', 58), full('Katzung', 57), full('Robbins', 14)],
  lanes=[('enGly', 'Glycolysis', 'glycolysis'), ('enTca', 'PDH & TCA', 'tca'), ('enEtc', 'Electron transport', 'ppp')],
  nodes=[
    ('en1', 'Pyruvate kinase deficiency', 330, 1340, 'enGly', 'red cells', ['pkdef', 'hkgk']),
    ('en2', 'Cori & Cahill cycles', 760, 1340, 'enGly', 'lactate', ['lacticmech']),
    ('en3', 'PDH deficiency', 1160, 1340, 'enTca', 'lactate · alanine', ['pdhdef'], 'hub'),
    ('en4', 'Thiamine · arsenic', 1560, 1340, 'enTca', 'TPP · lipoic acid', ['thiamine', 'arsenic']),
    ('en5', 'Fluoroacetate', 1960, 1340, 'enTca', 'aconitase', ['fluoroacetate']),
    ('en6', 'ETC inhibitors', 330, 1470, 'enEtc', 'I · III · IV · V', ['etcinhib']),
    ('en7', 'Cyanide · CO', 760, 1470, 'enEtc', 'complex IV', ['cyanide', 'cohb']),
    ('en8', 'Uncouplers', 1160, 1470, 'enEtc', 'heat, not ATP', ['uncoupler']),
    ('en9', 'Mitochondrial myopathies', 1580, 1470, 'enEtc', 'MELAS · MERRF', ['mito'])],
  panels=[
    (2420, PANY, 1000, 'ETC inhibitors (First Aid p. 76)', [
      ('Complex I', 'rotenone, amytal'),
      ('Complex III', 'antimycin'),
      ('Complex IV', 'cyanide, carbon monoxide'),
      ('Complex V', 'oligomycin'),
      ('Uncouplers', '2,4-DNP, aspirin overdose, thermogenin')])],
  dyn=dyn)
