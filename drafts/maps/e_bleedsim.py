# Head Bleeds in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A coronal section: skull with suture marks, dura, brain with ventricles, falx, tentorium, brainstem, cerebellum and the
# foramen magnum. A `one` switch picks the bleed — epidural (middle meningeal artery at the pterion; lens stopped at the
# sutures), acute and chronic subdural (bridging veins; crescent across the sutures, bright vs dark) and subarachnoid (berry
# aneurysm; blood in the cisterns and sulci) — and `ph` (steps, auto) grows it: injury → early → later, with the lucid
# interval and the midline shift. A second `one` switch pushes brain through each herniation route (subfalcine, uncal,
# central, tonsillar). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
D = lambda *k: [f'dx:{x}' for x in k]
H = lambda *k: [f'hx:{x}' for x in k]
def DP(d, *p): return [f'dx:{d}&ph:{x}' for x in p]
PANY = 1180
CX, CY, RX, RY = 1000, 720, 590, 510

def arcband(t1, t2, thick, shape='lens'):
    pts_o, pts_i = [], []
    for i in range(41):
        th = math.radians(t1 + (t2 - t1) * i / 40)
        f = math.sin(math.pi * i / 40)
        t = thick * (f if shape == 'lens' else min(1, 3 * f))
        pts_o.append((CX + RX * math.cos(th), CY - RY * math.sin(th)))
        pts_i.append((CX + (RX - t) * math.cos(th), CY - (RY - t) * math.sin(th)))
    p = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts_o) + ' L' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in reversed(pts_i)) + ' Z'
    return p

text('Head bleeds — where the blood goes, and where the brain goes next', 180, 150, 'dyn-big')
text('coronal section, patient’s right on your left · the bleed is on that side', 180, 176, 'dyn-cap')

# ════════ anatomy ════════
add(f'<ellipse cx="{CX}" cy="{CY}" rx="{RX + 30}" ry="{RY + 30}" style="fill:none;stroke:var(--dk6);stroke-width:30;opacity:.35"/>')
text('skull', CX + RX + 60, CY - 200, 'nf-l2')
add(f'<ellipse cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}" style="fill:none;stroke:var(--dk7);stroke-width:5"/>')
text('dura', CX + RX + 60, CY - 160, 'nf-l2')
for th in (90, 150, 210):
    r = math.radians(th); x, y = CX + (RX + 30) * math.cos(r), CY - (RY + 30) * math.sin(r)
    add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="14" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:4"/>')
