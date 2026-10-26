# m58 — Pancreatic Acinus & Islet in Motion (dynamic map, kit data)
# Top left: the pancreas from the front — head in the duodenal C-loop, body, tail — with islets dotted through it, thickest
# in the tail. Bottom left: one acinus (pyramidal acinar cells, apical zymogen granules, pale centroacinar cells in the
# middle) → intercalated duct → intralobular/interlobular duct, and one duct cell magnified (apical Cl⁻–HCO₃⁻ exchanger and
# CFTR, basal secretin receptor). Right: one islet of Langerhans — β cells in the core, α and δ cells mainly at the rim, PP
# cells in the islet and out among the acini, one ε cell — threaded by fenestrated capillaries whose efferent vessels run on
# to the acini. One `one` switch "Pick a cell" in two sections (exocrine, endocrine); seven readouts. pbsecsim covers juice
# composition by phase and flow rate and the bile; pancreas/betaflow cover insulin's actions and diabetes; this map is the
# cell-by-cell histology and what each cell secretes.
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   GI Exam 1 lecture notes (corpus/gastro/course_exam1_lecture_notes.txt, SDL 13 pp. 71–73): acinar cells pyramidal serous,
#     basophilic base, apical zymogen granules; proenzymes (trypsinogen, chymotrypsinogen, procarboxypeptidase, proelastase)
#     and active amylase and lipases; centroacinar cells pale, flattened, centre of the acinus, intra-acinar origin of the
#     intercalated ducts (unique to the pancreas), no zymogen granules or ergastoplasm, secrete the initial isotonic fluid rich
#     in Na⁺ and HCO₃⁻; intercalated ducts short, low cuboidal, continuous with centroacinar cells; ductal cells secrete
#     Na⁺/HCO₃⁻-rich fluid via CFTR + apical Cl⁻/HCO₃⁻ exchangers, pH ~8.0; secretin (S cells, pH < 4.5) → ductal (and
#     centroacinar) cells, cAMP; CCK (I cells; fatty acids, monoglycerides, peptides, amino acids esp. Phe, Met, Trp) → CCK1
#     receptors on acinar cells, IP3/Ca²⁺, zymogen exocytosis, low-volume enzyme juice; exocrine 80–85% of the organ;
#     endocrine 1–2%, ~1–3 million pale, highly vascular islets scattered among acini, most concentrated in the tail, cords
#     with fenestrated capillaries; B 60–70% central core, insulin (lowers glucose), ~300 nm angular-core granules with halo;
#     A 15–20% "primarily at the periphery of islets in humans", glucagon (glycogenolysis, raises glucose), ~250 nm round
#     eccentric core; D 5–10% at the periphery, somatostatin suppresses insulin and glucagon release and exocrine secretion;
#     PP (F) 1–2%, in islets and scattered in exocrine pancreas, inhibits intestinal motility and enzyme/HCO₃⁻ secretion.
#   Pawlina ch 18 (course histology printout, course_sdl_2_3_12_13_histo_foreguy_p3.txt pp. 66–87): every fact above
#     re-checked; no striated ducts; intercalated duct cells secrete a large volume of Na⁺/HCO₃⁻-rich fluid; Tables 18.2
#     (A/B/D %, granules) and 18.3 (PP cell inhibits pancreatic enzyme and HCO₃⁻ secretion, bile secretion, intestinal motility;
#     epsilon cell — ghrelin, also in the fundic epithelium, stimulates appetite); text: A cells "generally located
#     peripherally", D cells "also located peripherally"; islets get 10–15% of pancreatic blood flow; efferent capillaries
#     branch into the networks around the acini (cascading flow); somatostatin inhibits insulin and glucagon secretion and
#     suppresses exocrine secretion; insulin inhibits glucagon release.
#   First Aid 2025 p. 58 (CFTR: ↓ Cl⁻, H₂O, HCO₃⁻ secretion; thick secretions; pancreatic insufficiency) · p. 331 (α peripheral,
#     β central, δ interspersed) · p. 337 (glucagon from α cells raises blood glucose; inhibited by insulin, somatostatin) ·
#     p. 338 (insulin ↓ glucagon release) · p. 357 (insulinoma, glucagonoma, somatostatinoma) · p. 378 (somatostatin ↓ pancreatic
#     fluid secretion, ↓ insulin and glucagon; ghrelin ↑ appetite; secretin, CCK) · p. 380 (acinar enzymes, amylase active,
#     proteases as zymogens).
#   Robbins ch 19 (course pathology printout, course_sdl_19_patho.txt pp. 2–3): exocrine 80–85%, islets 1–2% of mass, scattered.
# Source conflicts (course wins):
#   1. α-cell position. Course lecture notes ("primarily at the periphery of islets in humans"), Pawlina's text ("generally
#      located peripherally") and First Aid 331 ("peripheral") all put α cells at the rim; Pawlina's figure legends (Fig. 18.26b,
#      18.27) say the strict rim is the rat pattern and that human A cells are "scattered throughout the islets". The course
#      text supports the rim → drawn mainly at the rim with two α cells among the β cells; the α note gives the Pawlina figure
#      caveat. sdl13_q29 (answer: islet periphery) matches the course lecture notes.
#   2. δ-cell position: course notes + Pawlina "periphery" vs First Aid 331 "interspersed" → drawn at the rim, note says
#      "First Aid: interspersed".
#   3. Epsilon (ghrelin) cells: Pawlina Table 18.3 only (not in First Aid or the lecture notes) — cited to Pawlina.
# Readout logic: ↑ = this cell makes it or raises it; ↓ = this cell's hormone suppresses it; – = not this cell / no source.
#   δ → enzymes ↓ (course: "exocrine secretion", as in sdl13_q30), HCO₃⁻ fluid ↓ (First Aid 378 "pancreatic fluid secretion"),
#   insulin ↓, glucagon ↓. PP → enzymes ↓, HCO₃⁻ ↓ (Pawlina Table 18.3, lecture notes). β → glucagon ↓ (First Aid 337–338,
#   Pawlina). α → blood glucose ↑, β → blood glucose ↓.
# Cut for lack of a stated direction or to stay in scope: glucagon's paracrine stimulation of β cells (Pawlina only — in the α
#   note, no arrow); insulin/VIP/CCK stimulating and glucagon inhibiting exocrine secretion (Pawlina p. 87 — no arrow on the α/β
#   rows, kept off to keep each row to the cell's own product); blood flow direction inside the islet (Pawlina gives two
#   patterns); blood glucose for δ (no source gives a direction for normal δ cells); carbonic anhydrase (not in the course
#   notes for this map; on pbsecsim).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

