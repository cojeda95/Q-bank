# m58 — Gastric Glands & the Mucosal Barrier in Motion (dynamic map, kit data)
# Left: one gastric pit and its fundic gland, drawn from the acid lumen down to the muscularis mucosae — the mucus–HCO₃⁻
# gel on the surface, surface mucous cells lining the surface and the pit, stem cells in the isthmus, mucous neck cells and
# parietal cells in the neck, chief cells (and an ECL cell) in the base, a mucosal capillary loop in the lamina propria,
# PGE₂ made in the mucosa. HCl, intrinsic factor and pepsinogen rise up the gland lumen; mucus and HCO₃⁻ leave the
# surface cells into the gel; back-diffusing H⁺ is neutralized in the gel. Right: the stomach with its three histologic
# regions (named for their glands) and the three gland types side by side at one scale (pit depth, cells).
# One `one` switch, "Pick a cell, a defense or an injury", in four sections (cells, glands, defenses, injury); seven
# readouts. Not a duplicate of acidflow (the parietal cell's transporters, keys, drugs, Cushing ulcer, ZES, H. pylori,
# autoimmune gastritis) or gutwallsim (the wall layer by layer, by gross segment).
#
# Sources (all read in the corpus; the GI course text wins for this block):
#   Course lecture notes, GI Exam 1 (corpus/gastro/course_exam1_lecture_notes.txt): p16 regions — cardiac: shallow pits,
#     tubular, somewhat tortuous, occasionally branched glands of mucus-secreting cells (flattened basal nuclei, pale
#     apical cytoplasm), occasional parietal cells at the fundic border; fundic (fundus + body, largest): pits ¼–⅓ of the
#     mucosa, simple branched tubular glands (isthmus, neck, base), surface mucous, mucous neck, parietal (neck/upper),
#     chief (base), enteroendocrine and stem cells; pyloric (antrum, before the sphincter): pits about half (50%) of the
#     mucosa, branched coiled glands with wide lumina, cells like surface mucous cells (viscous mucus), G and D cells
#     concentrated here, occasional parietal cells. pp16–17 cells — surface mucous cells: apical mucous cup, insoluble
#     gel-like mucus rich in HCO₃⁻; mucous neck cells: neck, among parietal cells, shorter, no cup, soluble less alkaline
#     mucus on vagal stimulation, precursors of surface cells; parietal: large triangular, intensely eosinophilic, H⁺/K⁺-
#     ATPase, HCl and intrinsic factor (44 kDa, B12 → distal ileum); chief: base, basophilic basal cytoplasm, apical
#     zymogen granules, pepsinogen + gastric lipase, pepsin below pH 5. p18: parietal cells the sole site of intrinsic
#     factor; loss (autoimmune gastritis, gastrectomy) → pernicious anemia, achlorhydria. pp19–20 barrier — mucus > 1 mm,
#     HCO₃⁻ under it, surface pH ~7, neutralizes back-diffusing H⁺ and inactivates pepsin; tight junctions; renewal every
#     3–7 days from isthmus stem cells; restitution = gland neck cells migrate along the basal lamina without mitosis;
#     blood flow washes away H⁺; PGE₂ and NO stimulate mucus and HCO₃⁻, keep vessels dilated, enhance repair; NSAIDs ↓ PGE₂
#     → ↓ HCO₃⁻ and mucus, ↓ blood flow, impaired restitution; aspirin damages hydrophobic membranes → acid leaks in;
#     ischemia/shock/alcohol → direct cytotoxicity or ↓ blood flow. p38: PGE₂ acts on Gi receptors on parietal cells,
#     opposing histamine (↓ acid); lumen pH near 1. pp46–47: reactive gastropathy (NSAIDs, alcohol, ischemia) — edema,
#     congestion, erosions, foveolar hyperplasia, few neutrophils; autoimmune gastritis — loss of parietal and chief cells.
#   Course histology, Pawlina ch 17 printout (course_sdl_2_3_histo_forgut_p2.txt): pp16–20 three histologic regions named for
#     their glands (cardiac near the esophageal orifice, pyloric before the sphincter, fundic between — the largest);
#     p21 surface mucous cells; p24 mucus gel, HCO₃⁻ secreted by surface cells and trapped in it, PGE stimulates HCO₃⁻,
#     thickens mucus, vasodilates the lamina propria; NO raises mucosal blood flow; aspirin/NSAIDs and alcohol damage the
#     surface epithelium; pp26–31 HCl (parietal), pepsinogen (chief), intrinsic factor (parietal), mucous neck cells;
#     pp44–46 cardiac and pyloric glands; pp51–53 surface cells renewed every 3–5 days, mucous neck cells ~6 days, chief
#     60–90 days, parietal 150–200 days.
#   Course physiology: Guyton ch 65 supplement (course_sdl_4_7_guyton_supplement_p3.txt pp12, 16–18) — oxyntic glands of
#     fundus and body secrete HCl, pepsinogen, intrinsic factor and mucus; pyloric glands secrete mainly mucus and the
#     hormone gastrin (G cells in the pyloric glands); ECL cells deep in oxyntic glands; surface mucous gel > 1 mm,
#     alkaline; aspirin or alcohol damage → acid leaks back. Costanzo ch 8 (course_sdl_4_7_physio.txt pp27–32) — pyloric
#     glands: G cells release gastrin into the circulation; PGE₂ antagonizes histamine (↓ H⁺), stimulates HCO₃⁻ and mucus,
#     increases mucosal blood flow; alcohol and caffeine stimulate HCl secretion.
#   Course pathology, Robbins ch 17 printout (course_sdl_8_9_patho.txt pp37–40): prostaglandins E and I support mucus,
#     HCO₃⁻, blood flow, restitution, and reduce acid; COX-2-selective drugs can also injure; alcohol direct cellular damage;
#     Curling ulcers (proximal duodenum and stomach, burns/trauma), local ischemia, systemic acidosis slows washout.
#   Course pharmacology, Katzung (course_sdl_10_pharm_p3.txt): misoprostol, a PGE₁ derivative, prevents peptic ulcer.
#   First Aid 2025 p. 379 (parietal → HCl ↓ by prostaglandin, intrinsic factor; chief → pepsin; HCO₃⁻ trapped in mucus),
#     p. 386 (NSAIDs ↓ PGE₂ → ↓ mucosal protection; burns → Curling ulcer, hypovolemia → mucosal ischemia).
#   Bootcamp.com Gastroenterology — Stomach (NSAIDs: ↓ PGE₂ → ↑ H⁺ secretion, ↓ HCO₃⁻, ↓ gastric blood flow; Curling:
#     hypovolemia → ↓ gastric blood flow) — the one explicit "NSAID ↑ acid"; Robbins (prostaglandins reduce acid) agrees.
# Readouts: ↑ made / raised · ↓ lowered · "–" where no source states a direction.
#   Fundic glands Mucus ↑ added (Guyton: oxyntic glands secrete mucus). Gel Mucus ↑ added (the gel is mucus).
#   Alcohol HCl ↑ added (Costanzo). Pyloric glands: Guyton says their mucous cells make "a small amount of pepsinogen" —
#   left "–" (an ↑ would mislead in Predict). Mucous neck cells: Costanzo lists mucus, HCO₃⁻ and pepsinogen for the
#   pyloric mucous cells — only Mucus ↑ shown. Burns: no source gives mucus/HCO₃⁻/acid directions — only blood flow ↓.
# Source conflicts: surface cell renewal 3–7 days (lecture notes, Robbins) vs 3–5 days (Pawlina) — both shown. Lumen pH
#   "near 1" (lecture notes) vs 1–2 (Costanzo) — "about 1–2".
# Cut: cardiac pit depth as a fraction (sources say only "shallow"); restitution "within minutes" (not in a source —
#   "rapidly"); phospholipid layer (Robbins only, not drawn); NO beyond a mention.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

