# Hypoxemia Simulator — the A–a gradient and 100% O₂ (dynamic map, kit data) — drafted on the drafts branch.
# One alveolus and its capillary, redrawn for each cause of hypoxemia: low inspired O₂ (altitude), hypoventilation,
# V/Q mismatch, diffusion limitation, right-to-left shunt, and dead space (pulmonary embolism). O₂ particles come
# down the airway, cross the membrane and leave in the blood; a toggle gives 100% O₂ and shows which causes
# correct (all but a true shunt). A worked panel computes PAO₂ from the alveolar gas equation with example values.
# No new cards: facts restate the pinned cards (hypoxemia, aagradient, vq, o2therapy, hypercap, deadspace, copd, ild,
# pe, altitude, respacid — fact-checked against the corpus). Example numbers are illustrative (marked).
# Sources: First Aid 2025 pp. 684–687.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

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

TAG = 'nf-l2 dyn-tag'
H = lambda *k: ['hx:' + x for x in k]
FIX = H('alt', 'hypov', 'vq', 'diff')          # corrected by O₂
WIDE = H('vq', 'diff', 'shunt', 'dead')         # widened A–a

# ════════ 1. the alveolus and its capillary ════════
box(160, 130, 1500, 1180)
text('One alveolus and its capillary', 180, 166, 'dyn-big')
text('air comes down the airway · O₂ crosses the membrane · blood carries it away', 180, 186, 'dyn-cap')
shapes.append(dict(tube='M820 220 V380', w=70, color='--dk1'))
add('<path d="M820 220 V380" style="stroke:var(--bad);stroke-width:46;opacity:.25"/>', when=H('vq'))
text('airway', 870, 250, 'nf-l2')
text('airway narrowed — less air reaches this alveolus', 870, 280, TAG, when=H('vq'))
add('<circle cx="820" cy="560" r="190" class="dyn-cell"/>')
add('<circle cx="820" cy="560" r="190" style="fill:var(--dk12);fill-opacity:.35;stroke:none"/>', when=H('shunt'))
text('alveolus', 820, 470, 'nf-l1', 'middle')
text('filled (fluid, pus) or collapsed — no air', 820, 560, TAG, 'middle', when=H('shunt'))
# the membrane, thicker in diffusion limitation
add('<path d="M640 760 H1000" style="stroke:var(--line-2);stroke-width:10"/>', unless=H('diff'))
add('<path d="M640 760 H1000" style="stroke:var(--dk7);stroke-width:34;opacity:.7"/>', when=H('diff'))
text('thickened membrane (fibrosis) — O₂ crosses slowly', 1010, 760, TAG, when=H('diff'))
shapes.append(dict(vessel='M220 860 H1440', w=70, color='--dk12'))
text('capillary: venous blood in →', 230, 800, 'nf-l2')
text('→ to the arteries (PaO₂)', 1430, 800, 'nf-l2', 'end')
add('<circle cx="560" cy="860" r="36" style="fill:var(--bad)"/><path d="M542 842 L578 878 M578 842 L542 878" class="nf-x"/>', when=H('dead'))
text('clot — perfusion stops: the alveolus is ventilated for nothing', 230, 940, TAG, when=H('dead'))
text('blood passes the alveolus without picking up O₂', 230, 940, TAG, when=H('shunt'))
text('too few breaths — CO₂ builds up, alveolar O₂ falls', 230, 940, TAG, when=H('hypov'))
text('thin air — less O₂ in every breath', 230, 940, TAG, when=H('alt'))
text('100% O₂: the alveolar PO₂ rises and the blood picks it up', 230, 980, TAG, when=['o2&hx:alt', 'o2&hx:hypov', 'o2&hx:vq', 'o2&hx:diff'])
text('100% O₂: blood never meets the extra O₂ — PaO₂ barely rises', 230, 980, TAG, when=['o2&hx:shunt'])
text('pick a cause of hypoxemia', 230, 940, 'dyn-cap', unless=['hx:*'])

# ════════ 2. the numbers ════════
box(1540, 130, 2340, 1180)
text('The alveolar gas equation', 1560, 166, 'dyn-big')
text('room air at sea level: PAO₂ = 150 − PaCO₂ ÷ 0.8', 1560, 196, 'nf-l1')
text('A–a gradient = PAO₂ − PaO₂ · normal ≈ age/4 + 4', 1560, 222, 'nf-l2')
text('example values — illustrative', 1560, 248, 'dyn-cap')
# UNVERIFIED: the example numbers below are illustrative, chosen to show the direction of each change
EX = dict(norm=(40, 100, 95), alt=(40, 60, 55), hypov=(72, 60, 55), vq=(40, 100, 65), diff=(40, 100, 70), shunt=(40, 100, 60), dead=(40, 100, 70))
ROWS = [('PaCO₂', 0), ('PAO₂ (alveolar)', 1), ('PaO₂ (arterial)', 2)]
for k, (c, A, a) in EX.items():
    w = [f'hx:{k}'] if k != 'norm' else None
    un = None if k != 'norm' else ['hx:*']
    vals = [c, A, a]
    for i, (lab, j) in enumerate(ROWS):
        text(lab, 1560, 330 + i * 70, 'nf-l1', when=w, unless=un)
        text(f'{vals[j]} mm Hg', 2300, 330 + i * 70, 'dyn-big', 'end', when=w, unless=un)
    text('A–a gradient', 1560, 560, 'nf-l1', when=w, unless=un)
    text(f'{A - a} mm Hg', 2300, 560, 'dyn-big', 'end', when=w, unless=un)
    text('normal' if A - a < 15 else 'widened', 2300, 586, TAG, 'end', when=w, unless=un)
