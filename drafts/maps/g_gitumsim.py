# m56 — GI Cancers along the Tube in Motion (dynamic map, kit data)
# A front view of the trunk (patient's right on your left) with the whole tube drawn as one continuous lumen — esophagus
# (upper ⅔ / lower ⅓) → stomach → duodenum → small bowel → colon → rectum — plus the liver, gallbladder, bile ducts and
# pancreas. Food rides the lumen and bile runs from the liver down the common bile duct to the ampulla. One `one` switch
# (sections in tube order) lights one cancer, polyp or syndrome: its lesion is drawn at its site, food or bile backs up where
# the tumor obstructs, tumor cells travel its spread route (lymph to Virchow node, portal vein to the liver, ovaries,
# umbilicus, lungs), and the "Road to cancer" column on the right steps a particle through its precursor sequence — the
# APC → KRAS → TP53 adenoma–carcinoma sequence, the serrated/MSI road, Barrett, PanIN, cirrhosis… — lighting how far that
# lesion has come. Readouts: AFP, CEA, CA 19-9, urine 5-HIAA, bilirubin, hemoglobin, cancer risk.
# Static tumgut lays the same cancers out as a flow chart (a ⇄ pair is fine); this map is the moving, site-by-site version.
# esosim (motility), acidflow (gastritis), sxgibleed, netsim (islet tumors), mapksim/chemosim (oncogene mechanics) and
# pancsim (pancreatitis) are not repeated: their topics appear here only as one-line causes.
#
# Sources (all read in the corpus):
#   First Aid 2025 p. 220 (KRAS: pancreatic, colorectal; APC, DCC, SMAD4, TP53 tumor suppressors) · p. 221 (aflatoxin → HCC;
#     arsenic, vinyl chloride → hepatic angiosarcoma; nitrosamines → intestinal gastric cancer; ethanol → esophageal SCC, HCC;
#     tobacco → esophagus, pancreas) · p. 222 (H. pylori, HBV/HCV, Clonorchis; AFP HCC; CEA colorectal + pancreatic, minor
#     gastric; CA 19-9 pancreatic; chromogranin NET) · p. 357 (carcinoid: intestine or lung, 5-HT cleared by liver, syndrome
#     after liver metastasis, ↑ urine 5-HIAA, chromogranin/synaptophysin, rule of thirds) · p. 385 (esophageal SCC upper ⅔ vs
#     adenocarcinoma lower ⅓, risk factors, dysphagia solids → liquids, no serosa) · p. 386 (chronic gastritis → atrophy →
#     intestinal metaplasia; intestinal vs diffuse gastric cancer, WEAPON, Virchow, Krukenberg, Sister Mary Joseph, Blumer)
#     · p. 394 (polyp histology, hyperplastic, adenomatous APC + KRAS, villous > tubular, serrated CIMP/MLH1/BRAF up to 20%;
#     FAP, Gardner, Turcot, Peutz-Jeghers, juvenile polyposis) · p. 395 (Lynch ~80% CRC, proximal colon; CRC risk factors,
#     right vs left, S. bovis, iron deficiency anemia, screening, apple core, CEA for recurrence, CIN vs MSI pathways)
#     · p. 399 (hemangioma, FNH, hepatic adenoma, HCC risk/findings/AFP, angiosarcoma, metastases) · p. 402 (PSC → cholangio-
#     carcinoma + gallbladder cancer; hemochromatosis → HCC) · p. 403 (porcelain gallbladder) · p. 404 (cholangiocarcinoma)
#     · p. 405 (pancreatic adenocarcinoma: head, CA 19-9, KRAS, risk factors, Trousseau, Courvoisier) · p. 435 (MALT lymphoma
#     t(11;18), regresses with H. pylori eradication).
#   Robbins ch 17 (esophageal SCC half in middle third, nodes by third; Barrett → dysplasia → adenocarcinoma, TP53/CDKN2A
#     early; gastric intestinal type from flat dysplasia/adenomas, diffuse type no precursor, CDH1, mean age 40 germline,
#     early satiety mainly diffuse; MALT not in normal stomach, induced by H. pylori; GI NETs >40% small intestine,
#     jejunum/ileum often multiple and aggressive, desmoplasia kinks bowel, syndrome <10%; hyperplastic polyps left colon,
#     < 5 mm, "no malignant potential"; villous harbor cancer more often, size matters most; sessile serrated right colon;
#     Table 17.9 Peutz-Jeghers STK11, juvenile polyposis SMAD4/BMPR1A, 30–50% CRC by 45; Table 17.10; HNPCC MSH2/MLH1, right
#     colon, younger; APC → β-catenin → MYC/cyclin D1, KRAS late, TP53 70–80% of cancers; CIMP MLH1 + BRAF; proximal tumors
#     exophytic, distal "napkin-ring"; liver the commonest distant site through portal drainage).
#   Robbins ch 18 (HCC: cirrhosis, 15–20% non-cirrhotic, HBV/HCV, hemochromatosis, α1-AT, alcohol, MASLD, aflatoxin;
#     dysplastic nodules; TP53/β-catenin/TERT; portal vein and IVC invasion; AFP in advanced disease; lung metastases late;
#     cavernous hemangioma subcapsular, < 2 cm; hepatocellular adenoma OCP/anabolic steroids, β-catenin subtype high risk of
#     HCC; angiosarcoma vinyl chloride, arsenic, thorotrast, almost uniformly fatal; metastases colon/breast/lung/pancreas;
#     gallbladder carcinoma: gallstones 95%, 1–2% of stone carriers, women ≥ 2×, fundus, liver + porta hepatis spread,
#     5-yr survival < 10%; cholangiocarcinoma: PSC, flukes, KRAS).
#   Robbins ch 19 (PanIN: KRAS first, CDKN2A, then TP53/SMAD4/BRCA2; 60% in the head, obstructs the CBD; Courvoisier;
#     Trousseau ~10%; new-onset diabetes; metastases liver and lungs).
#   Bootcamp.com Gastroenterology (Stomach: gastric malignancy, MALT; Liver: HCC ↑ AFP; Biliary system: cholangiocarcinoma
#     and gallbladder adenocarcinoma ↑ CA 19-9, ↑ CEA, cholangio bilirubin ↑↑↑, gallbladder "-/↑"; Pancreas: bilirubin ↑↑↑,
#     ↑ CA 19-9, ↑ CEA; Small intestine: carcinoid 24-h urine 5-HIAA; Large intestine: CRC ↑ CEA, right-sided anemia).
# Arrows deliberately left "–" (sources hedge or disagree):
#   gastric cancer CEA (FA p. 222 lists gastric only as a "minor" CEA association) · gallbladder carcinoma bilirubin (Bootcamp
#   "-/↑", card "normal or raised") · hyperplastic polyp cancer risk (FA p. 394 "occasionally evolve into serrated polyps"
#   vs Robbins ch 17 "no malignant potential" — flagged for the owner) · hepatic adenoma cancer risk (Robbins: varies by
#   subtype, minimal for HNF1α, high for β-catenin-activated) · hemangioma (no source states a risk either way).
# Cut: hepatoblastoma (Robbins only, not in FA), GIST (FA one line only, not in the spec), HCC polycythemia (not in Robbins
#   ch 18 or FA p. 399), Courvoisier for cholangiocarcinoma (Bootcamp only; a hilar tumor sits above the cystic duct).
# m57 pins (pins3.md P5 + cardgap #11): "Hepatic adenoma" → "Hepatocellular adenoma" (the course and Robbins term; FA p. 399
#   says hepatic adenoma); "HCC · hepatocellular carcinoma"; + focal nodular hyperplasia (FA p. 399: second commonest benign
#   liver tumor, women 35–50, reaction to an aberrant dystrophic artery, central stellate scar; Robbins ch 18 / GI Exam 1 lecture
#   notes SDL 17: radiating septa, map-like glutamine synthetase stain, no malignant change or rupture); + fibrolamellar HCC
#   (Robbins ch 18 / lecture notes SDL 17: adolescents and young adults without liver disease or cirrhosis, DNAJB1–PRKACA
#   fusion → protein kinase A, oncocytic cells in lamellar collagen, AFP not raised, up to 40% survive ≥ 10 years);
#   + new card pancysts and three options — serous cystic neoplasm, mucinous cystic neoplasm, IPMN (Robbins ch 19 in the course
#   text, course_sdl_19_patho pp. 21–25, and the lecture notes SDL 19 section 3; First Aid has no pancreatic cyst entry).
#   Arrows: AFP "–" (0) for fibrolamellar (AFP negative); cancer risk ↑ for MCN and IPMN (precancerous); none for serous
#   ("almost always benign") or FNH (no malignant risk) — left "–".
import sys, re, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full, card

