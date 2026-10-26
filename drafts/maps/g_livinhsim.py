# m57 — Inherited & Metabolic Liver Disease in Motion (dynamic map, kit data)
# One hepatocyte between the blood (the sinusoid, top and sides) and the bile (canaliculus, bottom). What arrives: iron from
# the duodenum, fatty acids from fat tissue, ammonia from the gut, and — per option — alcohol, aspirin or fetal metabolites.
# What leaves: α1-antitrypsin, ceruloplasmin and glucose into the blood, copper into the bile. A `l` switch picks one disease
# (sections: something builds up · big fat droplets · tiny fat droplets); each option blocks or boosts the matching
# transport, fills the cell with what accumulates (hemosiderin, copper, PAS+ globules, macro- or microvesicular fat), lights
# the organ where the excess ends up, and reads out 7 labs. New cards: alf (acute liver failure), aflp (acute fatty liver of
# pregnancy). Spec: batches/m57/coverage3.md §6, cardgap_newcards.md #15, #17.
#
# Sources (all read in the corpus):
#   OCOM GI Exam 1 lecture notes (corpus/gastro/course_exam1_lecture_notes.txt — course text, wins for this block):
#     p82–83 acute liver failure (26 weeks, encephalopathy + coagulopathy, massive necrosis, small shrunken liver; ammonia,
#     asterixis, cerebral edema; factors II V VII IX X XI XII + fibrinogen; Councilman/acidophil bodies; ascites);
#     p88 microvesicular steatosis (valproate, tetracycline, aspirin/Reye): central nucleus, mitochondrial β-oxidation
#     defect, hypoglycemia, lactic acidosis, encephalopathy; p90 ALD vs MASLD (NADH ↓ FA oxidation ↑ lipogenesis; insulin
#     resistance ↑ peripheral lipolysis → FFA influx; macrovesicular fat pushes the nucleus aside; Mallory hyaline more in
#     ALD; AST:ALT ≥ 2 in ALD, < 1 in MASLD/MASH until advanced fibrosis); p90–92 HH (HFE chr 6 AR, ↓ hepcidin, ferroportin
#     uninhibited, periportal hemosiderin, Prussian blue, diabetes, slate-gray skin, cardiomyopathy, hypogonadism,
#     pseudogout, HCC), Wilson (ATP7B chr 13 AR, ↓ ceruloplasmin, no biliary copper excretion, free copper → brain, cornea,
#     kidneys; ↓ serum ceruloplasmin, ↑ 24-h urinary copper), α1AT (SERPINA1, autosomal codominant, PiZZ ≈ 10% of normal
#     AAT, stuck in ER, PAS+ diastase-resistant globules starting periportal, panacinar emphysema); p97 AFLP (1 in 16,000,
#     third trimester, fetal LCHAD deficiency, diffuse microvesicular steatosis, bleeding, vomiting, jaundice, HYPOGLYCEMIA,
#     encephalopathy; urgent termination of pregnancy).
#   Robbins ch 18 (= course_sdl_15_19_patho.txt): p10–13 acute liver failure (80–90% of capacity lost before failure,
#     ~80% mortality without transplant, acetaminophen ~50% of US adult cases, rare microvesicular cases — fatty liver of
#     pregnancy, valproate, tetracycline); p6 Councilman bodies restricted to yellow fever, acidophil bodies elsewhere;
#     p56 ALD AST:ALT ≥ 2:1; p61 MASH AST/ALT raised; p69–71 Wilson, α1AT (codominant alleles, PiZZ); p113 AFLP
#     (20–40% coexisting preeclampsia; LCHAD metabolites from fetus/placenta).
#   First Aid 2025 p. 397 (AST:ALT; PT ↑ in advanced liver disease), 398 (Reye: aspirin metabolites ↓ β-oxidation,
#   microvesicular fat, hyperammonemia, hypoglycemia; ALD NADH; MASLD), 400 (α1AT codominant, PAS+ globules, panacinar
#   emphysema), 402 (Wilson ↓ ceruloplasmin ↑ urine copper; HH ↓ hepcidin), 423 (HH: ferritin ↑, % transferrin
#   saturation ↑↑), 168 (Councilman bodies, yellow fever).
#
# Readouts — every arrow sourced; "–" everywhere else:
#   Ferritin · transferrin sat. HH ↑ (FA 423) · Ceruloplasmin Wilson ↓ (FA 402, notes p92) · Urine copper Wilson ↑ (same)
#   Serum α1AT α1AT ↓ (FA 400, notes p92 ~10%) · AST:ALT ALD ↑ (≥ 2), MASLD ↓ (< 1) (FA 397, notes p90, Robbins)
#   Ammonia Reye ↑ (FA 398) · Glucose Reye ↓ (FA 398), AFLP ↓ (notes p97)
# Cuts / conflicts:
#   - coverage3 cited Robbins p113 for AFLP hypoglycemia; Robbins does not say it — the course lecture notes p97 do, so kept.
#   - α1AT inheritance: FA + notes "codominant", Robbins course p71 opening line "autosomal recessive" (later "codominant
#     alleles") → shown as "codominant (disease needs two Z alleles, PiZZ)".
#   - Councilman bodies: the notes use "Councilman/acidophil bodies" for any apoptotic hepatocyte; Robbins keeps the eponym for
#     yellow fever. The alf card says both.
#   - No ammonia arrow for AFLP/Wilson/ALF options and no aminotransferase-level readout (it would be ↑ for most options and
#     teach nothing); SERPINA1 chromosome not in the sources → left out. Portal-vein share not shown.
# m58 pins (P13): option a1at relabelled "α1-Antitrypsin deficiency · AAT deficiency" — the GI Exam 1 lecture notes (SDL 16)
#   abbreviate it "AAT"; First Aid p. 400. Key unchanged.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

