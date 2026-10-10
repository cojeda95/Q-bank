# m46 — Acid–Base Compensation Timeline (dynamic map, kit data)
# WHEN each defense acts and HOW FAR compensation goes (abflow shows WHERE the ions move).
# Three lines of defense on one time axis — chemical buffers (seconds), the lungs (minutes; full by 6–12 h),
# the kidneys (hours to days; full by 3–5 days) — over a drawn blood buffer pool, lungs and kidney, and a
# time-course graph of pH, PaCO₂ and HCO₃⁻ redrawn for each simple disorder with a marker at the current step.
# A `steps` switch walks the time; a `one` switch picks the disorder. Example numbers follow the rules
# (Winters, Costanzo Table 7.3) and pH is computed from Henderson–Hasselbalch.
# Sources: First Aid 2025 pp. 351, 609–610 · Costanzo ch 7 · Guyton ch 31.
import sys, math
sys.path.insert(0, '/Users/Alonso/Developer/atlas-review/batches/m18')
from common import full

CZ7, GY31 = full('Costanzo', 7), full('Guyton', 31)

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
def box(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')

TAG = 'nf-l2 dyn-tag'
TIMES = ['sec', 'min', 'day', 'days']
DZS = ['ma', 'malk', 'ara', 'cra', 'aralk', 'cralk', 'mxra', 'mxsal']
MIX = ['mxra', 'mxsal']                       # mixed: two disorders at once
def W(dzs, times=TIMES):                      # disorder(s) at time step(s)
    return [f'dz:{d}&time:{t}' for d in dzs for t in times]
Z = lambda *k: ['dz:' + x for x in k]
LATE = ['min', 'day', 'days']                 # the lungs have responded
RENAL = ['day', 'days']                       # the kidneys have responded
MET, RESP = ['ma', 'malk'], ['ara', 'cra', 'aralk', 'cralk']
RACID, RALK = ['ara', 'cra'], ['aralk', 'cralk']
HYPER = W(['ma'], LATE) + Z(*RALK, 'mxsal')           # breathing more than normal
HYPO = W(['malk'], LATE) + Z(*RACID, 'mxra')        # breathing less
KUP = W(['ma', 'cra', 'mxra'], RENAL)                 # kidneys excrete more acid (acute = before they act)
KDOWN = W(['cralk'], RENAL)                   # kidneys excrete less acid, let HCO₃⁻ go

# ════════ 1. blood buffer pool ════════
box(160, 130, 860, 720)
text('Blood & cells — chemical buffers', 180, 166, 'dyn-big')
text('act within seconds — they tie H⁺ up but do not remove it', 180, 186, 'dyn-cap')
shapes.append(dict(vessel='M180 300 H840', w=70, color='--dk2'))
add('<ellipse cx="330" cy="300" rx="52" ry="24" style="fill:var(--surface);fill-opacity:.85;stroke:var(--dk2);stroke-width:2.5"/>')
text('red cell', 330, 304, 'nf-l2', 'middle')
text('plasma', 760, 254, 'dyn-cap', 'middle')
add('<text class="nf-l1" x="510" y="400" text-anchor="middle" style="font-size:24px">H⁺ + HCO₃⁻  ⇌  H₂CO₃  ⇌  CO₂ + H₂O</text>')
text('HCO₃⁻ / CO₂ — the main buffer of the ECF (pK 6.1)', 190, 450, 'nf-l1')
text('Hemoglobin — buffers H⁺ inside red cells, which equilibrate fast', 190, 474)
text('Proteins & phosphate — inside other cells: 60–70% of all', 190, 498)
text('chemical buffering, but it takes several hours to be full', 190, 516)
text('H⁺ added — HCO₃⁻ is used up buffering it', 190, 560, TAG, when=Z('ma'))
text('HCO₃⁻ added — base excess', 190, 560, TAG, when=Z('malk'))
text('CO₂ retained — buffered inside cells, mostly by Hb', 190, 560, TAG, when=Z(*RACID))
text('CO₂ blown off — H⁺ leaves the buffers inside cells', 190, 560, TAG, when=Z(*RALK))
text('H⁺ added and CO₂ retained — both push pH down', 190, 560, TAG, when=Z('mxra'))
text('salicylic acid uses up HCO₃⁻ while CO₂ is blown off', 190, 560, TAG, when=Z('mxsal'))
# K⁺ shift (FA p. 608; Costanzo ch 7): metabolic only — in respiratory disorders CO₂ crosses cell membranes itself
add('<ellipse cx="740" cy="520" rx="70" ry="38" class="dyn-cell"/>')
text('a body cell', 740, 524, 'nf-l2', 'middle')
KOUT, KIN = Z('ma', 'mxra'), Z('malk')
add('<path d="M800 500 H848" class="dyn-line" marker-end="url(#ah-tbBuf)" style="stroke:var(--nf-k);stroke-width:4"/>'
    '<path d="M848 540 H812" class="dyn-line" marker-end="url(#ah-tbBuf)" style="stroke:var(--nf-h);stroke-width:4"/>', when=KOUT)
add('<path d="M848 500 H812" class="dyn-line" marker-end="url(#ah-tbBuf)" style="stroke:var(--nf-k);stroke-width:4"/>'
    '<path d="M800 540 H848" class="dyn-line" marker-end="url(#ah-tbBuf)" style="stroke:var(--nf-h);stroke-width:4"/>', when=KIN)
text('K⁺ out, H⁺ in → serum K⁺ ↑', 740, 590, TAG, 'middle', when=KOUT)
text('K⁺ in, H⁺ out → serum K⁺ ↓', 740, 590, TAG, 'middle', when=KIN)
text('CO₂ crosses cells itself — little K⁺ shift', 740, 590, TAG, 'middle', when=Z(*RESP))

# ════════ 2. lungs ════════
box(900, 130, 1600, 720)
text('Lungs — minutes to hours', 920, 166, 'dyn-big')
text('change PaCO₂ by breathing more or less', 920, 186, 'dyn-cap')
add('<ellipse cx="1040" cy="290" rx="96" ry="48" class="dyn-cell"/>')
text('Medulla', 1040, 286, 'nf-l1', 'middle')
text('respiratory center', 1040, 304, 'nf-l2', 'middle')
add('<path d="M1136 290 Q1220 290 1262 330" class="dyn-dash"/>')
shapes.append(dict(tube='M1350 200 V380', w=36, color='--dk1'))
add('<path d="M1336 376 Q1230 360 1200 470 Q1180 590 1270 610 Q1330 618 1336 560 Z" class="dyn-cell"/>'
    '<path d="M1364 376 Q1470 360 1500 470 Q1520 590 1430 610 Q1370 618 1364 560 Z" class="dyn-cell"/>')
text('breathing ↑ — more CO₂ blown off', 920, 660, TAG, when=HYPER)
text('breathing ↓ — CO₂ retained', 920, 660, TAG, when=HYPO)
text('acidemia drives the carotid body', 920, 680, TAG, when=W(['ma'], LATE))
text('alkalemia slows breathing', 920, 680, TAG, when=W(['malk'], LATE))
text('the lungs are the cause — they cannot compensate', 920, 680, TAG, when=Z(*RESP))
text('lungs not yet responding', 920, 660, TAG, when=W(MET, ['sec']))
text('emphysema — the lungs cannot blow off the CO₂', 920, 680, TAG, when=Z('mxra'))
text('salicylates drive breathing directly (early)', 920, 680, TAG, when=Z('mxsal'))

# ════════ 3. kidney ════════
box(1640, 130, 2340, 720)
text('Kidneys — hours to days', 1660, 166, 'dyn-big')
text('excrete fixed acid and make new HCO₃⁻', 1660, 186, 'dyn-cap')
shapes.append(dict(vessel='M1660 250 H2320', w=34, color='--dk12'))
text('blood', 2310, 226, 'dyn-cap', 'end')
add('<rect x="1690" y="290" width="600" height="230" rx="30" class="dyn-cell"/>')
shapes.append(dict(membrane='M1720 290 H2260 Q2290 290 2290 320 V490 Q2290 520 2260 520 H1720 Q1690 520 1690 490 V320 Q1690 290 1720 290 Z', w=20))
text('Tubule cell', 1710, 330, 'dyn-big')
text('CO₂ + H₂O → H⁺ + HCO₃⁻', 2040, 420, 'nf-l2', 'middle')
shapes.append(dict(tube='M1660 580 H2320', w=70))
text('urine: NH₄⁺ and titratable acid (H₂PO₄⁻) carry the H⁺ out', 1680, 650, 'nf-l2')
text('kidneys working harder: more H⁺ out, new HCO₃⁻ back', 1680, 690, TAG, when=KUP)
text('kidneys let HCO₃⁻ go: less H⁺ secreted', 1680, 690, TAG, when=KDOWN)
text('kidneys not yet acting', 1680, 690, TAG, when=W(DZS, ['sec', 'min']))
text('acute = before the kidneys act — pick Chronic to see them', 1680, 690, TAG, when=W(['ara', 'aralk'], RENAL))
text('kidneys excrete the extra HCO₃⁻ — unless volume loss holds it', 1680, 690, TAG, when=W(['malk'], RENAL))

# ════════ 4. the three defenses on the time axis ════════
X0, CW = 420, 475                                 # time axis: left edge, column width
CX = [X0 + CW * i + CW // 2 for i in range(4)]    # column centres
X1 = X0 + 4 * CW
box(160, 760, 2340, 1050)
box(160, 1080, 2340, 2020)
text('When each defense acts', 180, 796, 'dyn-big')
COLS = ['Seconds', 'Minutes–hours', '1 day', '3–5 days']
for i, l in enumerate(COLS):
    text(l, CX[i], 796, 'nf-l1', 'middle')
add(''.join(f'<path d="M{X0 + CW * i} 812 V2000" class="dyn-line" style="stroke-dasharray:3 7;opacity:.5"/>' for i in range(1, 4)))
# current step: a band over the axis and the graph, an underline under its heading
for i, t in enumerate(TIMES):
    add(f'<rect x="{X0 + CW * i + 4}" y="812" width="{CW - 8}" height="1188" rx="14" style="fill:var(--accent);fill-opacity:.07;stroke:var(--accent);stroke-opacity:.35;stroke-width:2"/>'
        f'<path d="M{CX[i] - 70} 806 H{CX[i] + 70}" class="dyn-hl"/>', when=[f'time:{t}'])
ROWY = dict(buf=850, lung=920, kid=990)
def bar(y, x_start, x_full, col, when=None, unless=None, cls=''):
    h = 15
    add(f'<path d="M{x_start} {y} L{x_full} {y - h} H{X1} V{y + h} H{x_full} Z" class="{cls}" style="fill:var({col});fill-opacity:.3;stroke:var({col});stroke-width:2"/>',
        when, unless)
text('Chemical buffers', 180, ROWY['buf'] + 5, 'nf-l1')
bar(ROWY['buf'], X0, X0 + 40, '--dk2')
text('at once in the ECF and red cells; other cells over hours', X0 + 60, ROWY['buf'] + 5)
text('Lungs', 180, ROWY['lung'] + 5, 'nf-l1')
bar(ROWY['lung'], X0 + CW, X0 + CW + 300, '--dk1', unless=Z(*RESP))
bar(ROWY['lung'], X0 + CW, X0 + CW + 300, '--dk1', when=Z(*RESP), cls='dyn-dim')
text('start within minutes (3–12 min) · full by 6–12 h · undo only 50–75% of the pH change', X0 + 2 * CW + 10, ROWY['lung'] + 5, unless=Z(*RESP))
text('no respiratory compensation — breathing is the cause', X0 + 2 * CW + 10, ROWY['lung'] + 5, TAG, when=Z(*RESP))
text('Kidneys', 180, ROWY['kid'] + 5, 'nf-l1')
bar(ROWY['kid'], X0 + CW + 240, X0 + 3 * CW, '--dk3')
text('begin in hours · full by 3–5 days · the most powerful', X0 + 3 * CW + 10, ROWY['kid'] + 5)
# acute vs chronic windows for the respiratory disorders (Costanzo: acute = before renal compensation)
for keys, x0, x1, lab in [(['ara', 'aralk'], X0 + 8, X0 + 2 * CW - 8, 'ACUTE — before the kidneys act'),
                          (['cra', 'cralk'], X0 + 3 * CW + 8, X1 - 8, 'CHRONIC — kidneys done')]:
    add(f'<path d="M{x0} 1030 H{x1}" class="dyn-hl" style="stroke:var(--bad);opacity:.6"/>', when=Z(*keys))
    text(lab, (x0 + x1) // 2, 1022, TAG, 'middle', when=Z(*keys))

# ════════ 5. the time-course graph ════════
text('What the blood gas shows — example values', 180, 1116, 'dyn-big')
text('pH from Henderson–Hasselbalch: 6.1 + log HCO₃⁻ / (0.03 × PaCO₂)', 180, 1136, 'dyn-cap')
for k, c in dict(ma='classic causes: DKA, diarrhea', malk='classic cause: vomiting', ara='classic cause: opioid overdose',
                 cra='classic cause: COPD', aralk='classic cause: panic attack', cralk='classic cause: high altitude',
                 mxra='e.g., diarrhea + emphysema', mxsal='e.g., salicylate (aspirin) overdose').items():
    text(c, 180, 1158, TAG, when=Z(k))
PLOTS = dict(ph=('pH', 1180, 7.0, 7.7, (7.1, 7.2, 7.3, 7.4, 7.5, 7.6), 7.40, '{:.2f}'),
             pco2=('PaCO₂, mm Hg', 1460, 20, 70, (20, 30, 40, 50, 60, 70), 40, '{:.0f}'),
             hco3=('HCO₃⁻, mEq/L', 1740, 8, 40, (12, 18, 24, 30, 36), 24, '{:.0f}'))
PH_ = 220                                         # plot height
def py(k, v):
    _, top, lo, hi, *_ = PLOTS[k]
    return round(top + PH_ - (v - lo) / (hi - lo) * PH_)
for k, (lab, top, lo, hi, ticks, norm, fmt) in PLOTS.items():
    add(f'<path d="M{X0} {top} V{top + PH_} H{X1}" class="dyn-line"/>'
        + ''.join(f'<path d="M{X0 - 8} {py(k, v)} H{X0}" class="dyn-line"/>'
                  f'<text class="nf-l2" x="{X0 - 14}" y="{py(k, v) + 4}" text-anchor="end">{fmt.format(v)}</text>' for v in ticks))
    text(lab, 180, top + 20, 'nf-l1')
    text('normal ' + fmt.format(norm), 180, top + 40, 'nf-l2')
    add(f'<path d="M{X0} {py(k, norm)} H{X1}" class="dyn-dash"/>', when=['dz:*'])
    add(f'<path d="M{X0} {py(k, norm)} H{X1}" class="dyn-trace" style="stroke:var(--ok);stroke-width:4"/>', unless=['dz:*'])
    for i, t in enumerate(TIMES):
        add(f'<circle cx="{CX[i]}" cy="{py(k, norm)}" r="9" style="fill:var(--ok)"/>', when=[f'!dz:*&time:{t}'])
text('onset', X0, 1990, 'dyn-cap', 'middle')

# example values: Winters (FA p. 609), Costanzo Table 7.3; pH = 6.1 + log(HCO₃⁻ / 0.03 PaCO₂)
DATA = dict(ma=dict(hco3=[12, 12, 12, 12], pco2=[40, 30, 26, 26]),
            malk=dict(hco3=[36, 36, 36, 36], pco2=[40, 44, 47, 47]),
            ara=dict(pco2=[60] * 4, hco3=[26] * 4), cra=dict(pco2=[60] * 4, hco3=[26, 26, 28, 30]),
            aralk=dict(pco2=[25] * 4, hco3=[21] * 4), cralk=dict(pco2=[25] * 4, hco3=[21, 21, 19.5, 18]),
            mxra=dict(hco3=[12] * 4, pco2=[46] * 4),                  # PaCO₂ far above Winters 26 ± 2
            mxsal=dict(pco2=[30, 22, 20, 20], hco3=[22, 16, 14, 14]))  # early resp. alkalosis, then AG acidosis; PaCO₂ below Winters
for d in DATA.values():
    d['ph'] = [6.1 + math.log10(h / (0.03 * p)) for h, p in zip(d['hco3'], d['pco2'])]
NORM = dict(ph=7.40, pco2=40, hco3=24)
COL = dict(ph='--dk11', pco2='--dk8', hco3='--nf-hco3')
for dz, d in DATA.items():
    for k in ('ph', 'pco2', 'hco3'):
        v = d[k]
        pts = ' '.join(f'L{CX[i]} {py(k, v[i])}' for i in range(4))
        add(f'<path d="M{X0} {py(k, NORM[k])} V{py(k, v[0])} {pts} H{X1}" class="dyn-trace" style="stroke:var({COL[k]});stroke-width:4"/>'
            + ''.join(f'<circle cx="{CX[i]}" cy="{py(k, v[i])}" r="5" style="fill:var({COL[k]})"/>' for i in range(4)), when=Z(dz))
        fmt = PLOTS[k][6]
        for i, t in enumerate(TIMES):
            up = v[i] >= NORM[k]
            add(f'<circle cx="{CX[i]}" cy="{py(k, v[i])}" r="11" style="fill:var({COL[k]});stroke:var(--surface);stroke-width:3"/>', when=[f'dz:{dz}&time:{t}'])
            text(fmt.format(v[i]), CX[i] + 18, py(k, v[i]) + (-12 if up else 24), 'nf-l1', when=[f'dz:{dz}&time:{t}'])
# expected-compensation lines
def expect(k, v, lab, dzs, x0=X0 + 2 * CW, band=None, x1=X1):
    band = band or (v - 1, v + 1)   # the rules give a point; ±1 just makes it visible (Winters gives ± 2)
    add(f'<rect x="{x0}" y="{py(k, band[1])}" width="{x1 - x0}" height="{py(k, band[0]) - py(k, band[1])}" style="fill:var(--accent);fill-opacity:.16"/>'
        f'<path d="M{x0} {py(k, v)} H{x1}" class="dyn-dash" style="stroke:var(--accent)"/>', when=Z(*dzs))
    text(lab, x1 - 8, py(k, v) + 22 if k != 'hco3' or v < 24 else py(k, v) - 10, 'nf-l2', 'end', when=Z(*dzs))
expect('pco2', 26, 'Winters: 1.5 × 12 + 8 = 26 ± 2', ['ma'], band=(24, 28))
expect('pco2', 47, 'expected ≈ 40 + 0.6 × 12 = 47', ['malk'])
expect('hco3', 26, 'acute rule: 24 + 1 × 2 = 26', ['ara'], x0=X0, x1=X0 + 2 * CW)
expect('hco3', 26, 'acute: 26', ['cra'], x0=X0, x1=X0 + 2 * CW)
expect('hco3', 30, 'chronic rule: 24 + 3 × 2 = 30', ['cra'], x0=X0 + 3 * CW)
expect('hco3', 21, 'acute rule: 24 − 2 × 1.5 = 21', ['aralk'], x0=X0, x1=X0 + 2 * CW)
expect('hco3', 21, 'acute: 21', ['cralk'], x0=X0, x1=X0 + 2 * CW)
expect('hco3', 18, 'chronic rule: 24 − 4 × 1.5 = 18', ['cralk'], x0=X0 + 3 * CW)
expect('pco2', 26, 'Winters for HCO₃⁻ 12: 26 ± 2 — measured 46', ['mxra'], band=(24, 28))
expect('pco2', 29, 'Winters for HCO₃⁻ 14: 29 ± 2 — measured 20', ['mxsal'], band=(27, 31))
text('pick a disorder to see its traces', CX[1], py('ph', 7.4) - 16, 'dyn-cap', 'middle', unless=['dz:*'])

# ════════ 6. motion ════════
def m(when, **kw): return dict(when=when, **kw)
def flow(d, ln, base, mods=(), speed=110, r=6, when=None):
    f = dict(d=d, len=ln, speed=speed, r=r, base=base, mods=list(mods))
    if when: f['when'] = when
    return f
flows = [
  # blood: H⁺ meets HCO₃⁻
  flow('M190 288 H830', 640, dict(hco3=6), [m(Z('ma', 'mxra', 'mxsal'), set=dict(hco3=3)), m(Z('malk'), set=dict(hco3=10)),
                                            m(W(['cra'], RENAL), set=dict(hco3=9)), m(W(['cralk'], RENAL), set=dict(hco3=4))]),
  flow('M830 314 H190', 640, dict(h=2, co2=2), [m(Z('ma'), set=dict(h=6, co2=2)), m(Z('mxra'), set=dict(h=6, co2=5)), m(Z('mxsal'), set=dict(h=4, co2=1)), m(Z('malk'), set=dict(h=1, co2=2)),
                                                m(Z(*RACID), set=dict(h=4, co2=6)), m(Z(*RALK), set=dict(h=1, co2=1))]),
  # drive to breathe and CO₂ out of the lungs
  flow('M1136 290 Q1220 290 1262 330', 140, dict(sig=2), [m(HYPER, set=dict(sig=5)), m(HYPO, set=dict(sig=1))], speed=110),
  flow('M1270 560 Q1300 470 1340 400 V200', 390, dict(co2=3), [m(HYPER, set=dict(co2=7), speed=1.5), m(HYPO, set=dict(co2=1), speed=.6)], speed=130),
  flow('M1430 560 Q1400 470 1360 400 V200', 390, dict(co2=3), [m(HYPER, set=dict(co2=7), speed=1.5), m(HYPO, set=dict(co2=1), speed=.6)], speed=130),
  # kidney: urine carries NH₄⁺ and titratable acid; new HCO₃⁻ to the blood
  flow('M1670 580 H2310', 640, dict(nh4=3), [m(KUP, set=dict(nh4=7)), m(KDOWN, set=dict(nh4=1))]),
  flow('M1670 250 H2310', 640, dict(hco3=3), [m(KUP, set=dict(hco3=6)), m(KDOWN, set=dict(hco3=1))]),
]

# ════════ 7. sites ════════
sites = [
  dict(x=382, y=300, n=[1, 0], w=8, t='ex', l='Hemoglobin buffer', s='H⁺ + Hb ⇌ HHb', ions=[], c='intrabuffer',
       lx=300, ly=360, la='start', boost=Z(*RESP)),
  dict(x=640, y=300, n=[0, 1], w=8, t='ex', l='Carbonic anhydrase', s='CO₂ + H₂O ⇌ H₂CO₃', ions=[], c='co2trans',
       lx=600, ly=360, la='start'),
  dict(x=1100, y=330, n=[0, 1], w=12, t='rec', l='Chemoreceptors', s='sense PaCO₂ and pH', ions=[], c='chemorec',
       lx=950, ly=380, la='start', boost=W(['ma'], LATE), low=W(['malk'], LATE),
       sfx=dict(boost=' — firing', low=' — quiet')),
  dict(x=1500, y=470, n=[1, 0], w=14, t='rec', l='Alveolar ventilation', s='sets PaCO₂', ions=[], c='alvvent',
       lx=1440, ly=540, la='end', boost=HYPER, low=HYPO, sfx=dict(boost=' ↑', low=' ↓')),
  dict(x=1820, y=520, n=[0, -1], w=20, t='pump', l='H⁺ secretion', s='H⁺ → urine', reach=50,
       ions=[['h', 'in', 2]], cross=True, c='newhco3', boost=KUP, low=KDOWN, lx=1820, ly=470, la='middle'),
  dict(x=2160, y=520, n=[0, -1], w=20, t='ex', l='Na⁺–H⁺ exchanger', s='reclaims filtered HCO₃⁻', reach=50,
       ions=[['h', 'in', 1], ['na', 'out', 1]], cross=True, c='hco3reabs', boost=KUP, low=KDOWN, lx=2160, ly=470, la='middle'),
  dict(x=1990, y=290, n=[0, 1], w=20, t='co', l='HCO₃⁻ exit', s='new HCO₃⁻ → blood', reach=44,
       ions=[['hco3', 'in', 2]], cross=True, c='newhco3', boost=KUP, low=KDOWN, lx=1990, ly=372, la='middle'),
]

# ════════ 8. readouts ════════
def ro(label, table):
    """table: {(dz, time-list): d}"""
    mods = []
    for (dzs, times), d in table.items():
        mods.append(dict(when=W(dzs, times), d=d))
    return dict(l=label, mods=mods)
A = tuple
readouts = [
  ro('pH', {(A(['ma', 'mxra'] + RACID), A(TIMES)): -1, (A(['malk'] + RALK), A(TIMES)): 1}),
  ro('PaCO₂', {(A(MET), ('sec',)): 0, (('ma',), A(LATE)): -1, (('malk',), A(LATE)): 1,
              (A(RACID + ['mxra']), A(TIMES)): 1, (A(RALK + ['mxsal']), A(TIMES)): -1}),
  ro('HCO₃⁻', {(('ma', 'mxra', 'mxsal'), A(TIMES)): -1, (('malk',), A(TIMES)): 1, (A(RACID), A(TIMES)): 1, (A(RALK), A(TIMES)): -1}),
  ro('Urine NH₄⁺ + titratable acid', {(A(DZS), ('sec',)): 0, (A(RESP), ('min',)): 0,
                                      (('ma', 'cra', 'mxra'), A(RENAL)): 1, (('cralk',), A(RENAL)): -1,
                                      (('ara', 'aralk'), A(RENAL)): 0}),
  ro('Serum K⁺ (shift)', {(('ma', 'mxra'), A(TIMES)): 1, (('malk',), A(TIMES)): -1}),
]

# ════════ 9. notes ════════
notes = {
  '!dz:*&time:sec': 'Seconds: the chemical buffers act at once — HCO₃⁻/CO₂ in the ECF and hemoglobin in red cells; proteins and '
                    'phosphate inside other cells take hours to share the load. Buffers only tie H⁺ up; they do not remove it. Pick a disorder.',
  '!dz:*&time:min': 'Minutes to hours: the respiratory center changes ventilation within minutes and the response is full by 6–12 h. '
                    'The lungs move PaCO₂ — they can remove CO₂ (volatile acid) but not fixed acid.',
  '!dz:*&time:day': '1 day: the kidneys have started — they act over hours to days, secreting H⁺, reclaiming filtered HCO₃⁻ and '
                    'making new HCO₃⁻ as NH₄⁺ and titratable acid leave in the urine.',
  '!dz:*&time:days': '3–5 days: renal compensation is complete. The kidneys are the slowest defense but the most powerful, and the only '
                     'one that rids the body of fixed acid.',
  # the disorders — each with its rule
  'dz:ma': 'Metabolic acidosis (e.g., DKA, diarrhea): HCO₃⁻ falls first. Acidemia drives the carotid bodies — hyperventilation '
           '(Kussmaul breathing in DKA) lowers PaCO₂. H⁺ entering cells without an organic anion trades for K⁺ (serum K⁺ ↑), though diarrhea also loses K⁺ in stool; in DKA it is mainly low insulin. Winters: expected PaCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 = 26 here. Higher means a '
           'respiratory acidosis too; lower, a respiratory alkalosis.',
  'dz:malk': 'Metabolic alkalosis (e.g., vomiting): HCO₃⁻ rises first. Alkalemia slows breathing, so PaCO₂ rises ≈ 0.6 mm Hg per '
             '1 mEq/L of HCO₃⁻ — ≈ 47 here. The falling PO₂ limits how far it goes. A PaCO₂ off this mark means a second disorder.',
  'dz:ara': 'Acute respiratory acidosis (e.g., opioid overdose): PaCO₂ rises at once. Before the kidneys act, buffering raises HCO₃⁻ '
            'only 1 mEq/L per 10 mm Hg of PaCO₂ — 60 mm Hg gives ≈ 26 — so pH falls a lot. A HCO₃⁻ off this mark means a second disorder.',
  'dz:cra': 'Chronic respiratory acidosis (e.g., COPD): over 3–5 days the kidneys excrete more H⁺ as NH₄⁺ and titratable acid and '
            'add new HCO₃⁻ — HCO₃⁻ rises 3 mEq/L per 10 mm Hg, ≈ 30 here — so pH comes back toward 7.40, but not all the way.',
  'dz:aralk': 'Acute respiratory alkalosis (e.g., panic attack): PaCO₂ falls at once. Buffering lowers HCO₃⁻ only 2 mEq/L per '
              '10 mm Hg — 25 mm Hg gives ≈ 21 — so pH rises a lot. A HCO₃⁻ off this mark means a second disorder.',
  'dz:cralk': 'Chronic respiratory alkalosis (e.g., high altitude): over 3–5 days the kidneys secrete less H⁺ and let filtered HCO₃⁻ '
              'go — HCO₃⁻ falls 4 mEq/L per 10 mm Hg, ≈ 18 here — so pH comes back toward 7.40, but not all the way.',
  'dz:mxra': 'Mixed: metabolic + respiratory acidosis (e.g., diarrhea in a patient with emphysema). HCO₃⁻ is 12, so Winters expects '
             'PaCO₂ 26 ± 2 — but the lungs cannot blow off CO₂ and it sits at 46. A PaCO₂ above the expected range = a respiratory '
             'acidosis on top, so pH falls far more than either alone.',
  'dz:mxsal': 'Mixed: respiratory alkalosis + anion gap metabolic acidosis — salicylate overdose. Salicylates drive breathing early '
              '(PaCO₂ falls first); later salicylic acid uses up HCO₃⁻. Once HCO₃⁻ is 14, Winters expects PaCO₂ 29 ± 2 — a measured '
              '20 is below it: a respiratory alkalosis too. The two pull pH opposite ways, so pH can be near normal.',
  # what the current step adds
  'dz:ma&time:sec': 'Seconds: only buffering so far — HCO₃⁻ is down, PaCO₂ is still 40, so pH is at its lowest.',
  'dz:malk&time:sec': 'Seconds: only buffering so far — HCO₃⁻ is up, PaCO₂ is still 40, so pH is at its highest.',
  'dz:ma&time:min': 'Minutes–hours: the lungs respond within minutes and are fully compensating by 6–12 h — PaCO₂ falls with HCO₃⁻.',
  'dz:malk&time:min': 'Minutes–hours: breathing slows within minutes — PaCO₂ rises with HCO₃⁻.',
  'dz:ma&time:day': '1 day: respiratory compensation is complete — check PaCO₂ against Winters. pH is nearer 7.40 but still low.',
  'dz:malk&time:day': '1 day: respiratory compensation is complete — pH is nearer 7.40 but still high.',
  'dz:ma&time:days': '3–5 days: PaCO₂ stays compensated. The real fix — excreting the extra acid as NH₄⁺ and titratable acid — '
                     'is the kidneys’ job and takes several days.',
  'dz:malk&time:days': '3–5 days: PaCO₂ stays compensated. Healthy kidneys excrete the extra HCO₃⁻; volume loss and aldosterone '
                       '(vomiting, diuretics) make them hold it instead.',
}
for keys, kind in ((RACID, 'acid'), (RALK, 'alk')):
    k = '|'.join(keys)
    dn = 'rises' if kind == 'acid' else 'falls'
    for t, s in [('sec', f'Seconds: PaCO₂ has moved; the cause is the breathing, so the lungs cannot compensate. Only buffers inside cells '
                         f'(mostly hemoglobin) act — HCO₃⁻ {dn} just a little.'),
                 ('min', 'Minutes–hours: still acute — the kidneys have barely begun, so pH is at its most abnormal.'),
                 ('day', f'1 day: the kidneys are partway — HCO₃⁻ {dn} further and pH starts back toward 7.40.'),
                 ('days', f'3–5 days: chronic — renal compensation is complete; HCO₃⁻ has moved {"3" if kind == "acid" else "2"}× as much as acutely.')]:
        for dz in keys:
            notes[f'dz:{dz}&time:{t}'] = s
    for t in RENAL:   # the acute option stays on the acute rule: it is defined as before renal compensation
        notes[f'dz:{keys[0]}&time:{t}'] = (f'{"1 day" if t == "day" else "3–5 days"}: acute means before the kidneys act — HCO₃⁻ stays on '
                                          f'the acute rule and pH stays far from 7.40. If PaCO₂ stays off, the kidneys respond and it '
                                          f'becomes chronic — pick Chronic.')

dyn = dict(
  kinds=dict(co2=['co2', '--dk8'], h=['h', '--nf-h'], hco3=['hco3', '--nf-hco3'], na=['h', '--nf-na'],
             nh4=['urine', '--dk4'], sig=['sig', '--dk11']),
  groups=[['co2', 'CO₂'], ['h', 'H⁺ · Na⁺'], ['hco3', 'HCO₃⁻'], ['urine', 'NH₄⁺ & titratable acid'], ['sig', 'Drive to breathe']],
  switches=[dict(id='time', label='Time since onset', type='steps', auto=4,
                 options=[['sec', 'Seconds'], ['min', 'Minutes–hours'], ['day', 'One day'], ['days', 'Three to five days']]),
            dict(id='dz', label='Pick one disorder', type='one',
                 options=[['ma', 'Metabolic acidosis', 'agma'], ['malk', 'Metabolic alkalosis', 'metalk'],
                          ['ara', 'Acute respiratory acidosis', 'respacid'], ['cra', 'Chronic respiratory acidosis', 'respacid'],
                          ['aralk', 'Acute respiratory alkalosis', 'respalk'], ['cralk', 'Chronic respiratory alkalosis', 'respalk'],
                          ['mxra', 'Mixed: metabolic + respiratory acidosis', 'abcompensation'],
                          ['mxsal', 'Mixed: salicylate overdose', 'aspirin']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 351, 608–610 · Costanzo ch 7 (Table 7.3) · Guyton ch 31')

MAP = dict(
  id='abtime', title='Acid–Base Compensation Timeline', topic='renal', after='abflow',
  sub='When each defense acts and how far it gets: buffers in seconds, the lungs in minutes to hours, the kidneys over 3–5 days. '
      'Pick a disorder and step through time to watch pH, PaCO₂ and HCO₃⁻ move toward — never back to — normal, against the '
      'expected-compensation rules. Tap a buffer, receptor or transporter for its card',
  w=3500, h=2100,
  fa='351, 608–610', src=[CZ7, GY31],
  lanes=[('tbBuf', 'Chemical buffers', 'sugars'), ('tbLung', 'Lungs', 'glycolysis'), ('tbKid', 'Kidneys', 'gluconeo'),
         ('tbDz', 'Disorders & rules', 'tca')],
  nodes=[
    ('tb1', 'Buffers', 360, 640, 'tbBuf', 'HCO₃⁻ · Hb · proteins', ['hhbuffer', 'buffpk', 'intrabuffer', 'co2trans']),
    ('tb7', 'K⁺ shifts', 700, 660, 'tbBuf', 'H⁺/K⁺ exchange', ['kacid', 'hyperk', 'hypok']),
    ('tb8', 'Classic causes', 1720, 1116, 'tbDz', 'FA p. 610', ['opioids', 'panic', 'acclim', 'pyloric', 'diarrheaapproach', 'aspirin']),
    ('tb2', 'Control of breathing', 1460, 250, 'tbLung', 'PaCO₂ follows ventilation', ['chemorec', 'ventresp', 'alvvent']),
    ('tb3', 'Renal H⁺ excretion', 2200, 350, 'tbKid', 'new HCO₃⁻', ['newhco3', 'hco3reabs', 'acidprod']),
    ('tb4', 'Compensation rules', 2180, 1116, 'tbDz', 'acid–base map', ['abcompensation', 'hhcalc']),
    ('tb5', 'Metabolic disorders', 1300, 1116, 'tbDz', 'HCO₃⁻ moves first', ['agma', 'nagma', 'metalk', 'dka']),
    ('tb6', 'Respiratory disorders', 900, 1116, 'tbDz', 'PaCO₂ moves first', ['respacid', 'respalk', 'copd', 'altitude'])],
  panels=[
    (2420, 700, 1000, 'Expected compensation (First Aid p. 609; Costanzo Table 7.3)', [
      ('Metabolic acidosis', 'Winters: PaCO₂ = 1.5 × HCO₃⁻ + 8 ± 2'),
      ('Metabolic alkalosis', 'PaCO₂ ↑ ≈ 0.6 mm Hg per 1 mEq/L HCO₃⁻ ↑'),
      ('Respiratory acidosis', 'HCO₃⁻ ↑ 1 per 10 mm Hg PaCO₂ acutely · 3 chronically'),
      ('Respiratory alkalosis', 'HCO₃⁻ ↓ 2 per 10 mm Hg PaCO₂ acutely · 4 chronically'),
      ('Off the rule', 'a second disorder: PaCO₂ above Winters = + resp. acidosis · below = + resp. alkalosis'),
      ('pH', 'moves toward 7.40 · the lungs undo only 50–75% of a metabolic change')]),
    (2420, 960, 1000, 'Timing (Guyton ch 31; Costanzo ch 7)', [
      ('Buffers', 'seconds — ECF and red cells at once; other cells over hours'),
      ('Lungs', 'within minutes · full by 6–12 h · 50–75% effective'),
      ('Kidneys', 'hours to days · full by 3–5 days · most powerful'),
      ('Acute vs chronic', 'respiratory disorders: before vs after renal compensation')])],
  dyn=dyn)
