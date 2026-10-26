# m56 — Hand, Wrist & Elbow Simulator (dynamic map, kit data) — coverage sweep m56 candidate #9.
# Three drawn views: (A) the right elbow from the front, palm up — humerus with both epicondyles, radius, ulna, the common
# extensor origin (ECRB) and the common flexor–pronator origin, the ulnar nerve behind the medial epicondyle; (B) the right
# wrist and hand, palm up — radius, ulna, eight carpals, metacarpals, phalanges, the transverse carpal ligament over the
# median nerve and the flexor tendons, Guyon canal (pisiform · hook of hamate) with the ulnar nerve, the first dorsal
# compartment (APL, EPB) at the radial styloid, the scaphoid with its retrograde blood supply, the thumb MCP ulnar collateral
# ligament, the ring-finger A1 pulley and the palmar fascia; (C) a finger from the side — metacarpal, three phalanges,
# extensor tendon (central slip, terminal tendon), FDS and FDP, A1/A2 pulleys, volar plate — whose joints MOVE: the normal
# fist, the jersey fist (DIP stays straight), the mallet droop, the trigger catch-and-snap, the Dupuytren contracture, the
# dorsal PIP dislocation and the boxer's head tipping toward the palm. One `one` switch in four sections picks the problem.
# Readouts (↑ = positive / present, ↓ = lost): epicondyle tenderness, Finkelstein, snuffbox tenderness, Tinel at the wrist,
# thumb MCP laxity on radial stress, finger held in flexion, active DIP motion.
#
# Sources (all read in the corpus; U+00A0/U+00AD normalized; the course texts win on any conflict):
#   OCOM Ortho SDL 14–15 lecture (Martin, Elbow wrist hand pain and injury): lateral = common extensor tendon, primarily
#     ECRB; medial = common flexor tendon; itis acute / osis chronic; 1–3% of the population; overuse of the wrist (sports,
#     manual laborers, office workers); eccentric overload; acute NSAIDs, steroid injection, unloader strap, OT; chronic OT,
#     nitroglycerin patches, regenerative injections, percutaneous tendon procedures · carpal tunnel: median nerve under the
#     transverse carpal ligament, F:M 3:1, pain worse in the morning / after repetitive activity, paresthesias, weakness;
#     Phalen, reverse Phalen, Tinel; clinical ± ultrasound ± NCS/EMG; bracing, injection, release · ulnar entrapment at the
#     wrist in Guyon's canal · de Quervain: first dorsal compartment at the radial styloid, APL + EPB, friction; women 30–50,
#     4–6 weeks after delivery; Finkelstein; radiographs not helpful, ultrasound shows the inflamed sheath; NSAIDs, OT,
#     bracing, injection, surgery rare · ganglion: synovial fluid leaks out of a joint (or tendon sheath) into its own cavity;
#     70% dorsal wrist (scapholunate ligament), 20% palmar wrist, 10% elsewhere; benign, non-fluctuant, well circumscribed,
#     painful if compressing; transillumination, ultrasound, MRI; observation, aspiration, injection, surgery · trigger finger:
#     stenosing flexor tenosynovitis, usually the A1 pulley at the MCP; 2%; women 40s–50s; multiple fingers, bilateral;
#     diabetes, RA, deposition diseases; painless snapping, pain at the pulley, worse in flexion, can lock in flexion; NSAIDs,
#     splinting, injection, surgery rare · thumb UCL (gamekeeper's, skier's): chronic degeneration or acute; forced
#     abduction and hyperextension of the MCP; partial tears skiing, complete tears non-sport falls; M:F 3:2; ulnar MCP pain,
#     worse pinching; laxity on valgus stress; X-ray, ultrasound, MRI; Stener lesion → ortho; thumb spica 3 weeks then ROM ·
#     mallet: extensor tendon of the DIP, most common finger tendon injury, can't actively extend the DIP, no passive limit;
#     full extension 6 weeks; fracture > 1/3 of the joint surface → ortho · jersey: FDP, forced extension against an actively
#     flexed DIP, contact sports, ring finger 75%; volar DIP pain and swelling, can't flex the DIP; X-ray, MRI if unclear;
#     splint PIP and DIP in mild flexion; refer all cases.
#   OCOM SDL 14–15 readings: Atlas of Emergency Medicine 5e ch 11.17 (mallet: forced flexion of an actively extended DIP or an
#     axial blow, DIP held passively flexed, dorsal avulsion chip; splint the DIP in extension continuously ≥ 6 weeks, PIP
#     free; jersey: grabbing a jersey, ring finger, test DIP flexion with the MCP and PIP held extended, prognosis worse with
#     delay or retraction) and ch 11.15 (gamekeeper's: forced radial deviation (abduction); tear usually at the proximal
#     phalanx; stress in extension and 30° flexion; > 30–40° = complete; firm end point; skier's acute, gamekeeper's
#     repetitive; Stener lesion = adductor aponeurosis between the torn ends, MRI gold standard; complete tears repair within
#     1 week; late arthritis) · Tintinalli 9e ch 283 (trigger: ring finger and thumb, A1 pulley at the volar crease, nodule,
#     binding as the finger extends then a painful snap, locks in flexion, buddy tape/splint, injection, A1 release; de
#     Quervain: pregnancy, postpartum, lifting a child, Finkelstein = thumb in the fist, examiner ulnar-deviates → pain along
#     the tendons, thumb spica; carpal tunnel: index, long, radial ring and palmar thumb, wakes at night, Tinel over the
#     median nerve, Phalen ≥ 1 minute, motor deficit → emergency hand consult, volar splint wrist neutral; Dupuytren:
#     fourth and fifth fingers earliest, men of northern European descent, tobacco, alcohol, diabetes, nodule at the distal
#     palmar crease; ganglion: herniated synovium, about one third resolve spontaneously, excision recurs less than aspiration).
#   OCOM Ortho SDL 25 readings: Current Diagnosis & Treatment in Orthopedics ch 3 (lateral epicondylitis: tenderness at the
#     ECRB origin just distal to the epicondyle, pain with resisted wrist extension most marked with the elbow extended,
#     normal motion, radiographs usually normal (< 10% calcification), MRI of questionable aid, counterforce brace, steroid or
#     PRP injection, release of the common extensor origin, angiofibroblastic degeneration; medial: valgus forces such as
#     throwing, flexor–pronator origin (pronator teres, FCU), ulnar nerve compression may occur with it, the tendon is
#     reattached rather than released) · ch 11 (de Quervain: thickened retinaculum over the first dorsal compartment,
#     forearm-based thumb spica leaving the IP free, injection beats splinting; trigger: A1 pulley, 2–3%, ring and long
#     fingers, worse in the morning, diabetes, injection 60–90%, A1 release; carpal tunnel: Tinel, Phalen within 60 s,
#     palmar cutaneous branch spared, night splint in neutral; ulnar tunnel: pisiform and hook of hamate, ganglion, ulnar
#     artery, hook fracture; Tinel at the wrist not the elbow, more prominent clawing, dorsal hand sensation spared;
#     Dupuytren: myofibroblasts, type III collagen, 40–60, M:F 2:1, MCP then PIP, little and ring fingers, northern European,
#     alcohol, diabetes, antiepileptics, HIV; treat a fixed MCP contracture > 30° or any PIP contracture; collagenase, needle
#     aponeurotomy, fasciectomy; recurrence; scaphoid: commonest carpal fracture, 15% of wrist injuries, blood enters
#     distally, waist 65%, ~1/3 of waist and ~100% of proximal pole fractures develop ischemic necrosis, displaced → ORIF;
#     boxer's: the neck is the weakest part of the metacarpal, direct blow, apex dorsal angulation, ring and little fingers
#     tolerate more because their CMC joints move, rotation unacceptable, "marble in the palm", ulnar gutter splint) ·
#     Tintinalli 9e ch 268 (splint table; jersey: zone I, ring finger, PIP and MCP still flex; mallet: zone I, forced flexion
#     of an extended DIP, splint in full extension 6–8 weeks, never let it flex, chronic → swan neck; PIP: axial load and
#     hyperextension, dorsal dislocation when the volar plate ruptures, reduce, test motion, splint 30° flexion 3 weeks,
#     irreducible → surgery, untreated → swan neck; thumb UCL: tear at the proximal phalanx, Stener lesion needs surgery,
#     weakness of pinch, > 30–35° or 10–15° more than the other thumb = complete, thumb spica, repair within 1 week;
#     metacarpal neck: direct impaction, 5th = boxer's fracture, pseudoclaw, rotation not acceptable; a laceration over the
#     metacarpal head or MCP = human bite until proven otherwise).
#   OCOM Ortho SDL 9 reading (Practical Office Orthopedics ch 8): boxer's = distal fifth metacarpal; scaphoid blood supply
#     poor, nondisplaced fractures hard to see; snuffbox tenderness → splint wrist and thumb, repeat X-ray at 7–10 days;
#     nondisplaced 6–8 weeks in a thumb spica cast; displaced → surgery.
#   First Aid 2025 p. 453 (scaphoid: snuffbox, most common carpal fracture, FOOSH, proximal fractures → AVN and nonunion from
#     the retrograde radial-artery supply, occult on the first X-ray; hook of hamate → Guyon) · p. 462 (golfer's: repetitive
#     wrist flexion; tennis: repetitive wrist extension, backhand) · p. 463 (Guyon: cyclists' handlebars, hook of hamate;
#     carpal tunnel: palmar cutaneous branch spared, Tinel, Phalen, pregnancy, RA, hypothyroidism, diabetes, acromegaly,
#     dialysis amyloid; boxer's: 5th metacarpal neck, young males punching a wall, reduced grip strength) · p. 465 (de
#     Quervain: noninflammatory thickening of APL and EPB, Finkelstein, new mothers, golfers, racquet players, texters;
#     Dupuytren: fibroblastic proliferation of the superficial palmar fascia, base of ring and little fingers, males > 50,
#     Northern European; ganglion: mucin-filled, dorsal wrist, transilluminates, tumors don't).
#   Moore ch 3 (snuffbox bounded by APL/EPB and EPL, radial artery in its floor; scaphoid pain in the snuffbox, X-ray at 10–14
#     days, poor proximal supply, AVN; boxer's: the head rotates over the shaft, a flexion deformity; mallet: hyperflexion of
#     the DIP avulses the extensor from the distal phalanx; tennis elbow: common extensor origin; Dupuytren pulls the 4th and
#     5th fingers into flexion at the MCP and PIP; ulnar canal syndrome: medial 1½ fingers, intrinsics, clawing, flexion kept).
#   Bootcamp.com MSK — Shoulder & elbow (epicondylitis: lateral elbow pain worsened with palpation and wrist extension, medial
#     with palpation and wrist flexion; ages 40–60) · Wrist & hand (scaphoid ↓ grip strength; Dupuytren table-top test).
# CONFLICTS (course text kept): ganglion — the SDL 14–15 lecture says "non-fluctuant" and Tintinalli "about one third resolve",
#   First Aid "usually resolves spontaneously", Bootcamp "fluctuant"; boxer's acceptable angulation — Tintinalli ≤ 40° for the
#   5th, CDT 50–60° (no number printed); boxer's splint angles differ within Tintinalli (table: 20° wrist flexion, 90° MCP; text:
#   20° wrist extension, 70° MCP) — the map says only "ulnar gutter splint"; scaphoid cast — POO ch 8 thumb spica, CDT ch 11
#   "thumb not necessary for nondisplaced waist fractures" (map: "splint the wrist and thumb" for the suspected fracture, POO);
#   thumb UCL immobilization 3 weeks (lecture) vs 4–6 weeks (Atlas) — no number printed; trigger finger — ring + thumb
#   (Tintinalli) vs ring + long (CDT): only "the ring finger" is drawn.
# CUT for lack of a source or to stay out of other maps: the nerve deficits themselves (sensory maps, claw/benediction —
#   plexsim), supracondylar / Colles / Monteggia / Galeazzi / elbow dislocation / nursemaid's (fxsim, elbowinj, nursemaid —
#   pinned only), cubital tunnel (no option — the medial note mentions the nerve), Leddy-Packer timing (lecture names the
#   classification only), a grip-strength readout (only Bootcamp/FA for some options), hand osteoarthritis (orthowork).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

