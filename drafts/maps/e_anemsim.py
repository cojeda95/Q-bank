# m52 — Anemia Work-up in Motion (dynamic map, kit data)
# The red cell's whole life, drawn for READING THE ANEMIA WORK-UP (anemiasim is the decision tree, ironflow the gut cell):
# small intestine (DMT1 → ferroportin, hepcidin ⊣; B12 and folate) → plasma transferrin → liver (hepcidin, ferritin stores,
# bilirubin conjugation) → bone marrow erythroblast (transferrin uptake, ALA synthase → ferrochelatase in the mitochondrion,
# globin chains, DNA synthesis on B12 + folate, EPO receptor) with the kidney's EPO below → reticulocytes into the blood
# (~120 days) → splenic red-pulp macrophage (extravascular: iron back out through ferroportin, heme → unconjugated
# bilirubin to the liver) or lysis in the vessel (intravascular: free Hb → haptoglobin → kidney → hemoglobinuria), a
# bleeding vessel, and a peripheral-smear inset redrawn for every cause. One `one` switch picks the cause, in `sections`
# (microcytic · normocytic, not hemolysis · normocytic hemolytic · macrocytic); particle size in the blood follows the MCV.
# Readouts: MCV, reticulocytes, ferritin, TIBC, LDH · indirect bilirubin, haptoglobin, methylmalonic acid.
#
# Sources (all read in the corpus; FA = First Aid 2025 page):
#   FA 413 (RBC life span ~120 d; reticulocyte = immature RBC, bluish polychromasia from residual rRNA) · FA 381 (iron as
#     Fe²⁺ in the duodenum, folate duodenum + jejunum, B12 terminal ileum with intrinsic factor) · FA 209 (hepcidin ↓ iron
#     absorption by degrading ferroportin and ↓ release from macrophages; haptoglobin binds free Hb; ferritin sequesters
#     iron) · FA 607 (EPO from interstitial cells of the peritubular capillary bed in response to hypoxia; stimulates RBC
#     proliferation; given for CKD anemia) · FA 67 (B12 cofactor for methionine synthase + methylmalonyl-CoA mutase; causes:
#     pernicious anemia, gastric bypass, ileal resection, D. latum, metformin, veganism) · FA 420 (smear: spherocytes HS/AIHA,
#     bite cells G6PD — Heinz bodies removed by splenic macrophages, schistocytes MAHA/mechanical, target cells HbC/asplenia/
#     liver/thal, macro-ovalocytes megaloblastic, echinocytes liver disease/ESRD/PK, sickle cells) · FA 421 (ringed
#     sideroblasts need Prussian blue; Howell-Jolly bodies functional hyposplenia; basophilic stippling sideroblastic + thal;
#     Heinz bodies = denatured Hb, supravital stain) · FA 422 (the MCV tree; acute blood loss with the normocytic
#     nonhemolytic anemias; liver disease and chronic alcohol = nonmegaloblastic) · FA 423 (RPI > 3 compensatory, < 2
#     inadequate, formula; Mentzer index < 13 thal trait; iron-studies table) · FA 424 (IDA causes and labs: ↓ iron ↑ TIBC
#     ↓ ferritin ↑ RDW ↓ RI, microcytosis + hypochromasia; α-thal minor = 2 deletions, target cells, often ↑ RBC count) ·
#     FA 425 (β-thal minor ↑ HbA2; lead: ferrochelatase + ALA dehydratase, ↑ protoporphyrin, rRNA retained = basophilic
#     stippling, Burton lines, colic, wrist/foot drop, chelation, exposures; sideroblastic causes, ↑ iron normal/↓ TIBC
#     ↑ ferritin, ringed sideroblasts, stippling, pyridoxine) · FA 426 (megaloblastic: nucleus lags cytoplasm,
#     macrocytosis + hypersegmented PMNs; folate causes, ↑ homocysteine normal MMA, no neuro, weeks–months of stores; B12
#     ↑ MMA, SCD; nonmegaloblastic = alcohol, liver disease, no hypersegmented PMNs) · FA 427 (hemolysis → ↑ LDH, retics,
#     unconjugated bilirubin, pigment stones, urine urobilinogen; intravascular ↓ haptoglobin, schistocytes, hemoglobinuria,
#     hemosiderinuria; extravascular = splenic macrophages, splenomegaly, spherocytes, no hemoglobinuria; ACD IL-6 →
#     hepcidin → ferroportin, ↓ iron ↓ TIBC ↑ ferritin, normocytic → microcytic; aplastic causes, ↓ retic ↑ EPO,
#     pancytopenia, normal morphology, hypocellular fatty marrow) · FA 428 (HS proteins, ↑ MCHC, EMA ↓, extravascular,
#     splenectomy; G6PD oxidants, both kinds of hemolysis, back pain + hemoglobinuria days later, Heinz + bite cells;
#     sickle Glu→Val, both kinds, autosplenectomy → Howell-Jolly) · FA 429 (warm AIHA IgG extravascular, SLE, CLL,
#     β-lactams, α-methyldopa, spherocytes, Coombs +, steroids/rituximab/splenectomy; MAHA: DIC, TTP/HUS, SLE, HELLP,
#     hypertensive emergency, intravascular, schistocytes) · FA 430 (heme synthesis: succinyl-CoA + glycine → ALA synthase,
#     rate-limiting, mitochondria; ferrochelatase the last step; lead → ringed sideroblasts too) · FA 434 (packed RBCs for
#     acute blood loss, ~1 g/dL Hb per unit).
#   Robbins ch 14 (Table 14.2 reticulocytes 0.5–1.5%; acute blood loss: volume first, fluid shift → hemodilution, renal
#     EPO, reticulocytes after ~5 days, 10–15% by day 7, polychromatophilic, iron lost if blood leaves the body; hemolysis:
#     ↑ EPO, extravascular in macrophages of spleen/liver/marrow, splenic cords, variable ↓ haptoglobin even when
#     extravascular, intravascular → haptoglobin depleted, hemoglobinuria, proximal-tubule reabsorption → hemosiderosis;
#     HS: spherocytes trapped in the cords, Coombs negative, ↑ MCHC, splenectomy corrects the anemia; sickle smear: sickled +
#     target cells, Howell-Jolly, reticulocytosis; β-thal minor: hypochromia, microcytosis, stippling, target cells; iron
#     studies exclude IDA; warm AIHA: IgG → Fc receptors → partial phagocytosis → spherocytes, splenomegaly; MAHA:
#     thrombi narrow vessels, shear → schistocytes, helmet cells; megaloblastic: thymidine, nuclear asynchrony,
#     macro-ovalocytes, retic count low, apoptosis in the marrow; iron metabolism: DMT1, ferroportin + hephaestin,
#     transferrin, hepcidin from the liver traps iron in enterocytes and macrophages, falls when stores are low; IDA: stores
#     first, wide central pallor, pencil cells; ACD: IL-6 → hepcidin, iron trapped in macrophages, EPO inappropriately low,
#     normocytic or slightly microcytic; renal failure: ↓ EPO; liver disease: slightly macrocytic — membranes take up
#     cholesterol + phospholipid; normal central pallor ~⅓ of the cell).
#   Guyton ch 33 (reticulocytes leave the marrow by diapedesis, < 1% of RBCs; ~90% of EPO from the kidney, the rest from the
#     liver; splenic red-pulp slits 3 µm; macrophages return iron on transferrin and make bilirubin; blood loss: plasma
#     replaced in 1–3 days, red cells normal again in 3–6 weeks; B12 + folate needed for thymidine triphosphate).
#   Bootcamp.com Hematology & Oncology — Microcytic / Normocytic / Macrocytic anemia (IDA ↓ retic ↑ RDW ↑ transferrin;
#     ACD ↓ retic, MCV mildly reduced; thalassemias normal iron studies; hemolysis ↓ haptoglobin ↑ LDH ↑ indirect
#     bilirubin, usually normal MCV, ↑ EPO → ↑ retics; HS ↓ haptoglobin ↑ indirect bilirubin ↑ retics; G6PD and sickle:
#     ↓ haptoglobin ↑ LDH ↑ bilirubin, ↑ retics; MAHA ↓ haptoglobin ↑ LDH, TTP/HUS thrombocytopenia; CKD: reticulocytopenia,
#     normal hemolysis labs; folate normal MMA; B12 ↑ MMA; liver disease burr + target cells).
# Readout choices where a source gives no single direction (left "–"): TIBC in sideroblastic anemia (FA: normal or ↓);
#   reticulocytes in thalassemia trait, sideroblastic anemia, lead, liver disease (no source for the trait/mild forms —
#   Bootcamp's ↑ retics + hemolysis labs are for thalassemia in general, not trait); LDH/haptoglobin in megaloblastic
#   anemia (Robbins: "a mild degree of hemolysis", no lab direction); iron studies in lead poisoning and acute bleeding.
# Cut for lack of a source / for focus: RDW as a readout
#   (only IDA ↑ and thal "normal" are sourced); LDH as a marker of ineffective erythropoiesis; "coarse" stippling in lead.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

