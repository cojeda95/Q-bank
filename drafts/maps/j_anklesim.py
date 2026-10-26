# m56 — Ankle & Leg Injuries (dynamic map, kit data) — coverage sweep 2 (batches/m56/coverage2.md) candidate #5.
# Four drawn views of the LEFT leg, in j_kneesim.py's style: (A) the whole leg from the front — tibia, fibula from its head to the
# lateral malleolus, the interosseous membrane, the syndesmosis (AITFL), the deltoid ligament and the talus in the mortise — where
# the Weber levels, Maisonneuve, the bi-/trimalleolar fracture, the stress fracture, shin splints and the open shaft fracture are
# drawn, and the talus SLIDES laterally when the mortise is unstable; (B) the ankle and calf from the lateral side (mirrored so the
# toes point left): ATFL, CFL, PTFL, AITFL, calf muscles and the Achilles tendon — the anterior drawer SLIDES the foot forward,
# the Achilles ruptures, the calf strains; (C) the mid-leg in cross-section (seen from below, as on CT): the four compartments,
# the deep fibular nerve and anterior tibial artery, tibialis posterior, the gastrocnemius heads; (D) the heel from behind:
# straight heel vs PTTD (heel tilts laterally, "too many toes") vs a newborn clubfoot. One `one` switch in five sections picks
# the injury; 7 readouts (Predict): anterior drawer/talar tilt, squeeze/external rotation test, syndesmosis injured, Thompson,
# pain on passive stretch, single-leg heel raise fails, localized bony tenderness.
#
# Sources (all read in the corpus; U+00A0/U+00AD normalized):
#   OCOM Ortho SDL 7 lecture (Martin, Foot/ankle pain and injury): MTSS — repetitive activity → overuse of posterior compartment
#     muscles (tibialis posterior, soleus, FDL) → traction periostitis → remodeling → fracture without rest; 13.6–20% of runners,
#     35% of military recruits; DIFFUSE pain along the distal posteromedial tibia, junction of proximal 2/3 and distal 1/3, eases
#     with warm-up, recurs after exercise; tenderness NOT localized, neurovascular exam normal; X-ray/bone scan/MRI often negative;
#     over-pronation the one "yes" risk factor, females 3×; rest, ice, anti-inflammatories, foot alignment/shoes/gait · ankle
#     sprain — lateral (ATFL, CFL, PTFL) 70–90%, isolated ATFL 73%; medial deltoid (eversion + dorsiflexion, multiligament, medial
#     malleolar avulsion); syndesmotic (anterior tibiofibular ligament; dorsiflexion + external rotation); lateral: anterior
#     drawer, talar tilt; medial/syndesmotic: external rotation test, squeeze test; Ottawa — posterior lateral or medial malleolar
#     tenderness or inability to bear weight for 4 steps; foot films for navicular or 5th MT pain; grades 1–3 (as in the notes);
#     lateral PRICE, grade 1 early rehab, grade 2 brief NWB + immobilization, grade 3 short immobilization; medial/syndesmotic
#     PRICE, immobilize, NWB, ortho consult · gastrocnemius strain — acceleration from standstill with the ankle dorsiflexed
#     (lunge), medial belly or musculotendinous junction, dorsiflexion reproduces pain, grade III palpable defect + Thompson
#     positive; ice, heel lift, crutches, strengthening within 24 h · PTTD — grades 1–3 (single heel raise lost in grade 2, pes
#     planus + forefoot abduction; grade 3 fixed subtalar joint → ortho), risk rises after 40 · Achilles tendinopathy — acute or
#     chronic, insertional or midportion, after an increase in activity; 24% of competitive athletes, 6–17% of recreational
#     runners' injuries; risk factors; activity modification, gastrosoleus mobilization, PT.
#   OCOM SDL 7 reading (Practical Office Orthopedics ch 5): ATFL torn in ~70%; ATFL sprain tender over the anterior half of the
#     lateral malleolus only, a fracture all along it; Ottawa rules only for malleolar pain, X-ray over 55 and with sensory loss;
#     a nondisplaced lateral malleolar fracture treated as a sprain can displace; displaced → ORIF; torn ankle ligaments heal even
#     at grade III; stirrup brace rather than a cast · Achilles rupture: violent "pop", tender, palpable defect, Thompson test
#     (squeeze the calf → no plantarflexion; toe flexors can still plantarflex), repair compromised after a week or two; "tennis →
#     Achilles tendon rupture" · Achilles tendonitis like plantar fasciitis (first steps), calf stretches, night splints, NSAIDs,
#     casting, NO cortisone injection (predisposes to rupture) · PTTD: tendon behind the medial malleolus into the arch, thickens,
#     can't glide, arch collapses, heel tilts laterally, foot externally rotated → "too many toes" from behind; ≥ 50 with
#     atraumatic medial arch pain → most likely; single-leg heel rise nearly impossible; flexible → arch support / UCBL brace,
#     rigid → surgery.
#   OCOM SDL 9 lecture (Martin, Lower extremity fracture): Maisonneuve — proximal fibula after a rotational force at the ankle,
#     deltoid injury or medial malleolar fracture, force through the interosseous membrane; ortho consult for Maisonneuve, displaced,
#     comminuted fibular fractures; ankle fractures 187/100,000/yr, 60–70% unimalleolar, 15–20% bimalleolar, 7–12% trimalleolar;
#     Ottawa rules; tibial shaft 2% of adult fractures, bimodal 20 and 50, sports and MVAs, usually high energy; displaced or soft
#     tissue injury → watch for compartment syndrome.
#   OCOM SDL 25 reading (Current Diagnosis & Treatment in Orthopedics ch 2): mortise = uniplanar hinge, malleoli as buttresses;
#     Danis-Weber A (fibula avulsed distal to the joint line, syndesmosis intact, medial malleolus intact or sheared) · B (spiral
#     from the joint line running proximal-posterior; parts of the syndesmosis can tear but the interosseous ligament usually holds,
#     no widening, complete disruption possible; medial malleolus intact ± deltoid tear or transverse avulsion; posterior malleolus
#     can avulse) · C (fibula above the syndesmosis, syndesmosis disrupted, medial malleolar avulsion or deltoid rupture ±
#     posterior malleolus); bi-/trimalleolar definitions, Maisonneuve counted as bimalleolar; reduce dislocations at once; a 1 mm
#     lateral talar shift cuts tibiotalar contact by 40%; lateral malleolus fixed first; syndesmotic injuries from external
#     rotation and hyperdorsiflexion, tibiofibular clear space > 6 mm the most reliable sign · tibia: a 1-cm wound can hide Gustilo
#     grade III damage; closed fractures can carry compartment syndrome; reamed, statically locked IM nail standard for displaced
#     closed and open Gustilo I–IIIA; open fracture → IV antibiotics, urgent irrigation and debridement · fibula: Maisonneuve →
#     examine the ankle.
#   OCOM SDL 9 p3 reading (Current Diagnosis & Treatment in Orthopedics ch 12): clubfoot — equinus, varus (inversion + internal
#     rotation of the subtalar joint), adductus, ± cavus, calf atrophy always; 1 in 1000; rigid, unlike metatarsus adductus;
#     Ponseti — weekly casts 3–5 weeks, percutaneous Achilles tenotomy, brace up to 3 years at night and naps; > 90% corrected,
#     relapse common when bracing lapses.
#   First Aid 2025 p. 458 (ATFL most common sprain, low sprain, overinversion/supination; AITFL most common high sprain) · p. 465
#     (compartment syndrome: venous outflow obstruction → arteriolar collapse → necrosis; tibial fracture; severe pain, tense
#     compartment, pain on passive stretch; CK and motor deficits late; MTSS in runners and recruits, resorption outpacing
#     formation) · p. 191 (fluoroquinolones: tendonitis or tendon rupture > 60 and with prednisone).
#   Moore ch 7 (Pott fracture-dislocation: eversion avulses the medial malleolus, the talus moves laterally, lateral malleolus or
#     fibula above the syndesmosis breaks, posterior lip if the tibia is carried forward; tibial shaft narrowest at the junction of
#     the middle and inferior thirds, the commonest fracture site; anterior surface subcutaneous → commonest compound fracture;
#     march (stress) fractures of the inferior third; anterior compartment bounded by both bones, the interosseous membrane and
#     dense fascia → most susceptible to compartment syndrome, deep fibular nerve + anterior tibial artery; fasciotomy; Achilles
#     rupture — push-off, gap 1–5 cm above the calcaneus, cannot raise the heel).
#   Bootcamp.com MSK — Foot & ankle (stress fractures: sharp localized pain after more activity, worse with activity; X-ray, repeat
#     in 2–3 weeks, MRI; low risk medial tibia, high risk anterior tibia; clubfoot ↑ in males).
# CUT for lack of a course/textbook source: Weber A/B/C treatment by type (only the anklestab card's journal citations), "within
#   the hour" for open-fracture antibiotics (journal only — the notes say IV antibiotics + urgent I&D), how the squeeze and
#   external-rotation tests are done (named only), anterior compartment symptoms beyond pain + passive stretch (no source ties
#   first-web-space numbness to it), eccentric calf loading (named only in a reference title), any readout arrow not stated:
#   grade II drawer (only "mild instability"), Weber B and bi-/trimalleolar syndesmosis, gastrocnemius passive stretch, tendinopathy
#   Thompson. Ottawa as a readout was dropped — whether each option meets the rules is not stated; the rules are a panel instead.
# CONFLICTS for the owner: Moore calls shin splints a tibialis anterior / mild anterior compartment syndrome, and Bootcamp calls a
#   medial tibial stress fracture "shin splints"; the course lecture (wins) makes MTSS a posterior-compartment traction periostitis
#   on the posteromedial tibia with diffuse, not localized, tenderness — the map follows the course. Clubfoot incidence: course
#   text 1 in 1000 vs the clubfoot card's 2 per 1000 (Moore) — the note uses the course figure.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

