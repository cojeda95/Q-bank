# m58 — Digestive Enzymes Step by Step in Motion (dynamic map, kit data)
# Top: where each enzyme is made and switched on — the stomach (chief cells, acid), the pancreas in the duodenal C-loop
# with its main duct to the ampulla, the small intestine; a close-up of one acinar cell (zymogen granules, SPINK1) and one
# of the duodenal brush border (enteropeptidase, lactase, sucrase · maltase · α-dextrinase, peptidases). Bottom left: the
# trypsin cascade (enteropeptidase makes the first trypsin; trypsin activates every other zymogen and more trypsinogen).
# Bottom right: what each enzyme cuts — carbohydrate, protein, lipid, nucleic acid, substrate → product.
# One `one` switch (`e`, 11 enzymes in four sections). Six readouts: starch, lactose, protein, lipid and nucleic acid
# digested, and trypsin activity. pbsecsim covers juice volume / HCO3- / bile, gutabs absorption, gihormsim the hormones;
# this map is the enzymes themselves.
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   GI Exam 1 lecture notes (course_exam1_lecture_notes.txt): p17 (SDL 3) chief cells secrete pepsinogen and gastric lipase;
#     acid below pH 5 (optimum 1.8–3.5) cleaves pepsinogen to pepsin. p74–75 (SDL 14 §1) enzymes made on rER → Golgi →
#     apical zymogen granules; proteases secreted only as zymogens; α-amylase, lipases, cholesterol ester hydrolase and
#     nucleases secreted active; enteropeptidase (enterokinase) in the duodenal brush-border glycocalyx cleaves a hexapeptide
#     from trypsinogen; trypsin autocatalyzes trypsinogen and activates chymotrypsinogen, proelastase, procarboxypeptidases
#     A and B, prophospholipase A2 and procolipase; colipase binds lipase so it works despite bile salts; endopeptidases
#     (trypsin, chymotrypsin, elastase) vs exopeptidases (carboxypeptidases A, B: single amino acids from the C-terminal end);
#     α-amylase: starch + glycogen → di- and trisaccharides; lipase: TG → 2-monoglyceride + free fatty acids; cholesterol ester
#     hydrolase; PLA2 → lysolecithin; autodigestion prevented by zymogen packaging, activation only in the duodenum, SPINK1
#     (co-packaged, inactivates up to 20% of prematurely formed trypsin), trypsin self-degradation (CTRC/caldecrin).
#     p106 (SDL 19) acute pancreatitis is initiated by intrapancreatic trypsinogen → trypsin activation; the cascade
#     (phospholipase, elastase) drives autodigestion and fat necrosis; genetic causes PRSS1, SPINK1, CFTR.
#   Costanzo ch 8 (course_sdl_4_7_physio): p35 Table 8.6 (sources of digestive enzymes: brush-border sucrase, maltase,
#     lactase, trehalase, α-dextrinase, amino-oligopeptidase, dipeptidase, enterokinase); p36 granules released on
#     parasympathetic activity or CCK, granules impermeable to proteins, trypsin inhibitors co-packaged; p44 pancreatic
#     amylase cuts interior α-1,4 bonds → α-limit dextrins, maltose, maltotriose → glucose by α-dextrinase, maltase, sucrase;
#     salivary amylase inactivated by gastric acid; lactose → glucose + galactose; p45 SGLT1; p46 lactase deficiency:
#     osmotic diarrhea, gas from fermentation; endo- vs exopeptidases; p47 pepsin optimum pH 1–3, denatured above pH 5,
#     not essential (gastrectomy: protein still digested); enterokinase → trypsin → all other proenzymes; p48–49 absence of
#     trypsin looks like absence of all pancreatic enzymes; p50 lingual + gastric lipases ~10% of TG; lipase secreted active,
#     inactivated by bile salts, colipase (procolipase, activated by trypsin) displaces them; cholesterol ester hydrolase;
#     PLA2 proenzyme activated by trypsin → lysolecithin + fatty acid; lysolecithin helps emulsify; p52 pancreatic
#     insufficiency → steatorrhea.
#   Pawlina ch 18 (course histology, histo_foreguy_p3 p69): nucleolytic enzymes (DNase, RNase) digest nucleic acids to
#     mononucleotides; enterokinase in the microvillus glycocalyx makes the first trypsin.
#   First Aid 2025 p. 79 (lactase on the brush border; lactose → glucose + galactose) · p. 379 (pepsin: chief cells, ↑ by
#     vagal ACh and local acid, pepsinogen → pepsin with H+) · p. 380 (α-amylase active; proteases as zymogens; trypsin
#     positive feedback; enterokinase/enteropeptidase on duodenal and jejunal mucosa) · p. 388 (lactose intolerance ↓ stool
#     pH; pancreatic insufficiency ↓ fecal elastase) · p. 404 (acute pancreatitis = autodigestion; SPINK1 in chronic).
# Conflict (course wins): Pawlina lists nucleases among the inactive proenzymes of the zymogen granules; the lecture notes
#   (and FA/Costanzo say nothing either way) give them as secreted active → "secreted active".
# Left as "–": enteropeptidase and trypsin on lipid digestion (they activate colipase / PLA2, but no source states a
#   direction for fat digested); trypsin on starch; every enzyme on what it does not cut.
# Cut for lack of a course/FA source: trehalase (only in Costanzo's table, not taught), Pawlina's "proaminopeptidase".
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ8, PW18 = full('Costanzo', 8), full('Pawlina', 18)
SRC = [CZ8, PW18]

