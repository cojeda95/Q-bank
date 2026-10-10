# Inflammation & Wound Healing in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A skin wound over time: neutrophils leave a postcapillary venule in four steps (rolling → tight binding →
# diapedesis → migration), then the three phases of repair — inflammatory (up to 3 days), proliferative (day 3 to
# weeks: granulation tissue, type III collagen, angiogenesis, myofibroblast contraction) and remodeling (1 week to
# 6+ months: type III replaced by type I, ~70–80% of strength by 3 months). A `steps` switch walks the time; a `one`
# switch adds a problem (vitamin C, copper or zinc deficiency, LAD type 1, hypertrophic scar, keloid).
# No new cards: facts restate the pinned cards (acuteinflam, woundheal, collagentypes, lad1, scurvy if present —
# fact-checked against the corpus). Drawings are schematic. Sources: First Aid 2025 pp. 210–214.
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
T = lambda *k: ['t:' + x for x in k]
D = lambda *k: ['dx:' + x for x in k]

# ════════ 1. the venule: leukocyte extravasation ════════
box(160, 130, 1100, 1180)
text('Acute inflammation — neutrophils leave a postcapillary venule', 180, 166, 'dyn-big')
text('seconds to minutes: vessels dilate and leak, neutrophils get out', 180, 186, 'dyn-cap')
shapes.append(dict(vessel='M290 420 H970', w=170, color='--dk12'))
add('<path d="M200 515 H1060" style="stroke:var(--line-2);stroke-width:16"/>')
text('endothelium', 1060, 550, 'nf-l2', 'end')
STEPS = [(300, 'Rolling', 'E- and P-selectin ↔ sialyl Lewis X'), (510, 'Tight binding', 'ICAM-1 ↔ CD11/18 integrins'),
         (720, 'Diapedesis', 'PECAM-1 between the cells'), (930, 'Migration', 'C5a, IL-8, LTB₄, fMet peptides')]
for i, (x, h, s) in enumerate(STEPS):
    y = 470 if i < 2 else (515 if i == 2 else 640)
    add(f'<circle cx="{x}" cy="{y}" r="30" class="dyn-cell" style="stroke:var(--dk5);stroke-width:4"/><text class="nf-l1" x="{x}" y="{y + 5}" text-anchor="middle">N</text>',
        unless=D('lad') if i >= 1 else None)
    text(f'{i + 1}. {h}', x, 760, 'nf-l1', 'middle'); text(s, x, 784, 'nf-l2', 'middle')
add('<circle cx="510" cy="440" r="30" class="dyn-cell dyn-dim"/><text class="nf-l1" x="510" y="445" text-anchor="middle">N</text>', when=D('lad'))
text('LAD type 1: no CD18 — neutrophils roll but never bind, so none reach the tissue', 180, 860, TAG, when=D('lad'))
text('the wound: no pus · delayed separation of the umbilical cord · ↑↑ blood neutrophils', 180, 886, TAG, when=D('lad'))
text('macrophages take over later (peak 2–3 days) and steer the outcome', 180, 860, 'nf-l2', unless=D('lad'))
text('outcomes: resolution · abscess · chronic inflammation · scar', 180, 886, 'nf-l2', unless=D('lad'))