MOORE7 = full('Moore', 7)
SDL7 = 'OCOM Ortho — SDL 7 lecture: Foot and ankle pain and injury'
SDL7R = 'OCOM Ortho — SDL 7 reading: Practical Office Orthopedics ch 5, The foot and ankle'
SDL9 = 'OCOM Ortho — SDL 9 lecture: Lower extremity fracture'
SDL9P = 'OCOM Ortho — SDL 9 reading: Pediatric orthopedic surgery (Current Diagnosis & Treatment in Orthopedics 6e ch 12)'
SDL25 = 'OCOM Ortho — SDL 25 readings: Joint dislocations (Current Diagnosis & Treatment in Orthopedics ch 2, 11)'
BC_FOOT = 'Bootcamp.com MSK — Foot & ankle'

O = lambda *k: ['an:' + x for x in k]
ANY = ['an:*']

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
def lead(x0, y0, x1, y1, when=None, unless=None):
    add(f'<path d="M{x0} {y0} L{x1} {y1}" class="dyn-line" style="stroke-width:1.5;opacity:.7"/>', when, unless)
TAG = 'nf-l2 dyn-tag'
TAG1 = 'nf-l1 dyn-tag'

BONE = 'class="dyn-cell" style="stroke:var(--dk10)"'
SKIN = 'style="fill:none;stroke:var(--ink-3);stroke-width:2.5;opacity:.6"'
MUS = 'style="fill:var(--dk7);fill-opacity:.16;stroke:var(--dk7);stroke-width:2;stroke-opacity:.5"'
LIGC, TORN, TEND = 'var(--dk5)', 'var(--bad)', 'var(--dk8)'
DUR = 'dur="3s" repeatCount="indefinite" keyTimes="0;.3;.55;.85;1"'
def slide(dx, dy=0):
    return f'<animateTransform attributeName="transform" type="translate" values="0 0;{dx} {dy};{dx} {dy};0 0;0 0" {DUR}/>'
def crack(x0, y0, x1, y1, w=5):
    """a fracture line: a zigzag from (x0, y0) to (x1, y1)"""
    pts = []
    for i in range(7):
        t = i / 6; x = x0 + (x1 - x0) * t; y = y0 + (y1 - y0) * t
        nx, ny = -(y1 - y0), (x1 - x0); n = (nx * nx + ny * ny) ** .5 or 1
        o = 0 if i in (0, 6) else (5 if i % 2 else -5)
        pts.append(f'{round(x + nx / n * o)} {round(y + ny / n * o)}')
    return f'<path d="M{" L".join(pts)}" style="fill:none;stroke:var(--bad);stroke-width:{w};stroke-linejoin:round"/>'
def lig(a, b, w, state='ok', moving=None):
    """a straight ligament a → b: ok · stretch (grade I) · partial (grade II) · torn (grade III, two stumps); moving = the
    animation that carries the b end (a slide) — the b stump of a torn ligament rides inside it"""
    seg = lambda p, q: f'M{round(p[0])} {round(p[1])} L{round(q[0])} {round(q[1])}'
    at = lambda t: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
    if state == 'torn':
        s1 = f'<path d="{seg(a, at(.4))}" style="stroke:{TORN};stroke-width:{w};stroke-linecap:round"/>'
        s2 = f'<path d="{seg(at(.62), b)}" style="stroke:{TORN};stroke-width:{w};stroke-linecap:round"/>'
        return s1 + (f'<g>{moving}{s2}</g>' if moving else s2)
    base = f'<path d="{seg(a, b)}" style="stroke:{LIGC};stroke-width:{w};stroke-linecap:round;opacity:.9"/>'
    if state == 'stretch':
        base += f'<path d="{seg(a, b)}" style="stroke:var(--bad);stroke-width:{max(2, w // 3)};stroke-dasharray:3 6;stroke-linecap:round"/>'
    if state == 'partial':
        base += f'<path d="{seg(at(.35), at(.65))}" style="stroke:{TORN};stroke-width:{w};stroke-linecap:round;opacity:.85"/>'
    return base

# ════════ title ════════
text('The ankle and the leg — what tears or breaks, how, and which test turns positive', 160, 140, 'dyn-big')
text('left leg in four views · pick an injury on the right', 160, 162, 'dyn-cap')

# ════════ VIEW A — the leg from the front (local coordinates, drawn 60 px lower) ════════
AY = 60
def gA(svg): return f'<g transform="translate(0 {AY})">{svg}</g>'
text('Front view', 160, 220, 'dyn-big')
text('left leg · medial on the left', 160, 240, 'dyn-cap')
FEM_A = 'M402 245 C400 210 436 194 480 196 L600 196 C646 194 668 212 666 245 Z'
TIB_A = ('M398 300 C396 268 430 252 470 250 L622 250 C656 252 670 270 668 300 C666 330 646 352 620 368 C600 382 588 410 585 440 '
         'L585 1000 C588 1040 606 1070 612 1100 L612 1135 L484 1135 L482 1182 C478 1196 456 1198 448 1186 C438 1160 438 1100 452 1060 '
         'C470 1030 488 1010 490 990 L490 440 C488 410 470 380 446 366 C416 348 400 330 398 300 Z')
FIB_A = ('M668 362 C672 340 714 338 720 362 C724 384 708 402 700 420 L698 1060 C712 1100 718 1170 702 1212 C692 1228 668 1222 662 1200 '
         'L652 1135 C650 1100 668 1070 672 1050 L676 420 C668 402 664 382 668 362 Z')
TAL_A = 'M488 1142 C520 1132 612 1132 646 1142 L652 1205 C640 1238 600 1250 566 1250 C530 1250 496 1238 488 1212 Z'
SKIN_A = ('M380 300 C372 420 360 560 384 760 C400 900 420 1040 430 1150 C432 1220 420 1290 404 1330 L762 1330 C744 1280 732 1210 '
          '734 1150 C740 1040 770 900 784 760 C800 600 780 420 764 300')
FOOT_A = 'M404 1290 C470 1270 690 1270 762 1290 C780 1320 770 1350 740 1360 L430 1360 C400 1350 392 1318 404 1290 Z'
IOM_A = 'M588 450 L676 440 L674 1040 L596 1016 Z'
COMP_A = 'M587 445 L676 432 L700 1000 L600 990 Z'
AITFL_A = ((604, 1080), (668, 1100))
DELT_A = (((458, 1160), (494, 1230)), ((474, 1146), (526, 1236)))
SHIFT_A = O('wc', 'mais', 'bitri')

