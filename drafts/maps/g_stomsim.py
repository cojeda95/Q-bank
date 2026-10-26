# m58 — Gastric Polyps, Gastropathy & Ulcer Complications in Motion (dynamic map, kit data)
# Left: a front view (patient's right on your left) of the stomach under the diaphragm, with the liver, the duodenal C-loop,
# the pancreas, the left gastric artery on the lesser curvature and the gastroduodenal artery behind the duodenal bulb. Chyme
# rides from the esophagus through the pylorus into the duodenum; acid comes off the body and fundus. Right: the gastric wall
# zoomed in (mucosa with pits and glands, muscularis mucosae, submucosa, muscularis propria, serosa).
# One `one` switch (sections: gastropathy · polyps & tumors · ulcer complications) draws each lesion where it sits, on the
# stomach and in the wall: reactive gastropathy (bile refluxing), Ménétrier disease (giant folds, albumin leaking), fundic
# gland / hyperplastic polyps and the adenoma, GIST in the muscularis propria, gastric NET nodules in the submucosa, and the
# four ulcer complications (bleeding from the left gastric or gastroduodenal artery, perforation with free air under the
# diaphragm, penetration into the pancreas, gastric outlet obstruction with food held back). 7 readouts.
# Not repeated: acidflow (H. pylori, autoimmune gastritis, Cushing ulcer, gastric vs duodenal ulcer — the parietal cell),
# gitumsim (gastric adenocarcinoma, MALT, colonic polyps), sxgibleed (peptic ulcer as a work-up answer).
#
# Sources (all read in the corpus; the course text wins):
#   GI Exam 1 lecture notes (corpus/gastro/course_exam1_lecture_notes.txt), SDL 9:
#     p. 46 (acute/reactive gastropathy: NSAIDs, alcohol, bile reflux, stress/ischemia, chemical irritants; COX inhibition,
#       direct cytotoxicity, ↓ mucosal blood flow; body and antrum; edema, congestion, erosions, foveolar hyperplasia with
#       corkscrew profiles, "notable paucity or absence of neutrophils"; erosion, ulceration, hematemesis, melena)
#     p. 47–48 (defenses: mucus–bicarbonate gel, tight junctions, blood flow, restitution, PGE₂; PUD complications —
#       hemorrhage (melena, hematemesis), perforation into the peritoneal cavity with free air, penetration into adjacent
#       structures (e.g., pancreas), gastric outlet obstruction from edema or fibrous scarring, intractable pain)
#     p. 49–50 (hyperplastic polyps up to 75%, < 1 cm, antrum, chronic H. pylori gastritis, corkscrew foveolar glands in an
#       inflamed lamina propria, dysplasia 1–20% rising > 1 cm pedunculated; fundic gland polyps: APC (FAP) or MUTYH, sporadic
#       ↑ with PPIs (acid inhibition → gastrin → oxyntic gland growth), body/fundus, cystic glands lined by parietal, chief and
#       foveolar cells, minimal inflammation, sporadic/PPI no significant malignant risk, FAP ones can become dysplastic;
#       adenomas up to 10%, atrophic gastritis + intestinal metaplasia, solitary antral, dysplasia, men 50–60, up to 30%
#       cancer when > 2 cm, complete resection)
#     p. 52–53 (gastric NETs from ECL-type cells, hypergastrinemia from autoimmune atrophic gastritis or ZES (MEN1),
#       synaptophysin/chromogranin A, submucosal yellow-tan nodules in oxyntic mucosa, salt-and-pepper chromatin, small
#       ones on autoimmune gastritis indolent; GIST: commonest abdominal mesenchymal tumor, interstitial cells of Cajal,
#       KIT ~75% / PDGFRA ~8%, CD117 and DOG1 95%, submucosal/intramural mass with frequent mucosal ulceration, upper GI
#       bleeding/anemia, resection, imatinib for unresectable/metastatic)
#     p. 54 (PPIs: long-term risk of benign fundic gland polyps).
#   Robbins ch 17 in the course text (course_sdl_8_9_patho.txt): p. 36–38 (gastropathy when inflammatory cells are rare or
#     absent; NSAIDs, alcohol, bile; neutrophils contacting epithelium are abnormal anywhere in the GI tract); p. 52–55
#     (gastric ulcers on the lesser curvature, duodenal ulcers near the pylorus; perforation = free air under the diaphragm;
#     thickened vessels in the scarred base bleed; penetrating ulcers refer pain to the back; Table 17.4: bleeding 15–20%,
#     commonest, 25% of ulcer deaths; perforation up to 5%, two-thirds of ulcer deaths; obstruction ~2%, edema or scarring,
#     pyloric channel, intractable vomiting); p. 56–59 (Ménétrier: TGF-α → EGFR, foveolar hyperplasia of body and fundus,
#     antrum spared, parietal and chief cell hypoplasia, albumin loss, edema, ↑ adenocarcinoma risk in adults); p. 61–62
#     (polyps, same facts as the notes); p. 72–75 (NETs: gastric ones in oxyntic mucosa, rarely metastasize; GIST > half in
#     the stomach, Cajal cells, KIT/PDGFRA, whorled cut surface, ulcerated mucosa, CD117).
#   First Aid 2025 p. 386 (NSAIDs ↓ PGE₂; Ménétrier: hypertrophied rugae, excess mucus, protein loss, parietal cell atrophy
#     with ↓ acid, precancerous, WAVEE: weight loss, anorexia, vomiting, epigastric pain, edema; GIST KIT or PDGFRA) · p. 387
#     (hemorrhage commonest: lesser-curvature gastric ulcer → left gastric artery, posterior duodenal → gastroduodenal artery;
#     obstruction: pyloric channel, duodenal; perforation: anterior duodenal → free air under the diaphragm, shoulder pain via
#     the phrenic nerve).
#   Bootcamp.com Gastroenterology — Stomach (Ménétrier: TGF-α/EGFR, protein-losing gastropathy → hypoalbuminemia, edema;
#     ulcer hemorrhage: hematemesis, melena, shock; perforation: anterior ulcer → pneumoperitoneum; gastric outlet
#     obstruction: pylorus or proximal duodenum, PUD or malignancy, postprandial nonbilious emesis, early satiety, weight loss,
#     succussion splash; GIST: older age, mostly stomach, c-KIT/PDGFRA).
# Readouts and where each arrow comes from:
#   Gastric acid ↓ Ménétrier (FA 386, Robbins: parietal cell atrophy). Serum albumin ↓ Ménétrier (Robbins, Bootcamp).
#   Mucosal neutrophils ↔ reactive gastropathy (notes "paucity or absence"; Robbins: any neutrophil touching the epithelium
#     is abnormal, so "few or none" = not raised) and fundic gland polyp (inflammation absent or minimal).
#   Cancer risk ↑ Ménétrier (FA "precancerous", Robbins adults) and adenoma (up to 30% > 2 cm); ↔ fundic gland polyp (sporadic/PPI:
#     no significant risk — the polyp shown is the PPI one).
#   Free air ↑ perforation. GI bleeding ↑ ulcer bleeding. Vomiting ↑ outlet obstruction (Robbins, Bootcamp) and Ménétrier (FA WAVEE).
# Arrows deliberately left "–": hyperplastic polyp cancer risk (sources give a dysplasia risk of 1–20%, not a cancer risk);
#   GIST and NET cancer risk (they are the tumors; behavior depends on size, site, mitoses); GIST bleeding (one possible
#   presentation, not a rule); neutrophils in ulcers; acid with the NET (hypergastrinemia from achlorhydria OR from ZES);
#   penetration lipase (the question says it; no source in the corpus does).
# Spec change: the spec's "Neutrophils ↓ (few or none)" for reactive gastropathy is printed as ↔ (normal mucosa has none);
#   the spec's "Cancer risk ↓ (negligible)" for the fundic gland polyp is printed as ↔ (no significant risk is not a
#   lowered risk). "Protein loss ↑" is printed as "Serum albumin ↓" (same fact as a lab).
# Source conflict (owner): lecture notes p. 52 list long-term PPI therapy as a cause of gastric NETs; Robbins (same course
#   text) says the progression risk of PPI-linked ECL hyperplasia is negligible. The map names only autoimmune gastritis
#   and ZES/MEN1 for the NET.
# Cut: GAVE and Dieulafoy lesion (Robbins only), Carney triad / Carney-Stratakis, gastritis cystica, penetration pain to the
#   LUQ or chest (Robbins "occasionally"), intractable pain as a complication (not drawable), "undigested food" in outlet
#   obstruction (the question's wording; not in a source).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

