# PFTs & Flow–Volume Loops (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A flow–volume loop redrawn over the normal one for each pattern — obstructive (emphysema/COPD, asthma: shifted to
# larger volumes with a scooped expiratory limb), intrinsic restriction (interstitial lung disease) and extrapulmonary
# restriction (neuromuscular weakness, severe obesity: shifted to smaller volumes) — beside bars for RV, FRC and TLC
# against normal, and FEV₁/FVC. Readouts: FEV₁, FEV₁/FVC, TLC, RV, DLCO.
# No new cards: facts restate the pinned cards (pfts, lungvol, compliance, copd, asthma, ild, mg, gbs — fact-checked
# against the corpus). Curves and bar heights are schematic. Sources: First Aid 2025 pp. 682–683, 692.
import sys
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
P = lambda *k: ['pf:' + x for x in k]
OBS, REST, EXT = P('copd', 'asthma'), P('ild', 'nm', 'obese'), P('nm', 'obese')

# ════════ 1. the flow–volume loop ════════
box(160, 130, 1400, 1180)
text('Flow–volume loop', 180, 166, 'dyn-big')
text('schematic · volume runs from TLC (left) to RV (right) — the convention used for these loops', 180, 186, 'dyn-cap')
# volume axis: 8 L at the left → 0 L at the right; flow axis: expiration up, inspiration down
VX = lambda v: round(260 + (8 - v) / 8 * 1060)
FY0 = 680
FY = lambda f: round(FY0 - f * 55)
add(f'<path d="M{VX(8)} {FY0} H{VX(0)}" class="dyn-line"/><path d="M{VX(8)} {FY(8)} V{FY(-6)}" class="dyn-line"/>'
    + ''.join(f'<path d="M{VX(v)} {FY0 - 6} V{FY0 + 6}" class="dyn-line"/><text class="nf-l2" x="{VX(v)}" y="{FY0 + 26}" text-anchor="middle">{v}</text>' for v in range(0, 9, 2)))
text('volume (L)', VX(0), FY0 + 52, 'dyn-cap', 'end')
text('expiration ↑', VX(8) + 10, FY(8) - 6, 'nf-l2')
text('inspiration ↓', VX(8) + 10, FY(-6) + 20, 'nf-l2')
def loop(tlc, rv, peak, scoop=0.0):
    """expiratory limb: a quick rise to peak flow, then down to RV (scooped = concave); inspiratory limb: a U below"""
    pts = []
    n = 60
    for i in range(n + 1):
        u = i / n                                  # 0 at TLC → 1 at RV
        v = tlc - u * (tlc - rv)
        if u < 0.12: f = peak * (u / 0.12)
        else:
            w = (u - 0.12) / 0.88
            f = peak * (1 - w) ** (1 + 1.6 * scoop)     # scoop > 0 bows the limb inward (concave)
        pts.append(f'{VX(v)} {FY(f)}')
    for i in range(n + 1):
        u = i / n
        v = rv + u * (tlc - rv)
        f = -peak * 0.75 * (1 - (2 * u - 1) ** 2)
        pts.append(f'{VX(v)} {FY(f)}')
    return 'M' + ' L'.join(pts) + ' Z'
NORM = dict(tlc=6, rv=1.5, peak=8)
LOOPS = dict(copd=dict(tlc=7.6, rv=4.2, peak=4.5, scoop=0.9), asthma=dict(tlc=7.0, rv=3.0, peak=5.5, scoop=0.6),
             ild=dict(tlc=3.8, rv=0.9, peak=7), nm=dict(tlc=4.0, rv=1.4, peak=5), obese=dict(tlc=4.4, rv=1.3, peak=6.5))
add(f'<path d="{loop(**NORM)}" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 6"/>', when=['pf:*'])
add(f'<path d="{loop(**NORM)}" class="dyn-trace" style="fill:var(--dk11);fill-opacity:.08;stroke:var(--dk11);stroke-width:4"/>', unless=['pf:*'])
for k, kw in LOOPS.items():
    add(f'<path d="{loop(**kw)}" class="dyn-trace" style="fill:var(--dk3);fill-opacity:.1;stroke:var(--dk3);stroke-width:4"/>', when=P(k))