RB14, GY33 = full('Robbins', 14), full('Guyton', 33)
BC_MI = 'Bootcamp.com Hematology & Oncology — Microcytic anemia'
BC_NO = 'Bootcamp.com Hematology & Oncology — Normocytic anemia'
BC_MA = 'Bootcamp.com Hematology & Oncology — Macrocytic anemia'
SRC = [RB14, GY33, BC_MI, BC_NO, BC_MA]

O = lambda *k: ['an:' + x for x in k]
MICRO = O('ida', 'acd', 'thal', 'sidero', 'lead')
MEGA = O('b12', 'fol')
MACRO = MEGA + O('liver')
EXTRA = O('hs', 'aiha')                       # mainly extravascular
BOTH = O('g6pd', 'sickle')                    # both kinds
INTRA = O('maha') + BOTH                      # free Hb in the plasma
SPLEEN = EXTRA + BOTH                         # the macrophage busier
HEMO = EXTRA + INTRA                          # every hemolytic option
LOWRET = O('ida', 'acd', 'aplastic', 'ckd') + MEGA
ALL = MICRO + O('aplastic', 'ckd', 'bleed') + HEMO + MACRO

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
def rrect(x0, y0, x1, y1, r):
    return (f'M{x0 + r} {y0} H{x1 - r} Q{x1} {y0} {x1} {y0 + r} V{y1 - r} Q{x1} {y1} {x1 - r} {y1} '
            f'H{x0 + r} Q{x0} {y1} {x0} {y1 - r} V{y0 + r} Q{x0} {y0} {x0 + r} {y0} Z')
TAG = 'nf-l2 dyn-tag'

