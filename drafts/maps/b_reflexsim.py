# m55 — Spinal Reflexes & Motor Neurons in Motion (dynamic map, kit data)
# One lumbar segment (L2–L4) in cross-section with the patellar reflex arc wired up: the tested leg on the left (seated,
# facing left — quadriceps on top of the thigh, hamstrings below, a muscle spindle in the quadriceps belly, a Golgi tendon
# organ at its tendon, a reflex hammer at the patellar tendon), the opposite leg on the right, and the upper motor neurons
# coming down from above into the lateral corticospinal tract. One `one` switch, in four `sections`, picks a reflex circuit
# (stretch, reciprocal inhibition, Golgi tendon, withdrawal + crossed extension, Renshaw, γ drive) or a lesion (spinal
# shock, chronic UMN, LMN, polio, SMA, cauda equina, ALS, tetanus, the newborn). Each option lights its fibres and moves
# its particles, puts the ✕ where the lesion is, moves the leg (kick, brisk kick + ankle clonus, none, held flexed,
# lengthening reaction, rigid), thins the muscle or makes it twitch, lights the reflex grade (0 … 4+) and turns the big
# toe up or down. Seven readouts: Ia firing, Ib firing, stretch reflexes, tone, muscle bulk, fasciculations, Babinski.
# cordsim (where in the cross-section a lesion sits, and the sensory tracts) and motorctl (cortex → muscle, static) cover
# the neighbours; this map is about WHY the reflexes and tone change.
#
# Sources (all read in the corpus; U+00A0 / U+00AD normalized):
#   First Aid 2025 p. 461 (muscle spindle: body of muscle, Ia and II, ↑ length and speed of stretch → DRG → inhibitory
#     interneuron + α motor neuron → antagonist inhibited, agonist contracts, deep tendon reflexes; Golgi tendon organ:
#     tendon, Ib, ↑ tension → inhibitory interneuron → agonist inhibited) · p. 523 (reflex roots: Achilles S1–S2, patellar
#     L2–L4, biceps and brachioradialis C5–C6, triceps C6–C8, cremasteric L1–L2, anal wink S3–S4; grades 0 absent, 1+
#     hypoactive, 2+ normal, 3+ hyperactive, 4+ clonus; plantar reflex is a primitive reflex, Babinski in an adult may
#     signify a UMN lesion) · p. 543 (motor neuron signs table: weakness both; atrophy, fasciculations LMN only; reflexes
#     and tone ↑ UMN / ↓ LMN; Babinski, spastic paresis, clasp-knife UMN; flaccid paralysis LMN; positive Babinski normal
#     in infants) · p. 544 (polio: anterior horns, fecal–oral, acute asymmetric LMN signs + viral meningitis, respiratory
#     failure; SMA: SMN1, AR, LMN signs only, floppy baby, hypotonia, tongue fasciculations, Werdnig-Hoffmann; ALS: UMN +
#     LMN, flaccid weakness, fasciculations, atrophy, bulbar palsy + spastic weakness, hyperreflexia, clonus, no sensory or
#     bowel/bladder deficits, riluzole, edaravone) · p. 520 (cord ends L1–L2; conus medullaris = symmetric weakness with UMN
#     signs, cauda equina = asymmetric with LMN signs; radicular pain, saddle anesthesia, bladder/bowel) · pp. 130, 136
#     (tetanospasmin: retrograde transport, blocks GABA and glycine release from Renshaw cells → spastic paralysis, trismus,
#     risus sardonicus, opisthotonos).
#   Guyton ch 55 (α and γ motor neurons; Renshaw cells: collaterals just after the axon leaves the cell body, inhibit the
#     surrounding motor neurons — lateral inhibition that focuses the signal; spindle: Ia primary ending 70–120 m/s, II
#     secondary; gamma excitation stretches the receptor region; stretch reflex monosynaptic; jerks exaggerated by
#     facilitation from above and weak or absent when it is depressed; clonus = oscillating jerks when the reflex is
#     highly sensitized; bulboreticular facilitatory region drives γ, stabilizes joints by sensitized stretch reflexes;
#     coactivation; Golgi tendon reflex: Ib → single inhibitory interneuron, entirely inhibitory, lengthening reaction;
#     flexor reflex: pain, interneuron pool, reciprocal inhibition, afterdischarge; crossed extensor 0.2–0.5 s later;
#     spinal shock: cord reflexes silent, BP to 40 mm Hg, sacral reflexes suppressed for weeks, humans 2 weeks to months,
#     stretch reflexes return first, some become hyperexcitable).
#   Costanzo ch 3 (Table 3.5: stretch reflex 1 synapse Ia → contraction; Golgi tendon reflex 2 synapses Ib → relaxation,
#     clasp-knife; flexor withdrawal many synapses, II/III/IV, ipsilateral flexion + contralateral extension,
#     afterdischarge; γ motoneurons adjust spindle sensitivity, α–γ coactivation; Ia and Ib among the largest, fastest).
#   Fundamental Neuroscience ch 9 (knee jerk: Ia → quadriceps motor neurons; Ia inhibitory glycinergic interneurons inhibit
#     the hamstrings; Golgi tendon organ → Ib inhibitory interneurons, autogenic inhibition; flexor reflex: Aδ/C →
#     excitatory interneurons → flexors (iliopsoas, hamstrings, tibialis anterior), extensors inhibited; crossed extension:
#     interneurons to the contralateral anterior horn excite extensors; conus at L1–L2, cauda equina L2–Co1) · ch 24 (LMN
#     loss → profound weakness and areflexia; gamma loop maintains stretch reflexes and tone; α–γ coactivation; Golgi tendon
#     organ in series, Ib 70–110 m/s → interneurons that inhibit the agonist; reciprocal inhibition via Ia interneurons;
#     crossed extensor) · ch 25 (LMN signs: flaccid paralysis → atrophy, fibrillations or fasciculations, hypotonia,
#     hyporeflexia/areflexia; UMN: initially weak and flaccid, eventually spastic, hypertonia, hyperreflexia, clonus,
#     Babinski; spasticity velocity-dependent, clasp-knife; descending fibres drive Ia inhibitory interneurons and Renshaw
#     cells (glycinergic, inhibit the same and adjacent motor neurons) — their loss → clonus; neonatal Babinski from
#     incomplete myelination of the corticospinal tract) · ch 33 (reflex roots, femoral L2–L4, tibial S1; hyperreflexia when
#     descending inhibition is damaged, hypo/areflexia when the nerve is injured; Babinski normal in infants; spasticity,
#     clasp-knife; hypotonia) · ch 4 (tetanus toxin: synaptobrevin, retrograde transport, inhibitory interneurons;
#     strychnine causes a tetanus-like hyperreflexia and spasticity).
#   Robbins ch 28 (ALS: UMN + LMN, spasticity, then muscle bulk falls and fasciculations; polio: flaccid paralysis with
#     muscle wasting and hyporeflexia; SMA: loss of LMNs, SMN1, type I Werdnig-Hoffmann fatal by about 2 years) · ch 8
#     (tetanus: increased muscle tone, generalized spasms).
#   Bootcamp.com Neurology — invasive spinal cord disease and spinal cord syndromes (supporting only: polio LMN signs incl.
#     fasciculations, hypotonia; tetanus → unregulated α motor neurons, hyperreflexia; conus = mix of UMN and LMN, cauda =
#     primarily LMN). Kept out of `src` (textbooks + FA only).
# Cut for lack of support in the corpus: the Jendrassik maneuver and anxiety as γ-drive examples (no hit anywhere); a
#   reflex grade for γ drive or tetanus (no source grades them); tone in ALS (both spastic and flaccid limbs → "–");
#   Babinski in ALS, spinal shock, cauda equina (no source says); atrophy/fasciculations in spinal shock and cauda equina;
#   the conus medullaris as its own option (FA says UMN signs, Bootcamp says a mix → kept only as a sentence in the cauda
#   note); which root is the "main" one for each reflex (FA marks it in bold, lost in the text) — the panel gives ranges;
#   the age when the infant Babinski fades (FA: primitive reflexes go in the 1st year; Moore: Babinski up to 4 years).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