RB17, RB18, RB19 = full('Robbins', 17), full('Robbins', 18), full('Robbins', 19)
BC = 'Bootcamp.com Gastroenterology — '
SRC = [RB17, RB18, RB19, BC + 'Stomach', BC + 'Liver', BC + 'Biliary system', BC + 'Pancreas', BC + 'Small intestine',
       BC + 'Large intestine']

# ── helpers ──
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

def plen(d):
    """length of an absolute M/L/H/V/C path"""
    toks = re.findall(r'[MLHVC]|-?\d+\.?\d*', d)
    i, x, y, L, cmd = 0, 0.0, 0.0, 0.0, None
    while i < len(toks):
        if toks[i] in 'MLHVC': cmd = toks[i]; i += 1; continue
        if cmd == 'M': x, y = float(toks[i]), float(toks[i + 1]); i += 2; cmd = 'L'
        elif cmd == 'L':
            nx, ny = float(toks[i]), float(toks[i + 1]); L += math.hypot(nx - x, ny - y); x, y = nx, ny; i += 2
        elif cmd == 'H': nx = float(toks[i]); L += abs(nx - x); x = nx; i += 1
        elif cmd == 'V': ny = float(toks[i]); L += abs(ny - y); y = ny; i += 1
        elif cmd == 'C':
            p = [float(t) for t in toks[i:i + 6]]; i += 6
            px, py = x, y
            for k in range(1, 41):
                t = k / 40
                bx = (1 - t) ** 3 * x + 3 * (1 - t) ** 2 * t * p[0] + 3 * (1 - t) * t * t * p[2] + t ** 3 * p[4]
                by = (1 - t) ** 3 * y + 3 * (1 - t) ** 2 * t * p[1] + 3 * (1 - t) * t * t * p[3] + t ** 3 * p[5]
                L += math.hypot(bx - px, by - py); px, py = bx, by
            x, y = p[4], p[5]
    return round(L)

SW = 'ca'
O = lambda *k: [f'{SW}:{x}' for x in k]
TAG = 'nf-l2 dyn-tag'
LES = 'fill:var(--dk4);fill-opacity:.55;stroke:var(--bad);stroke-width:4'      # a tumor
POL = 'fill:var(--dk4);fill-opacity:.45;stroke:var(--dk4);stroke-width:3'      # a polyp
HL = 'fill:none;stroke:var(--accent);stroke-width:6;opacity:.8'                # the site is lit

# ════════ the trunk ════════
add('<path d="M940 112 V232 C860 252 640 252 560 302 C520 332 520 402 525 502 L540 1500 C545 1700 600 1850 700 1975 '
    'L1300 1975 C1400 1850 1455 1700 1460 1500 L1475 502 C1480 402 1480 332 1440 302 C1360 252 1140 252 1060 232 V112 Z" '
    'class="dyn-soft" style="fill-opacity:.55"/>')
add('<path d="M600 300 C760 270 880 285 960 262 M1040 262 C1120 285 1240 270 1400 300" class="dyn-line" style="opacity:.45"/>')   # clavicles
add('<path d="M560 642 C700 592 860 612 1000 640 C1140 612 1300 592 1440 642" class="dyn-dash" style="opacity:.5"/>')   # diaphragm
text('diaphragm', 1450, 664, 'dyn-cap', 'end')

# ── liver (patient's right on your left), gallbladder, ducts ──
LIVER = 'M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z'
FALC = 'M58 62 C56 40 56 20 58 6'
def scale(d, x, y, w, h):
    return re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}', d)
LD, LF = scale(LIVER, 560, 646, 440, 296), scale(FALC, 560, 646, 440, 296)
add(f'<path d="{LD}" style="fill:var(--dk6);fill-opacity:.12;stroke:var(--dk6);stroke-width:4"/>'
    f'<path d="{LF}" style="fill:none;stroke:var(--dk6);stroke-width:2;opacity:.5"/>')
text('Liver', 586, 702, 'dyn-big')
GB = 'M800 845 C822 872 792 950 756 965 C722 976 704 946 714 916 C727 886 764 862 800 845 Z'
add(f'<path d="{GB}" style="fill:var(--dk3);fill-opacity:.18;stroke:var(--dk3);stroke-width:3"/>', unless=O('panc'))
add(f'<g transform="translate(760 905) scale(1.45) translate(-760 -905)"><path d="{GB}" style="fill:var(--dk3);fill-opacity:.3;stroke:var(--bad);stroke-width:3"/></g>',
    when=O('panc'))
text('Gallbladder', 700, 1000, 'nf-l1', 'end')
CBD = 'M815 828 L850 880 C865 960 870 1030 858 1088'
add(f'<path d="{CBD}" style="fill:none;stroke:var(--dk3);stroke-width:9;opacity:.55"/><path d="M800 848 L850 880" style="fill:none;stroke:var(--dk3);stroke-width:7;opacity:.55"/>')
text('bile duct', 876, 948, 'nf-l2')

# ── the tube ──
ESO_U, ESO_L = 'M1000 140 V513', 'M1000 513 V700 C1000 715 1015 728 1035 732'
shapes.append(dict(tube=ESO_U, w=24, color='--dk10', mods=[dict(when=O('escc'), d=-14)]))
shapes.append(dict(tube=ESO_L, w=24, color='--dk10', mods=[dict(when=O('eac'), d=-14)]))
add('<path d="M968 513 H1032" class="dyn-line"/>')
text('Esophagus', 1032, 190, 'nf-l1')
text('upper ⅔', 968, 330, 'nf-l2', 'end', unless=O('escc')); text('lower ⅓', 968, 610, 'nf-l2', 'end', unless=O('eac'))
STOM = ('M1035 722 C1060 665 1170 645 1250 695 C1320 745 1335 880 1285 955 C1245 1010 1120 1015 1005 995 L1000 955 '
        'C1060 945 1100 900 1100 840 C1100 790 1070 760 1035 742 Z')
add(f'<path d="{STOM}" style="fill:var(--dk10);fill-opacity:.14;stroke:var(--dk10);stroke-width:4"/>', unless=O('gdif'))
add(f'<path d="{STOM}" style="fill:var(--dk4);fill-opacity:.22;stroke:var(--dk4);stroke-width:20;stroke-opacity:.6"/>', when=O('gdif'))
text('Stomach', 1170, 760, 'nf-l1')
text('lesser curvature', 1112, 905, 'nf-l2', unless=O('gint'))
DUOD = 'M1000 975 C930 980 850 1000 840 1060 C830 1120 850 1175 920 1185 C990 1195 1060 1180 1090 1140'
shapes.append(dict(tube=DUOD, w=20, color='--dk10'))
text('Duodenum', 818, 1060, 'nf-l2', 'end')
PANC = ('M880 1065 C910 1040 960 1050 1010 1060 C1100 1070 1200 1035 1290 1040 C1315 1045 1312 1080 1285 1086 '
        'C1200 1100 1110 1100 1050 1110 C1020 1140 990 1160 940 1158 C895 1155 870 1110 880 1065 Z')
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.18;stroke:var(--dk5);stroke-width:3"/>'
    '<path d="M1280 1062 C1150 1075 1000 1080 860 1092" style="fill:none;stroke:var(--dk5);stroke-width:3;opacity:.6"/>')
text('Pancreas', 1300, 1120, 'nf-l1', 'end')
SB = ('M1090 1140 C1160 1180 1180 1300 1120 1390 C1060 1470 760 1400 730 1470 C700 1540 1240 1490 1250 1570 '
      'C1260 1650 860 1580 800 1650 C770 1690 700 1715 650 1712')
shapes.append(dict(tube=SB, w=18, color='--dk10'))
text('Small bowel', 1270, 1560, 'nf-l2')
COLON_A = ('M600 1730 V1300 C600 1272 622 1262 652 1264 C800 1272 900 1335 1000 1335 C1120 1335 1250 1272 1350 1264 '
           'C1382 1262 1400 1282 1400 1312 V1640 C1400 1725 1310 1758 1225 1742')
COLON_B = 'M1225 1742 C1150 1728 1095 1765 1080 1815 L1062 1930'
shapes.append(dict(tube=COLON_A, w=36, color='--dk8'))
shapes.append(dict(tube=COLON_B, w=36, color='--dk8', mods=[dict(when=O('crcl'), d=-8)]))
add('<ellipse cx="605" cy="1745" rx="34" ry="30" class="nf-wall" style="stroke:var(--dk8);stroke-width:10"/>')
text('cecum', 650, 1790, 'nf-l2')
text('ascending', 632, 1430, 'nf-l2')
text('transverse', 880, 1376, 'nf-l2')
text('descending', 1430, 1440, 'nf-l2')
text('sigmoid', 1300, 1790, 'nf-l2')
text('rectum', 1100, 1915, 'nf-l2')

