# m57 — Pancreatic Juice & Bile in Motion (dynamic map, kit data)
# Left: the organs from the front — brain and vagus, liver, gallbladder, the bile ducts, stomach, the duodenal C-loop with
# the pancreas in it (main duct + common bile duct meeting at the ampulla, sphincter of Oddi), the small intestine down to the
# terminal ileum and the portal vein back to the liver. Right: one acinus and its duct cell (CCK and muscarinic receptors on the
# acinar cell; apical Cl⁻–HCO₃⁻ exchanger and CFTR, basolateral Na⁺–H⁺ exchanger, Na⁺/K⁺-ATPase and secretin receptor on the
# duct cell) and a drawn graph of juice composition against flow rate. One `one` switch in three sections — the phases
# (cephalic, gastric, intestinal), pancreatic juice (low flow, high flow, cystic fibrosis) and bile (gallbladder concentrating,
# bile salts and micelles, enterohepatic circulation, ileal resection). Seven readouts. gutabs covers absorption by segment,
# biliflow bilirubin, pancsim pancreatitis; this map is about how the two juices are made, controlled and recycled.
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt, SDL 13–14): exocrine pancreas = compound tubuloacinar serous gland;
#     acinar, centroacinar, ductal cells; ductal HCO₃⁻ via CFTR + apical Cl⁻/HCO₃⁻ exchanger, H⁺ out by basolateral Na⁺/H⁺
#     exchanger (and Na⁺/K⁺-ATPase), Na⁺ and water follow paracellularly; Na⁺/K⁺ constant at plasma level at every flow rate,
#     low flow → low HCO₃⁻ high Cl⁻, high flow → HCO₃⁻ up to ~140–145 mEq/L with a reciprocal Cl⁻ fall; secretin (S cells,
#     pH < 4.5) → ductal cAMP; CCK (I cells; fatty acids, peptides, amino acids) → acinar CCK1 receptors, low-volume enzyme
#     juice; ACh and CCK potentiate secretin; phases: cephalic ~20% of the enzyme response (vagal ACh on acinar cells, very
#     little water, enzymes stay in the ducts), gastric ~5–10% (distension, vagovagal), intestinal ~70–80% (SDL 13: ~80%);
#     bile 0.5–1.0 L/day; bile salts 50%, lecithin 40%, cholesterol 4%, pigments 2%; conjugation with glycine/taurine; micelles;
#     gallbladder: Oddi closed between meals, Na⁺/K⁺-ATPase on lateral membranes, AQP1 + AQP8, ~90% of water removed, bile
#     salts, cholesterol, bilirubin up to 10- to 20-fold; CCK → gallbladder contraction + Oddi relaxation, spurts; ~95% of bile
#     salts reach the terminal ileum and return by Na⁺–bile salt cotransport (ASBT) and the portal vein; pool ~2.5–3.0 g,
#     2–3 circuits per meal; returning bile salts inhibit 7α-hydroxylase; ileal resection → synthesis cannot keep up → pool
#     depleted → steatorrhea; islets 1–2% of the organ, 1–3 million, most in the tail; B 60–70% central, A 15–20% periphery,
#     D 5–10% periphery, PP 1–2% (also in exocrine tissue); granule sizes and shapes.
#   Costanzo ch 8 (course_sdl_4_7_physio): Fig. 8.22–8.25 text — CFTR in ductal cells, flow-rate relationship, sympathetic
#     activity inhibits pancreatic secretion; intestinal phase ~80%; bile salt pool 2.5 g, fecal loss ~600 mg/day; Box 8.1
#     ileal resection (steatorrhea, B12, bile acid diarrhea via colonic cAMP Cl⁻ secretion, cholestyramine).
#   Guyton ch 65 (course supplement p3): cephalic ~20%, gastric 5–10%, intestinal 70–80%; secretin pH < 4.5–5.0, HCO₃⁻ up to
#     145 mEq/L; trypsin inhibitor; ~1 L/day of juice; bile 600–1000 mL/day; gallbladder holds 30–60 mL; ~95% of bile salts
#     recirculated (~5% by diffusion early, ~90% active in the distal ileum); without bile salts up to 40% of fat lost; bile
#     salts + lecithin keep cholesterol in solution.
#   Pawlina ch 18 (course histology): acini, centroacinar cells, no striated ducts; gallbladder ~50 mL, ~90% of water removed;
#     AQP1/AQP8, lateral Na⁺/K⁺-ATPase; islet Tables 18.2/18.3; PP inhibits pancreatic enzyme and HCO₃⁻ secretion, bile
#     secretion and intestinal motility; capillaries perfuse A and D cells before B cells.
#   First Aid 2025 p. 58 (CF: CFTR, ↓ Cl⁻, H₂O, HCO₃⁻ secretion, thick mucus, pancreatic insufficiency, steatorrhea, A D E K,
#     ↑ immunoreactive trypsinogen) · p. 331 (islets: α peripheral, β central, δ interspersed) · p. 378 (secretin, CCK) ·
#     p. 380 (isotonic juice; low flow high Cl⁻, high flow high HCO₃⁻; enzymes) · p. 382 (bile; distal ileal loss → fat
#     malabsorption, bile acid diarrhea, calcium oxalate stones) · p. 403 (Crohn disease → gallstones).
#   Robbins ch 10 (CF: pancreatic abnormalities in 85–90%, ducts plugged, acini atrophy, only islets in fibrofatty stroma;
#     mutant CFTR with abnormal HCO₃⁻ conductance → acidic secretions).
# Conflicts (course wins): gallbladder concentration — lecture notes "up to 10- to 20-fold" (Pawlina text 10-fold, Guyton ~5-fold,
#   up to 20) → "10- to 20-fold"; bile salts returned — lecture/Guyton/Costanzo ~95%, Pawlina ~90% → "about 95%"; intestinal
#   phase — lecture SDL 14 and Guyton 70–80%, SDL 13 and Costanzo ~80% → "about 70–80%"; α-cell position — lecture notes and
#   Pawlina text "periphery", Pawlina's rat figure legend says the strict rim is not the human pattern → card says "mainly at
#   the periphery".
# Cut for lack of a source giving a direction: juice volume in the cephalic and gastric phases (sources say only "little
#   water"), juice Cl⁻ in CF, any readout for the bile-salt/micelle option (a normal step, no change), fat absorption ↑.
# m58 pins (P2, P5): a "Bile acids" section — conjugation with glycine/taurine, secondary bile acids (deoxycholic,
#   lithocholic), the bile salt pool (lecture notes pp. 77–79: primary acids via 7α-hydroxylase, bacterial C-7
#   dehydroxylation, conjugation lowers pKa ~7 → 1–4, pool 2.5–3.0 g recirculating 2–3 times per meal, 12–30 g/day, returning
#   salts inhibit 7α-hydroxylase; Pawlina Table 18.1 primary vs secondary; Costanzo ch 8 pool 2.5 g, fecal loss ~600 mg/day;
#   FA p. 382 glycine/taurine, 7α-hydroxylase rate-limiting). No readout arrows for these normal steps. A "Bile acid
#   synthesis" option was left out (its only question gain was doubtful). The gastric-phase option now opens the
#   `digphases` card (Guyton ch 65 / Costanzo ch 8 phases).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

