# Stimulants & Addiction in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The reward pathway: a VTA dopamine neuron (nicotinic α4β2 receptors on it) projecting to the nucleus accumbens, a
# serotonin terminal with its transporter (SERT), and an adenosine A₂A receptor on a wake-promoting cell. A `drug` switch
# acts where its card says — nicotine (stimulates VTA nicotinic receptors), caffeine (blocks adenosine receptors), MDMA
# (reverses SERT, dumps serotonin; hyperthermia, hyponatremia) — with `phase` steps (use → withdrawal) and treatments
# (varenicline, nicotine replacement). A `stage` switch walks the stages of change. 5 readouts. Facts from the pinned cards;
# FA pages in `fa`. No new cards.
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

G = lambda *k: [f'drug:{x}' for x in k]
def GP(g, p): return [f'drug:{g}&phase:{p}']
PANY = 1180
VX, VY, AX, AY = 500, 980, 1100, 520

text('Stimulants & addiction — the reward pathway and what each drug does to it', 180, 150, 'dyn-big')
text('VTA dopamine neuron → nucleus accumbens · serotonin terminal · adenosine receptor · schematic', 180, 176, 'dyn-cap')

# ════════ VTA → NAc ════════
add(f'<circle cx="{VX}" cy="{VY}" r="80" style="fill:var(--dk4);fill-opacity:.2;stroke:var(--dk4);stroke-width:4"/>'); text('VTA dopamine neuron', VX, VY + 120, 'nf-l1', 'middle')
add(f'<path d="M{VX + 60} {VY - 60} C{VX + 250} {VY - 300} {AX - 250} {AY + 160} {AX - 70} {AY + 40}" style="fill:none;stroke:var(--dk4);stroke-width:10;opacity:.4"/>')
add(f'<ellipse cx="{AX}" cy="{AY}" rx="130" ry="90" style="fill:var(--dk9);fill-opacity:.12;stroke:var(--dk9);stroke-width:4"/>'); text('nucleus accumbens', AX, AY - 120, 'nf-l1', 'middle')
add(f'<ellipse cx="{AX}" cy="{AY}" rx="130" ry="90" style="fill:var(--accent);fill-opacity:.3"/>', when=['phase:use&drug:nic', 'phase:use&drug:mdma'])
for dx in (-50, 0, 50):
    add(f'<rect x="{VX + dx - 12}" y="{VY - 110}" width="24" height="34" rx="6" style="fill:var(--dk10);opacity:.7"/>')
text('nicotinic α4β2', VX - 90, VY - 120, 'nf-l2', 'end')
for dx in (-50, 0, 50):
    add(f'<rect x="{VX + dx - 12}" y="{VY - 110}" width="24" height="34" rx="6" style="fill:var(--accent)"/>', when=GP('nic', 'use'))
    add(f'<rect x="{VX + dx - 12}" y="{VY - 110}" width="24" height="34" rx="6" style="fill:var(--dk7)"/>', when=['drug:nic&rx'])
# serotonin terminal
SX, SY = 1400, 1000
add(f'<path d="M{SX - 140} {SY - 60} H{SX + 40} V{SY + 60} H{SX - 140}" style="fill:var(--dk7);fill-opacity:.12;stroke:var(--dk7);stroke-width:4"/>'); text('serotonin terminal', SX - 50, SY - 90, 'nf-l1', 'middle')
add(f'<rect x="{SX + 20}" y="{SY - 20}" width="40" height="40" rx="8" style="fill:var(--dk9);opacity:.6"/>'); text('SERT', SX + 80, SY + 6, 'nf-l2')
add(f'<rect x="{SX + 20}" y="{SY - 20}" width="40" height="40" rx="8" style="fill:var(--bad)"/>', when=GP('mdma', 'use'))
# adenosine
DX, DY = 1900, 520
add(f'<circle cx="{DX}" cy="{DY}" r="80" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:4"/>'); text('wake / sleep cell', DX, DY + 120, 'nf-l1', 'middle')
add(f'<rect x="{DX - 100}" y="{DY - 20}" width="30" height="40" rx="8" style="fill:var(--dk5);opacity:.7"/>'); text('A₂A', DX - 120, DY - 30, 'nf-l2', 'end')
add(f'<rect x="{DX - 100}" y="{DY - 20}" width="30" height="40" rx="8" style="fill:var(--bad)"/>', when=GP('caf', 'use'))
add(f'<path d="M{DX - 110} {DY - 30} l50 60 M{DX - 60} {DY - 30} l-50 60" class="nf-x"/>', when=GP('caf', 'use'))
TAG = {('nic', 'use'): 'nicotine stimulates VTA nicotinic receptors → dopamine in the accumbens · restlessness',
       ('nic', 'wd'): 'nicotine withdrawal — irritable, anxious, restless, poor focus, hungry (weight gain), craving',
       ('caf', 'use'): 'caffeine blocks adenosine receptors → awake · palpitations, tremor, insomnia; blunts adenosine for SVT',
       ('caf', 'wd'): 'caffeine withdrawal — headache, poor concentration, fatigue',
       ('mdma', 'use'): 'MDMA reverses SERT — serotonin floods out · euphoria, bruxism, thirst; hyperthermia, hyponatremia, serotonin syndrome',
       ('mdma', 'wd'): 'after MDMA — depression, fatigue, poor concentration'}