RB17 = full('Robbins', 17)
BC = 'Bootcamp.com Gastroenterology — Stomach'
SRC = [RB17, BC]

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

SW = 's'
O = lambda *k: [f'{SW}:{x}' for x in k]
TAG = 'nf-l1 dyn-tag'
POL = 'fill:var(--dk4);fill-opacity:.4;stroke:var(--dk4);stroke-width:3'        # a polyp
LES = 'fill:var(--dk4);fill-opacity:.35;stroke:var(--bad);stroke-width:4'        # a tumor
ULC = 'fill:var(--dyn-lost);stroke:var(--bad);stroke-width:4'                     # an ulcer crater (stays dark)
WALLHOLE = 'fill:var(--surface);stroke:var(--bad);stroke-width:3'                # the crater cut into the zoomed wall
ULCERS = O('bleed', 'perf', 'pen')
POLYPS = O('fgp', 'hpp', 'gad')

text('The stomach — where each lesion sits, and what it does', 180, 150, 'dyn-big')
text('front view, patient’s right on your left · grey dots = chyme · red = acid · dark red = blood · the right box zooms into the wall', 180, 176, 'dyn-cap')

# ════════ the stomach and its neighbors ════════
add('<path d="M170 300 C400 200 1000 200 1290 300" style="fill:none;stroke:var(--ink-3);stroke-width:5;opacity:.6"/>')
text('diaphragm', 1290, 326, 'nf-l2', 'end')
LIVER = 'M190 320 C350 270 600 270 760 330 C700 420 560 520 420 600 C320 650 220 640 190 560 Z'
add(f'<path d="{LIVER}" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:3;opacity:.8"/>'
    '<path d="M560 290 C540 380 520 450 470 560" style="fill:none;stroke:var(--dk2);stroke-width:2;opacity:.4"/>')
text('liver', 340, 450, 'dyn-big', 'middle')
# free air under the diaphragm (perforation)
add('<path d="M205 292 C380 222 600 214 760 266 L752 300 C600 262 380 268 205 322 Z" '
    'style="fill:var(--ink-3);fill-opacity:.28;stroke:var(--ink-3);stroke-width:2;stroke-dasharray:8 6"/>', when=O('perf'))
text('free air', 470, 270, 'nf-l1', 'middle', when=O('perf'))

ESO = 'M790 222 V428'
shapes.append(dict(tube=ESO, w=26, color='--dk10'))
text('esophagus', 812, 270, 'nf-l2')
STOM = ('M800 420 C840 330 1010 320 1080 420 C1160 540 1180 800 1110 980 C1040 1150 820 1180 680 1120 '
        'C600 1090 545 1050 520 1022 L520 958 C580 975 660 990 740 955 C830 905 790 700 772 560 C766 500 762 460 776 420 Z')
