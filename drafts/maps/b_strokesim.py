# m55 — Stroke Territory Simulator (dynamic map, kit data)
# The cerebral hemisphere three ways — lateral surface, medial surface and a coronal slice through the internal capsule and
# thalamus — with its arterial territories coloured (ACA, MCA superior and inferior divisions, PCA, the deep lenticulostriate
# and anterior choroidal territory, the border zones), the arterial tree with blood flowing to each territory, and the patient
# below: a weakness figure, a sensory figure, both visual fields, a language box, a clock-drawing box and other signs. One `one`
# switch in four sections (anterior circulation · posterior circulation · deep / lacunar · watershed) picks a stroke: the
# artery gets its ✕ and its blood stops there, the territory turns red, the body parts weaken or go numb, the fields go dark,
# and seven readouts give the direction (↓ lost or weak · ↑ present · ↔ normal · – not given by the sources).
# Neighbours: stemsim (brainstem syndromes), visfield (the whole visual pathway), cordsim, bleedsim, the static maps stroke and
# brainvessels. This map is about the cortical and deep TERRITORIES of the cerebrum and the deficit each one gives.
#
# Sources (all read in the corpus; U+00A0 / U+00AD normalized):
#   First Aid 2025 p. 513 (homunculus; cortical distribution: ACA anteromedial surface, MCA lateral surface, PCA posterior and
#     inferior surfaces; watershed: cortical border zones ACA–MCA and PCA–MCA, internal border zones between the superficial
#     and deep MCA territories; severe hypoperfusion: ACA–MCA watershed = proximal upper extremity weakness sparing the lower
#     extremities, "man-in-a-barrel"; PCA–MCA watershed = higher-order visual dysfunction) · p. 524 (frontal eye fields: eyes
#     look toward the lesion, away from the hemiplegia, seen in MCA stroke; dominant parietal = Gerstmann; nondominant parietal
#     = hemispatial neglect) · p. 525 (hypoxic stroke from systemic hypoperfusion, common during cardiovascular surgery, affects
#     watershed areas; embolic: atrial fibrillation, carotid stenosis) · p. 526 (effects of strokes: ACA = motor and sensory
#     cortices of the lower limb → contralateral paralysis and sensory loss of the lower limb, urinary incontinence; MCA = upper
#     limb and face, Wernicke (temporal) and Broca (frontal) areas → contralateral paralysis and sensory loss of the lower face
#     and upper limb, aphasia if dominant (usually left), hemineglect if nondominant (usually right); Wernicke aphasia with a
#     right superior quadrant field defect from temporal lobe involvement; lenticulostriate = striatum, internal capsule →
#     contralateral paralysis, absence of cortical signs (neglect, aphasia, visual field loss), pure motor stroke the most
#     common, lacunes from microatheroma and hyaline arteriosclerosis (lipohyalinosis) from unmanaged hypertension; PCA =
#     occipital lobe → contralateral hemianopia with macular sparing, alexia without agraphia (dominant, extending to the
#     splenium), prosopagnosia (nondominant)) · p. 528 (hypertensive bleeds from the same lenticulostriate vessels) · p. 529
#     (thalamic pain syndrome after thalamic lesions, may be lenticulostriate occlusion, contralateral; aphasias: Broca inferior
#     frontal gyrus, nonfluent, comprehension intact, insight kept; Wernicke superior temporal gyrus, fluent, comprehension
#     impaired, no insight; conduction = arcuate fasciculus, repetition; global = Broca + Wernicke) · p. 557 (Meyer loop in
#     the temporal lobe → contralateral upper quadrantanopia; visual cortex / PCA → hemianopia with macular sparing).
#   Fundamental Neuroscience ch 8 (ACA A4–A5 → lower-extremity areas of the somatomotor and somatosensory cortex; MCA superior
#     and inferior trunks serve cortex above and below the lateral fissure, M4 → trunk, upper extremity and face areas; M1 gives
#     the lenticulostriates; anterior choroidal along the optic tract → visual deficits + weakness of the opposite upper and
#     lower extremities; PCA P4 calcarine → contralateral homonymous hemianopia; border zones between ACA/MCA and MCA/PCA, ~10%
#     of infarcts, hypotension or embolic showers; posterior watershed → partial visual loss with language problems) · ch 15
#     (anterior choroidal syndrome; thalamogeniculate strokes → total or dissociated sensory loss, later Dejerine-Roussy) ·
#     ch 16 (lenticulostriates → genu and most of the posterior limb of the internal capsule; anterior choroidal → inferior
#     posterior limb, optic tract, Meyer loop: homonymous hemianopia + hemiparesis of upper and lower extremities) · ch 18
#     (lateral thalamic VPL/VPM lesions → loss of cutaneous and position sense) · ch 20 (calcarine artery; macular sparing from
#     MCA collaterals to the caudal visual cortex; Meyer loop → contralateral superior quadrantanopia; Meyer loop fibres served by
#     MCA branches; alexia without agraphia = splenium + adjacent occipital lesion, can write but cannot read) · ch 25 (capsular
#     infarcts: contralateral upper and lower extremity weakness, corticonuclear fibres in the genu → lower face) · ch 28 (frontal
#     eye field in the caudal middle frontal gyrus) · ch 32 (dominant = left in ~95%; Broca areas 44/45, nonfluent, agraphia,
#     frustration, from frontal MCA branches, with contralateral lower face and upper extremity weakness; Wernicke from temporal
#     and parietal MCA branches, fluent paraphasic speech, alexia, agraphia, little insight; global aphasia from left ICA or
#     proximal MCA occlusion; MCA superior trunk → trunk/upper extremity/head areas of the motor and sensory cortex, inferior
#     trunk → primary auditory cortex; pericentral aphasias from watershed infarcts, milder, repetition kept; right parietal →
#     contralateral neglect, clock drawing, asomatognosia, dressing and constructional apraxia, lack of concern).
#   Robbins ch 28 (lacunes in putamen, globus pallidus, thalamus, internal capsule, deep white matter, caudate, pons; < 15 mm;
#     hyaline arteriolosclerosis; deficits set by the anatomic distribution of the damage; border zone infarcts: ACA–MCA zone at
#     greatest risk, wedge-shaped, often bilateral, after severe hypotensive episodes, most often after resuscitation from
#     cardiac arrest).
#   Bootcamp.com Neurology — cerebrovascular accidents (supporting only, kept out of `src`: pure motor = posterior limb, face +
#     arm + leg; pure sensory = VPL/VPM thalamus, face + arm + leg; watershed hypoperfusion bilateral).
# Cut for lack of support in the corpus: ataxic hemiparesis and dysarthria–clumsy hand (no hit in FA, any textbook or Bootcamp);
#   Gerstmann as its own territory option (FA p. 524 names the area, no source names the branch — kept as a panel row); abulia
#   in ACA stroke (Bootcamp only); leg strength in MCA stem occlusion (no source says — "–"); face, sensation, language for the
#   anterior choroidal syndrome; the "man-in-a-barrel" face and sensation; strength and sensation in PCA strokes ("–", no source
#   states them); conduction aphasia as a territory option (FA gives no artery); amaurosis fugax, ACom and PCom aneurysms and the
#   basilar tip (not cortical territories — aneurysms are on brainvessels/stemsim/visfield). Fundamental Neuroscience ch 8
#   describes a ONE-sided anterior watershed infarct as contralateral LEG weakness with expressive language deficits; the map's
#   watershed option is First Aid's bilateral hypotensive "man in a barrel" (Robbins: often bilateral, after hypotension), and
#   the new card states both.
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