MOORE3 = full('Moore', 3)
SDL1415 = 'OCOM Ortho — SDL 14–15 lecture & readings: Elbow, wrist and hand pain and injury (Martin; Atlas of Emergency Medicine)'
SDL25 = 'OCOM Ortho — SDL 25 readings: Joint dislocations (Current Diagnosis & Treatment in Orthopedics ch 2, 11)'
SDL9R = 'OCOM Ortho — SDL 9 reading: Fracture management (Practical Office Orthopedics ch 8)'
BC_ELB = 'Bootcamp.com MSK — Shoulder & elbow'
BC_HAND = 'Bootcamp.com MSK — Wrist & hand'

O = lambda *k: ['hd:' + x for x in k]
ANY = ['hd:*']

shapes = []
def add(svg, when=None, unless=None):
    if when is None and unless is None: shapes.append(svg); return
    d = dict(svg=svg)
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def text(t, x, y, cls='nf-l2', anchor=None, when=None, unless=None):
    d = dict(text=t, x=round(x), y=round(y), cls=cls)
    if anchor: d['anchor'] = anchor
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def lead(x0, y0, x1, y1, when=None, unless=None):
    add(f'<path d="M{round(x0)} {round(y0)} L{round(x1)} {round(y1)}" class="dyn-line" style="stroke-width:1.5;opacity:.7"/>', when, unless)
TAG = 'nf-l2 dyn-tag'
TAG1 = 'nf-l1 dyn-tag'
BONE = 'class="dyn-cell" style="stroke:var(--dk10)"'
LIGC = 'var(--dk6)'
TEND = 'var(--dk10)'
MED_N, ULN_N = 'var(--dk5)', 'var(--dk1)'
FASC = 'var(--dk8)'

def capsule(a, b, hw):
    """a bone: a rounded bar from a to b, half-width hw"""
    (x0, y0), (x1, y1) = a, b
    L = math.hypot(x1 - x0, y1 - y0); nx, ny = -(y1 - y0) / L * hw, (x1 - x0) / L * hw
    f = lambda v: round(v, 1)
    return (f'M{f(x0 + nx)} {f(y0 + ny)} L{f(x1 + nx)} {f(y1 + ny)} A{hw} {hw} 0 0 0 {f(x1 - nx)} {f(y1 - ny)} '
            f'L{f(x0 - nx)} {f(y0 - ny)} A{hw} {hw} 0 0 0 {f(x0 + nx)} {f(y0 + ny)} Z')
def shift(d, dx, dy=0):
    """move every coordinate pair of a path (absolute M/L/C/Q commands only)"""
    import re
    toks = re.findall(r'[A-Za-z]|-?\d+(?:\.\d+)?', d); out = []; nums = []
    for t in toks:
        if t.isalpha(): out.append(t)
        else:
            nums.append(float(t))
            if len(nums) == 2: out.append(f'{round(nums[0] + dx)} {round(nums[1] + dy)}'); nums = []
    return ' '.join(out)
ZZ = lambda x, y, s=1: (f'<path d="M{round(x - 16 * s)} {round(y - 12 * s)} L{round(x - 5 * s)} {round(y + 10 * s)} '
                        f'L{round(x + 5 * s)} {round(y - 10 * s)} L{round(x + 16 * s)} {round(y + 12 * s)}" class="dyn-lesion"/>')
def ZZr(x, y, deg, s=1):
    return f'<g transform="rotate({deg} {round(x)} {round(y)})">{ZZ(x, y, s)}</g>'

# ════════ title ════════
text('Elbow, wrist and hand — what is strained, torn or squeezed, and which test turns positive', 160, 140, 'dyn-big')
text('a right arm, palm up, in three views · pick a problem on the right', 160, 162, 'dyn-cap')

# ════════ VIEW B — the wrist and hand, palm up (drawn in a local frame, then moved left by 620) ════════
HX = -620
def H(x, y): return (x + HX, y)
def hp(d): return shift(d, HX)
text('Wrist and hand', 160, 214, 'dyn-big')
text('right hand, palm up · thumb (radial) side on the right', 160, 234, 'dyn-cap')

FING = dict(little=((1022, 585), (975, 335)), ring=((1098, 575), (1089, 285)), middle=((1172, 570), (1186, 255)),
            index=((1250, 575), (1293, 300)))
THUMB_SK = 'M1300 770 L1372 662 L1470 525'
PALM = ('M995 590 C985 700 995 820 1010 900 L1005 1172 L1342 1172 L1352 935 C1350 880 1338 836 1322 800 '
        'C1312 780 1300 760 1296 735 C1300 690 1306 640 1300 600 C1280 580 1260 575 1240 575 L1020 575 Z')
sk = []
for a, b in FING.values():
    A, B = H(*a), H(*b); sk.append(f'M{A[0]} {A[1]} L{B[0]} {B[1]}')
skin_o = ''.join(f'<path d="{d}" style="fill:none;stroke:var(--ink-3);stroke-opacity:.45;stroke-width:64;stroke-linecap:round"/>' for d in sk)
skin_o += f'<path d="{hp(THUMB_SK)}" style="fill:none;stroke:var(--ink-3);stroke-opacity:.45;stroke-width:70;stroke-linecap:round;stroke-linejoin:round"/>'
skin_o += f'<path d="{hp(PALM)}" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-opacity:.45;stroke-width:4"/>'
skin_f = ''.join(f'<path d="{d}" style="fill:none;stroke:var(--surface-2);stroke-width:59;stroke-linecap:round"/>' for d in sk)
skin_f += f'<path d="{hp(THUMB_SK)}" style="fill:none;stroke:var(--surface-2);stroke-width:65;stroke-linecap:round;stroke-linejoin:round"/>'
skin_f += f'<path d="{hp(PALM)}" style="fill:var(--surface-2);stroke:none"/>'
add(skin_o + skin_f)
# forearm bones
RADIUS = 'M1200 1170 L1330 1170 C1335 1060 1340 960 1354 918 C1352 900 1330 892 1300 895 L1212 905 C1205 960 1200 1060 1200 1170 Z'
ULNA = 'M1010 1170 L1088 1170 C1086 1060 1084 960 1080 928 C1070 908 1040 902 1020 910 C1012 920 1008 932 1010 945 C1010 1000 1010 1080 1010 1170 Z'
add(f'<path d="{hp(RADIUS)}" {BONE}/><path d="{hp(ULNA)}" {BONE}/>')
# carpals
def ell(cx, cy, rx, ry, rot=0, extra=BONE):
    x, y = H(cx, cy)
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" {extra}' + (f' transform="rotate({rot} {x} {y})"' if rot else '') + '/>'
carp = (ell(1078, 868, 26, 24) + ell(1142, 874, 30, 26) + ell(1084, 795, 30, 30) + ell(1150, 790, 30, 36) +
        ell(1212, 796, 22, 25) + ell(1272, 810, 28, 26))