PW17, GY65, CO8, RB17, KZ62 = full('Pawlina', 17), full('Guyton', 65), full('Costanzo', 8), full('Robbins', 17), full('Katzung', 62)

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

O = lambda *k: [f'g:{x}' for x in k]
INJ = O('nsaid', 'alc', 'burn')
GAPW = O('nsaid', 'alc', 'burn', 'rest')     # the surface defect is drawn in these states
THIN = O('nsaid', 'alc')                     # thinned gel

text('One gastric pit and its gland, and the three gland types', 160, 80, 'dyn-big')
text('acid, intrinsic factor and pepsinogen rise out of the gland · mucus and HCO₃⁻ cover the surface · '
     'blood runs in the lamina propria', 160, 104, 'dyn-cap')

# ════════ A. one gastric pit + fundic gland ════════
add('<rect x="160" y="170" width="1040" height="1360" rx="24" class="dyn-soft"/>')
text('a gastric pit and its fundic gland', 190, 204, 'nf-l1')
text('fundus · body — lumen at the top, muscularis mucosae at the bottom', 190, 222, 'nf-l2')
# lumen
text('gastric lumen — HCl + pepsin, pH about 1–2', 190, 262, 'nf-l2')
# lamina propria tint under the epithelium
add('<rect x="186" y="466" width="990" height="980" style="fill:var(--dk10);fill-opacity:.05"/>')
# mucus–HCO₃⁻ gel (thick normally, thin when NSAIDs / alcohol strip it)
add('<rect x="186" y="330" width="990" height="56" rx="10" style="fill:var(--dk10);fill-opacity:.28;stroke:var(--dk10);stroke-width:2"/>',
    unless=THIN)
add('<rect x="186" y="364" width="990" height="22" rx="8" style="fill:var(--dk10);fill-opacity:.22;stroke:var(--dk10);stroke-width:2;stroke-dasharray:6 6"/>',
    when=THIN)
add('<rect x="180" y="322" width="1002" height="72" rx="14" class="dyn-hl"/>', when=O('gel'))
text('mucus–HCO₃⁻ gel · surface pH ≈ 7', 1170, 322, 'nf-l1', 'end', unless=THIN)
text('gel thinned', 1170, 322, 'nf-l1 dyn-tag', 'end', when=THIN)
# pit lumen (mucus-filled)
add('<rect x="600" y="386" width="160" height="256" style="fill:var(--dk10);fill-opacity:.10"/>')

# surface mucous cells (top row) — the cell at x 996 is the one injured / restituted
GAPX = 996
def smc(x, y, w=38, h=80):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="dyn-cell"/>'
            f'<ellipse cx="{x + w / 2:.0f}" cy="{y + 20}" rx="{w / 2 - 5:.0f}" ry="16" style="fill:var(--dk10);fill-opacity:.4"/>'
            f'<ellipse cx="{x + w / 2:.0f}" cy="{y + h - 16}" rx="7" ry="9" style="fill:var(--dk11);fill-opacity:.45"/>')
TOP = [x for x in range(188, 520, 42)] + [x for x in range(842, 1176, 42)]
for x in TOP:
    if x == 1010 or x == 968: add(smc(x, 386), unless=GAPW)
    else: add(smc(x, 386))
# pit walls — columnar cells turned sideways, mucous cups facing the pit lumen
for y in range(388, 640, 42):
    add(f'<rect x="522" y="{y}" width="78" height="38" rx="6" class="dyn-cell"/>'
        f'<ellipse cx="582" cy="{y + 19}" rx="14" ry="14" style="fill:var(--dk10);fill-opacity:.4"/>'
        f'<ellipse cx="538" cy="{y + 19}" rx="8" ry="7" style="fill:var(--dk11);fill-opacity:.45"/>')
    add(f'<rect x="760" y="{y}" width="78" height="38" rx="6" class="dyn-cell"/>'
        f'<ellipse cx="778" cy="{y + 19}" rx="14" ry="14" style="fill:var(--dk10);fill-opacity:.4"/>'
        f'<ellipse cx="822" cy="{y + 19}" rx="8" ry="7" style="fill:var(--dk11);fill-opacity:.45"/>')