FN8, FN15, FN16, FN18, FN20, FN25, FN28, FN32 = (full('Fundamental Neuroscience', c) for c in (8, 15, 16, 18, 20, 25, 28, 32))
RB28 = full('Robbins', 28)
SRC = [FN8, FN32, FN16, FN20, FN25, FN15, FN18, FN28, RB28]

O = lambda *k: ['st:' + x for x in k]
DEF = ['!st:*']
RIGHT = O('mcand', 'pcar')                       # right (nondominant) hemisphere strokes
M1BLK = O('mcastem', 'mcand')                    # the whole MCA (stem) is shut
SUPBLK = O('mcasup') + M1BLK
INFBLK = O('mcainf') + M1BLK
PCABLK = O('pcal', 'pcar')
WS = O('wsant', 'wspost')

def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))

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
RED = 'fill:var(--bad);fill-opacity:.42'
def box(x0, y0, x1, y1): add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')
def tint(col, op=.2): return f'fill:var({col});fill-opacity:{op}'

text('Stroke territories — which artery, which deficit', 160, 70, 'dyn-big')
text('the hemisphere three ways, the arteries with blood flowing, and the patient below · pick a stroke on the right', 160, 92, 'dyn-cap')

# ════════ 1. lateral surface ════════
box(150, 115, 1110, 770)
text('Lateral surface — left hemisphere (dominant)', 176, 148, 'nf-l1', unless=RIGHT + O('wsant'))
text('Lateral surface — right hemisphere (nondominant)', 176, 148, 'nf-l1', when=RIGHT)
text('Lateral surface — both hemispheres (left shown)', 176, 148, 'nf-l1', when=O('wsant'))
text('front to the left', 176, 166, 'dyn-cap', unless=RIGHT)
text('drawn like the left, front to the left', 176, 166, 'dyn-cap', when=RIGHT)
LAT = ('M215 430 C205 285 360 185 560 172 C760 160 960 220 1035 345 C1080 420 1070 520 1010 575 C960 615 880 625 820 612 '
       'C770 640 690 668 600 664 C520 662 455 640 425 600 C405 570 405 540 420 520 C360 528 290 520 250 492 C228 474 216 455 215 430 Z')
FISS = 'M425 515 C520 480 640 455 790 420 C830 410 880 400 940 400'
ACA_L = 'M240 300 C380 215 560 200 700 200 C820 205 930 240 1000 300 L1110 300 L1110 100 L150 100 L150 300 Z'
ACA_EDGE = 'M240 300 C380 215 560 200 700 200 C820 205 930 240 1000 300'
PCA_L = 'M960 250 C930 380 900 500 860 560 C800 610 700 640 560 655 L560 800 L1110 800 L1110 250 Z'
PCA_EDGE = 'M960 250 C930 380 900 500 860 560 C800 610 700 640 560 655'
SUP_L = f'M150 100 L1110 100 L1110 400 L940 400 C880 400 830 410 790 420 C640 455 520 480 425 515 L150 515 Z'
INF_L = f'M150 800 L150 515 L425 515 C520 480 640 455 790 420 C830 410 880 400 940 400 L1110 400 L1110 800 Z'
# cerebellum and brainstem behind/below
add('<path d="M700 640 L760 640 L772 752 L716 752 Z" class="dyn-cell"/>')
add('<path d="M820 622 C832 690 912 728 986 712 C1046 698 1062 640 1022 598 C962 620 882 628 820 622 Z" class="dyn-cell"/>'
    '<path d="M850 650 C900 680 960 682 1010 660 M842 676 C900 704 960 704 1000 690" class="dyn-line" style="opacity:.4"/>')
text('cerebellum', 935, 740, 'dyn-cap', 'middle')
add(f'<clipPath id="sk-lat"><path d="{LAT}"/></clipPath><g clip-path="url(#sk-lat)">'
    f'<path d="{LAT}" class="dyn-cell"/>'
    f'<path d="{SUP_L}" style="{tint("--dk1")}"/><path d="{INF_L}" style="{tint("--dk11")}"/></g>')
add(f'<g clip-path="url(#sk-lat)"><path d="{SUP_L}" style="{RED}"/></g>', when=SUPBLK)
add(f'<g clip-path="url(#sk-lat)"><path d="{INF_L}" style="{RED}"/></g>', when=INFBLK)
add(f'<g clip-path="url(#sk-lat)"><path d="{ACA_L}" style="fill:var(--dyn-cell)"/><path d="{ACA_L}" style="{tint("--dk3", .3)}"/>'
    f'<path d="{PCA_L}" style="fill:var(--dyn-cell)"/><path d="{PCA_L}" style="{tint("--dk7", .3)}"/></g>')
add(f'<g clip-path="url(#sk-lat)"><path d="{ACA_L}" style="{RED}"/></g>', when=O('aca'))
add(f'<g clip-path="url(#sk-lat)"><path d="{PCA_L}" style="{RED}"/></g>', when=PCABLK)
# border zones: dashed bands along the territory edges, red when they infarct
add(f'<g clip-path="url(#sk-lat)"><path d="{ACA_EDGE}" class="dyn-dash" style="stroke-width:3"/><path d="{PCA_EDGE}" class="dyn-dash" style="stroke-width:3"/></g>')
add(f'<g clip-path="url(#sk-lat)"><path d="{ACA_EDGE}" style="fill:none;stroke:var(--bad);stroke-width:34;stroke-opacity:.5"/></g>', when=O('wsant'))
add(f'<g clip-path="url(#sk-lat)"><path d="{PCA_EDGE}" style="fill:none;stroke:var(--bad);stroke-width:34;stroke-opacity:.5"/></g>', when=O('wspost'))
add(f'<path d="{LAT}" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:4"/>'
    f'<path d="{FISS}" class="dyn-line" style="stroke-width:5"/>'
    '<path d="M690 168 C680 230 655 300 640 340 C628 380 612 420 600 458" class="dyn-line" style="stroke-width:3.5"/>'
    '<path d="M664 172 C654 232 630 300 615 340 C603 380 588 420 576 452" style="fill:none;stroke:var(--dk5);stroke-width:12;stroke-opacity:.45;stroke-linecap:round"/>')
text('motor strip', 700, 150, 'nf-l2', 'middle')
text('leg over the top', 662, 222, 'dyn-cap', 'end')
text('arm', 616, 318, 'nf-l2', 'end')
text('face', 584, 414, 'nf-l2', 'end')
def dot(x, y, col='--ink-2'): add(f'<circle cx="{x}" cy="{y}" r="9" style="fill:var({col});stroke:var(--surface);stroke-width:2"/>')
dot(470, 470); text('Broca', 455, 476, 'nf-l1', 'end')
dot(770, 465); text('Wernicke', 786, 471, 'nf-l1')
dot(505, 300); text('frontal eye field', 490, 306, 'nf-l2', 'end')
text('lateral fissure', 470, 548, 'nf-l2')
text('frontal', 330, 390, 'dyn-cap', 'middle')
text('parietal', 845, 300, 'dyn-cap', 'middle')
text('temporal', 640, 610, 'dyn-cap', 'middle')
text('occipital', 985, 455, 'dyn-cap', 'middle')
text('ACA–MCA border zone', 860, 196, 'nf-l2', when=O('wsant'))
text('MCA–PCA border zone', 960, 560, 'nf-l2', 'middle', when=O('wspost'))

