# Climbing to Altitude (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A climber moves up a mountain (`alt` steps, auto): sea level → 10,000 ft → 20,000 ft → 20,000 ft after days to weeks of
# acclimatization. Bars show barometric and alveolar PO₂ with the card numbers; a lung, a kidney and a blood vessel show
# the ventilation rise (1.65× acute → ≈5× acclimatized), the renal HCO₃⁻ excretion that removes the alkalosis brake, and the
# hematocrit rise. A `one` switch shows acute mountain sickness, HACE, HAPE, chronic mountain sickness, high-altitude natives
# and breathing O₂. 5 readouts. Facts from the pinned cards only; FA pages in `fa`. No new cards.
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

A = lambda *k: [f'alt:{x}' for x in k]
D = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180

text('Climbing to altitude — less O₂ in the air, and how the body answers', 180, 150, 'dyn-big')
text('the fraction of O₂ stays about 21%; the barometric pressure falls', 180, 176, 'dyn-cap')

# ════════ mountain ════════
add('<path d="M140 1320 L520 960 L700 1040 L1120 480 L1400 1320 Z" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--dk2);stroke-width:5;stroke-linejoin:round"/>')
add('<path d="M140 1320 H1400" style="stroke:var(--nf-h2o);stroke-width:10"/>')
SPOT = dict(sea=(260, 1300, 'sea level'), k10=(620, 1000, '10,000 ft'), k20=(1060, 560, '20,000 ft'), acc=(1060, 560, '20,000 ft'))
for k, (x, y, l) in SPOT.items():
    add(f'<circle cx="{x}" cy="{y - 26}" r="20" style="fill:var(--accent);stroke:var(--ink);stroke-width:3"/>', when=A(k))
for x, y, l in ((260, 1300, 'sea level'), (620, 1000, '10,000 ft'), (1060, 560, '20,000 ft')):
    text(l, x + 36, y + 6, 'nf-l2')
text('days to weeks at 20,000 ft — acclimatized', 760, 400, 'nf-l1 dyn-tag', 'middle', when=A('acc'))
text('rapid ascent above 8,000–9,000 ft → acute mountain sickness', 760, 400, 'nf-l1 dyn-tag', 'middle', when=D('ams'))
text('natives above 13,000 ft — arterial PO₂ ≈ 40 mm Hg', 760, 400, 'nf-l1 dyn-tag', 'middle', when=D('native'))

# ════════ PO₂ bars ════════
BY = 1300
def bar(x, h, col, lab, when):
    add(f'<rect x="{x}" y="{BY - h}" width="110" height="{h}" style="fill:var({col});fill-opacity:.55;stroke:var({col});stroke-width:3"/>', when=when)
    text(lab, x + 55, BY - h - 14, 'nf-l1', 'middle', when=when)
add(f'<path d="M1520 {BY} H1960" style="stroke:var(--ink-3);stroke-width:3"/>')
text('barometric', 1595, BY + 34, 'nf-l2', 'middle'); text('alveolar PO₂', 1835, BY + 34, 'nf-l2', 'middle')
text('mm Hg', 1740, BY + 64, 'nf-l2', 'middle')
PB = dict(sea=760, k10=523, k20=349, acc=349); PA = dict(sea=104, k10=67, k20=40, acc=53)
for k in PB:
    bar(1540, PB[k] * 0.9, '--dk4', str(PB[k]), A(k))
    bar(1780, PA[k] * 0.9 * 4, '--nf-h2o', str(PA[k]), A(k))
text('alveolar bar drawn ×4', 1835, BY + 94, 'nf-l2', 'middle')
SAT = dict(sea='SaO₂ ≥ 90%', k10='SaO₂ ≥ 90% (up to about here)', k20='SaO₂ ≈ 73% on air', acc='')
for k, s in SAT.items():
    if s: text(s, 1740, 520, 'nf-l1', 'middle', when=A(k))
text('acclimatized: alveolar PO₂ 53 (vs 40) — breathing more', 1740, 520, 'nf-l1', 'middle', when=A('acc'))

