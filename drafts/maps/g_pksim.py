# Pharmacokinetics & Pharmacodynamics Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Top: plasma level over time with a dose every half-life (first-order, bolus model), a therapeutic window and the
# 4–5 half-lives to steady state; a `one` switch adds a loading dose, doubles the dose, adds a CYP inducer or
# inhibitor (half-life halved / doubled in the model), or shows zero- vs first-order elimination of one dose.
# Bottom: the agonist's log dose–response curve; a second `one` switch adds a competitive or noncompetitive
# antagonist, shows a partial agonist, or a more potent agonist. Curves are computed here; units are illustrative
# (time in baseline half-lives, level relative to the target) — the captions say so.
# No new cards: the rules restate the pinned cards (clearance, dosing, elimination, efficacypotency, antagonists, ti,
# cypinducers, cypinhibitors — fact-checked against the corpus). Sources: First Aid 2025 pp. 229–233, 251.
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
K = lambda *k: ['pk:' + x for x in k]
D = lambda *k: ['pd:' + x for x in k]

# ════════ 1. plasma level over time ════════
box(160, 130, 2340, 900)
text('Plasma level over time — a dose every half-life', 180, 166, 'dyn-big')
text('illustrative units: time in the drug’s usual half-lives, level relative to the target', 180, 186, 'dyn-cap')
TX0, TX1, TY0, TY1, TMAX, CMAX = 300, 2280, 820, 260, 8, 3.0
tx = lambda t: round(TX0 + t / TMAX * (TX1 - TX0), 1)
cy = lambda c: round(TY0 - min(c, CMAX) / CMAX * (TY0 - TY1), 1)
add(f'<path d="M{TX0} {TY1 - 20} V{TY0} H{TX1}" class="dyn-line"/>'
    + ''.join(f'<path d="M{tx(t)} {TY0} V{TY0 + 8}" class="dyn-line"/><text class="nf-l2" x="{tx(t)}" y="{TY0 + 26}" text-anchor="middle">{t}</text>' for t in range(0, TMAX + 1)))
text('half-lives', TX1, TY0 + 52, 'dyn-cap', 'end')
text('plasma level', TX0 - 20, TY1 - 30, 'nf-l2')
# therapeutic window (illustrative)
WLO, WHI = 0.5, 1.6
add(f'<rect x="{TX0}" y="{cy(WHI)}" width="{TX1 - TX0}" height="{cy(WLO) - cy(WHI)}" style="fill:var(--ok);fill-opacity:.12"/>'
    f'<path d="M{TX0} {cy(WHI)} H{TX1} M{TX0} {cy(WLO)} H{TX1}" class="dyn-dash" style="stroke:var(--ok)"/>')
text('toxic above', TX1 - 10, cy(WHI) - 10, 'nf-l2', 'end')
text('therapeutic window', TX1 - 10, cy(WLO) - 12, 'nf-l2', 'end')
text('too low to work', TX1 - 10, cy(WLO) + 24, 'nf-l2', 'end')

def level(t, dose=0.6, half=1.0, tau=1.0, load=None):
    k = math.log(2) / half; c = 0.0; n = 0
    while n * tau <= t + 1e-9:
        d = load if (n == 0 and load) else dose
        c += d * math.exp(-k * (t - n * tau)); n += 1
    return c
def series(**kw):
    pts = []
    t = 0.0
    while t <= TMAX + 1e-9:
        # sample just before and at each dose so the sawtooth stays sharp
        pts.append((t, level(t, **kw)))
        t = round(t + 0.02, 4)
    return 'M' + ' L'.join(f'{tx(a)} {cy(c)}' for a, c in pts)
TR = lambda col: f'class="dyn-trace" style="stroke:var({col});stroke-width:4;fill:none"'
SCEN = dict(base=dict(), load=dict(load=1.2), dbl=dict(dose=1.2), ind=dict(half=0.5), inh=dict(half=2.0))
add(f'<path d="{series(**SCEN["base"])}" {TR("--dk11")}/>', unless=K('load', 'dbl', 'ind', 'inh', 'zero'))
for k in ('load', 'dbl', 'ind', 'inh'):
    add(f'<path d="{series(**SCEN["base"])}" class="dyn-trace dyn-dim" style="stroke:var(--ink-3);stroke-width:3;fill:none;stroke-dasharray:6 6"/>'
        f'<path d="{series(**SCEN[k])}" {TR("--dk3")}/>', when=K(k))
