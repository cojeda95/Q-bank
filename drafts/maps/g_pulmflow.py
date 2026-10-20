# m55 — Pulmonary Blood Flow & Zones in Motion (dynamic map, kit data)
# An upright right lung, apex to base, with one alveolus + capillary at three heights (apex, mid-lung, base). Blood climbs
# a medial pulmonary-artery column from the right ventricle, crosses each capillary under its alveolus (blue → red where
# it picks up O₂) and returns down a lateral pulmonary-vein column to the left atrium. Zone bands (1–3) are shaded in the
# lung and named at each level with their PA / Pa / Pv order; a graph beside the lung (same height axis) shows blood flow
# per unit of lung from apex to base, and a graph under it shows PVR against lung volume (alveolar + extra-alveolar =
# U-shaped). One `one` switch, in sections: posture & exercise · zone 1 appears · lung volume · hypoxic vasoconstriction ·
# disease. Readouts: flow at the apex, zone 1 (no flow), PVR, pulmonary artery pressure, dead space, PaO₂.
#
# Sources (all read in the corpus, U+00A0/U+00AD normalized):
#   First Aid 2025 p. 300 (PCWP ≈ left atrial pressure, except mitral stenosis where PCWP > LVEDP; lung autoregulation:
#     hypoxia → vasoconstriction, unlike other organs) · p. 684 (low resistance, high compliance; ↓ PAO₂ → hypoxic
#     vasoconstriction shifts blood to well-ventilated regions; chronic → pulmonary hypertension ± cor pulmonale;
#     PVR = (P pulm artery − P left atrium) / Q, P left atrium ≈ wedge pressure) · p. 685 (V/Q ≈ 3 at the apex, 0.6 at the
#     base; both V and Q greater at the base; exercise → apical capillaries dilate, V/Q approaches 1; zone 1 PA ≥ Pa > Pv,
#     zone 2 Pa > PA > Pv, zone 3 Pa > Pv > PA; V/Q = ∞ dead space, e.g. PE, 100% O₂ improves PaO₂) · p. 688 (altitude:
#     ↓ PAO₂, chronic HPV → ↑ PVR → pulmonary hypertension, RVH; exercise: ↑ pulmonary blood flow, V/Q more uniform, PaO₂
#     and PaCO₂ maintained) · p. 691 (PE: ventilated but not perfused, hypoxemia, tachypnea, respiratory alkalosis) ·
#     p. 698 (pulmonary hypertension: mean PA pressure > 20 mm Hg at rest, ↑ PVR → RVH, RV failure; groups 1–5 with causes;
#     group 1 endothelial dysfunction ↑ endothelin, ↓ NO and prostacyclin; BMPR2).
#   Costanzo ch 5 (hypoxic vasoconstriction below PAO₂ ≈ 70 mm Hg, redirects flow without changing overall PVR, fails when
#     disease is widespread — multilobar pneumonia; global HPV at altitude → ↑ PVR → ↑ PA pressure → RV hypertrophy; fetal
#     lung: global HPV, ↑ PVR, flow ≈ 15% of cardiac output, first breath reverses it; inhaled NO offsets HPV; lung volume:
#     high volume crushes alveolar vessels, low volume narrows extra-alveolar vessels, PVR = their sum; supine → flow nearly
#     uniform; zone 1 when Pa falls (hemorrhage) or PA rises (positive-pressure breathing) → ventilated, not perfused →
#     physiologic dead space; zone 3 has the most open capillaries; physiologic shunt ≈ 2% — bronchial flow + thebesian
#     veins; V/Q highest in zone 1, lowest in zone 3; small emboli → dead space; diverted flow goes to the rest of the lung).
#   Guyton ch 39 (RV 25/0–1; PA 25/8, mean 15; capillary ≈ 7; LA ≈ 2 (1–5); wedge ≈ 5, 2–3 above LA; lung 30 cm tall,
#     23 mm Hg: 15 above heart level, 8 below; base flow ≈ 5× apex at rest; normally only zones 2 (apices) and 3; zone 2
#     begins ≈ 10 cm above the heart; lying down → all zone 3; zone 1 with positive alveolar pressure ≥ 10 mm Hg above
#     normal or very low systolic pressure after blood loss; exercise turns apices to zone 3, flow ↑ 4–7×, up to 3× more
#     capillaries open, each distended, PVR falls so PA pressure rises very little; LA > 7–8 mm Hg → PA and capillary
#     pressure rise almost equally, load on the right heart; LHF / mitral stenosis can raise lung blood volume 100%;
#     HPV below ≈ 73 mm Hg, up to 5× resistance; bronchial blood drains into pulmonary veins).
#   Guyton ch 40 (upright: V/Q at the top up to 2.5× ideal → physiological dead space; bottom 0.6 → physiological shunt;
#     exercise → far less physiological dead space).
#   Bootcamp.com Pulmonology — Respiratory physiology, blood (fetal lungs hypoxic → ↑ resistance → ↑ PA pressure, blood
#     PA → aorta through the PDA; first breath ↓ resistance; bronchial circulation = natural shunt).
# Conflict noted: Costanzo calls the apex "zone 1, perfused at a low rate" in health; Guyton (and the westzones card) say
#   healthy lungs have only zones 2 and 3. The map follows Guyton + FA (zone 1 appears only with ↓ Pa or ↑ PA).
# Cut for lack of a source: the lung volume where PVR is lowest (no textbook names it — the marker only says "normal
#   breathing"); arrows for PVR in acute PE, PA pressure in exercise ("rises very little" — left "–"), PaO₂ in local HPV
#   ("within limits" preserved — left "–"), PCWP/LA arrows outside heart failure; PEEP by name (sources say
#   positive-pressure breathing); a headstand option (Costanzo mentions it, too trivial); zone changes in heart failure
#   and PAH (no source moves the zone boundaries there).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ5, GY39, GY40 = full('Costanzo', 5), full('Guyton', 39), full('Guyton', 40)
BC = 'Bootcamp.com Pulmonology — Respiratory physiology, blood'
SRC = [CZ5, GY39, GY40, BC]