# ════════ each option: its lesion, captions, spread ════════
def blob(cx, cy, rx, ry, style=LES):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="{style}"/>'
def ring(cx, cy, rx, ry):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="{HL}"/>'

# esophagus
add(blob(1000, 400, 24, 46) + ring(1000, 400, 50, 80), when=O('escc'))
text('squamous cell carcinoma — mid-esophagus', 1036, 380, TAG, when=O('escc'))
text('food sticks — solids first, then liquids', 1036, 398, TAG, when=O('escc'))
add(''.join(f'<path d="M{985 if i % 2 else 1015} {y} v18" style="stroke:var(--dk5);stroke-width:6;stroke-linecap:round"/>' for i, y in enumerate(range(540, 690, 26))),
    when=O('eac'))
add(blob(1000, 650, 22, 34) + ring(1000, 640, 50, 80), when=O('eac'))
text('Barrett (orange) → adenocarcinoma', 1036, 556, TAG, when=O('eac'))
text('food sticks — solids first, then liquids', 1036, 574, TAG, when=O('eac'))

# stomach
add(blob(1100, 880, 26, 40) + '<ellipse cx="1100" cy="880" rx="9" ry="16" style="fill:var(--surface);opacity:.8"/>' + ring(1100, 880, 52, 70),
    when=O('gint'))
text('ulcerated mass on the lesser curvature', 1140, 970, TAG, when=O('gint'))
text('whole wall thick and leathery — linitis plastica', 1140, 640, TAG, when=O('gdif'))
add(''.join(f'<circle cx="{x}" cy="{y}" r="9" style="fill:var(--dk1);fill-opacity:.6;stroke:var(--dk1);stroke-width:2"/>'
            for x, y in ((1180, 820), (1205, 845), (1230, 815), (1195, 875), (1240, 865))) + ring(1210, 845, 60, 52), when=O('malt'))
text('lymphoid follicles from H. pylori gastritis', 1140, 640, TAG, when=O('malt'))
GASTRIC = O('gint', 'gdif')
add('<circle cx="1112" cy="268" r="14" style="fill:var(--dk4);fill-opacity:.55;stroke:var(--bad);stroke-width:3"/>', when=GASTRIC)
text('Virchow node (left supraclavicular)', 1134, 236, TAG, when=GASTRIC)
add('<circle cx="960" cy="1470" r="12" style="fill:var(--dk4);fill-opacity:.55;stroke:var(--bad);stroke-width:3"/>', when=GASTRIC)
text('umbilicus — Sister Mary Joseph', 982, 1482, TAG, when=GASTRIC)
add('<ellipse cx="760" cy="1868" rx="30" ry="20" style="fill:var(--dk7);fill-opacity:.35;stroke:var(--bad);stroke-width:3"/>'
    '<ellipse cx="1300" cy="1868" rx="30" ry="20" style="fill:var(--dk7);fill-opacity:.35;stroke:var(--bad);stroke-width:3"/>', when=GASTRIC)
text('Krukenberg — both ovaries', 700, 1920, TAG, when=GASTRIC)

# small bowel carcinoid
add(''.join(f'<circle cx="{x}" cy="{y}" r="11" style="fill:var(--dk5);fill-opacity:.7;stroke:var(--bad);stroke-width:3"/>'
            for x, y in ((1050, 1608), (960, 1600), (1150, 1622))) + ring(1050, 1610, 130, 44), when=O('net'))
text('ileal NETs — often multiple', 1030, 1680, TAG, 'middle', when=O('net'))
HEART = 'M1050 420 C1050 380 1105 368 1130 395 C1160 368 1225 382 1220 430 C1215 485 1170 525 1205 575 C1140 560 1075 505 1055 465 Z'
add(f'<path d="{HEART}" style="fill:var(--dk2);fill-opacity:.15;stroke:var(--dk2);stroke-width:3"/>'
    '<path d="M1080 440 C1100 470 1110 500 1130 520" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=O('net'))
text('right-sided valves — TR, PS', 1232, 460, TAG, when=O('net'))

# colon polyps
add('<path d="M1380 1500 h-18" style="stroke:var(--dk4);stroke-width:5"/>' + blob(1352, 1500, 12, 12, POL) + ring(1365, 1500, 46, 40),
    when=O('tub'))
text('tubular adenoma on a stalk', 1300, 1470, TAG, 'end', when=O('tub'))
add('<path d="M1384 1530 q-20 6 -26 20 q16 4 26 12 q-20 6 -22 22 q14 0 22 10" style="fill:var(--dk4);fill-opacity:.45;stroke:var(--dk4);stroke-width:3"/>'
    + ring(1375, 1558, 46, 50), when=O('vil'))
text('villous adenoma — broad, frond-like', 1300, 1470, TAG, 'end', when=O('vil'))
add(blob(1262, 1748, 8, 7, POL) + blob(1290, 1742, 7, 6, POL) + ring(1275, 1745, 40, 30), when=O('hyp'))
text('small (< 5 mm), rectosigmoid', 1432, 1702, TAG, when=O('hyp'))
add('<path d="M616 1440 q-10 -16 0 -32 q8 16 0 32 Z" style="fill:var(--dk4);fill-opacity:.45;stroke:var(--dk4);stroke-width:3"/>'
    '<path d="M616 1400 q-8 -12 0 -24 q6 12 0 24 Z" style="fill:var(--dk4);fill-opacity:.45;stroke:var(--dk4);stroke-width:3"/>'
    + ring(605, 1418, 34, 50), when=O('ssp'))
text('flat, sessile — right colon', 650, 1400, TAG, when=O('ssp'))
# FAP: adenomas carpet the colon, rectum included
FAPDOTS = ([(600, y) for y in range(1320, 1720, 44)] + [(700, 1288), (800, 1300), (900, 1325), (1000, 1335), (1100, 1330), (1200, 1300), (1300, 1272)] +
           [(1400, y) for y in range(1330, 1660, 44)] + [(1340, 1735), (1250, 1745), (1160, 1740), (1095, 1785), (1075, 1850), (1066, 1900)])
add(''.join(f'<circle cx="{x + (6 if i % 2 else -6)}" cy="{y}" r="6" style="{POL}"/>' for i, (x, y) in enumerate(FAPDOTS)), when=O('fap'))
text('hundreds to thousands of adenomas — always the rectum', 820, 1252, TAG, when=O('fap'))
# hamartomas
PJ = [(1150, 1300), (1090, 1420), (800, 1440), (1150, 1530), (900, 1610), (1230, 1590), (600, 1500), (1400, 1450), (1220, 850)]
add(''.join(f'<circle cx="{x}" cy="{y}" r="10" style="fill:var(--dk6);fill-opacity:.55;stroke:var(--dk6);stroke-width:3"/>' for x, y in PJ),
    when=O('pj'))
text('hamartomas — small bowel > colon > stomach', 820, 1252, TAG, when=O('pj'))
text('dark macules: lips, mouth, hands, genitalia', 1036, 190 + 20, TAG, when=O('pj'))
JP = [(600, 1360), (600, 1600), (1400, 1380), (1400, 1560), (900, 1325), (1240, 1745), (1180, 760), (1000, 1600)]
add(''.join(f'<path d="M{x} {y} v-14" style="stroke:var(--dk6);stroke-width:3"/><circle cx="{x}" cy="{y - 18}" r="9" style="fill:var(--dk6);fill-opacity:.55;stroke:var(--dk6);stroke-width:3"/>'
            for x, y in JP), when=O('jp'))
text('juvenile polyps — colon, stomach, small bowel', 820, 1252, TAG, when=O('jp'))
# colorectal cancer
RIGHT = O('lynch', 'crcr')
add(blob(608, 1600, 22, 44) + ring(605, 1600, 50, 82), when=RIGHT)
text('exophytic mass — rarely obstructs', 650, 1560, TAG, when=O('crcr'))
text('proximal colon — always involved', 650, 1560, TAG, when=O('lynch'))
text('also endometrium, ovary, skin', 650, 1578, TAG, when=O('lynch'))
add('<path d="M1245 1716 C1240 1740 1240 1752 1246 1772 M1205 1712 C1198 1736 1198 1752 1204 1770" style="fill:none;stroke:var(--bad);stroke-width:9"/>'
    + ring(1225, 1742, 54, 50), when=O('crcl'))
text('napkin-ring — obstruction, pencil-thin stools', 1432, 1702, TAG, when=O('crcl'))

# liver
add(''.join(f'<circle cx="{x}" cy="{y}" r="18" style="fill:none;stroke:var(--ink-3);stroke-width:3;opacity:.7"/>'
            for x, y in ((640, 800), (700, 850), (760, 780), (860, 740), (930, 700))), when=O('hcc'))
add(blob(700, 790, 46, 40) + ring(700, 790, 80, 70), when=O('hcc'))
text('cirrhotic nodules · tumor', 570, 590, TAG, when=O('hcc'))
add(blob(900, 690, 22, 16, 'fill:var(--dk2);fill-opacity:.55;stroke:var(--dk2);stroke-width:3') + ring(900, 690, 44, 34), when=O('hem'))
text('blood-filled — never biopsy', 940, 676, TAG, when=O('hem'))
add(blob(700, 800, 40, 36, 'fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:4') +
    '<path d="M690 790 C700 778 716 790 708 806 C700 818 684 806 690 790 Z" style="fill:var(--dk2);fill-opacity:.6"/>' + ring(700, 800, 70, 64), when=O('had'))
text('may bleed or rupture — pain, shock', 570, 590, TAG, when=O('had'))
add(''.join(blob(x, y, r, r * .8, 'fill:var(--dk2);fill-opacity:.5;stroke:var(--bad);stroke-width:3') for x, y, r in ((680, 770, 22), (760, 820, 16), (840, 720, 18), (640, 850, 14)))
    + ring(740, 790, 130, 90), when=O('angio'))
text('endothelial tumor — many bloody foci', 570, 590, TAG, when=O('angio'))
add(blob(840, 750, 44, 38, 'fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:4') +
    ''.join(f'<path d="M840 750 L{840 + 40 * math.cos(math.radians(a)):.0f} {750 + 34 * math.sin(math.radians(a)):.0f}" style="stroke:var(--ink-2);stroke-width:4"/>'
            for a in range(0, 360, 60)) + ring(840, 750, 74, 66), when=O('fnh'))
text('central stellate scar — a reaction to an aberrant artery', 570, 590, TAG, when=O('fnh'))
add(blob(720, 790, 50, 44) + ''.join(f'<path d="M{684 + i * 18} {766 + (i % 2) * 6} q12 24 0 48" style="fill:none;stroke:var(--ink-2);stroke-width:3;opacity:.7"/>' for i in range(4))
    + ring(720, 790, 84, 76), when=O('fl'))
text('one demarcated nodule — no cirrhosis', 570, 590, TAG, when=O('fl'))
LIVMET = O('crcl', 'crcr', 'net', 'panc')
add(''.join(f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--dk4);fill-opacity:.5;stroke:var(--bad);stroke-width:2"/>'
            for x, y in ((650, 780), (740, 840), (820, 730), (680, 870))), when=LIVMET)
