# m58 — Autoimmune Liver Disease — AIH, Primary Biliary & Sclerosing Cholangitis (dynamic map, kit data)
# Left: a front view of the liver (patient's right on your left) with its bile-duct tree — interlobular twigs at the edges,
# right and left hepatic ducts, common hepatic duct, gallbladder, common bile duct through the pancreatic head to the
# ampulla and duodenum; bile runs down the tree. Middle: one small portal tract magnified (portal vein, hepatic artery,
# interlobular bile duct, the limiting plate of hepatocytes, a canal of Hering fed by canaliculi). Below it: the bile's
# path from hepatocyte to duodenum as one strip, lit where the chosen disease strikes. One `one` switch, "Pick a disease
# or a drug" (sections: autoimmune · other cholestasis · injury · treating PBC), puts each lesion in place: interface
# hepatitis (AIH), the florid duct lesion and lost twigs (PBC), onion-skin fibrosis and beaded large ducts (PSC), a stone
# with dilated ducts above (large duct obstruction), septa and nodules (secondary biliary cirrhosis), bile plugs in canals
# of Hering (cholestasis of sepsis), scattered hepatocyte injury (drug-induced), massive necrosis and a shrunken liver
# (acute liver failure), ursodiol replacing the bile acids, obeticholic acid on FXR. 7 readouts.
# Not repeated: lftsim (Liver Tests Decoder — the enzyme decision tree, which also lists AIH/PBC/PSC as answers),
# lobulesim (lobule histology), portsim (zones), gallsim (stones), biliflow (bilirubin).
#
# Sources (all read in the corpus; the course text wins for this block):
#   GI Exam 1 lecture notes (corpus/gastro/course_exam1_lecture_notes.txt):
#     p. 82–83 (SDL 15 §1): acute liver failure = encephalopathy + coagulopathy within 26 weeks of the first injury, no
#       preexisting liver disease; massive necrosis, small shrunken liver; ammonia → encephalopathy, asterixis; clotting
#       factors II, V, VII, IX, X, XI, XII, fibrinogen not made; stellate cells → septa, regenerative nodules = cirrhosis.
#     p. 85 (SDL 15): cholestasis of sepsis — direct bacterial action, hypotension, or circulating endotoxins; ductular
#       (cholangiolar) cholestasis: dark bile plugs in dilated canals of Hering and ductules at the portal–parenchymal
#       interface, minimal parenchymal inflammation.
#     p. 86–87 (SDL 15 §4): AIH — 78% female, HLA-DR3 (Europeans), DR4 (Japanese), DRB1 (South Americans); triggers:
#       viruses, minocycline, nitrofurantoin, α-methyldopa, vaccines; CD4 T cells drive B cells to make autoantibodies, CD8
#       cytotoxic T cells with CD4 cells attack hepatocytes at the interface; interface hepatitis, lymphoplasmacytic
#       infiltrates with plasma-cell clusters, emperipolesis, bridging necrosis, rosettes; type 1: ANA + anti-smooth muscle
#       actin, ± anti-SLA/LPA, IgG > 1.1× ULN, all ages, thyroiditis/T1DM/celiac; type 2: children and adolescents, anti-LKM1
#       (against CYP2D6) and/or anti-LC1, ANA and SMA typically absent, IgG also high.
#     p. 87–88 (SDL 15 §5): DILI — direct (predictable, dose-dependent) vs idiosyncratic (unpredictable, not dose-dependent,
#       a small minority, weeks to months; CYP, transporter, HLA variants); acute idiosyncratic hepatitis (isoniazid,
#       nitrofurantoin, phenytoin, methyldopa, checkpoint inhibitors; ALT ≥ 5× ULN); cholestatic hepatitis
#       (amoxicillin-clavulanate, phenothiazines, statins; ALP ≥ 2× ULN); acetaminophen = direct.
#     p. 62 (SDL 11): uncorrected extrahepatic biliary atresia → secondary biliary cirrhosis by 3 to 6 months of age.
#     p. 93–95 (SDL 16 §4–5): large bile duct obstruction — CBD stones, biliary/pancreatic-head cancer, strictures, PSC;
#       children: biliary atresia, choledochal cyst, cystic fibrosis; jaundice, pruritus, dark urine, acholic stools;
#       ↑ ALP, GGT, conjugated bilirubin; uncorrected → periductal fibrosis → biliary cirrhosis with "jigsaw" nodules;
#       ascending cholangitis (Charcot triad). PBC: 90% female (9:1), 40–50 y, Sjögren 70%, thyroiditis, scleroderma, RA,
#       Raynaud, celiac; T cell destruction of small- and medium-sized intrahepatic interlobular ducts (large and
#       extrahepatic ducts spared); florid duct lesion (granulomatous, lymphoplasmacytic); ductopenia; AMA 95% (PDC-E2 of
#       pyruvate dehydrogenase), ANA 40–50%; fatigue, intense pruritus. PSC: 70% male (2:1), 3rd–5th decades, UC in ~70%;
#       extrahepatic and large intrahepatic ducts; onion-skin periductal fibrosis; beading on MRCP/ERCP; p-ANCA ~65%, AMA
#       characteristically negative; often found by a raised ALP in UC screening; cholangiocarcinoma lifetime risk 20%.
#     p. 112–113 (SDL 20 §2): ursodiol — hydrophilic bile acid, < 5% of the pool, 30–50% with long-term use; ↓ biliary
#       cholesterol by suppressing hepatic cholesterol secretion; stabilizes canalicular membranes, replaces toxic hydrophobic
#       bile acids; gallstone dissolution, prevention during rapid weight loss, first-line for early PBC (13–15 mg/kg/day):
#       "reduces hepatic biochemical abnormalities", slows progression, delays transplant; not hepatotoxic (unlike
#       chenodeoxycholate). Obeticholic acid — synthetic chenodeoxycholate derivative, FXR agonist → ↓ hepatic bile acid
#       synthesis; protects hepatocytes and cholangiocytes; PBC 5–10 mg/day with ursodiol after inadequate response (or
#       alone if ursodiol not tolerated); severe dose-dependent pruritus in up to 25%.
#   Robbins ch 18 (course_sdl_15_19_patho.txt): p. 4 (Table 18.1: ALP, GGT ↑ from canalicular damage; PT/PTT clotting
#     factors ↓) · p. 10–12 (acute liver failure: acetaminophen almost 50% of US adult cases, massive necrosis, small shrunken
#     liver, transaminases markedly elevated) · p. 44–45 (AIH types, ANA/ASMA vs anti-LKM1 against CYP2D6 and anti-LC1, serum
#     IgG, prednisone ± azathioprine) · p. 79–81 (ALP and GGT characteristic of cholestasis; large duct obstruction, proximal
#     duct dilation, portal edema, ductular reaction, neutrophils; persistent obstruction → biliary cirrhosis) · p. 83–84
#     (cholestasis of sepsis, gram-negative) · p. 89–95 (PBC vs PSC table, florid duct lesion, IgM, ALP; PSC beading,
#     onion skin, 2:1 male, UC 70%).
#   Katzung ch 62 (course_sdl_10_20_pharm.txt): ursodiol "improves liver biochemical abnormalities" in PBC; obeticholic acid
#     FXR ligand, added to ursodiol; pruritus up to 25%.
#   First Aid 2025 p. 397 (ALP ↑ in cholestasis, GGT ↑ in liver and biliary disease, PT ↑ in advanced disease) · p. 399
#     (AIH: anti-smooth muscle or anti-LKM1, ↑ ALT and AST, portal/periportal lymphoplasmacytic infiltrate) · p. 402 (biliary
#     tract disease: ↑ conjugated bilirubin, cholesterol, ALP, GGT; PSC: onion skin, beading, p-ANCA, ↑ IgM, UC, 2° biliary
#     cirrhosis, cholangiocarcinoma; PBC: lymphocytic infiltrate ± granulomas, AMA, ↑ IgM, ursodiol; secondary biliary
#     cirrhosis: extrahepatic obstruction → ↑ intrahepatic duct pressure → injury, fibrosis, bile stasis).
#
# Arrows deliberately left "–":
#   Ursodiol / obeticholic acid → ALP: the sources say ursodiol "reduces hepatic biochemical abnormalities" (lecture) /
#     "improves liver biochemical abnormalities" (Katzung) and never name ALP — no arrow (owner call; the spec had ↓).
#   AIH ALP (Robbins: "mild elevations … can occur" in chronic hepatitis) · AIH AMA (Robbins: "less commonly" in type 1) ·
#   PBC ANA (40–50%) · cholestasis of sepsis ALP/GGT (no lab stated for it) · drug-induced injury ALT or ALP (depends on the
#   pattern) · secondary biliary cirrhosis PT (FA: "advanced liver disease" — not stated for it).
#   AIH serum IgG ↑ is sourced but there is no IgG readout (7 max) — it is in the note and the panel.
# Shown as ↔ (stated negative): PSC AMA ("characteristically negative", lecture p. 95; Robbins "typically negative").
# Source conflicts: PBC non-responders to ursodiol — Robbins "up to 40%", Katzung "approximately 35%" (not printed).
#   PSC male share — lecture/Robbins 70% (2:1); FA "middle-aged males" (no number) — no conflict.
# Cut: HLA-B8 in PSC (Robbins only), nodular regenerative hyperplasia, IgG4 cholangitis, small-duct PSC, overlap syndrome,
#   transplant survival figures.
import sys, re, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

