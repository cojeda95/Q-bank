# The Orbit & Tears in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Left: the right orbit seen from the front — thick lateral wall, paper-thin medial wall and floor, the roof under the frontal
# lobe, the apex with the optic canal and the superior orbital fissure, the lacrimal gland and the tear drainage path to the
# inferior meatus. An `orb` switch fractures the floor and medial wall (blowout), or damages the fissure or the whole apex and
# shows which nerves stop working; a `blk` toggle blocks the nasolacrimal duct. Right: the front of the eye and a slice of
# cornea, where an `eye` switch adds a sty, a chalazion, sebaceous carcinoma, a pterygium, keratoconus or Fuchs dystrophy.
# Schematic. 5 readouts. Facts from the pinned cards (Moore ch 9, Robbins ch 29); FA page in `fa`. No new cards.
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

O = lambda *k: [f'orb:{x}' for x in k]
E = lambda *k: [f'eye:{x}' for x in k]
PANY = 1180
OX, OY = 760, 760        # orbit centre (patient's right orbit, front view: lateral = viewer's left, nose = viewer's right)

text('The orbit & tears — thin walls, a crowded apex, a tear path to the nose, and the front of the eye', 180, 150, 'dyn-big')
text('right orbit seen from the front (lateral on the left, nose on the right) · front of the eye and a slice of cornea on the right · schematic', 180, 176, 'dyn-cap')
WALL = dict(roof=(f'M{OX - 330} {OY - 300} Q{OX} {OY - 420} {OX + 330} {OY - 300}', '--dk5', 26, 'roof · frontal bone (frontal lobe above)', OX, OY - 440),
            lat=(f'M{OX - 330} {OY - 300} Q{OX - 420} {OY} {OX - 330} {OY + 300}', '--dk11', 46, 'lateral · zygomatic + greater wing: strongest', OX - 380, OY + 380),
            floor=(f'M{OX - 330} {OY + 300} Q{OX} {OY + 380} {OX + 330} {OY + 300}', '--dk9', 10, 'floor · maxilla: thin (maxillary sinus below)', OX, OY + 400),
            med=(f'M{OX + 330} {OY - 300} Q{OX + 360} {OY} {OX + 330} {OY + 300}', '--dk3', 8, 'medial · ethmoid: paper-thin', OX + 380, OY - 60))
for k, (d, c, w, l, tx, ty) in WALL.items():
    add(f'<path d="{d}" style="fill:none;stroke:var({c});stroke-width:{w};stroke-linecap:round"/>')
    text(l, tx, ty, 'nf-l2', 'end' if k == 'lat' else ('start' if k == 'med' else 'middle'))