GY55, CZ3 = full('Guyton', 55), full('Costanzo', 3)
FN4, FN9, FN24, FN25, FN33 = (full('Fundamental Neuroscience', c) for c in (4, 9, 24, 25, 33))
RB28, RB8 = full('Robbins', 28), full('Robbins', 8)
SRC = [GY55, CZ3, FN9, FN24, FN25, FN33, FN4, RB28, RB8]

O = lambda *k: ['rx:' + x for x in k]
DEF = ['!rx:*']
TAPPED = DEF + O('tap', 'recip', 'renshaw', 'gamma', 'shock', 'umn', 'lmn', 'als', 'polio', 'sma', 'cauda', 'tetanus')
UMNCUT = O('shock', 'umn', 'als')                 # the descending tract is cut / degenerated
MNDEAD = O('polio', 'sma', 'als')                 # anterior horn cells lost
ATROPHY = O('lmn', 'polio', 'sma', 'als')
FASC = O('lmn', 'polio', 'als')                   # limb fasciculations drawn (SMA: the tongue)
BABI = O('umn', 'infant')

def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))
MX = lambda x: 2480 - x                           # mirror across the cord's midline (x = 1240)
def mirror(pts): return [(MX(x), y) for x, y in pts]

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

# ════════ fibres (polylines) ════════
F = dict(
  ia_p=[(600, 1144), (600, 620), (660, 500), (722, 412)],
  ia_c=[(722, 412), (958, 402), (1090, 398), (1060, 560), (1015, 775)],
  ia_i=[(1065, 530), (1165, 687)],
  in_h=[(1160, 712), (1128, 795)],                                   # Ia inhibitory interneuron ⊣ hamstring α
  ib=[(490, 1138), (520, 1095), (588, 1095), (588, 620), (650, 495), (714, 420), (958, 410), (1080, 405), (1052, 560), (1100, 614)],
  ib_i=[(1100, 637), (1028, 782)],                                    # Ib interneuron ⊣ quadriceps α
  pain=[(440, 1185), (470, 1262), (576, 1262), (576, 620), (640, 490), (706, 426), (958, 418), (1070, 412), (1140, 528)],
  e_h=[(1145, 553), (1125, 795)],                                     # excitatory interneuron → hamstring α
  comm=[(1152, 548), (1215, 640), (1240, 712), (1300, 735), (1450, 786)],
  gam=[(975, 772), (872, 822), (720, 828), (624, 740), (624, 1078), (642, 1146)],
  aq_c=[(1000, 822), (876, 834), (796, 837)], aq_p=[(796, 837), (720, 840), (636, 752), (636, 1086), (700, 1124)],
  ah_c=[(1112, 836), (1000, 858), (880, 848), (796, 850)], ah_p=[(796, 850), (720, 852), (648, 764), (648, 1200), (700, 1222)],
  ren=[(990, 818), (1068, 778)], ren_q=[(1066, 766), (1030, 790)], ren_h=[(1084, 780), (1104, 800)],
  umn=[(820, 236), (820, 540), (858, 606)],
  cst_q=[(895, 668), (990, 782)], cst_g=[(886, 676), (966, 756)], cst_i=[(907, 646), (1156, 698)],
)
F['aqr'] = mirror([(1000, 822), (876, 834), (720, 840), (636, 752), (636, 1086), (700, 1124)])
F['aqr'][0] = (1470, 822)

ACTIVE = {   # which fibres light up in which states
  'ia_p': TAPPED + O('gamma'), 'ia_c': TAPPED, 'ia_i': DEF + O('tap', 'recip', 'gamma', 'umn', 'tetanus'),
  'in_h': DEF + O('recip', 'tap', 'gamma', 'umn'), 'ib': O('gto'), 'ib_i': O('gto'), 'pain': O('withdraw'), 'e_h': O('withdraw'),
  'comm': O('withdraw'), 'gam': O('gamma'), 'aq_c': TAPPED + O('gto'), 'aq_p': TAPPED + O('gto'), 'ah_c': O('withdraw', 'tetanus'),
  'ah_p': O('withdraw', 'tetanus'), 'ren': O('renshaw'), 'ren_q': O('renshaw'), 'ren_h': O('renshaw'), 'umn': DEF + O('gamma', 'tap', 'recip', 'renshaw'),
  'aqr': O('withdraw'), 'cst_q': [], 'cst_g': O('gamma'), 'cst_i': [],
}
DASH = {'in_h', 'ib_i', 'ren_q', 'ren_h'}      # inhibitory connections drawn dashed

# ════════ the drawing ════════
text('One lumbar segment (L2–L4) and the patellar reflex arc', 160, 80, 'dyn-big')
text('the tested leg on the left, seated and facing left · the opposite leg on the right · the brain’s drive from above', 160, 100, 'dyn-cap')