RB18, KZ62 = full('Robbins', 18), full('Katzung', 62)

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
def X(cx, cy, s=12): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def plen(d):
    """length of an M/L/H/V/C path (absolute commands only)"""
    tok = re.findall(r'[MLHVC]|-?\d+\.?\d*', d); i = 0; x = y = 0.0; L = 0.0; cmd = 'M'
    while i < len(tok):
        if tok[i] in 'MLHVC': cmd = tok[i]; i += 1; continue
        if cmd == 'M': x, y = float(tok[i]), float(tok[i + 1]); i += 2
        elif cmd == 'L': nx, ny = float(tok[i]), float(tok[i + 1]); L += math.hypot(nx - x, ny - y); x, y = nx, ny; i += 2
        elif cmd == 'H': nx = float(tok[i]); L += abs(nx - x); x = nx; i += 1
        elif cmd == 'V': ny = float(tok[i]); L += abs(ny - y); y = ny; i += 1
        elif cmd == 'C':
            p = [(x, y)] + [(float(tok[i + k]), float(tok[i + k + 1])) for k in (0, 2, 4)]; i += 6
            px, py = p[0]
            for s in range(1, 21):
                t = s / 20; u = 1 - t
                qx = u ** 3 * p[0][0] + 3 * u * u * t * p[1][0] + 3 * u * t * t * p[2][0] + t ** 3 * p[3][0]
                qy = u ** 3 * p[0][1] + 3 * u * u * t * p[1][1] + 3 * u * t * t * p[2][1] + t ** 3 * p[3][1]
                L += math.hypot(qx - px, qy - py); px, py = qx, qy
            x, y = p[3]
    return round(L)
def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(round(u ** 3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t ** 3 * d) for a, b, c, d in zip(p0, p1, p2, p3))

SW = 'a'
O = lambda *k: [f'{SW}:{x}' for x in k]
TAG = 'nf-l1 dyn-tag'
OBST = O('obst', 'sbc')

text('Where each disease strikes the bile’s path — hepatocytes, small ducts, large ducts or the common duct', 160, 80, 'dyn-big')
text('front view, patient’s right on your left · gold dots = bile · the boxed twig is magnified in the middle', 160, 104, 'dyn-cap')

# ════════ liver and bile-duct tree ════════
LIVER = 'M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z'
FALC = 'M58 62 C56 40 56 20 58 6'
def scale(d, x, y, w, h):
    return re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}', d)
LD, LF = scale(LIVER, 190, 230, 1000, 440), scale(FALC, 190, 230, 1000, 440)
LDS = scale(LIVER, 250, 270, 860, 380)          # acute liver failure: small, shrunken
add(f'<path d="{LD}" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:3.5;opacity:.8"/>'
    f'<path d="{LF}" style="fill:none;stroke:var(--dk2);stroke-width:2;opacity:.45"/>', unless=O('alf'))
add(f'<path d="{LD}" style="fill:none;stroke:var(--ink-3);stroke-width:2.5;stroke-dasharray:8 8;opacity:.6"/>'
    f'<path d="{LDS}" style="fill:var(--bad);fill-opacity:.1;stroke:var(--bad);stroke-width:4"/>', when=O('alf'))
add(f'<path d="{LD}" style="fill:var(--bad);fill-opacity:.08;stroke:none"/>', when=O('aih', 'dili'))
text('liver', 430, 292, 'dyn-big', 'middle')
text('right lobe', 430, 312, 'nf-l2', 'middle'); text('left lobe', 1010, 296, 'nf-l2', 'middle')
text('small, shrunken liver — massive necrosis', 200, 690, TAG, when=O('alf'))

