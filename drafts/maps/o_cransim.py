# Cranial Mechanism in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The sphenoid and occiput at the sphenobasilar synchondrosis (SBS), schematic, in three views: from the side (flexion and
# extension about two transverse axes), from behind (torsion and rotation about the anteroposterior axis) and from above
# (side bending, lateral strain). A `steps` switch (auto) breathes the SBS through flexion and extension; a `one` switch
# shows the strain patterns (torsion, side bending/rotation, compression, superior/inferior vertical, lateral) and a second
# the techniques (CV4, V-spread, venous sinus drainage, condylar decompression) with the CSF fluctuation moving. 3 readouts.
# Facts from the pinned cards (Atlas of Osteopathic Techniques ch 18, OCOM OMM); no First Aid pages. No new cards.
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

S = lambda *k: [f'st:{x}' for x in k]
T = lambda *k: [f'tx:{x}' for x in k]
FLEX, EXT = ['ph:flex'], ['ph:ext']
PANY = 1180
SPH = 'fill:var(--dk2);fill-opacity:.25;stroke:var(--dk2);stroke-width:4'
OCC = 'fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:4'
def rot(svg, ang, cx, cy): return f'<g transform="rotate({ang} {cx} {cy})">{svg}</g>'
def panel(x0, y0, x1, y1, t): add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="36" class="dyn-soft"/>'); text(t, x0 + 30, y0 + 44, 'nf-l1')
NONPHYS = S('comp', 'vsup', 'vinf', 'lat')

text('The cranial mechanism — motion named at the sphenobasilar synchondrosis', 180, 150, 'dyn-big')
text('schematic bones · the sphenoid (front) meets the occiput (back) at the SBS', 180, 176, 'dyn-cap')

# ════════ side view: flexion / extension ════════
panel(300, 230, 1300, 820, 'From the side — flexion and extension')
SX, OX, BY = 620, 980, 560                     # sphenoid axis, occiput axis (foramen magnum level), SBS height
SPHS = f'<path d="M{SX - 200} {BY - 60} L{SX + 120} {BY - 30} L{SX + 160} {BY + 20} L{SX - 180} {BY + 40} Z" style="{SPH}"/>'
OCCS = f'<path d="M{OX - 160} {BY + 20} L{OX - 120} {BY - 30} C{OX + 40} {BY - 200} {OX + 220} {BY - 120} {OX + 240} {BY + 80} L{OX + 60} {BY + 120} Z" style="{OCC}"/>'
for ang, when in ((0, None), (-8, FLEX), (8, EXT)):
    u = FLEX + EXT if ang == 0 else None
    add(rot(SPHS, ang, SX, BY), when=when, unless=u if when is None else None)
    add(rot(OCCS, -ang, OX, BY), when=when, unless=u if when is None else None)
