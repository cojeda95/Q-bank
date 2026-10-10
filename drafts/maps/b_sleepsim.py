# Sleep Stages in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Top: the EEG of the current stage drawn as a wave (beta, alpha, theta, spindles + K complexes, delta, REM) with what
# happens in that stage, stepping by itself (`steps`, auto). Bottom: a night's hypnogram (11 pm → 7 am) with a dot
# walking through it; a `one` switch redraws the night for depression, narcolepsy, alcohol/benzodiazepines or aging.
# The hypnograms are schematic (the cards give directions, not minutes) and the map says so. 4 readouts. Facts from
# the pinned cards (sleepstages, narcolepsy, parasomnias, rbd, insomnia, mdd); FA pages in `fa`. No new cards.
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


import math
ST = 'stg'
S = lambda *k: [f'{ST}:{x}' for x in k]
W = lambda *k: [f'who:{x}' for x in k]
PANY = 800

# ════════ the EEG ════════
box(160, 130, 2340, 640)
text('The EEG — what each stage looks like', 190, 170, 'dyn-big')
text('At night, BATS Drink Blood: beta, alpha, theta, spindles, delta, beta-like REM', 190, 196, 'dyn-cap')
def wave(freq, amp, x0=260, x1=1500, y=420, spindle=False, kcx=False):
    pts = []
    for i in range(0, x1 - x0, 3):
        t = i / 100
        a = amp
        if spindle and 380 < i < 560: a = amp * 2.6 * math.sin(math.pi * (i - 380) / 180) + amp
        v = a * math.sin(2 * math.pi * freq * t)
        if kcx and 820 < i < 940: v += -90 * math.sin(math.pi * (i - 820) / 120) * (1 if i < 880 else -0.6)
        pts.append(f'{x0 + i} {y - v:.0f}')
    return 'M' + ' L'.join(pts)
EEG = dict(
  aw=(wave(6.0, 14), 'Awake, eyes open — beta', 'fast, low-voltage'),
  ac=(wave(3.2, 26), 'Awake, eyes closed — alpha', 'relaxed, about to fall asleep'),
  n1=(wave(2.0, 36), 'N1 — theta', 'light sleep · 5% of the night'),
  n2=(wave(2.4, 28, spindle=True, kcx=True), 'N2 — sleep spindles and K complexes', '45% of the night · teeth grinding (bruxism)'),
  n3=(wave(0.6, 95), 'N3 — delta', 'slow-wave, deepest · 25% · sleepwalking, night terrors, bedwetting'),
  rem=(wave(5.0, 18), 'REM — beta-like', '25% · atonia except diaphragm and eye muscles · dreams, nightmares'),
)
for k, (d, a, b) in EEG.items():
    add(f'<path d="{d}" style="fill:none;stroke:var(--dk9);stroke-width:4"/>', when=S(k))
    text(a, 1580, 380, 'dyn-big', when=S(k)); text(b, 1580, 412, 'nf-l2', when=S(k))
text('one cycle ≈ 90 minutes · 4–6 cycles a night · REM lengthens toward morning', 1580, 560, 'nf-l2')
text('darkness → suprachiasmatic nucleus → pineal melatonin', 1580, 590, 'nf-l2')

# ════════ the night ════════
box(160, 680, 2340, 1320)
text('One night — the hypnogram', 190, 720, 'dyn-big')
text('schematic: the shapes follow the directions on the cards, not measured minutes', 190, 746, 'dyn-cap')
GX0, GX1 = 380, 2200
LVL = dict(W=820, R=900, N1=980, N2=1060, N3=1160)
for k, lab in (('W', 'Awake'), ('R', 'REM'), ('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3')):
    add(f'<path d="M{GX0} {LVL[k]} H{GX1}" style="stroke:var(--line-2);stroke-width:2;stroke-dasharray:4 8"/>')
    text(lab, GX0 - 20, LVL[k] + 5, 'nf-l1', 'end')
for h, lab in enumerate(['11 pm', '12', '1', '2', '3', '4', '5', '6', '7 am']):
    x = GX0 + h * (GX1 - GX0) / 8
    text(lab, round(x), 1220, 'nf-l2', 'middle')