O = lambda *k: ['e:' + x for x in k]

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
def XM(x, y, s=12):
    return (f'<circle cx="{x}" cy="{y}" r="{s + 8}" style="fill:var(--surface);opacity:.92"/>'
            f'<path class="dyn-lesion" d="M{x - s} {y - s} L{x + s} {y + s} M{x + s} {y - s} L{x - s} {y + s}"/>')
def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))
def HL(x0, y0, x1, y1, when):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="14" class="dyn-hl"/>', when=when)

text('Digestive enzymes — where each is made, what switches it on, what it cuts', 160, 80, 'dyn-big')
text('top: the organs from the front, an acinar cell and the duodenal brush border · bottom: the trypsin cascade and each nutrient, step by step', 160, 104, 'dyn-cap')

# ════════ A. where each enzyme is made and switched on ════════
add('<rect x="140" y="130" width="2200" height="770" rx="24" class="dyn-soft"/>')
text('Where each enzyme is made and switched on', 170, 172, 'dyn-big')

# stomach (front view, J shape: fundus up on the viewer's right, pylorus low on the viewer's left)
STOM0 = ('M940 330 C960 270 1090 260 1140 330 C1190 400 1200 570 1130 660 C1070 740 930 775 820 760 L805 712 '
         'C910 710 1000 680 1040 610 C1080 540 1060 430 1000 410 C965 400 940 380 940 330 Z')
import re as _re
def _tf(m):
    x, y = float(m.group(1)), float(m.group(2))
    return f'{(x - 805) * 0.85 + 330:.0f} {(y - 260) * 0.8 + 220:.0f}'
STOM = _re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', _tf, STOM0)
add(f'<path d="{STOM}" style="fill:var(--dk3);fill-opacity:.12;stroke:var(--dk3);stroke-width:4"/>', unless=O('pep'))
add(f'<path d="{STOM}" style="fill:var(--dk3);fill-opacity:.28;stroke:var(--accent);stroke-width:5"/>', when=O('pep'))
text('stomach', 560, 300, 'nf-l1', 'middle')
text('chief cells: pepsinogen', 700, 360)
text('acid (pH < 5) → pepsin', 700, 386)
text('lingual + gastric lipase: ~10% of triglyceride', 700, 412)

# duodenum (C-loop) → jejunum, and the pancreas in the loop
DUO = 'M336 616 C290 618 248 630 238 668 L232 770 C234 806 262 826 316 826 L2300 826'
add(dict(tube=DUO, w=44, color='--dk7'))
text('duodenum', 300, 880, 'nf-l1', 'middle')
text('jejunum →', 2290, 880, 'nf-l1', 'end')
PANC = ('M262 668 C300 650 340 676 380 700 C520 702 720 684 900 700 C930 710 930 748 900 756 C720 774 520 774 410 772 '
        'C370 790 316 792 284 774 C262 748 256 704 262 668 Z')
add(f'<path d="{PANC}" style="fill:var(--dk12);fill-opacity:.14;stroke:var(--dk12);stroke-width:4"/>')
text('pancreas', 700, 744, 'nf-l1', 'middle')
MPD = [(880, 726), (640, 734), (420, 738), (300, 722), (262, 712)]
add(f'<path d="{P(MPD)}" style="fill:none;stroke:var(--dk12);stroke-width:8;stroke-linecap:round;opacity:.6"/>')
add('<circle cx="258" cy="712" r="11" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:5"/>')
text('main duct → ampulla', 470, 712, 'nf-l2', 'middle')

