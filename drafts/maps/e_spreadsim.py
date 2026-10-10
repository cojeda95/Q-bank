# Seizure Spread in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A top view of both hemispheres with the thalamus, a medial temporal focus and an EEG strip. `ph` (steps, auto) runs a
# seizure through aura → ictal → postictal. A `one` switch picks the type: focal aware (stays put), focal impaired awareness
# (spreads within the hemisphere), secondarily generalized (crosses to both), absence (both hemispheres at once from the
# thalamus, 3 Hz, no postictal phase), status epilepticus (never stops) and psychogenic nonepileptic events (no discharge,
# normal EEG). A second `one` switch lists causes by age, febrile seizures included. The EEG traces are schematic. 3 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
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

T = lambda *k: [f'ty:{x}' for x in k]
def TP(t, *p): return [f'ty:{t}&ph:{x}' for x in p]
PANY = 1180
FX, FY = 700, 840

text('Seizure spread — where it starts, how far it goes, and what is left after', 180, 150, 'dyn-big')
text('top view, front at the top, patient’s left on your left · EEG below is schematic', 180, 176, 'dyn-cap')

# ════════ brain ════════
add('<ellipse cx="850" cy="700" rx="260" ry="400" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:5"/>')
add('<ellipse cx="1350" cy="700" rx="260" ry="400" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:5"/>')
text('left hemisphere', 850, 270, 'nf-l1', 'middle'); text('right hemisphere', 1350, 270, 'nf-l1', 'middle')
add('<ellipse cx="1100" cy="720" rx="60" ry="40" style="fill:var(--dk9);fill-opacity:.35;stroke:var(--dk9);stroke-width:3"/>'); text('thalamus', 1100, 790, 'nf-l2', 'middle')
add(f'<circle cx="{FX}" cy="{FY}" r="22" style="fill:var(--ink-3);opacity:.6"/>'); text('medial temporal focus', FX - 40, FY + 60, 'nf-l2', 'end')
FOC = ('aware', 'impaired', 'secgen', 'status')
for t in FOC:
    add(f'<circle cx="{FX}" cy="{FY}" r="50" style="fill:var(--accent);fill-opacity:.4"/>', when=TP(t, 'aura'))
add(f'<circle cx="{FX}" cy="{FY}" r="100" style="fill:var(--bad);fill-opacity:.4"/>', when=TP('aware', 'ictal'))
add('<ellipse cx="820" cy="760" rx="230" ry="300" style="fill:var(--bad);fill-opacity:.35"/>', when=TP('impaired', 'ictal') + TP('secgen', 'ictal'))
for cx in (850, 1350):
    add(f'<ellipse cx="{cx}" cy="700" rx="250" ry="390" style="fill:var(--bad);fill-opacity:.4"/>', when=TP('secgen', 'ictal') + TP('absence', 'ictal') + T('status'))
    add(f'<ellipse cx="{cx}" cy="700" rx="250" ry="390" style="fill:var(--ink-3);fill-opacity:.25"/>', when=TP('secgen', 'post') + TP('impaired', 'post'))
add('<ellipse cx="1100" cy="720" rx="70" ry="50" style="fill:var(--bad);fill-opacity:.7"/>', when=TP('absence', 'ictal'))
TAG = dict(aware='focal aware — consciousness kept; motor, sensory, autonomic or psychic symptoms',
           impaired='focal impaired awareness — consciousness impaired, automatisms',
           secgen='focal → secondarily generalized tonic-clonic', absence='absence — ~10 s blank stare, 3 Hz spike-and-wave, no postictal confusion',
           status='status epilepticus — ≥ 5 minutes, or no recovery between seizures', pnes='psychogenic — no discharge: normal video EEG, no postictal phase')
for k, s in TAG.items(): text(s, 1100, 1180, 'nf-l1 dyn-tag', 'middle', when=T(k))
PH = dict(aura='aura — the early part: odd smells or tastes', ictal='ictal — first symptom to the end of seizure activity',
          post='postictal — gradual recovery to baseline')
for k, s in PH.items(): text(s, 1100, 1220, 'nf-l1', 'middle', when=[f'ph:{k}'])
text('still seizing — benzodiazepine first, then fosphenytoin', 1100, 1260, 'nf-l1 dyn-tag', 'middle', when=TP('status', 'post'))
text('no postictal confusion', 1100, 1260, 'nf-l1', 'middle', when=TP('absence', 'post'))

