# Water Balance in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Hypothalamic osmoreceptors and the supraoptic nuclei → posterior pituitary → ADH in the blood → V2 receptor on the
# collecting-duct principal cell → cAMP → aquaporin-2 in the apical membrane → water follows the medullary gradient into the
# interstitium, and less, more concentrated urine reaches the cup. A `one` switch shows water deprivation, a water load,
# SIADH, central and nephrogenic DI, primary polydipsia, lithium, desmopressin and the vaptans; a toggle gives desmopressin
# on top (the DI work-up). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

O = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def room(x0, y0, x1, y1, lab, cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="{cls}"/>')
    if lab: text(lab, (x0 + x1) // 2, y0 + 34, 'nf-l1', 'middle')
DD = 'dd'
# where V2 → AQP2 works, and where it does not
NO_ADH = ['dx:drink&!dd', 'dx:poly&!dd', 'dx:cdi&!dd']
BLOCKED = O('ndi', 'lith', 'vapt')
HIGH = O('dry', 'siadh', 'desmo') + ['dx:cdi&dd', 'dx:drink&dd', 'dx:poly&dd', '!dx:*&dd']
CONC = HIGH
DIL = NO_ADH + BLOCKED

text('Water balance — ADH decides how much free water you keep', 180, 150, 'dyn-big')
text('blue = water · purple = ADH (or desmopressin)', 180, 176, 'dyn-cap')

# ════════ hypothalamus → posterior pituitary ════════
room(300, 250, 820, 420, 'Hypothalamus')
text('osmoreceptors · supraoptic nuclei make ADH', 560, 320, 'nf-l2', 'middle')
add('<path d="M560 420 V500" style="stroke:var(--dk2);stroke-width:8"/>')
room(440, 500, 680, 600, 'Posterior pituitary')
add(X(560, 460), when=O('cdi'))
text('no ADH made or released', 560, 380, 'nf-l1 dyn-tag', 'middle', when=O('cdi'))
text('drinks liters — ADH switched off', 560, 380, 'nf-l1 dyn-tag', 'middle', when=O('poly'))
text('plasma dilute — ADH switched off', 560, 380, 'nf-l1 dyn-tag', 'middle', when=O('drink'))
text('plasma concentrated — ADH released', 560, 380, 'nf-l1 dyn-tag', 'middle', when=O('dry'))
# SIADH: an ectopic source
room(300, 820, 820, 940, '', 'dyn-soft')
text('ADH from elsewhere: small cell lung cancer, CNS disease, drugs', 560, 870, 'nf-l1', 'middle', when=O('siadh'))
text('HEELD-up water (SSRIs, carbamazepine, cyclophosphamide)', 560, 900, 'nf-l2', 'middle', when=O('siadh'))
text('no other ADH source', 560, 885, 'nf-l2', 'middle', unless=O('siadh'))
# drug syringe
room(900, 250, 1100, 360, 'Desmopressin', 'dyn-soft')
text('V2 agonist', 1000, 336, 'nf-l2', 'middle')

# ════════ the collecting duct ════════
add('<rect x="1700" y="300" width="120" height="960" rx="40" style="fill:var(--nf-h2o);fill-opacity:.12;stroke:var(--dk3);stroke-width:4"/>')
text('collecting duct lumen', 1760, 280, 'nf-l1', 'middle')
room(1320, 560, 1700, 940, 'Principal cell')
text('cAMP → PKA → AQP2 vesicles', 1510, 640, 'nf-l2', 'middle')
for (x, y) in ((1450, 700), (1510, 720), (1570, 700)):
    add(f'<circle cx="{x}" cy="{y}" r="12" style="fill:none;stroke:var(--nf-h2o);stroke-width:4"/>', unless=CONC)
text('medullary interstitium', 1175, 1000, 'nf-l1', 'middle')
text('hyperosmotic — the countercurrent gradient', 1175, 1026, 'nf-l2', 'middle')
add('<rect x="1030" y="420" width="290" height="560" style="fill:var(--dk1);fill-opacity:.08"/>')
# blood carrying ADH
add('<path d="M560 600 V690 H1150 V760 H1290" style="fill:none;stroke:var(--nf-blood);stroke-width:14;opacity:.25;stroke-linejoin:round"/>')
text('ADH in the blood', 800, 670, 'nf-l2', 'middle')
add('<path d="M820 880 H1150 V760" style="fill:none;stroke:var(--nf-blood);stroke-width:14;opacity:.25"/>', when=O('siadh'))
add('<path d="M1000 360 V690" style="fill:none;stroke:var(--accent);stroke-width:8;opacity:.4"/>', when=O('desmo') + [DD])
# urine
room(1640, 1290, 1880, 1400, '', 'dyn-soft')
text('urine', 1760, 1440, 'nf-l1', 'middle')
text('small volume, concentrated', 1760, 1470, 'nf-l1 dyn-tag', 'middle', when=CONC)
text('large volume, dilute', 1760, 1470, 'nf-l1 dyn-tag', 'middle', when=DIL)
text('high urine Na⁺ — aldosterone escape', 1760, 1500, 'nf-l2', 'middle', when=O('siadh'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M560 600 V690 H1150 V760 H1290', len=1100, speed=260, r=9, base=dict(adh=3),
       mods=[m(O('dry', 'ndi', 'lith'), set=dict(adh=6)), m(O('drink', 'poly', 'cdi', 'siadh'), set=dict(adh=0))]),
  dict(d='M820 880 H1150 V760 H1290', len=600, speed=260, r=9, base=dict(adh=6), when=O('siadh')),
  dict(d='M1000 360 V690 H1150 V760 H1290', len=600, speed=200, r=9, base=dict(dd=4), when=O('desmo') + [DD]),
  dict(d='M1760 320 V1280', len=960, speed=160, r=9, base=dict(w=4), mods=[m(CONC, set=dict(w=1)), m(DIL, set=dict(w=8))]),
]
sites = [
  dict(x=1320, y=760, n=[-1, 0], w=12, t='rec', l='V2 receptor', s='Gs → cAMP', c='adhdrugs', ions=[],
       block=BLOCKED, stop=NO_ADH, boost=HIGH, la='end', lx=1300, ly=830),
  dict(x=1700, y=760, n=[1, 0], w=12, t='aqp', l='aquaporin-2', s='inserted by ADH', c='aquaporins', ions=[['w', 'in', 2]],
       cross=True, stop=NO_ADH + BLOCKED, boost=HIGH, la='start', lx=1850, ly=760),
  dict(x=1320, y=880, n=[-1, 0], w=12, t='aqp', l='', aria='Water out to the interstitium', c='countercurrent', ions=[['w', 'out', 2]],
       cross=True, stop=NO_ADH + BLOCKED, boost=HIGH),
  dict(x=560, y=550, n=[0, 1], w=10, t='rec', l='', aria='Posterior pituitary', c='posteriorpit', ions=[]),
]

readouts = [
  dict(l='Plasma ADH', mods=[dict(when=O('dry', 'siadh'), d=1), dict(when=O('drink', 'cdi', 'poly'), d=-1)]),
  dict(l='Serum osmolality', mods=[dict(when=O('cdi', 'ndi', 'lith'), d=1), dict(when=O('siadh', 'poly'), d=-1)]),
  dict(l='Serum Na⁺', mods=[dict(when=O('siadh'), d=-1)]),
  dict(l='Urine osmolality', mods=[dict(when=CONC, d=1), dict(when=DIL, d=-1)]),
  dict(l='Urine volume', mods=[dict(when=CONC, d=-1), dict(when=DIL, d=1)]),
]

notes = {
  '': 'ADH is made in the supraoptic nuclei and released from the posterior pituitary, mainly when plasma osmolality rises (also '
      'for low blood volume). On V2 receptors (Gs, cAMP) of the principal cell it inserts aquaporin-2, and water follows the '
      'hyperosmotic medulla out of the lumen — concentrated urine, negative free-water clearance.',
  'dx:dry': 'Water deprivation: plasma osmolality rises, ADH is released, aquaporin-2 goes in — a small volume of concentrated urine.',
  'dx:drink': 'Water load: plasma dilutes, ADH falls, the duct stays watertight — dilute urine, positive free-water clearance.',
  'dx:siadh': 'SIADH: ADH despite a low plasma osmolality — water is kept, serum Na⁺ falls, urine stays concentrated and urine Na⁺ '
              'high (aldosterone escape). Euvolemic. Fluid restriction; correct slowly (osmotic demyelination).',
  'dx:cdi': 'Central DI: no ADH from the posterior pituitary — dilute urine pours out, serum osmolality rises (hypernatremia if the '
            'patient cannot drink). Desmopressin raises urine osmolality by more than 50%.',
  'dx:ndi': 'Nephrogenic DI: ADH is there (normal or high) but the V2 pathway fails — hereditary V2 mutation, lithium, '
            'demeclocycline, hypercalcemia, hypokalemia. Desmopressin does little. Thiazides, amiloride, indomethacin.',
  'dx:poly': 'Primary polydipsia: so much water that ADH is suppressed and serum osmolality is LOW; withhold water and the urine '
             'concentrates sharply.',
  'dx:lith': 'Lithium blocks the V2 pathway → nephrogenic DI.',
  'dx:desmo': 'Desmopressin: a V2 agonist — central DI, von Willebrand disease, mild hemophilia A, nocturnal enuresis.',
  'dx:vapt': 'Conivaptan, tolvaptan: V2 antagonists for SIADH — water is no longer reabsorbed. Correct slowly.',
  'dd': 'Desmopressin test: urine osmolality rises more than 50% in central DI, little or not at all in nephrogenic DI.',
}

dyn = dict(
  kinds=dict(adh=['adh', '--dk2'], dd=['adh', '--accent'], w=['water', '--nf-h2o']),
  groups=[['water', 'Water'], ['adh', 'ADH · desmopressin']],
  switches=[dict(id='dx', label='State · disorder · drug', type='one', options=[
              ['dry', 'Water deprivation', 'freewater'], ['drink', 'Water load', 'freewater'], ['siadh', 'SIADH', 'siadh'],
              ['cdi', 'Central DI', 'di'], ['ndi', 'Nephrogenic DI', 'di'], ['poly', 'Primary polydipsia', 'polyuriadx'],
              ['lith', 'Lithium', 'adhdrugs'], ['desmo', 'Desmopressin', 'adhdrugs'], ['vapt', 'Tolvaptan · conivaptan', 'adhdrugs']]),
            dict(id=DD, label='DI work-up', type='toggle', on='Desmopressin given', off='Give desmopressin', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 331–333, 342, 608 · Guyton ch 29 · Costanzo ch 6')
dyn['switches'][1]['def'] = dyn['switches'][1].pop('def_')

MAP = dict(
  id='watersim', title='Water Balance in Motion', topic='renal', after='urineconc',
  sub='Follow ADH from the posterior pituitary to the V2 receptor and aquaporin-2, and watch the urine concentrate or dilute — '
      'then compare SIADH, central and nephrogenic DI, primary polydipsia, lithium, desmopressin and the vaptans',
  w=3600, h=1900,
  fa='237, 331, 332, 333, 341, 342, 360, 538, 587, 592, 608',
  src=['Guyton ch 76 — Pituitary Hormones and Their Control By the Hypothalamus', 'Costanzo ch 9 — Endocrine physiology',
       'Costanzo ch 6 — Renal physiology',
       'Guyton ch 29 — Urine Concentration and Dilution; Regulation of Extracellular Fluid Osmolarity and Sodium Concentration',
       'Fundamental Neuroscience ch 3 — The Electrochemical Basis of Nerve Function',
       'Guyton ch 25 — Regulation of Body Fluid Compartments: Extracellular and Intracellular Fluids; Edema',
       'Kaplan & Sadock ch 21 — Psychopharmacology', 'Katzung ch 29 — Antipsychotic Agents & Lithium',
       'Katzung ch 58 — Management of the Poisoned Patient'],
  lanes=[('waNorm', 'ADH and the collecting duct', 'glycolysis'), ('waDz', 'Too much or too little ADH', 'tca'), ('waRx', 'Drugs', 'gluconeo')],
  nodes=[
    ('wa1', 'Posterior pituitary — ADH', 330, 1620, 'waNorm', 'osmolality drives it', ['posteriorpit'], 'hub'),
    ('wa2', 'Concentrating urine', 760, 1620, 'waNorm', 'countercurrent · free water', ['countercurrent', 'freewater']),
    ('wa3', 'Aquaporins', 1200, 1620, 'waNorm', 'AQP2 in the principal cell', ['aquaporins']),
    ('wa4', 'SIADH', 1640, 1620, 'waDz', 'euvolemic hyponatremia', ['siadh']),
    ('wa5', 'Diabetes insipidus', 2080, 1620, 'waDz', 'central vs nephrogenic', ['di']),
    ('wa6', 'Polyuria work-up', 330, 1760, 'waDz', 'water restriction, DDAVP', ['polyuriadx']),
    ('wa7', 'Hyponatremia · hypernatremia', 760, 1760, 'waDz', 'correct slowly', ['hyponat', 'hypernat']),
    ('wa8', 'ADH drugs', 1200, 1760, 'waRx', 'desmopressin · vaptans', ['adhdrugs']),
    ('wa9', 'Lithium', 1640, 1760, 'waRx', 'nephrogenic DI', ['lithium'])],
  panels=[
    (2500, PANY, 1000, 'Polyuria: which one? (First Aid p. 342)', [
      ('Primary polydipsia', 'ADH ↓, serum osm ↓ — concentrates with water restriction'),
      ('Central DI', 'ADH ↓, serum osm ↑ — desmopressin works (>50%)'),
      ('Nephrogenic DI', 'ADH normal/↑, serum osm ↑ — desmopressin fails'),
      ('SIADH', 'urine osm > serum osm, urine Na⁺ high, euvolemic')])],
  dyn=dyn)