add(carp)
SCAPH = (1238, 862)
add(ell(*SCAPH, 46, 21, -40), unless=O('scaph'))
add(ell(1030, 882, 17, 17))                       # pisiform (on the triquetrum, palmar)
add(ell(1092, 816, 9, 13, 20))                    # hook of the hamate
# metacarpals and phalanges
BONES_H = dict(
  mc5=((1070, 760), (1022, 578), 13), mc4=((1115, 755), (1099, 563), 14), mc3=((1160, 752), (1172, 556), 15),
  mc2=((1210, 760), (1249, 563), 14), mc1=((1292, 778), (1368, 668), 15),
  l1=((1018, 562), (998, 464), 11), l2=((995, 452), (985, 398), 10), l3=((983, 388), (978, 352), 9),
  r1=((1098, 546), (1094, 432), 12), r2=((1093, 420), (1091, 356), 11), r3=((1091, 345), (1090, 302), 10),
  m1=((1173, 540), (1179, 412), 12), m2=((1181, 400), (1184, 328), 11), m3=((1184, 317), (1186, 272), 10),
  i1=((1251, 548), (1271, 438), 12), i2=((1274, 427), (1285, 366), 11), i3=((1286, 355), (1292, 316), 10),
)
THUMB_P = dict(t1=((1380, 652), (1430, 588), 13), t2=((1437, 578), (1466, 540), 11))
def bone_h(k, table=BONES_H, style=BONE):
    a, b, w = table[k]
    return f'<path d="{capsule(H(*a), H(*b), w)}" {style}/>'
add(''.join(bone_h(k) for k in BONES_H))
# flexor tendons through the carpal tunnel to the fingers (faint)
for fx, tx in ((1030, 1022), (1100, 1099), (1170, 1172), (1240, 1249)):
    x0 = H(1150 + (fx - 1150) * .35, 0)[0]; x1 = H(1150 + (fx - 1150) * .45, 0)[0]; x2 = H(tx, 0)[0]
    add(f'<path d="M{x0:.0f} 1170 L{x1:.0f} 850 C{x1:.0f} 760 {x2} 680 {x2} 600" style="fill:none;stroke:{TEND};stroke-width:5;opacity:.45"/>')
# median nerve (under the TCL) and its fingers
MED_TRUNK = 'M1185 1170 L1180 920 C1178 870 1175 830 1172 790 C1170 770 1168 755 1168 740'
MED_BR = ['M1168 740 C1230 720 1300 690 1395 620', 'M1168 740 C1210 680 1245 620 1262 470',
          'M1168 740 C1172 680 1178 600 1180 460', 'M1168 740 C1140 690 1112 620 1102 470']
ULN_TRUNK = 'M1058 1170 L1058 930 C1058 880 1059 845 1058 820 C1056 790 1048 760 1045 740'
ULN_BR = ['M1045 740 C1030 680 1015 620 1000 470', 'M1045 740 C1068 680 1080 620 1086 470']
def nerve(d, col, w=7, op=.9): return f'<path d="{hp(d)}" style="fill:none;stroke:{col};stroke-width:{w};stroke-linecap:round;opacity:{op}"/>'
add(nerve(MED_TRUNK, MED_N) + ''.join(nerve(d, MED_N, 4, .75) for d in MED_BR))
add(nerve(ULN_TRUNK, ULN_N) + ''.join(nerve(d, ULN_N, 4, .75) for d in ULN_BR))
# transverse carpal ligament (roof of the carpal tunnel) and the volar carpal ligament (roof of Guyon canal)
TCL = 'M1040 838 C1100 816 1230 816 1292 838'
add(f'<path d="{hp(TCL)}" style="fill:none;stroke:{LIGC};stroke-width:22;stroke-linecap:round;opacity:.5"/>', unless=O('ct'))
add(f'<path d="{hp(TCL)}" style="fill:none;stroke:var(--bad);stroke-width:24;stroke-linecap:round;opacity:.55"/>'
    + nerve('M1180 900 L1172 790', 'var(--bad)', 4, 1), when=O('ct'))
GUY = 'M1036 852 L1084 846'
add(f'<path d="{hp(GUY)}" style="fill:none;stroke:{LIGC};stroke-width:12;stroke-linecap:round;opacity:.45"/>', unless=O('guyon'))
add(f'<path d="{hp(GUY)}" style="fill:none;stroke:var(--bad);stroke-width:14;stroke-linecap:round;opacity:.6"/>'
    + nerve('M1058 900 L1058 812', 'var(--bad)', 4, 1) + ell(1092, 816, 16, 20, 20, 'class="dyn-hl"'), when=O('guyon'))
# radial artery and the scaphoid's retrograde supply
add(f'<path d="{hp("M1318 1170 C1322 1060 1326 960 1314 860")}" style="fill:none;stroke:var(--nf-blood);stroke-width:4;opacity:.55"/>')
# first dorsal compartment: APL to the 1st metacarpal base, EPB to the thumb proximal phalanx, under the retinaculum
APL = 'M1338 1120 C1350 1020 1362 950 1362 905 C1358 860 1336 812 1306 786'
EPB = 'M1348 1120 C1360 1020 1372 950 1371 905 C1366 860 1350 800 1338 760 C1350 720 1366 690 1378 660'
for d in (APL, EPB):
    add(f'<path d="{hp(d)}" style="fill:none;stroke:{TEND};stroke-width:5;opacity:.8"/>', unless=O('dq'))
    add(f'<path d="{hp(d)}" style="fill:none;stroke:var(--bad);stroke-width:7;opacity:.85"/>', when=O('dq'))
rx, ry = H(1344, 902)
add(f'<rect x="{rx}" y="{ry}" width="40" height="18" rx="5" style="fill:{LIGC};opacity:.5"/>', unless=O('dq'))
add(f'<rect x="{rx - 4}" y="{ry - 4}" width="48" height="26" rx="6" style="fill:var(--bad);opacity:.45"/>', when=O('dq'))
# thumb: metacarpal fixed, phalanges swing on radial stress (gamekeeper's)
MCP_T = (1374, 659)
u = (0.57, -0.82); nU = (-0.82, -0.57)
def tpt(t, s): return H(MCP_T[0] + u[0] * t + nU[0] * s, MCP_T[1] + u[1] * t + nU[1] * s)
UCL_A, UCL_B = tpt(-15, 17), tpt(15, 17)
def thumb_ph(ang=0, torn=False):
    inner = bone_h('t1', THUMB_P) + bone_h('t2', THUMB_P)
    cx, cy = H(*MCP_T)
    if torn:
        a2 = tpt(5, 17)
        inner += f'<path d="M{a2[0]:.0f} {a2[1]:.0f} L{UCL_B[0]:.0f} {UCL_B[1]:.0f}" style="stroke:var(--bad);stroke-width:8;stroke-linecap:round"/>'
    else:
        inner += f'<path d="M{UCL_A[0]:.0f} {UCL_A[1]:.0f} L{UCL_B[0]:.0f} {UCL_B[1]:.0f}" style="stroke:{LIGC};stroke-width:8;stroke-linecap:round;opacity:.9"/>'
    if not ang: return f'<g>{inner}</g>'
    return (f'<g><animateTransform attributeName="transform" type="rotate" values="0 {cx} {cy};{ang} {cx} {cy};{ang} {cx} {cy};0 {cx} {cy};0 {cx} {cy}" '
            f'keyTimes="0;.3;.6;.85;1" dur="3s" repeatCount="indefinite"/>{inner}</g>')
add(thumb_ph(), unless=O('ucl'))
add(thumb_ph(26, True), when=O('ucl'))
a1 = tpt(-5, 17)
add(f'<path d="M{UCL_A[0]:.0f} {UCL_A[1]:.0f} L{a1[0]:.0f} {a1[1]:.0f}" style="stroke:var(--bad);stroke-width:8;stroke-linecap:round"/>'
    f'<path d="M{tpt(-26, 30)[0]:.0f} {tpt(-26, 30)[1]:.0f} L{tpt(6, 22)[0]:.0f} {tpt(6, 22)[1]:.0f}" style="stroke:{FASC};stroke-width:6;stroke-linecap:round;opacity:.9"/>',
    when=O('ucl'))
