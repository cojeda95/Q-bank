# The Shoulder in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A front view of the left shoulder — clavicle, acromion, AC joint, glenoid, humeral head, subacromial space — with the
# arm abducting in `ab` steps (auto: 0 → 15 → 60 → 90 → 150°) and the muscle that drives each range lighting up (SALT:
# supraspinatus 0–15°, deltoid 15–90°, trapezius and serratus anterior above 90°). A `one` switch adds a problem:
# impingement (cuff squeezed under the acromion overhead), cuff tear (drop arm), frozen shoulder (global stiffness — the
# arm stops early; the stop angle is schematic, the card gives none), glenohumeral and AC osteoarthritis. 4 readouts.
# Facts from the pinned cards; FA page in `fa`. No new cards.
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

D = lambda *k: [f'dx:{x}' for x in k]
A = lambda *k: [f'ab:{x}' for x in k]
PANY = 1180
PX, PY = 1000, 620
ANG = dict(a0=0, a15=15, a60=60, a90=90, a150=150)

text('The shoulder — who lifts the arm, and what stops it', 180, 150, 'dyn-big')
text('front view of the left shoulder · step the arm up through abduction', 180, 176, 'dyn-cap')

# ════════ bones ════════
add('<path d="M560 420 C700 380 860 400 960 440" style="fill:none;stroke:var(--dk6);stroke-width:30;opacity:.35;stroke-linecap:round"/>'); text('clavicle', 640, 380, 'nf-l2')
add('<path d="M960 440 C1020 420 1080 440 1110 480" style="fill:none;stroke:var(--dk6);stroke-width:34;opacity:.45;stroke-linecap:round"/>'); text('acromion', 1120, 440, 'nf-l2')
add('<circle cx="960" cy="440" r="14" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>'); text('AC joint', 930, 410, 'nf-l2', 'end')
add('<path d="M900 540 C860 700 860 880 920 1040 L780 1000 C760 820 780 640 860 520 Z" style="fill:var(--dk6);fill-opacity:.12;stroke:var(--dk6);stroke-width:3"/>')
text('scapula · glenoid', 760, 760, 'nf-l2', 'end')
text('subacromial space', 1190, 530, 'nf-l2')
# arm per angle (the frozen / torn variants cap the angle)
def arm(theta, when, unless=None, col='--dk2'):
    add(f'<g transform="rotate({-theta} {PX} {PY})"><rect x="{PX - 45}" y="{PY}" width="90" height="520" rx="40" '
        f'style="fill:var({col});fill-opacity:.12;stroke:var({col});stroke-width:4"/>'
        f'<circle cx="{PX}" cy="{PY}" r="70" style="fill:var({col});fill-opacity:.15;stroke:var({col});stroke-width:4"/></g>', when=when, unless=unless)
STUCK = 60
for k, th in ANG.items():
    arm(th, A(k), unless=D('frozen', 'tear'))
    arm(min(th, STUCK), [f'ab:{k}&dx:frozen'])
    arm(th if th <= 15 else 30, [f'ab:{k}&dx:tear'])