text('hypoventilation: PAO₂ = 150 − 72 ÷ 0.8 = 60', 1560, 640, 'nf-l2', when=H('hypov'))
text('altitude: less O₂ inspired, so PAO₂ itself is low', 1560, 640, 'nf-l2', when=H('alt'))
text('the alveolus has the O₂ — the blood does not get it', 1560, 640, 'nf-l2', when=WIDE)
# the five causes, checked off
text('The five causes of hypoxemia', 1560, 740, 'nf-l1')
CAUSES = [('Low inspired PO₂', 'normal A–a · corrects with O₂', H('alt')),
          ('Hypoventilation', 'normal A–a · ↑ PaCO₂ · corrects', H('hypov')),
          ('V/Q mismatch', 'widened A–a · corrects', H('vq', 'dead')),
          ('Diffusion limitation', 'widened A–a · corrects', H('diff')),
          ('Right-to-left shunt', 'widened A–a · does NOT correct', H('shunt'))]
for i, (lab, sub, w) in enumerate(CAUSES):
    y = 790 + i * 72
    add(f'<rect x="1560" y="{y - 28}" width="760" height="60" rx="12" class="dyn-soft"/>')
    add(f'<rect x="1560" y="{y - 28}" width="760" height="60" rx="12" class="dyn-hl" style="fill:none"/>', when=w)
    text(f'{i + 1}. {lab}', 1580, y - 4, 'nf-l1'); text(sub, 1580, y + 18)

# ════════ 3. motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M820 200 V430', len=230, speed=90, r=6, base=dict(o2=4),
       mods=[m(H('alt', 'hypov', 'vq'), set=dict(o2=1)), m(H('shunt'), set=dict(o2=0)), m(['o2'], add=dict(o2=4)), m(['o2&hx:shunt'], set=dict(o2=0))]),
  dict(d='M230 860 H1430', len=1200, speed=120, r=6, base=dict(rbc=6),
       mods=[m(H('dead'), set=dict(rbc=1))]),
  dict(d='M820 600 V820', len=220, speed=60, r=6, base=dict(o2=3),
       mods=[m(H('alt', 'hypov', 'vq'), set=dict(o2=1)), m(H('diff'), set=dict(o2=1), speed=0.4), m(H('shunt', 'dead'), set=dict(o2=0)),
             m(['o2&hx:alt', 'o2&hx:hypov', 'o2&hx:vq', 'o2&hx:diff'], set=dict(o2=4))]),
]

# ════════ 4. sites ════════
sites = [
  dict(x=700, y=760, n=[0, -1], w=10, t='ch', l='', aria='Alveolar–capillary membrane — diffusion', ions=[], c='pulmcirc', low=H('diff')),
  dict(x=1000, y=380, n=[1, 0], w=10, t='ex', l='', aria='V/Q — shunt and dead space', ions=[], c='vq'),
  dict(x=2290, y=230, n=[0, 1], w=10, t='ex', l='', aria='A–a gradient', ions=[], c='aagradient'),
]

# ════════ 5. readouts ════════
readouts = [
  dict(l='PaO₂', mods=[m(['hx:*'], d=-1)]),
  dict(l='PaCO₂', mods=[m(H('hypov'), d=1), m(H('alt', 'vq', 'diff', 'shunt'), d=0)]),
  dict(l='A–a gradient', mods=[m(H('alt', 'hypov'), d=0), m(WIDE, d=1)]),
  dict(l='PaO₂ on 100% O₂', mods=[m(['o2&hx:alt', 'o2&hx:hypov', 'o2&hx:vq', 'o2&hx:diff'], d=1), m(['o2&hx:shunt'], d=0)]),
]

