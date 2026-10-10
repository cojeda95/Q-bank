# m41 · Brachial Plexus Lesion Simulator — roots C5–T1 → trunks → divisions → cords → terminal nerves, drawn
# left to right, running on into an outstretched arm (thumb side up) where each nerve reaches its muscles and
# its skin. Pick a lesion: the ✕ lands on the injured segment, the signals stop beyond it, the skin it supplies
# goes dark (front and back of the limb), and the posture box shows the sign (waiter's tip, claw, wrist drop…).
# Sources: First Aid 2025 pp. 450–453, 458, 463, 523 · Moore ch 3 (Upper Limb) · carpal tunnel: Moore ch 3.
import sys, re, math
sys.path.insert(0, '/Users/Alonso/Developer/atlas-review/batches/m18')
from common import full

MO3 = full('Moore', 3)
MO1 = full('Moore', 1)


def _pts(d):
    return re.findall(r'[MLQC]|-?\d+(?:\.\d+)?', d)


def plen(d):
    t = _pts(d); i = 0; x = y = 0.0; tot = 0.0; cmd = None
    while i < len(t):
        if t[i] in 'MLQC': cmd = t[i]; i += 1
        if cmd == 'M':
            x, y = float(t[i]), float(t[i + 1]); i += 2
        elif cmd == 'L':
            nx, ny = float(t[i]), float(t[i + 1]); i += 2
            tot += math.hypot(nx - x, ny - y); x, y = nx, ny
        elif cmd == 'Q':
            cx, cy, nx, ny = map(float, t[i:i + 4]); i += 4; px, py = x, y
            for k in range(1, 41):
                s = k / 40; qx = (1 - s) ** 2 * x + 2 * (1 - s) * s * cx + s * s * nx; qy = (1 - s) ** 2 * y + 2 * (1 - s) * s * cy + s * s * ny
                tot += math.hypot(qx - px, qy - py); px, py = qx, qy
            x, y = nx, ny
    return tot


L = lambda k: 'les:' + k
LL = lambda *ks: [L(k) for k in ks]


def T(x, y, s, cls='nf-l1', anchor='start', fs=None):
    f = f' font-size="{fs}" style="font-size:{fs}px"' if fs else ''
    a = f' text-anchor="{anchor}"' if anchor != 'start' else ''
    return f'<text class="{cls}" x="{x}" y="{y}"{a}{f}>{s}</text>'


SHADE = 'class="dyn-lesion" style="fill:var(--bad);fill-opacity:.18;stroke-dasharray:8 6"'
X = lambda x, y, s=15: (f'<circle cx="{x}" cy="{y}" r="{s + 8}" style="fill:var(--surface);opacity:.9"/>'
                        f'<path class="dyn-lesion" d="M{x - s} {y - s} L{x + s} {y + s} M{x + s} {y - s} L{x - s} {y + s}"/>')