# upper motor neurons
add('<rect x="580" y="130" width="500" height="100" rx="22" class="dyn-soft"/>')
text('Upper motor neurons', 606, 166, 'nf-l1')
text('motor cortex (corticospinal) · brainstem', 606, 186, 'nf-l2')
text('(reticulospinal, vestibulospinal) — drive γ too', 606, 204, 'nf-l2')
add('<rect x="580" y="130" width="500" height="100" rx="22" class="dyn-hl" style="opacity:.4"/>', when=O('gamma'))
text('bulboreticular region turns γ up', 1100, 186, TAG, when=O('gamma'))

# the cord: white matter, grey matter, central canal
CX, CY, RX, RY = 1240, 640, 470, 300
add(f'<ellipse cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}" class="dyn-cell"/>')
GL = [(1240, 585), (1180, 570), (1135, 405), (1090, 385), (1055, 415), (1100, 580), (1050, 640), (930, 740), (960, 850),
      (1090, 880), (1180, 770), (1240, 760)]
GR = [(MX(x), y) for x, y in reversed(GL)]
add(f'<path d="{P(GL + GR)} Z" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:3;stroke-linejoin:round"/>')
add(f'<circle cx="{CX}" cy="672" r="9" class="dyn-cell"/>')
text('dorsal horn', 1430, 470, 'nf-l2', 'middle')
text('ventral horn', 1470, 900, 'nf-l2', 'middle')
text('white matter', 1560, 640, 'nf-l2', 'middle')

# roots, ganglia and the nerve trunks (both sides)
for side in (1, -1):
    m = (lambda x: x) if side == 1 else MX
    add(f'<path d="M{m(722)} 412 L{m(958)} 404" class="dyn-line" style="stroke-width:26;opacity:.16;stroke-linecap:round"/>')
    add(f'<path d="M{m(720)} 840 L{m(880)} 836" class="dyn-line" style="stroke-width:30;opacity:.16;stroke-linecap:round"/>')
    add(f'<path d="M{m(706)} 432 L{m(612)} 620 V1080 M{m(712)} 830 L{m(624)} 740" class="dyn-line" style="stroke-width:62;opacity:.12;stroke-linejoin:round;stroke-linecap:round"/>')
    add(f'<ellipse cx="{m(726)}" cy="414" rx="40" ry="26" class="dyn-cell" style="stroke:var(--dk1)"/>')
text('Dorsal root ganglion', 726, 372, 'nf-l2', 'middle')
text('dorsal root', 850, 388, 'nf-l2', 'middle')
text('ventral root', 790, 884, 'nf-l2', 'middle')
text('spinal nerve', 548, 900, 'nf-l2', 'end')
text('to the thigh', 548, 916, 'nf-l2', 'end')

# the descending tract
add(f'<path d="{P(F["umn"])}" class="dyn-line" style="stroke-width:5;stroke:var(--dk10);opacity:.55" marker-end="url(#ah-rfUmn)"/>')
add(f'<circle cx="870" cy="640" r="38" class="dyn-soft" style="stroke:var(--dk10);stroke-width:2.5"/>')
text('Lateral', 870, 636, 'nf-l2', 'middle')
text('cortico-', 870, 652, 'nf-l2', 'middle')
text('spinal', 870, 668, 'nf-l2', 'middle')
add(f'<path d="{P(F["umn"])}" class="dyn-dash" style="stroke-width:7;stroke:var(--surface)"/>', when=O('infant'))
text('tract not yet fully myelinated', 836, 300, TAG, when=O('infant'))

# fibres: dim line always, highlighted when that circuit is in use
for k, pts in F.items():
    cls = 'dyn-dash' if k in DASH else 'dyn-line'
    if k in ('umn',): continue
    add(f'<path d="{P(pts)}" class="{cls}" style="stroke-width:2.5;opacity:.55;stroke-linejoin:round"/>')
    if ACTIVE.get(k):
        add(f'<path d="{P(pts)}" class="dyn-hl" style="opacity:.28"/>', when=ACTIVE[k])

# neurons (grey matter)
def cell(x, y, r, col, lab=None, lx=None, ly=None, an='middle', dim=None):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" class="dyn-cell" style="stroke:var({col});stroke-width:3"/>', unless=dim)
    if dim: add(f'<circle cx="{x}" cy="{y}" r="{r}" class="dyn-cell dyn-dim" style="stroke:var(--bad);stroke-width:3;stroke-dasharray:5 4"/>', when=dim)
    if lab: text(lab, lx, ly, 'nf-l2', an)
cell(1010, 800, 24, '--dk5', 'αQ', 1010, 805, dim=MNDEAD)
cell(1120, 815, 22, '--dk5', 'αH', 1120, 820, dim=MNDEAD)
cell(972, 756, 14, '--dk7', 'γ', 972, 761, dim=MNDEAD)
cell(1075, 770, 14, '--dk8', 'R', 1075, 775)
cell(1170, 700, 13, '--dk8', 'Ia inhib.', 1192, 704, 'start')
cell(1110, 625, 13, '--dk8', 'Ib inhib.', 1086, 629, 'end')
cell(1145, 540, 13, '--dk11', 'excit.', 1166, 544, 'start')
cell(1470, 800, 24, '--dk5', 'αQ', 1470, 805)
text('to the other leg’s quadriceps', 1500, 770, 'nf-l2', 'start')
cell(1360, 815, 22, '--dk5')
text('αQ, αH = α motor neurons to quadriceps, hamstrings · γ = γ motor neuron · R = Renshaw cell', 1240, 972, 'nf-l2', 'middle')
text('inhib. = inhibitory (glycine) interneuron · excit. = excitatory interneuron', 1240, 990, 'nf-l2', 'middle')

# ── the legs ──
KX, KY = 440, 1185                        # left knee; the thigh runs from the knee (x 440) to the hip end (x 800)
def thigh(m):
    out = (f'<path d="M{m(800)} 1110 H{m(470)} Q{m(408)} 1112 {m(402)} 1185 Q{m(408)} 1262 {m(470)} 1268 H{m(800)}" '
           f'class="dyn-cell" style="stroke-width:3"/>')
    out += f'<path d="M{m(470)} 1192 H{m(800)}" class="dyn-line" style="stroke-width:7;opacity:.25"/>'   # femur
    return out
L = lambda x: x
for m in (L, MX):
    add(thigh(m))
def quad(m, ry=34, extra=''):
    return f'<ellipse cx="{m(625)}" cy="1150" rx="170" ry="{ry}" class="dyn-cell" style="stroke:var(--dk4);stroke-width:3{extra}"/>'