add('<path d="M184 380 H526 V646 M834 646 V380 H1180 M180 474 H520 M840 474 H1180" class="dyn-hl" style="opacity:.6"/>', when=O('surf'))
text('surface mucous cells', 190, 500, 'nf-l1')
text('mucous cup · insoluble alkaline mucus', 190, 518, 'nf-l2')
# the defect (injury) and its sealing (restitution)
add(f'<path d="M966 390 l10 14 l-8 12 l12 16 l-8 14 l10 20 M1052 390 l-10 14 l8 12 l-12 16 l8 14 l-10 20" class="dyn-lesion"/>', when=INJ)
add(f'<rect x="958" y="378" width="104" height="104" rx="14" class="dyn-hl"/>', when=INJ)
text('erosion — acid leaks back in', 1170, 262, 'nf-l1 dyn-tag', 'end', when=INJ)
add(f'<rect x="966" y="436" width="44" height="30" rx="8" class="dyn-cell"/><rect x="1012" y="436" width="44" height="30" rx="8" class="dyn-cell"/>'
    f'<path d="M944 452 h22" class="dyn-line" marker-end="url(#ah-mcDef)"/><path d="M1078 452 h-22" class="dyn-line" marker-end="url(#ah-mcDef)"/>', when=O('rest'))
add(f'<rect x="958" y="378" width="104" height="104" rx="14" class="dyn-hl"/>', when=O('rest'))
text('neck cells slide over the gap', 1170, 244, 'nf-l1', 'end', when=O('rest'))
text('along the basal lamina — no mitosis', 1170, 262, 'nf-l2', 'end', when=O('rest'))

# basal lamina around the gland, isthmus stem cells
add('<path d="M600 642 H560 V1400 Q560 1440 680 1440 Q800 1440 800 1400 V642 H760" class="dyn-dash" style="opacity:.6"/>')
for (x, y) in ((620, 660), (620, 690), (740, 660), (740, 690)):
    add(f'<circle cx="{x}" cy="{y}" r="13" style="fill:var(--dk8);fill-opacity:.35;stroke:var(--dk8);stroke-width:2"/>')
text('isthmus · stem cells', 545, 680, 'nf-l1', 'end')
add('<path d="M600 662 L660 662" style="stroke:none"/>')
# gland lumen
add('<path d="M680 646 V1412" style="stroke:var(--dk10);stroke-width:30;stroke-opacity:.12;stroke-linecap:round"/>')

def neck(x0, x1, y):     # mucous neck cell: short, no cup
    return (f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="46" rx="8" style="fill:var(--dk9);fill-opacity:.22;stroke:var(--dk9);stroke-width:2.5"/>'
            f'<circle cx="{(x0 + x1) // 2}" cy="{y + 23}" r="8" style="fill:var(--dk11);fill-opacity:.45"/>')
def par(xb, xa, y):      # parietal cell: base on the basal lamina (xb), apex at the lumen (xa); pear-shaped, eosinophilic
    s = 1 if xa > xb else -1
    return (f'<path d="M{xb} {y} C{xb} {y - 4} {xb + s * 70} {y + 14} {xa} {y + 34} C{xb + s * 70} {y + 54} {xb} {y + 72} {xb} {y + 68} Z" '
            f'style="fill:var(--dk2);fill-opacity:.42;stroke:var(--dk2);stroke-width:2.5"/>'
            f'<circle cx="{xb + s * 30}" cy="{y + 34}" r="9" style="fill:var(--dk11);fill-opacity:.55"/>')
def chief(x0, x1, y, ap):   # chief cell: basophilic base, apical zymogen granules (ap = lumen side x)
    return (f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="56" rx="8" style="fill:var(--dk11);fill-opacity:.32;stroke:var(--dk11);stroke-width:2.5"/>'
            + ''.join(f'<circle cx="{ap}" cy="{y + dy}" r="4.5" style="fill:var(--dk2);fill-opacity:.55"/>' for dy in (14, 28, 42)))
# neck: left and right columns
NECK_L = [(700, 'n'), (750, 'p'), (826, 'n'), (876, 'p'), (952, 'n'), (1002, 'p')]
NECK_R = [(700, 'p'), (776, 'n'), (826, 'p'), (902, 'n'), (952, 'p'), (1028, 'n')]
for y, k in NECK_L: add(neck(584, 664, y) if k == 'n' else par(562, 666, y))
for y, k in NECK_R: add(neck(696, 776, y) if k == 'n' else par(798, 694, y))
# base: chief cells, one parietal, one ECL cell
for y in (1090, 1150, 1270, 1330): add(chief(584, 664, y, 656))
for y in (1080, 1200, 1260, 1320): add(chief(696, 776, y, 704))
add(par(562, 666, 1206))
add(par(798, 694, 1140))
add('<rect x="584" y="1388" width="80" height="34" rx="10" style="fill:var(--surface);stroke:var(--line-2);stroke-width:2.5"/>'
    + ''.join(f'<circle cx="{x}" cy="1412" r="3" style="fill:var(--dk5)"/>' for x in (600, 614, 628, 642)))
# highlights
add('<g>' + ''.join(f'<rect x="578" y="{y - 4}" width="92" height="54" rx="10" class="dyn-hl"/>' for y, k in NECK_L if k == 'n')
    + ''.join(f'<rect x="690" y="{y - 4}" width="92" height="54" rx="10" class="dyn-hl"/>' for y, k in NECK_R if k == 'n') + '</g>', when=O('neck'))
add('<g>' + ''.join(f'<ellipse cx="614" cy="{y + 34}" rx="62" ry="44" class="dyn-hl"/>' for y, k in NECK_L if k == 'p')
    + ''.join(f'<ellipse cx="746" cy="{y + 34}" rx="62" ry="44" class="dyn-hl"/>' for y, k in NECK_R if k == 'p')
    + '<ellipse cx="614" cy="1240" rx="62" ry="44" class="dyn-hl"/><ellipse cx="746" cy="1174" rx="62" ry="44" class="dyn-hl"/></g>', when=O('par'))
