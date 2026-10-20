# m55 — Clearance & Glomerular Dynamics Simulator (dynamic map, kit data)
# The glomerulus and proximal tubule as a clearance machine. Plasma enters through the afferent arteriole, crosses one
# glomerular capillary inside Bowman's capsule (water and small solutes filter out into Bowman's space) and leaves
# through the efferent arteriole into the peritubular capillary that runs above the proximal tubule. In the tubule
# glucose is taken back by SGLT2, water and about half the urea follow, and PAH (and a little creatinine) is secreted
# from the peritubular blood, so what reaches the urine shows each substance's clearance. Above the capsule, bars for
# the three Starling pressures (Guyton's numbers) add up to the net pressure and, with Kf, to the GFR; each option
# lengthens or shortens the pressure it changes. On the right, the glucose titration curve (filtered, reabsorbed,
# excreted against plasma glucose, GFR 125 mL/min) with a marker for the current state, and a clearance scale with
# Guyton's clearances for glucose, Na⁺, urea, inulin, creatinine and PAH. One `one` switch, in sections: arterioles ·
# pressures & volume · glucose load · glucose — drug & pregnancy. Readouts: GFR, RPF, FF, PAH clearance, urine glucose,
# serum creatinine.
# Not a repeat of nephflow (its 4-option "glomerular vessels" switch: NSAID, ACEi/ARB, ANP, sympathetic) or rbflow
# (static autoregulation map): this map is about the Starling sums, the clearance arithmetic and the titration curve.
#
# Sources (all read in the corpus, U+00A0/U+00AD normalized):
#   First Aid 2025 p. 600 (Cx = UxV/Px; Cx < GFR reabsorbed or not freely filtered, > GFR secreted, = GFR neither; inulin
#     clearance = GFR = Kf[(PGC − PBS) − (πGC − πBS)], πBS normally 0; normal GFR ≈ 100 mL/min; creatinine clearance slightly
#     overestimates GFR — moderately secreted by the proximal tubule; eRPF = C PAH, PAH 20% filtered, 80% secreted, ~100%
#     excreted; eRPF slightly underestimates RPF; RBF = RPF/(1 − Hct), 20–25% of cardiac output) · p. 601 (FF = GFR/RPF,
#     normal 20%; filtered load = GFR × P; prostaglandins dilate afferent, angiotensin II constricts efferent; NSAIDs and ACE
#     inhibitors not together; table: afferent constriction ↓↓—, efferent constriction ↑↓↑, ↑ plasma protein ↓—↓,
#     ↓ plasma protein ↑—↑, ureter constriction ↓—↓, dehydration ↓ ↓↓ ↑) · p. 602 (filtered load, excretion, reabsorption,
#     secretion; glucose 60–120 mg/dL fully reabsorbed in the PCT by Na⁺/glucose cotransport; glucosuria from ~200 mg/dL =
#     threshold; ~375 mg/min all transporters saturated = Tm; splay from nephron heterogeneity; pregnancy ↑ GFR → threshold at
#     lower plasma glucose → glucosuria at normal plasma glucose; SGLT2 inhibitors → glucosuria below 200 mg/dL) · p. 607
#     (prostaglandins dilate afferent arterioles → ↑ RBF; NSAIDs → afferent constriction → ↓ GFR, AKI in low-flow states) ·
#     p. 618 (hydronephrosis: serum creatinine rises only if the obstruction is bilateral or the kidney solitary) · p. 651
#     (pregnancy: ↑ GFR, ↓ BUN and creatinine, mild glucosuria).
#   Costanzo ch 6 (clearance of albumin and glucose ≈ 0; Na⁺, urea, phosphate, Cl⁻ filtered and partly reabsorbed; inulin =
#     glomerular marker; PAH and organic bases highest clearances; clearance ratios; Kf > 100× systemic capillaries, GFR
#     180 L/day; PGC constant along the capillary because of the efferent arteriole; πGC is the only pressure that rises
#     along the capillary; blood leaving has high π → drives proximal reabsorption; afferent constriction ↓ RPF, ↓ PGC, ↓ GFR
#     (sympathetic, high angiotensin II); efferent constriction ↓ RPF, ↑ PGC, ↑ GFR (low angiotensin II); high angiotensin II
#     (hemorrhage) → ↓ RPF, smaller ↓ GFR — GFR "protected"; ACE inhibitors remove that protection; ↑ plasma protein ↑ πGC
#     ↓ GFR; ↓ plasma protein (nephrotic syndrome) ↑ GFR; ureteral stone/constriction ↑ PBS ↓ GFR; Table 6.6; when GFR falls,
#     BUN and serum creatinine rise; prerenal azotemia: urea reabsorbed, creatinine not → BUN:Cr > 20; FF ≈ 0.20, ↑ FF → ↑
#     peritubular π; titration curve: reabsorption = filtration below 200 mg/dL, bends above 200, saturates (Tm), excretion
#     parallels filtration after Tm; splay — low-affinity carrier and nephron heterogeneity; pregnancy ↑ GFR → filtered load
#     may exceed capacity; Box 6.1 Tm 375 mg/min; 50% of filtered urea reabsorbed in the proximal tubule; SGLT2 inhibitors →
#     more Na⁺ at the macula densa → adenosine → afferent constriction → ↓ GFR, offsetting diabetic hyperfiltration).
#   Guyton ch 27 (GFR 125 mL/min, 180 L/day; FF ≈ 0.2; PGC 60, PBS 18, πGC 28 → 36, mean 32, πBS 0 → net +10 mm Hg;
#     Kf = 125/10 = 12.5 mL/min per mm Hg, ≈ 400× other capillaries; obstruction (stones) ↑ PBS ↓ GFR → hydronephrosis;
#     plasma protein rises ~20% along the capillary; ↑ FF → faster rise of π, ↓ FF the opposite; ↑ arterial π → ↓ GFR;
#     afferent dilation ↑ PGC ↑ GFR; moderate efferent constriction ↑ GFR, severe (> 3-fold) ↓ GFR; Table 27.2).
#   Guyton ch 28 (glucose Tm ≈ 375 mg/min; filtered load 125 mg/min at 100 mg/dL with GFR 125; above ~200 mg/dL (filtered
#     load > 250 mg/min) glucose appears = threshold, before Tm, because nephrons differ; urea about half reabsorbed (46.8 g
#     filtered, 23.4 g excreted per day); creatinine essentially not reabsorbed, slightly secreted, plasma creatinine
#     inversely related to GFR; PAH ~90% cleared: C PAH 585 mL/min ÷ 0.9 = RPF 650; FF = 125/650 = 0.19; clearances in mL/min:
#     glucose 0, Na⁺ 0.9, Cl⁻ 1.3, K⁺ 12, phosphate 25, inulin 125, creatinine 140).
#   Bootcamp.com Nephrology — Fluid and filtration physiology (afferent dilation ↑ GFR ↑ RPF no ΔFF; efferent dilation ↓ GFR
#     ↑ RPF ↓ FF; ↑/↓ plasma oncotic pressure; ureteral constriction; dehydration; pregnancy → glucosuria without hyperglycemia;
#     threshold ~200 mg/dL, splay).
#   OCOM Nephro — SDL 46 reading: ScholarRx, RAAS inhibitors (angiotensin II holds up GFR by efferent constriction; RAAS
#     inhibitors + NSAIDs → afferent dilation lost + efferent dilated → ↓ GFR → prerenal AKI; modest creatinine rise after
#     starting an ACE inhibitor — via the raasgfr card).
# Numbers recomputed: net = 60 − 18 − 32 = +10 mm Hg; afferent end 60 − 18 − 28 = +14, efferent end 60 − 18 − 36 = +6;
#   GFR = 12.5 × 10 = 125 mL/min; FF = 125/650 = 0.19; filtered glucose = 1.25 dL/min × P: 100 mg/dL → 125, 200 → 250,
#   500 → 625 mg/min; at 500 mg/dL excreted = 625 − 375 = 250 mg/min, glucose clearance = 250 mg/min ÷ 5 mg/mL = 50 mL/min;
#   urea clearance ≈ half the GFR (23.4/46.8 excreted).
# Cut for lack of a source: the plasma glucose at which every nephron is saturated (the curve bends gradually; no number is
#   printed); RPF and FF in pregnancy, after an SGLT2 inhibitor and after NSAID + ACE inhibitor (no source gives them);
#   Starling-pressure changes in volume contraction and pregnancy; serum creatinine arrows for afferent constriction or
#   dilation, efferent constriction and the plasma-protein options (no source ties them; GFR-rising states other than
#   pregnancy left "–"); creatinine in unilateral obstruction (rises only if bilateral — note says so, no arrow); myeloma as
#   the example of ↑ plasma protein (no corpus text names it); Kf changes (Guyton: not a normal regulator); ANP and
#   catecholamine options (already on nephflow); volume expansion (no GFR/RPF/FF table row).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ6, GY27, GY28 = full('Costanzo', 6), full('Guyton', 27), full('Guyton', 28)
BC = 'Bootcamp.com Nephrology — Fluid and filtration physiology'
RAAS = 'OCOM Nephro — SDL 46 reading: ScholarRx, Renin-angiotensin-aldosterone system inhibitors'
SRC = [CZ6, GY27, GY28, BC, RAAS]