def ham(m, ry=28):
    return f'<ellipse cx="{m(625)}" cy="1232" rx="170" ry="{ry}" class="dyn-cell" style="stroke:var(--dk9);stroke-width:3"/>'
add(quad(L), unless=ATROPHY)
add(quad(L, 18, ';opacity:.6'), when=ATROPHY)
add(ham(L), unless=ATROPHY)
add(ham(L, 16), when=ATROPHY)
add(quad(MX)); add(ham(MX))
add(f'<ellipse cx="625" cy="1150" rx="177" ry="40" class="dyn-hl" style="opacity:.32"/>',
    when=DEF + O('tap', 'recip', 'renshaw', 'gamma', 'umn', 'als', 'tetanus'))
add(f'<ellipse cx="625" cy="1232" rx="177" ry="34" class="dyn-hl" style="opacity:.32"/>', when=O('withdraw', 'tetanus'))
add(f'<ellipse cx="{MX(625)}" cy="1150" rx="177" ry="40" class="dyn-hl" style="opacity:.32"/>', when=O('withdraw'))
text('Quadriceps (extensor)', 520, 1100, 'nf-l1', 'middle')
text('Hamstrings (flexor)', 625, 1300, 'nf-l1', 'middle')
text('Quadriceps', MX(625), 1100, 'nf-l1', 'middle')
text('Hamstrings', MX(625), 1300, 'nf-l1', 'middle')
text('relaxes — Ia inhibitory interneuron', 640, 1340, TAG, 'middle', when=O('recip'))
text('flexors contract · extensors relax', 660, 1340, TAG, 'middle', when=O('withdraw'))
text('extends to bear the weight', MX(625), 1340, TAG, 'middle', when=O('withdraw'))
text('atrophy', 810, 1150, TAG, 'start', when=ATROPHY)
# fasciculations: little flickering arcs on the left quadriceps
fz = ''.join(f'<path d="M{x - 12} {y} q12 -14 24 0" class="dyn-line" style="stroke:var(--bad);stroke-width:3">'
             f'<animate attributeName="opacity" values="0;1;0;0" keyTimes="0;.1;.25;1" dur="{d}s" repeatCount="indefinite"/></path>'
             for x, y, d in ((500, 1146, 1.3), (690, 1156, 1.9), (740, 1142, 1.6), (540, 1158, 2.3)))
add(fz, when=FASC)
text('fasciculations', 810, 1172, TAG, 'start', when=FASC)
# muscle spindle (with γ-innervated poles) and Golgi tendon organ
add('<path d="M555 1150 Q600 1132 645 1150 Q600 1168 555 1150 Z" class="dyn-cell" style="stroke:var(--dk1);stroke-width:2.5"/>'
    '<path d="M587 1144 q4 6 8 0 q4 -6 8 0 q4 6 8 0" class="dyn-line" style="stroke:var(--dk1);stroke-width:2"/>')
add('<path d="M555 1150 Q600 1132 645 1150 Q600 1168 555 1150 Z" class="dyn-hl" style="opacity:.5"/>', when=O('gamma'))
add('<rect x="476" y="1138" width="28" height="24" rx="6" class="dyn-cell" style="stroke:var(--dk3);stroke-width:2.5"/>'
    '<path d="M480 1150 l5 -6 5 12 5 -12 5 6" class="dyn-line" style="stroke:var(--dk3);stroke-width:2"/>')

# the left lower leg: a group that rotates about the knee — one variant per state
def shin(anim='', static='', foot_anim='', extra=''):
    tr = f' transform="rotate({static} {KX} {KY})"' if static != '' else ''
    g = f'<g{tr}>{anim}'
    g += ('<path d="M412 1196 Q408 1400 420 1600 L470 1604 Q482 1400 472 1196 Z" class="dyn-cell" style="stroke-width:3"/>'
          '<path d="M440 1210 V1590" class="dyn-line" style="stroke-width:6;opacity:.25"/>'
          '<ellipse cx="430" cy="1172" rx="14" ry="22" class="dyn-cell" style="stroke-width:2.5"/>'                      # patella
          '<path d="M476 1150 Q422 1150 418 1176 Q418 1222 436 1246" class="dyn-line" style="stroke-width:5;opacity:.6;fill:none"/>')   # patellar tendon
    g += (f'<g>{foot_anim}<path d="M422 1596 L328 1640 Q312 1652 326 1662 L466 1664 Q482 1640 472 1600 Z" class="dyn-cell" style="stroke-width:3"/>'
          f'{extra}</g></g>')
    return g
rot = lambda vals, kt, dur: (f'<animateTransform attributeName="transform" type="rotate" values="{";".join(f"{v} {KX} {KY}" for v in vals)}" '
                             f'keyTimes="{kt}" dur="{dur}s" repeatCount="indefinite"/>')
ank = ('<animateTransform attributeName="transform" type="rotate" values="0 445 1606;-13 445 1606;0 445 1606;-13 445 1606;0 445 1606;-11 445 1606;0 445 1606;0 445 1606" '
       'keyTimes="0;.1;.2;.3;.4;.5;.6;1" dur="2.4s" repeatCount="indefinite"/>')
KICK = DEF + O('tap', 'recip', 'renshaw')
add(shin(rot((0, 0, 22, 0, 0), '0;.3;.4;.62;1', 2.4)), when=KICK)
add(shin(rot((0, 0, 30, 0, 0), '0;.3;.38;.6;1', 2.4)), when=O('gamma'))
add(shin(rot((0, 0, 34, 6, 20, 0, 0), '0;.3;.37;.47;.55;.66;1', 2.4), foot_anim=ank), when=O('umn', 'als'))
add(shin(), when=O('shock', 'lmn', 'polio', 'sma', 'cauda', 'infant'))
WEIGHT = ('<rect x="392" y="1600" width="70" height="44" rx="8" class="dyn-cell" style="stroke:var(--ink-3);stroke-width:3"/>'
          '<text class="nf-l1" x="427" y="1628" text-anchor="middle">kg</text>')
add(shin(rot((40, 40, 0, 0, 40), '0;.55;.6;.92;1', 3.2), extra=WEIGHT), when=O('gto'))
TACK = ('<path d="M372 1690 L386 1664 L400 1690 Z" style="fill:var(--bad)"/>'
        '<path d="M386 1660 L440 1600 L440 1192" class="dyn-hl" style="opacity:.3"/>'
        '<circle r="6" fill="var(--dk2)" stroke="var(--surface)" stroke-width="1.4"><animateMotion dur="2.2s" repeatCount="indefinite" path="M386 1660 L440 1600 L440 1190"/></circle>'
        '<circle r="6" fill="var(--dk2)" stroke="var(--surface)" stroke-width="1.4"><animateMotion dur="2.2s" begin="-1.1s" repeatCount="indefinite" path="M386 1660 L440 1600 L440 1190"/></circle>')