add('<rect x="572" y="1070" width="216" height="322" rx="20" class="dyn-hl"/>', when=O('chief'))
add('<rect x="540" y="630" width="280" height="820" rx="30" class="dyn-hl"/>', when=O('fund'))
# labels (left of the gland)
text('mucous neck cells', 545, 744, 'nf-l1', 'end')
text('soluble mucus · on vagal stimulation', 545, 762, 'nf-l2', 'end')
text('parietal (oxyntic) cells', 545, 892, 'nf-l1', 'end')
text('eosinophilic · HCl + intrinsic factor', 545, 910, 'nf-l2', 'end')
text('chief (peptic) cells', 545, 1160, 'nf-l1', 'end')
text('basophilic base · pepsinogen + lipase', 545, 1178, 'nf-l2', 'end')
text('ECL cell · histamine', 545, 1410, 'nf-l2', 'end')
text('neck', 820, 860, 'nf-l2')
text('base', 820, 1240, 'nf-l2')
add('<path d="M812 700 V1056 M812 1076 V1400" style="stroke:var(--ink-3);stroke-width:2;opacity:.6"/>')
# muscularis mucosae
add('<rect x="186" y="1458" width="990" height="34" rx="8" style="fill:var(--dk8);fill-opacity:.28;stroke:var(--dk8);stroke-width:2"/>')
text('muscularis mucosae', 1170, 1516, 'nf-l2', 'end')
# PGE₂ (made in the mucosa); crossed out by NSAIDs
text('PGE₂ · made by COX in the mucosa', 190, 600, 'nf-l1')
text('→ mucus, HCO₃⁻, blood flow, restitution', 190, 618, 'nf-l2')
add('<circle cx="440" cy="476" r="34" class="dyn-hl"/>', when=O('pge'))
add('<path d="M440 516 V580" class="dyn-dash"/>')
text('COX blocked', 190, 640, 'nf-l1 dyn-tag', when=O('nsaid'))
# mucosal capillary loop (lamina propria)
CAP = 'M1120 1452 V522 Q1120 498 1096 498 H924 Q900 498 900 522 V1452'
shapes.append(dict(vessel=CAP, w=16, color='--nf-blood',
                   mods=[dict(when=O('pge'), d=8), dict(when=O('nsaid'), d=-7), dict(when=O('burn'), d=-10)]))
add(f'<path d="{CAP}" class="dyn-hl" style="stroke-width:34;opacity:.35"/>', when=O('pge', 'burn'))
text('mucosal', 1010, 980, 'nf-l1', 'middle')
text('capillary', 1010, 998, 'nf-l1', 'middle')
text('lamina', 1010, 1200, 'nf-l2', 'middle')
text('propria', 1010, 1216, 'nf-l2', 'middle')
text('ischemia', 1010, 1060, 'nf-l1 dyn-tag', 'middle', when=O('burn'))
text('dilated', 1010, 1060, 'nf-l1', 'middle', when=O('pge'))
text('less flow', 1010, 1060, 'nf-l1 dyn-tag', 'middle', when=O('nsaid'))

# ════════ B. where each gland lives ════════
add('<rect x="1260" y="170" width="1070" height="620" rx="24" class="dyn-soft"/>')
text('where each gland lives', 1290, 204, 'nf-l1')
text('the stomach’s histologic regions are named for their glands', 1290, 222, 'nf-l2')
STOM = ('M1600 330 C1560 250 1420 230 1360 320 C1310 400 1320 590 1400 680 C1480 770 1720 780 1880 724 '
        'C1960 696 2010 668 2040 650 L2040 590 C1990 590 1930 620 1850 630 C1740 642 1690 590 1680 500 '
        'C1675 440 1680 380 1690 330 Z')
shapes.append(dict(tube='M1645 240 L1645 332', w=40))
shapes.append(dict(tube='M2036 620 C2100 620 2140 632 2160 690', w=40))
add(f'<path d="{STOM}" class="nf-wall" style="fill:var(--surface);stroke-width:12;stroke-linejoin:round"/>')
add(f'<path d="{STOM}" style="fill:var(--dk2);fill-opacity:.14;stroke:none"/>')
PYLR = 'M1800 634 C1860 628 1940 614 2036 594 L2036 646 C2000 670 1950 700 1880 720 C1810 740 1760 748 1716 752 Z'
add(f'<path d="{PYLR}" style="fill:var(--surface);stroke:none"/><path d="{PYLR}" style="fill:var(--dk3);fill-opacity:.28;stroke:var(--dk3);stroke-width:2;stroke-dasharray:6 5"/>')
CARD = 'M1594 330 C1590 380 1610 410 1645 412 C1680 410 1690 380 1688 330 Z'
add(f'<path d="{CARD}" style="fill:var(--surface);stroke:none"/><path d="{CARD}" style="fill:var(--dk10);fill-opacity:.45;stroke:var(--dk10);stroke-width:2;stroke-dasharray:6 5"/>')
add('<path d="M2040 590 V650" style="stroke:var(--ink-2);stroke-width:8"/>')   # pyloric sphincter
add(f'<path d="{CARD}" class="dyn-hl"/>', when=O('card'))
add(f'<path d="{PYLR}" class="dyn-hl"/>', when=O('pyl'))
add(f'<path d="{STOM}" class="dyn-hl"/>', when=O('fund'))
text('esophagus', 1670, 262, 'nf-l2')
text('cardiac region', 1720, 404, 'nf-l1')
text('around the esophageal orifice', 1720, 422, 'nf-l2')
add('<path d="M1716 400 L1680 392" class="dyn-line"/>')
text('fundic region', 1400, 500, 'nf-l1')
text('fundus + body — the largest', 1400, 518, 'nf-l2')
text('pyloric region', 1880, 760, 'nf-l1')
text('antrum, before the sphincter', 1880, 778, 'nf-l2')
text('duodenum', 2180, 680, 'nf-l2')
text('pyloric sphincter', 2060, 568, 'nf-l2')

