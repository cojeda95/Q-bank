# m57 — GI Hormones & Paracrines in Motion (dynamic map, kit data)
# The upper gut drawn front-on (patient's right on the viewer's left): hypothalamus, liver + gallbladder, stomach (fundus,
# body, antrum, pylorus), the duodenal C-loop with the pancreas in it (acinus, duct, islet), jejunum → ileum → cecum and
# ascending colon. Each gut messenger sits in its own cell (G, D, ghrelin, S, I, K, M, L cells, an enteric VIP neuron).
# One `one` switch (`h`, in sections) releases one messenger: its cell lights up, the top caption names its trigger, and
# dots ride out to each target — green to what it stimulates, red to what it inhibits; the target sites read "more / less
# active". Seven readouts: gastric acid, gastric motility & emptying, pancreatic HCO3- (watery juice), pancreatic enzymes,
# gallbladder contraction, insulin, appetite.
#
# Sources (all read in the corpus; course text wins for this block):
#   Course lecture notes, GI Exam 1 (corpus/gastro/course_exam1_lecture_notes.txt): SDL 5 §1–2 (hormone / paracrine /
#     neurocrine; gastrin, CCK, secretin, GIP sites, stimuli, actions: CCK potentiates secretin's HCO3-, secretin ↓ acid,
#     ↓ gastrin, mildly ↓ motility, GIP ↓ acid, ↓ gastrin, slows motility), §3 ZES, §4 incretin effect (GIP + GLP-1),
#     §5 somatostatin on G cells, §6 appetite (orexigenic ghrelin; anorexigenic leptin, insulin, GLP-1, PYY, CCK, GIP;
#     arcuate → PVN satiety / lateral feeding; POMC/CART vs NPY/AGRP; MC4R); SDL 6 §4 hormonal feedback (CCK most potent
#     inhibitor of emptying + ↑ pyloric tone; GIP mild); SDL 7 §5 acid phases 30/60/10%; SDL 14 §3 pancreatic phases
#     20 / 5–10 / 70–80%, enzyme-rich low-volume cephalic + gastric juice; SDL 19 VIPoma (WDHA, pancreatic tail).
#   Costanzo ch 8 (course reading, course_sdl_4_7_physio p6–12, 19, 37–38): Tables 8.1–8.2 (VIP: relaxes smooth muscle,
#     ↑ intestinal + pancreatic secretion; CCK ↑ enzymes, ↑ HCO3-, GB, ↓ emptying; secretin ↑ HCO3-, ↓ H+; GIP ↑ insulin,
#     ↓ H+, ↓ emptying); motilin upper duodenum, fasting, MMC every 90 min; GLP-1 L cells distal ileum + colon, incretin,
#     ↓ glucagon, ↓ emptying, anorexigenic, analogs for T2DM + weight loss; somatostatin D cells, acid releases it, inhibits
#     all GI hormones + H+; p19 gastrin + motilin ↑ gastric contractions, secretin + GIP ↓; p12 leptin / ghrelin pathways.
#   Guyton ch 63 Table 63.1 + text (course_sdl_4_7_guyton_supplement p12–16): GLP-1 ↓ emptying, ↓ acid, ↓ food intake;
#     GIP ↓ food intake; CCK ↑ HCO3-, satiety via vagal afferents; secretin ↓ gastric emptying. Guyton ch 65 (supplement
#     p3, p20–27): phases of gastric and pancreatic secretion.
#   Pawlina ch 17 Table 17.1 + ch 18 Table 18.3 (course histology): ghrelin from Gr cells of the fundus epithelium,
#     ↑ appetite + GH; Mo cells of duodenum and jejunum.
#   First Aid 2025 p. 378 (sources, actions, regulation, notes for every messenger; somatostatin ↓ pancreatic fluid, GB,
#     insulin; VIP ↓ acid, WDHA; erythromycin on motilin receptors; ghrelin ↑ Prader-Willi, ↓ after bypass; octreotide
#     uses), p. 379–380 (acid regulation; gastrin acts mostly through ECL histamine), p. 340 (leptin, ghrelin), p. 357
#     (somatostatinoma, ZES + secretin stimulation test), p. 584 (anorexia: ↓ leptin → ↓ GnRH).
# Left as "–" (no source gives a direction): VIP on pancreatic HCO3-/enzymes (Costanzo: "↑ pancreatic secretion", not which
#   part); somatostatin on pancreatic enzymes; secretin on enzymes (Pawlina tables say ↑, the lecture says "little enzyme"
#   — flagged for the owner, no arrow); every unlisted cell.
# Source conflicts (course wins): gastrin is shut off by gastric pH below 3 (lecture) vs below 1.5 (First Aid 378) — the
#   note says "acid in the antrum"; satiety center = paraventricular nucleus (lecture, Costanzo) vs ventromedial nucleus
#   (First Aid 340) — the leptin card gives both; motilin site "small intestine" (FA) → "upper small intestine (duodenum,
#   jejunum)" per Costanzo / Guyton / Pawlina.
import sys
import math
import re
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