O = lambda *k: ['st:' + x for x in k]
GFR_DN = O('affc', 'effd', 'nsacei', 'obst', 'protu', 'dehyd', 'sglt2')
GFR_UP = O('affd', 'effc', 'protd', 'preg')
GLU_SPILL = O('gthr', 'gtm', 'sglt2', 'preg')

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
CX, CY, CR = 640, 760, 220          # Bowman's capsule
CAPY = CY                           # the glomerular capillary runs straight across it
AFF0, CAP0, CAP1 = 180, CX - CR + 6, CX + CR - 6
TY = 1190                           # proximal tubule (horizontal run)
PTY = 1080                          # peritubular capillary above it
TX1 = 1460                          # the tubule turns down to the urine here

# ════════ title ════════
text('One glomerulus and its proximal tubule — a clearance machine', 180, 160, 'dyn-big')
text('Plasma filters across the capillary into Bowman’s space; the tubule then takes back or adds each substance — the urine shows the sum',
     180, 184, 'dyn-cap')

# ════════ Starling bars (Guyton ch 27): scale 7 px per mm Hg ════════
BX, SC = 420, 7
text('Starling pressures, mm Hg (Guyton’s estimates)', 180, 236, 'nf-l1')
ROWS = [('P_GC', 'PGC — favors filtration', 60, 272, '--dk2'),
        ('P_BS', 'PBS — opposes', 18, 312, '--dk1'),
        ('PI', 'πGC — opposes (28 → 36)', 32, 352, '--dk10')]