text('humeral head', PX + 80, PY + 10, 'nf-l2')
# muscles
add('<path d="M720 520 C820 470 920 520 990 560" style="fill:none;stroke:var(--dk4);stroke-width:18;opacity:.25"/>'); text('supraspinatus', 760, 500, 'nf-l2', 'end')
add('<path d="M720 520 C820 470 920 520 990 560" style="fill:none;stroke:var(--dk4);stroke-width:26;opacity:.8"/>', when=A('a15'))
add(f'<path d="M1110 480 C1180 560 1160 700 1080 800" style="fill:none;stroke:var(--dk9);stroke-width:26;opacity:.25"/>'); text('deltoid', 1190, 680, 'nf-l2')
add(f'<path d="M1110 480 C1180 560 1160 700 1080 800" style="fill:none;stroke:var(--dk9);stroke-width:34;opacity:.8"/>', when=A('a60', 'a90'))
add('<path d="M560 260 C700 320 820 380 960 430" style="fill:none;stroke:var(--dk5);stroke-width:22;opacity:.25"/>'); text('trapezius', 560, 240, 'nf-l2')
add('<path d="M560 260 C700 320 820 380 960 430" style="fill:none;stroke:var(--dk5);stroke-width:30;opacity:.8"/>', when=A('a150'))
add('<path d="M780 1000 C700 1060 640 1120 620 1200" style="fill:none;stroke:var(--dk10);stroke-width:22;opacity:.25"/>'); text('serratus anterior', 600, 1230, 'nf-l2')
add('<path d="M780 1000 C700 1060 640 1120 620 1200" style="fill:none;stroke:var(--dk10);stroke-width:30;opacity:.8"/>', when=A('a150'))
SALT = dict(a0='at rest', a15='0–15°: supraspinatus (suprascapular n.) starts abduction', a60='15–90°: deltoid (axillary n.)',
            a90='15–90°: deltoid (axillary n.)', a150='above 90°: trapezius (accessory n.) and serratus anterior (long thoracic n.)')
