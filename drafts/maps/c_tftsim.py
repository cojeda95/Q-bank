# m51 — Thyroid Function Tests in Motion (dynamic map, kit data)
# The whole hypothalamic–pituitary–thyroid axis, drawn for READING LAB PATTERNS (follflow shows the follicle's chemistry,
# thytsim the tumors): TRH neuron → portal veins → thyrotroph (TSH) → thyroid (T4 ≫ T3) → blood (a free lane and a
# TBG-bound reservoir lane, with the liver that makes TBG) → target cell (5′-deiodinase T4 → T3 / reverse T3 → nuclear
# receptor) → free hormone feeding back on the thyrotroph and the TRH neuron. One `one` switch picks a pattern, grouped
# in `sections` (primary · central · hormone pills · binding protein · other); each option changes the particle traffic,
# the feedback vessels (thin and dim when free hormone is low, wide when it is high), the gland's size and the captions,
# and reads out TSH, free T4, total T4, total T3, TBG and radioactive iodine uptake.
#
# Sources (all read in the corpus):
#   First Aid 2025 p. 332 (TRH ↑ TSH and prolactin; ↑ TRH in 1°/2° hypothyroidism may raise prolactin; somatostatin and
#     dopamine ↓ TSH) · p. 335 (T4 the major product; 5′-deiodinase in tissues; only free hormone active; feedback by free
#     T3/T4 on pituitary and hypothalamus; TBG binds most; ↑ TBG pregnancy/OCP → ↑ total T3/T4; ↓ TBG steroids, nephrotic)
#     · p. 343 (hypopituitarism causes: hypothalamic disease, pituitary surgery, masses, empty sella, Sheehan) · p. 344
#     (1° hypo: TSH ↑ free T4 ↓; 1° hyper: TSH ↓ free T3/T4 ↑; symptoms) · p. 345 (Hashimoto; nonthyroidal illness:
#     ↓ T3 with normal/↓ T4 and TSH) · p. 346 (Graves TSI; diffuse goiter causes incl. TSH-secreting pituitary adenoma;
#     exogenous thyrotoxicosis) · p. 360 (levothyroxine / liothyronine; RAIU separates exogenous from endogenous).
#   Costanzo ch 9 (TRH from PVN via portal blood; TSH via cAMP drives every step incl. I⁻ uptake + trophic effect; feedback
#     by down-regulating TRH receptors, anterior lobe has deiodinase; Table 9.9 TSH by cause: Graves/neoplasm/exogenous
#     T3 or T4 → TSH ↓, excess TSH → TSH ↑; primary hypo → TSH ↑, hypothalamic/pituitary → TSH ↓; goiter rules: TSH-
#     secreting tumor goiter, factitious → gland involutes, TSH deficiency → no goiter; TBG: pregnancy (estrogen slows
#     hepatic breakdown) total ↑ free normal, hepatic failure total ↓ free near-normal; starvation inhibits 5′-iodinase;
#     target tissue resistance — cause mentioned only, no lab pattern).
#   Guyton ch 77 (93% T4 / 7% T3; >99% bound to liver-made TBG, prealbumin, albumin; T3 ~4× potent; TRH tripeptide from
#     PVN via portal blood, Gq/phospholipase; blocked portal blood → TSH falls greatly but not to zero; feedback mainly on
#     the pituitary, also on TRH; Graves TSI → TSH almost absent; TRH test dose raises TSH in hypothyroidism except when
#     the pituitary cannot respond).
#   Katzung ch 38 (Table 38-1 free fraction 0.04% T4 / 0.4% T3, half-lives 7 d / 1 d; 80% of T3 from tissues; T3 3–4×
#     potent; Table 38-2 TFTs in hypo/hyper incl. total T3 "normal or low" in hypothyroidism and ¹²³I uptake low/high;
#     Table 38-3 drugs: ↑ TBG estrogens, tamoxifen, raloxifene, methadone…; ↓ TBG androgens, anabolic steroids,
#     glucocorticoids…; deiodinase blockers; ↓ TSH secretion dopamine, corticosteroids, somatostatin, octreotide;
#     hepatic inducers; severe illness/starvation inhibit 5′-deiodinase → T3 ↓ rT3 ↑; secondary hypothyroidism: no goiter;
#     subclinical hypo = ↑ TSH, normal hormone, 4–10% (20% of women > 50), treat > 10 mIU/L; subclinical hyper =
#     suppressed TSH, normal hormone, AF risk, treat < 0.1 mIU/L; Graves labs; chronic T4 excess → AF, osteoporosis).
# Cut for lack of a sourced lab pattern: thyroid hormone resistance (Costanzo and Katzung name it, neither gives labs).
# Uptake / T4 arrows that no textbook prints directly, now sourced (owner asked, 2026-10-18):
#   liothyronine excess → free T4 ↓ (Jonklaas 2014 ATA hypothyroidism guideline, PMID 25266247: "LT3 therapy induced
#     subclinical hyperthyroidism based on lower FT4 and TSH levels"); total T4 follows; RAIU ↓ (De Leo 2016 Lancet,
#     PMID 27038492, Table 1: excess exogenous thyroid hormone = thyrotoxicosis without hyperthyroidism, low RAIU)
#   levothyroxine excess → RAIU ↓ (same Table 1); TSH-secreting adenoma → RAIU normal or ↑ (same Table 1: "thyrotoxicosis
#     with hyperthyroidism (normal or high radioactive iodine uptake)")
#   central (secondary/tertiary) hypothyroidism → RAIU ↓ (Guyton ch 77: "TSH stimulates and hypophysectomy greatly
#     diminishes activity of the iodide pump in thyroid cells"). The refs sit on the thyroiddrugs and pitnet cards.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