# scaphoid states: normal / fractured at the waist with the proximal pole starved
add(ell(*SCAPH, 46, 21, -40, 'class="dyn-cell" style="stroke:var(--bad)"') + ell(*SCAPH, 56, 30, -40, 'class="dyn-hl"'), when=O('scaph'))
sx, sy = H(*SCAPH)
add(f'<path d="M{sx - 4} {sy + 2} A46 21 0 0 0 {sx - 35} {sy + 30} A46 21 0 0 0 {sx + 4} {sy - 2} Z" style="fill:var(--dyn-lost);opacity:.55" '
    f'transform="rotate(0 {sx} {sy})"/>' + ZZr(sx, sy, 50, .9), when=O('scaph'))
# boxer's: the 5th metacarpal neck
bx, by = H(1027, 602)
add(ZZr(bx, by, -15, .9) + f'<circle cx="{bx}" cy="{by}" r="26" class="dyn-hl"/>', when=O('boxer'))
# trigger finger: the ring finger's A1 pulley over its MCP, with a nodule on the tendon
ax, ay = H(1097, 553)
add(f'<rect x="{ax - 18}" y="{ay - 6}" width="36" height="12" rx="4" style="fill:{LIGC};opacity:.55"/>', unless=O('trigger'))
add(f'<rect x="{ax - 20}" y="{ay - 7}" width="40" height="14" rx="4" style="fill:var(--bad);opacity:.7"/>'
    f'<ellipse cx="{ax}" cy="{ay + 26}" rx="9" ry="12" style="fill:{TEND}"/><circle cx="{ax}" cy="{ay + 8}" r="30" class="dyn-hl"/>', when=O('trigger'))
# palmar fascia (thin) / Dupuytren cords and a nodule at the distal palmar crease
PF = ['M1110 760 C1106 680 1102 620 1098 560', 'M1090 770 C1060 700 1035 640 1022 580']
add(''.join(f'<path d="{hp(d)}" style="fill:none;stroke:{FASC};stroke-width:3;opacity:.5;stroke-dasharray:6 5"/>' for d in PF), unless=O('dup'))
nx_, ny_ = H(1100, 612)
add(''.join(f'<path d="{hp(d)}" style="fill:none;stroke:{FASC};stroke-width:13;stroke-linecap:round;opacity:.85"/>' for d in PF)
    + f'<ellipse cx="{nx_}" cy="{ny_}" rx="15" ry="12" style="fill:{FASC}"/>', when=O('dup'))
# ganglion: a dorsal cyst seen through the hand, from the scapholunate joint
gx, gy = H(1192, 884)
add(f'<circle cx="{gx}" cy="{gy}" r="40" style="fill:var(--nf-h2o);fill-opacity:.25;stroke:var(--nf-h2o);stroke-width:3;stroke-dasharray:7 5"/>'
    f'<circle cx="{gx}" cy="{gy}" r="52" class="dyn-hl" style="opacity:.45"/>', when=O('ganglion'))
# finger dislocation, mallet, jersey on the hand: mark the ring finger joint
px_, py_ = H(1092, 426)
add(f'<circle cx="{px_}" cy="{py_}" r="22" class="dyn-hl"/>', when=O('pipdis'))
dx_, dy_ = H(1091, 350)
add(f'<circle cx="{dx_}" cy="{dy_}" r="20" class="dyn-hl"/>', when=O('mallet', 'jersey'))

# hand labels — ulnar side (left) and radial side (right)
LXh, RXh = 330, 790
def labh(side, y, normal, to, when_red=None, red=''):
    x = LXh if side == 'L' else RXh; an = 'end' if side == 'L' else 'start'
    tx, ty = H(*to)
    lead(x + (6 if side == 'L' else -6), y - 4, tx, ty)
    text(normal, x, y, 'nf-l2', an, unless=when_red or None)
    if when_red: text(red, x, y, TAG1, an, when=when_red)
labh('L', 470, 'flexor tendon → fingertip', (1093, 500))
labh('L', 548, 'A1 pulley (ring finger)', (1084, 553), O('trigger'), 'A1 pulley — tendon catches')
labh('L', 604, '5th metacarpal neck', (1018, 600), O('boxer'), '5th metacarpal neck — broken')
labh('L', 660, 'palmar fascia', (1094, 650), O('dup'), 'palmar fascia — cords')
labh('L', 722, 'ulnar nerve', (1040, 712))
labh('L', 790, 'hook of the hamate', (1086, 812))
labh('L', 850, 'Guyon canal', (1058, 850), O('guyon'), 'Guyon canal — nerve squeezed')
labh('L', 910, 'pisiform', (1022, 888))
labh('L', 1080, 'ulna', (1030, 1080))
labh('R', 708, 'thumb UCL (ulnar side of the MCP)', (1358, 652), O('ucl'), 'thumb UCL — torn')
labh('R', 796, 'transverse carpal ligament', (1290, 834), O('ct'), 'transverse carpal ligament — tunnel crowded')
labh('R', 856, 'scaphoid — under the anatomic snuffbox', (1268, 846), O('scaph'), 'scaphoid — waist fracture')
labh('R', 914, 'first dorsal compartment (APL, EPB)', (1364, 910), O('dq'), 'APL + EPB — rubbing at the radial styloid')
labh('R', 1000, 'median nerve', (1181, 1000))
labh('R', 1060, 'radial artery', (1320, 1060))
labh('R', 1110, 'radius', (1290, 1110))
text('Stener lesion: adductor aponeurosis between the ends', 790, 732, TAG, when=O('ucl'))
text('blood enters distally — the proximal pole is starved', 790, 878, TAG, when=O('scaph'))
text('dorsal cyst, seen through — scapholunate joint', 790, 940, TAG, when=O('ganglion'))
text('tingling: thumb to half the ring · palm spared', 790, 1018, TAG, when=O('ct'))
text('tingling: little + half the ring', 330, 744, TAG, 'end', when=O('guyon'))
text('handlebar', 330, 960, 'nf-l1', 'end', when=O('guyon'))
text('nodule at the distal palmar crease', 330, 682, TAG, 'end', when=O('dup'))

# ════════ VIEW A — the right elbow from the front (local frame, moved right by 870) ════════
EX = 870
def E(x, y): return (x + EX, y)
def ep(d): return shift(d, EX)
text('Elbow', 1300, 214, 'dyn-big', 'middle')
text('from the front · lateral (thumb) side on the right', 1300, 234, 'dyn-cap', 'middle')
EXT_M = 'M548 470 C590 500 612 560 608 640 C604 720 592 780 572 830 L540 830 C552 760 562 700 562 640 C562 580 548 520 530 495 Z'
FLX_M = 'M298 470 C258 500 242 560 248 640 C254 720 270 780 290 830 L322 830 C306 760 296 700 296 640 C296 580 306 520 322 495 Z'
add(f'<path d="{ep(EXT_M)}" class="dyn-soft"/><path d="{ep(FLX_M)}" class="dyn-soft"/>')
HUM = ('M400 250 L460 250 L462 405 C495 420 545 440 562 462 C570 474 560 488 545 492 C540 505 530 520 505 528 C490 532 478 530 '
       '468 522 C455 532 430 540 400 538 C380 536 368 528 360 515 C340 505 300 490 286 474 C278 462 288 450 300 446 C340 432 380 420 398 405 Z')
ULNA_E = 'M362 546 C382 550 420 554 440 547 L432 600 C425 640 418 700 415 830 L385 830 C382 700 375 640 366 600 Z'
RAD_E = ('M478 540 C490 536 515 536 525 542 L522 562 C518 566 510 568 506 572 L512 640 C520 700 528 760 532 830 L502 830 '
         'C496 760 488 700 482 640 L478 572 C474 568 472 562 474 556 Z')
add(f'<path d="{ep(ULNA_E)}" {BONE}/><path d="{ep(RAD_E)}" {BONE}/><path d="{ep(HUM)}" {BONE}/>')
ULN_E = 'M330 250 C320 330 300 400 296 440 C292 480 318 520 340 560 C356 620 370 720 380 830'
add(f'<path d="{ep(ULN_E)}" style="fill:none;stroke:{ULN_N};stroke-width:6;stroke-dasharray:9 6;opacity:.8"/>')
LAT_O, MED_O = 'M560 474 C572 492 580 510 584 532', 'M290 474 C278 492 270 510 266 532'
add(f'<path d="{ep(LAT_O)}" style="fill:none;stroke:{TEND};stroke-width:10;stroke-linecap:round;opacity:.8"/>', unless=O('lat'))
add(f'<path d="{ep(MED_O)}" style="fill:none;stroke:{TEND};stroke-width:10;stroke-linecap:round;opacity:.8"/>', unless=O('med'))
add(f'<path d="{ep(LAT_O)}" style="fill:none;stroke:var(--bad);stroke-width:12;stroke-linecap:round"/>'
    f'<circle cx="{E(566, 478)[0]}" cy="478" r="30" class="dyn-hl"/>', when=O('lat'))