add(f'<path d="{STOM}" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:4"/>')
add(f'<path d="{STOM}" style="fill:none;stroke:var(--bad);stroke-width:18;stroke-opacity:.3"/>', when=O('react'))
text('fundus', 950, 404, 'nf-l1', 'middle')
text('body', 1040, 700, 'nf-l1', 'middle')
text('antrum', 840, 1080, 'nf-l1', 'middle')
text('greater curvature', 1192, 860, 'nf-l2')
text('lesser curvature', 735, 830, 'nf-l2', 'end')
text('pylorus', 548, 938, 'nf-l2')
# pylorus: a ring, scarred tight in outlet obstruction
add('<path d="M520 950 V968 M520 1012 V1030" style="stroke:var(--dk7);stroke-width:16"/>', unless=O('goo'))
add('<path d="M520 944 V984 M520 996 V1036" style="stroke:var(--ink-3);stroke-width:24"/>', when=O('goo'))

DUO = 'M522 990 C440 990 380 1000 352 1060 C322 1150 332 1290 400 1350 C470 1410 640 1420 780 1380'
shapes.append(dict(tube=DUO, w=30, color='--dk10'))
text('duodenum', 330, 1200, 'nf-l1', 'end')
PANC = ('M410 1110 C450 1080 520 1100 560 1150 C640 1185 800 1180 960 1180 C1080 1180 1180 1188 1222 1214 '
        'C1236 1246 1196 1262 1150 1258 C1000 1254 800 1262 640 1272 C570 1300 520 1330 460 1320 C400 1306 384 1180 410 1110 Z')
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.16;stroke:var(--dk5);stroke-width:3"/>', unless=O('pen'))
add(f'<path d="{PANC}" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--bad);stroke-width:5"/>', when=O('pen'))
text('pancreas', 1000, 1228, 'nf-l2', 'middle')

# arteries: left gastric on the lesser curvature, gastroduodenal behind the duodenal bulb
LGA, GDA = 'M752 470 C768 620 776 780 724 920', 'M470 880 V1110'
shapes.append(dict(vessel=LGA, w=7, color='--nf-blood'))
shapes.append(dict(vessel=GDA, w=7, color='--nf-blood'))
add(f'<path d="{LGA}" style="fill:none;stroke:var(--bad);stroke-width:16;stroke-opacity:.35"/>'
    f'<path d="{GDA}" style="fill:none;stroke:var(--bad);stroke-width:16;stroke-opacity:.35"/>', when=O('bleed'))
text('left gastric a.', 740, 640, 'nf-l2', 'end')
text('gastroduodenal a.', 458, 872, 'nf-l2', 'end')

# ── lesions on the stomach ──
# Ménétrier: giant folds in the body and fundus, antrum spared
add(''.join(f'<path d="M{x} {y0} q22 38 0 76 q-22 38 0 76 q22 38 0 76 q-22 38 0 76" '
            f'style="fill:none;stroke:var(--dk10);stroke-width:16;stroke-linecap:round;opacity:.45"/>'
            for x, y0 in ((860, 470), (920, 430), (980, 420), (1040, 440), (1100, 520))), when=O('men'))
# fundic gland polyps: several, small, smooth — body and fundus
add(''.join(f'<circle cx="{x}" cy="{y}" r="13" style="{POL}"/>' for x, y in ((1000, 362), (1108, 520), (1134, 650), (1128, 780))),
    when=O('fgp'))
# hyperplastic polyps: small, antral
add(''.join(f'<circle cx="{x}" cy="{y}" r="12" style="{POL}"/>' for x, y in ((650, 1094), (770, 1124))), when=O('hpp'))
# adenoma: solitary, lobulated, antral
add(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" style="{POL};stroke:var(--bad)"/>' for x, y, r in ((700, 1098, 22), (726, 1110, 18), (684, 1118, 16))),
    when=O('gad'))
# GIST: an intramural mass bulging from the greater-curvature wall, its mucosa ulcerated
add(f'<ellipse cx="1160" cy="700" rx="64" ry="92" style="{LES}"/>'
    '<path d="M1104 680 q8 18 0 36" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=O('gist'))
# gastric NET: small yellow-tan submucosal nodules in the body
add(''.join(f'<circle cx="{x}" cy="{y}" r="15" style="fill:var(--dk5);fill-opacity:.6;stroke:var(--dk5);stroke-width:3"/>'
            for x, y in ((1112, 560), (1140, 690), (1124, 816))), when=O('gnet'))
# ulcers
add(f'<ellipse cx="790" cy="850" rx="14" ry="22" style="{ULC}"/><ellipse cx="470" cy="1006" rx="18" ry="12" style="{ULC}"/>', when=O('bleed'))
add(f'<ellipse cx="440" cy="986" rx="18" ry="12" style="{ULC}"/>', when=O('perf'))
add(f'<ellipse cx="450" cy="1008" rx="18" ry="12" style="{ULC}"/>'
    '<path d="M450 1018 C452 1060 456 1100 458 1150" style="fill:none;stroke:var(--dyn-lost);stroke-width:12;stroke-linecap:round;opacity:.8"/>',
    when=O('pen'))
add(f'<ellipse cx="560" cy="1010" rx="14" ry="10" style="{ULC}"/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="16" style="fill:var(--dk8);opacity:.75"/>'
              for x, y in ((580, 1020), (606, 1000), (612, 1040), (640, 1018), (636, 1060), (668, 1040), (664, 1080), (700, 1060))),
    when=O('goo'))

# tag zone under the stomach (one or two lines per state)
TY = 1478
def tag(k, a, b=None):
    text(a, 180, TY, TAG, when=O(k))
    if b: text(b, 180, TY + 28, 'nf-l2', when=O(k))
