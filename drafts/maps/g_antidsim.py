# Poison & Antidote in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The poison flows to its target and does its damage; a toggle gives the antidote, which arrives and works one of four
# ways — competes at the target, binds the poison, blocks the step that makes it toxic (or replenishes what it
# consumes), or bypasses or replaces what was lost. One `one` switch picks the poison (16). Every pairing and
# mechanism is from the pinned cards (opioids, benzos, organophosphate, antimusc, acetaminophen, ethyleneglycol,
# digoxin, cyanide, anticoagrev, ironrx, chelators, tca, glucagondrug, methb, cohb, toxidromes); FA pages in `fa`.
# 4 readouts. No new cards.
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


SW = 'p'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 860
GIVE, NOGIVE = ['give'], ['!give']

# key: (poison, target, effect, antidote, how, family)
P = dict(
  opi=('Opioid', 'μ-opioid receptor', 'pinpoint pupils, respiratory depression, coma', 'Naloxone', 'competes at the μ receptor', 'compete'),
  benzo=('Benzodiazepine', 'GABA-A receptor', 'sedation, coma', 'Flumazenil', 'competes at the benzodiazepine site — can provoke seizures', 'compete'),
  op=('Organophosphate', 'acetylcholinesterase', 'miosis, DUMBBELSS, weakness', 'Atropine + pralidoxime', 'atropine blocks muscarinic receptors; pralidoxime regenerates the enzyme', 'compete'),
  ach=('Anticholinergic', 'muscarinic receptors', 'hot, dry, flushed, mydriasis, delirium', 'Physostigmine', 'inhibits cholinesterase — more ACh to outcompete the blocker', 'compete'),
  apap=('Acetaminophen', 'NAPQI after glutathione runs out', 'hepatic necrosis — AST and ALT in the thousands', 'N-acetylcysteine', 'replenishes glutathione', 'block'),
  meth=('Methanol · ethylene glycol', 'alcohol dehydrogenase → toxic acids', 'blindness · oxalate kidney injury', 'Fomepizole', 'blocks alcohol dehydrogenase — the parent alcohol is harmless', 'block'),
  dig=('Digoxin', 'Na⁺/K⁺-ATPase', 'vomiting, yellow vision, arrhythmias', 'Digoxin immune Fab', 'antibody fragments bind digoxin', 'bind'),
  cn=('Cyanide', 'complex IV (cytochrome oxidase)', 'lactic acidosis; venous blood stays red', 'Hydroxocobalamin', 'binds cyanide → cyanocobalamin', 'bind'),
  hep=('Heparin', 'antithrombin', 'bleeding', 'Protamine sulfate', 'positive charge binds negatively charged heparin', 'bind'),
  fe=('Iron', 'GI mucosa, then every organ', 'GI bleeding, anion-gap acidosis', 'Deferoxamine', 'chelates iron', 'bind'),
  pb=('Lead', 'ALA dehydratase, ferrochelatase', 'anemia, encephalopathy, wrist drop', 'Succimer · EDTA · dimercaprol', 'chelate lead', 'bind'),
  war=('Warfarin', 'vitamin K–dependent factors II, VII, IX, X', 'bleeding, long PT', 'Vitamin K · PCC or FFP', 'vitamin K restores synthesis (slowly); PCC replaces now', 'bypass'),
  tca=('Tricyclic overdose', 'cardiac Na⁺ channels', 'wide QRS, arrhythmia, seizures', 'Sodium bicarbonate', 'prevents the arrhythmia', 'bypass'),
  bb=('β-blocker', 'β₁ receptor', 'bradycardia, hypotension', 'Glucagon', 'raises cAMP without the β receptor', 'bypass'),
  mhb=('Oxidizer (nitrites, dapsone)', 'hemoglobin Fe²⁺ → Fe³⁺', 'cyanosis unchanged by O₂, brown blood', 'Methylene blue', 'returns heme iron to Fe²⁺ (with vitamin C)', 'bypass'),
  co=('Carbon monoxide', 'hemoglobin (and complex IV)', 'headache, confusion; normal pulse oximetry', '100% or hyperbaric O₂', 'displaces CO from hemoglobin', 'compete'),
)
# UNVERIFIED: the "how" for physostigmine (cholinesterase inhibitor), methylene blue (reducing Fe³⁺ back to Fe²⁺) and for 100% O₂ (displacing CO) are standard teaching; the cards name the treatment only
FAM = {f: [k for k, v in P.items() if v[5] == f] for f in ('compete', 'bind', 'block', 'bypass')}