# ════════ C. the three gland types at one scale ════════
add('<rect x="1260" y="820" width="1070" height="710" rx="24" class="dyn-soft"/>')
text('the three gland types, one scale', 1290, 854, 'nf-l1')
text('surface at the top, muscularis mucosae at the bottom', 1290, 872, 'nf-l2')
SY, MY = 930, 1390
COLS = dict(card=1440, fund=1795, pyl=2150)
PIT = dict(card=1040, fund=1060, pyl=1160)       # pyloric pit ≈ half the mucosa; fundic ¼–⅓; cardiac "shallow"
for k, cx in COLS.items():
    add(f'<rect x="{cx - 140}" y="{SY - 12}" width="280" height="22" rx="6" style="fill:var(--dk10);fill-opacity:.32;stroke:var(--dk10);stroke-width:2"/>')
    add(f'<rect x="{cx - 140}" y="{MY}" width="280" height="16" rx="5" style="fill:var(--dk8);fill-opacity:.3"/>')
    pb = PIT[k]
    add(f'<path d="M{cx - 22} {SY + 10} V{pb} M{cx + 22} {SY + 10} V{pb}" style="stroke:var(--dk10);stroke-width:12;stroke-opacity:.5"/>')
# cardiac: tubular, tortuous mucous glands
cx = COLS['card']
add(f'<path d="M{cx} 1040 C{cx - 50} 1080 {cx + 50} 1120 {cx} 1160 C{cx - 50} 1200 {cx + 50} 1240 {cx} 1280 C{cx - 40} 1310 {cx + 30} 1350 {cx + 10} 1380" '
    'style="fill:none;stroke:var(--dk10);stroke-width:34;stroke-opacity:.45;stroke-linecap:round"/>')
add(f'<path d="M{cx} 1160 C{cx + 60} 1190 {cx + 90} 1250 {cx + 70} 1330" style="fill:none;stroke:var(--dk10);stroke-width:28;stroke-opacity:.35;stroke-linecap:round"/>')
add(f'<circle cx="{cx - 8}" cy="1060" r="9" style="fill:var(--dk2);fill-opacity:.6"/>')
# fundic: long glands — parietal cells upper, chief cells lower
cx = COLS['fund']
add(f'<path d="M{cx} 1060 V1380" style="stroke:var(--dk8);stroke-width:40;stroke-opacity:.16;stroke-linecap:round"/>')
add('<g>' + ''.join(f'<circle cx="{cx + (-14 if i % 2 else 14)}" cy="{y}" r="10" style="fill:var(--dk2);fill-opacity:.65"/>'
                    for i, y in enumerate(range(1078, 1250, 24))) + '</g>')
add('<g>' + ''.join(f'<circle cx="{cx + (-14 if i % 2 else 14)}" cy="{y}" r="9" style="fill:var(--dk11);fill-opacity:.6"/>'
                    for i, y in enumerate(range(1262, 1376, 22))) + '</g>')
text('parietal', cx + 34, 1150, 'nf-l2')
text('chief', cx + 34, 1320, 'nf-l2')
# pyloric: deep pits, coiled glands with wide lumina — mucous cells, G cells, D cells
cx = COLS['pyl']
add(f'<path d="M{cx} 1160 C{cx + 60} 1190 {cx + 60} 1230 {cx} 1250 C{cx - 60} 1270 {cx - 60} 1320 {cx} 1340 C{cx + 40} 1355 {cx + 40} 1375 {cx + 10} 1384" '
    'style="fill:none;stroke:var(--dk10);stroke-width:40;stroke-opacity:.45;stroke-linecap:round"/>')
add(f'<path d="M{cx} 1160 C{cx + 60} 1190 {cx + 60} 1230 {cx} 1250 C{cx - 60} 1270 {cx - 60} 1320 {cx} 1340" '
    'style="fill:none;stroke:var(--surface);stroke-width:10;stroke-linecap:round"/>')
for (x, y) in ((cx + 40, 1210), (cx - 40, 1290)):
    add(f'<circle cx="{x}" cy="{y}" r="10" style="fill:var(--dk5)"/>')
add(f'<circle cx="{cx + 22}" cy="1346" r="9" style="fill:var(--dk6)"/>')
text('G cells → gastrin', cx + 62, 1214, 'nf-l2')
text('D cell', cx + 42, 1350, 'nf-l2')
add(f'<path d="M{cx - 120} {SY} V1160" style="stroke:var(--ink-3);stroke-width:2"/><path d="M{cx - 128} {SY} h16 M{cx - 128} 1160 h16" style="stroke:var(--ink-3);stroke-width:2"/>')
text('pit ≈ ½', cx - 112, 1090, 'nf-l2')
cx = COLS['fund']
add(f'<path d="M{cx - 120} {SY} V1060" style="stroke:var(--ink-3);stroke-width:2"/><path d="M{cx - 128} {SY} h16 M{cx - 128} 1060 h16" style="stroke:var(--ink-3);stroke-width:2"/>')
text('pit ¼–⅓', cx - 112, 1000, 'nf-l2')
# names + swatches
for k, nm, s1, col in (('card', 'Cardiac glands', 'shallow pits · mucous cells', '--dk10'),
                       ('fund', 'Fundic (oxyntic) glands', 'parietal + chief cells', '--dk2'),
                       ('pyl', 'Pyloric glands', 'deep pits · mucus + G cells', '--dk3')):
    cx = COLS[k]
    text(nm, cx, 1446, 'nf-l1', 'middle')
    text(s1, cx, 1464, 'nf-l2', 'middle')
    add(f'<rect x="{cx - 70}" y="1478" width="140" height="10" rx="5" style="fill:var({col});fill-opacity:.5"/>')
    add(f'<rect x="{cx - 160}" y="{SY - 30}" width="320" height="580" rx="22" class="dyn-hl"/>', when=O(k))