O = lambda *k: ['st:' + x for x in k]
Z1 = O('hem', 'ppv')                  # zone 1 at the apex
ALLZ3 = O('sup', 'ex')                # the whole lung is zone 3
STD = None                            # default zone layout = unless Z1 + ALLZ3
GLOBAL = O('alt', 'fet')              # global hypoxic vasoconstriction
NARROW = GLOBAL + O('pah')            # every arteriole narrowed

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

# ── geometry ──
AX, VX = 1110, 720            # artery column (medial), vein column (lateral)
ALVX = 910                    # alveoli
LEV = dict(ap=420, mid=820, base=1170)    # alveolus centres; the capillary runs 62 px below
CAP = {k: y + 62 for k, y in LEV.items()}
APEX_Y, Z23_Y, HEART_Y, BASE_Y = 250, 618, 991, 1390

# ════════ title ════════
text('An upright lung — apex to base', 180, 160, 'dyn-big')
text('30 cm tall: pulmonary arterial pressure is about 15 mm Hg lower at the apex than at heart level, about 8 mm Hg higher at the base',
     180, 184, 'dyn-cap')

# ════════ the lung, its zone bands, the heart-level line ════════
LUNG = ('M880 250 C720 250 600 420 565 650 C540 820 535 1100 545 1395 C680 1345 820 1325 950 1335 '
        'C1080 1345 1200 1365 1290 1375 C1300 1200 1300 1000 1270 920 C1245 880 1240 790 1265 740 C1250 520 1060 255 880 250 Z')
add(f'<defs><clipPath id="pfLungClip"><path d="{LUNG}"/></clipPath></defs>')
add(f'<path d="{LUNG}" class="dyn-cell"/>')
def band(y0, y1, col, op):
    return f'<rect x="530" y="{y0}" width="780" height="{y1 - y0}" fill="var({col})" opacity="{op}" clip-path="url(#pfLungClip)"/>'
add(band(APEX_Y - 10, Z23_Y, '--dk5', .20) + band(Z23_Y, 1420, '--dk1', .16), unless=Z1 + ALLZ3)
add(band(APEX_Y - 10, 1420, '--dk1', .16), when=ALLZ3)
add(band(APEX_Y - 10, 540, '--ink-3', .30) + band(540, 760, '--dk5', .20) + band(760, 1420, '--dk1', .16), when=Z1)
# fissures (right lung: horizontal + oblique), faint
add('<path d="M560 700 C700 690 900 700 1262 745" class="dyn-line" style="opacity:.35"/>'
    '<path d="M1180 470 C1000 700 820 1000 640 1360" class="dyn-line" style="opacity:.25"/>')
# zone boundaries + names inside the lung (right edge)
add(f'<path d="M560 {Z23_Y} H1250" class="dyn-dash" style="opacity:.6"/>', unless=Z1 + ALLZ3)
add('<path d="M600 540 H1210 M560 760 H1262" class="dyn-dash" style="opacity:.6"/>', when=Z1)
text(f'— heart level —', 1000, HEART_Y + 5, 'dyn-cap', 'middle')
add(f'<path d="M560 {HEART_Y} H930 M1070 {HEART_Y} H1268" class="dyn-dash" style="opacity:.45"/>')

# ════════ the three alveolar units ════════
for k, y in LEV.items():
    c = CAP[k]
    add(f'<path d="M{ALVX} {y - 160} V{y - 52}" class="nf-wall" stroke-width="26"/><path d="M{ALVX} {y - 160} V{y - 52}" class="nf-lumen" stroke-width="14"/>',
        unless=O('fet') if k != 'base' else O('fet', 'loc'))
    add(f'<circle cx="{ALVX}" cy="{y}" r="54" class="dyn-soft"/>', unless=O('lov', 'hiv'))
    add(f'<circle cx="{ALVX}" cy="{y}" r="38" class="dyn-soft"/>', when=O('lov'))
    add(f'<circle cx="{ALVX}" cy="{y}" r="66" class="dyn-soft"/>', when=O('hiv'))
# airway labels (apex unit only)
text('terminal bronchiole', ALVX + 24, LEV['ap'] - 120, 'nf-l2')
text('alveolus', ALVX + 70, LEV['ap'] - 10, 'nf-l2', unless=O('fet'))
# local hypoxia: base alveolus consolidated (pneumonia / blocked airway)
add(f'<circle cx="{ALVX}" cy="{LEV["base"]}" r="54" fill="var(--dk10)" opacity=".55"/>'
    f'<path d="M{ALVX - 20} {LEV["base"] - 150} L{ALVX + 20} {LEV["base"] - 110} M{ALVX + 20} {LEV["base"] - 150} L{ALVX - 20} {LEV["base"] - 110}" class="dyn-lesion"/>',
    when=O('loc'))