# zoom links to the two close-ups
add('<path d="M900 712 L990 640" class="dyn-dash"/>')
add('<path d="M1700 812 L1760 732" class="dyn-dash"/>')

# ── close-up 1: acinar cell ──
add('<rect x="990" y="196" width="620" height="536" rx="22" style="fill:var(--surface);stroke:var(--line-2);stroke-width:2"/>')
text('Acinar cell (pancreas)', 1016, 236, 'dyn-big')
add('<rect x="1060" y="350" width="480" height="300" rx="34" class="dyn-cell"/>')
add('<path d="M1060 330 L1540 330" style="stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 6"/>')
text('acinar lumen → duct', 1066, 318, 'nf-l2')
for i, gx in enumerate(range(1110, 1500, 56)):
    gy = 392 if i % 2 == 0 else 420
    add(f'<circle cx="{gx}" cy="{gy}" r="20" style="fill:var(--dk5);fill-opacity:.35;stroke:var(--dk5);stroke-width:3"/>')
text('zymogen granules: proenzymes + SPINK1', 1300, 478, 'nf-l2', 'middle')
text('rough ER → Golgi → granules', 1300, 504, 'nf-l2', 'middle')
add('<ellipse cx="1300" cy="590" rx="58" ry="36" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--ink-3);stroke-width:2"/>')
for k in range(3):
    add(f'<path d="M1110 {556 + k * 22} C1160 {546 + k * 22} 1190 {566 + k * 22} 1220 {556 + k * 22}" style="fill:none;stroke:var(--ink-3);stroke-width:2"/>')
    add(f'<path d="M1380 {556 + k * 22} C1420 {546 + k * 22} 1450 {566 + k * 22} 1490 {556 + k * 22}" style="fill:none;stroke:var(--ink-3);stroke-width:2"/>')
text('nucleus · rER', 1300, 640, 'nf-l2', 'middle')
# SPINK1 traps a trypsin formed too early inside a granule
add('<circle cx="1222" cy="392" r="8" style="fill:var(--bad)"/>' + XM(1222, 392, 10), when=O('spink'))
text('SPINK1 traps trypsin formed too early', 1300, 690, 'nf-l1', 'middle', when=O('spink'))
text('if trypsin forms here → the gland digests itself', 1300, 690, 'nf-l1', 'middle', when=O('tryp'))
HL(1086, 364, 1514, 444, O('spink'))

# ── close-up 2: duodenal brush border ──
add('<rect x="1640" y="196" width="680" height="536" rx="22" style="fill:var(--surface);stroke:var(--line-2);stroke-width:2"/>')
text('Duodenal brush border', 1666, 236, 'dyn-big')
BBY = 440                                  # microvillus tips
for cx0 in (1680, 1990):
    add(f'<rect x="{cx0}" y="{BBY + 30}" width="300" height="200" rx="16" class="dyn-cell"/>')
    add(f'<ellipse cx="{cx0 + 150}" cy="{BBY + 150}" rx="34" ry="46" style="fill:var(--dk5);fill-opacity:.2;stroke:var(--ink-3);stroke-width:2"/>')
    add(''.join(f'<rect x="{x}" y="{BBY}" width="8" height="34" rx="4" style="fill:var(--dyn-cell);stroke:var(--dyn-cell-line);stroke-width:1.5"/>'
                for x in range(cx0 + 8, cx0 + 296, 16)))
text('enterocytes (duodenum, jejunum)', 1980, 712, 'nf-l2', 'middle')

# ════════ B. the trypsin cascade ════════
add('<rect x="140" y="930" width="900" height="970" rx="24" class="dyn-soft"/>')
text('Trypsin switches the zymogens on (duodenal lumen)', 170, 972, 'dyn-big')
text('left: secreted inactive · right: active', 170, 1000, 'dyn-cap')
ZX0, ZX1, AX0, AX1 = 180, 480, 720, 1000
ROWS = [('tg', 'trypsinogen', 'trypsin', 1100), ('chy', 'chymotrypsinogen', 'chymotrypsin', 1220),
        ('el', 'proelastase', 'elastase', 1310), ('cp', 'procarboxypeptidase A · B', 'carboxypeptidase A · B', 1400),
        ('pl', 'prophospholipase A₂', 'phospholipase A₂', 1490), ('co', 'procolipase', 'colipase', 1580)]