text('nose →', OX + 520, OY + 120, 'nf-l1')
# apex
add(f'<circle cx="{OX + 60}" cy="{OY - 20}" r="34" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:4"/>')
text('optic canal: II + ophthalmic a.', OX + 110, OY - 60, 'nf-l2')
add(f'<path d="M{OX + 20} {OY + 40} Q{OX - 80} {OY + 30} {OX - 200} {OY - 80}" style="fill:none;stroke:var(--ink-3);stroke-width:18;stroke-linecap:round;opacity:.5"/>')
text('superior orbital fissure: III, IV, V1, VI, ophthalmic vv.', OX - 210, OY - 110, 'nf-l2', 'middle')
add(f'<path d="M{OX + 20} {OY + 90} Q{OX - 100} {OY + 140} {OX - 220} {OY + 160}" style="fill:none;stroke:var(--ink-3);stroke-width:12;stroke-linecap:round;opacity:.3"/>')
text('inferior orbital fissure', OX - 100, OY + 200, 'nf-l2', 'middle')
# fractures and lesions
add(f'<path d="M{OX - 120} {OY + 330} l40 30 l30 -40 l40 40 l30 -30" style="fill:none;stroke:var(--bad);stroke-width:8"/>', when=O('blow'))
add(f'<path d="M{OX + 340} {OY - 80} l-20 40 l30 30 l-20 40" style="fill:none;stroke:var(--bad);stroke-width:8"/>', when=O('blow'))
add(f'<ellipse cx="{OX}" cy="{OY + 120}" rx="200" ry="90" style="fill:var(--nf-blood);opacity:.3"/>', when=O('blow'))
text('blood in the orbit → eye pushed forward', OX, OY + 270, 'nf-l1', 'middle', when=O('blow'))
# FA 555: floor fracture can trap the inferior rectus / orbital fat and injure the infraorbital nerve (V2, in the floor — Moore ch 9)
add(f'<path d="M{OX - 80} {OY + 345} q30 70 70 0" style="fill:var(--dk4);fill-opacity:.55;stroke:var(--bad);stroke-width:4"/>', when=O('blow'))
text('inferior rectus / fat caught in the crack · infraorbital n. (V2) at risk', OX, OY + 475, 'nf-l1', 'middle', when=O('blow'))
add(f'<path d="M{OX + 20} {OY + 40} Q{OX - 80} {OY + 30} {OX - 200} {OY - 80}" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-linecap:round;opacity:.7"/>', when=O('sof', 'apex'))
add(f'<circle cx="{OX + 60}" cy="{OY - 20}" r="40" style="fill:var(--bad);opacity:.5"/>', when=O('apex'))
# lacrimal apparatus
add(f'<ellipse cx="{OX - 230}" cy="{OY - 230}" rx="80" ry="40" transform="rotate(-25 {OX - 230} {OY - 230})" style="fill:var(--dk6);fill-opacity:.3;stroke:var(--dk6);stroke-width:4"/>')
text('lacrimal gland', OX - 230, OY - 160, 'nf-l2', 'middle')
DRAIN = f'M{OX + 300} {OY + 40} C{OX + 400} {OY + 40} {OX + 460} {OY + 100} {OX + 460} {OY + 200} V{OY + 520} L{OX + 420} {OY + 600}'
add(f'<path d="{DRAIN}" style="fill:none;stroke:var(--dk6);stroke-width:14;opacity:.4;stroke-linecap:round"/>')
text('puncta → canaliculi → sac', OX + 480, OY + 200, 'nf-l2'); text('nasolacrimal duct → inferior meatus', OX + 480, OY + 560, 'nf-l2')
add(f'<path d="M{OX + 430} {OY + 380} h60" style="stroke:var(--bad);stroke-width:14"/>', when=['blk'])
# front of the eye
EX, EY = 1900, 600
add(f'<path d="M{EX - 300} {EY} Q{EX} {EY - 220} {EX + 300} {EY} Q{EX} {EY + 220} {EX - 300} {EY} Z" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:5"/>')
add(f'<circle cx="{EX}" cy="{EY}" r="110" style="fill:var(--dk1);fill-opacity:.25;stroke:var(--dk1);stroke-width:4"/>')
add(f'<circle cx="{EX}" cy="{EY}" r="40" style="fill:var(--ink);opacity:.8"/>')
text('front of the eye (nose side on the right)', EX, EY - 220, 'nf-l1', 'middle')
add(f'<path d="M{EX + 300} {EY} L{EX + 110} {EY - 50} L{EX + 110} {EY + 50} Z" style="fill:var(--nf-blood);fill-opacity:.4;stroke:var(--bad);stroke-width:3"/>', when=E('pter'))
add(f'<circle cx="{EX - 80}" cy="{EY - 150}" r="34" style="fill:var(--bad);opacity:.6"/>', when=E('hord'))
add(f'<circle cx="{EX + 60}" cy="{EY - 130}" r="30" style="fill:var(--dk10);opacity:.6;stroke:var(--ink-2);stroke-width:2"/>', when=E('chal'))
add(f'<path d="M{EX - 300} {EY} Q{EX} {EY - 220} {EX + 300} {EY}" style="fill:none;stroke:var(--bad);stroke-width:24;opacity:.5"/>', when=E('seb'))
# cornea slice
CX, CY = 1650, 1050
LAY = [('epithelium', 30, '--dk9'), ('Bowman layer', 10, '--dk11'), ('stroma', 80, '--dk1'), ('Descemet', 8, '--dk4'), ('endothelium', 14, '--dk6')]
y, ly = CY, CY - 40
for l, h, c in LAY:
    ly = max(ly + 30, y + h / 2 + 6)
    add(f'<rect x="{CX}" y="{y}" width="500" height="{h}" style="fill:var({c});fill-opacity:.3"/>'); text(l, CX + 520, ly, 'nf-l2'); y += h
text('cornea, slice', CX, CY - 20, 'nf-l1')
add(f'<path d="M{CX + 220} {CY + 30} v10 m40 -10 v10" style="stroke:var(--bad);stroke-width:8"/>', when=E('kc'))
add(f'<path d="M{CX + 150} {CY} Q{CX + 250} {CY + 60} {CX + 350} {CY}" style="fill:var(--surface);opacity:.9"/>', when=E('kc'))
for i in range(6):
    add(f'<circle cx="{CX + 60 + i * 75}" cy="{CY + 135}" r="9" style="fill:var(--dk4);opacity:.8"/>', when=E('fuchs'))
add(f'<rect x="{CX}" y="{CY + 40}" width="500" height="80" style="fill:var(--nf-h2o);opacity:.35"/>', when=E('fuchs'))
add(f'<path d="M{CX + 200} {CY} Q{CX + 250} {CY - 40} {CX + 320} {CY}" style="fill:var(--nf-blood);fill-opacity:.4;stroke:var(--bad);stroke-width:3"/>', when=E('pter'))
OTAG = dict(blow='blowout fracture — rim holds; thin floor (→ maxillary sinus) or medial wall (→ ethmoid, sphenoid sinuses) breaks',
            sof='superior orbital fissure — III, IV, VI: eye frozen, ptosis · V1: cornea numb',
            apex='orbital apex — the fissure plus the optic canal: add blindness (II and ophthalmic a.)')
