# The Cervical Spine in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# One cervical vertebra seen from above (body in front, canal with the cord, a foramen on each side with its root) beside an
# arm showing the C5–C8 territories. A `dz` switch narrows the spine: spondylosis alone (osteophytes, facets, thick ligamentum
# flavum — common on films, often silent), foraminal stenosis (one root → radiculopathy; an `rt` stepper picks C5–C8 and lights
# its numb skin, weak movements and reflex), central stenosis (cord → myelopathy) and a hyperextension injury on a narrow canal
# (central cord syndrome). A `test` toggle runs the bedside sign that fits: Spurling, or Lhermitte and Hoffman.
# Schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

Z = lambda *k: [f'dz:{x}' for x in k]
R = lambda k: [f'dz:foram&rt:{k}']
PANY = 1180
VX, VY = 800, 760

text('Cervical spine — a narrowed foramen pinches a root, a narrowed canal squeezes the cord', 180, 150, 'dyn-big')
text('one cervical vertebra seen from above (body in front, at the bottom) · the arm with its root territories · schematic', 180, 176, 'dyn-cap')
add(f'<ellipse cx="{VX}" cy="{VY + 300}" rx="230" ry="130" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:5"/>')
text('vertebral body · disc', VX, VY + 470, 'nf-l2', 'middle')
add(f'<path d="M{VX - 230} {VY + 200} C{VX - 330} {VY} {VX - 220} {VY - 260} {VX} {VY - 300} C{VX + 220} {VY - 260} {VX + 330} {VY} {VX + 230} {VY + 200}" '
    'style="fill:none;stroke:var(--dk5);stroke-width:40;stroke-opacity:.25"/>')
text('lamina · facets', VX - 330, VY - 260, 'nf-l2', 'end')
add(f'<circle cx="{VX}" cy="{VY}" r="150" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>')
text('canal', VX + 160, VY - 150, 'nf-l2')
add(f'<ellipse cx="{VX}" cy="{VY}" rx="105" ry="75" style="fill:var(--dk7);fill-opacity:.2;stroke:var(--dk7);stroke-width:4"/>')
add(f'<path d="M{VX - 40} {VY - 50} q40 50 0 100 M{VX + 40} {VY - 50} q-40 50 0 100" style="fill:none;stroke:var(--dk7);stroke-width:5;opacity:.6"/>')
text('cord', VX, VY + 6, 'nf-l1', 'middle')
for s in (-1, 1):
    add(f'<path d="M{VX + s * 100} {VY + 20} C{VX + s * 260} {VY + 60} {VX + s * 350} {VY + 160} {VX + s * 480} {VY + 200}" style="fill:none;stroke:var(--dk7);stroke-width:14;stroke-linecap:round"/>')
    add(f'<circle cx="{VX + s * 300}" cy="{VY + 110}" r="56" style="fill:none;stroke:var(--line-2);stroke-width:3;stroke-dasharray:8 6"/>')
text('foramen', VX + 370, VY + 60, 'nf-l2'); text('root', VX + 500, VY + 230, 'nf-l2')
# spondylosis: osteophytes, thick ligamentum flavum, facets
SP_ = ['dz:spond', 'dz:foram', 'dz:central', 'dz:hyper']
for s in (-1, 1):
    add(f'<path d="M{VX + s * 200} {VY + 190} l{s * 40} -50 l{s * 10} 60 Z" style="fill:var(--dk5);opacity:.6"/>', when=SP_)
    add(f'<path d="M{VX + s * 120} {VY - 160} Q{VX} {VY - 190} {VX - s * 0} {VY - 165}" style="fill:none;stroke:var(--dk11);stroke-width:18;opacity:.6"/>', when=SP_)
text('osteophytes · thick ligamentum flavum · worn facets', VX, VY - 400, 'nf-l1', 'middle', when=SP_)
# foraminal stenosis (left side pinched)
add(f'<path d="M{VX + 250} {VY + 60} l50 40 l-30 40 Z" style="fill:var(--bad);opacity:.7"/>', when=Z('foram'))
add(f'<path d="M{VX + 100} {VY + 20} C{VX + 260} {VY + 60} {VX + 350} {VY + 160} {VX + 480} {VY + 200}" style="fill:none;stroke:var(--bad);stroke-width:14;stroke-dasharray:18 10"/>', when=Z('foram'))
# central stenosis: canal pinched, cord flattened
add(f'<path d="M{VX - 150} {VY + 90} Q{VX} {VY + 30} {VX + 150} {VY + 90}" style="fill:var(--dk5);fill-opacity:.4;stroke:var(--bad);stroke-width:5"/>', when=Z('central', 'hyper'))
add(f'<path d="M{VX - 150} {VY - 100} Q{VX} {VY - 40} {VX + 150} {VY - 100}" style="fill:var(--dk11);fill-opacity:.4;stroke:var(--bad);stroke-width:5"/>', when=Z('central', 'hyper'))
add(f'<ellipse cx="{VX}" cy="{VY}" rx="110" ry="40" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:5"/>', when=Z('central'))
add(f'<circle cx="{VX}" cy="{VY}" r="45" style="fill:var(--bad);fill-opacity:.55"/>', when=Z('hyper'))
text('central gray + medial (arm) corticospinal fibers', VX, VY + 560, 'nf-l1', 'middle', when=Z('hyper'))