TAG = dict(surf='surface mucous cells — line the surface and pits, make the mucus gel and its HCO₃⁻',
           neck='mucous neck cells — soluble mucus in the gland neck; precursors of surface cells',
           par='parietal cells — HCl and intrinsic factor (the only source)',
           chief='chief cells — pepsinogen (+ weak lipase); acid turns it into pepsin',
           card='cardiac glands — mucous glands around the esophageal orifice',
           fund='fundic (oxyntic) glands — HCl, pepsinogen, intrinsic factor, mucus',
           pyl='pyloric glands — deep pits, mucus, G cells (gastrin)',
           gel='mucus–HCO₃⁻ gel — surface pH about 7 under a lumen near pH 1–2',
           pge='PGE₂ — more mucus, HCO₃⁻ and blood flow; less acid',
           rest='restitution — neck cells migrate over a small defect, no mitosis',
           nsaid='NSAIDs — COX blocked: PGE₂ ↓, so the barrier fails and acid rises',
           alc='alcohol — direct damage to surface cells; acid leaks back',
           burn='burns (Curling ulcer) — hypovolemia → mucosal ischemia')
for k, s in TAG.items(): text(s, 160, 150, 'nf-l1 dyn-tag', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  # acid in the lumen
  dict(d='M190 296 H1170', len=980, speed=60, r=6, base=dict(h=6), mods=[m(O('par', 'fund', 'nsaid', 'alc'), add=dict(h=2)), m(O('pge'), add=dict(h=-2))]),
  # HCO₃⁻ held in the gel
  dict(d='M190 370 H1170', len=980, speed=34, r=5, base=dict(hco3=5),
       mods=[m(O('surf', 'gel', 'pge'), add=dict(hco3=4)), m(THIN, set=dict(hco3=1))]),
  # what the gland secretes, rising to the pit and the lumen
  dict(d='M680 1400 V420', len=980, speed=110, r=6, base=dict(h=2, pep=1, inf=1, muc=1),
       mods=[m(O('par'), add=dict(h=3, inf=2)), m(O('fund'), add=dict(h=2, pep=2, inf=1, muc=1)), m(O('chief'), add=dict(pep=3)),
             m(O('neck'), add=dict(muc=3)), m(O('pge'), add=dict(h=-1)), m(O('nsaid', 'alc'), add=dict(h=2))]),
  # blood in the mucosal capillary
  dict(d=CAP, len=2080, speed=120, r=6, base=dict(bl=10),
       mods=[m(O('pge'), add=dict(bl=4), speed=1.3), m(O('nsaid'), add=dict(bl=-4), speed=0.7), m(O('burn'), add=dict(bl=-7), speed=0.45)]),
  # acid leaking back through the erosion into the lamina propria
  dict(d=f'M{GAPX + 14} 300 V720', len=420, speed=60, r=6, base=dict(h=4), when=INJ),
]
for x in (250, 460, 880, 1140):     # back-diffusing H⁺ stopped in the gel
    flows.append(dict(d=f'M{x} 300 V356', len=56, speed=22, r=5, base=dict(h=1), unless=INJ))

def surf_site(x, unless=None):
    d = dict(x=x, y=386, n=[0, -1], w=8, t='ex', l='', aria='Surface mucous cell — mucus and HCO₃⁻ into the gel', c='mucosaldef',
             ions=[['muc', 'out', 1], ['hco3', 'out', 1]], cross=True, reach=34, boost=O('surf', 'gel', 'pge'), low=O('nsaid', 'burn'), stop=O('alc'))
    if unless: d['unless'] = unless
    return d
sites = [surf_site(x) for x in (250, 418, 884, 1136)] + [
  dict(x=355, y=386, n=[0, -1], w=8, t='wall', l='', aria='Tight junction between surface cells', c='celljunctions'),
  dict(x=440, y=472, n=[0, 1], w=8, t='rec', l='', aria='PGE₂ made by COX in the mucosa', c='mucosaldef',
       ions=[['pg', 'out', 1]], cross=True, reach=34, block=O('nsaid'), boost=O('pge')),
  # parietal cells → HCl + intrinsic factor into the gland lumen
  dict(x=664, y=784, n=[1, 0], w=8, t='pump', l='', aria='Parietal cell — H⁺/K⁺-ATPase, HCl and intrinsic factor', c='gastricacid',
       ions=[['h', 'out', 1], ['inf', 'out', 1]], cross=True, reach=14, boost=O('par', 'fund', 'nsaid', 'alc'), low=O('pge')),
  dict(x=664, y=1036, n=[1, 0], w=8, t='pump', l='', aria='Parietal cell — H⁺/K⁺-ATPase, HCl and intrinsic factor', c='gastricacid',
       ions=[['h', 'out', 1]], cross=True, reach=14, boost=O('par', 'fund', 'nsaid', 'alc'), low=O('pge')),
  dict(x=696, y=860, n=[-1, 0], w=8, t='pump', l='', aria='Parietal cell — H⁺/K⁺-ATPase, HCl and intrinsic factor', c='gastricacid',
       ions=[['h', 'out', 1], ['inf', 'out', 1]], cross=True, reach=14, boost=O('par', 'fund', 'nsaid', 'alc'), low=O('pge')),
  # mucous neck cells → soluble mucus
  dict(x=664, y=723, n=[1, 0], w=8, t='ex', l='', aria='Mucous neck cell — soluble mucus', c='gastricglands',
       ions=[['muc', 'out', 1]], cross=True, reach=14, boost=O('neck', 'fund')),
  dict(x=696, y=925, n=[-1, 0], w=8, t='ex', l='', aria='Mucous neck cell — soluble mucus', c='gastricglands',
       ions=[['muc', 'out', 1]], cross=True, reach=14, boost=O('neck', 'fund')),
  # chief cells → pepsinogen
  dict(x=664, y=1178, n=[1, 0], w=8, t='ex', l='', aria='Chief cell — pepsinogen', c='gastricacid',
       ions=[['pep', 'out', 1]], cross=True, reach=14, boost=O('chief', 'fund')),
  dict(x=696, y=1228, n=[-1, 0], w=8, t='ex', l='', aria='Chief cell — pepsinogen', c='gastricacid',
       ions=[['pep', 'out', 1]], cross=True, reach=14, boost=O('chief', 'fund')),
  dict(x=664, y=1358, n=[1, 0], w=8, t='ex', l='', aria='Chief cell — pepsinogen', c='gastricacid',
       ions=[['pep', 'out', 1]], cross=True, reach=14, boost=O('chief', 'fund')),
  # pyloric G and D cells
  dict(x=COLS['pyl'] + 40, y=1200, n=[0, -1], w=8, t='rec', l='', aria='G cell — gastrin into the blood', c='gastrin'),
  dict(x=COLS['pyl'] + 22, y=1336, n=[0, -1], w=8, t='rec', l='', aria='D cell — somatostatin', c='sstgi'),
  dict(x=COLS['card'], y=SY - 12, n=[0, -1], w=8, t='rec', l='', aria='Cardiac glands', c='gastricglands'),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='HCl', mods=[R(O('par', 'fund', 'nsaid', 'alc'), 1), R(O('pge'), -1)]),
  dict(l='Intrinsic factor', mods=[R(O('par', 'fund'), 1)]),
  dict(l='Pepsinogen', mods=[R(O('chief', 'fund'), 1)]),
  dict(l='Mucus', mods=[R(O('surf', 'neck', 'card', 'fund', 'pyl', 'gel', 'pge'), 1), R(O('nsaid'), -1)]),
  dict(l='Surface HCO₃⁻', mods=[R(O('surf', 'gel', 'pge'), 1), R(O('nsaid'), -1)]),
  dict(l='Mucosal blood flow', mods=[R(O('pge'), 1), R(O('nsaid', 'burn'), -1)]),
  dict(l='Gastrin', mods=[R(O('pyl'), 1)]),
]

