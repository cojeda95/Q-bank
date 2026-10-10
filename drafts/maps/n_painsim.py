# Pain Gone Wrong in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The spinothalamic route — free nerve ending → Aδ/C fiber → dorsal horn → across the anterior white commissure → opposite
# side up to VPL of the thalamus → primary somatosensory cortex — with pain signals moving along it. A `dx` switch breaks it:
# peripheral neuropathic pain (upregulated, persistently active Na⁺ channels — diabetic neuropathy, postherpetic neuralgia),
# thalamic pain syndrome (lenticulostriate occlusion → contralateral allodynia weeks to months later), phantom limb (limb gone,
# S1 reorganized) and fibromyalgia (widespread pain, normal inflammatory markers). An `rx` switch gives gabapentinoid, TCA,
# SNRI, capsaicin or TENS; pain eases only where the card pairs the drug with that condition. 4 readouts. Facts from the
# pinned cards; FA pages in `fa`. No new cards.
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

D = lambda *k: [f'dx:{x}' for x in k]
R = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
WORKS = dict(neuro=('gaba', 'tca', 'caps'), fibro=('snri', 'tca', 'gaba'))
OK = [f'dx:{d}&rx:{r}' for d, rs in WORKS.items() for r in rs]
NERVE = 'M420 1350 C560 1300 720 1180 850 1070'
CROSS = 'M850 1070 C880 1120 960 1150 1020 1120'
UP = 'M1020 1120 C1060 900 1150 720 1200 620'
CTX = 'M1200 620 C1220 500 1250 400 1260 320'

text('Pain gone wrong — the pain pathway, and where it misfires', 180, 150, 'dyn-big')
text('free nerve ending → dorsal horn → cross → opposite side up to thalamus (VPL) → cortex', 180, 176, 'dyn-cap')

# ════════ anatomy ════════
add('<path d="M330 1360 C360 1320 460 1320 500 1360 C480 1400 360 1400 330 1360 Z" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--dk2);stroke-width:3"/>',
    unless=D('phantom'))
add('<path d="M330 1360 C360 1320 460 1320 500 1360 C480 1400 360 1400 330 1360 Z" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 8"/>',
    when=D('phantom'))
text('foot (free nerve endings)', 420, 1430, 'nf-l2', 'middle')
text('amputated — the limb is gone', 420, 1470, 'nf-l1 dyn-tag', 'middle', when=D('phantom'))
add(f'<path d="{NERVE}" style="fill:none;stroke:var(--dk7);stroke-width:8;opacity:.5"/>', unless=D('phantom')); text('Aδ / C fibers', 620, 1230, 'nf-l2', 'end')
add('<circle cx="920" cy="1110" r="150" style="fill:var(--dk3);fill-opacity:.08;stroke:var(--dk3);stroke-width:4"/>'); text('spinal cord', 920, 1300, 'nf-l1', 'middle')
add('<path d="M850 1010 C860 1050 860 1080 870 1110" style="fill:none;stroke:var(--dk4);stroke-width:30;opacity:.3"/>'); text('dorsal horn', 780, 1000, 'nf-l2', 'end')
text('anterior white commissure', 920, 1200, 'nf-l2', 'middle')
add(f'<path d="{CROSS} {UP[UP.index("C"):]} " style="fill:none;stroke:var(--dk7);stroke-width:8;opacity:.4"/>'); text('spinothalamic (opposite side)', 1120, 900, 'nf-l2')
add('<ellipse cx="1200" cy="620" rx="80" ry="50" style="fill:var(--dk9);fill-opacity:.25;stroke:var(--dk9);stroke-width:3"/>', unless=D('thal'))
add('<ellipse cx="1200" cy="620" rx="80" ry="50" style="fill:var(--bad);fill-opacity:.5;stroke:var(--bad);stroke-width:4"/>', when=D('thal'))
text('thalamus (VPL)', 1300, 630, 'nf-l2')
add('<path d="M1100 760 C1140 700 1170 670 1190 650" style="stroke:var(--nf-blood);stroke-width:6"/>', when=D('thal')); text('lenticulostriate', 1080, 780, 'nf-l2', 'end', when=D('thal'))
add('<path d="M1000 330 C1100 260 1400 260 1500 330" style="fill:none;stroke:var(--dk4);stroke-width:34;opacity:.25;stroke-linecap:round"/>', unless=D('phantom'))
add('<path d="M1000 330 C1100 260 1400 260 1500 330" style="fill:none;stroke:var(--bad);stroke-width:34;opacity:.4;stroke-linecap:round"/>', when=D('phantom'))
text('primary somatosensory cortex', 1250, 240, 'nf-l1', 'middle')
for x in (520, 640, 760):
    add(f'<rect x="{x - 10}" y="1260" width="20" height="30" rx="4" style="fill:var(--bad);opacity:.8"/>', when=D('neuro'))