CZ8, GY63, GY65 = full('Costanzo', 8), full('Guyton', 63), full('Guyton', 65)
PW17, PW18 = full('Pawlina', 17), full('Pawlina', 18)
SRC = [CZ8, GY63, GY65, PW17, PW18]

O = lambda *k: ['h:' + x for x in k]

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

# ════════ 1. hypothalamus ════════
BRAIN = ('M260 330 C230 230 310 150 420 140 C500 125 590 130 650 170 C720 215 735 300 700 360 '
         'C680 400 640 420 600 425 C560 470 470 470 430 430 C360 440 280 410 260 330 Z')
add(f'<path d="{BRAIN}" class="dyn-cell" style="stroke:var(--dk4)"/>'
    '<path d="M330 250 C380 220 420 260 470 230 M500 200 C540 240 590 210 630 250" class="dyn-line" style="stroke-width:2;opacity:.45"/>')
add('<ellipse cx="520" cy="405" rx="42" ry="24" class="dyn-soft" style="stroke:var(--dk4)"/>')
text('Brain', 300, 200, 'dyn-big')

# ════════ 2. liver, gallbladder, bile duct ════════
add('<path d="M300 640 C320 560 700 545 1080 600 C1060 700 900 800 700 840 C520 870 340 860 300 780 Z" class="dyn-cell" style="stroke:var(--dk9)"/>'
    '<path d="M760 575 Q740 700 770 828" class="dyn-line" style="stroke-width:2;opacity:.6"/>')
text('Liver', 400, 690, 'dyn-big')
GB = 'M612 852 C560 900 570 995 640 1004 C712 1004 728 920 688 852 Z'
add(f'<path d="{GB}" class="dyn-cell" style="stroke:var(--dk6)"/><path d="{GB}" fill="var(--dk6)" opacity=".18"/>')
add('<path d="M672 858 C720 880 800 882 900 905" class="dyn-line" style="stroke:var(--dk6);stroke-width:5"/>'
    '<path d="M800 832 C860 860 920 880 925 960 V1320 L892 1336" class="dyn-line" style="stroke:var(--dk6);stroke-width:5"/>')
add(f'<g transform="translate(650 930) scale(.86) translate(-650 -930)"><path d="{GB}" class="dyn-hl"/></g>', when=O('cck'))

# ════════ 3. esophagus + stomach ════════
shapes.append(dict(tube='M1625 300 V548', w=38))
text('esophagus', 1660, 330, 'nf-l2')
STOM = ('M1592 552 C1600 500 1660 470 1740 470 C1860 470 1950 600 1950 800 C1950 1020 1790 1150 1580 1150 '
        'C1400 1150 1250 1100 1160 1052 L1160 958 C1300 950 1450 900 1520 800 C1570 720 1585 640 1592 552 Z')
add(f'<path d="{STOM}" class="dyn-cell" style="stroke:var(--dk5);stroke-width:5"/><path d="{STOM}" fill="var(--dk5)" opacity=".1"/>')
add('<rect x="1146" y="952" width="22" height="106" rx="6" style="fill:var(--dk7);opacity:.8"/>')
text('Stomach', 1700, 760, 'dyn-big')
text('fundus', 1850, 540, 'dyn-cap')
text('body', 1820, 800, 'dyn-cap')
text('antrum', 1500, 990, 'dyn-cap')
text('pylorus', 1157, 935, 'nf-l2', 'middle')