# ════════ 1. small intestine: the enterocyte ════════
add('<rect class="dyn-soft" x="150" y="120" width="640" height="395" rx="30"/>')
text('Small intestine', 175, 160, 'dyn-big')
text('duodenum: iron (Fe²⁺) · jejunum: folate · ileum: B12 + intrinsic factor', 175, 182, 'dyn-cap')
add(f'<path d="{rrect(250, 250, 700, 400, 26)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(250, 250, 700, 400, 26), w=16))
text('Enterocyte', 330, 320, 'nf-l1')
text('keeps some iron as mucosal ferritin', 330, 338, 'nf-l2')
text('too little iron in — or lost by bleeding', 175, 500, TAG, when=O('ida'))
text('hepcidin holds iron in the gut cell', 175, 500, TAG, when=O('acd'))
text('no intrinsic factor, gastrectomy, ileal disease, vegan diet', 175, 500, TAG, when=O('b12'))
text('poor diet, alcohol, malabsorption, methotrexate', 175, 500, TAG, when=O('fol'))
# B12 + folate to the marrow (dashed)
add('<path d="M172 236 V905 H292" class="dyn-dash"/>')
text('B12 · folate', 186, 620, 'nf-l2')

# ════════ 2. liver ════════
LIVER = ('M1000 170 C1150 130 1420 135 1550 175 C1580 230 1560 300 1520 350 C1440 420 1300 455 1180 465 '
         'C1080 470 1010 440 995 380 C985 300 975 220 1000 170 Z')
add(f'<path d="{LIVER}" class="dyn-cell" style="stroke:var(--dk9)"/>'
    '<path d="M1270 142 Q1250 300 1290 460" class="dyn-line" style="stroke-width:2"/>')
text('Liver', 1030, 210, 'dyn-big')
text('makes hepcidin · stores ferritin', 1030, 232, 'nf-l2')
add('<ellipse class="dyn-soft" cx="1250" cy="400" rx="70" ry="34"/>')
add('<ellipse cx="1250" cy="400" rx="70" ry="34" class="dyn-dim" fill="var(--surface)"/>', when=O('ida'))
add('<ellipse cx="1250" cy="400" rx="70" ry="34" class="dyn-hl"/>', when=O('acd', 'sidero'))
text('stores empty — ferritin ↓', 1330, 470, TAG, when=O('ida'))
text('stores full — ferritin ↑ (also an acute-phase protein)', 1330, 470, TAG, when=O('acd'))
text('iron piles up — ferritin ↑', 1330, 470, TAG, when=O('sidero'))
text('hepcidin ↑ (IL-6)', 1060, 300, TAG, when=O('acd'))
text('hepcidin ↓ (stores low)', 1060, 300, TAG, when=O('ida'))
# hepcidin to the gut cell's ferroportin and to the macrophage's ferroportin
add('<path d="M1000 430 H648" class="dyn-dash" marker-end="url(#ah-amIron)"/>')
add('<path d="M1555 430 H2120 V872 H2082" class="dyn-dash" marker-end="url(#ah-amIron)"/>')
text('hepcidin ⊣ ferroportin', 1700, 418, 'nf-l2')

# ════════ 3. plasma: iron on transferrin ════════
shapes.append(dict(vessel='M2060 905 V560 H300 V786', w=22, color='--dk10'))
text('Plasma: iron rides on transferrin — TIBC measures transferrin', 1330, 600, 'nf-l2')
text('little iron to carry', 1330, 618, TAG, when=O('ida', 'acd'))
add('<path d="M1250 548 V438" class="dyn-dash"/>')

# ════════ 4. bone marrow: the erythroblast ════════
add('<rect class="dyn-soft" x="150" y="640" width="720" height="650" rx="30"/>')
text('Bone marrow', 330, 680, 'dyn-big')
text('erythroblasts mature, then leave as reticulocytes', 330, 702, 'dyn-cap')
add(f'<path d="{rrect(230, 800, 830, 1190, 40)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(230, 800, 830, 1190, 40), w=18))
text('Erythroblast', 560, 836, 'nf-l1', 'middle')
add('<circle cx="340" cy="1010" r="70" class="dyn-soft"/>')
text('nucleus', 340, 1016, 'dyn-cap', 'middle')
add('<ellipse cx="650" cy="1000" rx="120" ry="46" class="dyn-soft" style="stroke:var(--dk10)"/>')
text('mitochondrion', 650, 1006, 'dyn-cap', 'middle')
# aplastic: fat replaces the marrow; the erythroblast fades
add(''.join(f'<circle cx="{x}" cy="{y}" r="22" class="dyn-soft" style="fill:var(--surface)"/>'
            for x, y in ((190, 760), (240, 1240), (300, 1250), (700, 760), (780, 1240), (840, 1000), (190, 1200), (830, 760))),
    when=O('aplastic'))
add(f'<path d="{rrect(230, 800, 830, 1190, 40)}" class="dyn-dim" fill="var(--surface)"/>', when=O('aplastic'))
text('hypocellular, fatty marrow — every line falls (pancytopenia)', 180, 1276, TAG, when=O('aplastic'))
# ringed sideroblast: iron in the mitochondria around the nucleus
add(''.join(f'<circle cx="{340 + 92 * c}" cy="{1010 + 92 * s}" r="7" fill="var(--dk10)"/>'
            for c, s in ((1, 0), (.87, .5), (.5, .87), (0, 1), (-.5, .87), (-.87, .5), (-1, 0), (-.87, -.5), (.5, -.87), (.87, -.5))),
    when=O('sidero', 'lead'))
text('ringed sideroblasts — iron-laden mitochondria (Prussian blue)', 180, 1276, TAG, when=O('sidero', 'lead'))
text('megaloblasts: the nucleus lags the cytoplasm — many die in the marrow', 180, 1276, TAG, when=MEGA)
text('globin chains short — small cells despite normal iron', 180, 1276, TAG, when=O('thal'))
text('heme short — the cell keeps dividing into a small, pale cell', 180, 1276, TAG, when=O('ida', 'acd'))

# ════════ 5. kidney: EPO ════════
KIDNEY = ('M470 1390 C340 1390 280 1470 280 1545 C280 1625 340 1695 470 1695 C560 1695 620 1655 632 1605 '
          'C602 1588 592 1565 602 1545 C592 1525 602 1502 632 1485 C622 1432 560 1390 470 1390 Z')
add(f'<path d="{KIDNEY}" class="dyn-cell" style="stroke:var(--dk2)"/>')
add('<path d="M612 1600 C600 1660 592 1720 590 1790" class="dyn-line" style="stroke-width:6"/>')
text('Kidney', 330, 1590, 'dyn-big')
text('makes about 90% of EPO', 330, 1612, 'nf-l2')
text('scarred kidney — too little EPO', 300, 1730, TAG, when=O('ckd'))
text('EPO inappropriately low for the anemia', 300, 1730, TAG, when=O('acd'))
text('low O₂ — EPO ↑', 300, 1730, TAG, when=O('bleed', 'aplastic') + HEMO)
add('<path d="M560 1440 V1210" class="dyn-dash" marker-end="url(#ah-amMarrow)"/>')
text('EPO', 572, 1330, 'nf-l1')
# urine
text('Urine', 612, 1824, 'nf-l1')
text('hemoglobinuria · hemosiderinuria', 680, 1824, TAG, when=INTRA)
text('tubules reabsorb Hb and store its iron (hemosiderin)', 660, 1630, TAG, when=INTRA)

# ════════ 6. the circulation ════════
shapes.append(dict(vessel='M830 1000 H1925', w=56, color='--dk2'))
text('Circulating red cells — about 120 days', 900, 958, 'nf-l1')
text('fewer cells — the anemia', 900, 940, TAG, when=ALL)
# acute bleeding: a tear in the vessel
add('<path d="M968 1028 L982 1046 L996 1030 L1010 1048" class="dyn-lesion"/>', when=O('bleed'))
text('whole blood lost — counts lag until fluid shifts in', 1010, 1110, TAG, when=O('bleed'))
# MAHA: microthrombi across small vessels
add(''.join(f'<path d="M{x} 974 L{x + 30} 1026" class="dyn-line" style="stroke:var(--dk8);stroke-width:4"/>' for x in (1190, 1230, 1270))
    + '<circle cx="1215" cy="990" r="9" fill="var(--dk8)"/><circle cx="1262" cy="1012" r="9" fill="var(--dk8)"/>', when=O('maha'))
text('microthrombi shear cells — TTP, HUS, DIC, HELLP', 1150, 940, TAG, when=O('maha'))
text('oxidant → Heinz bodies → cells burst', 1150, 940, TAG, when=O('g6pd'))
text('deoxygenated HbS polymerizes → sickling, vaso-occlusion', 1150, 940, TAG, when=O('sickle'))
text('IgG on the cell — direct Coombs positive', 1150, 940, TAG, when=O('aiha'))
text('membrane shed — cells become spheres', 1150, 940, TAG, when=O('hs'))
add('<path d="M1236 1014 L1250 994 L1264 1014 L1286 1006 L1270 1024 L1286 1042 L1262 1036 L1250 1054 L1238 1036 L1214 1042 L1230 1024 L1214 1006 Z" '
    'class="dyn-hl"/>', when=INTRA)
# free Hb path down to haptoglobin, then to the spleen, and to the kidney when haptoglobin runs out
add('<path d="M1250 1040 V1186" class="dyn-dash"/>', when=INTRA)
add('<path d="M1264 1200 H1830" class="dyn-dash"/>')
add('<path d="M1250 1214 V1560 H640" class="dyn-dash" marker-end="url(#ah-amLysis)"/>', when=INTRA)
text('free Hb beyond haptoglobin → filtered', 1270, 1540, 'nf-l2', when=INTRA)
text('LDH spills from burst cells', 1270, 1310, TAG, when=INTRA)
text('Hb–haptoglobin → macrophages', 1450, 1230, 'nf-l2')

# ════════ 7. spleen: the red-pulp macrophage ════════
SPLEEN_D = ('M1840 820 C1910 770 2120 760 2220 815 C2290 865 2290 1150 2220 1210 C2140 1268 1910 1270 1850 1215 '
            'C1818 1185 1830 1125 1862 1102 C1832 1080 1824 1048 1852 1030 L1852 972 C1822 952 1822 924 1852 906 '
            'C1822 880 1810 850 1840 820 Z')
sp = lambda k: f'<g transform="translate(2060 1015) scale({k}) translate(-2060 -1015)">'
SPL = f'<path d="{SPLEEN_D}" class="dyn-cell" style="stroke:var(--dk7)"/>'
add(SPL, unless=EXTRA)
add(sp(1.08) + SPL + '</g>', when=EXTRA)
text('Spleen', 1880, 812, 'dyn-big')
text('red-pulp slits ~3 µm', 1960, 836, 'nf-l2')
add('<ellipse cx="2045" cy="1010" rx="118" ry="80" class="dyn-soft" style="stroke:var(--dk7)"/>')
text('Macrophage', 2045, 1006, 'nf-l1', 'middle')
text('heme → bilirubin · iron out', 2045, 1024, 'nf-l2', 'middle')
add(''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="var(--dk2)"/>' for x, y in ((1900, 1110), (1930, 1140), (1965, 1118), (2150, 1130), (2180, 1105))),
    when=EXTRA)
text('splenomegaly — spherocytes trapped in the cords', 1880, 1236, TAG, when=EXTRA)
text('spleen infarcts over time — autosplenectomy', 1880, 1236, TAG, when=O('sickle'))
text('macrophages bite out Heinz bodies', 1880, 1236, TAG, when=O('g6pd'))
# bilirubin to the liver
add('<path d="M2165 1010 H2300 V300 H1600" class="dyn-dash" marker-end="url(#ah-amLysis)"/>')
text('unconjugated (indirect) bilirubin → liver', 1700, 286, 'nf-l2')
text('more bilirubin — jaundice, pigment stones', 1700, 266, TAG, when=HEMO)

# ════════ 8. the peripheral smear ════════
add('<rect x="1480" y="1340" width="840" height="470" rx="26" fill="var(--surface)" style="stroke:var(--line-2);stroke-width:2"/>')
text('Peripheral smear', 1510, 1380, 'dyn-big')
RBC = 'fill="var(--dk2)" opacity=".55"'
PALE = 'fill="var(--surface)" opacity=".85"'
def disc(x, y, r=30, pal=.33):
    return f'<circle cx="{x}" cy="{y}" r="{r}" {RBC}/><circle cx="{x}" cy="{y}" r="{r * pal:.1f}" {PALE}/>'
def target(x, y, r=30):
    return f'<circle cx="{x}" cy="{y}" r="{r}" {RBC}/><circle cx="{x}" cy="{y}" r="{r * .62:.1f}" {PALE}/><circle cx="{x}" cy="{y}" r="{r * .28:.1f}" {RBC}/>'
def sphere(x, y, r=21):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--dk2)" opacity=".9"/>'
def stipple(x, y, r=30, pal=.33):
    dots = ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="2.6" fill="var(--dk11)"/>'
                   for dx, dy in ((-14, -8), (-6, -17), (8, -14), (16, -2), (12, 12), (-2, 16), (-15, 8)))
    return disc(x, y, r, pal) + dots