def view_A(shift=False, aitfl='ok', delt='ok'):
    mv = slide(16) if shift else ''
    s = f'<path d="{SKIN_A}" {SKIN}/><path d="{FOOT_A}" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:2;opacity:.7"/>'
    s += f'<path d="{FEM_A}" class="dyn-cell" style="stroke:var(--dk10);stroke-dasharray:6 5;opacity:.6"/>'
    s += f'<path d="{IOM_A}" style="fill:var(--dk8);fill-opacity:.14;stroke:var(--dk8);stroke-width:1.5;stroke-opacity:.5"/>'
    s += ''.join(f'<path d="M{590} {y} L{674} {y - 36}" style="stroke:var(--dk8);stroke-width:1.5;opacity:.35"/>' for y in range(500, 1020, 60))
    s += f'<g>{mv}<path d="{TAL_A}" {BONE}/></g>'          # the talus slides out from under the tibia in an unstable mortise
    s += f'<path d="{TIB_A}" {BONE}/><path d="{FIB_A}" {BONE}/>'
    s += lig(*AITFL_A, 16, aitfl)
    for a, b in DELT_A: s += lig(a, b, 12, delt, mv if delt == 'torn' else None)
    return gA(s)
add(view_A(), unless=O('high', 'wc', 'mais', 'bitri'))
add(view_A(aitfl='torn'), when=O('high'))
add(view_A(True, 'torn', 'torn'), when=O('wc', 'mais'))
add(view_A(True), when=O('bitri'))
# the joint line (the tibial plafond)
add(gA('<path d="M420 1135 H740" style="stroke:var(--ink-3);stroke-width:1.5;stroke-dasharray:4 6;opacity:.7"/>'))
# fractures
add(gA(crack(658, 1186, 714, 1180)), when=O('wa'))
add(gA(crack(652, 1152, 712, 1078)), when=O('wb'))
add(gA(crack(670, 1000, 702, 950)), when=O('wc'))
add(gA(crack(672, 470, 704, 432)), when=O('mais'))
add(gA(crack(654, 1168, 716, 1150) + crack(440, 1142, 484, 1140)
       + '<path d="M520 1128 C540 1118 580 1118 604 1128" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-dasharray:7 5"/>'),
    when=O('bitri'))
# Maisonneuve: the force runs up the interosseous membrane — torn along its length
add(gA('<path d="M630 1040 L660 520" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:12 7;opacity:.85"/>'), when=O('mais'))
# the tibiofibular clear space widens
add(gA('<path d="M614 1112 H650 M620 1106 l-6 6 6 6 M644 1106 l6 6 -6 6" style="fill:none;stroke:var(--bad);stroke-width:2.5"/>'),
    when=O('high', 'wc', 'mais'))
# the medial clear space widens as the talus shifts
add(gA('<path d="M486 1172 H504" style="stroke:var(--bad);stroke-width:3"/>'), when=SHIFT_A)
# the leg: shin splints, stress fracture, open shaft fracture, compartment
add(gA('<path d="M490 760 L490 990 C488 1010 480 1022 470 1036" style="fill:none;stroke:var(--bad);stroke-width:20;stroke-linecap:round;opacity:.3"/>'),
    when=O('mtss'))
add(gA(crack(494, 962, 556, 958, 4) + '<circle cx="520" cy="960" r="26" class="dyn-hl"/>'), when=O('stress'))
add(gA(crack(490, 862, 585, 852) + crack(676, 846, 698, 842)
       + '<ellipse cx="530" cy="858" rx="38" ry="16" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/>'
       + '<path d="M530 850 L556 822 L566 836 Z" class="dyn-cell" style="stroke:var(--dk10)"/>'), when=O('open'))
add(gA(f'<path d="{COMP_A}" style="fill:var(--bad);fill-opacity:.22;stroke:var(--bad);stroke-width:3"/>'), when=O('comp'))

# labels: medial (left) and lateral (right), with leaders; a hurt structure's label turns red
LX, RX = 362, 792
def lab(side, y, normal, hurt, to, hurt_when, cls='nf-l2', hide=()):
    x = LX if side == 'L' else RX; an = 'end' if side == 'L' else 'start'
    lead(x + (6 if side == 'L' else -6), y - 4, to[0], to[1])
    text(normal, x, y, cls, an, unless=(hurt_when + list(hide)) or None)
    if hurt_when: text(hurt, x, y, TAG1, an, when=hurt_when)
lab('L', 300, 'femur', '', (470, 290), [])
lab('L', 660, 'tibia', '', (530, 660), [])
text('open fracture — wound over the tibia', LX, 946, TAG1, 'end', when=O('open'))
lead(LX + 6, 942, 512, 920, when=O('open'))
lab('L', 1238, 'medial malleolus', 'medial malleolus — broken', (452, 1226), O('bitri'))
lab('L', 1296, 'deltoid ligament', 'deltoid — torn (or the malleolus breaks)', (494, 1272), O('wc', 'mais'))
lab('L', 1354, 'talus', '', (540, 1290), [])
lab('R', 430, 'fibular head', 'proximal fibula — broken (Maisonneuve)', (712, 420), O('mais'))
lab('R', 760, 'interosseous membrane', 'interosseous membrane — the force runs up it', (640, 760), O('mais'))
lab('R', 900, 'fibula', 'fibula — fractured', (694, 900), O('open'))
lab('R', 1150, 'syndesmosis (AITFL)', 'syndesmosis — torn', (650, 1150), O('high', 'wc', 'mais'))
lab('R', 1200, 'joint line', 'Weber B — at the joint line', (712, 1195), O('wb'))
lab('R', 1258, 'lateral malleolus', 'lateral malleolus — broken', (706, 1250), O('bitri'), hide=O('wa'))
text('Weber A — below the joint line', RX, 1258, TAG1, when=O('wa'))
text('Weber C — above the syndesmosis', RX, 1036, TAG1, when=O('wc'))
lead(RX - 6, 1032, 700, 1036, when=O('wc'))
text('talus slides laterally', 566, 1400, TAG, 'middle', when=SHIFT_A)
text('clear space > 6 mm', RX, 1100, TAG, when=O('high', 'wc', 'mais'))
text('diffuse tenderness —', LX, 900, TAG1, 'end', when=O('mtss'))
text('posteromedial border', LX, 920, TAG, 'end', when=O('mtss'))
text('one tender spot —', LX, 1010, TAG1, 'end', when=O('stress'))
text('inferior third', LX, 1030, TAG, 'end', when=O('stress'))
text('repetitive loading', LX, 560, TAG, 'end', when=O('stress'))
text('high-energy blow', LX, 826, TAG, 'end', when=O('open'))
text('anterior compartment — tense', RX, 640, TAG1, when=O('comp'))
text('external rotation + dorsiflexion', 566, 1512, 'nf-l1', 'middle', when=O('high'))
text('rotational force at the ankle', 566, 1512, 'nf-l1', 'middle', when=O('mais'))
text('forced eversion (Pott)', 566, 1512, 'nf-l1', 'middle', when=O('bitri'))

# ════════ VIEW B — the ankle and calf from the lateral side (mirrored: toes to the left) ════════
MB = 3260
def BX(x, y): return (MB - x, y + AY)
def gB(svg): return f'<g transform="matrix(-1 0 0 1 {MB} {AY})">{svg}</g>'
text('Side view', 1060, 220, 'dyn-big')
text('left ankle and calf, lateral side · toes to the left', 1060, 240, 'dyn-cap')
TIB_B = 'M1480 200 L1600 200 L1600 600 C1606 625 1618 640 1622 650 L1462 650 C1468 630 1480 615 1480 600 Z'
FIB_B = 'M1496 200 L1530 200 L1534 600 C1550 630 1556 680 1528 708 C1510 720 1488 712 1484 690 C1478 660 1490 630 1494 600 Z'
TAL_B = ('M1470 652 C1520 638 1600 638 1640 655 C1680 670 1720 690 1760 700 C1780 712 1774 738 1750 742 L1640 744 C1600 752 1520 752 '
         '1478 738 C1462 720 1460 680 1470 652 Z')
CAL_B = 'M1300 760 C1300 728 1340 716 1400 722 C1450 728 1490 740 1540 748 L1640 750 C1660 770 1660 800 1640 820 L1600 852 L1330 852 C1300 840 1290 800 1300 760 Z'
MID_B = 'M1752 700 C1800 700 1850 712 1900 730 L2120 800 C2150 810 2160 830 2140 846 L2080 852 L1720 852 C1680 840 1650 820 1650 790 L1650 760 C1680 740 1720 712 1752 700 Z'
SKIN_B = ('M1210 200 C1186 300 1196 410 1246 510 C1284 584 1290 640 1280 700 C1262 760 1250 820 1280 862 C1300 870 1320 870 1340 870 '
          'L2150 870 C2200 868 2214 842 2190 820 C2120 780 1900 690 1720 640 C1680 628 1662 600 1660 560 L1650 200')