for k, s in SALT.items(): text(s, 1000, 1380, 'nf-l1', 'middle', when=A(k))
# problems
add('<ellipse cx="1060" cy="530" rx="60" ry="22" style="fill:var(--bad);fill-opacity:.55"/>', when=['dx:impinge&ab:a90', 'dx:impinge&ab:a150'])
add('<ellipse cx="1060" cy="530" rx="60" ry="22" style="fill:var(--bad);fill-opacity:.25"/>', when=D('impinge'))
add('<path d="M970 545 l30 30 M1000 545 l-30 30" class="nf-x"/>', when=D('tear'))
add('<circle cx="960" cy="440" r="34" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('acoa'))
add(f'<circle cx="{PX - 50}" cy="{PY}" r="60" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('ghoa'))
TAG = dict(impinge='supraspinatus pinched under the acromion — pain overhead, at night, lying on that side · Neer, Hawkins',
           tear='cuff tear — weakness; drop arm test: the arm cannot be held up', frozen='frozen shoulder — global loss of motion in many planes (stop angle schematic)',
           ghoa='glenohumeral OA — anterior pain, worst with abduction and external rotation', acoa='AC OA — superior pain, worst with adduction and forward flexion')
for k, s in TAG.items(): text(s, 1000, 1420, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ motion ════════
flows = [
  dict(d='M720 520 C820 470 920 520 990 560', len=300, speed=90, r=8, base=dict(sig=3), when=A('a15'), unless=D('tear')),
  dict(d='M1110 480 C1180 560 1160 700 1080 800', len=360, speed=90, r=8, base=dict(sig=3), when=A('a60', 'a90'), unless=D('frozen')),
  dict(d='M560 260 C700 320 820 380 960 430', len=420, speed=90, r=8, base=dict(sig=3), when=A('a150'), unless=D('frozen', 'tear')),
  dict(d='M1040 520 C1100 560 1140 640 1150 720', len=240, speed=70, r=8, base=dict(pain=3), when=['dx:impinge&ab:a90', 'dx:impinge&ab:a150']),
]
sites = [dict(x=1060, y=490, n=[0, -1], w=10, t='rec', l='', aria='Impingement', c='impinge', ions=[]),
         dict(x=900, y=540, n=[-1, -1], w=10, t='rec', l='', aria='Rotator cuff tear', c='rctear', ions=[]),
         dict(x=1230, y=600, n=[1, 0], w=10, t='rec', l='', aria='Rotator cuff muscles', c='rotatorcuff', ions=[]),
         dict(x=880, y=650, n=[-1, 0], w=10, t='rec', l='', aria='Frozen shoulder', c='frozen', ions=[]),
         dict(x=960, y=380, n=[0, -1], w=10, t='rec', l='', aria='Shoulder osteoarthritis', c='shoa', ions=[])]

readouts = [
  dict(l='Pain overhead', mods=[dict(when=['dx:impinge&ab:a90', 'dx:impinge&ab:a150'], d=1)]),
  dict(l='Strength', mods=[dict(when=D('tear'), d=-1)]),
  dict(l='Range of motion', mods=[dict(when=D('frozen', 'ghoa', 'acoa'), d=-1)]),
  dict(l='Night pain', mods=[dict(when=D('impinge'), d=1)]),
]

notes = {
  '': 'Four cuff muscles (SItS) hold the humeral head in the glenoid. Abduction: supraspinatus 0–15°, deltoid 15–90°, trapezius '
      'and serratus anterior above 90° (SALT). Step the arm up, then add a problem.',
  'dx:impinge': 'Impingement: the supraspinatus is trapped between the humeral head and the acromion in the extra-articular '
                'subacromial space (bursa may swell) — pain with overhead motion, referred to the deltoid insertion, worse at '
                'night and lying on that side. Neer, Hawkins. Physical therapy first.',
  'dx:tear': 'Cuff tendinosis and tears (supraspinatus most often torn): partial, full thickness or massive; weakness when '
             'significant, drop arm test. MRI or ultrasound. PT first; surgery for recalcitrant, full-thickness, massive tears.',
  'dx:frozen': 'Adhesive capsulitis: gradual global loss of motion in many planes; peak mid-50s; diabetes, thyroid disease. Pain '
               'first, then stiffness. Early glenohumeral steroid injection + PT.',
  'dx:ghoa': 'Glenohumeral OA: over 70, women; prior dislocation, fracture or big cuff tears. Anterior shoulder pain, worst with '
             'abduction and external rotation.',
  'dx:acoa': 'AC joint OA: superior shoulder pain, worst with adduction and forward flexion.',
}

dyn = dict(
  kinds=dict(sig=['mov', '--dk4'], pain=['mov', '--bad']), groups=[['mov', 'Muscle drive · pain']],
  switches=[dict(id='ab', label='Abduction', type='steps', auto=3, options=[
              ['a0', '0°'], ['a15', '15°'], ['a60', '60°'], ['a90', '90°'], ['a150', '150°']]),
            dict(id='dx', label='Problem', type='one', options=[
              ['impinge', 'Impingement', 'impinge'], ['tear', 'Cuff tear', 'rctear'], ['frozen', 'Frozen shoulder', 'frozen'],
              ['ghoa', 'Glenohumeral OA', 'shoa'], ['acoa', 'AC joint OA', 'shoa']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='OCOM Ortho SDL 13')

MAP = dict(
  id='shsim', title='The Shoulder in Motion', topic='msk', after='shoulder',
  sub='Lift the arm through abduction and watch supraspinatus, deltoid, trapezius and serratus take over — then add impingement, '
      'a cuff tear, frozen shoulder or arthritis',
  w=3600, h=1900,
  fa='451',
  src=['OCOM Ortho — SDL 13 lecture: Shoulder pain and injury'],
  lanes=[('shCuff', 'Rotator cuff', 'tca'), ('shJoint', 'Joint', 'glycolysis')],
  nodes=[
    ('sh1', 'Rotator cuff injury', 330, 1700, 'shCuff', 'SItS · SALT', ['rotatorcuff'], 'hub'),
    ('sh2', 'Impingement', 760, 1700, 'shCuff', 'subacromial', ['impinge']),
    ('sh3', 'Cuff tendinosis & tears', 1200, 1700, 'shCuff', 'drop arm', ['rctear']),
    ('sh4', 'Adhesive capsulitis', 1640, 1700, 'shJoint', 'global stiffness', ['frozen']),
    ('sh5', 'Shoulder osteoarthritis', 2080, 1700, 'shJoint', 'GH vs AC', ['shoa'])],
  panels=[
    (2500, PANY, 1000, 'Who abducts (SALT)', [
      ('0–15°', 'supraspinatus — suprascapular n.'), ('15–90°', 'deltoid — axillary n.'),
      ('Above 90°', 'trapezius — accessory n.'), ('Above 90°', 'serratus anterior — long thoracic n.')])],
  dyn=dyn)