# secondary biliary cirrhosis: septa around irregular nodules
NOD = [(325, 412, 40), (390, 440, 40), (330, 520, 50), (440, 560, 42), (520, 470, 38), (380, 610, 34),
       (640, 400, 44), (720, 330, 40), (620, 300, 34), (830, 300, 36), (900, 380, 30), (1040, 330, 30), (520, 360, 36)]
add('<g>' + ''.join(f'<path d="M{x - r} {y} C{x - r} {y - r * .8} {x - r * .2} {y - r} {x + r * .3} {y - r * .9} C{x + r} {y - r * .6} {x + r * 1.05} {y + r * .3} '
                    f'{x + r * .5} {y + r * .8} C{x} {y + r * 1.1} {x - r * .9} {y + r * .7} {x - r} {y} Z" '
                    f'style="fill:var(--dk6);fill-opacity:.12;stroke:var(--dk8);stroke-width:7;stroke-opacity:.55"/>' for x, y, r in NOD) + '</g>',
    when=O('sbc'))
text('septa around irregular “jigsaw” nodules', 200, 690, TAG, when=O('sbc'))

HUB, JN, AMP = (770, 503), (780, 715), (722, 1170)
# intrahepatic branches: (tip, mid, joins at) — the tips carry the small interlobular ducts
BR = [((330, 330), (450, 390), (560, 430)), ((300, 480), (450, 455), (560, 430)), ((430, 590), (580, 525), HUB),
      ((1090, 320), (960, 380), HUB), ((880, 300), (960, 380), HUB)]
DUP = dict(when=OBST, d=7)
duct = lambda d, w: dict(tube=d, w=w, color='--dk10', mods=[DUP, dict(when=O('psc'), d=-3)])
for tip, mid, j in BR:
    shapes.append(duct(f'M{tip[0]} {tip[1]} L{mid[0]} {mid[1]} L{j[0]} {j[1]}', 5))
shapes.append(duct(f'M560 430 L{HUB[0]} {HUB[1]}', 8))
CHD = f'M{HUB[0]} {HUB[1]} L{JN[0]} {JN[1]}'
CBDP = ((780, 715), (792, 860), (782, 1010), (750, 1110))
CBD = f'M{JN[0]} {JN[1]} C792 860 782 1010 750 1110 L{AMP[0]} {AMP[1]}'
shapes += [duct(CHD, 10), duct(CBD, 11), dict(tube='M780 715 C752 660 700 575 650 585', w=7, color='--dk10')]
# the twigs at each tip: small interlobular ducts (lost in PBC)
TW = []
for tip, mid, j in BR:
    ang = math.atan2(tip[1] - mid[1], tip[0] - mid[0])
    for da in (-0.65, 0, 0.65):
        TW.append((tip, (round(tip[0] + 42 * math.cos(ang + da)), round(tip[1] + 42 * math.sin(ang + da)))))
