# m58 — Saliva & Salivary Glands in Motion (dynamic map, kit data)
# Left: the head from the side (face looking left) with the parotid, submandibular and sublingual glands, their ducts into the
# mouth, the salivatory nuclei in the brainstem and the two parasympathetic routes (VII → chorda tympani → submandibular
# ganglion; IX → otic ganglion → auriculotemporal nerve), and the sympathetic route (T1–T3 → superior cervical ganglion →
# along the external carotid). Right: one acinus with its myoepithelial (basket) cells and M₃ / β receptors, the intercalated
# duct, a striated-duct cell with its luminal and basolateral transporters, the capillary under it, and a drawn graph of
# saliva ÷ plasma against flow rate. One `one` switch in five sections — the gland (acinar, ductal, myoepithelial cells), flow
# rate (low, high), nerves (parasympathetic, sympathetic), products (amylase, kallikrein), dry or swollen (xerostomia ·
# Sjögren, mumps). Seven readouts. No other moving map has saliva; the static map `oral` holds the gland cards.
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt p36–37, SDL 7): acinar initial saliva isotonic, plasma-like,
#     α-amylase, lingual lipase, mucins, sIgA; ductal cells (intercalated + striated) reabsorb Na⁺ and Cl⁻, secrete K⁺ and
#     HCO₃⁻, relatively water-impermeable → hypotonic; myoepithelial "basket" cells between basal membrane and basal lamina,
#     contract on neural stimulation, compress acini, shorten ducts, eject saliva; flow rate: high (~4 mL/min) → closest to
#     isotonic initial saliva, higher Na⁺ Cl⁻, lower K⁺; low (< 1 mL/min) → most hypotonic, lowest Na⁺ Cl⁻, highest K⁺;
#     HCO₃⁻ the exception, rises with flow; exclusively neural control, both limbs ↑ secretion, parasympathetic dominant;
#     VII and IX → submandibular and otic ganglia → ACh on muscarinic M₃ → IP₃/Ca²⁺ → large volume of watery enzyme-rich
#     saliva, myoepithelial contraction, vasodilation partly by kallikrein → bradykinin; drive ↑ food, taste (sour), smell,
#     touch, nausea, conditioned reflexes, ↓ fear, sleep, dehydration; sympathetic T1–T3 → superior cervical ganglion → NE on
#     β → adenylyl cyclase → cAMP → smaller volume of viscous, protein- and mucin-rich saliva; concurrent vasoconstriction
#     reduces blood supply and blunts fluid output.
#   Costanzo ch 8 (course_sdl_4_7_physio p23–26, p. 1865 region on amylase): 1 L/day; parotid serous, submandibular and
#     sublingual mixed; acinus → intercalated duct → striated duct; luminal Na⁺–H⁺ exchange, ENaC, CFTR, Cl⁻–HCO₃⁻ exchange,
#     H⁺–K⁺ exchange; basolateral Na⁺/K⁺-ATPase and Cl⁻ channels; kallikrein → bradykinin; max blood flow > 10× exercising
#     muscle per organ size; flow-rate figure (Fig. 8.14) text; muscarinic → IP₃/Ca²⁺ ↑ volume and enzymes; β → cAMP;
#     stimulation ↑ HCO₃⁻ and enzyme secretion and myoepithelial contraction; salivary amylase inactivated by gastric acid.
#   Guyton ch 65 (course supplement p3, file pp. 4, 7–11): sympathetic constricts gland vessels, so on top of copious secretion
#     it reduces secretion; 800–1500 mL/day, pH 6.0–7.0, ptyalin; resting Na⁺ and Cl⁻ ≈ 15 mEq/L (1/7–1/10 of plasma), K⁺
#     ≈ 30 mEq/L (7×), HCO₃⁻ 50–70 mEq/L (2–3×); maximal salivation: acinar output up to 20×, NaCl 1/2–2/3 of plasma, K⁺ only
#     4×; basal ~0.5 mL/min, mostly mucous; superior and inferior salivatory nuclei; sympathetic saliva slight and thicker;
#     xerostomia causes. Guyton ch 54: taste signals from the tractus solitarius to the salivatory nuclei.
#   Moore ch 9–10: IX (inferior salivatory nucleus, medulla) → otic ganglion → auriculotemporal nerve → parotid; VII (superior
#     salivatory nucleus, pons) → chorda tympani → submandibular ganglion → submandibular and sublingual glands; parotid duct
#     pierces the buccinator; sympathetic fibres from the superior cervical ganglion along the external carotid plexus are
#     vasoconstrictive and may reduce secretion.
#   Pawlina ch 16 (course_sdl_2_3_histo_foregut p67–73): basket cells around acini and along intercalated/striated ducts —
#     compress the acinus, shorten the ducts; striated ducts modify serous secretion; Sjögren: focal lymphocytic infiltration,
#     acini replaced, less flow.
#   Robbins ch 16: xerostomia (Sjögren, radiation, drugs — anticholinergics first); mumps the commonest viral sialadenitis,
#     mostly parotids. First Aid 2025 p. 167 (mumps: parotitis, orchitis, aseptic meningitis, pancreatitis) · p. 383
#     (sialadenitis from obstruction, S aureus, mumps, Sjögren) · p. 474 (Sjögren: xerostomia, anti-SSA/SSB, lip biopsy).
# Readout frame (the default note says so): the two cell options compare the saliva with plasma; low and high flow compare
#   with each other (sdl07_q16 asks it that way); nerves, products and diseases show the change they cause.
# Cut for lack of a source giving a direction: saliva volume for myoepithelial cells (the sources say "eject", not more
#   volume); HCO₃⁻ for sympathetic stimulation (Costanzo's "stimulation ↑ HCO₃⁻" is not given per limb); osmolarity,
#   Na⁺/Cl⁻ and K⁺ for either nerve; any readout for amylase and mumps; Cl⁻ direction through the ductal CFTR channel (drawn
#   without moving ions); HCO₃⁻ ÷ plasma at maximal flow (graph line has no end value).
# Source conflicts: HCO₃⁻ at low flow — Costanzo/lecture "lowest at low flow", Guyton "2–3× plasma at rest"; both drawn
#   (the graph line starts above plasma and rises). FA p. 236 lists α₂ on salivary glands as "inhibition of salivary
#   secretion"; Costanzo says sympathetic α receptors on acinar cells are activated but β matter more — left out.
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ8, GY65, GY54, PW16, MO9, MO10, RB16, RB8 = (full('Costanzo', 8), full('Guyton', 65), full('Guyton', 54), full('Pawlina', 16),
                                               full('Moore', 9), full('Moore', 10), full('Robbins', 16), full('Robbins', 8))