def bite(x, y, r=30):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" {RBC}/><circle cx="{x}" cy="{y}" r="{r * .33:.1f}" {PALE}/>'
            f'<circle cx="{x + r * .95:.1f}" cy="{y - r * .35:.1f}" r="{r * .45:.1f}" fill="var(--surface)"/>')
def heinz(x, y, r=30):
    return disc(x, y, r) + ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="4" fill="var(--ink-3)"/>' for dx, dy in ((-20, -14), (18, 16), (-8, 22)))
def sickle(x, y):
    return f'<path d="M{x - 42} {y + 6} Q{x} {y - 40} {x + 42} {y + 6} Q{x} {y - 16} {x - 42} {y + 6} Z" fill="var(--dk2)" opacity=".8"/>'
def schisto(x, y, k=1):
    return (f'<path d="M{x - 26 * k} {y} A{26 * k} {26 * k} 0 0 1 {x + 26 * k} {y} L{x + 14 * k} {y - 6 * k} L{x} {y + 2 * k} '
            f'L{x - 14 * k} {y - 6 * k} Z" fill="var(--dk2)" opacity=".8"/>')
def burr(x, y, r=28):
    import math
    sp_ = ''.join(f'<path d="M{x + r * math.cos(a):.1f} {y + r * math.sin(a):.1f} L{x + (r + 7) * math.cos(a):.1f} {y + (r + 7) * math.sin(a):.1f}" '
                  f'style="stroke:var(--dk2);stroke-width:3" opacity=".7"/>' for a in [i * math.pi / 8 for i in range(16)])
    return disc(x, y, r) + sp_
def oval(x, y):
    return f'<ellipse cx="{x}" cy="{y}" rx="42" ry="30" fill="var(--dk2)" opacity=".62"/>'
def retic(x, y, r=34):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--dk1)" opacity=".45"/>'
def hj(x, y):
    return target(x, y) + f'<circle cx="{x + 12}" cy="{y + 12}" r="5" fill="var(--ink)"/>'
def neut(x, y):
    lobes = ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="10" fill="var(--dk4)"/>' for dx, dy in ((-24, -6), (-12, -18), (4, -20), (18, -10), (22, 8), (6, 16)))
    return f'<circle cx="{x}" cy="{y}" r="46" fill="var(--dk4)" opacity=".22"/>' + lobes
def pencil(x, y):
    return f'<ellipse cx="{x}" cy="{y}" rx="34" ry="11" fill="var(--dk2)" opacity=".45"/>'
XS = [1590, 1720, 1850, 1980, 2110, 2240]
def row(fns, y):
    return ''.join(f(XS[i], y) for i, f in enumerate(fns) if f)