# ════════ 2. medial surface ════════
box(1130, 115, 2340, 770)
text('Medial surface — same hemisphere', 1156, 148, 'nf-l1')
text('front to the left', 1156, 166, 'dyn-cap')
MED = ('M1215 440 C1205 290 1370 185 1570 172 C1780 160 1980 220 2060 350 C2105 430 2095 520 2040 575 C1990 618 1900 628 1830 615 '
       'C1770 645 1680 668 1590 664 C1500 660 1440 640 1410 600 C1380 560 1300 540 1260 510 C1232 490 1216 466 1215 440 Z')
ACA_M = 'M1130 100 L1950 100 L1975 250 L1900 470 L1700 540 L1400 575 L1130 575 Z'
PCA_M = 'M1975 250 L2340 250 L2340 800 L1130 800 L1130 640 L1420 612 L1700 560 L1900 470 Z'
add('<path d="M1700 560 L1760 560 L1772 752 L1716 752 Z" class="dyn-cell"/>'
    '<path d="M1820 622 C1832 690 1912 728 1986 712 C2046 698 2062 640 2022 598 C1962 620 1882 628 1820 622 Z" class="dyn-cell"/>')
add(f'<clipPath id="sk-med"><path d="{MED}"/></clipPath><g clip-path="url(#sk-med)"><path d="{MED}" class="dyn-cell"/>'
    f'<path d="{ACA_M}" style="{tint("--dk3", .3)}"/><path d="{PCA_M}" style="{tint("--dk7", .3)}"/></g>')
add(f'<g clip-path="url(#sk-med)"><path d="{ACA_M}" style="{RED}"/></g>', when=O('aca'))
add(f'<g clip-path="url(#sk-med)"><path d="{PCA_M}" style="{RED}"/></g>', when=PCABLK)
CC = ('M1430 430 C1460 335 1600 300 1740 308 C1850 316 1912 360 1906 410 C1892 444 1850 444 1830 420 C1800 382 1720 362 1640 364 '
      'C1540 368 1484 402 1474 440 C1462 470 1424 462 1430 430 Z')
add(f'<path d="{MED}" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:4"/>'
    f'<path d="{CC}" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:3"/>'
    '<path d="M1972 236 C1950 320 1925 400 1900 470" class="dyn-line" style="stroke-width:4"/>'
    '<path d="M1900 476 C1960 470 2020 466 2088 462" class="dyn-line" style="stroke-width:4"/>'
    '<path d="M1690 170 C1680 200 1672 230 1668 262" class="dyn-line" style="stroke-width:3.5"/>')
add('<path d="M1820 410 C1860 444 1900 440 1906 410" style="fill:var(--bad);fill-opacity:.55"/>', when=O('pcal'))
dot(1640, 222); text('paracentral lobule — leg and foot', 1656, 228, 'nf-l1')
text('corpus callosum', 1650, 345, 'nf-l2', 'middle')
text('splenium', 1920, 420, 'nf-l2', unless=O('pcal'))
text('parieto-occipital sulcus', 1990, 236, 'nf-l2')
text('calcarine cortex — vision', 1990, 500, 'nf-l1', 'middle')
text('medial frontal — bladder control', 1260, 470, 'nf-l2', when=O('aca'))
text('splenium involved', 1920, 420, TAG, when=O('pcal'))
text('brainstem', 1740, 760, 'dyn-cap', 'middle')

# legend
LEG = [('--dk3', 'ACA'), ('--dk1', 'MCA superior division'), ('--dk11', 'MCA inferior division'), ('--dk7', 'PCA'),
       ('--dk5', 'deep — lenticulostriate'), (None, 'border zone'), ('--bad', 'infarct')]
lx = 180
for col, lab in LEG:
    if col: add(f'<rect x="{lx}" y="788" width="28" height="16" rx="4" style="fill:var({col});fill-opacity:{.42 if col == "--bad" else .35}"/>')
    else: add(f'<path d="M{lx} 796 H{lx + 28}" class="dyn-dash" style="stroke-width:3"/>')
    text(lab, lx + 36, 801, 'nf-l2')
    lx += 64 + int(len(lab) * 7.2)

# ════════ 3. coronal slice — the deep territory ════════
box(150, 830, 1110, 1450)
text('Coronal slice — the deep territory', 176, 862, 'nf-l1')
text('midline on the right', 176, 880, 'dyn-cap')
COR = ('M1000 900 C820 892 600 920 430 1005 C290 1080 232 1180 262 1275 C288 1352 372 1402 470 1405 C560 1408 640 1380 700 1345 '
       'C760 1362 860 1360 1000 1335 Z')
add(f'<path d="{COR}" class="dyn-cell" style="stroke-width:4"/>')
add('<path d="M268 1196 C360 1190 470 1182 560 1172" class="dyn-line" style="stroke-width:5"/>'        # lateral fissure
    '<path d="M560 1046 C538 1094 543 1132 560 1172" class="dyn-line" style="stroke-width:6;opacity:.5"/>'  # insula
    '<path d="M1000 948 C930 944 860 958 800 990" style="fill:none;stroke:var(--line-2);stroke-width:18;stroke-linecap:round"/>'  # corpus callosum
    '<path d="M1000 972 C962 972 934 986 930 1004 C934 1022 962 1034 1000 1034 Z" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:2.5"/>'
    '<ellipse cx="896" cy="1010" rx="34" ry="28" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<ellipse cx="948" cy="1150" rx="50" ry="58" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M852 1040 C842 1100 852 1172 880 1232" style="fill:none;stroke:var(--surface-2);stroke-width:30;stroke-linecap:round"/>'
    '<path d="M700 1012 C648 1062 648 1162 700 1212 C762 1192 804 1122 794 1042 C772 1020 736 1010 700 1012 Z" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<ellipse cx="894" cy="1270" rx="22" ry="11" style="fill:var(--surface-2);stroke:var(--dk8);stroke-width:2.5"/>')
# the deep (lenticulostriate) territory, tinted
add('<path d="M700 1012 C648 1062 648 1162 700 1212 C762 1192 804 1122 794 1042 C772 1020 736 1010 700 1012 Z" style="fill:var(--dk5);fill-opacity:.22"/>'
    '<path d="M852 1040 C842 1100 852 1172 880 1232" style="fill:none;stroke:var(--dk5);stroke-width:30;stroke-opacity:.22;stroke-linecap:round"/>')
