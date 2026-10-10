# Pharyngeal Arches in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Clefts (ectoderm, outside), arches (mesoderm + neural crest, middle) and pouches (endoderm, inside) — CAP — drawn as a
# schematic stack, with neural crest streaming into each arch and toward the heart's outflow tract, and a face and neck
# beside it. A `one` switch breaks one piece: DiGeorge (3rd and 4th pouches), Treacher Collins and Pierre Robin (1st arch),
# cleft lip, cleft palate, a thyroglossal duct cyst and a pharyngeal cleft cyst. 5 readouts. Facts from the pinned cards;
# FA pages in `fa`. No new cards.
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

text('Pharyngeal arches — CAP: clefts outside, arches in the middle, pouches inside', 180, 150, 'dyn-big')
text('schematic: one stack from the 1st arch (top) to the 4th/6th (bottom)', 180, 176, 'dyn-cap')

# ════════ the stack ════════
AX0, AX1, AY0, AH, GAP = 560, 1160, 330, 120, 50
ARCH = [('1st arch — CN V3', 'chew: muscles of mastication, malleus, incus', '--dk1'),
        ('2nd arch — CN VII', 'smile: facial expression, stapes, styloid', '--dk2'),
        ('3rd arch — CN IX', 'swallow: stylopharyngeus, greater hyoid horn', '--dk3'),
        ('4th & 6th arches — CN X', 'speak: constrictors, larynx muscles, cartilages', '--dk4')]
POUCH = ['1st pouch → middle ear, eustachian tube', '2nd pouch → palatine tonsil',
         '3rd pouch → thymus + inferior parathyroids', '4th pouch → superior parathyroids + C cells']