CHG = {   # which bar each option lengthens (+) or shortens (−)
  'P_GC': [(O('affc', 'effd', 'nsacei', 'sglt2'), -1), (O('affd', 'effc'), 1)],
  'P_BS': [(O('obst'), 1)],
  'PI':   [(O('protu'), 1), (O('protd'), -1)],
}
ALLCHG = sum([w for v in CHG.values() for w, _ in v], [])
for key, lab, mm, y, col in ROWS:
    text(lab, BX - 16, y + 5, 'nf-l2', 'end')
    full_w = mm * SC
    bar = lambda w, extra='': f'<rect x="{BX}" y="{y - 12}" width="{w}" height="22" rx="6" fill="var({col})" opacity=".75"{extra}/>'
    chg = CHG.get(key, [])
    others = sum([w for w, _ in chg], [])
    add(bar(full_w), unless=others or None)
    text(f'{mm}', BX + full_w + 12, y + 5, 'nf-l1', unless=others or None)
    for when, sgn in chg:
        w2 = round(full_w * (1.3 if sgn > 0 else 0.7))
        add(bar(w2) + f'<rect x="{BX}" y="{y - 12}" width="{full_w}" height="22" rx="6" class="dyn-dash" fill="none"/>', when=when)
        text(('↑' if sgn > 0 else '↓') + ' from ' + str(mm), BX + max(w2, full_w) + 12, y + 5, 'nf-l1', when=when)
# net
NY = 404
add(f'<path d="M180 {NY - 26} H1180" class="dyn-line" style="opacity:.35"/>')
text('Net = 60 − 18 − 32 = +10 mm Hg', BX - 16, NY + 5, 'nf-l1', 'end')
add(f'<rect x="{BX}" y="{NY - 12}" width="{10 * SC}" height="22" rx="6" fill="var(--accent)"/>', unless=GFR_DN + GFR_UP)
add(f'<rect x="{BX}" y="{NY - 12}" width="{4 * SC}" height="22" rx="6" fill="var(--accent)"/>'
    f'<rect x="{BX}" y="{NY - 12}" width="{10 * SC}" height="22" rx="6" class="dyn-dash" fill="none"/>', when=GFR_DN)
add(f'<rect x="{BX}" y="{NY - 12}" width="{15 * SC}" height="22" rx="6" fill="var(--accent)"/>'
    f'<rect x="{BX}" y="{NY - 12}" width="{10 * SC}" height="22" rx="6" class="dyn-dash" fill="none"/>', when=GFR_UP)
text('× Kf 12.5 mL/min per mm Hg = GFR 125 mL/min', BX + 140, NY + 5, 'nf-l2', unless=GFR_DN + GFR_UP)
text('net pressure ↓ → GFR ↓', BX + 140, NY + 5, 'nf-l1', when=GFR_DN)
text('net pressure ↑ → GFR ↑', BX + 140, NY + 5, 'nf-l1', when=GFR_UP)

# ════════ Bowman's capsule + the glomerular capillary ════════
add(f'<circle cx="{CX}" cy="{CY}" r="{CR}" class="dyn-cell"/>'
    f'<circle cx="{CX}" cy="{CY}" r="{CR - 18}" class="dyn-soft"/>')
text('Bowman’s space', CX, CY - 150, 'nf-l1', 'middle')
text('πBS ≈ 0 — almost no protein filters', CX, CY - 132, 'nf-l2', 'middle')
# obstruction: fluid backs up into Bowman's space
add(f'<circle cx="{CX}" cy="{CY}" r="{CR - 18}" fill="var(--nf-h2o)" opacity=".28"/>', when=O('obst'))
text('urine backs up — PBS ↑', CX, CY + 160, TAG, 'middle', when=O('obst'))
# the vessels
shapes.append(dict(vessel=f'M{AFF0} {CAPY} H{CAP0}', w=28, color='--dk2',
                   mods=[dict(when=O('affc'), d=-12), dict(when=O('affd'), d=10), dict(when=O('nsacei'), d=-12),
                         dict(when=O('dehyd'), d=-8), dict(when=O('sglt2'), d=-6)]))
shapes.append(dict(vessel=f'M{CAP0} {CAPY} H{CAP1}', w=34, color='--dk2', mods=[dict(when=O('affd', 'effc'), d=4)]))
shapes.append(dict(vessel=f'M{CAP1} {CAPY} H1020 V{PTY} H{TX1 + 40} V{CAPY} H1560', w=22, color='--dk2',
                   mods=[dict(when=O('effc'), d=-10), dict(when=O('effd', 'nsacei'), d=8), dict(when=O('dehyd'), d=-10)]))
text('glomerular capillary', CX, CAPY + 50, 'nf-l1', 'middle')
text('PGC stays high along its length', CX, CAPY + 68, 'nf-l2', 'middle')
text('afferent end: 60 − 18 − 28 = +14', CAP0 + 20, CAPY + 108, 'nf-l2')
text('efferent end: 60 − 18 − 36 = +6', CAP0 + 20, CAPY + 126, 'nf-l2')
text('renal vein →', 1580, CAPY + 6, 'nf-l2')
text('peritubular capillary', 1100, PTY - 26, 'nf-l1')
text('leaves with π ≈ 36 — pulls fluid back', 1100, PTY - 46, 'nf-l2', unless=O('effc', 'dehyd', 'effd'))
text('higher FF → higher π → more proximal reabsorption', 1100, PTY - 46, TAG, when=O('effc', 'dehyd'))
text('lower FF → lower π', 1100, PTY - 46, TAG, when=O('effd'))
# arteriole states
text('afferent constricted', 270, CAPY - 40, TAG, 'middle', when=O('affc', 'nsacei', 'dehyd'))
text('afferent narrowed (TGF)', 270, CAPY - 40, TAG, 'middle', when=O('sglt2'))
text('afferent dilated', 270, CAPY - 40, TAG, 'middle', when=O('affd'))
text('efferent constricted', 920, CAPY - 40, TAG, 'middle', when=O('effc', 'dehyd'))
text('efferent dilated', 920, CAPY - 40, TAG, 'middle', when=O('effd', 'nsacei'))
text('plasma protein ↑ — πGC ↑', CX, CY + 160, TAG, 'middle', when=O('protu'))
text('plasma protein ↓ — πGC ↓', CX, CY + 160, TAG, 'middle', when=O('protd'))
text('GFR ↑ — more glucose filtered', CX, CY + 160, TAG, 'middle', when=O('preg'))