# ════════ EEG ════════
EY = 1400
add(f'<rect x="580" y="{EY - 90}" width="1040" height="180" rx="16" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>')
text('EEG', 600, EY - 100, 'nf-l1')
calm = 'M600 {y} ' + ' '.join(f'l20 {(-8 if i % 2 else 8)}' for i in range(50))
add(f'<path d="{calm.format(y=EY)}" style="fill:none;stroke:var(--ink-2);stroke-width:3"/>',
    unless=TP('aware', 'ictal') + TP('impaired', 'ictal') + TP('secgen', 'ictal') + TP('absence', 'ictal') + T('status'))
spikes = f'M600 {EY} ' + ' '.join(f'l12 {(-60 if i % 2 else 60)}' for i in range(84))
add(f'<path d="{spikes}" style="fill:none;stroke:var(--bad);stroke-width:3"/>', when=TP('aware', 'ictal') + TP('impaired', 'ictal') + TP('secgen', 'ictal') + T('status'))
sw = f'M600 {EY} ' + ' '.join('l10 -70 l10 70 c40 0 40 40 80 0' for _ in range(10))
add(f'<path d="{sw}" style="fill:none;stroke:var(--bad);stroke-width:3"/>', when=TP('absence', 'ictal'))
text('3 Hz spike-and-wave', 1100, EY + 120, 'nf-l2', 'middle', when=TP('absence', 'ictal'))
text('normal during the event', 1100, EY + 120, 'nf-l2', 'middle', when=T('pnes'))

# ════════ causes by age ════════
AG = dict(kid='under 18: genetic, infection (febrile), trauma, congenital, metabolic · febrile seizures are provoked — not epilepsy',
          adult='18–65: tumor, trauma, stroke, infection', old='over 65: stroke, tumor, trauma, metabolic, infection')