text('chyme leaves through the pylorus · acid comes off the body and fundus', 180, TY, 'nf-l2', unless=O(
    'react', 'men', 'fgp', 'hpp', 'gad', 'gist', 'gnet', 'bleed', 'perf', 'pen', 'goo'))
tag('react', 'NSAIDs · alcohol · bile reflux · ischemia injure the lining directly', 'green dots = bile refluxing through the pylorus')
tag('men', 'giant cerebriform folds in the body and fundus — antrum spared', 'teal dots = albumin lost into the lumen · fewer acid dots')
tag('fgp', 'several small smooth polyps in the body and fundus', 'sporadic with PPI use, or with FAP (APC)')
tag('hpp', 'small antral polyps (mostly under 1 cm) on chronic gastritis', 'often H. pylori')
tag('gad', 'solitary antral polyp on atrophic gastritis', 'up to 30% carcinoma when over 2 cm')
tag('gist', 'intramural mass of the wall — more than half of GISTs are gastric', 'its mucosa often ulcerates')
tag('gnet', 'small yellow-tan submucosal nodules in the body', 'hypergastrinemia: autoimmune atrophic gastritis · ZES (MEN1)')
tag('bleed', 'lesser-curvature ulcer → left gastric a. · posterior duodenal ulcer → gastroduodenal a.', 'hematemesis · melena · shock')
tag('perf', 'anterior duodenal ulcer opens into the peritoneal cavity', 'free air under the diaphragm · shoulder pain (phrenic nerve)')
tag('pen', 'posterior duodenal ulcer burrows into the pancreas', 'pain referred to the back')
tag('goo', 'scar or edema at the pyloric channel holds food back', 'non-bilious vomiting after meals · early satiety · succussion splash')

# ════════ the wall, zoomed in ════════
ZX0, ZX1 = 1400, 2120
SURF, MM, SUB, MP, SER = 440, 760, 776, 950, 1210
add('<rect x="1370" y="212" width="970" height="1310" rx="24" class="dyn-soft"/>')
text('The gastric wall, zoomed in', 1400, 256, 'dyn-big')
text('lumen on top · glands of the body (parietal cells pink, chief cells teal)', 1400, 280, 'dyn-cap')
add(f'<rect x="{ZX0}" y="{SURF - 18}" width="{ZX1 - ZX0}" height="18" style="fill:var(--dk11);fill-opacity:.18"/>'
    f'<rect x="{ZX0}" y="{SURF}" width="{ZX1 - ZX0}" height="{MM - SURF}" style="fill:var(--dk10);fill-opacity:.07"/>'
    f'<rect x="{ZX0}" y="{MM}" width="{ZX1 - ZX0}" height="{SUB - MM}" style="fill:var(--dk7);fill-opacity:.45"/>'
    f'<rect x="{ZX0}" y="{SUB}" width="{ZX1 - ZX0}" height="{MP - SUB}" style="fill:var(--dk6);fill-opacity:.06"/>'
    f'<rect x="{ZX0}" y="{MP}" width="{ZX1 - ZX0}" height="{SER - MP}" style="fill:var(--dk7);fill-opacity:.18"/>'
    f'<path d="M{ZX0} 1080 H{ZX1}" style="stroke:var(--dk7);stroke-width:2;opacity:.5"/>'
    f'<path d="M{ZX0} {SER + 8} H{ZX1}" style="stroke:var(--ink-3);stroke-width:5"/>')
add(''.join(f'<path d="M{x} {MP + 12} V1068" style="stroke:var(--dk7);stroke-width:2;opacity:.35"/>' for x in range(ZX0 + 20, ZX1, 40))
    + ''.join(f'<path d="M{ZX0 + 10} {y} H{ZX1 - 10}" style="stroke:var(--dk7);stroke-width:2;opacity:.3"/>' for y in (1110, 1140, 1170, 1195)),
    unless=O('gist'))
# submucosal vessels
add(''.join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="9" style="fill:var(--nf-blood);opacity:.55"/>' for x, y in ((1480, 860), (1700, 900), (1990, 850))))
for lab, y in (('lumen', 360), ('mucus · HCO₃⁻', 436), ('mucosa', 600), ('muscularis mucosae', 772), ('submucosa', 870),
               ('muscularis propria', 1084), ('serosa', 1224)):
    text(lab, ZX1 + 18, y, 'nf-l2')

GX = [1450 + 90 * i for i in range(8)]
def gland(x, top=520, cells=4):
    s = f'<rect x="{x - 16}" y="{top}" width="32" height="{MM - 12 - top}" rx="14" style="fill:var(--surface);stroke:var(--dk10);stroke-width:2.5"/>'
    for j in range(cells):
        s += f'<circle cx="{x - 16 if j % 2 == 0 else x + 16}" cy="{top + 56 + 30 * j}" r="7" style="fill:var(--dk7);opacity:.8"/>'
    s += f'<circle cx="{x - 10}" cy="{MM - 30}" r="6" style="fill:var(--dk6)"/><circle cx="{x + 10}" cy="{MM - 26}" r="6" style="fill:var(--dk6)"/>'
    return s
def pit(x, bottom=520): return f'<path d="M{x - 7} {SURF} V{bottom} M{x + 7} {SURF} V{bottom}" style="stroke:var(--dk10);stroke-width:2.5"/>'
def cork(x, y0, y1, amp=10):
    n = max(1, int((y1 - y0) / 30))
    seg = ''.join(f' q{amp if j % 2 == 0 else -amp} 15 0 30' for j in range(n))
    return (f'<path d="M{x - 7} {y0}{seg}" style="fill:none;stroke:var(--dk10);stroke-width:2.5"/>'
            f'<path d="M{x + 7} {y0}{seg}" style="fill:none;stroke:var(--dk10);stroke-width:2.5"/>')
# normal glands and pits
add(''.join(gland(x) for x in GX), unless=O('men'))
add(''.join(pit(x) for x in GX), unless=O('react', 'men'))
# reactive gastropathy: corkscrew pits, edema, congested capillaries, no neutrophils
add(f'<rect x="{ZX0}" y="{SURF}" width="{ZX1 - ZX0}" height="{MM - SURF}" style="fill:var(--nf-h2o);fill-opacity:.12"/>'
    + ''.join(cork(x, SURF, 560) for x in GX)
    + ''.join(f'<ellipse cx="{x + 45}" cy="{y}" rx="8" ry="16" style="fill:var(--nf-blood);opacity:.7"/>' for x in GX[:-1] for y in (500, 660)),
    when=O('react'))
# Ménétrier: giant folds rise into the lumen; long corkscrew pits; short glands with few parietal cells
FOLD = 'M1400 440 ' + ' '.join(f'C{x + 30} 300 {x + 150} 300 {x + 180} 440' for x in range(1400, 2120, 180))
add(f'<path d="{FOLD} Z" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'
    + ''.join(cork(x, 360 if (x - 1400) % 180 < 120 else 400, 650, 8) for x in GX)
    + ''.join(gland(x, 650, 1) for x in GX), when=O('men'))
# polyp domes above the surface
DOME = '<path d="M1630 440 C1630 300 1910 300 1910 440 Z" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:3"/>'
add(DOME + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--surface);stroke:var(--dk10);stroke-width:2.5"/>'
                   + ''.join(f'<circle cx="{x + r * dx:.0f}" cy="{y + r * dy:.0f}" r="5" style="fill:var(--dk7)"/>' for dx, dy in ((-1, 0), (1, 0), (0, -1)))
                   for x, y, r in ((1700, 400, 26), (1770, 356, 22), (1840, 400, 26))), when=O('fgp'))