# ════════ lung · kidney · blood ════════
add('<ellipse cx="2160" cy="420" rx="110" ry="150" style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>')
text('ventilation', 2160, 610, 'nf-l1', 'middle')
VT = dict(sea='1×', k10='≈ 1.65× (acute)', k20='≈ 1.65× (acute)', acc='≈ 5×')
for k, s in VT.items(): text(s, 2160, 640, 'nf-l2', 'middle', when=A(k))
add('<path d="M2090 800 C2020 800 2020 980 2090 980 C2130 980 2140 940 2120 890 C2140 840 2130 800 2090 800 Z" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/>')
text('kidney', 2160, 1020, 'nf-l1', 'middle')
text('excretes HCO₃⁻ over 2–5 days', 2160, 1050, 'nf-l2', 'middle', when=A('acc'))
text('alkalosis brakes breathing', 2160, 1050, 'nf-l2', 'middle', when=A('k10', 'k20'))
add('<path d="M1520 1460 H2380" style="stroke:var(--nf-blood);stroke-width:46;opacity:.18;stroke-linecap:round"/>')
text('blood', 1500, 1468, 'nf-l1', 'end')
HCT = dict(sea='Hct 40–45% · Hb 15', k10='Hct 40–45% · Hb 15', k20='Hct 40–45% · Hb 15', acc='Hct ≈ 60% · Hb ≈ 20 g/dL · volume +20–30%')
for k, s in HCT.items(): text(s, 1950, 1530, 'nf-l2', 'middle', when=A(k))

# ════════ illness tags ════════
TAG = dict(hace='HACE — cerebral arterioles dilate, capillaries leak (VEGF, cytokines)',
           hape='HAPE — uneven hypoxic vasoconstriction forces flow through few vessels at high pressure',
           cms='Chronic mountain sickness — huge red cell mass, pulmonary hypertension, right heart failure',
           o2='Pure O₂ at 30,000 ft: alveolar PO₂ 139 (vs 18 on air)')
for k, s in TAG.items(): text(s, 760, 400, 'nf-l1 dyn-tag', 'middle', when=D(k))
add('<ellipse cx="2160" cy="420" rx="90" ry="120" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--bad);stroke-width:4;stroke-dasharray:8 6"/>', when=D('hape'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M2160 260 V560', len=300, speed=120, r=8, base=dict(air=2),
       mods=[m(A('k10', 'k20'), set=dict(air=3), speed=1.65), m(A('acc'), set=dict(air=6), speed=2.5)]),
  dict(d='M2080 900 C2000 900 1990 1100 2000 1180', len=300, speed=80, r=8, base=dict(bic=3), when=A('acc')),
  dict(d='M1540 1460 H2360', len=820, speed=110, r=9, base=dict(rbc=4),
       mods=[m(A('acc'), set=dict(rbc=8)), m(D('native'), set=dict(rbc=8)), m(D('cms'), set=dict(rbc=11), speed=0.4)]),
]
sites = [dict(x=1740, y=560, n=[0, -1], w=10, t='rec', l='', aria='Altitude and alveolar PO₂', c='alttable', ions=[]),
         dict(x=2160, y=270, n=[0, -1], w=10, t='rec', l='', aria='Ventilatory responses', c='ventresp', ions=[]),
         dict(x=2240, y=890, n=[1, 0], w=10, t='rec', l='', aria='Acclimatization', c='acclim', ions=[]),
         dict(x=1120, y=470, n=[0, -1], w=10, t='rec', l='', aria='Mountain sickness', c='altillness', ions=[]),
         dict(x=2380, y=1460, n=[1, 0], w=10, t='rec', l='', aria='High-altitude natives', c='altnatives', ions=[])]

readouts = [
  dict(l='Alveolar PO₂', mods=[dict(when=A('k10', 'k20', 'acc'), d=-1)]),
  dict(l='Ventilation', mods=[dict(when=A('k10', 'k20', 'acc'), d=1)]),
  dict(l='Arterial pH (alkalosis)', mods=[dict(when=A('k10', 'k20'), d=1), dict(when=A('acc'), d=0)]),
  dict(l='Hematocrit', mods=[dict(when=A('acc'), d=1), dict(when=D('native', 'cms'), d=1)]),
  dict(l='SaO₂', mods=[dict(when=A('k20', 'acc'), d=-1)]),
]