text('caudate', 896, 1015, 'nf-l2', 'middle')
text('thalamus', 948, 1130, 'nf-l2', 'middle')
text('lentiform', 722, 1100, 'nf-l2', 'middle')
text('nucleus', 722, 1116, 'nf-l2', 'middle')
text('ventricle', 1010, 1006, 'nf-l2')
text('insula', 574, 1080, 'nf-l2')
text('lateral fissure', 300, 1180, 'nf-l2')
text('temporal lobe', 470, 1350, 'dyn-cap', 'middle')
text('optic tract', 920, 1274, 'nf-l2')
add('<path d="M650 1000 L846 1070" class="dyn-line" style="stroke-width:1.6"/>')
text('internal capsule', 642, 1000, 'nf-l1', 'end')
text('posterior limb', 642, 1016, 'nf-l2', 'end')
# arteries in the slice
CA = dict(
  ica=[(930, 1448), (930, 1336)],
  m1=[(930, 1336), (860, 1306), (760, 1266), (640, 1252), (580, 1236), (560, 1186)],
  sup=[(560, 1186), (500, 1124), (420, 1066), (352, 1028)],
  inf=[(560, 1186), (470, 1234), (380, 1272), (318, 1292)],
  ls1=[(820, 1292), (832, 1220), (850, 1150), (858, 1080)],
  ls2=[(760, 1266), (762, 1200), (770, 1130), (775, 1062)],
  ls3=[(700, 1256), (692, 1190), (700, 1120), (715, 1062)],
  aca=[(930, 1336), (972, 1322), (992, 1290), (995, 1240), (995, 930)],
  ach=[(930, 1380), (904, 1356), (886, 1320), (888, 1286), (878, 1240)],
  thal=[(990, 1448), (986, 1330), (976, 1250), (960, 1200)],
)
for k, pts in CA.items():
    w = 5 if k.startswith('ls') or k in ('ach', 'thal') else 11
    add(f'<path d="{P(pts)}" style="fill:none;stroke:var(--dk2);stroke-width:{w};stroke-opacity:.35;stroke-linecap:round;stroke-linejoin:round"/>')
text('ICA', 944, 1440, 'nf-l1')
text('ACA', 1010, 1100, 'nf-l1')
text('MCA stem (M1) and its lenticulostriates', 650, 1300, 'nf-l2', 'middle')
text('anterior choroidal', 900, 1400, 'nf-l2', 'end')
text('from PCA', 1004, 1440, 'nf-l2')
# lesions in the slice
def blob(x, y, rx, ry, when): add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" style="fill:var(--bad);fill-opacity:.75;stroke:var(--bad);stroke-width:2"/>', when=when)
blob(858, 1120, 13, 20, O('lacmotor'))
blob(930, 1168, 16, 14, O('lacsens'))
add('<path d="M866 1196 C870 1220 878 1236 884 1246" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-opacity:.6;stroke-linecap:round"/>'
    '<ellipse cx="894" cy="1270" rx="22" ry="11" style="fill:var(--bad);fill-opacity:.6"/>', when=O('achor'))
add(f'<path d="{COR}" style="fill:none;stroke:var(--bad);stroke-width:0"/>')
# cortex of the slice: above the fissure = superior division, below = inferior division
add('<path d="M430 1005 C320 1066 262 1140 268 1196" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-opacity:.55;stroke-linecap:round"/>', when=SUPBLK)
add('<path d="M268 1196 C266 1300 340 1384 470 1402" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-opacity:.55;stroke-linecap:round"/>', when=INFBLK)
add('<path d="M1000 902 C900 896 800 902 700 920" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-opacity:.55;stroke-linecap:round"/>', when=O('aca'))
add('<path d="M700 920 C600 935 500 968 430 1005" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-opacity:.55;stroke-linecap:round"/>', when=O('wsant'))
CTAG = [('lacmotor', 'lacune in the posterior limb — the motor fibers'), ('lacsens', 'lacune in the lateral thalamus (VPL/VPM)'),
        ('achor', 'inferior posterior limb + optic tract'), ('wsant', 'the wedge between the ACA and MCA cortex'),
        ('aca', 'medial cortex over the top'), ('mcasup', 'cortex above the fissure'), ('mcainf', 'cortex below the fissure'),
        ('mcastem', 'cortex above and below the fissure'), ('mcand', 'cortex above and below the fissure')]
for k, s in CTAG:
    text(s, 176, 1432, TAG, when=O(k))

# ════════ 4. the arterial tree with blood flowing ════════
box(1130, 830, 2340, 1450)
text('Arteries — blood flowing to each territory', 1156, 862, 'nf-l1')
TV = dict(
  ica=[(1420, 1440), (1420, 1300)], aca=[(1420, 1300), (1300, 1220), (1300, 960)], m1=[(1420, 1300), (1640, 1300)],
  sup=[(1640, 1300), (1700, 1200), (1700, 960)], inf=[(1640, 1300), (1920, 1240), (1920, 960)],
  ls1=[(1490, 1300), (1490, 1222)], ls2=[(1540, 1300), (1540, 1222)], ls3=[(1590, 1300), (1590, 1222)],
  ach=[(1420, 1392), (1290, 1392), (1258, 1344)], bas=[(2240, 1440), (2240, 1300)], pca=[(2240, 1300), (2240, 960)],
  thal=[(2240, 1250), (2150, 1212)],
)
for k, pts in TV.items():
    w = 6 if k.startswith('ls') or k in ('ach', 'thal') else 14
    add(f'<path d="{P(pts)}" style="fill:none;stroke:var(--dk2);stroke-width:{w};stroke-opacity:.3;stroke-linecap:round;stroke-linejoin:round"/>')
add('<path d="M1420 1360 H2240" class="dyn-dash" style="stroke-width:3"/>')
BADGES = [(1300, 'ACA', 'leg · bladder', '--dk3', O('aca') + O('wsant')), (1700, 'MCA superior', 'face · arm · Broca', '--dk1', SUPBLK + O('wsant')),
          (1920, 'MCA inferior', 'Wernicke · Meyer loop', '--dk11', INFBLK + O('wspost')), (2240, 'PCA', 'vision · reading', '--dk7', PCABLK + O('wspost'))]