D = lambda x, y: disc(x, y)
SMEAR = {
  '': (row([D, D, D, D, D, D], 1500) + row([D, D, D, D, D, D], 1630), 'biconcave discs — central pallor about a third of the cell'),
  'ida': (row([lambda x, y: disc(x, y, 21, .62)] * 4 + [pencil, lambda x, y: disc(x, y, 21, .62)], 1500) +
          row([lambda x, y: disc(x, y, 21, .62), pencil] + [lambda x, y: disc(x, y, 21, .62)] * 4, 1630),
          'microcytic, hypochromic — wide central pallor · pencil cells'),
  'acd': (row([lambda x, y: disc(x, y, 26, .4)] * 6, 1500) + row([lambda x, y: disc(x, y, 26, .4)] * 6, 1630),
          'normocytic — or slightly small and pale'),
  'thal': (row([lambda x, y: target(x, y, 22), lambda x, y: stipple(x, y, 22, .4), lambda x, y: target(x, y, 22),
                lambda x, y: disc(x, y, 21, .5), lambda x, y: target(x, y, 22), lambda x, y: stipple(x, y, 22, .4)], 1500) +
           row([lambda x, y: disc(x, y, 21, .5), lambda x, y: target(x, y, 22), lambda x, y: disc(x, y, 21, .5),
                lambda x, y: target(x, y, 22), lambda x, y: disc(x, y, 21, .5), lambda x, y: target(x, y, 22)], 1630),
           'small cells · target cells · basophilic stippling'),
  'sidero': (row([lambda x, y: stipple(x, y, 22, .55), lambda x, y: disc(x, y, 22, .55)] * 3, 1500) +
             row([lambda x, y: disc(x, y, 22, .55), lambda x, y: stipple(x, y, 22, .55)] * 3, 1630),
             'small cells · basophilic stippling (ringed sideroblasts are in the marrow)'),
  'lead': (row([lambda x, y: stipple(x, y, 23, .5)] * 6, 1500) + row([lambda x, y: stipple(x, y, 23, .5), lambda x, y: disc(x, y, 23, .5)] * 3, 1630),
           'basophilic stippling — rRNA left undegraded'),
  'aplastic': (row([D, None, None, D, None, None], 1500) + row([None, None, D, None, None, D], 1630),
               'normal-looking cells — but too few of every kind'),
  'ckd': (row([D, lambda x, y: burr(x, y), D, D, lambda x, y: burr(x, y), D], 1500) + row([D, D, lambda x, y: burr(x, y), D, None, D], 1630),
          'normocytic · burr cells (echinocytes) in end-stage renal disease'),
  'bleed': (row([D, retic, D, D, retic, D], 1500) + row([retic, D, D, retic, D, D], 1630),
            'normal size and color · polychromatophilic reticulocytes from day ~5'),
  'hs': (row([sphere, D, sphere, retic, sphere, sphere], 1500) + row([sphere, sphere, D, sphere, retic, sphere], 1630),
         'spherocytes — small, dense, no central pallor · ↑ MCHC'),
  'g6pd': (row([lambda x, y: bite(x, y), D, heinz, lambda x, y: bite(x, y), D, heinz], 1500) +
           row([D, lambda x, y: bite(x, y), D, heinz, lambda x, y: bite(x, y), D], 1630),
           'bite cells · Heinz bodies (supravital stain)'),
  'sickle': (row([sickle, lambda x, y: target(x, y), sickle, hj, D, sickle], 1500) + row([D, sickle, lambda x, y: target(x, y), sickle, retic, hj], 1630),
             'sickled cells · target cells · Howell-Jolly bodies'),
  'aiha': (row([sphere, D, sphere, sphere, retic, sphere], 1500) + row([D, sphere, sphere, D, sphere, retic], 1630),
           'spherocytes — direct Coombs test positive'),
  'maha': (row([schisto, D, lambda x, y: schisto(x, y, .8), D, schisto, D], 1500) + row([D, schisto, D, lambda x, y: schisto(x, y, .8), D, schisto], 1630),
           'schistocytes — helmet cells (fragments)'),
  'b12': (row([oval, oval, None, oval, oval, None], 1500) + row([oval, None, oval, oval, None, oval], 1630) + neut(2240, 1500) + neut(1850, 1630),
          'macro-ovalocytes · hypersegmented neutrophils'),
  'fol': (row([oval, oval, None, oval, oval, None], 1500) + row([oval, None, oval, oval, None, oval], 1630) + neut(2240, 1500) + neut(1850, 1630),
          'macro-ovalocytes · hypersegmented neutrophils'),
  'liver': (row([lambda x, y: disc(x, y, 38, .3), lambda x, y: target(x, y, 36), lambda x, y: disc(x, y, 38, .3),
                 lambda x, y: burr(x, y, 34), lambda x, y: target(x, y, 36), lambda x, y: disc(x, y, 38, .3)], 1500) +
            row([lambda x, y: target(x, y, 36), lambda x, y: disc(x, y, 38, .3), lambda x, y: target(x, y, 36),
                 lambda x, y: disc(x, y, 38, .3), lambda x, y: burr(x, y, 34), lambda x, y: target(x, y, 36)], 1630),
            'macrocytes · target and burr cells · no hypersegmented neutrophils'),
}
for k, (svg, cap) in SMEAR.items():
    if k: add(svg, when=O(k)); text(cap, 1510, 1770, TAG, when=O(k))
    else: add(svg, unless=ALL); text(cap, 1510, 1770, TAG, unless=ALL)

# ════════ particles ════════
kinds = dict(rbc=['rbc', '--dk2'], retic=['retic', '--dk1'], fe=['iron', '--dk10'], epo=['epo', '--dk3'], hep=['hep', '--dk4'],
             b12=['b12', '--dk6'], fol=['fol', '--dk9'], hb=['hb', '--dk7'], hphb=['hphb', '--dk8'], bili=['bili', '--dk5'])
# one colour per group, so every dot in the Key row has its own name
groups = [['rbc', 'Red cells'], ['retic', 'Reticulocytes'], ['iron', 'Iron'], ['epo', 'EPO'], ['hep', 'Hepcidin'], ['b12', 'B12'],
          ['fol', 'Folate'], ['hb', 'Free Hb'], ['hphb', 'Hb–haptoglobin'], ['bili', 'Bilirubin']]

def m(when, **kw):
    return dict(when=when if isinstance(when, list) else [when], **kw)
CIRC = 'M840 1000 H1925'
flows = [
  # red cells round the circulation into the splenic macrophage; size follows the MCV
  dict(d=CIRC, len=1085, speed=120, r=7, base=dict(rbc=9), unless=MICRO + MACRO, mods=[
      m(O('aplastic'), set=dict(rbc=3)), m(O('ckd', 'bleed') + HEMO, set=dict(rbc=6))]),
  dict(d=CIRC, len=1085, speed=120, r=5, base=dict(rbc=6), when=MICRO),
  dict(d=CIRC, len=1085, speed=120, r=9.5, base=dict(rbc=5), when=MACRO),
  # reticulocytes leaving the marrow
  dict(d='M840 1000 H1150', len=310, speed=80, r=8, base=dict(retic=2), mods=[
      m(LOWRET, set=dict(retic=1)), m(O('aplastic'), set=dict(retic=0)), m(HEMO + O('bleed'), set=dict(retic=5))]),
  # iron: gut cell → plasma, plasma → marrow, macrophage → plasma, plasma ⇄ liver stores, into the mitochondrion
  dict(d='M620 412 V548', len=136, speed=70, base=dict(fe=2), mods=[m(O('ida'), set=dict(fe=1)), m(O('acd'), set=dict(fe=0))]),
  dict(d='M2060 905 V560 H300 V786', len=345 + 1760 + 226, speed=150, base=dict(fe=6), mods=[
      m(O('ida', 'acd'), set=dict(fe=2)), m(O('sidero'), set=dict(fe=9))]),
  dict(d='M1250 548 V438', len=110, speed=50, base=dict(fe=1), mods=[m(O('ida'), set=dict(fe=0)), m(O('acd', 'sidero'), set=dict(fe=3))]),
  dict(d='M300 830 H790 V1046 H740', len=490 + 216 + 50, speed=90, base=dict(fe=2), mods=[
      m(O('ida', 'acd'), set=dict(fe=1)), m(O('sidero', 'lead'), set=dict(fe=4)), m(O('aplastic'), set=dict(fe=0))]),
  # EPO: kidney → marrow
  dict(d='M560 1440 V1210', len=230, speed=90, base=dict(epo=2), mods=[
      m(O('ckd'), set=dict(epo=0)), m(O('acd'), set=dict(epo=1)), m(O('aplastic', 'bleed') + HEMO, set=dict(epo=5))]),
  # B12 and folate → the nucleus
  dict(d='M172 236 V905 H292', len=669 + 120, speed=130, base=dict(b12=2, fol=2), mods=[
      m(O('b12'), set=dict(b12=0)), m(O('fol'), set=dict(fol=0))]),
  # hepcidin → both ferroportins
  dict(d='M1000 430 H648', len=352, speed=90, base=dict(hep=1), mods=[m(O('acd'), set=dict(hep=5)), m(O('ida'), set=dict(hep=0))]),
  dict(d='M1555 430 H2120 V872 H2082', len=565 + 442 + 38, speed=140, base=dict(hep=1), mods=[m(O('acd'), set=dict(hep=6)), m(O('ida'), set=dict(hep=0))]),
  # bilirubin → liver
  dict(d='M2165 1010 H2300 V300 H1600', len=135 + 710 + 700, speed=150, base=dict(bili=3), mods=[m(HEMO, set=dict(bili=9))]),
  # intravascular: free Hb → haptoglobin → (macrophages); beyond haptoglobin → kidney → urine
  dict(d='M1250 1040 V1186', len=146, speed=60, when=INTRA, base=dict(hb=4)),
  dict(d='M1264 1200 H1830', len=566, speed=100, base=dict(hphb=1), mods=[m(INTRA, set=dict(hphb=4)), m(EXTRA, set=dict(hphb=2))]),
  dict(d='M1250 1214 V1560 H640', len=346 + 610, speed=120, when=INTRA, base=dict(hb=5)),
  dict(d='M612 1600 C600 1660 592 1720 590 1790', len=192, speed=60, when=INTRA, base=dict(hb=2)),
  # bleeding out
  dict(d='M990 1028 V1190', len=162, speed=80, r=7, when=O('bleed'), base=dict(rbc=5)),
]