RB18 = full('Robbins', 18)
NOTES = 'OCOM Gastro — Exam 1 lecture notes (SDL 15–17)'

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

L = lambda *k: [f'l:{x}' for x in k]
MACRO, MICRO = L('ald', 'masld'), L('reye', 'aflp')
PANY = 1250
CX0, CY0, CX1, CY1 = 640, 440, 1960, 1160    # the hepatocyte
SX, SY, RX = 520, 330, 2060                   # sinusoid: left limb x, top y, right limb x

text('Inherited & metabolic liver disease — one hepatocyte: what comes in, what gets stuck', 180, 150, 'dyn-big')
text('blood in the sinusoid around it (top) · bile leaves underneath · the organs where the excess ends up (right)', 180, 176, 'dyn-cap')

# a small liver for orientation (from the front: right lobe on your left, falciform between the lobes)
LIVER = 'M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z'
FALC = 'M58 62 C56 40 56 20 58 6'
def scale(d, x, y, w, h):
    import re as _re
    return _re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}', d)
LD, LF = scale(LIVER, 1740, 110, 250, 165), scale(FALC, 1740, 110, 250, 165)
add(f'<path d="{LD}" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>', unless=L('hh') + MACRO + MICRO)
add(f'<path d="{LD}" style="fill:var(--dk10);fill-opacity:.5;stroke:var(--dk10);stroke-width:4"/>', when=L('hh'))
add(f'<path d="{LD}" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--dk5);stroke-width:4"/>', when=MACRO + MICRO)
add(f'<path d="{LF}" style="fill:none;stroke:var(--ink-3);stroke-width:2;opacity:.6"/>')
text('liver', 2010, 190, 'nf-l1')
text('dark brown with iron', 2010, 210, 'nf-l2', when=L('hh'))
text('yellow, fatty', 2010, 210, 'nf-l2', when=MACRO + MICRO)