text('dashed = normal', 1380, 230, 'dyn-cap', 'end', when=['pf:*'])
text('shifted left (larger volumes) · scooped expiration — air trapped', 180, 1100, TAG, when=OBS)
text('shifted right (smaller volumes) · shape kept, everything smaller', 180, 1100, TAG, when=REST)
text('pick a pattern to compare with normal', 180, 1100, 'dyn-cap', unless=['pf:*'])

# ════════ 2. lung volumes ════════
box(1440, 130, 2340, 1180)
text('Lung volumes', 1460, 166, 'dyn-big')
text('RV · FRC · TLC — residual volume can’t be measured by spirometry', 1460, 186, 'dyn-cap')
BX, BY, BH = 1540, 900, 560          # bars: base y, height of 8 L
by = lambda v: round(BY - v / 8 * BH)
VOLS = dict(norm=(1.5, 3.0, 6.0), copd=(4.2, 5.0, 7.6), asthma=(3.0, 4.2, 7.0), ild=(0.9, 1.9, 3.8), nm=(1.4, 2.2, 4.0), obese=(1.3, 1.8, 4.4))
LAB = ['RV', 'FRC', 'TLC']
add(f'<path d="M{BX - 20} {BY} H{BX + 3 * 220}" class="dyn-line"/>')
for i, l in enumerate(LAB):
    text(l, BX + i * 220 + 70, BY + 30, 'nf-l1', 'middle')
def bars(vals, when=None, unless=None):
    add(''.join(f'<rect x="{BX + i * 220 + 20}" y="{by(v)}" width="100" height="{BY - by(v)}" rx="8" style="fill:var(--dk9);fill-opacity:.7"/>'
                for i, v in enumerate(vals)), when, unless)
bars(VOLS['norm'], unless=['pf:*'])
for k in LOOPS:
    bars(VOLS[k], when=P(k))
    add(''.join(f'<path d="M{BX + i * 220 + 10} {by(v)} H{BX + i * 220 + 130}" class="dyn-dash"/>' for i, v in enumerate(VOLS['norm'])), when=P(k))
text('dashed = normal · heights schematic', 1460, 980, 'dyn-cap')
text('RV, FRC and TLC up — hyperinflation', 1460, 1040, TAG, when=OBS)
text('TLC down — the lung (or the chest) can’t fill', 1460, 1040, TAG, when=REST)
text('FEV₁ ÷ FVC below 70%', 1460, 1070, TAG, when=OBS)
text('FEV₁ ÷ FVC normal or high', 1460, 1070, TAG, when=REST)
text('DLCO low — alveolar surface destroyed', 1460, 1100, TAG, when=P('copd'))
text('DLCO low — thickened interstitium · A–a gradient widened', 1460, 1100, TAG, when=P('ild'))
text('DLCO normal — the lung itself is healthy · normal A–a', 1460, 1100, TAG, when=EXT)

# ════════ 3. sites ════════
sites = [
  dict(x=VX(6), y=FY(8) - 30, n=[0, 1], w=10, t='ex', l='', aria='Obstructive vs restrictive PFTs', ions=[], c='pfts'),
  dict(x=BX + 3 * 220 + 40, y=by(6.0), n=[-1, 0], w=10, t='ex', l='', aria='Lung volumes and capacities', ions=[], c='lungvol'),
]

# ════════ 4. readouts ════════
m = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='FEV₁', mods=[m(['pf:*'], -1)]),
  dict(l='FEV₁/FVC', mods=[m(OBS, -1)]),
  dict(l='TLC', mods=[m(OBS, 1), m(REST, -1)]),
  dict(l='RV', mods=[m(OBS, 1)]),
  dict(l='DLCO', mods=[m(P('copd', 'ild'), -1), m(EXT, 0)]),
]