# zero vs first order: one dose of 2.0, then nothing
FO = 'M' + ' L'.join(f'{tx(t / 50)} {cy(2.0 * math.exp(-math.log(2) * t / 50))}' for t in range(0, TMAX * 50 + 1))
ZO = 'M' + ' L'.join(f'{tx(t / 50)} {cy(max(0.0, 2.0 - 0.35 * t / 50))}' for t in range(0, TMAX * 50 + 1))
add(f'<path d="{FO}" {TR("--dk11")}/><path d="{ZO}" {TR("--dk3")}/>', when=K('zero'))
text('first-order: half of what is left, each half-life — a curve', tx(1.6), cy(0.85), TAG, when=K('zero'))
text('zero-order: the same amount each time — a straight line', tx(3.7), cy(1.0), TAG, when=K('zero'))
# steady state marker: 4–5 half-lives of the drug in use
def ssband(t0, t1, lab, when=None, unless=None, lx=None, anchor=None):
    x0, x1 = tx(min(t0, TMAX)), tx(min(t1, TMAX))
    add(f'<rect x="{x0}" y="{TY1 - 20}" width="{max(6, x1 - x0)}" height="{TY0 - TY1 + 20}" style="fill:var(--accent);fill-opacity:.08;stroke:var(--accent);stroke-opacity:.4"/>', when, unless)
    text(lab, lx if lx is not None else x0 + 8, TY1 - 30, 'nf-l1', anchor, when=when, unless=unless)
ssband(4, 5, 'steady state: 4–5 half-lives', unless=K('load', 'ind', 'inh', 'zero'))
ssband(0, 0.15, 'at the target from the first dose', when=K('load'), lx=TX0 + 140)
ssband(2, 2.5, 'steady state sooner — shorter half-life', when=K('ind'))
ssband(8, 8, 'steady state takes 8–10 baseline half-lives — off the graph →', when=K('inh'), lx=TX1 - 20, anchor='end')
text('a loading dose fills the volume of distribution at once', tx(1.2), cy(2.2), TAG, when=K('load'))
text('twice the dose → twice the level · same time to steady state', tx(1.2), cy(2.6), TAG, when=K('dbl'))
text('inducer: more enzyme, cleared faster — the level falls below the window, the drug fails', tx(0.4), cy(2.6), TAG, when=K('ind'))
text('inhibitor: cleared slower — the level climbs into the toxic range', tx(0.4), cy(2.8), TAG, when=K('inh'))

# ════════ 2. dose–response ════════
box(160, 940, 2340, 1700)
text('Effect vs log dose — the agonist’s curve', 180, 976, 'dyn-big')
text('illustrative: the agonist alone has its EC50 at dose 1 and a full effect of 100%', 180, 996, 'dyn-cap')
DX0, DX1, DY0, DY1 = 300, 1500, 1620, 1080
dx = lambda logd: round(DX0 + (logd + 3) / 6 * (DX1 - DX0), 1)   # log10 dose −3 … +3
dy = lambda e: round(DY0 - e / 100 * (DY0 - DY1), 1)
add(f'<path d="M{DX0} {DY1 - 20} V{DY0} H{DX1}" class="dyn-line"/>'
    + ''.join(f'<path d="M{dx(l)} {DY0} V{DY0 + 8}" class="dyn-line"/><text class="nf-l2" x="{dx(l)}" y="{DY0 + 26}" text-anchor="middle">{10 ** l:g}</text>' for l in range(-3, 4))
    + ''.join(f'<text class="nf-l2" x="{DX0 - 12}" y="{dy(e) + 4}" text-anchor="end">{e}%</text>' for e in (0, 50, 100)))
text('dose (log scale)', DX1, DY0 + 52, 'dyn-cap', 'end')
text('effect', DX0 - 20, DY1 - 30, 'nf-l2')
def drc(ec50=1.0, emax=100):
    return 'M' + ' L'.join(f'{dx(l / 20)} {dy(emax * 10 ** (l / 20) / (10 ** (l / 20) + ec50))}' for l in range(-60, 61))
add(f'<path d="{drc()}" {TR("--dk11")}/>')
text('agonist', dx(0.6), dy(78), 'nf-l1')
PDS = dict(comp=dict(ec50=10), noncomp=dict(emax=50), partial=dict(emax=40), potent=dict(ec50=0.1))
for k, kw in PDS.items():
    add(f'<path d="{drc(**kw)}" {TR("--dk3")}/>', when=D(k))