# ════════ sinusoid (blood) ════════
add(f'<path d="M{SX} 1300 V{SY} H{RX} V1100" style="fill:none;stroke:var(--nf-blood);stroke-width:34;opacity:.2;stroke-linejoin:round"/>')
text('sinusoid — portal blood in', SX + 30, SY - 30, 'nf-l1')
text('→ hepatic vein → the body', RX - 20, SY - 30, 'nf-l2', 'end')

# sources on the left
SRCS = [(500, 'Duodenum', 'iron (via ferroportin)'), (760, 'Fat tissue', 'fatty acids'), (1020, 'Gut', 'ammonia (NH₃)')]
for y, a, b in SRCS:
    add(f'<rect x="160" y="{y - 70}" width="290" height="140" rx="22" class="dyn-soft"/>')
    text(a, 180, y - 8, 'nf-l1'); text(b, 180, y + 14, 'nf-l2')
add('<rect x="160" y="1210" width="290" height="140" rx="22" class="dyn-soft"/>')
text('Also arriving', 180, 1250, 'nf-l1')
text('nothing else', 180, 1272, 'nf-l2', unless=L('ald', 'reye', 'aflp'))
text('alcohol → excess NADH', 180, 1272, 'nf-l2', when=L('ald'))
text('aspirin, during a viral illness', 180, 1272, 'nf-l2', when=L('reye'))
text('from an LCHAD-deficient fetus:', 180, 1272, 'nf-l2', when=L('aflp'))
text('3-hydroxyacyl metabolites', 180, 1290, 'nf-l2', when=L('aflp'))

# ════════ the hepatocyte ════════
add(f'<rect x="{CX0}" y="{CY0}" width="{CX1 - CX0}" height="{CY1 - CY0}" rx="44" class="dyn-cell"/>')
text('hepatocyte', CX0 + 24, CY1 - 24, 'nf-l1')
# nucleus: central, or pushed aside by one big droplet
add('<ellipse cx="1000" cy="790" rx="70" ry="62" style="fill:var(--dk11);fill-opacity:.25;stroke:var(--dk11);stroke-width:3"/>', unless=MACRO)
text('nucleus', 1000, 795, 'nf-l2', 'middle', unless=MACRO)
add('<ellipse cx="760" cy="1010" rx="70" ry="34" style="fill:var(--dk11);fill-opacity:.25;stroke:var(--dk11);stroke-width:3"/>', when=MACRO)
text('nucleus', 760, 1015, 'nf-l2', 'middle', when=MACRO)
add('<circle cx="1060" cy="790" r="160" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--dk5);stroke-width:3"/>', when=MACRO)
text('macrovesicular fat', 1060, 780, 'nf-l1', 'middle', when=MACRO)
text('one big droplet pushes the nucleus aside', 1060, 800, 'nf-l2', 'middle', when=MACRO)
import math
for i in range(14):
    a = 2 * math.pi * i / 14
    add(f'<circle cx="{1000 + 112 * math.cos(a):.0f}" cy="{790 + 100 * math.sin(a):.0f}" r="15" style="fill:var(--dk5);fill-opacity:.45;stroke:var(--dk5);stroke-width:2"/>', when=MICRO)
text('microvesicular fat — tiny droplets, nucleus stays central', 1000, 935, 'nf-l2', 'middle', when=MICRO)
# Mallory hyaline (alcoholic hepatitis)
add('<path d="M1290 620 c15 -18 30 18 45 0 s30 18 45 0 s30 18 45 0" style="fill:none;stroke:var(--dk7);stroke-width:7;stroke-linecap:round"/>', when=L('ald'))
text('Mallory hyaline (clumped keratin)', 1290, 660, 'nf-l2', when=L('ald'))
# ER
for k in range(3):
    add(f'<path d="M1520 {610 + 34 * k} c40 -16 80 16 120 0 s80 16 120 0" style="fill:none;stroke:var(--dk1);stroke-width:5;opacity:.55"/>')