# ════════ 4. duodenum → jejunum → ileum → colon ════════
DUO = 'M1160 1005 H940 Q860 1005 860 1085 V1480 Q860 1580 960 1580 H1380 Q1460 1580 1480 1520'
JEJ = ('M1480 1520 C1500 1460 1700 1480 1760 1600 C1810 1720 1600 1800 1350 1800 C1100 1800 950 1860 750 1840 '
       'C600 1825 480 1850 420 1870')
shapes.append(dict(tube=DUO, w=54, color='--dk5'))
shapes.append(dict(tube=JEJ, w=46, color='--dk5'))
shapes.append(dict(tube='M380 1880 V1180 Q380 1110 460 1110 H560', w=74, color='--dk8'))
text('Duodenum', 760, 1040, 'dyn-big', 'end')
text('jejunum', 1800, 1500, 'nf-l2')
text('ileum', 1150, 1765, 'nf-l2')
text('Colon', 470, 1180, 'dyn-big')
text('cecum · ascending', 470, 1200, 'dyn-cap')

# ════════ 5. pancreas: acinus, duct, islet ════════
PANC = ('M945 1110 C1040 1085 1150 1135 1180 1255 C1350 1245 1700 1245 1900 1225 C2020 1213 2080 1255 2060 1302 '
        'C2040 1360 1900 1382 1700 1400 C1450 1420 1260 1440 1185 1500 C1125 1555 985 1550 955 1480 C935 1380 935 1200 945 1110 Z')
add(f'<path d="{PANC}" class="dyn-cell" style="stroke:var(--dk3)"/><path d="{PANC}" fill="var(--dk3)" opacity=".12"/>')
add('<path d="M2010 1295 C1700 1322 1300 1342 1100 1360 C1010 1368 950 1352 895 1340" class="dyn-line" style="stroke:var(--dk3);stroke-width:4"/>')
text('Pancreas', 2070, 1250, 'dyn-big')
text('duct → ampulla', 1000, 1395, 'dyn-cap')
add(''.join(f'<circle cx="{x}" cy="{y}" r="15" class="dyn-cell" style="stroke:var(--dk3)"/>'
            for x, y in ((1272, 1294), (1300, 1280), (1328, 1294), (1286, 1320), (1314, 1320))))   # an acinus
add('<circle cx="1715" cy="1322" r="44" class="dyn-soft" style="stroke:var(--dk2)"/>'
    '<circle cx="1735" cy="1312" r="12" style="fill:var(--dk2);opacity:.75"/><circle cx="1698" cy="1336" r="10" style="fill:var(--dk11);opacity:.85"/>')
text('islet: β cell (insulin) · δ cell (somatostatin)', 1715, 1440, 'nf-l2', 'middle')