# ════════ sites ════════
sites = [
  dict(x=380, y=250, n=[0, -1], w=16, t='co', l='DMT1', s='Fe²⁺ into the gut cell', ions=[['fe', 'in', 1]], reach=40,
       lx=410, ly=222, la='start', c='ironcycle', low=O('ida'), sfx=dict(low=' — little iron in')),
  dict(x=620, y=400, n=[0, 1], w=16, t='co', l='Ferroportin', s='iron out to transferrin', ions=[['fe', 'out', 1]], reach=30,
       lx=600, ly=446, la='end', c='ironcycle', low=O('acd'), sfx=dict(low=' — degraded by hepcidin')),
  dict(x=1000, y=400, n=[1, 0], w=16, t='ex', l='Hepcidin made', s='rises with iron and inflammation', ions=[['hep', 'out', 1]], reach=30,
       lx=1030, ly=258, la='start', c='hemochrom', boost=O('acd'), low=O('ida'), sfx=dict(boost=' — IL-6 drives it', low=' — falls')),
  dict(x=1250, y=434, n=[0, -1], w=14, t='ex', l='Ferritin stores', s='storage iron', ions=[['fe', 'in', 1]], reach=24,
       lx=1335, ly=392, la='start', c='ironstudies', low=O('ida'), boost=O('acd', 'sidero'), sfx=dict(low=' — empty', boost=' — full')),
  dict(x=1600, y=300, n=[1, 0], w=14, t='ex', l='Conjugation', s='bilirubin → bile', ions=[['bili', 'in', 1]], reach=26,
       lx=1580, ly=346, la='start', c='bilicycle', boost=HEMO, sfx=dict(boost=' — swamped')),
  dict(x=300, y=800, n=[0, -1], w=18, t='rec', l='Transferrin uptake', s='iron enters by endocytosis', ions=[['fe', 'in', 1]], reach=28,
       lx=322, ly=758, la='start', c='ironcycle', low=O('ida', 'acd'), stop=O('aplastic')),
  dict(x=340, y=940, n=[0, -1], w=14, t='ex', l='DNA synthesis', s='B12 + folate → thymidine', ions=[['b12', 'in', 1], ['fol', 'in', 1]], reach=40,
       c='folatetrap', block=MEGA, stop=O('aplastic'), sfx=dict(block=' — stalled')),
  dict(x=590, y=954, n=[0, -1], w=14, t='ex', l='ALA synthase', s='glycine + succinyl-CoA', ions=[], c='hemesynth',
       low=O('sidero'), stop=O('aplastic'), sfx=dict(low=' — defective')),
  dict(x=720, y=1046, n=[0, 1], w=14, t='ex', l='Ferrochelatase', s='protoporphyrin + Fe²⁺ → heme', ions=[['fe', 'in', 1]], reach=24,
       c='hemesynth', block=O('lead'), low=O('ida', 'acd'), stop=O('aplastic'), sfx=dict(low=' — short of iron')),
  dict(x=430, y=1110, n=[0, 1], w=14, t='ex', l='Globin chains', s='α₂β₂ in HbA', ions=[], c='hbtypes',
       low=O('thal'), stop=O('aplastic'), sfx=dict(low=' — too few made')),
  dict(x=560, y=1190, n=[0, 1], w=18, t='rec', l='EPO receptor', s='drives proliferation', ions=[['epo', 'in', 1]], reach=30,
       lx=600, ly=1232, la='start', c='esa', low=O('ckd', 'acd'), boost=O('bleed') + HEMO, stop=O('aplastic'),
       sfx=dict(stop=' — no stem cells answer')),
  dict(x=830, y=1000, n=[1, 0], w=18, t='para', l='Reticulocytes out', s='< 1% of red cells normally', ions=[['retic', 'out', 1]], reach=30,
       lx=880, ly=1062, la='start', c='reticindex', low=LOWRET, boost=O('bleed') + HEMO, stop=O('aplastic'),
       sfx=dict(low=' — few', boost=' — many', stop=' — almost none')),
  dict(x=560, y=1450, n=[0, 1], w=14, t='ex', l='EPO-making cells', s='sense low O₂', ions=[['epo', 'out', 1]], reach=22,
       lx=535, ly=1492, la='end', c='ckdanemia', low=O('ckd', 'acd'), boost=O('bleed', 'aplastic') + HEMO),
  dict(x=1925, y=1000, n=[-1, 0], w=18, t='rec', l='Red cells eaten', s='old (120 d) or misshapen cells', ions=[['rbc', 'in', 1]], reach=30,
       lx=1890, ly=1160, la='start', c='hemolysislabs', boost=SPLEEN, sfx=dict(boost=' — many more')),
  dict(x=2060, y=930, n=[0, -1], w=16, t='co', l='Ferroportin', s='iron back to transferrin', ions=[['fe', 'out', 1]], reach=26,
       lx=2036, ly=896, la='end', c='acd', low=O('acd'), sfx=dict(low=' — iron trapped')),
  dict(x=1250, y=1028, n=[0, 1], w=18, t='para', l='Lysis in the vessel', s='free Hb, LDH released', ions=[['hb', 'out', 1]], reach=30,
       lx=1272, ly=1076, la='start', c='hemolysislabs', need=INTRA, closed='rare in health', boost=INTRA, sfx=dict(boost=' — cells burst')),
  dict(x=1250, y=1200, n=[-1, 0], w=16, t='rec', l='Haptoglobin', s='binds free Hb', ions=[['hphb', 'out', 1]], reach=24,
       lx=1272, ly=1250, la='start', c='hemolysislabs', boost=HEMO, sfx=dict(boost=' — used up')),
]