for k, s in AG.items(): text(s, 1100, 1580, 'nf-l1', 'middle', when=[f'age:{k}'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{FX} {FY} C760 760 820 680 880 600', len=300, speed=140, r=8, base=dict(fire=3), when=TP('impaired', 'ictal') + TP('secgen', 'ictal') + T('status')),
  dict(d=f'M{FX} {FY} C800 700 1000 600 1300 560', len=700, speed=160, r=8, base=dict(fire=3), when=TP('secgen', 'ictal') + T('status')),
  dict(d='M1100 720 C1000 600 900 500 820 420', len=400, speed=160, r=8, base=dict(fire=3), when=TP('absence', 'ictal')),
  dict(d='M1100 720 C1200 600 1300 500 1380 420', len=400, speed=160, r=8, base=dict(fire=3), when=TP('absence', 'ictal')),
  dict(d=f'M{FX} {FY} C{FX + 30} {FY - 30} {FX + 50} {FY - 40} {FX + 70} {FY - 60}', len=100, speed=60, r=8, base=dict(fire=2), when=TP('aware', 'ictal')),
]
sites = [dict(x=FX - 30, y=FY - 40, n=[-1, -1], w=10, t='rec', l='', aria='Focal seizures', c='focalseiz', ions=[]),
         dict(x=1180, y=720, n=[1, 0], w=10, t='rec', l='', aria='Absence seizures', c='absence', ions=[]),
         dict(x=1600, y=500, n=[1, 0], w=10, t='rec', l='', aria='Status epilepticus', c='statusepi', ions=[]),
         dict(x=1640, y=EY, n=[1, 0], w=10, t='rec', l='', aria='Psychogenic nonepileptic events', c='pnes', ions=[]),
         dict(x=560, y=500, n=[-1, 0], w=10, t='rec', l='', aria='Seizure phases and causes', c='seizure', ions=[]),
         dict(x=560, y=1580, n=[-1, 0], w=10, t='rec', l='', aria='Febrile seizures', c='febrileseiz', ions=[])]

readouts = [
  dict(l='Consciousness', mods=[dict(when=TP('impaired', 'ictal') + TP('secgen', 'ictal') + TP('absence', 'ictal') + T('status'), d=-1),
                                dict(when=TP('secgen', 'post') + TP('impaired', 'post'), d=-1)]),
  dict(l='Epileptic discharge', mods=[dict(when=TP('aware', 'ictal') + TP('impaired', 'ictal') + TP('secgen', 'ictal') + TP('absence', 'ictal') + T('status'), d=1)]),
  dict(l='Brain injury risk', mods=[dict(when=T('status'), d=1)]),
]

notes = {
  '': 'A seizure is synchronized, high-frequency firing of a population of neurons. Focal seizures start in one area (most often '
      'the medial temporal lobe); generalized ones are diffuse. Epilepsy = recurrent, unprovoked seizures.',
  'ty:aware': 'Focal aware (simple partial): consciousness intact — motor, sensory, autonomic or psychic symptoms.',
  'ty:impaired': 'Focal impaired awareness (complex partial): consciousness impaired, automatisms.',
  'ty:secgen': 'Focal seizures may spread and become secondarily generalized tonic-clonic seizures.',
  'ty:absence': 'Absence: thalamic T-type Ca²⁺ channels drive 3 Hz spike-and-wave — ~10 s blank stares, many a day, triggered by '
                'hyperventilation, no postictal confusion. Childhood (4–10 y), mostly remits by 12. Ethosuximide; valproate.',
  'ty:status': 'Status epilepticus: continuous seizure ≥ 5 minutes, or recurrent seizures without return to baseline — it can '
               'injure the brain. Lorazepam, diazepam or midazolam first, then IV fosphenytoin.',
  'ty:pnes': 'Psychogenic nonepileptic events: prolonged (> 1 min) syncope- or tonic-clonic-like episodes with no epileptic EEG '
             'correlate — no postictal phase, no autonomic disturbance, no tongue biting; often witnessed, vocal, with an aura.',
  'age:kid': 'Febrile seizures: provoked by fever in a young child — benign, not epilepsy; roseola (HHV-6) after days of high '
             'fever. Antipyretics are for comfort; they do not prevent future febrile seizures.',
}

dyn = dict(
  kinds=dict(fire=['mov', '--bad']), groups=[['mov', 'Seizure discharge']],
  switches=[dict(id='ph', label='Phase', type='steps', auto=3, options=[['aura', 'Aura'], ['ictal', 'Ictal'], ['post', 'Postictal']]),
            dict(id='ty', label='Seizure', type='one', options=[
              ['aware', 'Focal aware', 'focalseiz'], ['impaired', 'Focal impaired awareness', 'focalseiz'],
              ['secgen', 'Secondarily generalized', 'focalseiz'], ['absence', 'Absence', 'absence'],
              ['status', 'Status epilepticus', 'statusepi'], ['pnes', 'Psychogenic (PNES)', 'pnes']]),
            dict(id='age', label='Causes by age', type='one', options=[
              ['kid', 'Under 18', 'febrileseiz'], ['adult', '18–65', 'seizure'], ['old', 'Over 65', 'seizure']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Katzung ch 24')

MAP = dict(
  id='spreadsim', title='Seizure Spread in Motion', topic='neuro', after='seizhead',
  sub='Run a seizure through aura, ictal and postictal phases — focal, spreading, secondarily generalized, absence, status and '
      'psychogenic — with the EEG under it and the causes by age',
  w=3600, h=1900,
  fa='177, 530, 531',
  src=['Katzung ch 24 — Antiseizure Medications', 'Guyton ch 60 — States of Brain Activity—Sleep, Brain Waves, Epilepsy, Psychoses, and Dementia'],
  lanes=[('ssType', 'Seizure types', 'tca'), ('ssMimic', 'Provoked & mimics', 'glycolysis')],
  nodes=[
    ('ss1', 'Seizure phases & causes', 330, 1760, 'ssType', 'aura · ictal · postictal', ['seizure'], 'hub'),
    ('ss2', 'Focal seizures', 760, 1760, 'ssType', 'medial temporal', ['focalseiz']),
    ('ss3', 'Absence seizures', 1200, 1760, 'ssType', '3 Hz · T-type Ca²⁺', ['absence']),
    ('ss4', 'Status epilepticus', 1640, 1760, 'ssType', '≥ 5 min', ['statusepi']),
    ('ss5', 'Febrile seizures', 2080, 1760, 'ssMimic', 'provoked · not epilepsy', ['febrileseiz']),
    ('ss6', 'Psychogenic events', 2520, 1760, 'ssMimic', 'normal video EEG', ['pnes'])],
  panels=[
    (2500, PANY, 1000, 'Telling them apart (Katzung ch 24)', [
      ('Absence', 'no postictal confusion'), ('Generalized tonic-clonic', 'postictal recovery'), ('Status', '≥ 5 min or no recovery'),
      ('PNES', 'normal EEG, no tongue biting')])],
  dyn=dyn)