text('ER — makes α1-antitrypsin', 1520, 590, 'nf-l2')
for x, y in ((1560, 640), (1640, 676), (1720, 640), (1600, 708), (1700, 712)):
    add(f'<circle cx="{x}" cy="{y}" r="17" style="fill:var(--dk1);fill-opacity:.65;stroke:var(--dk1);stroke-width:2"/>', when=L('a1at'))
text('misfolded Z protein stuck: PAS+, diastase-resistant globules', 1500, 760, 'nf-l2', when=L('a1at'))
# hemosiderin (periportal hepatocytes first)
for i in range(22):
    x, y = 690 + (i * 53) % 260, 560 + (i * 37) % 130
    add(f'<rect x="{x}" y="{y}" width="12" height="12" rx="3" style="fill:var(--dk10);opacity:.85"/>', when=L('hh'))
text('hemosiderin (Prussian blue +)', 690, 720, 'nf-l2', when=L('hh'))
# copper building up
for i in range(18):
    x, y = 1500 + (i * 61) % 380, 820 + (i * 29) % 110
    add(f'<circle cx="{x}" cy="{y}" r="8" style="fill:var(--dk2);opacity:.85"/>', when=L('wil'))
text('free copper builds up (radicals)', 1500, 965, 'nf-l2', when=L('wil'))
# mitochondria
for x, y in ((1180, 1010), (1300, 1040), (1420, 1010)):
    add(f'<ellipse cx="{x}" cy="{y}" rx="52" ry="24" style="fill:var(--dk3);fill-opacity:.15;stroke:var(--dk3);stroke-width:3"/>')
    add(f'<path d="M{x - 34} {y} c10 -12 18 12 28 0 s18 12 28 0 s18 12 28 0" style="fill:none;stroke:var(--dk3);stroke-width:2"/>')

# ════════ bile ════════
shapes.append(dict(tube=f'M660 1240 H2250', w=18, color='--dk3'))
text('bile canaliculus → bile ducts → duodenum', 700, 1300, 'nf-l2')

# ════════ where the excess ends up ════════
TX = 2110
text('Lung', TX, 500, 'nf-l1')
text('elastase unchecked →', TX, 518, 'nf-l2', when=L('a1at')); text('panacinar emphysema', TX, 534, 'nf-l2', when=L('a1at'))
text('Brain', TX, 660, 'nf-l1')
text('copper → basal ganglia:', TX, 678, 'nf-l2', when=L('wil')); text('tremor, dystonia, psychiatric', TX, 694, 'nf-l2', when=L('wil'))
text('NH₃ → cerebral edema, coma', TX, 678, 'nf-l2', when=L('reye'))
text('encephalopathy', TX, 678, 'nf-l2', when=L('aflp'))
text('Cornea', TX, 790, 'nf-l1')
text('Kayser-Fleischer rings', TX, 808, 'nf-l2', when=L('wil'))
text('Pancreas · heart · skin', TX, 920, 'nf-l1')
text('iron → diabetes, cardio-', TX, 938, 'nf-l2', when=L('hh')); text('myopathy, slate-gray skin', TX, 954, 'nf-l2', when=L('hh'))
text('Kidney · urine', TX, 1060, 'nf-l1')
text('copper spills into urine', TX, 1078, 'nf-l2', when=L('wil'))

TAG = dict(hh='HFE → hepcidin ↓ → ferroportin open → the gut over-absorbs iron for decades',
           wil='ATP7B ✕ → copper neither into ceruloplasmin nor into bile → free copper spills',
           a1at='α1-antitrypsin made but not secreted — liver injured by the protein, lung by its absence',
           ald='ethanol → NADH ↑ → fatty acid oxidation ↓, lipogenesis ↑ · AST > ALT, usually ≥ 2 : 1',
           masld='insulin resistance → more fatty acids from fat tissue → stored as triglyceride · ALT > AST',
           reye='aspirin metabolites ✕ mitochondrial β-oxidation → tiny droplets, NH₃ ↑, glucose ↓',
           aflp='the fetus poisons the mother\'s mitochondria → third-trimester liver failure, glucose ↓')