notes = {
  '': 'Left: one gastric pit and its fundic gland, from the acid lumen down to the muscularis mucosae. Surface cells cover the '
      'mucosa with a mucus gel that traps HCO₃⁻; parietal and chief cells deep in the gland make acid, intrinsic factor and '
      'pepsinogen. Right: the three gland types and where they sit. Pick one. ↑ made or raised · ↓ lowered · – not stated.',
  'g:surf': 'Surface mucous cells line the whole surface and the gastric pits: simple columnar cells with a large apical cup of '
            'mucinogen. They secrete the thick, insoluble “visible” mucus and the HCO₃⁻ trapped in it — the first line of '
            'protection. They are replaced every 3–7 days (Pawlina: 3–5) from stem cells in the isthmus.',
  'g:neck': 'Mucous neck cells sit in the neck of fundic glands among the parietal cells. Shorter than surface cells and without a '
            'mucous cup, they secrete a soluble, less alkaline mucus when the vagus fires. They are immature precursors of '
            'surface mucous cells and live about 6 days.',
  'g:par': 'Parietal (oxyntic) cells: large, triangular, intensely eosinophilic cells, most numerous in the upper neck of fundic '
           'glands. Their H⁺/K⁺-ATPase pumps HCl, and they are the only source of intrinsic factor, which carries B12 to the '
           'distal ileum. Lose them (autoimmune gastritis, total gastrectomy) and acid and B12 absorption both fail — pernicious anemia.',
  'g:chief': 'Chief (peptic) cells fill the base of fundic glands: basophilic basal cytoplasm (rough ER) under apical zymogen '
             'granules. They secrete pepsinogen and a weak gastric lipase; acid below pH 5 turns pepsinogen into pepsin. '
             'Autoimmune atrophic gastritis destroys chief cells along with parietal cells.',
  'g:card': 'Cardiac region: a narrow zone around the esophageal orifice. Its pits are shallow and its glands tubular, somewhat '
            'tortuous and made almost entirely of mucus-secreting cells, with only occasional parietal cells at the fundic border. '
            'With the esophageal cardiac glands, they protect the esophagus against refluxed acid.',
  'g:fund': 'Fundic region: fundus and body, the largest part of the stomach. Shallow pits (¼–⅓ of the mucosa) open onto long, '
            'simple branched tubular glands — isthmus, neck, base — holding mucous neck, parietal, chief and enteroendocrine '
            '(ECL) cells. These oxyntic glands make the gastric juice: HCl, pepsinogen, intrinsic factor and mucus.',
  'g:pyl': 'Pyloric region: the antrum, before the pyloric sphincter. Its pits are deep — about half the thickness of the mucosa — '
           'over branched, coiled glands with wide lumina, lined by cells like surface mucous cells that make viscous mucus. '
           'G cells here release gastrin into the blood, D cells somatostatin; parietal cells are only occasional.',
  'g:gel': 'The mucus–HCO₃⁻ gel: an adherent mucus coat over 1 mm thick traps the HCO₃⁻ secreted by surface cells, so the cell '
           'surface sits near pH 7 while the lumen is near pH 1–2. Back-diffusing H⁺ is neutralized and pepsin inactivated '
           'before they reach the epithelium; tight junctions seal the rest.',
  'g:pge': 'Prostaglandin E₂ (with NO) keeps the barrier up: it stimulates mucus and HCO₃⁻ secretion, keeps mucosal vessels '
           'dilated and supports restitution. On Gi-coupled receptors of parietal cells it also lowers acid. Misoprostol, a '
           'PGE₁ analog, copies this to prevent NSAID ulcers.',
  'g:rest': 'Restitution: cells from the gland neck migrate along the basal lamina to cover a small erosion rapidly, with no cell '
            'division needed. Renewal from isthmus stem cells then replaces the surface cells over days. Prostaglandins support '
            'restitution, so NSAIDs impair it.',
  'g:nsaid': 'NSAIDs block cyclooxygenase, so PGE₂ falls: less mucus and HCO₃⁻, less mucosal blood flow, slower restitution, and '
             'more acid. Aspirin also damages the surface cells’ hydrophobic membranes, letting acid leak back into the lamina '
             'propria. Result: erosions, reactive gastropathy and gastric ulcers — COX-2-selective drugs can do it too.',
  'g:alc': 'Alcohol injures the surface cells directly (chemical cytotoxicity) and breaks the barrier, so secreted acid leaks back '
           'down its gradient into the mucosa; it also stimulates acid secretion. Result: acute reactive gastropathy — edema, '
           'congestion, erosions, few neutrophils.',
  'g:burn': 'Curling ulcer: after severe burns or trauma, hypovolemia cuts mucosal blood flow and the ischemic mucosa erodes, in the '
            'stomach and proximal duodenum. Systemic acidosis also slows washout of back-diffused acid. Compare the Cushing ulcer '
            'of brain injury, which is vagal acid hypersecretion.',
}