add(shin(static=-32, extra=TACK), when=O('withdraw'))
add(shin(rot((26, 29, 25, 30, 26), '0;.25;.5;.75;1', 0.6)), when=O('tetanus'))
# the right lower leg: hangs, or extends in the crossed extensor reflex (drawn mirrored: +angle = extension)
def rshin(static=''):
    return f'<g transform="translate(2480 0) scale(-1 1)">{shin(static=static)}</g>'
add(rshin(), unless=O('withdraw'))
add(rshin(static=30), when=O('withdraw'))

# the reflex hammer
HAM = ('<g>{a}<path d="M260 1330 L390 1226" class="dyn-line" style="stroke:var(--dk8);stroke-width:7;stroke-linecap:round"/>'
       '<rect x="376" y="1196" width="34" height="54" rx="8" class="dyn-cell" style="stroke:var(--dk8);stroke-width:3" transform="rotate(-38 393 1223)"/></g>')
tap_anim = ('<animateTransform attributeName="transform" type="rotate" values="-18 260 1330;-18 260 1330;0 260 1330;-18 260 1330;-18 260 1330" '
            'keyTimes="0;.18;.28;.4;1" dur="2.4s" repeatCount="indefinite"/>')
add(HAM.format(a=tap_anim), when=TAPPED)
text('tap the patellar tendon', 160, 1360, 'nf-l2', when=TAPPED)
text('a weight pulls on the tendon', 160, 1360, 'nf-l2', when=O('gto'))
text('a tack under the foot', 640, 1700, 'nf-l2', 'middle', when=O('withdraw'))

# lesion ✕s and tags
add(XM(820, 300), when=UMNCUT)
text('cord transected above this segment', 850, 306, TAG, when=O('shock'))
text('corticospinal (UMN) lesion', 850, 306, TAG, when=O('umn'))
text('UMNs degenerate', 850, 306, TAG, when=O('als'))
for x, y in ((1010, 800), (1120, 815)):
    add(XM(x, y, 11), when=MNDEAD)
add(XM(800, 842), when=O('lmn', 'cauda'))
add(XM(840, 406), when=O('cauda'))
text('motor root cut', 760, 918, TAG, 'middle', when=O('lmn'))
text('roots compressed (cauda equina)', 760, 918, TAG, 'middle', when=O('cauda'))
text('anterior horn cells lost', 1240, 1016, TAG, 'middle', when=O('polio', 'sma'))
text('UMNs and anterior horn cells lost', 1240, 1016, TAG, 'middle', when=O('als'))
for x, y in ((1075, 770), (1170, 700)):
    add(XM(x, y, 10), when=O('tetanus'))
text('GABA and glycine release blocked', 1240, 1016, TAG, 'middle', when=O('tetanus'))

# what the patient shows (under the tested leg)
SIGN = [('shock', 'flaccid · no reflexes · BP falls — days to weeks'), ('umn', 'spastic · clasp-knife · brisk jerks · ankle clonus'),
        ('lmn', 'flaccid · reflex lost · wasting · fasciculations'), ('polio', 'asymmetric flaccid paralysis after a fever'),
        ('sma', 'floppy baby · tongue fasciculations'), ('cauda', 'saddle anesthesia · bladder, bowel · flaccid'),
        ('als', 'spastic and wasted · fasciculations · no sensory loss'), ('tetanus', 'rigid spasms · trismus · risus sardonicus'),
        ('gto', 'tension too high → the leg drops (lengthening reaction)'), ('gamma', 'more sensitive spindle → a brisker jerk'),
        ('withdraw', 'flexes and stays flexed (afterdischarge)'), ('renshaw', 'neighbouring motor neurons held back')]
for k, s in SIGN:
    text(s, 160, 1800, TAG, when=O(k))

# ── reflex grade (First Aid p. 523) ──
GX, GY = 900, 1090
text('Stretch reflex grade', GX, GY - 16, 'nf-l1')
GR_ = [('0', 'absent'), ('1+', 'low'), ('2+', 'normal'), ('3+', 'brisk'), ('4+', 'clonus')]
LIT = {0: O('shock', 'lmn', 'polio', 'sma', 'cauda'), 1: O('lmn', 'polio', 'sma', 'cauda'), 2: DEF + O('tap', 'recip', 'renshaw'),
       3: O('umn', 'als'), 4: O('umn', 'als')}
for i, (g, s) in enumerate(GR_):
    x = GX + i * 136
    add(f'<rect x="{x}" y="{GY}" width="120" height="64" rx="12" class="dyn-soft"/>')
    add(f'<rect x="{x}" y="{GY}" width="120" height="64" rx="12" class="dyn-hl" style="opacity:.6"/>', when=LIT[i])
    text(g, x + 60, GY + 30, 'nf-l1', 'middle')
    text(s, x + 60, GY + 50, 'nf-l2', 'middle')

# ── plantar response inset ──
PX, PY = 900, 1290
add(f'<rect x="{PX}" y="{PY}" width="680" height="300" rx="24" class="dyn-soft"/>')
text('Plantar response — stroke the lateral sole', PX + 24, PY + 36, 'nf-l1')
FOOT = (f'<path d="M{PX + 110} {PY + 210} Q{PX + 90} {PY + 150} {PX + 140} {PY + 120} L{PX + 230} {PY + 90} Q{PX + 300} {PY + 110} '
        f'{PX + 420} {PY + 170} L{PX + 470} {PY + 196} Q{PX + 480} {PY + 226} {PX + 450} {PY + 232} L{PX + 140} {PY + 236} '
        f'Q{PX + 112} {PY + 234} {PX + 110} {PY + 210} Z" class="dyn-cell" style="stroke-width:3"/>')