text('Poison → target → harm, then the antidote', 180, 150, 'dyn-big')
text('turn on “Give the antidote” to see how it works', 180, 176, 'dyn-cap')
box(160, 210, 2340, 1180)
# poison, target, antidote, effect, excreted
add('<rect x="220" y="440" width="460" height="200" rx="30" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:4"/>')
add('<rect x="1020" y="420" width="560" height="240" rx="30" class="dyn-cell"/>')
add('<rect x="1880" y="440" width="420" height="200" rx="30" style="fill:var(--ok);fill-opacity:.12;stroke:var(--ok);stroke-width:4"/>')
add('<rect x="1020" y="840" width="560" height="160" rx="30" class="dyn-soft"/>')
text('POISON', 450, 480, 'nf-l2', 'middle'); text('TARGET', 1300, 460, 'nf-l2', 'middle'); text('ANTIDOTE', 2090, 480, 'nf-l2', 'middle')
text('HARM', 1300, 880, 'nf-l2', 'middle')
for k, (poi, tgt, eff, ant, how, fam) in P.items():
    w = O(k)
    text(poi, 450, 550, 'dyn-big', 'middle', when=w)
    text(tgt, 1300, 550, 'nf-l1', 'middle', when=w)
    text(eff, 1300, 940, 'nf-l1', 'middle', when=w)
    text(ant, 2090, 550, 'nf-l1', 'middle', when=w)
    text(how, 1300, 1110, 'nf-l1 dyn-tag', 'middle', when=[f'{SW}:{k}&give'])
text('pick a poison on the right', 1300, 550, 'nf-l1', 'middle', unless=[f'{SW}:*'])
FT = dict(compete='COMPETES at the target', bind='BINDS the poison', block='BLOCKS the toxic step / REPLENISHES', bypass='BYPASSES or REPLACES')
for f, t in FT.items():
    text(t, 2090, 610, 'nf-l1 dyn-tag', 'middle', when=[f'{SW}:{k}&give' for k in FAM[f]])