notes = {
  '': 'Healthy: EPO from the kidney drives erythroblasts, which build hemoglobin from heme (iron + protoporphyrin) and globin and '
      'need B12 and folate to copy DNA. Reticulocytes leave for the blood and live about 120 days; splenic macrophages then send '
      'the iron back on transferrin and turn heme into bilirubin. Pick a cause and read the results.',
  'an:ida': 'Iron deficiency (chronic GI or menstrual bleeding, poor intake, malabsorption, pregnancy): stores empty first, then serum '
            'iron falls and transferrin rises — ferritin ↓, TIBC ↑. Too little heme leaves small, pale cells: microcytic and '
            'hypochromic with a wide central pallor, pencil cells, ↑ RDW and few reticulocytes.',
  'an:acd': 'Anemia of chronic disease (infection, cancer, autoimmune disease, CKD): IL-6 makes the liver release hepcidin, which '
            'degrades ferroportin — iron is locked in macrophages and gut cells, and EPO is inappropriately low. Iron ↓, TIBC ↓, '
            'ferritin ↑; the cells are normocytic or mildly microcytic.',
  'an:thal': 'Thalassemia trait (β minor with ↑ HbA2; α minor with two α genes lost): too few globin chains make small cells while '
             'iron stores are normal. Microcytic with target cells and basophilic stippling, normal ferritin and TIBC; a Mentzer '
             'index (MCV ÷ RBC count) under 13 favors trait over iron deficiency.',
  'an:sidero': 'Sideroblastic anemia (X-linked ALA synthase defect; alcohol, lead, B6 deficiency, isoniazid, myelodysplasia): heme '
               'synthesis stalls in the mitochondria, so iron piles up there — ringed sideroblasts on Prussian blue. Iron and '
               'ferritin ↑, TIBC normal or low, basophilic stippling; pyridoxine treats it.',
  'an:lead': 'Lead poisoning (old paint in children, batteries or ammunition at work): lead blocks ALA dehydratase and ferrochelatase, '
             'so protoporphyrin builds up, and stops rRNA breakdown — basophilic stippling, ringed sideroblasts. Burton lines, '
             'colic, wrist or foot drop; chelate with succimer, EDTA or dimercaprol.',
  'an:aplastic': 'Aplastic anemia (radiation, benzene, chloramphenicol, alkylating agents, viruses, Fanconi anemia, idiopathic): stem '
                 'cells fail, so the marrow is hypocellular and fatty and every line falls — pancytopenia. EPO is high but nothing '
                 'answers: reticulocytes ↓, cells normocytic and normal in shape.',
  'an:ckd': 'Anemia of chronic kidney disease: the damaged kidneys make too little EPO, so the marrow is never pushed — a normocytic '
            'anemia with low reticulocytes and normal hemolysis labs; burr cells (echinocytes) may appear in end-stage renal '
            'disease. Recombinant EPO, with iron, treats it.',
  'an:bleed': 'Acute blood loss: at first the cells are normal in size and color — the hematocrit falls only as fluid moves in to '
              'restore volume. Low O₂ raises EPO, and about 5 days later reticulocytes pour out (10–15% by day 7, larger and '
              'polychromatophilic); blood lost from the body also takes its iron.',
  'an:hs': 'Hereditary spherocytosis (ankyrin, band 3, protein 4.2, spectrin): membrane is shed until the cells are spherocytes that '
           'cannot squeeze out of the splenic cords — extravascular hemolysis, splenomegaly, ↑ MCHC, Coombs negative, ↓ EMA binding. '
           'Retics, LDH and indirect bilirubin ↑, haptoglobin ↓; splenectomy corrects the anemia.',
  'an:g6pd': 'G6PD deficiency: no NADPH, no reduced glutathione — an oxidant (sulfa drugs, antimalarials, fava beans, infection) '
             'denatures hemoglobin into Heinz bodies, which splenic macrophages bite out (bite cells). Hemolysis is both intra- and '
             'extravascular: hemoglobinuria and back pain a few days later, haptoglobin ↓, LDH ↑.',
  'an:sickle': 'Sickle cell anemia (HbS, glutamic acid → valine): deoxygenated HbS polymerizes, cells sickle and block small vessels, '
               'and hemolysis is both extravascular and intravascular. Sickled and target cells, Howell-Jolly bodies after '
               'autosplenectomy; reticulocytes, LDH and indirect bilirubin ↑, haptoglobin ↓.',
  'an:aiha': 'Warm autoimmune hemolytic anemia (idiopathic, SLE, CLL, penicillins, cephalosporins, α-methyldopa): IgG coats the red '
             'cells, splenic macrophages nibble membrane away, and the spherocytes die in the spleen — mainly extravascular. Direct '
             'Coombs positive, spherocytes, splenomegaly; steroids, rituximab, splenectomy if refractory.',
  'an:maha': 'Microangiopathic hemolytic anemia (TTP, HUS, DIC, HELLP, malignant hypertension): microthrombi narrow small vessels '
             'and shear passing cells into schistocytes (helmet cells) — intravascular hemolysis. Free Hb uses up haptoglobin and '
             'spills into the urine; LDH ↑, and platelets fall in TTP and HUS.',
  'an:b12': 'B12 deficiency (pernicious anemia — no intrinsic factor — gastrectomy, ileal disease, veganism, fish tapeworm, '
            'metformin): thymidine runs short, so the nucleus lags the cytoplasm — megaloblasts, many dying in the marrow. '
            'Macro-ovalocytes, hypersegmented neutrophils, few reticulocytes; MMA and homocysteine ↑, subacute combined degeneration.',
  'an:fol': 'Folate deficiency (alcohol, poor diet, pregnancy, hemolysis, methotrexate, trimethoprim, phenytoin): the same '
            'megaloblastic picture — macro-ovalocytes, hypersegmented neutrophils, few reticulocytes. Homocysteine ↑ but '
            'methylmalonic acid normal and no neurologic signs; stores last only weeks to months.',
  'an:liver': 'Non-megaloblastic macrocytosis (chronic alcohol use, liver disease): DNA synthesis is normal, so there are no '
              'megaloblasts or hypersegmented neutrophils. In liver disease the membranes take up extra cholesterol and '
              'phospholipid and the cells grow — macrocytes with target and burr cells.',
}