# ════════ 2. the wound ════════
box(1140, 130, 2340, 1180)
text('The wound — three overlapping phases of repair', 1160, 166, 'dyn-big')
text('schematic cross-section of skin', 1160, 186, 'dyn-cap')
WX0, WX1, EPI, DERM = 1200, 2280, 320, 760
add(f'<rect x="{WX0}" y="{EPI}" width="{WX1 - WX0}" height="{DERM - EPI}" rx="10" class="dyn-cell" style="opacity:.6"/>')
GAP0, GAP1 = 1600, 1880
add(f'<path d="M{WX0} {EPI} H{GAP0} M{GAP1} {EPI} H{WX1}" style="stroke:var(--dk7);stroke-width:14"/>')
add(f'<path d="M{GAP0} {EPI} H{GAP1}" style="stroke:var(--dk7);stroke-width:14;stroke-dasharray:18 12"/>', when=T('prolif'))
add(f'<path d="M{GAP0} {EPI} H{GAP1}" style="stroke:var(--dk7);stroke-width:14"/>', when=T('remod'))
text('epidermis', WX0, EPI - 16, 'nf-l2')
text('dermis', WX0 + 10, DERM - 12, 'nf-l2')
# the wound bed per phase
add(f'<path d="M{GAP0} {EPI} L{GAP0 + 40} 640 H{GAP1 - 40} L{GAP1} {EPI} Z" style="fill:var(--bad);fill-opacity:.35"/>', when=T('min', 'inflam'))
text('clot — platelets and fibrin', (GAP0 + GAP1) // 2, 480, 'nf-l1', 'middle', when=T('min', 'inflam'))
add(f'<path d="M{GAP0} {EPI} L{GAP0 + 40} 640 H{GAP1 - 40} L{GAP1} {EPI} Z" style="fill:var(--bad);fill-opacity:.18"/>'
    + ''.join(f'<path d="M{GAP0 + 40 + i * 40} 640 Q{GAP0 + 60 + i * 40} 520 {GAP0 + 40 + i * 40} {EPI + 30}" style="fill:none;stroke:var(--bad);stroke-width:3"/>' for i in range(5))
    + ''.join(f'<path d="M{GAP0 + 30} {360 + j * 50} q30 -14 60 0 t60 0 t60 0 t60 0" style="fill:none;stroke:var(--dk9);stroke-width:3"/>' for j in range(5)),
    when=T('prolif'))
text('granulation tissue — new capillaries, fibroblasts, type III collagen', 1160, 860, TAG, when=T('prolif'))
add(''.join(f'<path d="M{GAP0 + 30} {360 + j * 50} H{GAP1 - 30}" style="stroke:var(--dk9);stroke-width:7"/>' for j in range(5)), when=T('remod'), unless=D('keloid', 'hyper'))
text('remodeling — type III replaced by type I; the scar shrinks and strengthens', 1160, 860, TAG, when=T('remod'))
text('inflammatory phase: platelets, neutrophils, macrophages — the clot, leaky vessels, debris cleared', 1160, 860, TAG, when=T('inflam'))
text('first minutes: the vessels dilate and leak; neutrophils begin to leave', 1160, 860, TAG, when=T('min'))
# problems
add(''.join(f'<path d="M{GAP0 - 120 + i * 30} {EPI - 10 - (i % 3) * 18} q40 -30 80 0" style="fill:none;stroke:var(--dk9);stroke-width:6"/>' for i in range(14))
    + f'<path d="M{GAP0 - 140} {EPI} Q{(GAP0 + GAP1) // 2} {EPI - 130} {GAP1 + 140} {EPI}" style="fill:var(--dk9);fill-opacity:.25;stroke:var(--dk9);stroke-width:4"/>',
    when=D('keloid'))
add(''.join(f'<path d="M{GAP0 + 30} {360 + j * 50} H{GAP1 - 30}" style="stroke:var(--dk9);stroke-width:4"/>' for j in range(7))
    + f'<path d="M{GAP0} {EPI} Q{(GAP0 + GAP1) // 2} {EPI - 70} {GAP1} {EPI}" style="fill:var(--dk9);fill-opacity:.2;stroke:var(--dk9);stroke-width:4"/>',
    when=D('hyper'))
text('keloid: lots of types I and III, disorganized, spreading beyond the wound; often recurs', 1160, 900, TAG, when=D('keloid'))
text('earlobes, face, upper limbs · more common in darker skin', 1160, 926, 'nf-l2', when=D('keloid'))
text('hypertrophic scar: more type III, parallel, stays within the wound; seldom recurs', 1160, 900, TAG, when=D('hyper'))
text('vitamin C deficiency: the proliferative phase is delayed', 1160, 900, TAG, when=D('vitc'))
text('copper deficiency: the proliferative phase is delayed', 1160, 900, TAG, when=D('cu'))
text('zinc deficiency: the zinc-dependent collagenases can’t remodel — healing is delayed', 1160, 900, TAG, when=D('zn'))
text('excess TGF-β drives hypertrophic and keloid scars', 1160, 952, 'nf-l2', when=D('keloid', 'hyper'))
# tensile strength bar
text('Tensile strength of the scar', 1160, 1030, 'nf-l1')
add('<rect x="1160" y="1050" width="1100" height="34" rx="10" class="dyn-soft"/>')
for k, f in [('min', .02), ('inflam', .05), ('prolif', .3), ('remod', .75)]:
    add(f'<rect x="1160" y="1050" width="{round(1100 * f)}" height="34" rx="10" style="fill:var(--accent);fill-opacity:.75"/>', when=T(k))
text('~70–80% of normal by 3 months — little more after that', 1160, 1120, 'nf-l2', when=T('remod'))
text('bar is schematic', 2260, 1120, 'dyn-cap', 'end')

# ════════ 3. motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M300 420 H960', len=660, speed=110, r=7, base=dict(neu=3), mods=[m(T('min', 'inflam'), set=dict(neu=6)), m(D('lad'), set=dict(neu=9))]),
  dict(d='M930 560 V700', len=140, speed=50, r=7, base=dict(), mods=[m(T('min', 'inflam'), set=dict(neu=3)), m(D('lad'), set=dict(neu=0))]),
  dict(d=f'M{GAP0 + 60} 700 Q{(GAP0 + GAP1) // 2} 600 {GAP1 - 60} 700', len=320, speed=60, r=8, base=dict(), mods=[m(T('inflam', 'prolif'), set=dict(mac=3))]),
]