add('<path d="M1300 660 V840" class="dyn-line"/>')
text('harm reversed', 1300, 820, 'nf-l1', 'middle', when=['give&p:*'])
add('<rect x="1060" y="860" width="480" height="120" rx="24" style="fill:var(--ok);fill-opacity:.18"/>', when=['give&p:*'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
ALL = list(P)
flows = [
  # poison → target: full until the antidote, then a trickle (bind: none reaches)
  dict(d='M680 540 H1020', len=340, speed=110, r=8, base=dict(), when=O(*ALL),
       mods=[m(O(*ALL), set=dict(poi=6)), m([f'give&{SW}:{k}' for k in ALL], set=dict(poi=2)), m([f'give&{SW}:{k}' for k in FAM['bind']], set=dict(poi=0))]),
  # target → harm
  dict(d='M1300 660 V840', len=180, speed=80, r=7, base=dict(), when=O(*ALL), mods=[m(O(*ALL), set=dict(poi=3)), m(GIVE, set=dict(poi=0))]),
  # antidote → target (compete, block, bypass)
  dict(d='M1880 540 H1580', len=300, speed=110, r=8, base=dict(), when=[f'give&{SW}:{k}' for k in FAM['compete'] + FAM['block'] + FAM['bypass']],
       mods=[m(GIVE, set=dict(ant=6))]),
  # antidote → the poison on its way in, and the pair out to excretion (bind)
  dict(d='M1880 600 C1500 760 1000 760 850 560', len=1300, speed=140, r=8, base=dict(), when=[f'give&{SW}:{k}' for k in FAM['bind']],
       mods=[m(GIVE, set=dict(ant=6))]),
  dict(d='M850 600 C850 900 700 1060 450 1100', len=640, speed=90, r=9, base=dict(), when=[f'give&{SW}:{k}' for k in FAM['bind']],
       mods=[m(GIVE, set=dict(pair=4))]),
]
text('bound → excreted', 450, 1150, 'nf-l1', 'middle', when=[f'give&{SW}:{k}' for k in FAM['bind']])
sites = [dict(x=1300, y=420, n=[0, -1], w=40, t='rec', l='', aria='Toxidromes', c='toxidromes', ions=[])]

readouts = [
  dict(l='Toxic effect', mods=[dict(when=[f'{SW}:*&!give'], d=1), dict(when=[f'{SW}:*&give'], d=-1)]),
  dict(l='Pupil size', mods=[dict(when=[f'{SW}:opi&!give', f'{SW}:op&!give'], d=-1), dict(when=[f'{SW}:ach&!give'], d=1)]),
  dict(l='Anion-gap acidosis', mods=[dict(when=[f'{SW}:meth&!give', f'{SW}:fe&!give', f'{SW}:cn&!give'], d=1)]),
  dict(l='QRS width', mods=[dict(when=[f'{SW}:tca&!give'], d=1)]),
]

notes = {'': 'Every antidote works one of four ways: it competes at the target, binds the poison, blocks the step that makes it '
             'toxic (or replenishes what it uses up), or bypasses the blocked route and replaces what was lost.',
         'give': 'The antidote is on board — watch how it gets there and what it does to the poison’s flow.'}
for k, (poi, tgt, eff, ant, how, fam) in P.items():
    notes[f'{SW}:{k}'] = f'{poi} acts on {tgt}: {eff}. Antidote: {ant} — {how}.'

dyn = dict(
  kinds=dict(poi=['poi', '--bad'], ant=['ant', '--ok'], pair=['ant', '--dk5']), groups=[['poi', 'Poison'], ['ant', 'Antidote']],
  switches=[dict(id=SW, label='Poison', type='one', options=[
    ['opi', 'Opioid', 'opioids'], ['benzo', 'Benzodiazepine', 'benzos'], ['op', 'Organophosphate', 'organophosphate'],
    ['ach', 'Anticholinergic', 'antimusc'], ['apap', 'Acetaminophen', 'acetaminophen'], ['meth', 'Methanol · ethylene glycol', 'ethyleneglycol'],
    ['dig', 'Digoxin', 'digoxin'], ['cn', 'Cyanide', 'cyanide'], ['hep', 'Heparin', 'anticoagrev'], ['fe', 'Iron', 'ironrx'],
    ['pb', 'Lead', 'chelators'], ['war', 'Warfarin', 'anticoagrev'], ['tca', 'Tricyclic overdose', 'tca'], ['bb', 'β-blocker', 'glucagondrug'],
    ['mhb', 'Methemoglobinemia', 'methb'], ['co', 'Carbon monoxide', 'cohb']]),
    dict(id='give', label='Treatment', type='toggle', on='Antidote given', off='Give the antidote', **{'def': False})],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 70, 73, 239–240, 247, 326–327, 442, 567, 588, 593, 688–689 · Katzung ch 58')

MAP = dict(
  id='antidsim', title='Poison & Antidote in Motion', topic='pharm', after='tox',
  sub='Pick a poison and watch it reach its target and do harm — then give the antidote and see whether it competes, binds the '
      'poison for excretion, blocks the toxic step or bypasses it; the readouts show the toxic effect, pupils, anion gap and QRS',
  w=3500, h=1600,
  fa='70, 73, 239–240, 247, 326–327, 397, 431, 442, 495, 561–562, 567, 588, 593, 617, 688–689',
  src=[full('Katzung', 58), full('Katzung', 57), full('Katzung', 31), full('Katzung', 7), full('Katzung', 34)],
  lanes=[('adRec', 'Receptor poisons', 'glycolysis'), ('adBind', 'Bound & chelated', 'tca'), ('adMet', 'Metabolism & blood', 'gluconeo')],
  nodes=[
    ('ad1', 'Toxidromes', 330, 1300, 'adRec', 'pupils · skin · vitals', ['toxidromes'], 'hub'),
    ('ad2', 'Opioids · benzodiazepines', 760, 1300, 'adRec', 'naloxone · flumazenil', ['opioids', 'benzos']),
    ('ad3', 'Cholinergic poisons', 1250, 1300, 'adRec', 'atropine · physostigmine', ['organophosphate', 'antimusc']),
    ('ad4', 'Digoxin · cyanide', 1780, 1300, 'adBind', 'Fab · hydroxocobalamin', ['digoxin', 'cyanide']),
    ('ad5', 'Iron · lead', 330, 1430, 'adBind', 'chelators', ['ironrx', 'chelators']),
    ('ad6', 'Anticoagulant reversal', 760, 1430, 'adBind', 'protamine · vitamin K', ['anticoagrev']),
    ('ad7', 'Acetaminophen · toxic alcohols', 1220, 1430, 'adMet', 'NAC · fomepizole', ['acetaminophen', 'ethyleneglycol']),
    ('ad8', 'TCA · β-blocker', 1650, 1430, 'adMet', 'bicarbonate · glucagon', ['tca', 'glucagondrug']),
    ('ad9', 'MetHb · CO', 2030, 1430, 'adMet', 'methylene blue · O₂', ['methb', 'cohb'])],
  panels=[
    (2420, PANY, 1000, 'Four ways an antidote works', [
      ('Competes', 'naloxone, flumazenil, atropine, physostigmine'),
      ('Binds', 'digoxin Fab, hydroxocobalamin, protamine, chelators'),
      ('Blocks or replenishes', 'fomepizole, N-acetylcysteine'),
      ('Bypasses or replaces', 'glucagon, vitamin K / PCC, bicarbonate')])],
  dyn=dyn)
