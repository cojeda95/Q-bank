# Diagnostic Test Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Two overlapping value distributions (healthy and diseased) with a movable cutoff, the ROC curve with the
# cutoff marked, a 2 × 2 table for 1000 people, and bars for sensitivity, specificity, PPV and NPV. Two `steps`
# switches: the cutoff (low / middle / high) and the prevalence (1% / 10% / 50%). Every number is computed
# here from the formulas on the pinned cards (sensspec, ppvnpv, cutoff, likelihood); the distributions are
# illustrative (healthy N(40, 8), diseased N(60, 8)) — the caption says so. Readout arrows compare each state
# with the middle cutoff at 10% prevalence.
# No new cards. Sources: First Aid 2025 pp. 259–262 (as the pinned cards cite).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

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
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
MH, MD, SD = 40, 60, 8
CUTS = dict(lo=44, mid=50, hi=56)
PREVS = dict(lo=0.01, mid=0.10, hi=0.50)
N = 1000
def stats(c, p):
    sens = 1 - Phi((CUTS[c] - MD) / SD); spec = Phi((CUTS[c] - MH) / SD)
    dz = round(N * PREVS[p]); ok = N - dz
    tp = round(dz * sens); fn = dz - tp; tn = round(ok * spec); fp = ok - tn
    ppv = tp / (tp + fp) if tp + fp else 0; npv = tn / (tn + fn) if tn + fn else 0
    return dict(sens=sens, spec=spec, tp=tp, fp=fp, fn=fn, tn=tn, ppv=ppv, npv=npv, lrp=sens / (1 - spec), dz=dz, ok=ok)
S = {(c, p): stats(c, p) for c in CUTS for p in PREVS}
W = lambda c, p: [f'cut:{c}&prev:{p}']
C = lambda *k: ['cut:' + x for x in k]
P = lambda *k: ['prev:' + x for x in k]
pct = lambda v: f'{v * 100:.0f}%' if v * 100 >= 9.5 or v == 0 else f'{v * 100:.1f}%'

# ════════ 1. the two distributions ════════
box(160, 130, 1400, 760)
text('The test values — healthy vs diseased', 180, 166, 'dyn-big')
text('illustrative curves; each group drawn to its own height — sensitivity and specificity don’t depend on prevalence', 180, 186, 'dyn-cap')
VX0, VX1, VY = 220, 1340, 640                       # value axis 20 → 80
vx = lambda v: round(VX0 + (v - 20) / 60 * (VX1 - VX0))
pdf = lambda v, m: math.exp(-((v - m) / SD) ** 2 / 2)
HT = 330
def curve(m, lo=20, hi=80, close=False):
    pts = [f'{vx(v / 4)} {round(VY - HT * pdf(v / 4, m), 1)}' for v in range(int(lo * 4), int(hi * 4) + 1)]
    d = 'M' + ' L'.join(pts)
    return d + (f' L{vx(hi)} {VY} L{vx(lo)} {VY} Z' if close else '')
add(f'<path d="M{VX0} {VY} H{VX1}" class="dyn-line"/>' + ''.join(
    f'<path d="M{vx(v)} {VY} V{VY + 8}" class="dyn-line"/><text class="nf-l2" x="{vx(v)}" y="{VY + 26}" text-anchor="middle">{v}</text>' for v in range(20, 81, 10)))
text('test value', VX1, VY + 50, 'dyn-cap', 'end')
for c, cut in CUTS.items():
    add(f'<path d="{curve(MH, cut, 80, True)}" style="fill:var(--bad);fill-opacity:.28;stroke:none"/>'
        f'<path d="{curve(MD, 20, cut, True)}" style="fill:var(--dk8);fill-opacity:.35;stroke:none"/>', when=C(c))
add(f'<path d="{curve(MH)}" class="dyn-trace" style="stroke:var(--dk1);stroke-width:4;fill:none"/>'
    f'<path d="{curve(MD)}" class="dyn-trace" style="stroke:var(--dk3);stroke-width:4;fill:none"/>')