SRC = [CZ8, GY65, GY54, PW16, MO9, MO10, RB16, RB8]

O = lambda *k: ['s:' + x for x in k]
NERVE = O('para', 'sym')

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
TAG = 'nf-l1 dyn-tag'
def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))
HL = 'style="fill:none;stroke:var(--accent);stroke-width:6"'

text('Saliva — made by acini, reworked by ducts, run only by nerves', 160, 76, 'dyn-big')
text('left: the head from the side (face looking left) · right: one acinus and its duct, and saliva ÷ plasma by flow rate', 160, 100, 'dyn-cap')

# ════════ the head ════════
# skin: back of the head and neck; forehead → nose → lips → chin → front of the neck
add('<path d="M420 170 C650 120 1000 140 1130 330 C1200 450 1190 640 1120 760 C1080 830 1060 920 1060 1000 L1060 1190" '
    'class="dyn-line" style="stroke-width:3;fill:none;opacity:.7"/>')
add('<path d="M420 170 C300 220 250 330 260 420 C262 450 250 470 235 490 L170 600 Q160 625 190 635 L235 645 '
    'Q225 670 228 690 Q245 705 235 720 Q220 740 232 760 Q250 800 245 840 C260 880 330 900 420 905 '
    'C520 912 580 950 600 1010 L620 1190" class="dyn-line" style="stroke-width:3;fill:none;opacity:.7"/>')
# eye, mandible, ear
add('<path d="M300 440 Q330 425 360 440 Q330 452 300 440 Z" style="fill:var(--dyn-lost);opacity:.75"/>')
add('<path d="M270 830 C380 860 560 820 650 790 L668 560" class="dyn-line" style="stroke-width:5;fill:none;opacity:.25"/>')
text('mandible', 300, 872, 'nf-l2')
add('<path d="M770 500 C830 480 860 560 840 620 C830 650 800 652 788 630 C805 600 800 540 770 520" '
    'class="dyn-line" style="stroke-width:4;fill:none;opacity:.6"/>')
text('ear', 850, 470, 'nf-l2')
# mouth: palate, tongue
add('<path d="M250 690 L560 676" class="dyn-line" style="stroke-width:6;opacity:.35"/>')
text('palate', 400, 670, 'nf-l2', 'middle')
add('<path d="M250 722 C320 692 480 686 560 722 C562 760 480 790 300 776 C270 772 252 750 250 722 Z" '
    'style="fill:var(--dk11);fill-opacity:.15;stroke:var(--dk11);stroke-width:3"/>')
text('tongue', 420, 742, 'nf-l2', 'middle')

