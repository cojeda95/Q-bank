# m52 — Cranial Nerve Reflexes in Motion (dynamic map, kit data)
# The patient faces you (their RIGHT on your left). Both eyes and lacrimal glands on top, the brainstem in the middle
# (midbrain · pons · medulla, with the nuclei of every arc on both sides), the open mouth, jaw and masseters below it and
# the larynx at the bottom. A `steps` switch picks ONE reflex — its afferent limb (particles coloured by the side they come
# from), the brainstem relay and the efferent limb light up and move; a `one` switch puts ONE lesion on the patient's left
# (or both pretectal nuclei): the ✕ lands on the nerve, the particles stop there, the sign is drawn (blown pupil, ptosis,
# small pupils, lid that won't blink, jaw or uvula deviation, sagging palate) and six readouts give the response on each
# side for a left-sided, right-sided or midline stimulus (↔ present · ↓ lost or weak · – not graded by the sources).
#
# Sources (all read in the corpus):
#   First Aid 2025 p. 519 (cranial nerve reflexes table: accommodation II→III; corneal V1 nasociliary → bilateral VII
#     temporal + zygomatic → orbicularis oculi; cough X→X also phrenic and spinal nerves; gag IX→X; jaw jerk V3 spindle
#     from masseter → V3 motor to masseter; lacrimation V1→VII, loss of reflex does not preclude emotional tears;
#     pupillary II→III · CN table: III = sphincter, ciliary muscle, levator; VII = orbicularis oculi, lacrimation; IX =
#     carotid sinus; X = midline uvula, cough reflex, aortic arch) · p. 546 (CN V motor lesion: jaw deviates toward the
#     lesion, unopposed opposite pterygoid; CN X lesion: uvula deviates away; LMN facial lesion: whole half of the face,
#     incomplete eye closure; Bell palsy) · p. 554 (pupillary light reflex: CN II → pretectal nuclei → bilateral EW → CN III
#     → ciliary ganglion → short ciliary nerves → sphincter, direct and consensual; RAPD/Marcus Gunn: swinging light, both
#     dilate) · p. 556 (CN III: compression hits the outer parasympathetic fibers — blown pupil; ischemia spares the pupil;
#     ptosis, down and out; PCom aneurysm, uncal herniation) · p. 557 (cavernous sinus: ↓ corneal sensation) · p. 145
#     (Argyll Robertson pupil constricts with accommodation, not to light — tertiary syphilis) · p. 299 (baroreceptor
#     figure — panel row only) · p. 527 (PICA / lateral medullary: nucleus ambiguus → dysphagia, hoarseness, ↓ gag).
#   Fundamental Neuroscience ch 28 (light reflex = four-neuron arc; K-type ganglion cells → optic nerve and tract; half the
#     fibers cross in the chiasm; olivary pretectal nucleus → BOTH EW nuclei, crossing in the posterior commissure; EW
#     fibers ride CN III to the ipsilateral ciliary ganglion; lesion patterns: optic nerve total → neither direct nor
#     consensual when that eye is lit, partial → RAPD; oculomotor nucleus or nerve → both responses lost in that eye,
#     present in the other; near triad: converge, lens rounds, pupil constricts; near-response region in the supraoculomotor
#     area → medial and lateral rectus motor neurons and EW; ciliary muscle contraction from ciliary-ganglion fibers; Argyll
#     Robertson: small pupils, very weak/absent light reflexes bilaterally, constrict to near, bilateral pretectal damage
#     assumed; corneal blink: trigeminal fibers → spinal trigeminal nucleus → facial nucleus → orbicularis oculi, with
#     inhibition of levator motor neurons).
#   Fundamental Neuroscience ch 14 (corneal: V1, cell bodies in the trigeminal ganglion, end in the ipsilateral spinal
#     trigeminal nucleus, collaterals BILATERALLY to the facial motor nuclei; a trigeminal root lesion loses the afferent limb
#     on that side, touching the other cornea still blinks both; jaw jerk: spindle afferents on V3 with cell bodies in the
#     mesencephalic nucleus, collaterals bilaterally to the trigeminal motor nucleus; injury to one trigeminal nerve does not
#     necessarily abolish the jaw jerk; motor root lesion → jaw deviates toward the weak side; superior salivatory nucleus
#     → intermediate nerve → greater petrosal nerve at the geniculate ganglion → pterygopalatine ganglion → lacrimal gland;
#     Bell palsy proximal to the geniculate ganglion: whole ipsilateral face + ↓ tear fluid; nucleus ambiguus → IX
#     (stylopharyngeus) and X (pharynx, larynx, palate); gag depends on IX and X).
#   Fundamental Neuroscience ch 19 (IX tactile/nociceptive afferents from the oropharynx = afferent limb of the gag reflex;
#     NTS receives IX and X viscerosensory fibers) · ch 33 (neuro exam: corneal reflex via V1 → blink via VII; jaw jerk by
#     a tap on the chin, mouth partly open; vagus lesion → ipsilateral palatal paralysis, uvula pulled to the healthy side;
#     gag by touching the posterior pharyngeal wall).
#   Moore ch 10 (gag reflex IX afferent → X efferent, absent in about 37% of normal people; IX lesion → gag absent on the
#     side of the lesion, taste lost posterior third; IX/X lesion → palate and pharyngeal wall deviate to the opposite side,
#     "curtain sign"; Table 10.6: CN II orbit/optic canal trauma → loss of pupillary constriction; CN III → dilated pupil,
#     ptosis, down and out, reflex lost on that side; CN V → masseter and temporalis don't contract, mandible deviates to
#     the side of the lesion; CN X → soft palate sags, uvula to the normal side, hoarseness) · Moore ch 9 (gag: IX and X
#     contract each side of the pharynx, IX the afferent limb).
#   Guyton ch 38 (cough: larynx and carina most sensitive; afferents mainly in the vagus to the medulla; ~2.5 L inspired,
#     epiglottis and vocal cords shut, abdominal and internal intercostal muscles contract, then the cords burst open).
#   Bootcamp.com Neurology — Cranial nerves I–VI (II: afferent limb of the light reflex, Marcus Gunn; III: efferent limb,
#     loss of ipsilateral reflex and of the consensual reflex when the healthy eye is lit; V: V3 both limbs of the jaw jerk,
#     V1 afferent of corneal and lacrimation reflexes, V1 lesion loses both; cavernous sinus → absent corneal reflex) ·
#   Bootcamp.com Neurology — Cranial nerves VII–XII (VII: efferent limb of corneal and lacrimation reflexes, lesion → lost
#     corneal reflex, impaired lacrimation; IX afferent / X efferent of the gag; X lesion → uvula deviates away, hoarseness).
# Cut for lack of support: carotid sinus / baroreflex as a moving reflex (only IX "monitors" it on the CN page; the arc
#   already moves in baroflow — kept as one panel row); what a one-sided vagus lesion does to the cough; whether an optic
#   nerve lesion changes the near response; whether the lacrimation reflex tears the opposite eye; a brisk jaw jerk in
#   upper motor neuron lesions (no source in the corpus).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