add(f'<path d="M{dx(0)} {dy(50)} V{DY0}" class="dyn-dash"/>')
text('EC50', dx(0) + 8, DY0 - 10, 'nf-l2')
TX = 1580
text('Reading the curve', TX, 1090, 'nf-l1')
text('height = efficacy (Emax) · left–right position = potency (EC50)', TX, 1114)
text('left-shifted = more potent · taller = more efficacious — the two are unrelated', TX, 1138)
text('competitive: shifted right — potency falls, efficacy unchanged;', TX, 1200, TAG, when=D('comp'))
text('more agonist overcomes it (flumazenil vs diazepam)', TX, 1222, TAG, when=D('comp'))
text('noncompetitive: the curve flattens — efficacy falls;', TX, 1200, TAG, when=D('noncomp'))
text('more agonist cannot overcome it (phenoxybenzamine vs norepinephrine)', TX, 1222, TAG, when=D('noncomp'))
text('partial agonist: same site, a lower maximum; with a full agonist it blocks', TX, 1200, TAG, when=D('partial'))
text('buprenorphine can precipitate withdrawal on full opioids', TX, 1222, TAG, when=D('partial'))
text('more potent: same height, shifted left — less drug for the same effect', TX, 1200, TAG, when=D('potent'))
text('Therapeutic index = TD50 ÷ ED50 — higher is safer', TX, 1320, 'nf-l1')
text('narrow: warfarin, theophylline, digoxin, antiepileptics, lithium — monitor levels', TX, 1344)

# ════════ 3. tap targets ════════
sites = [
  dict(x=tx(4.5), y=TY1 + 10, n=[0, 1], w=8, t='ex', l='', aria='Steady state and half-life', ions=[], c='clearance'),
  dict(x=dx(0), y=dy(50), n=[1, 0], w=8, t='ex', l='', aria='Efficacy and potency', ions=[], c='efficacypotency'),
  dict(x=TX - 30, y=1206, n=[1, 0], w=8, t='ex', l='', aria='Antagonists', ions=[], c='antagonists'),
]

# ════════ 4. readouts ════════
m = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Steady-state level', mods=[m(K('load'), 0), m(K('dbl', 'inh'), 1), m(K('ind'), -1)]),
  dict(l='Time to steady state', mods=[m(K('load', 'ind'), -1), m(K('dbl'), 0), m(K('inh'), 1)]),
  dict(l='Half-life', mods=[m(K('load', 'dbl'), 0), m(K('ind'), -1), m(K('inh'), 1)]),
  dict(l='Potency', mods=[m(D('comp'), -1), m(D('potent'), 1)]),
  dict(l='Efficacy', mods=[m(D('comp', 'potent'), 0), m(D('noncomp', 'partial'), -1)]),
]

# ════════ 5. notes ════════
notes = {
  '': 'A dose every half-life: the level climbs with each dose and levels off at steady state after 4–5 half-lives — when '
      'elimination equals administration. Time to steady state depends on the half-life only, not the dose. Pick a dosing '
      'change above, or an antagonist below.',
  'pk:load': 'A loading dose fills the volume of distribution to the target at once — LD = Cp × Vd ÷ F — so the level starts in '
             'the window instead of climbing for 4–5 half-lives. The maintenance dose (MD = Cp × CL × τ ÷ F) then replaces '
             'what clearance removes.',
  'pk:dbl': 'Twice the dose gives twice the steady-state level, but steady state still takes 4–5 half-lives — the dose does '
            'not change the timing.',
  'pk:ind': 'A CYP inducer (rifampin, carbamazepine, phenytoin, St John’s wort) makes more enzyme: the substrate is cleared '
            'faster, its level falls and it fails — OCP failure, low cyclosporine, a subtherapeutic INR on warfarin.',
  'pk:inh': 'A CYP inhibitor (azoles, macrolides, ritonavir, grapefruit juice) slows clearance: the substrate builds up toward '
            'toxicity — bleeding on warfarin, statin myopathy — and takes longer to reach steady state.',
  'pk:zero': 'Zero-order elimination: the machinery is saturated, so a constant amount is removed per unit time and the level '
             'falls in a straight line — phenytoin, ethanol, aspirin at high doses (PEA). First-order removes a constant '
             'fraction, so the half-life is constant.',
  'pd:comp': 'A competitive antagonist binds the same site reversibly: the agonist’s curve shifts right — potency falls, '
             'efficacy is unchanged, and more agonist overcomes it (flumazenil vs diazepam at GABA-A).',
  'pd:noncomp': 'A noncompetitive antagonist flattens the curve: efficacy falls and more agonist cannot overcome it '
                '(phenoxybenzamine vs norepinephrine at α receptors).',
  'pd:partial': 'A partial agonist binds the same site with a lower maximal effect: alone it activates; given with a full agonist '
                'it blocks — buprenorphine can precipitate withdrawal in someone on full opioids.',
  'pd:potent': 'A more potent agonist reaches the same effect with less drug — the curve shifts left at the same height. '
               'Potency (EC50) and efficacy (Emax) are unrelated.',
}