CALF_B = 'M1236 200 L1424 200 C1434 280 1414 380 1376 460 C1354 510 1342 560 1338 600 L1318 600 C1300 540 1262 470 1244 400 C1226 330 1224 260 1236 200 Z'
ACH_B = ((1328, 590), (1306, 782))
ATFL_B, CFL_B, PTFL_B, AITFL_B = ((1548, 668), (1650, 702)), ((1515, 708), (1480, 790)), ((1488, 688), (1464, 700)), ((1540, 598), (1600, 612))

def view_B(drawer=0, atfl='ok', ach='ok', aitfl='ok', calf=False):
    mv = slide(drawer) if drawer else ''
    s = f'<path d="M1100 870 H2240" style="stroke:var(--ink-3);stroke-width:4"/>'
    s += f'<path d="{SKIN_B}" {SKIN}/>'
    s += f'<path d="{CALF_B}" {MUS}/>'
    if calf:
        s += '<path d="M1250 470 L1270 500 L1290 470 L1310 505 L1330 475" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-linejoin:round"/>'
    # the foot (talus, calcaneus, midfoot, toes) — the anterior drawer slides it forward under the tibia
    foot = (f'<path d="{CAL_B}" {BONE}/><path d="{MID_B}" {BONE}/><ellipse cx="2170" cy="842" rx="30" ry="14" {BONE}/>'
            f'<path d="{TAL_B}" {BONE}/>')
    if ach == 'ok':
        foot += f'<path d="M{ACH_B[0][0]} {ACH_B[0][1]} L{ACH_B[1][0]} {ACH_B[1][1]}" style="stroke:{TEND};stroke-width:22;stroke-linecap:round;opacity:.9"/>'
    s += f'<g>{mv}{foot}</g>'
    if ach == 'torn':
        s += ('<path d="M1328 590 L1324 668" style="stroke:var(--bad);stroke-width:22;stroke-linecap:round"/>'
              '<path d="M1316 724 L1306 782" style="stroke:var(--bad);stroke-width:22;stroke-linecap:round"/>')
    s += f'<path d="{TIB_B}" {BONE}/><path d="{FIB_B}" class="dyn-cell" style="stroke:var(--dk10);fill-opacity:.9"/>'
    s += lig(*AITFL_B, 12, aitfl)
    s += lig(*PTFL_B, 10)
    s += lig(*CFL_B, 12)
    if atfl == 'ok' or not drawer:
        s += lig(*ATFL_B, 14, atfl)
    elif atfl == 'torn':
        s += lig(*ATFL_B, 14, 'torn', mv)
    else:          # partial: the talar end rides with the foot
        a, b = ATFL_B
        d0 = f'M{a[0]} {a[1]} L{b[0]} {b[1]}'; d1 = f'M{a[0]} {a[1]} L{b[0] + drawer} {b[1]}'
        s += (f'<path d="{d0}" style="stroke:{LIGC};stroke-width:14;stroke-linecap:round"><animate attributeName="d" values="{d0};{d1};{d1};{d0};{d0}" {DUR}/></path>'
              f'<path d="M1584 680 L1612 689" style="stroke:{TORN};stroke-width:14;stroke-linecap:round;opacity:.85"/>')
    return gB(s)
add(view_B(), unless=O('sp1', 'sp2', 'sp3', 'high', 'achrup', 'gastroc'))
add(view_B(atfl='stretch'), when=O('sp1'))
add(view_B(8, 'partial'), when=O('sp2'))
add(view_B(22, 'torn'), when=O('sp3'))
add(view_B(aitfl='torn'), when=O('high'))
add(view_B(ach='torn'), when=O('achrup'))
add(view_B(calf=True), when=O('gastroc'))
# tendinopathy: the midportion and the insertion
add(gB('<path d="M1326 630 L1316 720" style="stroke:var(--bad);stroke-width:30;stroke-linecap:round;opacity:.3"/>'
       '<circle cx="1306" cy="780" r="22" class="dyn-hl"/>'), when=O('achtend'))
# fibular fractures seen from the side
add(gB(crack(1488, 688, 1550, 682)), when=O('wa'))
add(gB(crack(1488, 654, 1546, 606)), when=O('wb', 'bitri'))
add(gB(crack(1496, 540, 1532, 500)), when=O('wc'))
add(gB(crack(1466, 640, 1500, 600, 4)), when=O('bitri'))      # the posterior lip of the tibia
x, y = BX(1328, 640)
x2, y2 = BX(1600, 684)
# labels (canvas coordinates): behind the leg on the right, the foot's ligaments below the ground
PX = 2142
def labB(y, normal, hurt, to, hurt_when, x=PX, an='start'):
    lead(x - 6 if an == 'start' else x + 6, y - 4, to[0], to[1])
    text(normal, x, y, 'nf-l2', an, unless=hurt_when or None)
    if hurt_when: text(hurt, x, y, TAG1, an, when=hurt_when)
labB(400, 'gastrocnemius · soleus', 'gastrocnemius — strained', BX(1240, 340), O('gastroc'))
labB(720, 'Achilles tendon', 'Achilles — ruptured', BX(1322, 660), O('achrup'))
text('gap 1–5 cm above the heel', PX, 742, TAG, when=O('achrup'))
text('midportion · insertion', PX, 742, TAG, when=O('achtend'))
labB(880, 'calcaneus', '', BX(1340, 800), [])
labB(340, 'tibia', '', BX(1590, 340), [], 1570, 'end')
labB(420, 'fibula — behind the tibia', 'fibula — broken above the syndesmosis', BX(1514, 420), O('wc'), 1570, 'end')
labB(640, 'AITFL — front of the syndesmosis', 'AITFL — torn', BX(1570, 605), O('high'), 1570, 'end')
labB(965, 'talus', '', BX(1620, 724), [], 1450, 'end')
lead(1514, 986, *BX(1600, 685))
text('ATFL — malleolus to talar neck', 1520, 990, 'nf-l2', unless=O('sp1', 'sp2', 'sp3'))
text('ATFL — torn', 1520, 990, TAG1, when=O('sp3'))
text('ATFL — stretched', 1520, 990, TAG1, when=O('sp1'))
text('ATFL — partly torn', 1520, 990, TAG1, when=O('sp2'))
labB(965, 'CFL — to the calcaneus', '', BX(1497, 749), [], 1800, 'start')
labB(1015, 'PTFL — to the back of the talus', '', BX(1476, 694), [], 1800, 'start')
# what the examiner does / sees in this view (the empty space in front of the leg)
BT = 1080
text('anterior drawer · talar tilt: no abnormal motion', BT, 330, 'nf-l1', when=O('sp1'))
text('stress test: mild instability, moderate pain', BT, 330, 'nf-l1', when=O('sp2'))
text('anterior drawer: the talus slides forward', BT, 330, 'nf-l1', when=O('sp3'))
text('inversion of the plantarflexed foot', BT, 354, 'nf-l2', when=O('sp1', 'sp2', 'sp3'))
text('squeeze test · external rotation test', BT, 330, 'nf-l1', when=O('high'))
text('Thompson: squeeze the calf →', BT, 330, 'nf-l1', when=O('achrup'))
text('the foot does not plantarflex', BT, 354, 'nf-l2', when=O('achrup'))
text('a “pop” on forceful push-off', BT, 378, TAG, when=O('achrup'))
text('lunge forward, ankle dorsiflexed', BT, 330, 'nf-l1', when=O('gastroc'))
text('medial belly / musculotendinous junction', BT, 354, 'nf-l2', when=O('gastroc'))
text('worst with the first steps of the day', BT, 330, 'nf-l1', when=O('achtend'))
text('no cortisone injection — it predisposes to rupture', BT, 354, 'nf-l2', when=O('achtend'))
text('posterior malleolus — the posterior lip of the tibia', BT, 330, 'nf-l1', when=O('bitri'))

