# m57 — Gallstones & the Gallbladder in Motion (dynamic map, kit data)
# A front view (patient's right on your left) of the liver, hepatic ducts, cystic duct, gallbladder, common bile duct,
# pancreas and duodenum, with the small bowel running down to the ileocecal valve. Bile runs from the liver into the
# gallbladder (between meals) and down the common bile duct; pancreatic juice joins it at the ampulla. Right column: the
# gallbladder wall zoomed in (simple columnar cells pumping Na⁺, Cl⁻, HCO₃⁻ into the side spaces, water following into the
# lamina propria's capillaries; no muscularis mucosae, no submucosa), a schematic "what the bile holds" bar trio
# (cholesterol, bile salts + lecithin, unconjugated bilirubin), and "the tell" (three clue lines per state).
# One `one` switch (sections: stones · gallbladder · ducts & beyond) puts the stone where it belongs and shows what follows:
# stones form, colic, calculous / acalculous / chronic cholecystitis, carcinoma, choledocholithiasis, cholangitis, gallstone
# pancreatitis, gallstone ileus. 7 readouts. biliflow (bilirubin), lftsim (liver test patterns), pancsim (pancreatitis
# causes) and gitumsim (GI cancers) are not repeated: their gallstone options appear here as the stone's route.
#
# Sources (all read in the corpus; the course text wins):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt) p. 70–71 (gallbladder wall: simple columnar cholangiocytes, short
#     microvilli, folds that flatten as it fills, lamina propria with fenestrated capillaries, no muscularis mucosae or
#     submucosa, randomly oriented muscularis externa, adventitia vs serosa, Rokitansky-Aschoff sinuses; Na⁺/Cl⁻/HCO₃⁻ across
#     the lateral membranes by Na⁺/K⁺-ATPase, water through AQP1 and AQP8, ~90% of the water removed, bile salts,
#     cholesterol and bilirubin concentrated up to 10- to 20-fold) · p. 28 (CCK: gallbladder contraction, sphincter of Oddi
#     relaxation; interdigestive filling with the sphincter closed, p. 78) · p. 85, 94 (ALP, GGT, direct
#     bilirubin; choledocholithiasis → colic, pancreatitis; ascending cholangitis: coliforms E. coli, Enterococcus,
#     Klebsiella; Charcot triad; neutrophils in duct epithelium and lumens) · p. 100–104 (cholesterol vs pigment stones,
#     4 Fs, ABCG8, cholesterolosis "strawberry gallbladder", black vs brown morphology and radiology, black-stone pathogenesis
#     with ~1% deconjugation, ileal disease; acute calculous 90% vs acalculous 10%, lysolecithin, E. coli / Enterococcus
#     superinfection, empyema, gangrenous, emphysematous; acalculous: cystic artery an end artery, ICU risk factors, more
#     gangrene and perforation; chronic: stones > 90%, Rokitansky-Aschoff, porcelain, hyalinizing, xanthogranulomatous,
#     hydrops; cholecystenteric fistula → gallstone ileus at the ileocecal valve; carcinoma: stones ~95%, F:M > 2:1, Chile,
#     Bolivia, northern India, flat dysplasia / IPTN / intestinal metaplasia, TP53 ~50%, jaundice = porta hepatis or CBD
#     invasion, 5-year survival < 10%) · p. 105 (ursodiol: ↓ hepatic cholesterol secretion; dissolves small < 5–10 mm
#     radiolucent noncalcified cholesterol stones, up to 50% over 12–24 months; prevents stones in rapid weight loss).
#   Robbins ch 18 (course_sdl_15_19_patho.txt p. 137–153: same facts; biliary "colic" pain is steady, radiates to the right
#     shoulder or back, follows a fatty meal; small stones ("gravel") most dangerous; acute cholecystitis pain > 6 h with
#     mild fever, jaundice suggests CBD obstruction; chronic: E. coli and enterococci in the bile in about a third).
#   Robbins ch 19 (course_sdl_19_patho.txt: gallstones obstruct the pancreatic duct → ductal pressure → enzyme leak, lipase
#     → fat necrosis; gallstone pancreatitis in about 5% of people with gallstones).
#   Pawlina ch 18 (course histo p3, p. 52–63: ~50 mL; up to 10-fold; cells like intestinal absorptive cells).
#   Guyton ch 65 (course supplement p3: Table 65.2 liver vs gallbladder bile; ~5-fold, up to 20-fold; Ca²⁺ not absorbed;
#     CCK the most potent stimulus, sphincter of Oddi must relax).
#   Katzung ch 62 (course pharm: ursodiol).
#   First Aid 2025 p. 378 (CCK) · p. 403 (stones, 8 F's, 80% cholesterol, black/brown, colic labs normal, choledocholithiasis
#     labs, cholecystitis, Murphy sign, shoulder pain, gallstone ileus, Rigler triad, porcelain gallbladder, cholangitis,
#     Charcot, Reynolds) · p. 404 (acute pancreatitis: lipase > 3×) · p. 427–428 (hemolysis, hereditary spherocytosis →
#     pigmented gallstones).
# Arrows deliberately left "–": acute cholecystitis ALP (Robbins "may" be modestly raised; FA only "if bile duct becomes
#   involved") · acalculous pain/fever (course: symptoms masked by the illness) · carcinoma (insidious) · choledocholithiasis
#   and pancreatitis RUQ pain (sources give "biliary colic" / epigastric pain, not a RUQ readout) · gallstone ileus.
# Source conflict (owner): how much the gallbladder concentrates bile — lecture notes "up to 10- to 20-fold", Pawlina "up to
#   10-fold", Guyton "about 5-fold, maximum 20-fold". The map prints the lecture figure.
# Cut: Bouveret syndrome (Robbins names it only), IgG4 sclerosing cholecystitis, Reynolds-pentad shock readout.
# m58 pins (P8): two chronic-cholecystitis forms in "Gallbladder" — hydrops and xanthogranulomatous (lecture notes pp. 102–103:
#   "massively thickened, shrunken, nodular wall … foamy, lipid-laden macrophages (xanthoma cells) … ruptured Rokitansky-Aschoff
#   sinuses"; "chronically obstructed, dilated gallbladder filled with clear mucoid fluid"; Robbins ch 18, course_sdl_15_19_patho
#   pp. 144–149: atrophic, chronically obstructed, often dilated, only clear secretions; necrosis and hemorrhage). The spec's
#   "mucocele" synonym was cut: no course or FA source uses it for the gallbladder (Robbins uses it only for the salivary-gland
#   lesion). "Gallbladder empyema" not added (0 gain; teaching-only). No readout arrows (no source gives one).
import sys, re, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