text('liver metastases', 570, 590, TAG, when=LIVMET)
PORTAL = 'M1000 1300 C970 1150 900 960 820 836'
add(f'<path d="{PORTAL}" style="fill:none;stroke:var(--dk9);stroke-width:12;opacity:.45"/>', when=LIVMET)
text('portal vein', 960, 1240, 'nf-l2', 'end', when=LIVMET)

# biliary + pancreas
add('<g style="fill:var(--dk10);stroke:var(--ink-3);stroke-width:2">' + ''.join(f'<circle cx="{x}" cy="{y}" r="7"/>' for x, y in ((750, 930), (765, 945), (738, 948))) + '</g>'
    f'<path d="{GB}" style="fill:none;stroke:var(--ink-2);stroke-width:7;stroke-dasharray:3 5"/>' + blob(738, 958, 16, 12) + ring(760, 905, 64, 80), when=O('gbca'))
text('stones · porcelain wall · mass', 700, 1022, TAG, 'end', when=O('gbca'))
add(blob(822, 836, 18, 16) + ring(822, 836, 44, 40) +
    '<path d="M815 828 L760 760 M815 828 L870 760 M790 795 L740 800 M845 795 L900 790" style="fill:none;stroke:var(--dk3);stroke-width:8;opacity:.6"/>',
    when=O('chol'))
text('hilar tumor · bile dammed upstream', 880, 860, TAG, when=O('chol'))
add(blob(920, 1112, 40, 34) + ring(920, 1110, 70, 60), when=O('panc'))
text('head mass squeezes the bile duct', 1320, 1160, TAG, when=O('panc'))
text('Courvoisier: big, painless GB', 700, 1022, TAG, 'end', when=O('panc'))
# pancreatic cystic neoplasms
add(''.join(f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--surface);stroke:var(--dk5);stroke-width:2.5"/>'
            for x, y in ((1236, 1056), (1250, 1056), (1243, 1068), (1257, 1068), (1229, 1068), (1236, 1080), (1250, 1080)))
    + ring(1243, 1068, 40, 32), when=O('scn'))
text('honeycomb of tiny cysts in the tail', 1320, 1160, TAG, 'end', when=O('scn'))
add(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>'
            for x, y, r in ((1230, 1062, 22), (1262, 1060, 16), (1248, 1088, 14)))
    + ring(1245, 1068, 50, 42), when=O('mcn'))
text('large mucin-filled cysts in the tail', 1320, 1160, TAG, 'end', when=O('mcn'))
add('<path d="M900 1075 C1000 1072 1150 1062 1280 1060" style="fill:none;stroke:var(--dk5);stroke-width:14;opacity:.55"/>'
    + ''.join(f'<path d="M{x} 1070 l6 -10 l6 10" style="fill:none;stroke:var(--dk4);stroke-width:3"/>' for x in (930, 980, 1030, 1080))
    + blob(930, 1080, 26, 20, 'fill:var(--dk5);fill-opacity:.3;stroke:var(--dk5);stroke-width:3') + ring(940, 1076, 62, 46), when=O('ipmn'))
text('dilated main duct with papillae — head', 1320, 1160, TAG, 'end', when=O('ipmn'))
JAUND = O('panc', 'chol', 'hcc')