for k, s in TAG.items(): text(s, 1300, 1380, 'nf-l1 dyn-tag', 'middle', when=L(k))
text('pick a disease: see what arrives, what gets stuck and where it ends up', 1300, 1380, 'dyn-cap', 'middle', unless=['l:*'])

# ════════ motion ════════
TOP = lambda x: f'M{x} {CY0 + 4} V{SY} '
flows = [
  dict(d=f'M450 500 H{SX} V{SY} H720 V{CY0}', len=80 + 170 + 200 + 110, speed=110, r=8, base=dict(fe=2), mods=[dict(when=L('hh'), add=dict(fe=4))]),
  dict(d=f'M450 760 H{SX} V{SY} H880 V{CY0}', len=80 + 430 + 360 + 110, speed=130, r=8, base=dict(ffa=3), mods=[dict(when=L('masld'), add=dict(ffa=4))]),
  dict(d=f'M450 1020 H{SX} V{SY} H1060 V{CY0}', len=80 + 690 + 540 + 110, speed=150, r=8, base=dict(nh3=3)),
  dict(d=f'M450 1280 H{SX} V{SY} H1250 V990', len=80 + 950 + 730 + 660, speed=220, r=8, base=dict(tox=4), when=L('ald', 'reye', 'aflp')),
  dict(d=TOP(1430) + f'H{RX} V500', len=110 + 630 + 170, speed=120, r=8, base=dict(aat=3), unless=L('a1at')),
  dict(d=TOP(1610) + f'H{RX} V1100', len=110 + 450 + 770, speed=140, r=8, base=dict(cu=3), unless=L('wil')),
  dict(d=TOP(1610) + f'H{RX} V1060', len=110 + 450 + 730, speed=140, r=8, base=dict(cu=5), when=L('wil')),
  dict(d=TOP(1800) + f'H{RX} V1100', len=110 + 260 + 770, speed=140, r=8, base=dict(glu=3), mods=[dict(when=L('reye', 'aflp'), set=dict(glu=1))]),
  dict(d=f'M720 {SY} H{RX} V920', len=1340 + 590, speed=150, r=8, base=dict(fe=5), when=L('hh')),
  dict(d=f'M1060 {SY} H{RX} V660', len=1000 + 330, speed=150, r=8, base=dict(nh3=4), when=L('reye')),
  dict(d=f'M1700 {CY1 - 4} V1240 H2250', len=80 + 550, speed=110, r=8, base=dict(cu=3), unless=L('wil')),
]
sites = [
  dict(x=720, y=CY0, n=[0, 1], w=10, t='rec', l='Iron in', s='', c='hemochrom', ions=[['fe', 'out', 1]], boost=L('hh'), sfx=dict(boost=' — more')),
  dict(x=880, y=CY0, n=[0, 1], w=10, t='rec', l='Fatty acids in', s='', c='masld', ions=[['ffa', 'out', 1]], boost=L('masld'), sfx=dict(boost=' — more')),
  dict(x=1060, y=CY0, n=[0, 1], w=10, t='rec', l='NH₃ → urea', s='', c='hepenceph', ions=[['nh3', 'out', 1]], low=L('reye'), sfx=dict(low=' — fails')),
  dict(x=1430, y=CY0, n=[0, 1], w=10, t='rec', l='α1-antitrypsin out', s='', c='a1at', ions=[['aat', 'in', 1]], block=L('a1at'), sfx=dict(block=' — stuck')),
  dict(x=1610, y=CY0, n=[0, 1], w=10, t='rec', l='Ceruloplasmin out', s='', c='wilson', ions=[['cu', 'in', 1]], low=L('wil'), sfx=dict(low=' — low')),
  dict(x=1800, y=CY0, n=[0, 1], w=10, t='rec', l='Glucose out', s='', c='reye', ions=[['glu', 'in', 1]], low=L('reye', 'aflp'), sfx=dict(low=' — low')),
  dict(x=1700, y=CY1, n=[0, -1], w=10, t='rec', l='ATP7B: copper → bile', s='', c='wilson', ions=[['cu', 'in', 1]], block=L('wil')),
  dict(x=1300, y=1040, n=[0, 1], w=8, t='rec', l='β-oxidation', s='', c='faoxpattern', ions=[], lx=1300, ly=1100,
       block=L('reye', 'aflp'), low=L('ald'), sfx=dict(block=' — blocked', low=' — slowed by NADH')),
]