FN14, FN19, FN28, FN33 = (full('Fundamental Neuroscience', c) for c in (14, 19, 28, 33))
MO9, MO10, GY38 = full('Moore', 9), full('Moore', 10), full('Guyton', 38)
BC1 = 'Bootcamp.com Neurology — Cranial nerves I–VI'
BC2 = 'Bootcamp.com Neurology — Cranial nerves VII–XII'
SRC = [FN14, FN28, FN19, FN33, MO10, MO9, GY38, BC1, BC2]

CX = 1240                       # the midline; the patient's LEFT is to the right (s = +1), their RIGHT to the left (s = -1)
SIDES = ((+1, 'L'), (-1, 'R'))
X = lambda s, dx: round(CX + s * dx)

def path(s, pts):
    return 'M' + ' L'.join(f'{X(s, dx)} {y}' for dx, y in pts)
def plen(pts):
    return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))

R_ = lambda *k: ['rx:' + x for x in k]
L_ = lambda *k: ['les:' + x for x in k]

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
TAG = 'nf-l2 dyn-tag'
def XM(x, y, s=14):      # the lesion ✕
    return (f'<circle cx="{x}" cy="{y}" r="{s + 9}" style="fill:var(--surface);opacity:.92"/>'
            f'<path class="dyn-lesion" d="M{x - s} {y - s} L{x + s} {y + s} M{x + s} {y - s} L{x - s} {y + s}"/>')

# ════════ the nerves: every arc as (dx, y) polylines, mirrored for the two sides ════════
N = dict(
  # light / near — afferent
  on1=[(470, 322), (400, 350), (240, 410)], on2=[(240, 410), (60, 462)],
  tr_i=[(60, 462), (140, 500), (196, 550)], tr_x=[(60, 462), (0, 476), (-140, 505), (-196, 550)],
  pt_i=[(200, 572), (140, 615), (90, 644)], pt_x=[(196, 548), (90, 526), (-90, 526), (-130, 590), (-86, 640)],
  ctx=[(60, 462), (30, 430), (30, 290)], soa=[(0, 600), (40, 622), (74, 644)],
  # CN III — efferent (EW → ciliary ganglion → sphincter, ciliary muscle; the medial rectus rides along)
  c3a=[(80, 662), (160, 726), (300, 746), (360, 702), (395, 630)], c3b=[(395, 630), (430, 560), (440, 470), (468, 358)],
  # V1 — corneal / lacrimation afferent
  v1a=[(505, 312), (590, 346), (600, 520), (600, 600)], v1b=[(600, 600), (580, 860), (545, 890), (300, 902), (250, 948)],
  sv_i=[(244, 962), (200, 1010), (160, 1050)], sv_x=[(240, 972), (110, 1000), (-110, 1000), (-152, 1048)],
  sv_s=[(252, 990), (258, 1132), (124, 1152)],
  # VII — facial nucleus / superior salivatory nucleus → geniculate ganglion → orbicularis oculi / lacrimal gland
  f7a=[(160, 1068), (330, 1098), (470, 1090)], f7b=[(470, 1090), (640, 1060), (720, 980), (740, 420), (640, 302)],
  s7a=[(110, 1160), (330, 1118), (470, 1096)], s7b=[(470, 1096), (640, 1066), (800, 960), (822, 712), (800, 420), (700, 222)],
  tear=[(668, 210), (560, 262), (480, 300), (430, 420)],
  # V3 — jaw jerk
  v3a=[(430, 1640), (545, 1300), (545, 1240)], v3b=[(545, 1240), (545, 930), (545, 890), (330, 846), (244, 808)],
  ms_i=[(232, 816), (195, 856), (160, 892)], ms_x=[(228, 820), (100, 866), (-100, 866), (-150, 896)],
  m5a=[(160, 914), (300, 962), (490, 980), (500, 1240)], m5b=[(500, 1240), (500, 1300), (410, 1626)],
  # IX — gag afferent
  g9a=[(180, 1690), (300, 1660), (365, 1590), (365, 1540)], g9b=[(365, 1540), (360, 1470), (300, 1340), (116, 1298)],
  ns_i=[(104, 1306), (140, 1345), (160, 1372)], ns_x=[(94, 1312), (45, 1338), (-45, 1338), (-158, 1376)],
  # X — nucleus ambiguus → palate / larynx; vagal afferents from the larynx → NTS
  x10a=[(178, 1392), (250, 1428), (272, 1468)], x10p=[(272, 1468), (290, 1512), (240, 1566), (150, 1592)],
  x10l=[(272, 1468), (292, 1520), (305, 1880), (58, 1932)],
  ca1=[(66, 1920), (322, 1874), (308, 1520), (290, 1470)], ca2=[(290, 1470), (264, 1426), (122, 1306)],
  air=[(0, 2070), (0, 1900)],
)
NERVE = [  # (polylines, reflexes that light it up)
  (('on1', 'on2'), ('light', 'near')), (('tr_i', 'tr_x'), ('light',)), (('pt_i', 'pt_x'), ('light',)), (('ctx', 'soa'), ('near',)),
  (('c3a', 'c3b'), ('light', 'near')), (('v1a', 'v1b'), ('corneal', 'lacri')), (('sv_i', 'sv_x', 'f7a', 'f7b'), ('corneal',)),
  (('sv_s', 's7a', 's7b'), ('lacri',)), (('v3a', 'v3b', 'ms_i', 'ms_x', 'm5a', 'm5b'), ('jaw',)),
  (('g9a', 'g9b'), ('gag',)), (('ns_i', 'ns_x'), ('gag', 'cough')), (('x10a', 'x10p'), ('gag',)), (('x10a', 'x10l', 'ca1', 'ca2'), ('cough',)),
]

# ════════ the drawing ════════
text('Reflex arcs through the brainstem', 160, 80, 'dyn-big')
text('facing the patient — their right on your left · lesions on their left', 160, 100, 'dyn-cap')
text('Patient’s RIGHT', X(-1, 480), 150, 'dyn-big', 'middle')
text('Patient’s LEFT', X(1, 480), 150, 'dyn-big', 'middle')

# the brainstem
BS = [(-260, 505), (260, 505), (300, 620), (300, 800), (345, 880), (345, 1120), (262, 1200), (250, 1480), (-250, 1480),
      (-262, 1200), (-345, 1120), (-345, 880), (-300, 800), (-300, 620)]