# ════════ the road to cancer (right column) ════════
RX, RW, RY0, RS, RH = 1580, 740, 250, 160, 104
text('The road to this cancer', RX, 170, 'dyn-big')
text('a particle steps down each change; lit boxes = how far this lesion has come', RX, 192, 'dyn-cap')
ROAD = {
  'escc': (3, [('Squamous lining', 'alcohol, smoking, hot liquids, achalasia'), ('Squamous dysplasia', 'an in situ lesion'),
               ('Squamous cell carcinoma', 'half in the middle third')]),
  'eac': (4, [('Chronic GERD', 'reflux injures the squamous lining'), ('Barrett esophagus', 'columnar cells with goblet cells'),
              ('Dysplasia', 'TP53 and CDKN2A lost early'), ('Adenocarcinoma', 'distal third · may invade the cardia')]),
  'gint': (4, [('Chronic gastritis', 'H. pylori · or autoimmune'), ('Atrophy · intestinal metaplasia', 'less acid'),
               ('Dysplasia · adenoma', 'precursor lesions'), ('Intestinal-type carcinoma', 'bulky mass · lesser curvature')]),
  'gdif': (2, [('E-cadherin lost (CDH1)', 'no H. pylori link · no precursor lesion'), ('Diffuse carcinoma', 'signet ring cells infiltrate the wall')]),
  'malt': (3, [('H. pylori gastritis', 'induces lymphoid tissue (MALT)'), ('Marginal-zone B-cell clone', 't(11;18) in some'),
               ('MALT lymphoma', 'may regress when H. pylori is cleared')]),
  'net': (3, [('Neuroendocrine cells', 'over 40% of GI NETs are small intestinal'), ('Well-differentiated NET', 'ileal ones: often multiple, aggressive'),
              ('Liver metastases', '5-HT now skips the liver → carcinoid syndrome')]),
  'hyp': (2, [('Normal mucosa', ''), ('Hyperplastic polyp', 'the commonest polyp · benign piling-up')]),
  'tub': (3, [('Normal colon', ''), ('Colon at risk', 'APC lost — both copies'), ('Tubular adenoma', 'KRAS mutated as it grows'),
              ('Carcinoma — if left', 'TP53 and DCC lost · size matters most')]),
  'vil': (3, [('Normal colon', ''), ('Colon at risk', 'APC lost — both copies'), ('Villous adenoma', 'KRAS · harbors cancer more often'),
              ('Carcinoma — if left', 'TP53 and DCC lost')]),
  'ssp': (3, [('Normal colon', ''), ('CpG island methylation', 'MLH1 silenced → microsatellite instability'), ('Sessile serrated polyp', 'BRAF mutated · saw-tooth crypts'),
              ('Carcinoma — if left', 'right colon · up to 20% of sporadic CRC')]),
  'fap': (4, [('APC germline mutation', 'chromosome 5q · first hit inherited'), ('Second APC hit', 'polyps from puberty'),
              ('Thousands of adenomas', 'KRAS'), ('Carcinoma — 100% without colectomy', 'TP53 and DCC')]),
  'pj': (3, [('STK11 germline mutation', 'autosomal dominant'), ('Hamartomatous polyps', 'can cause intussusception'),
             ('Cancer risk ↑', 'colon, stomach, small bowel, pancreas, breast')]),
  'jp': (3, [('SMAD4 or BMPR1A mutation', 'TGF-β pathway · autosomal dominant'), ('Juvenile polyps', 'children, typically under 5'),
             ('Colorectal cancer', '30–50% by age 45')]),
  'lynch': (4, [('Germline mismatch repair mutation', 'MLH1, MSH2 — one copy'), ('Second copy lost', 'mismatch repair fails'),
                ('Microsatellite instability', 'mutations pile up in repeats'), ('Carcinoma', 'proximal colon · younger patients')]),
  'crcl': (4, [('Normal colon', ''), ('APC lost', 'β-catenin → MYC, cyclin D1'), ('Adenoma', 'KRAS mutated'),
               ('Carcinoma', 'TP53, DCC lost · chromosomal instability')]),
  'crcr': (4, [('Normal colon', ''), ('Mismatch repair lost', 'MLH1 methylated or mutated → MSI'), ('Serrated polyp', 'BRAF mutated'),
               ('Carcinoma', 'commonly the right side')]),
  'hcc': (4, [('Chronic liver injury', 'HBV, HCV, alcohol, MASLD, hemochromatosis'), ('Cirrhosis', '15–20% arise without it (HBV)'),
              ('Dysplastic nodule', 'small cell change'), ('Hepatocellular carcinoma', 'TP53, β-catenin, TERT')]),
  'hem': (1, [('Cavernous hemangioma', 'a venous malformation · the commonest benign liver tumor')]),
  'had': (2, [('Oral contraceptives · anabolic steroids', ''), ('Hepatocellular adenoma', 'may regress or rupture'),
              ('HCC — uncommon', 'mainly β-catenin-activated adenomas')]),
  'fnh': (2, [('Altered arterial flow', 'an aberrant, dystrophic artery'), ('Focal nodular hyperplasia', 'hepatocytes react — not a neoplasm')]),
  'fl': (3, [('No cirrhosis · no liver disease', 'adolescents and young adults'), ('DNAJB1–PRKACA fusion', 'protein kinase A overactive'),
             ('Fibrolamellar HCC', 'oncocytic cells in lamellar collagen')]),
  'angio': (2, [('Vinyl chloride · arsenic', 'also thorotrast'), ('Hepatic angiosarcoma', 'malignant endothelium · almost always fatal')]),
  'gbca': (4, [('Gallstones', 'in 95% of cases'), ('Chronic cholecystitis', 'porcelain gallbladder'),
               ('Dysplasia · metaplasia', 'flat in situ lesions'), ('Adenocarcinoma', 'fundus · found late')]),
  'chol': (2, [('Chronic duct inflammation', 'PSC (with UC) · liver fluke (Clonorchis)'), ('Cholangiocarcinoma', 'hilum most often · KRAS')]),
  'panc': (5, [('Normal duct', ''), ('Low-grade PanIN', 'KRAS — the first hit'), ('PanIN', 'CDKN2A (p16) lost'),
               ('High-grade PanIN', 'TP53, SMAD4, BRCA2 lost'), ('Invasive adenocarcinoma', '60% in the head')]),
  'scn': (2, [('VHL inactivated', 'chromosome 3p'), ('Serous cystic neoplasm', 'almost always benign')]),
  'mcn': (2, [('KRAS (about half) · RNF43', 'mucinous columnar lining on ovarian-type stroma'), ('Mucinous cystic neoplasm', 'precancerous'),
              ('Invasive adenocarcinoma', 'in up to a third · TP53, SMAD4')]),
  'ipmn': (2, [('KRAS (~80%) · GNAS (~⅔)', 'GNAS: in no other pancreatic cyst'), ('IPMN', 'in the main or a branch duct'),
               ('Invasive adenocarcinoma', 'TP53, SMAD4 on invasion')]),
}
for k, (reach, steps) in ROAD.items():
    svg = ''
    for i, (lab, sub) in enumerate(steps):
        y = RY0 + i * RS
        lit = i < reach
        st = 'class="dyn-cell" style="stroke:var(--accent)"' if lit else 'class="dyn-soft dyn-dim"'
        svg += f'<rect x="{RX}" y="{y}" width="{RW}" height="{RH}" rx="22" {st}/>'
        if i: svg += f'<path d="M{RX + 60} {y - RS + RH + 4} V{y - 8}" class="dyn-line" marker-end="url(#ah-gtSeq)"/>'
    add(svg, when=O(k))
    for i, (lab, sub) in enumerate(steps):
        y = RY0 + i * RS
        text(f'{i + 1} · {lab}', RX + 100, y + 44, 'nf-l1', when=O(k))
        if sub: text(sub, RX + 100, y + 68, 'nf-l2', when=O(k))
text('pick a cancer, polyp or syndrome — its precursor road appears here', RX, 290, 'nf-l2', unless=[SW + ':*'])

# ════════ at this site (under the road) ════════
IY = 1090
text('At this site', RX, IY, 'dyn-big', when=[SW + ':*'])
INFO = {
  'escc': ['upper two-thirds · more common worldwide', 'progressive dysphagia, weight loss · no serosa → spreads early',
           'nodes follow the level: neck, mediastinum, celiac'],
  'eac': ['lower third · more common in the US', 'GERD, Barrett, obesity, smoking', 'lower-third tumors spread to gastric and celiac nodes'],
  'gint': ['antrum, lesser curvature · H. pylori, nitrosamines, smoking', 'WEAPON: weight loss, early satiety, pain, obstruction, acanthosis nigricans',
           'Virchow node · Sister Mary Joseph nodule · Krukenberg · Blumer shelf'],
  'gdif': ['the whole wall — no dominant mass', 'signet ring cells · germline CDH1 → prophylactic gastrectomy',
           'same metastatic sites · Krukenberg tumors carry signet ring cells'],
  'malt': ['stomach, where MALT is induced by H. pylori', 't(11;18) — those tumors usually ignore H. pylori clearance',
           'treat early disease by eradicating H. pylori'],
  'net': ['small intestine, usually the ileum', 'chromogranin A ⊕ · synaptophysin ⊕ · salt-and-pepper nuclei',
          'flushing, diarrhea, wheezing only once 5-HT escapes the liver'],
  'hyp': ['left colon, rectosigmoid · often multiple', 'tell it apart from a sessile serrated polyp', 'removed and classified at colonoscopy'],
  'tub': ['small, pedunculated · round glands', 'usually silent · occult bleeding if large', 'colonoscopy from 45 finds and removes it'],
  'vil': ['larger, sessile · slender villi', 'villous histology is villainous', 'colonoscopy from 45 finds and removes it'],
  'ssp': ['right colon · flat and easy to miss', 'serration down to the crypt base · no typical dysplasia', 'up to 20% of sporadic colorectal cancer'],
  'fap': ['the whole colon, always the rectum', 'Gardner: + osteomas, extra teeth · Turcot: + brain tumor', 'prophylactic colectomy'],
  'pj': ['small bowel > colon > stomach', 'dark macules on lips, mouth, hands, genitalia', 'lifetime cancer risk about 40% → surveillance'],
  'jp': ['colon, stomach, small bowel', 'autosomal dominant · children under 5', 'dysplasia in the polyps → colorectal cancer'],
  'lynch': ['proximal colon · younger than sporadic', 'endometrial, ovarian, skin cancers too (CEOS)', 'MSI-high: loss of MMR protein staining'],
  'crcl': ['rectosigmoid — the commonest site', 'hematochezia, obstruction, colicky pain, narrow stools', 'apple-core lesion · liver is the main distant site'],
  'crcr': ['cecum, ascending colon', 'occult bleeding → iron deficiency anemia, weight loss', 'S. gallolyticus bacteremia → look for colon cancer'],
  'hcc': ['the commonest primary liver cancer in adults', 'jaundice, tender hepatomegaly, decompensated cirrhosis, portal vein thrombosis',
          'hematogenous spread · ultrasound screening in cirrhosis'],
  'hem': ['subcapsular, usually < 2 cm · age 30–50', 'incidental on imaging', 'biopsy is contraindicated — it bleeds'],
  'had': ['young women on oral contraceptives', 'anabolic steroids too', 'may regress when the drug stops, or rupture'],
  'fnh': ['women 35–50 · second commonest benign liver tumor', 'central stellate scar, radiating septa · map-like GS stain',
          'no malignant change, no rupture · left alone'],
  'fl': ['adolescents and young adults · no cirrhosis', 'AFP not raised · DNAJB1–PRKACA fusion', 'resectable — up to 40% live 10 years or more'],
  'angio': ['rare, malignant', 'PVC-pipe workers (vinyl chloride), arsenic', 'almost uniformly fatal'],
  'gbca': ['fundus · women at least 2× · Chile, northern India', 'mimics gallstone disease · found late',
           'spreads into the liver and porta hepatis nodes · 5-yr survival < 10%'],
  'chol': ['where the right and left hepatic ducts meet', 'painless obstructive jaundice, weight loss', 'desmoplastic stroma around the glands'],
  'panc': ['head of the pancreas', 'painless jaundice + palpable gallbladder (Courvoisier) · Trousseau',
           'smoking (strongest), chronic pancreatitis, diabetes · survival about 1 year'],
  'scn': ['pancreatic tail · women 2× · age 50–70', 'honeycomb of 1–3 mm cysts · glycogen-rich cuboidal cells, clear fluid',
          'almost always benign · resection cures'],
  'mcn': ['pancreatic tail · about 95% women', 'thick mucin · columnar lining over ovarian-type stroma (ER/PR+)',
          'precancerous — resect early'],
  'ipmn': ['pancreatic head · men more often · up to 20% multifocal', 'in the main or branch ducts · no ovarian stroma',
           'precancerous — find and resect early'],
}
KEYS = ('Where', 'Clue', 'Then')
for k, rows in INFO.items():
    for i, v in enumerate(rows):
        text(KEYS[i], RX, IY + 34 + i * 28, 'nf-l1', when=O(k))
        text(v, RX + 70, IY + 34 + i * 28, 'nf-l2', when=O(k))