text('no air in — alveolar PO₂ falls', ALVX + 74, LEV['base'] - 10, TAG, when=O('loc'))
# fetal: fluid-filled alveoli
for y in LEV.values():
    add(f'<circle cx="{ALVX}" cy="{y}" r="54" fill="var(--nf-h2o)" opacity=".35"/>', when=O('fet'))
text('fluid-filled — no breathing', ALVX + 74, LEV['ap'] - 10, TAG, when=O('fet'))
# positive pressure: + signs in each alveolus
for y in LEV.values():
    text('+ +', ALVX, y + 6, 'nf-l1', 'middle', when=O('ppv'))
# heart failure: fluid at the base alveolus
add(f'<path d="M{ALVX - 44} {LEV["base"] + 26} Q{ALVX} {LEV["base"] + 48} {ALVX + 44} {LEV["base"] + 26} Z" fill="var(--nf-h2o)" opacity=".6"/>',
    when=O('lhf'))

# ════════ vessels ════════
# the artery column (extra-alveolar) + the trunk from the RV
shapes.append(dict(vessel=f'M{AX} {CAP["ap"]} V{CAP["base"]}', w=22, color='--dk1',
                   mods=[dict(when=O('lov'), d=-10), dict(when=O('hiv'), d=6), dict(when=O('hem'), d=-6),
                         dict(when=O('lhf', 'pah', 'alt'), d=8), dict(when=O('ex'), d=4)]))
shapes.append(dict(vessel=f'M1560 935 V860 H{AX}', w=30, color='--dk1',
                   mods=[dict(when=O('hem'), d=-8), dict(when=O('lhf', 'pah', 'alt', 'fet'), d=10)]))
# the vein column + the vein to the left atrium
shapes.append(dict(vessel=f'M{VX} {CAP["ap"]} V1330 H1250 Q1340 1330 1380 1080', w=22, color='--dk2',
                   mods=[dict(when=O('lhf'), d=12), dict(when=O('hem'), d=-6)]))
# capillaries — one per level, red after the alveolus
def capw(k):
    mods = [dict(when=O('ex'), d=6), dict(when=O('hiv'), d=-6)]
    if k == 'ap': mods += [dict(when=O('sup'), d=4)]
    if k == 'base': mods += [dict(when=O('sup'), d=-2)]
    return mods
for k in LEV:
    c = CAP[k]
    w0 = 8 if k == 'ap' else 12 if k == 'mid' else 16
    extra = dict(unless=Z1) if k == 'ap' else {}
    shapes.append(dict(vessel=f'M{AX} {c} H{ALVX}', w=w0, color='--dk1', mods=capw(k), **extra))
    shapes.append(dict(vessel=f'M{ALVX} {c} H{VX}', w=w0, color='--dk2', mods=capw(k), **extra))
# zone 1: the apical capillary squeezed shut
add(f'<path d="M{AX - 12} {CAP["ap"]} H{VX + 12}" class="dyn-dash" style="stroke-width:3"/>', when=Z1)
# recruited capillaries (a second one per level, collapsed at rest except at the base — zone 3 has the most open)
for k in LEV:
    c = CAP[k] + 34
    if k == 'base':
        shapes.append(dict(vessel=f'M{AX} {c} H{VX}', w=10, color='--dk8', unless=O('fet')))
    else:
        add(f'<path d="M{AX - 12} {c} H{VX + 12}" class="dyn-dash" style="opacity:.55"/>', unless=O('ex'))
        shapes.append(dict(vessel=f'M{AX} {c} H{VX}', w=10, color='--dk8', when=O('ex')))
text('closed capillary — opens in exercise', 1090, CAP['mid'] + 56, 'dyn-cap', 'end', unless=O('ex'))
text('recruited — open', 1090, CAP['mid'] + 56, 'dyn-cap', 'end', when=O('ex'))
# arteriolar constriction rings (HPV / PAH)
def ring(y):
    return (f'<path d="M{AX - 50} {y - 15} V{y + 15} M{AX - 62} {y - 15} V{y + 15}" class="dyn-line" '
            f'style="stroke:var(--bad);stroke-width:5"/>')
add(''.join(ring(CAP[k]) for k in LEV), when=NARROW)
add(ring(CAP['base']), when=O('loc'))
text('arterioles constricted', AX - 60, CAP['ap'] - 26, TAG, 'end', when=GLOBAL)
text('arterioles thickened, narrowed', AX - 60, CAP['ap'] - 26, TAG, 'end', when=O('pah'))
# pulmonary embolus in the mid-lung branch
add(f'<path d="M{AX - 64} {CAP["mid"] - 14} q20 -10 40 0 q12 14 0 28 q-20 10 -40 0 q-12 -14 0 -28 Z" fill="var(--ink-2)"/>', when=O('pe'))
text('ventilated, not perfused — V/Q = ∞', 190, 900, TAG, when=O('pe'))
# bronchial artery (from the aorta) → its veins drain into the pulmonary vein
add(f'<path d="M1250 640 C1150 650 1010 690 {ALVX + 20} {LEV["mid"] - 120}" class="nf-art" stroke-width="5" style="stroke:var(--dk2)"/>'
    f'<path d="M{ALVX - 20} {LEV["mid"] - 110} C840 690 780 680 {VX + 10} 680" class="dyn-dash" style="stroke:var(--dk2)"/>')
text('bronchial artery (from the aorta)', 1262, 630, 'nf-l2')