add('<path d="M{} Z" class="dyn-soft" style="stroke-linejoin:round"/>'.format(' L'.join(f'{CX + dx} {y}' for dx, y in BS)))
add(f'<path d="M{CX - 300} 812 H{CX + 300} M{CX - 345} 1186 H{CX + 345}" class="dyn-dash" style="opacity:.6"/>')
text('MIDBRAIN', CX, 795, 'nf-h', 'middle')
text('PONS', CX, 1172, 'nf-h', 'middle')
text('MEDULLA', CX, 1462, 'nf-h', 'middle')
# the spinal trigeminal nucleus — a column from the pons into the medulla
for s, _ in SIDES:
    add(f'<rect x="{X(s, 245) - 13}" y="935" width="26" height="520" rx="13" class="dyn-soft" style="opacity:.85"/>')
# nerves, dim when their reflex is off, highlighted under the particles when it is on
for keys, rx in NERVE:
    for s, _ in SIDES:
        d = ' '.join(path(s, N[k]) for k in keys)
        add(f'<path d="{d}" class="dyn-line" style="stroke-linejoin:round"/>')
        add(f'<path d="{d}" class="dyn-hl" style="opacity:.32"/>', when=R_(*rx))
# nuclei (an ellipse on each side; the name on the patient's right, i.e. your left)
NUC = [  # dx, y, rx, ry, label, label x (dx, negative side), label y, anchor, reflexes
  (200, 560, 34, 18, 'Pretectal nucleus', 240, 566, 'end', ('light',)),
  (80, 652, 28, 16, 'Edinger–Westphal · III', 116, 690, 'end', ('light', 'near')),
  (236, 808, 22, 13, 'Mesencephalic V', 236, 786, 'middle', ('jaw',)),
  (152, 904, 30, 17, 'Motor V', 140, 946, 'middle', ('jaw',)),
  (152, 1060, 30, 17, 'Facial nucleus', 116, 1096, 'start', ('corneal',)),
  (112, 1156, 22, 12, 'Sup. salivatory', 145, 1176, 'end', ('lacri',)),
  (100, 1300, 26, 14, 'Solitary nucleus', 140, 1288, 'end', ('gag', 'cough')),
  (172, 1386, 24, 14, 'Ambiguus', 146, 1424, 'start', ('gag', 'cough')),
]
for dx, y, rx_, ry, lab, ldx, ly, an, rx in NUC:
    for s, _ in SIDES:
        add(f'<ellipse cx="{X(s, dx)}" cy="{y}" rx="{rx_}" ry="{ry}" class="dyn-cell"/>')
        add(f'<ellipse cx="{X(s, dx)}" cy="{y}" rx="{rx_ + 7}" ry="{ry + 7}" class="dyn-hl" style="opacity:.45"/>', when=R_(*rx))
    text(lab, X(-1, ldx), ly, 'nf-l2', an)
text('spinal V nucleus', X(-1, 245), 1236, 'nf-l2', 'middle')
add(f'<ellipse cx="{CX}" cy="600" rx="30" ry="12" class="dyn-cell"/>')
add(f'<ellipse cx="{CX}" cy="600" rx="41" ry="20" class="dyn-hl" style="opacity:.45"/>', when=R_('near'))
add(f'<path d="M{CX} 288 V586" class="dyn-dash"/>')
add(f'<path d="M{CX} 288 V586" class="dyn-hl" style="opacity:.32"/>', when=R_('near'))
text('near-response region', CX, 576, 'nf-l2', 'middle')
text('posterior commissure', CX, 516, 'dyn-cap', 'middle', when=R_('light'))
text('chiasm', CX, 492, 'dyn-cap', 'middle')

# visual cortex and the near target
add(f'<rect x="{CX - 150}" y="230" width="300" height="56" rx="18" class="dyn-soft"/>')
text('Visual cortex', CX, 256, 'nf-l1', 'middle')
text('(via LGN) — near response only', CX, 274, 'dyn-cap', 'middle')
add(f'<path d="M{CX} 112 l7 14 15 2 -11 10 3 15 -14 -7 -14 7 3 -15 -11 -10 15 -2 Z" class="dyn-cell" style="stroke:var(--dk8)"/>'
    f'<path d="M{CX - 14} 135 L{X(-1, 470)} 286 M{CX + 14} 135 L{X(1, 470)} 286" class="dyn-dash"/>', when=R_('near'))
text('near target', CX + 26, 126, 'nf-l1', when=R_('near'))

# ── the eyes ──
def almond(cx, cy=300, hw=150, hh=82):
    return f'M{cx - hw} {cy} Q{cx} {cy - hh * 2 + 24} {cx + hw} {cy} Q{cx} {cy + hh * 2 - 24} {cx - hw} {cy} Z'
def lid(cx, k):   # an upper-lid shape: k = 0 open … 1 closed
    hw, cy = 150, 300
    return f'M{cx - hw} {cy} Q{cx} {cy - 140} {cx + hw} {cy} Q{cx} {cy - 136 + 276 * k} {cx - hw} {cy} Z'
for s, sd in SIDES:
    ex = X(s, 480)
    add(f'<path d="{almond(ex)}" class="dyn-cell" style="fill:var(--surface)"/>')
    # lacrimal gland, upper outer corner
    gx = X(s, 680)
    add(f'<path d="M{gx - 40} 200 Q{gx - 30} 168 {gx} 172 Q{gx + 34} 166 {gx + 40} 196 Q{gx + 30} 222 {gx} 218 Q{gx - 32} 226 {gx - 40} 200 Z" '
        f'class="dyn-cell" style="stroke:var(--nf-h2o)"/>')
text('Lacrimal gland', X(-1, 680), 158, 'nf-l2', 'middle')
text('Lacrimal gland', X(1, 680), 158, 'nf-l2', 'middle')

def iris(ex, ey, pr, when=None, unless=None):
    add(f'<circle cx="{ex}" cy="{ey}" r="46" fill="var(--dk9)" opacity=".55"/><circle cx="{ex}" cy="{ey}" r="{pr}" fill="#16161a"/>',
        when=when, unless=unless)