add(f'<path d="{ep(MED_O)}" style="fill:none;stroke:var(--bad);stroke-width:12;stroke-linecap:round"/>'
    f'<circle cx="{E(284, 478)[0]}" cy="478" r="30" class="dyn-hl"/>', when=O('med'))
def labe(side, y, normal, to, when_red=None, red=''):
    x = 1115 if side == 'L' else 1482; an = 'end' if side == 'L' else 'start'
    tx, ty = E(*to)
    lead(x + (6 if side == 'L' else -6), y - 4, tx, ty)
    text(normal, x, y, 'nf-l2', an, unless=when_red or None)
    if when_red: text(red, x, y, TAG1, an, when=when_red)
labe('L', 300, 'humerus', (402, 300))
labe('L', 462, 'medial epicondyle', (288, 466), O('med'), 'medial epicondyle — tender')
labe('L', 544, 'common flexor–pronator origin', (270, 520), O('med'), 'flexor–pronator origin — strained')
labe('L', 640, 'ulnar nerve, behind the epicondyle', (316, 600))
labe('L', 780, 'ulna', (392, 780))
labe('R', 462, 'lateral epicondyle', (560, 466), O('lat'), 'lateral epicondyle — tender')
labe('R', 544, 'common extensor origin (ECRB)', (582, 524), O('lat'), 'ECRB origin — strained')
labe('R', 780, 'radius', (528, 780))
text('forearm extensors', 1300 + 120, 690, 'nf-l2', 'start')
text('flexors', 1300 - 168, 690, 'nf-l2', 'end')
text('resisted wrist extension → pain', 1300, 868, TAG1, 'middle', when=O('lat'))
text('wrist flexion, pronation, throwing → pain', 1300, 868, TAG1, 'middle', when=O('med'))

# ════════ VIEW C — a finger from the side; the joints move ════════
Y = 560
MCP, PIP, DIP, NECK = (1960, Y), (2125, Y), (2230, Y), (1915, Y)
text('A finger from the side', 1960, 380, 'dyn-big', 'start')
text('back of the hand up · fingertip on the right', 1960, 400, 'dyn-cap', 'start')
def skin(x0, x1, w):
    return (f'<path d="M{x0} {Y} L{x1} {Y}" style="fill:none;stroke:var(--ink-3);stroke-opacity:.45;stroke-width:{w + 4};stroke-linecap:round"/>'
            f'<path d="M{x0} {Y} L{x1} {Y}" style="fill:none;stroke:var(--surface-2);stroke-width:{w};stroke-linecap:round"/>')
def tln(x0, y0, x1, y1, col=TEND, w=6, op=.9):
    return f'<path d="M{x0} {y0} L{x1} {y1}" style="fill:none;stroke:{col};stroke-width:{w};stroke-linecap:round;opacity:{op}"/>'
def rotg(c, vals, inner, kt=None, dur=4, extra=''):
    """a group turned about c — static if one angle, animated if several"""
    cx, cy = c
    if isinstance(vals, (int, float)):
        t = f' transform="{extra}rotate({vals} {cx} {cy})"' if (vals or extra) else ''
        return f'<g{t}>{inner}</g>'
    kt = kt or ';'.join(f'{i / (len(vals) - 1):.2f}' for i in range(len(vals)))
    v = ';'.join(f'{a} {cx} {cy}' for a in vals)
    return (f'<g><animateTransform attributeName="transform" type="rotate" values="{v}" keyTimes="{kt}" dur="{dur}s" '
            f'repeatCount="indefinite"/>{inner}</g>')
def finger(head=0, p=0, m=0, d=0, kt=None, dur=4, mallet=False, jersey=False, trigger=False, dup=False, pip=False, boxer=False):
    # distal phalanx
    g3 = skin(2230, 2300, 44) + f'<path d="{capsule((2238, Y), (2298, Y), 11)}" {BONE}/>'
    if not mallet: g3 += tln(2226, Y - 14, 2244, Y - 13, w=7)
    else: g3 += tln(2232, Y - 14, 2244, Y - 13, 'var(--bad)', 7)
    if not jersey: g3 += tln(2226, Y + 15, 2248, Y + 12, w=7)
    else: g3 += tln(2236, Y + 14, 2248, Y + 12, 'var(--bad)', 7)
    # middle phalanx
    g2 = skin(2125, 2230, 50) + f'<path d="{capsule((2134, Y), (2222, Y), 13)}" {BONE}/>'
    g2 += tln(2122, Y - 19, 2142, Y - 17, w=9)                                  # central slip into its base
    g2 += tln(2125, Y - 17, 2205 if mallet else 2230, Y - 15, 'var(--bad)' if mallet else TEND, 6)   # terminal tendon
    g2 += tln(2125, Y + 23, 2152, Y + 16, w=7)                                  # FDS into its base
    if not jersey: g2 += tln(2125, Y + 19, 2230, Y + 16)                       # FDP on to the tip
    g2 += tln(2110, Y + 14, 2142, Y + 14, 'var(--bad)' if pip else LIGC, 9, .85)   # volar plate
    g2 += rotg(DIP, d, g3, kt, dur)
    # proximal phalanx
    g1 = skin(1960, 2125, 56) + f'<path d="{capsule((1970, Y), (2116, Y), 15)}" {BONE}/>'
    g1 += tln(1960, Y - 21, 2125, Y - 19)                                      # extensor hood
    g1 += tln(1960, Y + 27, 2125, Y + 23)                                      # FDS
    if not jersey: g1 += tln(1960, Y + 21, 2125, Y + 19)                       # FDP
    g1 += f'<rect x="2000" y="{Y + 15}" width="62" height="18" rx="5" style="fill:{LIGC};opacity:.45"/>'   # A2 pulley
    if pip:
        g1 += rotg(PIP, -6, g2, extra='translate(-30 -34) ')
    else:
        g1 += rotg(PIP, m, g2, kt, dur)
    # metacarpal head (turns in a boxer's fracture)
    gh = skin(1915, 1960, 66) + f'<path d="{capsule((1912, Y), (1950, Y), 17)}" {BONE}/>'
    gh += tln(1915, Y - 22, 1960, Y - 21)
    gh += tln(1915, Y + 28, 1960, Y + 27)
    if not jersey: gh += tln(1915, Y + 22, 1960, Y + 21)
    a1c = 'var(--bad)' if trigger else LIGC
    gh += f'<rect x="1936" y="{Y + 15}" width="40" height="20" rx="5" style="fill:{a1c};opacity:{.75 if trigger else .45}"/>'   # A1 pulley
    gh += rotg(MCP, p, g1, kt, dur)
    s = skin(1700, 1915, 70)
    if dup:
        s += f'<path d="M1740 {Y + 44} C1820 {Y + 46} 1900 {Y + 44} 1960 {Y + 40}" style="fill:none;stroke:{FASC};stroke-width:12;stroke-linecap:round;opacity:.85"/>'
    s += f'<path d="{capsule((1740, Y), (1912, Y), 17)}" {BONE}/>'
    s += tln(1700, Y - 22, 1915, Y - 22)                                         # extensor
    s += tln(1700, Y + 28, 1915, Y + 28)                                         # FDS
    if jersey:
        s += (tln(1700, Y + 22, 1842, Y + 22, 'var(--bad)', 6) +
              f'<path d="M1842 {Y + 22} C1856 {Y + 22} 1858 {Y + 34} 1846 {Y + 36}" style="fill:none;stroke:var(--bad);stroke-width:6;stroke-linecap:round"/>')
    else:
        s += tln(1700, Y + 22, 1915, Y + 22)                                     # FDP
    s += rotg(NECK, head, gh)
    if boxer: s += ZZr(1915, Y, 90, .9)
    if trigger:
        s += (f'<ellipse cx="1985" cy="{Y + 22}" rx="10" ry="8" style="fill:{TEND};stroke:var(--bad);stroke-width:2">'
              f'<animateTransform attributeName="transform" type="translate" values="0 0;-78 0;-78 0;0 0;0 0" keyTimes="{kt}" '
              f'dur="{dur}s" repeatCount="indefinite"/></ellipse>')
    if dup:
        s += f'<ellipse cx="1880" cy="{Y + 46}" rx="14" ry="10" style="fill:{FASC}"/>'
    return s