hx = lambda hr: round(GX0 + hr * (GX1 - GX0) / 8)
def gram(seq):
    """seq: [(hours from 11 pm, level), …] — a step path"""
    d, ln, px, py = '', 0, None, None
    for hr, lv in seq:
        x, y = hx(hr), LVL[lv]
        if px is None: d = f'M{x} {y}'
        else:
            d += f' H{x} V{y}'; ln += abs(x - px) + abs(y - py)
        px, py = x, y
    return d, ln
# five cycles: N3 early, REM growing toward morning
NORMAL = [(0, 'W'), (0.25, 'N1'), (0.4, 'N2'), (0.7, 'N3'), (1.2, 'N2'), (1.35, 'R'), (1.5, 'N2'), (1.9, 'N3'), (2.3, 'N2'), (2.75, 'R'), (3.0, 'N2'),
          (3.6, 'N3'), (3.8, 'N2'), (4.4, 'R'), (4.8, 'N2'), (5.7, 'R'), (6.2, 'N2'), (6.9, 'R'), (7.6, 'W'), (8, 'W')]
DEP = [(0, 'W'), (0.3, 'N1'), (0.45, 'N2'), (0.8, 'R'), (1.3, 'N2'), (1.9, 'N3'), (2.1, 'N2'), (2.6, 'R'), (3.2, 'N2'), (4.0, 'R'), (4.7, 'N2'), (5.2, 'R'),
       (6.0, 'W'), (8, 'W')]
NARC = [(0, 'W'), (0.1, 'R'), (0.5, 'N2'), (0.8, 'N3'), (1.2, 'N2'), (1.5, 'R'), (1.9, 'W'), (2.1, 'N2'), (2.8, 'R'), (3.2, 'N2'), (3.9, 'W'), (4.1, 'R'),
        (4.6, 'N2'), (5.4, 'R'), (6.0, 'W'), (6.3, 'N2'), (7.0, 'R'), (7.6, 'W'), (8, 'W')]
ALC = [(0, 'W'), (0.2, 'N1'), (0.3, 'N2'), (1.6, 'N2'), (1.8, 'N3'), (2.0, 'N2'), (4.0, 'N2'), (4.3, 'R'), (4.5, 'N2'), (6.0, 'N2'), (6.3, 'R'), (6.6, 'N1'),
       (7.0, 'W'), (8, 'W')]
AGE = [(0, 'W'), (0.8, 'N1'), (1.0, 'N2'), (1.5, 'N3'), (1.7, 'N2'), (2.2, 'R'), (2.4, 'N2'), (3.2, 'W'), (3.4, 'N2'), (4.2, 'R'), (4.5, 'N2'), (5.6, 'R'),
       (5.9, 'W'), (8, 'W')]
GR = dict(nl=NORMAL, dep=DEP, narc=NARC, alc=ALC, age=AGE)
flows = []
for k, seq in GR.items():
    d, ln = gram(seq)
    cond = W(k) if k != 'nl' else ['!who:*']
    add(f'<path d="{d}" style="fill:none;stroke:var(--dk11);stroke-width:5;stroke-linejoin:round"/>', when=cond)
    flows.append(dict(d=d, len=ln, speed=160, r=10, base=dict(you=1), when=cond))
TAG = dict(dep='REM comes early (short REM latency), less N3, more REM, early-morning waking',
           narc='REM within minutes of falling asleep — sleep-onset REM; sleep and REM intrude into the day',
           alc='less N3 and less REM', age='longer to fall asleep, less N3 and REM, early waking')
for k, t in TAG.items():
    text(t, 190, 1290, 'nf-l1 dyn-tag', when=W(k))
text('normal: N3 early in the night, REM periods lengthening toward morning', 190, 1290, 'nf-l1', unless=['who:*'])

sites = [dict(x=hx(0.7), y=LVL['N3'], n=[0, 1], w=10, t='rec', l='', aria='Slow-wave sleep — parasomnias', c='parasomnias', ions=[]),
         dict(x=1500, y=420, n=[1, 0], w=10, t='rec', l='', aria='Sleep stages and EEG', c='sleepstages', ions=[])]

readouts = [
  dict(l='REM latency', mods=[dict(when=W('dep', 'narc'), d=-1)]),
  dict(l='N3 (slow-wave sleep)', mods=[dict(when=W('dep', 'alc', 'age'), d=-1)]),
  dict(l='REM sleep', mods=[dict(when=W('dep'), d=1), dict(when=W('alc', 'age'), d=-1)]),
  dict(l='Time to fall asleep', mods=[dict(when=W('age'), d=1), dict(when=W('narc'), d=-1)]),
]

