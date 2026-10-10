# Headaches in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A side view of the head, face to the left: cortex, meningeal vessels with trigeminal (V1) afferents, the trigeminal
# ganglion and its V1/V2/V3 branches, eye and nose, and an artery looping against the CN V root. A `one` switch picks the
# headache — migraine (with `ph` steps: aura as a spreading cortical wave → CGRP/substance P release → throbbing pain),
# tension-type (a band), cluster (periorbital pain with same-side tearing and rhinorrhea) or trigeminal neuralgia (shocks
# down V2/V3) — and a second `one` switch gives a drug; it works only where its card names it for that headache. The site of
# aura onset is not drawn — the card does not give it. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
PANY = 1180
WORKS = dict(migraine=('nsaid', 'triptan', 'cgrpab'), tension=('nsaid',), cluster=('o2', 'triptan', 'verapamil'), tn=('carba',))
OK = [f'dx:{d}&rx:{r}' for d, rs in WORKS.items() for r in rs]
OKP = [f'dx:{d}&rx:{r}' + ('&ph:pain' if d == 'migraine' else '') for d, rs in WORKS.items() for r in rs]

text('Headaches — migraine, tension, cluster and trigeminal neuralgia', 180, 150, 'dyn-big')
text('side view, face to the left · trigeminal nerve in purple', 180, 176, 'dyn-cap')

# ════════ head ════════
add('<path d="M1000 260 C1300 260 1460 480 1440 760 C1420 1000 1260 1140 1120 1180 L1100 1400 H820 L800 1200 C700 1180 640 1120 600 1060 '
    'C560 1000 600 960 580 930 C540 900 520 860 540 820 C500 780 480 740 540 720 C560 600 560 560 600 480 C680 330 820 260 1000 260 Z" '
    'style="fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:5"/>')