for s, sd in SIDES:
    ex = X(s, 480); cv = ex - s * 18   # converged: toward the nose
    c3 = L_('cn3') if sd == 'L' else []
    iris(ex, 300, 20, unless=c3 + L_('argyll') + R_('light', 'near'))
    iris(ex, 300, 12, when=R_('light'), unless=c3 + L_('argyll'))
    iris(cv, 300, 12, when=R_('near'), unless=c3 + L_('argyll'))
    iris(ex, 300, 9, when=L_('argyll'), unless=R_('near'))
    iris(cv, 300, 8, when=['les:argyll&rx:near'])
    if sd == 'L':
        iris(ex + 24, 314, 34, when=L_('cn3'))   # down and out, blown pupil
    # the upper lid: blinking in the corneal reflex, drooping with CN III, still when VII is cut
    stuck = L_('cn7') if sd == 'L' else []
    blink = (f'<path d="{lid(ex, 0.04)}" fill="var(--surface-2)" stroke="var(--ink-3)" stroke-width="2.5">'
             f'<animate attributeName="d" dur="2.6s" repeatCount="indefinite" keyTimes="0;.42;.5;.6;1" '
             f'values="{lid(ex, 0.04)};{lid(ex, 0.04)};{lid(ex, 1)};{lid(ex, 0.04)};{lid(ex, 0.04)}"/></path>')
    add(blink, when=R_('corneal'), unless=stuck)
    add(f'<path d="{lid(ex, 0.04)}" fill="var(--surface-2)" stroke="var(--ink-3)" stroke-width="2.5"/>',
        unless=R_('corneal') + (L_('cn3') if sd == 'L' else []) if sd == 'L' else R_('corneal'))
    if sd == 'L':
        add(f'<path d="{lid(ex, 0.04)}" fill="var(--surface-2)" stroke="var(--ink-3)" stroke-width="2.5"/>', when=['rx:corneal&les:cn7'])
        add(f'<path d="{lid(ex, 0.5)}" fill="var(--surface-2)" stroke="var(--ink-3)" stroke-width="2.5"/>', when=L_('cn3'), unless=R_('corneal'))
# stimuli at the eyes
for s, sd in SIDES:
    ex = X(s, 480)
    add(f'<circle cx="{X(s, 330)}" cy="196" r="14" fill="var(--dk8)" opacity=".8"/>'
        f'<path d="M{X(s, 342)} 206 L{X(s, 440)} 278" class="dyn-dash" style="stroke:var(--dk8)"/>', when=R_('light'))
    add(f'<path d="M{X(s, 300)} 218 Q{X(s, 360)} 236 {X(s, 438)} 288" class="dyn-line" style="stroke:var(--dk8);stroke-width:3"/>',
        when=R_('corneal', 'lacri'))
text('light in both eyes', X(-1, 330), 180, 'nf-l2', 'middle', when=R_('light'))
text('a wisp on each cornea', X(-1, 300), 206, 'nf-l2', 'end', when=R_('corneal', 'lacri'))

# lesion signs at the eyes
text('blind left eye', X(1, 480), 212, TAG, 'middle', when=L_('cn2'))
text('partial — the light looks dimmer', X(1, 480), 212, TAG, 'middle', when=L_('rapd'))
text('blown pupil · ptosis · down and out', X(1, 480), 212, TAG, 'middle', when=L_('cn3'))
text('small pupils that ignore light', CX, 214, TAG, 'middle', when=L_('argyll'))
text('left eye won’t close', X(1, 480), 212, TAG, 'middle', when=L_('cn7'))
add(f'<path d="M{X(1, 330)} 230 Q{X(1, 480)} 150 {X(1, 620)} 226 Q{X(1, 480)} 196 {X(1, 330)} 230 Z" fill="var(--bad)" opacity=".22"/>',
    when=L_('v1'))
text('numb V1 skin', X(1, 400), 205, TAG, 'end', when=L_('v1'))

# ganglia and nerve names (named on the patient's right)
for s, _ in SIDES:
    add(f'<ellipse cx="{X(s, 440)}" cy="472" rx="14" ry="10" class="dyn-cell"/>')                       # ciliary
    add(f'<path d="M{X(s, 520)} 872 Q{X(s, 575)} 868 {X(s, 580)} 900 Q{X(s, 560)} 916 {X(s, 520)} 908 Z" class="dyn-cell"/>')   # trigeminal
    add(f'<ellipse cx="{X(s, 640)}" cy="1062" rx="13" ry="10" class="dyn-cell"/>')                      # geniculate
    add(f'<ellipse cx="{X(s, 822)}" cy="712" rx="15" ry="11" class="dyn-cell"/>')                       # pterygopalatine
text('Ciliary ganglion', X(-1, 462), 494, 'nf-l2', 'end')
text('CN II', X(-1, 300), 366, 'nf-l1', 'end')
text('CN III', X(-1, 404), 690, 'nf-l1', 'end')
text('V1', X(-1, 612), 560, 'nf-l1', 'end')
text('nasociliary', X(-1, 612), 576, 'nf-l2', 'end')
text('Trigeminal ganglion', X(-1, 592), 904, 'nf-l2', 'end')
text('VII', X(-1, 752), 760, 'nf-l1', 'end')
text('orbicularis oculi', X(-1, 752), 776, 'nf-l2', 'end')
text('Geniculate ganglion', X(-1, 650), 1092, 'nf-l2', 'end')
text('Pterygopalatine', X(-1, 845), 708, 'nf-l2', 'end')
text('ganglion', X(-1, 845), 724, 'nf-l2', 'end')
text('greater petrosal', X(-1, 812), 846, 'nf-l2', 'end')
text('V3', X(-1, 560), 1400, 'nf-l1', 'end')
text('spindle in · motor out', X(-1, 560), 1416, 'nf-l2', 'end')
text('IX', X(-1, 376), 1520, 'nf-l1', 'end')
text('X', X(-1, 250), 1520, 'nf-l1', 'end')

# ── jaw, mouth, palate ──
def mandible(dev):
    pts = [(-420, 1560), (-410, 1720), (-300 + dev, 1820), (0 + dev, 1846), (300 + dev, 1820), (410, 1720), (420, 1560)]
    return 'M' + ' L'.join(f'{CX + dx} {y}' for dx, y in pts)
add(f'<path d="{mandible(0)}" class="dyn-line" style="stroke-width:6;stroke-linejoin:round"/>', unless=L_('v3'))
add(f'<path d="{mandible(46)}" class="dyn-line" style="stroke-width:6;stroke-linejoin:round"/>', when=L_('v3'))
add(f'<path d="M{CX - 50} 1880 L{CX + 46} 1880" class="dyn-lesion" style="stroke:var(--ink-3);stroke-width:3" marker-end="url(#ah-crFace)"/>',
    when=L_('v3'))
text('jaw deviates toward the lesion', CX + 60, 1884, TAG, when=L_('v3'))
for s, sd in SIDES:
    mx = X(s, 425)
    weak = L_('v3') if sd == 'L' else []
    add(f'<ellipse cx="{mx}" cy="1645" rx="30" ry="72" class="dyn-cell" style="stroke:var(--dk4)" transform="rotate({-s * 12} {mx} 1645)"/>',
        unless=weak)
    if weak:
        add(f'<ellipse cx="{mx}" cy="1645" rx="30" ry="72" class="dyn-cell dyn-dim" style="stroke:var(--bad)" transform="rotate({-s * 12} {mx} 1645)"/>',
            when=weak)