add(DOME + ''.join(f'<path d="M{x} 430 q14 -15 0 -30 q-14 -15 0 -30 q14 -15 0 -30" style="fill:none;stroke:var(--dk10);stroke-width:7;opacity:.6"/>'
                   for x in (1700, 1770, 1840))
    + ''.join(f'<circle cx="{x}" cy="{y}" r="4" style="fill:var(--dk7)"/>' for x, y in ((1668, 410), (1735, 380), (1735, 420), (1805, 350), (1805, 410), (1875, 400))),
    when=O('hpp'))
add(DOME + ''.join(f'<rect x="{x - 10}" y="{y}" width="20" height="44" rx="8" style="fill:var(--surface);stroke:var(--bad);stroke-width:2"/>'
                   f'<ellipse cx="{x - 6}" cy="{y + 22}" rx="3" ry="9" style="fill:var(--dyn-lost)"/><ellipse cx="{x + 6}" cy="{y + 22}" rx="3" ry="9" style="fill:var(--dyn-lost)"/>'
                   for x, y in ((1680, 380), (1716, 350), (1752, 380), (1788, 340), (1824, 380), (1860, 360))),
    when=O('gad'))
# GIST: a whorled spindle-cell mass in the muscularis propria, mucosa ulcerated over it
add(f'<ellipse cx="1760" cy="1030" rx="240" ry="200" style="{LES}"/>'
    + ''.join(f'<path d="M{x - 26} {y} q26 -22 52 0" style="fill:none;stroke:var(--bad);stroke-width:3;opacity:.7"/>'
              for x, y in ((1620, 980), (1700, 940), (1800, 960), (1880, 1000), (1660, 1060), (1760, 1040), (1860, 1080), (1720, 1130), (1820, 1150)))
    + f'<path d="M1720 {SURF} C1730 470 1790 470 1800 {SURF} Z" style="{WALLHOLE}"/>', when=O('gist'))
# gastric NET: nests of uniform cells in the deep mucosa and submucosa, salt-and-pepper nuclei
add(''.join(f'<ellipse cx="{x}" cy="{y}" rx="62" ry="40" style="fill:var(--dk5);fill-opacity:.35;stroke:var(--dk5);stroke-width:3"/>'
            + ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="3" style="fill:var(--dyn-lost)"/>' for dx, dy in ((-30, -10), (-12, 12), (6, -14), (24, 8), (36, -6), (-24, 16)))
            for x, y in ((1560, 830), (1760, 870), (1960, 836))), when=O('gnet'))
# ulcers in the wall
add(f'<path d="M1620 {SURF} C1660 450 1680 900 1760 900 C1840 900 1860 450 1900 {SURF} Z" style="{WALLHOLE}"/>'
    '<path d="M1664 600 C1690 860 1830 860 1856 600" style="fill:none;stroke:var(--dk4);stroke-width:8;opacity:.5"/>'
    '<circle cx="1760" cy="908" r="17" style="fill:var(--nf-blood);stroke:var(--bad);stroke-width:4"/>', when=O('bleed'))
HOLE = f'<path d="M1650 {SURF} C1690 470 1720 {SER} 1738 {SER + 16} L1782 {SER + 16} C1800 {SER} 1830 470 1870 {SURF} Z" style="{WALLHOLE}"/>'
add(HOLE, when=O('perf', 'pen'))
add('<path d="M1500 1262 C1560 1240 1700 1250 1760 1236 C1840 1250 1980 1240 2080 1264 C2110 1330 2090 1420 2040 1440 '
    'C1900 1450 1640 1452 1520 1436 C1470 1400 1470 1300 1500 1262 Z" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>'
    '<path d="M1760 1226 V1330" style="stroke:var(--dyn-lost);stroke-width:30;stroke-linecap:round;opacity:.75"/>', when=O('pen'))