# ════════ 5. notes ════════
notes = {
  '': 'Obstructive disease closes airways early at high lung volumes and traps air: FEV₁ falls more than FVC, so FEV₁/FVC drops '
      'below 70%, and RV, FRC and TLC rise. Restrictive disease shrinks the volumes: TLC falls and FEV₁/FVC is normal or high. '
      'DLCO separates restriction in the lung from restriction outside it. Pick a pattern.',
  'pf:copd': 'Emphysema / COPD (obstructive): airways close early and air is trapped — the loop shifts left with a scooped '
             'expiratory limb; FEV₁/FVC below 70%; RV, FRC and TLC up. Compliance is increased and DLCO is low (alveolar '
             'surface destroyed).',
  'pf:asthma': 'Asthma (obstructive): bronchospasm narrows the airways — FEV₁/FVC low, with air trapping during an attack.',
  'pf:ild': 'Interstitial lung disease (intrinsic restriction): a stiff, fibrotic lung — low compliance, TLC and FVC down, '
            'FEV₁/FVC normal or high; the loop shifts right. DLCO low and the A–a gradient widened.',
  'pf:nm': 'Respiratory muscle weakness (polio, myasthenia gravis, Guillain-Barré, ALS) — extrapulmonary restriction: the '
           'lung is normal but cannot be filled. TLC down with a normal DLCO and A–a gradient.',
  'pf:obese': 'Severe obesity (or scoliosis) — extrapulmonary restriction from the chest wall: TLC down, but DLCO and the A–a '
              'gradient are normal because the lung itself is healthy.',
}
# UNVERIFIED: RV direction in restriction left "–" (no card states it); asthma DLCO not given

dyn = dict(
  kinds={}, groups=[],
  switches=[dict(id='pf', label='Pick a pattern', type='one',
                 options=[['copd', 'Emphysema / COPD', 'copd'], ['asthma', 'Asthma', 'asthma'], ['ild', 'Interstitial lung disease', 'ild'],
                          ['nm', 'Neuromuscular weakness', 'pfts'], ['obese', 'Severe obesity', 'pfts']])],
  notes=notes, shapes=shapes, flows=[], sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 682–683, 692 · schematic curves')

MAP = dict(
  id='pftsim', title='PFTs & Flow–Volume Loops', topic='pulmo', after='lungdz',
  sub='A flow–volume loop and the lung volumes for obstructive disease (COPD, asthma) and restrictive disease inside the lung '
      '(interstitial lung disease) or outside it (muscle weakness, obesity), against normal — with FEV₁, FEV₁/FVC, TLC, RV and '
      'DLCO. Tap the loop or the bars for their cards',
  w=3500, h=2100,
  fa='682–683, 692', src=[],
  lanes=[('pfObs', 'Obstructive', 'glycolysis'), ('pfRes', 'Restrictive', 'tca'), ('pfPhys', 'Mechanics', 'gluconeo')],
  nodes=[
    ('pf1', 'Obstructive vs restrictive', 380, 1300, 'pfPhys', 'FEV₁/FVC · TLC · DLCO', ['pfts']),
    ('pf2', 'Lung volumes', 820, 1300, 'pfPhys', 'four volumes, four capacities', ['lungvol', 'lungthorax']),
    ('pf3', 'Compliance', 1260, 1300, 'pfPhys', 'emphysema ↑ · fibrosis ↓', ['compliance']),
    ('pf4', 'COPD & asthma', 1700, 1300, 'pfObs', 'air trapping', ['copd', 'asthma']),
    ('pf5', 'Interstitial lung disease', 380, 1440, 'pfRes', 'stiff lung · ↓ DLCO', ['ild']),
    ('pf6', 'Muscle weakness', 820, 1440, 'pfRes', 'normal DLCO', ['mg', 'sleepapnea'])],
  panels=[
    (2420, 760, 1000, 'The patterns (First Aid p. 692)', [
      ('Normal', 'FEV₁ and FVC over 80% predicted · FEV₁/FVC over 70%'),
      ('Obstructive', 'FEV₁/FVC < 70% · RV, FRC, TLC ↑ · loop shifted left, scooped'),
      ('Restrictive', 'TLC ↓ · FEV₁/FVC normal or ↑ · loop shifted right'),
      ('Intrinsic restriction', 'interstitial disease · DLCO ↓ · A–a ↑'),
      ('Extrapulmonary restriction', 'muscle weakness, chest wall · DLCO and A–a normal')])],
  dyn=dyn)