# ════════ the proximal tubule → urine ════════
shapes.append(dict(tube=f'M{CX} {CY + CR - 10} V{TY} H{TX1} V1500', w=40, color='--dk3'))
text('proximal tubule', 760, TY + 70, 'nf-l1')
text('urine', TX1 + 40, 1490, 'nf-l1')
text('C = U × V ÷ P', TX1 + 40, 1510, 'nf-l2')
# glucose in the urine
text('glucose in the urine', TX1 + 40, 1450, TAG, when=GLU_SPILL)

# ════════ graph 1: the glucose titration curve (GFR 125 mL/min) ════════
GX0, GY0, GX1, GY1 = 1720, 1000, 2290, 300     # axes: x 0–800 mg/dL, y 0–1000 mg/min
def gx(p): return round(GX0 + (GX1 - GX0) * p / 800)
def gy(v): return round(GY0 - (GY0 - GY1) * v / 1000)
text('Glucose titration curve', GX0 - 60, 236, 'nf-l1')
text('GFR 125 mL/min · Tm ≈ 375 mg/min', GX0 - 60, 256, 'dyn-cap')
add(f'<path d="M{GX0} {GY1} V{GY0} H{GX1}" class="dyn-line"/>')
for v in (0, 250, 500, 750, 1000):
    text(str(v), GX0 - 10, gy(v) + 5, 'nf-l2', 'end')
for p in (0, 200, 400, 600, 800):
    text(str(p), gx(p), GY0 + 22, 'nf-l2', 'middle')
text('plasma glucose, mg/dL →', GX1, GY0 + 48, 'nf-l2', 'end')
text('mg/min', GX0 - 10, GY1 - 16, 'nf-l2', 'end')
# filtered: 1.25 × P
add(f'<path d="M{gx(0)} {gy(0)} L{gx(800)} {gy(1000)}" class="dyn-trace" style="stroke:var(--dk1)"/>')
text('filtered', gx(640) - 12, gy(800) - 6, 'nf-l1', 'end')
# reabsorbed: = filtered to 200 mg/dL, splay, plateau at 375
REAB = f'M{gx(0)} {gy(0)} L{gx(200)} {gy(250)} C{gx(260)} {gy(325)} {gx(320)} {gy(372)} {gx(420)} {gy(375)} L{gx(800)} {gy(375)}'
add(f'<path d="{REAB}" class="dyn-trace" style="stroke:var(--ok)"/>', unless=O('sglt2'))
add(f'<path d="{REAB}" class="dyn-trace dyn-dim" style="stroke:var(--ok)"/>', when=O('sglt2'))
text('reabsorbed', gx(800), gy(375) - 10, 'nf-l1', 'end')
text('Tm', gx(800) + 8, gy(375) + 5, 'nf-l2')
# excreted: 0 to 200, then filtered − reabsorbed
EXC = f'M{gx(0)} {gy(0)} L{gx(200)} {gy(0)} C{gx(260)} {gy(0)} {gx(320)} {gy(28)} {gx(420)} {gy(150)} L{gx(800)} {gy(625)}'
add(f'<path d="{EXC}" class="dyn-trace" style="stroke:var(--bad)"/>', unless=O('sglt2', 'preg'))
add(f'<path d="{EXC}" class="dyn-trace dyn-dim" style="stroke:var(--bad)"/>', when=O('sglt2', 'preg'))
text('excreted', gx(800) - 10, gy(625) + 26, 'nf-l1', 'end')
# threshold + splay
add(f'<path d="M{gx(200)} {gy(180)} V{gy(250) - 20}" class="dyn-dash"/><path d="M{gx(200)} {GY0} V{GY0 - 14}" class="dyn-line"/>')
text('threshold ≈ 200', gx(200) + 8, gy(250) - 24, 'nf-l2')
add(f'<rect x="{gx(200)}" y="{gy(375)}" width="{gx(420) - gx(200)}" height="{GY0 - gy(375)}" fill="var(--ink-3)" opacity=".08"/>')
text('splay', gx(310), GY0 - 12, 'dyn-cap', 'middle')
# pregnancy: a steeper filtered line → threshold at a lower plasma glucose
add(f'<path d="M{gx(0)} {gy(0)} L{gx(560)} {gy(1000)}" class="dyn-hl"/>', when=O('preg'))
text('filtered, GFR ↑', gx(560) - 10, gy(1000) + 4, 'nf-l1', 'end', when=O('preg'))
text('threshold at a lower plasma glucose', gx(430), gy(60), TAG, when=O('preg'))
# SGLT2 inhibitor: less reabsorbed, spill below 200
add(f'<path d="M{gx(0)} {gy(0)} L{gx(70)} {gy(87)} C{gx(110)} {gy(120)} {gx(160)} {gy(140)} {gx(260)} {gy(145)} L{gx(800)} {gy(145)}" class="dyn-hl"/>',
    when=O('sglt2'))