RY = {k: y for k, _, _, y in ROWS}
for k, z, a, y in ROWS:
    add(f'<rect x="{ZX0}" y="{y - 22}" width="{ZX1 - ZX0}" height="44" rx="12" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 5"/>')
    add(f'<rect x="{AX0}" y="{y - 22}" width="{AX1 - AX0}" height="44" rx="12" style="fill:var(--dk5);fill-opacity:.16;stroke:var(--dk5);stroke-width:3"/>')
    text(z, (ZX0 + ZX1) // 2, y + 5, 'nf-l1', 'middle')
    text(a, (AX0 + AX1) // 2, y + 5, 'nf-l1', 'middle')
    add(f'<path d="M{ZX1} {y} L{AX0 - 6} {y}" class="dyn-line" marker-end="url(#ah-dgMake)"/>')
text('enteropeptidase', 600, 1090, 'nf-l1', 'middle')
text('(brush border)', 600, 1126, 'nf-l2', 'middle')
# trypsin feeds every other conversion, and more trypsinogen
add(f'<path d="M860 1122 L860 1152 L600 1152 L600 {RY["co"]}" style="fill:none;stroke:var(--dk11);stroke-width:4"/>')
for k in ('chy', 'el', 'cp', 'pl', 'co'):
    add(f'<circle cx="600" cy="{RY[k]}" r="8" style="fill:var(--dk11)"/>')
text('trypsin', 628, 1182, 'nf-l1')
add('<path d="M860 1078 C860 1032 330 1032 330 1072" class="dyn-line" style="stroke:var(--dk11)" marker-end="url(#ah-dgMake)"/>')
text('trypsin makes more trypsin (positive feedback)', 595, 1032, 'nf-l2', 'middle')
# already active
add('<rect x="180" y="1650" width="820" height="110" rx="14" style="fill:var(--dk5);fill-opacity:.1;stroke:var(--dk5);stroke-width:2"/>')
text('secreted already active — no trypsin needed', 200, 1684, 'nf-l1')
text('α-amylase · lipase · cholesterol ester hydrolase · nucleases', 200, 1714)
text('(colipase, which lipase needs, does wait for trypsin)', 200, 1742)
text('inside the gland: SPINK1 traps early trypsin; trypsin can also destroy itself (CTRC)', 180, 1810)
text('in the stomach: pepsinogen → pepsin by acid, not by trypsin', 180, 1846)
HL(160, 1066, 1020, 1134, O('ent', 'tryp'))
HL(160, 1190, 1020, 1340, O('chy'))
HL(160, 1376, 1020, 1424, O('cpb'))
HL(160, 1466, 1020, 1514, O('pla2'))
HL(160, 1556, 1020, 1604, O('lip'))
HL(160, 1636, 1020, 1774, O('pamy', 'lip', 'nuc'))
HL(160, 1786, 1020, 1826, O('spink'))
HL(160, 1822, 1020, 1862, O('pep'))
HL(584, 1140, 616, 1596, O('tryp'))

# ════════ C. what each enzyme cuts ════════
add('<rect x="1100" y="930" width="1240" height="970" rx="24" class="dyn-soft"/>')
text('What each enzyme cuts', 1130, 972, 'dyn-big')
def box(x0, x1, y, t, col):
    add(f'<rect x="{x0}" y="{y - 20}" width="{x1 - x0}" height="40" rx="12" style="fill:var({col});fill-opacity:.14;stroke:var({col});stroke-width:3"/>')
    text(t, (x0 + x1) // 2, y + 5, 'nf-l2', 'middle')
def arrow(x0, x1, y, lab, sub=None):
    add(f'<path d="M{x0} {y} L{x1 - 6} {y}" class="dyn-line" marker-end="url(#ah-dgMake)"/>')
    text(lab, (x0 + x1) // 2, y - 10, 'nf-l1', 'middle')
    if sub: text(sub, (x0 + x1) // 2, y + 22, 'nf-l2', 'middle')
CARB, PROT, LIPC, NUCC = '--dk1', '--dk3', '--dk10', '--dk8'
CUTS = {}                                     # option → [(x0, x1, y)] arrows its particles ride
text('Carbohydrate', 1130, 1018, 'nf-l1')
box(1140, 1300, 1060, 'starch · glycogen', CARB); arrow(1300, 1540, 1060, 'pancreatic α-amylase')
box(1540, 1830, 1060, 'α-limit dextrins · maltose · maltotriose', CARB); arrow(1830, 2090, 1060, 'α-dextrinase · maltase', 'sucrase (brush border)')
box(2090, 2300, 1060, 'glucose', CARB)
box(1140, 1300, 1140, 'lactose', CARB); arrow(1300, 1540, 1140, 'lactase', 'brush border')
box(1540, 1760, 1140, 'glucose + galactose', CARB)
text('Protein', 1130, 1220, 'nf-l1')
box(1140, 1300, 1260, 'protein', PROT); arrow(1300, 1540, 1260, 'pepsin', 'stomach')
box(1540, 1700, 1260, 'peptides', PROT); arrow(1700, 2060, 1260, 'trypsin · chymotrypsin · elastase', 'cut inside the chain')
box(2060, 2240, 1260, 'oligopeptides', PROT)
box(1140, 1300, 1350, 'peptides', PROT); arrow(1300, 1700, 1350, 'carboxypeptidases A · B', 'one at a time off the C-terminal end')
box(1700, 1880, 1350, 'amino acids', PROT)
box(1140, 1300, 1430, 'oligopeptides', PROT); arrow(1300, 1700, 1430, 'brush-border peptidases')
box(1700, 1980, 1430, 'amino acids · di- & tripeptides', PROT)
text('Lipid', 1130, 1510, 'nf-l1')
box(1140, 1300, 1550, 'triglyceride', LIPC); arrow(1300, 1700, 1550, 'lipase + colipase')
box(1700, 1980, 1550, '2-monoglyceride + 2 fatty acids', LIPC)
text('colipase moves bile salts aside', 2000, 1555, 'nf-l2', when=O('lip'))
box(1140, 1300, 1630, 'phospholipid (lecithin)', LIPC); arrow(1300, 1700, 1630, 'phospholipase A₂')
box(1700, 1980, 1630, 'lysolecithin + fatty acid', LIPC)
box(1140, 1300, 1710, 'cholesterol ester', LIPC); arrow(1300, 1700, 1710, 'cholesterol ester hydrolase')
box(1700, 1980, 1710, 'cholesterol + fatty acid', LIPC)
text('Nucleic acid', 1130, 1790, 'nf-l1')
box(1140, 1300, 1840, 'DNA · RNA', NUCC); arrow(1300, 1700, 1840, 'nucleases', 'DNase · RNase')
box(1700, 1920, 1840, 'mononucleotides', NUCC)
HL(1290, 1028, 1550, 1084, O('pamy'))
HL(1290, 1108, 1550, 1176, O('lact'))
HL(1290, 1228, 1550, 1296, O('pep'))
HL(1690, 1228, 2070, 1296, O('tryp', 'chy'))
HL(1290, 1318, 1710, 1386, O('cpb'))
HL(1290, 1520, 1710, 1574, O('lip'))
HL(1290, 1600, 1710, 1654, O('pla2'))
HL(1290, 1808, 1710, 1876, O('nuc'))

# ════════ kinds and motion ════════
kinds = {'carb': ['food', CARB, 'carbohydrate'], 'prot': ['food', PROT, 'protein'], 'lipd': ['food', LIPC, 'lipid'],
         'nucl': ['food', NUCC, 'nucleic acid'], 'zym': ['enz', '--ink-3', 'proenzyme (inactive)'],
         'enz': ['enz', '--dk5', 'active enzyme'], 'tryp': ['enz', '--dk11', 'trypsin'], 'h': ['acid', '--nf-h', 'H⁺ · acid']}
groups = [['food', 'food being cut'], ['enz', 'enzymes'], ['acid', 'acid']]

flows = []
def fl(pts_or_d, base, when=None, unless=None, mods=None, sp=110, r=7, ln=None):
    d = pts_or_d if isinstance(pts_or_d, str) else P(pts_or_d)
    f = dict(d=d, len=ln or plen(pts_or_d), speed=sp, r=r, base=base)
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
# chyme through the gut (always), heavier in the nutrient being cut
fl(DUO, dict(carb=1, prot=1, lipd=1), ln=2300, sp=150, mods=[
   dict(when=O('pamy', 'lact'), add=dict(carb=3)), dict(when=O('pep', 'tryp', 'chy', 'cpb'), add=dict(prot=3)),
   dict(when=O('lip', 'pla2'), add=dict(lipd=3)), dict(when=O('nuc'), add=dict(nucl=3))])
# pancreatic juice down the main duct: proenzymes + active enzymes
fl(MPD, dict(zym=2, enz=1), sp=80, mods=[dict(when=O('ent', 'tryp', 'chy', 'cpb', 'pla2', 'spink'), add=dict(zym=2)),
                                         dict(when=O('pamy', 'lip', 'nuc'), add=dict(enz=2))])
# stomach: acid and pepsin
fl([(600, 300), (580, 420), (520, 520), (420, 590), (340, 608)], dict(h=2), when=O('pep'), sp=70, mods=[dict(when=O('pep'), add=dict(enz=3))])
# acinar cell: granules out to the lumen and on to the duct
fl([(1066, 300), (1600, 300)], dict(zym=2, enz=1), sp=70, mods=[dict(when=O('spink', 'tryp', 'ent', 'chy', 'cpb', 'pla2'), add=dict(zym=2))])
# brush border: chyme over the microvilli
fl([(1660, 400), (2300, 400)], dict(carb=1, prot=1), sp=80, mods=[dict(when=O('lact', 'pamy'), add=dict(carb=2)),
                                                                     dict(when=O('ent'), add=dict(zym=3))])
# the cascade
fl([(ZX1, RY['tg']), (AX0, RY['tg'])], dict(tryp=2), when=O('ent', 'tryp'), sp=60, mods=[dict(when=O('ent'), add=dict(tryp=2))])
fl('M860 1078 C860 1032 330 1032 330 1072', dict(tryp=3), when=O('tryp'), sp=90, ln=600)
fl([(860, 1122), (860, 1152), (600, 1152), (600, RY['co'])], dict(tryp=4), when=O('tryp'), sp=90)
for k, opts in (('chy', O('tryp', 'chy')), ('el', O('tryp', 'chy')), ('cp', O('tryp', 'cpb')), ('pl', O('tryp', 'pla2')), ('co', O('tryp', 'lip'))):
    fl([(ZX1, RY[k]), (AX0, RY[k])], dict(enz=2), when=opts, sp=60)
# what each enzyme cuts: particles ride the arrow of the chosen enzyme
for (x0, x1, y), opts, kind in (((1300, 1540, 1060), O('pamy'), 'carb'), ((1830, 2090, 1060), O('pamy'), 'carb'),
                                ((1300, 1540, 1140), O('lact'), 'carb'), ((1300, 1540, 1260), O('pep'), 'prot'),
                                ((1700, 2060, 1260), O('tryp', 'chy'), 'prot'), ((1300, 1700, 1350), O('cpb'), 'prot'),
                                ((1300, 1700, 1430), O('pep', 'tryp', 'chy', 'cpb'), 'prot'),
                                ((1300, 1700, 1550), O('lip'), 'lipd'), ((1300, 1700, 1630), O('pla2'), 'lipd'),
                                ((1300, 1700, 1840), O('nuc'), 'nucl')):
    fl([(x0, y), (x1, y)], {kind: 4}, when=opts, sp=70)

# ════════ sites (tap targets) ════════
sites = [
  # stomach chief cells
  dict(x=430, y=560, n=[1, 0], w=10, t='rec', l='', aria='Chief cells — pepsinogen', ions=[['enz', 'out', 1]], c='gastricacid',
       boost=O('pep')),
  # acinar cell: exocytosis of zymogen granules
  dict(x=1300, y=350, n=[0, -1], w=12, t='rec', l='exocytosis', s='on CCK or vagal ACh', ions=[['zym', 'out', 2]],
       lx=1440, ly=262, la='middle', c='pancsec', boost=O('ent', 'tryp', 'chy', 'cpb', 'pla2', 'pamy', 'lip', 'nuc')),
  # brush border enzymes on the microvillus tips
  dict(x=1730, y=BBY, n=[0, -1], w=12, t='rec', l='enteropeptidase', s='trypsinogen → trypsin', ions=[['tryp', 'out', 1]],
       lx=1730, ly=286, la='middle', c='pancsec', boost=O('ent', 'tryp')),
  dict(x=1890, y=BBY, n=[0, -1], w=12, t='rec', l='lactase', s='lactose → glucose + galactose', ions=[['carb', 'out', 1]],
       lx=1890, ly=344, la='middle', c='lactose', boost=O('lact')),
  dict(x=2060, y=BBY, n=[0, -1], w=12, t='rec', l='sucrase · maltase · α-dextrinase', s='→ glucose', ions=[['carb', 'out', 1]],
       lx=2060, ly=286, la='middle', c='nutabsorb', boost=O('pamy')),
  dict(x=2230, y=BBY, n=[0, -1], w=12, t='rec', l='peptidases', s='oligopeptides → amino acids', ions=[['prot', 'out', 1]],
       lx=2210, ly=344, la='middle', c='nutabsorb', boost=O('tryp', 'chy', 'cpb')),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Starch digested', mods=[R(O('pamy'), 1)]),
  dict(l='Lactose digested', mods=[R(O('lact'), 1)]),
  dict(l='Protein digested', mods=[R(O('pep', 'tryp', 'chy', 'cpb'), 1)]),
  dict(l='Trypsin activity', mods=[R(O('ent', 'tryp'), 1), R(O('spink'), -1)]),
  dict(l='Lipid digested', mods=[R(O('lip', 'pla2'), 1)]),
  dict(l='Nucleic acids digested', mods=[R(O('nuc'), 1)]),
]

notes = {
  '': 'The pancreas packs its proteases into zymogen granules as inactive proenzymes and sends them, with α-amylase, lipase and '
      'nucleases (already active), down the duct to the duodenum. Pick an enzyme to see where it is made, what switches it on '
      'and what it cuts. ↑ more of that nutrient digested (or more trypsin), ↓ less, – not given.',
  'e:pamy': 'Pancreatic α-amylase is secreted already active. In the duodenum it cuts the interior α-1,4 bonds of starch and '
            'glycogen into α-limit dextrins, maltose and maltotriose; brush-border α-dextrinase, maltase and sucrase finish them '
            'to glucose. Salivary amylase starts in the mouth but gastric acid inactivates it.',
  'e:lact': 'Lactase is a brush-border enzyme, not a pancreatic one: it splits lactose into glucose and galactose for SGLT1. '
            'Without it (lactose intolerance) lactose stays in the lumen, holds water — osmotic diarrhea — and colonic bacteria '
            'ferment it to gas, so stool pH falls.',
  'e:pep': 'Chief cells secrete pepsinogen (vagal ACh, local acid); acid below pH 5 cleaves it to pepsin, an endopeptidase that '
           'starts protein digestion in the stomach. Pepsin is denatured once pancreatic HCO₃⁻ raises the duodenal pH — and it is '
           'not essential: after gastrectomy pancreatic and brush-border proteases digest protein normally.',
  'e:ent': 'Enteropeptidase (enterokinase) sits in the brush-border glycocalyx of the duodenum. It cuts a hexapeptide off '
           'trypsinogen to make the first trypsin — the trigger for every pancreatic protease, which is why they normally switch '
           'on only in the gut lumen, never in the pancreas.',
  'e:tryp': 'Trypsin is the master activator: it converts chymotrypsinogen, proelastase, procarboxypeptidases A and B, '
            'prophospholipase A₂, procolipase — and more trypsinogen (positive feedback) — and cuts proteins inside the chain. '
            'Trypsinogen activated inside the pancreas starts this cascade there: acute pancreatitis.',
  'e:chy': 'Chymotrypsin and elastase are endopeptidases like trypsin: they cut peptide bonds inside proteins, leaving '
           'oligopeptides. Both are secreted as zymogens (chymotrypsinogen, proelastase) and switched on by trypsin. Fecal '
           'elastase falls in pancreatic insufficiency.',
  'e:cpb': 'Carboxypeptidases A and B are exopeptidases: they remove single amino acids, one at a time, from the C-terminal end of '
           'peptides. Trypsin activates them from procarboxypeptidases A and B.',
  'e:lip': 'Pancreatic lipase is secreted active and splits triglyceride into 2-monoglyceride and two fatty acids. Bile salts would '
           'push it off the fat droplet, so colipase — cut from procolipase by trypsin — displaces them and binds lipase. No lipase '
           '(pancreatic insufficiency) → steatorrhea.',
  'e:pla2': 'Phospholipase A₂ is secreted as prophospholipase A₂ and activated by trypsin. It cleaves a fatty acid from '
            'phospholipids such as lecithin, leaving lysolecithin, which helps bile salts emulsify fat and is carried in micelles.',
  'e:nuc': 'Nucleases (deoxyribonuclease, ribonuclease) digest the DNA and RNA in chyme to mononucleotides. Like α-amylase and '
           'lipase they are secreted already active — they do not wait for trypsin.',
  'e:spink': 'SPINK1 (serine protease inhibitor Kazal type 1) is made by acinar and duct cells and packed into the zymogen granules. '
             'It inactivates up to 20% of any trypsin formed too early inside the gland; SPINK1 mutations predispose to '
             'pancreatitis, chronic and acute.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='e', label='Pick an enzyme', type='one', options=[
      ['pamy', 'Pancreatic amylase', 'pancsec'], ['lact', 'Lactase · brush-border disaccharidases', 'lactose'],
      ['pep', 'Pepsin · pepsinogen', 'gastricacid'], ['ent', 'Enteropeptidase · enterokinase', 'pancsec'],
      ['tryp', 'Trypsin · trypsinogen', 'pancsec'], ['chy', 'Chymotrypsin · elastase', 'pancsec'],
      ['cpb', 'Carboxypeptidases', 'pancsec'], ['lip', 'Pancreatic lipase · colipase', 'pancsec'],
      ['pla2', 'Phospholipase A₂ · lysolecithin', 'pancsec'], ['nuc', 'Nucleases', 'pancsec'],
      ['spink', 'SPINK1 · trypsin inhibitor', 'chronicpanc']],
      sections=[['Carbohydrate', ['pamy', 'lact']],
                ['Protein', ['pep', 'ent', 'tryp', 'chy', 'cpb']],
                ['Fat', ['lip', 'pla2']],
                ['Other & protection', ['nuc', 'spink']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI course lecture notes (SDL 3, 14, 19) · Costanzo ch 8 · Pawlina ch 18 · First Aid pp. 79, 379, 380, 388, 404')

MAP = dict(
  id='digestsim', title='Digestive Enzymes Step by Step in Motion', topic='gi', after='gutabs',
  sub='Pick an enzyme: see where it is made, what switches it on — enteropeptidase lights the trypsin cascade, trypsin wakes '
      'every other zymogen, SPINK1 guards the gland — and what it cuts in starch, lactose, protein, fat and nucleic acid. '
      'Tap an enzyme or pin for its card',
  w=3500, h=2160,
  fa='79, 379, 380, 388, 404', src=SRC,
  lanes=[('dgMake', 'Made & switched on', 'glycolysis'), ('dgDz', 'When it fails', 'tca')],
  comps=[],
  nodes=[
    ('dg1', 'Pancreatic secretions', 260, 1980, 'dgMake', 'zymogens · active enzymes', ['pancsec'], 'hub'),
    ('dg2', 'Pepsin & gastric acid', 720, 1980, 'dgMake', 'chief cells', ['gastricacid']),
    ('dg3', 'Brush border & absorption', 1180, 1980, 'dgMake', 'lactase · peptidases', ['nutabsorb']),
    ('dg4', 'CCK', 1620, 1980, 'dgMake', 'enzyme-rich juice', ['cck']),
    ('dg5', 'Secretin', 2020, 1980, 'dgMake', 'HCO₃⁻ stops pepsin', ['secretin']),
    ('dg6', 'Lactose intolerance', 260, 2080, 'dgDz', 'lactase', ['lactose']),
    ('dg7', 'Acute pancreatitis', 720, 2080, 'dgDz', 'trypsin in the gland', ['acutepanc']),
    ('dg8', 'Chronic pancreatitis', 1180, 2080, 'dgDz', 'SPINK1 · PRSS1', ['chronicpanc']),
    ('dg9', 'Pancreatic insufficiency', 1620, 2080, 'dgDz', 'steatorrhea', ['pancins']),
    ('dg10', 'Bile salts', 2020, 2080, 'dgMake', 'lipase needs colipase', ['bileacid']),
  ],
  panels=[
    (2420, 680, 1000, 'Secreted active or as zymogens (course notes SDL 14; Costanzo ch 8)', [
      ('Secreted active', 'α-amylase · lipase · cholesterol ester hydrolase · nucleases'),
      ('Secreted as zymogens', 'trypsinogen · chymotrypsinogen · proelastase · procarboxypeptidases'),
      ('Also woken by trypsin', 'prophospholipase A₂ · procolipase'),
      ('The first trypsin', 'enteropeptidase on the duodenal brush border'),
      ('In the stomach', 'pepsinogen → pepsin by acid below pH 5')]),
    (2420, 960, 1000, 'Why the pancreas does not digest itself (course notes SDL 14, 19; Costanzo ch 8)', [
      ('Zymogen granules', 'proteases stored inactive, sealed from the cytoplasm'),
      ('Activation far away', 'only in the duodenum, where enteropeptidase is'),
      ('SPINK1', 'inactivates up to 20% of trypsin formed too early'),
      ('Trypsin self-destruction', 'autolysis, helped by chymotrypsin C (CTRC)'),
      ('When it fails', 'trypsin activated in the gland → acute pancreatitis')]),
  ],
  dyn=dyn,
)