add(FOOT)
add(f'<path d="M{PX + 150} {PY + 256} Q{PX + 300} {PY + 266} {PX + 440} {PY + 252}" class="dyn-line" style="stroke:var(--dk8);stroke-width:3" marker-end="url(#ah-rfArc)"/>')
TOE_DN = f'<path d="M{PX + 462} {PY + 200} Q{PX + 520} {PY + 210} {PX + 540} {PY + 250}" class="dyn-line" style="stroke-width:16;stroke-linecap:round"/>'
TOE_UP = f'<path d="M{PX + 462} {PY + 200} Q{PX + 520} {PY + 180} {PX + 548} {PY + 128}" class="dyn-line" style="stroke:var(--bad);stroke-width:16;stroke-linecap:round"/>'
add(TOE_DN, unless=BABI)
add(TOE_UP, when=BABI)
text('toes curl down — normal adult', PX + 560, PY + 250, 'nf-l2', unless=BABI)
text('big toe up — Babinski sign', PX + 470, PY + 110, TAG, when=O('umn'))
text('big toe up — normal in a newborn', PX + 380, PY + 80, TAG, when=O('infant'))

# ════════ particles ════════
kinds = {'ia': ['ia', '--dk1'], 'ib': ['ib', '--dk3'], 'pain': ['pain', '--dk2'], 'alpha': ['alpha', '--dk5'],
         'gamma': ['gamma', '--dk7'], 'inh': ['inh', '--dk8'], 'exc': ['exc', '--dk11'], 'umn': ['umn', '--dk10']}
groups = [['ia', 'Ia — spindle'], ['ib', 'Ib — tendon organ'], ['pain', 'Pain (Aδ, C)'], ['alpha', 'α motor'], ['gamma', 'γ motor'],
          ['inh', 'Inhibitory interneuron'], ['exc', 'Excitatory interneuron'], ['umn', 'Descending drive']]
flows = []
def fl(key, kind, n, when, unless=None, mods=None, sp=130, pts=None):
    pts = pts or F[key]
    f = dict(d=P(pts), len=plen(pts), speed=sp, r=6, base={kind: n}, when=when)
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
fl('umn', 'umn', 3, None, unless=UMNCUT, mods=[dict(when=O('gamma'), add={'umn': 2}), dict(when=O('infant'), set={'umn': 1})])
fl('cst_g', 'umn', 3, O('gamma'))
fl('cst_i', 'umn', 1, DEF + O('tap', 'recip', 'renshaw', 'gamma', 'lmn', 'polio', 'sma', 'cauda', 'gto', 'withdraw', 'tetanus', 'infant'))
fl('ia_p', 'ia', 3, TAPPED, mods=[dict(when=O('gamma'), add={'ia': 2})])
fl('ia_c', 'ia', 3, TAPPED, unless=O('cauda'), mods=[dict(when=O('gamma'), add={'ia': 2})])
fl('ia_i', 'ia', 1, DEF + O('tap', 'recip', 'gamma', 'umn', 'tetanus'))
fl('in_h', 'inh', 2, DEF + O('tap', 'recip', 'gamma'))
fl('ib', 'ib', 4, O('gto'))
fl('ib_i', 'inh', 3, O('gto'))
fl('pain', 'pain', 4, O('withdraw'))
fl('e_h', 'exc', 2, O('withdraw'))
fl('comm', 'exc', 3, O('withdraw'))
fl('gam', 'gamma', 1, DEF + O('tap', 'recip', 'renshaw', 'umn', 'tetanus'), mods=[])
fl('gam', 'gamma', 4, O('gamma'))
ALPHA_ON = TAPPED + O('gto')
alpha_mods = [dict(when=O('umn', 'tetanus', 'gamma'), add={'alpha': 2}), dict(when=O('als', 'gto'), set={'alpha': 1})]
fl('aq_c', 'alpha', 2, ALPHA_ON, unless=O('shock', 'polio', 'sma', 'cauda'), mods=alpha_mods)
fl('aq_p', 'alpha', 3, ALPHA_ON, unless=O('shock', 'polio', 'sma', 'cauda', 'lmn'), mods=alpha_mods)
fl('ah_c', 'alpha', 2, O('withdraw', 'tetanus'))
fl('ah_p', 'alpha', 3, O('withdraw', 'tetanus'))
fl('aqr', 'alpha', 3, O('withdraw'))
fl('ren', 'alpha', 1, O('renshaw'), sp=60)
fl('ren_q', 'inh', 1, O('renshaw'), sp=40)
fl('ren_h', 'inh', 1, O('renshaw'), sp=40)

# ════════ sites (tap targets) ════════
sites = [
  dict(x=600, y=1150, n=[0, -1], w=20, t='rec', l='Muscle spindle', s='senses length · Ia, II out · γ in', ions=[['ia', 'in', 1]], reach=18,
       lx=670, ly=1062, la='start', c='stretchrec', when=TAPPED, boost=O('gamma'), sfx=dict(boost=' — sensitized')),
  dict(x=600, y=1150, n=[0, -1], w=20, t='rec', l='Muscle spindle', s='senses length · Ia, II out · γ in', ions=[], lx=670, ly=1062, la='start',
       c='stretchrec', unless=TAPPED),
  dict(x=490, y=1150, n=[0, -1], w=20, t='rec', l='Golgi tendon organ', s='senses tension · Ib out', ions=[['ib', 'in', 1]], reach=18,
       lx=420, ly=1010, la='middle', c='stretchrec', need=O('gto'), closed='quiet', sfx={}),
  dict(x=700, y=1124, n=[1, 0], w=14, t='rec', l='', s='', ions=[['alpha', 'in', 1]], reach=16, c='motorunit', aria='Neuromuscular junction — motor unit',
       when=ALPHA_ON, unless=O('shock', 'polio', 'sma', 'cauda', 'lmn')),
  dict(x=1075, y=770, n=[0, 1], w=44, t='rec', l='', s='', ions=[], c='spinalcirc', aria='Renshaw cell', block=O('tetanus')),
  dict(x=1170, y=700, n=[0, -1], w=28, t='rec', l='', s='', ions=[], c='recipinhib', aria='Ia inhibitory interneuron', block=O('tetanus')),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Ia firing (spindle)', mods=[R(O('tap', 'recip', 'gamma'), 1)]),
  dict(l='Ib firing (tendon organ)', mods=[R(O('gto'), 1)]),
  dict(l='Stretch reflexes', mods=[R(O('tap', 'recip', 'renshaw'), 0), R(O('gamma', 'umn', 'als', 'tetanus'), 1),
                                   R(O('shock', 'lmn', 'polio', 'sma', 'cauda'), -1)]),
  dict(l='Muscle tone', mods=[R(O('umn', 'tetanus'), 1), R(O('shock', 'lmn', 'polio', 'sma', 'cauda'), -1)]),
  dict(l='Muscle bulk', mods=[R(O('umn'), 0), R(O('lmn', 'polio', 'sma', 'als'), -1)]),
  dict(l='Fasciculations', mods=[R(O('umn'), 0), R(O('lmn', 'polio', 'sma', 'als'), 1)]),
  dict(l='Babinski (toe up)', mods=[R(O('umn', 'infant'), 1), R(O('lmn', 'polio', 'sma'), 0)]),
]