for (g, p), s in TAG.items(): text(s, 1200, 1400, 'nf-l1 dyn-tag', 'middle', when=GP(g, p))
text('varenicline (α4β2 partial agonist) or nicotine replacement blunts reward and withdrawal · or bupropion', 1200, 1440, 'nf-l1', 'middle', when=['drug:nic&rx'])
text('MDMA care: cooling, fluids guided by sodium, benzodiazepines', 1200, 1440, 'nf-l1', 'middle', when=['drug:mdma&rx'])
text('caffeine: taper', 1200, 1440, 'nf-l1', 'middle', when=['drug:caf&rx'])
ST = dict(pre='precontemplation — denies a problem: raise awareness', con='contemplation — ambivalent: weigh pros and cons',
          prep='preparation — committed: help make the plan', act='action — changing: support coping with triggers',
          maint='maintenance — sustained: plan for relapse (common, not failure)')
for k, s in ST.items(): text(s, 1200, 1500, 'nf-l1', 'middle', when=[f'stage:{k}'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{VX + 60} {VY - 60} C{VX + 250} {VY - 300} {AX - 250} {AY + 160} {AX - 70} {AY + 40}', len=900, speed=110, r=9, base=dict(da=2),
       mods=[m(GP('nic', 'use') + GP('mdma', 'use'), set=dict(da=6), speed=1.6), m(GP('nic', 'wd'), set=dict(da=1)), m(['drug:nic&rx'], set=dict(da=2), speed=1)]),
  dict(d=f'M{SX + 40} {SY} H{SX + 260}', len=220, speed=60, r=9, base=dict(ser=1), mods=[m(GP('mdma', 'use'), set=dict(ser=7), speed=2)]),
  dict(d=f'M{SX + 260} {SY + 30} H{SX + 60}', len=200, speed=60, r=8, base=dict(ser=2), unless=GP('mdma', 'use')),
  dict(d=f'M{DX - 260} {DY} H{DX - 110}', len=150, speed=60, r=9, base=dict(ado=3), mods=[m(GP('caf', 'use'), set=dict(ado=1))]),
]
sites = [dict(x=VX - 110, y=VY, n=[-1, 0], w=10, t='rec', l='', aria='Nicotine', c='nicotine', ions=[]),
         dict(x=DX + 100, y=DY, n=[1, 0], w=10, t='rec', l='', aria='Caffeine', c='caffeine', ions=[]),
         dict(x=SX - 160, y=SY, n=[-1, 0], w=10, t='rec', l='', aria='MDMA', c='mdma', ions=[]),
         dict(x=AX + 150, y=AY, n=[1, 0], w=10, t='rec', l='', aria='Substance use disorder', c='sud', ions=[]),
         dict(x=AX - 150, y=AY - 60, n=[-1, -1], w=10, t='rec', l='', aria='Gambling disorder', c='gambling', ions=[]),
         dict(x=600, y=1320, n=[-1, 1], w=10, t='rec', l='', aria='Stages of change', c='stageschange', ions=[]),
         dict(x=VX + 120, y=VY + 60, n=[1, 1], w=10, t='rec', l='', aria='Neonatal abstinence', c='nas', ions=[])]

readouts = [
  dict(l='Accumbens dopamine', mods=[dict(when=GP('nic', 'use') + GP('mdma', 'use'), d=1), dict(when=GP('nic', 'wd'), d=-1)]),
  dict(l='Synaptic serotonin', mods=[dict(when=GP('mdma', 'use'), d=1), dict(when=GP('mdma', 'wd'), d=-1)]),
  dict(l='Wakefulness', mods=[dict(when=GP('caf', 'use'), d=1), dict(when=GP('caf', 'wd'), d=-1)]),
  dict(l='Craving', mods=[dict(when=GP('nic', 'wd'), d=1), dict(when=['drug:nic&rx&phase:wd'], d=-1)]),
  dict(l='Serum sodium', mods=[dict(when=GP('mdma', 'use'), d=-1)]),
]