# ════════ 4. sites ════════
sites = [
  dict(x=510, y=505, n=[0, -1], w=14, t='rec', l='', aria='Integrins and ICAM-1 — tight binding', ions=[], c='lad1', block=D('lad')),
  dict(x=300, y=505, n=[0, -1], w=14, t='rec', l='', aria='Selectins — rolling', ions=[], c='acuteinflam'),
  dict(x=GAP1 + 60, y=EPI + 40, n=[1, 0], w=14, t='ex', l='', aria='Wound healing', ions=[], c='woundheal'),
]

# ════════ 5. readouts (compared with unwounded skin) ════════
readouts = [
  dict(l='Neutrophils', mods=[m(T('min', 'inflam'), d=1)]),
  dict(l='Macrophages', mods=[m(T('inflam'), d=1)]),
  dict(l='Type III collagen', mods=[m(T('prolif'), d=1)]),
  dict(l='Type I collagen', mods=[m(T('remod'), d=1)]),
]
# UNVERIFIED: macrophages ↑ only in the inflammatory step here; the cards say they predominate late (peak 2–3 days) without an end point

# ════════ 6. notes ════════
notes = {
  't:min': 'Minutes: acute inflammation. Vessels dilate and leak fluid and protein; neutrophils leave postcapillary venules — '
           'roll on E- and P-selectin, bind tightly through CD11/18 integrins to ICAM-1, squeeze through on PECAM-1 and follow '
           'chemokines (C5a, IL-8, LTB₄) to the wound.',
  't:inflam': 'Inflammatory phase (up to 3 days): platelets form the clot, neutrophils and then macrophages clear the debris. '
              'Macrophages predominate late (peak 2–3 days) and their cytokines steer what comes next.',
  't:prolif': 'Proliferative phase (day 3 to weeks): fibroblasts, myofibroblasts, endothelial cells and keratinocytes build '
              'granulation tissue — type III collagen, new capillaries (VEGF, FGF) — and myofibroblasts contract the wound.',
  't:remod': 'Remodeling (1 week to 6+ months): fibroblasts replace type III collagen with type I, using zinc-dependent '
             'collagenases. About 70–80% of the original strength returns by 3 months, and little more after that.',
  'dx:vitc': 'Vitamin C deficiency delays the proliferative phase — granulation tissue and type III collagen come late.',
  'dx:cu': 'Copper deficiency delays the proliferative phase.',
  'dx:zn': 'Zinc deficiency delays remodeling — the collagenases that replace type III with type I are zinc-dependent.',
  'dx:lad': 'Leukocyte adhesion deficiency type 1: without CD18, neutrophils roll but cannot bind tightly or leave the vessel — '
            'very high blood neutrophils, no pus at infected sites, delayed separation of the umbilical cord.',
  'dx:hyper': 'Hypertrophic scar: more type III collagen, laid down in parallel, staying within the wound — it seldom recurs.',
  'dx:keloid': 'Keloid: much more type I and III collagen, disorganized, spreading beyond the wound (earlobes, face, upper limbs) '
               'and often recurring; more common in darker skin. Excess TGF-β drives both keloids and hypertrophic scars.',
}