RB18, RB19 = full('Robbins', 18), full('Robbins', 19)
PW18, GY65, KZ62 = full('Pawlina', 18), full('Guyton', 65), full('Katzung', 62)
SRC = [RB18, RB19, PW18, GY65, KZ62]

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
def box(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')
def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(round(u ** 3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t ** 3 * d) for a, b, c, d in zip(p0, p1, p2, p3))
def X(cx, cy, s=14): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'

SW = 'g'
O = lambda *k: [f'{SW}:{x}' for x in k]
TAG = 'nf-l1 dyn-tag'
CHOLST = 'fill:var(--surface);stroke:var(--dk10);stroke-width:4'          # pale cholesterol stone
BLACKST = 'fill:var(--dyn-lost);stroke:var(--ink-3);stroke-width:1.5'      # stays dark in dark mode
BROWNST = 'fill:var(--dk10);fill-opacity:.85;stroke:var(--dk10);stroke-width:2'
def stone(x, y, r, st): return f'<circle cx="{x}" cy="{y}" r="{r}" style="{st}"/>'

text('The gallbladder and its stones — where each stone sits, and what follows', 180, 150, 'dyn-big')
text('front view, patient’s right on your left · gold dots = bile · the right column zooms into the wall and the bile', 180, 176, 'dyn-cap')

# ════════ liver, ducts, gallbladder ════════
LIVER = 'M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z'
FALC = 'M58 62 C56 40 56 20 58 6'
def scale(d, x, y, w, h):
    return re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}', d)
LD, LF = scale(LIVER, 200, 220, 1000, 430), scale(FALC, 200, 220, 1000, 430)
add(f'<path d="{LD}" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:3.5;opacity:.8"/>'
    f'<path d="{LF}" style="fill:none;stroke:var(--dk2);stroke-width:2;opacity:.45"/>')
text('liver', 420, 330, 'dyn-big', 'middle')
text('right lobe', 420, 352, 'nf-l2', 'middle'); text('left lobe', 1010, 300, 'nf-l2', 'middle')

HUB, JN = (780, 490), (790, 700)                         # hepatic duct confluence, cystic + common hepatic junction
CYS = (JN, (760, 640), (700, 548), (650, 572))            # cystic duct curve (junction → gallbladder neck)
CBDC = (JN, (800, 850), (790, 1000), (760, 1100))         # common bile duct curve
AMP = (728, 1160)
CBD = f'M{JN[0]} {JN[1]} C800 850 790 1000 760 1100 L{AMP[0]} {AMP[1]}'
DUCTS_UP = O('cdl', 'ang', 'brown')                        # stone in the common bile duct: the tree above it dilates
duct = lambda d, w=11: dict(tube=d, w=w, color='--dk10', mods=[dict(when=DUCTS_UP, d=10)])
shapes += [duct(f'M560 420 L{HUB[0]} {HUB[1]}', 9), duct(f'M1000 400 L{HUB[0]} {HUB[1]}', 9),
           duct(f'M{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]}'),
           dict(tube=CBD, w=12, color='--dk10', mods=[dict(when=DUCTS_UP, d=8)]),
           dict(tube='M790 700 C760 640 700 548 650 572', w=8, color='--dk10')]
text('right · left hepatic ducts', 780, 400, 'nf-l2', 'middle')
text('common hepatic duct', 812, 610, 'nf-l2')
text('cystic duct', 700, 530, 'nf-l2', 'middle')
text('common bile duct', 812, 760, 'nf-l2')

GB = 'M640 570 C680 575 690 620 680 660 L668 800 C664 860 630 885 600 880 C560 875 540 840 545 800 L575 640 C585 600 605 568 640 570 Z'
add(f'<path d="{GB}" style="fill:var(--dk10);fill-opacity:.14;stroke:var(--dk10);stroke-width:5"/>', unless=O('acute', 'acalc', 'chron', 'gbca', 'hyd', 'xan'))
add(f'<g transform="translate(610 730) scale(1.22) translate(-610 -730)"><path d="{GB}" style="fill:var(--surface-2);fill-opacity:.6;stroke:var(--dk10);stroke-width:4"/></g>', when=O('hyd'))
add(f'<g transform="translate(610 740) scale(.9) translate(-610 -740)"><path d="{GB}" style="fill:var(--dk5);fill-opacity:.2;stroke:var(--dk5);stroke-width:22;opacity:.8"/></g>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="9" style="fill:var(--dk5);opacity:.75"/>' for x, y in ((575, 700), (660, 690), (585, 820), (650, 830), (612, 868))), when=O('xan'))
add(f'<g transform="translate(610 730) scale(1.12) translate(-610 -730)"><path d="{GB}" style="fill:var(--bad);fill-opacity:.14;stroke:var(--bad);stroke-width:6"/></g>', when=O('acute', 'acalc'))
add(f'<path d="{GB}" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--ink-3);stroke-width:16;opacity:.75"/>'
    f'<path d="{GB}" style="fill:none;stroke:var(--surface);stroke-width:5;stroke-dasharray:6 10"/>', when=O('chron'))
add(f'<path d="{GB}" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--ink-3);stroke-width:10;opacity:.7"/>', when=O('gbca'))
text('gallbladder', 530, 700, 'nf-l1', 'end')
text('~50 mL · fills between meals', 530, 718, 'nf-l2', 'end', unless=O('acute', 'acalc', 'chron', 'gbca', 'colic', 'hyd', 'xan'))

# cystic artery (an end artery) — lights up for acalculous cholecystitis
add('<path d="M760 540 C716 590 700 660 684 760" class="nf-art" style="stroke-width:4;opacity:.55"/>', unless=O('acalc'))
add('<path d="M760 540 C716 590 700 660 684 760" class="nf-art" style="stroke-width:6;stroke-dasharray:10 8"/>' + X(708, 640), when=O('acalc'))
text('cystic artery — an end artery', 900, 560, TAG, when=O('acalc'))