text('Masseter', X(-1, 470), 1660, 'nf-l1', 'end')
text('weak masseter', X(1, 470), 1740, TAG, 'start', when=L_('v3'))
# hammer at the chin (jaw jerk)
add(f'<path d="M{CX - 70} 1890 L{CX - 18} 1858" class="dyn-line" style="stroke:var(--dk8);stroke-width:5"/>'
    f'<rect x="{CX - 40}" y="1840" width="30" height="20" rx="5" class="dyn-cell" style="stroke:var(--dk8)" transform="rotate(-25 {CX - 25} 1850)"/>',
    when=R_('jaw'))
text('tap the chin, mouth partly open', CX - 80, 1866, 'nf-l2', 'end', when=R_('jaw'))
# the open mouth: pharyngeal wall, palate, uvula, tongue
add(f'<ellipse cx="{CX}" cy="1676" rx="262" ry="118" class="dyn-cell" style="fill:var(--surface)"/>'
    f'<rect x="{CX - 200}" y="1596" width="400" height="150" rx="40" class="dyn-soft"/>'
    f'<ellipse cx="{CX}" cy="1772" rx="190" ry="34" class="dyn-cell" style="stroke:var(--dk4)"/>')
def palate(s, sag=False, up=False):
    y0 = 1598 + (24 if sag else 0) - (12 if up else 0)
    return f'<path d="M{X(s, 220)} 1600 Q{X(s, 130)} {y0 - 30} {X(s, 26)} {y0 - 14}" class="dyn-line" style="stroke-width:7;stroke-linecap:round"/>'
for s, sd in SIDES:
    sag = L_('cn10') if sd == 'L' else []
    add(palate(s), unless=sag + R_('gag'))
    add(palate(s, up=True), when=R_('gag'), unless=sag)
    if sag: add(palate(s, sag=True), when=sag)
add(f'<path d="M{CX} 1584 Q{CX + 4} 1626 {CX} 1660" class="dyn-line" style="stroke-width:9;stroke-linecap:round"/>', unless=L_('cn10'))
add(f'<path d="M{CX + 10} 1590 Q{CX - 4} 1630 {CX - 34} 1652" class="dyn-line" style="stroke:var(--bad);stroke-width:9;stroke-linecap:round"/>',
    when=L_('cn10'))
text('uvula pulled AWAY from the lesion', CX - 40, 1700, TAG, 'middle', when=L_('cn10'))
text('left palate sags', X(1, 120), 1574, TAG, 'middle', when=L_('cn10'))
add(f'<path d="M{CX + 30} 1610 H{CX + 196} V1742 H{CX + 30} Z" fill="var(--bad)" opacity=".18"/>', when=L_('cn9'))
text('left pharynx numb', CX + 112, 1726, TAG, 'middle', when=L_('cn9'))
for s, _ in SIDES:
    add(f'<path d="M{X(s, 260)} 1736 L{X(s, 186)} 1690" class="dyn-line" style="stroke:var(--dk8);stroke-width:5"/>', when=R_('gag'))
text('Soft palate · uvula', CX, 1566, 'nf-l2', 'middle', unless=L_('cn10'))
text('touch each side of the pharynx', CX, 1820, 'nf-l2', 'middle', when=R_('gag'))

# ── larynx and trachea (cough) ──
add(f'<path d="M{CX - 62} 1912 H{CX + 62} L{CX + 48} 1968 H{CX - 48} Z" class="dyn-cell"/>'
    f'<path d="M{CX - 40} 1924 L{CX - 4} 1956 M{CX + 40} 1924 L{CX + 4} 1956" class="dyn-line" style="stroke-width:3"/>'
    f'<rect x="{CX - 26}" y="1968" width="52" height="100" rx="12" class="dyn-soft"/>'
    + ''.join(f'<path d="M{CX - 22} {y} H{CX + 22}" class="dyn-line" style="stroke-width:2;opacity:.5"/>' for y in range(1984, 2064, 16))
    + f'<path d="M{CX} 2068 L{CX - 70} 2120 M{CX} 2068 L{CX + 70} 2120" class="dyn-line" style="stroke-width:14;stroke-linecap:round;opacity:.5"/>')
text('Larynx · trachea · carina', CX + 70, 2032, 'nf-l2')
text('irritant at the carina', CX + 84, 2096, 'nf-l2', when=R_('cough'))
text('+ phrenic and spinal nerves → diaphragm, abdominal muscles', CX + 84, 2116, 'nf-l2', when=R_('cough'))
text('glottis shuts, then bursts open', CX + 84, 1972, 'nf-l2', when=R_('cough'))

# ── the lesion ✕s ──
P1 = lambda pt: (X(1, pt[0]), pt[1])
add(XM(*P1((240, 410))), when=L_('cn2'))
add(f'<circle cx="{X(1, 240)}" cy="410" r="20" class="dyn-lesion" style="stroke-dasharray:6 6"/>', when=L_('rapd'))
add(XM(*P1((395, 630))), when=L_('cn3'))
for s, _ in SIDES:
    add(XM(X(s, 200), 560, 13), when=L_('argyll'))
add(XM(*P1((600, 600))), when=L_('v1'))
add(XM(X(1, 522), 1240), when=L_('v3'))
add(XM(*P1((470, 1093))), when=L_('cn7'))
add(XM(*P1((365, 1540))), when=L_('cn9'))
add(XM(*P1((272, 1468)), 12), when=L_('cn10'))
text('optic nerve', X(1, 240) + 30, 448, TAG, when=L_('cn2', 'rapd'))
text('compressed CN III', X(1, 395) + 30, 636, TAG, when=L_('cn3'))
text('both pretectal nuclei', X(1, 200) + 30, 600, TAG, when=L_('argyll'))
text('V1', X(1, 600) + 30, 606, TAG, when=L_('v1'))
text('V3 — sensory + motor', X(1, 522) + 30, 1246, TAG, when=L_('v3'))
text('VII before the geniculate ganglion', X(1, 470) + 2, 1134, TAG, when=L_('cn7'))
text('IX', X(1, 365) + 30, 1546, TAG, when=L_('cn9'))
text('X', X(1, 272) + 24, 1474, TAG, when=L_('cn10'))

# ════════ particles ════════
kinds = {'inL': ['inL', '--dk1'], 'inR': ['inR', '--dk7'], 'rel': ['rel', '--dk10'], 'out': ['out', '--dk5'],
         'tear': ['tear', '--nf-h2o'], 'air': ['air', '--dk12']}
groups = [['inL', 'In from the left'], ['inR', 'In from the right'], ['rel', 'Brainstem relay'], ['out', 'Out to muscle · gland'],
          ['tear', 'Tears'], ['air', 'Air']]