# ════════ the heart ════════
HEART = 'M1400 930 C1480 900 1600 905 1650 950 C1720 1010 1745 1150 1705 1300 C1620 1292 1480 1262 1400 1180 C1350 1120 1350 990 1400 930 Z'
add(f'<path d="{HEART}" class="dyn-cell" style="stroke:var(--dk2)"/>'
    '<path d="M1480 960 C1500 1060 1560 1180 1700 1296" class="dyn-line" style="opacity:.5"/>')
add('<path d="M1632 945 C1630 860 1650 790 1720 772 H1820" class="nf-art" stroke-width="26" style="stroke:var(--dk2)"/>')
text('aorta', 1834, 778, 'nf-l2')
add('<ellipse cx="1420" cy="1060" rx="46" ry="34" class="dyn-soft"/>', unless=O('lhf'))
add('<ellipse cx="1420" cy="1060" rx="64" ry="48" class="dyn-soft" style="stroke:var(--bad)"/>', when=O('lhf'))
text('Heart', 1760, 1010, 'dyn-big')
add('<path d="M1530 960 C1560 1050 1600 1130 1690 1220" class="dyn-line" style="stroke:var(--bad);stroke-width:12;opacity:.5"/>',
    when=O('pah', 'alt'))
text('RV hypertrophy', 1740, 1240, TAG, when=O('pah'))
text('chronic → RV hypertrophy', 1740, 1240, TAG, when=O('alt'))
text('Pulmonary artery', 1300, 818, 'nf-l1')
text('pulmonary vein', 1150, 1370, 'nf-l2', 'middle')
text('blood pressure falls', 1300, 905, TAG, when=O('hem'))
text('pressure ↑', 1300, 905, TAG, when=O('lhf', 'pah', 'alt', 'fet'))
# fetal ductus arteriosus
add('<path d="M1575 860 H1626" class="nf-art" stroke-width="14" style="stroke:var(--dk1)"/>', when=O('fet'))
text('ductus arteriosus → aorta', 1662, 884, TAG, when=O('fet'))
text('pulmonary blood volume up to 2×', 1360, 1370, TAG, when=O('lhf'))
text('ventilator: + alveolar pressure', ALVX + 24, LEV['ap'] - 140, TAG, when=O('ppv'))

# ════════ left column: what each level is doing ════════
LX = 190
# apex
text('Zone 2 — Pa > PA > Pv', LX, 452, 'nf-l2', unless=Z1 + ALLZ3)
text('flows in systole only', LX, 470, 'nf-l2', unless=Z1 + ALLZ3)
text('Zone 3 — Pa > Pv > PA', LX, 452, 'nf-l2', when=ALLZ3)
text('flows all the time', LX, 470, 'nf-l2', when=ALLZ3)
text('Zone 1 — PA ≥ Pa > Pv', LX, 452, 'nf-l2', when=Z1)
text('no flow — dead space', LX, 470, TAG, when=Z1)
text('V/Q ≈ 3 · alveolar PO₂ highest', LX, 500, 'dyn-cap', unless=O('ex'))
text('V/Q approaches 1', LX, 500, 'dyn-cap', when=O('ex'))
# mid
text('Zone 3 — Pa > Pv > PA', LX, 852, 'nf-l2')
text('flow driven by Pa − Pv', LX, 870, 'nf-l2')
# base
text('Zone 3 — Pa > Pv > PA', LX, 1202, 'nf-l2')
text('most capillaries open', LX, 1220, 'nf-l2')
text('flow ≈ 5× the apex · V/Q ≈ 0.6', LX, 1250, 'dyn-cap', unless=ALLZ3)
text('flow nearly the same as the apex', LX, 1250, 'dyn-cap', when=O('sup'))
text('lying down — no part of the lung is far above the heart', 180, 214, TAG, when=O('sup'))
text('exercise — pressures rise enough to open the apex', 180, 214, TAG, when=O('ex'))

# ════════ graph 1: blood flow per unit of lung, apex → base (same height axis as the lung) ════════
GX = 1880
def fx(f): return round(GX + 60 * f)
add(f'<path d="M{GX} {APEX_Y} V{BASE_Y} H2310" class="dyn-line"/>')
text('Blood flow per unit of lung', GX, 226, 'nf-l1')
text('apex', GX - 12, APEX_Y + 6, 'nf-l2', 'end')
text('base', GX - 12, BASE_Y, 'nf-l2', 'end')
text('flow →', 2310, BASE_Y + 26, 'nf-l2', 'end')
def curve(pts): return 'M' + ' L'.join(f'{fx(f)} {y}' for y, f in pts)
REST = [(250, .2), (618, 1.4), (991, 3.2), (1390, 5.0)]
add(f'<path d="{curve(REST)}" class="dyn-trace"/>', unless=ALLZ3 + Z1)
add(f'<path d="{curve(REST)}" class="dyn-trace dyn-dim"/>', when=ALLZ3 + Z1)
text('at rest', fx(5.0) + 10, 1360, 'nf-l2')
EXC = [(250, 2.0), (618, 3.4), (991, 5.0), (1390, 6.4)]
add(f'<path d="{curve(EXC)}" class="dyn-hl"/>', when=O('ex'))
text('exercise', fx(2.0) + 12, 280, 'nf-l1', when=O('ex'))
add(f'<path d="M{fx(3)} {APEX_Y} V{BASE_Y}" class="dyn-hl"/>', when=O('sup'))
text('lying down: nearly uniform', fx(3) + 12, 300, 'nf-l1', when=O('sup'))
HEM = [(250, 0), (540, 0), (700, .8), (991, 2.4), (1390, 4.0)]
PPV = [(250, 0), (540, 0), (700, 1.0), (991, 2.8), (1390, 4.6)]
add(f'<path d="{curve(HEM)}" class="dyn-hl"/>', when=O('hem'))
add(f'<path d="{curve(PPV)}" class="dyn-hl"/>', when=O('ppv'))
text('zone 1: no flow', fx(0) + 14, 380, 'nf-l1', when=Z1)
text('shape after Guyton ch 39', GX, BASE_Y + 26, 'dyn-cap')