text('glucose spills below 200 mg/dL', gx(430), gy(60), TAG, when=O('sglt2'))
# the marker
def mark(p, v, lab, when=None, unless=None):
    add(f'<circle cx="{gx(p)}" cy="{gy(v)}" r="11" fill="var(--accent)" stroke="var(--surface)" stroke-width="3"/>', when=when, unless=unless)
GLU_OPT = O('gthr', 'gtm', 'sglt2', 'preg')
mark(100, 125, '', unless=GLU_OPT)
text('100 mg/dL: none excreted', gx(100) + 18, gy(125) + 40, 'nf-l2', unless=GLU_OPT)
mark(200, 250, '', when=O('gthr'))
text('200 mg/dL: 250 filtered — the first glucose escapes', gx(200) + 18, gy(250) + 34, 'nf-l1', when=O('gthr'))
mark(500, 625, '', when=O('gtm'))
mark(500, 375, '', when=O('gtm'))
mark(500, 250, '', when=O('gtm'))
text('500 mg/dL: 625 filtered', gx(500) - 16, gy(625) - 14, 'nf-l1', 'end', when=O('gtm'))
text('375 reabsorbed (Tm)', gx(500) - 16, gy(375) - 14, 'nf-l1', 'end', when=O('gtm'))
text('250 excreted', gx(500) + 18, gy(250) + 6, 'nf-l1', when=O('gtm'))
mark(100, 125, '', when=O('sglt2'))
mark(100, 155, '', when=O('preg'))

# ════════ graph 2: the clearance scale (Guyton ch 28) ════════
SX0, SX1 = 1720, 2290
def sx(c): return round(SX0 + (SX1 - SX0) * c / 600)
text('Clearance, mL/min (Guyton ch 28)', GX0 - 60, 1120, 'nf-l1')
CL = [('Glucose', 0, 1170), ('Na⁺', 0.9, 1210), ('Urea', 62, 1250), ('Inulin = GFR', 125, 1290),
      ('Creatinine', 140, 1330), ('PAH ≈ RPF', 585, 1370)]
add(f'<path d="M{SX0} 1150 V1392" class="dyn-line"/>')
for nm, c, y in CL:
    text(nm, SX0 - 12, y + 5, 'nf-l2', 'end')
    if nm == 'Glucose':
        text('0 — filtered, all reabsorbed', SX0 + 12, y + 5, 'nf-l2', unless=GLU_SPILL)
        add(f'<rect x="{SX0}" y="{y - 10}" width="{sx(50) - SX0}" height="18" rx="5" fill="var(--nf-glu)"/>', when=O('gtm'))
        text('50 at 500 mg/dL (250 ÷ 5)', sx(50) + 12, y + 5, 'nf-l1', when=O('gtm'))
        add(f'<rect x="{SX0}" y="{y - 10}" width="12" height="18" rx="5" fill="var(--nf-glu)"/>', when=O('gthr', 'sglt2', 'preg'))
        text('above 0 — glucose in the urine', SX0 + 24, y + 5, 'nf-l1', when=O('gthr', 'sglt2', 'preg'))
        continue
    w = max(4, sx(c) - SX0)
    col = {'Na⁺': '--nf-na', 'Urea': '--nf-urea', 'Inulin = GFR': '--dk4', 'Creatinine': '--dk7', 'PAH ≈ RPF': '--dk9'}[nm]
    add(f'<rect x="{SX0}" y="{y - 10}" width="{w}" height="18" rx="5" fill="var({col})"/>')
    lab = {'Na⁺': '0.9 — 99% reabsorbed', 'Urea': '≈ half the GFR — half reabsorbed', 'Inulin = GFR': '125 — only filtered',
           'Creatinine': '140 — filtered + a little secreted', 'PAH ≈ RPF': '585'}[nm]
    if nm == 'PAH ≈ RPF':
        text('585 — filtered + secreted', sx(585) - 12, y - 16, 'nf-l2', 'end')
    else:
        text(lab, SX0 + w + 12, y + 5, 'nf-l2')
add(f'<path d="M{sx(125)} 1272 V1392" class="dyn-dash" style="opacity:.6"/>')
text('below the line: reabsorbed · above: secreted', SX0, 1420, 'dyn-cap')

# ════════ particles ════════
kinds = dict(bl=['bl', '--dk2'], h2o=['h2o', '--nf-h2o'], inu=['inu', '--dk4'], cr=['cr', '--dk7'],
             pah=['pah', '--dk9'], glu=['glu', '--nf-glu'], urea=['urea', '--nf-urea'])
groups = [['bl', 'Blood'], ['h2o', 'Filtered water'], ['inu', 'Inulin'], ['cr', 'Creatinine'], ['pah', 'PAH'],
          ['glu', 'Glucose'], ['urea', 'Urea']]
def m(when, **kw):
    return dict(when=when if isinstance(when, list) else [when], **kw)