FIST = '0;.35;.65;1'
TRIG = '0;.3;.7;.76;1'
add(finger(p=[0, 50, 50, 0], m=[0, 60, 60, 0], d=[0, 40, 40, 0], kt=FIST), unless=O('mallet', 'jersey', 'trigger', 'dup', 'pipdis', 'boxer'))
add(finger(d=40, mallet=True), when=O('mallet'))
add(finger(p=[0, 50, 50, 0], m=[0, 60, 60, 0], d=0, kt=FIST, jersey=True), when=O('jersey'))
add(finger(p=[0, 45, 45, 0, 0], m=[0, 55, 55, 0, 0], d=[0, 35, 35, 0, 0], kt=TRIG, trigger=True), when=O('trigger'))
add(finger(p=35, m=32, dup=True), when=O('dup'))
add(finger(pip=True), when=O('pipdis'))
add(finger(head=30, p=-30, boxer=True), when=O('boxer'))
# finger labels: back of the finger above, palm side below (leaders go to parts that do not move)
text('MCP', 1960, 512, 'nf-l2', 'middle', unless=O('boxer'))
text('extensor tendon', 1780, 478, 'nf-l2', 'middle'); lead(1780, 484, 1790, 536)
text('central slip → middle phalanx base', 2125, 440, 'nf-l2', 'middle', unless=O('pipdis', 'mallet'))
text('terminal tendon → distal phalanx', 2330, 470, 'nf-l2', 'end', unless=O('mallet', 'pipdis'))
text('FDP → distal phalanx · FDS → middle', 1880, 660, 'nf-l2', 'end', unless=O('jersey', 'dup'))
lead(1886, 652, 1880, 590, unless=O('jersey', 'dup'))
text('A1 pulley', 1900, 704, 'nf-l2', 'end', unless=O('trigger', 'boxer')); lead(1904, 696, 1944, 596, unless=O('trigger', 'boxer'))
text('normal: make a fist — all three joints bend', 1700, 860, 'nf-l2', 'start', unless=ANY)
text('terminal tendon torn — the tip droops and cannot be lifted', 2330, 470, TAG1, 'end', when=O('mallet'))
text('passively it straightens fully', 2330, 680, 'nf-l2', 'end', when=O('mallet'))
text('FDP torn off and pulled back into the palm', 1880, 660, TAG1, 'end', when=O('jersey'))
text('fist: the PIP and MCP bend, the fingertip stays straight', 1700, 860, 'nf-l2', 'start', when=O('jersey'))
text('nodule catches at the A1 pulley', 1900, 704, TAG1, 'end', when=O('trigger'))
text('bends, locks, then snaps straight', 1700, 860, 'nf-l2', 'start', when=O('trigger'))
text('cord pulls the MCP and PIP into flexion', 1880, 660, TAG1, 'end', when=O('dup'))
text('can’t lay the hand flat on a table', 1700, 860, 'nf-l2', 'start', when=O('dup'))
text('volar plate torn · middle phalanx on the back of the proximal', 2125, 440, TAG1, 'middle', when=O('pipdis'))
text('axial load + hyperextension', 2330, 640, 'nf-l1', 'end', when=O('pipdis'))
text('neck broken — the head tips toward the palm (apex dorsal)', 1700, 860, TAG1, 'start', when=O('boxer'))
text('knuckle hits a wall', 1925, 430, 'nf-l1', 'middle', when=O('boxer'))
text('ball jams the tip', 2330, 430, 'nf-l1', 'end', when=O('mallet'))
text('jersey yanks the bent tip straight', 2330, 690, 'nf-l1', 'end', when=O('jersey'))

# ════════ what happened (under the elbow and the finger) ════════
CX0 = 1100
text('What happened', CX0, 920, 'dyn-big')
CAP = dict(
  lat=('Who & how: repetitive wrist extension against resistance — the backhand, manual labor, office work · ages 40–60',
       'Test: tender at the ECRB origin just distal to the lateral epicondyle · resisted wrist extension hurts, most with the elbow straight',
       'Imaging: X-ray usually normal (calcification in < 10%) · MRI adds little — a clinical diagnosis',
       'Treat: counterforce strap, NSAIDs, therapy, injection · surgery (release the extensor origin) only if recalcitrant'),
  med=('Who & how: repetitive wrist flexion and pronation · the valgus load of throwing',
       'Test: tender at the flexor–pronator origin · pain with palpation and wrist flexion · check the ulnar nerve behind it',
       'Imaging: X-ray usually normal (calcification in < 10%)',
       'Treat: as for tennis elbow, stretching the wrist flexors · in surgery the tendon is reattached — it steadies the medial elbow'),
  dq=('Who & how: overuse of the thumb and wrist · women 30–50, often 4–6 weeks after delivery (lifting the baby)',
      'Test: Finkelstein — thumb in the fist, the examiner ulnar-deviates the wrist → sharp pain over the radial styloid',
      'Imaging: X-rays don’t help · ultrasound shows the swollen sheath',
      'Treat: forearm thumb spica splint (thumb tip free), NSAIDs, then steroid injection · surgery is rare'),
  ganglion=('Who & how: synovial fluid herniates from a joint or tendon sheath · 70% dorsal wrist, 20% palmar wrist',
            'Test: firm, well-circumscribed, non-fluctuant lump that transilluminates — a solid tumor does not',
            'Imaging: ultrasound or MRI if unsure',
            'Treat: about a third resolve — watch, aspirate or excise (excision recurs less) · painful only if it presses on something'),
  scaph=('Who & how: a fall on an outstretched hand · the most often fractured carpal bone, usually at the waist',
         'Test: tender anatomic snuffbox',
         'Imaging: the first X-ray can be normal — splint the wrist and thumb, repeat it at 7–10 days (or MRI)',
         'Red flag: blood enters distally, so a proximal fragment can die — avascular necrosis, nonunion · displaced → surgery'),
  ct=('Who & how: a crowded tunnel — pregnancy, RA, hypothyroidism, diabetes, acromegaly, dialysis amyloid, overuse · women 3:1',
      'Test: Tinel over the median nerve at the wrist · Phalen — wrist flexed for a minute · tingling wakes the patient at night',
      'Imaging: a clinical diagnosis · nerve studies or ultrasound to support it, or before surgery',
      'Treat: night splint with the wrist neutral, NSAIDs, injection, release of the ligament · motor loss → urgent hand surgeon'),
  guyon=('Who & how: handlebar pressure in cyclists · hook of hamate fracture · a ganglion or ulnar artery aneurysm in the canal',
         'Test: Tinel at the wrist, not the elbow · numb little finger and half the ring, weak intrinsics, clawing',
         'Imaging: nerve studies localize it · MRI may show a ganglion · X-ray for a hook of hamate fracture',
         'Treat: splint · decompress the canal if that fails · the back of the hand keeps its feeling'),
  boxer=('Who & how: punching a hard object — young men · the neck is the weakest part of the metacarpal',
         'Test: pain, swelling, a flattened knuckle, reduced grip · make a fist — the fingers must not cross (rotation)',
         'Imaging: X-ray — the head tips toward the palm · ring and little fingers tolerate more angulation (mobile CMC joints)',
         'Red flag: a cut over the knuckle is a human bite until proven otherwise · ulnar gutter splint'),
  ucl=('Who & how: forced abduction and hyperextension of the thumb MCP — a fall on a ski pole (acute) or chronic laxity',
       'Test: radial stress in extension and 30° flexion vs the other thumb · > 30–40° or no firm end point = complete tear',
       'Imaging: X-ray for an avulsion chip · MRI shows a Stener lesion',
       'Red flag: Stener lesion — the adductor aponeurosis blocks healing → repair within a week · partial tears: thumb spica'),
  dup=('Who & how: older men of Northern European descent · alcohol, diabetes, antiepileptics, family history',
       'Test: painless nodules and cords at the base of the ring and little fingers · the table-top test fails',
       'Imaging: none needed — a clinical diagnosis',
       'Treat: when the MCP is fixed past 30° or the PIP at all — collagenase, needle release, fasciectomy · it often recurs'),
  trigger=('Who & how: women in their 40s–50s · diabetes, rheumatoid arthritis, crystal disease · often several fingers',
           'Test: catching or snapping, pain at the A1 pulley in the palm · it can lock bent · worst in the morning',
           'Imaging: none needed — a clinical diagnosis',
           'Treat: NSAIDs, splint or buddy tape, steroid injection into the sheath · release the A1 pulley if it fails'),
  mallet=('Who & how: a ball jams an extended fingertip — the DIP is forced into flexion · the commonest finger tendon injury',
          'Test: the tip droops and cannot be actively straightened · passive motion is full',
          'Imaging: X-ray for a dorsal bone chip',
          'Treat: DIP splint in full extension, continuously, ≥ 6 weeks, PIP free · a chip > 1/3 of the joint → orthopedics'),
  jersey=('Who & how: grabbing a jersey — forced extension of an actively flexed DIP · the ring finger in about 75%',
          'Test: hold the PIP straight and ask for DIP flexion — none · volar DIP pain and swelling',
          'Imaging: X-ray for an avulsed fragment · MRI if unclear',
          'Red flag: refer every case — delay and retraction worsen the outcome · splint PIP and DIP in mild flexion'),
  pipdis=('Who & how: an axial load with hyperextension — the commonest finger dislocation is dorsal at the PIP',
          'Test: after reduction (digital block), check active motion and stability',
          'Imaging: X-ray before and after reduction for a fracture-dislocation',
          'Treat: dorsal splint with the PIP at 30° flexion for 3 weeks · irreducible or unstable → surgery · neglect → swan neck'),
)
for k, rows in CAP.items():
    for i, s in enumerate(rows):
        text(s, CX0, 948 + 24 * i, 'nf-l1' if i == 0 else 'nf-l2', when=O(k))