# ════════ VIEW C — the mid-leg in cross-section (seen from below; anterior up, medial left) ════════
CX, CY = 1330, 1340
def gC(svg): return f'<g transform="translate({CX} {CY})">{svg}</g>'
def PC(x, y): return (CX + x, CY + y)
text('Mid-leg in cross-section', 1060, 1080, 'dyn-big')
text('seen from below, as on CT · anterior up, medial on the left', 1060, 1100, 'dyn-cap')
SKIN_C = 'M-130 -190 C-40 -215 70 -205 130 -165 C210 -115 250 -20 240 70 C230 170 120 210 0 210 C-130 210 -240 160 -250 60 C-258 -30 -210 -150 -130 -190 Z'
TIB_C = 'M-100 -175 C-80 -170 -40 -100 -35 -62 C-60 -48 -150 -45 -175 -60 C-170 -100 -125 -168 -100 -175 Z'
ANT_C = 'M-90 -168 C-30 -178 60 -170 120 -120 C150 -95 160 -50 150 -18 L128 -6 L-35 -60 C-40 -100 -70 -150 -90 -168 Z'
LAT_C = 'M150 -18 C160 -50 180 -100 212 -112 C236 -60 244 0 236 80 L176 34 C178 10 170 -8 150 -18 Z'
DEEP_C = 'M-35 -60 L128 -4 C140 30 130 50 110 60 C40 70 -60 60 -120 30 C-170 0 -180 -40 -175 -58 C-150 -45 -60 -48 -35 -60 Z'
SUP_C = 'M-200 -10 C-150 90 80 110 175 50 C185 90 150 130 100 140 C0 150 -150 120 -210 40 Z'
TP_C = (40, 10, 46, 22)            # tibialis posterior (cx, cy, rx, ry) against the membrane
def view_C():
    s = f'<clipPath id="anC-clip"><path d="{SKIN_C}"/></clipPath><path d="{SKIN_C}" style="fill:var(--surface-2);stroke:none"/><g clip-path="url(#anC-clip)">'
    for d in (ANT_C, LAT_C, DEEP_C, SUP_C):
        s += f'<path d="{d}" {MUS}/>'
    s += '<ellipse cx="-92" cy="162" rx="84" ry="38" style="fill:var(--dk7);fill-opacity:.26;stroke:var(--dk7);stroke-width:2"/>'
    s += '<ellipse cx="92" cy="166" rx="78" ry="34" style="fill:var(--dk7);fill-opacity:.26;stroke:var(--dk7);stroke-width:2"/>'
    cx, cy, rx, ry = TP_C
    s += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="fill:var(--dk7);fill-opacity:.3;stroke:var(--dk7);stroke-width:2"/>'
    s += '<path d="M-35 -62 L128 -4" style="stroke:var(--dk8);stroke-width:4"/>'                       # interosseous membrane
    s += '<path d="M-205 -36 C-160 62 60 92 168 38" style="fill:none;stroke:var(--dk8);stroke-width:3;opacity:.8"/>'   # transverse septum
    s += '<path d="M160 -14 L214 -110 M172 34 L236 80" style="stroke:var(--dk8);stroke-width:3;opacity:.8"/></g>'         # intermuscular septa
    s += f'<path d="{SKIN_C}" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>'
    s += f'<path d="{TIB_C}" {BONE}/><circle cx="152" cy="10" r="26" {BONE}/>'
    s += '<circle cx="34" cy="-74" r="8" style="fill:var(--dk10)"/><circle cx="56" cy="-62" r="8" style="fill:var(--nf-blood)"/>'
    s += '<circle cx="-20" cy="34" r="8" style="fill:var(--dk10)"/><circle cx="-2" cy="44" r="8" style="fill:var(--nf-blood)"/>'
    return gC(s)
add(view_C())
add(gC(f'<path d="{ANT_C}" style="fill:var(--bad);fill-opacity:.28;stroke:var(--bad);stroke-width:5"/>'), when=O('comp'))
add(gC('<path d="M-172 -56 C-150 -46 -80 -46 -40 -58" style="fill:none;stroke:var(--bad);stroke-width:10;stroke-linecap:round;opacity:.75"/>'),
    when=O('mtss'))
add(gC('<path d="M-150 136 L-134 150 L-118 134 L-102 150 L-86 136" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-linejoin:round"/>'),
    when=O('gastroc'))
add(gC(f'<ellipse cx="{TP_C[0]}" cy="{TP_C[1]}" rx="{TP_C[2] + 8}" ry="{TP_C[3] + 8}" class="dyn-hl"/>'), when=O('pttd'))
add(gC(crack(-120, -160, -86, -120, 4)), when=O('stress'))
add(gC(crack(-170, -100, -50, -110) + '<path d="M-150 -176 C-130 -186 -96 -188 -76 -182" style="fill:none;stroke:var(--bad);stroke-width:8;stroke-linecap:round"/>'),
    when=O('open'))
# labels inside the section
for t, x, y, cls in (('tibia', -105, -82, 'nf-l1'), ('anterior', 40, -128, 'nf-l1'), ('lateral', 196, -30, 'nf-l2'),
                     ('deep posterior', -100, 8, 'nf-l2'), ('soleus', 40, 106, 'nf-l2'), ('fibula', 152, 54, 'nf-l2')):
    text(t, *PC(x, y), cls, 'middle')
text('medial head', *PC(-92, 166), 'nf-l2', 'middle')
text('lateral head', *PC(92, 170), 'nf-l2', 'middle')
text('tib. post.', *PC(40, 54), 'nf-l2', 'middle')
text('nerve · artery', *PC(46, -94), 'nf-l2', 'middle')
text('gastrocnemius', *PC(0, 236), 'nf-l1', 'middle')
text('deep fibular nerve + anterior tibial artery inside', *PC(0, 262), TAG, 'middle', when=O('comp'))
text('pain on passive stretch · emergency fasciotomy', *PC(0, 284), TAG, 'middle', when=O('comp'))
text('posterior muscles pull on the periosteum', *PC(0, 262), TAG, 'middle', when=O('mtss'))
text('medial head of gastrocnemius — torn', *PC(0, 262), TAG, 'middle', when=O('gastroc'))
text('tibialis posterior — thickened, can’t glide', *PC(0, 262), TAG, 'middle', when=O('pttd'))
text('anterior surface is subcutaneous → open', *PC(0, 262), TAG, 'middle', when=O('open'))
text('crack in the cortex', *PC(0, 262), TAG, 'middle', when=O('stress'))

# ════════ VIEW D — the heel from behind ════════
DX0, DY0 = 2066, 1300
def gD(svg): return f'<g transform="translate({DX0} {DY0})">{svg}</g>'
def PD(x, y): return (DX0 + x, DY0 + y)
text('Heel from behind', 1760, 1080, 'dyn-big')
text('standing · lateral on the left', 1760, 1100, 'dyn-cap')
LEG_D = ('<path d="M-72 -190 C-62 -120 -46 -60 -48 -6 M72 -190 C62 -120 46 -60 48 -6" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>'
         '<path d="M-48 -6 C-62 4 -64 22 -50 28 M48 -22 C62 -14 64 4 50 10" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>'
         '<path d="M0 -160 L0 10" style="stroke:var(--dk8);stroke-width:10;stroke-linecap:round;opacity:.8"/>')
def heel(rot=0, toes=1, lift=0):
    tr = f' transform="rotate({rot} 0 110) translate(0 {-lift})"'
    ex = 60 + 18 * toes        # the forefoot shows past the heel on the lateral side — further when the foot turns out
    t = (f'<path d="M-30 74 C-50 70 {-ex + 6} 78 {-ex} 92 C{-ex - 4} 106 -50 112 -30 108 Z" {BONE}/>'
         + ''.join(f'<ellipse cx="{-ex + 4 + 16 * i}" cy="{100 - 4 * i}" rx="9" ry="8" {BONE}/>' for i in range(toes)))
    return (f'<g{tr}>{t}<path d="M-50 20 C-60 60 -50 108 0 112 C50 108 60 60 50 20 Z" {BONE}/>'
            f'<path d="M0 -10 L0 120" style="stroke:var(--accent);stroke-width:3;stroke-dasharray:6 5"/></g>')
add(gD('<path d="M-150 116 H150" style="stroke:var(--ink-3);stroke-width:4"/>'))
add(gD(LEG_D + heel()), unless=O('pttd', 'club'))
add(gD(LEG_D + heel(9, 4)
       + '<path d="M38 -120 C46 -60 50 -20 60 0 C66 14 64 30 54 44" style="fill:none;stroke:var(--bad);stroke-width:6;stroke-linecap:round"/>'),
    when=O('pttd'))
# newborn clubfoot: a small heel, high and inverted, the forefoot turned in (toes show on the medial side)
add(gD('<path d="M-50 -150 C-44 -90 -36 -40 -36 -10 M50 -150 C44 -90 36 -40 36 -10" style="fill:none;stroke:var(--ink-3);stroke-width:3"/>'
       '<g transform="rotate(-18 0 0) translate(0 -26)">'
       '<path d="M20 30 C50 26 84 36 92 56 C96 72 78 80 60 72 C44 64 30 54 20 46 Z" class="dyn-cell" style="stroke:var(--bad);stroke-width:3"/>'
       '<ellipse cx="86" cy="60" rx="8" ry="7" class="dyn-cell" style="stroke:var(--dk10)"/>'
       '<path d="M-34 8 C-42 40 -34 74 0 78 C34 74 42 40 34 8 Z" class="dyn-cell" style="stroke:var(--bad);stroke-width:3"/></g>'),
    when=O('club'))
