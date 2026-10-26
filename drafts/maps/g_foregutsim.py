# m57 — Foregut Rotation & Buds in Motion (dynamic map, kit data)
# Top: the gut tube at week 5 (head on the left) — pharyngeal gut, foregut, midgut loop with the vitelline duct, hindgut —
# with the aorta and its celiac, SMA and IMA branches (blood moving). Below: the foregut as it ends up, front view (patient's
# right on your left): food runs esophagus → stomach → pylorus → duodenal C-loop → jejunum; bile runs liver → bile duct →
# major papilla; pancreatic juice runs the main duct to the major papilla and the accessory duct to the minor papilla.
# One `one` switch in two sections — normal development (gut tube divisions, stomach rotation, duodenal recanalization,
# liver bud, ventral bud rotation: each with its own close-up on the right) and defects (pyloric stenosis, biliary atresia,
# pancreas divisum, ectopic pancreas, midgut malrotation: each changes what moves). 6 readouts. New cards pancdev, foregutdev.
#
# Sources (all read in the corpus; course text wins for this block):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt): SDL 1 — four divisions and arteries; foregut/midgut junction
#     just distal to the liver bud = major papilla, so celiac (superior pancreaticoduodenal) + SMA (inferior
#     pancreaticoduodenal) supply; stomach rotation in the 5th week, 90° clockwise, left side → anterior, posterior wall →
#     greater curvature, left vagus → anterior trunk, right → posterior; AP-axis rotation (pylorus up and right); omental
#     bursa, lesser omentum pulled right, greater omentum, spleen in the dorsal mesogastrium (5th week); duodenal solid
#     stage weeks 5–6, vacuoles coalesce, lumen restored by weeks 8–10; atresia (complete failure) / stenosis (partial);
#     bilious vomiting in 80–85% of atresias (block distal to the papilla); Down syndrome; HPS: nNOS deficiency, macrolides,
#     3–6 weeks, projectile non-bilious vomiting (pylorus is proximal to the papilla), olive, hypochloremic hypokalemic
#     metabolic alkalosis, pyloromyotomy. SDL 11 — liver induction (FGF2, BMP), HNF3/HNF4; biliary atresia (perinatal ~80%
#     vs fetal form), presentation 2–6 weeks, acholic stools, cirrhosis by 3–6 months, Kasai, 50–60% of pediatric liver
#     transplants; pancreas from two buds, ventral swings behind, fuses weeks 5–8, ventral = uncinate + inferior/posterior
#     head, dorsal = body, tail, superior/anterior head; Wirsung = distal dorsal + whole ventral duct; Santorini = proximal
#     dorsal duct at the minor papilla; PDX1 (homozygous loss → agenesis), PAX4 + PAX6 → β δ PP, PAX6 alone → α; annular
#     pancreas (bifid ventral bud, D2), divisum (3–10%, ~5% pancreatitis), ectopic pancreas (~2% of autopsies; stomach and
#     duodenum; pain, inflammation, mucosal bleeding).
#   Langman 15e ch 15 (course_sdl_1_11_embryo): gut divisions, liver bud in mid week 3 into the septum transversum, stalk →
#     bile duct, ventral outgrowth → gallbladder + cystic duct, septum mesoderm → Kupffer/hematopoietic/connective cells,
#     lesser omentum, falciform; midgut herniation week 6, 270° counterclockwise around the SMA, return from week 10 (by
#     week 12); malrotation (90° only → colon on the left), reversed rotation.
#   Robbins (course_sdl_8_9_patho, course_sdl_19_patho, course_sdl_15_19_patho): pyloric stenosis, ectopic pancreas in the
#     pylorus can scar and obstruct the outlet, divisum, ectopic pancreas, PDX1 agenesis, biliary atresia.
#   First Aid 2025 pp. 364 (foregut to the ampulla; 90° clockwise; vagus; midgut herniation and 270°), 366 (pyloric
#     stenosis; duodenal atresia), 367 (buds, annular pancreas, divisum, spleen), 392 (malrotation: small bowel right, colon
#     left, Ladd bands → volvulus, duodenal obstruction), 401 (biliary atresia: ↑ direct bilirubin and GGT).
# Cuts: bilious vomiting arrow for malrotation (FA 392 says only "can lead to volvulus, duodenal obstruction"; Bootcamp says
#   volvulus vomit "may be bilious" — kept as words, no arrow); Langman's "approximately 28 weeks" for the duodenal solid
#   stage (the lecture notes give weeks 5–6, course notes win); holopros pin (no gut content); "narrow mesentery".
# m58 pins (P3, P7): four pancreas options in "Normal development" — dorsal bud, ventral bud, duct of Wirsung · duct of
#   Santorini, PDX1 · PAX4 · PAX6 (lecture notes SDL 11 pp. 63–65: bud fates, Wirsung = distal dorsal + whole ventral duct →
#   major papilla, Santorini = proximal dorsal duct → minor papilla or obliterated, PDX1 master factor / homozygous loss →
#   agenesis, PAX4 + PAX6 → β δ PP (gamma), PAX6 alone → α; Langman ch 15; FA p. 367) with close-ups; "Stomach rotation"
#   relabelled "… · dorsal mesogastrium" (lecture notes SDL 1; Langman ch 15: rotation pulls the dorsal mesogastrium left →
#   omental bursa). No readout arrows for normal steps. 14 options.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

LG15, RB17, RB18, RB19, MO5 = full('Langman', 15), full('Robbins', 17), full('Robbins', 18), full('Robbins', 19), full('Moore', 5)
BC_EMB = 'Bootcamp.com Gastroenterology — Embryology'

# ── new cards ──
card('pancdev', 'Pancreas development — dorsal & ventral buds', 'reg', 'fgPanc', 'Two duodenal buds fuse into one gland', 1,
     'Two endodermal buds grow from the duodenum: the <b>dorsal bud</b> in the dorsal mesentery and the <b>ventral bud</b> beside '
     'the bile duct. As the duodenum turns to the right and becomes C-shaped, the ventral bud swings dorsally around it to lie '
     '<b>below and behind</b> the dorsal bud, and their tissue and ducts fuse (weeks 5–8).',
     ['<b>Dorsal bud</b>: body, tail and the superior/anterior head · <b>ventral bud</b>: <b>uncinate process</b> and the '
      'inferior/posterior head',
      '<b>Main duct (Wirsung)</b> = distal dorsal duct + the whole ventral duct; it enters with the bile duct at the <b>major '
      'papilla</b> · the proximal dorsal duct is obliterated or persists as the <b>accessory duct (Santorini)</b> at the minor papilla',
      '<b>PDX1</b> (pancreatic and duodenal homeobox 1) drives pancreatic outgrowth; homozygous PDX1 loss → <b>pancreatic agenesis</b>',
      '<b>PAX4 + PAX6</b> → β (insulin), δ (somatostatin) and PP cells · <b>PAX6 alone</b> → α (glucagon) cells',
      '<b>Ectopic pancreas</b>: rests of normal acini, ducts, sometimes islets, in ~2% of autopsies — stomach and duodenum most '
      'often; usually incidental, can cause pain, inflammation or mucosal bleeding'],
     ['—'],
     ['Ventral bud = uncinate process', 'PAX6 alone = alpha cell'],
     [LG15, RB19], ['—'],
     ['ventral pancreatic bud', 'dorsal pancreatic bud', 'ventral bud', 'dorsal bud', 'uncinate process', 'pdx1', 'pax4',
      'duct of wirsung', 'main pancreatic duct', 'ectopic pancreas'],
     fa='367')