def fl(d, kind, cut=(), low=(), per=95, sp=110):
    ln = plen(d); n = max(1, round(ln / per))
    f = dict(d=d, len=round(ln), speed=sp, r=7, base={kind: n})
    if cut: f['unless'] = LL(*cut)
    if low: f['mods'] = [dict(when=LL(*low), set={kind: max(1, n // 3)})]
    return f


COL = {'px': '--dk8', 'mc': '--dk1', 'ax': '--dk5', 'rad': '--dk7', 'med': '--dk3', 'uln': '--dk4', 'lt': '--dk6', 'ss': '--dk10'}
S, flows = [], []
track = lambda d, c, w=12, dash='': (f'<path d="{d}" style="fill:none;stroke:var({c});stroke-width:{w};opacity:.25;'
                                     f'stroke-linecap:round;stroke-linejoin:round{";stroke-dasharray:" + dash if dash else ""}"/>')

# ═══════════════ 1. the plexus (First Aid p. 452 · Moore ch 3) ═══════════════
PX = [  # (path, cut by, low by)
  ('M180 300 Q340 300 440 340', (), ()), ('M180 380 Q340 380 440 340', (), ()), ('M180 460 L440 460', (), ()),
  ('M180 540 Q340 540 440 580', (), ()), ('M180 620 Q340 620 440 580', (), ()),
  ('M440 340 L560 340', ('erb',), ()), ('M440 460 L560 460', (), ()), ('M440 580 L560 580', ('klump', 'tos'), ()),
  ('M560 340 L720 320', ('erb',), ()), ('M560 340 Q640 400 720 460', ('erb',), ()),
  ('M560 460 Q640 380 720 320', (), ()), ('M560 460 L720 460', (), ()),
  ('M560 580 L720 600', ('klump', 'tos'), ()), ('M560 580 Q640 520 720 460', ('klump', 'tos'), ()),
  ('M720 320 L880 320', (), ('erb',)), ('M720 460 L880 460', (), ('erb', 'klump', 'tos')), ('M720 600 L880 600', ('klump', 'tos'), ()),
]
for d, c, lo in PX:
    S.append(track(d, '--dk8', 22))
    flows.append(fl(d, 'px', c, lo, per=70))
for x, y, nm in ((560, 340, ''), (560, 460, ''), (560, 580, ''), (720, 320, ''), (720, 460, ''), (720, 600, '')):
    S.append(f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--surface);stroke:var(--dk8);stroke-width:3"/>')
S.append(''.join(T(166, y + 5, nm, 'nf-l1', 'end') for y, nm in ((300, 'C5'), (380, 'C6'), (460, 'C7'), (540, 'C8'), (620, 'T1')))
         + T(500, 326, 'Upper', 'nf-l2', 'middle') + T(500, 446, 'Middle', 'nf-l2', 'middle') + T(500, 566, 'Lower', 'nf-l2', 'middle')
         + T(800, 306, 'Lateral', 'nf-l2', 'middle') + T(800, 446, 'Posterior', 'nf-l2', 'middle') + T(800, 586, 'Medial', 'nf-l2', 'middle'))
S.append(''.join(T(x, 712, t, 'dyn-big', 'middle') for x, t in ((210, 'Roots'), (500, 'Trunks'), (640, 'Divisions'), (800, 'Cords'), (980, 'Branches')))
         + T(640, 734, 'anterior → flexors · posterior → extensors', 'dyn-cap', 'middle')
         + T(150, 150, 'Right brachial plexus and arm, from the front —', 'dyn-cap') + T(150, 166, 'arm held out to the side, palm forward, thumb up', 'dyn-cap'))
# subclavian artery between the scalenes with the lower trunk (First Aid p. 452)
S.append(dict(vessel='M160 668 Q400 668 560 632 Q700 604 880 650', w=11, cls='nf-art', color='--dk2', mods=[dict(when=LL('tos'), d=-7)]))
S.append(T(250, 690, 'subclavian a.', 'dyn-cap'))

# ═══════════════ 2. the nerves, plexus → arm ═══════════════
NV = {  # kind: [(path, cut by, low by)]
  'mc':  [('M880 320 Q960 300 1040 340 Q1080 398 1140 400', ('erb',), ()), ('M1140 400 L1262 402', ('erb',), ()),
          ('M1262 402 L1495 402', ('erb', 'mcut'), ()), ('M1495 402 L1860 392', ('erb', 'mcut'), ())],
  'ax':  [('M880 460 Q940 430 1000 380 Q1040 350 1100 350', ('erb',), ()), ('M1100 350 Q1150 334 1190 362', ('erb', 'axil'), ())],
  'rad': [('M880 460 Q960 474 1040 444 Q1090 438 1140 440', (), ('erb', 'klump', 'tos')), ('M1140 440 L1340 440', (), ('erb', 'klump', 'tos')),
          ('M1340 440 Q1420 462 1505 430 L1880 424', ('radial',), ('erb', 'klump', 'tos')), ('M1880 424 L1960 412', ('radial',), ('erb', 'klump', 'tos'))],
  'tri': [('M1240 440 Q1262 500 1250 540', (), ('erb', 'klump', 'tos'))],
  'med': [('M880 320 Q930 400 960 520', (), ('erb',)), ('M880 600 Q930 560 960 520', ('klump', 'tos'), ()),
          ('M960 520 Q1050 520 1140 520', (), ('erb', 'klump', 'tos')), ('M1140 520 L1480 520', (), ('erb', 'klump', 'tos')),
          ('M1480 520 L1880 512', ('medsc',), ('erb', 'klump', 'tos')), ('M1880 512 Q1910 500 1930 456', ('medsc', 'medct', 'klump', 'tos'), ()),
          ('M1890 508 L2100 468', ('medsc', 'medct'), ())],
  'uln': [('M880 600 Q960 620 1040 612 L1140 610', ('klump', 'tos'), ()), ('M1140 610 L1500 624', ('klump', 'tos'), ()),
          ('M1500 624 L1880 600', ('klump', 'tos', 'ulnp'), ()), ('M1880 600 Q1940 602 1990 590', ('klump', 'tos', 'ulnp', 'ulnd'), ()),
          ('M1960 596 L2120 566', ('klump', 'tos', 'ulnp', 'ulnd'), ())],
  'lt':  [('M262 460 L262 300', (), ()), ('M262 300 Q262 222 340 202', (), ()), ('M340 202 L430 198', ('lthor',), ())],
  'ss':  [('M500 340 Q510 270 560 252 L620 250', ('erb',), ())],
}
KIND = {'tri': 'rad'}

# ═══════════════ 3. the limb (drawn once for the front, again smaller for the back) ═══════════════
FING = [('index', 392, 150), ('middle', 444, 172), ('ring', 496, 158), ('little', 548, 128)]
LIMB = [
  'M1100 340 Q1300 330 1505 360 L1505 642 Q1300 660 1100 655 Z',
  'M1495 362 L1880 376 L1880 616 L1495 646 Z',
  'M1875 380 L2065 380 L2065 625 L1875 625 Z',
] + [f'M2050 {y} L{2050 + ln - 23} {y} Q{2050 + ln} {y} {2050 + ln} {y + 23} Q{2050 + ln} {y + 46} {2050 + ln - 23} {y + 46} L2050 {y + 46} Z'
     for _, y, ln in FING]
THUMB = '<ellipse cx="1932" cy="372" rx="58" ry="24" transform="rotate(-55 1932 372)"/>'
ring_top = 'M2050 496 L2208 496 L2208 519 L2050 519 Z'
ring_bot = 'M2050 519 L2208 519 L2208 542 L2050 542 Z'
fpath = {nm: LIMB[3 + i] for i, (nm, _, _) in enumerate(FING)}
TH = 'M1968 352 m-62 0 a62 24 0 1 0 124 0 a62 24 0 1 0 -124 0'


def thumb_path():
    return f'<ellipse cx="1932" cy="372" rx="58" ry="24" transform="rotate(-55 1932 372)"'


# skin zones (paths in limb coordinates)
R = lambda x0, y0, x1, y1: f'M{x0} {y0} L{x1} {y0} L{x1} {y1} L{x0} {y1} Z'
ZF = {   # front of the limb — Moore ch 3 (Table 3.1, cutaneous nerves) · First Aid pp. 450–451
  'ax': 'M1110 372 a80 30 0 1 0 160 0 a80 30 0 1 0 -160 0',
  'mc': R(1495, 355, 1880, 445),
  'medcut': R(1100, 590, 1880, 660),
  'med_palm': R(1875, 380, 1990, 520) + fpath['index'] + fpath['middle'] + ring_top,
  'med_fing': fpath['index'] + fpath['middle'] + ring_top,
  'uln_palm': R(1875, 545, 2065, 625) + fpath['little'] + ring_bot,
  'uln_fing': fpath['little'] + ring_bot,
  'c5': R(1100, 330, 1505, 430), 'c6': R(1495, 355, 1880, 445),
  't1': R(1290, 575, 1700, 665), 'c8': R(1700, 560, 1880, 660) + R(1875, 545, 2065, 625) + fpath['little'],
}
ZB = {   # back of the limb
  'ax': ZF['ax'], 'mc': R(1495, 355, 1880, 425),
  'rad_arm': R(1100, 430, 1505, 570), 'rad_fa': R(1495, 425, 1880, 560),
  'rad_hand': R(1875, 380, 2065, 500) + R(2050, 392, 2125, 490),
  'med_tips': R(2125, 392, 2240, 519),
  'uln_dors': R(1875, 500, 2065, 625) + fpath['little'] + ring_bot,
  'c5': ZF['c5'], 'c6': ZF['c6'], 't1': ZF['t1'], 'c8': ZF['c8'],
}
BASEF = [('ax', '--dk5'), ('mc', '--dk1'), ('medcut', '--dk8'), ('med_palm', '--dk3'), ('uln_palm', '--dk4')]
BASEB = [('ax', '--dk5'), ('mc', '--dk1'), ('rad_arm', '--dk7'), ('rad_fa', '--dk7'), ('rad_hand', '--dk7'), ('med_tips', '--dk3'),
         ('uln_dors', '--dk4')]
LOST = {   # lesion → (front zones, back zones)
  'erb': (['c5', 'c6'], ['c5', 'c6']), 'klump': (['t1', 'c8'], ['t1', 'c8']), 'tos': (['t1', 'c8'], ['t1', 'c8']),
  'axil': (['ax'], ['ax']), 'mcut': (['mc'], ['mc']), 'radial': ([], ['rad_hand']),
  'medsc': (['med_palm'], ['med_tips']), 'medct': (['med_fing'], ['med_tips']),
  'ulnp': (['uln_palm'], ['uln_dors']), 'ulnd': (['uln_fing'], []),
}
CLIP = '<clipPath id="pslimb">' + ''.join(f'<path d="{d}"/>' for d in LIMB) + THUMB + '</clipPath>'
skin = lambda: ''.join(f'<path d="{d}" class="dyn-cell" style="stroke-width:3"/>' for d in LIMB) + thumb_path() + ' class="dyn-cell" style="stroke-width:3"/>'


def zones(Z, base, lost=()):
    out = '<g clip-path="url(#pslimb)">'
    for k, c in base:
        out += f'<path d="{Z[k]}" style="fill:var({c});opacity:.2"/>'
    for k in lost:
        out += f'<path d="{Z[k]}" class="dyn-lost" style="opacity:.6"/>'
        if k in ('med_palm', 'med_fing', 'c6'):
            out += '<ellipse cx="1932" cy="372" rx="58" ry="24" transform="rotate(-55 1932 372)" class="dyn-lost" style="opacity:.6"/>'
        if k == 'rad_hand':
            out += '<ellipse cx="1932" cy="372" rx="58" ry="24" transform="rotate(-55 1932 372)" class="dyn-lost" style="opacity:.6"/>'
    return out + '</g>'


# back view: the same limb, scaled into the lower right
BT = 'translate(498 556) scale(.62)'
S.append(CLIP)
S.append(skin())
S.append('<path class="dyn-dash" style="opacity:.5" d="M1505 362 L1505 642 M1880 376 L1880 616"/>'
         '<ellipse cx="1505" cy="652" rx="22" ry="13" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:2"/>'
         '<path d="M1880 470 L1880 560" style="stroke:var(--ink-3);stroke-width:7;opacity:.35;stroke-linecap:round"/>')
S.append(f'<g transform="{BT}">' + skin() + '</g>')
for k, (fz, bz) in LOST.items():
    S.append(dict(svg=zones(ZF, BASEF, fz) + f'<g transform="{BT}">' + zones(ZB, BASEB, bz) + '</g>', when=[L(k)]))
S.append(dict(svg=zones(ZF, BASEF) + f'<g transform="{BT}">' + zones(ZB, BASEB) + '</g>', unless=LL('erb', 'klump', 'tos', 'axil', 'mcut', 'radial', 'medsc', 'medct', 'ulnp', 'ulnd')))
S.append(dict(svg=zones(ZF, BASEF) + f'<g transform="{BT}">' + zones(ZB, BASEB) + '</g>', when=[L('lthor')]))
S.append(T(1180, 712, 'Back of the same limb (thumb side still up)', 'nf-l1') + T(1505, 690, 'medial epicondyle', 'dyn-cap', 'middle')
         + T(1880, 368, 'wrist', 'dyn-cap', 'middle').replace('y="368"', 'y="650"')
         + T(1990, 312, 'thumb', 'dyn-cap') + T(2240, 420, 'index', 'dyn-cap') + T(2240, 580, 'little', 'dyn-cap'))

# nerve tracks and particles (after the skin so they sit on the arm)
for k, segs in NV.items():
    kind = KIND.get(k, k)
    for d, cut, lo in segs:
        dash = '9 8' if kind == 'rad' and ('1505' in d or '1880' in d or '1340' in d) else ''
        S.append(track(d, COL[kind], 10, dash))
        flows.append(fl(d, kind, cut, lo))
S.append(T(1300, 395, 'musculocutaneous', 'dyn-cap') + T(1120, 330, 'axillary', 'dyn-cap') + T(1560, 418, 'radial (runs behind)', 'dyn-cap')
         + T(1180, 513, 'median', 'dyn-cap') + T(1180, 603, 'ulnar', 'dyn-cap')
         + T(440, 196, 'Long thoracic → serratus anterior', 'nf-l2') + T(630, 254, 'Suprascapular → supra-, infraspinatus', 'nf-l2'))
# muscles on the limb
MUS = {'del': ('Deltoid', 1190, 380, '--dk5'), 'bic': ('Biceps · brachialis', 1320, 482, '--dk1'), 'tri': ('Triceps (behind)', 1320, 562, '--dk7'),
       'ext': ('Wrist, finger extensors (behind)', 1690, 470, '--dk7'), 'flx': ('Wrist, finger flexors', 1690, 562, '--dk3'),
       'the': ('Thenar', 1925, 438, '--dk3'), 'int': ('Interossei', 1972, 532, '--dk4'), 'hyp': ('Hypothenar', 1965, 604, '--dk4')}


def mtag(k, bad=False):
    nm, x, y, c = MUS[k]; w = len(nm) * 6.6 + 16
    st = f'fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:2.5' if bad else f'fill:var(--surface);stroke:var({c});stroke-width:2'
    return f'<rect x="{x - w / 2:.0f}" y="{y - 13}" width="{w:.0f}" height="22" rx="11" style="{st}"/>' + T(x, y + 3, nm, 'nf-l2', 'middle')


LOSTM = {'erb': ['del', 'bic'], 'klump': ['the', 'int', 'hyp'], 'tos': ['the', 'int', 'hyp'], 'axil': ['del'], 'mcut': ['bic'],
         'radial': ['ext'], 'medsc': ['flx', 'the'], 'medct': ['the'], 'ulnp': ['int', 'hyp'], 'ulnd': ['int', 'hyp'], 'lthor': []}
S.append(dict(svg=''.join(mtag(k) for k in MUS), unless=LL(*LOSTM)))
for les, bad in LOSTM.items():
    S.append(dict(svg=''.join(mtag(k, k in bad) for k in MUS), when=[L(les)]))
# key for the skin colours
KEY = [('--dk5', 'Axillary'), ('--dk1', 'Musculocutaneous'), ('--dk7', 'Radial'), ('--dk3', 'Median'), ('--dk4', 'Ulnar'),
       ('--dk8', 'Medial cutaneous nerves (medial cord)')]
S.append(f'<rect x="1930" y="740" width="400" height="250" rx="16" style="fill:var(--surface);stroke:var(--line-2);stroke-width:2"/>'
         + T(1950, 770, 'Skin by nerve', 'dyn-big')
         + ''.join(f'<rect x="1952" y="{786 + i * 30}" width="20" height="18" rx="4" style="fill:var({c});opacity:.45"/>' + T(1982, 800 + i * 30, t, 'nf-l2')
                   for i, (c, t) in enumerate(KEY))
         + '<rect x="2200" y="786" width="20" height="18" rx="4" class="dyn-lost"/>' + T(2228, 800, 'lost', 'nf-l2'))

# ═══════════════ 4. lesion marks ═══════════════
LES = {
  'erb': X(500, 340) + T(290, 282, 'upper trunk (C5–C6)', 'nf-l1 dyn-tag'),
  'klump': X(500, 580) + T(270, 506, 'lower trunk (C8–T1)', 'nf-l1 dyn-tag'),
  'tos': (X(500, 580) + '<path d="M330 760 Q430 700 520 640" style="fill:none;stroke:var(--ink-2);stroke-width:12;stroke-linecap:round;opacity:.6"/>'
          + T(320, 770, 'cervical rib', 'nf-l1 dyn-tag', 'end') + T(250, 506, 'lower trunk + subclavian a.', 'nf-l1 dyn-tag')),
  'lthor': X(400, 199, 12) + T(360, 240, 'chest-wall injury', 'nf-l1 dyn-tag', 'end'),
  'axil': X(1110, 352, 13) + T(1090, 310, 'surgical neck', 'nf-l1 dyn-tag', 'end'),
  'mcut': X(1262, 402, 13),
  'radial': X(1340, 440) + f'<ellipse cx="1340" cy="440" rx="70" ry="30" {SHADE}/>' + T(1340, 316, 'midshaft — spiral groove', 'nf-l1 dyn-tag', 'middle'),
  'medsc': X(1480, 520) + T(1480, 690, 'supracondylar fracture', 'nf-l1 dyn-tag', 'end').replace('y="690"', 'y="372"'),
  'medct': X(1880, 512) + f'<rect x="1862" y="462" width="36" height="104" rx="10" {SHADE}/>' + T(1850, 690, 'carpal tunnel', 'nf-l1 dyn-tag', 'end'),
  'ulnp': X(1505, 640),
  'ulnd': X(1888, 600, 13) + T(1880, 690, 'Guyon canal · hook of hamate', 'nf-l1 dyn-tag', 'end'),
}
for k, svg in LES.items():
    S.append(dict(svg=svg, when=[L(k)]))

# ═══════════════ 5. the posture box ═══════════════
PB = (140, 800, 920, 560)
S.append(f'<rect x="{PB[0]}" y="{PB[1]}" width="{PB[2]}" height="{PB[3]}" rx="18" style="fill:var(--surface);stroke:var(--line-2);stroke-width:2"/>'
         + T(PB[0] + 24, PB[1] + 34, 'What you see', 'dyn-big', 'start', 18))
SK = 'class="dyn-cell" style="stroke-width:3"'


def finger(x, y, ln, st, w=30):
    """a finger pointing up from (x, y) — ext straight, fist folded down, claw bent at the joints"""
    if st == 'ext':
        return f'<rect x="{x - w / 2}" y="{y - ln}" width="{w}" height="{ln + 8}" rx="{w / 2}" {SK}/>'
    if st == 'fist':
        return f'<rect x="{x - w / 2}" y="{y - 26}" width="{w}" height="34" rx="{w / 2}" {SK}/>' + f'<path d="M{x - 11} {y - 12} L{x + 11} {y - 12}" class="dyn-line"/>'
    if st == 'mild':
        return (f'<rect x="{x - w / 2}" y="{y - ln * .82}" width="{w}" height="{ln * .82 + 8}" rx="{w / 2}" {SK}/>'
                f'<path d="M{x - w / 2 + 2} {y - ln * .74} Q{x} {y - ln * .86} {x + w / 2 - 2} {y - ln * .74}" style="fill:none;stroke:var(--bad);stroke-width:3"/>')
    # claw: proximal phalanx tipped back, the rest curled — seen from the front it shortens and hooks
    return (f'<rect x="{x - w / 2}" y="{y - ln * .62}" width="{w}" height="{ln * .62 + 8}" rx="{w / 2}" {SK}/>'
            f'<path d="M{x - w / 2 + 2} {y - ln * .55} Q{x} {y - ln * .72} {x + w / 2 - 2} {y - ln * .55}" style="fill:none;stroke:var(--bad);stroke-width:3"/>'
            f'<path d="M{x - 9} {y - ln * .4} q9 -12 18 0" style="fill:none;stroke:var(--bad);stroke-width:3"/>')


def hand(cx, cy, fs=('ext',) * 4, thumb='out', thenar=True, hypo=True):
    """palm view of a hand, fingers up; thumb 'out' (normal), 'flat' (in the plane of the palm — ape hand)"""
    out = ''
    if thumb == 'out':
        out += f'<ellipse cx="{cx - 92}" cy="{cy + 12}" rx="22" ry="62" transform="rotate(-38 {cx - 92} {cy + 12})" {SK}/>'
    else:
        out += f'<rect x="{cx - 104}" y="{cy - 56}" width="30" height="120" rx="15" {SK}/>'
    out += f'<rect x="{cx - 80}" y="{cy - 60}" width="160" height="150" rx="34" {SK}/>'
    out += f'<rect x="{cx - 52}" y="{cy + 86}" width="104" height="70" {SK}/>'
    for (dx, ln), st in zip(((-57, 104), (-19, 120), (19, 112), (57, 92)), fs):
        out += finger(cx + dx, cy - 56, ln, st)
    out += (f'<ellipse cx="{cx - 46}" cy="{cy + 46}" rx="30" ry="38" style="fill:var(--dk3);fill-opacity:{.25 if thenar else 0};'
            f'stroke:var({"--dk3" if thenar else "--bad"});stroke-width:2;{"" if thenar else "stroke-dasharray:5 4"}"/>'
            f'<ellipse cx="{cx + 50}" cy="{cy + 46}" rx="24" ry="38" style="fill:var(--dk4);fill-opacity:{.25 if hypo else 0};'
            f'stroke:var({"--dk4" if hypo else "--bad"});stroke-width:2;{"" if hypo else "stroke-dasharray:5 4"}"/>')
    return out


def body(cx, cy):
    return (f'<circle cx="{cx}" cy="{cy - 150}" r="38" {SK}/>'
            f'<rect x="{cx - 70}" y="{cy - 104}" width="140" height="210" rx="40" {SK}/>')


def arm(x0, y0, x1, y1, w=30):
    return f'<path d="M{x0} {y0} L{x1} {y1}" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:{w + 6};stroke-linecap:round"/>' \
           f'<path d="M{x0} {y0} L{x1} {y1}" style="fill:none;stroke:var(--dyn-cell);stroke-width:{w};stroke-linecap:round"/>'


C = (600, 1070)
POSE = {
  '': (hand(*C), 'A normal hand', 'pick a lesion to see its sign'),
  'erb': (body(*C) + arm(C[0] - 70, C[1] - 90, C[0] - 120, C[1] + 60) + arm(C[0] - 120, C[1] + 60, C[0] - 130, C[1] + 170)
          + arm(C[0] + 70, C[1] - 90, C[0] + 112, C[1] + 60) + arm(C[0] + 112, C[1] + 60, C[0] + 150, C[1] + 150)
          + f'<path d="M{C[0] - 150} {C[1] + 170} q-10 30 18 38 q22 4 18 -22" {SK}/>'
          + T(C[0] - 180, C[1] - 40, 'arm at the side,', 'nf-l2', 'end') + T(C[0] - 180, C[1] - 24, 'turned in (medially rotated)', 'nf-l2', 'end')
          + T(C[0] - 180, C[1] + 110, 'elbow straight,', 'nf-l2', 'end') + T(C[0] - 180, C[1] + 126, 'forearm pronated', 'nf-l2', 'end')
          + T(C[0] - 180, C[1] + 210, 'palm faces back', 'nf-l2', 'end'),
          '“Waiter’s tip”', 'the right arm hangs limp, turned in, palm back'),
  'klump': (hand(*C, fs=('claw',) * 4, thenar=False, hypo=False), 'Total claw hand',
            'MCP joints extended, IP joints flexed · flat thenar and hypothenar'),
  'tos': (hand(*C, fs=('claw',) * 4, thenar=False, hypo=False)
          + T(C[0] + 150, C[1] - 40, 'pale, cold,', 'nf-l1 dyn-tag') + T(C[0] + 150, C[1] - 22, 'swollen, aching arm', 'nf-l1 dyn-tag')
          + T(C[0] + 150, C[1] - 4, '(vessels squeezed)', 'nf-l2'), 'Klumpke-like hand + vascular signs', 'intrinsic hand atrophy · ischemia, pain, edema'),
  'lthor': (f'<rect x="{C[0] - 110}" y="{C[1] - 140}" width="220" height="270" rx="50" {SK}/>'
            f'<circle cx="{C[0]}" cy="{C[1] - 186}" r="40" {SK}/>'
            f'<path d="M{C[0] - 30} {C[1] - 110} L{C[0] - 95} {C[1] - 100} L{C[0] - 40} {C[1] + 10} Z" style="fill:var(--surface-2);stroke:var(--ink-2);stroke-width:3"/>'
            f'<path d="M{C[0] + 40} {C[1] - 116} L{C[0] + 120} {C[1] - 108} L{C[0] + 70} {C[1] + 18} Z" style="fill:var(--surface-2);stroke:var(--bad);stroke-width:4"/>'
            f'<path d="M{C[0] + 54} {C[1] + 30} q30 10 50 -20" style="fill:none;stroke:var(--bad);stroke-width:3"/>'
            + arm(C[0] - 100, C[1] - 110, C[0] - 150, C[1] + 120, 26) + arm(C[0] + 100, C[1] - 110, C[0] + 150, C[1] + 120, 26)
            + T(C[0] + 140, C[1] + 40, 'medial border lifts', 'nf-l1 dyn-tag')
            + T(C[0], C[1] + 160, 'seen from behind · worse when pushing on a wall', 'dyn-cap', 'middle'),
            'Winged scapula', 'serratus anterior cannot hold the scapula to the chest'),
  'axil': (body(*C) + f'<path d="M{C[0] - 70} {C[1] - 104} Q{C[0] - 108} {C[1] - 104} {C[0] - 112} {C[1] - 60}" style="fill:none;stroke:var(--bad);stroke-width:4"/>'
           + arm(C[0] - 100, C[1] - 80, C[0] - 160, C[1] + 130)
           + f'<path class="dyn-dash" d="M{C[0] - 100} {C[1] - 80} L{C[0] - 320} {C[1] - 80}"/>'
           + f'<path d="M{C[0] - 100} {C[1] + 30} A110 110 0 0 1 {C[0] - 132} {C[1] + 26}" class="dyn-line"/>'
           + arm(C[0] + 70, C[1] - 90, C[0] + 110, C[1] + 130) + f'<circle cx="{C[0] + 80}" cy="{C[1] - 84}" r="32" style="fill:var(--dk5);opacity:.3"/>'
           + T(C[0] - 330, C[1] - 92, 'cannot raise it past ~15°', 'nf-l2') + T(C[0] - 200, C[1] - 130, 'flat deltoid', 'nf-l1 dyn-tag', 'middle')
           + T(C[0] + 130, C[1] - 120, 'normal deltoid', 'nf-l2'),
           'Flattened deltoid', 'abduction lost beyond 15° · numb lateral shoulder'),
  'mcut': (arm(C[0] - 30, C[1] - 160, C[0] - 30, C[1]) + arm(C[0] - 30, C[1], C[0] - 30, C[1] + 150)
           + f'<path class="dyn-dash" d="M{C[0] - 30} {C[1]} L{C[0] + 110} {C[1] - 110}"/>'
           + f'<circle cx="{C[0] - 30}" cy="{C[1] - 90}" r="26" style="fill:var(--bad);opacity:.18;stroke:var(--bad);stroke-width:2"/>'
           + T(C[0] + 120, C[1] - 116, 'cannot bend the elbow well', 'nf-l2') + T(C[0] + 10, C[1] - 86, 'weak biceps', 'nf-l1 dyn-tag')
           + T(C[0] + 10, C[1] + 60, 'cannot turn a doorknob', 'nf-l2') + T(C[0] + 10, C[1] + 76, '(supination)', 'nf-l2'),
           'Weak elbow flexion and supination', '↓ biceps reflex · numb lateral forearm'),
  'radial': (f'<rect x="{C[0] - 330}" y="{C[1] - 40}" width="290" height="70" rx="30" {SK}/>'
             f'<path d="M{C[0] - 40} {C[1] - 30} Q{C[0] + 10} {C[1] - 20} {C[0] + 30} {C[1] + 60} L{C[0] + 50} {C[1] + 160} Q{C[0] + 20} {C[1] + 190} {C[0] - 10} {C[1] + 160} L{C[0] - 40} {C[1] + 30} Z" {SK}/>'
             f'<path class="dyn-dash" d="M{C[0] - 40} {C[1] - 5} L{C[0] + 200} {C[1] - 5}"/>'
             + T(C[0] + 210, C[1] + 0, 'normal level', 'dyn-cap') + T(C[0] + 70, C[1] + 120, 'the wrist and fingers', 'nf-l2')
             + T(C[0] + 70, C[1] + 136, 'cannot be lifted', 'nf-l2') + T(C[0] - 190, C[1] + 64, 'forearm, palm down', 'dyn-cap', 'middle'),
             'Wrist drop', 'triceps spared at the midshaft · weak grip'),
  'medsc': (hand(*C, fs=('ext', 'ext', 'fist', 'fist'), thumb='out', thenar=False)
            + T(C[0] + 150, C[1] - 120, 'asked to make a fist:', 'nf-l2') + T(C[0] + 150, C[1] - 104, 'index and middle stay straight', 'nf-l1 dyn-tag'),
            '“Hand of benediction”', 'no wrist flexion · LOAF lost · numb lateral 3½ fingers + thenar'),
  'medct': (hand(*C, thumb='flat', thenar=False)
            + T(C[0] - 130, C[1] - 70, 'thumb lies flat,', 'nf-l2', 'end') + T(C[0] - 130, C[1] - 54, 'cannot oppose', 'nf-l2', 'end')
            + T(C[0] - 130, C[1] + 50, 'thenar wasting', 'nf-l1 dyn-tag', 'end'),
            '“Ape hand”', 'numb lateral 3½ fingers, palm spared · Tinel, Phalen'),
  'ulnp': (hand(*C, fs=('ext', 'ext', 'mild', 'mild'), hypo=False)
           + f'<path d="M{C[0]} {C[1] + 170} Q{C[0] - 40} {C[1] + 200} {C[0] - 90} {C[1] + 190}" class="dyn-line" marker-end="url(#ah-psLow)"/>'
           + T(C[0] + 150, C[1] - 104, 'milder claw of 4th, 5th', 'nf-l1 dyn-tag') + T(C[0] + 150, C[1] - 88, '(the ulnar deep flexor is lost too)', 'nf-l2')
           + T(C[0] - 100, C[1] + 218, 'wrist pulls toward the thumb on flexion', 'nf-l2', 'end'),
           'Ulnar nerve at the elbow', 'cannot spread or close the fingers · numb medial 1½ fingers'),
  'ulnd': (hand(*C, fs=('ext', 'ext', 'claw', 'claw'), hypo=False)
           + T(C[0] + 150, C[1] - 104, '4th and 5th claw', 'nf-l1 dyn-tag') + T(C[0] + 150, C[1] - 88, 'when the fingers are extended', 'nf-l2'),
           '“Ulnar claw”', 'no radial deviation · numb medial 1½ fingers'),
}
for k, (svg, name, sub) in POSE.items():
    svg += T(PB[0] + PB[2] / 2, PB[1] + PB[3] - 50, name, 'dyn-big' + (' dyn-tag' if k else ''), 'middle', 19) + T(PB[0] + PB[2] / 2, PB[1] + PB[3] - 26, sub, 'nf-l2', 'middle')
    S.append(dict(svg=svg, when=[L(k)]) if k else dict(svg=svg, unless=[L('*')]))

NOTES = {
  '': "The brachial plexus: roots C5–T1 → upper, middle, lower trunks → anterior and posterior divisions → lateral, posterior, "
      "medial cords → branches. Posterior divisions form the posterior cord (axillary, radial — extensors); anterior divisions "
      "form the lateral and medial cords (musculocutaneous, median, ulnar — flexors). Pick a lesion: signals stop at the ✕ and "
      "the skin it supplies goes dark.",
  L('erb'): "Erb palsy — traction on the upper trunk (C5–C6): an infant’s neck pulled sideways at delivery, or an adult falling on "
            "the head and shoulder. Deltoid and supraspinatus (abduction), infraspinatus (lateral rotation) and biceps (flexion, "
            "supination) are lost: the arm hangs at the side, medially rotated, elbow extended, forearm pronated — ‘waiter’s tip’.",
  L('klump'): "Klumpke palsy — traction on the lower trunk (C8–T1) when the arm is pulled up: an infant’s arm at delivery, an adult "
              "grabbing a branch to break a fall. The intrinsic hand muscles are lost; the lumbricals normally flex the MCP and "
              "extend the IP joints, so the fingers claw — a total claw hand.",
  L('tos'): "Thoracic outlet syndrome — the lower trunk and the subclavian vessels are squeezed, most often in the scalene triangle, "
            "by a cervical or anomalous first rib or a Pancoast tumor. Klumpke-like atrophy of the intrinsic hand muscles, plus "
            "ischemia, pain and edema of the arm from the compressed vessels.",
  L('lthor'): "Long thoracic nerve (roots C5–C7) — injured in axillary node dissection after mastectomy, or by stab wounds. Serratus "
              "anterior can no longer anchor the scapula to the chest wall: the scapula wings when pushing on a wall, and the arm "
              "cannot be raised above the horizontal.",
  L('axil'): "Axillary nerve (C5–C6) — it runs against the surgical neck of the humerus, so a fracture there or an anterior "
             "shoulder dislocation injures it. Flattened deltoid, no abduction beyond about 15° (supraspinatus still starts the "
             "movement), and a numb patch over the deltoid and lateral arm.",
  L('mcut'): "Musculocutaneous nerve (C5–C7) — classically from upper trunk compression. Biceps, brachialis and coracobrachialis "
             "fail: weak elbow flexion and supination, a reduced biceps reflex (C5–C6), and numbness over the radial and dorsal "
             "forearm, where the nerve ends as a skin branch.",
  L('radial'): "Radial nerve at the midshaft of the humerus (spiral groove fracture): wrist drop — no wrist or finger extension, and "
               "a weak grip because the wrist cannot be held extended; numb dorsum of the hand. The triceps branches leave above the "
               "groove, so triceps and posterior arm skin are spared. Crutches or an arm over a chair (‘Saturday night palsy’) hit it higher.",
  L('medsc'): "Median nerve at a supracondylar fracture (proximal lesion): wrist flexion and the lateral finger flexors fail, so on "
              "making a fist the index and middle fingers stay straight — ‘hand of benediction’. The LOAF muscles (lateral two "
              "lumbricals, opponens, abductor and flexor pollicis brevis) are lost; numb thenar eminence and lateral 3½ fingers.",
  L('medct'): "Median nerve in the carpal tunnel (distal lesion) — pregnancy, rheumatoid arthritis, hypothyroidism, diabetes, "
              "acromegaly, dialysis amyloid. Forearm flexors spared; the thenar muscles waste and the thumb cannot oppose — ‘ape "
              "hand’. Tingling in the lateral 3½ fingers but not the palm (its branch passes outside the tunnel). Tinel and Phalen signs.",
  L('ulnp'): "Ulnar nerve at the medial epicondyle (proximal lesion) — fracture or a blow to the ‘funny bone’. Interossei, medial "
             "lumbricals and hypothenar muscles fail: the fingers cannot spread or close, and the wrist deviates radially on "
             "flexion. The claw is milder, because the ulnar half of the deep flexor is lost too. Numb medial palm, dorsum and 1½ fingers.",
  L('ulnd'): "Ulnar nerve at the wrist (Guyon canal) — a hook of hamate fracture after a fall, or handlebar pressure in cyclists. "
             "The intrinsic muscles fail but the ulnar half of the deep flexor still pulls: a marked ‘ulnar claw’ of the 4th and 5th "
             "fingers on extension, no radial deviation. Numb medial 1½ fingers; the palm and dorsum branches leave in the forearm.",
}

RO = lambda l, *mods: dict(l=l, mods=[dict(when=w, d=d) for w, d in mods])
readouts = [
  RO('Shoulder abduction', (LL('erb', 'axil', 'lthor'), -1)),
  RO('Elbow flexion', (LL('erb', 'mcut'), -1)),
  RO('Wrist extension', (LL('radial'), -1)),
  RO('Thumb opposition', (LL('medsc', 'medct', 'klump', 'tos'), -1)),
  RO('Finger spreading', (LL('ulnp', 'ulnd', 'klump', 'tos'), -1)),
  RO('Biceps reflex', (LL('erb', 'mcut'), -1)),
]

dyn = dict(
  kinds={'px': ['px', '--dk8'], 'mc': ['mc', '--dk1'], 'ax': ['ax', '--dk5'], 'rad': ['rad', '--dk7'], 'med': ['med', '--dk3'],
         'uln': ['uln', '--dk4'], 'lt': ['lt', '--dk6'], 'ss': ['lt', '--dk10']},
  groups=[['px', 'Plexus'], ['mc', 'Musculocutaneous'], ['ax', 'Axillary'], ['rad', 'Radial'], ['med', 'Median'], ['uln', 'Ulnar'],
          ['lt', 'Long thoracic · suprascapular']],
  groupsLabel='Signals',
  switches=[dict(id='les', label='Lesion — pick one', type='one',
                 options=[['erb', 'Erb palsy (upper trunk)', 'erb'], ['klump', 'Klumpke palsy (lower trunk)', 'klumpke'],
                          ['tos', 'Thoracic outlet syndrome', 'klumpke'], ['lthor', 'Long thoracic nerve', 'longthoracic'],
                          ['axil', 'Axillary nerve', 'axillarynerve'], ['mcut', 'Musculocutaneous nerve', 'musculocut'],
                          ['radial', 'Radial nerve — midshaft', 'radialnerve'], ['medsc', 'Median — supracondylar', 'mediannerve'],
                          ['medct', 'Median — carpal tunnel', 'carpaltunnel'], ['ulnp', 'Ulnar — medial epicondyle', 'ulnarnerve'],
                          ['ulnd', 'Ulnar — Guyon canal', 'ulnarnerve']])],
  notes=NOTES, shapes=S, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 450–453, 458, 463, 523 · Moore ch 1, 3',
)

MAP = dict(
  id='plexsim', title='Brachial Plexus Lesion Simulator', topic='msk', after='plexus',
  sub='Roots, trunks, divisions, cords and branches running on into the arm, with each nerve’s muscles and skin — pick a lesion to '
      'see the ✕, the signals that stop, the skin that goes numb and the hand or arm sign. Tap a pin for its card',
  w=3500, h=1720,
  fa='450–453, 458, 463, 523',
  src=[MO3, MO1],
  lanes=[('psUp', 'Upper plexus & posterior cord', 'tca'), ('psLow', 'Lower plexus, median & ulnar', 'gluconeo'),
         ('psExam', 'Levels & exam', 'ppp')],
  comps=[(140, 1420, 2210, 280, 'Cards for each lesion')],
  nodes=[
    ('ps1', 'Erb palsy', 330, 1490, 'psUp', 'upper trunk · waiter’s tip', ['erb', 'rotatorcuff']),
    ('ps2', 'Long thoracic nerve', 330, 1570, 'psUp', 'winged scapula', ['longthoracic']),
    ('ps3', 'Axillary nerve', 330, 1650, 'psUp', 'surgical neck · dislocation', ['axillarynerve']),
    ('ps4', 'Musculocutaneous', 860, 1490, 'psUp', 'biceps · lateral forearm', ['musculocut']),
    ('ps5', 'Radial nerve', 860, 1570, 'psUp', 'wrist drop', ['radialnerve']),
    ('ps6', 'Klumpke · thoracic outlet', 860, 1650, 'psLow', 'lower trunk · claw hand', ['klumpke', 'lungca']),
    ('ps7', 'Median nerve', 1390, 1490, 'psLow', 'benediction · ape hand', ['mediannerve']),
    ('ps8', 'Carpal tunnel', 1390, 1570, 'psLow', 'Tinel · Phalen', ['carpaltunnel']),
    ('ps9', 'Ulnar nerve', 1390, 1650, 'psLow', 'claw · Guyon canal', ['ulnarnerve']),
    ('ps10', 'Dermatomes', 1920, 1490, 'psExam', 'C6 thumb · C8 little finger', ['dermatomes'], 'hub'),
    ('ps11', 'Reflexes and roots', 1920, 1570, 'psExam', 'biceps C5–C6', ['reflexroots']),
  ],
  panels=[
    (2420, 760, 1000, 'Humerus fractures follow the ARM nerves (First Aid p. 450)', [
      ('Surgical neck', 'Axillary — flat deltoid, no abduction past 15°'),
      ('Midshaft (spiral groove)', 'Radial — wrist drop, triceps spared'),
      ('Supracondylar', 'Median — hand of benediction'),
      ('Medial epicondyle', 'Ulnar — claw, radial deviation on wrist flexion'),
      ('Hook of hamate (wrist)', 'Ulnar — Guyon canal, ulnar claw')]),
    (2420, 1000, 1000, 'Arm abduction — SALT (First Aid p. 451)', [
      ('0–15°', 'Supraspinatus — suprascapular nerve'),
      ('15–90°', 'Deltoid — axillary nerve'),
      ('Above 90°', 'Trapezius (accessory) · serratus anterior (long thoracic)'),
      ('Dermatomes (Moore ch 3)', 'C5 lateral arm · C6 thumb · C7 middle finger · C8 little finger · T1 medial forearm')]),
  ],
  dyn=dyn,
)