# ════════ particles ════════
kinds = dict(food=['food', '--dk10'], bile=['bile', '--dk3'], met=['met', '--dk4'], blood=['blood', '--dk2'],
             ser=['ser', '--dk7'], mut=['mut', '--dk1'])
groups = [['food', 'Food & stool'], ['bile', 'Bile'], ['met', 'Tumor cells'], ['blood', 'Blood'], ['ser', 'Serotonin'], ['mut', 'Mutation steps']]
def m(when, **kw): return dict(when=when if isinstance(when, list) else [when], **kw)
STOM_C = 'M1035 732 C1150 740 1225 800 1215 880 C1205 945 1110 975 1000 975'
VIR = 'M1150 760 C1180 600 1150 400 1112 282'
UMB = 'M1150 990 C1120 1200 1050 1350 966 1460'
OVL = 'M1060 1000 C900 1300 780 1600 760 1850'
OVR = 'M1250 960 C1350 1300 1330 1600 1300 1850'
LUNG = 'M780 760 C770 650 770 560 780 470'
HEPV = 'M760 700 C820 640 950 600 1080 470'
BILE = 'M815 828 L850 880 C865 960 870 1030 858 1088 L845 1090'
flows = [
  dict(d=ESO_U + ' V700', len=plen(ESO_U + ' V700'), speed=110, base=dict(food=3), mods=[m(O('escc', 'eac'), set=dict(food=1), speed=0.4)]),
  dict(d=STOM_C, len=plen(STOM_C), speed=90, base=dict(food=2), mods=[m(O('escc', 'eac'), set=dict(food=1))]),
  dict(d=DUOD, len=plen(DUOD), speed=110, base=dict(food=2)),
  dict(d=SB, len=plen(SB), speed=150, base=dict(food=6)),
  dict(d=COLON_A, len=plen(COLON_A), speed=150, base=dict(food=6), mods=[m(O('crcr'), add=dict(blood=4))]),
  dict(d=COLON_B, len=plen(COLON_B), speed=110, base=dict(food=2), mods=[m(O('crcl'), set=dict(food=1), speed=0.4), m(O('crcr'), add=dict(blood=1))]),
  dict(d=BILE, len=plen(BILE), speed=80, base=dict(bile=3), mods=[m(O('panc', 'chol'), set=dict(bile=0))]),
  # spread
  dict(d=VIR, len=plen(VIR), speed=90, when=GASTRIC, base=dict(met=3)),
  dict(d=UMB, len=plen(UMB), speed=90, when=GASTRIC, base=dict(met=2)),
  dict(d=OVL, len=plen(OVL), speed=110, when=GASTRIC, base=dict(met=2)),
  dict(d=OVR, len=plen(OVR), speed=110, when=GASTRIC, base=dict(met=2)),
  dict(d=PORTAL, len=plen(PORTAL), speed=90, when=LIVMET, base=dict(met=4), mods=[m(O('net'), add=dict(ser=2))]),
  dict(d=LUNG, len=plen(LUNG), speed=70, when=O('hcc'), base=dict(met=2)),
  dict(d=HEPV, len=plen(HEPV), speed=90, when=O('net'), base=dict(ser=4)),
]
add(f'<path d="{LUNG}" class="dyn-dash"/>', when=O('hcc'))
text('hematogenous → lungs (late)', 792, 470, TAG, when=O('hcc'))
add(f'<path d="{HEPV}" class="dyn-dash"/>', when=O('net'))
text('5-HT via the hepatic veins', 1240, 580, TAG, when=O('net'))
for d in (VIR, UMB, OVL, OVR):
    add(f'<path d="{d}" class="dyn-dash" style="opacity:.6"/>', when=GASTRIC)
# the mutation particle down the road, to the last lit box
for k, (reach, steps) in ROAD.items():
    if reach < 2: continue
    d = f'M{RX + 60} {RY0 + RH // 2} V{RY0 + (reach - 1) * RS + RH // 2}'
    flows.append(dict(d=d, len=plen(d), speed=80, r=8, when=O(k), base=dict(mut=min(reach, 4))))

# ════════ sites ════════
sites = [
  dict(x=858, y=1090, n=[-1, 0], w=14, t='ch', l='Ampulla — bile enters', s='', ions=[['bile', 'in', 1]], c='pancca',
       lx=810, ly=1222, la='end', stop=O('panc', 'chol'), sfx=dict(stop=' — no bile')),
  dict(x=1050, y=1608, n=[0, -1], w=18, t='ex', l='Serotonin (5-HT) out', s='', ions=[['ser', 'out', 2]], c='carcinoid',
       lx=1190, ly=1660, la='start', when=O('net')),
  dict(x=620, y=1640, n=[1, 0], w=36, t='para', l='Occult bleeding', s='', ions=[['blood', 'in', 2]], c='crc',
       lx=668, ly=1650, la='start', when=O('crcr')),
]

