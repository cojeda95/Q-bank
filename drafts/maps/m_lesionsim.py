# Skin Lesions Drawn to Scale (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A long cross-section of skin with a 1 cm ruler. One `one` switch draws the chosen lesion word in profile — flat
# (macule, patch), raised and solid (papule, nodule, plaque), fluid-filled (vesicle, bulla, pustule), transient
# (wheal) and the surface changes (scale, crust, erosion, ulcer, lichenification) — with its classic examples.
# Readouts: elevation, larger than 1 cm, fluid-filled, below the basement membrane. Every word and example is from
# the pinned cards (lesprim, lessec, skinlayers, dermmicro); their FA pages are in `fa`. No new cards.
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


SW = 'les'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 700

# ════════ the skin ════════
box(160, 130, 2340, 1240)
text('One lesion word at a time — in profile, to scale', 190, 170, 'dyn-big')
text('flat or raised? solid or fluid? smaller or larger than 1 cm?', 190, 196, 'dyn-cap')
X0, X1, SURF, BMY, DERM = 300, 2240, 640, 720, 960
CX = 1270
add(f'<rect x="{X0}" y="{SURF}" width="{X1 - X0}" height="{BMY - SURF}" style="fill:var(--dk4);fill-opacity:.22"/>', unless=O('lich'))
add(f'<rect x="{X0}" y="{BMY}" width="{X1 - X0}" height="{DERM - BMY}" style="fill:var(--dk1);fill-opacity:.14"/>')
add(f'<path d="M{X0} {BMY} H{X1}" style="stroke:var(--dk11);stroke-width:4"/>')
add(f'<path d="M{X0} {SURF} H{X1}" style="stroke:var(--ink-3);stroke-width:3"/>', unless=O('pap', 'nod', 'plq', 'ves', 'bul', 'pus', 'whl', 'ero', 'ulc', 'lich'))
text('Epidermis', X0 - 16, 686, 'nf-l2', 'end')
text('Dermis', X0 - 16, 850, 'nf-l2', 'end')
text('basement membrane', X1, BMY + 26, 'nf-l2', 'end')
# 1 cm ruler (300 px)
add(f'<path d="M{CX - 150} 1060 H{CX + 150} M{CX - 150} 1046 V1074 M{CX + 150} 1046 V1074" style="stroke:var(--ink);stroke-width:4"/>')
text('1 cm', CX, 1100, 'nf-l1', 'middle')

def surface_with(bump):
    """the skin surface with a bump (or dip) in the middle: bump = (half-width, height; negative = dip)"""
    hw, h = bump
    return f'M{X0} {SURF} H{CX - hw} C{CX - hw * .6} {SURF - h} {CX + hw * .6} {SURF - h} {CX + hw} {SURF} H{X1}'
FILL = dict(solid='fill:var(--dk4);fill-opacity:.55', fluid='fill:var(--nf-h2o);fill-opacity:.55', pus='fill:var(--dk5);fill-opacity:.7',
            edema='fill:var(--bad);fill-opacity:.22')