text('Pick a problem: the structure that is strained, torn or squeezed turns red and the force that did it arrives', CX0, 948, 'nf-l1', unless=ANY)
text('Elbow: tendon origins at the epicondyles · wrist: tunnels, a sheath and the scaphoid · fingers: tendons, pulleys, ligaments', CX0, 972, 'nf-l2', unless=ANY)
text('The finger view moves: a normal fist bends the MCP, PIP and DIP together', CX0, 996, 'nf-l2', unless=ANY)
text('Nerve deficits themselves (claw, benediction, sensory maps) are on the Brachial Plexus Lesion Simulator', CX0, 1020, 'nf-l2', unless=ANY)
# colour key for the drawn structures
KEY = [('bone', 'var(--dk10)', 'b'), ('tendon', TEND, 'l'), ('ligament · pulley · retinaculum', LIGC, 'l'),
       ('median nerve', MED_N, 'l'), ('ulnar nerve', ULN_N, 'l'), ('palmar fascia', FASC, 'l'), ('artery', 'var(--nf-blood)', 'l')]
kx = CX0
for lab_, col, kind in KEY:
    if kind == 'b':
        add(f'<rect x="{kx}" y="1082" width="26" height="14" rx="6" class="dyn-cell" style="stroke:{col}"/>')
    else:
        add(f'<path d="M{kx} 1089 L{kx + 26} 1089" style="stroke:{col};stroke-width:7;stroke-linecap:round"/>')
    text(lab_, kx + 34, 1094, 'nf-l2')
    kx += 34 + round(len(lab_) * 6.4) + 30

# ════════ particles ════════
kinds = dict(force=['force', '--dk2'], test=['test', '--dk4'], ting=['ting', '--dk7'], blood=['blood', '--nf-blood'])
groups = [['force', 'Injuring force'], ['test', 'Examiner’s test'], ['ting', 'Tingling'], ['blood', 'Blood supply']]
def EP(d): return ep(d)
flows = [
  dict(d=EP('M600 820 C606 700 600 580 566 490'), len=345, speed=90, r=7, base=dict(force=3), when=O('lat')),   # wrist extensors pull on the origin
  dict(d=EP('M262 820 C250 700 256 580 286 490'), len=345, speed=90, r=7, base=dict(force=3), when=O('med')),
  dict(d=hp('M1362 1100 C1366 1000 1368 950 1366 905'), len=196, speed=70, r=6, base=dict(test=3), when=O('dq')),   # Finkelstein stretches the tendons
  dict(d=hp('M1340 860 L1268 860'), len=72, speed=45, r=7, base=dict(test=2), when=O('scaph')),                 # pressing the snuffbox
  dict(d=hp('M1296 836 C1270 850 1245 862 1205 888'), len=105, speed=45, r=5, base=dict(blood=3), unless=O('scaph')),   # retrograde supply
  dict(d=hp('M1296 836 C1280 845 1262 852 1244 860'), len=60, speed=35, r=5, base=dict(blood=2), when=O('scaph')),      # stops at the waist
  dict(d=hp('M1260 784 L1205 806'), len=59, speed=40, r=6, base=dict(test=2), when=O('ct')),                    # Tinel tap
] + [dict(d=hp(b), len=300, speed=70, r=5, base=dict(ting=2), when=O('ct')) for b in MED_BR] + [
  dict(d=hp(b), len=280, speed=70, r=5, base=dict(ting=2), when=O('guyon')) for b in ULN_BR] + [
  dict(d=hp('M980 960 L1030 905'), len=74, speed=45, r=7, base=dict(force=2), when=O('guyon')),                 # handlebar
  dict(d=hp('M1470 600 L1500 640'), len=50, speed=30, r=7, base=dict(test=2), when=O('ucl')),                   # radial stress on the thumb
  dict(d=hp('M1150 930 L1192 892'), len=57, speed=30, r=6, base=dict(test=2), when=O('ganglion')),             # light shone through
  dict(d='M2010 445 L1965 518', len=86, speed=60, r=8, base=dict(force=3), when=O('boxer')),                     # knuckle strike
  dict(d='M2330 445 L2300 535', len=95, speed=70, r=8, base=dict(force=3), when=O('mallet')),                    # ball onto the tip
  dict(d='M2250 700 L2320 640', len=92, speed=70, r=8, base=dict(force=3), when=O('jersey')),                    # yank into extension
  dict(d='M2340 470 L2300 500', len=50, speed=30, r=8, base=dict(force=2), when=O('pipdis')),                    # axial load
]

# ════════ tap targets ════════
st = lambda x, y, c, aria: dict(x=round(x), y=round(y), n=[0, -1], w=10, t='rec', l='', aria=aria, c=c, ions=[])
sites = [
  st(*E(566, 480), 'overuse', 'Lateral epicondyle — common extensor origin'),
  st(*E(284, 480), 'overuse', 'Medial epicondyle — common flexor–pronator origin'),
  st(*H(1362, 960), 'overuse', 'First dorsal compartment'),
  st(*H(1238, 862), 'wristinj', 'Scaphoid'),
  st(*H(1030, 620), 'wristinj', '5th metacarpal neck'),
  st(*H(1170, 822), 'carpaltunnel', 'Transverse carpal ligament'),
  st(*H(1060, 850), 'ulnarnerve', 'Guyon canal'),
  st(*H(1182, 1080), 'mediannerve', 'Median nerve'),
  st(*H(1360, 645), 'thumbucl', 'Thumb ulnar collateral ligament'),
  st(*H(1097, 553), 'triggerfinger', 'A1 pulley'),
  st(*H(1104, 690), 'fibromatosis', 'Palmar fascia'),
  st(*H(1192, 930), 'ganglion', 'Dorsal wrist ganglion site'),
  st(1840, Y - 22, 'fingertendon', 'Extensor tendon'),
  st(1800, Y + 22, 'fingertendon', 'Flexor digitorum profundus'),
  dict(st(1956, Y + 25, 'triggerfinger', 'A1 pulley (side view)'), unless=O('boxer')),
]