# ════════ notes ════════
notes = {
  '': 'The whole tube, top to bottom: food runs down the lumen and bile joins it at the ampulla. Pick a cancer, polyp or '
      'syndrome — its lesion lights up at its site, tumor cells travel its usual spread route, and the right column steps '
      'through the precursor road to carcinoma. Then read the markers and signs.',
  O('escc')[0]: 'Esophageal squamous cell carcinoma: the upper two-thirds, from carcinogens touching the squamous lining — '
                'alcohol, smoking, hot liquids, caustic strictures, achalasia, Plummer-Vinson. Progressive dysphagia (solids, '
                'then liquids) and weight loss; the wall has no serosa, so it is usually advanced when found.',
  O('eac')[0]: 'Esophageal adenocarcinoma: the lower third, at the end of the reflux road — chronic GERD → Barrett metaplasia '
               '(columnar cells with goblet cells) → dysplasia → carcinoma. Obesity and smoking add risk; it is the commoner '
               'esophageal cancer in the US.',
  O('gint')[0]: 'Intestinal-type gastric adenocarcinoma: H. pylori (or autoimmune) gastritis → atrophy and intestinal metaplasia → '
                'dysplasia → a bulky, ulcerated mass, often on the lesser curvature. Nitrosamines and smoking add risk. It '
                'presents late (WEAPON) and spreads to the Virchow node, umbilicus and ovaries.',
  O('gdif')[0]: 'Diffuse-type gastric adenocarcinoma: no H. pylori link and no precursor — loss of E-cadherin (CDH1) lets single '
                'signet ring cells infiltrate the whole wall, which turns thick and leathery (linitis plastica). Krukenberg '
                'tumors of both ovaries carry the same signet ring cells.',
  O('malt')[0]: 'Gastric MALT lymphoma: the normal stomach has no lymphoid tissue; H. pylori gastritis induces it, and a marginal-zone '
                'B-cell clone can emerge — some with t(11;18). Early tumors may regress when H. pylori is eradicated.',
  O('net')[0]: 'Small-bowel carcinoid (well-differentiated neuroendocrine tumor): ileal tumors are often multiple. Their serotonin '
               'is cleared by the liver until liver metastases release it into the systemic veins — flushing, diarrhea, '
               'wheezing and right-sided valve disease, with high urine 5-HIAA.',
  O('hyp')[0]: 'Hyperplastic polyp: the commonest colonic polyp — small, often multiple, in the rectosigmoid. It is generally '
               'non-neoplastic; its importance is being told apart from a sessile serrated polyp, which looks similar.',
  O('tub')[0]: 'Tubular adenoma: a neoplastic, usually pedunculated polyp on the chromosomal instability road — APC lost, then '
               'KRAS as it grows. Less malignant potential than villous; size matters most. Removing it at colonoscopy stops '
               'the road.',
  O('vil')[0]: 'Villous adenoma: the same APC → KRAS road, but broad and covered in slender villi — villous adenomas harbor '
               'cancer more often than tubular ones (villous is villainous), partly because they are larger.',
  O('ssp')[0]: 'Sessile serrated polyp: the other road — CpG island methylation silences MLH1, so mismatch repair fails '
               '(microsatellite instability) and BRAF is mutated. Flat, in the right colon, saw-tooth crypts; behind up to '
               '20% of sporadic colorectal cancer.',
  O('fap')[0]: 'Familial adenomatous polyposis: one APC copy (5q) is inherited mutated; the second hit comes in the colon, and '
               'thousands of adenomas appear after puberty, always including the rectum. Without prophylactic colectomy, '
               '100% become colorectal cancer. Gardner and Turcot are variants.',
  O('pj')[0]: 'Peutz-Jeghers syndrome: autosomal dominant (STK11). Hamartomatous polyps throughout the GI tract — they can cause '
              'intussusception — with dark macules on the lips, mouth, hands and genitalia, and a raised risk of breast, '
              'colorectal, gastric, small-bowel and pancreatic cancer.',
  O('jp')[0]: 'Juvenile polyposis syndrome: autosomal dominant (SMAD4 or BMPR1A, the TGF-β pathway). Many hamartomatous polyps '
              'in the colon, stomach and small bowel, usually in children under 5; dysplasia develops in them, and colorectal '
              'cancer risk is raised.',
  O('lynch')[0]: 'Lynch syndrome (HNPCC): one mismatch repair gene (MLH1, MSH2) is inherited mutated; when the second copy fails, '
                 'mutations pile up in microsatellites. About 80% progress to colorectal cancer, always involving the proximal '
                 'colon — plus endometrial, ovarian and skin cancers.',
  O('crcl')[0]: 'Left-sided colorectal cancer: the classic adenoma–carcinoma sequence — APC lost → KRAS mutated → TP53 and DCC '
                'lost ("Always kill polyps"). An annular napkin-ring tumor in the rectosigmoid narrows the lumen: hematochezia, '
                'obstruction, narrow stools. It spreads by the portal vein to the liver; CEA tracks recurrence.',
  O('crcr')[0]: 'Right-sided colorectal cancer: commonly the microsatellite instability road. An exophytic mass in the wide cecum '
                'rarely obstructs but bleeds slowly — iron deficiency anemia in an older man or a postmenopausal woman means '
                'colonoscopy. S. gallolyticus bacteremia also points here.',
  O('hcc')[0]: 'Hepatocellular carcinoma: years of injury and regeneration — HBV (even without cirrhosis), HCV, alcohol, MASLD, '
               'hemochromatosis, aflatoxin. Jaundice, tender hepatomegaly, decompensated cirrhosis; it invades the portal vein '
               'and spreads in the blood. AFP is raised and follows recurrence.',
  O('hem')[0]: 'Hepatic (cavernous) hemangioma: the commonest benign liver tumor — a venous malformation, usually small, '
               'subcapsular and found by chance at age 30–50. Biopsy is contraindicated because it bleeds.',
  O('had')[0]: 'Hepatocellular adenoma: a rare benign tumor of young women on oral contraceptives, or of anabolic steroid users. '
               'It may regress, or rupture with abdominal pain and shock; β-catenin-activated adenomas can turn into HCC.',
  O('fnh')[0]: 'Focal nodular hyperplasia: the second commonest benign liver tumor, mostly in women aged 35–50 — not a neoplasm but '
               'a hyperplastic reaction of hepatocytes to an aberrant, dystrophic artery. A central stellate scar with radiating '
               'septa; usually found by chance. No malignant change and no rupture.',
  O('fl')[0]: 'Fibrolamellar HCC: a variant in adolescents and young adults with no cirrhosis or other liver disease, driven by a '
              'DNAJB1–PRKACA fusion (overactive protein kinase A). Oncocytic tumor cells sit in lamellar bands of collagen. AFP is '
              'not raised; resection is possible, and up to 40% live 10 years or more.',
  O('angio')[0]: 'Hepatic angiosarcoma: a rare malignant tumor of the liver’s endothelium, tied to vinyl chloride (PVC '
                 'manufacture), arsenic and thorotrast. It is almost uniformly fatal.',
  O('gbca')[0]: 'Gallbladder adenocarcinoma: gallstones are present in 95%, though only 1–2% of stone carriers get it; a porcelain '
                '(calcified) gallbladder is a reason for prophylactic cholecystectomy. Found late — it spreads into the liver — '
                'with CA 19-9 and CEA raised.',
  O('chol')[0]: 'Cholangiocarcinoma: chronic bile duct inflammation — primary sclerosing cholangitis (with ulcerative colitis) or '
                'the liver fluke Clonorchis — most often at the hilum, where the hepatic ducts meet. Bile is dammed upstream: '
                'painless obstructive jaundice, late; CA 19-9 and CEA raised.',
  O('panc')[0]: 'Pancreatic adenocarcinoma: PanIN steps from KRAS to CDKN2A to TP53/SMAD4. Most arise in the head and squeeze the '
                'bile duct: painless jaundice with a palpable, nontender gallbladder (Courvoisier), pain to the back, Trousseau '
                'thrombophlebitis. CA 19-9 is the marker; smoking is the strongest risk.',
  O('scn')[0]: 'Serous cystic neoplasm (serous cystadenoma): usually in the pancreatic tail, twice as common in women, age 50–70 — a '
               'honeycomb of 1–3 mm cysts lined by glycogen-rich cuboidal cells with clear, thin fluid. VHL is inactivated. Almost '
               'always benign; resection cures.',
  O('mcn')[0]: 'Mucinous cystic neoplasm: about 95% in women, in the pancreatic tail, painless and slow-growing. Large cysts of thick '
               'mucin, lined by mucinous columnar cells over a dense ovarian-type stroma (ER/PR+). Precancerous — up to a third '
               'harbor invasive adenocarcinoma, so it is resected early.',
  O('ipmn')[0]: 'Intraductal papillary mucinous neoplasm (IPMN): more often men, in the pancreatic head, inside the main duct or a '
                'branch duct, up to 20% multifocal; no ovarian stroma. GNAS mutations (about two-thirds) are found in no other '
                'pancreatic cyst. Precancerous — found and resected before it invades.',
}

R = lambda when, d: dict(when=when if isinstance(when, list) else [when], d=d)
readouts = [
  dict(l='AFP', mods=[R(O('hcc'), 1), R(O('fl'), 0)]),
  dict(l='CEA', mods=[R(O('crcl', 'crcr', 'panc', 'gbca', 'chol'), 1)]),
  dict(l='CA 19-9', mods=[R(O('panc', 'gbca', 'chol'), 1)]),
  dict(l='Urine 5-HIAA', mods=[R(O('net'), 1)]),
  dict(l='Bilirubin', mods=[R(JAUND, 1)]),
  dict(l='Hemoglobin', mods=[R(O('crcr'), -1)]),
  dict(l='Cancer risk', mods=[R(O('tub', 'vil', 'ssp', 'fap', 'pj', 'jp', 'lynch', 'mcn', 'ipmn'), 1)]),
]