R = lambda when, d: dict(when=when if isinstance(when, list) else [when], d=d)
readouts = [
  dict(l='MCV', mods=[R(MICRO, -1), R(O('aplastic', 'ckd', 'bleed') + HEMO, 0), R(MACRO, 1)]),
  dict(l='Reticulocytes', mods=[R(LOWRET, -1), R(O('bleed') + HEMO, 1)]),
  dict(l='Ferritin', mods=[R(O('ida'), -1), R(O('acd', 'sidero'), 1), R(O('thal'), 0)]),
  dict(l='TIBC', mods=[R(O('ida'), 1), R(O('acd'), -1), R(O('thal'), 0)]),
  dict(l='LDH · bilirubin', mods=[R(HEMO, 1), R(O('ckd'), 0)]),
  dict(l='Haptoglobin', mods=[R(HEMO, -1), R(O('ckd'), 0)]),
  dict(l='MMA', mods=[R(O('b12'), 1), R(O('fol'), 0)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='an', label='Cause', type='one', options=[
                ['ida', 'Iron deficiency', 'ida'], ['acd', 'Anemia of chronic disease', 'acd'],
                ['thal', 'Thalassemia trait (α or β)', 'betathal'], ['sidero', 'Sideroblastic anemia', 'sidero'],
                ['lead', 'Lead poisoning', 'lead'],
                ['aplastic', 'Aplastic anemia', 'aplastic'], ['ckd', 'Chronic kidney disease', 'ckdanemia'],
                ['bleed', 'Acute blood loss (a week on)', 'acutebloodloss'],
                ['hs', 'Hereditary spherocytosis', 'hs'], ['g6pd', 'G6PD deficiency', 'g6pd'], ['sickle', 'Sickle cell anemia', 'sickle'],
                ['aiha', 'Warm autoimmune hemolysis', 'warmaiha'], ['maha', 'Microangiopathic (TTP, HUS, DIC)', 'ttp'],
                ['b12', 'B12 deficiency', 'b12def'], ['fol', 'Folate deficiency', 'b9def'],
                ['liver', 'Liver disease · alcohol', 'nonmegalo']],
                 sections=[['Microcytic — MCV < 80', ['ida', 'acd', 'thal', 'sidero', 'lead']],
                           ['Normocytic — not hemolysis', ['aplastic', 'ckd', 'bleed']],
                           ['Normocytic — hemolysis', ['hs', 'g6pd', 'sickle', 'aiha', 'maha']],
                           ['Macrocytic — MCV > 100', ['b12', 'fol', 'liver']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 67, 209, 381, 413, 420–430, 434, 607 · Robbins ch 14 · Guyton ch 33 · Bootcamp Hematology')

# ════════ the one new card: a real gap (First Aid lists acute blood loss; no card covered it) ════════
card('acutebloodloss', 'Acute blood loss anemia', 'dz', 'amLoss', 'Hemorrhage — volume is lost first, red cells show it later', 1,
     'The first danger of acute bleeding is the lost <b>intravascular volume</b> — if massive, shock and death. If the patient '
     'survives, water moves from the interstitial fluid into the vessels within 1–3 days, diluting the blood so the hematocrit '
     'falls. The hypoxia raises renal <b>erythropoietin</b>, and about 5 days later new reticulocytes reach the blood.',
     ['Early red cells are normocytic and normochromic — the counts lag the bleed',
      'Reticulocytosis reaching 10–15% after about 7 days; reticulocytes are larger and polychromatophilic',
      'If blood pressure falls, adrenergic release mobilizes marginated granulocytes (leukocytosis); thrombocytosis is common in early recovery',
      'Blood lost into the gut or out of the body takes its iron and can end in iron deficiency',
      'Without further bleeding the red cell count is usually normal again within 3–6 weeks'],
     ['Normocytic anemia that deepens over the first days as plasma volume is restored', 'Reticulocytes ↑ from about day 5'],
     ['After an acute bleed the hematocrit falls only once fluid shifts in'],
     [RB14, GY33],
     ['Restore volume; packed red cells for acute blood loss (each unit raises hemoglobin about 1 g/dL)'],
     ['acute blood loss', 'acute blood loss anemia', 'anemia of acute blood loss', '=blood loss anemia'],
     fa='422, 434')

MAP = dict(
  id='anemsim', title='Anemia Work-up in Motion', topic='heme', after='ironflow',
  sub='Iron from the gut on transferrin, heme and globin and DNA built in the marrow erythroblast on EPO\'s signal, reticulocytes '
      'into the blood for 120 days, then the splenic macrophage or lysis in the vessel — pick a cause and read the MCV, '
      'reticulocytes, ferritin, TIBC, LDH, haptoglobin and MMA beside a smear. Tap a transporter or enzyme for its card',
  w=3500, h=1900,
  fa='67, 209, 381, 413, 420–430, 434, 607', src=SRC,
  lanes=[('amIron', 'Iron & heme', 'glycogen'), ('amMarrow', 'Marrow, EPO & DNA', 'ppp'), ('amLysis', 'Red cell destruction', 'tca'),
         ('amLoss', 'Blood loss', 'sugars')],
  comps=[],
  nodes=[
    ('am1', 'Classifying anemia', 1880, 150, 'amMarrow', 'MCV · reticulocytes', ['anemiaapproach', 'reticindex'], 'hub'),
    ('am2', 'Iron in and out', 1880, 215, 'amIron', 'DMT1 · ferroportin · transferrin', ['ironcycle', 'ironstudies', 'ironrx']),
    ('am3', 'Iron-poor vs iron-locked', 1030, 660, 'amIron', 'deficiency · chronic disease · overload', ['ida', 'acd', 'hemochrom']),
    ('am4', 'B12 · folate', 1060, 780, 'amMarrow', 'megaloblastic · non-megaloblastic', ['b12def', 'b9def', 'mmacid', 'folatetrap', 'nonmegalo']),
    ('am5', 'Immune & mechanical', 1560, 860, 'amLysis', 'AIHA · TTP · HUS · DIC · PNH', ['warmaiha', 'coldaiha', 'antiglobulin', 'ttp', 'ahus', 'dic', 'pnh']),
    ('am6', 'Heme & globin', 960, 1340, 'amIron', 'lead · sideroblastic · thalassemias', ['hemesynth', 'lead', 'sidero', 'betathal', 'alphathal', 'hbtypes']),
    ('am7', 'Marrow failure', 960, 1430, 'amMarrow', 'aplastic · pure red cell aplasia', ['aplastic', 'fanconi', 'dba', 'parvo', 'myelophthisic']),
    ('am8', 'EPO & the kidney', 1000, 1700, 'amMarrow', 'CKD · ESA therapy', ['ckdanemia', 'esa']),
    ('am9', 'Acute blood loss', 1010, 1250, 'amLoss', 'volume first, retics by day 5–7', ['acutebloodloss', 'hypovshock', 'bloodproducts']),
    ('am10', 'Where red cells die', 1620, 1140, 'amLysis', 'extravascular vs intravascular', ['hemolysislabs', 'bilicycle', 'jaundice', 'transfusion'], 'hub'),
    ('am11', 'Membrane · enzyme · Hb', 2000, 1300, 'amLysis', 'spherocytosis · G6PD · sickle', ['hs', 'g6pd', 'pkdef', 'sickle', 'sickletrait', 'hbc', 'asplenia']),
  ],
  panels=[
    # placed low enough for the main kit's sectioned chips (four sub-headings add ~230 px over check.py's estimate)
    (2420, 940, 1000, 'Where the red cell dies (First Aid pp. 427–428; Robbins ch 14)', [
      ('Extravascular', 'splenic macrophages · splenomegaly · spherocytes · no hemoglobinuria'),
      ('Intravascular', 'haptoglobin used up · hemoglobinuria · hemosiderinuria · schistocytes'),
      ('Both show', 'LDH ↑ · reticulocytes ↑ · unconjugated bilirubin ↑ · pigment stones'),
      ('Both kinds at once', 'sickle cell anemia · G6PD deficiency')]),
    (2420, 1110, 1000, 'Reading the reticulocytes (First Aid p. 423; Robbins ch 14)', [
      ('Normal', 'about 0.5–1.5% of red cells'),
      ('Index > 3', 'the marrow is compensating — hemolysis, or recovery from a bleed'),
      ('Index < 2', 'inadequate response — marrow, iron, B12/folate or EPO short'),
      ('Index', 'retic % × (Hct ÷ normal Hct) ÷ maturation time'),
      ('Mentzer index', 'MCV ÷ RBC count — under 13 favors thalassemia trait')]),
  ],
  dyn=dyn,
)