def raised(key, hw, h, kind, deep=0):
    d = surface_with((hw, h))
    add(f'<path d="M{CX - hw} {SURF} C{CX - hw * .6} {SURF - h} {CX + hw * .6} {SURF - h} {CX + hw} {SURF} '
        f'C{CX + hw * .6} {SURF + deep} {CX - hw * .6} {SURF + deep} {CX - hw} {SURF} Z" style="{FILL[kind]};stroke:none"/>', when=O(key))
    add(f'<path d="{d}" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=O(key))
# flat: macule ≤ 1 cm, patch > 1 cm
add(f'<rect x="{CX - 110}" y="{SURF}" width="220" height="26" style="fill:var(--dk8);fill-opacity:.6"/>', when=O('mac'))
add(f'<rect x="{CX - 420}" y="{SURF}" width="840" height="26" style="fill:var(--dk8);fill-opacity:.6"/>', when=O('pat'))
# raised and solid
raised('pap', 120, 90, 'solid')
raised('nod', 360, 200, 'solid', deep=220)
add(f'<path d="M{X0} {SURF} H{CX - 480} V{SURF - 70} H{CX + 480} V{SURF} H{X1}" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=O('plq'))
add(f'<rect x="{CX - 480}" y="{SURF - 70}" width="960" height="70" style="{FILL["solid"]}"/>', when=O('plq'))
# fluid-filled
raised('ves', 120, 100, 'fluid')
raised('bul', 400, 180, 'fluid')
raised('pus', 120, 100, 'pus')
# wheal: raised, pink, dermal edema
raised('whl', 380, 70, 'edema')
add(f'<ellipse cx="{CX}" cy="{(BMY + DERM) // 2}" rx="420" ry="90" style="fill:var(--bad);fill-opacity:.14"/>', when=O('whl'))
text('dermal edema', CX, (BMY + DERM) // 2 + 6, 'nf-l2', 'middle', when=O('whl'))
# surface changes
for i in range(9):
    x = CX - 360 + i * 90
    add(f'<path d="M{x} {SURF - 8} l60 -18 l10 12 l-60 18 Z" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2"/>', when=O('scl'))
add(f'<path d="M{CX - 300} {SURF} C{CX - 200} {SURF - 50} {CX + 200} {SURF - 46} {CX + 300} {SURF} Z" style="fill:var(--dk5);fill-opacity:.85"/>', when=O('crs'))
add(f'<path d="M{X0} {SURF} H{CX - 300} V{SURF + 44} H{CX + 300} V{SURF} H{X1}" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=O('ero'))
add(f'<rect x="{CX - 300}" y="{SURF}" width="600" height="44" style="fill:var(--surface)"/>', when=O('ero'))
add(f'<path d="M{X0} {SURF} H{CX - 300} L{CX - 200} {BMY + 140} H{CX + 200} L{CX + 300} {SURF} H{X1}" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=O('ulc'))
add(f'<path d="M{CX - 300} {SURF} L{CX - 200} {BMY + 140} H{CX + 200} L{CX + 300} {SURF} Z" style="fill:var(--surface)"/>', when=O('ulc'))
add(f'<rect x="{X0}" y="{SURF - 40}" width="{X1 - X0}" height="{BMY - SURF + 40}" style="fill:var(--dk4);fill-opacity:.32"/>', when=O('lich'))
for i in range(14):
    x = X0 + 80 + i * 130
    add(f'<path d="M{x} {SURF - 40} l40 40 l40 -40" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>', when=O('lich'))

# the word, its rule and its examples
W = dict(
  mac=('Macule', 'flat color change, ≤ 1 cm', 'freckle · solar lentigo'),
  pat=('Patch', 'flat color change, > 1 cm', 'vitiligo · port-wine stain'),
  pap=('Papule', 'elevated and solid, ≤ 1 cm', 'acne · molluscum'),
  nod=('Nodule', 'elevated and solid, > 1 cm', 'neurofibroma'),
  plq=('Plaque', 'elevated and flat-topped, usually > 1 cm', 'psoriasis'),
  ves=('Vesicle', 'fluid-filled blister, ≤ 1 cm', 'varicella · zoster · herpes simplex'),
  bul=('Bulla', 'fluid-filled blister, > 1 cm', 'bullous pemphigoid · pemphigus · burns'),
  pus=('Pustule', 'pus-filled', 'acne · folliculitis · pustular psoriasis'),
  whl=('Wheal', 'itchy, transient, raised and pink — dermal edema', 'urticaria · insect bites'),
  scl=('Scale', 'flakes of thickened stratum corneum', 'psoriasis · eczema · actinic keratosis'),
  crs=('Crust', 'dried exudate on the surface', 'honey-colored in impetigo'),
  ero=('Erosion', 'epidermis lost — basement membrane not exposed', 'partial or full loss of epidermis'),
  ulc=('Ulcer', 'tissue lost through the basement membrane into dermis or deeper', 'arterial and decubitus ulcers'),
  lich=('Lichenification', 'thick, rough skin with exaggerated markings', 'lichen simplex chronicus'),
)
for k, (a, b, c) in W.items():
    text(a, 190, 300, 'dyn-big', when=O(k)); text(b, 190, 330, 'nf-l1', when=O(k)); text(c, 190, 356, 'nf-l2', when=O(k))
text('pick a lesion word on the right', 190, 320, 'nf-l1', unless=[f'{SW}:*'])

# fluid moving inside the blisters; edema in the dermis
flows = [
  dict(d=f'M{CX - 70} {SURF - 40} H{CX + 70} H{CX - 70}', len=280, speed=60, r=6, base=dict(fl=3), when=O('ves', 'pus')),
  dict(d=f'M{CX - 300} {SURF - 70} H{CX + 300} H{CX - 300}', len=1200, speed=90, r=7, base=dict(fl=8), when=O('bul')),
  dict(d=f'M{CX - 360} {(BMY + DERM) // 2 + 40} H{CX + 360} H{CX - 360}', len=1440, speed=80, r=6, base=dict(fl=8), when=O('whl')),
]
sites = [dict(x=X1 - 140, y=BMY, n=[0, 1], w=10, t='wall', l='', aria='Basement membrane — erosion vs ulcer', c='lessec', ions=[])]

# ════════ readouts ════════
readouts = [
  dict(l='Above the skin surface', mods=[dict(when=O('pap', 'nod', 'plq', 'ves', 'bul', 'pus', 'whl'), d=1), dict(when=O('mac', 'pat'), d=0),
                                         dict(when=O('ero', 'ulc'), d=-1)]),
  dict(l='Larger than 1 cm', mods=[dict(when=O('pat', 'nod', 'plq', 'bul'), d=1), dict(when=O('mac', 'pap', 'ves'), d=-1)]),
  dict(l='Fluid-filled', mods=[dict(when=O('ves', 'bul', 'pus'), d=1), dict(when=O('mac', 'pat', 'pap', 'nod', 'plq'), d=-1)]),
  dict(l='Below the basement membrane', mods=[dict(when=O('ulc'), d=1), dict(when=O('ero'), d=-1)]),
]

notes = {
  '': 'Most lesion words answer two questions — flat or raised, solid or fluid-filled — and the 1 cm mark splits the small word '
      'from the large one. The surface words say what happened on top: shedding, drying, scratching or tissue loss.',
  'les:mac': 'Macule: a flat, circumscribed color change up to 1 cm — a freckle or solar lentigo.',
  'les:pat': 'Patch: the same flat color change, larger than 1 cm — vitiligo, a port-wine stain.',
  'les:pap': 'Papule: an elevated, solid lesion up to 1 cm — acne, molluscum.',
  'les:nod': 'Nodule: an elevated, solid lesion larger than 1 cm — a neurofibroma.',
  'les:plq': 'Plaque: elevated and flat-topped, usually larger than 1 cm, often from coalescing papules — psoriasis.',
  'les:ves': 'Vesicle: a fluid-filled blister up to 1 cm — varicella, zoster, herpes simplex.',
  'les:bul': 'Bulla: a fluid-filled blister larger than 1 cm — bullous pemphigoid, pemphigus, burns.',
  'les:pus': 'Pustule: a pus-filled blister — acne, folliculitis, pustular psoriasis.',
  'les:whl': 'Wheal: an itchy, transient, raised pink lesion from dermal edema — urticaria, insect bites.',
  'les:scl': 'Scale: dry white-silver plates of thickened stratum corneum from imperfect cornification — psoriasis, eczema, '
             'actinic keratosis, squamous cell carcinoma.',
  'les:crs': 'Crust: dried exudate or secretions — honey-colored in impetigo; also atopic dermatitis and scabs.',
  'les:ero': 'Erosion: loss of epidermis without exposing the basement membrane.',
  'les:ulc': 'Ulcer: tissue loss that exposes the basement membrane and dermis — even muscle, bone or tendon — as in arterial and '
             'decubitus ulcers.',
  'les:lich': 'Lichenification: thickened, rough skin with exaggerated markings from repeated rubbing or scratching — lichen simplex '
              'chronicus.',
}

dyn = dict(
  kinds=dict(fl=['fl', '--nf-h2o']), groups=[['fl', 'Fluid']],
  switches=[dict(id=SW, label='Lesion word', type='one', options=[
    ['mac', 'Macule', 'lesprim'], ['pat', 'Patch', 'lesprim'], ['pap', 'Papule', 'lesprim'], ['nod', 'Nodule', 'lesprim'],
    ['plq', 'Plaque', 'lesprim'], ['ves', 'Vesicle', 'lesprim'], ['bul', 'Bulla', 'lesprim'], ['pus', 'Pustule', 'lesprim'],
    ['whl', 'Wheal', 'lesprim'], ['scl', 'Scale', 'lessec'], ['crs', 'Crust', 'lessec'], ['ero', 'Erosion', 'lessec'],
    ['ulc', 'Ulcer', 'lessec'], ['lich', 'Lichenification', 'lessec']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 481, 483, 487')

MAP = dict(
  id='lesionsim', title='Skin Lesions Drawn to Scale', topic='msk', after='skinbasics',
  sub='Pick a lesion word and see it drawn in profile against a 1 cm ruler — macule to nodule, vesicle to wheal, scale to '
      'ulcer — with the classic examples; the readouts ask raised, over 1 cm, fluid-filled, below the basement membrane',
  w=3500, h=1560,
  fa='481, 483, 487',
  src=[full('Robbins', 25), full('Pawlina', 15)],
  lanes=[('lsPrim', 'Primary lesions', 'glycolysis'), ('lsSec', 'Surface changes', 'tca'), ('lsSkin', 'The skin', 'gluconeo')],
  nodes=[
    ('ls1', 'Lesion morphology', 330, 1340, 'lsPrim', 'flat · raised · fluid', ['lesprim'], 'hub'),
    ('ls2', 'Surface changes', 760, 1340, 'lsSec', 'scale · crust · ulcer', ['lessec']),
    ('ls3', 'Epidermal layers', 1180, 1340, 'lsSkin', 'basale to corneum', ['skinlayers']),
    ('ls4', 'Microscopic terms', 1600, 1340, 'lsSkin', 'hyperkeratosis …', ['dermmicro']),
    ('ls5', 'Psoriasis', 330, 1470, 'lsPrim', 'plaque with scale', ['psoriasis']),
    ('ls6', 'Impetigo · cellulitis', 760, 1470, 'lsSec', 'honey crust', ['skininfect'])],
  panels=[
    (2420, PANY, 1000, 'Small word · large word (First Aid p. 483)', [
      ('Flat', 'macule · patch'),
      ('Raised, solid', 'papule · nodule (plaque: flat-topped)'),
      ('Fluid', 'vesicle · bulla'),
      ('Pus', 'pustule'),
      ('Transient', 'wheal')])],
  dyn=dyn)