RPF_DN = O('affc', 'effc', 'dehyd')
RPF_UP = O('affd', 'effd')
flows = [
  # afferent arteriole → capillary
  dict(d=f'M{AFF0} {CAPY} H{CAP0}', len=CAP0 - AFF0, base=dict(bl=4, pah=1), mods=[
      m(RPF_DN, set=dict(bl=2)), m(O('dehyd'), set=dict(bl=1)), m(RPF_UP, set=dict(bl=6))]),
  dict(d=f'M{CAP0} {CAPY} H{CAP1}', len=CAP1 - CAP0, base=dict(bl=4), mods=[
      m(RPF_DN, set=dict(bl=2)), m(O('dehyd'), set=dict(bl=1)), m(RPF_UP, set=dict(bl=6))]),
  # efferent → peritubular → renal vein (PAH almost gone after the secretion sites)
  dict(d=f'M{CAP1} {CAPY} H1020 V{PTY} H{TX1 + 40} V{CAPY} H1560', len=(1020 - CAP1) + (PTY - CAPY) + (TX1 + 40 - 1020) + (PTY - CAPY) + 100,
       base=dict(bl=6), mods=[m(RPF_DN, set=dict(bl=3)), m(O('dehyd'), set=dict(bl=2)), m(RPF_UP, set=dict(bl=8))]),
  # Bowman's space → the first part of the tubule (everything filtered)
  dict(d=f'M{CX} {CY + CR - 30} V{TY} H1040', len=(TY - CY - CR + 30) + (1040 - CX), speed=110,
       base=dict(h2o=4, inu=1, cr=1, glu=2, urea=2, pah=1), mods=[
      m(GFR_DN, add=dict(h2o=-2, glu=-1)), m(GFR_UP, add=dict(h2o=2)),
      m(O('gthr'), set=dict(glu=3)), m(O('gtm'), set=dict(glu=5)), m(O('preg'), set=dict(glu=3))]),
  # the rest of the tubule → urine (glucose gone, PAH and creatinine added, half the urea left)
  dict(d=f'M1040 {TY} H{TX1} V1500', len=(TX1 - 1040) + (1500 - TY), speed=110,
       base=dict(h2o=1, inu=1, cr=2, urea=1, pah=3), mods=[
      m(O('gthr'), set=dict(glu=1)), m(O('gtm'), set=dict(glu=3)), m(O('sglt2'), set=dict(glu=2)), m(O('preg'), set=dict(glu=1)),
      m(RPF_DN, set=dict(pah=2)), m(RPF_UP, set=dict(pah=4))]),
]

# ════════ sites (tap targets) ════════
LBL = TY + 120          # labels under the tubule
sites = [
  # filtration across the capillary wall — two points, afferent and efferent ends
  dict(x=CX - 110, y=CAPY - 17, n=[0, -1], w=10, t='ch', l='Filtration', s='',
       ions=[['h2o', 'out', 2], ['inu', 'out', 1]], reach=60, lx=CX - 110, ly=CAPY - 96, la='middle', c='glomstarling',
       low=GFR_DN, boost=GFR_UP, sfx=dict(low=' ↓', boost=' ↑')),
  dict(x=CX + 110, y=CAPY - 17, n=[0, -1], w=10, t='ch', l='Filtration', s='',
       ions=[['h2o', 'out', 1], ['glu', 'out', 1]], reach=60, lx=CX + 110, ly=CAPY - 96, la='middle', c='gfrcalc',
       low=GFR_DN, boost=GFR_UP, sfx=dict(low=' ↓', boost=' ↑')),
  # the arterioles
  dict(x=280, y=CAPY, n=[0, 1], w=28, t='rec', l='Afferent arteriole', s='prostaglandins dilate it', ions=[],
       lx=280, ly=CAPY + 60, la='middle', c='glomdyn', boost=O('affc', 'nsacei', 'dehyd', 'sglt2'), low=O('affd'),
       sfx=dict(boost=' — constricted', low=' — dilated')),
  dict(x=1020, y=CAPY + 120, n=[1, 0], w=22, t='rec', l='Efferent arteriole', s='angiotensin II constricts it', ions=[],
       lx=1048, ly=CAPY + 116, la='start', c='raasgfr', boost=O('effc', 'dehyd'), low=O('effd', 'nsacei'),
       sfx=dict(boost=' — constricted', low=' — dilated')),
  # the tubule wall (top) — reabsorption up into the peritubular capillary, secretion down into the lumen
  dict(x=1100, y=TY - 22, n=[0, -1], w=10, t='co', l='SGLT2', s='glucose back to blood', ions=[['glu', 'out', 2]], reach=62,
       lx=1100, ly=LBL, la='middle', c='glucthresh', block=O('sglt2'), boost=O('gtm'),
       sfx=dict(boost=' — saturated (Tm)')),
  dict(x=1230, y=TY - 22, n=[0, -1], w=10, t='ch', l='Water, urea', s='about half the urea', ions=[['h2o', 'out', 2], ['urea', 'out', 1]],
       reach=62, lx=1230, ly=LBL + 44, la='middle', c='bunratio', boost=O('dehyd'), sfx=dict(boost=' — more taken back')),
  dict(x=1360, y=TY - 22, n=[0, -1], w=10, t='ex', l='PAH, creatinine', s='secreted from the blood', ions=[['pah', 'in', 2], ['cr', 'in', 1]],
       reach=62, lx=1360, ly=LBL, la='middle', c='erpf', low=RPF_DN, boost=RPF_UP),
  # Bowman's space (the urinary pole)
  dict(x=CX, y=CY + CR - 4, n=[1, 0], w=14, t='rec', l='Bowman’s space pressure', s='rises when urine backs up', ions=[],
       lx=CX + 40, ly=CY + CR + 50, la='start', c='obstructuro', boost=O('obst'), sfx=dict(boost=' ↑')),
  # the urine
  dict(x=TX1, y=1480, n=[-1, 0], w=40, t='rec', l='Clearance', s='what reaches the urine', ions=[],
       lx=TX1 - 40, ly=1476, la='end', c='renalclear'),
]