for x in (SX, OX): add(f'<circle cx="{x}" cy="{BY}" r="9" style="fill:var(--ink-2)"/>')
text('sphenoid', SX - 60, BY + 110, 'nf-l1', 'middle'); text('occiput', OX + 80, BY + 170, 'nf-l1', 'middle')
text('SBS', (SX + OX) // 2 + 20, BY - 70, 'nf-l1', 'middle')
add(f'<path d="M{(SX + OX) // 2 + 20} {BY - 56} V{BY - 10}" style="stroke:var(--ink-3);stroke-width:2"/>')
text('• = transverse axes (body of the sphenoid · foramen magnum)', 800, 790, 'nf-l2', 'middle')
text('flexion: SBS rises · skull widens, shortens front to back', 800, 300, 'nf-l1 dyn-tag', 'middle', when=FLEX)
text('extension: SBS drops · skull narrows, lengthens', 800, 300, 'nf-l1 dyn-tag', 'middle', when=EXT)
add(f'<rect x="{SX + 100}" y="{BY - 50}" width="140" height="90" rx="10" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:4"/>', when=S('comp'))
text('compression — rock hard, no motion', 800, 340, 'nf-l1 dyn-tag', 'middle', when=S('comp'))
# vertical strain: same-direction rotation about the transverse axes
for st, ang in (('vsup', -10), ('vinf', 10)):
    add(rot(SPHS, ang, SX, BY) + rot(OCCS, ang, OX, BY), when=S(st))
text('superior vertical: basisphenoid up — same-direction rotation', 800, 340, 'nf-l1 dyn-tag', 'middle', when=S('vsup'))
text('inferior vertical: basisphenoid down', 800, 340, 'nf-l1 dyn-tag', 'middle', when=S('vinf'))

# ════════ from behind: torsion, rotation ════════
panel(300, 880, 1300, 1450, 'From behind — anteroposterior axis')
CX, CY = 800, 1180
WING = f'<path d="M{CX - 300} {CY - 60} L{CX + 300} {CY - 60} L{CX + 260} {CY - 10} L{CX - 260} {CY - 10} Z" style="{SPH}"/>'
SQU = f'<path d="M{CX - 260} {CY + 20} C{CX - 200} {CY + 200} {CX + 200} {CY + 200} {CX + 260} {CY + 20} Z" style="{OCC}"/>'
add(WING + SQU, unless=S('tors', 'sbr'))
add(rot(WING, -10, CX, CY) + rot(SQU, 10, CX, CY), when=S('tors'))
add(rot(WING, 8, CX, CY) + rot(SQU, 8, CX, CY), when=S('sbr'))
add(f'<circle cx="{CX}" cy="{CY}" r="9" style="fill:var(--ink-2)"/>')
text('greater wings (sphenoid)', CX, CY - 90, 'nf-l2', 'middle'); text('occipital squama', CX, CY + 230, 'nf-l2', 'middle')
text('right torsion: right greater wing up, right occiput down — opposite rotation', CX, 940, 'nf-l1 dyn-tag', 'middle', when=S('tors'))
text('rotation: both turn the same way, dropping on the convex side', CX, 940, 'nf-l1 dyn-tag', 'middle', when=S('sbr'))

# ════════ from above: side bending, lateral strain ════════
panel(1350, 230, 2400, 1450, 'From above — vertical axes')
AX, AY = 1875, 840
SPT = f'<rect x="{AX - 120}" y="{AY - 320}" width="240" height="280" rx="40" style="{SPH}"/>'
OCT = f'<rect x="{AX - 140}" y="{AY + 40}" width="280" height="300" rx="80" style="{OCC}"/>'
add(SPT + OCT, unless=S('sbr', 'lat'))
add(rot(SPT, -8, AX, AY - 180) + rot(OCT, 8, AX, AY + 190), when=S('sbr'))
add(rot(SPT, 8, AX, AY - 180) + rot(OCT, 8, AX, AY + 190), when=S('lat'))
text('front (sphenoid)', AX, AY - 350, 'nf-l2', 'middle'); text('back (occiput)', AX, AY + 380, 'nf-l2', 'middle')
add(f'<path d="M{AX - 200} {AY} H{AX + 200}" style="stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 8"/>'); text('SBS', AX + 220, AY + 6, 'nf-l2')
text('side bending: opposite rotation — SBS closes on one side (concave), opens on the other', AX, 1310, 'nf-l1 dyn-tag', 'middle', when=S('sbr'))
text('named for the convex side', AX, 1340, 'nf-l2', 'middle', when=S('sbr'))
text('lateral strain: same-direction rotation — a parallelogram head', AX, 1310, 'nf-l1 dyn-tag', 'middle', when=S('lat'))
text('named for the side the basisphenoid shifts to', AX, 1340, 'nf-l2', 'middle', when=S('lat'))
text('nonphysiologic — trauma, birth, dental work', AX, 1380, 'nf-l1', 'middle', when=NONPHYS)
text('physiologic', AX, 1380, 'nf-l1', 'middle', when=S('tors', 'sbr'))

# techniques — a vault/occiput hand outline and the fluid wave
TT = dict(cv4='CV4: follow the occiput into extension, resist flexion until a still point, hold until the CRI returns',
          vs='V-spread: crossed thumbs near lambda, a fluid impulse from the opposite side spreads the suture',
          vsd='Venous sinus drainage: transverse → confluence → occipital → superior sagittal sinus → metopic suture',
          cond='Condylar decompression: cephalad + lateral at the occiput base, then OA decompression with a chin tuck')
for k, t in TT.items(): text(t, 1350, 1520, 'nf-l1', 'middle', when=T(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{SX - 60} {BY + 60} C{SX + 100} {BY + 200} {OX - 100} {BY + 200} {OX} {BY + 80}', len=520, speed=90, r=8, base=dict(csf=4),
       mods=[m(S('comp'), set=dict(csf=0)), m(T('cv4'), speed=0.3), m(T('vs'), set=dict(csf=7))]),
  dict(d=f'M{AX - 300} {AY - 100} C{AX - 300} {AY + 200} {AX + 300} {AY + 200} {AX + 300} {AY - 100}', len=900, speed=110, r=8,
       base=dict(csf=3), mods=[m(S('comp'), set=dict(csf=0)), m(T('cv4'), speed=0.3)]),
  dict(d=f'M{AX - 260} {AY + 260} H{AX + 260} M{AX} {AY + 260} V{AY + 340} M{AX} {AY + 340} V{AY - 340}', len=1000, speed=140, r=8,
       base=dict(ven=4), when=T('vsd')),
  dict(d=f'M{AX + 100} {AY - 250} L{AX - 40} {AY - 300}', len=150, speed=50, r=9, base=dict(csf=3), when=T('vs')),
]
sites = [dict(x=(SX + OX) // 2 + 20, y=BY, n=[0, 1], w=10, t='rec', l='', aria='Flexion and extension', c='sbsflexext', ions=[]),
         dict(x=CX, y=CY, n=[0, 1], w=10, t='rec', l='', aria='Torsion', c='sbstorsion', ions=[]),
         dict(x=AX, y=AY, n=[0, 1], w=10, t='rec', l='', aria='Primary respiratory mechanism', c='prm', ions=[])]

readouts = [
  dict(l='SBS motion', mods=[dict(when=S('comp'), d=-1)]),
  dict(l='CRI amplitude', mods=[dict(when=S('comp'), d=-1), dict(when=T('cv4'), d=1)]),
  dict(l='Venous outflow', mods=[dict(when=T('vsd'), d=1)]),
]

notes = {
  '': 'Sutherland’s primary respiratory mechanism has five parts: motility of the brain and cord, fluctuation of the CSF, mobility of '
      'the membranes, articular mobility of the cranial bones and involuntary motion of the sacrum between the ilia. It is palpated as '
      'the cranial rhythmic impulse (CRI) and named at the SBS.',
  'ph:flex': 'Flexion: sphenoid and occiput rotate in opposite directions about their transverse axes; the basisphenoid and basiocciput '
             'rise, the occipital squama and greater wings drop. Paired bones externally rotate; the skull widens and shortens. '
             'Inhalation favors flexion.',
  'ph:ext': 'Extension: the reverse — paired bones internally rotate; the skull narrows and lengthens front to back.',
  'st:tors': 'Torsion (physiologic): opposite rotation about an anteroposterior axis, named for the side of the elevated greater wing.',
  'st:sbr': 'Side bending/rotation (physiologic): opposite rotation about two vertical axes closes the SBS on one side; both bones also '
            'rotate the same way about the AP axis, dropping on the convex side. Named for the convexity.',
  'st:comp': 'Compression (nonphysiologic): basisphenoid and basiocciput forced together — no motion, rock hard, like a bowling ball. '
             'Trauma to the front or back of the head, or birth.',
  'st:vsup': 'Superior vertical strain (nonphysiologic): same-direction rotation about the transverse axes; basisphenoid elevated — the '
             'greater wings feel as if they move inferiorly.',
  'st:vinf': 'Inferior vertical strain: basisphenoid depressed — the greater wings feel as if they move superiorly.',
  'st:lat': 'Lateral strain (nonphysiologic): same-direction rotation about the vertical axes, a lateral shear — the head feels like a '
            'parallelogram. Named for the direction the basisphenoid deviates.',
  'tx:cv4': 'CV4 (still point): the occiput isn’t forced into extension, it is kept from flexing until the fluctuation stops; hold until '
            'the CRI returns. Not on the mastoids (temporal external rotation). Can be done from the sacrum after acute head trauma.',
  'tx:vs': 'V-spread and sutural spread use the CSF fluctuation, not muscular force, to release a restricted suture.',
  'tx:vsd': 'Venous sinus drainage: clear thoracic outlet, cervical and OA dysfunction first; then transverse sinus → confluence → '
            'occipital sinus → superior sagittal sinus → metopic suture, with only the weight of the head.',
  'tx:cond': 'Condylar decompression balances the membrane at the hypoglossal canal (CN XII); usually before OA decompression.',
}

dyn = dict(
  kinds=dict(csf=['fluid', '--nf-h2o'], ven=['fluid', '--dk11']), groups=[['fluid', 'CSF fluctuation · venous flow']],
  switches=[dict(id='ph', label='Phase', type='steps', auto=3, options=[['flex', 'Flexion'], ['ext', 'Extension']]),
            dict(id='st', label='Strain pattern', type='one', options=[
              ['tors', 'Torsion', 'sbstorsion'], ['sbr', 'Side bending / rotation', 'sbssbr'], ['comp', 'Compression', 'sbscompress'],
              ['vsup', 'Superior vertical strain', 'sbsvertical'], ['vinf', 'Inferior vertical strain', 'sbsvertical'],
              ['lat', 'Lateral strain', 'sbslateral']]),
            dict(id='tx', label='Technique', type='one', options=[
              ['cv4', 'CV4', 'cv4'], ['vs', 'V-spread', 'vspread'], ['vsd', 'Venous sinus drainage', 'venoussinus'],
              ['cond', 'Condylar decompression', 'condylar']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Atlas of Osteopathic Techniques ch 18 · OCOM OMM')

MAP = dict(
  id='cransim', title='Cranial Mechanism in Motion', topic='omm', after='cranial',
  sub='The sphenoid and occiput breathing through flexion and extension at the SBS, the physiologic and nonphysiologic strain '
      'patterns seen from the side, behind and above, and what CV4, V-spread, venous sinus drainage and condylar decompression do',
  w=3600, h=1900,
  fa='',
  src=['Atlas of Osteopathic Techniques ch 18 — Osteopathic Cranial Manipulative Medicine', 'OCOM OMM — OMS2 written midterm study guide'],
  lanes=[('cmMech', 'The mechanism', 'glycolysis'), ('cmStr', 'Strain patterns', 'tca'), ('cmTx', 'Techniques', 'gluconeo')],
  nodes=[
    ('cr1', 'Primary respiratory mechanism', 330, 1660, 'cmMech', 'five components', ['prm'], 'hub'),
    ('cr2', 'Flexion · extension', 760, 1660, 'cmMech', 'named at the SBS', ['sbsflexext']),
    ('cr3', 'Torsion · side bending', 1200, 1660, 'cmStr', 'physiologic', ['sbstorsion', 'sbssbr']),
    ('cr4', 'Compression', 1640, 1660, 'cmStr', 'no motion', ['sbscompress']),
    ('cr5', 'Vertical · lateral strain', 2080, 1660, 'cmStr', 'nonphysiologic', ['sbsvertical', 'sbslateral']),
    ('cr6', 'CV4 · V-spread', 330, 1790, 'cmTx', 'still point · fluid', ['cv4', 'vspread']),
    ('cr7', 'Venous sinus · condylar', 760, 1790, 'cmTx', 'drainage · OA', ['venoussinus', 'condylar']),
    ('cr8', 'Lifts · technique types', 1200, 1790, 'cmTx', 'direct vs indirect', ['craniallifts', 'ocmmtech']),
    ('cr9', 'Indications · safety', 1640, 1790, 'cmTx', 'contraindications', ['ocmmsafety'])],
  panels=[
    (2500, PANY, 1000, 'Same or opposite rotation? (Atlas ch 18)', [
      ('Flexion / extension', 'opposite · transverse axes'),
      ('Torsion', 'opposite · AP axis'),
      ('Side bending', 'opposite · vertical axes'),
      ('Vertical strain', 'same · transverse axes'),
      ('Lateral strain', 'same · vertical axes')])],
  dyn=dyn)