CZ8, GY65, PW18, RB10 = full('Costanzo', 8), full('Guyton', 65), full('Pawlina', 18), full('Robbins', 10)
SRC = [CZ8, GY65, PW18, RB10]

O = lambda *k: ['p:' + x for x in k]
PHASE = O('ceph', 'gast', 'intest')
VAGAL = O('ceph', 'gast', 'intest')
SECR = O('intest', 'high')
GUTBILE = O('intest', 'bs', 'ehc', 'ileal', 'secba', 'pool')

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
def XM(x, y, s=14):
    return (f'<circle cx="{x}" cy="{y}" r="{s + 9}" style="fill:var(--surface);opacity:.92"/>'
            f'<path class="dyn-lesion" d="M{x - s} {y - s} L{x + s} {y + s} M{x + s} {y - s} L{x - s} {y + s}"/>')
def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))

text('Pancreatic juice and bile — how each is made, released and recycled', 160, 80, 'dyn-big')
text('left: the organs from the front (the patient’s right on your left) · right: one acinus and its duct cell, and the juice by flow rate', 160, 104, 'dyn-cap')

# ════════ the organs ════════
# brain and vagus
add('<rect x="880" y="140" width="300" height="52" rx="22" class="dyn-soft"/>')
text('brain — sight, smell, taste', 1030, 172, 'nf-l2', 'middle')
add('<rect x="880" y="140" width="300" height="52" rx="22" style="fill:none;stroke:var(--accent);stroke-width:4"/>', when=O('ceph'))
VAG_ST = [(1030, 192), (1030, 290)]
VAG_PA = [(1150, 192), (1300, 300), (1320, 560), (1290, 820)]
add(f'<path d="{P(VAG_ST)}" class="dyn-dash"/><path d="{P(VAG_PA)}" class="dyn-dash"/>')
text('vagus (ACh)', 1290, 470, 'nf-l2', 'end')

# liver (front view, as in portsim)
LIVER = 'M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z'
FALC = 'M58 62 C56 40 56 20 58 6'
import re as _re
def sc(d, x, y, w, h): return _re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}', d)
add(f'<path d="{sc(LIVER, 170, 230, 620, 360)}" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>'
    f'<path d="{sc(FALC, 170, 230, 620, 360)}" style="fill:none;stroke:var(--dk6);stroke-width:2;opacity:.5"/>')
text('liver', 330, 360, 'dyn-big', 'middle')
text('hepatocytes make bile all day', 330, 386, 'nf-l2', 'middle')
text('bile acids + glycine or taurine → bile salts', 330, 412, 'nf-l2', 'middle', when=O('conj'))
text('pool ~2.5–3 g, 2–3 circuits a meal', 330, 412, 'nf-l2', 'middle', when=O('pool'))

# gallbladder (pear-shaped, below the liver)
GB = 'M300 650 C300 610 330 590 370 590 C420 592 450 615 450 650 C450 720 420 780 375 790 C335 795 300 760 300 650 Z'
GBS = 'M318 660 C318 628 342 612 372 612 C410 614 432 632 432 660 C432 716 410 764 375 772 C344 776 318 748 318 660 Z'
add(f'<path d="{GB}" style="fill:var(--dk5);fill-opacity:.18;stroke:var(--dk5);stroke-width:4"/>', unless=O('intest', 'gbconc'))
add(f'<path d="{GB}" style="fill:var(--dk5);fill-opacity:.4;stroke:var(--dk5);stroke-width:5"/>', when=O('gbconc'))
add(f'<path d="{GBS}" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--accent);stroke-width:5"/>', when=O('intest'))
text('gallbladder', 375, 820, 'nf-l1', 'middle')
text('squeezes (CCK)', 375, 844, 'nf-l2', 'middle', when=O('intest'))
text('Na⁺ out, water follows (aquaporins)', 375, 844, 'nf-l2', 'middle', when=O('gbconc'))