# parotid (in front of the ear), submandibular (under the mandible), sublingual (floor of the mouth)
PAR = 'M640 470 C700 455 755 490 752 560 C752 640 735 720 690 762 C660 784 625 764 620 724 C604 640 602 512 640 470 Z'
PAR_BIG = 'M615 440 C690 418 762 470 764 560 C766 660 748 760 690 800 C640 828 590 790 582 730 C562 640 562 488 615 440 Z'
add(f'<path d="{PAR}" style="fill:var(--dk5);fill-opacity:.2;stroke:var(--dk5);stroke-width:4"/>', unless=O('mumps'))
add(f'<path d="{PAR_BIG}" style="fill:var(--bad);fill-opacity:.16;stroke:var(--bad);stroke-width:5"/>', when=O('mumps'))
text('Parotid', 686, 560, 'nf-l1', 'middle')
text('serous', 686, 578, 'nf-l2', 'middle')
SMG = 'M410 836 C430 802 540 800 566 836 C582 872 540 894 486 893 C436 892 400 868 410 836 Z'
add(f'<path d="{SMG}" style="fill:var(--dk5);fill-opacity:.2;stroke:var(--dk5);stroke-width:4"/>')
text('Submandibular', 488, 852, 'nf-l1', 'middle')
text('mixed', 488, 870, 'nf-l2', 'middle')
SLG = 'M300 792 C318 772 392 768 414 788 C402 804 330 810 300 792 Z'
add(f'<path d="{SLG}" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>')
text('Sublingual', 250, 812, 'nf-l1', 'end')
# Sjögren: the glands shrink and fill with lymphocytes
for gx, gy in ((660, 520), (700, 640), (650, 700), (428, 826), (540, 878), (350, 790)):
    add(f'<circle cx="{gx}" cy="{gy}" r="7" style="fill:var(--dk8)"/><circle cx="{gx + 14}" cy="{gy + 6}" r="6" style="fill:var(--dk8)"/>',
        when=O('xer'))
# ducts into the mouth: parotid (Stensen) across the cheek, through the buccinator, opposite the upper 2nd molar;
# submandibular (Wharton) forward to the floor of the mouth beside the frenulum
STEN = [(622, 600), (470, 640), (450, 684)]
WHAR = [(420, 830), (300, 760)]
for pts in (STEN, WHAR):
    add(f'<path d="{P(pts)}" style="fill:none;stroke:var(--dk5);stroke-width:8;stroke-linecap:round;opacity:.6"/>')
text('parotid duct', 520, 612, 'nf-l2', 'middle')
text('dry mouth', 330, 650, TAG, 'middle', when=O('xer'))
text('parotitis — swollen, tender', 600, 420, TAG, 'middle', when=O('mumps'))
text('α-amylase starts starch here', 210, 560, TAG, 'end', when=O('amy'))

# brainstem with the salivatory nuclei
add('<path d="M930 360 L1030 360 C1046 430 1046 500 1030 540 L1020 760 L955 760 L945 540 C925 500 925 430 930 360 Z" '
    'class="dyn-cell" style="stroke-width:3"/>')
add('<path d="M936 540 Q985 556 1036 540" class="dyn-line" style="stroke-width:2;opacity:.4;fill:none"/>')
text('pons', 1050, 400, 'nf-l2')
text('medulla', 1040, 740, 'nf-l2')
for ny, lab in ((470, 'superior salivatory n.'), (620, 'inferior salivatory n.')):
    add(f'<circle cx="985" cy="{ny}" r="12" style="fill:var(--dk9);opacity:.8"/>')
    text(lab, 1006, ny + 5, 'nf-l2')
# VII: superior salivatory → chorda tympani → submandibular ganglion → submandibular + sublingual
VII = [(985, 470), (900, 520), (880, 760), (780, 846), (606, 846)]
VII_POST = [(606, 846), (566, 846)]
VII_SL = [(606, 846), (590, 900), (420, 930), (360, 806)]
# IX: inferior salivatory → otic ganglion → auriculotemporal nerve → parotid
IX = [(985, 620), (900, 700), (812, 700)]
IX_POST = [(812, 700), (760, 650), (746, 610)]
for pts, cond in ((VII, None), (VII_POST, None), (VII_SL, None), (IX, None), (IX_POST, None)):
    add(f'<path d="{P(pts)}" class="dyn-dash" style="stroke:var(--dk9)"/>')
    add(f'<path d="{P(pts)}" {HL}/>', when=O('para'))
add('<circle cx="606" cy="846" r="11" style="fill:var(--surface);stroke:var(--dk9);stroke-width:4"/>'
    '<circle cx="812" cy="700" r="11" style="fill:var(--surface);stroke:var(--dk9);stroke-width:4"/>')
text('VII · chorda tympani', 892, 800, 'nf-l2')
text('submandibular ganglion', 626, 880, 'nf-l2')
text('otic ganglion', 812, 736, 'nf-l2', 'middle')
text('IX', 850, 690, 'nf-l2', 'middle')
# sympathetic: T1–T3 → superior cervical ganglion → along the external carotid
add('<path d="M720 1190 C716 1080 700 960 700 860 L706 780" style="fill:none;stroke:var(--nf-blood);stroke-width:14;opacity:.35;stroke-linecap:round"/>')
text('external carotid', 690, 1120, 'nf-l2', 'end')
SYM_PRE = [(960, 1190), (960, 1010)]
SYM_POST = [(940, 980), (820, 980), (726, 940), (712, 800)]
SYM_SMG = [(726, 940), (600, 940), (560, 892)]
add('<ellipse cx="960" cy="985" rx="24" ry="34" style="fill:var(--surface);stroke:var(--dk2);stroke-width:4"/>')
text('superior cervical ganglion', 994, 990, 'nf-l2')
text('T1–T3', 980, 1170, 'nf-l2')
for pts in (SYM_PRE, SYM_POST, SYM_SMG):
    add(f'<path d="{P(pts)}" class="dyn-dash" style="stroke:var(--dk2)"/>')
    add(f'<path d="{P(pts)}" {HL}/>', when=O('sym'))