flows = []
def fl(s, key, kind, rx, n=2, cut=(), low=(), sp=120):
    pts = N[key]; f = dict(d=path(s, pts), len=plen(pts), speed=sp, r=6, base={kind: n}, when=R_(*rx))
    if cut: f['unless'] = L_(*cut)
    if low: f['mods'] = [dict(when=L_(*low), set={kind: 1})]
    flows.append(f)
for s, sd in SIDES:
    inn = 'in' + sd; Lo = lambda *k: k if sd == 'L' else ()
    # pupillary light reflex
    fl(s, 'on1', inn, ('light', 'near'), low=Lo('rapd'))
    fl(s, 'on2', inn, ('light', 'near'), cut=Lo('cn2'), low=Lo('rapd'))
    fl(s, 'tr_i', inn, ('light',), 1, cut=Lo('cn2'))
    fl(s, 'tr_x', inn, ('light',), 1, cut=Lo('cn2'))
    fl(s, 'pt_i', 'rel', ('light',), 1, cut=('argyll',))
    fl(s, 'pt_x', 'rel', ('light',), 2, cut=('argyll',))
    fl(s, 'c3a', 'out', ('light', 'near'), 3)
    fl(s, 'c3b', 'out', ('light', 'near'), 2, cut=Lo('cn3'))
    # near response: up to the cortex and back to the near-response region
    fl(s, 'ctx', inn, ('near',), 1, cut=Lo('cn2'))
    fl(s, 'soa', 'rel', ('near',), 1)
    # corneal and lacrimation: V1 in
    fl(s, 'v1a', inn, ('corneal', 'lacri'), 2)
    fl(s, 'v1b', inn, ('corneal', 'lacri'), 3, cut=Lo('v1'))
    fl(s, 'sv_i', 'rel', ('corneal',), 1, cut=Lo('v1'))
    fl(s, 'sv_x', 'rel', ('corneal',), 2, cut=Lo('v1'))
    fl(s, 'f7a', 'out', ('corneal',), 2)
    fl(s, 'f7b', 'out', ('corneal',), 4, cut=Lo('cn7'))
    fl(s, 'sv_s', 'rel', ('lacri',), 1, cut=Lo('v1'))
    fl(s, 's7a', 'out', ('lacri',), 2, cut=Lo('v1'))
    fl(s, 's7b', 'out', ('lacri',), 4, cut=Lo('v1', 'cn7'))
    fl(s, 'tear', 'tear', ('lacri',), 3, cut=Lo('v1', 'cn7'), sp=60)
    # jaw jerk
    fl(s, 'v3a', inn, ('jaw',), 2)
    fl(s, 'v3b', inn, ('jaw',), 3, cut=Lo('v3'))
    fl(s, 'ms_i', 'rel', ('jaw',), 1, cut=Lo('v3'))
    fl(s, 'ms_x', 'rel', ('jaw',), 2, cut=Lo('v3'))
    fl(s, 'm5a', 'out', ('jaw',), 3)
    fl(s, 'm5b', 'out', ('jaw',), 2, cut=Lo('v3'))
    # gag
    fl(s, 'g9a', inn, ('gag',), 2)
    fl(s, 'g9b', inn, ('gag',), 2, cut=Lo('cn9'))
    fl(s, 'ns_i', 'rel', ('gag',), 1, cut=Lo('cn9'))
    fl(s, 'ns_x', 'rel', ('gag',), 2, cut=Lo('cn9'))
    fl(s, 'x10a', 'out', ('gag', 'cough'), 1)
    fl(s, 'x10p', 'out', ('gag',), 2, cut=Lo('cn10'))
    # cough
    fl(s, 'ca1', inn, ('cough',), 3)
    fl(s, 'ca2', inn, ('cough',), 1, cut=Lo('cn10'))
    fl(s, 'ns_i', 'rel', ('cough',), 1, cut=Lo('cn10'))
    fl(s, 'ns_x', 'rel', ('cough',), 2, cut=Lo('cn10'))
    fl(s, 'x10l', 'out', ('cough',), 3, cut=Lo('cn10'))
fl(1, 'air', 'air', ('cough',), 4, sp=170)
flows.append(dict(d=f'M{CX} 282 V592', len=310, speed=110, r=6, base={'rel': 2}, when=R_('near')))   # cortex → near-response region

# ════════ sites: the ganglia where the efferent limbs synapse (tap for the card) ════════
sites = []
for s, sd in SIDES:
    lft = sd == 'L'
    sites.append(dict(x=X(s, 440), y=472, n=[0, -1], w=10, t='rec', ions=[['out', 'out', 1]], reach=20, c='pupilpath',
                      aria=f'Ciliary ganglion ({"left" if lft else "right"})', when=R_('light', 'near'),
                      stop=(L_('cn3') if lft else []) + (['les:argyll&rx:light'])))
    sites.append(dict(x=X(s, 822), y=712, n=[0, -1], w=10, t='rec', ions=[['out', 'out', 1]], reach=20, c='lacrimal',
                      aria=f'Pterygopalatine ganglion ({"left" if lft else "right"})', when=R_('lacri'),
                      stop=L_('v1', 'cn7') if lft else []))

# ════════ readouts: stimulus side → response side ════════
LES = ['cn2', 'rapd', 'cn3', 'argyll', 'v1', 'v3', 'cn7', 'cn9', 'cn10']
_ = None
# per reflex: the normal pattern, then the lesions that change it — (L→L, L→R, R→R, R→L, mid→L, mid→R); None = not graded
NORMAL = dict(light=(0, 0, 0, 0, _, _), near=(_, _, _, _, 0, 0), corneal=(0, 0, 0, 0, _, _), lacri=(0, _, 0, _, _, _),
              jaw=(_, _, _, _, 0, 0), gag=(0, 0, 0, 0, _, _), cough=(_, _, _, _, _, _))
CHANGE = {
  ('light', 'cn2'): (-1, -1, 0, 0, _, _), ('light', 'rapd'): (-1, -1, 0, 0, _, _), ('light', 'cn3'): (-1, 0, 0, -1, _, _),
  ('light', 'argyll'): (-1, -1, -1, -1, _, _),
  ('near', 'cn2'): (_, _, _, _, _, _), ('near', 'rapd'): (_, _, _, _, _, _), ('near', 'cn3'): (_, _, _, _, -1, 0),
  ('corneal', 'v1'): (-1, -1, 0, 0, _, _), ('corneal', 'cn7'): (-1, 0, 0, -1, _, _),
  ('lacri', 'v1'): (-1, _, 0, _, _, _), ('lacri', 'cn7'): (-1, _, 0, _, _, _),
  ('jaw', 'v3'): (_, _, _, _, -1, 0),
  ('gag', 'cn9'): (-1, -1, 0, 0, _, _), ('gag', 'cn10'): (-1, 0, 0, -1, _, _),
}
RO = ['L stimulus → L', 'L stimulus → R', 'R stimulus → R', 'R stimulus → L', 'Midline → L', 'Midline → R']
RX = ['light', 'near', 'corneal', 'lacri', 'jaw', 'gag', 'cough']
readouts = []
for i, lab in enumerate(RO):
    mods = []
    for r in RX:
        for les in [''] + LES:
            v = CHANGE.get((r, les), NORMAL[r])[i]
            if v is None: continue
            mods.append(dict(when=[f'rx:{r}&' + (f'les:{les}' if les else '!les:*')], d=v))
    readouts.append(dict(l=lab, mods=mods))