# ════════ graph 2: PVR vs lung volume (Costanzo ch 5) ════════
PX0, PY0, PX1, PY1 = 260, 1790, 920, 1500
add(f'<path d="M{PX0} {PY1} V{PY0} H{PX1}" class="dyn-line"/>')
text('PVR and lung volume', 180, 1470, 'nf-l1')
text('PVR', PX0 - 12, PY1 + 10, 'nf-l2', 'end')
text('lung volume →', 900, PY0 + 26, 'nf-l2', 'end')
add(f'<path d="M290 1745 C420 1720 650 1640 900 1530" class="dyn-dash" style="stroke:var(--dk3)"/>')   # alveolar
add(f'<path d="M290 1530 C520 1640 760 1720 900 1745" class="dyn-dash" style="stroke:var(--dk4)"/>')   # extra-alveolar
TOT = 'M290 1510 C410 1760 780 1760 900 1510'
add(f'<path d="{TOT}" class="dyn-trace"/>')
text('alveolar vessels — crushed as alveoli inflate', 300, 1774, 'nf-l2')
text('extra-alveolar vessels — pulled open', 912, 1752, 'nf-l2')
text('total PVR', 912, 1508, 'nf-l1')
def bez(t, p0=(290, 1510), p1=(410, 1760), p2=(780, 1760), p3=(900, 1510)):
    u = 1 - t
    return tuple(round(u**3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t**3 * d) for a, b, c, d in zip(p0, p1, p2, p3))
MK = dict(lov=bez(.08), norm=bez(.5), hiv=bez(.93))
def dot(p, lab, side='middle', dy=-18):
    return f'<circle cx="{p[0]}" cy="{p[1]}" r="11" fill="var(--accent)" stroke="var(--surface)" stroke-width="3"/>'
add(dot(MK['norm'], ''), unless=O('lov', 'hiv'))
text('normal breathing', MK['norm'][0], MK['norm'][1] + 34, 'nf-l2', 'middle', unless=O('lov', 'hiv'))
add(dot(MK['lov'], ''), when=O('lov'))
text('low volume', MK['lov'][0] + 24, MK['lov'][1] + 40, 'nf-l1', when=O('lov'))
add(dot(MK['hiv'], ''), when=O('hiv'))
text('high volume', MK['hiv'][0] - 20, MK['hiv'][1] + 6, 'nf-l1', 'end', when=O('hiv'))

# ════════ particles ════════
kinds = dict(deo=['deo', '--dk1'], oxy=['oxy', '--dk2'], air=['air', '--dk5'])   # one colour per group: the Show chips name them
groups = [['deo', 'Blood low in O₂'], ['oxy', 'Blood carrying O₂'], ['air', 'Inspired air']]
def m(when, **kw):
    return dict(when=when if isinstance(when, list) else [when], **kw)