# ════════ 6. notes ════════
notes = {
  '': 'Hypoxemia has five causes. Two leave the alveolus short of O₂ (low inspired PO₂, hypoventilation) — the A–a gradient is '
      'normal. Three stop O₂ getting from a normal alveolus into the blood (V/Q mismatch, diffusion limitation, shunt) — the '
      'gradient widens. Then give 100% O₂: everything corrects except a true shunt.',
  'hx:alt': 'High altitude: less O₂ in every breath, so alveolar and arterial PO₂ fall together — normal A–a gradient. '
            'Supplemental O₂ fully corrects it.',
  'hx:hypov': 'Hypoventilation (opioids, obesity hypoventilation, neuromuscular disease): CO₂ builds up and displaces alveolar O₂ — '
              'PaCO₂ high, A–a gradient normal. O₂ helps the hypoxemia but does nothing for the CO₂.',
  'hx:vq': 'V/Q mismatch (pneumonia, COPD): some alveoli get too little air for their blood — widened A–a gradient. '
           'Supplemental O₂ raises the alveolar PO₂ even in poorly ventilated units, so it corrects.',
  'hx:diff': 'Diffusion limitation (interstitial fibrosis, edema): a thick membrane slows O₂ crossing — widened A–a gradient, '
             'and it corrects with O₂. CO₂ is rarely retained because it diffuses about 20 times faster than O₂.',
  'hx:shunt': 'Right-to-left shunt (V/Q → 0: atelectasis, pneumonia, pulmonary edema, ARDS, intracardiac shunt): blood passes '
              'alveoli with no air in them — widened A–a gradient, and 100% O₂ barely helps because that blood never meets it.',
  'hx:dead': 'Dead space (V/Q → ∞): a pulmonary embolism stops perfusion, so ventilation of that region is wasted; blood is '
             'diverted to other units, widening the A–a gradient.',
  'o2': 'Giving 100% O₂ separates the causes: low inspired O₂, hypoventilation, V/Q mismatch and diffusion limitation all '
        'correct; a true right-to-left shunt does not.',
}
# UNVERIFIED: dead space widens the A–a gradient "because blood is diverted to other units" — the vq card names PE as dead space
# but does not explain its A–a effect

dyn = dict(
  kinds=dict(o2=['o2', '--dk2'], rbc=['rbc', '--dk12']),
  groups=[['o2', 'O₂'], ['rbc', 'Blood']],
  switches=[dict(id='hx', label='Pick a cause of hypoxemia', type='one',
                 options=[['alt', 'High altitude', 'altitude'], ['hypov', 'Hypoventilation', 'respacid'], ['vq', 'V/Q mismatch', 'vq'],
                          ['diff', 'Diffusion limitation', 'ild'], ['shunt', 'Right-to-left shunt', 'vq'], ['dead', 'Dead space (PE)', 'deadspace']]),
            dict(id='o2', label='100% O₂', type='toggle', on='Breathing 100% O₂', off='Room air', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 684–687 · example values illustrative')
dyn['switches'][1]['def'] = dyn['switches'][1].pop('def_')

MAP = dict(
  id='hypoxsim', title='Hypoxemia Simulator — A–a Gradient & 100% O₂', topic='pulmo', after='hypoxia',
  sub='One alveolus and its capillary for each cause of hypoxemia — altitude, hypoventilation, V/Q mismatch, diffusion limitation, '
      'shunt and dead space — with the alveolar gas equation worked through and a 100% O₂ switch that shows which causes correct. '
      'Tap the membrane or the numbers for their cards',
  w=3500, h=2100,
  fa='684–687', src=[],
  lanes=[('hxGas', 'Gas exchange', 'glycolysis'), ('hxDz', 'Causes', 'tca')],
  nodes=[
    ('hx1', 'Five causes of hypoxemia', 380, 1300, 'hxGas', 'A–a and O₂ response', ['hypoxemia', 'hypoxtypes']),
    ('hx2', 'A–a gradient', 820, 1300, 'hxGas', 'alveolar gas equation', ['aagradient']),
    ('hx3', 'V/Q, shunt, dead space', 1260, 1300, 'hxGas', 'V/Q → 0 · V/Q → ∞', ['vq', 'deadspace', 'pulmcirc']),
    ('hx4', 'Oxygen therapy', 1700, 1300, 'hxGas', 'who it helps', ['o2therapy', 'hypercap']),
    ('hx5', 'Altitude', 380, 1440, 'hxDz', 'low inspired O₂', ['altitude']),
    ('hx6', 'Hypoventilation', 820, 1440, 'hxDz', '↑ PaCO₂', ['respacid', 'sleepapnea']),
    ('hx7', 'Lung disease', 1260, 1440, 'hxDz', 'COPD · fibrosis', ['copd', 'ild'])],
  panels=[
    (2420, 800, 1000, 'The five causes (First Aid pp. 686–687)', [
      ('Low inspired PO₂', 'altitude · normal A–a · corrects with O₂'),
      ('Hypoventilation', 'normal A–a · ↑ PaCO₂ · corrects with O₂'),
      ('V/Q mismatch', 'widened A–a · corrects with O₂'),
      ('Diffusion limitation', 'widened A–a · corrects with O₂'),
      ('Right-to-left shunt', 'widened A–a · does NOT correct with O₂')]),
    (2420, 1020, 1000, 'Remember (First Aid pp. 685–687)', [
      ('Normal A–a', '≈ age/4 + 4 — under 14 before age 40'),
      ('Hypoxia ≠ hypoxemia', 'anemia and CO poisoning: tissue hypoxia with a normal PaO₂'),
      ('Cyanosis', 'needs ≈ 5 g/dL deoxyhemoglobin')])],
  dyn=dyn)