card('foregutdev', 'Foregut development — stomach rotation, mesogastria & duodenum', 'reg', 'fgDev',
     'The stomach turns 90° clockwise; the duodenum joins foregut to midgut', 1,
     'In the 5th week the stomach rotates <b>90° clockwise</b> around its long axis, so its original left side faces '
     'anteriorly and its right side posteriorly. The faster-growing <b>original posterior wall</b> becomes the greater '
     'curvature; the anterior wall becomes the lesser curvature.',
     ['<b>Left vagus → anterior trunk</b>; right vagus → posterior trunk · a second turn around the AP axis moves the pylorus '
      'up and to the right, the cardia left and slightly down',
      'Rotation pulls the <b>dorsal mesogastrium</b> to the left, opening the <b>omental bursa</b> (lesser sac) behind the stomach, '
      'and pulls the lesser omentum to the right; the dorsal mesogastrium then bulges down as the greater omentum',
      '<b>Spleen</b>: mesoderm between the leaves of the dorsal mesogastrium (5th week), yet supplied by the celiac trunk',
      '<b>Duodenum</b> = terminal foregut + cephalic midgut, joined just distal to the liver bud (the major papilla) — so it gets '
      'celiac and SMA branches · its lumen fills (solid stage, weeks 5–6) and recanalizes by weeks 8–10; failure → atresia',
      '<b>Liver bud</b> (mid week 3) grows into the septum transversum; its cells become hepatocytes and biliary cells under '
      '<b>HNF3 and HNF4</b>'],
     ['—'],
     ['Left vagus anterior, right vagus posterior'],
     [LG15], ['—'],
     ['90 degree clockwise rotation', 'original posterior wall', 'dorsal mesogastrium', 'terminal part of the foregut', 'liver bud',
      'solid stage', 'rotation of the stomach'],
     fa='364, 367')

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
F = lambda *k: [f'f:{x}' for x in k]
NORMAL = F('div', 'stom', 'duod', 'liv', 'dbud', 'vpb', 'vbud', 'ducts', 'pdx')
def X(cx, cy, s=14): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def stroke(d, col, w, op=1, extra='', when=None, unless=None):
    add(f'<path d="{d}" style="fill:none;stroke:var({col});stroke-width:{w};opacity:{op};stroke-linecap:round;stroke-linejoin:round{extra}"/>',
        when=when, unless=unless)
CAPY = 1610   # the caption line under the close-up
PANY = 1250

text('The foregut — rotation, buds and what goes wrong', 180, 150, 'dyn-big')
text('top: the gut tube at week 5, head on the left · below: the foregut as it ends up, front view (patient’s right on your left)', 180, 176, 'dyn-cap')