notes = {
  '': 'Every addictive drug raises dopamine in the nucleus accumbens — by stimulating VTA neurons (nicotine), blocking or reversing '
      'transporters, or disinhibiting them. Repeated surges remodel synapses into compulsive use. Gambling is the one '
      'non-substance addiction in DSM-5.',
  'drug:nic': 'Nicotine: α4β2 nicotinic agonist on VTA dopamine neurons; mild withdrawal but highly addictive, relapse common. '
              'Smoking, not nicotine, causes most harm. Patch + gum or lozenge; varenicline; bupropion.',
  'drug:caf': 'Caffeine: adenosine (A₂A) receptor antagonist — promotes wakefulness; blunts adenosine given for SVT. Theophylline '
              'is a related methylxanthine.',
  'drug:mdma': 'MDMA: reverses SERT (more than DAT, NET) — euphoria, empathy, bruxism, mydriasis, thirst; hyperthermia, '
               'hyponatremia, hypertension, serotonin syndrome, seizures. Afterward depression and fatigue.',
  'rx': 'Treatment from each card: nicotine — replacement, varenicline, bupropion; caffeine — taper; MDMA — cooling, sodium-guided '
        'fluids, benzodiazepines.',
  'stage:pre': 'Precontemplation: denies a problem — raise awareness, link risks to the patient’s own priorities.',
  'stage:con': 'Contemplation: ambivalent — weigh pros and cons (“I know I drink too much but…”).',
  'stage:prep': 'Preparation: committed — help make the plan.', 'stage:act': 'Action: changing — support self-efficacy and coping with triggers.',
  'stage:maint': 'Maintenance: sustained — reinforce and plan for relapse, which is common and not failure.',
}

dyn = dict(
  kinds=dict(da=['mov', '--dk4'], ser=['mov', '--dk7'], ado=['mov', '--dk5']), groups=[['mov', 'Dopamine · serotonin · adenosine']],
  switches=[dict(id='drug', label='Drug', type='one', options=[['nic', 'Nicotine', 'nicotine'], ['caf', 'Caffeine', 'caffeine'], ['mdma', 'MDMA', 'mdma']]),
            dict(id='phase', label='Phase', type='steps', auto=3, options=[['use', 'Using'], ['wd', 'Withdrawal / after']]),
            dict(id='rx', label='Treat', type='toggle', on='Treatment given', off='Give the treatment', def_=False),
            dict(id='stage', label='Stage of change', type='one', options=[
              ['pre', 'Precontemplation', 'stageschange'], ['con', 'Contemplation', 'stageschange'], ['prep', 'Preparation', 'stageschange'],
              ['act', 'Action', 'stageschange'], ['maint', 'Maintenance', 'stageschange']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Kaplan & Sadock ch 4')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='stimsim', title='Stimulants & Addiction in Motion', topic='behav', after='substance',
  sub='Watch nicotine fire the VTA, caffeine block adenosine and MDMA reverse SERT — through use and withdrawal — then treat, and walk a '
      'patient through the stages of change',
  w=3600, h=1900,
  fa='585, 586, 589, 594, 633',
  src=['Kaplan & Sadock ch 4 — Substance Use and Addictive Disorders', 'Katzung ch 32 — Drugs of Abuse'],
  lanes=[('stDrug', 'Stimulants', 'tca'), ('stRec', 'Addiction & recovery', 'glycolysis')],
  nodes=[
    ('sm1', 'Nicotine', 330, 1720, 'stDrug', 'α4β2 · varenicline', ['nicotine'], 'hub'),
    ('sm2', 'Caffeine', 760, 1720, 'stDrug', 'adenosine block', ['caffeine']),
    ('sm3', 'MDMA', 1200, 1720, 'stDrug', 'SERT reversal · Na⁺', ['mdma']),
    ('sm4', 'Substance use disorder', 1640, 1720, 'stRec', 'accumbens dopamine', ['sud']),
    ('sm5', 'Stages of change', 2080, 1720, 'stRec', 'motivational interviewing', ['stageschange']),
    ('sm6', 'Gambling disorder', 2520, 1720, 'stRec', 'behavioral addiction', ['gambling']),
    ('sm7', 'Neonatal abstinence', 2960, 1720, 'stRec', 'opioid withdrawal', ['nas'])],
  panels=[
    (2500, PANY, 1000, 'Target of each (Katzung ch 32)', [
      ('Nicotine', 'nicotinic α4β2 on VTA'), ('Caffeine', 'adenosine receptors'), ('MDMA', 'SERT, reversed')])],
  dyn=dyn)