CLEFT = ['1st cleft → external auditory meatus', '2nd cleft — obliterated', '3rd cleft — obliterated', '4th cleft — obliterated']
text('clefts · ectoderm', 300, AY0 - 40, 'nf-l1')
text('arches · mesoderm + neural crest', (AX0 + AX1) // 2, AY0 - 40, 'nf-l1', 'middle')
text('pouches · endoderm', 1220, AY0 - 40, 'nf-l1')
for i, (a, b, c) in enumerate(ARCH):
    y = AY0 + i * (AH + GAP)
    add(f'<rect x="{AX0}" y="{y}" width="{AX1 - AX0}" height="{AH}" rx="30" style="fill:var({c});fill-opacity:.18;stroke:var({c});stroke-width:4"/>')
    text(a, AX0 + 30, y + 50, 'nf-l1'); text(b, AX0 + 30, y + 80, 'nf-l2')
    py = y + AH + GAP // 2 - 10 if i < 3 else y + AH + 40
    add(f'<ellipse cx="{AX1 + 20}" cy="{py}" rx="28" ry="20" style="fill:var(--dk8);fill-opacity:.35;stroke:var(--dk8);stroke-width:3"/>')
    text(POUCH[i], AX1 + 64, py + 5, 'nf-l2')
    add(f'<ellipse cx="{AX0 - 20}" cy="{py}" rx="28" ry="20" style="fill:var(--dk6);fill-opacity:.3;stroke:var(--dk6);stroke-width:3"/>')
    text(CLEFT[i], AX0 - 64, py + 5, 'nf-l2', 'end')
PY3 = AY0 + 2 * (AH + GAP) + AH + GAP // 2 - 10
PY4 = AY0 + 3 * (AH + GAP) + AH + 40
add(X(AX1 + 20, PY3) + X(AX1 + 20, PY4), when=O('digeorge'))
text('3rd + 4th pouches fail: no thymus, no parathyroids', AX1 + 64, PY4 + 50, 'nf-l1 dyn-tag', when=O('digeorge'))
add(f'<rect x="{AX0}" y="{AY0}" width="{AX1 - AX0}" height="{AH}" rx="30" style="fill:none;stroke:var(--bad);stroke-width:6;stroke-dasharray:10 8"/>', when=O('treacher', 'pierre'))
text('1st-arch structures under-built', AX0 + 300, AY0 + AH + 32, 'nf-l1 dyn-tag', 'middle', when=O('treacher', 'pierre'))
text('a persistent cervical sinus (2nd–4th clefts) → lateral cyst', 300, PY4 + 50, 'nf-l1 dyn-tag', when=O('bcc'))
# neural crest source and the heart's outflow tract
add(f'<rect x="{AX0 + 100}" y="230" width="400" height="44" rx="22" class="dyn-soft"/>')
text('neural crest', AX0 + 300, 258, 'nf-l1', 'middle')
add('<rect x="660" y="1080" width="400" height="60" rx="24" class="dyn-cell"/>')
text('heart outflow tract (conotruncus)', 860, 1117, 'nf-l1', 'middle')
add(X(860, 1110), when=O('digeorge'))
text('conotruncal defects: truncus, tetralogy', 860, 1180, 'nf-l1 dyn-tag', 'middle', when=O('digeorge'))

# ════════ face and neck ════════
FX, FY = 2050, 560
add(f'<ellipse cx="{FX}" cy="{FY}" rx="210" ry="250" class="dyn-cell"/>')
text('face', FX, FY - 270, 'nf-l1', 'middle')
add(f'<path d="M{FX - 210} {FY - 20} q-40 30 0 70" style="fill:none;stroke:var(--ink-2);stroke-width:5"/>')
text('ear', FX - 270, FY + 20, 'nf-l2', 'end')
add(f'<path d="M{FX - 150} {FY + 120} Q{FX} {FY + 300} {FX + 150} {FY + 120}" style="fill:none;stroke:var(--ink-2);stroke-width:6"/>', unless=O('treacher', 'pierre'))
add(f'<path d="M{FX - 110} {FY + 140} Q{FX} {FY + 230} {FX + 110} {FY + 140}" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=O('treacher', 'pierre'))
text('small mandible', FX + 230, FY + 200, 'nf-l1 dyn-tag', 'start', when=O('treacher', 'pierre'))
text('zygoma small · hearing loss', FX + 230, FY - 20, 'nf-l1 dyn-tag', 'start', when=O('treacher'))
add(f'<path d="M{FX - 60} {FY + 110} Q{FX} {FY + 140} {FX + 60} {FY + 110}" style="fill:none;stroke:var(--ink-2);stroke-width:4"/>')
add(f'<path d="M{FX - 20} {FY + 60} V{FY + 118}" style="stroke:var(--bad);stroke-width:6"/>', when=O('lip'))
text('maxillary + medial nasal processes don’t fuse', FX + 230, FY + 90, 'nf-l1 dyn-tag', 'start', when=O('lip'))
add(f'<path d="M{FX} {FY - 30} V{FY + 40}" style="stroke:var(--bad);stroke-width:6;stroke-dasharray:6 6"/>', when=O('palate', 'pierre'))
text('palatine shelves don’t fuse', FX + 230, FY + 30, 'nf-l1 dyn-tag', 'start', when=O('palate', 'pierre'))
text('tongue falls back — airway blocked', FX + 230, FY + 150, 'nf-l1 dyn-tag', 'start', when=O('pierre'))
# neck
NY = 950
add(f'<rect x="{FX - 120}" y="{NY - 120}" width="240" height="260" rx="40" class="dyn-soft"/>')
text('neck', FX, NY + 170, 'nf-l1', 'middle')
add(f'<path d="M{FX - 80} {NY - 100} L{FX - 40} {NY + 120}" style="stroke:var(--dk5);stroke-width:8;opacity:.6"/>')
text('SCM', FX - 140, NY - 80, 'nf-l2', 'end')
add(f'<circle cx="{FX}" cy="{NY}" r="30" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/>', when=O('tgd'))
text('midline — rises with swallowing or tongue out', FX + 150, NY, 'nf-l1 dyn-tag', 'start', when=O('tgd'))
add(f'<circle cx="{FX - 105}" cy="{NY + 20}" r="30" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/>', when=O('bcc'))
text('lateral, in front of SCM — doesn’t move', FX + 150, NY + 40, 'nf-l1 dyn-tag', 'start', when=O('bcc'))
text('thyroid: foramen cecum → down the neck', FX + 150, NY - 90, 'nf-l2', 'start')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = []
for i in range(4):
    y = AY0 + i * (AH + GAP) + AH // 2
    f = dict(d=f'M{AX1 - 60} 274 V{y}', len=y - 274, speed=90, r=8, base=dict(nc=2))
    if i == 0: f['mods'] = [m(O('treacher'), set=dict(nc=0))]
    flows.append(f)
flows.append(dict(d=f'M{AX0 + 520} 274 C1300 500 1260 900 1060 1110', len=950, speed=110, r=8, base=dict(nc=3),
                  mods=[m(O('digeorge'), set=dict(nc=1))]))
flows.append(dict(d=f'M{FX} {NY - 300} V{NY - 40}', len=260, speed=40, r=9, base=dict(thy=1)))
sites = [dict(x=AX1 + 20, y=PY3 - 40, n=[1, 0], w=10, t='rec', l='', aria='Pharyngeal apparatus', c='pharyngeal', ions=[]),
         dict(x=FX, y=FY + 110, n=[0, 1], w=10, t='rec', l='', aria='Cleft lip and palate', c='cleft', ions=[]),
         dict(x=FX + 30, y=NY + 90, n=[0, 1], w=10, t='rec', l='', aria='Neck cysts', c='neckcysts', ions=[])]

readouts = [
  dict(l='T cells', mods=[dict(when=O('digeorge'), d=-1)]),
  dict(l='Serum Ca²⁺', mods=[dict(when=O('digeorge'), d=-1)]),
  dict(l='Hearing', mods=[dict(when=O('treacher'), d=-1)]),
  dict(l='Airway trouble', mods=[dict(when=O('treacher', 'pierre'), d=1)]),
  dict(l='Feeding difficulty', mods=[dict(when=O('pierre'), d=1)]),
]

notes = {
  '': 'Clefts (ectoderm) outside, arches (mesoderm + neural crest) in the middle, pouches (endoderm) inside — CAP. Arches: chew, '
      'smile, swallow, speak. Pouches, bottom to top: the ear, the tonsils, then the thymus and inferior parathyroids (3rd) and the '
      'superior parathyroids (4th). Only the 1st cleft persists, as the external auditory meatus.',
  'dx:digeorge': 'DiGeorge (22q11.2 microdeletion): the 3rd and 4th pouches fail — no thymus (T-cell defect, recurrent viral and fungal '
                 'infection) and no parathyroids (neonatal tetany) — plus conotruncal heart defects from neural crest. CATCH-22.',
  'dx:treacher': 'Treacher Collins: a neural crest disorder that under-builds the 1st-arch face — zygomatic and mandibular hypoplasia, '
                 'hearing loss, airway compromise.',
  'dx:pierre': 'Pierre Robin sequence: micrognathia → the tongue falls back (glossoptosis) → cleft palate and airway obstruction; '
               'feeding difficulty.',
  'dx:lip': 'Cleft lip: the intermaxillary segment (fused medial nasal processes) fails to fuse with the maxillary process — the '
            'primary palate.',
  'dx:palate': 'Cleft palate: the lateral palatine shelves fail to fuse with each other or with the nasal septum and primary palate — the '
               'secondary palate.',
  'dx:tgd': 'Thyroglossal duct cyst: the thyroid descends from the foramen cecum at the tongue base, trailing the duct — a midline neck '
            'mass that moves up with swallowing or tongue protrusion.',
  'dx:bcc': 'Pharyngeal cleft cyst: a persistent cervical sinus from the 2nd–4th clefts — a lateral neck mass in front of the '
            'sternocleidomastoid that does not move with swallowing.',
}

dyn = dict(
  kinds=dict(nc=['nc', '--dk7'], thy=['nc', '--dk5']), groups=[['nc', 'Migrating cells (neural crest · thyroid)']],
  switches=[dict(id='dx', label='What goes wrong', type='one', options=[
    ['digeorge', 'DiGeorge syndrome', 'digeorge'], ['treacher', 'Treacher Collins', 'treacher'],
    ['pierre', 'Pierre Robin sequence', 'treacher'], ['lip', 'Cleft lip', 'cleft'], ['palate', 'Cleft palate', 'cleft'],
    ['tgd', 'Thyroglossal duct cyst', 'neckcysts'], ['bcc', 'Pharyngeal cleft cyst', 'neckcysts']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 114, 330, 637–639 · Langman ch 17')

MAP = dict(
  id='archsim', title='Pharyngeal Arches in Motion', topic='devrepro', after='embryo',
  sub='Clefts outside, arches in the middle, pouches inside: watch neural crest fill the arches, see what each arch, pouch and cleft '
      'becomes, then break one — DiGeorge, Treacher Collins, Pierre Robin, cleft lip and palate, and the two neck cysts',
  w=3600, h=1900,
  fa='114, 330, 364, 501, 527, 637, 638, 639',
  src=['Langman ch 17 — Head and Neck', 'Moore ch 8 — Neck', 'Moore ch 10 — Cranial Nerves', 'Moore ch 9 — Head',
       'Langman ch 9 — Birth Defects and Prenatal Diagnosis', 'Robbins ch 16 — Head and neck', 'Bootcamp.com Gastroenterology — Oral Cavity'],
  lanes=[('arNorm', 'The pharyngeal apparatus', 'glycolysis'), ('arDz', 'Arch and pouch defects', 'tca'), ('arFace', 'Face and neck', 'gluconeo')],
  nodes=[
    ('ar1', 'Arches, pouches & clefts', 330, 1620, 'arNorm', 'CAP · chew smile swallow speak', ['pharyngeal'], 'hub'),
    ('ar2', 'Tongue development', 760, 1620, 'arNorm', 'V3/IX touch, VII/IX taste', ['tongueanat']),
    ('ar3', 'DiGeorge syndrome', 1200, 1620, 'arDz', 'CATCH-22', ['digeorge']),
    ('ar4', 'Treacher Collins · Robin', 1640, 1620, 'arDz', '1st arch under-built', ['treacher']),
    ('ar5', 'Cleft lip · cleft palate', 760, 1760, 'arFace', 'which processes', ['cleft']),
    ('ar6', 'Neck cysts', 1200, 1760, 'arFace', 'midline vs lateral', ['neckcysts'])],
  panels=[
    (2500, PANY, 1000, 'Arch → nerve → what it builds (First Aid p. 637)', [
      ('1st', 'CN V3 — mastication, malleus, incus'),
      ('2nd', 'CN VII — facial expression, stapes, styloid'),
      ('3rd', 'CN IX — stylopharyngeus, greater hyoid horn'),
      ('4th & 6th', 'CN X — constrictors, larynx muscles, cartilages')])],
  dyn=dyn)