for k, s in OTAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=O(k))
ETAG = dict(hord='hordeolum (sty) — infected gland at the lash line: painful, red, suppurative',
            chal='chalazion — blocked meibomian or Zeis gland leaks lipid: firm painless lipogranuloma',
            seb='sebaceous carcinoma — mimics a chalazion or blepharitis, pagetoid spread, to parotid & submandibular nodes',
            pter='pterygium — sun-damaged fibrovascular wedge from the limbus onto the cornea in the Bowman plane; never crosses the pupil',
            kc='keratoconus — thin cone, Bowman layer breaks: irregular astigmatism (Down, Marfan, atopy) · rigid lenses, transplant',
            fuchs='Fuchs dystrophy — endothelium lost, guttata on Descemet: stroma swells, ground-glass blur · transplant')
for k, s in ETAG.items(): text(s, 1100, 1520, 'nf-l1', 'middle', when=E(k))
text('duct blocked → tears overflow onto the cheek', 1100, 1560, 'nf-l1', 'middle', when=['blk'])

# ════════ motion ════════
TEAR = f'M{OX - 230} {OY - 230} C{OX - 100} {OY - 120} {OX + 150} {OY + 20} {OX + 300} {OY + 40}'
flows = [dict(d=TEAR, len=600, speed=90, r=8, base=dict(tear=3)),
         dict(d=DRAIN, len=750, speed=90, r=8, base=dict(tear=3), when=['!blk']),
         dict(d=f'M{OX + 300} {OY + 40} C{OX + 280} {OY + 200} {OX + 320} {OY + 300} {OX + 300} {OY + 420}', len=400, speed=70, r=8,
              base=dict(tear=3), when=['blk']),
         dict(d=f'M{OX - 200} {OY - 80} Q{OX - 80} {OY + 30} {OX + 20} {OY + 40}', len=300, speed=80, r=7, base=dict(sig=3), when=['!orb:sof&!orb:apex'])]
sites = [dict(x=OX - 120, y=OY + 440, n=[-1, 1], w=10, t='rec', l='', aria='Orbital walls', c='orbitwalls', ions=[]),
         dict(x=OX - 20, y=OY - 180, n=[-1, -1], w=10, t='rec', l='', aria='Orbital apex', c='orbitapex', ions=[]),
         dict(x=OX + 560, y=OY + 380, n=[1, 1], w=10, t='rec', l='', aria='Lacrimal apparatus', c='lacrimal', ions=[]),
         dict(x=EX - 360, y=EY - 120, n=[-1, -1], w=10, t='rec', l='', aria='Eyelid lumps', c='lidlumps', ions=[]),
         dict(x=EX + 360, y=EY - 80, n=[1, -1], w=10, t='rec', l='', aria='Pterygium', c='pterygium', ions=[]),
         dict(x=CX - 60, y=CY + 80, n=[-1, 1], w=10, t='rec', l='', aria='Keratoconus & Fuchs dystrophy', c='corneadz', ions=[])]

readouts = [
  dict(l='Eye movements', mods=[dict(when=O('sof', 'apex'), d=-1)]),
  dict(l='Corneal sensation', mods=[dict(when=O('sof', 'apex'), d=-1)]),
  dict(l='Vision', mods=[dict(when=O('apex'), d=-1), dict(when=E('kc', 'fuchs'), d=-1), dict(when=E('pter'), d=0)]),
  dict(l='Tear overflow', mods=[dict(when=['blk'], d=1)]),
  dict(l='Lid pain', mods=[dict(when=E('hord'), d=1), dict(when=E('chal'), d=0)]),
]