notes = {
  '': 'At rest (Guyton) capillary pressure 60 mm Hg pushes fluid out; Bowman’s space pressure 18 and capillary oncotic '
      'pressure 32 (28 → 36) push back: net +10. With a filtration coefficient of 12.5 that '
      'is a GFR of 125 mL/min from a renal plasma flow of 650: a filtration fraction of 0.19. Inulin clearance = GFR; PAH '
      'clearance ≈ RPF.',
  'st:affc': 'Afferent constriction (sympathetic nerves, high angiotensin II): less blood enters, so RPF falls, and the capillary '
             'pressure behind the narrowing falls, so GFR falls too. Both drop together, so the filtration fraction does not change. '
             'PAH clearance tracks RPF down.',
  'st:affd': 'Afferent dilation (prostaglandins): more blood enters at a higher pressure, so RPF and GFR both rise and the '
             'filtration fraction stays the same. This is the support an NSAID takes away.',
  'st:effc': 'Efferent constriction (angiotensin II, which prefers the efferent arteriole): blood is held in the glomerulus, so '
             'capillary pressure and GFR rise while RPF falls — the filtration fraction rises, and the peritubular blood leaves '
             'with a higher oncotic pressure. Very severe efferent constriction (over 3-fold) lowers GFR instead.',
  'st:effd': 'Efferent dilation (ACE inhibitor or ARB — angiotensin II lost): capillary pressure falls, so GFR and the filtration '
             'fraction fall while RPF rises. A modest rise in serum creatinine after starting the drug is expected; avoid it in '
             'bilateral renal artery stenosis.',
  'st:nsacei': 'NSAID with an ACE inhibitor: the afferent arteriole loses its prostaglandin dilation while the efferent arteriole '
               'loses its angiotensin II tone, so glomerular pressure has no support — GFR falls and prerenal acute kidney injury '
               'can follow, worst in patients already at risk. That is why the two are not given together.',
  'st:obst': 'Ureteral obstruction (a stone or constriction): urine backs up as far as Bowman’s space, so Bowman’s space pressure '
             'rises and GFR falls with RPF unchanged — the filtration fraction falls. Serum creatinine rises only if both sides are '
             'blocked or there is one kidney.',
  'st:protu': 'Plasma protein up: the capillary oncotic pressure starts higher and opposes filtration more, so GFR falls while RPF '
              'is unchanged — the filtration fraction falls.',
  'st:protd': 'Plasma protein down: capillary oncotic pressure falls, so net pressure and GFR rise with RPF unchanged — the '
              'filtration fraction rises (Costanzo Table 6.6). This is the Starling force alone; in nephrotic syndrome the '
              'glomerular disease itself decides the GFR.',
  'st:dehyd': 'Volume contraction (dehydration, hemorrhage): high angiotensin II squeezes the efferent arteriole hard and the '
              'afferent moderately, so RPF falls steeply and GFR falls less — GFR is “protected” and the filtration fraction '
              'rises. Urea is reabsorbed and creatinine is not, so BUN climbs more than creatinine (BUN:Cr > 20 — prerenal).',
  'st:gthr': 'Plasma glucose about 200 mg/dL: with a GFR of 125 the filtered load is 250 mg/min. Some nephrons have already reached '
             'their own maximum, so the first glucose escapes into the urine — the threshold — before the whole kidney reaches its '
             'Tm. The bend between threshold and Tm is the splay.',
  'st:gtm': 'Plasma glucose 500 mg/dL: 625 mg/min is filtered, the carriers are saturated at their Tm of about 375 mg/min, so '
            '250 mg/min is excreted — a glucose clearance of 50 mL/min. Past Tm the excretion line runs parallel to the filtered '
            'line. This is the glucosuria of uncontrolled diabetes mellitus, and it drags water with it (osmotic diuresis).',
  'st:sglt2': 'SGLT2 inhibitor (-flozin): the proximal Na⁺/glucose cotransporter is blocked, so glucose spills into the urine at a '
              'plasma glucose below 200 mg/dL. More Na⁺ reaches the macula densa, tubuloglomerular feedback constricts the afferent '
              'arteriole and GFR falls — which offsets the hyperfiltration of diabetes.',
  'st:preg': 'Pregnancy: GFR rises, so more glucose is filtered at the same plasma level and the threshold is reached at a lower '
             'plasma glucose — mild glucosuria with normal blood glucose. The higher GFR also lowers BUN and serum creatinine.',
}