add('<g>' + ''.join(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" style="stroke:var(--dk10);stroke-width:5;stroke-linecap:round"/>' for a, b in TW) + '</g>',
    unless=O('pbc'))
add('<g>' + ''.join(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" style="stroke:var(--dk10);stroke-width:3;stroke-dasharray:3 6;opacity:.5"/>' for a, b in TW)
    + ''.join(X(b[0], b[1], 8) for a, b in TW[::2]) + '</g>', when=O('pbc'))
text('interlobular ducts: the twigs at the tips', 200, 690, 'nf-l2', unless=O('pbc', 'sbc', 'alf'))
text('PBC: the small ducts vanish (ductopenia)', 200, 690, TAG, when=O('pbc'))
text('large ducts stay normal', 200, 708, 'nf-l2', when=O('pbc'))
# PSC: beading of the large intrahepatic and extrahepatic ducts — dilations between strictures
BEAD = [bez(*CBDP, t / 10) for t in range(1, 10, 2)] + [(775, 560), (778, 650), (640, 458), (700, 479), (880, 432), (930, 399)]
add('<g>' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="15" style="fill:var(--dk10);fill-opacity:.55;stroke:var(--dk10);stroke-width:3"/>' for x, y in BEAD)
    + ''.join(f'<path d="M{x - 14} {y} h28" style="stroke:var(--dk8);stroke-width:7;stroke-linecap:round"/>' for x, y in [bez(*CBDP, t / 10) for t in range(2, 10, 2)] + [(776, 605), (779, 690)])
    + '</g>', when=O('psc'))
text('beading: strictures between dilations', 812, 905, TAG, when=O('psc'))
text('large intrahepatic + extrahepatic ducts', 812, 923, 'nf-l2', when=O('psc'))
# ducts and organs labels
text('hepatic ducts → common hepatic duct', 804, 560, 'nf-l2')
text('cystic duct', 690, 628, 'nf-l2', 'end')
text('common bile duct', 812, 800, 'nf-l2')

GB = 'M640 580 C680 585 690 630 680 670 L668 810 C664 870 630 895 600 890 C560 885 540 850 545 810 L575 650 C585 610 605 578 640 580 Z'
add(f'<path d="{GB}" style="fill:var(--dk10);fill-opacity:.14;stroke:var(--dk10);stroke-width:5"/>')
text('gallbladder', 530, 780, 'nf-l1', 'end')

DUO = 'M1060 960 C900 960 720 950 700 1030 L692 1290 C690 1370 760 1382 900 1382 L1120 1382'
shapes.append(dict(tube=DUO, w=34, color='--dk8'))
PANC = ('M760 1070 C800 1040 900 1050 960 1070 C1040 1060 1120 1040 1170 1042 C1200 1050 1200 1092 1168 1102 '
        'C1100 1118 1040 1132 1000 1150 C990 1210 980 1290 900 1310 C820 1320 760 1290 750 1210 Z')
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3.5"/>')
add(f'<rect x="{AMP[0] - 6}" y="{AMP[1] - 16}" width="14" height="32" rx="5" style="fill:var(--dk7)"/>')
text('pancreas (head)', 1000, 1230, 'nf-l2', 'middle')
text('duodenum', 655, 1080, 'nf-l1', 'end')
text('ampulla', 655, 1176, 'nf-l2', 'end')

# large duct obstruction: a stone low in the common bile duct; the tree above it dilates
STONE = bez(*CBDP, .5)
add(f'<circle cx="{STONE[0]}" cy="{STONE[1]}" r="17" style="fill:var(--surface);stroke:var(--dk10);stroke-width:5"/>', when=OBST)
text('stone — or a pancreatic-head or bile-duct tumour, a stricture', 812, 870, TAG, when=O('obst'))
text('ducts above it dilate · bile backs up', 812, 888, 'nf-l2', when=O('obst'))
text('obstruction never relieved — infants: biliary atresia', 812, 870, TAG, when=O('sbc'))
text('pressure in the intrahepatic ducts → fibrosis', 812, 888, 'nf-l2', when=O('sbc'))

# drug-induced injury: a pill, carried to the liver in portal blood
add('<g><rect x="1070" y="760" width="76" height="34" rx="17" style="fill:var(--dk4);fill-opacity:.35;stroke:var(--dk4);stroke-width:3"/>'
    '<path d="M1108 760 V794" style="stroke:var(--dk4);stroke-width:3"/>'
    '<path d="M1080 752 C1060 700 1040 660 1010 620" class="dyn-line" marker-end="url(#ah-ilInj)"/></g>', when=O('dili'))
text('a drug', 1108, 820, 'nf-l1', 'middle', when=O('dili'))
text('hits only a few people', 1108, 838, 'nf-l2', 'middle', when=O('dili'))
# sepsis: gram-negative bacteria in the blood
add('<g>' + ''.join(f'<rect x="{x}" y="{y}" width="20" height="9" rx="4.5" style="fill:var(--dk4);opacity:.75"/>'
                    for x, y in ((1050, 760), (1084, 790), (1040, 812), (1100, 744), (1070, 836))) + '</g>', when=O('sep'))
text('circulating microbial products', 1080, 870, 'nf-l1', 'middle', when=O('sep'))
text('often gram-negative sepsis', 1080, 888, 'nf-l2', 'middle', when=O('sep'))

# the magnified twig: box on the left lobe's tip, leaders to the enlargement
add('<rect x="1052" y="282" width="80" height="72" rx="8" style="fill:none;stroke:var(--accent);stroke-width:3"/>')
add('<path d="M1132 282 L1300 210 M1132 354 L1300 1040" style="fill:none;stroke:var(--accent);stroke-width:1.5;stroke-dasharray:5 6;opacity:.7"/>')

# ════════ one portal tract, magnified ════════
ZX0, ZY0, ZX1, ZY1 = 1300, 200, 2330, 1050
add(f'<rect x="{ZX0}" y="{ZY0}" width="{ZX1 - ZX0}" height="{ZY1 - ZY0}" rx="24" class="dyn-soft"/>')
text('one small portal tract, magnified', ZX0 + 30, 236, 'nf-l1')
text('portal vein · hepatic artery · interlobular bile duct, ringed by hepatocytes', ZX0 + 30, 254, 'nf-l2')
PX, PY, PRX, PRY = 1800, 640, 280, 200
CELLS = []
for r, y in enumerate(range(320, 921, 60)):
    for c, x in enumerate(range(1325, 2206, 80)):
        q = ((x + 35 - PX) / (PRX + 40)) ** 2 + ((y + 25 - PY) / (PRY + 35)) ** 2
        if q > 1: CELLS.append((x, y, q))
add('<g>' + ''.join(f'<rect x="{x}" y="{y}" width="70" height="50" rx="12" class="dyn-cell"/><circle cx="{x + 35}" cy="{y + 25}" r="8" style="fill:var(--dk6);fill-opacity:.25"/>'
                    for x, y, q in CELLS) + '</g>')
# the portal tract stroma
add(f'<ellipse cx="{PX}" cy="{PY}" rx="{PRX}" ry="{PRY}" style="fill:var(--dk8);fill-opacity:.1;stroke:var(--dk8);stroke-width:3;stroke-opacity:.6"/>')
PV, HA, BD = (1690, 640), (1790, 770), (1920, 590)
add(f'<ellipse cx="{PV[0]}" cy="{PV[1]}" rx="78" ry="60" style="fill:var(--dk9);fill-opacity:.3;stroke:var(--dk9);stroke-width:4"/>')
add(f'<circle cx="{HA[0]}" cy="{HA[1]}" r="20" style="fill:var(--nf-blood);fill-opacity:.35;stroke:var(--nf-blood);stroke-width:7"/>')
text('portal vein', PV[0], PV[1] + 5, 'nf-l1', 'middle')
text('hepatic artery', HA[0] + 34, HA[1] + 5, 'nf-l2')
text('portal tract', PX, PY - PRY + 34, 'nf-l1', 'middle')
text('limiting plate (hepatocytes)', 2240, PY + 4, 'nf-l2', 'end')
# the interlobular bile duct: cuboidal cholangiocytes around a lumen
def ductring(cx, cy, rr, lum, n=10, broken=()):
    s = f'<circle cx="{cx}" cy="{cy}" r="{lum}" style="fill:var(--dk10);fill-opacity:.25"/>'
    for i in range(n):
        if i in broken: continue
        a = 2 * math.pi * i / n
        s += f'<circle cx="{cx + rr * math.cos(a):.0f}" cy="{cy + rr * math.sin(a):.0f}" r="{rr * .33:.0f}" style="fill:var(--dk10);fill-opacity:.35;stroke:var(--dk10);stroke-width:2.5"/>'
    return s
add(ductring(*BD, 40, 24), unless=O('pbc', 'psc', 'obst', 'sbc'))
add(ductring(*BD, 50, 34, 12), when=OBST)                        # dilated above an obstruction
text('interlobular bile duct', BD[0], BD[1] + 72, 'nf-l1', 'middle', unless=O('pbc', 'psc'))
# a canal of Hering fed by a canaliculus, joining the duct
CAN = 'M2270 435 H2140'
HER = f'M2140 435 L2040 530 L{BD[0] + 30} {BD[1] - 20}'
add(f'<path d="{CAN}" style="fill:none;stroke:var(--dk10);stroke-width:4;stroke-dasharray:6 5"/>')
add(f'<path d="{HER}" style="fill:none;stroke:var(--dk10);stroke-width:9;stroke-linecap:round;stroke-opacity:.6"/>', unless=O('sep'))
text('canaliculus', 2270, 414, 'nf-l2', 'end')
text('canal of Hering', 2150, 500, 'nf-l2')

# AIH: lymphocytes and plasma cells spill across the limiting plate; hepatocytes die at the interface; a rosette
def lym(x, y): return f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--dk11);opacity:.8"/>'
def plas(x, y): return (f'<ellipse cx="{x}" cy="{y}" rx="12" ry="8.5" style="fill:var(--dk11);fill-opacity:.3;stroke:var(--dk11);stroke-width:2"/>'
                        f'<circle cx="{x + 5}" cy="{y}" r="4.5" style="fill:var(--dk11)"/>')
INFL = [(1560, 560), (1590, 700), (1620, 790), (1700, 820), (1600, 520), (1550, 640), (1650, 480), (1840, 820), (1880, 760), (1520, 760)]
SPILL = [(1460, 600), (1450, 700), (1470, 820), (1500, 880), (1440, 500), (1520, 470)]
add('<g>' + ''.join(plas(x, y) if i % 2 else lym(x, y) for i, (x, y) in enumerate(INFL + SPILL)) + '</g>', when=O('aih'))
EDGE = [(x, y) for x, y, q in CELLS if q < 1.55 and x + 35 < PX - 120]
add('<g>' + ''.join(f'<rect x="{x}" y="{y}" width="70" height="50" rx="12" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:2.5"/>' for x, y in EDGE[::2]) + '</g>',
    when=O('aih'))
add('<g>' + ''.join(f'<circle cx="{1400 + 22 * math.cos(2 * math.pi * i / 6):.0f}" cy="{980 + 22 * math.sin(2 * math.pi * i / 6):.0f}" r="10" style="fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:2"/>' for i in range(6))
    + '<circle cx="1400" cy="980" r="5" style="fill:var(--dk10)"/></g>', when=O('aih'))
text('interface hepatitis', 1330, 282, TAG, when=O('aih'))
text('plasma cells + T cells cross the limiting plate', 1330, 300, 'nf-l2', when=O('aih'))
text('rosette', 1432, 985, 'nf-l2', when=O('aih'))

# PBC: a granuloma centred on the duct — the florid duct lesion — and a broken duct
add('<g>' + ''.join(f'<ellipse cx="{BD[0] + 78 * math.cos(2 * math.pi * i / 12):.0f}" cy="{BD[1] + 64 * math.sin(2 * math.pi * i / 12):.0f}" rx="18" ry="11" '
                    f'transform="rotate({360 * i / 12 + 90:.0f} {BD[0] + 78 * math.cos(2 * math.pi * i / 12):.0f} {BD[1] + 64 * math.sin(2 * math.pi * i / 12):.0f})" '
                    f'style="fill:var(--dk7);fill-opacity:.35;stroke:var(--dk7);stroke-width:2"/>' for i in range(12))
    + ''.join(lym(BD[0] + round(112 * math.cos(a)), BD[1] + round(94 * math.sin(a))) for a in (0.3, 1.1, 1.9, 2.7, 3.5, 4.3, 5.1, 5.8))
    + ductring(*BD, 40, 14, broken=(1, 2, 5, 7)) + X(BD[0] + 26, BD[1] + 26, 9) + '</g>', when=O('pbc'))
text('florid duct lesion', BD[0], BD[1] + 120, TAG, 'middle', when=O('pbc'))
text('granuloma + lymphocytes destroy the duct', BD[0], BD[1] + 138, 'nf-l2', 'middle', when=O('pbc'))
# PSC: concentric onion-skin fibrosis around an atrophic duct
add('<g>' + ''.join(f'<circle cx="{BD[0]}" cy="{BD[1]}" r="{r}" style="fill:none;stroke:var(--dk8);stroke-width:6;stroke-opacity:{.75 - (r - 34) / 160:.2f}"/>' for r in range(34, 110, 15))
    + ductring(*BD, 22, 8, n=7) + '</g>', when=O('psc'))
text('onion-skin fibrosis', BD[0], BD[1] + 128, TAG, 'middle', when=O('psc'))
text('a larger duct, trapped in a concentric scar', BD[0], BD[1] + 146, 'nf-l2', 'middle', when=O('psc'))
# obstruction: portal edema, ductular reaction with neutrophils at the interface, bile plugs in canaliculi
add('<g>' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="20" ry="11" style="fill:var(--nf-h2o);fill-opacity:.25"/>' for x, y in ((1600, 540), (1640, 760), (1880, 720), (1980, 680), (1760, 520)))
    + ''.join(f'<circle cx="{x}" cy="{y}" r="11" style="fill:none;stroke:var(--dk10);stroke-width:4"/>' for x, y in ((2050, 560), (2070, 730), (1560, 700)))
    + ''.join(f'<circle cx="{x}" cy="{y}" r="5" style="fill:var(--dk4)"/>' for x, y in ((2030, 590), (2090, 700), (1580, 730), (2060, 520)))
    + ''.join(f'<circle cx="{x}" cy="{y}" r="6" style="fill:var(--dk10)"/>' for x, y in ((1400, 435), (1560, 375), (2200, 525), (2120, 885), (1480, 945))) + '</g>',
    when=OBST)
text('dilated duct · portal edema · ductular reaction, neutrophils', 1330, 282, TAG, when=O('obst'))
text('bile plugs in the canaliculi', 1330, 300, 'nf-l2', when=O('obst'))
# secondary biliary cirrhosis: fibrous septa run out from the portal tract
add('<g>' + ''.join(f'<path d="{d}" style="fill:none;stroke:var(--dk8);stroke-width:22;stroke-opacity:.45;stroke-linecap:round"/>'
                    for d in ('M2075 600 C2160 560 2230 470 2290 420', 'M1525 660 C1440 700 1380 760 1330 800', 'M1800 840 C1820 900 1860 960 1900 1010',
                              'M1700 445 C1660 380 1600 330 1560 290')) + '</g>', when=O('sbc'))
text('fibrous septa link the portal tracts', 1330, 282, TAG, when=O('sbc'))
# sepsis: dark bile plugs in a dilated canal of Hering and ductules at the interface
add(f'<path d="{HER}" style="fill:none;stroke:var(--dk10);stroke-width:22;stroke-linecap:round;stroke-opacity:.45"/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="9" class="dyn-lost"/>' for x, y in ((2120, 457), (2085, 495), (2050, 520), (2010, 545), (1980, 560)))
    + ''.join(f'<path d="M{x} {y} l-30 30" style="stroke:var(--dk10);stroke-width:16;stroke-linecap:round;stroke-opacity:.45"/><circle cx="{x - 15}" cy="{y + 15}" r="7" class="dyn-lost"/>'
              for x, y in ((1560, 470), (1570, 820))), when=O('sep'))