add('<path d="M680 520 C760 360 1000 320 1180 380 C1340 440 1400 600 1380 760" style="fill:none;stroke:var(--dk4);stroke-width:34;opacity:.2;stroke-linecap:round"/>')
text('cortex', 1300, 460, 'nf-l2')
add('<path d="M720 470 C820 380 980 360 1100 400" style="fill:none;stroke:var(--nf-blood);stroke-width:12;opacity:.45"/>', unless=D('migraine'))
add('<path d="M720 470 C820 380 980 360 1100 400" style="fill:none;stroke:var(--nf-blood);stroke-width:22;opacity:.7"/>', when=['dx:migraine&ph:pain'])
add('<path d="M720 470 C820 380 980 360 1100 400" style="fill:none;stroke:var(--nf-blood);stroke-width:12;opacity:.45"/>', when=['dx:migraine&!ph:pain'])
text('meningeal vessels', 1110, 390, 'nf-l2')
add('<circle cx="920" cy="860" r="34" style="fill:var(--dk7);fill-opacity:.35;stroke:var(--dk7);stroke-width:4"/>'); text('trigeminal ganglion', 960, 920, 'nf-l2')
add('<path d="M920 860 C860 760 780 620 720 470" style="fill:none;stroke:var(--dk7);stroke-width:6"/>'); text('V1', 790, 600, 'nf-l1')
add('<path d="M920 860 C820 840 700 830 600 820" style="fill:none;stroke:var(--dk7);stroke-width:6"/>'); text('V2', 700, 810, 'nf-l1')
add('<path d="M920 860 C840 930 740 990 640 1020" style="fill:none;stroke:var(--dk7);stroke-width:6"/>'); text('V3', 740, 1010, 'nf-l1')
add('<path d="M920 860 H1060" style="stroke:var(--dk7);stroke-width:10"/>'); text('CN V root', 1080, 850, 'nf-l2')
add('<path d="M1000 820 c40 20 40 60 0 80" style="fill:none;stroke:var(--nf-blood);stroke-width:12"/>', when=D('tn'))
add('<ellipse cx="640" cy="650" rx="44" ry="26" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>'); text('eye', 640, 610, 'nf-l2', 'middle')
add('<ellipse cx="640" cy="650" rx="70" ry="50" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('cluster'))
add('<path d="M560 330 C700 230 1300 230 1440 420" style="fill:none;stroke:var(--bad);stroke-width:26;opacity:.5"/>', when=D('tension'))
add('<path d="M560 600 C700 560 1300 560 1440 640" style="fill:none;stroke:var(--bad);stroke-width:14;opacity:.35;stroke-dasharray:14 10"/>', when=D('tension'))
for x, y in ((820, 520), (960, 450), (1120, 470), (1260, 560)):
    add(f'<circle cx="{x}" cy="{y}" r="30" style="fill:var(--accent);fill-opacity:.35"/>', when=['dx:migraine&ph:aura'])
TAG = dict(migraine='POUND — pulsatile, 4–72 h, unilateral, nausea, disabling · photophobia, phonophobia',
           tension='bilateral band-like pressure, 30 min to days · no nausea, no aura',
           cluster='excruciating periorbital pain 15 min–3 h · same-side tearing, rhinorrhea, red eye, ± Horner',
           tn='seconds-long electric shocks in V2/V3 — triggered by touch, chewing, brushing teeth')
for k, s in TAG.items(): text(s, 1000, 1500, 'nf-l1 dyn-tag', 'middle', when=D(k))
PH = dict(aura='aura — a wave of cortical spreading depression (zigzags, scintillating scotoma)',
          pain='trigeminal afferents release CGRP and substance P → neurogenic inflammation → throbbing pain')
for k, s in PH.items(): text(s, 1000, 1540, 'nf-l1', 'middle', when=[f'dx:migraine&ph:{k}'])
text('works for this headache', 1000, 1580, 'nf-l1', 'middle', when=OK)
text('not this drug’s card indication for this headache', 1000, 1580, 'nf-l2', 'middle', when=['rx:*&dx:*'], unless=OK)

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
STOP = lambda d: m([f'dx:{d}&rx:{r}' for r in WORKS[d]], set=dict(pain=0))
flows = [
  dict(d='M760 500 C900 380 1100 380 1260 470 C1340 540 1380 640 1380 760', len=1000, speed=60, r=10, base=dict(wave=3), when=['dx:migraine&ph:aura']),
  dict(d='M740 500 C800 460 860 430 920 410', len=220, speed=70, r=8, base=dict(cgrp=4), when=['dx:migraine&ph:pain'],
       mods=[m(['dx:migraine&rx:cgrpab'], set=dict(cgrp=0))]),
  dict(d='M720 470 C780 620 860 760 920 860', len=440, speed=120, r=9, base=dict(pain=3), when=['dx:migraine&ph:pain'], mods=[STOP('migraine')]),
  dict(d='M640 650 C760 700 860 800 920 860', len=360, speed=140, r=9, base=dict(pain=4), when=D('cluster'), mods=[STOP('cluster')]),
  dict(d='M610 680 C600 720 590 760 580 800', len=130, speed=50, r=8, base=dict(tear=3), when=D('cluster'), mods=[STOP('cluster')]),
  dict(d='M560 330 C700 230 1300 230 1440 420', len=1000, speed=40, r=9, base=dict(pain=4), when=D('tension'), mods=[STOP('tension')]),
  dict(d='M1000 860 H920 C820 840 700 830 600 820', len=420, speed=260, r=9, base=dict(pain=4), when=D('tn'), mods=[STOP('tn')]),
  dict(d='M920 860 C840 930 740 990 640 1020', len=330, speed=260, r=9, base=dict(pain=3), when=D('tn'), mods=[STOP('tn')]),
]
sites = [dict(x=1180, y=330, n=[1, -1], w=10, t='rec', l='', aria='Migraine', c='migraine', ions=[]),
         dict(x=1460, y=420, n=[1, 0], w=10, t='rec', l='', aria='Tension-type headache', c='tensionha', ions=[]),
         dict(x=560, y=620, n=[-1, 0], w=10, t='rec', l='', aria='Cluster headache', c='clusterha', ions=[]),
         dict(x=1110, y=800, n=[1, -1], w=10, t='rec', l='', aria='Trigeminal neuralgia', c='trigeminal', ions=[])]

readouts = [
  dict(l='Pain', mods=[dict(when=['dx:migraine&ph:pain'] + D('tension', 'cluster', 'tn'), d=1), dict(when=OKP, d=-1)]),
  dict(l='Aura', mods=[dict(when=['dx:migraine&ph:aura'], d=1)]),
  dict(l='Same-side autonomic signs', mods=[dict(when=D('cluster'), d=1), dict(when=['dx:cluster&rx:o2', 'dx:cluster&rx:triptan', 'dx:cluster&rx:verapamil'], d=-1)]),
  dict(l='Nausea', mods=[dict(when=['dx:migraine&ph:pain'], d=1)]),
]

notes = {
  '': 'Pick a headache. Migraine runs through its phases; the others show where the pain comes from. Then give a drug — it '
      'works only where its card lists it for that headache.',
  'dx:migraine': 'Migraine: trigeminal afferents to meningeal vessels release CGRP and substance P → neurogenic inflammation and '
                 'throbbing pain; aura is cortical spreading depression. Women, family history; triggers: sleep loss, menses, '
                 'stress, foods. Exclude medication overuse, SAH, GCA, mass.',
  'dx:tension': 'Tension-type: the commonest primary headache — steady, band-like, bilateral, 30 min to days; no nausea, no aura, '
                'at most one of photo- or phonophobia.',
  'dx:cluster': 'Cluster: men; excruciating periorbital pain 15 min–3 h in repeated attacks, with same-side lacrimation, '
                'rhinorrhea, conjunctival injection, sometimes Horner.',
  'dx:tn': 'Trigeminal neuralgia: an aberrant artery presses on the CN V root and demyelinates it, so touch fires pain fibers — '
           'seconds-long shocks in V2/V3, normal exam between attacks.',
  'rx:nsaid': 'NSAIDs: acute treatment for migraine and tension-type headache.',
  'rx:triptan': 'Triptans (5-HT₁B/₁D agonists): acute migraine and cluster (sumatriptan) — avoid in coronary disease.',
  'rx:cgrpab': 'Anti-CGRP antibodies: migraine prevention (with β-blockers, amitriptyline, topiramate, valproate, botulinum toxin).',
  'rx:o2': '100% oxygen: acute cluster headache.',
  'rx:verapamil': 'Verapamil: cluster prevention.',
  'rx:carba': 'Carbamazepine or oxcarbazepine: trigeminal neuralgia.',
}

dyn = dict(
  kinds=dict(wave=['mov', '--accent'], cgrp=['mov', '--dk9'], pain=['mov', '--bad'], tear=['mov', '--nf-h2o']),
  groups=[['mov', 'Aura wave · CGRP · pain · tears']],
  switches=[dict(id='dx', label='Headache', type='one', options=[
              ['migraine', 'Migraine', 'migraine'], ['tension', 'Tension-type', 'tensionha'], ['cluster', 'Cluster', 'clusterha'],
              ['tn', 'Trigeminal neuralgia', 'trigeminal']]),
            dict(id='ph', label='Migraine phase', type='steps', auto=3, options=[['aura', 'Aura'], ['pain', 'Headache']]),
            dict(id='rx', label='Drug', type='one', options=[
              ['nsaid', 'NSAID', 'migraine'], ['triptan', 'Triptan', 'migraine'], ['cgrpab', 'Anti-CGRP antibody', 'migraine'],
              ['o2', '100% O₂', 'clusterha'], ['verapamil', 'Verapamil', 'clusterha'], ['carba', 'Carbamazepine', 'trigeminal']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Katzung ch 16')

MAP = dict(
  id='hasim', title='Headaches in Motion', topic='neuro', after='seizhead',
  sub='Run a migraine from aura to CGRP-driven pain, tighten a tension band, fire a cluster attack and a trigeminal shock — '
      'then give each its drug',
  w=3600, h=1900,
  fa='532',
  src=['Katzung ch 16 — Histamine, Serotonin, Anti-Obesity Drugs, & the Ergot Alkaloids', 'Moore ch 9 — Head'],
  lanes=[('haPri', 'Primary headaches', 'tca'), ('haNeur', 'Neuralgia', 'glycolysis')],
  nodes=[
    ('ha1', 'Migraine', 330, 1760, 'haPri', 'CGRP · aura', ['migraine'], 'hub'),
    ('ha2', 'Tension-type headache', 760, 1760, 'haPri', 'band · bilateral', ['tensionha']),
    ('ha3', 'Cluster headache', 1200, 1760, 'haPri', 'periorbital · O₂', ['clusterha']),
    ('ha4', 'Trigeminal neuralgia', 1640, 1760, 'haNeur', 'V2/V3 · carbamazepine', ['trigeminal'])],
  panels=[
    (2500, PANY, 1000, 'Drug for each (Katzung ch 16)', [
      ('Migraine', 'NSAID, triptan · prevent: anti-CGRP, β-blocker'), ('Tension-type', 'NSAID, acetaminophen'),
      ('Cluster', '100% O₂, sumatriptan · prevent: verapamil'), ('Trigeminal neuralgia', 'carbamazepine')])],
  dyn=dyn)