# bile ducts: common hepatic duct, cystic duct, common bile duct to the ampulla
CHD = [(520, 560), (520, 650)]
CYS = [(445, 625), (520, 650)]
CBD = [(520, 650), (560, 740), (630, 800), (640, 860), (600, 915)]
for pts in (CHD, CYS, CBD):
    add(f'<path d="{P(pts)}" style="fill:none;stroke:var(--dk5);stroke-width:12;stroke-linecap:round;opacity:.55"/>')
text('common bile duct', 660, 790, 'nf-l2')

# stomach (J shape) and duodenum
STOM = ('M940 330 C960 270 1090 260 1140 330 C1190 400 1200 570 1130 660 C1070 740 930 775 820 760 L805 712 '
        'C910 710 1000 680 1040 610 C1080 540 1060 430 1000 410 C965 400 940 380 940 330 Z')
add(f'<path d="{STOM}" style="fill:var(--dk3);fill-opacity:.12;stroke:var(--dk3);stroke-width:4"/>', unless=O('gast'))
add(f'<path d="{STOM}" style="fill:var(--dk3);fill-opacity:.3;stroke:var(--accent);stroke-width:5"/>', when=O('gast'))
text('stomach', 1090, 470, 'nf-l1', 'middle')
text('food stretches it', 1090, 494, 'nf-l2', 'middle', when=O('gast'))
DUO = 'M805 738 C720 742 620 740 585 785 L575 1020 C578 1068 620 1088 690 1088 L900 1088 C960 1083 985 1052 990 1010'
add(dict(tube=DUO, w=40, color='--dk7'))
text('duodenum', 760, 1130, 'nf-l1', 'middle')

# pancreas in the C-loop, main duct to the ampulla
PANC = ('M640 830 C700 800 780 828 840 828 C950 820 1100 800 1265 828 C1290 858 1272 898 1240 904 C1100 918 960 930 870 936 '
        'C840 980 800 1025 725 1030 C665 1034 630 995 630 950 Z')
add(f'<path d="{PANC}" style="fill:var(--dk12);fill-opacity:.14;stroke:var(--dk12);stroke-width:4"/>', unless=O('cf'))
add(f'<path d="{PANC}" style="fill:var(--ink-3);fill-opacity:.22;stroke:var(--bad);stroke-width:4;stroke-dasharray:10 8"/>', when=O('cf'))
text('pancreas', 1200, 958, 'nf-l1', 'middle')
MPD = [(1240, 864), (1000, 878), (800, 900), (680, 912), (600, 918)]
add(f'<path d="{P(MPD)}" style="fill:none;stroke:var(--dk12);stroke-width:9;stroke-linecap:round;opacity:.6"/>')
for x in (760, 940, 1120):
    add(XM(x, 890 if x > 900 else 902, 10), when=O('cf'))
text('mucus plugs the ducts', 960, 960, 'nf-l2', when=O('cf'))
# ampulla + sphincter of Oddi
add('<circle cx="598" cy="918" r="15" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:7"/>', unless=O('intest'))
add('<circle cx="598" cy="918" r="15" style="fill:var(--surface);stroke:var(--ok);stroke-width:4"/>', when=O('intest'))
text('sphincter of Oddi', 545, 960, 'nf-l2', 'end')
text('closed', 545, 984, 'nf-l2', 'end', unless=O('intest'))
text('open (CCK)', 545, 984, 'nf-l2', 'end', when=O('intest'))
# S and I cells
text('S cells → secretin', 545, 884, 'nf-l2', 'end')
text('I cells → CCK', 545, 908, 'nf-l2', 'end')
add('<rect x="566" y="842" width="20" height="60" rx="8" style="fill:var(--accent);opacity:.55"/>', when=SECR)

# small intestine down to the terminal ileum, colon
SI = 'M990 1010 C1120 1000 1210 1060 1190 1140 C1170 1220 900 1190 860 1260 C820 1330 1000 1360 1120 1350 L1240 1350'
add(dict(tube=SI, w=34, color='--dk7'))
text('jejunum', 1215, 1120, 'nf-l2')
text('terminal ileum', 1130, 1418, 'nf-l1')
add('<path d="M1240 1350 C1290 1350 1300 1300 1300 1250 L1300 1160" style="fill:none;stroke:var(--dk7);stroke-width:46;opacity:.25;stroke-linecap:round"/>')
text('colon', 1320, 1210, 'nf-l2')
add(XM(1060, 1352, 16), when=O('ileal'))
text('resected', 1060, 1320, 'nf-l1', 'middle', when=O('ileal'))

# portal vein back to the liver
PV = 'M1110 1378 C900 1480 330 1470 260 1260 L250 560'
add(dict(vessel=PV, w=16, color='--dk9', mods=[dict(when=O('ileal'), d=-8)]))
text('portal vein', 270, 1010, 'nf-l2')