readouts = [
  dict(l='Ferritin · transferrin saturation', mods=[dict(when=L('hh'), d=1)]),
  dict(l='Serum ceruloplasmin', mods=[dict(when=L('wil'), d=-1)]),
  dict(l='Urine copper', mods=[dict(when=L('wil'), d=1)]),
  dict(l='Serum α1-antitrypsin', mods=[dict(when=L('a1at'), d=-1)]),
  dict(l='AST : ALT ratio', mods=[dict(when=L('ald'), d=1), dict(when=L('masld'), d=-1)]),
  dict(l='Ammonia', mods=[dict(when=L('reye'), d=1)]),
  dict(l='Glucose', mods=[dict(when=L('reye', 'aflp'), d=-1)]),
]

notes = {
  '': 'One hepatocyte: it takes up iron, fatty acids and ammonia from the sinusoid, burns fat in its mitochondria, sends '
      'α1-antitrypsin, ceruloplasmin and glucose into the blood and copper into the bile. Pick a disease to see what gets stuck.',
  'l:hh': 'Hereditary hemochromatosis: HFE mutations (chromosome 6, autosomal recessive) lower hepcidin, so ferroportin stays open '
          'and the gut over-absorbs iron. Hemosiderin (Prussian blue) fills periportal hepatocytes, then pancreas, heart, skin, '
          'joints — cirrhosis, diabetes, cardiomyopathy, high HCC risk; ferritin and transferrin saturation ↑.',
  'l:wil': 'Wilson disease: ATP7B (chromosome 13, autosomal recessive) fails, so copper is neither built into ceruloplasmin nor '
           'excreted into bile. Free copper injures the liver and spills to the basal ganglia, the cornea (Kayser-Fleischer '
           'rings) and the kidneys — serum ceruloplasmin ↓, urine copper ↑.',
  'l:a1at': 'α1-Antitrypsin deficiency (SERPINA1, codominant — disease needs two Z alleles, PiZZ): the misfolded protein is stuck '
            'in the ER as PAS-positive, diastase-resistant globules and injures the liver. Only about 10% reaches the blood, so '
            'elastase goes unchecked in the lung → panacinar emphysema.',
  'l:ald': 'Alcohol-associated liver disease: ethanol metabolism makes excess NADH, which slows fatty acid oxidation and drives '
           'lipogenesis → macrovesicular fat that pushes the nucleus aside. Alcoholic hepatitis adds ballooning, neutrophils '
           'and Mallory hyaline; AST exceeds ALT, usually ≥ 2 : 1.',
  'l:masld': 'MASLD: insulin resistance releases more fatty acids from fat tissue, and the liver stores them as triglyceride '
             '(macrovesicular steatosis). MASH adds lobular inflammation, ballooning and chicken-wire fibrosis around the central '
             'vein; ALT usually exceeds AST (ratio < 1) until fibrosis is advanced.',
  'l:reye': 'Reye syndrome: a child given aspirin during a viral illness (VZV, influenza) — aspirin metabolites inhibit '
            'mitochondrial β-oxidation. Tiny fat droplets surround a central nucleus (microvesicular), with hyperammonemia, '
            'hypoglycemia, cerebral edema and coma.',
  'l:aflp': 'Acute fatty liver of pregnancy (third trimester, ~1 in 16,000): in some cases the fetus is LCHAD-deficient and its '
            'long-chain 3-hydroxyacyl metabolites poison the mother\'s mitochondria → diffuse microvesicular fat, bleeding, '
            'vomiting, jaundice, hypoglycemia, encephalopathy. 20–40% also have preeclampsia; treatment is ending the pregnancy.',
}