# arm with root territories
AX = 1500
add(f'<rect x="{AX}" y="300" width="160" height="300" rx="70" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
add(f'<rect x="{AX}" y="620" width="160" height="320" rx="60" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
add(f'<rect x="{AX - 10}" y="960" width="180" height="150" rx="40" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
for i in range(5):
    add(f'<rect x="{AX - 10 + i * 38}" y="1110" width="28" height="{120 if i else 80}" rx="14" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--line-2);stroke-width:3"/>')
text('thumb', AX - 40, 1180, 'nf-l2', 'end'); text('little', AX + 200, 1240, 'nf-l2')
text('lateral', AX - 30, 280, 'nf-l2', 'end'); text('medial', AX + 190, 280, 'nf-l2')
ZONE = dict(c5=f'<rect x="{AX}" y="320" width="70" height="260" rx="30"', c6=f'<path d="M{AX} 640 h70 v300 h-70 Z M{AX - 10} 1110 h66 v120 h-66 Z"',
            c7=f'<path d="M{AX + 66} 1110 h66 v120 h-66 Z"', c8=f'<path d="M{AX + 90} 640 h70 v470 h-70 Z M{AX + 104} 1110 h66 v120 h-66 Z"')
for k, z in ZONE.items():
    add(f'{z} style="fill:var(--bad);fill-opacity:.45"/>', when=R(k))
RTAG = dict(c5='C5 — numb lateral arm · weak shoulder abduction, external rotation, elbow flexion · biceps & brachioradialis reflexes',
            c6='C6 — numb lateral forearm, thumb, index · weak elbow flexion, supination, pronation · biceps & brachioradialis reflexes',
            c7='C7 — numb index & middle fingers, palm · weak elbow & wrist extension, wrist flexion · triceps reflex',
            c8='C8 — numb medial forearm, ring & little fingers · weak finger flexion/extension, hand intrinsics · no reflex')
for k, s in RTAG.items(): text(s, 1100, 1520, 'nf-l1', 'middle', when=R(k))
TAG = dict(spond='spondylosis — on films in ~95% by 65 and does not track symptoms: neck & periscapular pain, stiffness',
           foram='foraminal stenosis — one root pinched: neck/arm pain, mild numbness, weakness only when severe',
           central='central stenosis — cord squeezed: clumsy hands, stiff legs, brisk reflexes, bowel/bladder trouble',
           hyper='neck hyperextension on a narrow canal — central cord syndrome: arms weaker than legs')
for k, s in TAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=Z(k))
text('Spurling: extend + tilt toward the sore side + press down → arm pain (~90% specific, ~45% sensitive)', 1100, 1560, 'nf-l1', 'middle', when=['test&dz:foram'])
text('Lhermitte: flex the neck → shock down the spine · Hoffman: flick middle fingertip → thumb & index pinch', 1100, 1560, 'nf-l1', 'middle', when=['test&dz:central', 'test&dz:hyper'])

# ════════ motion ════════
def sig(d, ln, when, kind='sig', n=3, sp=130):
    return dict(d=d, len=ln, speed=sp, r=8, base={kind: n}, when=when)
ROOT = f'M{VX + 100} {VY + 20} C{VX + 260} {VY + 60} {VX + 350} {VY + 160} {VX + 480} {VY + 200} C{VX + 600} {VY + 230} {AX - 60} 600 {AX + 40} 800'
flows = [sig(f'M{VX - 100} {VY + 20} C{VX - 260} {VY + 60} {VX - 350} {VY + 160} {VX - 480} {VY + 200}', 400, ['!dz:foram'], n=2),
         sig(ROOT, 1000, ['!dz:foram'], n=2), sig(ROOT, 1000, Z('foram'), kind='pain', n=4, sp=90),
         sig(f'M{VX} {VY - 600} V{VY + 700}', 1300, ['!dz:central&!dz:hyper'], n=3),
         sig(f'M{VX} {VY - 600} V{VY + 700}', 1300, Z('central', 'hyper'), kind='pain', n=1, sp=50)]
sites = [dict(x=VX - 260, y=VY + 260, n=[-1, 1], w=10, t='rec', l='', aria='Cervical spondylosis & stenosis', c='cervspond', ions=[]),
         dict(x=VX + 380, y=VY + 300, n=[1, 1], w=10, t='rec', l='', aria='Cervical radiculopathy', c='cervradic', ions=[]),
         dict(x=VX - 180, y=VY - 40, n=[-1, -1], w=10, t='rec', l='', aria='Cervical myelopathy', c='cervmyel', ions=[]),
         dict(x=VX + 180, y=VY + 520, n=[1, 1], w=10, t='rec', l='', aria='Central cord syndrome', c='centralcord', ions=[])]

readouts = [
  dict(l='Root pain & numbness', mods=[dict(when=Z('foram'), d=1)]),
  dict(l='Upper motor neuron signs', mods=[dict(when=Z('central', 'hyper'), d=1)]),
  dict(l='Arm strength', mods=[dict(when=Z('foram', 'central', 'hyper'), d=-1)]),
  dict(l='Leg strength', mods=[dict(when=Z('central'), d=-1)]),
]

notes = {
  '': 'Each cervical root leaves through a foramen beside the vertebra; the cord sits in the central canal. Narrow a foramen and one '
      'root suffers (radiculopathy); narrow the canal and the cord suffers (myelopathy).',
  'dz:spond': 'Cervical spondylosis: disc degeneration, facet arthropathy, osteophytes, thick or ossified posterior longitudinal ligament '
              'and ligamenta flava. Seen on imaging in ~95% by 65 and does not correlate with symptoms. X-ray first; MRI over CT.',
  'dz:foram': 'Cervical radiculopathy: one root, often from spondylosis. Almost all have neck or arm pain (can mimic chest pain); sensory '
              'loss is mild and weakness comes late. Clinical diagnosis, MRI for the cause. Pick a root to see its territory.',
  'dz:central': 'Cervical myelopathy: cord compression adds upper motor neuron signs — weak clumsy hands, spastic arms and legs, brisk '
                'reflexes, bowel or bladder trouble. MRI; progressive myelopathy goes to a spine surgeon.',
  'dz:hyper': 'Central cord syndrome: hyperextension on a spondylotic, narrow canal injures the central cord, where the arm fibers of the '
              'lateral corticospinal tracts lie medially — arms weaker than legs.',
  'test': 'Spurling sign (neck extended, tilted to the sore side, pressed down) reproduces radicular pain: specific, not sensitive; '
          'shoulder abduction may ease it, Valsalva can worsen it. Lhermitte and Hoffman point to the cord.',
}

dyn = dict(
  kinds=dict(sig=['mov', '--dk7'], pain=['mov', '--bad']), groups=[['mov', 'Nerve signal · pain']],
  switches=[dict(id='dz', label='Narrowing', type='one', options=[
              ['spond', 'Spondylosis only', 'cervspond'], ['foram', 'Foraminal stenosis → root', 'cervradic'],
              ['central', 'Central stenosis → cord', 'cervmyel'], ['hyper', 'Hyperextension injury', 'centralcord']]),
            dict(id='rt', label='Root (foraminal)', type='steps', options=[['c5', 'C5'], ['c6', 'C6'], ['c7', 'C7'], ['c8', 'C8']]),
            dict(id='test', label='Bedside sign', type='toggle', on='Sign tested', off='Test the sign', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='OCOM Ortho SDL 19 · Tintinalli ch 279')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='cervsim', title='The Cervical Spine in Motion', topic='msk', after='neckpain',
  sub='Wear down a cervical vertebra, then narrow a foramen to pinch C5, C6, C7 or C8, or narrow the canal to squeeze the cord — and run '
      'Spurling, Lhermitte and Hoffman',
  w=3600, h=1900,
  fa='458, 521',
  src=['OCOM Ortho — SDL 19 lecture: Neck and back pain and injury',
       'OCOM Ortho — SDL 19 reading: Neck and back pain (Tintinalli’s Emergency Medicine 9e ch 279)',
       'Fundamental Neuroscience ch 25 — Motor System II: Corticofugal Systems and the Control of Movement'],
  lanes=[('csDeg', 'Degeneration', 'tca'), ('csNrv', 'Root & cord', 'glycolysis')],
  nodes=[
    ('cs1', 'Cervical spondylosis', 300, 1720, 'csDeg', 'films ≠ symptoms', ['cervspond'], 'hub'),
    ('cs2', 'Cervical radiculopathy', 750, 1720, 'csNrv', 'one root · Spurling', ['cervradic']),
    ('cs3', 'Cervical myelopathy', 1200, 1720, 'csNrv', 'UMN · Lhermitte · Hoffman', ['cervmyel']),
    ('cs4', 'Central cord syndrome', 1650, 1720, 'csNrv', 'arms > legs', ['centralcord'])],
  panels=[
    (2500, PANY, 1000, 'Which root? (course lecture)', [
      ('C5', 'lateral arm · biceps'), ('C6', 'thumb · biceps, brachioradialis'), ('C7', 'middle finger · triceps'),
      ('C8', 'little finger · no reflex')])],
  dyn=dyn)