text('healthy', vx(MH), VY - HT - 14, 'nf-l1', 'middle')
text('diseased', vx(MD), VY - HT - 14, 'nf-l1', 'middle')
for c, cut in CUTS.items():
    add(f'<path d="M{vx(cut)} {VY - HT - 40} V{VY + 4}" style="stroke:var(--ink);stroke-width:3;stroke-dasharray:8 6"/>', when=C(c))
    text(f'cutoff {cut} — positive above', vx(cut) + 10, VY - HT - 40, 'nf-l1', when=C(c))
text('false positives', vx(CUTS['hi']) + 70, VY - 40, TAG, when=C('lo', 'mid', 'hi'))
for c, cut in CUTS.items():
    text('false negatives ←', vx(cut) - 14, VY - 14, TAG, 'end', when=C(c))

# ════════ 2. the ROC curve ════════
box(1440, 130, 2340, 760)
text('ROC curve', 1460, 166, 'dyn-big')
text('sensitivity against 1 − specificity for every cutoff', 1460, 186, 'dyn-cap')
RX0, RY0, RS = 1560, 680, 420                       # origin and side length
add(f'<path d="M{RX0} {RY0 - RS} V{RY0} H{RX0 + RS}" class="dyn-line"/>'
    f'<path d="M{RX0} {RY0} L{RX0 + RS} {RY0 - RS}" class="dyn-dash"/>'
    f'<text class="nf-l2" x="{RX0 + RS // 2}" y="{RY0 + 34}" text-anchor="middle">1 − specificity (false-positive rate)</text>'
    f'<text class="nf-l2" x="{RX0 - 20}" y="{RY0 - RS - 14}">sensitivity</text>'
    f'<text class="dyn-cap" x="{RX0 + RS - 10}" y="{RY0 - RS // 2 + 60}" text-anchor="end">AUC 0.5 — a coin flip</text>')
roc = []
for v in range(10, 91):
    se, sp = 1 - Phi((v - MD) / SD), Phi((v - MH) / SD)
    roc.append(f'{round(RX0 + (1 - sp) * RS, 1)} {round(RY0 - se * RS, 1)}')
add(f'<path d="M{" L".join(roc)}" class="dyn-trace" style="stroke:var(--dk11);stroke-width:4;fill:none"/>')
for c in CUTS:
    s = S[(c, 'mid')]
    x, y = round(RX0 + (1 - s['spec']) * RS), round(RY0 - s['sens'] * RS)
    add(f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--surface);stroke:var(--dk11);stroke-width:3"/>')
    add(f'<circle cx="{x}" cy="{y}" r="13" style="fill:var(--accent);stroke:var(--surface);stroke-width:3"/>', when=C(c))
    text(f'cutoff {CUTS[c]}', x + 22, y + 30, 'nf-l1', when=C(c))
text('the better test bows toward the upper left — a bigger area under the curve', 1460, 730, 'nf-l2')

# ════════ 3. the 2 × 2 table ════════
box(160, 800, 1400, 1400)
text('1000 people tested', 180, 836, 'dyn-big')
TX, TY, CW, RH = 460, 900, 300, 110
add(f'<rect x="{TX}" y="{TY}" width="{2 * CW}" height="{2 * RH}" rx="10" class="dyn-soft"/>'
    f'<path d="M{TX + CW} {TY} V{TY + 2 * RH} M{TX} {TY + RH} H{TX + 2 * CW}" class="dyn-line"/>')