dyn = dict(
  # Key labels for the Mac-side table: fe iron · ffa fatty acids · nh3 ammonia · tox alcohol/aspirin/fetal metabolites ·
  # aat α1-antitrypsin · cu copper · glu glucose
  kinds=dict(fe=['mov', '--dk10'], ffa=['mov', '--dk5'], nh3=['mov', '--dk4'], tox=['mov', '--dk7'], aat=['mov', '--dk1'],
             cu=['mov', '--dk2'], glu=['mov', '--dk9']),
  groups=[['mov', 'Iron · fatty acids · NH₃ · alcohol/aspirin/fetal toxins · α1AT · copper · glucose']],
  switches=[dict(id='l', label='Disease', type='one', options=[
              ['hh', 'Hereditary hemochromatosis', 'hemochrom'], ['wil', 'Wilson disease', 'wilson'],
              ['a1at', 'α1-Antitrypsin deficiency · AAT deficiency', 'a1at'],
              ['ald', 'Alcohol-associated liver disease', 'ald'], ['masld', 'MASLD · MASH', 'masld'],
              ['reye', 'Reye syndrome', 'reye'], ['aflp', 'Acute fatty liver of pregnancy', 'aflp']],
              sections=[['Something builds up', ['hh', 'wil', 'a1at']], ['Big fat droplets', ['ald', 'masld']],
                        ['Tiny fat droplets — mitochondria fail', ['reye', 'aflp']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2520, y=110, w=1000),
  src='First Aid pp. 397–398, 400, 402, 423 · Robbins ch 18 · OCOM GI Exam 1 lecture notes (SDL 15–17)')

# ════════ new cards ════════
card('alf', 'Acute liver failure', 'dz', 'liEnd', 'Encephalopathy + coagulopathy within 26 weeks, no prior liver disease', 0,
 'Acute liver illness with <b>encephalopathy and coagulopathy within 26 weeks</b> of the first injury, without preexisting liver '
 'disease. Usually <b>massive hepatic necrosis</b> (acetaminophen ≈ half of US adult cases; also hepatitis viruses, autoimmune '
 'hepatitis, other drugs); rarely microvesicular fat without necrosis (fatty liver of pregnancy, valproate, tetracycline). '
 'About 80–90% of functional capacity is lost before failure shows.',
 ['Small, shrunken liver: broad zones of parenchymal loss around islands of surviving cells',
  'Hepatic encephalopathy from ammonia: confusion → coma, <b>asterixis</b>, rigidity, hyperreflexia, cerebral edema',
  'Coagulopathy: factors II, V, VII, IX, X, XI, XII and fibrinogen not made; activated factors not cleared (DIC)',
  'Portal hypertension here is intrahepatic and shows as <b>ascites</b>',
  'Apoptotic hepatocytes = <b>acidophil bodies</b> (the course notes also say Councilman bodies; Robbins keeps that name for yellow fever)'],
 ['Aminotransferases markedly ↑ — a fall while jaundice, coagulopathy and encephalopathy worsen means few hepatocytes are left',
  'PT ↑ (lost synthesis of clotting factors)'],
 ['Encephalopathy and coagulopathy within 26 weeks'],
 [RB18],
 ['Liver transplantation — without it, mortality of hepatic failure is about 80%'],
 ['acute liver failure', 'fulminant liver failure', 'fulminant hepatic failure', 'acidophil bodies', 'acidophil body',
  'councilman bodies'],
 fa='168, 397, 402')
card('aflp', 'Acute fatty liver of pregnancy', 'dz', 'liMito', 'Fetal LCHAD deficiency can poison the mother\'s liver', 0,
 'In a subset of cases both parents carry a mutation in mitochondrial <b>long-chain 3-hydroxyacyl-CoA dehydrogenase (LCHAD)</b>; '
 'the deficient fetus and placenta release long-chain 3-hydroxyacyl metabolites that enter the mother and overwhelm her '
 'hepatocyte mitochondria — a rare case of the fetus causing metabolic disease in the mother.',
 ['Latter half of pregnancy, usually the <b>third trimester</b>; about 1 in 16,000 pregnancies',
  'Biopsy: diffuse <b>microvesicular steatosis</b> (tiny droplets, central nucleus); severe cases: hepatocyte dropout, cholestasis',
  'Incipient liver failure: bleeding, nausea and vomiting, jaundice, hypoglycemia, encephalopathy or coma',
  '20–40% present with coexisting <b>preeclampsia</b>'],
 ['Aminotransferases ↑ (from subclinical rises to liver failure)', 'Hypoglycemia'],
 ['Third-trimester liver failure with microvesicular fat'],
 [RB18],
 ['Termination of pregnancy (delivery) — it can progress to liver failure within days'],
 ['acute fatty liver of pregnancy', 'fatty liver of pregnancy', 'aflp'],
 alias='AFLP')

MAP = dict(
  id='livinhsim', title='Inherited & Metabolic Liver Disease in Motion', topic='gi', after='liver',
  sub='One hepatocyte between blood and bile: iron, copper, α1-antitrypsin and fat each get stuck in their own disease — see what '
      'accumulates, where the excess ends up and which labs move. Tap a transporter for its card',
  w=3600, h=1880,
  fa='168, 397–398, 400, 402, 423',
  src=[RB18],
  lanes=[('liInh', 'Something builds up', 'glycogen'), ('liFat', 'Fatty liver', 'gluconeo'),
         ('liMito', 'Mitochondria fail', 'tca'), ('liEnd', 'Where it ends', 'glycolysis')],
  nodes=[
    ('li1', 'Hemochromatosis', 300, 1560, 'liInh', 'HFE · hepcidin ↓', ['hemochrom'], 'hub'),
    ('li2', 'Wilson disease', 660, 1560, 'liInh', 'ATP7B · copper', ['wilson']),
    ('li3', 'α1-Antitrypsin deficiency', 1020, 1560, 'liInh', 'PiZZ · PAS+ globules', ['a1at']),
    ('li4', 'Alcohol-associated', 1380, 1560, 'liFat', 'AST : ALT ≥ 2 · Mallory', ['ald', 'cytoskel']),
    ('li5', 'MASLD · MASH', 1740, 1560, 'liFat', 'insulin resistance', ['masld']),
    ('li6', 'Reye syndrome', 2100, 1560, 'liMito', 'aspirin + virus', ['reye']),
    ('li7', 'Fatty liver of pregnancy', 300, 1730, 'liMito', 'fetal LCHAD', ['aflp', 'faoxpattern', 'preeclampsia']),
    ('li8', 'Acute liver failure', 660, 1730, 'liEnd', 'within 26 weeks', ['alf', 'hepenceph']),
    ('li9', 'Cirrhosis · HCC', 1020, 1730, 'liEnd', 'the shared endpoint', ['cirrhosis', 'hcc']),
    ('li10', 'Reading liver labs', 1380, 1730, 'liEnd', 'AST · ALT · ALP', ['lfts'])],
  panels=[
    (2520, PANY, 1000, 'Gene · inheritance · stain (First Aid 400, 402; course notes)', [
      ('Hemochromatosis', 'HFE, chr 6 · autosomal recessive · Prussian blue'),
      ('Wilson disease', 'ATP7B, chr 13 · autosomal recessive'),
      ('α1-Antitrypsin def.', 'SERPINA1 · codominant (PiZZ) · PAS+, diastase-resistant'),
      ('Alcohol vs MASLD', 'AST : ALT ≥ 2 vs < 1'),
      ('Reye · AFLP', 'microvesicular fat · mitochondrial β-oxidation fails')])],
  dyn=dyn)