R = lambda when, d: dict(when=O(*when), d=d)
readouts = [
  dict(l='GFR', mods=[R(('affc', 'effd', 'nsacei', 'obst', 'protu', 'dehyd', 'sglt2'), -1), R(('affd', 'effc', 'protd', 'preg'), 1)]),
  dict(l='RPF', mods=[R(('affc', 'effc', 'dehyd'), -1), R(('affd', 'effd'), 1), R(('obst', 'protu', 'protd'), 0)]),
  dict(l='FF', mods=[R(('effd', 'obst', 'protu'), -1), R(('effc', 'protd', 'dehyd'), 1), R(('affc', 'affd'), 0)]),
  dict(l='PAH clearance', mods=[R(('affc', 'effc', 'dehyd'), -1), R(('affd', 'effd'), 1), R(('obst', 'protu', 'protd'), 0)]),
  dict(l='Urine glucose', mods=[R(('gthr', 'gtm', 'sglt2', 'preg'), 1)]),
  dict(l='Serum creatinine', mods=[R(('effd', 'nsacei', 'dehyd'), 1), R(('preg',), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='st', label='Change one thing', type='one', options=[
                ['affc', 'Afferent constriction', 'glomdyn'], ['affd', 'Afferent dilation (prostaglandins)', 'glomdyn'],
                ['effc', 'Efferent constriction (angiotensin II)', 'glomdyn'], ['effd', 'Efferent dilation (ACE inhibitor)', 'raasgfr'],
                ['nsacei', 'NSAID + ACE inhibitor', 'nsaidkidney'],
                ['obst', 'Ureteral obstruction — PBS ↑', 'obstructuro'], ['protu', 'Plasma protein ↑ — πGC ↑', 'glomdyn'],
                ['protd', 'Plasma protein ↓', 'glomdyn'], ['dehyd', 'Volume contraction', 'prerenal'],
                ['gthr', 'Plasma glucose 200 — threshold', 'glucthresh'], ['gtm', 'Plasma glucose 500 — past Tm', 'glucthresh'],
                ['sglt2', 'SGLT2 inhibitor', 'sglt2'], ['preg', 'Pregnancy', 'pregphys']],
                 sections=[['Arterioles', ['affc', 'affd', 'effc', 'effd', 'nsacei']],
                           ['Pressures & volume', ['obst', 'protu', 'protd', 'dehyd']],
                           ['Glucose load', ['gthr', 'gtm']],
                           ['Glucose — drug & pregnancy', ['sglt2', 'preg']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2400, y=110, w=1000),
  src='First Aid pp. 600–602, 607, 618, 651 · Costanzo ch 6 · Guyton ch 27–28 · Bootcamp Nephrology · OCOM Nephro SDL 46')

MAP = dict(
  id='gfrsim', title='Clearance & Glomerular Dynamics Simulator', topic='renal', after='rbflow',
  sub='Plasma filters across a glomerular capillary into Bowman’s space and runs down the proximal tubule, where glucose is taken '
      'back and PAH is secreted — narrow or widen an arteriole, raise Bowman’s pressure or plasma protein, shrink the volume, or '
      'push glucose past its threshold and Tm, and read GFR, RPF, filtration fraction, PAH clearance, urine glucose and serum '
      'creatinine. Tap a transporter for its card',
  w=3460, h=1830,
  fa='600–602, 607, 618, 651', src=SRC,
  lanes=[('gsFilt', 'Filtration', 'glycolysis'), ('gsClear', 'Clearance', 'tca'), ('gsTube', 'Tubule & glucose', 'gluconeo'),
         ('gsDz', 'Drugs & disorders', 'sugars')],
  comps=[],
  nodes=[
    ('gs1', 'Glomerular Starling forces', 260, 1640, 'gsFilt', 'PGC · PBS · πGC · Kf', ['glomstarling'], 'hub'),
    ('gs2', 'GFR — inulin & creatinine', 560, 1640, 'gsClear', 'clearance = GFR', ['gfrcalc']),
    ('gs3', 'RPF & filtration fraction', 860, 1640, 'gsClear', 'PAH · FF = GFR / RPF', ['erpf'], 'hub'),
    ('gs4', 'Changes in glomerular dynamics', 1160, 1640, 'gsFilt', 'GFR · RPF · FF table', ['glomdyn']),
    ('gs5', 'Renal clearance', 1460, 1640, 'gsClear', 'Cx = Ux × V ÷ Px', ['renalclear', 'clearratio']),
    ('gs6', 'Glucose threshold & Tm', 1760, 1640, 'gsTube', 'titration curve · splay', ['glucthresh'], 'hub'),
    ('gs7', 'Filtered, reabsorbed, secreted', 2060, 1640, 'gsTube', 'filtered load · FENa', ['reabsec', 'pttfp']),
    ('gs8', 'Peritubular forces', 260, 1740, 'gsTube', 'glomerulotubular balance', ['gtbalance']),
    ('gs9', 'Autoregulation', 560, 1740, 'gsFilt', 'myogenic · TGF', ['rbfauto']),
    ('gs10', 'Arteriole drugs', 860, 1740, 'gsDz', 'NSAIDs · ACE inhibitors', ['nsaidkidney', 'raasgfr']),
    ('gs11', 'BUN, creatinine, prerenal', 1160, 1740, 'gsDz', 'BUN:Cr > 20', ['bunratio', 'prerenal']),
    ('gs12', 'Glucosuria drugs & states', 1460, 1740, 'gsDz', 'SGLT2 · pregnancy', ['sglt2', 'pregphys']),
    ('gs13', 'Obstruction & protein loss', 1760, 1740, 'gsDz', 'PBS ↑ · πGC ↓', ['obstructuro', 'hydroneph', 'nephrotic']),
  ],
  panels=[
    (2400, 1300, 1000, 'The clearance equations (First Aid pp. 600–602)', [
      ('Clearance', 'Cx = Ux × V ÷ Px — below GFR reabsorbed, above GFR secreted'),
      ('GFR', 'inulin clearance · creatinine slightly overestimates it'),
      ('Effective RPF', 'PAH clearance · slightly underestimates true RPF'),
      ('Blood flow', 'RBF = RPF ÷ (1 − Hct), 20–25% of cardiac output'),
      ('Filtration fraction', 'GFR ÷ RPF, normally about 20%'),
      ('Filtered load', 'GFR × Px · reabsorbed = filtered − excreted')]),
  ],
  dyn=dyn,
)