FETAL0 = m(O('fet'), set=dict(deo=0, oxy=0))
flows = [
  # the trunk
  dict(d=f'M1560 935 V860 H{AX}', len=525, base=dict(deo=4), mods=[
      m(O('ex'), set=dict(deo=8)), m(O('fet'), set=dict(deo=1)), m(O('hem'), set=dict(deo=2))]),
  # up the artery column to the apex, down to the base
  dict(d=f'M{AX} 860 V{CAP["ap"]}', len=860 - CAP['ap'], speed=90, base=dict(deo=1), mods=[
      m(O('ex', 'sup'), set=dict(deo=3)), m(Z1 + O('fet'), set=dict(deo=0))]),
  dict(d=f'M{AX} 860 V{CAP["base"]}', len=CAP['base'] - 860, base=dict(deo=3), mods=[
      m(O('ex'), set=dict(deo=5)), m(O('fet'), set=dict(deo=0)), m(O('hem'), set=dict(deo=2))]),
  # apex capillary (zone 2: a trickle)
  dict(d=f'M{AX} {CAP["ap"]} H{ALVX}', len=AX - ALVX, speed=70, base=dict(deo=1), mods=[
      m(O('ex', 'sup'), set=dict(deo=3)), m(O('loc', 'pe'), add=dict(deo=1)), m(Z1 + O('fet'), set=dict(deo=0))]),
  dict(d=f'M{ALVX} {CAP["ap"]} H{VX}', len=ALVX - VX, speed=70, base=dict(oxy=1), mods=[
      m(O('ex', 'sup'), set=dict(oxy=3)), m(O('loc', 'pe'), add=dict(oxy=1)), m(Z1 + O('fet'), set=dict(oxy=0))]),
  # mid-lung capillary
  dict(d=f'M{AX} {CAP["mid"]} H{ALVX}', len=AX - ALVX, base=dict(deo=3), mods=[
      m(O('ex'), set=dict(deo=4)), m(O('loc'), add=dict(deo=1)), m(O('pe') + O('fet'), set=dict(deo=0))]),
  dict(d=f'M{ALVX} {CAP["mid"]} H{VX}', len=ALVX - VX, base=dict(oxy=3), mods=[
      m(O('ex'), set=dict(oxy=4)), m(O('loc'), add=dict(oxy=1)), m(O('pe') + O('fet'), set=dict(oxy=0))]),
  # base capillary (zone 3: the most flow)
  dict(d=f'M{AX} {CAP["base"]} H{ALVX}', len=AX - ALVX, base=dict(deo=5), mods=[
      m(O('ex'), set=dict(deo=7)), m(O('sup'), set=dict(deo=3)), m(O('loc'), set=dict(deo=1)),
      m(O('pe'), add=dict(deo=1)), m(O('fet'), set=dict(deo=1))]),
  dict(d=f'M{ALVX} {CAP["base"]} H{VX}', len=ALVX - VX, base=dict(oxy=5), mods=[
      m(O('ex'), set=dict(oxy=7)), m(O('sup'), set=dict(oxy=3)), m(O('loc'), set=dict(oxy=0), add=dict(deo=1)),
      m(O('pe'), add=dict(oxy=1)), m(O('fet'), set=dict(oxy=0, deo=1))]),
  # the recruited second capillaries
  dict(d=f'M{AX} {CAP["base"] + 34} H{VX}', len=AX - VX, base=dict(oxy=2), unless=O('fet'), mods=[m(O('ex'), set=dict(oxy=3))]),
  dict(d=f'M{AX} {CAP["mid"] + 34} H{VX}', len=AX - VX, when=O('ex'), base=dict(oxy=3)),
  dict(d=f'M{AX} {CAP["ap"] + 34} H{VX}', len=AX - VX, when=O('ex'), base=dict(oxy=2)),
  # down the vein to the left atrium
  dict(d=f'M{VX} {CAP["ap"]} V1330 H1250 Q1340 1330 1380 1080', len=848 + 530 + 270, base=dict(oxy=6), mods=[
      m(O('ex'), set=dict(oxy=11)), m(O('hem'), set=dict(oxy=3)), m(O('fet'), set=dict(oxy=1)), m(O('lhf'), speed=.5)]),
  # air into each alveolus (ventilation rises toward the base, less steeply than blood flow)
  dict(d=f'M{ALVX} {LEV["ap"] - 160} V{LEV["ap"] - 20}', len=140, speed=80, base=dict(air=1), unless=O('fet'),
       mods=[m(O('ex'), set=dict(air=2)), m(O('ppv'), set=dict(air=2))]),
  dict(d=f'M{ALVX} {LEV["mid"] - 160} V{LEV["mid"] - 20}', len=140, speed=80, base=dict(air=2), unless=O('fet'),
       mods=[m(O('ex'), set=dict(air=3))]),
  dict(d=f'M{ALVX} {LEV["base"] - 160} V{LEV["base"] - 20}', len=140, speed=80, base=dict(air=2), unless=O('fet', 'loc'),
       mods=[m(O('ex'), set=dict(air=3))]),
]

# ════════ sites (tap targets) ════════
sites = [
  dict(x=ALVX, y=LEV['ap'] + 54, n=[0, 1], w=8, t='ch', l='Apex capillaries', s='', ions=[['air', 'out', 1]], reach=12,
       lx=LX, ly=430, la='start', c='westzones', block=Z1, boost=ALLZ3, stop=O('fet'),
       sfx=dict(block=' — squeezed shut', boost=' — open all the time', stop=' — little flow')),
  dict(x=ALVX, y=LEV['mid'] + 54, n=[0, 1], w=8, t='ch', l='Mid-lung capillaries', s='', ions=[['air', 'out', 1]], reach=12,
       lx=LX, ly=830, la='start', c='westzones', block=O('pe'), stop=O('fet'), boost=O('ex'),
       sfx=dict(block=' — no blood (embolus)', stop=' — little flow', boost=' — recruited')),
  dict(x=ALVX, y=LEV['base'] + 54, n=[0, 1], w=8, t='ch', l='Base capillaries', s='', ions=[['air', 'out', 1]], reach=12,
       lx=LX, ly=1180, la='start', c='westzones', low=O('loc'), stop=O('fet'), boost=O('ex'),
       sfx=dict(low=' — blood steered away', stop=' — little flow', boost=' — recruited')),
  dict(x=AX - 56, y=CAP['base'], n=[0, 1], w=16, t='rec', l='Arteriole smooth muscle', s='constricts when alveolar PO₂ < ~70',
       ions=[], lx=AX - 56, ly=CAP['base'] + 50, la='middle', c='pulmcirc', boost=O('loc') + NARROW,
       sfx=dict(boost=' — constricted')),
  dict(x=AX - 44, y=CAP['mid'], n=[0, -1], w=12, t='wall', l='Embolus', s='blocks the branch', ions=[], when=O('pe'),
       lx=AX + 30, ly=CAP['mid'] + 18, la='start', c='pe', block=O('pe'), sfx=dict(block='')),
  dict(x=1580, y=1225, n=[0, 1], w=14, t='pump', l='Right ventricle', s='25/0–1 mm Hg', ions=[], lx=1600, ly=1140, la='middle',
       c='pulmpress', boost=O('lhf', 'pah', 'alt', 'fet'), low=O('hem'), sfx=dict(boost=' — higher afterload', low=' — less filled')),
  dict(x=1420, y=1060, n=[0, -1], w=14, t='rec', l='Left atrium', s='≈ wedge pressure, about 2 mm Hg', ions=[], lx=1340, ly=1124, la='end',
       c='pulmpress', boost=O('lhf'), sfx=dict(boost=' — pressure ↑')),
  dict(x=VX + 10, y=680, n=[-1, 0], w=12, t='rec', l='Bronchial veins', s='→ pulmonary veins: physiologic shunt', ions=[],
       lx=LX, ly=640, la='start', c='bronchcirc'),
]