text('pancreas', ZX1 + 18, 1350, 'nf-l2', when=O('pen'))
text('peritoneal cavity', ZX1 + 18, 1350, 'nf-l2', when=O('perf'))
# outlet obstruction: edema and dense scar thicken the wall at the pylorus
add(''.join(f'<path d="M{ZX0 + 10} {y} q40 -14 80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t80 0 t60 0" style="fill:none;stroke:var(--ink-3);stroke-width:4;opacity:.7"/>'
            for y in (810, 850, 890, 930, 990, 1040, 1100, 1160)), when=O('goo'))
# zoom tags
ZT = 1478
def ztag(k, a, b=None):
    text(a, 1400, ZT, TAG, when=O(k))
    if b: text(b, 1400, ZT + 28, 'nf-l2', when=O(k))
text('surface mucous cells and their gel protect the lining · acid rises from the glands', 1400, ZT, 'nf-l2', unless=O(
    'react', 'men', 'fgp', 'hpp', 'gad', 'gist', 'gnet', 'bleed', 'perf', 'pen', 'goo'))
ztag('react', 'corkscrew foveolar hyperplasia · edema · congestion', 'few or no neutrophils — gastropathy, not gastritis')
ztag('men', 'foveolar (mucous) hyperplasia · parietal and chief cells atrophy', 'albumin leaks across the mucosa')
ztag('fgp', 'cystically dilated glands lined by parietal, chief and foveolar cells', 'little or no inflammation')
ztag('hpp', 'elongated, dilated corkscrew pits in an inflamed lamina propria', 'dysplasia 1–20%, rising in polyps over 1 cm')
ztag('gad', 'dysplastic glands — crowded, elongated, hyperchromatic nuclei', 'a true neoplasm')
ztag('gist', 'spindle cells from the interstitial cells of Cajal · KIT (CD117) · DOG1', 'KIT (~75%) or PDGFRA (~8%) mutations')
ztag('gnet', 'nests of uniform cells, salt-and-pepper chromatin', 'chromogranin A · synaptophysin')
ztag('bleed', 'the ulcer base erodes an artery', 'necrotic debris · neutrophils · granulation tissue · scar')
ztag('perf', 'the crater goes through every layer', 'air and acid escape into the peritoneal cavity')
ztag('pen', 'the crater goes through the wall into the pancreas', 'a neighbor organ instead of the open peritoneum')
ztag('goo', 'edema or fibrous scar thickens the wall', 'the pyloric channel narrows')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
GOO = O('goo')
flows = [
  # chyme: esophagus → stomach → pylorus → duodenum
  dict(d='M790 232 V430 C850 600 960 780 900 940 C860 1040 680 1060 540 990 L480 992 C400 994 352 1010 344 1080 '
         'C330 1180 336 1290 400 1350 C470 1410 640 1420 780 1380', len=2120, speed=150, r=10, base=dict(chyme=10), unless=GOO),
  # outlet obstruction: chyme reaches the antrum and stops; some comes back up the esophagus
  dict(d='M790 232 V430 C850 600 960 780 900 940 C860 1010 760 1040 680 1050', len=1000, speed=120, r=10, base=dict(chyme=6), when=GOO),
  dict(d='M700 1040 C860 1000 930 820 880 640 C840 520 800 460 790 232', len=1000, speed=110, r=10, base=dict(chyme=4), when=GOO),
  # acid off the body and fundus (fewer in Ménétrier)
  dict(d='M1060 410 C1010 460 960 510 900 570', len=230, speed=70, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=1))], unless=O('bleed')),
  dict(d='M1150 600 C1080 620 1000 650 940 700', len=230, speed=70, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=0))], unless=O('bleed')),
  dict(d='M1140 800 C1060 810 990 830 930 860', len=230, speed=70, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=1))], unless=O('bleed')),
  # reactive gastropathy: bile refluxes back through the pylorus
  dict(d='M360 1180 C340 1060 420 996 540 994 C620 998 690 1040 780 1070', len=620, speed=80, r=8, base=dict(bile=6), when=O('react')),
  # Ménétrier: albumin lost into the lumen
  dict(d='M1000 560 C960 740 930 880 880 960 C820 1030 680 1050 560 996', len=640, speed=90, r=8, base=dict(prot=6), when=O('men')),
  # bleeding ulcers: into the lumen and downstream
  dict(d='M790 850 C840 920 800 1000 700 1030 C640 1040 580 1010 540 994', len=360, speed=90, r=8, base=dict(blood=5), when=O('bleed')),
  dict(d='M470 1004 C420 1000 370 1020 350 1080 C330 1180 338 1290 400 1350', len=420, speed=90, r=8, base=dict(blood=6), when=O('bleed')),
  # perforation: air out of the anterior ulcer, up under the diaphragm
  dict(d='M440 976 C260 900 170 720 186 520 C196 420 240 340 380 286', len=860, speed=110, r=8, base=dict(air=7), when=O('perf')),
  # penetration: acid into the pancreas
  dict(d='M450 1012 C452 1060 456 1100 460 1160', len=150, speed=50, r=7, base=dict(acid=3), when=O('pen')),
  # ── zoomed wall ──
  # acid up out of the glands into the lumen
  dict(d='M1540 720 V300', len=420, speed=80, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=0))], unless=ULCERS + O('gist')),
  dict(d='M1990 720 V300', len=420, speed=80, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=1))]),
  dict(d='M1720 720 V300', len=420, speed=80, r=7, base=dict(acid=3), mods=[m(O('men'), set=dict(acid=0))], unless=ULCERS + O('gist') + POLYPS),
  # Ménétrier: albumin from the submucosal vessels across the mucosa into the lumen
  dict(d='M1700 890 V330', len=560, speed=80, r=8, base=dict(prot=4), when=O('men')),
  dict(d='M1480 850 V330', len=520, speed=80, r=8, base=dict(prot=4), when=O('men')),
  dict(d='M1990 840 V330', len=510, speed=80, r=8, base=dict(prot=4), when=O('men')),
  # bleeding: from the eroded artery into the lumen
  dict(d='M1760 900 C1760 700 1720 420 1600 320', len=620, speed=90, r=8, base=dict(blood=7), when=O('bleed')),
  # perforation: air and acid out through the hole into the peritoneal cavity
  dict(d='M1760 320 V1290 C1700 1350 1620 1390 1520 1420', len=1240, speed=130, r=8, base=dict(air=6), when=O('perf')),
  dict(d='M1760 320 V1290 C1820 1350 1900 1390 2000 1420', len=1240, speed=130, r=8, base=dict(air=6), when=O('perf')),
  # penetration: acid down the tract into the pancreas
  dict(d='M1760 320 V1320', len=1000, speed=110, r=8, base=dict(acid=6), when=O('pen')),
  # reactive gastropathy: bile in the lumen against the surface
  dict(d='M2110 330 C1900 400 1600 400 1410 330', len=740, speed=90, r=8, base=dict(bile=6), when=O('react')),
]