text('disease +', TX + CW // 2, TY - 14, 'nf-l1', 'middle'); text('disease −', TX + CW + CW // 2, TY - 14, 'nf-l1', 'middle')
text('test +', TX - 20, TY + RH // 2 + 6, 'nf-l1', 'end'); text('test −', TX - 20, TY + RH + RH // 2 + 6, 'nf-l1', 'end')
for (c, p), s in S.items():
    w = W(c, p)
    for (lab, k, cx, cy) in [('TP', 'tp', 0, 0), ('FP', 'fp', 1, 0), ('FN', 'fn', 0, 1), ('TN', 'tn', 1, 1)]:
        x, y = TX + cx * CW + CW // 2, TY + cy * RH + RH // 2
        text(f'{lab} {s[k]}', x, y + 8, 'dyn-big', 'middle', when=w)
    text(f'{s["dz"]} with the disease · {s["ok"]} without', TX, TY + 2 * RH + 40, 'nf-l2', when=w)
    text(f'{s["tp"] + s["fp"]} test positive — {s["tp"]} of them truly ill', TX, TY + 2 * RH + 64, TAG, when=w)
text('prevalence = (TP + FN) ÷ everyone tested', 180, 1370, 'dyn-cap')

# ════════ 4. the four numbers ════════
box(1440, 800, 2340, 1400)
text('What the result means', 1460, 836, 'dyn-big')
BX0, BW, BY = 1700, 520, 900
ROWS = [('Sensitivity', 'sens', 'TP ÷ (TP + FN)'), ('Specificity', 'spec', 'TN ÷ (TN + FP)'),
        ('PPV', 'ppv', 'TP ÷ (TP + FP)'), ('NPV', 'npv', 'TN ÷ (TN + FN)')]
for i, (lab, k, f) in enumerate(ROWS):
    y = BY + i * 110
    text(lab, 1460, y + 4, 'nf-l1'); text(f, 1460, y + 24, 'nf-l2')
    add(f'<rect x="{BX0}" y="{y - 18}" width="{BW}" height="30" rx="8" class="dyn-soft"/>')
    for (c, p), s in S.items():
        add(f'<rect x="{BX0}" y="{y - 18}" width="{round(BW * s[k])}" height="30" rx="8" style="fill:var(--accent);fill-opacity:.75"/>', when=W(c, p))
        text(pct(s[k]), BX0 + BW + 14, y + 4, 'nf-l1', when=W(c, p))
for (c, p), s in S.items():
    text(f'LR+ = sensitivity ÷ (1 − specificity) = {s["lrp"]:.1f}', 1460, 1350, 'nf-l2', when=W(c, p))

# ════════ 5. the rules ════════
box(160, 1440, 2340, 1700)
text('The rules', 180, 1476, 'dyn-big')
text('SN-N-OUT: a highly sensitive test, when negative, rules the disease out — screen with it', 180, 1510, 'nf-l2')
text('SP-P-IN: a highly specific test, when positive, rules it in — confirm with it', 180, 1534, 'nf-l2')
text('lower cutoff → sensitivity and NPV up, specificity and PPV down', 180, 1580, TAG, when=C('lo'))
text('higher cutoff → specificity and PPV up, sensitivity and NPV down', 180, 1580, TAG, when=C('hi'))
text('low prevalence → most positives are false: PPV falls, NPV rises', 180, 1610, TAG, when=P('lo'))
text('high prevalence → PPV rises, NPV falls — the test itself has not changed', 180, 1610, TAG, when=P('hi'))

# ════════ 6. tap targets ════════
sites = [
  dict(x=vx(MH) - 110, y=VY - HT + 10, n=[0, -1], w=8, t='ex', l='', aria='Healthy curve — specificity', ions=[], c='sensspec'),
  dict(x=vx(MD) + 120, y=VY - HT + 10, n=[0, -1], w=8, t='ex', l='', aria='Diseased curve — sensitivity', ions=[], c='sensspec'),
  dict(x=RX0 + 30, y=RY0 - RS + 30, n=[0, -1], w=8, t='ex', l='', aria='ROC curve', ions=[], c='cutoff'),
  dict(x=TX + 2 * CW + 30, y=TY + 20, n=[0, -1], w=8, t='ex', l='', aria='Predictive values', ions=[], c='ppvnpv'),
]

# ════════ 7. readouts — compared with the middle cutoff at 10% prevalence ════════
BASE = S[('mid', 'mid')]
def ro(lab, k):
    mods = []
    for (c, p), s in S.items():
        diff = s[k] - BASE[k]
        mods.append(dict(when=W(c, p), d=0 if abs(diff) < 0.005 else (1 if diff > 0 else -1)))
    return dict(l=lab, mods=mods)
readouts = [ro('Sensitivity', 'sens'), ro('Specificity', 'spec'), ro('PPV', 'ppv'), ro('NPV', 'npv'), ro('LR+', 'lrp')]

# ════════ 8. notes ════════
notes = {
  'cut:lo': 'Low cutoff: more people are called positive — fewer false negatives, so sensitivity and NPV rise, but more false '
            'positives, so specificity and PPV fall. A sensitive test is the one to screen with (SN-N-OUT).',
  'cut:mid': 'Middle cutoff: the healthy and diseased curves overlap, so any cutoff misclassifies someone — moving it only trades '
             'false positives for false negatives.',
  'cut:hi': 'High cutoff: fewer false positives, so specificity and PPV rise, but more false negatives — sensitivity and NPV fall. '
            'A specific test is the one to confirm with (SP-P-IN).',
  'prev:lo': '1% prevalence: even a good test yields mostly false positives — PPV is low, NPV is near 100%. Sensitivity and '
             'specificity have not changed.',
  'prev:mid': '10% prevalence — the reference state for the arrows.',
  'prev:hi': '50% prevalence (a high-risk group): PPV rises and NPV falls with the same test. Predictive values follow prevalence; '
             'sensitivity and specificity do not.',
}

dyn = dict(
  kinds={}, groups=[],
  switches=[dict(id='cut', label='Cutoff', type='steps', def_='mid', options=[['lo', 'Low cutoff (44)'], ['mid', 'Middle cutoff (50)'], ['hi', 'High cutoff (56)']]),
            dict(id='prev', label='Prevalence', type='steps', options=[['lo', '1% — a screening population'], ['mid', '10%'], ['hi', '50% — a high-risk clinic']])],
  notes=notes, shapes=shapes, flows=[], sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 259–262 · illustrative distributions')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')
dyn['switches'][1]['def'] = 'mid'

MAP = dict(
  id='testsim', title='Diagnostic Test Simulator', topic='stats', after='biostats',
  sub='Move the cutoff and the prevalence and watch the false positives and negatives, the ROC point, a 2 × 2 table of 1000 people '
      'and sensitivity, specificity, PPV and NPV change — sensitivity and specificity follow the cutoff; predictive values follow '
      'prevalence too. Tap a curve for its card',
  w=3500, h=2100,
  fa='259–262', src=[],
  lanes=[('tsTest', 'The test', 'glycolysis'), ('tsUse', 'Using the result', 'tca'), ('tsBias', 'Screening pitfalls', 'gluconeo')],
  nodes=[
    ('ts1', 'Sensitivity & specificity', 380, 1800, 'tsTest', 'SN-N-OUT · SP-P-IN', ['sensspec']),
    ('ts2', 'Cutoffs & ROC', 820, 1800, 'tsTest', 'trade one error for the other', ['cutoff']),
    ('ts3', 'Predictive values', 1260, 1800, 'tsUse', 'follow prevalence', ['ppvnpv', 'incprev']),
    ('ts4', 'Likelihood ratios', 1700, 1800, 'tsUse', 'pretest odds × LR', ['likelihood']),
    ('ts5', 'Screening biases', 2140, 1800, 'tsBias', 'lead time · length time', ['screenbias', 'selectionbias']),
    ('ts6', 'Errors & power', 380, 1940, 'tsBias', 'type I · type II', ['typeerrors', 'ci']),
    ('ts7', 'Precision vs accuracy', 820, 1940, 'tsBias', 'random vs systematic error', ['precacc'])],
  panels=[
    (2420, 760, 1000, 'Formulas (First Aid pp. 259–260)', [
      ('Sensitivity', 'TP ÷ (TP + FN) — 1 − false-negative rate'),
      ('Specificity', 'TN ÷ (TN + FP) — 1 − false-positive rate'),
      ('PPV · NPV', 'TP ÷ (TP + FP) · TN ÷ (TN + FN)'),
      ('LR+ · LR−', 'sens ÷ (1 − spec) · (1 − sens) ÷ spec'),
      ('Posttest odds', 'pretest odds × LR')]),
    (2420, 1000, 1000, 'What moves what (First Aid p. 260)', [
      ('Lower the cutoff', 'sensitivity ↑ · NPV ↑ · specificity ↓ · PPV ↓'),
      ('Raise the cutoff', 'specificity ↑ · PPV ↑ · sensitivity ↓ · NPV ↓'),
      ('Prevalence ↑', 'PPV ↑ · NPV ↓ · sensitivity and specificity unchanged'),
      ('Disease of LOW values', 'e.g., anemia — the cutoff directions flip')])],
  dyn=dyn)