dyn = dict(
  kinds=dict(h=['h', '--nf-h'], hco3=['hco3', '--nf-hco3'], muc=['muc', '--dk10'],
             pep=['enz', '--dk11', 'pepsinogen'], inf=['enz', '--dk7', 'intrinsic factor'],
             bl=['bl', '--nf-blood'], pg=['pg', '--dk3']),
  groups=[['h', 'H⁺ (acid)'], ['hco3', 'HCO₃⁻'], ['muc', 'Mucus'], ['enz', 'Pepsinogen · intrinsic factor'],
          ['bl', 'Red cells'], ['pg', 'PGE₂']],
  switches=[dict(id='g', label='Pick a cell, a defense or an injury', type='one', options=[
      ['surf', 'Surface mucous cells', 'mucosaldef'], ['neck', 'Mucous neck cells', 'gastricglands'],
      ['par', 'Parietal (oxyntic) cells', 'gastricacid'], ['chief', 'Chief cells', 'gastricacid'],
      ['card', 'Cardiac glands · cardiac region', 'gastricglands'], ['fund', 'Fundic (oxyntic) glands · fundic region', 'gastricglands'],
      ['pyl', 'Pyloric glands · pyloric region', 'gastricglands'],
      ['gel', 'Mucus–bicarbonate gel', 'mucosaldef'], ['pge', 'Prostaglandin E₂ · PGE₂', 'mucosaldef'],
      ['rest', 'Restitution', 'gastricglands'],
      ['nsaid', 'NSAID injury', 'gastritis'], ['alc', 'Alcohol injury', 'gastritis'], ['burn', 'Burns · Curling ulcer', 'gastritis']],
      sections=[['The cells', ['surf', 'neck', 'par', 'chief']], ['The glands', ['card', 'fund', 'pyl']],
                ['The defenses', ['gel', 'pge', 'rest']], ['Injury', ['nsaid', 'alc', 'burn']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Course lecture notes (GI Exam 1, SDL 3, 7, 9) · Pawlina ch 17 · Guyton ch 65 · Costanzo ch 8 · Robbins ch 17 · '
      'Katzung · Bootcamp GI · First Aid pp. 379, 386')

MAP = dict(
  id='mucosim', title='Gastric Glands & the Mucosal Barrier in Motion', topic='gi', after='acidflow',
  sub='One gastric pit and its fundic gland — surface mucous, mucous neck, parietal and chief cells — with the cardiac, fundic '
      'and pyloric glands side by side; the mucus–HCO₃⁻ gel, PGE₂ and blood flow that protect the mucosa, restitution, and '
      'what NSAIDs, alcohol and burns break. Tap a pin for its card',
  w=3500, h=1760,
  fa='379, 386',
  src=[PW17, GY65, CO8, RB17, KZ62],
  lanes=[('mcCell', 'Gland cells', 'glycolysis'), ('mcDef', 'Mucosal barrier', 'gluconeo'), ('mcDz', 'Injury', 'tca')],
  nodes=[
    ('mc1', 'Gastric glands', 300, 1610, 'mcCell', 'cardiac · fundic · pyloric', ['gastricglands'], 'hub'),
    ('mc2', 'Parietal & chief cells', 680, 1610, 'mcCell', 'HCl · IF · pepsinogen', ['gastricacid']),
    ('mc3', 'Simple columnar lining', 1060, 1610, 'mcCell', 'surface mucous cells', ['simcol']),
    ('mc4', 'G cells → gastrin', 1440, 1610, 'mcCell', 'pyloric glands', ['gastrin']),
    ('mc5', 'D cells → somatostatin', 1820, 1610, 'mcCell', 'the brake', ['sstgi']),
    ('mc6', 'Mucus–HCO₃⁻ barrier', 2200, 1610, 'mcDef', 'PGE₂ · blood flow', ['mucosaldef']),
    ('mc7', 'Tight junctions', 300, 1700, 'mcDef', 'block acid back-diffusion', ['celljunctions']),
    ('mc8', 'NSAIDs', 680, 1700, 'mcDz', 'COX blocked → PGE₂ ↓', ['nsaids']),
    ('mc9', 'Gastritis · Curling ulcer', 1060, 1700, 'mcDz', 'NSAIDs · alcohol · burns', ['gastritis']),
    ('mc10', 'Peptic ulcer disease', 1440, 1700, 'mcDz', 'defense vs damage', ['pud']),
    ('mc11', 'H. pylori', 1820, 1700, 'mcDz', 'urease · antral gastritis', ['hpylori']),
  ],
  panels=[
    (2420, 1250, 1000, 'Gland cells (course: lecture notes SDL 3 · Pawlina ch 17)', [
      ('Surface mucous cells', 'surface + pits · insoluble alkaline mucus · 3–7 days'),
      ('Mucous neck cells', 'gland neck · soluble mucus · about 6 days'),
      ('Parietal cells', 'upper neck · HCl + intrinsic factor · 150–200 days'),
      ('Chief cells', 'gland base · pepsinogen + lipase · 60–90 days'),
      ('G and D cells', 'pyloric glands · gastrin, somatostatin'),
      ('Pit depth', 'fundic ¼–⅓ of the mucosa · pyloric about ½')]),
  ],
  dyn=dyn,
)