notes = {
  '': 'Pick a reflex, then a lesion. Results: ↔ the response is there, ↓ it is lost or weak, – not graded.',
  'rx:light&!les:*': 'Pupillary light reflex — CN II in, CN III out. Light in either eye runs the optic nerve and tract to the pretectal '
                     'nuclei, which drive BOTH Edinger–Westphal nuclei (half the fibers cross at the chiasm, the relay crosses in the '
                     'posterior commissure); CN III carries the order to the ciliary ganglion and the sphincter, so each eye '
                     'constricts directly and consensually. ↔ = response present, ↓ = lost or weak.',
  'rx:near&!les:*': 'Near response — CN II in, CN III out. A near target, seen through the visual cortex, drives the midbrain '
                    'near-response region, which fires the medial rectus motor neurons and Edinger–Westphal: the eyes converge, '
                    'the ciliary muscle lets the lens round up (accommodation) and the pupils constrict.',
  'rx:corneal&!les:*': 'Corneal reflex — V1 in, both VII out. Touching one cornea sends V1 (nasociliary) fibers, cell bodies in the '
                       'trigeminal ganglion, to the spinal trigeminal nucleus; it projects to BOTH facial nuclei, so orbicularis oculi '
                       'closes both eyes.',
  'rx:lacri&!les:*': 'Lacrimation reflex — V1 in, VII out. Irritating the cornea drives the superior salivatory nucleus; its fibers '
                     'leave with VII, become the greater petrosal nerve at the geniculate ganglion, relay in the pterygopalatine '
                     'ganglion and reach the lacrimal gland. Losing the reflex does not stop emotional tears.',
  'rx:jaw&!les:*': 'Jaw jerk — V3 in, V3 out. A tap on the chin, mouth partly open, stretches the spindles of the jaw-closing '
                   'muscles; their V3 fibers (cell bodies in the mesencephalic nucleus) excite the trigeminal motor nuclei on BOTH '
                   'sides, and the masseters close the jaw. A one-sided reflex (Midline → L or R) means each masseter.',
  'rx:gag&!les:*': 'Gag reflex — IX in, X out. Touching the back of the pharynx sends IX to the solitary nucleus; the nucleus '
                   'ambiguus fires X on both sides, so both halves of the palate and pharynx rise and the uvula stays midline. The '
                   'gag is absent in about a third of normal people.',
  'rx:cough&!les:*': 'Cough reflex — X in, X out, with the phrenic and spinal nerves. An irritant on the larynx, trachea or carina '
                     'sends vagal fibers to the medulla, which runs a fixed sequence: a deep breath in, the glottis shuts, the '
                     'abdominal and expiratory muscles squeeze, then the glottis bursts open. One-sided lesions are not graded here.',
  'les:cn2': 'Left optic nerve cut (trauma to the orbit or optic canal): the left eye is blind, and light in it gives no direct and '
             'no consensual response; light in the right eye still constricts BOTH pupils, because both CN IIIs work.',
  'les:rapd': 'Left relative afferent pupillary defect (Marcus Gunn pupil) — a partial left optic nerve lesion such as optic '
              'neuritis: light in the left eye gives a weaker direct and consensual response. Swing the light from the right eye '
              'to the left and both pupils dilate.',
  'les:cn3': 'Left oculomotor nerve palsy: direct and consensual responses are lost in the LEFT eye whichever eye is lit, but '
             'present in the right. Compression (PCom aneurysm, uncal herniation) blows the pupil first — the parasympathetic '
             'fibers ride on the outside — with ptosis, a down-and-out eye and no near response on that side.',
  'les:argyll': 'Argyll Robertson pupils (neurosyphilis, tabes dorsalis): small pupils that barely react to light in either eye '
                'but still constrict for a near target — light-near dissociation. Both limbs work; the damage is thought to lie '
                'in both pretectal nuclei or their projections.',
  'les:v1': 'Left V1 lesion (cavernous sinus disease, zoster in V1): touching the left cornea gives no blink in either eye — the '
            'afferent limb is gone — while touching the right cornea still blinks both. The left forehead is numb and the left '
            'lacrimation reflex is lost.',
  'les:v3': 'Left V3 (mandibular) lesion: the left masseter and temporalis are paralyzed, so the jaw deviates TOWARD the lesion — '
            'the healthy right pterygoids push it over. The jaw jerk need not vanish: the right spindles still reach both motor '
            'nuclei and the right masseter still answers the tap.',
  'les:cn7': 'Left facial nerve lesion before the geniculate ganglion (Bell palsy): touching either cornea blinks only the right '
             'eye — the left orbicularis oculi is paralyzed though the left cornea still feels. The whole left face is weak, '
             'forehead included, and the left eye makes less tear fluid.',
  'les:cn9': 'Left glossopharyngeal lesion: touching the left side of the pharynx gives no gag — the afferent limb is cut — while '
             'touching the right still raises both sides through X. Taste and sensation from the posterior third of the tongue '
             'are lost on the left. Isolated IX lesions are rare.',
  'les:cn10': 'Left vagus lesion: the left palate and pharynx don’t rise whichever side is touched, so the uvula is pulled AWAY '
              'from the lesion, toward the right (curtain sign). Hoarseness (left vocal fold paralyzed) and dysphagia; a lateral '
              'medullary (PICA) stroke hits the nucleus ambiguus the same way.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[
    dict(id='rx', label='Reflex', type='steps', options=[
      ['light', 'Pupillary light', 'pupilpath'], ['near', 'Near response', 'neartriad'], ['corneal', 'Corneal blink', 'cnreflexes'],
      ['lacri', 'Lacrimation', 'lacrimal'], ['jaw', 'Jaw jerk', 'cnreflexes'], ['gag', 'Gag', 'cnreflexes'],
      ['cough', 'Cough', 'coughreflex']]),
    dict(id='les', label='Lesion — pick one (on the patient’s left)', type='one', options=[
      ['cn2', 'Left optic nerve (II)', 'opticneuritis'], ['rapd', 'Marcus Gunn (partial II)', 'rapd'],
      ['cn3', 'Left oculomotor (III)', 'cn3palsy'], ['argyll', 'Argyll Robertson (both)', 'lightnear'],
      ['v1', 'Left V1', 'cnreflexes'], ['v3', 'Left V3', 'cnreflexes'], ['cn7', 'Left facial (VII) — Bell', 'bell'],
      ['cn9', 'Left glossopharyngeal (IX)', 'jugfor'], ['cn10', 'Left vagus (X)', 'jugfor']],
      sections=[['Eye', ['cn2', 'rapd', 'cn3', 'argyll']], ['Face and jaw', ['v1', 'v3', 'cn7']], ['Throat', ['cn9', 'cn10']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 145, 519, 527, 546, 554, 556, 557 · Fundamental Neuroscience ch 14, 19, 28, 33 · Moore ch 9–10 · Guyton ch 38 · Bootcamp Neurology')

# ════════ the one new card: no card holds the cranial nerve reflex table and its one-sided lesion signs ════════
card('cnreflexes', 'Cranial nerve reflexes — afferent & efferent limbs', 'reg', 'crFace',
     'Which nerve carries each reflex in, and which carries it out', 1,
     'Each brainstem reflex has a sensory (afferent) nerve and a motor (efferent) nerve, joined by nuclei in the brainstem. '
     'Testing one side and watching <b>both</b> sides tells which limb is broken: an afferent lesion silences the response on '
     'both sides when the bad side is stimulated; an efferent lesion silences only its own side, whichever side is stimulated.',
     ['<b>Pupillary light</b>: II → III · <b>Accommodation</b>: II → III',
      '<b>Corneal</b>: V1 (nasociliary) → <b>both</b> VII (orbicularis oculi) — V1 cut: no blink either eye from that cornea; '
      'VII cut: that eye never blinks',
      '<b>Lacrimation</b>: V1 → VII (greater petrosal → pterygopalatine ganglion); emotional tears are spared',
      '<b>Jaw jerk</b>: V3 spindle afferents (cell bodies in the mesencephalic nucleus) → V3 motor to the masseter, both sides',
      '<b>Gag</b>: IX → X · <b>Cough</b>: X → X, plus phrenic and spinal nerves'],
     ['—'],
     ['One-sided CN V motor lesion: jaw deviates toward the lesion', 'CN X lesion: uvula deviates away from the lesion'],
     [FN14, FN33, MO10, BC1, BC2],
     ['—'],
     ['cranial nerve reflexes', 'corneal reflex', 'corneal blink reflex', 'jaw jerk', 'jaw jerk reflex', 'gag reflex',
      'lacrimation reflex', '=jaw deviates toward the side of the lesion', '=uvula deviates away from the side of the lesion'],
     fa='519, 546')

MAP = dict(
  id='cnrefsim', title='Cranial Nerve Reflexes in Motion', topic='neuro', after='stemsim',
  sub='The brainstem reflex arcs — pupillary light, near response, corneal blink, lacrimation, jaw jerk, gag, cough — each with '
      'its afferent nerve, its nuclei on both sides and its efferent nerve lit as the signal moves. Put a lesion on the left '
      '(II, III, V1, V3, VII, IX, X, or both pretectal nuclei) and read which responses are lost on which side. Tap a pin for its card',
  w=3500, h=2200,
  fa='145, 519, 527, 546, 554, 556, 557', src=SRC,
  lanes=[('crEye', 'Eye reflexes', 'glycolysis'), ('crFace', 'Face & jaw reflexes', 'glycogen'),
         ('crThroat', 'Throat & airway reflexes', 'tca'), ('crStem', 'Brainstem & lesions', 'ppp')],
  comps=[],
  nodes=[
    ('cr1', 'Pupillary light reflex', 2640, 1640, 'crEye', 'II in · III out, direct + consensual', ['pupilpath'], 'hub'),
    ('cr2', 'Near response', 2640, 1720, 'crEye', 'converge · accommodate · constrict', ['neartriad', 'accommodation', 'lensaccom']),
    ('cr3', 'Marcus Gunn pupil', 2640, 1800, 'crEye', 'partial afferent defect', ['rapd', 'opticneuritis']),
    ('cr4', 'Argyll Robertson pupil', 2640, 1880, 'crEye', 'light-near dissociation', ['lightnear']),
    ('cr5', 'Oculomotor nerve palsy', 2640, 1960, 'crStem', 'blown pupil · down and out', ['cn3palsy']),
    ('cr6', 'Corneal blink · eyelids', 2640, 2040, 'crFace', 'V1 in · both VII out', ['cnreflexes', 'eyelids'], 'hub'),
    ('cr7', 'Lacrimal gland', 2640, 2120, 'crFace', 'VII → pterygopalatine ganglion', ['lacrimal']),
    ('cr8', 'Bell palsy', 3110, 1640, 'crStem', 'whole half of the face', ['bell']),
    ('cr9', 'Trigeminal nerve', 3110, 1720, 'crFace', 'V1 corneal · V3 jaw', ['cavernous', 'trigeminal', 'chewing']),
    ('cr10', 'Gag · palate', 3110, 1800, 'crThroat', 'IX in · X out', ['jugfor', 'pharynxanat']),
    ('cr11', 'Cough', 3110, 1880, 'crThroat', 'X in · X out', ['coughreflex', 'laryngealnerves']),
    ('cr12', 'Solitary nucleus', 3110, 1960, 'crThroat', 'visceral relay · baroreflex', ['nts', 'baroreflex']),
    ('cr13', 'Brainstem strokes', 3110, 2040, 'crStem', 'PICA · AICA · Weber', ['wallenberg', 'aicastroke', 'weber']),
    ('cr14', 'Cranial nerve nuclei', 3110, 2120, 'crStem', 'motor medial · sensory lateral', ['cncomponents', 'pons']),
  ],
  panels=[
    (2420, 860, 1000, 'Cranial nerve reflexes (First Aid p. 519)', [
      ('Pupillary · accommodation', 'II in → III out'),
      ('Corneal', 'V1 (nasociliary) in → both VII out (orbicularis oculi)'),
      ('Lacrimation', 'V1 in → VII out — emotional tears survive'),
      ('Jaw jerk', 'V3 spindle in (masseter) → V3 motor out'),
      ('Gag', 'IX in → X out'),
      ('Cough', 'X in → X out, plus phrenic and spinal nerves'),
      ('Carotid sinus', 'IX in (X: aortic arch) — the baroreflex map moves it')]),
    (2420, 1110, 1000, 'One-sided lesion signs (First Aid p. 546; Moore ch 10; Fund. Neurosci. ch 14, 28)', [
      ('Afferent limb cut', 'no response on either side from that side'),
      ('Efferent limb cut', 'only that side fails, whichever side is tested'),
      ('CN V motor', 'jaw deviates toward the lesion'),
      ('CN X', 'uvula and palate pulled away from the lesion'),
      ('CN VII (LMN)', 'whole half of the face, forehead too; eye won’t close')]),
  ],
  dyn=dyn,
)