text('lateral', *PD(-140, -150), 'dyn-cap', 'middle')
text('medial', *PD(140, -150), 'dyn-cap', 'middle')
text('heel straight · one toe shows', *PD(0, 150), 'nf-l2', 'middle', unless=O('pttd', 'club'))
text('heel tilts laterally', *PD(0, 150), TAG1, 'middle', when=O('pttd'))
text('“too many toes” on the lateral side', *PD(0, 172), TAG, 'middle', when=O('pttd'))
text('tendon behind the medial malleolus', *PD(0, 194), TAG, 'middle', when=O('pttd'))
text('newborn: small, high, inverted heel', *PD(0, 150), TAG1, 'middle', when=O('club'))
text('equinus · varus · adductus — rigid', *PD(0, 172), TAG, 'middle', when=O('club'))
text('Ponseti: casts → tenotomy → brace', *PD(0, 194), TAG, 'middle', when=O('club'))

# ════════ what happened: force · test · imaging and treatment ════════
text('What happened', 160, 1590, 'dyn-big')
CAP = dict(
  sp1=('Force: inversion of the weight-bearing, plantarflexed foot — the ATFL stretches (microtears)', 'Test: walks with minimal pain · little swelling · no abnormal motion or pain on stress testing',
       'Care: PRICE · usually no immobilization · early rehabilitation'),
  sp2=('Force: the same inversion — an incomplete ATFL tear', 'Test: bears weight with pain · moderate swelling and bruising · mild instability, moderate pain on stress testing',
       'Care: PRICE · brief non–weight bearing and immobilization · rehabilitation'),
  sp3=('Force: the same inversion — the ATFL tears through (the calcaneofibular ligament may tear too)', 'Test: cannot bear weight · large swelling within 1–2 hours · positive stress test (anterior drawer, talar tilt)',
       'Care: cannot bear weight, so the Ottawa rules call for an X-ray · short immobilization, rehab — even complete tears heal'),
  high=('Force: dorsiflexion + external rotation — the anterior inferior tibiofibular ligament (most common high sprain)', 'Test: squeeze test · external rotation test · X-ray: tibiofibular clear space over 6 mm',
        'Care: PRICE · immobilize · non–weight bearing · orthopedic consult'),
  wa=('Fracture: the fibula is avulsed below the joint line', 'Syndesmosis: intact · medial malleolus undamaged or sheared',
      'Watch: a nondisplaced lateral malleolar fracture can pass for a sprain — treated like one, it can displace'),
  wb=('Fracture: spiral, from the joint line running up and back', 'Syndesmosis: parts may tear, the interosseous ligament usually holds — no widening (complete tears happen)',
      'Medial side: intact ± deltoid tear, or a transverse avulsion · the posterior malleolus can chip off'),
  wc=('Fracture: the fibula above the syndesmosis', 'Syndesmosis: disrupted · plus a medial malleolar avulsion or a deltoid rupture',
      'Mortise: the talus can shift — 1 mm of lateral shift cuts tibiotalar contact by 40% · displaced → open reduction and fixation'),
  mais=('Force: a rotational injury at the ankle — the force travels up the interosseous membrane', 'Injury: deltoid tear or medial malleolar fracture + syndesmosis torn + proximal fibular fracture (counted as bimalleolar)',
        'Care: examine the whole fibula after an ankle injury · orthopedic consult'),
  bitri=('Fracture: medial + lateral malleoli (bimalleolar, 15–20%) ± the posterior lip of the tibia (trimalleolar, 7–12%)', 'Pott: forced eversion avulses the medial malleolus, the talus moves laterally and shears the lateral malleolus',
         'Care: reduce a dislocation at once · surgery fixes the lateral malleolus first, which sets the talus in the mortise'),
  achrup=('Force: forceful push-off — a violent “pop” in the calf or heel (classic: tennis), often after tendinitis', 'Test: Thompson — squeeze the calf, no plantarflexion · palpable gap · cannot raise the heel on that side',
          'Care: usually surgical repair — results suffer if it waits more than a week or two'),
  achtend=('Load: an increase in activity · prior tendinopathy, poor mechanics, worn shoes, age, male sex, weight', 'Feel: pain worst with the first steps of the day · insertional or midportion',
           'Care: activity change, calf stretches, night splints, NSAIDs, PT · no steroid injection · fluoroquinolones raise the risk (> 60, prednisone)'),
  gastroc=('Force: sudden acceleration from a standstill with the ankle dorsiflexed — a lunge (eccentric overstretch)', 'Test: tender medial belly · dorsiflexion reproduces the pain · grade III: palpable defect, Thompson positive',
           'Care: ice, heel lift, crutches if needed · strengthening within 24 hours · ultrasound or MRI to grade beyond grade I'),
  mtss=('Load: repetitive running — tibialis posterior, soleus and FDL pull on the posteromedial tibia (traction periostitis)', 'Test: DIFFUSE tenderness, middle-to-distal third · eases with warm-up, back after exercise · imaging often negative',
        'Care: rest, ice, NSAIDs · correct foot alignment, shoes, gait (overpronation) · cross-train'),
  stress=('Load: repetitive loading faster than bone can remodel — untreated shin splints end here', 'Test: sharp, LOCALIZED pain, worse with activity, better with rest',
          'Imaging: X-ray first, repeat in 2–3 weeks · MRI more sensitive · medial tibia low risk, anterior tibia high risk'),
  comp=('Cause: a tibial fracture, crush, reperfusion — pressure blocks venous outflow, then arterioles', 'Test: severe pain, a tense compartment, pain on passive stretch · CK rise and motor deficit are late',
        'Care: emergency fasciotomy · the anterior compartment is the most confined'),
  open=('Force: high energy — sports, car crashes · the junction of the middle and distal thirds breaks most', 'Open: the bone meets a skin wound — a 1-cm wound can hide grade III muscle damage · watch for compartment syndrome',
        'Care: IV antibiotics, urgent irrigation and debridement · reamed, locked intramedullary nail'),
  pttd=('Cause: degeneration of the tibialis posterior tendon — risk rises after 40 · ≥ 50 with atraumatic medial arch pain', 'Test: from behind, the heel tilts laterally — “too many toes” · grade 2 cannot do a single-leg heel raise',
        'Care: flexible — arch support or UCBL brace, PT · rigid (grade 3, fixed subtalar joint) — foot and ankle surgeon'),
  club=('Newborn: about 1 in 1000 · fixed equinus, varus, adductus ± cavus · calf atrophy', 'Exam: rigid — cannot be passively corrected, unlike metatarsus adductus',
        'Care: Ponseti — weekly casts for 3–5 weeks, percutaneous Achilles tenotomy, brace at night and naps up to 3 years'),
)
for k, (a, b, c) in CAP.items():
    for i, s in enumerate((a, b, c)):
        text(s, 160, 1622 + 26 * i, 'nf-l1' if i == 0 else 'nf-l2', when=O(k))
text('Force: pick an injury — the structure it tears or breaks turns red', 160, 1622, 'nf-l1', unless=ANY)
text('Ankle: lateral ligaments resist inversion, the deltoid eversion, the syndesmosis holds tibia and fibula together', 160, 1648, 'nf-l2', unless=ANY)
text('Leg: four compartments in tight fascia — the anterior one is the most confined', 160, 1674, 'nf-l2', unless=ANY)