text('suture', CX - 30, CY - RY - 60, 'nf-l2', 'end')
add(f'<ellipse cx="{CX}" cy="{CY - 90}" rx="530" ry="390" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:3"/>',
    unless=DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late'))
add(f'<ellipse cx="{CX + 40}" cy="{CY - 90}" rx="490" ry="380" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:3"/>',
    when=DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late'))
add(f'<path d="M{CX} {CY - RY} V{CY - 130}" style="stroke:var(--dk7);stroke-width:8"/>'); text('falx', CX + 16, CY - 300, 'nf-l2')
for dx_ in (-90, 90):
    add(f'<ellipse cx="{CX + dx_}" cy="{CY - 40}" rx="50" ry="80" style="fill:var(--nf-h2o);fill-opacity:.4;stroke:var(--nf-h2o);stroke-width:3"/>',
        unless=DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late'))
    add(f'<ellipse cx="{CX + dx_ + 70}" cy="{CY - 40}" rx="44" ry="70" style="fill:var(--nf-h2o);fill-opacity:.4;stroke:var(--bad);stroke-width:3"/>',
        when=DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late'))
text('midline shift →', CX + 120, CY - 120, 'nf-l1 dyn-tag', when=DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late'))
add(f'<path d="M{CX - 420} {CY + 330} Q{CX} {CY + 150} {CX + 420} {CY + 330}" style="fill:none;stroke:var(--dk7);stroke-width:7"/>')
text('tentorium', CX + 430, CY + 320, 'nf-l2')
add(f'<rect x="{CX - 60}" y="{CY + 200}" width="120" height="420" rx="40" style="fill:var(--dk3);fill-opacity:.2;stroke:var(--dk3);stroke-width:3"/>')
text('brainstem', CX + 80, CY + 470, 'nf-l2')
for dx_ in (-210, 210):
    add(f'<ellipse cx="{CX + dx_}" cy="{CY + 380}" rx="140" ry="75" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:3"/>')
text('cerebellum', CX - 210, CY + 490, 'nf-l2', 'middle')
add(f'<path d="M{CX - 110} {CY + 540} H{CX - 70} M{CX + 70} {CY + 540} H{CX + 110}" style="stroke:var(--ink-2);stroke-width:8"/>')
text('foramen magnum', CX + 130, CY + 600, 'nf-l2')
add(f'<circle cx="{CX - 150}" cy="{CY + 260}" r="22" style="fill:var(--dk9);opacity:.5"/>'); text('uncus', CX - 190, CY + 270, 'nf-l2', 'end')
add(f'<path d="M{CX - 560} {CY - 40} c-20 20 -20 60 0 90" style="fill:none;stroke:var(--nf-blood);stroke-width:8"/>')
text('middle meningeal a. (pterion)', CX - 640, CY - 60, 'nf-l2', 'end')

# ════════ bleeds ════════
EPI = dict(hit=30, lucid=60, late=110)
for k, t in EPI.items():
    add(f'<path d="{arcband(152, 208, t)}" style="fill:var(--nf-blood);fill-opacity:.75;stroke:var(--bad);stroke-width:3"/>', when=DP('epi', k))
SUB = dict(hit=8, lucid=22, late=46)
for k, t in SUB.items():
    add(f'<path d="{arcband(100, 230, t, "cres")}" style="fill:var(--nf-blood);fill-opacity:.7;stroke:var(--bad);stroke-width:2"/>', when=DP('sub', k))
    add(f'<path d="{arcband(100, 230, t, "cres")}" style="fill:var(--ink-3);fill-opacity:.35;stroke:var(--ink-3);stroke-width:2"/>', when=DP('subc', k))
text('lens — stops at the sutures', CX - 700, CY + 160, 'nf-l1 dyn-tag', 'end', when=D('epi'))
text('crescent — crosses the sutures', CX - 700, CY + 160, 'nf-l1 dyn-tag', 'end', when=D('sub', 'subc'))
text('acute: bright on CT', CX - 700, CY + 196, 'nf-l2', 'end', when=D('sub'))
text('chronic: dark on CT', CX - 700, CY + 196, 'nf-l2', 'end', when=D('subc'))
for x, y in ((CX - 120, CY + 240), (CX + 120, CY + 240), (CX - 300, CY + 120), (CX + 300, CY + 120), (CX, CY + 200)):
    add(f'<path d="M{x - 40} {y} q40 -30 80 0" style="fill:none;stroke:var(--nf-blood);stroke-width:12;opacity:.8"/>', when=D('sah'))
add(f'<circle cx="{CX + 30}" cy="{CY + 200}" r="18" style="fill:var(--bad)"/>', when=D('sah'))
text('berry aneurysm (circle of Willis) — blood in cisterns and sulci', CX, CY + 760, 'nf-l1 dyn-tag', 'middle', when=D('sah'))
text('vasospasm 3–10 days later — nimodipine', CX, CY + 800, 'nf-l2', 'middle', when=DP('sah', 'late'))
text('lucid interval — awake and talking', CX, CY + 760, 'nf-l1 dyn-tag', 'middle', when=DP('epi', 'lucid'))
text('rapid decline — uncal herniation', CX, CY + 760, 'nf-l1 dyn-tag', 'middle', when=DP('epi', 'late'))
text('slow venous ooze — days to weeks', CX, CY + 760, 'nf-l1 dyn-tag', 'middle', when=D('sub', 'subc'))

# herniation arrows
HX = dict(cing=f'M{CX - 140} {CY - 120} C{CX - 60} {CY - 40} {CX + 40} {CY - 40} {CX + 120} {CY - 80}',
          uncal=f'M{CX - 150} {CY + 260} C{CX - 120} {CY + 330} {CX - 80} {CY + 360} {CX - 60} {CY + 380}',
          central=f'M{CX} {CY + 220} V{CY + 560}',
          tonsil=f'M{CX - 190} {CY + 420} C{CX - 160} {CY + 480} {CX - 110} {CY + 520} {CX - 70} {CY + 560}')
HT = dict(cing='subfalcine — ACA compressed → contralateral leg weak', uncal='uncal — ipsilateral blown pupil, contralateral hemiparesis',
          central='central — brainstem pulled down → Duret hemorrhages', tonsil='tonsillar — tonsils into the foramen magnum')
for k, s in HT.items(): text(s, CX, CY + 840, 'nf-l1', 'middle', when=H(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{CX - 570} {CY - 10} C{CX - 560} {CY + 40} {CX - 540} {CY + 60} {CX - 520} {CY + 40}', len=140, speed=120, r=8, base=dict(art=3),
       when=D('epi'), mods=[m(DP('epi', 'late'), speed=1.6)]),
  dict(d=f'M{CX - 380} {CY - 400} C{CX - 440} {CY - 300} {CX - 520} {CY - 200} {CX - 560} {CY - 60}', len=420, speed=30, r=7, base=dict(ven=3),
       when=D('sub', 'subc')),
  dict(d=f'M{CX + 30} {CY + 200} C{CX - 100} {CY + 160} {CX - 250} {CY + 140} {CX - 320} {CY + 100}', len=380, speed=140, r=8, base=dict(art=4), when=D('sah')),
  dict(d=f'M{CX + 30} {CY + 200} C{CX + 120} {CY + 160} {CX + 250} {CY + 140} {CX + 320} {CY + 100}', len=380, speed=140, r=8, base=dict(art=4), when=D('sah')),
] + [dict(d=p, len=320, speed=60, r=10, base=dict(brain=3), when=H(k)) for k, p in HX.items()]
sites = [dict(x=CX - 600, y=CY - 140, n=[-1, 0], w=10, t='rec', l='', aria='Epidural hematoma', c='epidural', ions=[]),
         dict(x=CX - 420, y=CY - 440, n=[-1, -1], w=10, t='rec', l='', aria='Subdural hematoma', c='subdural', ions=[]),
         dict(x=CX + 80, y=CY + 200, n=[1, 0], w=10, t='rec', l='', aria='Subarachnoid hemorrhage', c='sah', ions=[]),
         dict(x=CX + 80, y=CY + 380, n=[1, 0], w=10, t='rec', l='', aria='Herniation', c='herniation', ions=[])]

LATE = DP('epi', 'late') + DP('sub', 'late') + DP('subc', 'late')
readouts = [
  dict(l='Consciousness', mods=[dict(when=DP('epi', 'hit'), d=-1), dict(when=DP('epi', 'lucid'), d=0), dict(when=LATE, d=-1),
                                dict(when=D('sah'), d=-1), dict(when=H('central', 'tonsil'), d=-1)]),
  dict(l='Midline shift', mods=[dict(when=LATE, d=1)]),
  dict(l='Same-side pupil size', mods=[dict(when=DP('epi', 'late') + H('uncal'), d=1)]),
  dict(l='Opposite-side strength', mods=[dict(when=DP('epi', 'late') + H('uncal', 'cing'), d=-1)]),
  dict(l='Headache', mods=[dict(when=D('sah'), d=1), dict(when=D('sub', 'subc'), d=1)]),
]

notes = {
  '': 'Pick a bleed and step through time. Arterial blood under pressure strips the dura; venous blood oozes under it; '
      'aneurysm blood floods the subarachnoid space. Then push the brain through a herniation route.',
  'dx:epi': 'Epidural: a pterion fracture tears the middle meningeal artery (branch of the maxillary). Arterial blood strips the '
            'dura from the skull; the dura is anchored at the sutures, so the clot is a lens that does not cross them. Brief '
            'loss of consciousness → lucid interval → rapid decline. Emergency evacuation.',
  'dx:sub': 'Acute subdural: torn bridging veins (cortex → dural sinuses), stretched by atrophy (age, alcohol); minor fall, '
            'anticoagulants, shaken infants. Crescent that crosses sutures; bright on CT.',
  'dx:subc': 'Chronic subdural: the same crescent, dark on CT; headache, confusion or fluctuating consciousness over days to weeks. '
             'Reverse anticoagulation; burr hole or craniotomy if large.',
  'dx:sah': 'Subarachnoid: a berry aneurysm (most often ACom) ruptures — thunderclap "worst headache of my life". CT: blood in '
            'cisterns and sulci; LP: bloody or xanthochromic CSF. Vasospasm or rebleeding 3–10 days later — nimodipine; '
            'hydrocephalus. PCom aneurysm → CN III palsy.',
  'hx:cing': 'Subfalcine (cingulate): under the falx → ACA compression → contralateral leg weakness.',
  'hx:uncal': 'Uncal: medial temporal lobe through the tentorial notch → early ipsilateral blown pupil (CN III), contralateral '
              'hemiparesis; late Kernohan phenomenon gives a misleading ipsilateral hemiparesis.',
  'hx:central': 'Central/downward: brainstem pulled down → paramedian basilar branches tear → Duret hemorrhages, usually fatal.',
  'hx:tonsil': 'Tonsillar: cerebellar tonsils into the foramen magnum → brainstem compression.',
}

dyn = dict(
  kinds=dict(art=['mov', '--nf-blood'], ven=['mov', '--dk10'], brain=['mov', '--dk2']),
  groups=[['mov', 'Arterial · venous blood · brain tissue']],
  switches=[dict(id='dx', label='Bleed', type='one', options=[
              ['epi', 'Epidural', 'epidural'], ['sub', 'Subdural, acute', 'subdural'], ['subc', 'Subdural, chronic', 'subdural'],
              ['sah', 'Subarachnoid', 'sah']]),
            dict(id='ph', label='Time', type='steps', auto=3, options=[['hit', 'Injury'], ['lucid', 'Early'], ['late', 'Later']]),
            dict(id='hx', label='Herniation', type='one', options=[
              ['cing', 'Subfalcine', 'herniation'], ['uncal', 'Uncal', 'herniation'], ['central', 'Central', 'herniation'],
              ['tonsil', 'Tonsillar', 'herniation']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 28')

MAP = dict(
  id='bleedsim', title='Head Bleeds in Motion', topic='neuro', after='neuroer',
  sub='Grow an epidural lens, a subdural crescent or a subarachnoid flood through time — lucid interval, midline shift, '
      'vasospasm — then push the brain under the falx, through the tentorium or into the foramen magnum',
  w=3600, h=1900,
  fa='528, 530, 543',
  src=['Robbins ch 28 — The central nervous system', 'Moore ch 9 — Head'],
  lanes=[('hbBleed', 'Bleeds', 'tca'), ('hbHern', 'Herniation', 'glycolysis')],
  nodes=[
    ('hb1', 'Epidural hematoma', 330, 1700, 'hbBleed', 'artery · lens · lucid', ['epidural'], 'hub'),
    ('hb2', 'Subdural hematoma', 760, 1700, 'hbBleed', 'veins · crescent', ['subdural']),
    ('hb3', 'Subarachnoid hemorrhage', 1200, 1700, 'hbBleed', 'aneurysm · thunderclap', ['sah']),
    ('hb4', 'Herniation syndromes', 1640, 1700, 'hbHern', 'falx · uncus · tonsils', ['herniation'])],
  panels=[
    (2500, PANY, 1000, 'On CT (Robbins ch 28)', [
      ('Epidural', 'lens, stops at sutures'), ('Subdural', 'crescent, crosses sutures'), ('Acute vs chronic', 'bright vs dark'),
      ('Subarachnoid', 'blood in cisterns and sulci')])],
  dyn=dyn)