# ════════ duodenum, pancreas, small bowel ════════
DUO = 'M1090 950 C900 950 720 940 700 1020 L692 1280 C690 1360 760 1372 900 1372 L1240 1372 C1300 1372 1322 1322 1322 1262'
SB = 'M1322 1262 C1360 1192 1480 1222 1460 1330 C1440 1450 1220 1450 1110 1510 C990 1580 1090 1670 1250 1650 C1380 1630 1440 1670 1500 1702'
shapes += [dict(tube=DUO, w=34, color='--dk8'),
           dict(tube=SB, w=22, color='--dk8', mods=[dict(when=O('ileus'), d=14)])]
CEC = 'M1520 1650 C1560 1620 1640 1630 1660 1680 C1680 1740 1640 1790 1580 1786 C1530 1782 1506 1740 1512 1700 Z'
add(f'<path d="{CEC}" style="fill:var(--dk8);fill-opacity:.12;stroke:var(--dk8);stroke-width:4"/>'
    '<path d="M1620 1636 V1500" style="stroke:var(--dk8);stroke-width:46;opacity:.25;stroke-linecap:round"/>')
text('duodenum', 655, 1060, 'nf-l1', 'end')
text('from the stomach', 1112, 1000, 'nf-l2')
text('small bowel', 1490, 1400, 'nf-l2')
text('cecum', 1690, 1760, 'nf-l2')
text('ileocecal valve', 1498, 1736, 'nf-l2', 'end', unless=O('ileus'))
PANC = ('M760 1060 C800 1030 900 1040 960 1060 C1100 1040 1300 990 1460 960 C1520 950 1540 1000 1500 1030 '
        'C1350 1080 1150 1110 1000 1140 C990 1200 980 1280 900 1300 C820 1310 760 1280 750 1200 Z')
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3.5"/>', unless=O('gsp'))
add(f'<path d="{PANC}" style="fill:var(--bad);fill-opacity:.2;stroke:var(--bad);stroke-width:5"/>', when=O('gsp'))
PD = f'M1480 990 C1300 1030 1100 1080 1000 1100 L{AMP[0] + 12} {AMP[1] + 4}'
add(f'<path d="{PD}" style="fill:none;stroke:var(--dk5);stroke-width:7;opacity:.6"/>')
text('pancreas · pancreatic duct', 1260, 1110, 'nf-l2')
add(f'<rect x="{AMP[0] - 6}" y="{AMP[1] - 16}" width="14" height="32" rx="5" style="fill:var(--dk7)"/>')
text('ampulla · sphincter of Oddi', 655, 1166, 'nf-l2', 'end')
text('I cells — CCK', 655, 1230, 'nf-l2', 'end')