# micelle (bile salts round a fat core) in the jejunum
def micelle(cx, cy):
    s = f'<circle cx="{cx}" cy="{cy}" r="16" style="fill:var(--dk10);opacity:.7"/>'
    for a in range(0, 360, 36):
        x, y = cx + 24 * math.cos(math.radians(a)), cy + 24 * math.sin(math.radians(a))
        s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" style="fill:var(--dk6)"/>'
    return s
add(micelle(780, 1260) + micelle(1250, 1215), when=O('bs'))
text('micelle: bile salts round fatty acids', 640, 1320, 'nf-l2', when=O('bs'))
text('gut bacteria: cholic → deoxycholic acid,', 820, 1296, 'nf-l2', 'end', when=O('secba'))
text('chenodeoxycholic → lithocholic acid', 820, 1320, 'nf-l2', 'end', when=O('secba'))

# zoom link from the pancreas to the inset
add('<path d="M1270 830 L1380 640" class="dyn-dash"/>')

# ════════ inset: acinus + duct cell ════════
add('<rect x="1380" y="140" width="960" height="790" rx="24" class="dyn-soft"/>')
text('Inside the pancreas: acinus → duct', 1410, 184, 'dyn-big')
AC = (1560, 520)
for i in range(7):
    a0, a1 = math.radians(i * 360 / 7 + 4), math.radians((i + 1) * 360 / 7 - 4)
    ro, ri = 140, 46
    pts = [(AC[0] + ro * math.cos(a0), AC[1] + ro * math.sin(a0)), (AC[0] + ro * math.cos(a1), AC[1] + ro * math.sin(a1)),
           (AC[0] + ri * math.cos(a1), AC[1] + ri * math.sin(a1)), (AC[0] + ri * math.cos(a0), AC[1] + ri * math.sin(a0))]
    add('<path class="dyn-cell" d="M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts) + ' Z"/>', unless=O('cf'))
    add('<path class="dyn-cell dyn-dim" d="M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts) + ' Z"/>', when=O('cf'))
    am = (a0 + a1) / 2
    for r in (60, 74):
        gx, gy = AC[0] + r * math.cos(am), AC[1] + r * math.sin(am)
        add(f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="6" style="fill:var(--dk5)"/>', unless=O('cf'))
add(f'<circle cx="{AC[0]}" cy="{AC[1]}" r="34" class="nf-lumen" style="stroke:none"/>')
add(f'<ellipse cx="{AC[0] + 30}" cy="{AC[1]}" rx="16" ry="10" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:2"/>')
text('acinar cells', AC[0], AC[1] + 176, 'nf-l1', 'middle')
text('zymogen granules', AC[0], AC[1] + 200, 'nf-l2', 'middle')
text('centroacinar cell', 1650, 610, 'nf-l2')
add(f'<path d="M{AC[0] + 46} {AC[1] - 4} L1704 {AC[1] - 4}" style="stroke:var(--ink-3);stroke-width:2"/>')
# the duct: lumen band, then the duct cell, then blood
DY = 470                                   # duct lumen centre
add(dict(tube=f'M{AC[0] + 40} {AC[1]} C1660 {AC[1]} 1690 {DY} 1760 {DY} L2320 {DY}', w=40, color='--dk12'))
text('duct lumen → duodenum', 2310, 420, 'nf-l2', 'end')
CX0, CX1, CY0, CY1 = 1790, 2320, 510, 800
add(f'<rect x="{CX0}" y="{CY0}" width="{CX1 - CX0}" height="{CY1 - CY0}" rx="18" class="dyn-cell"/>', unless=O('cf'))
add(f'<rect x="{CX0}" y="{CY0}" width="{CX1 - CX0}" height="{CY1 - CY0}" rx="18" class="dyn-cell" style="stroke:var(--bad)"/>', when=O('cf'))
text('duct cell', 2055, 622, 'nf-l1', 'middle')
text('CO₂ + H₂O → H⁺ + HCO₃⁻ (carbonic anhydrase)', 2055, 646, 'nf-l2', 'middle')
add(dict(vessel='M1790 860 L2320 860', w=26, color='--nf-blood'))
text('blood', 2310, 908, 'nf-l2', 'end')
text('secretin arrives', 1800, 908, 'nf-l2', when=SECR)

# ════════ inset: composition vs flow rate (Costanzo Fig. 8.23, described in the text) ════════
GX0, GX1, GY0, GY1 = 1500, 2240, 1040, 1380
add('<rect x="1380" y="960" width="960" height="480" rx="24" class="dyn-soft"/>')
text('Juice composition and flow rate', 1410, 1000, 'dyn-big')
add(f'<path d="M{GX0} {GY0 - 10} L{GX0} {GY1} L{GX1 + 20} {GY1}" style="fill:none;stroke:var(--ink-2);stroke-width:3"/>')
text('flow rate →', (GX0 + GX1) // 2, GY1 + 34, 'nf-l2', 'middle')
text('ion', 1420, 1200, 'nf-l2')
text('conc.', 1420, 1222, 'nf-l2')
CUR = dict(na=(f'M{GX0} 1070 L{GX1} 1070', '--nf-na', 'Na⁺', 1075), hco3=(f'M{GX0} 1300 C1800 1270 2000 1170 {GX1} 1130', '--nf-hco3', 'HCO₃⁻', 1134),
           cl=(f'M{GX0} 1160 C1800 1190 2000 1270 {GX1} 1300', '--nf-cl', 'Cl⁻', 1305), k=(f'M{GX0} 1350 L{GX1} 1350', '--nf-k', 'K⁺', 1355))
for k, (d, col, lab, ly) in CUR.items():
    add(f'<path d="{d}" style="fill:none;stroke:var({col});stroke-width:6"/>')
    text(lab, GX1 + 14, ly, 'nf-l1')
for key, x, lab in (('low', 1560, 'low flow'), ('high', 2180, 'high flow')):
    w = O('low') if key == 'low' else O('high', 'intest')
    add(f'<path d="M{x} {GY0} L{x} {GY1}" style="stroke:var(--accent);stroke-width:5;stroke-dasharray:12 8"/>', when=w)
    text(lab, x, GY0 - 4, 'nf-l1', 'middle', when=w)

# ════════ kinds and motion ════════
KL = [('enz', '--dk5', 'enzymes'), ('hco3', '--nf-hco3', 'HCO₃⁻'), ('cl', '--nf-cl', 'Cl⁻'), ('h2o', '--nf-h2o', 'water'),
      ('na', '--nf-na', 'Na⁺'), ('h', '--nf-h', 'H⁺ · acid'), ('bs', '--dk6', 'bile salts'), ('fat', '--dk10', 'fat'),
      ('ach', '--dk9', 'ACh'), ('sec', '--dk2', 'secretin'), ('cck', '--dk11', 'CCK')]
kinds = {k: [k, c] for k, c, _ in KL}
groups = [[k, l] for k, _, l in KL]

flows = []
def fl(pts_or_d, base, when=None, unless=None, mods=None, sp=120, r=7, ln=None):
    d = pts_or_d if isinstance(pts_or_d, str) else P(pts_or_d)
    f = dict(d=d, len=ln or plen(pts_or_d), speed=sp, r=r, base=base)
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
# vagus
fl(VAG_ST, dict(ach=2), when=O('ceph', 'gast'))
fl(VAG_PA, dict(ach=3), when=VAGAL)
# acid chyme and fat from the stomach into the duodenum
fl([(1060, 600), (960, 700), (805, 738), (650, 748), (590, 800), (580, 1000)], dict(h=4, fat=2), when=O('intest'))
# secretin / CCK from the duodenal wall
fl([(590, 870), (660, 880), (720, 920)], dict(sec=2), when=SECR, sp=60)
fl([(570, 860), (500, 820), (440, 760)], dict(cck=2), when=O('intest'), sp=60)
# main pancreatic duct
fl(MPD, dict(cl=1), unless=O('cf'), sp=90, mods=[
   dict(when=O('low'), set=dict(cl=3)), dict(when=O('high'), set=dict(cl=0, hco3=5, h2o=2)),
   dict(when=O('intest'), set=dict(cl=0, hco3=4, h2o=2, enz=3)), dict(when=O('ceph', 'gast'), set=dict(enz=1), speed=0.4)])
# bile: liver → gallbladder between meals
fl(CHD + [(445, 625), (390, 680)], dict(bs=3), unless=O('intest'), sp=70)
# bile: gallbladder and liver → duodenum when CCK squeezes
fl([(390, 680), (445, 625)] + CBD[0:] + [(585, 960)], dict(bs=5), when=O('intest'), sp=110)
fl(CHD + CBD[1:], dict(bs=2), when=O('intest'), sp=110)
# bile salts down the small intestine
fl(SI, dict(bs=4), when=GUTBILE, ln=1000, mods=[dict(when=O('bs'), add=dict(fat=3))])
fl('M580 1000 L578 1060 C590 1080 630 1088 690 1088 L900 1088 C960 1083 985 1052 990 1010', dict(bs=2), when=GUTBILE, ln=500)
# return by the portal vein / loss to the colon
fl(PV, dict(bs=6), when=O('ehc', 'pool'), ln=1400, sp=160)
fl(PV, dict(bs=2), when=O('intest', 'bs'), ln=1400, sp=160)
fl('M1240 1350 C1290 1350 1300 1300 1300 1250 L1300 1160', dict(bs=1), when=O('ehc', 'pool', 'secba'), ln=250, sp=60)
fl('M1240 1350 C1290 1350 1300 1300 1300 1250 L1300 1160', dict(bs=6), when=O('ileal'), ln=250, sp=60)
# inset: hormones and ACh to the receptors, enzymes and fluid down the duct
fl([(1478, 240), (1478, 382)], dict(cck=2), when=O('intest'), sp=50)
fl([(1642, 240), (1642, 382)], dict(ach=2), when=VAGAL, sp=50)
fl([(2250, 860), (2250, 802)], dict(sec=2), when=SECR, sp=40)
fl([(AC[0], AC[1]), (1660, AC[1]), (1760, DY), (2320, DY)], dict(enz=2), when=PHASE, unless=O('cf'), sp=90,
   mods=[dict(when=O('ceph', 'gast'), speed=0.3), dict(when=O('intest'), add=dict(enz=2))])
fl([(1760, DY), (2320, DY)], dict(cl=2, na=1), unless=O('cf'), sp=90, mods=[
   dict(when=O('low'), set=dict(cl=4, na=2)), dict(when=SECR, set=dict(cl=0, na=2, hco3=5, h2o=3))])

# ════════ sites (tap targets) ════════
sites = [
  dict(x=1478, y=392, n=[0, -1], w=14, t='rec', l='CCK receptor', s='CCK1 · acinar', ions=[], c='cck', lx=1452, ly=304, la='end',
       need=O('intest'), closed='no signal'),
  dict(x=1642, y=392, n=[0, -1], w=14, t='rec', l='muscarinic (ACh)', s='vagus', ions=[], c='ansreg', lx=1668, ly=304, la='start',
       stop=['!p:*'] + O('low', 'high', 'cf', 'gbconc', 'bs', 'ehc', 'ileal', 'conj', 'secba', 'pool'), sfx=dict(stop=' — no signal')),
  dict(x=1890, y=CY0, n=[0, 1], w=12, t='ex', l='Cl⁻–HCO₃⁻ exchanger', s='apical', ions=[['hco3', 'in', 2], ['cl', 'out', 1]],
       lx=1810, ly=560, la='start', c='pancsec', boost=SECR, low=O('low'), stop=O('cf'), sfx=dict(stop=' — no Cl⁻ to swap')),
  dict(x=2120, y=CY0, n=[0, 1], w=12, t='ch', l='CFTR Cl⁻ channel', s='Cl⁻ back to the lumen', ions=[['cl', 'in', 2]],
       lx=2300, ly=560, la='end', c='cf', block=O('cf'), boost=SECR),
  dict(x=1890, y=CY1, n=[0, -1], w=12, t='ex', l='Na⁺–H⁺ exchanger', s='', ions=[['h', 'in', 1], ['na', 'out', 1]],
       lx=1810, ly=744, la='start', c='pancsec', boost=SECR, stop=O('cf')),
  dict(x=2060, y=CY1, n=[0, -1], w=12, t='pump', l='Na⁺/K⁺-ATPase', s='', ions=[['na', 'in', 1]],
       lx=2060, ly=700, la='start', c='nakpump'),
  dict(x=2250, y=CY1, n=[0, -1], w=12, t='rec', l='secretin receptor', s='cAMP', ions=[], lx=2300, ly=744, la='end',
       c='secretin', stop=['!p:*'] + O('ceph', 'gast', 'low', 'cf', 'gbconc', 'bs', 'ehc', 'ileal', 'conj', 'secba', 'pool'), sfx=dict(stop=' — no signal')),
  # gallbladder wall: pump and aquaporins (water leaves as it concentrates)
  dict(x=302, y=700, n=[-1, 0], w=10, t='aqp', l='', aria='Gallbladder aquaporins — water out', ions=[['h2o', 'out', 2]],
       c='aquaporins', unless=O('intest'), boost=O('gbconc')),
  dict(x=448, y=690, n=[1, 0], w=10, t='pump', l='', aria='Gallbladder Na⁺/K⁺-ATPase', ions=[['na', 'out', 1]],
       c='nakpump', unless=O('intest'), boost=O('gbconc')),
  # terminal ileum: Na⁺–bile salt cotransporter
  dict(x=1150, y=1333, n=[0, -1], w=14, t='co', l='', aria='Ileal Na⁺–bile salt cotransporter', ions=[['bs', 'out', 2]],
       c='bileacid', when=O('intest', 'bs', 'ehc', 'pool', 'secba'), boost=O('ehc', 'pool')),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Juice volume (water)', mods=[R(O('intest', 'high'), 1), R(O('low', 'cf'), -1)]),
  dict(l='Juice HCO₃⁻', mods=[R(O('intest', 'high'), 1), R(O('low', 'cf'), -1)]),
  dict(l='Juice Cl⁻', mods=[R(O('intest', 'high'), -1), R(O('low'), 1)]),
  dict(l='Enzyme secretion', mods=[R(O('ceph', 'gast', 'intest'), 1), R(O('cf'), -1)]),
  dict(l='Bile salts in gallbladder bile', mods=[R(O('gbconc'), 1), R(O('ileal'), -1)]),
  dict(l='Bile salts back to the liver', mods=[R(O('ehc'), 1), R(O('ileal'), -1)]),
  dict(l='Fat absorption', mods=[R(O('cf', 'ileal'), -1)]),
]

notes = {
  '': 'Between meals: the liver makes bile all day, the sphincter of Oddi is shut, so bile backs up into the gallbladder, which '
      'stores and concentrates it; the pancreas trickles a little Cl⁻-rich juice. Pick a phase, a flow rate or a bile step. '
      '↑ rises, ↓ falls, – no source gives a direction.',
  'p:ceph': 'Cephalic phase: the sight, smell and taste of food send impulses down the vagus, whose ACh acts directly on the '
            'acinar cells (muscarinic receptors). They release enzymes — about 20% of the meal’s enzyme output — with very little '
            'water, so most of it waits in the ducts until fluid comes later.',
  'p:gast': 'Gastric phase: food distends the stomach, and vagovagal and local enteric reflexes keep ACh on the acinar cells — another '
            '5–10% of the enzymes, still low in volume, so little reaches the duodenum yet.',
  'p:intest': 'Intestinal phase — about 70–80% of pancreatic secretion. Acid chyme (pH < 4.5) makes S cells release secretin: the '
              'duct cells pour out HCO₃⁻-rich water. Fatty acids and peptides make I cells release CCK: acinar enzymes, gallbladder '
              'contraction and an open sphincter of Oddi. ACh and CCK potentiate secretin.',
  'p:low': 'Low (basal) flow: the ducts add little, so the isotonic juice is mostly Na⁺, Cl⁻ and water — Cl⁻ high, HCO₃⁻ low. '
           'Na⁺ and K⁺ stay at their plasma concentrations at every flow rate.',
  'p:high': 'High flow, driven by secretin (cAMP): the duct cell makes HCO₃⁻ with carbonic anhydrase and swaps it for luminal Cl⁻ at '
            'the apical exchanger, while CFTR returns the Cl⁻ to the lumen. HCO₃⁻ climbs to about 145 mEq/L as Cl⁻ falls — base '
            'to neutralize duodenal acid so the enzymes work at pH 7–8.',
  'p:cf': 'Cystic fibrosis: misfolded CFTR never reaches the duct-cell membrane, so little Cl⁻, water or HCO₃⁻ is secreted; thick '
          'mucus plugs the ducts, and in 85–90% of patients the acini atrophy and fibrose (pancreatic insufficiency): steatorrhea, '
          'A, D, E, K deficiency. Trypsinogen backs up into the blood — the newborn screen.',
  'p:gbconc': 'Gallbladder concentrating bile: its columnar cells pump Na⁺, Cl⁻ and HCO₃⁻ into the spaces between them (Na⁺/K⁺-ATPase '
              'on the lateral membranes) and water follows through aquaporins (AQP1, AQP8). About 90% of the water leaves, so bile '
              'salts, cholesterol and bilirubin rise up to 10- to 20-fold.',
  'p:bs': 'Bile salts: bile acids (cholic, chenodeoxycholic) conjugated to glycine or taurine — water-soluble and amphipathic. They '
          'emulsify fat droplets for lipase, then line micelles that ferry fatty acids, monoglycerides and cholesterol to the brush '
          'border. In bile, bile salts and lecithin hold cholesterol in solution.',
  'p:ehc': 'Enterohepatic circulation: about 95% of bile salts are taken back, mostly by Na⁺–bile salt cotransport in the terminal '
           'ileum, and ride the portal vein to the liver, which resecretes them. The 2.5–3 g pool goes round 2–3 times a meal; '
           'returning bile salts inhibit 7α-hydroxylase, so the liver makes only what is lost in stool.',
  'p:ileal': 'Ileal resection or terminal-ileal Crohn disease: bile salts are not taken back and new synthesis cannot keep up, so the '
             'pool shrinks — steatorrhea and A, D, E, K loss; bile acids in the colon cause a secretory diarrhea; B12 is lost; '
             'free oxalate is absorbed → calcium oxalate stones; gallstones are more likely.',
  'p:conj': 'Conjugation: hepatocytes make the primary bile acids (cholic, chenodeoxycholic) from cholesterol — 7α-hydroxylase is '
            'the rate-limiting step — and conjugate primary and returning secondary bile acids with glycine or taurine '
            '(glycocholic, taurocholic acid). That lowers the pKa from about 7 to 1–4, so bile salts stay ionized and '
            'water-soluble in the duodenum.',
  'p:secba': 'Secondary bile acids: in the intestine, bacteria dehydroxylate the primary bile acids at C-7 — cholic acid becomes '
             'deoxycholic acid and chenodeoxycholic acid becomes lithocholic acid. They return to the liver with the rest and '
             'are conjugated again.',
  'p:pool': 'The bile salt pool is only about 2.5–3 g, so it recirculates 2–3 times per meal (12–30 g a day). Bile salts '
            'returning in portal blood inhibit 7α-hydroxylase, so the liver makes only the ~600 mg a day lost in stool; if '
            'ileal return fails, synthesis cannot keep pace and the pool shrinks.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='p', label='Phase, juice or bile step — pick one', type='one', options=[
      ['ceph', 'Cephalic phase', 'ansreg'], ['gast', 'Gastric phase', 'digphases'], ['intest', 'Intestinal phase', 'pancsec'],
      ['low', 'Low flow — Cl⁻-rich', 'pancsec'], ['high', 'High flow — secretin, HCO₃⁻-rich', 'pancsec'],
      ['cf', 'Cystic fibrosis (CFTR)', 'cf'],
      ['gbconc', 'Gallbladder concentrates bile', 'aquaporins'], ['bs', 'Bile salts · micelles', 'bileacid'],
      ['ehc', 'Enterohepatic circulation', 'bileacid'], ['ileal', 'Ileal resection', 'crohn'],
      ['conj', 'Conjugation — glycine · taurine', 'bileacid'],
      ['secba', 'Secondary bile acids · deoxycholic acid · lithocholic acid', 'bileacid'],
      ['pool', 'Bile salt pool', 'bileacid']],
      sections=[['Phases of pancreatic secretion', ['ceph', 'gast', 'intest']],
                ['Pancreatic juice', ['low', 'high', 'cf']],
                ['Bile', ['gbconc', 'bs', 'ehc', 'ileal']],
                ['Bile acids', ['conj', 'secba', 'pool']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI course lecture notes (SDL 13–14) · Costanzo ch 8 · Guyton ch 65 · Pawlina ch 18 · Robbins ch 10 · First Aid pp. 58, 331, 378, 380, 382, 403')

# ════════ the one new card (cardgap #6): islets and exocrine pancreas histology ════════
card('islets', 'Pancreas histology — acini, ducts & islet cells', 'reg', 'psPanc', 'Serous acini · centroacinar cells · islets of Langerhans', 1,
     'The exocrine pancreas is a <b>compound tubuloacinar serous gland</b>: pyramidal acinar cells with basophilic bases and '
     'apical zymogen granules, and <b>centroacinar cells</b> inside the acinus that begin the intercalated duct — a feature '
     'unique to the pancreas. The <b>islets of Langerhans</b> (about 1–3 million) are only 1–2% of the organ, most numerous in '
     'the tail, and are threaded by fenestrated capillaries.',
     ['<b>B (β) cells</b> 60–70%, mainly central: insulin; ~300 nm granules with a dense crystalline (angular) core and a clear halo',
      '<b>A (α) cells</b> 15–20%, mainly at the periphery: glucagon; ~250 nm granules with a dense round eccentric core',
      '<b>D (δ) cells</b> 5–10%, at the periphery: somatostatin; 300–350 nm granules with a homogeneous matrix',
      '<b>PP (F) cells</b> (with the other minor cells ~5% of islet tissue), also scattered in the exocrine tissue: pancreatic polypeptide inhibits pancreatic enzyme and '
      'HCO₃⁻ secretion, bile secretion and intestinal motility',
      'Capillaries reach the A and D cells before the central B cells; no striated ducts in the pancreas'],
     ['—'],
     ['β most and central, α next at the rim; islets crowd the tail'],
     [PW18],
     ['—'],
     ['islets of langerhans', 'islet of langerhans', 'islet cells', 'beta cell granules', 'delta cell granules', 'pp cells',
      'pancreatic polypeptide', 'exocrine pancreas', 'compound tubuloacinar'],
     fa='331')

MAP = dict(
  id='pbsecsim', title='Pancreatic Juice & Bile in Motion', topic='gi', after='gutabs',
  sub='Run the cephalic, gastric and intestinal phases of pancreatic secretion, change the flow rate and watch HCO₃⁻ and Cl⁻ '
      'trade places, break CFTR — then concentrate bile in the gallbladder, build micelles, send bile salts round the '
      'enterohepatic circulation and cut out the ileum. Tap a transporter or pin for its card',
  w=3500, h=1960,
  fa='58, 331, 378, 380, 382, 403', src=SRC,
  lanes=[('psPanc', 'Pancreatic juice', 'glycolysis'), ('psCtl', 'Control', 'ppp'), ('psBile', 'Bile', 'glycogen'),
         ('psDz', 'When it fails', 'tca')],
  comps=[],
  nodes=[
    ('ps1', 'Pancreatic secretions', 260, 1620, 'psPanc', 'enzymes + HCO₃⁻ juice', ['pancsec'], 'hub'),
    ('ps2', 'Acini, ducts & islets', 720, 1620, 'psPanc', 'histology', ['islets']),
    ('ps3', 'Secretin', 1150, 1620, 'psCtl', 'S cells · acid', ['secretin']),
    ('ps4', 'CCK', 1530, 1620, 'psCtl', 'I cells · fat, peptides', ['cck']),
    ('ps5', 'Vagal ACh', 1930, 1620, 'psCtl', 'cephalic · gastric', ['ansreg']),
    ('ps6', 'Bile salts & EHC', 260, 1720, 'psBile', 'ileum → portal vein', ['bileacid'], 'hub'),
    ('ps7', 'Micelles & fat uptake', 720, 1720, 'psBile', 'A, D, E, K too', ['nutabsorb']),
    ('ps8', 'Gallbladder concentrating', 1170, 1720, 'psBile', 'Na⁺ pump · aquaporins', ['aquaporins', 'nakpump']),
    ('ps9', 'Bilirubin in bile', 1650, 1720, 'psBile', 'conjugated → stool', ['bilicycle']),
    ('ps10', 'Cystic fibrosis', 260, 1820, 'psDz', 'CFTR', ['cf', 'cfcourse']),
    ('ps11', 'Pancreatic insufficiency', 720, 1820, 'psDz', 'steatorrhea', ['pancins', 'chronicpanc']),
    ('ps12', 'Ileal Crohn · resection', 1170, 1820, 'psDz', 'bile salts lost', ['crohn']),
    ('ps13', 'Gallstones', 1600, 1820, 'psDz', 'too little bile salt', ['gallstones']),
  ],
  panels=[
    (2420, 830, 1000, 'What drives the pancreas (course notes; Guyton ch 65; Costanzo ch 8)', [
      ('Vagal ACh', 'acinar cells: enzymes, little water'),
      ('CCK (fatty acids, peptides)', 'acinar CCK1 receptors: enzymes'),
      ('Secretin (acid, pH < 4.5)', 'duct cells: water + HCO₃⁻ to ~145 mEq/L'),
      ('All three together', 'potentiate one another'),
      ('Sympathetic', 'inhibits pancreatic secretion')]),
    (2420, 1060, 1000, 'Bile in numbers (course notes; Guyton ch 65)', [
      ('Made by the liver', '0.5–1.0 L a day'),
      ('Gallbladder', 'holds 30–60 mL · removes ~90% of the water'),
      ('Bile salt pool', '2.5–3 g · 2–3 circuits a meal'),
      ('Back from the ileum', 'about 95%'),
      ('No bile salts in the gut', 'up to 40% of dietary fat lost')]),
  ],
  dyn=dyn,
)