# ════════ 6. the messenger cells ════════
CELLS = {   # key: (x, y, colour)
  'gas': (1420, 1112, '--dk1'), 'sst': (1272, 1078, '--dk11'), 'ghr': (1760, 505, '--dk7'),
  'sec': (842, 1120, '--dk10'), 'cck': (842, 1220, '--dk6'), 'gip': (842, 1320, '--dk2'), 'mot': (842, 1420, '--dk8'),
  'glp': (800, 1842, '--dk12'),
}
for k, (x, y, col) in CELLS.items():
    add(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="10" style="fill:var({col});stroke:var(--surface);stroke-width:2"/>')
    add(f'<circle cx="{x}" cy="{y}" r="30" class="dyn-hl"/>', when=O(k))
add('<circle cx="1715" cy="1322" r="56" class="dyn-hl"/>', when=O('sst'))
# the VIP neuron beside the jejunum
add('<circle cx="1900" cy="1640" r="16" class="dyn-cell" style="stroke:var(--dk9)"/>'
    '<path d="M1886 1648 C1850 1660 1820 1655 1792 1640" class="dyn-line" style="stroke:var(--dk9);stroke-width:4"/>')
add('<circle cx="1900" cy="1640" r="34" class="dyn-hl"/>', when=O('vip'))

# ════════ 7. what each messenger is and what releases it (top band) ════════
HEAD = {
  'gas': ('Gastrin — a GI hormone from G cells', 'released by peptides and amino acids, distention, vagal GRP · acid in the antrum stops it'),
  'sst': ('Somatostatin — a paracrine from D cells', 'released by acid · the vagus holds it back · acts on its neighbours'),
  'ghr': ('Ghrelin — from the stomach', 'rises with fasting and before meals · food lowers it'),
  'cck': ('CCK — a GI hormone from I cells', 'released by fatty acids, monoglycerides, peptides, amino acids'),
  'sec': ('Secretin — a GI hormone from S cells', 'released by acid chyme (duodenal pH below 4.5) and fatty acids'),
  'gip': ('GIP — a GI hormone from K cells', 'released by glucose, amino acids and fatty acids — all three nutrients'),
  'mot': ('Motilin — from M cells', 'released in the fasting state · food stops it'),
  'glp': ('GLP-1 — from L cells', 'released after carbohydrate, fat and protein'),
  'vip': ('VIP — a neurocrine from enteric neurons', 'released by distention and vagal stimulation'),
}
text('Release one messenger', 780, 160, 'dyn-big', unless=['h:*'])
text('green dots → what it stimulates · red dots → what it inhibits', 780, 184, 'dyn-cap', unless=['h:*'])
for k, (a, b) in HEAD.items():
    text(a, 780, 160, 'dyn-big', when=O(k))
    text(b, 780, 184, 'dyn-cap', when=O(k))
text('green dots → what it stimulates · red dots → what it inhibits', 780, 206, 'nf-l2', when=['h:*'])
text('migrating motor complex — a wave every ~90 min', 1810, 1690, TAG, when=O('mot'))
text('water and electrolytes into the gut · smooth muscle relaxes', 1940, 1600, TAG, when=O('vip'))

# ════════ 8. motion ════════
T = dict(acid=(1930, 860), pump=(1790, 1128), duct=(1520, 1334), acin=(1300, 1300), gb=(640, 940),
         beta=(1735, 1312), app=(540, 405), gcell=(1420, 1112), wall=(1790, 1640))
S = {k: (x, y) for k, (x, y, _) in CELLS.items()}
S['vip'] = (1900, 1640); S['dlt'] = (1698, 1336)
def curve(a, b, bend=0.18):
    (x0, y0), (x1, y1) = a, b
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0
    cx, cy = round(mx - dy * bend), round(my + dx * bend)
    return f'M{x0} {y0} Q{cx} {cy} {x1} {y1}'
EDGES = {
  'gas': [('acid', 'up'), ('pump', 'up')],
  'sst': [('acid', 'dn'), ('gcell', 'dn'), ('duct', 'dn'), ('gb', 'dn'), ('beta', 'dn', 'dlt')],
  'ghr': [('app', 'up')],
  'cck': [('gb', 'up'), ('acin', 'up'), ('duct', 'up'), ('pump', 'dn'), ('app', 'dn')],
  'sec': [('duct', 'up'), ('acid', 'dn'), ('gcell', 'dn'), ('pump', 'dn')],
  'gip': [('beta', 'up'), ('acid', 'dn'), ('gcell', 'dn'), ('pump', 'dn'), ('app', 'dn')],
  'mot': [('pump', 'up')],
  'glp': [('beta', 'up'), ('acid', 'dn'), ('pump', 'dn'), ('app', 'dn')],
  'vip': [('acid', 'dn'), ('wall', 'up')],
}
CHYME = ('M1625 310 V560 Q1700 820 1400 990 L1160 1005 H940 Q860 1005 860 1085 V1480 Q860 1580 960 1580 H1380 Q1460 1580 1480 1520 '
         + JEJ[JEJ.index('C'):])
flows = [dict(d=CHYME, len=plen(CHYME), speed=60, r=7, base=dict(chyme=8),
              mods=[dict(when=O('mot'), set=dict(chyme=4, up=4), speed=2.2)])]
for k, lst in EDGES.items():
    for e in lst:
        tgt, kind = e[0], e[1]
        src = S[e[2]] if len(e) > 2 else S[k]
        d = curve(src, T[tgt])
        add(f'<path d="{d}" class="dyn-dash" style="stroke:var({"--ok" if kind == "up" else "--bad"});opacity:.7"/>', when=O(k))
        n = plen(d)
        flows.append(dict(d=d, len=n, speed=150, r=7, when=O(k), base={kind: max(2, min(5, n // 220))}))

# ════════ 9. sites: the cells (tap → their card) and the targets ════════
ACID_UP, ACID_DN = O('gas'), O('sst', 'sec', 'gip', 'glp', 'vip')
MOT_UP, MOT_DN = O('gas', 'mot'), O('cck', 'sec', 'gip', 'glp')
SFX = dict(boost=' — releasing')
sites = [
  # targets
  dict(x=1938, y=860, n=[1, 0], w=14, t='rec', l='Parietal cell', s='acid (HCl)', ions=[], c='gastricacid',
       boost=ACID_UP, low=ACID_DN),
  dict(x=1790, y=1136, n=[0, 1], w=14, t='rec', l='Antral pump', s='gastric contractions, emptying', ions=[], c='motilin',
       lx=1815, ly=1180, la='start', boost=MOT_UP, low=MOT_DN),
  dict(x=1520, y=1334, n=[0, -1], w=14, t='rec', l='Duct cells', s='watery HCO₃⁻ juice', ions=[], c='pancsec',
       lx=1540, ly=1200, la='middle', boost=O('sec', 'cck'), low=O('sst')),
  dict(x=1300, y=1300, n=[0, -1], w=14, t='rec', l='Acinar cells', s='enzymes', ions=[], c='pancsec',
       lx=1300, ly=1200, la='middle', boost=O('cck')),
  dict(x=612, y=940, n=[-1, 0], w=14, t='rec', l='Gallbladder', s='contracts → bile out', ions=[], c='cck',
       lx=560, ly=940, la='end', boost=O('cck'), low=O('sst')),
  dict(x=1748, y=1312, n=[1, 0], w=12, t='rec', l='', aria='β cell — insulin', ions=[], c='insulinsecr',
       boost=O('gip', 'glp'), low=O('sst')),
  dict(x=540, y=405, n=[0, 1], w=14, t='rec', l='Hypothalamus — appetite', s='arcuate nucleus → PVN (satiety), lateral (feeding)', ions=[], c='hypothalnuc',
       lx=540, ly=348, la='middle', boost=O('ghr'), low=O('cck', 'gip', 'glp')),
  # the messenger cells
  dict(x=1420, y=1112, n=[0, -1], w=10, t='ex', l='G cells', s='gastrin', ions=[], c='gastrin', lx=1420, ly=1048, la='middle',
       boost=O('gas'), low=O('sst', 'sec', 'gip'), sfx=SFX),
  dict(x=1272, y=1078, n=[0, -1], w=10, t='ex', l='D cells', s='somatostatin', ions=[], c='sstgi', lx=1272, ly=1020, la='middle',
       boost=O('sst'), sfx=SFX),
  dict(x=1760, y=505, n=[0, 1], w=10, t='ex', l='Ghrelin cells', s='fundus', ions=[], c='ghrelin', lx=1700, ly=580, la='middle',
       boost=O('ghr'), sfx=SFX),
  dict(x=842, y=1120, n=[-1, 0], w=10, t='ex', l='S cells', s='secretin', ions=[], c='secretin', lx=800, ly=1116, la='end', boost=O('sec'), sfx=SFX),
  dict(x=842, y=1220, n=[-1, 0], w=10, t='ex', l='I cells', s='CCK', ions=[], c='cck', lx=800, ly=1216, la='end', boost=O('cck'), sfx=SFX),
  dict(x=842, y=1320, n=[-1, 0], w=10, t='ex', l='K cells', s='GIP', ions=[], c='gip', lx=800, ly=1316, la='end', boost=O('gip'), sfx=SFX),
  dict(x=842, y=1420, n=[-1, 0], w=10, t='ex', l='M cells', s='motilin', ions=[], c='motilin', lx=800, ly=1416, la='end', boost=O('mot'), sfx=SFX),
  dict(x=800, y=1842, n=[0, 1], w=10, t='ex', l='L cells', s='GLP-1 · ileum and colon', ions=[], c='glp1ra', lx=800, ly=1900, la='middle',
       boost=O('glp'), sfx=SFX),
  dict(x=1900, y=1640, n=[1, 0], w=10, t='ex', l='Enteric neuron', s='VIP', ions=[], c='vip', lx=1940, ly=1650, la='start',
       boost=O('vip'), sfx=SFX),
]

notes = {
  '': 'Gut messengers come in three kinds: hormones (gastrin, CCK, secretin, GIP) ride the blood, the paracrine somatostatin '
      'diffuses to its neighbours, and the neurocrine VIP is released from enteric neurons. Release one and follow the dots — '
      'green to what it stimulates, red to what it inhibits — then read the seven arrows.',
  'h:gas': 'Gastrin (G cells of the antrum) answers peptides and amino acids, distention and vagal GRP, and acid in the antrum turns '
           'it off. It raises acid — directly and, mostly, by making ECL cells release histamine — speeds gastric motility and makes '
           'the mucosa grow; a gastrinoma (Zollinger-Ellison) gives refractory ulcers and thick gastric folds.',
  'h:sst': 'Somatostatin, from D cells of the antrum, gut mucosa and islets, is released by acid and acts locally as the brake: less '
           'gastric acid and gastrin, less pancreatic fluid, a quiet gallbladder, less insulin and glucagon. Its analog octreotide '
           'treats acromegaly, carcinoid syndrome, VIPoma and variceal bleeding.',
  'h:ghr': 'Ghrelin, from the gastric fundus, rises with fasting and just before meals and acts on the arcuate nucleus (NPY/AgRP '
           'neurons) to raise hunger; it also releases GH. It is high in Prader-Willi syndrome and low after gastric bypass.',
  'h:cck': 'CCK (I cells of the duodenum and jejunum) answers fat and protein products. It contracts the gallbladder and relaxes '
           'the sphincter of Oddi, drives pancreatic enzymes and boosts secretin’s bicarbonate, and is the strongest hormonal brake on '
           'gastric emptying (it raises pyloric tone) — while it signals satiety.',
  'h:sec': 'Secretin (S cells of the duodenum) is released when acid chyme drops duodenal pH below 4.5. Duct cells answer with a '
           'copious, watery bicarbonate juice (bile adds more) while acid secretion, gastrin release and gastric motility slow until '
           'the acid is neutralized. In a gastrinoma secretin raises gastrin instead — the secretin stimulation test.',
  'h:gip': 'GIP (K cells of the duodenum, jejunum and ileum) is the only gut hormone released by all three nutrients. It is an incretin: '
           'oral glucose releases more insulin than the same glucose IV, through GIP (and GLP-1). It also inhibits acid and gastrin, '
           'mildly slows gastric emptying and is anorexigenic.',
  'h:mot': 'Motilin (M cells of the upper small intestine) is released in the fasting state and drives the migrating motor '
           'complexes — waves about every 90 minutes that sweep leftovers from the stomach through the small intestine; eating stops '
           'them. Erythromycin works on motilin receptors to stimulate motility.',
  'h:glp': 'GLP-1 (L cells, mostly ileum and colon) is an incretin: it raises insulin only when glucose is high, lowers glucagon, '
           'slows gastric emptying and acid secretion, and cuts appetite — the reason GLP-1 analogs treat type 2 diabetes and help '
           'weight loss.',
  'h:vip': 'VIP is a neurocrine: enteric neurons release it to pour water and electrolytes into the intestine, relax intestinal '
           'smooth muscle and sphincters (with nitric oxide — lost in achalasia) and lower acid. A VIPoma, usually in the pancreatic '
           'tail, gives WDHA: watery diarrhea, hypokalemia, achlorhydria.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Gastric acid', mods=[R(ACID_UP, 1), R(ACID_DN, -1)]),
  dict(l='Gastric motility & emptying', mods=[R(MOT_UP, 1), R(MOT_DN, -1)]),
  dict(l='Pancreatic HCO₃⁻ (watery juice)', mods=[R(O('sec', 'cck'), 1), R(O('sst'), -1)]),
  dict(l='Pancreatic enzymes', mods=[R(O('cck'), 1)]),
  dict(l='Gallbladder contraction', mods=[R(O('cck'), 1), R(O('sst'), -1)]),
  dict(l='Insulin release', mods=[R(O('gip', 'glp'), 1), R(O('sst'), -1)]),
  dict(l='Appetite', mods=[R(O('ghr'), 1), R(O('cck', 'gip', 'glp'), -1)]),
]

dyn = dict(
  kinds=dict(chyme=['chyme', '--dk10'], up=['up', '--ok'], dn=['dn', '--bad']),
  groups=[['chyme', 'Chyme'], ['up', 'Stimulates'], ['dn', 'Inhibits']],
  switches=[dict(id='h', label='Release one messenger', type='one', options=[
      ['gas', 'Gastrin (G cells)', 'gastrin'], ['sst', 'Somatostatin (D cells)', 'sstgi'], ['ghr', 'Ghrelin', 'ghrelin'],
      ['cck', 'CCK (I cells)', 'cck'], ['sec', 'Secretin (S cells)', 'secretin'], ['gip', 'GIP (K cells)', 'gip'],
      ['mot', 'Motilin (M cells)', 'motilin'], ['glp', 'GLP-1 (L cells)', 'glp1ra'], ['vip', 'VIP (enteric neurons)', 'vip']],
      sections=[['Stomach', ['gas', 'sst', 'ghr']], ['Duodenum & jejunum', ['cck', 'sec', 'gip', 'mot']],
                ['Ileum & colon', ['glp']], ['Neurocrine', ['vip']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Course lecture notes, GI Exam 1 (SDL 5–7, 14, 19) · Costanzo ch 8 · Guyton ch 63, 65 · Pawlina ch 17–18 · '
      'First Aid pp. 340, 357, 378–380')

# ════════ new cards ════════
card('leptin', 'Leptin', 'reg', 'gxApp', 'Adipocytes — tells the hypothalamus how much fat is stored', 1,
     'Leptin is secreted by <b>adipocytes in proportion to body fat</b>. In the <b>arcuate nucleus</b> it activates anorexigenic '
     '<b>POMC/CART</b> neurons (POMC → α-MSH → MC4R in the paraventricular nucleus) and inhibits orexigenic <b>NPY/AgRP</b> neurons, '
     'so appetite falls and energy expenditure rises — a long-term signal of stored fat.',
     ['<b>Leptin gene mutation</b> → no leptin → severe obesity',
      'Common obesity: leptin is <b>high</b> (more fat), but the brain is resistant to it',
      'Starvation and sleep deprivation → ↓ leptin; in anorexia nervosa low leptin → ↓ GnRH → amenorrhea',
      'Satiety center: the paraventricular nucleus in the course and Costanzo; First Aid names the ventromedial hypothalamus',
      '<b>Ghrelin</b> (stomach) is the opposite signal: it drives NPY/AgRP neurons → hunger'],
     ['—'],
     ['Leptin from fat keeps you thin'],
     [CZ8],
     ['—'],
     ['leptin'],
     fa='340, 584')

card('digphases', 'Cephalic, gastric & intestinal phases of secretion', 'reg', 'gxStom',
     'Gastric acid and pancreatic juice — before, during and after a meal reaches the gut', 1,
     'Gastric acid and pancreatic juice are both secreted in three phases: <b>cephalic</b> (sight, smell, taste, chewing, '
     'thought of food — all through the vagus), <b>gastric</b> (food distends the stomach; peptides and amino acids) and '
     '<b>intestinal</b> (chyme in the duodenum).',
     ['<b>Acid</b>: cephalic ~30% (vagal ACh on parietal cells + vagal GRP → gastrin) · <b>gastric ~60%</b> (distention via '
      'vagovagal and local reflexes, peptides on G cells) · intestinal ~10% (duodenal gastrin, absorbed amino acids)',
      '<b>Pancreas</b>: cephalic ~20% and gastric 5–10% of the enzymes — vagal ACh on acinar cells gives an enzyme-rich, '
      '<b>low-volume</b> juice that stays mostly in the ducts',
      'Pancreatic <b>intestinal phase ~70–80%</b>: secretin (acid, pH below 4.5) → copious watery HCO₃⁻; CCK (fatty acids, '
      'amino acids) → enzymes; vagovagal ACh potentiates both'],
     ['—'],
     ['Gastric phase makes most of the acid; intestinal phase most of the pancreatic juice'],
     [CZ8, GY65],
     ['—'],
     ['cephalic phase', 'gastric phase', 'intestinal phase', 'cephalic response'])

NY1, NY2 = 1990, 2075
MAP = dict(
  id='gihormsim', title='GI Hormones & Paracrines in Motion', topic='gi', after='gihorm',
  sub='Release one gut messenger — gastrin, somatostatin, ghrelin, CCK, secretin, GIP, motilin, GLP-1 or VIP — and watch it leave '
      'its cell for each target: acid, the antral pump, pancreatic ducts and acini, the gallbladder, the β cell and the '
      'hypothalamus. Tap a cell or a target for its card',
  w=3500, h=2140,
  fa='340, 357, 378–380, 584', src=SRC,
  lanes=[('gxStom', 'Stomach', 'tca'), ('gxGut', 'Small intestine & colon', 'glycolysis'), ('gxPanc', 'Pancreas & targets', 'gluconeo'),
         ('gxApp', 'Appetite', 'ppp')],
  comps=[],
  nodes=[
    ('gn1', 'Gastrin · G cells', 300, NY1, 'gxStom', 'acid · mucosal growth · gastrinoma', ['gastrin', 'zes'], 'hub'),
    ('gn2', 'Somatostatin · D cells', 690, NY1, 'gxStom', 'the brake · somatostatinoma', ['sstgi', 'somatostatinoma']),
    ('gn3', 'Parietal cell · acid', 1080, NY1, 'gxStom', 'ACh, histamine, gastrin', ['gastricacid']),
    ('gn4', 'Phases of secretion', 1470, NY1, 'gxStom', 'cephalic · gastric · intestinal', ['digphases']),
    ('gn5', 'Ghrelin & leptin', 1860, NY1, 'gxApp', 'hunger vs satiety', ['ghrelin', 'leptin', 'hypothalnuc']),
    ('gn6', 'CCK · I cells', 300, NY2, 'gxGut', 'bile, enzymes, slow emptying', ['cck']),
    ('gn7', 'Secretin · S cells', 690, NY2, 'gxGut', 'bicarbonate', ['secretin']),
    ('gn8', 'GIP · K cells', 1080, NY2, 'gxGut', 'incretin', ['gip', 'insulinsecr']),
    ('gn9', 'Motilin · M cells', 1470, NY2, 'gxGut', 'migrating motor complex', ['motilin']),
    ('gn10', 'GLP-1 · L cells', 1860, NY2, 'gxGut', 'incretin · satiety', ['glp1ra']),
    ('gn11', 'Pancreatic juice', 2250, NY1, 'gxPanc', 'ducts · acini', ['pancsec']),
    ('gn12', 'VIP · enteric neurons', 2250, NY2, 'gxGut', 'WDHA · VIPoma', ['vip', 'vipoma', 'ansreg']),
  ],
  panels=[
    (2420, 1180, 1000, 'Where each is made, what releases it (lecture SDL 5 · First Aid p. 378)', [
      ('Gastrin · G cells', 'antrum — peptides, distention, vagal GRP'),
      ('Somatostatin · D cells', 'gut mucosa, islets — acid'),
      ('CCK · I cells', 'duodenum, jejunum — fatty acids, amino acids'),
      ('Secretin · S cells', 'duodenum — acid (pH below 4.5), fatty acids'),
      ('GIP · K cells', 'duodenum, jejunum, ileum — glucose, amino acids, fat'),
      ('Motilin · M cells', 'upper small intestine — fasting'),
      ('GLP-1 · L cells', 'ileum, colon — carbohydrate, fat, protein'),
      ('Ghrelin', 'gastric fundus — fasting; food lowers it')]),
    (2420, 1520, 1000, 'Hormone, paracrine or neurocrine? (lecture SDL 5 · Costanzo ch 8)', [
      ('Hormones', 'gastrin, CCK, secretin, GIP — portal blood → liver → systemic'),
      ('Paracrines', 'somatostatin, histamine — diffuse to neighbouring cells'),
      ('Neurocrines', 'VIP, NO, GRP, ACh, substance P — from enteric neurons'),
      ('Candidates', 'motilin, ghrelin, GLP-1, PYY — meet some criteria')]),
  ],
  dyn=dyn,
)