notes = {
  '': 'The elbow, the wrist and hand (palm up) and a finger from the side. Tendons pull bones across joints, pulleys and '
      'sheaths hold them close, ligaments hold joints together, and two nerves cross the wrist in tunnels. Pick a problem: '
      'its structure turns red, the force that did it arrives, and its test turns positive. The nerve deficits themselves '
      'are on the Brachial Plexus Lesion Simulator.',
  'hd:lat': 'Lateral epicondylitis (tennis elbow): repetitive wrist extension against resistance — the backhand — overloads the '
            'common extensor origin, mostly the extensor carpi radialis brevis. Tender just distal to the lateral epicondyle; '
            'resisted wrist extension hurts, most with the elbow straight; motion and X-ray are normal. It is degeneration '
            'more than inflammation. Strap, NSAIDs, therapy, injection.',
  'hd:med': 'Medial epicondylitis (golfer’s elbow): repetitive wrist flexion and pronation, or the valgus load of throwing, '
            'strains the common flexor–pronator origin (pronator teres, flexor carpi ulnaris). Medial elbow pain, worse with '
            'pressure on the epicondyle and with wrist flexion. The ulnar nerve runs just behind it and can be compressed too. '
            'Treated like tennis elbow.',
  'hd:dq': 'De Quervain tenosynovitis: the abductor pollicis longus and extensor pollicis brevis rub under a thickened '
           'retinaculum in the first dorsal compartment at the radial styloid — overuse, classically 4–6 weeks after '
           'delivery. Finkelstein: thumb tucked in the fist, the wrist ulnar-deviated → sharp pain over the styloid. '
           'Thumb spica splint, NSAIDs, then steroid injection.',
  'hd:ganglion': 'Ganglion cyst: synovial fluid herniates out of a joint capsule or tendon sheath into its own sac — 70% on the '
                 'dorsal wrist from the scapholunate joint. A firm, well-circumscribed, non-fluctuant lump that '
                 'transilluminates (a solid tumor does not); painful only if it presses on something. About a third resolve: '
                 'watch, aspirate or excise.',
  'hd:scaph': 'Scaphoid fracture: a fall on an outstretched hand breaks the most often fractured carpal bone, usually at the '
              'waist. Tender anatomic snuffbox — and the first X-ray can be normal, so splint wrist and thumb and repeat it '
              'at 7–10 days. Blood enters the distal pole and flows backward, so the proximal fragment can die: avascular '
              'necrosis and nonunion.',
  'hd:ct': 'Carpal tunnel syndrome: anything that crowds the tunnel under the transverse carpal ligament squeezes the median '
           'nerve — pregnancy, RA, hypothyroidism, diabetes, acromegaly, overuse. Tingling in the thumb, index, middle and '
           'half the ring finger wakes the patient at night; the palm is spared (its branch runs above the ligament). Tinel '
           'and Phalen. Neutral night splint, injection, release.',
  'hd:guyon': 'Guyon canal syndrome: the ulnar nerve is squeezed between the pisiform and the hook of the hamate — handlebar '
              'pressure in cyclists, a hook of hamate fracture, a ganglion. Numb little finger and half the ring, weak '
              'intrinsics, clawing; Tinel is positive at the wrist, not the elbow, and the back of the hand keeps its '
              'feeling (that branch leaves above the wrist).',
  'hd:boxer': 'Boxer’s fracture: punching a hard object breaks the neck of the 5th metacarpal; the head tips toward the palm '
              'and the knuckle flattens; grip is weak. The ring and little fingers tolerate more angulation because their CMC '
              'joints move, but rotation is never accepted. Ulnar gutter splint; a cut over the knuckle is a human bite until '
              'proven otherwise.',
  'hd:ucl': 'Gamekeeper’s (skier’s) thumb: forced abduction and hyperextension of the thumb MCP tears the ulnar collateral '
            'ligament, usually from the proximal phalanx. Radial stress in extension and 30° flexion: more than 30–40° or no '
            'firm end point = complete tear. In a Stener lesion the adductor aponeurosis lies between the torn ends and it '
            'cannot heal: MRI, repair within a week.',
  'hd:dup': 'Dupuytren contracture: myofibroblasts thicken the palmar fascia into painless nodules and cords that pull the '
            'ring and little fingers into flexion at the MCP and PIP — older men of Northern European descent; alcohol and '
            'diabetes add risk. The hand can’t lie flat on a table. Treat a fixed MCP past 30° or any PIP contracture; it '
            'often recurs.',
  'hd:trigger': 'Trigger finger (stenosing flexor tenosynovitis): the flexor tendon, often with a nodule, catches at the A1 '
                'pulley over the MCP joint. Catching or snapping, then pain at the pulley; the finger can lock bent and snap '
                'straight, worst in the morning. Women in their 40s–50s, diabetes, RA. NSAIDs, splint, steroid injection; '
                'release the A1 pulley if it fails.',
  'hd:mallet': 'Mallet finger: a ball jams an extended fingertip and forces the DIP into flexion, tearing the extensor tendon '
               'from the distal phalanx (± a bone chip). The tip droops and cannot be actively straightened, though it moves '
               'fully when pushed. Splint the DIP in full extension, continuously, for at least 6 weeks, PIP free. Untreated, '
               'it can become a swan neck.',
  'hd:jersey': 'Jersey finger: grabbing an opponent’s jersey forces a flexed DIP straight and tears the flexor digitorum '
               'profundus off the distal phalanx — the ring finger in about 75%. In a fist that fingertip stays straight; '
               'test it alone by holding the PIP straight and asking for DIP flexion. Splint in mild flexion and refer every '
               'case — delay and retraction worsen the outcome.',
  'hd:pipdis': 'Dorsal PIP dislocation, the commonest finger dislocation: an axial load with hyperextension ruptures the volar '
               'plate and the middle phalanx comes to rest on the back of the proximal phalanx. Reduce under a digital block, '
               'test active motion, then splint the PIP in about 30° of flexion for 3 weeks. Irreducible joints need surgery.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Epicondyle tenderness', mods=[R(O('lat', 'med'), 1)]),
  dict(l='Finkelstein', mods=[R(O('dq'), 1)]),
  dict(l='Snuffbox tenderness', mods=[R(O('scaph'), 1)]),
  dict(l='Tinel at the wrist', mods=[R(O('ct', 'guyon'), 1)]),
  dict(l='Thumb MCP laxity (radial stress)', mods=[R(O('ucl'), 1)]),
  dict(l='Finger held in flexion', mods=[R(O('trigger', 'dup', 'mallet'), 1)]),
  dict(l='Active DIP motion', mods=[R(O('mallet', 'jersey'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='hd', label='Problem', type='one', options=[
                ['lat', 'Tennis elbow (lateral)', 'overuse'], ['med', 'Golfer’s elbow (medial)', 'overuse'],
                ['dq', 'De Quervain', 'overuse'], ['ganglion', 'Ganglion cyst', 'ganglion'], ['scaph', 'Scaphoid fracture', 'wristinj'],
                ['ct', 'Carpal tunnel', 'carpaltunnel'], ['guyon', 'Guyon canal', 'ulnarnerve'],
                ['boxer', 'Boxer’s fracture', 'wristinj'], ['ucl', 'Gamekeeper’s thumb', 'thumbucl'], ['dup', 'Dupuytren', 'fibromatosis'],
                ['trigger', 'Trigger finger', 'triggerfinger'], ['mallet', 'Mallet finger', 'fingertendon'],
                ['jersey', 'Jersey finger', 'fingertendon'], ['pipdis', 'PIP dislocation', 'dislocs']],
                 sections=[['Elbow', ['lat', 'med']],
                           ['Wrist', ['dq', 'ganglion', 'scaph', 'ct', 'guyon']],
                           ['Hand & thumb', ['boxer', 'ucl', 'dup']],
                           ['Fingers', ['trigger', 'mallet', 'jersey', 'pipdis']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM Ortho SDL 14–15, 25, 9 (Tintinalli, CDT Orthopedics, Atlas of EM) · First Aid pp. 453, 462–465 · Moore ch 3 · Bootcamp')

MAP = dict(
  id='handsim', title='Hand, Wrist & Elbow Simulator', topic='msk', after='shoulder',
  sub='The elbow, the wrist and hand palm up, and a finger from the side whose joints move — pick an elbow tendinopathy, de '
      'Quervain, a ganglion, a scaphoid or boxer’s fracture, carpal tunnel or Guyon canal, gamekeeper’s thumb, Dupuytren, or a '
      'trigger, mallet or jersey finger or a PIP dislocation: the structure turns red, the force arrives, the test turns '
      'positive. Tap a structure for its card',
  w=3500, h=1640,
  fa='453, 462, 463, 465', src=[SDL1415, SDL25, SDL9R, MOORE3, BC_ELB, BC_HAND],
  lanes=[('hsElb', 'Elbow', 'tca'), ('hsWr', 'Wrist', 'ppp'), ('hsHand', 'Hand & fingers', 'glycogen'),
         ('hsNv', 'Nerves at the wrist', 'glycolysis')],
  comps=[],
  nodes=[
    ('hs1', 'Elbow & wrist overuse', 250, 1250, 'hsElb', 'epicondyles · de Quervain', ['overuse'], 'hub'),
    ('hs2', 'Elbow fractures', 500, 1250, 'hsElb', 'see Arm Injuries', ['elbowinj', 'nursemaid']),
    ('hs3', 'Scaphoid & boxer’s', 740, 1250, 'hsWr', 'snuffbox · 5th neck', ['wristinj']),
    ('hs4', 'Ganglion cyst', 960, 1250, 'hsWr', 'transilluminates', ['ganglion']),
    ('hs5', 'Carpal tunnel', 1180, 1250, 'hsNv', 'Tinel · Phalen', ['carpaltunnel', 'mediannerve']),
    ('hs6', 'Guyon canal', 1400, 1250, 'hsNv', 'hook of hamate', ['ulnarnerve']),
    ('hs7', 'Gamekeeper’s thumb', 1620, 1250, 'hsHand', 'Stener lesion', ['thumbucl']),
    ('hs8', 'Dupuytren', 1830, 1250, 'hsHand', 'palmar fascia', ['fibromatosis']),
    ('hs9', 'Trigger finger', 2030, 1250, 'hsHand', 'A1 pulley', ['triggerfinger']),
    ('hs10', 'Mallet & jersey', 2230, 1250, 'hsHand', 'extensor · FDP', ['fingertendon']),
    ('hs11', 'Finger dislocations', 2440, 1330, 'hsHand', 'volar plate', ['dislocs']),
  ],
  panels=[
    (140, 1330, 1040, 'Which test, which structure (OCOM SDL 14–15; First Aid pp. 463, 465)', [
      ('Finkelstein', 'thumb in the fist, ulnar-deviate the wrist → radial styloid pain → de Quervain'),
      ('Snuffbox pressure', 'tender over the scaphoid → treat as a fracture even if the X-ray is normal'),
      ('Tinel · Phalen', 'tap the median nerve · flex the wrist for a minute → carpal tunnel'),
      ('Tinel at the wrist', 'ulnar side, with a normal elbow → Guyon canal'),
      ('Thumb radial stress', 'MCP opens > 30–40° or has no end point → complete UCL tear'),
      ('Isolated DIP flexion', 'hold the PIP straight, flex the tip → none in jersey finger'),
      ('Transillumination', 'light shines through a ganglion, not through a solid tumor')]),
    (1220, 1330, 1100, 'How it is splinted (Tintinalli ch 268, 283; Atlas of Emergency Medicine; CDT ch 11)', [
      ('Mallet finger', 'DIP in full extension, continuously ≥ 6 weeks — PIP left free'),
      ('Jersey finger', 'PIP and DIP in mild flexion — and refer'),
      ('Thumb UCL, partial', 'thumb spica, thumb tip free to bend'),
      ('De Quervain', 'forearm thumb spica — the thumb tip moves'),
      ('Carpal tunnel', 'volar wrist splint in neutral, at night'),
      ('Suspected scaphoid', 'wrist and thumb, then X-ray again at 7–10 days (POO ch 8)'),
      ('Boxer’s (ring, little)', 'ulnar gutter splint'),
      ('Dorsal PIP dislocation', 'after reduction, PIP at 30° flexion for 3 weeks')]),
  ],
  dyn=dyn,
)