notes = {
  '': 'Upright at rest: the lung is about 30 cm tall, so pulmonary arterial pressure is about 15 mm Hg lower at the apex than at heart '
      'level and about 8 mm Hg higher at the base. The apices are zone 2 (flow only in systole), all the lower lung is zone 3, and the '
      'base gets about 5× the flow of the apex. Ventilation also rises toward the base, but less, so V/Q is about 3 at the apex and 0.6 '
      'at the base.',
  'st:sup': 'Lying down, no part of the lung is more than a few centimetres above the heart, so the whole lung — apices included — '
            'is zone 3 and blood flow is nearly uniform from top to bottom.',
  'st:ex': 'Exercise raises pulmonary pressures enough to turn the apices from zone 2 into zone 3: flow rises in every part of the lung, '
           'apical V/Q falls toward 1 and less ventilation is wasted. Flow can rise 4- to 7-fold, yet pulmonary artery pressure barely '
           'rises — up to 3× more capillaries open (recruitment) and each widens (distension), so PVR falls; PaO₂ is maintained.',
  'st:hem': 'After severe blood loss, pulmonary arterial pressure at the apex no longer beats alveolar pressure, so the apical capillaries '
            'are squeezed shut through the whole cycle — zone 1. Those alveoli are ventilated but not perfused: they add to the '
            'physiologic dead space.',
  'st:ppv': 'Positive-pressure breathing (as on a ventilator) raises alveolar pressure; at the apex it now beats arterial pressure, the '
            'capillaries close and zone 1 appears. The apical alveoli are ventilated but not perfused, adding to physiologic dead space.',
  'st:lov': 'At low lung volume the extra-alveolar vessels (arteries and veins outside the alveolar walls) are no longer pulled open by '
            'a more negative intrapleural pressure, so they narrow and PVR rises.',
  'st:hiv': 'At high lung volume the inflated alveoli crush the alveolar vessels (the capillaries), and their resistance rises sharply. '
            'PVR is the sum of the two, so it is high at both extremes of lung volume.',
  'st:loc': 'When one region stops being ventilated (lobar pneumonia, a blocked airway, atelectasis) its alveolar PO₂ falls; below about '
            '70 mm Hg the nearby arterioles constrict and steer blood to well-ventilated alveoli — hypoxic vasoconstriction, the opposite '
            'of systemic vessels. Overall PVR is unchanged, but the rescue fails when disease is widespread (multilobar pneumonia).',
  'st:alt': 'At altitude (or breathing a low-O₂ mix) alveolar PO₂ is low everywhere, so hypoxic vasoconstriction is global: PVR and '
            'pulmonary artery pressure rise. Chronic, it causes pulmonary hypertension with right ventricular hypertrophy (group 3).',
  'st:fet': 'The fetus does not breathe, so alveolar PO₂ is low and the whole pulmonary bed is constricted: PVR and pulmonary artery '
            'pressure are high and only about 15% of the cardiac output goes through the lungs — the rest crosses the ductus arteriosus '
            'to the aorta. The first breath raises alveolar PO₂, reverses the constriction and PVR falls.',
  'st:pe': 'A pulmonary embolus blocks a branch of the pulmonary artery: its alveoli are ventilated but not perfused — V/Q = ∞, dead '
           'space. The diverted blood goes to the rest of the lung, and the patient is hypoxemic, tachypneic and alkalotic; unlike a '
           'shunt, 100% O₂ improves PaO₂.',
  'st:lhf': 'Left heart failure or mitral stenosis dams blood back into the lungs — their blood volume can double. Once left atrial '
            'pressure passes about 7–8 mm Hg, each further rise lifts capillary and pulmonary artery pressure almost equally: a load on '
            'the right heart (pulmonary hypertension group 2) and, high enough, pulmonary edema. Wedge pressure tracks left atrial '
            'pressure, but in mitral stenosis it exceeds LV end-diastolic pressure.',
  'st:pah': 'Pulmonary arterial hypertension (group 1 — often idiopathic, heritable with BMPR2 mutations; also drugs, connective tissue '
            'disease, HIV, portal hypertension): endothelial dysfunction raises endothelin and lowers NO and prostacyclin. The arterioles '
            'thicken and narrow, PVR rises, mean pulmonary artery pressure exceeds 20 mm Hg at rest, and the RV hypertrophies, then fails.',
}