# ════════ particles ════════
kinds = dict(force=['force', '--dk2'], test=['test', '--dk4'], press=['press', '--bad'])
groups = [['force', 'Injuring force or load'], ['test', 'Examiner’s push or squeeze'], ['press', 'Compartment pressure']]
ARC = 'M450 1430 C500 1478 632 1478 682 1430'
flows = [
  dict(d='M1660 700 C1650 780 1610 830 1540 870', len=210, speed=100, r=7, base=dict(force=3), when=O('sp1', 'sp2', 'sp3')),   # inversion
  dict(d='M1840 952 H1640', len=200, speed=100, r=7, base=dict(test=3), when=O('sp2', 'sp3')),                                # drawer pull
  dict(d=ARC, len=260, speed=110, r=7, base=dict(force=3), when=O('high', 'mais')),
  dict(d='M682 1430 C632 1478 500 1478 450 1430', len=260, speed=110, r=7, base=dict(force=3), when=O('bitri')),              # eversion
  dict(d='M630 1100 L668 560', len=545, speed=120, r=7, base=dict(force=4), when=O('mais')),                                  # up the membrane
  dict(d='M2230 520 H2100', len=130, speed=70, r=7, base=dict(test=2), when=O('achrup')),                                     # calf squeeze
  dict(d='M1990 230 H1760', len=230, speed=130, r=7, base=dict(force=3), when=O('gastroc')),                                  # lunge forward
  dict(d='M1990 900 L2000 800', len=101, speed=60, r=6, base=dict(force=2), when=O('achtend')),                               # load on the tendon
  dict(d='M537 380 V1000', len=620, speed=150, r=6, base=dict(force=4), when=O('stress')),                                    # repetitive load
  dict(d='M200 852 H470', len=270, speed=140, r=8, base=dict(force=3), when=O('open')),                                       # high-energy blow
  dict(d='M1306 1338 L1176 1264', len=150, speed=60, r=6, base=dict(force=3), when=O('mtss')),                                # traction on the periosteum
  dict(d='M1300 1200 C1340 1160 1420 1180 1440 1220 C1400 1250 1340 1250 1300 1200', len=330, speed=50, r=6, base=dict(press=6), when=O('comp')),
  dict(d='M620 600 C640 560 660 620 640 700 C620 780 650 860 640 940', len=380, speed=50, r=6, base=dict(press=4), when=O('comp')),
]

# ════════ tap targets ════════
st = lambda x, y, c, aria, n=(0, -1), when=None, unless=None: dict(
    x=x, y=y, n=list(n), w=10, t='rec', l='', aria=aria, c=c, ions=[], **({'when': when} if when else {}), **({'unless': unless} if unless else {}))
sites = [
  st(*BX(1600, 685), 'anklesprain', 'Anterior talofibular ligament'),
  st(636, 1150, 'anklesprain', 'Syndesmosis — anterior inferior tibiofibular ligament'),
  st(504, 1286, 'anklesprain', 'Deltoid ligament'),
  st(690, 1232, 'anklestab', 'Lateral malleolus'),
  st(458, 1214, 'anklefx', 'Medial malleolus'),
  st(694, 494, 'anklestab', 'Proximal fibula'),
  st(*BX(1318, 680), 'achilles', 'Achilles tendon'),
  st(*BX(1300, 380), 'gastroc', 'Gastrocnemius'),
  st(537, 760, 'tibshaft', 'Tibial shaft'),
  st(*PC(-150, -40), 'mtss', 'Posteromedial tibia'),
  st(*PC(-30, -140), 'compartment', 'Anterior compartment'),
  st(*PC(40, 14), 'pttd', 'Tibialis posterior'),
  st(*PD(0, 70), 'flatfoot', 'Heel', unless=O('club')),
  st(*PD(10, 30), 'clubfoot', 'Clubfoot', when=O('club')),
]

