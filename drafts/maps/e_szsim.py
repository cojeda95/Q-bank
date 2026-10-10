# Antiseizure Drugs in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# An excitatory neuron (action potentials down the axon through voltage-gated Na⁺ channels → Ca²⁺ entry at the terminal →
# SV2A vesicles → glutamate onto the next neuron), an inhibitory interneuron (GABA → GABA-A chloride channel, GABA
# transaminase in glia), and a thalamocortical inset with T-type Ca²⁺ channels and the 3-Hz rhythm, plus an EEG strip. A
# `one` switch picks the seizure (focal, absence, generalized tonic-clonic, status); a second gives a drug (phenytoin,
# carbamazepine, lamotrigine, valproate, topiramate, levetiracetam, ethosuximide, gabapentin, benzodiazepine) and its
# target is blocked or boosted and the firing settles. 4 readouts. Facts from the pinned cards; FA pages in `fa`.
# No new cards.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

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
def box(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')

S = lambda *k: [f'sz:{x}' for x in k]
D = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
NA = D('phen', 'carb', 'lamo', 'valp', 'topi')
CA = D('gaba', 'valp')
GABAUP = D('benzo', 'topi', 'valp')
QUIET = NA + CA + D('leve', 'benzo')
def box(x0, y0, x1, y1, lab, cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="30" class="{cls}"/>')
    if lab: text(lab, (x0 + x1) // 2, y0 + 36, 'nf-l1', 'middle')

text('Antiseizure drugs — four ways to quiet a neuron', 180, 150, 'dyn-big')
text('Na⁺ channels · Ca²⁺ channels · more GABA · less glutamate release', 180, 176, 'dyn-cap')

# ════════ excitatory neuron ════════
box(300, 300, 620, 520, 'Excitatory neuron')
add('<path d="M620 410 H1260" style="stroke:var(--dk2);stroke-width:26;opacity:.3;stroke-linecap:round"/>')
text('axon — action potentials', 940, 380, 'nf-l2', 'middle')
box(1260, 300, 1560, 560, 'Terminal')
for (x, y) in ((1330, 450), (1400, 480), (1470, 450)):
    add(f'<circle cx="{x}" cy="{y}" r="22" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>')
text('glutamate vesicles', 1410, 530, 'nf-l2', 'middle')
box(1260, 640, 1560, 900, 'Postsynaptic neuron')
add('<path d="M1300 600 H1520" style="stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 6"/>')
text('synapse', 1580, 606, 'nf-l2')
# inhibitory interneuron and glia
box(1700, 640, 2000, 900, 'Inhibitory interneuron')
text('GABA', 1850, 760, 'nf-l2', 'middle')
box(1700, 960, 2000, 1080, 'Glia')
text('GABA transaminase breaks GABA down', 1850, 1050, 'nf-l2', 'middle')
add('<path d="M1700 760 H1560" style="stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 6"/>')
# thalamus inset
box(300, 640, 1000, 1080, 'Thalamus ⇄ cortex', 'dyn-soft')
add('<ellipse cx="650" cy="860" rx="220" ry="110" style="fill:none;stroke:var(--dk7);stroke-width:5;opacity:.5"/>')
text('thalamocortical loop', 650, 865, 'nf-l2', 'middle')
text('T-type Ca²⁺ drives the 3-Hz rhythm of absence seizures', 650, 1050, 'nf-l2', 'middle')
# EEG strip
EY = 1260
add(f'<rect x="300" y="{EY - 90}" width="1700" height="180" rx="24" class="dyn-soft"/>')
text('EEG', 330, EY - 56, 'nf-l1')
def wave(amp, step, when=None, unless=None, cls='var(--ink-2)'):
    pts = ' '.join(f'L{x} {EY + (amp if (x // step) % 2 else -amp)}' for x in range(400, 1960, step))
    add(f'<path d="M400 {EY} {pts}" style="fill:none;stroke:{cls};stroke-width:3"/>', when=when, unless=unless)
wave(8, 20, unless=['sz:*&!rx:*'] + [f'sz:{s}&rx:{r}' for s in ('focal', 'gtc', 'status', 'absence') for r in ()])
wave(60, 26, when=['sz:focal&!rx:*', 'sz:gtc&!rx:*', 'sz:status&!rx:*'], cls='var(--bad)')
add(f'<path d="M400 {EY} ' + ' '.join(f'L{x} {EY - 70} L{x + 12} {EY + 50} L{x + 60} {EY - 10}' for x in range(400, 1900, 86)) + '" style="fill:none;stroke:var(--bad);stroke-width:3"/>', when=['sz:absence&!rx:*'])
text('3-Hz spike-and-wave', 1150, EY + 76, 'nf-l1 dyn-tag', 'middle', when=['sz:absence&!rx:*'])
text('seizure activity', 1150, EY + 76, 'nf-l1 dyn-tag', 'middle', when=['sz:focal&!rx:*', 'sz:gtc&!rx:*', 'sz:status&!rx:*'])
text('≥ 5 minutes, or no recovery between seizures', 1150, EY - 100, 'nf-l1 dyn-tag', 'middle', when=S('status'))
TOX = dict(phen='zero-order kinetics · gingival hyperplasia · hirsutism · fetal hydantoin · SJS',
           carb='SIADH · agranulocytosis, aplastic anemia · CYP inducer · trigeminal neuralgia',
           lamo='rash — SJS, DRESS', valp='hepatotoxicity · pancreatitis · neural tube defects (highest risk)',
           topi='weight loss · kidney stones · angle-closure glaucoma', leve='neuropsychiatric effects',
           etho='sedation, dizziness, vomiting — absence only', gaba='sedation, ataxia · neuropathic pain',
           benzo='lorazepam first for status · respiratory depression with alcohol/opioids')
for k, t in TOX.items(): text(t, 1150, 1470, 'nf-l1', 'middle', when=D(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
SEIZE = S('focal', 'gtc', 'status')
flows = [
  dict(d='M620 410 H1260', len=640, speed=220, r=9, base=dict(ap=3), mods=[m(SEIZE, set=dict(ap=7)), m(NA, set=dict(ap=1))]),
  dict(d='M1410 500 V640', len=140, speed=80, r=8, base=dict(glu=3),
       mods=[m(SEIZE, set=dict(glu=6)), m(D('leve') + CA, set=dict(glu=1)), m(NA, set=dict(glu=1))]),
  dict(d='M1700 800 H1560', len=140, speed=70, r=8, base=dict(gab=2), mods=[m(GABAUP, set=dict(gab=5))]),
  dict(d='M1850 900 V960', len=60, speed=40, r=8, base=dict(gab=2), mods=[m(D('valp'), set=dict(gab=0))]),
  dict(d='M870 860 A220 110 0 1 1 869.9 859.9', len=1060, speed=150, r=9, base=dict(t=2),
       mods=[m(S('absence'), set=dict(t=6)), m(D('etho'), set=dict(t=1))]),
]
sites = [
  dict(x=940, y=410, n=[0, 1], w=26, t='ch', l='Na⁺ channel', s='held inactivated', c='phenytoin', ions=[['na', 'in', 2]],
       block=NA, lx=940, ly=470, la='middle'),
  dict(x=1260, y=380, n=[-1, 0], w=10, t='ch', l='Ca²⁺ channel', s='gabapentin · valproate', c='gabapentinoids', ions=[['ca', 'in', 1]],
       block=CA, lx=1240, ly=330, la='end'),
  dict(x=1470, y=400, n=[0, -1], w=10, t='rec', l='SV2A', s='levetiracetam', c='levetiracetam', ions=[], block=D('leve'),
       lx=1500, ly=360, la='start'),
  dict(x=1560, y=820, n=[1, 0], w=12, t='ch', l='GABA-A', s='Cl⁻ in', c='benzos', ions=[['cl', 'out', 2]], boost=GABAUP,
       lx=1580, ly=860, la='start'),
  dict(x=1850, y=960, n=[0, -1], w=10, t='rec', l='', aria='GABA transaminase', c='valproate', ions=[], block=D('valp')),
  dict(x=870, y=860, n=[1, 0], w=10, t='ch', l='T-type Ca²⁺', s='ethosuximide', c='ethosuximide', ions=[], block=D('etho'),
       lx=890, ly=800, la='start'),
]

readouts = [
  dict(l='Neuronal firing', mods=[dict(when=['sz:focal&!rx:*', 'sz:gtc&!rx:*', 'sz:status&!rx:*'], d=1), dict(when=QUIET, d=-1)]),
  dict(l='Glutamate release', mods=[dict(when=D('leve') + CA, d=-1)]),
  dict(l='GABA tone', mods=[dict(when=GABAUP, d=1)]),
  dict(l='Thalamic 3-Hz rhythm', mods=[dict(when=['sz:absence&!rx:etho'], d=1), dict(when=D('etho'), d=-1)]),
]

notes = {
  '': 'Each antiseizure drug quiets neurons one of four ways: hold voltage-gated Na⁺ channels inactivated, block thalamic T-type Ca²⁺ '
      'channels, boost GABA, or reduce transmitter release (SV2A, α₂δ Ca²⁺ channels).',
  'sz:focal': 'Focal seizures start in one area, most often the medial temporal lobe → carbamazepine, lamotrigine, levetiracetam.',
  'sz:absence': 'Absence: ~10-s staring spells, 3-Hz spike-and-wave, no postictal confusion, provoked by hyperventilation — thalamic '
                'T-type Ca²⁺ channels → ethosuximide (valproate is broad spectrum).',
  'sz:gtc': 'Generalized tonic-clonic: both hemispheres from the outset → valproate, levetiracetam, lamotrigine.',
  'sz:status': 'Status epilepticus: ≥ 5 minutes of seizure, or recurrent seizures without recovery — benzodiazepine (lorazepam) first.',
  'rx:phen': 'Phenytoin (fosphenytoin IV): holds Na⁺ channels inactivated; focal seizures. Zero-order kinetics; gingival hypertrophy, '
             'hirsutism, CYP induction, SJS/DRESS, fetal hydantoin syndrome.',
  'rx:carb': 'Carbamazepine: Na⁺-channel blocker for focal seizures; first line for trigeminal neuralgia; mood stabilizer. SIADH, '
             'agranulocytosis and aplastic anemia (check counts), CYP induction, SJS.',
  'rx:lamo': 'Lamotrigine: broad-spectrum Na⁺-channel blocker; mood stabilizer. Rash — SJS, DRESS.',
  'rx:valp': 'Valproate: broad spectrum (absence too) — blocks Na⁺ and Ca²⁺ channels and inhibits GABA transaminase, so GABA builds up. '
             'Hepatotoxicity, pancreatitis, CYP inhibition, the highest teratogenic risk (neural tube defects).',
  'rx:topi': 'Topiramate: Na⁺ channels + GABA-A potentiation; migraine prophylaxis. Weight loss, kidney stones, angle-closure glaucoma.',
  'rx:leve': 'Levetiracetam: binds SV2A on synaptic vesicles and reduces glutamate release. Broad spectrum. Neuropsychiatric effects.',
  'rx:etho': 'Ethosuximide: blocks thalamic T-type Ca²⁺ channels — the 3-Hz rhythm. Absence seizures only.',
  'rx:gaba': 'Gabapentin, pregabalin: act on voltage-gated Ca²⁺ channels; narrow-spectrum for focal seizures, more often for neuropathic pain.',
  'rx:benzo': 'Benzodiazepines bind the GABA-A chloride channel and increase the frequency of opening (GABA must be present). '
              'Lorazepam first for status epilepticus.',
}

dyn = dict(
  kinds=dict(ap=['sig', '--dk2'], glu=['tx', '--dk5'], gab=['tx', '--dk4'], t=['sig', '--dk7'], na=['ion', '--dk1'], ca=['ion', '--dk3'], cl=['ion', '--dk6']),
  groups=[['sig', 'Firing'], ['tx', 'Glutamate · GABA'], ['ion', 'Ions']],
  switches=[dict(id='sz', label='Seizure', type='one', options=[
              ['focal', 'Focal', 'epilepsyreg'], ['absence', 'Absence', 'epilepsyreg'], ['gtc', 'Generalized tonic-clonic', 'epilepsyreg'],
              ['status', 'Status epilepticus', 'statusepi']]),
            dict(id='rx', label='Drug', type='one', options=[
              ['phen', 'Phenytoin', 'phenytoin'], ['carb', 'Carbamazepine', 'carbamazepine'], ['lamo', 'Lamotrigine', 'lamotrigine'],
              ['valp', 'Valproate', 'valproate'], ['topi', 'Topiramate', 'topiramate'], ['leve', 'Levetiracetam', 'levetiracetam'],
              ['etho', 'Ethosuximide', 'ethosuximide'], ['gaba', 'Gabapentin', 'gabapentinoids'], ['benzo', 'Lorazepam', 'benzos']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 560–562 · Katzung ch 24')

MAP = dict(
  id='szsim', title='Antiseizure Drugs in Motion', topic='neuro', after='seizhead',
  sub='Pick a seizure and a drug: watch Na⁺ channels, Ca²⁺ channels, SV2A, GABA-A and the thalamic T-type rhythm respond — phenytoin, '
      'carbamazepine, lamotrigine, valproate, topiramate, levetiracetam, ethosuximide, gabapentin and lorazepam',
  w=3600, h=1900,
  fa='531, 560, 561, 562, 632, 660',
  src=['Katzung ch 24 — Antiseizure Medications', 'Kaplan & Sadock ch 21 — Psychopharmacology', 'Katzung ch 22 — Sedative-Hypnotic Drugs'],
  lanes=[('szNa', 'Na⁺-channel drugs', 'glycolysis'), ('szCa', 'Ca²⁺ & release', 'tca'), ('szGaba', 'GABA & seizure types', 'gluconeo')],
  nodes=[
    ('sz1', 'Antiseizure mechanisms', 330, 1620, 'szGaba', 'four ways', ['antiepileptics', 'epilepsyreg'], 'hub'),
    ('sz2', 'Phenytoin', 760, 1620, 'szNa', 'zero-order', ['phenytoin']),
    ('sz3', 'Carbamazepine', 1200, 1620, 'szNa', 'SIADH · aplastic', ['carbamazepine']),
    ('sz4', 'Lamotrigine · topiramate', 1640, 1620, 'szNa', 'SJS · stones', ['lamotrigine', 'topiramate']),
    ('sz5', 'Valproate', 2080, 1620, 'szNa', 'broad · teratogen', ['valproate']),
    ('sz6', 'Ethosuximide', 330, 1760, 'szCa', 'absence only', ['ethosuximide']),
    ('sz7', 'Levetiracetam', 760, 1760, 'szCa', 'SV2A', ['levetiracetam']),
    ('sz8', 'Gabapentin · pregabalin', 1200, 1760, 'szCa', 'neuropathic pain', ['gabapentinoids']),
    ('sz9', 'Benzodiazepines · status', 1640, 1760, 'szGaba', 'lorazepam first', ['benzos', 'statusepi'])],
  panels=[
    (2500, PANY, 1000, 'Seizure → first choices (First Aid p. 560)', [
      ('Focal', 'carbamazepine, lamotrigine, levetiracetam'),
      ('Absence', 'ethosuximide (valproate is broad)'),
      ('Generalized tonic-clonic', 'valproate, levetiracetam, lamotrigine'),
      ('Status epilepticus', 'lorazepam first')])],
  dyn=dyn)
