# m58 — Foregut, Midgut & Hindgut: Arteries, Nerves & Referred Pain in Motion (dynamic map, kit data)
# The gut drawn front-on (patient's right on the viewer's left): esophagus, stomach, duodenal C-loop with the pancreas,
# liver + gallbladder, spleen, small-bowel loops, cecum + appendix, colon frame (hepatic flexure, transverse, splenic
# flexure, descending, sigmoid), rectum. The abdominal aorta is drawn beside the gut (to the right) with its three gut
# branches — celiac trunk, SMA, IMA — and a prevertebral ganglion on each. Top left: the medulla and the nodose ganglion
# on the vagus; far right: the spinal cord (T5–L2 sympathetic outflow, S2–S4 pelvic splanchnics) with dorsal root ganglia.
# Chyme moves along the gut in three territories (foregut / midgut / hindgut), blood along the aorta and branches,
# nerve signals along the vagus, pelvic splanchnics, splanchnic sympathetics and afferents.
# One `one` switch (`n`, 12 options in 4 sections). Three readouts: gut motility & secretion, sphincter tone, gut blood flow.
#
# Labels chosen with the m58 sweep (coverage4.md §3 ★7): the card-less `vag` option and the `nod` option must not pull the
# pulmonary Hering-Breuer question (pulm sdl31_q10, linked cards medulla · nts · respctr). That question reached the map
# only through the `nts` card, so `nts` is neither an option card nor a pin here (`nod` uses `viscafferent`), and
# `vagusomm` / `pelvicsplanch` / `foregutdev` are not pinned (they pulled nephro bladder/kidney/erection and a
# stomach-rotation question onto `vag`/`pel`). Re-simulated in scratch m58/gutnervsim (sim3.json, scenario a2): gastro
# +6 (sdl01_q01, sdl01_q16, trial_sdl01_q01 → mg; trial_sdl04_q02 → smg; trial_sdl04_q04 → nod; trial_sdl04_q06 → drg);
# elsewhere neuro sdl31_q03/q08/q33 → nod, sdl31_bloom_q08 → vag, sdl46_q31 → img; OMM sdl10_q14 → fg, sdl14_q20 → smg,
# sdl28_q12 → img; pulm sdl31_q10 NOT taken; nothing lost.
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt) p2–3, SDL 1 §1: four gut divisions; foregut (esophagus →
#     duodenum to the major papilla, liver, gallbladder, biliary ducts, pancreas) = celiac; midgut (distal duodenum, jejunum,
#     ileum, cecum, appendix, ascending colon, proximal 2/3 transverse colon) = SMA; hindgut (distal 1/3 transverse colon →
#     upper anal canal) = IMA; duodenum: superior pancreaticoduodenal (celiac via gastroduodenal) vs inferior
#     pancreaticoduodenal (SMA). p23–25, SDL 4 §2–4: prevertebral ganglia (celiac, SM, IM, hypogastric); sympathetic
#     preganglionics T5–L2, short pre / long post, NE; parasympathetic long pre / short post in the enteric plexuses;
#     parasympathetic ↑ motility, relaxes sphincters, ↑ secretions, secondarily ↑ mucosal blood flow; sympathetic
#     ↓ motility, contracts sphincters, inhibits secretion, vasoconstriction; vagus to esophagus … proximal transverse
#     colon; pelvic nerve S2–S4 to distal transverse colon … anal canal, dense in sigmoid/rectum/anus (defecation);
#     75–80% of vagal fibers afferent → nucleus tractus solitarius; vagovagal reflexes (receptive relaxation, gastric
#     secretion, gastrocolic reflex).
#   Robbins ch 17 (course reading, course_sdl_8_9_patho p82, p94): watershed zones at the splenic flexure (SMA and IMA end)
#     and, less, sigmoid colon/rectum; hypotension/hypoxemia → ischemic injury there.
#   Guyton ch 63 (course reading, course_sdl_4_7_guyton_supplement p9–11, 26): afferents to prevertebral ganglia, cord and
#     vagus; afferent cell bodies in enteric system or dorsal root ganglia; 80% of vagal fibers afferent; sympathetic
#     stimulation can cut splanchnic blood flow to very little in shock / exercise.
#   Foundations of Osteopathic Medicine ch 6 (corpus/omm): celiac ganglia ← thoracic splanchnics T5–T9 → celiac territory
#     (distal esophagus, stomach, proximal duodenum, liver, gallbladder, spleen, part of pancreas); superior mesenteric
#     ganglia ← T9–T11 or T12 → SMA territory (distal duodenum, part of pancreas, jejunum, ileum, ascending colon, proximal
#     2/3 transverse colon); inferior mesenteric ganglia ← lumbar splanchnics L1–L2 → distal 1/3 transverse, descending,
#     sigmoid colon; each ganglion serves its artery's territory; vagal afferent cell bodies in the nodose ganglion (→
#     solitary nucleus), splanchnic afferent cell bodies in dorsal root ganglia (stretch, bradykinin).
#   Fundamental Neuroscience ch 14: vagal visceral afferents from heart, aortic arch, lungs and gut to about the splenic
#     flexure, cell bodies in the inferior (nodose) ganglion, central processes → solitary nucleus; vagal influence ↑ blood
#     flow, peristalsis and secretions in the gut.
#   Moore ch 5: visceral pain poorly localized, referred to the dermatomes of the spinal ganglia that receive the organ's
#     afferents; foregut → epigastric, midgut → periumbilical, hindgut → hypogastric (pubic); gastric pain via greater
#     splanchnic to T7–T8; early appendicitis periumbilical because the afferents enter at T10.
#   First Aid 2025 pp. 370 (watershed areas: splenic flexure SMA/IMA, rectosigmoid junction), 371 (region · artery ·
#     parasympathetic · vertebral level T12/L1, L1, L3; celiac branches; prevertebral ganglia), 393 (acute mesenteric
#     ischemia — often SMA embolus, pain out of proportion; colonic ischemia at watershed areas, thumbprint sign),
#     523 (T10 — umbilicus, referred pain of early appendicitis).
# Readout arrows: only where the lecture notes p23 state them (parasympathetic ↑ motility / secretion, sphincters relax,
#   ↑ mucosal blood flow — also Fundamental Neuroscience ch 14; sympathetic ↓ motility / secretion, sphincters contract,
#   vasoconstriction — also Guyton ch 63) and the watershed (↓ flow = the ischemia itself, Robbins / FA 370). Arteries and
#   afferent options carry "–" (no source gives a direction for them).
# Cuts: the vertebral level of the aortic bifurcation (not needed, unsourced here); a "hypogastric ganglion" option (the
#   lecture lists it; no question asks it, no card); exact preganglionic levels as hard facts — given only as Foundations'
#   "typically" ranges in the ganglion panel; phrenic referral of upper-abdominal pain to the shoulder (FA 387/Moore —
#   peritoneal, not visceral referral; left out to keep the pain option to the three gut regions).
# Source conflicts for the owner: (1) the vagus' lower limit — lecture notes "proximal portion of the transverse colon",
#   FA 371 "midgut … proximal 2/3 of transverse colon", Fundamental Neuroscience "just proximal to the splenic flexure";
#   the map draws the vagus to the 2/3 point (course + FA). (2) Superior mesenteric ganglion inputs — Foundations
#   "T9–T11 or T12", OMM course question T9–T11, gastro trial question (Bootcamp) T10–T12; the panel prints Foundations'.
#   (3) IMG inputs — Foundations L1–L2, OMM course chart (Written Midterm guide, SDL 13/14) T12–L2: the map prints the OMM chart
#   (course wins for OMM, whose questions land here), with Foundations' lumbar splanchnics L1–L2 alongside. SMG: chart T9–T11. (4) Sympathetic outflow T5–L2 (lecture notes).
import sys
import math
import re
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

GY63, RB17, MO5, LG15 = full('Guyton', 63), full('Robbins', 17), full('Moore', 5), full('Langman', 15)
FN14 = full('Fundamental Neuroscience', 14)
FOM6 = 'Foundations of Osteopathic Medicine ch 6 — Autonomic Nervous System'
SRC = [GY63, RB17, MO5, LG15, FN14, FOM6]

O = lambda *k: ['n:' + x for x in k]

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

# ── path length (absolute M L H V Q C only) ──
def plen(d):
    toks = re.findall(r'[MLHVQC]|-?\d+(?:\.\d+)?', d)
    i, x, y, L, cmd = 0, 0.0, 0.0, 0.0, None
    def num():
        nonlocal i
        v = float(toks[i]); i += 1; return v
    while i < len(toks):
        if toks[i] in 'MLHVQC': cmd = toks[i]; i += 1
        if cmd == 'M': x, y = num(), num(); cmd = 'L'
        elif cmd == 'L': nx, ny = num(), num(); L += math.hypot(nx - x, ny - y); x, y = nx, ny
        elif cmd == 'H': nx = num(); L += abs(nx - x); x = nx
        elif cmd == 'V': ny = num(); L += abs(ny - y); y = ny
        elif cmd in 'QC':
            pts = [(x, y)] + [(num(), num()) for _ in range(2 if cmd == 'Q' else 3)]
            px, py = x, y
            for s in range(1, 41):
                t = s / 40
                if cmd == 'Q':
                    (a, b), (c, e), (f, g) = pts
                    qx = (1 - t) ** 2 * a + 2 * (1 - t) * t * c + t * t * f; qy = (1 - t) ** 2 * b + 2 * (1 - t) * t * e + t * t * g
                else:
                    (a, b), (c, e), (f, g), (h, k) = pts
                    qx = (1 - t) ** 3 * a + 3 * (1 - t) ** 2 * t * c + 3 * (1 - t) * t * t * f + t ** 3 * h
                    qy = (1 - t) ** 3 * b + 3 * (1 - t) ** 2 * t * e + 3 * (1 - t) * t * t * g + t ** 3 * k
                L += math.hypot(qx - px, qy - py); px, py = qx, qy
            x, y = pts[-1]
    return round(L)
def join(*ds):   # one continuous path from pieces that start where the last one ended
    return ' '.join([ds[0]] + ['L' + d[1:] if d.startswith('M') else d for d in ds[1:]])

ARTS, FORE, MID, HIND = ['n:fg', 'n:mg', 'n:hg', 'n:ws'], O('fg'), O('mg'), O('hg')
SYM, PARA = O('cel', 'smg', 'img'), O('vag', 'pel')

# ════════ 0. referred-pain bands (under everything) ════════
BANDS = [('fg', 430, 830, '--dk5', 'Epigastric', 'foregut pain'), ('mg', 830, 1330, '--dk3', 'Umbilical (T10)', 'midgut pain'),
         ('hg', 1330, 1830, '--dk1', 'Hypogastric', 'hindgut pain')]
for k, y0, y1, col, nm, sub in BANDS:
    add(f'<rect x="150" y="{y0}" width="1500" height="{y1 - y0}" rx="18" style="fill:var({col});opacity:.10"/>', when=O('ref', k))
    text(nm, 250, y0 + 34, 'dyn-big', when=O('ref', k))
    text(sub + ' felt here', 250, y0 + 56, 'dyn-cap', when=O('ref', k))

# ════════ 1. medulla + nodose ganglion ════════
BS = 'M300 120 C300 100 460 100 460 120 L452 250 C450 290 430 310 400 312 L360 312 C330 310 310 290 308 250 Z'
add(f'<path d="{BS}" class="dyn-cell" style="stroke:var(--dk4)"/>')
add('<circle cx="350" cy="230" r="13" style="fill:var(--dk1);opacity:.85"/><circle cx="410" cy="230" r="13" style="fill:var(--dk3);opacity:.85"/>')
text('Medulla', 380, 92, 'dyn-big', 'middle')
text('solitary nucleus (afferents in)', 480, 270, 'dyn-cap')
text('dorsal motor nucleus of X (out)', 480, 200, 'dyn-cap')
add('<ellipse cx="440" cy="400" rx="20" ry="13" style="fill:var(--dk1);stroke:var(--surface);stroke-width:2"/>')

# ════════ 2. organs: liver, gallbladder, spleen, pancreas ════════
LIV = 'M420 560 C440 470 700 450 990 468 C1040 474 1050 510 1030 548 C960 630 760 690 580 708 C470 718 412 660 420 560 Z'
add(f'<path d="{LIV}" class="dyn-cell" style="stroke:var(--dk9)"/><path d="M800 470 Q790 560 800 690" class="dyn-line" style="stroke-width:2;opacity:.5"/>')
text('Liver', 520, 590, 'dyn-big')
GB = 'M720 690 C690 720 700 780 740 784 C780 784 790 735 765 690 Z'
add(f'<path d="{GB}" class="dyn-cell" style="stroke:var(--dk6)"/><path d="{GB}" fill="var(--dk6)" opacity=".2"/>')
SPL = 'M1480 470 C1510 420 1590 430 1600 490 C1608 540 1580 590 1540 596 C1520 580 1530 540 1500 530 C1470 520 1466 490 1480 470 Z'
add(f'<path d="{SPL}" class="dyn-cell" style="stroke:var(--dk12)"/><path d="{SPL}" fill="var(--dk12)" opacity=".14"/>')
text('spleen', 1545, 625, 'dyn-cap', 'middle')
PANC = ('M780 850 C840 830 900 862 960 868 C1100 880 1300 850 1400 858 C1440 862 1440 900 1404 906 C1300 920 1100 932 960 934 '
        'C890 938 820 958 790 928 Z')
add(f'<path d="{PANC}" class="dyn-cell" style="stroke:var(--dk3)"/><path d="{PANC}" fill="var(--dk3)" opacity=".12"/>')
text('pancreas', 1200, 880, 'dyn-cap', 'middle')

# ════════ 3. the gut tube ════════
ESO = 'M1090 330 V520'
STOM = ('M1090 520 C1100 470 1180 452 1260 470 C1380 500 1440 600 1420 700 C1400 800 1280 846 1150 832 '
        'C1050 820 960 792 912 772 L916 724 C990 742 1060 732 1078 684 C1094 632 1086 572 1090 520 Z')
DUO = 'M912 748 H780 Q712 748 712 812 V940 Q712 1000 776 1000 H960'
SI = ('M960 1000 C1080 1000 1180 1080 1150 1150 C1120 1220 900 1190 860 1260 C820 1340 1000 1380 1090 1340 '
      'C1170 1305 1270 1330 1230 1400 C1190 1460 880 1470 680 1455')
COL_A = 'M620 1560 V1080 Q620 1040 662 1040 H1230'      # cecum → ascending → hepatic flexure → 2/3 of the transverse colon
COL_B = 'M1230 1040 H1440 Q1540 1040 1556 960 V1480'      # distal 1/3 transverse → splenic flexure → descending
COL_C = 'M1556 1480 C1556 1580 1400 1600 1300 1570 C1200 1540 1120 1570 1110 1640 V1800'   # sigmoid → rectum → anal canal
shapes.append(dict(tube=ESO, w=30, color='--dk5'))
add(f'<path d="{STOM}" class="dyn-cell" style="stroke:var(--dk5);stroke-width:5"/><path d="{STOM}" fill="var(--dk5)" opacity=".1"/>')
shapes.append(dict(tube=DUO, w=40, color='--dk5'))
shapes.append(dict(tube=SI, w=36, color='--dk3'))
shapes.append(dict(tube=COL_A, w=60, color='--dk3'))
shapes.append(dict(tube=COL_B, w=60, color='--dk1'))
shapes.append(dict(tube=COL_C, w=54, color='--dk1'))
add('<path d="M640 1580 C650 1620 640 1650 620 1668" class="dyn-line" style="stroke:var(--dk3);stroke-width:12;stroke-linecap:round"/>')   # appendix
text('Stomach', 1320, 720, 'dyn-big', 'middle')
text('esophagus', 1060, 360, 'dyn-cap', 'end')
text('duodenum', 690, 880, 'dyn-cap', 'end')
text('major papilla', 690, 960, 'nf-l2', 'end')
add('<circle cx="732" cy="960" r="6" style="fill:var(--ink-2)"/>')
text('jejunum · ileum', 1010, 1290, 'dyn-cap', 'middle')
text('cecum', 590, 1560, 'dyn-cap', 'end')
text('ascending colon', 590, 1240, 'dyn-cap', 'end')
text('transverse colon', 900, 1010, 'dyn-cap', 'middle')
text('⅔ | ⅓', 1230, 1105, 'nf-l1', 'middle')
add('<path d="M1230 1004 V1076" class="dyn-line" style="stroke:var(--ink-2);stroke-width:3;stroke-dasharray:5 4"/>')
text('splenic flexure', 1600, 950, 'dyn-cap')
text('descending colon', 1600, 1240, 'dyn-cap')
text('sigmoid', 1360, 1640, 'dyn-cap', 'middle')
text('rectum', 1150, 1730, 'dyn-cap')
# sphincters: pylorus, ileocecal, internal anal — tight (sympathetic) or open (parasympathetic)
SPH = dict(pyl=(912, 748, 'v'), ilc=(690, 1455, 'v'), ias=(1110, 1790, 'h'))
for k, (x, y, o) in SPH.items():
    r = f'x="{x - 8}" y="{y - 26}" width="16" height="52"' if o == 'v' else f'x="{x - 30}" y="{y - 8}" width="60" height="16"'
    add(f'<rect {r} rx="6" style="fill:var(--dk7);opacity:.75"/>')
TIGHT = dict(pyl=O('cel'), ilc=O('smg'), ias=O('img'))
OPEN = dict(pyl=O('vag'), ilc=O('vag'), ias=O('pel'))
for k, (x, y, o) in SPH.items():
    r = f'x="{x - 14}" y="{y - 34}" width="28" height="68"' if o == 'v' else f'x="{x - 38}" y="{y - 14}" width="76" height="28"'
    add(f'<rect {r} rx="8" style="fill:var(--dk7)"/>', when=TIGHT[k])
    add(f'<rect {r} rx="8" style="fill:none;stroke:var(--dk7);stroke-width:3;stroke-dasharray:4 4"/>', when=OPEN[k])
text('pylorus', 930, 700, 'nf-l2')
text('ileocecal', 700, 1420, 'nf-l2')
text('internal anal sphincter', 1160, 1796, 'nf-l2')

# territory highlights
add(f'<path d="{ESO} M1090 520" class="dyn-hl"/><path d="{STOM}" class="dyn-hl"/><path d="M912 748 H780 Q712 748 712 812 V960" class="dyn-hl"/>'
    f'<path d="{LIV}" class="dyn-hl" style="stroke-width:4"/><path d="{PANC}" class="dyn-hl" style="stroke-width:4"/>'
    f'<path d="{SPL}" class="dyn-hl" style="stroke-width:3;opacity:.5"/>', when=FORE + O('cel'))
add(f'<path d="M712 960 V940 Q712 1000 776 1000 H960" class="dyn-hl"/><path d="{SI}" class="dyn-hl"/><path d="{COL_A}" class="dyn-hl"/>',
    when=MID + O('smg'))
add(f'<path d="{COL_B}" class="dyn-hl"/><path d="{COL_C}" class="dyn-hl"/>', when=HIND + O('img'))
# vagal territory (foregut + midgut) and pelvic territory (hindgut), drawn thinner in green
add(f'<path d="{ESO}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/><path d="{STOM}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/>'
    f'<path d="{DUO}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/><path d="{SI}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/>'
    f'<path d="{COL_A}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/>', when=O('vag', 'nod'))
add(f'<path d="{COL_B}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/><path d="{COL_C}" class="dyn-hl" style="stroke:var(--dk3);stroke-width:5"/>',
    when=O('pel'))
# watershed: the splenic flexure (SMA ↔ IMA) and the rectosigmoid junction (IMA branches)
add('<circle cx="1520" cy="1000" r="64" style="fill:var(--bad);opacity:.14"/><circle cx="1520" cy="1000" r="64" class="dyn-lesion" style="stroke-dasharray:8 6"/>'
    '<circle cx="1140" cy="1580" r="50" style="fill:var(--bad);opacity:.12"/><circle cx="1140" cy="1580" r="50" class="dyn-lesion" style="stroke-dasharray:8 6"/>',
    when=O('ws'))
text('rectosigmoid junction', 1060, 1500, TAG, 'end', when=O('ws'))

# ════════ 4. abdominal aorta (drawn beside the gut) and its three gut branches ════════
AO = 'M1830 300 V1250'
CEL0 = 'M1830 545 H1700'
LGA = 'M1700 545 C1520 500 1320 470 1190 505'
SPLA = 'M1700 545 C1660 530 1630 515 1600 512'
CHA = 'M1700 545 C1600 610 1320 650 1100 650 C1000 650 900 630 850 610'
SMA0 = 'M1830 650 H1720 C1600 690 1470 790 1400 900'
SMA_SI = 'M1400 900 C1350 1060 1220 1200 1080 1250'
SMA_RC = 'M1400 900 C1200 1010 820 1160 650 1250'
SMA_MC = 'M1400 900 C1320 950 1200 990 1060 1030'
SMA_DU = 'M1400 900 C1150 905 900 960 735 975'
IMA0 = 'M1830 800 H1730 C1690 820 1660 900 1650 980'
IMA_LC = 'M1650 980 C1630 975 1600 975 1580 980'
IMA_SG = 'M1650 980 C1650 1200 1620 1420 1560 1530'
IMA_SR = 'M1650 980 C1640 1320 1320 1600 1140 1620'
narrow = lambda *k: [dict(when=O(*k), d=-4)]
shapes.append(dict(vessel=AO, w=20))
shapes.append(dict(vessel='M1830 1250 L1740 1420 M1830 1250 L1920 1420', w=16))
for d in (CEL0, LGA, SPLA, CHA):
    shapes.append(dict(vessel=d, w=9 if d == CEL0 else 5, mods=narrow('cel') + [dict(when=O('fg'), d=5)]))
for d in (SMA0, SMA_SI, SMA_RC, SMA_MC, SMA_DU):
    shapes.append(dict(vessel=d, w=9 if d == SMA0 else 5, mods=narrow('smg') + [dict(when=O('mg'), d=4)]))
for d in (IMA0, IMA_LC, IMA_SG, IMA_SR):
    shapes.append(dict(vessel=d, w=9 if d == IMA0 else 5, mods=narrow('img') + [dict(when=O('hg'), d=4)]))
text('Abdominal aorta', 1830, 280, 'dyn-big', 'middle')
text('drawn beside the gut', 1830, 260, 'dyn-cap', 'middle')
text('celiac trunk', 1610, 470, 'nf-l2', 'middle', when=O('fg'))
text('superior mesenteric artery', 1640, 820, 'nf-l2', 'end', when=O('mg'))
text('inferior mesenteric artery', 1700, 1060, 'nf-l2', when=O('hg'))

# ════════ 5. spinal cord, dorsal root ganglia ════════
SEG = ['T5', 'T6', 'T7', 'T8', 'T9', 'T10', 'T11', 'T12', 'L1', 'L2']
SY = {s: 300 + i * 82 for i, s in enumerate(SEG)}
SY.update(S2=1500, S3=1560, S4=1620)
add('<rect x="2200" y="270" width="40" height="870" rx="18" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<rect x="2200" y="1470" width="40" height="180" rx="18" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M2220 1170 V1440" class="dyn-line" style="stroke-dasharray:3 10;opacity:.5"/>')
text('Spinal cord', 2220, 245, 'dyn-big', 'middle')
for s, y in SY.items():
    text(s, 2256, y + 5, 'nf-l2')
for s in ('T7', 'T10', 'L1'):
    add(f'<ellipse cx="2160" cy="{SY[s]}" rx="16" ry="11" style="fill:var(--dk1);stroke:var(--surface);stroke-width:2"/>')
add('<rect x="2196" y="296" width="48" height="742" rx="20" style="fill:var(--dk7);opacity:.14"/>', when=SYM)
add('<rect x="2196" y="1478" width="48" height="160" rx="20" style="fill:var(--dk3);opacity:.2"/>', when=O('pel'))
text('T5–L2: sympathetic outflow', 2120, 1180, 'nf-l2', 'end', when=SYM)

# ════════ 6. nerves ════════
VAG = 'M400 312 L440 400 C480 460 700 430 900 405 C1000 395 1060 410 1078 440 L1080 520'
VAG_ST = 'M1080 520 C1130 560 1200 600 1250 640'
VAG_SI = 'M1080 520 C1010 700 990 900 1010 1210'
VAG_CO = 'M1080 520 C1160 760 1210 920 1228 1030'
add(f'<path d="{VAG}" class="dyn-line" style="stroke:var(--dk3);stroke-width:4"/>')
for d in (VAG_ST, VAG_SI, VAG_CO):
    add(f'<path d="{d}" class="dyn-line" style="stroke:var(--dk3);stroke-width:3;opacity:.55"/>', unless=O('vag', 'nod'))
    add(f'<path d="{d}" class="dyn-line" style="stroke:var(--dk3);stroke-width:4"/>', when=O('vag', 'nod'))
text('vagus (CN X)', 700, 418, 'nf-l2', 'middle')
PEL = 'M2200 1560 C2000 1580 1700 1660 1400 1690 C1260 1700 1170 1690 1135 1680'
PEL_UP = 'M2200 1560 C1900 1520 1700 1460 1620 1380 C1600 1240 1610 1100 1560 1010 C1500 990 1400 990 1300 1000'
add(f'<path d="{PEL}" class="dyn-line" style="stroke:var(--dk3);stroke-width:3;opacity:.55"/><path d="{PEL_UP}" class="dyn-line" style="stroke:var(--dk3);stroke-width:3;opacity:.55"/>',
    unless=O('pel'))
add(f'<path d="{PEL}" class="dyn-line" style="stroke:var(--dk3);stroke-width:4"/><path d="{PEL_UP}" class="dyn-line" style="stroke:var(--dk3);stroke-width:4"/>',
    when=O('pel'))
text('pelvic splanchnics', 1900, 1640, 'nf-l2', 'middle')
# splanchnic (sympathetic preganglionic) nerves: cord → ganglion
GSP = 'M2200 464 C2050 470 1920 520 1780 545'
SSP = 'M2200 710 C2050 690 1920 660 1780 650'
LSP = 'M2200 1000 C2050 960 1920 830 1780 800'
for d, k in ((GSP, 'cel'), (SSP, 'smg'), (LSP, 'img')):
    add(f'<path d="{d}" class="dyn-dash" style="stroke:var(--dk7);opacity:.6"/>', unless=O(k))
    add(f'<path d="{d}" class="dyn-line" style="stroke:var(--dk7);stroke-width:4"/>', when=O(k))
# afferent paths (to the DRG) for drg / ref
AFF_F = 'M1300 650 C1500 640 1700 520 1900 470 C2000 440 2100 430 2160 430'
AFF_M = 'M1100 1220 C1400 1100 1700 760 1900 700 C2000 690 2100 685 2160 685'
AFF_H = 'M1500 1300 C1700 1150 1900 990 2000 950 C2080 940 2130 940 2160 940'
for d in (AFF_F, AFF_M, AFF_H):
    add(f'<path d="{d}" class="dyn-line" style="stroke:var(--dk1);stroke-width:3;stroke-dasharray:2 7"/>', when=O('drg', 'ref'))

# prevertebral ganglia on the aorta
GANG = dict(cel=(1765, 545), smg=(1765, 650), img=(1765, 800))
for k, (x, y) in GANG.items():
    add(f'<ellipse cx="{x}" cy="{y}" rx="24" ry="15" style="fill:var(--dk7);stroke:var(--surface);stroke-width:2"/>')
    add(f'<ellipse cx="{x}" cy="{y}" rx="40" ry="30" class="dyn-hl"/>', when=O(k))
add('<ellipse cx="440" cy="400" rx="38" ry="28" class="dyn-hl"/>', when=O('nod'))
add(''.join(f'<ellipse cx="2160" cy="{SY[s]}" rx="32" ry="24" class="dyn-hl"/>' for s in ('T7', 'T10', 'L1')), when=O('drg', 'ref'))

# ════════ 7. the top caption: what is switched on ════════
HEAD = {
  'fg': ('Foregut — celiac trunk (T12/L1)', 'esophagus to the major papilla · liver, gallbladder, pancreas · vagus · celiac ganglion'),
  'mg': ('Midgut — superior mesenteric artery (L1)', 'distal duodenum to ⅔ of the transverse colon · vagus · superior mesenteric ganglion'),
  'hg': ('Hindgut — inferior mesenteric artery (L3)', 'distal ⅓ of the transverse colon to the upper anal canal · pelvic splanchnics · IM ganglion'),
  'ws': ('Watershed — where two arterial trees end', 'splenic flexure (SMA ↔ IMA) · rectosigmoid junction (last sigmoid ↔ superior rectal)'),
  'vag': ('Vagus — parasympathetic to foregut and midgut', 'long preganglionic fibers synapse in the enteric plexuses of the gut wall'),
  'pel': ('Pelvic splanchnics (S2–S4) — parasympathetic to the hindgut', 'distal transverse colon, descending and sigmoid colon, rectum, anal canal'),
  'cel': ('Celiac ganglion — sympathetic relay for the foregut', 'thoracic splanchnics (typically T5–T9) synapse here · fibers ride the celiac branches'),
  'smg': ('Superior mesenteric ganglion — relay for the midgut', 'thoracic splanchnics T9–T11 (OMM chart; to T12 in some texts) · fibers ride the SMA'),
  'img': ('Inferior mesenteric ganglion — relay for the hindgut', 'T12–L2 (OMM chart; lumbar splanchnics L1–L2) · fibers ride the IMA'),
  'nod': ('Nodose ganglion — cell bodies of vagal afferents', 'stretch and chemical signals → solitary nucleus → vagovagal reflexes'),
  'drg': ('Splanchnic afferents — cell bodies in dorsal root ganglia', 'run back with the sympathetic splanchnic nerves → dorsal horn · visceral pain'),
  'ref': ('Referred visceral pain', 'dull, poorly localized, felt in the dermatomes that share the organ’s spinal ganglia'),
}
text('Pick a gut division, a nerve or a ganglion', 620, 150, 'dyn-big', unless=['n:*'])
text('red dots: blood · amber: chyme · green: parasympathetic · magenta: sympathetic · blue: afferent', 620, 174, 'dyn-cap', unless=['n:*'])
for k, (a, b) in HEAD.items():
    text(a, 620, 150, 'dyn-big', when=O(k))
    text(b, 620, 174, 'dyn-cap', when=O(k))

# ════════ 8. motion ════════
CH_F = join(ESO, 'M1090 520 C1200 560 1330 640 1300 740 C1260 820 1000 790 912 748', 'M912 748 H780 Q712 748 712 812 V960')
CH_M = join('M712 960 V940 Q712 1000 776 1000 H960', SI, 'M680 1455 C650 1500 620 1520 620 1540', 'M620 1540 V1080 Q620 1040 662 1040 H1230')
CH_H = join(COL_B, COL_C)
FAST, SLOW = 1.9, 0.45
flows = [
  dict(d=CH_F, len=plen(CH_F), speed=50, r=7, base=dict(ch=6),
       mods=[dict(when=O('vag'), speed=FAST), dict(when=O('cel'), speed=SLOW, set=dict(ch=3))]),
  dict(d=CH_M, len=plen(CH_M), speed=60, r=7, base=dict(ch=10),
       mods=[dict(when=O('vag'), speed=FAST), dict(when=O('smg'), speed=SLOW, set=dict(ch=5))]),
  dict(d=CH_H, len=plen(CH_H), speed=50, r=8, base=dict(ch=6),
       mods=[dict(when=O('pel'), speed=FAST), dict(when=O('img'), speed=SLOW, set=dict(ch=3))]),
  dict(d=AO, len=plen(AO), speed=160, r=7, base=dict(bl=5)),
]
def blood(d, k, art):
    return dict(d=d, len=plen(d), speed=120, r=6, base=dict(bl=2), when=None,
                mods=[dict(when=O(k), set=dict(bl=0)), dict(when=O(art), add=dict(bl=1))])
for d in (join(CEL0, LGA), join(CEL0, SPLA), join(CEL0, CHA)):
    flows.append(blood(d, 'cel', 'fg'))
for b in (SMA_SI, SMA_RC, SMA_MC, SMA_DU):
    flows.append(blood(join(SMA0, b), 'smg', 'mg'))
for b in (IMA_LC, IMA_SG, IMA_SR):
    flows.append(blood(join(IMA0, b), 'img', 'hg'))
for f in flows:
    if f.get('when') is None: f.pop('when', None)
# watershed: the ends of the middle colic and left colic run almost dry
flows[-3]['mods'].append(dict(when=O('ws'), set=dict(bl=0)))          # IMA → left colic
flows[-5]['mods'].append(dict(when=O('ws'), set=dict(bl=1)))          # SMA → middle colic
flows[-1]['mods'].append(dict(when=O('ws'), set=dict(bl=1)))          # IMA → superior rectal
# nerve signals
def sig(d, kind, when, n=None):
    L = plen(d)
    return dict(d=d, len=L, speed=170, r=6, when=when, base={kind: n or max(2, min(6, L // 230))})
for b in (VAG_ST, VAG_SI, VAG_CO):
    flows.append(sig(join(VAG, b), 'para', O('vag')))
flows.append(sig(PEL, 'para', O('pel')))
flows.append(sig(PEL_UP, 'para', O('pel')))
SYM_POST = dict(cel=[join('M1765 545 H1700', LGA), join('M1765 545 H1700', CHA)],
                smg=[join('M1765 650 H1720 C1600 690 1470 790 1400 900', SMA_SI), join('M1765 650 H1720 C1600 690 1470 790 1400 900', SMA_RC)],
                img=[join('M1765 800 H1730 C1690 820 1660 900 1650 980', IMA_SG), join('M1765 800 H1730 C1690 820 1660 900 1650 980', IMA_SR)])
for k, pre in (('cel', GSP), ('smg', SSP), ('img', LSP)):
    flows.append(sig(pre, 'sym', O(k), 3))
    for d in SYM_POST[k]:
        flows.append(sig(d, 'sym', O(k)))
# afferents: vagal (gut → nodose → medulla) and splanchnic (gut → DRG)
def rev(d):   # reverse a path made of M + C/L segments only (for the afferent direction)
    toks = re.findall(r'[MLC]|-?\d+(?:\.\d+)?', d)
    segs, i, cur = [], 0, None
    while i < len(toks):
        if toks[i] in 'MLC': cur = toks[i]; i += 1
        n = 1 if cur in 'ML' else 3
        pts = [(toks[i + 2 * j], toks[i + 2 * j + 1]) for j in range(n)]; i += 2 * n
        segs.append((cur, pts))
    start = segs[0][1][0]; out = []; prev = start
    for cmd, pts in segs[1:]:
        out.append((cmd, pts, prev)); prev = pts[-1]
    s = f'M{prev[0]} {prev[1]}'
    for cmd, pts, p0 in reversed(out):
        if cmd == 'L': s += f' L{p0[0]} {p0[1]}'
        else: s += f' C{pts[1][0]} {pts[1][1]} {pts[0][0]} {pts[0][1]} {p0[0]} {p0[1]}'
    return s
for b in (VAG_ST, VAG_SI):
    flows.append(sig(rev(join(VAG, b)), 'aff', O('nod')))
for d in (AFF_F, AFF_M, AFF_H):
    flows.append(sig(d, 'aff', O('drg', 'ref'), 3))

# ════════ 9. sites (tap → card) ════════
sites = [
  dict(x=1765, y=545, n=[1, 0], w=30, t='rec', l='Celiac ganglion', s='on the celiac trunk · T12/L1', ions=[], c='ganglioninh',
       lx=1870, ly=530, la='start', boost=O('cel'), sfx=dict(boost=' — firing')),
  dict(x=1765, y=650, n=[1, 0], w=30, t='rec', l='Superior mesenteric ganglion', s='on the SMA · L1', ions=[], c='ganglioninh',
       lx=1870, ly=630, la='start', boost=O('smg'), sfx=dict(boost=' — firing')),
  dict(x=1765, y=800, n=[1, 0], w=30, t='rec', l='Inferior mesenteric ganglion', s='on the IMA · L3', ions=[], c='ganglioninh',
       lx=1870, ly=790, la='start', boost=O('img'), sfx=dict(boost=' — firing')),
  dict(x=440, y=400, n=[-1, 0], w=26, t='rec', l='Nodose ganglion', s='vagal afferent cell bodies', ions=[], c='viscafferent',
       lx=410, ly=420, la='end', boost=O('nod'), sfx=dict(boost=' — signalling')),
  dict(x=2160, y=685, n=[-1, 0], w=22, t='rec', l='Dorsal root ganglia', s='splanchnic afferent cell bodies', ions=[], c='viscafferent',
       lx=2130, ly=750, la='end', boost=O('drg', 'ref'), sfx=dict(boost=' — signalling')),
  dict(x=1520, y=1000, n=[1, 0], w=40, t='rec', l='Watershed', s='SMA ↔ IMA', ions=[], c='mesenteric',
       lx=1600, ly=1080, la='start', low=O('ws', 'img', 'smg'), sfx=dict(low=' — low flow')),
  dict(x=820, y=414, n=[0, -1], w=10, t='para', l='', aria='autonomic wiring', ions=[], c='ansreg'),
  dict(x=1830, y=420, n=[1, 0], w=26, t='rec', l='', aria='abdominal aorta — gut arteries by region', ions=[], c='gutarteries'),
  dict(x=260, y=1700, n=[0, -1], w=10, t='rec', l='Referred pain', s='where visceral pain is felt', ions=[], c='viscpain',
       lx=260, ly=1770, la='start', when=O('ref')),
]

notes = {
  '': 'Each gut division has its own artery, its own sympathetic ganglion on that artery, and its own parasympathetic nerve: '
      'foregut — celiac trunk, celiac ganglion, vagus; midgut — SMA, superior mesenteric ganglion, vagus; hindgut — IMA, '
      'inferior mesenteric ganglion, pelvic splanchnics. Pick one and follow the dots.',
  'n:fg': 'The foregut runs from the esophagus to the major duodenal papilla and includes the liver, gallbladder and pancreas; '
          'the celiac trunk (T12/L1) feeds it through the left gastric, splenic and common hepatic arteries. Foregut pain is '
          'felt in the epigastrium.',
  'n:mg': 'The midgut runs from the duodenum past the major papilla to the proximal two-thirds of the transverse colon and is '
          'fed by the superior mesenteric artery (L1). An SMA embolus — often from atrial fibrillation — gives acute mesenteric '
          'ischemia, with periumbilical pain out of proportion to the exam.',
  'n:hg': 'The hindgut runs from the distal third of the transverse colon to the upper anal canal and is fed by the inferior '
          'mesenteric artery (L3). Its parasympathetic supply is the pelvic splanchnic nerves, not the vagus, and its pain is '
          'felt in the hypogastrium.',
  'n:ws': 'Where two arterial trees end — the splenic flexure (SMA ↔ IMA) and the rectosigmoid junction — blood flow is the '
          'first to fail in hypotension or emboli. Colonic (ischemic) colitis follows: crampy pain then hematochezia in an older '
          'adult, with a thumbprint sign on imaging.',
  'n:vag': 'The vagus is the parasympathetic nerve of the foregut and midgut, as far as the proximal two-thirds of the transverse '
           'colon. Its long preganglionic fibers synapse in the enteric plexuses: motility and secretion rise, sphincters relax and '
           'mucosal blood flow rises with digestion.',
  'n:pel': 'The pelvic splanchnic nerves (S2–S4) are the parasympathetics of the hindgut — distal transverse, descending and '
           'sigmoid colon, rectum and anal canal — densest in the sigmoid, rectum and anus, where they drive the defecation '
           'reflexes.',
  'n:cel': 'Preganglionic sympathetic fibers (thoracic splanchnics, typically T5–T9) synapse in the celiac ganglion on the celiac '
           'trunk; postganglionic fibers ride its branches to the foregut. Sympathetic tone slows motility and secretion, contracts '
           'the sphincters (here the pylorus) and constricts the vessels.',
  'n:smg': 'The superior mesenteric ganglion, wrapped around the SMA, relays sympathetic fibers (T9–T11 on the OMM chart) to the '
           'whole midgut territory: jejunum, ileum, ascending colon and proximal two-thirds of the transverse colon. Motility falls, '
           'the ileocecal sphincter tightens and the vessels constrict.',
  'n:img': 'The inferior mesenteric ganglion on the IMA relays sympathetic fibers (T12–L2 on the OMM chart; the lumbar splanchnics, L1–L2) to the hindgut: distal '
           'transverse, descending and sigmoid colon. Motility falls, the internal anal sphincter tightens and the vessels '
           'constrict.',
  'n:nod': 'About three-quarters of vagal fibers are afferent. Their cell bodies sit in the nodose (inferior vagal) ganglion and '
           'they carry stretch and chemical signals from the gut — and from the heart, aortic arch and lungs — to the solitary '
           'nucleus: the sensory limb of vagovagal reflexes such as receptive relaxation.',
  'n:drg': 'Visceral afferents that run back with the splanchnic (sympathetic) nerves have their cell bodies in the dorsal root '
           'ganglia and end in the dorsal horn. They respond to stretch and chemical irritants — the route of visceral pain.',
  'n:ref': 'Visceral pain is dull and poorly localized and is felt in the skin served by the same spinal ganglia: foregut in the '
           'epigastrium, midgut around the umbilicus (T10 — early appendicitis), hindgut in the hypogastrium.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Gut motility & secretion', mods=[R(PARA, 1), R(SYM, -1)]),
  dict(l='Sphincter tone', mods=[R(SYM, 1), R(PARA, -1)]),
  dict(l='Gut blood flow', mods=[R(PARA, 1), R(SYM + O('ws'), -1)]),
]

dyn = dict(
  kinds=dict(ch=['chyme', '--dk10', 'chyme'], bl=['blood', '--dk2', 'blood'], para=['nerve', '--dk3', 'parasympathetic'],
             sym=['nerve', '--dk7', 'sympathetic'], aff=['nerve', '--dk1', 'afferent']),
  groups=[['chyme', 'Chyme'], ['blood', 'Blood'], ['nerve', 'Nerve signals']],
  switches=[dict(id='n', label='Pick a gut division, a nerve or a ganglion', type='one', options=[
      ['fg', 'Foregut — celiac trunk', 'gutarteries'], ['mg', 'Midgut — superior mesenteric artery', 'gutarteries'],
      ['hg', 'Hindgut — inferior mesenteric artery', 'gutarteries'], ['ws', 'Splenic flexure watershed', 'mesenteric'],
      ['vag', 'Vagus nerve — foregut & midgut'], ['pel', 'Pelvic splanchnic nerves (S2–S4)'],
      ['cel', 'Celiac ganglion', 'ganglioninh'], ['smg', 'Superior mesenteric ganglion', 'ganglioninh'],
      ['img', 'Inferior mesenteric ganglion', 'ganglioninh'],
      ['nod', 'Nodose ganglion — vagal afferents', 'viscafferent'],
      ['drg', 'Splanchnic afferents · dorsal root ganglia', 'viscafferent'], ['ref', 'Referred visceral pain', 'viscpain']],
      sections=[['Arteries', ['fg', 'mg', 'hg', 'ws']], ['Parasympathetic', ['vag', 'pel']],
                ['Sympathetic ganglia', ['cel', 'smg', 'img']], ['Afferents & pain', ['nod', 'drg', 'ref']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI lecture notes (SDL 1, 4) · Robbins ch 17 · Guyton ch 63 · Moore ch 5 · Langman ch 15 · Fundamental Neuroscience ch 14 · '
      'Foundations of Osteopathic Medicine ch 6 · First Aid pp. 370–371, 393, 523')

NY1, NY2 = 1950, 2035
MAP = dict(
  id='gutnervsim', title='Foregut, Midgut & Hindgut: Arteries, Nerves & Referred Pain in Motion', topic='gi', after='gitract',
  sub='Pick a gut division, a nerve or a ganglion — the celiac trunk, SMA and IMA with their territories, the splenic-flexure '
      'watershed, the vagus and pelvic splanchnics, the celiac and mesenteric ganglia, vagal and splanchnic afferents — and watch '
      'blood, chyme and nerve signals change. Tap a ganglion or a vessel for its card',
  w=3500, h=2100,
  fa='370, 371, 393, 523', src=SRC,
  lanes=[('gvArt', 'Arteries', 'tca'), ('gvAut', 'Autonomic nerves', 'gluconeo'), ('gvAff', 'Afferents & pain', 'glycolysis')],
  comps=[],
  nodes=[
    ('gv1', 'Gut arteries by region', 300, NY1, 'gvArt', 'celiac · SMA · IMA', ['gutarteries'], 'hub'),
    ('gv2', 'Mesenteric ischemia', 690, NY1, 'gvArt', 'SMA embolus · watershed colitis', ['mesenteric']),
    ('gv3', 'Prevertebral ganglia', 1080, NY1, 'gvAut', 'celiac · SM · IM', ['ganglioninh']),
    ('gv4', 'Autonomic wiring', 1470, NY1, 'gvAut', 'transmitters, pre and post', ['ansreg']),
    ('gv6', 'Visceral afferents', 300, NY2, 'gvAff', 'nodose · dorsal root ganglia', ['viscafferent']),
    ('gv7', 'Referred visceral pain', 690, NY2, 'gvAff', 'epigastric · umbilical · hypogastric', ['viscpain']),
  ],
  panels=[
    (2420, 1180, 1000, 'The three gut divisions (lecture SDL 1 · First Aid p. 371)', [
      ('Foregut · celiac · T12/L1', 'esophagus → duodenum to the papilla; liver, GB, pancreas · vagus'),
      ('Midgut · SMA · L1', 'distal duodenum → ⅔ transverse colon · vagus'),
      ('Hindgut · IMA · L3', 'distal ⅓ transverse colon → upper anal canal · pelvic splanchnics'),
      ('Watershed (FA p. 370)', 'splenic flexure (SMA–IMA) · rectosigmoid junction')]),
    (2420, 1470, 1000, 'Sympathetic relays and pain (OMM course chart · Foundations ch 6 · Moore ch 5)', [
      ('Celiac ganglion', 'typically T5–T9 → foregut · pain epigastric'),
      ('Superior mesenteric ganglion', 'T9–T11 → midgut · pain umbilical'),
      ('Inferior mesenteric ganglion', 'T12–L2 → hindgut · pain hypogastric'),
      ('Afferent cell bodies', 'vagal → nodose ganglion · splanchnic → dorsal root ganglia')]),
  ],
  dyn=dyn,
)