notes = {
  '': 'Sleep runs in 4–6 cycles of about 90 minutes: down through N1 and N2 to slow-wave N3, then REM. N3 dominates early in the '
      'night; REM periods lengthen toward morning.',
  'stg:aw': 'Awake with eyes open: fast, low-voltage beta waves.',
  'stg:ac': 'Awake with eyes closed: alpha waves.',
  'stg:n1': 'N1, about 5% of the night: theta waves — light sleep.',
  'stg:n2': 'N2, about 45%: sleep spindles and K complexes. Bruxism (teeth grinding) happens here.',
  'stg:n3': 'N3, about 25%: delta waves, the deepest sleep. Sleepwalking, night terrors and bedwetting arise here — and leave no '
            'memory.',
  'stg:rem': 'REM, about 25%: a beta-like EEG with atonia of everything but the diaphragm and eye muscles; dreams and nightmares '
             '(remembered), penile and clitoral tumescence.',
  'who:dep': 'Depression: REM comes early (short REM latency), N3 falls, REM rises, and the patient wakes early in the morning.',
  'who:narc': 'Narcolepsy: orexin (hypocretin) neurons are lost, so the patient falls straight into REM — very short REM latency, '
              'cataplexy, hypnagogic hallucinations, sleep paralysis.',
  'who:alc': 'Alcohol, benzodiazepines and barbiturates reduce N3 and REM.',
  'who:age': 'Aging: less N3 and REM, a longer time to fall asleep, and early waking.',
}

dyn = dict(
  kinds=dict(you=['you', '--accent']), groups=[['you', 'The sleeper']],
  switches=[dict(id=ST, label='EEG stage', type='steps', auto=3, options=[['aw', 'Awake, eyes open'], ['ac', 'Awake, eyes closed'], ['n1', 'N1'],
                                                                             ['n2', 'N2'], ['n3', 'N3'], ['rem', 'REM']]),
            dict(id='who', label='Whose night?', type='one', options=[['dep', 'Depression', 'mdd'], ['narc', 'Narcolepsy', 'narcolepsy'],
                                                                      ['alc', 'Alcohol · benzodiazepines', 'sleepstages'], ['age', 'Aging', 'sleepstages']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 507, 578, 585 · Kaplan & Sadock ch 15')

MAP = dict(
  id='sleepsim', title='Sleep Stages in Motion', topic='behav', after='sleepdev',
  sub='Step through the EEG of each sleep stage and what happens in it, then watch a night’s hypnogram — and how depression, '
      'narcolepsy, alcohol and aging reshape it. The readouts give REM latency, slow-wave sleep, REM and time to fall asleep',
  w=3500, h=1640,
  fa='507–508, 562, 578, 585, 697',
  src=[full('Kaplan & Sadock', 15), full('Kaplan & Sadock', 7)],
  lanes=[('slStage', 'Sleep stages', 'glycolysis'), ('slDz', 'Sleep disorders', 'tca'), ('slShift', 'What shifts the night', 'gluconeo')],
  nodes=[
    ('sl1', 'Sleep stages & EEG waves', 330, 1420, 'slStage', 'BATS Drink Blood', ['sleepstages'], 'hub'),
    ('sl2', 'Narcolepsy', 760, 1420, 'slDz', 'orexin lost', ['narcolepsy']),
    ('sl3', 'Parasomnias', 1160, 1420, 'slDz', 'N3 vs REM', ['parasomnias', 'rbd']),
    ('sl4', 'Insomnia · sleep apnea', 1580, 1420, 'slDz', 'hypnotics · OSA', ['insomnia', 'sleepapnea']),
    ('sl5', 'Depression', 330, 1550, 'slShift', 'short REM latency', ['mdd']),
    ('sl6', 'Circadian · enuresis', 760, 1550, 'slShift', 'timing · N3', ['circadian', 'enuresis'])],
  panels=[
    (2420, PANY, 1000, 'Stage → event (First Aid p. 507)', [
      ('N2', 'bruxism'),
      ('N3', 'sleepwalking, night terrors, bedwetting'),
      ('REM', 'dreams, nightmares, tumescence'),
      ('N3 + REM ↓', 'alcohol, benzodiazepines, aging'),
      ('REM latency ↓', 'depression, narcolepsy')])],
  dyn=dyn)