# ════════ stones and lesions, per option ════════
gbst = [(590, 838), (628, 846), (612, 808), (575, 805), (642, 812)]
add(''.join(stone(x, y, 17, CHOLST) for x, y in gbst), when=O('chol', 'chron', 'gbca'))
text('cholesterol stones — pale, radiolucent', 530, 830, TAG, 'end', when=O('chol'))
add(''.join(stone(570 + 13 * (i % 7), 800 + 13 * (i // 7) + (6 if i % 2 else 0), 6, BLACKST) for i in range(35)), when=O('black'))
text('many small black stones — sterile bile', 530, 830, TAG, 'end', when=O('black'))
CSt = bez(*CYS, .8)
add(stone(CSt[0], CSt[1], 13, CHOLST) + ''.join(stone(x, y, 15, CHOLST) for x, y in gbst[:3]), when=O('colic', 'acute'))
add(stone(CSt[0], CSt[1], 13, CHOLST), when=O('hyd'))
text('outlet blocked for a long time', 530, 760, TAG, 'end', when=O('hyd'))
text('dilated, filled with clear mucoid fluid', 530, 830, TAG, 'end', when=O('hyd'))
text('thick, shrunken, nodular wall', 530, 830, TAG, 'end', when=O('xan'))
text('stone jammed in the outlet', 530, 760, TAG, 'end', when=O('colic', 'acute'))
for dx in (-1, 1):
    add(f'<path d="M{610 + dx * 110} 730 l{-dx * 34} 0" style="stroke:var(--dk4);stroke-width:5" marker-end="url(#ah-gbWall)"/>', when=O('colic'))
text('CCK squeezes the gallbladder', 530, 830, TAG, 'end', when=O('colic'))
text('tense, inflamed wall — Murphy sign', 530, 830, TAG, 'end', when=O('acute'))
add(''.join(f'<circle cx="{575 + 9 * (i % 9)}" cy="{845 + 7 * (i // 9)}" r="3.5" style="fill:var(--dk10);opacity:.8"/>' for i in range(27)), when=O('acalc'))
text('no stone — sludge and ischemia', 530, 830, TAG, 'end', when=O('acalc'))
text('thick, fibrotic, maybe calcified wall', 530, 830, TAG, 'end', when=O('chron'))
add('<path d="M560 860 C548 820 570 780 600 790 C630 800 640 850 618 872 C600 884 570 884 560 860 Z" style="fill:var(--bad);fill-opacity:.4;stroke:var(--bad);stroke-width:4"/>'
    '<path d="M650 640 C700 600 720 560 700 500" class="dyn-lesion" marker-end="url(#ah-gbDuct)"/>', when=O('gbca'))
text('fundus mass · invades the liver', 530, 830, TAG, 'end', when=O('gbca'))
CDS = bez(*CBDC, .35)
add(stone(CDS[0], CDS[1], 15, CHOLST), when=O('cdl', 'ang'))
add(stone(CDS[0], CDS[1] - 14, 15, BROWNST) + stone(CDS[0] + 2, CDS[1] + 16, 13, BROWNST), when=O('brown'))
text('stone in the common bile duct — bile backs up', 832, CDS[1] + 6, TAG, when=O('cdl', 'ang'))
text('soft brown stones in an infected duct', 832, CDS[1] + 6, TAG, when=O('brown'))
text('jaundice · dark urine · pale stool', 832, CDS[1] + 26, 'nf-l2', when=O('cdl', 'ang'))
add(stone(AMP[0] + 14, AMP[1] - 14, 12, CHOLST), when=O('gsp'))
text('stone at the ampulla blocks the pancreatic duct', 1010, 1255, TAG, when=O('gsp'))
add('<path d="M630 878 L688 952" style="stroke:var(--bad);stroke-width:12;opacity:.6;stroke-linecap:round"/>'
    + stone(1506, 1704, 18, CHOLST), when=O('ileus'))
text('cholecystenteric fistula', 600, 940, TAG, 'end', when=O('ileus'))
text('stone stuck at the ileocecal valve', 1490, 1752, TAG, 'end', when=O('ileus'))
text('air in the bile ducts', 812, 640, TAG, when=O('ileus'))

# ════════ the wall, zoomed in ════════
AX0, AX1, LBX = 1580, 2340, 2096
box(AX0, 220, AX1, 896)
text('Gallbladder wall — zoomed in', 1600, 256, 'dyn-big')
text('no muscularis mucosae · no submucosa', 1600, 280, 'dyn-cap')
add(f'<rect x="1606" y="300" width="476" height="84" rx="10" style="fill:var(--dk10);fill-opacity:.12"/>')
text('lumen: hepatic bile in', LBX, 346, 'nf-l2')
CELLX = [1610 + 80 * i for i in range(6)]
for i, x in enumerate(CELLX):
    if i == 2: add(f'<rect x="{x}" y="390" width="70" height="132" rx="8" class="dyn-cell"/>', unless=O('acute', 'acalc'))
    else: add(f'<rect x="{x}" y="390" width="70" height="132" rx="8" class="dyn-cell"/>')
    add(f'<ellipse cx="{x + 35}" cy="492" rx="13" ry="17" style="fill:var(--ink-3);opacity:.45"/>' + ''.join(
        f'<path d="M{x + 8 + 9 * k} 390 v-9" style="stroke:var(--ink-3);stroke-width:2"/>' for k in range(7)), unless=O('acute', 'acalc') if i == 2 else None)
text('simple columnar cells', LBX, 446, 'nf-l1'); text('short microvilli · tight junctions', LBX, 464, 'nf-l2')
text('mucosal erosion', CELLX[2] + 35, 470, TAG, 'middle', when=O('acute', 'acalc'))
add(f'<rect x="1606" y="528" width="476" height="118" rx="6" style="fill:var(--dk5);fill-opacity:.08"/>', unless=O('acute', 'acalc'))
add(f'<rect x="1606" y="528" width="476" height="118" rx="6" style="fill:var(--bad);fill-opacity:.18"/>', when=O('acute', 'acalc'))
shapes.append(dict(vessel='M1620 622 H2068', w=16, color='--nf-blood', mods=[dict(when=O('acalc'), d=-10)]))
add(X(1840, 622), when=O('acalc'))
text('lamina propria', LBX, 580, 'nf-l1'); text('fenestrated capillaries', LBX, 598, 'nf-l2')
import random
rnd = random.Random(57)
bund = ''
for k in range(26):
    cx, cy, a = 1630 + (k % 9) * 52 + rnd.randint(-8, 8), 676 + (k // 9) * 34 + rnd.randint(-6, 6), rnd.randint(0, 179)
    bund += f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="7" transform="rotate({a} {cx} {cy})" style="fill:var(--dk2);opacity:.3"/>'
add(bund)
add('<rect x="1606" y="656" width="476" height="118" rx="6" style="fill:var(--ink-3);opacity:.22"/>', when=O('chron', 'xan'))
add(''.join(f'<circle cx="{x}" cy="{y}" r="13" style="fill:var(--surface);stroke:var(--dk5);stroke-width:3"/>'
            f'<circle cx="{x - 4}" cy="{y - 3}" r="2.5" style="fill:var(--dk5)"/><circle cx="{x + 4}" cy="{y + 4}" r="2.5" style="fill:var(--dk5)"/>'
            for x, y in ((1660, 690), (1740, 740), (1850, 700), (1960, 745))), when=O('xan'))
text('muscularis externa', LBX, 708, 'nf-l1'); text('bundles run every way', LBX, 726, 'nf-l2')
add('<rect x="1606" y="784" width="476" height="60" rx="6" style="fill:var(--dk8);fill-opacity:.12"/>')
text('adventitia (liver side)', LBX, 808, 'nf-l1'); text('serosa (free side)', LBX, 826, 'nf-l2')
# per-state changes in the wall
add(''.join(f'<circle cx="{x}" cy="{y}" r="5" style="fill:var(--dk7)"/>' for x, y in ((1660, 560), (1790, 580), (1950, 556))), when=O('acute'))
add('<path d="M2030 522 C2026 600 2020 720 2046 760 C2072 720 2066 600 2062 522" style="fill:var(--dk10);fill-opacity:.4;stroke:var(--dyn-cell-line);stroke-width:4"/>'
    + ''.join(f'<circle cx="{1620 + 26 * k}" cy="{838 if k % 2 else 832}" r="5" style="fill:var(--ink-3)"/>' for k in range(18)), when=O('chron'))
text('Rokitansky-Aschoff sinus', 2026, 770, TAG, 'end', when=O('chron'))
add(''.join(f'<circle cx="{x}" cy="{y}" r="11" style="fill:none;stroke:var(--bad);stroke-width:4"/>'
            for x, y in ((1650, 560), (1720, 690), (1800, 740), (1880, 680), (1960, 750))), when=O('gbca'))
add(''.join(f'<circle cx="{x}" cy="562" r="12" style="fill:var(--surface);stroke:var(--dk10);stroke-width:2"/>'
            f'<circle cx="{x - 4}" cy="559" r="2.5" style="fill:var(--dk10)"/><circle cx="{x + 4}" cy="566" r="2.5" style="fill:var(--dk10)"/>'
            for x in (1660, 1730, 1880, 1990)), when=O('chol'))
text('Na⁺, Cl⁻, HCO₃⁻ pumped into the side spaces · water follows (AQP1, AQP8) · ~90% removed', 1600, 880, 'dyn-cap',
     unless=O('acute', 'acalc', 'chron', 'gbca', 'chol', 'hyd', 'xan'))
text('cholesterolosis (“strawberry gallbladder”): foamy macrophages in the lamina propria', 1600, 880, 'dyn-cap', when=O('chol'))
text('acute: edema, congestion, mucosal erosion, early neutrophils', 1600, 880, 'dyn-cap', when=O('acute'))
text('acalculous: the same injury — from ischemia of the cystic artery', 1600, 880, 'dyn-cap', when=O('acalc'))
text('chronic: fibrosis, Rokitansky-Aschoff sinus, calcified wall (porcelain)', 1600, 880, 'dyn-cap', when=O('chron'))
text('carcinoma: malignant glands infiltrating a fibrotic wall', 1600, 880, 'dyn-cap', when=O('gbca'))
text('hydrops: an atrophic, obstructed wall — only clear secretions inside', 1600, 880, 'dyn-cap', when=O('hyd'))
text('xanthogranulomatous: foamy macrophages after Rokitansky-Aschoff sinuses rupture', 1600, 880, 'dyn-cap', when=O('xan'))

# ════════ what the bile holds (schematic) ════════
box(AX0, 920, AX1, 1270)
text('What the bile holds', 1600, 956, 'dyn-big')
text('schematic · cholesterol stays dissolved only in micelles with bile salts and lecithin', 1600, 980, 'dyn-cap')
BASE = 1220
def bar(cx, h, col, when=None, unless=None):
    add(f'<rect x="{cx - 55}" y="{BASE - h}" width="110" height="{h}" rx="6" style="fill:var({col});fill-opacity:.7"/>', when=when, unless=unless)
bar(1720, 90, '--dk10', unless=O('chol')); bar(1720, 190, '--dk10', when=O('chol'))
bar(1960, 170, '--dk6', unless=O('chol')); bar(1960, 80, '--dk6', when=O('chol'))
bar(2200, 40, '--dk5', unless=O('black', 'brown')); bar(2200, 170, '--dk5', when=O('black', 'brown'))
add(f'<path d="M1630 {BASE} H2290" class="dyn-line"/>')
text('cholesterol', 1720, BASE + 24, 'nf-l1', 'middle')
text('bile salts + lecithin', 1960, BASE + 24, 'nf-l1', 'middle')
text('unconjugated bilirubin', 2200, BASE + 24, 'nf-l1', 'middle')
text('more cholesterol than micelles can hold → crystals', 1600, 1012, TAG, when=O('chol'))
text('hemolysis or ileal disease: ~1% of the extra bilirubin deconjugates', 1600, 1012, TAG, when=O('black'))
text('bacterial β-glucuronidase deconjugates bilirubin', 1600, 1012, TAG, when=O('brown'))

# ════════ the tell ════════
C = {
  '': ['The gallbladder between meals', 'the sphincter of Oddi is shut, so bile backs up into it and is concentrated up to 10–20-fold',
       'after fat: CCK contracts it and relaxes the sphincter of Oddi'],
  'chol': ['Cholesterol stones — about 80% of stones', '↑ cholesterol, ↓ bile salts, stasis · estrogen, obesity, rapid weight loss, fibrates',
           'over 50% cholesterol · 10–20% radiopaque · ursodiol dissolves small ones'],
  'black': ['Black pigment stones — sterile gallbladder bile', 'chronic hemolysis (spherocytosis, sickle cell) · ileal disease or resection',
            'small, many, friable, spiculated · 50–75% radiopaque'],
  'brown': ['Brown pigment stones — infected large bile ducts', 'infection (E. coli, Ascaris, Clonorchis) → microbial β-glucuronidase',
            'soft, greasy, laminated (calcium soaps) · radiolucent'],
  'colic': ['Biliary colic — no inflammation', 'after a fatty meal, CCK squeezes a stone into the outlet',
            'steady RUQ pain, to the right shoulder or back · labs normal'],
  'acute': ['Acute calculous cholecystitis — 90% of cases', 'RUQ pain over 6 h, mild fever, Murphy sign · E. coli, Enterococcus later',
            'pus = empyema · necrosis = gangrenous · gas-formers = emphysematous'],
  'acalc': ['Acalculous cholecystitis — about 10%', 'ICU: sepsis with hypotension, burns, trauma, immunosuppression',
            'recognized late → gangrene and perforation more often'],
  'chron': ['Chronic cholecystitis — stones in over 90%', 'fibrosis · Rokitansky-Aschoff sinuses · hydrops, xanthogranulomatous forms',
            'porcelain gallbladder → adenocarcinoma risk → prophylactic cholecystectomy'],
  'hyd': ['Hydrops of the gallbladder — a chronic cholecystitis form', 'chronically obstructed, often dilated, atrophic gallbladder',
          'holds only clear mucoid fluid'],
  'xan': ['Xanthogranulomatous cholecystitis — a chronic form', 'Rokitansky-Aschoff sinuses rupture and spill bile into the wall',
          'massively thick, shrunken, nodular · foamy xanthoma cells · necrosis, hemorrhage'],
  'gbca': ['Gallbladder carcinoma — adenocarcinoma, fundus', 'gallstones in ~95% · women over 2× · Chile, Bolivia, northern India',
           'found late (liver, porta hepatis; jaundice = advanced) · 5-year survival under 10%'],
  'cdl': ['Choledocholithiasis — a stone in the common bile duct', '↑ ALP, GGT, direct bilirubin (± AST, ALT) · jaundice',
          'small stones (“gravel”) slip out of the gallbladder'],
  'ang': ['Ascending cholangitis', 'Charcot triad: fever, jaundice, RUQ pain · + confusion, shock = Reynolds pentad',
          'coliforms climb the stagnant ducts · neutrophils in the duct epithelium'],
  'gsp': ['Gallstone pancreatitis', 'a stone or sludge blocks the pancreatic duct at the ampulla',
          'epigastric pain to the back · lipase over 3× normal · ~5% of stone carriers'],
  'ileus': ['Gallstone ileus', 'a large stone erodes through a cholecystenteric fistula',
            'Rigler triad: pneumobilia, small bowel obstruction, ectopic gallstone'],
}
TY = 1300
box(AX0, TY, AX1, TY + 150)
text('The tell', 1600, TY + 36, 'dyn-big')
for k, lines in C.items():
    for i, t in enumerate(lines):
        kw = dict(unless=[f'{SW}:*']) if k == '' else dict(when=O(k))
        text(t, 1600, TY + 66 + 26 * i, 'nf-l2' if i else 'nf-l1', **kw)

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
CBD_BLOCK = O('cdl', 'ang', 'brown')
CYS_BLOCK = O('colic', 'acute', 'hyd')
CBD_TO_DUO = f'C800 850 790 1000 760 1100 L{AMP[0]} {AMP[1]} L700 1180 L694 1300'
cdx, cdy = bez(*CBDC, .3)
flows = [
  # left hepatic duct → common hepatic → common bile duct → duodenum
  dict(d=f'M1000 400 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} {CBD_TO_DUO}', len=1060, speed=120, r=6, base=dict(bile=5), unless=CBD_BLOCK + O('gsp')),
  dict(d=f'M1000 400 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} L{cdx} {cdy}', len=680, speed=60, r=6, base=dict(bile=6), when=CBD_BLOCK),
  dict(d=f'M1000 400 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} C800 850 790 1000 760 1100 L{AMP[0] + 4} {AMP[1] - 26}', len=920, speed=80, r=6, base=dict(bile=6), when=O('gsp')),
  # right hepatic duct → cystic duct → gallbladder (filling between meals)
  dict(d=f'M560 420 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} C760 640 700 548 650 572 L615 760', len=840, speed=110, r=6, base=dict(bile=5),
       unless=CYS_BLOCK + CBD_BLOCK + O('gsp')),
  dict(d=f'M560 420 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} {CBD_TO_DUO}', len=1100, speed=120, r=6, base=dict(bile=4), when=CYS_BLOCK),
  dict(d=f'M560 420 L{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]} L{cdx} {cdy}', len=680, speed=60, r=6, base=dict(bile=5), when=CBD_BLOCK + O('gsp')),
  # pancreatic juice to the ampulla
  dict(d=f'{PD} L700 1186 L694 1290', len=950, speed=130, r=6, base=dict(pj=5), unless=O('gsp')),
  dict(d='M1480 990 C1300 1030 1100 1080 1000 1100 L790 1150', len=730, speed=60, r=6, base=dict(pj=5), when=O('gsp')),
  dict(d='M900 1140 C960 1190 900 1260 840 1220 C800 1190 840 1140 900 1140', len=360, speed=60, r=6, base=dict(pj=4), when=O('gsp')),
  # CCK from the duodenal I cells to the gallbladder (blood route, schematic)
  dict(d='M690 1230 C560 1150 540 950 600 790', len=520, speed=110, r=7, base=dict(cck=4), when=O('colic')),
  # bacteria: in the brown-stone duct, and climbing the obstructed tree in cholangitis
  dict(d=f'M{cdx} {cdy + 40} L{cdx - 6} {cdy - 40} L{cdx + 6} {cdy + 40}', len=170, speed=40, r=6, base=dict(bact=4), when=O('brown')),
  dict(d=f'M{cdx} {cdy - 10} L{JN[0]} {JN[1]} L{HUB[0]} {HUB[1]} L560 420', len=700, speed=70, r=6, base=dict(bact=5), when=O('ang')),
  dict(d=f'M{cdx} {cdy - 10} L{JN[0]} {JN[1]} L{HUB[0]} {HUB[1]} L1000 400', len=720, speed=70, r=6, base=dict(bact=4), when=O('ang')),
  # gallstone ileus: the stone's trip, and air climbing into the bile ducts
  dict(d=f'M630 878 L692 952 L694 1020 L692 1280 C690 1360 760 1372 900 1372 L1240 1372 C1300 1372 1322 1322 1322 1262 '
         'C1360 1192 1480 1222 1460 1330 C1440 1450 1220 1450 1110 1510 C990 1580 1090 1670 1250 1650 C1380 1630 1440 1670 1490 1700',
       len=2700, speed=110, r=15, base=dict(stone=1), when=O('ileus')),
  dict(d=f'M692 960 L630 878 L615 700 L650 572 C700 548 760 640 {JN[0]} {JN[1]} L{HUB[0]} {HUB[1]}', len=780, speed=90, r=7, base=dict(air=4), when=O('ileus')),
]
# the wall: salt pumped into the lateral spaces, water following, both into the capillary
for sx in (1685, 1845, 2005):
    flows.append(dict(d=f'M{sx - 30} 330 L{sx - 30} 470 L{sx} 470 L{sx} 560 L{sx + 20} 618', len=360, speed=70, r=6, base=dict(salt=2)))
    flows.append(dict(d=f'M{sx + 28} 330 L{sx + 28} 440 L{sx} 440 L{sx} 560 L{sx - 20} 618', len=360, speed=70, r=6, base=dict(h2o=3)))

sites = [
  dict(x=2005, y=455, n=[1, 0], w=8, t='pump', l='', aria='Na⁺/K⁺-ATPase on the lateral membrane', c='gbstruct', ions=[['salt', 'out', 1]]),
  dict(x=1925, y=430, n=[-1, 0], w=8, t='aqp', l='', aria='Aquaporins AQP1 and AQP8', c='gbstruct', ions=[['h2o', 'out', 1]]),
  dict(x=AMP[0] - 40, y=AMP[1] + 60, n=[-1, 0], w=10, t='rec', l='', aria='I cells — cholecystokinin', c='cck', ions=[]),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Bile cholesterol', mods=[R(O('chol'), 1)]),
  dict(l='Bile salts', mods=[R(O('chol'), -1)]),
  dict(l='Unconjugated bilirubin in bile', mods=[R(O('black', 'brown'), 1)]),
  dict(l='RUQ pain', mods=[R(O('colic', 'acute', 'chron', 'ang'), 1)]),
  dict(l='ALP · direct bilirubin', mods=[R(O('cdl', 'ang'), 1), R(O('colic'), 0)]),
  dict(l='Fever', mods=[R(O('acute', 'ang'), 1)]),
  dict(l='Lipase', mods=[R(O('gsp'), 1)]),
]

# ════════ notes ════════
notes = {
  '': 'Between meals the sphincter of Oddi is shut, so bile backs up the cystic duct into the gallbladder, whose cells pump Na⁺, Cl⁻ '
      'and HCO₃⁻ into the spaces between them; water follows and about 90% of it is removed, concentrating bile salts, cholesterol '
      'and bilirubin up to 10–20-fold. After a fatty meal, CCK contracts the gallbladder and relaxes the sphincter.',
  'g:chol': 'Cholesterol stones (about 80%; over 50% cholesterol monohydrate) form when bile carries more cholesterol than its bile '
            'salts and lecithin can hold in micelles: crystals nucleate, a sluggish gallbladder keeps them and mucin glues them into '
            'stones. Estrogen, obesity, rapid weight loss and fibrates raise biliary cholesterol; ursodiol lowers it and can dissolve '
            'small radiolucent stones.',
  'g:black': 'Black pigment stones form in sterile gallbladder bile when chronic hemolysis (hereditary spherocytosis, sickle cell) '
             'or ileal disease makes the liver pour out conjugated bilirubin: about 1% deconjugates, and the unconjugated bilirubin '
             'precipitates with calcium. Small, many, friable; 50–75% radiopaque.',
  'g:brown': 'Brown pigment stones form in infected large bile ducts: infection with E. coli, Ascaris or Clonorchis releases microbial β-glucuronidase, which '
             'deconjugates bilirubin so calcium bilirubinate precipitates with calcium soaps. Soft, greasy, laminated — radiolucent.',
  'g:colic': 'Biliary colic: after a fatty meal CCK contracts the gallbladder and forces a stone into its outlet — steady RUQ or '
             'epigastric pain that can spread to the right shoulder or back, with nausea. Nothing is inflamed, so the labs are normal.',
  'g:acute': 'Acute calculous cholecystitis (90%): a stone stays impacted in the neck or cystic duct; lysolecithin and bile salts '
             'injure the mucosa and the distended wall loses blood flow, with E. coli or Enterococcus superinfection later. RUQ pain '
             'over 6 hours, fever, Murphy sign, pain to the right shoulder; jaundice means the common bile duct is involved.',
  'g:acalc': 'Acalculous cholecystitis (10%): no stone — ischemia through the cystic artery, an end artery, plus stasis and sludge, '
             'in the critically ill (sepsis with hypotension, burns, trauma, immunosuppression). Found late, so gangrene and '
             'perforation are more frequent than with stones.',
  'g:chron': 'Chronic cholecystitis: stones in over 90%, after repeated attacks or none. Fibrosis thickens the wall, Rokitansky-'
             'Aschoff sinuses push mucosa through the muscle, and extensive dystrophic calcification makes a porcelain gallbladder, '
             'which raises the risk of adenocarcinoma.',
  'g:hyd': 'Hydrops of the gallbladder: a form of chronic cholecystitis in which a chronically obstructed, often dilated and '
           'atrophic gallbladder holds only clear mucoid secretions — no bile reaches it past the blocked outlet.',
  'g:xan': 'Xanthogranulomatous cholecystitis: a form of chronic cholecystitis in which Rokitansky-Aschoff sinuses rupture and '
           'spill bile into the wall; macrophages that eat the biliary lipids become foamy xanthoma cells. The wall is massively '
           'thickened, shrunken and nodular, with foci of necrosis and hemorrhage.',
  'g:gbca': 'Gallbladder carcinoma: an adenocarcinoma, usually of the fundus, driven by chronic inflammation — gallstones in about '
            '95%, though only 1–2% of stone carriers get it. It mimics gallstone disease and is found late, invading the liver and '
            'porta hepatis: 5-year survival under 10%.',
  'g:cdl': 'Choledocholithiasis: a stone in the common bile duct dams bile behind it — the ducts dilate and ALP, GGT and direct '
           'bilirubin rise, often with the aminotransferases, with jaundice. Small stones are the ones that slip out of the '
           'gallbladder; the blocked duct invites cholangitis and pancreatitis.',
  'g:ang': 'Ascending cholangitis: obstruction leaves bile stagnant, and enteric coliforms (E. coli, Enterococcus, Klebsiella) '
           'climb the tree — Charcot triad of fever, jaundice and RUQ pain; add confusion and shock for Reynolds pentad. Neutrophils '
           'fill the duct epithelium and lumen.',
  'g:gsp': 'Gallstone pancreatitis: a stone or sludge blocks the pancreatic duct at the ampulla, ductal pressure rises and enzyme-'
           'rich fluid leaks into the gland, where lipase starts fat necrosis. Epigastric pain to the back with lipase over 3× normal.',
  'g:ileus': 'Gallstone ileus: a large stone erodes from an inflamed gallbladder into the bowel through a cholecystenteric fistula '
             'and lodges at the ileocecal valve, the narrowest point. Air enters the bile ducts — Rigler triad: pneumobilia, small '
             'bowel obstruction, ectopic gallstone.',
}

dyn = dict(
  # one colour per "Show" group, so the chips double as the colour key (the drafts check.py takes 2-element kinds)
  kinds=dict(bile=['bile', '--dk10'], stone=['bile', '--dk10'], pj=['pj', '--dk5'], salt=['salt', '--nf-na'], h2o=['h2o', '--nf-h2o'],
             cck=['cck', '--dk4'], bact=['bact', '--dk7'], air=['air', '--ink-3']),
  groups=[['bile', 'Bile · a moving stone'], ['pj', 'Pancreatic juice'], ['salt', 'Na⁺ · Cl⁻ · HCO₃⁻'], ['h2o', 'Water'], ['cck', 'CCK'],
          ['bact', 'Bacteria'], ['air', 'Air']],
  switches=[dict(id=SW, label='Pick a stone or a complication', type='one', options=[
    ['chol', 'Cholesterol stones', 'gallstones'], ['black', 'Black pigment stones', 'gallstones'], ['brown', 'Brown pigment stones', 'gallstones'],
    ['colic', 'Biliary colic', 'cholecystitis'], ['acute', 'Acute cholecystitis', 'cholecystitis'], ['acalc', 'Acalculous cholecystitis', 'cholecystitis'],
    ['chron', 'Chronic cholecystitis · porcelain gallbladder', 'cholecystitis'],
    ['hyd', 'Hydrops · clear mucoid fluid', 'cholecystitis'], ['xan', 'Xanthogranulomatous cholecystitis', 'cholecystitis'],
    ['gbca', 'Gallbladder carcinoma', 'gbca'],
    ['cdl', 'Choledocholithiasis', 'gallstones'], ['ang', 'Ascending cholangitis', 'cholangitis'], ['gsp', 'Gallstone pancreatitis', 'acutepanc'],
    ['ileus', 'Gallstone ileus', 'gallstones']],
    sections=[['Stones', ['chol', 'black', 'brown']], ['Gallbladder', ['colic', 'acute', 'acalc', 'chron', 'hyd', 'xan', 'gbca']],
              ['Ducts & beyond', ['cdl', 'ang', 'gsp', 'ileus']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI lecture notes (SDL 13, 16, 18, 20) · First Aid pp. 378, 403–404, 428 · Robbins ch 18–19 · Pawlina ch 18 · Guyton ch 65 · Katzung ch 62')

# ════════ the one new card: the gallbladder's own structure and concentrating job (no card covers it) ════════
card('gbstruct', 'Gallbladder wall & bile concentration', 'reg', 'gbWall', 'Simple columnar cells pump salt; water follows', 0,
     'Between meals the gallbladder stores bile and removes about <b>90% of its water</b>: its epithelial cells actively pump '
     '<b>Na⁺, Cl⁻ and HCO₃⁻</b> across their lateral membranes (Na⁺/K⁺-ATPase) into the intercellular spaces, water follows through '
     '<b>aquaporins</b> (AQP1, AQP8), and the nearly isotonic fluid passes into the fenestrated capillaries of the lamina propria. '
     'Bile salts, cholesterol and bilirubin stay behind and concentrate.',
     ['Concentrates bile up to 10–20-fold (Pawlina: up to 10-fold; Guyton: about 5-fold, at most 20-fold) · holds about 50 mL',
      'Empty or partly filled: many deep <b>mucosal folds</b> that flatten as it fills',
      '<b>Simple columnar epithelium</b> (cholangiocytes): short microvilli, apical tight junctions, many mitochondria — like intestinal absorptive cells',
      'Wall: mucosa → muscularis externa (bundles run every way) → adventitia (liver side) or serosa — <b>no muscularis mucosae, no submucosa</b>',
      '<b>CCK</b> from duodenal I cells (fat) contracts it and relaxes the sphincter of Oddi'],
     ['Gallbladder bile vs hepatic bile: bile salts 6 vs 1.1 g/dL, Cl⁻ 25 vs 100 mEq/L; Ca²⁺ is not absorbed (Guyton)'],
     ['Gallbladder wall has no muscularis mucosae and no submucosa'],
     [PW18, GY65],
     ['—'],
     ['gallbladder mucosa', 'gallbladder epithelial cells', 'gallbladder epithelium', 'hepatic bile'],
     fa='378')

MAP = dict(
  id='gallsim', title='Gallstones & the Gallbladder in Motion', topic='gi', after='biliflow',
  sub='Bile fills the gallbladder between meals and its wall pulls the water out — then pick a stone (cholesterol, black, brown) or '
      'a complication (colic, acute, acalculous or chronic cholecystitis, carcinoma, a duct stone, cholangitis, pancreatitis, '
      'gallstone ileus) and see where the stone sits and what follows. Tap a pump for its card',
  w=3500, h=2060,
  fa='378, 403, 404, 427, 428', src=SRC,
  lanes=[('gbStone', 'Stones', 'glycolysis'), ('gbWall', 'Gallbladder', 'tca'), ('gbDuct', 'Ducts & beyond', 'gluconeo')],
  nodes=[
    ('gs1', 'Gallstones', 330, 1880, 'gbStone', 'cholesterol · pigment', ['gallstones', 'bileacid'], 'hub'),
    ('gs2', 'Hemolysis → black stones', 760, 1880, 'gbStone', 'hereditary spherocytosis', ['hs']),
    ('gs3', 'Estrogen · the pill', 1190, 1880, 'gbStone', '↑ biliary cholesterol', ['ocp']),
    ('gs4', 'Gallbladder wall', 1620, 1880, 'gbWall', 'pumps salt, water follows', ['gbstruct', 'simcol'], 'hub'),
    ('gs5', 'CCK', 2050, 1880, 'gbWall', 'I cells · squeezes it', ['cck']),
    ('gs6', 'Cholecystitis', 330, 2000, 'gbWall', 'colic · acute · chronic', ['cholecystitis', 'necrosis'], 'hub'),
    ('gs7', 'Porcelain GB · carcinoma', 760, 2000, 'gbWall', 'dystrophic calcification', ['calcification', 'gbca']),
    ('gs8', 'Cholangitis', 1190, 2000, 'gbDuct', 'Charcot triad', ['cholangitis', 'ecoli', 'enterococcus']),
    ('gs9', 'Gallstone pancreatitis', 1620, 2000, 'gbDuct', 'lipase over 3×', ['acutepanc']),
    ('gs10', 'Gallstone ileus', 2050, 2000, 'gbDuct', 'ileocecal valve', ['sbo'])],
  panels=[
    (2420, 800, 1000, 'Bile: liver vs gallbladder (Guyton ch 65, Table 65.2)', [
      ('Water', '97.5 → 92 g/dL'),
      ('Bile salts', '1.1 → 6 g/dL'),
      ('Bilirubin · cholesterol', '0.04 → 0.3 · 0.1 → 0.3–0.9 g/dL'),
      ('Na⁺ · Cl⁻ · HCO₃⁻', '145 → 130 · 100 → 25 · 28 → 10 mEq/L'),
      ('Ca²⁺', '5 → 23 mEq/L — not absorbed')]),
    (2420, 1060, 1000, 'Cholesterol vs pigment stones (lecture notes SDL 18 · First Aid p. 403)', [
      ('Cholesterol', 'about 80% · over 50% cholesterol · only 10–20% radiopaque'),
      ('Black pigment', 'sterile gallbladder bile · hemolysis, ileal disease · 50–75% radiopaque'),
      ('Brown pigment', 'infected large ducts · β-glucuronidase · radiolucent'),
      ('Common thread', '↑ cholesterol or bilirubin, ↓ bile salts, stasis')])],
  dyn=dyn,
)