for x, t1, t2, col, hit in BADGES:
    add(f'<rect x="{x - 96}" y="892" width="192" height="64" rx="14" style="fill:var({col});fill-opacity:.25;stroke:var({col});stroke-width:2.5"/>')
    add(f'<rect x="{x - 96}" y="892" width="192" height="64" rx="14" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=hit)
    text(t1, x, 918, 'nf-l1', 'middle')
    text(t2, x, 938, 'nf-l2', 'middle')
text('ACA', 1284, 1090, 'nf-l1', 'end')
text('superior division', 1716, 1090, 'nf-l2')
text('inferior division', 1936, 1090, 'nf-l2')
text('PCA', 2256, 1090, 'nf-l1')
text('ICA', 1436, 1436, 'nf-l1')
text('basilar', 2256, 1436, 'nf-l1')
text('MCA stem (M1)', 1530, 1330, 'nf-l2', 'middle')
text('lenticulostriates', 1540, 1210, 'nf-l2', 'middle')
text('posterior communicating', 1830, 1352, 'dyn-cap', 'middle')
text('anterior choroidal', 1300, 1424, 'nf-l2', 'middle')
text('to the thalamus', 2140, 1200, 'nf-l2', 'end')
text('systemic pressure falls — every branch slows, the far ends starve first', 1760, 1410, TAG, 'middle', when=WS)

kinds = {'bl': ['blood', '--dk2']}
groups = []
flows = []
def fl(pts, n, when=None, unless=None, sp=120, r=6):
    f = dict(d=P(pts), len=plen(pts), speed=sp, r=r, base={'bl': n}, mods=[dict(when=WS, set={'bl': 1}, speed=.35)])
    if when: f['when'] = when
    if unless: f['unless'] = unless
    flows.append(f)
cut = lambda pts, y: pts[:-1] + [(pts[-1][0], y)]          # a vertical end segment that stops at the ✕
# tree
fl(TV['ica'], 2); fl(TV['bas'], 2)
fl(TV['aca'], 3, unless=O('aca')); fl(cut(TV['aca'], 1162), 2, when=O('aca'), sp=60)
fl(TV['m1'], 3, unless=M1BLK); fl([(1420, 1300), (1598, 1300)], 2, when=M1BLK, sp=60)
fl(TV['sup'], 3, unless=SUPBLK); fl(cut(TV['sup'], 1162), 2, when=O('mcasup'), sp=60)
fl(TV['inf'], 3, unless=INFBLK); fl(cut(TV['inf'], 1162), 2, when=O('mcainf'), sp=60)
fl(TV['ls1'], 1); fl(TV['ls3'], 1); fl(TV['ls2'], 1, unless=O('lacmotor'))
fl(TV['ach'], 1, unless=O('achor'))
fl(TV['pca'], 3, unless=PCABLK); fl(cut(TV['pca'], 1162), 2, when=PCABLK, sp=60)
fl(TV['thal'], 1, unless=O('lacsens'))
# coronal slice
fl(CA['ica'], 1); fl(CA['m1'], 2, unless=M1BLK)
fl(CA['sup'], 1, unless=SUPBLK); fl(CA['inf'], 1, unless=INFBLK)
fl(CA['ls1'], 1, unless=O('lacmotor')); fl(CA['ls2'], 1); fl(CA['ls3'], 1)
fl(CA['aca'], 2, unless=O('aca')); fl(CA['ach'], 1, unless=O('achor')); fl(CA['thal'], 1, unless=O('lacsens'))

# ════════ sites: tap targets on the arteries; the ✕ falls where the stroke is ════════
def site(x, y, n, c, aria, block):
    return dict(x=x, y=y, n=n, w=14, t='rec', l='', s='', ions=[], c=c, aria=aria, block=block)
sites = [
  site(1300, 1150, [-1, 0], 'acastroke', 'Anterior cerebral artery', O('aca')),
  site(1612, 1300, [0, -1], 'mcastroke', 'MCA stem (M1)', M1BLK),
  site(1700, 1150, [1, 0], 'mcastroke', 'MCA superior division', O('mcasup')),
  site(1920, 1150, [1, 0], 'aphasia', 'MCA inferior division', O('mcainf')),
  site(2240, 1150, [1, 0], 'pcastroke', 'Posterior cerebral artery', PCABLK),
  site(1540, 1250, [1, 0], 'lacunar', 'Lenticulostriate artery', O('lacmotor')),
  site(1330, 1392, [0, -1], 'carotidsys', 'Anterior choroidal artery', O('achor')),
  site(2196, 1231, [0, -1], 'thalamicpain', 'Thalamic branch of the PCA', O('lacsens')),
]

# ════════ 5. the patient: weakness and sensory figures ════════
box(150, 1470, 930, 2270)
text('The patient — they face you: their right side is on your left', 176, 1502, 'nf-l1')
HEADY = 1590
def limbs(cx):
    return dict(
      ar=[(cx - 70, 1676), (cx - 94, 1776), (cx - 106, 1876)], al=[(cx + 70, 1676), (cx + 94, 1776), (cx + 106, 1876)],
      arp=[(cx - 70, 1676), (cx - 94, 1776)], alp=[(cx + 70, 1676), (cx + 94, 1776)],
      lr=[(cx - 32, 1866), (cx - 38, 2016), (cx - 42, 2160)], ll=[(cx + 32, 1866), (cx + 38, 2016), (cx + 42, 2160)])
def figure(cx, lab):
    text(lab, cx, 1532, 'nf-l1', 'middle')
    L_ = limbs(cx)
    out = ''
    for k in ('ar', 'al', 'lr', 'll'):
        d = P(L_[k])
        out += (f'<path d="{d}" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:42;stroke-linecap:round;stroke-linejoin:round"/>'
                f'<path d="{d}" style="fill:none;stroke:var(--dyn-cell);stroke-width:36;stroke-linecap:round;stroke-linejoin:round"/>')
    out += (f'<rect x="{cx - 64}" y="1652" width="128" height="224" rx="30" class="dyn-cell"/>'
            f'<rect x="{cx - 14}" y="1630" width="28" height="26" class="dyn-cell" style="stroke-width:2"/>'
            f'<circle cx="{cx}" cy="{HEADY}" r="46" class="dyn-cell"/>')
    add(out)
    return L_
def paint(L_, keys, col, when):
    out = ''.join(f'<path d="{P(L_[k])}" style="fill:none;stroke:var({col});stroke-width:36;stroke-opacity:.55;stroke-linecap:round;stroke-linejoin:round"/>' for k in keys)
    add(out, when=when)
def lowface(cx, side, col, when):     # side -1 = their right (your left), +1 = their left
    r = 44
    d = (f'M{cx} {HEADY} L{cx - r} {HEADY} A{r} {r} 0 0 0 {cx} {HEADY + r} Z' if side < 0 else
         f'M{cx} {HEADY} L{cx} {HEADY + r} A{r} {r} 0 0 0 {cx + r} {HEADY} Z')
    add(f'<path d="{d}" style="fill:var({col});fill-opacity:.55"/>', when=when)
CW, CS = 330, 720
LW = figure(CW, 'Weakness')
LS = figure(CS, 'Sensory loss')
for cx in (CW, CS):
    add(f'<path d="M{cx - 16} {HEADY + 22} Q{cx} {HEADY + 30} {cx + 16} {HEADY + 22}" class="dyn-line" style="stroke-width:2.5"/>', unless=O('mcasup', 'mcastem', 'lacmotor'))
add(f'<path d="M{CW - 16} {HEADY + 28} Q{CW} {HEADY + 28} {CW + 16} {HEADY + 20}" class="dyn-line" style="stroke-width:2.5"/>', when=O('mcasup', 'mcastem', 'lacmotor'))
add(f'<path d="M{CS - 16} {HEADY + 22} Q{CS} {HEADY + 30} {CS + 16} {HEADY + 22}" class="dyn-line" style="stroke-width:2.5"/>', when=O('mcasup', 'mcastem', 'lacmotor'))
add(f'<path d="M{CW - 16} {HEADY + 20} Q{CW} {HEADY + 28} {CW + 16} {HEADY + 28}" class="dyn-line" style="stroke-width:2.5"/>', when=O('mcand'))
# eyes (pupils look toward the lesion in MCA strokes that take the frontal eye field)
def eyes(cx, dx, when=None, unless=None):
    s = ''.join(f'<circle cx="{cx + o}" cy="{HEADY - 8}" r="9" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2"/>'
                f'<circle cx="{cx + o + dx}" cy="{HEADY - 8}" r="4.5" style="fill:var(--ink)"/>' for o in (-17, 17))
    add(s, when=when, unless=unless)
EYEL = O('mcasup', 'mcastem')
eyes(CW, 0, unless=EYEL + O('mcand')); eyes(CW, 5, when=EYEL); eyes(CW, -5, when=O('mcand')); eyes(CS, 0)
text('eyes look toward the lesion', CW + 56, HEADY - 30, TAG, when=EYEL)
text('eyes look toward the lesion', CW - 56, HEADY - 30, TAG, 'end', when=O('mcand'))
# weakness: face, arm, leg (their right = your left, keys *r)
lowface(CW, -1, '--bad', O('mcasup', 'mcastem', 'lacmotor')); lowface(CW, 1, '--bad', O('mcand'))
paint(LW, ['ar'], '--bad', O('mcasup', 'mcastem', 'lacmotor', 'achor')); paint(LW, ['al'], '--bad', O('mcand'))
paint(LW, ['lr'], '--bad', O('aca', 'lacmotor', 'achor'))
paint(LW, ['arp', 'alp'], '--bad', O('wsant'))
# sensory loss
lowface(CS, -1, '--dk1', O('mcasup', 'mcastem', 'lacsens')); lowface(CS, 1, '--dk1', O('mcand'))
paint(LS, ['ar'], '--dk1', O('mcasup', 'mcastem', 'lacsens')); paint(LS, ['al'], '--dk1', O('mcand'))
paint(LS, ['lr'], '--dk1', O('aca', 'lacsens'))
for cx in (CW, CS):
    text('their right', cx - 46, 2200, 'dyn-cap', 'middle')
    text('their left', cx + 46, 2222, 'dyn-cap', 'middle')
BODY = [('aca', 'right leg weak and numb · face and arm spared'), ('mcasup', 'right lower face and arm weak and numb · leg spared'),
        ('mcainf', 'strength and sensation spared'), ('mcastem', 'right lower face and arm weak and numb'),
        ('mcand', 'left lower face and arm weak and numb · leg spared'), ('lacmotor', 'right face, arm and leg weak · sensation spared'),
        ('lacsens', 'right face, arm and leg numb · strength spared'), ('achor', 'right arm and leg weak'),
        ('wsant', 'both shoulders and upper arms weak · legs spared'), ('pcal', 'no limb finding is given by the sources'),
        ('pcar', 'no limb finding is given by the sources'), ('wspost', 'no limb finding is given by the sources')]
for k, s in BODY:
    text(s, 176, 2252, TAG, when=O(k))

# ════════ 6. visual fields ════════
box(960, 1470, 1490, 1810)
text('Visual fields — as each eye sees', 984, 1502, 'nf-l1')
FY, FR = 1630, 82
for cx, lab in ((1100, 'left eye'), (1350, 'right eye')):
    add(f'<circle cx="{cx}" cy="{FY}" r="{FR}" class="dyn-field"/>')
    rh = f'<path d="M{cx} {FY - FR} A{FR} {FR} 0 0 1 {cx} {FY + FR} Z" class="dyn-lost"/>'
    lh = f'<path d="M{cx} {FY - FR} A{FR} {FR} 0 0 0 {cx} {FY + FR} Z" class="dyn-lost"/>'
    ruq = f'<path d="M{cx} {FY} L{cx} {FY - FR} A{FR} {FR} 0 0 1 {cx + FR} {FY} Z" class="dyn-lost"/>'
    mac = f'<circle cx="{cx}" cy="{FY}" r="18" class="dyn-field" style="stroke:none"/>'
    add(rh, when=O('achor'))
    add(rh + mac, when=O('pcal'))
    add(lh + mac, when=O('pcar'))
    add(ruq, when=O('mcainf', 'mcastem'))
    add(f'<path d="M{cx - 7} {FY} H{cx + 7} M{cx} {FY - 7} V{FY + 7}" class="dyn-line" style="stroke-width:2"/>'
        f'<path d="M{cx} {FY - FR} V{FY + FR} M{cx - FR} {FY} H{cx + FR}" class="dyn-dash" style="stroke-width:1.2;opacity:.6"/>')
    text(lab, cx, FY + FR + 24, 'nf-l2', 'middle')
FIELD = [('mcainf', 'right upper quadrantanopia — the Meyer loop'), ('mcastem', 'right upper field lost — the Meyer loop'),
         ('pcal', 'right homonymous hemianopia, macula spared'), ('pcar', 'left homonymous hemianopia, macula spared'),
         ('achor', 'right homonymous hemianopia — optic tract'), ('wspost', 'partial field loss · higher-order visual problems'),
         ('lacmotor', 'full fields — no cortical signs'), ('lacsens', 'full fields — no cortical signs')]
for k, s in FIELD:
    text(s, 1225, 1790, TAG, 'middle', when=O(k))

# ════════ 7. language ════════
box(1520, 1470, 2340, 1810)
text('Language — the dominant (left) hemisphere', 1544, 1502, 'nf-l1')
ROWS = ['Fluency', 'Comprehension', 'Repetition', 'Reading · writing']
RY = [1556, 1606, 1656, 1706]
for lab, y in zip(ROWS, RY):
    text(lab, 1544, y, 'nf-l1')
    add(f'<path d="M1544 {y + 14} H2316" class="dyn-line" style="stroke-width:1;opacity:.35"/>')
LANG = {
  'mcasup': ['nonfluent, slow, effortful', 'intact', 'impaired', 'writing as hard as speaking (agraphia)', 'Broca aphasia — frustrated, insight kept'],
  'mcainf': ['fluent but paraphasic — word salad', 'impaired', 'impaired', 'cannot read (alexia) or write sense (agraphia)', 'Wernicke aphasia — little insight'],
  'mcastem': ['nonfluent', 'impaired', 'lost', 'lost', 'Global aphasia — Broca and Wernicke areas both gone'],
  'pcal': ['–', '–', '–', 'writes, but cannot read what was written', 'Alexia without agraphia — splenium + left occipital'],
  'wspost': ['–', 'receptive problems, milder than Wernicke', 'usually kept', '–', 'Pericentral aphasia — outside the language centers'],
}
LANGN = {'mcand': 'Language spared — it sits in the left hemisphere in about 95%', 'lacmotor': 'Language spared — no cortical signs',
         'lacsens': 'Language spared — no cortical signs'}
VX = 1770
for k, vals in LANG.items():
    for v, y in zip(vals[:4], RY):
        text(v, VX, y, 'nf-l2', when=O(k))
    text(vals[4], 1544, 1782, TAG, when=O(k))
for k, s in LANGN.items():
    for y in RY: text('normal', VX, y, 'nf-l2', when=O(k))
    text(s, 1544, 1782, TAG, when=O(k))
for y in RY: text('normal', VX, y, 'nf-l2', when=DEF)
for y in RY: text('–', VX, y, 'nf-l2', when=O('aca', 'pcar', 'achor', 'wsant'))

# ════════ 8. attention: the clock ════════
box(960, 1840, 1490, 2270)
text('Attention — “draw a clock”', 984, 1872, 'nf-l1')
KX, KY, KR = 1225, 2062, 120
add(f'<circle cx="{KX}" cy="{KY}" r="{KR}" class="dyn-field"/>')
def numbers(angles):
    return ''.join(f'<text class="nf-l1" x="{KX + .78 * KR * math.sin(math.radians(a)):.0f}" y="{KY - .78 * KR * math.cos(math.radians(a)) + 5:.0f}" '
                   f'text-anchor="middle">{n}</text>' for n, a in zip(range(1, 13), angles))
add(numbers([n * 30 for n in range(1, 13)]), unless=O('mcand'))
add(numbers([12 + (n - 1) * 14.5 for n in range(1, 13)]), when=O('mcand'))
add(f'<path d="M{KX} {KY} L{KX} {KY - 62} M{KX} {KY} L{KX + 44} {KY + 10}" class="dyn-line" style="stroke-width:4;stroke:var(--ink-2)"/>')
add(f'<path d="M{KX} {KY - KR} A{KR} {KR} 0 0 0 {KX} {KY + KR} Z" style="fill:var(--bad);fill-opacity:.12"/>', when=O('mcand'))
text('every number crowded onto the right', KX, 2250, TAG, 'middle', when=O('mcand'))
text('left side of space ignored', KX, 1912, TAG, 'middle', when=O('mcand'))

# ════════ 9. other signs ════════
box(1520, 1840, 2340, 2270)
text('Other signs', 1544, 1872, 'nf-l1')
OTHER = {
  'aca': ['urinary incontinence (medial frontal cortex)'],
  'mcasup': ['eyes deviate toward the lesion — frontal eye field', 'right lower face droops — an upper motor neuron pattern'],
  'mcainf': ['primary auditory cortex in the territory', 'unaware of the deficit — no frustration'],
  'mcastem': ['eyes deviate toward the lesion — frontal eye field', 'the same picture can follow a left ICA occlusion'],
  'mcand': ['eyes deviate toward the lesion — frontal eye field', 'may ignore the left of their own body (asomatognosia)',
            'dressing and constructional apraxia', 'little concern for the deficit'],
  'pcal': ['the calcarine artery feeds the visual cortex', 'macula spared: MCA collaterals reach the occipital pole'],
  'pcar': ['prosopagnosia — familiar faces not recognized', 'macula spared: MCA collaterals reach the occipital pole'],
  'lacmotor': ['pure motor stroke — the commonest lacune', 'unmanaged hypertension → lipohyalinosis of the artery',
               'no aphasia, neglect or field cut'],
  'lacsens': ['pure sensory stroke', 'later: thalamic pain syndrome — allodynia, burning pain'],
  'achor': ['anterior choroidal artery syndrome', 'hemiparesis + homonymous hemianopia together'],
  'wsant': ['“man in a barrel” — proximal arms weak, legs spared', 'often both sides, after a hypotensive episode or cardiac arrest'],
  'wspost': ['higher-order visual dysfunction', 'from hypotension or a shower of emboli'],
}
for k, lines in OTHER.items():
    for i, s in enumerate(lines):
        text(s, 1544, 1920 + i * 34, 'nf-l2', when=O(k))
text('Pick a stroke on the right', 1544, 1920, 'dyn-cap', when=DEF)

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
NORM = lambda *k: R(DEF + O(*k), 0)
readouts = [
  dict(l='Lower face strength', mods=[NORM('aca', 'mcainf', 'lacsens'), R(O('mcasup', 'mcastem', 'mcand', 'lacmotor'), -1)]),
  dict(l='Arm strength', mods=[NORM('aca', 'mcainf', 'lacsens'), R(O('mcasup', 'mcastem', 'mcand', 'lacmotor', 'achor', 'wsant'), -1)]),
  dict(l='Leg strength', mods=[NORM('mcasup', 'mcainf', 'mcand', 'lacsens', 'wsant'), R(O('aca', 'lacmotor', 'achor'), -1)]),
  dict(l='Sensation', mods=[NORM('mcainf', 'lacmotor'), R(O('aca', 'mcasup', 'mcastem', 'mcand', 'lacsens'), -1)]),
  dict(l='Language', mods=[NORM('mcand', 'lacmotor', 'lacsens'), R(O('mcasup', 'mcainf', 'mcastem', 'wspost'), -1)]),
  dict(l='Neglect', mods=[NORM('mcasup', 'mcainf', 'mcastem', 'lacmotor', 'lacsens'), R(O('mcand'), 1)]),
  dict(l='Visual field', mods=[NORM('lacmotor', 'lacsens'), R(O('mcainf', 'mcastem', 'pcal', 'pcar', 'achor', 'wspost'), -1)]),
]

notes = {
  '': 'The cerebral hemisphere from the side, from the midline and in a coronal slice, with each artery’s territory coloured and '
      'blood flowing to it. Pick a stroke: its artery gets the ✕, the territory turns red and the patient shows the deficit. '
      '↓ weak or lost · ↑ present · ↔ normal · – not given by the sources.',
  'st:aca': 'ACA stroke (left). The ACA feeds the medial surface of the frontal and parietal lobes, where the motor and sensory '
            'strips map the leg and foot (paracentral lobule). So the right leg is weak and numb, the face and arm are spared, '
            'and there is urinary incontinence.',
  'st:mcasup': 'MCA superior division (left). Its branches serve the cortex above the lateral fissure: the face and arm areas of the '
               'motor and sensory strips, the frontal eye field and Broca area. Right lower face and arm are weak and numb, the leg '
               'is spared, the eyes look toward the lesion, and speech is nonfluent with comprehension intact — Broca aphasia.',
  'st:mcainf': 'MCA inferior division (left). Its branches serve the cortex below the lateral fissure — Wernicke area, the auditory '
               'cortex and the Meyer loop. Speech stays fluent but makes no sense and comprehension fails, with little insight '
               '(Wernicke aphasia), plus a right upper quadrantanopia. The motor and sensory strips are spared.',
  'st:mcastem': 'MCA stem (M1, left): both divisions are lost, so the face–arm strips and both language areas go. Right lower face '
                'and arm are weak and numb, the eyes look toward the lesion, the right upper field is lost and language is lost '
                'almost completely — global aphasia. A left ICA occlusion can do the same.',
  'st:mcand': 'MCA stroke in the right (nondominant) hemisphere. Left face and arm weakness and sensory loss with the eyes toward '
              'the lesion, but no aphasia — language sits in the left hemisphere in about 95% of people. Instead right parietal '
              'damage brings hemispatial neglect: the left side of space, even of the body, is ignored.',
  'st:pcal': 'PCA stroke (left, dominant). The calcarine branch feeds the primary visual cortex: a right homonymous hemianopia with '
             'macular sparing, because MCA collaterals reach the occipital pole. When the infarct reaches the splenium of the '
             'corpus callosum: alexia without agraphia — the patient writes but cannot read it back.',
  'st:pcar': 'PCA stroke (right, nondominant). A left homonymous hemianopia with macular sparing. A nondominant PCA infarct is also '
             'where First Aid puts prosopagnosia: faces are seen but familiar ones are not recognized.',
  'st:lacmotor': 'Lacune in the posterior limb of the internal capsule (left) — pure motor stroke, the commonest lacunar syndrome. '
                 'A lenticulostriate artery narrowed by lipohyalinosis from unmanaged hypertension occludes. The packed motor fibers '
                 'take the right face, arm and leg together; sensation is spared and there are no cortical signs.',
  'st:lacsens': 'Lacune in the lateral thalamus (VPL/VPM, left) — pure sensory stroke. Sensation fades over the whole right side, '
                'face, arm and leg, with strength and the cortex spared. Weeks to months later some patients develop thalamic pain '
                'syndrome (Dejerine-Roussy): allodynia and burning pain on the same side.',
  'st:achor': 'Anterior choroidal artery (left), a branch of the internal carotid that runs along the optic tract. It supplies the '
              'inferior posterior limb of the internal capsule and the optic tract, so its occlusion gives right arm and leg '
              'weakness with a right homonymous hemianopia — the anterior choroidal artery syndrome.',
  'st:wsant': 'ACA–MCA watershed infarct — the border zone at greatest risk. After a severe fall in systemic pressure (cardiac '
              'arrest, cardiovascular surgery) the far ends of both arteries starve, often on both sides: weakness of both proximal '
              'arms with the legs spared, the “man in a barrel”.',
  'st:wspost': 'MCA–PCA watershed infarct (left), after hypotension or a shower of emboli. The posterior border zone gives partial '
               'visual field loss and higher-order visual dysfunction, with receptive language problems that are milder than '
               'Wernicke aphasia and usually spare repetition (a pericentral aphasia).',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='st', label='Stroke — pick one', type='one', options=[
      ['aca', 'ACA (left)', 'acastroke'], ['mcasup', 'MCA superior division (left)', 'mcastroke'],
      ['mcainf', 'MCA inferior division (left)', 'mcastroke'], ['mcastem', 'MCA stem — M1 (left)', 'mcastroke'],
      ['mcand', 'MCA (right, nondominant)', 'mcastroke'],
      ['pcal', 'PCA (left, dominant)', 'pcastroke'], ['pcar', 'PCA (right, nondominant)', 'pcastroke'],
      ['lacmotor', 'Lacune — internal capsule', 'lacunar'], ['lacsens', 'Lacune — thalamus', 'thalamicpain'],
      ['achor', 'Anterior choroidal artery', 'carotidsys'],
      ['wsant', 'ACA–MCA watershed (both sides)', 'wshedinf'], ['wspost', 'MCA–PCA watershed (left)', 'wshedinf']],
      sections=[['Anterior circulation', ['aca', 'mcasup', 'mcainf', 'mcastem', 'mcand']],
                ['Posterior circulation', ['pcal', 'pcar']],
                ['Deep / lacunar', ['lacmotor', 'lacsens', 'achor']],
                ['Watershed', ['wsant', 'wspost']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 513, 524–526, 528–529, 557 · Fundamental Neuroscience ch 8, 15, 16, 18, 20, 25, 28, 32 · Robbins ch 28')

# ════════ the one new card: no card covers cerebral watershed infarcts or the man-in-a-barrel picture ════════
card('wshedinf', 'Cerebral watershed (border-zone) infarct', 'dz', 'skWs', 'Hypotension starves the edges between two arterial territories', 1,
     'Where the distal branches of the ACA and MCA, or of the MCA and PCA, meet on the lateral surface of the hemisphere, the cortex '
     'sits at the far end of two supplies with little collateral flow. A severe fall in systemic pressure, or hypoperfusion of a major '
     'artery’s distal bed, infarcts these <b>border zones</b> first; they account for about 10% of brain infarcts.',
     ['<b>ACA–MCA</b> border zone, the one at greatest risk: wedge-shaped cortical infarct, often bilateral — proximal arm weakness '
      'with the legs spared, the “man in a barrel” (First Aid)',
      '<b>MCA–PCA</b> border zone: higher-order visual dysfunction; partial visual loss with language problems',
      'Fundamental Neuroscience describes a one-sided anterior watershed infarct as contralateral leg weakness with expressive '
      'language deficits or behavioral change',
      'Border-zone language deficits (pericentral aphasias) resemble Broca or Wernicke aphasia but are milder and usually spare repetition'],
     ['Infarcts in the wedges between territories; internal border zones lie between the superficial and deep MCA territories',
      'Often shows secondary hemorrhagic transformation'],
     ['Both proximal arms weak after a hypotensive episode = ACA–MCA watershed'],
     [FN8, FN32, RB28],
     ['—'],
     ['cerebral watershed', 'watershed stroke', 'border zone infarct', 'border-zone infarct', 'man in a barrel', 'man-in-a-barrel',
      'aca-mca watershed', 'mca-pca watershed', 'pca-mca watershed', 'anterior watershed infarct', 'posterior watershed infarct',
      'pericentral aphasia', '=watershed infarct'],
     fa='206, 513, 525')

MAP = dict(
  id='strokesim', title='Stroke Territory Simulator', topic='neuro', after='stroke',
  sub='The hemisphere from the side, from the midline and in a coronal slice, with the ACA, the MCA’s superior and inferior '
      'divisions, the PCA, the deep lenticulostriate and anterior choroidal territory and the border zones — pick a stroke and '
      'watch the blood stop, the territory infarct and the patient’s face, arm, leg, sensation, language, attention and visual '
      'fields change. Tap a pin for its card',
  w=3500, h=2300,
  fa='206, 513, 524, 525, 526, 528, 529, 557', src=SRC,
  lanes=[('skAnt', 'Anterior circulation', 'glycolysis'), ('skPost', 'Posterior circulation', 'ppp'),
         ('skDeep', 'Deep & lacunar', 'glycogen'), ('skWs', 'Watershed', 'tca')],
  comps=[],
  nodes=[
    ('sk1', 'ACA stroke', 2640, 1240, 'skAnt', 'leg · bladder', ['acastroke']),
    ('sk2', 'MCA stroke', 2640, 1320, 'skAnt', 'face, arm · aphasia or neglect', ['mcastroke'], 'hub'),
    ('sk3', 'Aphasias · language areas', 2640, 1400, 'skAnt', 'Broca · Wernicke · global', ['aphasia', 'ctxareas']),
    ('sk4', 'Dominance · cortical signs', 2640, 1480, 'skAnt', 'Gerstmann · neglect', ['ctxdominance', 'cortexlesions']),
    ('sk5', 'Motor strip · eye fields', 2640, 1560, 'skAnt', 'homunculus · gaze', ['motorcortex', 'corteye']),
    ('sk6', 'Carotid & its branches', 2640, 1640, 'skAnt', 'ophthalmic · anterior choroidal', ['carotidsys', 'willis']),
    ('sk7', 'PCA stroke', 3110, 1240, 'skPost', 'hemianopia, macula spared', ['pcastroke', 'vbsystem'], 'hub'),
    ('sk8', 'Visual field defects', 3110, 1320, 'skPost', 'Meyer loop · cortex', ['vfdefects']),
    ('sk9', 'Prosopagnosia · agnosias', 3110, 1400, 'skPost', 'nondominant PCA', ['agnosia']),
    ('sk10', 'Lacunar stroke', 3110, 1480, 'skDeep', 'pure motor · no cortical signs', ['lacunar', 'cstsomato', 'ich'], 'hub'),
    ('sk11', 'Thalamic pain syndrome', 3110, 1560, 'skDeep', 'Dejerine-Roussy', ['thalamicpain']),
    ('sk12', 'Watershed infarct', 3110, 1640, 'skWs', 'man in a barrel', ['wshedinf', 'ischemiavuln']),
  ],
  panels=[
    (2420, 720, 1000, 'Aphasias (First Aid p. 529; Fund. Neurosci. ch 32)', [
      ('Broca — inferior frontal gyrus', 'nonfluent, comprehension intact, insight kept'),
      ('Wernicke — superior temporal gyrus', 'fluent word salad, comprehension impaired, no insight'),
      ('Conduction — arcuate fasciculus', 'repetition impaired'),
      ('Global — Broca + Wernicke areas', 'nonfluent, comprehension impaired · left ICA or M1')]),
    (2420, 960, 1000, 'Cortical signs by site (First Aid pp. 524, 526)', [
      ('Frontal eye field', 'eyes look toward the lesion (MCA stroke)'),
      ('Dominant parietal', 'Gerstmann — agraphia, acalculia, finger agnosia, left–right confusion'),
      ('Nondominant parietal', 'hemispatial neglect of the opposite side'),
      ('Lacune', 'no cortical signs — no neglect, aphasia or field cut')]),
  ],
  dyn=dyn,
)