sites = [
  dict(x=292, y=1130, n=[-1, 0], w=10, t='rec', l='', aria='Pylorus and duodenal bulb — peptic ulcers', c='pud', ions=[]),
  dict(x=1188, y=640, n=[1, 0], w=10, t='rec', l='', aria='Gastric mucosa — gastritis and gastropathy', c='gastritis', ions=[], unless=O('gist')),
  dict(x=ZX1 - 6, y=1030, n=[1, 0], w=10, t='rec', l='', aria='Muscularis propria — interstitial cells of Cajal', c='gutwall', ions=[]),
  dict(x=ZX1 - 6, y=600, n=[1, 0], w=10, t='rec', l='', aria='Gastric glands and polyps', c='polyps', ions=[]),
]

readouts = [
  dict(l='Gastric acid', mods=[dict(when=O('men'), d=-1)]),
  dict(l='Serum albumin', mods=[dict(when=O('men'), d=-1)]),
  dict(l='Mucosal neutrophils', mods=[dict(when=O('react', 'fgp'), d=0)]),
  dict(l='Cancer risk', mods=[dict(when=O('men', 'gad'), d=1), dict(when=O('fgp'), d=0)]),
  dict(l='Vomiting', mods=[dict(when=O('goo', 'men'), d=1)]),
  dict(l='GI bleeding', mods=[dict(when=O('bleed'), d=1)]),
  dict(l='Free air under the diaphragm', mods=[dict(when=O('perf'), d=1)]),
]

notes = {
  '': 'Chyme leaves the stomach through the pylorus while parietal cells of the body and fundus pour out acid. The mucus–bicarbonate '
      'gel, tight junctions, mucosal blood flow, restitution and PGE₂ keep the lining intact. Pick a lesion to see where it sits '
      'and what it does.',
  f'{SW}:react': 'Reactive (chemical) gastropathy: NSAIDs, alcohol, bile reflux or ischemia injure the lining directly — edema, '
                 'vascular congestion and corkscrew foveolar hyperplasia with few or no neutrophils (neutrophils would make it gastritis). '
                 'Severe cases erode, ulcerate and bleed.',
  f'{SW}:men': 'Ménétrier disease: excess TGF-α drives the EGF receptor, so foveolar mucous cells overgrow into giant cerebriform folds '
               'in the body and fundus (antrum spared) while parietal and chief cells atrophy — ↓ acid. Albumin leaks across the mucosa: '
               'hypoalbuminemia and edema, weight loss, vomiting; precancerous.',
  f'{SW}:fgp': 'Fundic gland polyp: smooth polyps of cystically dilated glands lined by parietal, chief and foveolar cells in the body and '
               'fundus. Sporadic ones rose with PPI use (acid blocked → gastrin → oxyntic gland growth) and carry no significant cancer '
               'risk; with FAP (APC) they can become dysplastic.',
  f'{SW}:hpp': 'Gastric hyperplastic (inflammatory) polyp: up to 75% of gastric polyps, mostly antral and under 1 cm — a reactive growth on '
               'chronic, often H. pylori, gastritis, with elongated corkscrew foveolar glands in an inflamed lamina propria. Dysplasia '
               'risk 1–20%, rising in pedunculated polyps over 1 cm.',
  f'{SW}:gad': 'Gastric adenoma: a true neoplasm (up to 10% of gastric polyps), usually a solitary antral polyp on atrophic gastritis '
               'with intestinal metaplasia; every adenoma is dysplastic. Men aged 50–60; up to 30% harbor or become adenocarcinoma when '
               'over 2 cm, so it is resected completely.',
  f'{SW}:gist': 'GIST: the commonest mesenchymal tumor of the abdomen, more than half in the stomach, arising in the wall from the '
                'interstitial cells of Cajal (the pacemaker cells). Gain-of-function KIT or PDGFRA mutations; KIT (CD117) and DOG1 '
                'positive; the mucosa over it can ulcerate and bleed. Resection; imatinib if unresectable or metastatic.',
  f'{SW}:gnet': 'Gastric neuroendocrine (carcinoid) tumor: small yellow-tan submucosal nodules in the oxyntic mucosa, from ECL-type cells '
                'driven by hypergastrinemia — autoimmune atrophic gastritis or Zollinger-Ellison syndrome (MEN1). Chromogranin A and '
                'synaptophysin positive; those on atrophic gastritis rarely metastasize.',
  f'{SW}:bleed': 'Ulcer bleeding, the commonest complication (15–20% of patients): the ulcer erodes a vessel in its base. A lesser-curvature '
                 'gastric ulcer bleeds from the left gastric artery, a posterior duodenal ulcer from the gastroduodenal artery — '
                 'hematemesis, melena, shock.',
  f'{SW}:perf': 'Ulcer perforation: an anterior duodenal ulcer opens into the peritoneal cavity — free air under the diaphragm on an '
                'upright film, peritonitis, shoulder pain from phrenic nerve irritation. Up to 5% of patients, but two-thirds of ulcer deaths.',
  f'{SW}:pen': 'Ulcer penetration: a posterior ulcer burrows through the wall into a neighbor such as the pancreas instead of the open '
               'peritoneum, and the pain becomes referred to the back.',
  f'{SW}:goo': 'Gastric outlet obstruction: edema or fibrous scar around a pyloric-channel or duodenal ulcer narrows the outlet (about 2% '
               'of patients). Food is held in the stomach — non-bilious vomiting after meals, early satiety, weight loss, a succussion splash.',
}