text('ductular cholestasis: bile plugs in canals of Hering', 1330, 282, TAG, when=O('sep'))
text('little inflammation · hepatocytes mostly intact', 1330, 300, 'nf-l2', when=O('sep'))
# drug-induced injury: scattered injured hepatocytes
HURT = CELLS[3::7]
add('<g>' + ''.join(f'<rect x="{x}" y="{y}" width="70" height="50" rx="12" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:2.5"/>' for x, y, q in HURT) + '</g>',
    when=O('dili'))
text('injured hepatocytes — pattern depends on the drug', 1330, 282, TAG, when=O('dili'))
text('hepatitis-like (ALT) or cholestatic (ALP)', 1330, 300, 'nf-l2', when=O('dili'))
# acute liver failure: broad loss, islands of survivors
ISL = {(x, y) for x, y, q in CELLS if (1400 < x < 1560 and 850 < y < 960) or (2050 < x < 2210 and 280 < y < 420)}
add('<g>' + ''.join(f'<rect x="{x - 2}" y="{y - 2}" width="74" height="54" rx="12" style="fill:var(--surface-2);opacity:.85"/>'
                    f'<path d="M{x + 14} {y + 12} l42 26" style="stroke:var(--bad);stroke-width:2;opacity:.5"/>' for x, y, q in CELLS if (x, y) not in ISL) + '</g>',
    when=O('alf'))