CZ9, GY77, KZ38 = full('Costanzo', 9), full('Guyton', 77), full('Katzung', 38)
SRC = [CZ9, GY77, KZ38]

O = lambda *k: ['tft:' + x for x in k]
HYPO_LOW = O('hashi', 'sec', 'ter')                 # free hormone low → feedback weak
HIGH = O('graves', 'tshoma', 'lt4')                 # free T4 and T3 high → feedback strong
FB_HIGH = HIGH + O('lt3')                           # T3 high (lt3: T3 only)
BIG = O('hashi', 'graves', 'tshoma')                # goiter
SMALL = O('lt4', 'lt3')                             # the suppressed gland involutes
NORM = O('subhypo', 'subhyper', 'tbghi', 'tbglo', 'sick')   # free hormone normal

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

# ════════ 1. hypothalamus: the TRH neuron ════════
add('<rect class="dyn-soft" x="520" y="120" width="760" height="330" rx="40"/>')
text('Hypothalamus', 550, 165, 'dyn-big')
text('paraventricular nucleus', 550, 185, 'dyn-cap')
add('<path d="M900 350 V468" class="dyn-line" stroke-width="7"/><circle cx="900" cy="470" r="11" class="dyn-cell"/>')
add(f'<path d="{rrect(790, 230, 1010, 350, 30)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(790, 230, 1010, 350, 30), w=18))
text('TRH neuron', 900, 286, 'nf-l1', 'middle')
text('TRH: a tripeptide · cold ⊕', 900, 304, 'nf-l2', 'middle')
add(f'<path d="{rrect(790, 230, 1010, 350, 30)}" class="dyn-dim" fill="var(--surface)"/>', when=O('ter'))
add('<path d="M820 250 L980 330 M980 250 L820 330" class="dyn-lesion"/>', when=O('ter'))
text('TRH ↑ — feedback lost', 880, 400, TAG, 'end', when=O('hashi', 'sec'))
text('TRH ↓ — strong feedback', 880, 400, TAG, 'end', when=O('graves', 'lt4', 'lt3'))
text('damaged — mass, radiation, infiltration', 880, 400, TAG, 'end', when=O('ter'))
text('axon to the median eminence', 920, 430, 'dyn-cap')

# ════════ 2. portal veins and the anterior pituitary ════════
shapes.append(dict(vessel='M900 482 V676', w=20))
text('Hypophyseal portal veins', 880, 590, 'nf-l2', 'end')
add('<ellipse class="dyn-soft" cx="900" cy="840" rx="340" ry="165"/>')
text('Anterior pituitary', 590, 790, 'dyn-big')
add(f'<path d="{rrect(780, 760, 1020, 920, 34)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(780, 760, 1020, 920, 34), w=18))
text('Thyrotroph', 900, 832, 'nf-l1', 'middle', unless=O('tshoma'))
text('TSH-secreting adenoma', 900, 832, 'nf-l1', 'middle', when=O('tshoma'))
text('makes TSH · senses free hormone', 900, 852, 'nf-l2', 'middle')
add(f'<path d="{rrect(766, 746, 1034, 934, 42)}" class="dyn-lesion"/>', when=O('tshoma'))
add('<path d="M805 785 L995 895 M995 785 L805 895" class="dyn-lesion"/>', when=O('sec'))
text('thyrotrophs lost — mass, surgery, Sheehan', 880, 1040, TAG, 'end', when=O('sec'))
text('TSH ↑ — no feedback brake', 880, 1040, TAG, 'end', when=O('hashi'))
text('TSH ↑ — the tumor makes it', 880, 1040, TAG, 'end', when=O('tshoma'))
text('TSH almost zero — suppressed', 880, 1040, TAG, 'end', when=O('graves', 'lt4', 'lt3'))
text('TSH low — no TRH to drive it', 880, 1040, TAG, 'end', when=O('ter'))
text('only TSH is off — free T4 still normal', 880, 1040, TAG, 'end', when=O('subhypo', 'subhyper'))

# ════════ 3. TSH down to the thyroid ════════
shapes.append(dict(vessel='M900 936 V1090 H790 V1146', w=22))
text('TSH in the blood', 918, 1062, 'nf-l2')
# lymphocytes making TSI (Graves)
add(''.join(f'<circle cx="{x}" cy="{y}" r="13" class="dyn-cell" style="stroke:var(--dk2)"/>' for x, y in ((500, 1150), (528, 1170), (528, 1132))),
    when=O('graves'))
text('lymphocytes → TSI (IgG)', 470, 1104, 'nf-l1', when=O('graves'))

# ════════ 4. the thyroid gland, with the trachea behind it ════════
TR = ('<rect x="874" y="1180" width="52" height="360" rx="20" class="dyn-soft"/>' +
      ''.join(f'<path d="M878 {y} H922" class="dyn-line" style="stroke-width:2;opacity:.5"/>' for y in range(1200, 1540, 26)))
add(TR)
LOBE_L = 'M865 1250 C845 1205 760 1195 722 1250 C690 1300 695 1400 735 1440 C770 1475 840 1470 862 1420 Z'
LOBE_R = 'M935 1250 C955 1205 1040 1195 1078 1250 C1110 1300 1105 1400 1065 1440 C1030 1475 960 1470 938 1420 Z'
GLAND = (f'<path d="{LOBE_L}" class="dyn-cell"/><path d="{LOBE_R}" class="dyn-cell"/>'
         '<rect x="855" y="1345" width="90" height="50" rx="18" class="dyn-cell"/>'
         f'<path d="{LOBE_L}" fill="var(--dk5)" opacity=".22"/><path d="{LOBE_R}" fill="var(--dk5)" opacity=".22"/>'
         '<rect x="855" y="1345" width="90" height="50" rx="18" fill="var(--dk5)" opacity=".22"/>')
sc = lambda k: f'<g transform="translate(900 1330) scale({k}) translate(-900 -1330)">'
add(GLAND, unless=BIG + SMALL)
add(sc(1.25) + GLAND + '</g>', when=BIG)
add(sc(0.8) + GLAND + '</g>', when=SMALL)
# Hashimoto: lymphocytes in the gland
add(''.join(f'<circle cx="{x}" cy="{y}" r="7" fill="var(--dk2)" opacity=".8"/>'
            for x, y in ((760, 1290), (800, 1330), (770, 1380), (820, 1410), (1040, 1290), (1000, 1330), (1030, 1380), (980, 1410))),
    when=O('hashi'))
text('Thyroid gland', 630, 1250, 'dyn-big', 'end')
text('secretes T4 ≫ T3', 630, 1272, 'nf-l2', 'end')
text('lymphocytes destroy follicles · goiter early (TSH is trophic)', 900, 1580, TAG, 'middle', when=O('hashi'))
text('TSI drives the TSH receptor — diffuse goiter', 900, 1580, TAG, 'middle', when=O('graves'))
text('TSH drives growth — goiter', 900, 1580, TAG, 'middle', when=O('tshoma'))
text('no goiter — nothing drives the gland', 900, 1580, TAG, 'middle', when=O('sec', 'ter'))
text('TSH suppressed — the gland involutes', 900, 1580, TAG, 'middle', when=SMALL)

# ════════ 5. blood: the free lane, the TBG-bound reservoir, the liver ════════
add('<rect class="dyn-soft" x="1170" y="1180" width="480" height="340" rx="26"/>')
text('Blood', 1190, 1215, 'dyn-big')
text('over 99% bound — mostly TBG, also prealbumin, albumin', 1190, 1236, 'dyn-cap')
text('more TBG — total T4 ↑, free T4 normal', 1190, 1262, TAG, when=O('tbghi'))
text('less TBG — total T4 ↓, free T4 normal', 1190, 1262, TAG, when=O('tbglo'))
text('both pools full — bound and free ↑', 1190, 1262, TAG, when=HIGH)
text('both pools low', 1190, 1262, TAG, when=HYPO_LOW)
text('T3 high · T4 low', 1190, 1262, TAG, when=O('lt3'))
text('free hormone — the only active form', 1300, 1304, 'nf-l2')
shapes.append(dict(vessel='M1190 1440 H1630', w=26, color='--dk10', cls='nf-art dyn-dim',
                   mods=[dict(when=O('tbghi'), d=14), dict(when=O('tbglo'), d=-14)]))
text('bound to TBG — a reservoir, not active', 1190, 1490, 'nf-l2')
text('⇅ exchange', 1540, 1392, 'nf-l2')
# liver (right lobe on the viewer's left, falciform ligament)
add('<path d="M1200 1640 C1200 1600 1300 1585 1420 1590 C1530 1595 1620 1610 1630 1640 C1600 1680 1520 1700 1450 1720 '
    'C1380 1745 1300 1765 1240 1750 C1205 1735 1195 1690 1200 1640 Z" class="dyn-cell" style="stroke:var(--dk9)"/>'
    '<path d="M1432 1592 Q1420 1650 1446 1720" class="dyn-line" style="stroke-width:2"/>')
text('Liver', 1250, 1648, 'dyn-big')
text('makes TBG', 1250, 1668, 'nf-l2')
add('<path d="M1520 1604 V1470" class="dyn-dash" marker-end="url(#ah-tfBlood)"/>')
text('estrogen slows TBG breakdown (pregnancy, OCP)', 1210, 1796, TAG, when=O('tbghi'))
text('hepatic failure: less made · nephrotic, androgens, steroids', 1210, 1796, TAG, when=O('tbglo'))

# ════════ 6. the trunk back up: free hormone to the tissues and to both feedback sites ════════
shapes.append(dict(vessel='M1110 1330 H1700 V290 H1028', w=26))
FB = [dict(when=HYPO_LOW, d=-8), dict(when=FB_HIGH, d=8)]
add('<path d="M1700 840 H1038" class="nf-art" stroke-width="14"/>', unless=HYPO_LOW + FB_HIGH)
add('<path d="M1700 840 H1038" class="nf-art dyn-dim" stroke-width="6"/>', when=HYPO_LOW)
add('<path d="M1700 840 H1038" class="nf-art" stroke-width="22"/>', when=FB_HIGH)
shapes.append(dict(vessel='M1700 1110 H1874', w=14))
text('free T4 + T3 in the blood', 1718, 700, 'nf-l2')
text('⊣ feedback', 1480, 275, 'nf-l1')
text('⊣ feedback', 1480, 822, 'nf-l1')
text('weak — little free hormone', 1300, 326, TAG, when=HYPO_LOW)
text('strong — lots of free hormone', 1300, 326, TAG, when=FB_HIGH)
text('weak — little free hormone', 1300, 876, TAG, when=HYPO_LOW)
text('strong — lots of free hormone', 1300, 876, TAG, when=FB_HIGH)
text('(the thyrotrophs are gone)', 1300, 894, 'nf-l2', when=O('sec'))

# tablets (levothyroxine / liothyronine)
add('<rect x="1760" y="1600" width="180" height="40" rx="20" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M1850 1600 V1640" class="dyn-line" style="stroke:var(--dk8)"/>'
    '<path d="M1760 1620 H1700 V1344" class="dyn-dash"/>', when=SMALL)
text('Levothyroxine (T4) tablets', 1760, 1580, 'nf-l1', when=O('lt4'))
text('Liothyronine (T3) tablets', 1760, 1580, 'nf-l1', when=O('lt3'))
text('by mouth — too much', 1760, 1666, 'nf-l2', when=SMALL)

# ════════ 7. a target cell: 5′-deiodinase and the nuclear receptor ════════
add(f'<path d="{rrect(1860, 960, 2320, 1240, 30)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(1860, 960, 2320, 1240, 30), w=18))
text('Target cell', 1890, 1000, 'dyn-big')
text('liver, kidney, muscle…', 1890, 1020, 'dyn-cap')
add('<ellipse cx="2215" cy="1110" rx="62" ry="52" class="dyn-soft"/>')
text('nucleus', 2215, 1150, 'dyn-cap', 'middle')
add('<path d="M2008 1118 L2090 1200" class="dyn-dash"/>')
text('reverse T3 (inactive)', 2096, 1214, 'nf-l2')
text('illness, starvation: deiodinase inhibited → T3 ↓, rT3 ↑', 1860, 1270, TAG, when=O('sick'))
text('T3 from the tablet needs no conversion', 1860, 1270, TAG, when=O('lt3'))
text('slowed — cold intolerance, weight gain, bradycardia', 1860, 1302, TAG, when=HYPO_LOW)
text('speeded — heat intolerance, weight loss, tachycardia', 1860, 1302, TAG, when=FB_HIGH)

# ════════ particles ════════
kinds = dict(trh=['trh', '--dk4'], tsh=['tsh', '--dk1'], tsi=['tsi', '--dk2'], t4=['t4', '--dk5'], t3=['t3', '--dk7'],
             rt3=['rt3', '--dk12'], bound=['bound', '--dk10'])
groups = [['trh', 'TRH'], ['tsh', 'TSH'], ['tsi', 'TSI'], ['t4', 'T4'], ['t3', 'T3'], ['rt3', 'Reverse T3'], ['bound', 'On TBG']]

def m(when, **kw):
    return dict(when=when if isinstance(when, list) else [when], **kw)
flows = [
  # TRH: neuron → axon → portal veins → thyrotroph
  dict(d='M900 352 V745', len=393, speed=110, base=dict(trh=3), mods=[
      m(O('hashi', 'sec'), set=dict(trh=6)), m(O('graves', 'tshoma', 'lt4', 'lt3'), set=dict(trh=1)), m(O('ter'), set=dict(trh=0))]),
  # TSH: thyrotroph → blood → the TSH receptor on the gland
  dict(d='M900 935 V1090 H790 V1145', len=320, base=dict(tsh=3), mods=[
      m(O('hashi'), set=dict(tsh=7)), m(O('tshoma'), set=dict(tsh=8)), m(O('subhypo'), set=dict(tsh=5)),
      m(O('subhyper', 'sec', 'ter'), set=dict(tsh=1)), m(O('graves', 'lt4', 'lt3'), set=dict(tsh=0))]),
  # TSI from the lymphocytes (Graves)
  dict(d='M540 1150 H776', len=236, speed=100, when=O('graves'), base=dict(tsi=5)),
  # the gland's output into the free lane
  dict(d='M1110 1330 H1700', len=590, base=dict(t4=3, t3=1), mods=[
      m(HYPO_LOW + SMALL, set=dict(t4=1, t3=0)), m(O('graves', 'tshoma'), set=dict(t4=7, t3=3))]),
  # the TBG-bound reservoir
  dict(d='M1190 1440 H1630', len=440, speed=55, r=8, base=dict(bound=6), mods=[
      m(O('tbghi') + HIGH, set=dict(bound=11)), m(O('tbglo') + HYPO_LOW + O('lt3'), set=dict(bound=2))]),
  # free hormone up the trunk to the TRH neuron
  dict(d='M1700 1330 V290 H1028', len=1712, base=dict(t4=4, t3=2), mods=[
      m(HYPO_LOW, set=dict(t4=1, t3=0)), m(O('graves', 'tshoma'), set=dict(t4=10, t3=5)), m(O('lt4'), set=dict(t4=10, t3=4)),
      m(O('lt3'), set=dict(t4=0, t3=9)), m(O('sick'), set=dict(t3=0))]),
  # free hormone to the thyrotroph
  dict(d='M1700 840 H1038', len=662, base=dict(t4=2, t3=1), mods=[
      m(HYPO_LOW, set=dict(t4=0, t3=0)), m(HIGH, set=dict(t4=4, t3=2)), m(O('lt3'), set=dict(t4=0, t3=4)), m(O('sick'), set=dict(t3=0))]),
  # free T4 into the target cell, to the deiodinase
  dict(d='M1700 1110 H1990', len=290, speed=110, base=dict(t4=3), mods=[
      m(HYPO_LOW, set=dict(t4=1)), m(HIGH, set=dict(t4=6)), m(O('lt3'), set=dict(t4=0, t3=5))]),
  # T3 made by the deiodinase → nucleus
  dict(d='M2012 1110 H2150', len=138, speed=70, base=dict(t3=2), mods=[
      m(HYPO_LOW + O('sick'), set=dict(t3=1)), m(HIGH, set=dict(t3=4)), m(O('lt3'), set=dict(t3=5))]),
  # reverse T3
  dict(d='M2008 1118 L2090 1200', len=116, speed=50, base=dict(rt3=1), mods=[m(O('sick'), set=dict(rt3=4))]),
  # tablets
  dict(d='M1760 1620 H1700 V1344', len=336, speed=110, when=O('lt4'), base=dict(t4=6)),
  dict(d='M1760 1620 H1700 V1344', len=336, speed=110, when=O('lt3'), base=dict(t3=6)),
]

# ════════ sites ════════
sites = [
  dict(x=1010, y=290, n=[1, 0], w=18, t='rec', l='Thyroid hormone receptor', s='T3 ⊣ TRH release', ions=[['t3', 'in', 1]], cross=True, reach=34,
       lx=1040, ly=236, la='start', c='thyroidreg', boost=FB_HIGH, low=HYPO_LOW + O('sick'), need=['!tft:ter'], closed='neuron damaged'),
  dict(x=900, y=760, n=[0, -1], w=18, t='rec', l='TRH receptor', s='TRH → TSH release', ions=[['trh', 'in', 1]], reach=40,
       lx=930, ly=712, la='start', c='pitcells', need=['!tft:sec'], closed='thyrotrophs lost', stop=O('ter'),
       boost=O('hashi'), low=O('graves', 'tshoma', 'lt4', 'lt3')),
  dict(x=1020, y=840, n=[1, 0], w=18, t='rec', l='Feedback receptor', s='T3 ↓ TRH receptors', ions=[['t3', 'in', 1]], cross=True, reach=34,
       lx=1050, ly=790, la='start', c='axisreg', need=['!tft:sec'], closed='gone', boost=FB_HIGH, low=O('hashi', 'ter', 'sick')),
  dict(x=900, y=920, n=[0, 1], w=18, t='ex', l='TSH released', s='glycoprotein — α + β subunits', ions=[['tsh', 'out', 1]], reach=30,
       lx=930, ly=982, la='start', c='glycoprot', need=['!tft:sec'], closed='thyrotrophs lost',
       boost=O('hashi', 'tshoma', 'subhypo'), low=O('graves', 'lt4', 'lt3', 'subhyper', 'ter'), sfx=dict(boost=' — more')),
  dict(x=790, y=1160, n=[0, -1], w=14, t='rec', l='TSH receptor', s='cAMP → every step + growth', ions=[['tsh', 'in', 1]], reach=26,
       lx=810, ly=1140, la='start', c='thyroidreg', unless=O('graves'),
       boost=O('hashi', 'tshoma', 'subhypo'), low=O('lt4', 'lt3', 'sec', 'ter', 'subhyper')),
  dict(x=790, y=1160, n=[0, -1], w=14, t='rec', l='TSH receptor', s='switched on by TSI', ions=[['tsi', 'in', 2]], reach=26,
       lx=810, ly=1140, la='start', c='hyperthyroid', when=O('graves'), boost=O('graves'), sfx=dict(boost=' — always on')),
  dict(x=1110, y=1330, n=[1, 0], w=26, t='para', l='T4 ≫ T3 out', s='about 93% T4 · 7% T3', ions=[['t4', 'out', 2], ['t3', 'out', 1]], cross=True,
       reach=30, lx=1130, ly=1370, la='start', c='thyroidreg', boost=O('graves', 'tshoma'), low=HYPO_LOW + SMALL, sfx=dict(low=' — less made')),
  dict(x=2000, y=1110, n=[0, 1], w=14, t='ex', l='5′-deiodinase', s='T4 → T3, or reverse T3', ions=[], c='thyroidreg',
       lx=1890, ly=1170, la='start', low=O('sick'), boost=HIGH, sfx=dict(low=' — inhibited', boost=' — busy')),
  dict(x=2153, y=1110, n=[0, -1], w=14, t='rec', l='Nuclear T3 receptor', s='gene transcription → the 7 B’s', ions=[['t3', 'in', 1]], reach=24,
       c='thyroidact', boost=FB_HIGH, low=HYPO_LOW + O('sick')),
]

notes = {
  '': 'Normal: TRH from the hypothalamus reaches the thyrotrophs through the portal veins; TSH drives the thyroid, which secretes '
      'mostly T4 (about 93%). Over 99% of it rides on TBG and other liver-made proteins — only the free hormone acts, is turned into the '
      'more potent T3 in the tissues, and feeds back on the pituitary and hypothalamus. Pick a pattern and read the six results.',
  'tft:hashi': 'Primary hypothyroidism (Hashimoto, the commonest cause where iodine is sufficient): lymphocytes destroy the gland, free T4 '
               'falls and feedback lifts, so TRH and TSH climb — the high TRH can raise prolactin. TSH ↑ with free T4 ↓; total T3 is low or '
               'still normal; the high TSH makes a goiter early; iodine uptake is low.',
  'tft:graves': 'Primary hyperthyroidism (Graves disease): thyroid-stimulating immunoglobulin (IgG) switches the TSH receptor on, so T4 and '
                'T3 pour out and feedback suppresses TSH almost to zero. TSH ↓ with free T4 and T3 ↑, a diffuse goiter and a high iodine uptake.',
  'tft:subhypo': 'Subclinical hypothyroidism: TSH is high while free T4 and T3 are still normal. It affects 4–10% of adults and up to 20% of '
                 'women over 50; levothyroxine is considered when TSH is above 10 mIU/L, smaller rises are watched.',
  'tft:subhyper': 'Subclinical hyperthyroidism: TSH is suppressed while free T4 and T3 are normal. The worry is the heart — atrial '
                  'fibrillation, above all in older patients and those with heart disease; treatment is advised when TSH is below 0.1 mIU/L.',
  'tft:sec': 'Secondary (pituitary) hypothyroidism: the thyrotrophs are lost — a pituitary mass, surgery, Sheehan syndrome — so TSH and '
             'free T4 fall together while TRH rises unopposed. No goiter, since nothing drives the gland; other pituitary hormones may be '
             'missing too.',
  'tft:ter': 'Tertiary (hypothalamic) hypothyroidism: a hypothalamic mass, radiation or infiltration cuts TRH, so TSH falls (though not to '
             'zero) and free T4 follows — the same low-low pattern as secondary. A TRH test dose still raises TSH, because the pituitary '
             'itself works.',
  'tft:tshoma': 'TSH-secreting pituitary adenoma (rare): the tumor makes TSH, so TSH and T4/T3 are high together — hyperthyroidism with a '
                'diffuse goiter, because TSH is trophic. A high TSH with a high T4 points above the thyroid.',
  'tft:lt4': 'Too much levothyroxine (overtreatment, or taken to lose weight): T4 comes from the tablet and the tissues make T3 from it, so '
             'feedback suppresses TSH and the gland involutes — no goiter, low iodine uptake. Chronic excess risks atrial fibrillation and '
             'osteoporosis.',
  'tft:lt3': 'Too much liothyronine (T3, 3–4× as potent as T4, half-life about a day): T3 is high and suppresses TSH, so the gland — whose '
             'output is mostly T4 — slows down: T3 ↑ but T4 ↓, low iodine uptake, a small gland.',
  'tft:tbghi': 'High TBG — pregnancy, estrogen, oral contraceptives (estrogen slows the liver’s breakdown of TBG): more hormone is bound, '
               'so total T4 and T3 rise, but after a brief catch-up free T4 and TSH are normal — the patient is euthyroid.',
  'tft:tbglo': 'Low TBG — nephrotic syndrome, androgens or anabolic steroids, glucocorticoids, hepatic failure: less hormone is bound, so '
               'total T4 and T3 fall while free T4 and TSH stay normal (free hormone can drop in advanced liver failure).',
  'tft:sick': 'Euthyroid sick (nonthyroidal illness, low T3) syndrome — critical illness or starvation inhibits 5′-deiodinase, so less T4 '
              'becomes T3 and more becomes inactive reverse T3. T3 ↓ with TSH and T4 normal (sometimes low); the thyroid itself is fine.',
}

R = lambda when, d: dict(when=when if isinstance(when, list) else [when], d=d)
readouts = [
  dict(l='TSH', mods=[R(O('hashi', 'subhypo', 'tshoma'), 1), R(O('graves', 'subhyper', 'sec', 'ter', 'lt4', 'lt3'), -1),
                      R(O('tbghi', 'tbglo', 'sick'), 0)]),
  dict(l='Free T4', mods=[R(O('hashi', 'sec', 'ter', 'lt3'), -1), R(O('graves', 'tshoma', 'lt4'), 1),
                          R(O('subhypo', 'subhyper', 'tbghi', 'tbglo', 'sick'), 0)]),
  dict(l='Total T4', mods=[R(O('hashi', 'sec', 'ter', 'lt3', 'tbglo'), -1), R(O('graves', 'tshoma', 'lt4', 'tbghi'), 1),
                           R(O('subhypo', 'subhyper', 'sick'), 0)]),
  # hypothyroidism (Hashimoto, central): total T3 'normal or low' (Katzung Table 38-2) → no arrow
  dict(l='Total T3', mods=[R(O('tbglo', 'sick'), -1), R(O('graves', 'tshoma', 'lt4', 'lt3', 'tbghi'), 1),
                           R(O('subhypo', 'subhyper'), 0)]),
  dict(l='TBG', mods=[R(O('tbghi'), 1), R(O('tbglo'), -1)]),
  dict(l='RAIU', mods=[R(O('graves', 'tshoma'), 1), R(O('hashi', 'sec', 'ter', 'lt4', 'lt3'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='tft', label='Pattern', type='one', options=[
                ['hashi', 'Hashimoto — primary hypo', 'hypothyroid'], ['graves', 'Graves — primary hyper', 'hyperthyroid'],
                ['subhypo', 'Subclinical hypothyroid', 'subclinthy'], ['subhyper', 'Subclinical hyperthyroid', 'subclinthy'],
                ['sec', 'Secondary (pituitary)', 'hypopit'], ['ter', 'Tertiary (hypothalamus)', 'hypopit'],
                ['tshoma', 'TSH-secreting adenoma', 'thylabs'],
                ['lt4', 'Too much levothyroxine (T4)', 'thyroiddrugs'], ['lt3', 'Too much liothyronine (T3)', 'thyroiddrugs'],
                ['tbghi', 'High TBG (pregnancy, OCP)', 'thyroidreg'], ['tbglo', 'Low TBG (nephrotic, androgens)', 'thyroidreg'],
                ['sick', 'Euthyroid sick (low T3)', 'thylabs']],
                 sections=[['Primary — the gland', ['hashi', 'graves', 'subhypo', 'subhyper']],
                           ['Central — pituitary or hypothalamus', ['sec', 'ter', 'tshoma']],
                           ['Hormone pills', ['lt4', 'lt3']],
                           ['Binding protein', ['tbghi', 'tbglo']],
                           ['Other', ['sick']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 332, 335, 343–346, 360 · Costanzo ch 9 · Guyton ch 77 · Katzung ch 38')

# ════════ the one new card: a real gap (no card covers subclinical hyperthyroidism) ════════
card('subclinthy', 'Subclinical hypothyroidism & hyperthyroidism', 'dz', 'tfDz', 'An abnormal TSH with normal thyroid hormone levels', 0,
     'Defined by the TSH alone. <b>Subclinical hypothyroidism</b> is a raised TSH with normal thyroid hormone levels; '
     '<b>subclinical hyperthyroidism</b> is a suppressed TSH (below the normal range) with normal thyroid hormone levels.',
     ['Subclinical hypothyroidism is common: 4–10% of the general population and up to 20% of women older than 50',
      'Subclinical hyperthyroidism: the main concern is cardiac toxicity — <b>atrial fibrillation</b> — especially in older patients and '
      'those with heart disease'],
     ['Subclinical hypothyroidism: <b>TSH ↑</b> · free T4 and T3 normal',
      'Subclinical hyperthyroidism: <b>TSH ↓</b> · free T4 and T3 normal'],
     ['Abnormal TSH with a normal free T4 = subclinical thyroid disease'],
     [KZ38],
     ['Subclinical hypothyroidism: levothyroxine may be considered when TSH is above 10 mIU/L; smaller rises are monitored',
      'Subclinical hyperthyroidism: treatment is appropriate when TSH is below 0.1 mIU/L; milder suppression is monitored'],
     ['subclinical hypothyroidism', 'subclinical hyperthyroidism', 'subclinical hypothyroid', 'subclinical hyperthyroid',
      '=elevated tsh with normal free t4', '=suppressed tsh with normal free t4'])

MAP = dict(
  id='tftsim', title='Thyroid Function Tests in Motion', topic='endo', after='follflow',
  sub='TRH → TSH → T4 ≫ T3, carried mostly on TBG, turned into T3 in the tissues, free hormone feeding back on the pituitary and '
      'hypothalamus — pick a pattern (primary, central, hormone pills, a TBG change, euthyroid sick) and read TSH, free and total T4, '
      'T3, TBG and iodine uptake. Tap a receptor for its card',
  w=3500, h=1860,
  fa='332, 335, 343–346, 360', src=SRC,
  lanes=[('tfAxis', 'Hypothalamus & pituitary', 'ppp'), ('tfGland', 'Thyroid gland', 'glycogen'), ('tfBlood', 'Blood & tissues', 'sugars'),
         ('tfDz', 'Patterns', 'tca')],
  comps=[],
  nodes=[
    ('tf1', 'TRH neuron · portal veins', 330, 250, 'tfAxis', 'reading an axis', ['pitportal', 'axisreg']),
    ('tf2', 'Thyrotroph · TSH', 330, 700, 'tfAxis', 'shared α subunit with LH, FSH, hCG', ['pitcells', 'glycoprot'], 'hub'),
    ('tf3', 'Central hypothyroidism', 330, 900, 'tfDz', 'pituitary · hypothalamus', ['hypopit', 'sheehan']),
    ('tf4', 'TSH-secreting adenoma', 330, 1010, 'tfDz', 'TSH ↑ with T4 ↑', ['pitnet', 'thylabs']),
    ('tf5', 'Hashimoto thyroiditis', 300, 1250, 'tfGland', 'primary hypothyroidism', ['hypothyroid'], 'hub'),
    ('tf6', 'Graves disease', 300, 1360, 'tfGland', 'primary hyperthyroidism', ['hyperthyroid']),
    ('tf7', 'Subclinical disease', 300, 1470, 'tfDz', 'TSH off · free T4 normal', ['subclinthy']),
    ('tf8', 'Thyroid hormone pills', 2150, 1620, 'tfBlood', 'levothyroxine · liothyronine', ['thyroiddrugs']),
    ('tf9', 'TBG — total vs free', 1820, 1760, 'tfBlood', 'pregnancy, OCP ↑ · nephrotic, androgens ↓',
     ['thyroidreg', 'pregphys', 'ocp', 'nephrotic', 'anabolic'], 'hub'),
    ('tf10', 'Euthyroid sick syndrome', 2090, 1360, 'tfDz', 'low T3 · reading the tests', ['thylabs']),
    ('tf11', 'Thyroid hormone actions', 2090, 900, 'tfBlood', 'T3 on the nuclear receptor — the 7 B’s', ['thyroidact']),
  ],
  panels=[
    (140, 1640, 960, 'Thyroid hormone in the blood (Guyton ch 77; Katzung ch 38)', [
      ('Output', 'about 93% T4, 7% T3 · 80% of circulating T3 is made in the tissues'),
      ('Binding', 'over 99% on liver-made proteins, mainly TBG · free: 0.04% of T4, 0.4% of T3'),
      ('Potency', 'T3 about 3–4× T4 — T4 is largely a prohormone'),
      ('Half-life', 'T4 about 7 days · T3 about 1 day'),
      ('Feedback', 'free hormone ⊣ TSH (mostly at the pituitary) and ⊣ TRH')]),
    # placed low enough for the main kit's sectioned chips (five sub-headings add ~230 px over check.py's estimate)
    (2420, 900, 1000, 'Locate the problem — TSH with free T4 (Costanzo ch 9; First Aid pp. 335, 344)', [
      ('TSH ↑ · free T4 ↓', 'primary hypothyroidism — the gland fails'),
      ('TSH ↓ · free T4 ↑', 'primary hyperthyroidism — Graves, a nodule, or hormone pills'),
      ('TSH ↓ · free T4 ↓', 'central — pituitary (secondary) or hypothalamus (tertiary)'),
      ('TSH ↑ · free T4 ↑', 'TSH-secreting pituitary adenoma'),
      ('TSH off · free T4 normal', 'subclinical disease (Katzung ch 38)'),
      ('Total T4 off · TSH normal', 'a TBG change, not thyroid disease')]),
    (2420, 1120, 1000, 'Drugs that move the numbers (Katzung ch 38; First Aid pp. 332, 335)', [
      ('↑ TBG', 'estrogens, oral contraceptives, tamoxifen, raloxifene, methadone'),
      ('↓ TBG', 'androgens, anabolic steroids, glucocorticoids'),
      ('Block 5′-deiodinase', 'amiodarone, β-blockers, glucocorticoids, PTU — T3 ↓, rT3 ↑'),
      ('Lower TSH secretion', 'dopamine, glucocorticoids, somatostatin, octreotide'),
      ('Faster T4 breakdown', 'phenytoin, carbamazepine, rifampin, phenobarbital')]),
  ],
  dyn=dyn,
)