dyn = dict(
  kinds=dict(neu=['neu', '--dk5'], mac=['mac', '--dk3']),
  groups=[['neu', 'Neutrophils'], ['mac', 'Macrophages']],
  switches=[dict(id='t', label='Time since the wound', type='steps', auto=5,
                 options=[['min', 'Minutes — acute inflammation'], ['inflam', 'Up to 3 days — inflammatory'],
                          ['prolif', 'Day 3 to weeks — proliferative'], ['remod', '1 week to 6+ months — remodeling']]),
            dict(id='dx', label='Add a problem', type='one',
                 options=[['vitc', 'Vitamin C deficiency', 'woundheal'], ['cu', 'Copper deficiency', 'woundheal'], ['zn', 'Zinc deficiency', 'woundheal'],
                          ['lad', 'Leukocyte adhesion deficiency', 'lad1'], ['hyper', 'Hypertrophic scar', 'woundheal'], ['keloid', 'Keloid', 'woundheal']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 210–214')

MAP = dict(
  id='healsim', title='Inflammation & Wound Healing in Motion', topic='path', after='genpath',
  sub='Neutrophils leaving a venule in four steps, then a skin wound through the inflammatory, proliferative and remodeling '
      'phases — collagen type III to type I, strength returning to ~70–80% by 3 months. Add a deficiency, LAD, a hypertrophic '
      'scar or a keloid. Tap the vessel or the wound for its card',
  w=3500, h=2100,
  fa='210–214', src=[],
  lanes=[('hlInf', 'Inflammation', 'glycolysis'), ('hlRep', 'Repair', 'tca')],
  nodes=[
    ('hl1', 'Acute inflammation', 380, 1300, 'hlInf', 'extravasation in four steps', ['acuteinflam']),
    ('hl2', 'Leukocyte adhesion deficiency', 820, 1300, 'hlInf', 'no CD18', ['lad1']),
    ('hl3', 'Wound healing & scars', 1260, 1300, 'hlRep', 'three phases · keloids', ['woundheal']),
    ('hl4', 'Collagen types', 1700, 1300, 'hlRep', 'III early, I later', ['collagentypes']),
    ('hl5', 'Labile, stable, permanent', 380, 1440, 'hlRep', 'who can regenerate', ['celltypes'])],
  panels=[
    (2420, 860, 1000, 'The phases (First Aid p. 212)', [
      ('Inflammatory', 'up to 3 days · platelets, neutrophils, macrophages'),
      ('Proliferative', 'day 3 to weeks · granulation tissue, type III collagen · vit C, copper'),
      ('Remodeling', '1 week to 6+ months · type III → type I · zinc collagenases'),
      ('Strength', '~70–80% by 3 months')]),
    (2420, 1060, 1000, 'Scars (First Aid p. 214)', [
      ('Hypertrophic', '↑ type III · parallel · within the wound · seldom recurs'),
      ('Keloid', '↑↑ types I and III · disorganized · beyond the wound · recurs'),
      ('Driver', 'excess TGF-β')])],
  dyn=dyn)