text('massive necrosis — islands of surviving cells', 1330, 282, TAG, when=O('alf'))
# ursodiol / obeticholic acid at the hepatocyte
text('hydrophilic ursodiol replaces toxic bile acids', 1330, 282, TAG, when=O('urso'))
text('stabilizes canalicular membranes · ↓ biliary cholesterol', 1330, 300, 'nf-l2', when=O('urso'))
text('FXR agonist → ↓ bile acid synthesis', 1330, 282, TAG, when=O('oca'))
text('protects hepatocytes and cholangiocytes', 1330, 300, 'nf-l2', when=O('oca'))
add('<g><rect x="2205" y="500" width="70" height="50" rx="12" class="dyn-hl"/></g>', when=O('urso', 'oca'))
text('this hepatocyte', 2200, 570, 'nf-l2', 'end', when=O('urso', 'oca'))

# ════════ the bile's path as one strip ════════
SY = 1180
text('Along the bile’s path — lit where the chosen one does its damage', ZX0, SY - 56, 'nf-l1')
SEG = [(1310, 1460, 14, 'hepatocytes', 'canaliculi', O('aih', 'dili', 'alf', 'urso', 'oca')),
       (1470, 1630, 18, 'canals of Hering', 'ductules', O('sep')),
       (1640, 1810, 24, 'small interlobular', 'ducts', O('pbc')),
       (1820, 1990, 32, 'large intrahepatic', 'ducts', O('psc')),
       (2000, 2170, 40, 'extrahepatic', 'ducts · CBD', O('psc', 'obst', 'sbc')),
       (2180, 2320, 44, 'ampulla', 'duodenum', None)]