OPTS = [
  ['escc', 'Esophagus — squamous cell', 'esophca'], ['eac', 'Esophagus — adenocarcinoma', 'esophca'],
  ['gint', 'Gastric — intestinal type', 'gastricca'], ['gdif', 'Gastric — diffuse (signet ring)', 'gastricca'],
  ['malt', 'Gastric MALT lymphoma', 'malt'],
  ['net', 'Small-bowel carcinoid', 'carcinoid'],
  ['hyp', 'Hyperplastic polyp', 'polyps'], ['tub', 'Tubular adenoma', 'polyps'], ['vil', 'Villous adenoma', 'polyps'],
  ['ssp', 'Sessile serrated polyp', 'polyps'],
  ['fap', 'FAP (APC)', 'fap'], ['pj', 'Peutz-Jeghers', 'polyposis'], ['jp', 'Juvenile polyposis', 'polyposis'],
  ['lynch', 'Lynch syndrome (MSI)', 'lynch'],
  ['crcl', 'Colorectal — left-sided', 'crc'], ['crcr', 'Colorectal — right-sided', 'crc'],
  ['hcc', 'HCC · hepatocellular carcinoma', 'hcc'], ['fl', 'Fibrolamellar HCC', 'hcc'], ['hem', 'Hepatic hemangioma', 'livertumors'],
  ['fnh', 'Focal nodular hyperplasia', 'livertumors'], ['had', 'Hepatocellular adenoma', 'livertumors'],
  ['angio', 'Hepatic angiosarcoma', 'angiosarcoma'],
  ['gbca', 'Gallbladder carcinoma', 'gbca'], ['chol', 'Cholangiocarcinoma', 'cholangio'], ['panc', 'Pancreatic adenocarcinoma', 'pancca'],
  ['scn', 'Serous cystic neoplasm', 'pancysts'], ['mcn', 'Mucinous cystic neoplasm', 'pancysts'],
  ['ipmn', 'IPMN · intraductal papillary mucinous neoplasm', 'pancysts'],
]
SECTIONS = [['Esophagus', ['escc', 'eac']], ['Stomach', ['gint', 'gdif', 'malt']], ['Small bowel', ['net']],
            ['Colon polyps', ['hyp', 'tub', 'vil', 'ssp']], ['Inherited syndromes', ['fap', 'pj', 'jp', 'lynch']],
            ['Colorectal cancer', ['crcl', 'crcr']], ['Liver', ['hcc', 'fl', 'hem', 'fnh', 'had', 'angio']],
            ['Gallbladder, ducts & pancreas', ['gbca', 'chol', 'panc', 'scn', 'mcn', 'ipmn']]]

# ════════ new card (m57 cardgap #11) ════════
card('pancysts', 'Pancreatic cystic neoplasms — serous, mucinous & IPMN', 'dz', 'gtLiver',
     'Serous is benign; mucinous cystic neoplasm and IPMN are precancerous', 0,
     '<b>Serous cystic neoplasms</b> are almost always benign. <b>Mucinous cystic neoplasms (MCN)</b> and <b>IPMNs</b> are '
     'precancerous: they can progress to invasive adenocarcinoma, so they are found and removed early.',
     ['<b>Serous</b>: pancreatic tail, women 2×, age 50–70; honeycomb of 1–3 mm cysts, glycogen-rich cuboidal cells, thin clear '
      'fluid; VHL inactivated',
      '<b>MCN</b>: ~95% women, tail, painless and slow-growing; thick mucin, columnar mucinous lining over a dense '
      '<b>ovarian-type stroma</b> (ER/PR+); up to one-third harbor invasive cancer',
      '<b>IPMN</b>: men more often, head; inside the main or a branch duct; no ovarian stroma; up to 20% multifocal',
      'Genes: MCN KRAS (~half) and RNF43; IPMN KRAS (~80%) and <b>GNAS</b> (~two-thirds, in no other pancreatic cyst); '
      'TP53 and SMAD4 only on invasion'],
     ['—'],
     ['Ovarian stroma = MCN; GNAS = IPMN; honeycomb = serous'],
     [RB19],
     ['MCN and IPMN: early resection, before invasive cancer', 'Serous: resection is curative when it causes symptoms'],
     ['mucinous cystic neoplasm', 'mcn', 'intraductal papillary mucinous neoplasm', 'ipmn', 'serous cystic neoplasm',
      'serous cystadenoma', 'ovarian type stroma', 'ovarian-type stroma'],
     alias='MCN · IPMN · serous cystadenoma', fa='')

PX = 2420
dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id=SW, label='Cancer, polyp or syndrome', type='one', options=OPTS, sections=SECTIONS)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=PX, y=110, w=1000),
  src='First Aid pp. 220–222, 357, 385–386, 394–395, 399, 402–405, 435 · Robbins ch 17–19 · Bootcamp Gastroenterology')

MAP = dict(
  id='gitumsim', title='GI Cancers along the Tube in Motion', topic='gi', after='gitract',
  sub='The tube from esophagus to rectum, with liver, gallbladder and pancreas — light one cancer, polyp or syndrome to see its '
      'site, what it blocks, where it spreads, and its precursor road (APC → KRAS → TP53, serrated/MSI, Barrett, PanIN, '
      'cirrhosis, mucinous cysts); read AFP, CEA, CA 19-9, 5-HIAA, bilirubin and hemoglobin. Tap a site for its card',
  w=3500, h=2080,
  fa='220, 221, 222, 357, 385, 386, 394, 395, 399, 402, 403, 404, 405, 435', src=SRC,
  lanes=[('gtUpper', 'Esophagus & stomach', 'glycolysis'), ('gtBowel', 'Small bowel & colon', 'tca'),
         ('gtLiver', 'Liver, biliary & pancreas', 'gluconeo'), ('gtSeq', 'Genes & markers', 'ppp')],
  comps=[],
  nodes=[
    ('gt1', 'Esophageal cancer', 260, 200, 'gtUpper', 'squamous ⅔ · adeno ⅓', ['esophca', 'barrett'], 'hub'),
    ('gt2', 'Gastric adenocarcinoma', 260, 320, 'gtUpper', 'intestinal · diffuse', ['gastricca', 'hpylori']),
    ('gt3', 'Gastric MALT lymphoma', 260, 440, 'gtUpper', 't(11;18)', ['malt']),
    ('gt4', 'Hepatocellular carcinoma', 260, 600, 'gtLiver', 'cirrhosis · HBV · fibrolamellar', ['hcc']),
    ('gt5', 'Benign liver tumors', 260, 720, 'gtLiver', 'hemangioma · FNH · adenoma', ['livertumors']),
    ('gt6', 'Hepatic angiosarcoma', 260, 840, 'gtLiver', 'vinyl chloride · arsenic', ['angiosarcoma']),
    ('gt7', 'Gallbladder · bile ducts', 260, 960, 'gtLiver', 'porcelain GB · Klatskin', ['gbca', 'cholangio']),
    ('gt8', 'Pancreatic cancer & cysts', 260, 1080, 'gtLiver', 'PanIN · MCN · IPMN · CA 19-9', ['pancca', 'pancysts'], 'hub'),
    ('gt9', 'Small-bowel carcinoid', 260, 1240, 'gtBowel', '5-HT · 5-HIAA', ['carcinoid']),
    ('gt10', 'Colonic polyps', 260, 1360, 'gtBowel', 'hyperplastic · adenoma · serrated', ['polyps'], 'hub'),
    ('gt11', 'FAP & polyposis', 260, 1480, 'gtBowel', 'APC · STK11 · SMAD4', ['fap', 'polyposis']),
    ('gt12', 'Lynch syndrome', 260, 1600, 'gtBowel', 'mismatch repair · MSI', ['lynch']),
    ('gt13', 'Colorectal cancer', 260, 1720, 'gtBowel', 'right vs left · S. gallolyticus', ['crc', 'sbovis'], 'hub'),
    ('gt14', 'Driver genes', 260, 1840, 'gtSeq', 'KRAS · TP53', ['kras', 'p53']),
    ('gt15', 'Serum tumor markers', 260, 1960, 'gtSeq', 'AFP · CEA · CA 19-9', ['serummarkers']),
  ],
  panels=[
    (RX, 1300, 760, 'Markers along the tube (First Aid pp. 222, 357, 399, 405)', [
      ('AFP', 'hepatocellular carcinoma — follows recurrence'),
      ('CEA', 'colorectal and pancreatic — recurrence, not screening'),
      ('CA 19-9', 'pancreatic adenocarcinoma (also biliary — Bootcamp)'),
      ('5-HIAA', '24-hour urine — carcinoid tumors'),
      ('Chromogranin', 'neuroendocrine tumors'),
      ('Biopsy', 'makes the diagnosis — markers only follow a tumor')]),
  ],
  dyn=dyn,
)