dyn = dict(
  kinds={}, groups=[],
  switches=[dict(id='pk', label='Change the dosing', type='one',
                 options=[['load', 'Give a loading dose', 'dosing'], ['dbl', 'Double the dose', 'clearance'],
                          ['ind', 'Add a CYP inducer', 'cypinducers'], ['inh', 'Add a CYP inhibitor', 'cypinhibitors'],
                          ['zero', 'Zero- vs first-order', 'elimination']]),
            dict(id='pd', label='Change the dose–response', type='one',
                 options=[['comp', 'Competitive antagonist', 'antagonists'], ['noncomp', 'Noncompetitive antagonist', 'antagonists'],
                          ['partial', 'Partial agonist', 'antagonists'], ['potent', 'A more potent agonist', 'efficacypotency']])],
  notes=notes, shapes=shapes, flows=[], sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 229–233, 251 · illustrative curves')

MAP = dict(
  id='pksim', title='Pharmacokinetics & Dose–Response Simulator', topic='pharm', after='pkpd',
  sub='Dose a drug every half-life and watch it reach steady state — then add a loading dose, double the dose, add a CYP inducer '
      'or inhibitor, or compare zero- and first-order elimination. Below, see what competitive and noncompetitive antagonists, a '
      'partial agonist and a more potent drug do to the dose–response curve. Tap a curve for its card',
  w=3500, h=2100,
  fa='229–233, 251', src=[],
  lanes=[('pkKin', 'Pharmacokinetics', 'glycolysis'), ('pkDyn', 'Pharmacodynamics', 'tca'), ('pkCyp', 'Drug interactions', 'gluconeo')],
  nodes=[
    ('pk1', 'Half-life & steady state', 380, 1800, 'pkKin', 't½ = 0.7 × Vd ÷ CL', ['clearance', 'vd']),
    ('pk2', 'Loading & maintenance', 820, 1800, 'pkKin', 'volume · clearance', ['dosing', 'bioavail']),
    ('pk3', 'Zero vs first order', 1260, 1800, 'pkKin', 'PEA', ['elimination']),
    ('pk4', 'CYP inducers & inhibitors', 1700, 1800, 'pkCyp', 'levels down · levels up', ['cypinducers', 'cypinhibitors', 'cyp3a4']),
    ('pk5', 'Efficacy vs potency', 2140, 1800, 'pkDyn', 'height vs position', ['efficacypotency']),
    ('pk6', 'Agonists & antagonists', 380, 1940, 'pkDyn', 'right shift vs flattened', ['antagonists']),
    ('pk7', 'Therapeutic index', 820, 1940, 'pkDyn', 'TD50 ÷ ED50', ['ti', 'druginteract'])],
  panels=[
    (2420, 860, 1000, 'Formulas (First Aid p. 229)', [
      ('Half-life', 't½ = 0.7 × Vd ÷ CL'),
      ('Loading dose', 'Cp × Vd ÷ F — depends on volume'),
      ('Maintenance dose', 'Cp × CL × τ ÷ F — depends on clearance'),
      ('Steady state', '4–5 half-lives · 50, 75, 87.5, 94% after 1–4'),
      ('Renal or liver failure', 'loading dose usually unchanged · lower the maintenance dose')]),
    (2420, 1100, 1000, 'Curves and interactions (First Aid pp. 230–233, 251)', [
      ('Zero-order', 'constant amount per time — phenytoin, ethanol, aspirin (high doses)'),
      ('Competitive antagonist', 'right shift · potency ↓ · surmountable'),
      ('Noncompetitive antagonist', 'flattened · efficacy ↓ · not surmountable'),
      ('Partial agonist', 'lower maximum · blocks a full agonist'),
      ('CYP inducer · inhibitor', 'substrate level ↓ (fails) · ↑ (toxic)')])],
  dyn=dyn)