for a, b, h, l1, l2, hit in SEG:
    add(f'<rect x="{a}" y="{SY - h / 2:.0f}" width="{b - a}" height="{h}" rx="{h / 2:.0f}" style="fill:var(--dk10);fill-opacity:.18;stroke:var(--dk10);stroke-width:2.5"/>')
    text(l1, (a + b) // 2, SY + 50, 'nf-l2', 'middle'); text(l2, (a + b) // 2, SY + 66, 'nf-l2', 'middle')
    if hit:
        add(f'<rect x="{a - 6}" y="{SY - h / 2 - 8:.0f}" width="{b - a + 12}" height="{h + 16}" rx="{h / 2 + 8:.0f}" class="dyn-hl"/>', when=hit)
add(f'<path d="M2000 {SY + 4} V{SY + 28}" class="nf-x" style="stroke-width:6"/>' + X(2000, SY, 14), when=OBST)
text('the blockage', 2000, SY + 92, 'nf-l1 dyn-tag', 'middle', when=OBST)
text('whole tree behind it', 2000, SY + 110, 'nf-l2', 'middle', when=O('sbc'))
text('protects', 1385, SY + 92, 'nf-l1 dyn-tag', 'middle', when=O('urso', 'oca'))
text('hepatocytes and ducts', 1385, SY + 110, 'nf-l2', 'middle', when=O('urso', 'oca'))
text('the whole liver', 1385, SY + 92, 'nf-l1 dyn-tag', 'middle', when=O('alf'))
text('the interface', 1385, SY + 92, 'nf-l1 dyn-tag', 'middle', when=O('aih'))

TAGS = dict(aih='Autoimmune hepatitis — T cells kill hepatocytes at the portal interface',
            pbc='PBC — the small interlobular ducts are destroyed',
            psc='PSC — the large ducts scar, narrow and bead',
            obst='Large bile duct obstruction — the common duct is blocked',
            sbc='Secondary biliary cirrhosis — long obstruction scars the whole liver',
            sep='Cholestasis of sepsis — bile stalls in the ductules',
            dili='Idiosyncratic drug-induced liver injury — a few unlucky people',
            alf='Acute liver failure — encephalopathy + coagulopathy within 26 weeks',
            urso='Ursodiol — first-line for PBC; also prevents gallstones',
            oca='Obeticholic acid — added when ursodiol is not enough')
for k, s in TAGS.items(): text(s, 160, 150, 'nf-l1 dyn-tag', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FEW = m(O('pbc'), add=dict(bile=-1))
URSO = m(O('urso'), set=dict(bile=0), add=dict(urso=2))
SLOW = m(O('psc', 'sep', 'alf'), speed=.45)
flows = []
for tip, mid, j in BR:
    d = f'M{tip[0]} {tip[1]} L{mid[0]} {mid[1]} L{j[0]} {j[1]}' + ('' if j == HUB else f' L{HUB[0]} {HUB[1]}')
    flows.append(dict(d=d, len=plen(d), speed=60, r=5, base=dict(bile=2), mods=[FEW, URSO, SLOW, m(O('alf'), add=dict(bile=-1)), m(O('oca'), add=dict(bile=-1))]))
MAIN = f'{CHD} C792 860 782 1010 750 1110 L{AMP[0]} {AMP[1]}'
UPTO = f'{CHD} C789 820 790 900 {STONE[0]} {STONE[1] - 20}'
OUT = 'M705 1185 L695 1290 C693 1370 760 1380 900 1380 L1110 1380'
flows += [
  dict(d=MAIN, len=plen(MAIN), speed=70, r=6, base=dict(bile=4), unless=OBST, mods=[URSO, SLOW, m(O('urso'), add=dict(urso=1))]),
  dict(d=UPTO, len=plen(UPTO), speed=22, r=6, base=dict(bile=6), when=OBST),
  dict(d=OUT, len=plen(OUT), speed=70, r=6, base=dict(bile=3), unless=OBST, mods=[URSO, SLOW]),
  # magnified: canaliculus → canal of Hering → duct
  dict(d=CAN + ' ' + HER.replace('M2140 435 ', 'L'), len=plen(CAN + ' ' + HER.replace('M2140 435 ', 'L')), speed=55, r=5, base=dict(bile=3),
       unless=O('sep', 'alf'), mods=[URSO]),
  # portal blood out into the sinusoids
  dict(d='M1612 615 C1560 605 1480 615 1330 615', len=290, speed=90, r=6, base=dict(bl=3), unless=O('alf')),
  dict(d='M1640 700 L1330 735', len=312, speed=90, r=6, base=dict(bl=3), unless=O('alf')),
  # the strip: bile from hepatocyte to duodenum
  dict(d=f'M1320 {SY} H2310', len=990, speed=110, r=5, base=dict(bile=6), unless=OBST, mods=[URSO, SLOW]),
  dict(d=f'M1320 {SY} H1985', len=665, speed=40, r=5, base=dict(bile=5), when=OBST),
  # AIH: T cells and plasma cells cross the limiting plate
  dict(d='M1700 760 C1640 800 1560 830 1460 860', len=260, speed=40, r=6, base=dict(tc=3), when=O('aih')),
  dict(d='M1640 520 C1580 500 1520 480 1440 470', len=210, speed=40, r=6, base=dict(tc=3), when=O('aih')),
  # PBC: T cells home to the duct
  dict(d=f'M1700 470 C1780 470 {BD[0] - 60} {BD[1] - 80} {BD[0] - 30} {BD[1] - 30}', len=260, speed=40, r=6, base=dict(tc=3), when=O('pbc')),
]
sites = [
  dict(x=2200, y=430, n=[0, 1], w=8, t='ex', l='', aria='Hepatocyte secretes bile acids into the canaliculus', c='bileacid',
       ions=[['bile', 'out', 1]], cross=True, reach=14, unless=O('urso', 'alf'), low=O('oca')),
  dict(x=2200, y=430, n=[0, 1], w=8, t='ex', l='', aria='Hepatocyte secretes ursodiol into the canaliculus', c='bileacid',
       ions=[['urso', 'out', 2]], cross=True, reach=14, when=O('urso')),
  dict(x=2240, y=525, n=[1, 0], w=8, t='rec', l='', aria='FXR in the hepatocyte — obeticholic acid binds it', c='bileacid', ions=[], when=O('oca')),
  dict(x=BD[0], y=BD[1] - 40, n=[0, -1], w=8, t='rec', l='', aria='Interlobular bile duct — the target in PBC', c='pbc', ions=[]),
  dict(x=PX - PRX, y=PY, n=[-1, 0], w=8, t='rec', l='', aria='Limiting plate — interface hepatitis in autoimmune hepatitis', c='aih', ions=[]),
  dict(x=HUB[0], y=HUB[1] + 60, n=[1, 0], w=10, t='rec', l='', aria='Large bile ducts — beaded in PSC', c='psc', ions=[]),
  dict(x=STONE[0] + 24, y=STONE[1], n=[1, 0], w=10, t='rec', l='', aria='Common bile duct stone', c='gallstones', ions=[], when=OBST),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='ALP · GGT', mods=[R(O('pbc', 'psc', 'obst', 'sbc'), 1)]),
  dict(l='ALT · AST', mods=[R(O('aih', 'alf'), 1)]),
  dict(l='Antimitochondrial antibody', mods=[R(O('pbc'), 1), R(O('psc'), 0)]),
  dict(l='Anti-smooth muscle or anti-LKM1', mods=[R(O('aih'), 1)]),
  dict(l='p-ANCA', mods=[R(O('psc'), 1)]),
  dict(l='IgM', mods=[R(O('pbc', 'psc'), 1)]),
  dict(l='Prothrombin time', mods=[R(O('alf'), 1)]),
]

notes = {
  '': 'Autoimmune and look-alike liver diseases, each placed where it strikes: hepatocytes at the portal interface (autoimmune '
      'hepatitis), small interlobular ducts (PBC), large ducts (PSC) or the common bile duct (obstruction). Pick one to see its '
      'lesion. ↑ raised or positive · ↔ negative · – not stated.',
  'a:aih': 'Autoimmune hepatitis · AIH: CD4 helper T cells drive B cells to make autoantibodies while CD8 cytotoxic T cells kill '
           'hepatocytes at the interface — interface hepatitis with plasma cells, emperipolesis and rosettes; ↑ ALT, AST and IgG. '
           'Type 1: ANA + anti-smooth muscle actin; type 2 (children, teens): anti-LKM1 (against CYP2D6) and/or anti-LC1. '
           'About 78% female, HLA-DR3 in Europeans; minocycline and nitrofurantoin are triggers.',
  'a:pbc': 'PBC · primary biliary cholangitis: T cells destroy the small and medium intrahepatic interlobular bile ducts — the '
           'florid duct lesion, a granuloma on the duct — then the ducts vanish (ductopenia); large ducts are spared. '
           'Antimitochondrial antibody in 95% (against PDC-E2 of pyruvate dehydrogenase), ↑ ALP and IgM. About 90% women aged '
           '40–50 with fatigue and intense itching; Sjögren syndrome in 70%.',
  'a:psc': 'PSC · primary sclerosing cholangitis: inflammation and onion-skin fibrosis of the large intrahepatic and extrahepatic '
           'ducts leave strictures between dilations — beading on MRCP or ERCP. p-ANCA in about 65%, AMA negative, ↑ ALP and IgM; '
           'about 70% male and about 70% have ulcerative colitis. Lifetime cholangiocarcinoma risk about 20%.',
  'a:obst': 'Large bile duct obstruction: a common duct stone, a pancreatic-head or bile-duct cancer, a stricture or PSC (in '
            'children biliary atresia, a choledochal cyst, cystic fibrosis); the ducts above it dilate. Jaundice, itching, dark '
            'urine and pale stools with ↑ ALP, GGT and conjugated bilirubin; stagnant bile invites ascending cholangitis.',
  'a:sbc': 'Secondary biliary cirrhosis: obstruction left in place raises pressure in the intrahepatic ducts, and periductal '
           'fibrosis builds septa until cirrhosis — irregular “jigsaw” nodules. Uncorrected extrahepatic biliary atresia reaches '
           'it by 3 to 6 months of age; in adults, gallstones, strictures or pancreatic carcinoma.',
  'a:sep': 'Cholestasis of sepsis: circulating microbial products — most often in gram-negative sepsis — cause ductular '
           '(cholangiolar) cholestasis, with dark bile plugs in dilated canals of Hering and ductules at the portal–parenchymal '
           'interface. Inflammation and hepatocyte injury stay mild.',
  'a:dili': 'Idiosyncratic hepatotoxicity · drug-induced liver injury: unpredictable, not dose dependent, in a small minority '
            'after weeks to months, through variant CYP enzymes, transporters or HLA alleles. It can mimic hepatitis (isoniazid, '
            'nitrofurantoin, methyldopa: ALT ≥ 5× normal) or cholestasis (amoxicillin-clavulanate, statins: ALP ≥ 2×); '
            'acetaminophen is the direct, dose-dependent kind.',
  'a:alf': 'Acute liver failure: encephalopathy and coagulopathy within 26 weeks of the first injury, with no prior liver '
           'disease — usually massive necrosis and a small, shrunken liver. Aminotransferases rise steeply, the prothrombin time '
           'lengthens as clotting factors stop being made, and ammonia brings asterixis and coma. Acetaminophen causes almost half '
           'of US adult cases.',
  'a:urso': 'Ursodiol, a hydrophilic bile acid, is first-line for early PBC: it replaces toxic hydrophobic bile acids, stabilizes '
            'canalicular membranes and lowers biliary cholesterol, slowing progression and delaying transplant. It also prevents '
            'gallstones during rapid weight loss and, unlike chenodeoxycholate, is not hepatotoxic.',
  'a:oca': 'Obeticholic acid, a synthetic chenodeoxycholate derivative, is an FXR agonist that turns down hepatic bile acid '
           'synthesis. It is added to ursodiol (5–10 mg/day) when PBC responds inadequately to ursodiol alone, or used alone if '
           'ursodiol is not tolerated. Dose-dependent itching in up to 25%.',
}

dyn = dict(
  kinds=dict(bile=['bile', '--dk10'], urso=['urso', '--dk3'], tc=['tc', '--dk11'], bl=['bl', '--nf-blood']),
  groups=[['bile', 'Bile'], ['urso', 'Ursodiol'], ['tc', 'T cells'], ['bl', 'Portal blood']],
  switches=[dict(id=SW, label='Pick a disease or a drug', type='one', options=[
      ['aih', 'Autoimmune hepatitis · AIH', 'aih'], ['pbc', 'PBC · primary biliary cholangitis', 'pbc'],
      ['psc', 'PSC · primary sclerosing cholangitis', 'psc'],
      ['obst', 'Large bile duct obstruction', 'lfts'], ['sbc', 'Secondary biliary cirrhosis', 'cirrhosis'],
      ['sep', 'Cholestasis of sepsis', 'sepsistnf'],
      ['dili', 'Idiosyncratic hepatotoxicity · drug-induced liver injury', 'adrgi'], ['alf', 'Acute liver failure', 'alf'],
      ['urso', 'Ursodiol', 'pbc'], ['oca', 'Obeticholic acid', 'pbc']],
      sections=[['Autoimmune', ['aih', 'pbc', 'psc']], ['Other cholestasis', ['obst', 'sbc', 'sep']],
                ['Injury', ['dili', 'alf']], ['Treating PBC', ['urso', 'oca']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Course GI lecture notes (SDL 11, 15, 16, 20) · Robbins ch 18 · Katzung ch 62 · First Aid pp. 397, 399, 402')

MAP = dict(
  id='immlivsim', title='Autoimmune Liver Disease — AIH, Primary Biliary & Sclerosing Cholangitis', topic='gi', after='liver',
  sub='The liver’s bile-duct tree and one portal tract magnified: autoimmune hepatitis at the interface, PBC destroying the '
      'small ducts, PSC beading the large ones, a blocked common duct and the cirrhosis it leaves, cholestasis of sepsis, '
      'drug injury and acute liver failure — with antibodies, ALP, ALT, IgM and PT read out, and ursodiol and obeticholic acid '
      'for PBC. Tap a pin for its card',
  w=3500, h=1760,
  fa='397, 399, 402',
  src=[RB18, KZ62],
  lanes=[('ilAuto', 'Autoimmune', 'glycolysis'), ('ilChol', 'Cholestasis', 'gluconeo'), ('ilInj', 'Injury & drugs', 'tca')],
  nodes=[
    ('il1', 'Autoimmune hepatitis', 300, 1580, 'ilAuto', 'interface · ASMA · anti-LKM1', ['aih', 'cyp2d6'], 'hub'),
    ('il2', 'Primary biliary', 740, 1580, 'ilAuto', 'AMA · florid duct lesion', ['pbc']),
    ('il3', 'Primary sclerosing', 1180, 1580, 'ilAuto', 'p-ANCA · beading · UC', ['psc', 'crohn', 'cholangio']),
    ('il4', 'Liver enzymes', 1620, 1580, 'ilChol', 'ALP · GGT vs ALT · AST', ['lfts']),
    ('il5', 'Common duct obstruction', 2060, 1580, 'ilChol', 'stones · cholangitis', ['gallstones', 'cholangitis']),
    ('il6', 'Biliary cirrhosis', 300, 1670, 'ilChol', 'secondary · biliary atresia', ['cirrhosis', 'biliaryatresia']),
    ('il7', 'Cholestasis of sepsis', 740, 1670, 'ilChol', 'gram-negative sepsis', ['sepsistnf']),
    ('il8', 'Drug-induced injury', 1180, 1670, 'ilInj', 'idiosyncratic vs direct', ['adrgi', 'acetaminophen']),
    ('il9', 'Acute liver failure', 1620, 1670, 'ilInj', 'encephalopathy · coagulopathy', ['alf', 'hepenceph']),
    ('il10', 'Bile acid drugs', 2060, 1670, 'ilInj', 'ursodiol · obeticholic acid', ['bileacid']),
  ],
  panels=[
    (2420, 900, 1000, 'Antibodies and patients (course SDL 15–16 · Robbins ch 18 · First Aid pp. 399, 402)', [
      ('AIH type 1', 'ANA + anti-smooth muscle actin · ± anti-SLA/LPA · ↑ IgG · all ages'),
      ('AIH type 2', 'anti-LKM1 (against CYP2D6) and/or anti-LC1 · children and teens'),
      ('PBC', 'AMA 95% (PDC-E2) · ANA 40–50% · ↑ IgM · 90% female, 40–50 years'),
      ('PSC', 'p-ANCA ~65% · AMA negative · ↑ IgM · 70% male · UC in ~70%'),
      ('Treatment', 'AIH: prednisone ± azathioprine · PBC: ursodiol, then add obeticholic acid')]),
  ],
  dyn=dyn,
)