PW18, RB19 = full('Pawlina', 18), full('Robbins', 19)

O = lambda *k: ['c:' + x for x in k]
DUCTFLUID = O('cent', 'icd', 'duct')
BRAKE = O('delta', 'pp')

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
def P(pts): return 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))
def ring(x, y, r, w=5, col='--accent'):
    return f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" style="fill:none;stroke:var({col});stroke-width:{w}"/>'
def lead(x0, y0, x1, y1):
    return f'<path d="M{x0:.0f} {y0:.0f} L{x1:.0f} {y1:.0f}" style="stroke:var(--ink-3);stroke-width:2"/>'

text('The pancreas cell by cell — what each exocrine and islet cell makes', 160, 80, 'dyn-big')
text('top left: the gland from the front · bottom left: one acinus and its ducts · right: one islet of Langerhans', 160, 104, 'dyn-cap')

# ════════ the gland ════════
add('<rect x="160" y="130" width="1060" height="440" rx="24" class="dyn-soft"/>')
text('The pancreas: head in the duodenal C-loop, tail toward the spleen', 190, 170, 'dyn-big')
DUO = 'M470 210 L330 214 C240 230 220 470 300 520 L520 532'
add(dict(tube=DUO, w=40, color='--dk7'))
text('duodenum', 330, 560, 'nf-l2')
PANC = ('M330 300 C390 262 470 296 540 300 C700 292 900 246 1130 252 C1166 266 1166 304 1132 318 C950 338 760 352 640 362 '
        'C590 424 540 470 462 480 C392 488 330 452 322 392 Z')
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.14;stroke:var(--dk5);stroke-width:4"/>')
MPD = [(1110, 286), (900, 300), (700, 322), (560, 352), (430, 420), (300, 462)]
add(f'<path d="{P(MPD)}" style="fill:none;stroke:var(--dk5);stroke-width:7;stroke-linecap:round;opacity:.5"/>')
text('head', 420, 448, 'nf-l2', 'middle')
text('body', 760, 272, 'nf-l2', 'middle')
text('tail', 1110, 238, 'nf-l2', 'middle')
# islets: sparse in the head, crowded in the tail
ISL_DOTS = [(400, 360), (520, 330), (650, 330), (790, 320), (860, 296), (930, 312), (980, 280), (1010, 304), (1050, 268),
            (1070, 300), (1100, 262), (1120, 292), (1140, 278), (960, 300), (1030, 288)]