notes = {
  '': 'The orbit is a four-walled pyramid with its apex behind. The lateral wall is the strongest; the medial wall (lamina papyracea of the '
      'ethmoid) and floor (maxilla) are thin. Tears from the superolateral lacrimal gland are blinked toward the medial canthus and drain to '
      'the inferior nasal meatus.',
  'orb:blow': 'Blowout fracture: a blow breaks the thin medial wall (into the ethmoid and sphenoid sinuses) or floor (into the maxillary '
              'sinus) while the rim holds. The floor is the classic site: the inferior rectus or orbital fat can be trapped in the crack, '
              'and the infraorbital nerve (V2, cheek and upper lip) injured. Bleeding in the orbit pushes the eye forward.',
  'orb:sof': 'The superior orbital fissure carries III, IV and VI to the eye muscles, the frontal, lacrimal and nasociliary branches of V1, '
             'and the ophthalmic veins to the cavernous sinus — a lesion gives ophthalmoplegia, ptosis and lost corneal sensation.',
  'orb:apex': 'The optic canal (lesser wing of the sphenoid) lies just medial to the fissure and carries II and the ophthalmic artery; '
              'add it and vision goes too. The recti arise from the common tendinous ring around the canal and part of the fissure.',
  'blk': 'Tear drainage: lacrimal lake → puncta → canaliculi → lacrimal sac → nasolacrimal duct → inferior meatus. Secretion is driven by '
         'CN VII parasympathetics via the pterygopalatine ganglion. Block the drainage, or make too much, and tears overflow.',
  'eye:hord': 'Hordeolum: acute infection or duct obstruction of a lid gland at the lash line — painful, red, suppurative.',
  'eye:chal': 'Chalazion: a blocked tarsal (meibomian) or Zeis gland leaks lipid into the lid → granulomatous lipogranuloma — small, firm, painless.',
  'eye:seb': 'Sebaceous carcinoma can pass for a chalazion or blepharitis; pagetoid spread; first to parotid and submandibular nodes; mortality '
             'up to 22%. Basal cell carcinoma is the most common lid malignancy (lower lid, medial canthus).',
  'eye:pter': 'Pinguecula and pterygium come from sun damage in the interpalpebral fissure. A pterygium is a fibrovascular wedge from the '
              'limbus onto the cornea in the Bowman plane; it does not cross the pupillary axis. Examine excised tissue.',
  'eye:kc': 'Keratoconus: noninflammatory thinning into a cone with Bowman layer breaks; a Descemet rupture floods the stroma (hydrops). '
            'Associated with Down, Marfan and atopy (eye rubbing).',
  'eye:fuchs': 'Fuchs endothelial dystrophy: endothelial cells are lost and leave guttata; the rest cannot pump the stroma dry → edema, '
               'bullous keratopathy. A leading reason for corneal transplant.',
}

dyn = dict(
  kinds=dict(tear=['mov', '--dk6'], sig=['mov', '--dk7']), groups=[['mov', 'Tears · nerve signal']],
  switches=[dict(id='orb', label='Orbit', type='one', options=[
              ['blow', 'Blowout fracture', 'orbitwalls'], ['sof', 'Superior orbital fissure lesion', 'orbitapex'], ['apex', 'Orbital apex lesion', 'orbitapex']]),
            dict(id='blk', label='Tear duct', type='toggle', on='Duct blocked', off='Block the duct', def_=False),
            dict(id='eye', label='Lid & cornea', type='one', options=[
              ['hord', 'Hordeolum (sty)', 'lidlumps'], ['chal', 'Chalazion', 'lidlumps'], ['seb', 'Sebaceous carcinoma', 'lidlumps'],
              ['pter', 'Pterygium', 'pterygium'], ['kc', 'Keratoconus', 'corneadz'], ['fuchs', 'Fuchs dystrophy', 'corneadz']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 518, 555, 557, 559 · Moore ch 9 · Robbins ch 29')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='orbitsim', title='The Orbit & Tears in Motion', topic='eent', after='anteye',
  sub='Break the thin orbital floor, damage the superior orbital fissure or the whole apex, block the tear duct — then put a sty, a chalazion, '
      'a pterygium, keratoconus or Fuchs dystrophy on the front of the eye',
  w=3600, h=1900,
  fa='518, 555, 557, 559',
  src=['Moore ch 9 — Head', 'Robbins ch 29 — The eye'],
  lanes=[('obOrb', 'Orbit & tears', 'tca'), ('obEye', 'Lid & cornea', 'glycolysis')],
  nodes=[
    ('ob1', 'Orbital walls', 260, 1720, 'obOrb', 'blowout', ['orbitwalls'], 'hub'),
    ('ob2', 'Orbital apex', 620, 1720, 'obOrb', 'canal · fissure', ['orbitapex']),
    ('ob3', 'Lacrimal apparatus', 980, 1720, 'obOrb', 'gland → meatus', ['lacrimal']),
    ('ob4', 'Eyelid lumps', 1340, 1720, 'obEye', 'sty · chalazion', ['lidlumps']),
    ('ob5', 'Pterygium', 1700, 1720, 'obEye', 'sun · limbus', ['pterygium']),
    ('ob6', 'Keratoconus & Fuchs', 2060, 1720, 'obEye', 'Bowman · endothelium', ['corneadz'])],
  panels=[
    (2500, PANY, 1000, 'Through the apex (Moore ch 9)', [
      ('Optic canal', 'II, ophthalmic artery'), ('Superior orbital fissure', 'III, IV, V1, VI, ophthalmic veins'),
      ('Inferior orbital fissure', 'V2 → infraorbital n. in the floor'), ('Tears end in', 'inferior nasal meatus')])],
  dyn=dyn)