notes = {
  '': 'The ankle mortise is a hinge: the tibia and fibula hold the talus between the two malleoli, tied by the lateral ligaments '
      '(ATFL, CFL, PTFL), the medial deltoid ligament and, just above the joint, the syndesmosis. Pick an injury: what tears or breaks '
      'turns red, the force arrives, and the talus moves when a test or an unstable fracture lets it.',
  'an:sp1': 'Lateral ankle sprain, grade I: inversion of the plantarflexed foot stretches the anterior talofibular ligament — lateral '
            'sprains are 70–90% of all sprains, and the ATFL alone is involved in 73%. The patient walks with minimal pain, and stress '
            'testing shows no abnormal motion. PRICE and early rehabilitation, usually without immobilization.',
  'an:sp2': 'Lateral ankle sprain, grade II: an incomplete tear of the ATFL. The patient bears weight with pain; moderate swelling, '
            'bruising and tenderness, pain through normal motion, mild instability and moderate pain on stress testing. PRICE, brief '
            'non–weight bearing and immobilization, then rehabilitation.',
  'an:sp3': 'Lateral ankle sprain, grade III: the ATFL tears through. The patient cannot bear weight, the ankle swells within 1–2 hours '
            'and the stress test is positive — the anterior drawer slides the talus forward. Unable to bear weight, so the Ottawa rules '
            'call for an X-ray; even complete ankle-ligament tears usually heal without surgery.',
  'an:high': 'High (syndesmotic) ankle sprain: dorsiflexion with external rotation injures the anterior inferior tibiofibular ligament '
             '— the most common high sprain — above the joint, where the tibia and fibula are tied together. Squeeze and external '
             'rotation tests; a tibiofibular clear space over 6 mm on X-ray is the most reliable sign. Immobilize, no weight bearing, '
             'orthopedic consult.',
  'an:wa': 'Weber A: the fibula is avulsed below the joint line; the syndesmosis is intact and the medial malleolus is undamaged or '
           'sheared. Danis-Weber sorts ankle fractures by where the fibula breaks — the higher the break, the more of the syndesmosis '
           'goes with it. A nondisplaced lateral malleolar fracture treated as a sprain can displace.',
  'an:wb': 'Weber B: a spiral fibular fracture starting at the joint line and running up and back. Parts of the syndesmosis can tear '
           'but the interosseous ligament usually holds, so the tibiofibular space does not widen — although complete disruption can '
           'happen; the medial side may be intact (± a deltoid tear) or avulsed, and the posterior malleolus can chip off.',
  'an:wc': 'Weber C: the fibula breaks above the syndesmosis, so the syndesmosis is disrupted, with a medial malleolar avulsion or a '
           'deltoid rupture — the talus is free to shift laterally. A lateral talar shift of only 1 mm cuts tibiotalar contact by 40%, '
           'so the mortise has to be restored anatomically.',
  'an:mais': 'Maisonneuve fracture: a rotational force at the ankle tears the deltoid ligament (or breaks the medial malleolus), '
             'travels up the interosseous membrane and breaks the proximal fibula, with the syndesmosis completely disrupted — counted '
             'as a bimalleolar injury. A proximal fibular fracture after an ankle injury means examining the ankle; orthopedic consult.',
  'an:bitri': 'Bimalleolar (medial + lateral malleoli, 15–20% of ankle fractures) and trimalleolar (+ the posterior lip of the tibia, '
              '7–12%) fractures. In the Pott fracture-dislocation, forced eversion avulses the medial malleolus, the talus moves '
              'laterally and shears the lateral malleolus; if the tibia is carried forward the posterior lip breaks too. Reduce a '
              'dislocation at once; surgery fixes the lateral malleolus first.',
  'an:achrup': 'Achilles tendon rupture: a violent “pop” in the calf or heel on forceful push-off (tennis is the classic), usually in '
               'a poorly conditioned person with prior tendinitis; a gap 1–5 cm above the calcaneus. The toe flexors can still '
               'plantarflex the foot, so squeeze the calf (Thompson): no plantarflexion. Repair suffers if delayed beyond a week or two.',
  'an:achtend': 'Achilles tendinopathy — insertional or midportion — usually follows an increase in activity (24% of competitive '
                'athletes). Like plantar fasciitis it hurts most with the first steps: activity change, calf stretches, night '
                'splints, NSAIDs, PT — never a cortisone injection, which predisposes to rupture. Fluoroquinolones can cause tendonitis '
                'or rupture, especially over 60 or with prednisone.',
  'an:gastroc': 'Gastrocnemius strain (tennis leg): sudden acceleration from a standstill with the ankle dorsiflexed — a lunge — '
                'overstretches the medial belly or its musculotendinous junction. Tender there, dorsiflexion reproduces the pain, a '
                'palpable defect and a positive Thompson test in grade III. Ice, a heel lift, crutches if needed, strengthening '
                'within 24 hours.',
  'an:mtss': 'Medial tibial stress syndrome (shin splints): repetitive running overloads tibialis posterior, soleus and flexor '
             'digitorum longus, whose pull causes a traction periostitis on the posteromedial tibia. DIFFUSE tenderness at the junction '
             'of the middle and distal thirds that eases with warm-up; imaging is often negative. Overpronation is the one confirmed '
             'risk factor; rest, ice, NSAIDs, fix shoes and gait.',
  'an:stress': 'Tibial stress fracture: bone takes repetitive loads faster than it can remodel — untreated shin splints end here. Sharp, '
               'LOCALIZED pain after more activity, worse with activity, better with rest. X-ray first (repeat in 2–3 weeks if normal), '
               'MRI more sensitive; a medial tibial stress fracture is low risk, an anterior tibial one high risk.',
  'an:comp': 'Anterior compartment syndrome: pressure in a closed fascial compartment blocks venous outflow, then arterioles → ischemia '
             'and necrosis. The anterior compartment — walled by both bones, the interosseous membrane and dense fascia, and holding the '
             'deep fibular nerve and anterior tibial artery — is the most confined. Severe pain, pain on passive stretch; a tibial '
             'fracture is the classic cause. Emergency fasciotomy.',
  'an:open': 'Open tibial shaft fracture: the tibia’s anterior surface lies under the skin, so the shaft — narrowest and most often '
             'broken at the junction of the middle and distal thirds — is the commonest site of an open fracture. High energy (sports, '
             'car crashes); a 1-cm wound can hide grade III damage, and compartment syndrome must be watched for. IV antibiotics, '
             'urgent irrigation and debridement, an intramedullary nail.',
  'an:pttd': 'Posterior tibial tendon dysfunction: the tibialis posterior tendon, running behind the medial malleolus into the arch, '
             'thickens and can no longer glide, so the arch collapses and the heel tilts laterally — the commonest cause of adult '
             'acquired flatfoot. From behind, “too many toes”; from grade 2 a single-leg heel raise is lost. Arch support or a UCBL brace '
             'while flexible; a rigid foot needs a surgeon.',
  'an:club': 'Congenital clubfoot (talipes equinovarus), about 1 in 1000 newborns: fixed plantarflexion (equinus), an inverted, '
             'internally rotated subtalar joint (varus) and an adducted forefoot, with calf atrophy — rigid, unlike metatarsus '
             'adductus. Ponseti: weekly casts for 3–5 weeks, a percutaneous Achilles tenotomy, then a brace at night and naps for up to '
             '3 years; relapse is common if bracing lapses.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Anterior drawer · talar tilt', mods=[R(O('sp1'), 0), R(O('sp3'), 1)]),          # grade II: only "mild instability"
  dict(l='Squeeze · external rotation test', mods=[R(O('high'), 1)]),
  dict(l='Syndesmosis injured', mods=[R(O('wa'), 0), R(O('high', 'wc', 'mais'), 1)]),     # Weber B: "can be torn"
  dict(l='Thompson test (no plantarflexion)', mods=[R(O('achrup'), 1)]),
  dict(l='Pain on passive stretch', mods=[R(O('comp'), 1)]),
  dict(l='Single-leg heel raise fails', mods=[R(O('pttd', 'achrup'), 1)]),
  dict(l='Localized bony tenderness', mods=[R(O('mtss'), 0), R(O('stress'), 1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='an', label='Injury', type='one', options=[
                ['sp1', 'Lateral sprain — grade I', 'anklesprain'], ['sp2', 'Lateral sprain — grade II', 'anklesprain'],
                ['sp3', 'Lateral sprain — grade III', 'anklesprain'], ['high', 'High (syndesmotic) sprain', 'anklesprain'],
                ['wa', 'Weber A', 'anklestab'], ['wb', 'Weber B', 'anklestab'], ['wc', 'Weber C', 'anklestab'],
                ['mais', 'Maisonneuve fracture', 'anklestab'], ['bitri', 'Bi- / trimalleolar fracture', 'anklefx'],
                ['achrup', 'Achilles rupture', 'achilles'], ['achtend', 'Achilles tendinopathy', 'achtend'],
                ['gastroc', 'Tennis leg', 'gastroc'],
                ['mtss', 'Shin splints (MTSS)', 'mtss'], ['stress', 'Tibial stress fracture', 'stressfx'],
                ['comp', 'Anterior compartment syndrome', 'compartment'], ['open', 'Open tibial shaft fracture', 'openfx'],
                ['pttd', 'PTTD — adult flatfoot', 'pttd'], ['club', 'Clubfoot (newborn)', 'clubfoot']],
                 sections=[['Sprains', ['sp1', 'sp2', 'sp3', 'high']],
                           ['Ankle fractures', ['wa', 'wb', 'wc', 'mais', 'bitri']],
                           ['Tendons & calf', ['achrup', 'achtend', 'gastroc']],
                           ['Shin & leg', ['mtss', 'stress', 'comp', 'open']],
                           ['Foot shape', ['pttd', 'club']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM Ortho SDL 7, SDL 9, SDL 25 (Practical Office Orthopedics ch 5; Current Diagnosis & Treatment in Orthopedics ch 2, 12) · '
      'First Aid pp. 191, 458, 465 · Moore ch 7 · Bootcamp MSK')

MAP = dict(
  id='anklesim', title='Ankle & Leg Injuries Simulator', topic='msk', after='legfx',
  sub='The left leg from the front, the ankle and calf from the side, the mid-leg in cross-section and the heel from behind — pick a '
      'sprain, a Weber or Maisonneuve fracture, an Achilles or calf injury, shin splints, a stress or open fracture, compartment '
      'syndrome, adult flatfoot or clubfoot: what tears or breaks turns red, the force arrives, and the talus slides when the test or '
      'the fracture lets it. Tap a structure for its card',
  w=3500, h=2170,
  fa='191, 458, 465', src=[SDL7, SDL7R, SDL9, SDL25, SDL9P, MOORE7, BC_FOOT],
  lanes=[('anAnk', 'Ankle', 'tca'), ('anTen', 'Tendons & calf', 'glycogen'), ('anLeg', 'Shin & leg', 'glycolysis'),
         ('anFoot', 'Foot shape', 'sugars')],
  comps=[],
  nodes=[
    ('an1', 'Ankle sprains', 260, 1780, 'anAnk', 'ATFL first · grades', ['anklesprain', 'anklefx'], 'hub'),
    ('an2', 'Unstable ankle fractures', 640, 1780, 'anAnk', 'Weber · Maisonneuve', ['anklestab']),
    ('an3', 'Foot fractures', 1020, 1780, 'anAnk', 'Jones · navicular', ['footfx']),
    ('an4', 'Achilles', 1400, 1780, 'anTen', 'rupture · tendinopathy', ['achilles', 'achtend'], 'hub'),
    ('an5', 'Tennis leg', 1780, 1780, 'anTen', 'medial gastrocnemius', ['gastroc']),
    ('an6', 'Peroneal nerve', 2160, 1780, 'anAnk', 'fibular neck · sprains', ['peroneal']),
    ('an7', 'Shin splints vs stress fx', 260, 1860, 'anLeg', 'diffuse vs focal', ['mtss', 'stressfx', 'lowerlimboveruse'], 'hub'),
    ('an8', 'Compartment syndrome', 640, 1860, 'anLeg', 'passive stretch', ['compartment']),
    ('an9', 'Tibial shaft · open fx', 1020, 1860, 'anLeg', 'antibiotics · nail', ['tibshaft', 'openfx', 'fxdescribe']),
    ('an10', 'Adult flatfoot', 1400, 1860, 'anFoot', 'too many toes', ['pttd', 'flatfoot']),
    ('an11', 'Clubfoot', 1780, 1860, 'anFoot', 'Ponseti', ['clubfoot']),
  ],
  panels=[
    (140, 1940, 1040, 'Ottawa ankle rules (OCOM SDL 7 lecture; Practical Office Orthopedics ch 5)', [
      ('Ankle X-ray', 'malleolar pain + tenderness at the posterior lateral or medial malleolus'),
      ('— or —', 'cannot bear weight for 4 steps'),
      ('Foot X-ray', 'navicular or 5th metatarsal pain'),
      ('ATFL sprain', 'tender over the anterior half of the lateral malleolus only'),
      ('Fracture', 'tender all along the lateral malleolus, front and back'),
      ('Also X-ray', 'over 55 · sensory loss, such as diabetic neuropathy')]),
    (1220, 1940, 1100, 'Danis-Weber: where the fibula breaks (Current Diagnosis & Treatment in Orthopedics ch 2)', [
      ('A — below the joint', 'fibula avulsed · syndesmosis intact'),
      ('B — at the joint', 'spiral, up and back · syndesmosis usually holds'),
      ('C — above', 'syndesmosis disrupted + medial malleolus or deltoid'),
      ('Maisonneuve', 'proximal fibula + syndesmosis + medial side'),
      ('1 mm talar shift', 'tibiotalar contact −40%'),
      ('Clear space', 'tibiofibular > 6 mm → syndesmotic injury')]),
  ],
  dyn=dyn,
)