# ════════ gut tube strip ════════
TY, AY = 345, 262
add(f'<rect x="200" y="200" width="2200" height="370" rx="24" class="dyn-soft"/>')
stroke(f'M240 {AY} H2360', '--nf-blood', 14, .45)
text('aorta', 2370, AY + 5, 'nf-l2')
for x0, x1, col, lab in ((260, 480, '--dk8', 'pharyngeal gut'), (480, 1060, '--dk1', 'foregut'),
                         (1060, 1820, '--dk3', 'midgut'), (1820, 2300, '--dk5', 'hindgut')):
    text(lab, (x0 + x1) // 2, 232, 'nf-l1', 'middle')
LOOP = f'M1060 {TY} H1250 C1300 {TY} 1320 470 1420 470 C1520 470 1540 {TY} 1590 {TY} H1820'
stroke(f'M260 {TY} H480', '--dk8', 26, .45)
stroke(f'M480 {TY} H1060', '--dk1', 26, .45)
add(f'<ellipse cx="760" cy="{TY}" rx="90" ry="34" style="fill:var(--dk1);fill-opacity:.45"/>')
text('stomach', 760, TY + 58, 'nf-l2', 'middle')
stroke(LOOP, '--dk3', 26, .45)
stroke(f'M1820 {TY} H2300', '--dk5', 26, .45)
stroke(f'M1040 {TY + 14} L1015 420', '--dk1', 14, .6)                       # the liver bud, ventral (down)
add('<circle cx="1010" cy="428" r="14" style="fill:var(--dk1);fill-opacity:.6"/>')
text('liver bud', 1010, 466, 'nf-l2', 'middle')
stroke('M1420 484 V520', '--dk3', 6, .6)                                    # vitelline duct → yolk sac
add('<circle cx="1420" cy="540" r="22" style="fill:var(--surface);stroke:var(--dk3);stroke-width:4"/>')
text('yolk sac', 1386, 546, 'nf-l2', 'end')
for x in (480, 1060, 1820):
    add(f'<path d="M{x} 244 V{TY + 30}" class="dyn-dash"/>')
for x, yb, lab in ((820, TY - 16, 'celiac'), (1420, 456, 'SMA'), (2050, TY - 16, 'IMA')):
    stroke(f'M{x} {AY} V{yb}', '--nf-blood', 8, .55)
    text(lab, x + 12, 300, 'nf-l2')
# divisions: what each region becomes
for t, x in (('esophagus → duodenum to the papilla · liver · pancreas', 770), ('rest of duodenum → ⅔ of transverse colon', 1700),
             ('last ⅓ of transverse colon → upper anal canal', 2100)):
    text(t, x, 520, 'nf-l2', 'middle', when=F('div'))
for d in (f'M480 {TY} H1060', LOOP, f'M1820 {TY} H2300'):
    stroke(d, '--accent', 34, .25, when=F('div'))
# malrotation: the loop stops short
stroke(LOOP, '--bad', 30, .35, when=F('mal'))
text('rotation stops short of 270° → colon left, small bowel right', 1700, 520, 'nf-l1 dyn-tag', 'middle', when=F('mal'))
text('normal: herniates week 6, turns 270° counterclockwise around the SMA, back by week 12', 1610, 430, 'nf-l2', when=F('div'))

# ════════ the foregut, front view ════════
add('<rect x="200" y="610" width="1520" height="960" rx="24" class="dyn-soft"/>')
LIVER = 'M230 720 C300 650 600 640 760 680 C820 700 840 740 800 780 C740 850 620 900 520 930 C420 960 300 950 250 880 C210 820 200 760 230 720 Z'
add(f'<path d="{LIVER}" style="fill:var(--dk10);fill-opacity:.22;stroke:var(--dk10);stroke-width:4"/>')
add('<path d="M600 662 C590 760 575 850 560 925" class="dyn-dash"/>')   # falciform
text('liver', 420, 790, 'nf-l1', 'middle')
text('right lobe', 420, 812, 'nf-l2', 'middle'); text('left lobe', 690, 740, 'nf-l2', 'middle')
GB = 'M612 928 C642 932 662 962 652 992 C642 1018 612 1018 602 992 C594 966 597 938 612 928 Z'
add(f'<path d="{GB}" style="fill:var(--dk3);fill-opacity:.3;stroke:var(--dk3);stroke-width:4"/>')
text('gallbladder', 590, 1040, 'nf-l2', 'end')
CBD = 'M640 890 C670 930 700 960 720 1000 C750 1060 780 1100 808 1120'
stroke(CBD, '--dk3', 8, .7)
stroke('M622 936 C640 940 660 945 680 950', '--dk3', 6, .7)   # cystic duct
text('bile duct', 735, 1010, 'nf-l2', unless=F('ba'))
# stomach, esophagus, spleen
STOM = ('M1140 700 C1170 640 1290 610 1360 660 C1430 710 1460 820 1430 900 C1400 980 1300 1012 1180 1002 C1080 994 1000 '
        '986 952 978 L952 934 C1010 940 1080 930 1118 890 C1150 850 1150 760 1140 700 Z')
add(f'<path d="{STOM}" style="fill:var(--dk1);fill-opacity:.16;stroke:var(--dk1);stroke-width:5"/>')
stroke('M1155 620 V705', '--dk1', 30, .35)
text('esophagus', 1180, 640, 'nf-l2')
text('stomach', 1300, 760, 'nf-l1', 'middle')
SPLEEN = 'M1540 700 C1600 680 1660 720 1660 780 C1660 840 1610 870 1560 860 C1585 830 1585 800 1560 790 C1580 770 1570 735 1540 700 Z'
add(f'<path d="{SPLEEN}" style="fill:var(--dk7);fill-opacity:.25;stroke:var(--dk7);stroke-width:4"/>')
text('spleen', 1610, 896, 'nf-l2', 'middle')
add('<rect x="928" y="928" width="30" height="58" rx="8" style="fill:var(--dk1);fill-opacity:.35;stroke:var(--dk1);stroke-width:3"/>')
text('pylorus', 940, 912, 'nf-l2', 'middle')
# duodenum + jejunum
DUO = 'M955 956 C860 956 790 970 790 1050 V1220 C790 1290 840 1300 900 1300 H1150 C1220 1300 1240 1260 1240 1200'
JEJ = 'M1240 1200 C1240 1150 1300 1150 1360 1200 C1420 1260 1500 1300 1640 1290'
DUO_MAL = 'M955 956 C860 956 790 970 790 1050 V1340 C790 1420 740 1460 660 1480'
JEJ_MAL = 'M660 1480 C560 1500 500 1460 540 1420 C580 1380 500 1340 440 1380 C380 1420 360 1500 300 1510'
shapes.append(dict(tube=DUO, w=24, color='--dk8', unless=F('mal')))
shapes.append(dict(tube=JEJ, w=22, color='--dk8', unless=F('mal')))
shapes.append(dict(tube=DUO_MAL, w=24, color='--dk8', when=F('mal')))
shapes.append(dict(tube=JEJ_MAL, w=22, color='--dk8', when=F('mal')))
text('duodenum', 735, 1250, 'nf-l2', 'end', unless=F('mal'))
text('jejunum', 1560, 1340, 'nf-l2', 'middle', unless=F('mal'))
# pancreas
PANC = ('M855 1015 C900 992 980 1012 1040 1032 C1200 1060 1400 1010 1590 945 C1640 930 1670 962 1645 990 C1450 1080 1250 1120 '
        '1060 1130 C1000 1140 982 1180 990 1230 C995 1262 900 1272 862 1258 C838 1240 838 1062 855 1015 Z')
VENT = 'M842 1172 C870 1162 940 1166 990 1180 C994 1230 994 1262 900 1272 C860 1265 836 1240 842 1172 Z'
add(f'<path d="{PANC}" style="fill:var(--dk9);fill-opacity:.25;stroke:var(--dk9);stroke-width:4"/>')
text('pancreas', 1300, 1100, 'nf-l1', 'middle')
PB = F('vbud', 'divis')
add(f'<path d="{PANC}" style="fill:var(--dk4);fill-opacity:.25"/>', when=PB + F('dbud'))
add(f'<path d="{VENT}" style="fill:var(--dk6);fill-opacity:.5;stroke:var(--dk6);stroke-width:4"/>', when=PB + F('vpb'))
text('dorsal bud: body, tail, upper head', 1490, 1150, 'nf-l2', 'middle', when=PB + F('dbud'))
text('ventral bud: uncinate process, lower head', 1000, 1350, 'nf-l2', 'middle', when=PB + F('vpb'))
MAIN = 'M1600 978 C1400 1060 1200 1090 1060 1096 C960 1100 880 1112 808 1120'
ACC = 'M960 1098 C900 1082 860 1064 808 1060'
DORS_DIV = 'M1600 978 C1400 1060 1200 1090 1060 1096 C1010 1097 980 1097 960 1096 C900 1082 860 1064 808 1060'
VENT_DIV = 'M950 1230 C900 1190 860 1140 808 1120'
stroke(MAIN, '--dk9', 6, .8, unless=F('divis')); stroke(ACC, '--dk9', 3, .8, unless=F('divis'))
stroke(DORS_DIV, '--dk4', 8, .9, when=F('divis')); stroke(VENT_DIV, '--dk6', 4, .9, when=F('divis'))
text('major papilla', 850, 1150, 'nf-l2', when=F('vbud', 'divis', 'ducts'))
text('minor papilla', 850, 1040, 'nf-l2', when=F('vbud', 'divis', 'ducts'))
stroke(MAIN, '--accent', 12, .45, when=F('ducts')); stroke(ACC, '--accent', 8, .45, when=F('ducts'))
# foregut | midgut at the papilla
add('<path d="M700 1120 H880" style="stroke:var(--accent);stroke-width:4;stroke-dasharray:8 6"/>', when=F('div', 'duod'))
text('foregut ↑ celiac', 690, 1105, 'nf-l1', 'end', when=F('div', 'duod'))
text('midgut ↓ SMA', 690, 1145, 'nf-l1', 'end', when=F('div', 'duod'))
# highlights for normal steps
add(f'<path d="{STOM}" class="dyn-hl"/>', when=F('stom'))
add('<path d="M1360 660 C1430 710 1460 820 1430 900 C1400 980 1300 1012 1180 1002" style="fill:none;stroke:var(--dk5);stroke-width:12;opacity:.8"/>', when=F('stom'))
text('greater curvature =', 1450, 900, 'nf-l2', when=F('stom'))
text('original posterior wall', 1450, 920, 'nf-l2', when=F('stom'))
stroke('M1167 600 V700 C1180 740 1220 770 1260 790', '--accent', 5, .9, when=F('stom'))
stroke('M1143 600 V700', '--accent', 5, .9, ';stroke-dasharray:6 6', when=F('stom'))
text('left vagus → anterior', 1180, 620, 'nf-l2', when=F('stom'))
text('right vagus → posterior', 1130, 620, 'nf-l2', 'end', when=F('stom'))
add(f'<path d="{DUO}" class="dyn-hl" style="opacity:.5"/>', when=F('duod'))
for s in (LIVER, GB):
    add(f'<path d="{s}" class="dyn-hl"/>', when=F('liv'))
stroke(CBD, '--accent', 10, .6, when=F('liv'))
add('<path d="M842 1172 C870 1162 940 1166 990 1180" class="dyn-hl"/>', when=F('vbud'))
add(f'<path d="{PANC}" class="dyn-hl" style="opacity:.6"/>', when=F('pdx'))
# defects
add('<rect x="918" y="918" width="50" height="78" rx="14" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:6"/>', when=F('pyl'))
text('thick pyloric muscle — the “olive”', 940, 892, 'nf-l1 dyn-tag', 'middle', when=F('pyl'))
add(X(700, 970), when=F('ba')); add(X(770, 1075), when=F('ba'))
add(f'<path d="{GB}" style="fill:var(--surface);fill-opacity:.7"/>', when=F('ba'))
text('bile ducts obliterated', 735, 1010, 'nf-l1 dyn-tag', when=F('ba'))
for cx, cy in ((1415, 860), (870, 990)):
    add(f'<circle cx="{cx}" cy="{cy}" r="17" style="fill:var(--dk9);fill-opacity:.55;stroke:var(--dk9);stroke-width:3"/>', when=F('ect'))
text('pancreatic rest', 1450, 866, 'nf-l1 dyn-tag', when=F('ect'))
add('<ellipse cx="1000" cy="1420" rx="60" ry="40" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--dk5);stroke-width:4"/>', when=F('mal'))
text('cecum', 1000, 1426, 'nf-l2', 'middle', when=F('mal'))
for d in ('M950 1400 L260 1260', 'M950 1425 L260 1330'):
    add(f'<path d="{d}" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:10 7"/>', when=F('mal'))
text('Ladd bands across the duodenum', 470, 1240, 'nf-l1 dyn-tag', when=F('mal'))
text('small bowel on the right', 330, 1550, 'nf-l2', when=F('mal'))
stroke('M1100 1470 C1300 1420 1450 1440 1600 1380', '--dk5', 30, .35, when=F('mal'))
text('colon on the left', 1450, 1490, 'nf-l2', 'middle', when=F('mal'))
# captions
CAP = dict(
  div='each region keeps its artery — the duodenum, half foregut and half midgut, gets celiac and SMA branches',
  stom='90° clockwise: left side → front · omental bursa opens behind · spleen in the dorsal mesogastrium',
  duod='lumen fills (weeks 5–6), then vacuoles reopen it (weeks 8–10) — failure: duodenal atresia',
  liv='liver bud → hepatocytes and bile ducts · its stalk → bile duct · an outgrowth → gallbladder',
  dbud='the dorsal bud grows into the dorsal mesentery — it becomes the body, tail and upper head',
  vpb='the ventral bud grows beside the bile duct — it becomes the uncinate process and lower head',
  vbud='the ventral bud swings behind the duodenum, below the dorsal bud — split halves ring it: annular pancreas',
  ducts='main duct (Wirsung) → major papilla with the bile duct · accessory duct (Santorini) → minor papilla',
  pdx='PDX1 drives the pancreas to grow out; PAX4 and PAX6 decide which islet cell each endocrine cell becomes',
  pyl='food can’t leave the stomach — projectile vomiting without bile (the block is above the papilla)',
  ba='no bile reaches the gut — pale stools, dark urine, ↑ direct bilirubin and GGT',
  divis='ducts never fuse — most of the gland drains through the small minor papilla',
  ect='normal pancreatic tissue in the stomach or duodenal wall — usually an incidental finding',
  mal='incomplete rotation — the midgut can twist on itself: volvulus')
for k, t in CAP.items(): text(t, 960, CAPY, 'nf-l1 dyn-tag', 'middle', when=F(k))

# ════════ close-ups for normal development ════════
BX0, BY0, BX1, BY1 = 1760, 610, 2400, 1570
add(f'<rect x="{BX0}" y="{BY0}" width="{BX1 - BX0}" height="{BY1 - BY0}" rx="24" class="dyn-soft"/>')
text('close-up', 1790, 650, 'dyn-big', unless=NORMAL)
text('pick a step of normal development', 1790, 676, 'dyn-cap', unless=NORMAL)
text('to see it here', 1790, 696, 'dyn-cap', unless=NORMAL)
CX = 2080
# div: duodenal blood supply
text('Duodenum: two arteries', 1790, 650, 'dyn-big', when=F('div'))
stroke('M2200 760 C2050 760 1960 790 1960 900 V1080 C1960 1160 2020 1180 2100 1180 H2260', '--dk8', 30, .35, when=F('div'))
add('<path d="M1930 960 H2000" style="stroke:var(--accent);stroke-width:4;stroke-dasharray:8 6"/>', when=F('div'))
stroke('M2300 700 C2200 720 2120 760 2010 840', '--nf-blood', 6, .7, when=F('div'))
stroke('M2300 1300 C2200 1260 2100 1150 2010 1060', '--nf-blood', 6, .7, when=F('div'))
text('celiac → gastroduodenal', 2080, 700, 'nf-l2', when=F('div'))
text('→ superior pancreaticoduodenal', 2080, 720, 'nf-l2', when=F('div'))
text('SMA → inferior', 2120, 1320, 'nf-l2', when=F('div'))
text('pancreaticoduodenal', 2120, 1340, 'nf-l2', when=F('div'))
text('papilla', 1925, 950, 'nf-l2', 'end', when=F('div'))
text('foregut above the papilla,', 1790, 1440, 'nf-l1', when=F('div'))
text('midgut below it', 1790, 1462, 'nf-l1', when=F('div'))
# stom: transverse sections seen from above
text('Seen from above (front ↓)', 1790, 650, 'dyn-big', when=F('stom'))
add('<path d="M1790 760 H2370" style="stroke:var(--ink-3);stroke-width:4"/>', when=F('stom'))
text('back wall', 1795, 748, 'nf-l2', when=F('stom'))
text('front', 2080, 1080, 'nf-l2', 'middle', when=F('stom'))
add('<circle cx="1930" cy="920" r="70" style="fill:var(--dk1);fill-opacity:.2;stroke:var(--dk1);stroke-width:4"/>', when=F('stom'))
add('<path d="M1930 850 V762" style="stroke:var(--dk7);stroke-width:5"/>', when=F('stom'))
add('<ellipse cx="2215" cy="805" rx="62" ry="26" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2;stroke-dasharray:5 4"/>', when=F('stom'))
add('<circle cx="2240" cy="920" r="70" style="fill:var(--dk1);fill-opacity:.2;stroke:var(--dk1);stroke-width:4"/>', when=F('stom'))
add('<path d="M2295 878 C2320 830 2335 800 2340 762" style="fill:none;stroke:var(--dk7);stroke-width:5"/>', when=F('stom'))
for cx, cy, lab in ((2000, 920, 'L'), (1860, 920, 'R'), (2240, 990, 'L'), (2240, 850, 'R')):
    add(f'<circle cx="{cx}" cy="{cy}" r="13" style="fill:var(--accent)"/>', when=F('stom'))
    text(lab, cx, cy + 5, 'nf-l1', 'middle', when=F('stom'))
add('<path d="M2010 1010 C2060 1050 2120 1050 2170 1010" class="dyn-line" marker-end="url(#ah-fgDev)"/>', when=F('stom'))
text('90° clockwise', 2090, 1000, 'nf-l1', 'middle', when=F('stom'))
text("omental bursa", 2215, 810, 'nf-l2', 'middle', when=F('stom'))
text('dorsal mesogastrium', 1945, 795, 'nf-l2', when=F('stom'))
for i, t in enumerate(('left vagus → anterior trunk', 'right vagus → posterior trunk', 'posterior wall → greater curvature',
                       'mesogastrium pulled left → lesser sac', 'lesser omentum pulled right', 'spleen grows in the mesogastrium')):
    text(t, 1790, 1150 + i * 26, 'nf-l2', when=F('stom'))
# duod: solid stage → vacuoles → lumen
text('Duodenum: solid stage', 1790, 650, 'dyn-big', when=F('duod'))
for i, (lab, sub) in enumerate((('solid cord', 'weeks 5–6'), ('vacuoles merge', ''), ('lumen restored', 'weeks 8–10'))):
    y = 760 + i * 200
    add(f'<rect x="1840" y="{y}" width="480" height="70" rx="35" style="fill:var(--dk8);fill-opacity:.25;stroke:var(--dk8);stroke-width:4"/>', when=F('duod'))
    if i == 0:
        add(f'<rect x="1852" y="{y + 12}" width="456" height="46" rx="23" style="fill:var(--dk8);fill-opacity:.45"/>', when=F('duod'))
        for cx in range(1875, 2300, 26):
            for cy in (y + 25, y + 45):
                add(f'<circle cx="{cx + (13 if cy > y + 30 else 0)}" cy="{cy}" r="9" style="fill:var(--surface);fill-opacity:.6;stroke:var(--dk8);stroke-width:2"/>', when=F('duod'))
    elif i == 1:
        for vx in (1900, 1990, 2080, 2170, 2260):
            add(f'<ellipse cx="{vx}" cy="{y + 35}" rx="30" ry="14" style="fill:var(--nf-lumen);stroke:var(--ink-3);stroke-width:2"/>', when=F('duod'))
    else:
        add(f'<rect x="1852" y="{y + 18}" width="456" height="34" rx="17" style="fill:var(--nf-lumen)"/>', when=F('duod'))
    text(lab + (' · ' + sub if sub else ''), 1840, y + 100, 'nf-l1', when=F('duod'))
    if i < 2: text('↓', 2080, y + 160, 'nf-l1', 'middle', when=F('duod'))
text('complete failure → atresia', 1790, 1400, 'nf-l1 dyn-tag', when=F('duod'))
text('partial → stenosis', 1790, 1424, 'nf-l1 dyn-tag', when=F('duod'))
text('double bubble · Down syndrome', 1790, 1448, 'nf-l2', when=F('duod'))
# liv: liver bud into the septum transversum
text('Liver bud (mid week 3)', 1790, 650, 'dyn-big', when=F('liv'))
add('<rect x="1800" y="700" width="560" height="200" rx="18" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>', when=F('liv'))
text('septum transversum (mesoderm)', 1820, 730, 'nf-l2', when=F('liv'))
stroke('M1800 1120 H2360', '--dk8', 40, .35, when=F('liv'))
text('foregut (future duodenum)', 1820, 1180, 'nf-l2', when=F('liv'))
stroke('M2080 1100 V900', '--dk1', 18, .6, when=F('liv'))
for d in ('M2080 900 L2000 790', 'M2080 900 L2080 770', 'M2080 900 L2170 800', 'M2040 850 L1960 840', 'M2120 850 L2220 860'):
    stroke(d, '--dk1', 9, .6, when=F('liv'))
text('liver cords', 2240, 820, 'nf-l2', when=F('liv'))
stroke('M2080 1040 C2120 1030 2150 1000 2160 970', '--dk3', 12, .6, when=F('liv'))
text('stalk → bile duct', 2000, 1000, 'nf-l2', 'end', when=F('liv'))
text('outgrowth → gallbladder', 2175, 990, 'nf-l2', when=F('liv'))
for i, t in enumerate(('hepatocytes + bile duct lining: HNF3, HNF4', 'induced by FGF2 (cardiac mesoderm) + BMP',
                       'septum → Kupffer, blood-forming cells', 'septum → lesser omentum, falciform')):
    text(t, 1790, 1260 + i * 26, 'nf-l2', when=F('liv'))
# vbud (and dbud, vpb): two buds → fused
BUDS = F('dbud', 'vpb', 'vbud')
text('Pancreatic buds', 1790, 650, 'dyn-big', when=BUDS)
for cx, lab in ((1950, 'week 5'), (2250, 'weeks 5–8: fused')):
    stroke(f'M{cx - 50} 720 V1100', '--dk8', 36, .35, when=BUDS)
    text(lab, cx, 1150, 'nf-l1', 'middle', when=BUDS)
add('<ellipse cx="2010" cy="830" rx="40" ry="55" style="fill:var(--dk4);fill-opacity:.5"/>', when=BUDS)
add('<ellipse cx="1840" cy="960" rx="30" ry="34" style="fill:var(--dk6);fill-opacity:.6"/>', when=BUDS)
stroke('M1880 1060 C1860 1010 1850 980 1845 960', '--dk3', 6, .7, when=BUDS)
text('bile duct', 1830, 1080, 'nf-l2', 'middle', when=BUDS)
text('dorsal', 2010, 760, 'nf-l2', 'middle', when=BUDS); text('ventral', 1840, 910, 'nf-l2', 'middle', when=BUDS)
add('<path d="M1850 1000 C1880 1060 1960 1060 1995 960" class="dyn-dash" marker-end="url(#ah-fgPanc)"/>', when=BUDS)
add('<ellipse cx="2310" cy="830" rx="44" ry="60" style="fill:var(--dk4);fill-opacity:.5"/>', when=BUDS)
add('<ellipse cx="2300" cy="935" rx="34" ry="30" style="fill:var(--dk6);fill-opacity:.6"/>', when=BUDS)
text('ventral: below + behind', 2300, 1010, 'nf-l2', 'middle', when=BUDS)
for i, t in enumerate(('main duct (Wirsung) = distal dorsal', '+ whole ventral duct → major papilla', 'proximal dorsal duct → accessory',
                       '(Santorini) → minor papilla', 'PDX1 drives the buds · PAX4 + PAX6 → β δ PP', 'PAX6 alone → α cells')):
    text(t, 1790, 1210 + i * 26, 'nf-l2', when=BUDS)

add('<ellipse cx="2010" cy="830" rx="56" ry="71" style="fill:none;stroke:var(--accent);stroke-width:5"/>', when=F('dbud'))
add('<ellipse cx="1840" cy="960" rx="46" ry="50" style="fill:none;stroke:var(--accent);stroke-width:5"/>', when=F('vpb'))
# ducts: the two ducts at their papillae
text('Pancreatic ducts', 1790, 650, 'dyn-big', when=F('ducts'))
stroke('M1880 720 V1160', '--dk8', 40, .35, when=F('ducts'))
text('duodenum', 1880, 1200, 'nf-l2', 'middle', when=F('ducts'))
stroke('M2340 930 C2200 960 2050 990 1900 1010', '--dk9', 10, .8, when=F('ducts'))
stroke('M2120 975 C2060 920 2000 880 1900 860', '--dk9', 5, .8, when=F('ducts'))
stroke('M2000 740 C1990 860 1960 960 1900 1010', '--dk3', 8, .7, when=F('ducts'))
add('<circle cx="1900" cy="1010" r="13" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:5"/>', when=F('ducts'))
add('<circle cx="1900" cy="860" r="9" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:4"/>', when=F('ducts'))
text('bile duct', 2015, 760, 'nf-l2', when=F('ducts'))
text('accessory duct (Santorini)', 2090, 850, 'nf-l2', when=F('ducts'))
text('main duct (Wirsung)', 2120, 1040, 'nf-l2', when=F('ducts'))
text('minor papilla', 1920, 820, 'nf-l2', when=F('ducts'))
text('major papilla', 1925, 1060, 'nf-l2', when=F('ducts'))
for i, t in enumerate(('Wirsung = distal dorsal duct + the whole', 'ventral duct → major papilla, beside the bile duct',
                       'Santorini = proximal dorsal duct: obliterates', 'or stays open → minor papilla',
                       'never fused → pancreas divisum')):
    text(t, 1790, 1260 + i * 26, 'nf-l2', when=F('ducts'))
# pdx: transcription factors
text('Pancreas transcription factors', 1790, 650, 'dyn-big', when=F('pdx'))
for x, y, w, lab, sub in ((1830, 730, 520, 'PDX1', 'pancreatic and duodenal homeobox 1'),
                          (1830, 930, 250, 'PAX4 + PAX6', 'β · δ · PP cells'),
                          (2100, 930, 250, 'PAX6 alone', 'α cells')):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="110" rx="16" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>', when=F('pdx'))
    text(lab, x + w // 2, y + 46, 'nf-l1', 'middle', when=F('pdx'))
    text(sub, x + w // 2, y + 78, 'nf-l2', 'middle', when=F('pdx'))
for x in (1955, 2225):
    add(f'<path d="M{x} 845 V922" class="dyn-line" marker-end="url(#ah-fgPanc)"/>', when=F('pdx'))
for i, t in enumerate(('PDX1: master factor for pancreatic outgrowth', 'and differentiation · homozygous loss →',
                       'pancreatic agenesis', 'PAX4 + PAX6: endocrine lineage → β (insulin),', 'δ (somatostatin), PP · PAX6 alone → α (glucagon)')):
    text(t, 1790, 1210 + i * 26, 'nf-l2', when=F('pdx'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
EST = 'M1155 600 V700 C1160 780 1250 830 1300 880 C1300 940 1200 962 1100 962 H955'
DUO_B = 'M800 1130 V1220 C790 1290 840 1300 900 1300 H1150 C1220 1300 1240 1260 1240 1200'
flows = [
  dict(d=EST, len=620, speed=110, r=8, base=dict(food=6), mods=[m(F('pyl'), set=dict(food=10), speed=0.25)]),
  dict(d=DUO, len=830, speed=110, r=8, base=dict(food=5), unless=F('mal'), mods=[m(F('pyl'), set=dict(food=0))]),
  dict(d=JEJ, len=430, speed=110, r=8, base=dict(food=3), unless=F('mal'), mods=[m(F('pyl'), set=dict(food=0))]),
  dict(d=DUO_MAL + ' ' + JEJ_MAL.replace('M660 1480', 'L660 1480'), len=1250, speed=110, r=8, base=dict(food=7), when=F('mal')),
  dict(d='M1250 850 C1200 800 1160 770 1155 700 V560', len=330, speed=200, r=9, base=dict(vom=4), when=F('pyl')),
  dict(d='M500 820 C560 850 610 870 640 890 C660 915 675 935 690 955', len=230, speed=70, r=7, base=dict(bile=3),
       mods=[m(F('ba'), speed=0.2)]),
  dict(d='M690 955 C705 975 715 990 720 1000 C750 1060 780 1100 808 1120', len=200, speed=70, r=7, base=dict(bile=2), mods=[m(F('ba'), set=dict(bile=0))]),
  dict(d=DUO_B, len=560, speed=110, r=7, base=dict(bile=3), unless=F('mal'), mods=[m(F('ba'), set=dict(bile=0))]),
  dict(d=MAIN, len=820, speed=90, r=7, base=dict(juice=5), unless=F('divis')),
  dict(d=ACC, len=160, speed=60, r=6, base=dict(juice=1), unless=F('divis')),
  dict(d=DORS_DIV, len=820, speed=70, r=7, base=dict(juice=6), when=F('divis')),
  dict(d=VENT_DIV, len=180, speed=60, r=6, base=dict(juice=1), when=F('divis')),
  dict(d=f'M240 {AY} H2360', len=2120, speed=260, r=7, base=dict(bl=6)),
  dict(d=f'M820 {AY} V{TY - 16}', len=70, speed=60, r=6, base=dict(bl=1)),
  dict(d=f'M1420 {AY} V456', len=190, speed=90, r=6, base=dict(bl=1)),
  dict(d=f'M2050 {AY} V{TY - 16}', len=70, speed=60, r=6, base=dict(bl=1)),
]
sites = [
  dict(x=806, y=AY + 40, n=[-1, 0], w=8, t='rec', l='', aria='Gut arteries', c='gutarteries', ions=[]),
  dict(x=1420, y=430, n=[1, 0], w=8, t='rec', l='', aria='Midgut rotation and malrotation', c='volvulus', ions=[]),
  dict(x=1380, y=700, n=[1, -1], w=8, t='rec', l='', aria='Stomach rotation', c='foregutdev', ions=[]),
  dict(x=943, y=1000, n=[0, 1], w=8, t='rec', l='', aria='Pyloric stenosis', c='pyloric', ions=[]),
  dict(x=700, y=960, n=[1, 0], w=8, t='rec', l='', aria='Biliary atresia', c='biliaryatresia', ions=[]),
  dict(x=1500, y=1010, n=[1, 1], w=8, t='rec', l='', aria='Pancreatic buds', c='pancdev', ions=[]),
  dict(x=905, y=1250, n=[0, 1], w=8, t='rec', l='', aria='Annular pancreas', c='annularpanc', ions=[]),
  dict(x=880, y=1078, n=[1, 0], w=8, t='rec', l='', aria='Pancreas divisum', c='pancdivisum', ions=[]),
  dict(x=1150, y=1320, n=[0, 1], w=8, t='rec', l='', aria='Duodenal atresia', c='atresia', ions=[], unless=F('mal')),
]

readouts = [
  dict(l='Projectile non-bilious vomiting', mods=[dict(when=F('pyl'), d=1)]),
  dict(l='Blood pH (metabolic alkalosis)', mods=[dict(when=F('pyl'), d=1)]),
  dict(l='Serum K⁺ and Cl⁻', mods=[dict(when=F('pyl'), d=-1)]),
  dict(l='Direct bilirubin · GGT', mods=[dict(when=F('ba'), d=1)]),
  dict(l='Pancreatitis risk', mods=[dict(when=F('divis'), d=1)]),
  dict(l='Volvulus risk', mods=[dict(when=F('mal'), d=1)]),
]

notes = {
  '': 'The foregut as it ends up: food runs from the esophagus through the stomach into the duodenum, bile drains from the liver '
      'down the bile duct, and pancreatic juice joins it at the major papilla. Pick a step of normal development, or a defect, '
      'and see what moves, stops or backs up.',
  'f:div': 'The gut tube has four parts: pharyngeal gut, foregut (to just past the liver bud), midgut (to the proximal two-thirds '
           'of the transverse colon) and hindgut (to the cloacal membrane), fed by the celiac trunk, SMA and IMA. The duodenum is '
           'foregut above the major papilla and midgut below it, so it gets celiac and SMA branches.',
  'f:stom': 'In the 5th week the stomach turns 90° clockwise on its long axis: its left side faces front, so the left vagus becomes '
            'the anterior trunk and the right vagus the posterior. The faster-growing original posterior wall becomes the greater '
            'curvature, and the dorsal mesogastrium swings left, opening the omental bursa (lesser sac) behind the stomach.',
  'f:duod': 'The duodenum’s lumen fills with proliferating cells (the solid stage, weeks 5–6), then vacuoles open and merge until the '
            'lumen is restored by weeks 8–10. Complete failure leaves duodenal atresia — vomiting within hours of birth, bilious '
            'when the block is below the papilla (80–85%), a double bubble, Down syndrome.',
  'f:liv': 'In the middle of week 3 the liver bud grows from the distal foregut into the septum transversum; its stalk becomes the '
           'bile duct, and a small outgrowth of the duct makes the gallbladder and cystic duct. Liver cords become hepatocytes and '
           'the biliary lining (HNF3, HNF4); Kupffer and blood-forming cells come from the septum’s mesoderm.',
  'f:vbud': 'The dorsal bud lies in the dorsal mesentery, the ventral bud beside the bile duct. As the duodenum turns right, the '
            'ventral bud swings behind it to lie below and behind the dorsal bud, and they fuse (weeks 5–8): ventral = uncinate '
            'process and lower head. If the two halves of a bifid ventral bud go opposite ways, they ring the 2nd part of the '
            'duodenum — annular pancreas.',
  'f:dbud': 'The dorsal pancreatic bud grows from the duodenum into the dorsal mesentery. After fusion it forms the body, the '
            'tail and the superior/anterior part of the head, and its duct supplies the distal main duct and the accessory duct.',
  'f:vpb': 'The ventral pancreatic bud grows from the duodenum beside the bile duct. When the duodenum turns, it swings behind '
           'to lie below and behind the dorsal bud; it forms the uncinate process and the inferior/posterior head.',
  'f:ducts': 'When the buds fuse, the main pancreatic duct (of Wirsung) forms from the distal dorsal duct plus the whole ventral '
             'duct and empties with the common bile duct at the major papilla. The proximal dorsal duct either obliterates or '
             'persists as the accessory duct (of Santorini) at the minor papilla.',
  'f:pdx': 'PDX1 (pancreatic and duodenal homeobox 1) is the master transcription factor for pancreatic outgrowth and '
           'differentiation; homozygous PDX1 mutations cause pancreatic agenesis. PAX4 and PAX6 specify the endocrine lineage: '
           'cells with both become β, δ or PP cells, and cells with PAX6 alone become α cells.',
  'f:pyl': 'Hypertrophic pyloric stenosis: the pyloric muscle thickens (nNOS-deficient, so it can’t relax) and blocks the outlet. '
           'At 3–6 weeks (GI course; First Aid 2–6) a hungry infant has projectile non-bilious vomiting — the block is above the papilla — with an olive and '
           'a hypochloremic, hypokalemic metabolic alkalosis; firstborn boys, macrolides; pyloromyotomy.',
  'f:ba': 'Biliary atresia: the extrahepatic bile ducts are destroyed (perinatal form, about 80%) or never form properly (fetal form), '
          'so no bile reaches the gut — jaundice at 2–6 weeks, dark urine, acholic stools, hepatomegaly, ↑ direct bilirubin and '
          'GGT, a small or absent gallbladder. Untreated it is cirrhosis by 3–6 months; Kasai portoenterostomy, and it is the '
          'leading reason for a child’s liver transplant.',
  'f:divis': 'Pancreas divisum: the dorsal and ventral duct systems never fuse — the commonest pancreatic anomaly (3–10%). Most of '
             'the gland, from the dorsal bud, must drain through the accessory duct of Santorini and the small minor papilla; '
             'usually silent, but about 5% get pancreatitis.',
  'f:ect': 'Ectopic pancreas: rests of normal acini, ducts and sometimes islets, in about 2% of autopsies — most often in the stomach '
           'and duodenum, then jejunum, Meckel diverticulum and ileum. Usually incidental; they can cause pain, inflammation or '
           'mucosal bleeding, and in the pylorus can scar and obstruct the outlet.',
  'f:mal': 'Normally the midgut loop herniates into the cord in week 6, turns 270° counterclockwise around the SMA and returns from '
           'week 10. In malrotation the small bowel lies on the right and the colon on the left, and Ladd bands can cross and '
           'obstruct the duodenum; the midgut can twist — volvulus, whose vomiting may be bilious.',
}

dyn = dict(
  kinds=dict(food=['food', '--dk5'], vom=['vom', '--bad'], bile=['bile', '--dk3'], juice=['juice', '--dk9'], bl=['bl', '--nf-blood']),
  groups=[['food', 'Feeds'], ['vom', 'Vomit'], ['bile', 'Bile'], ['juice', 'Pancreatic juice'], ['bl', 'Blood']],
  switches=[dict(id='f', label='Step or defect', type='one', options=[
              ['div', 'Gut tube divisions', 'gutarteries'], ['stom', 'Stomach rotation · dorsal mesogastrium', 'foregutdev'],
              ['duod', 'Duodenal recanalization', 'atresia'], ['liv', 'Liver bud', 'foregutdev'],
              ['dbud', 'Dorsal pancreatic bud', 'pancdev'], ['vpb', 'Ventral pancreatic bud', 'pancdev'],
              ['vbud', 'Ventral bud rotation', 'annularpanc'],
              ['ducts', 'Duct of Wirsung · duct of Santorini', 'pancdev'], ['pdx', 'PDX1 · PAX4 · PAX6', 'pancdev'],
              ['pyl', 'Pyloric stenosis', 'pyloric'], ['ba', 'Biliary atresia', 'biliaryatresia'],
              ['divis', 'Pancreas divisum', 'pancdivisum'], ['ect', 'Ectopic pancreas', 'pancdev'],
              ['mal', 'Midgut malrotation', 'volvulus']],
            sections=[['Normal development', ['div', 'stom', 'duod', 'liv', 'dbud', 'vpb', 'vbud', 'ducts', 'pdx']],
                      ['Defects', ['pyl', 'ba', 'divis', 'ect', 'mal']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='GI Exam 1 lecture notes (SDL 1, 11) · Langman ch 15 · Robbins ch 17–19 · First Aid pp. 364, 366, 367, 392, 401')

MAP = dict(
  id='foregutsim', title='Foregut Rotation & Buds in Motion', topic='gi', after='abdanat',
  sub='Watch food, bile and pancreatic juice move through the foregut, then step through how it forms — gut tube divisions, '
      'stomach rotation, duodenal recanalization, liver bud, ventral bud — and break it: pyloric stenosis, biliary atresia, '
      'pancreas divisum, ectopic pancreas, malrotation. Tap a structure for its card',
  w=3580, h=2000,
  fa='364, 366, 367, 392, 401',
  src=[LG15, RB17, RB18, RB19, MO5, BC_EMB],
  lanes=[('fgDev', 'Normal development', 'glycolysis'), ('fgPanc', 'Liver, biliary & pancreas', 'gluconeo'), ('fgDz', 'Defects', 'tca')],
  nodes=[
    ('fg1', 'Gut tube & arteries', 330, 1720, 'fgDev', 'celiac · SMA · IMA', ['gutarteries', 'lungdev'], 'hub'),
    ('fg2', 'Stomach rotation', 770, 1720, 'fgDev', '90° clockwise', ['foregutdev', 'giligaments']),
    ('fg3', 'Duodenum · atresia', 1210, 1720, 'fgDev', 'solid stage', ['atresia', 'down']),
    ('fg4', 'Pancreatic buds', 1650, 1720, 'fgPanc', 'dorsal + ventral', ['pancdev']),
    ('fg5', 'Annular · divisum', 2090, 1720, 'fgPanc', 'ring · unfused ducts', ['annularpanc', 'pancdivisum']),
    ('fg6', 'Biliary atresia', 2530, 1720, 'fgPanc', 'acholic stools', ['biliaryatresia']),
    ('fg7', 'Pyloric stenosis', 330, 1860, 'fgDz', 'non-bilious', ['pyloric']),
    ('fg8', 'Malrotation · volvulus', 770, 1860, 'fgDz', 'Ladd bands', ['volvulus']),
    ('fg9', 'Meckel diverticulum', 1210, 1860, 'fgDz', 'vitelline duct', ['meckel']),
    ('fg10', 'TEF · germ layers', 1650, 1860, 'fgDev', 'foregut partition', ['tef', 'germlayers'])],
  panels=[
    (2500, PANY, 1000, 'What each part becomes (course notes · Langman ch 15)', [
      ('Dorsal bud', 'body, tail, upper head · accessory duct (Santorini)'),
      ('Ventral bud', 'uncinate process, lower head · part of the main duct'),
      ('Liver bud', 'hepatocytes, bile ducts · stalk → bile duct · outgrowth → gallbladder'),
      ('Septum transversum', 'Kupffer and blood-forming cells · lesser omentum, falciform'),
      ('Dorsal mesogastrium', 'spleen · greater omentum · omental bursa behind the stomach'),
      ('Major papilla', 'bile enters: a block above it → non-bilious vomit, below → bilious')])],
  dyn=dyn)