notes = {
  '': 'Barometric pressure falls with altitude while O₂ stays about 21% of the gas, so inspired and alveolar PO₂ fall. Water vapor '
      '(47 mm Hg) and CO₂ dilute the alveolar gas further.',
  'alt:sea': 'Sea level: 760 mm Hg, alveolar PO₂ 104 mm Hg, arterial saturation above 90%.',
  'alt:k10': '10,000 ft: 523 mm Hg, alveolar PO₂ 67 mm Hg; saturation stays ≥ 90% up to about here. Hypoxic drive raises '
             'ventilation only ≈ 1.65× — blown-off CO₂ and the alkalosis brake the respiratory center.',
  'alt:k20': '20,000 ft unacclimatized: 349 mm Hg, alveolar PO₂ 40 mm Hg, saturation about 73% on air.',
  'alt:acc': 'Acclimatized: over 2–5 days the kidneys excrete HCO₃⁻, CSF bicarbonate and pH fall, the brake fades and ventilation '
             'rises to ≈ 5× — alveolar PO₂ 53 at 20,000 ft. Over weeks Hct 40–45% → ≈ 60%, Hb 15 → ≈ 20 g/dL, diffusing capacity '
             'up to ≈ 3×, more capillaries.',
  'dx:ams': 'Acute mountain sickness: fatigue, headache, dizziness, nausea, vomiting — a few hours to ≈ 2 days after rapid ascent '
            'above 8,000–9,000 ft. Give O₂ or descend.',
  'dx:hace': 'High-altitude cerebral edema: hypoxia dilates cerebral arterioles, raising capillary flow and pressure; VEGF and '
             'cytokines raise permeability → disorientation.',
  'dx:hape': 'High-altitude pulmonary edema: hypoxic pulmonary vasoconstriction is uneven, so flow is forced through the few '
             'unconstricted vessels at very high capillary pressure → patchy edema. O₂ usually reverses it within hours.',
  'dx:cms': 'Chronic mountain sickness: very high red cell mass and viscosity, pulmonary hypertension, right heart enlargement, '
            'heart failure — recovers within days to weeks at lower altitude.',
  'dx:native': 'High-altitude natives: arterial PO₂ ≈ 40 mm Hg, yet the extra hemoglobin carries more O₂ per volume of blood than '
               'in sea-level natives; large chest, larger heart.',
  'dx:o2': 'Breathing pure O₂ replaces the nitrogen: alveolar PO₂ 139 mm Hg at 30,000 ft (vs 18 on air); saturation stays '
           '> 90% to about 39,000 ft.',
}

dyn = dict(
  kinds=dict(air=['mov', '--nf-h2o'], bic=['mov', '--dk10'], rbc=['mov', '--nf-blood']),
  groups=[['mov', 'Air · HCO₃⁻ · red cells']],
  switches=[dict(id='alt', label='Altitude', type='steps', auto=3, options=[
              ['sea', 'Sea level'], ['k10', '10,000 ft'], ['k20', '20,000 ft'], ['acc', '20,000 ft, acclimatized']]),
            dict(id='dx', label='Show', type='one', options=[
              ['ams', 'Acute mountain sickness', 'altillness'], ['hace', 'HACE', 'altillness'], ['hape', 'HAPE', 'altillness'],
              ['cms', 'Chronic mountain sickness', 'altillness'], ['native', 'High-altitude natives', 'altnatives'],
              ['o2', 'Breathing O₂', 'alttable']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Guyton ch 44')

MAP = dict(
  id='altsim', title='Climbing to Altitude in Motion', topic='pulmo', after='highalt',
  sub='Take a climber from sea level to 20,000 ft and watch alveolar PO₂ fall, ventilation rise, the kidneys excrete HCO₃⁻ and '
      'the hematocrit climb — then see mountain sickness, HACE, HAPE, chronic mountain sickness and high-altitude natives',
  w=3600, h=1900,
  fa='299, 688',
  src=['Guyton ch 44 — Aviation, High Altitude, and Space Physiology', 'Guyton ch 42 — Regulation of Respiration'],
  lanes=[('alPhys', 'Physiology', 'glycolysis'), ('alDz', 'Illness', 'tca')],
  nodes=[
    ('al1', 'Altitude & alveolar PO₂', 330, 1660, 'alPhys', '760 → 349 mm Hg', ['alttable'], 'hub'),
    ('al2', 'Ventilatory responses', 760, 1660, 'alPhys', '1.65× → 5×', ['ventresp']),
    ('al3', 'Acclimatization', 1200, 1660, 'alPhys', 'five changes', ['acclim']),
    ('al4', 'High-altitude natives', 1640, 1660, 'alPhys', 'PaO₂ ≈ 40', ['altnatives']),
    ('al5', 'Mountain sickness', 2080, 1660, 'alDz', 'AMS · HACE · HAPE', ['altillness'])],
  panels=[
    (2500, PANY, 1000, 'Altitude table (Guyton ch 44)', [
      ('Sea level', '760 · PAO₂ 104'), ('10,000 ft', '523 · PAO₂ 67 (77 acclim.)'), ('20,000 ft', '349 · PAO₂ 40 (53 acclim.)'),
      ('50,000 ft', '87 mm Hg')])],
  dyn=dyn)