# key strip under the head
text('dashed lines are nerves: parasympathetic (ACh) from the brainstem nuclei, sympathetic (NE) from T1–T3', 160, 1240, 'dyn-cap')

# ════════ inset: acinus → ducts ════════
BX0, BY0, BX1, BY1 = 1240, 140, 2340, 990
add(f'<rect x="{BX0}" y="{BY0}" width="{BX1 - BX0}" height="{BY1 - BY0}" rx="24" class="dyn-soft"/>')
text('Inside the gland: acinus → intercalated duct → striated duct', 1270, 184, 'dyn-big')
AC = (1420, 540)
RO, RI = 130, 40
cell_paths = []
for i in range(7):
    a0, a1 = math.radians(i * 360 / 7 + 4), math.radians((i + 1) * 360 / 7 - 4)
    pts = [(AC[0] + RO * math.cos(a0), AC[1] + RO * math.sin(a0)), (AC[0] + RO * math.cos(a1), AC[1] + RO * math.sin(a1)),
           (AC[0] + RI * math.cos(a1), AC[1] + RI * math.sin(a1)), (AC[0] + RI * math.cos(a0), AC[1] + RI * math.sin(a0))]
    cell_paths.append('M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts) + ' Z')
for d in cell_paths:
    add(f'<path class="dyn-cell" d="{d}"/>', unless=O('xer'))
    add(f'<path class="dyn-cell dyn-dim" d="{d}"/>', when=O('xer'))
for i in range(7):
    am = math.radians((i + 0.5) * 360 / 7)
    for r in (58, 74):
        add(f'<circle cx="{AC[0] + r * math.cos(am):.0f}" cy="{AC[1] + r * math.sin(am):.0f}" r="6" style="fill:var(--dk5)"/>',
            unless=O('xer'))
add(f'<circle cx="{AC[0]}" cy="{AC[1]}" r="{RO + 4}" {HL}/>', when=O('acin'))
for i in range(5):
    a = math.radians(i * 72 + 20)
    add(f'<circle cx="{AC[0] + 70 * math.cos(a):.0f}" cy="{AC[1] + 70 * math.sin(a):.0f}" r="8" style="fill:var(--dk8)"/>', when=O('xer'))
add(f'<circle cx="{AC[0]}" cy="{AC[1]}" r="30" class="nf-lumen" style="stroke:none"/>')
text('acinar cells', AC[0], AC[1] + 180, 'nf-l1', 'middle')
text('secretory granules', AC[0], AC[1] + 198, 'nf-l2', 'middle')
text('initial saliva: isotonic, plasma-like', AC[0], AC[1] + 224, TAG, 'middle', when=O('acin'))
text('lymphocytes replace acini', AC[0], AC[1] + 224, TAG, 'middle', when=O('xer'))
# myoepithelial (basket) cells hugging the acinus
MYO = []
for i in range(4):
    a = math.radians(i * 90 + 45)
    cx, cy = AC[0] + (RO + 8) * math.cos(a), AC[1] + (RO + 8) * math.sin(a)
    a0, a1 = a - 0.5, a + 0.5
    arc = (f'M{AC[0] + (RO + 8) * math.cos(a0):.0f} {AC[1] + (RO + 8) * math.sin(a0):.0f} '
           f'A{RO + 8} {RO + 8} 0 0 1 {AC[0] + (RO + 8) * math.cos(a1):.0f} {AC[1] + (RO + 8) * math.sin(a1):.0f}')
    MYO.append((arc, cx, cy))
for arc, cx, cy in MYO:
    add(f'<path d="{arc}" style="fill:none;stroke:var(--dk3);stroke-width:7;stroke-linecap:round"/>'
        f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="9" ry="6" style="fill:var(--dk3)"/>')
    add(f'<path d="{arc}" style="fill:none;stroke:var(--accent);stroke-width:11;stroke-linecap:round"/>', when=O('myo'))
text('basket cell', 1300, 410, 'nf-l2', 'end')
text('contracts: squeezes the acinus', AC[0], AC[1] + 224, TAG, 'middle', when=O('myo'))
# nerve endings on the acinus (receptors are sites)
add('<path d="M1360 230 L1360 380" class="dyn-dash" style="stroke:var(--dk9)"/><path d="M1490 230 L1490 384" class="dyn-dash" style="stroke:var(--dk2)"/>')
text('parasympathetic', 1350, 226, 'nf-l2', 'end')
text('sympathetic', 1500, 226, 'nf-l2')
# intercalated duct (narrow) then the striated duct (wide) to the mouth
DY = 470
add(dict(tube=f'M{AC[0] + 28} {AC[1]} L1560 {AC[1]} C1600 {AC[1]} 1610 {DY} 1650 {DY}', w=16, color='--dk5'))
add(dict(tube=f'M1650 {DY} L2330 {DY}', w=40, color='--dk5'))
text('intercalated duct', 1600, 600, 'nf-l2', 'middle')
text('→ excretory duct → mouth', 2320, 424, 'nf-l2', 'end')
CX0, CX1, CY0, CY1 = 1660, 2320, 500, 780
add(f'<rect x="{CX0}" y="{CY0}" width="{CX1 - CX0}" height="{CY1 - CY0}" rx="18" class="dyn-cell"/>')
add(f'<rect x="{CX0 - 6}" y="{CY0 - 6}" width="{CX1 - CX0 + 12}" height="{CY1 - CY0 + 12}" rx="22" {HL}/>', when=O('duct'))
for x in range(1700, 2300, 40):   # basal infoldings (the "striations")
    add(f'<path d="M{x} {CY1 - 4} L{x} {CY1 - 40}" class="dyn-line" style="stroke-width:2;opacity:.25"/>')
text('striated duct cell', 1990, 636, 'nf-l1', 'middle')
text('absorbs Na⁺ · Cl⁻ — secretes K⁺ · HCO₃⁻ — water-tight', 1990, 656, 'nf-l2', 'middle')
text('more NaCl out than KHCO₃ in, water stays → hypotonic', 1990, 694, TAG, 'middle', when=O('duct'))
text('long contact time: most NaCl out, most K⁺ in', 1990, 694, TAG, 'middle', when=O('low'))
text('little contact time: closest to plasma', 1990, 694, TAG, 'middle', when=O('high'))
# capillary under the duct and acinus
VY = 870
add(dict(vessel=f'M{BX0 + 30} {VY} L{BX1 - 20} {VY}', w=24, color='--nf-blood',
         mods=[dict(when=O('para', 'kall'), d=12), dict(when=O('sym'), d=-12)]))
text('capillary', BX1 - 30, VY + 42, 'nf-l2', 'end')
text('bradykinin → vasodilation', 1640, VY + 46, TAG, 'middle', when=O('kall'))
text('vasodilation', 1640, VY + 46, TAG, 'middle', when=O('para'))
text('vasoconstriction', 1640, VY + 46, TAG, 'middle', when=O('sym'))

# ════════ inset: saliva ÷ plasma by flow rate (Guyton ch 65 numbers; Costanzo Fig. 8.14 text) ════════
GX0, GX1, GT, GB = 1400, 2120, 1110, 1440
add(f'<rect x="{BX0}" y="1030" width="{BX1 - BX0}" height="480" rx="24" class="dyn-soft"/>')
text('Saliva ÷ plasma as flow rises', 1270, 1072, 'dyn-big')
def gy(r): return round(GT + (1 - math.log10(r)) / 2.155 * (GB - GT))
add(f'<path d="M{GX0} {GT - 10} L{GX0} {GB} L{GX1 + 20} {GB}" style="fill:none;stroke:var(--ink-2);stroke-width:3"/>')
add(f'<path d="M{GX0} {gy(1)} L{GX1} {gy(1)}" class="dyn-dash"/>')
text('= plasma', GX0 - 12, gy(1) + 5, 'nf-l2', 'end')
text('above', GX0 - 12, GT + 20, 'nf-l2', 'end')
text('below', GX0 - 12, GB - 8, 'nf-l2', 'end')
text('flow rate →', (GX0 + GX1) // 2, GB + 32, 'nf-l2', 'middle')
text('< 1 mL/min', GX0 + 60, GB + 32, 'nf-l2', 'middle')
text('~4 mL/min', GX1 - 40, GB + 32, 'nf-l2', 'middle')
def curve(r0, r1, sag=0):
    y0, y1 = gy(r0), gy(r1)
    return f'M{GX0} {y0} C{GX0 + 240} {y0 + sag} {GX1 - 240} {y1 + sag} {GX1} {y1}'
CUR = [('na', curve(1 / 8.5, 0.58, -10), '--nf-na', 'Na⁺ · Cl⁻  1/7–1/10 → 1/2–2/3', gy(0.58)),
       ('k', curve(7, 4, 6), '--nf-k', 'K⁺  7× → 4×', gy(4) - 4),
       ('hco3', curve(2.5, 3.6, 4), '--nf-hco3', 'HCO₃⁻  2–3× at rest, rises', gy(3.6) + 20)]
for k, d, col, lab, ly in CUR:
    add(f'<path d="{d}" style="fill:none;stroke:var({col});stroke-width:6"/>')
    text(lab, GX1 + 14, ly, 'nf-l1')
for key, x, lab in (('low', GX0 + 60, 'low flow'), ('high', GX1 - 40, 'high flow')):
    add(f'<path d="M{x} {GT - 10} L{x} {GB}" style="stroke:var(--accent);stroke-width:5;stroke-dasharray:12 8"/>', when=O(key))
    text(lab, x, GT - 18, 'nf-l1', 'middle', when=O(key))

# ════════ kinds and motion ════════
KL = [('na', '--nf-na', 'Na⁺'), ('cl', '--nf-cl', 'Cl⁻'), ('k', '--nf-k', 'K⁺'), ('hco3', '--nf-hco3', 'HCO₃⁻'),
      ('h', '--nf-h', 'H⁺'), ('h2o', '--nf-h2o', 'water'), ('enz', '--dk5', 'amylase · enzymes'), ('muc', '--dk10', 'mucin'),
      ('kal', '--dk11', 'kallikrein · bradykinin'), ('ach', '--dk9', 'ACh'), ('ne', '--dk2', 'NE'), ('bl', '--nf-blood', 'blood')]
kinds = {k: [k, c, l] for k, c, l in KL}
groups = [[k, l] for k, _, l in KL]

flows = []
def fl(pts_or_d, base, when=None, unless=None, mods=None, sp=120, r=7, ln=None):
    d = pts_or_d if isinstance(pts_or_d, str) else P(pts_or_d)
    f = dict(d=d, len=ln or plen(pts_or_d), speed=sp, r=r, base=base)
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
SLOW = dict(when=O('low', 'xer'), speed=0.4)
FAST = dict(when=O('high', 'para'), speed=1.8)
# nerves in the head
for pts in (VII, VII_POST, VII_SL, IX, IX_POST):
    fl(pts, dict(ach=2), when=O('para'), sp=90)
for pts in (SYM_PRE, SYM_POST, SYM_SMG):
    fl(pts, dict(ne=2), when=O('sym'), sp=90)
# saliva down the ducts into the mouth
for pts in (STEN, WHAR):
    fl(pts, dict(h2o=2), sp=70, mods=[SLOW, FAST, dict(when=O('xer'), set=dict(h2o=1)), dict(when=O('amy'), add=dict(enz=2)),
                                       dict(when=O('sym'), add=dict(muc=2))])
# acinus → intercalated duct (initial saliva, plasma-like)
UP = [(AC[0], AC[1]), (1560, AC[1]), (1600, DY + 20), (1660, DY)]
fl(UP, dict(na=1, cl=1, h2o=2, enz=1), sp=80, mods=[
   SLOW, FAST, dict(when=O('acin'), add=dict(na=1, cl=1, k=1, hco3=1)), dict(when=O('para'), add=dict(h2o=2, enz=2)),
   dict(when=O('sym'), add=dict(enz=2, muc=2)), dict(when=O('amy'), add=dict(enz=3)), dict(when=O('myo'), speed=1.6),
   dict(when=O('xer'), set=dict(na=0, cl=0, h2o=1, enz=0))])
# striated duct lumen: the final saliva
DOWN = [(1660, DY), (2330, DY)]
fl(DOWN, dict(na=1, cl=1, k=1, hco3=1, h2o=2), sp=90, mods=[
   SLOW, FAST,
   dict(when=O('low'), set=dict(na=0, cl=0, k=3, hco3=0, h2o=1)),
   dict(when=O('high'), set=dict(na=3, cl=3, k=1, hco3=3, h2o=4)),
   dict(when=O('duct'), set=dict(na=0, cl=0, k=2, hco3=2, h2o=2)),
   dict(when=O('para'), set=dict(h2o=4, hco3=3, enz=3)),
   dict(when=O('sym'), add=dict(enz=2, muc=3)), dict(when=O('amy'), add=dict(enz=3)),
   dict(when=O('xer'), set=dict(na=0, cl=0, k=0, hco3=0, h2o=1))])
# transmitters onto the acinus
fl([(1360, 240), (1360, 376)], dict(ach=2), when=O('para'), sp=50)
fl([(1490, 240), (1490, 380)], dict(ne=2), when=O('sym'), sp=50)
# kallikrein out of the acinus → bradykinin at the capillary
fl([(1460, 660), (1520, 760), (1600, VY - 14)], dict(kal=3), when=O('kall', 'para'), sp=60)
# blood in the capillary
fl([(BX0 + 40, VY), (BX1 - 30, VY)], dict(bl=2), sp=110, mods=[dict(when=O('para', 'kall'), add=dict(bl=3), speed=1.5),
                                                              dict(when=O('sym'), set=dict(bl=1), speed=0.5)])

# ════════ sites (tap targets) ════════
STIM = O('para', 'sym', 'high')
sites = [
  dict(x=1360, y=AC[1] - RO - 6, n=[0, -1], w=12, t='rec', l='M₃ receptor', s='IP₃ / Ca²⁺', ions=[], c='ansreg',
       lx=1350, ly=300, la='end', boost=O('para')),
  dict(x=1490, y=AC[1] - RO + 4, n=[0, -1], w=12, t='rec', l='β receptor', s='cAMP', ions=[], c='ansreg',
       lx=1500, ly=300, la='start', boost=O('sym')),
  # luminal membrane of the striated-duct cell (label side = into the cell)
  dict(x=1720, y=CY0, n=[0, 1], w=12, t='ex', l='Na⁺–H⁺', s='', ions=[['na', 'out', 1], ['h', 'in', 1]],
       lx=1720, ly=548, c='salivaphys', boost=O('low', 'duct'), low=O('high'), sfx=dict(boost=' ↑', low=' ↓')),
  dict(x=1840, y=CY0, n=[0, 1], w=12, t='ch', l='ENaC', s='', ions=[['na', 'out', 2]],
       lx=1840, ly=548, c='salivaphys', boost=O('low', 'duct'), low=O('high'), sfx=dict(boost=' ↑', low=' ↓')),
  dict(x=1960, y=CY0, n=[0, 1], w=12, t='ch', l='CFTR', s='', ions=[],
       lx=1960, ly=548, c='cf'),
  dict(x=2080, y=CY0, n=[0, 1], w=12, t='ex', l='Cl⁻–HCO₃⁻', s='', ions=[['cl', 'out', 1], ['hco3', 'in', 1]],
       lx=2080, ly=548, c='salivaphys', boost=STIM + O('duct'), low=O('low'), sfx=dict(boost=' ↑', low=' ↓')),
  dict(x=2200, y=CY0, n=[0, 1], w=12, t='ex', l='H⁺–K⁺', s='', ions=[['k', 'in', 1], ['h', 'out', 1]],
       lx=2200, ly=548, c='salivaphys', boost=O('low', 'duct'), low=O('high'), sfx=dict(boost=' ↑', low=' ↓')),
  # basolateral membrane
  dict(x=1800, y=CY1, n=[0, -1], w=12, t='pump', l='Na⁺/K⁺-ATPase', s='', ions=[['na', 'in', 1], ['k', 'out', 1]],
       lx=1800, ly=740, c='salivaphys'),
  dict(x=2180, y=CY1, n=[0, -1], w=12, t='ch', l='Cl⁻ channel', s='', ions=[['cl', 'in', 1]],
       lx=2180, ly=740, c='salivaphys'),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Saliva volume', mods=[R(O('high', 'para', 'sym'), 1), R(O('low', 'xer'), -1)]),
  dict(l='Osmolarity', mods=[R(O('acin'), 0), R(O('duct', 'low'), -1), R(O('high'), 1)]),
  dict(l='Na⁺ · Cl⁻', mods=[R(O('acin'), 0), R(O('duct', 'low'), -1), R(O('high'), 1)]),
  dict(l='K⁺', mods=[R(O('acin'), 0), R(O('duct', 'low'), 1), R(O('high'), -1)]),
  dict(l='HCO₃⁻', mods=[R(O('acin'), 0), R(O('duct', 'high', 'para'), 1), R(O('low'), -1)]),
  dict(l='Enzymes · protein', mods=[R(O('para', 'sym'), 1)]),
  dict(l='Gland blood flow', mods=[R(O('para', 'kall'), 1), R(O('sym'), -1)]),
]

notes = {
  '': 'Resting saliva: acinar cells make a plasma-like fluid and the striated ducts rework it on its way to the mouth. Pick a '
      'cell, a flow rate, a nerve, a product or a disease. Arrows: for the two cells, the saliva compared with plasma; for '
      'low and high flow, compared with each other; for the rest, the change it causes; – no source gives a direction.',
  's:acin': 'Acinar cells make the initial saliva: isotonic, with Na⁺, K⁺, Cl⁻ and HCO₃⁻ close to plasma. They also secrete '
            'α-amylase, lingual lipase, mucins, IgA and kallikrein.',
  's:duct': 'Ductal cells of the intercalated and striated ducts absorb Na⁺ and Cl⁻ and secrete K⁺ and HCO₃⁻. More NaCl leaves '
            'than KHCO₃ enters, and the ducts are nearly water-tight, so water stays behind and the final saliva is hypotonic.',
  's:myo': 'Myoepithelial (basket) cells lie between the acinar and duct cells and the basal lamina. A nerve signal makes them '
           'contract, squeezing the acinus and shortening the ducts to push saliva toward the mouth.',
  's:low': 'Low flow (< 1 mL/min, as in dehydration): saliva lingers in the ducts, so the most Na⁺ and Cl⁻ is taken out and the '
           'most K⁺ added — the most hypotonic saliva. HCO₃⁻ is lowest, because its secretion is turned up only when '
           'salivation is stimulated.',
  's:high': 'High flow (about 4 mL/min, as with sour taste): little contact time in the ducts, so saliva comes closest to plasma — '
            'more Na⁺ and Cl⁻, less K⁺ than at low flow. HCO₃⁻ is the exception: stimulated ductal secretion makes it highest '
            'at high flow.',
  's:para': 'Parasympathetic (dominant): salivatory nuclei → VII (chorda tympani, submandibular ganglion) and IX (otic ganglion) → '
            'ACh on muscarinic M₃ receptors → IP₃/Ca²⁺. Copious watery, enzyme-rich saliva, basket-cell contraction and '
            'vasodilation; anticholinergic drugs dry the mouth.',
  's:sym': 'Sympathetic: T1–T3 → superior cervical ganglion → norepinephrine on β receptors → cAMP. It also raises secretion, '
           'but only a small volume of viscous, protein- and mucin-rich saliva, and its vasoconstriction cuts gland blood flow '
           '— so a frightened patient has a dry mouth.',
  's:amy': 'Salivary α-amylase (ptyalin), from the serous acinar cells, begins starch digestion in the mouth at saliva’s pH of '
           '6–7. Gastric acid inactivates it, so it does little overall; pancreatic amylase does most of the work.',
  's:kall': 'Kallikrein: during high salivary activity the acinar cells release it, and it cleaves high-molecular-weight kininogen '
            'into bradykinin, a potent vasodilator. That is why gland blood flow climbs with secretion — at its peak more than '
            '10 times that of exercising muscle, gram for gram.',
  's:xer': 'Xerostomia — too little saliva. In Sjögren syndrome lymphocytes infiltrate and destroy the salivary and lacrimal glands: '
           'dry mouth and dry eyes, fissured tongue, caries, anti-SSA/SSB, focal lymphocytic sialadenitis on lip biopsy. '
           'Anticholinergic and other drugs and head-and-neck radiation are the other big causes.',
  's:mumps': 'Mumps: the paramyxovirus is the commonest viral cause of sialadenitis, swelling the major salivary glands — above '
             'all the parotids. It also brings orchitis, aseptic meningitis and pancreatitis; MMR prevents it.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='s', label='Pick a cell, a nerve or a flow rate', type='one', options=[
      ['acin', 'Acinar cells', 'salivaphys'], ['duct', 'Ductal cells', 'salivaphys'],
      ['myo', 'Myoepithelial (basket) cells', 'salivaphys'],
      ['low', 'Low flow rate', 'salivaphys'], ['high', 'High flow rate', 'salivaphys'],
      ['para', 'Parasympathetic — muscarinic M₃ · IP₃/Ca²⁺', 'salivaphys'],
      ['sym', 'Sympathetic — beta receptors · cAMP', 'salivaphys'],
      ['amy', 'Salivary amylase', 'salivaphys'], ['kall', 'Kallikrein · bradykinin', 'salivaphys'],
      ['xer', 'Xerostomia · Sjögren', 'xerostomia'], ['mumps', 'Mumps parotitis', 'mumps']],
      sections=[['The gland', ['acin', 'duct', 'myo']],
                ['Flow rate', ['low', 'high']],
                ['Nerves', ['para', 'sym']],
                ['Products', ['amy', 'kall']],
                ['Dry or swollen', ['xer', 'mumps']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI course lecture notes (SDL 7) · Costanzo ch 8 · Guyton ch 54, 65 · Moore ch 9–10 · Pawlina ch 16 · Robbins ch 8, 16 · '
      'First Aid pp. 167, 383, 474')

MAP = dict(
  id='salivsim', title='Saliva & Salivary Glands in Motion', topic='gi', after='oral',
  sub='Watch acinar cells make a plasma-like saliva and the ducts turn it hypotonic, change the flow rate and see Na⁺, K⁺ and '
      'HCO₃⁻ shift, fire the parasympathetic and sympathetic nerves, release amylase and kallikrein — then dry the glands out '
      'or swell the parotid. Tap a transporter or receptor for its card',
  w=3500, h=1880,
  fa='167, 383, 474', src=SRC,
  lanes=[('svGl', 'The gland', 'glycolysis'), ('svCtl', 'Nerves', 'ppp'), ('svDz', 'Dry or swollen', 'tca')],
  comps=[],
  nodes=[
    ('sv1', 'Saliva & salivary glands', 260, 1600, 'svGl', 'acini · ducts · flow rate', ['salivaphys'], 'hub'),
    ('sv2', 'Cystic fibrosis', 760, 1600, 'svGl', 'CFTR on duct cells', ['cf']),
    ('sv3', 'Autonomic wiring', 260, 1700, 'svCtl', 'M₃ · β receptors', ['ansreg'], 'hub'),
    ('sv4', 'Solitary nucleus', 760, 1700, 'svCtl', 'taste → salivatory nuclei', ['nts']),
    ('sv5', 'Cranial nerve components', 1260, 1700, 'svCtl', 'VII · IX visceral motor', ['cncomponents']),
    ('sv6', 'Xerostomia', 260, 1800, 'svDz', 'drugs · Sjögren · radiation', ['xerostomia'], 'hub'),
    ('sv7', 'Sjögren syndrome', 760, 1800, 'svDz', 'dry mouth + dry eyes', ['sjogren']),
    ('sv8', 'Salivary gland disease', 1260, 1800, 'svDz', 'stones · sialadenitis · tumors', ['salivary']),
    ('sv9', 'Mumps', 1760, 1800, 'svDz', 'parotitis', ['mumps']),
  ],
  panels=[
    (2420, 820, 1000, 'Three glands, two nerve routes (Costanzo ch 8; Moore ch 9–10)', [
      ('Parotid', 'serous · IX → otic ganglion → auriculotemporal n.'),
      ('Submandibular', 'mixed · VII → chorda tympani → submandibular ganglion'),
      ('Sublingual', 'mixed · same VII route'),
      ('Sympathetic', 'T1–T3 → superior cervical ganglion → NE on β'),
      ('Drive ↑ / ↓', 'food, sour taste, smell, nausea, conditioning / fear, sleep, dehydration')]),
    (2420, 1060, 1000, 'Saliva in numbers (Costanzo ch 8; Guyton ch 65)', [
      ('Daily volume', 'about 1 L (800–1500 mL)'),
      ('pH', '6.0–7.0'),
      ('Flow', 'basal ~0.5 mL/min · stimulated ~4 mL/min'),
      ('Peak gland blood flow', '> 10× exercising muscle, per gram')]),
  ],
  dyn=dyn,
)