for x, y in ISL_DOTS:
    add(f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--surface);stroke:var(--dk2);stroke-width:3"/>')
add('<ellipse cx="1060" cy="286" rx="110" ry="50" style="fill:none;stroke:var(--accent);stroke-width:5"/>', when=O('isl'))
text('○ islets — 1–2% of the organ, most in the tail', 720, 410, 'nf-l2')
text('the tail holds the most islets', 720, 434, 'nf-l1', when=O('isl'))
# zoom lines
add('<path d="M560 360 L430 630" class="dyn-dash"/>')
add('<path d="M1150 290 L1440 470" class="dyn-dash"/>')

# ════════ exocrine: acinus → ducts ════════
add('<rect x="160" y="600" width="1060" height="840" rx="24" class="dyn-soft"/>')
text('Exocrine: acinus → ducts (80–85% of the organ)', 190, 642, 'dyn-big')
AC = (430, 960)
RO, RI = 170, 52
for i in range(8):
    a0, a1 = math.radians(i * 45 + 3), math.radians((i + 1) * 45 - 3)
    pts = [(AC[0] + RO * math.cos(a0), AC[1] + RO * math.sin(a0)), (AC[0] + RO * math.cos(a1), AC[1] + RO * math.sin(a1)),
           (AC[0] + RI * math.cos(a1), AC[1] + RI * math.sin(a1)), (AC[0] + RI * math.cos(a0), AC[1] + RI * math.sin(a0))]
    if i == 0: continue          # the gap where the intercalated duct leaves
    add('<path class="dyn-cell" d="' + P(pts) + ' Z"/>')
    am = (a0 + a1) / 2
    for r in (64, 80, 96):       # apical zymogen granules
        gx, gy = AC[0] + r * math.cos(am), AC[1] + r * math.sin(am)
        add(f'<circle cx="{gx:.0f}" cy="{gy:.0f}" r="6" style="fill:var(--dk5)"/>')
    nx, ny = AC[0] + 142 * math.cos(am), AC[1] + 142 * math.sin(am)   # basal nucleus
    add(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="10" style="fill:var(--ink-3);opacity:.45"/>')
add(f'<circle cx="{AC[0]}" cy="{AC[1]}" r="44" class="nf-lumen" style="stroke:none"/>')
# centroacinar cells: pale, flat, in the middle
for cx, cy, rot in ((AC[0] + 14, AC[1] - 22, -20), (AC[0] + 32, AC[1] + 16, 25), (AC[0] - 22, AC[1] + 10, 80)):
    add(f'<ellipse cx="{cx}" cy="{cy}" rx="20" ry="7" transform="rotate({rot} {cx} {cy})" '
        f'style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:2"/>')
add(ring(AC[0], AC[1], 182, 6), when=O('acin'))
add(ring(AC[0] + 8, AC[1], 54, 5), when=O('cent'))
text('acinar cells', AC[0], AC[1] + 206, 'nf-l1', 'middle')
text('basophilic base · zymogen granules at the apex', AC[0], AC[1] + 230, 'nf-l2', 'middle')
add(lead(AC[0] + 40, AC[1] + 20, 610, 1090))
text('centroacinar cells', 620, 1096, 'nf-l1')
text('pale · no granules', 620, 1118, 'nf-l2')
# ducts
ICD = f'M{AC[0] + 40} {AC[1]} L760 {AC[1]}'
add(dict(tube=ICD, w=26, color='--dk6'))
add(f'<path d="{ICD}" style="fill:none;stroke:var(--accent);stroke-width:46;opacity:.25"/>', when=O('icd'))
text('intercalated duct', 690, 920, 'nf-l1', 'middle')
DUCT = f'M760 {AC[1]} C820 {AC[1]} 840 1000 900 1000 L1190 1000'
add(dict(tube=DUCT, w=40, color='--dk6'))
text('intralobular → interlobular → main duct', 1190, 948, 'nf-l2', 'end')
text('no striated ducts in the pancreas', 1190, 926, 'nf-l2', 'end', when=O('icd'))
# the duct cell
CX0, CX1, CY0, CY1 = 800, 1190, 1046, 1290
add(f'<rect x="{CX0}" y="{CY0}" width="{CX1 - CX0}" height="{CY1 - CY0}" rx="16" class="dyn-cell"/>')
add(f'<rect x="{CX0 - 8}" y="{CY0 - 8}" width="{CX1 - CX0 + 16}" height="{CY1 - CY0 + 16}" rx="20" '
    f'style="fill:none;stroke:var(--accent);stroke-width:5"/>', when=O('duct'))
text('duct cell', 820, 1206, 'nf-l1')
text('secretin → cAMP', 820, 1228, 'nf-l2')
add(dict(vessel=f'M{CX0} 1350 L{CX1} 1350', w=22, color='--nf-blood'))
text('blood', CX0, 1396, 'nf-l2')
text('secretin arrives (acid in the duodenum)', CX1, 1396, 'nf-l2', 'end', when=DUCTFLUID)
# CCK from the blood to the acinar cell
text('CCK (I cells)', 200, 760, 'nf-l2', when=O('acin'))
# efferent capillaries: islet → acini (cascading flow)
EFF = [(1420, 700), (700, 700), (640, 712), (600, 760), (580, 812)]
add(dict(vessel=P(EFF), w=14, color='--nf-blood'))
text('efferent capillaries carry islet hormones on to the acini', 720, 746, 'nf-l2')

# ════════ the islet ════════
add('<rect x="1260" y="130" width="1080" height="1310" rx="24" class="dyn-soft"/>')
text('Endocrine: one islet of Langerhans', 1290, 170, 'dyn-big')
text('pale cords of cells wrapped in fenestrated capillaries', 1290, 196, 'dyn-cap')
IC, IR = (1720, 700), 300
add(f'<circle cx="{IC[0]}" cy="{IC[1]}" r="{IR + 20}" style="fill:var(--surface-2);stroke:var(--ink-3);stroke-width:2;stroke-dasharray:8 6"/>')
add(ring(IC[0], IC[1], IR + 34, 6), when=O('isl'))
# acini around the islet (it sits among exocrine tissue)
def rosette(cx, cy, r=46):
    s = ''
    for i in range(6):
        a0, a1 = math.radians(i * 60 + 6), math.radians((i + 1) * 60 - 6)
        pts = [(cx + r * math.cos(a0), cy + r * math.sin(a0)), (cx + r * math.cos(a1), cy + r * math.sin(a1)),
               (cx + 12 * math.cos(a1), cy + 12 * math.sin(a1)), (cx + 12 * math.cos(a0), cy + 12 * math.sin(a0))]
        s += '<path class="dyn-cell" d="' + P(pts) + ' Z" style="opacity:.6"/>'
    return s
for cx, cy in ((1380, 300), (1350, 1090), (1560, 1150), (2080, 1110)):
    add(rosette(cx, cy))
# capillaries through the islet
for d in ('M1440 640 C1560 560 1640 760 1760 680 C1860 610 1920 760 2010 720',
          'M1520 900 C1600 820 1700 920 1800 840 C1880 780 1940 860 1980 820',
          'M1560 470 C1640 540 1740 440 1840 520 C1900 560 1950 500 1990 560'):
    add(f'<path d="{d}" style="fill:none;stroke:var(--nf-blood);stroke-width:8;opacity:.45"/>')

CELLR = 24
def cell(x, y, col):
    return f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{CELLR}" style="fill:var({col});fill-opacity:.32;stroke:var({col});stroke-width:2.5"/>'
BETA, ALPHA, DELTA, PPC, EPS = [], [], [], [], []
# β cells fill the core (hex packing within r 210)
for row in range(-5, 6):
    for col in range(-5, 6):
        x = IC[0] + col * 50 + (25 if row % 2 else 0)
        y = IC[1] + row * 44
        if math.hypot(x - IC[0], y - IC[1]) <= 205: BETA.append((x, y))
# the rim: α cells mostly, δ cells and PP cells among them
RIM = [(IC[0] + 262 * math.cos(math.radians(a)), IC[1] + 262 * math.sin(math.radians(a))) for a in range(0, 360, 15)]
for i, p in enumerate(RIM):
    if i % 6 == 2: DELTA.append(p)
    elif i in (3, 13): PPC.append(p)
    elif i == 5: EPS.append(p)
    else: ALPHA.append(p)
# two α cells among the β cells (Pawlina Fig. 18.27: human α cells also scattered)
SCAT = [(IC[0] - 75, IC[1] - 44), (IC[0] + 100, IC[1] + 88)]
BETA = [b for b in BETA if min(math.hypot(b[0] - s[0], b[1] - s[1]) for s in SCAT) > 30]
ALPHA += SCAT
for pts, colr in ((BETA, '--dk2'), (ALPHA, '--dk4'), (DELTA, '--dk9'), (PPC, '--dk11'), (EPS, '--dk10')):
    add(''.join(cell(x, y, colr) for x, y in pts))
# one PP cell out among the acini
PPX = (1440, 1100)
add(cell(*PPX, '--dk11'))
# highlights per option
add(f'<circle cx="{IC[0]}" cy="{IC[1]}" r="222" style="fill:none;stroke:var(--accent);stroke-width:6"/>', when=O('beta'))
add(''.join(ring(x, y, CELLR + 6, 4) for x, y in ALPHA), when=O('alpha'))
add(''.join(ring(x, y, CELLR + 6, 4) for x, y in DELTA), when=O('delta'))
add(''.join(ring(x, y, CELLR + 6, 4) for x, y in PPC + [PPX]), when=O('pp'))
add(''.join(ring(x, y, CELLR + 6, 4) for x, y in EPS), when=O('eps'))
# labels at the right, with leaders
LX = 2060
def near(pts, ly): return min(pts, key=lambda q: math.hypot(LX - q[0], ly - q[1]))
for (px, py), ly, t1, t2 in ((near(ALPHA, 470), 470, 'α cells — glucagon', 'mainly at the rim'),
                             (near(BETA, 640), 640, 'β cells — insulin', 'the central core'),
                             (near(DELTA, 780), 780, 'δ cells — somatostatin', 'at the rim'),
                             (near(PPC, 900), 900, 'PP (F) cells', 'islet + exocrine tissue'),
                             (near(EPS, 1010), 1010, 'ε cell — ghrelin', 'minor type (Pawlina)')):
    add(lead(px + CELLR * 0.7, py, LX - 10, ly - 5))
    text(t1, LX, ly, 'nf-l1')
    text(t2, LX, ly + 20, 'nf-l2')
text('PP cell among the acini', PPX[0], PPX[1] + 52, 'nf-l2', 'middle', when=O('pp'))
text('1–2% of the mass · 10–15% of the pancreatic blood flow', IC[0], 1250, 'nf-l2', 'middle', when=O('isl'))
text('islet cells', IC[0], 1250, 'nf-l2', 'middle', unless=O('isl'))
add(dict(vessel=f'M{IC[0]} {IC[1] + IR + 20} L{IC[0]} 1200', w=14, color='--nf-blood'))
text('to the blood', IC[0] + 20, 1196, 'nf-l2')
text('↑ blood glucose (liver: glycogenolysis)', IC[0], 1290, 'nf-l1', 'middle', when=O('alpha'))
text('↓ blood glucose (glucose into muscle and fat)', IC[0], 1290, 'nf-l1', 'middle', when=O('beta'))
text('brakes insulin, glucagon and the exocrine pancreas', IC[0], 1290, 'nf-l1', 'middle', when=O('delta'))
text('brakes enzyme and HCO₃⁻ secretion, bile, gut motility', IC[0], 1290, 'nf-l1', 'middle', when=O('pp'))
text('↑ appetite (also made in the gastric fundus)', IC[0], 1290, 'nf-l1', 'middle', when=O('eps'))

# ════════ kinds and motion ════════
KL = [('enz', '--dk5', 'enzymes'), ('hco3', '--nf-hco3', 'HCO₃⁻ fluid'), ('cl', '--nf-cl', 'Cl⁻'),
      ('ins', '--dk2', 'insulin'), ('glu', '--dk4', 'glucagon'), ('sst', '--dk9', 'somatostatin'),
      ('pp', '--dk11', 'pancreatic polypeptide'), ('ghr', '--dk10', 'ghrelin'),
      ('sec', '--dk8', 'secretin'), ('cck', '--dk7', 'CCK')]
GRP = dict(enz='exo', hco3='exo', cl='exo', ins='isl', glu='isl', sst='isl', pp='isl', ghr='isl', sec='gut', cck='gut')
kinds = {k: [GRP[k], c, l] for k, c, l in KL}
groups = [['exo', 'Exocrine juice'], ['isl', 'Islet hormones'], ['gut', 'Gut hormones']]

flows = []
def fl(pts_or_d, base, when=None, unless=None, mods=None, sp=110, r=7, ln=None):
    d = pts_or_d if isinstance(pts_or_d, str) else P(pts_or_d)
    f = dict(d=d, len=ln or plen(pts_or_d), speed=sp, r=r, base=base)
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
# enzymes out of the acinar lumen down the ducts
fl([AC, (760, AC[1]), (820, 975), (900, 1000), (1190, 1000)], dict(enz=2), sp=90, mods=[
   dict(when=O('acin'), set=dict(enz=6)), dict(when=BRAKE, set=dict(enz=1), speed=0.5)])
# HCO₃⁻-rich water added from the centroacinar cells and ducts
fl([(AC[0] + 30, AC[1]), (760, AC[1]), (820, 975), (900, 1000), (1190, 1000)], dict(hco3=2), sp=120, mods=[
   dict(when=DUCTFLUID, set=dict(hco3=6)), dict(when=BRAKE, set=dict(hco3=1), speed=0.5)])
# gut hormones
fl([(200, 780), (300, 790), (400, 790)], dict(cck=3), when=O('acin'), sp=50)
fl([(CX0, 1350), (1100, 1350), (1100, 1310)], dict(sec=3), when=DUCTFLUID, sp=60)
# islet hormones: into the capillaries, out to the acini and to the blood
OUT_ACINI = [(IC[0], IC[1]), (1420, 700)] + EFF[1:]
OUT_BLOOD = [(IC[0], IC[1]), (IC[0], 1200)]
fl(OUT_ACINI, dict(ins=1, glu=1), sp=120, mods=[
   dict(when=O('beta'), set=dict(ins=5, glu=0)), dict(when=O('alpha'), set=dict(glu=5, ins=1)),
   dict(when=O('delta'), set=dict(ins=0, glu=0, sst=4)), dict(when=O('pp'), set=dict(pp=4)),
   dict(when=O('isl'), set=dict(ins=2, glu=1, sst=1, pp=1)), dict(when=O('eps'), set=dict(ghr=2))])
fl(OUT_BLOOD, dict(ins=1), sp=90, mods=[
   dict(when=O('beta'), set=dict(ins=4)), dict(when=O('alpha'), set=dict(ins=0, glu=4)),
   dict(when=O('delta'), set=dict(ins=0, sst=2)), dict(when=O('pp'), set=dict(ins=0, pp=3)),
   dict(when=O('eps'), set=dict(ins=0, ghr=3))])
# α/δ/PP hormones from the rim into the core capillaries
for (x, y), k, opt in ((ALPHA[0], 'glu', 'alpha'), (ALPHA[8], 'glu', 'alpha'), (DELTA[1], 'sst', 'delta'), (PPC[1], 'pp', 'pp'),
                       (EPS[0], 'ghr', 'eps')):
    fl([(x, y), (IC[0], IC[1])], {k: 2}, when=O(opt), sp=70)

# ════════ sites (tap targets) ════════
sites = [
  dict(x=AC[0], y=AC[1] - RO, n=[0, -1], w=12, t='rec', l='CCK1 receptor', s='IP3 · Ca²⁺', ions=[], c='cck',
       lx=AC[0] + 30, ly=AC[1] - RO - 46, la='start', boost=O('acin'), low=BRAKE),
  dict(x=880, y=CY0, n=[0, 1], w=12, t='ex', l='Cl⁻–HCO₃⁻ exchanger', s='apical', ions=[['hco3', 'in', 2], ['cl', 'out', 1]],
       c='pancsec', lx=820, ly=1094, la='start', boost=DUCTFLUID, low=BRAKE),
  dict(x=1110, y=CY0, n=[0, 1], w=12, t='ch', l='CFTR Cl⁻ channel', s='Cl⁻ back to the lumen', ions=[['cl', 'in', 2]],
       c='cf', lx=1172, ly=1146, la='end', boost=DUCTFLUID, low=BRAKE),
  dict(x=1100, y=CY1, n=[0, -1], w=12, t='rec', l='secretin receptor', s='', ions=[], c='secretin', lx=1172, ly=1262, la='end',
       stop=['!c:*'] + O('acin', 'isl', 'alpha', 'beta', 'delta', 'pp', 'eps'), boost=DUCTFLUID, sfx=dict(stop=' — no signal')),
  dict(x=IC[0], y=IC[1] - 130, n=[0, -1], w=8, t='rec', l='', aria='β cell — insulin secretion', ions=[], c='insulinsecr'),
  dict(x=ALPHA[0][0], y=ALPHA[0][1], n=[1, 0], w=8, t='rec', l='', aria='α cell — glucagon', ions=[], c='glucagonact'),
  dict(x=DELTA[0][0], y=DELTA[0][1], n=[1, 0], w=8, t='rec', l='', aria='δ cell — somatostatin', ions=[], c='sstgi'),
  dict(x=EPS[0][0], y=EPS[0][1], n=[-1, 0], w=8, t='rec', l='', aria='ε cell — ghrelin', ions=[], c='ghrelin'),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Digestive enzymes', mods=[R(O('acin'), 1), R(BRAKE, -1)]),
  dict(l='HCO₃⁻-rich fluid', mods=[R(DUCTFLUID, 1), R(BRAKE, -1)]),
  dict(l='Insulin', mods=[R(O('beta'), 1), R(O('delta'), -1)]),
  dict(l='Glucagon', mods=[R(O('alpha'), 1), R(O('beta', 'delta'), -1)]),
  dict(l='Somatostatin', mods=[R(O('delta'), 1)]),
  dict(l='Pancreatic polypeptide', mods=[R(O('pp'), 1)]),
  dict(l='Blood glucose', mods=[R(O('alpha'), 1), R(O('beta'), -1)]),
]

notes = {
  '': 'The pancreas is two glands in one: serous acini and their ducts make the digestive juice (80–85% of the organ), and the '
      'islets of Langerhans (1–2%) make hormones. Pick a cell. ↑ this cell makes or raises it · ↓ its hormone suppresses it · '
      '– not this cell.',
  'c:acin': 'Acinar cells: pyramidal serous cells with a basophilic base (rough ER) and apical zymogen granules. They release '
            'proteases as proenzymes (trypsinogen, chymotrypsinogen, procarboxypeptidase, proelastase) but amylase and lipase in '
            'active form. CCK on CCK1 receptors (IP3 and Ca²⁺) triggers the exocytosis.',
  'c:cent': 'Centroacinar cells: pale, flattened cells in the middle of the acinus, with no zymogen granules — the start of the '
            'intercalated duct inside the acinus, a feature unique to the pancreas. They secrete the first isotonic fluid rich in '
            'Na⁺ and HCO₃⁻, and answer to secretin.',
  'c:icd': 'Intercalated ducts: short ducts of low cuboidal cells, continuous with the centroacinar cells. They add a large volume '
           'of Na⁺- and HCO₃⁻-rich water, then drain into intralobular and interlobular ducts and the main duct. The pancreas has '
           'no striated ducts.',
  'c:duct': 'Duct cells secrete Na⁺- and HCO₃⁻-rich fluid: the apical Cl⁻–HCO₃⁻ exchanger swaps HCO₃⁻ for luminal Cl⁻, and CFTR '
            'returns the Cl⁻; secretin (cAMP) drives them, bringing the juice to about pH 8. In cystic fibrosis CFTR never reaches '
            'the membrane, so less Cl⁻, water and HCO₃⁻ are secreted and thick secretions plug the ducts.',
  'c:isl': 'Islets of Langerhans: about 1–3 million pale clusters scattered among the acini, only 1–2% of the organ and most '
           'concentrated in the tail. Their cords of cells are wrapped in fenestrated capillaries; the islets get 10–15% of the '
           'pancreatic blood flow, and their efferent capillaries run on to the acini.',
  'c:alpha': 'Alpha (A) cells, 15–20% of islet cells, sit mainly at the islet periphery in humans (course notes; First Aid) and '
             'make glucagon, which drives glycogenolysis and raises blood glucose. Pawlina’s figures add that human α cells are '
             'also scattered among the β cells — a strict rim is the rat pattern. A tumor of them is a glucagonoma.',
  'c:beta': 'Beta (B) cells, 60–70% of islet cells, fill the central core and make insulin, which lowers blood glucose and '
            'restrains glucagon release. Their ~300 nm granules have a dense, angular (crystalline) core and a clear halo. A '
            'tumor of them is an insulinoma: low glucose with high C-peptide.',
  'c:delta': 'Delta (D) cells, 5–10% of islet cells, sit at the islet periphery (First Aid: interspersed) and make somatostatin, '
             'which suppresses insulin and glucagon release and the exocrine pancreas. A somatostatinoma gives diabetes, '
             'steatorrhea, gallstones and achlorhydria.',
  'c:pp': 'PP (F) cells, 1–2% of islet cells, lie in the islets and also scattered in the exocrine tissue. Pancreatic polypeptide '
          'inhibits pancreatic enzyme and HCO₃⁻ secretion, bile secretion and intestinal motility.',
  'c:eps': 'Epsilon cells are a minor islet cell type (Pawlina Table 18.3) that make ghrelin — the appetite hormone made mostly by '
           'the gastric fundus, which rises with fasting.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='c', label='Pick a cell', type='one', options=[
      ['acin', 'Acinar cells — zymogen granules', 'pancsec'], ['cent', 'Centroacinar cells', 'pancsec'],
      ['icd', 'Intercalated ducts', 'pancsec'], ['duct', 'Ductal cells — CFTR · HCO₃⁻', 'cf'],
      ['isl', 'Islets of Langerhans', 'islets'], ['alpha', 'Alpha cells — glucagon', 'islets'],
      ['beta', 'Beta cells — insulin', 'islets'], ['delta', 'Delta cells — somatostatin', 'islets'],
      ['pp', 'PP (F) cells — pancreatic polypeptide', 'islets'], ['eps', 'Epsilon cells — ghrelin', 'islets']],
      sections=[['Exocrine', ['acin', 'cent', 'icd', 'duct']],
                ['Endocrine', ['isl', 'alpha', 'beta', 'delta', 'pp', 'eps']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI course lecture notes (SDL 13) · Pawlina ch 18 · Robbins ch 19 · First Aid pp. 58, 331, 337–338, 357, 378, 380')

MAP = dict(
  id='isletsim', title='Pancreatic Acinus & Islet in Motion', topic='gi', after='biliflow',
  sub='Pick a pancreatic cell — acinar, centroacinar, intercalated or main-duct, or an islet α, β, δ, PP or ε cell — and watch '
      'what it secretes, where it sits and which outputs its hormone brakes. Tap a receptor, channel or pin for its card',
  w=3480, h=1820,
  fa='58, 331, 337, 338, 357, 378, 380', src=[PW18, RB19],
  lanes=[('isExo', 'Exocrine pancreas', 'glycolysis'), ('isCtl', 'Gut hormones', 'ppp'), ('isEndo', 'Islet hormones', 'gluconeo'),
         ('isDz', 'When it fails', 'tca')],
  comps=[],
  nodes=[
    ('is1', 'Acini, ducts & islets', 260, 1530, 'isExo', 'histology', ['islets'], 'hub'),
    ('is2', 'Pancreatic secretions', 680, 1530, 'isExo', 'enzymes + HCO₃⁻', ['pancsec']),
    ('is3', 'Exocrine secretion', 1100, 1530, 'isExo', 'merocrine · zymogen', ['exocrine']),
    ('is4', 'Secretin', 1500, 1530, 'isCtl', 'S cells · duct cells', ['secretin']),
    ('is5', 'CCK', 1880, 1530, 'isCtl', 'I cells · acinar cells', ['cck']),
    ('is6', 'Insulin secretion', 260, 1630, 'isEndo', 'β cell', ['insulinsecr'], 'hub'),
    ('is7', 'Glucagon', 680, 1630, 'isEndo', 'α cell', ['glucagonact']),
    ('is8', 'Somatostatin', 1100, 1630, 'isEndo', 'δ cell · the brake', ['sstgi']),
    ('is9', 'Ghrelin', 1500, 1630, 'isEndo', 'ε cell · fundus', ['ghrelin']),
    ('is10', 'Cystic fibrosis', 260, 1730, 'isDz', 'CFTR', ['cf', 'cfcourse']),
    ('is11', 'Pancreatic insufficiency', 680, 1730, 'isDz', 'steatorrhea', ['pancins']),
    ('is12', 'Insulinoma · glucagonoma', 1100, 1730, 'isDz', 'β · α tumors', ['insulinoma', 'glucagonoma']),
    ('is13', 'Somatostatinoma', 1500, 1730, 'isDz', 'δ tumor', ['somatostatinoma']),
  ],
  panels=[
    (2420, 830, 1000, 'Islet cells (course notes; Pawlina ch 18, Tables 18.2–18.3)', [
      ('β (B) · 60–70%', 'central core · insulin'),
      ('α (A) · 15–20%', 'mainly at the rim · glucagon'),
      ('δ (D) · 5–10%', 'at the rim · somatostatin'),
      ('PP (F) · 1–2%', 'islets + exocrine tissue · pancreatic polypeptide'),
      ('ε (epsilon)', 'minor type · ghrelin')]),
    (2420, 1050, 1000, 'Islet cell tumors (First Aid p. 357)', [
      ('Insulinoma (β)', 'hypoglycemia · ↑ C-peptide · Whipple triad'),
      ('Glucagonoma (α)', 'necrolytic migratory erythema · diabetes · DVT'),
      ('Somatostatinoma (δ)', 'diabetes · steatorrhea · gallstones · achlorhydria')]),
  ],
  dyn=dyn,
)