notes = {
  '': 'One lumbar segment (L2–L4) wired to the patellar reflex: the tested leg on the left, the opposite leg on the right, '
      'the brain’s drive coming down from above. Pick a reflex circuit or a lesion and read the signs: ↑ more or present, '
      '↓ less or lost, ↔ normal or absent, – not graded by the sources.',
  'rx:tap': 'Stretch (myotatic) reflex — the knee jerk. Tapping the patellar tendon stretches the quadriceps spindles; their Ia '
            'fibers, among the fastest in the body, excite the quadriceps α motor neurons directly — one synapse — and the leg '
            'kicks. A normal jerk is graded 2+.',
  'rx:recip': 'Reciprocal inhibition. The same Ia fibers also excite Ia inhibitory (glycinergic) interneurons, which inhibit the '
              'hamstring motor neurons — the antagonist relaxes while the quadriceps contracts, so the reflex is not opposed.',
  'rx:gto': 'Golgi tendon reflex (inverse myotatic, two synapses). Rising tension fires the tendon organ’s Ib fibers, which excite '
            'an inhibitory interneuron that switches off the same muscle’s α motor neurons. At extreme tension the whole muscle '
            'lets go — the lengthening reaction, protecting the tendon; it is also what collapses a spastic limb’s resistance '
            '(clasp-knife).',
  'rx:withdraw': 'Flexor (withdrawal) reflex with crossed extension. Pain fibers (Aδ, C) from the foot drive many interneurons: '
                 'this leg’s flexors contract and its extensors relax, while commissural interneurons make the opposite leg '
                 'extend about 0.2–0.5 s later to bear the weight. Afterdischarge holds the limb away after the stimulus ends.',
  'rx:renshaw': 'Renshaw cells — recurrent inhibition. A collateral of each α motor axon, given off just after it leaves the cell '
                'body, excites a glycinergic Renshaw cell that inhibits that motor neuron and its neighbors. This lateral '
                'inhibition focuses the motor signal; descending fibers also drive Renshaw cells, and their loss helps cause clonus.',
  'rx:gamma': 'γ drive turned up. The brainstem’s bulboreticular facilitatory region fires γ motor neurons; the spindle’s '
              'intrafusal fibers contract at both ends and stretch its middle, so Ia fibers fire more and the stretch reflex '
              'grows more sensitive. Normally α and γ fire together (coactivation) so the spindle keeps signaling as the muscle '
              'shortens.',
  'rx:shock': 'Spinal shock — the first days to weeks after an acute cord transection above this segment. The cord loses its '
              'tonic descending excitation, so every reflex below the level falls silent: flaccid, areflexic limbs, a sudden '
              'fall in blood pressure and no bladder or bowel reflexes. Stretch reflexes come back first and may become '
              'hyperactive — the UMN picture.',
  'rx:umn': 'Upper motor neuron lesion, weeks on (cortex, internal capsule, or the cord above this level). The reflex arc is '
            'intact but has lost its descending control, including the drive to the Ia inhibitory interneurons and Renshaw '
            'cells: spastic weakness, ↑ tone, brisk jerks, clonus, clasp-knife resistance and a Babinski sign — no atrophy, '
            'no fasciculations.',
  'rx:lmn': 'Lower motor neuron lesion — here the motor root; the anterior horn cell or the peripheral nerve gives the same '
            'picture. The reflex arc itself is broken: flaccid weakness, ↓ tone, reduced or absent reflexes, then atrophy with '
            'fasciculations or fibrillations. The plantar response stays down-going.',
  'rx:polio': 'Poliomyelitis: poliovirus, spread fecal–oral, reaches the cord through the blood and destroys anterior horn cells. '
              'A fever with meningitis symptoms is followed by asymmetric flaccid paralysis, hyporeflexia and later muscle '
              'wasting — pure lower motor neuron, sensation spared; respiratory muscle involvement can be fatal.',
  'rx:sma': 'Spinal muscular atrophy type 1 (Werdnig-Hoffmann): autosomal recessive loss of SMN1, so anterior horn cells die. A '
            '“floppy baby” with symmetric weakness, marked hypotonia and tongue fasciculations — lower motor neuron signs only; '
            'untreated, fatal by about age 2.',
  'rx:cauda': 'Cauda equina syndrome: the lumbosacral roots below the end of the cord (L1–L2) are compressed — dorsal and ventral '
              'roots alike. Asymmetric flaccid (LMN) leg weakness with lost reflexes, radicular back pain, saddle anesthesia, '
              'bladder and bowel dysfunction: a surgical emergency. A conus medullaris lesion gives symmetric weakness with UMN signs.',
  'rx:als': 'Amyotrophic lateral sclerosis: upper motor neurons (corticospinal tracts) and lower motor neurons (anterior horns, '
            'brainstem nuclei) degenerate together. Spastic weakness, hyperreflexia and clonus sit beside atrophy and '
            'fasciculations, with bulbar palsy; no sensory or bowel/bladder loss. Riluzole and edaravone slow it.',
  'rx:tetanus': 'Tetanus: tetanospasmin travels back up motor axons into the cord and cleaves synaptobrevin in Renshaw cells and '
                'other inhibitory interneurons, so GABA and glycine are not released. Motor neurons fire unchecked — spastic '
                'paralysis with hyperreflexia, trismus, risus sardonicus and opisthotonos.',
  'rx:infant': 'Newborn: stroking the lateral sole lifts the big toe — a Babinski sign that is normal at this age, because the '
               'corticospinal tract is not yet fully myelinated. It disappears as the tract matures; in an adult the same sign '
               'points to an upper motor neuron lesion.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='rx', label='Reflex circuit or lesion — pick one', type='one', options=[
      ['tap', 'Stretch reflex (knee jerk)', 'stretchrec'], ['recip', 'Reciprocal inhibition', 'recipinhib'],
      ['gto', 'Golgi tendon reflex', 'stretchrec'], ['withdraw', 'Withdrawal + crossed extension', 'spinalcirc'],
      ['renshaw', 'Renshaw cells', 'spinalcirc'], ['gamma', 'γ drive up', 'motorunit'],
      ['shock', 'Spinal shock (acute)', 'spinalshock'], ['umn', 'UMN lesion (chronic)', 'umnlmn'],
      ['lmn', 'LMN lesion (motor root)', 'umnlmn'], ['polio', 'Polio', 'polio'], ['sma', 'SMA (floppy baby)', 'sma'],
      ['cauda', 'Cauda equina', 'caudaequina'],
      ['als', 'ALS — both', 'als'], ['tetanus', 'Tetanus', 'tetanus'], ['infant', 'Newborn — Babinski', 'umnlmn']],
      sections=[['Reflex circuits', ['tap', 'recip', 'gto', 'withdraw', 'renshaw', 'gamma']],
                ['Upper motor neuron', ['shock', 'umn']],
                ['Lower motor neuron', ['lmn', 'polio', 'sma', 'cauda']],
                ['Both, toxin, or normal', ['als', 'tetanus', 'infant']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 130, 136, 461, 520, 523, 543–544 · Guyton ch 55 · Costanzo ch 3 · Fundamental Neuroscience ch 4, 9, 24, 25, 33 · Robbins ch 8, 28')

# ════════ the one new card: no card covers spinal shock (32 mentions in the question bank) ════════
card('spinalshock', 'Spinal shock', 'dz', 'rfUmn', 'The silent cord just after an acute transection', 0,
     'When the cord is suddenly transected, the segments below lose the tonic excitation they normally get from the '
     'reticulospinal, vestibulospinal and corticospinal tracts, and <b>all cord reflexes fall silent</b>. In humans the '
     'spinal neurons regain their excitability over weeks to months, and some reflexes may end up hyperexcitable.',
     ['Below the level: <b>flaccid</b> weakness and <b>areflexia</b>, although the lesion is an upper motor neuron one',
      'Arterial pressure falls at once (sympathetic activity nearly abolished) and recovers within days',
      'Sacral reflexes for bladder and bowel are suppressed for the first weeks',
      'Recovery: stretch reflexes first, then flexor, postural and stepping reflexes; the spastic, hyperreflexic UMN picture follows'],
     ['—'],
     ['Acute cord injury: flaccid and areflexic first, spastic later'],
     [GY55, FN25],
     ['—'],
     ['spinal shock', 'resolution of spinal shock', 'spinal shock resolves', 'period of spinal shock', 'phase of spinal shock'])

MAP = dict(
  id='reflexsim', title='Spinal Reflexes & Motor Neurons in Motion', topic='neuro', after='motorctl',
  sub='The patellar reflex arc in one lumbar segment — spindle and Ia, Golgi tendon organ and Ib, reciprocal and Renshaw '
      'inhibition, withdrawal with crossed extension, γ drive — then the lesions that change it: spinal shock, upper and lower '
      'motor neuron, polio, SMA, cauda equina, ALS, tetanus and the newborn’s Babinski. Read reflexes, tone, bulk, '
      'fasciculations and the toe. Tap a pin for its card',
  w=3500, h=2260,
  fa='130, 136, 461, 520, 523, 543, 544', src=SRC,
  lanes=[('rfArc', 'Reflex arc', 'glycolysis'), ('rfUmn', 'Upper motor neuron', 'ppp'), ('rfLmn', 'Lower motor neuron', 'tca'),
         ('rfDz', 'Diseases & toxins', 'glycogen')],
  comps=[],
  nodes=[
    ('rf1', 'Muscle spindle · tendon organ', 2640, 1640, 'rfArc', 'Ia, II length · Ib tension', ['stretchrec'], 'hub'),
    ('rf2', 'α & γ motor neurons', 2640, 1720, 'rfArc', 'final common path · coactivation', ['motorunit']),
    ('rf3', 'Reciprocal inhibition', 2640, 1800, 'rfArc', 'Ia interneuron ⊣ antagonist', ['recipinhib']),
    ('rf4', 'Renshaw · withdrawal reflex', 2640, 1880, 'rfArc', 'recurrent inhibition · crossed extension', ['spinalcirc']),
    ('rf5', 'Reflexes & root levels', 2640, 1960, 'rfArc', 'S1 · L2–L4 · C5–C6 · C6–C8', ['reflexroots']),
    ('rf6', 'Corticospinal tract', 2640, 2040, 'rfUmn', 'crosses at the pyramids', ['csttract', 'bsmotor']),
    ('rf7', 'UMN vs LMN signs', 2640, 2120, 'rfUmn', 'everything up · everything lowered', ['umnlmn', 'weakloc'], 'hub'),
    ('rf8', 'Spinal shock', 3110, 1640, 'rfUmn', 'flaccid first, spastic later', ['spinalshock', 'autodysreflexia']),
    ('rf9', 'Polio · SMA', 3110, 1720, 'rfLmn', 'anterior horn cells', ['polio', 'sma']),
    ('rf10', 'Cauda equina · conus', 3110, 1800, 'rfLmn', 'roots below L1–L2', ['caudaequina']),
    ('rf11', 'ALS', 3110, 1880, 'rfDz', 'UMN + LMN, sensation spared', ['als']),
    ('rf12', 'Tetanus toxin', 3110, 1960, 'rfDz', 'Renshaw cells silenced', ['tetanus']),
    ('rf13', 'Newborn Babinski', 3110, 2040, 'rfDz', 'primitive reflexes fade', ['milestones']),
  ],
  panels=[
    (2420, 900, 1000, 'Reflexes and root levels (First Aid p. 523; Fund. Neurosci. ch 33)', [
      ('Biceps · brachioradialis', 'C5–C6'), ('Triceps', 'C6–C8'), ('Patellar', 'L2–L4 (femoral nerve)'),
      ('Achilles', 'S1–S2 (tibial nerve)'), ('Cremasteric · anal wink', 'L1–L2 · S3–S4'),
      ('Grades', '0 absent · 1+ low · 2+ normal · 3+ brisk · 4+ clonus')]),
    (2420, 1120, 1000, 'Three cord reflexes (Costanzo ch 3)', [
      ('Stretch (knee jerk)', '1 synapse · Ia · the stretched muscle contracts'),
      ('Golgi tendon (clasp-knife)', '2 synapses · Ib · the tensed muscle relaxes'),
      ('Flexor withdrawal', 'many synapses · pain fibers · flexion here, extension opposite')]),
    (2420, 1300, 1000, 'UMN vs LMN lesion (First Aid p. 543)', [
      ('Reflexes · tone', 'UMN ↑ · LMN ↓'), ('Atrophy · fasciculations', 'LMN only'),
      ('Babinski · clasp-knife spasticity', 'UMN only'), ('Paralysis', 'UMN spastic · LMN flaccid')]),
  ],
  dyn=dyn,
)