text('upregulated Na⁺ channels fire on their own', 640, 1330, 'nf-l1 dyn-tag', 'middle', when=D('neuro'))
for x, y in ((1700, 500), (1900, 500), (1700, 900), (1900, 900)):
    add(f'<circle cx="{x}" cy="{y}" r="60" style="fill:var(--bad);fill-opacity:.25;stroke:var(--bad);stroke-width:3"/>', when=D('fibro'))
text('widespread pain in all four quadrants ≥ 3 months · ESR normal', 1800, 1020, 'nf-l1 dyn-tag', 'middle', when=D('fibro'))
TAG = dict(neuro='diabetic neuropathy, postherpetic neuralgia — burning, electric pain ordinary analgesics miss',
           thal='thalamic lesion — paresthesias, then allodynia, hyperalgesia, dysesthesia on the opposite side',
           phantom='burning, aching or shock-like pain in a limb that is gone — S1 reorganizes',
           fibro='fibromyalgia — tender points, stiffness, poor sleep, fatigue; no inflammation to find')
for k, s in TAG.items(): text(s, 1000, 1560, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('this drug is listed for this pain — it eases', 1000, 1600, 'nf-l1', 'middle', when=OK)
text('TENS — thought to work through the gate mechanism and endogenous opioids', 1000, 1640, 'nf-l2', 'middle', when=R('tens'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
EASE = m(OK, set=dict(pain=1), speed=0.6)
flows = [
  dict(d=NERVE, len=560, speed=130, r=9, base=dict(pain=2), unless=D('phantom'), mods=[m(D('neuro'), set=dict(pain=6)), EASE]),
  dict(d=CROSS, len=200, speed=130, r=9, base=dict(pain=2), unless=D('phantom'), mods=[m(D('neuro', 'fibro'), set=dict(pain=4)), EASE]),
  dict(d=UP, len=560, speed=130, r=9, base=dict(pain=2), unless=D('phantom'), mods=[m(D('neuro', 'fibro'), set=dict(pain=5)), EASE]),
  dict(d=CTX, len=320, speed=130, r=9, base=dict(pain=2), mods=[m(D('neuro', 'fibro', 'thal'), set=dict(pain=4)), EASE]),
  dict(d='M1200 620 C1300 500 1400 400 1450 330', len=360, speed=130, r=9, base=dict(pain=3), when=D('thal', 'phantom')),
  dict(d='M760 960 C800 1000 830 1030 850 1050', len=120, speed=80, r=8, base=dict(gate=3), when=R('tens')),
] + [dict(d=f'M{x} {y} C{(x + 1200) / 2:.0f} {y - 100} 1300 700 1260 320', len=900, speed=110, r=8, base=dict(pain=2), when=D('fibro'),
          mods=[EASE]) for x, y in ((1700, 500), (1900, 900))]
sites = [dict(x=560, y=1200, n=[-1, -1], w=10, t='rec', l='', aria='Neuropathic pain', c='neuropathicpain', ions=[]),
         dict(x=1080, y=1110, n=[1, 0], w=10, t='rec', l='', aria='Spinothalamic tract', c='stttract', ions=[]),
         dict(x=1290, y=560, n=[1, -1], w=10, t='rec', l='', aria='Thalamic pain syndrome', c='thalamicpain', ions=[]),
         dict(x=1520, y=300, n=[1, 0], w=10, t='rec', l='', aria='Phantom limb pain', c='phantomlimb', ions=[]),
         dict(x=1980, y=700, n=[1, 0], w=10, t='rec', l='', aria='Fibromyalgia', c='fibromyalgia', ions=[]),
         dict(x=740, y=940, n=[-1, -1], w=10, t='rec', l='', aria='TENS', c='estim', ions=[])]

readouts = [
  dict(l='Pain', mods=[dict(when=D('neuro', 'thal', 'phantom', 'fibro'), d=1), dict(when=OK, d=-1)]),
  dict(l='Spontaneous nerve firing', mods=[dict(when=D('neuro'), d=1)]),
  dict(l='Allodynia (light touch hurts)', mods=[dict(when=D('thal'), d=1)]),
  dict(l='Inflammatory markers', mods=[dict(when=D('fibro'), d=0)]),
]

notes = {
  '': 'Pain and temperature ride Aδ and C fibers to the dorsal horn; the second neuron crosses in the anterior white commissure '
      'within a segment or two and ascends to VPL; the third goes to the primary somatosensory cortex.',
  'dx:neuro': 'Neuropathic pain: dysfunction of the nerves themselves, carried by upregulated, persistently active voltage-gated '
              'Na⁺ channels — diabetic neuropathy, postherpetic neuralgia. Gabapentinoids, TCAs, topical capsaicin.',
  'dx:thal': 'Thalamic pain syndrome (Dejerine-Roussy): a thalamic lesion, perhaps a lenticulostriate occlusion — paresthesias '
             'first, then weeks to months later allodynia, hyperalgesia, dysesthesia on the opposite side; treatment-resistant.',
  'dx:phantom': 'Phantom limb pain: burning, aching or shock-like pain in an amputated limb, with reorganization of the primary '
                'somatosensory cortex.',
  'dx:fibro': 'Fibromyalgia: chronic widespread musculoskeletal pain (all four quadrants, ≥ 3 months), tender points, stiffness, '
              'poor sleep, fatigue; normal ESR and imaging. Exercise, TCAs, SNRIs (duloxetine, milnacipran), pregabalin.',
  'rx:tens': 'TENS fires nerve action potentials that alter sensory input — thought to act through the gate mechanism and by '
             'releasing endogenous opioids and cortisol. Not with pacemakers, arrhythmias, thrombosis or on a pregnant abdomen.',
}

dyn = dict(
  kinds=dict(pain=['mov', '--bad'], gate=['mov', '--accent']), groups=[['mov', 'Pain signal · TENS input']],
  switches=[dict(id='dx', label='Pain', type='one', options=[
              ['neuro', 'Peripheral neuropathic', 'neuropathicpain'], ['thal', 'Thalamic pain', 'thalamicpain'],
              ['phantom', 'Phantom limb', 'phantomlimb'], ['fibro', 'Fibromyalgia', 'fibromyalgia']]),
            dict(id='rx', label='Treatment', type='one', options=[
              ['gaba', 'Gabapentinoid', 'neuropathicpain'], ['tca', 'TCA', 'neuropathicpain'], ['snri', 'SNRI', 'fibromyalgia'],
              ['caps', 'Topical capsaicin', 'neuropathicpain'], ['tens', 'TENS', 'estim']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Fundamental Neuroscience ch 18')

MAP = dict(
  id='painsim', title='Pain Gone Wrong in Motion', topic='pharm', after='pain',
  sub='Send pain up the spinothalamic tract, then make it misfire — neuropathic Na⁺ channels, a thalamic stroke, a phantom limb, '
      'fibromyalgia — and treat each with the drug its card lists',
  w=3600, h=1900,
  fa='235, 477, 529',
  src=['Fundamental Neuroscience ch 18 — The Somatosensory System II: Nociception, Thermal Sense, and Touch',
       'Katzung ch 30 — Antidepressant Agents'],
  lanes=[('pwPath', 'Pathway', 'glycolysis'), ('pwDz', 'Pain syndromes', 'tca')],
  nodes=[
    ('pn1', 'Spinothalamic tract', 330, 1780, 'pwPath', 'cross in 1–2 segments', ['stttract'], 'hub'),
    ('pn2', 'Neuropathic pain', 760, 1780, 'pwDz', 'Na⁺ channels', ['neuropathicpain']),
    ('pn3', 'Thalamic pain syndrome', 1200, 1780, 'pwDz', 'contralateral allodynia', ['thalamicpain']),
    ('pn4', 'Phantom limb pain', 1640, 1780, 'pwDz', 'S1 reorganization', ['phantomlimb']),
    ('pn5', 'Fibromyalgia', 2080, 1780, 'pwDz', 'normal ESR', ['fibromyalgia']),
    ('pn6', 'Electrical stimulation & TENS', 2520, 1780, 'pwPath', 'gate mechanism', ['estim'])],
  panels=[
    (2500, PANY, 1000, 'Drug for each (Katzung ch 30)', [
      ('Neuropathic', 'gabapentinoid, TCA, capsaicin'), ('Fibromyalgia', 'exercise, TCA, SNRI, pregabalin'),
      ('Thalamic pain', 'treatment-resistant')])],
  dyn=dyn)