R = lambda when, d: dict(when=O(*when), d=d)
readouts = [
  dict(l='Flow at the apex', mods=[R(('sup', 'ex'), 1), R(('hem', 'ppv'), -1)]),
  dict(l='Zone 1 (no flow)', mods=[R(('hem', 'ppv'), 1)]),
  dict(l='PVR', mods=[R(('ex',), -1), R(('lov', 'hiv', 'alt', 'fet', 'pah'), 1), R(('loc',), 0)]),
  # exercise: "rises very little" (Guyton ch 39) → no arrow
  dict(l='PA pressure', mods=[R(('hem',), -1), R(('alt', 'fet', 'lhf', 'pah'), 1)]),
  dict(l='Dead space', mods=[R(('ex',), -1), R(('hem', 'ppv', 'pe'), 1)]),
  dict(l='PaO₂', mods=[R(('ex',), 0), R(('alt', 'pe'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='st', label='State', type='one', options=[
                ['sup', 'Lying down (supine)', 'westzones'], ['ex', 'Exercise', 'pulmex'],
                ['hem', 'Hemorrhage — Pa falls', 'westzones'], ['ppv', 'Positive-pressure breathing', 'westzones'],
                ['lov', 'Low lung volume', 'pulmcirc'], ['hiv', 'High lung volume', 'pulmcirc'],
                ['loc', 'Local hypoxia — lobar pneumonia', 'pulmcirc'], ['alt', 'Global hypoxia — altitude', 'altitude'],
                ['fet', 'Fetal lung', 'fetalcirc'],
                ['pe', 'Pulmonary embolism', 'pe'], ['lhf', 'Left heart failure · mitral stenosis', 'hf'],
                ['pah', 'Pulmonary arterial hypertension', 'pulmhtn']],
                 sections=[['Posture & exercise', ['sup', 'ex']],
                           ['Zone 1 appears', ['hem', 'ppv']],
                           ['Lung volume', ['lov', 'hiv']],
                           ['Hypoxic vasoconstriction', ['loc', 'alt', 'fet']],
                           ['Disease', ['pe', 'lhf', 'pah']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2400, y=110, w=1000),
  src='First Aid pp. 300, 684–685, 688, 691, 698 · Costanzo ch 5 · Guyton ch 39–40 · Bootcamp Pulmonology')

MAP = dict(
  id='pulmflow', title='Pulmonary Blood Flow & Zones in Motion', topic='pulmo', after='gasx',
  sub='Blood climbs an upright lung from the right ventricle and crosses three alveoli — apex, mid-lung, base — through zones 2 and 3; '
      'lie down, exercise, bleed, ventilate, change lung volume, turn on hypoxic vasoconstriction, or add an embolus, heart failure or '
      'pulmonary hypertension, and read apical flow, zone 1, PVR, PA pressure, dead space and PaO₂. Tap a capillary for its card',
  w=3460, h=2080,
  fa='300, 684–685, 688, 691, 698', src=SRC,
  lanes=[('pfFlow', 'Blood flow & zones', 'glycolysis'), ('pfVr', 'Resistance & vasoconstriction', 'gluconeo'),
         ('pfDz', 'Disorders', 'tca')],
  comps=[],
  nodes=[
    ('pf1', 'West zones', 260, 1930, 'pfFlow', 'PA vs Pa vs Pv · V/Q apex → base', ['westzones', 'vq'], 'hub'),
    ('pf2', 'Pulmonary pressures', 640, 1930, 'pfFlow', '25/8 · wedge ≈ left atrium', ['pulmpress']),
    ('pf3', 'Flow in exercise', 1020, 1930, 'pfFlow', 'recruit + distend', ['pulmex']),
    ('pf4', 'Bronchial circulation', 1400, 1930, 'pfFlow', 'the normal shunt', ['bronchcirc']),
    ('pf5', 'Hypoxic vasoconstriction', 1780, 1930, 'pfVr', 'PVR · local and global', ['pulmcirc', 'altitude'], 'hub'),
    ('pf6', 'Fetal lung', 2160, 1930, 'pfVr', 'high PVR until the first breath', ['fetalcirc']),
    ('pf7', 'Dead space', 260, 2020, 'pfDz', 'zone 1 · embolus', ['deadspace', 'pe']),
    ('pf8', 'Collapsed or filled alveoli', 640, 2020, 'pfDz', 'local hypoxia', ['pneumonia', 'atelectasis']),
    ('pf9', 'Left heart → lungs', 1020, 2020, 'pfDz', 'group 2 · edema', ['hf', 'mitralsten', 'pulmedema']),
    ('pf10', 'Pulmonary hypertension', 1400, 2020, 'pfDz', 'groups 1–5 · drugs', ['pulmhtn', 'pahdrugs'], 'hub'),
    ('pf11', 'Lung volumes', 1780, 2020, 'pfVr', 'and PVR', ['lungvol']),
  ],
  panels=[
    (1170, 1480, 1130, 'Normal pressures in the lung (Guyton ch 39; First Aid pp. 300, 684)', [
      ('Right ventricle', 'about 25/0–1 mm Hg — one-fifth of the left ventricle'),
      ('Pulmonary artery', 'about 25/8 mm Hg, mean 15'),
      ('Capillaries · left atrium', 'mean about 7 · about 2 mm Hg (1–5)'),
      ('Wedge pressure', 'about 5 mm Hg, 2–3 above left atrial · above LVEDP in mitral stenosis'),
      ('PVR', '(pulmonary artery − left atrial pressure) ÷ cardiac output')]),
    (2400, 1500, 1000, 'Pulmonary hypertension — five groups (First Aid p. 698)', [
      ('1 · arterial', 'idiopathic, BMPR2, drugs, connective tissue disease, HIV, portal hypertension'),
      ('2 · left heart', 'systolic or diastolic dysfunction, valve disease'),
      ('3 · lung or hypoxia', 'COPD, interstitial lung disease, sleep apnea, high altitude'),
      ('4 · thromboembolic', 'recurrent microthrombi shrink the vascular bed'),
      ('5 · multifactorial', 'hematologic, systemic, metabolic, tumor compression')]),
  ],
  dyn=dyn,
)