dyn = dict(
  kinds=dict(chyme=['chyme', '--dk8'], acid=['acid', '--nf-h'], bile=['bile', '--dk3'], prot=['prot', '--dk6'],
             blood=['blood', '--dk12'], air=['air', '--dk9']),
  groups=[['chyme', 'Chyme'], ['acid', 'Acid (H⁺)'], ['bile', 'Bile'], ['prot', 'Albumin'], ['blood', 'Blood'], ['air', 'Free air']],
  switches=[dict(id=SW, label='Pick a lesion', type='one', options=[
    ['react', 'Reactive gastropathy', 'gastritis'], ['men', 'Ménétrier disease', 'gastritis'],
    ['fgp', 'Fundic gland polyp', 'polyps'], ['hpp', 'Gastric hyperplastic polyp', 'polyps'], ['gad', 'Gastric adenoma', 'polyps'],
    ['gist', 'GIST · gastrointestinal stromal tumor', 'gutwall'], ['gnet', 'Gastric neuroendocrine tumor', 'carcinoid'],
    ['bleed', 'Ulcer bleeding', 'pud'], ['perf', 'Ulcer perforation', 'pud'], ['pen', 'Ulcer penetration', 'pud'],
    ['goo', 'Gastric outlet obstruction', 'pud']],
    sections=[['Gastropathy', ['react', 'men']], ['Polyps & tumors', ['fgp', 'hpp', 'gad', 'gist', 'gnet']],
              ['Ulcer complications', ['bleed', 'perf', 'pen', 'goo']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI lecture notes (SDL 9) · First Aid pp. 386–387 · Robbins ch 17 · Bootcamp GI')

PANY = 820
MAP = dict(
  id='stomsim', title='Gastric Polyps, Gastropathy & Ulcer Complications in Motion', topic='gi', after='acidflow',
  sub='Chyme rides through the stomach and acid comes off its body — then pick a gastropathy (reactive, Ménétrier), a polyp or '
      'tumor (fundic gland, hyperplastic, adenoma, GIST, neuroendocrine) or an ulcer complication (bleeding, perforation, '
      'penetration, outlet obstruction) and see where it sits, in the stomach and in the wall. Tap a site for its card',
  w=3500, h=1880,
  fa='386, 387', src=SRC,
  lanes=[('stGp', 'Gastropathy', 'glycolysis'), ('stPol', 'Polyps & tumors', 'tca'), ('stUl', 'Ulcer complications', 'gluconeo')],
  nodes=[
    ('st1', 'Gastritis · gastropathy', 330, 1660, 'stGp', 'reactive · Ménétrier', ['gastritis'], 'hub'),
    ('st2', 'NSAIDs', 760, 1660, 'stGp', '↓ PGE₂ defenses', ['nsaids']),
    ('st3', 'H. pylori', 1190, 1660, 'stGp', 'gastritis → polyps, ulcers', ['hpylori']),
    ('st4', 'PPIs', 1620, 1660, 'stPol', 'fundic gland polyps', ['ppi']),
    ('st5', 'Gastric polyps', 2050, 1660, 'stPol', 'hyperplastic · fundic · adenoma', ['polyps'], 'hub'),
    ('st6', 'FAP', 330, 1780, 'stPol', 'APC · fundic gland polyps', ['fap']),
    ('st7', 'Gastric adenocarcinoma', 760, 1780, 'stPol', 'where adenomas lead', ['gastricca']),
    ('st8', 'GIST · Cajal cells', 1190, 1780, 'stPol', 'KIT · imatinib', ['gutwall', 'cml']),
    ('st9', 'Gastric NET · ZES', 1620, 1780, 'stPol', 'hypergastrinemia', ['carcinoid', 'zes']),
    ('st10', 'Peptic ulcer', 2050, 1780, 'stUl', 'bleed · perforate · penetrate · obstruct', ['pud'], 'hub')],
  panels=[
    (2420, PANY, 1000, 'Gastric polyps (GI lecture notes SDL 9 · Robbins ch 17)', [
      ('Hyperplastic', 'up to 75% · antrum · on gastritis · dysplasia 1–20%'),
      ('Fundic gland', 'body, fundus · PPI or FAP · sporadic: no significant risk'),
      ('Adenoma', 'up to 10% · antrum · dysplastic · up to 30% cancer over 2 cm')]),
    (2420, PANY + 220, 1000, 'Ulcer complications (Robbins Table 17.4 · lecture notes SDL 9)', [
      ('Bleeding', '15–20% · commonest · 25% of ulcer deaths'),
      ('Perforation', 'up to 5% · two-thirds of ulcer deaths · free air'),
      ('Obstruction', 'about 2% · pyloric channel · edema or scar'),
      ('Penetration', 'into a neighbor such as the pancreas')])],
  dyn=dyn,
)
