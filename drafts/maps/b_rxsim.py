# Psych Drugs at the Receptors (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A drug in the middle sends particles to every receptor it blocks: D₂ in the four dopamine pathways (the target
# and three side-effect pathways), 5-HT₂A, histamine H₁, muscarinic, α₁, cardiac Na⁺ channels and the NE/5-HT
# reuptake transporters. One `one` switch picks the drug (haloperidol, chlorpromazine, clozapine, olanzapine,
# risperidone, aripiprazole, amitriptyline); each blocked box lights up with its consequence. Receptor lists are only
# those the pinned cards state (antipsychotics, dapathways, eps, tca, h1blockers); drug-specific toxicities are
# drawn as tags, not receptors. 6 readouts. FA pages in `fa`. No new cards.
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


SW = 'rx'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 780
APS = ['halo', 'chlor', 'cloz', 'olan', 'risp', 'arip']
CX, CY = 1250, 680

text('Psych drugs at the receptors — the target and the side effects', 180, 150, 'dyn-big')
text('every antipsychotic blocks D₂ in all four dopamine pathways; only one of them is the point', 180, 176, 'dyn-cap')

# boxes: (key, x, y, w, title, role, blocked consequence, which drugs block it)
# UNVERIFIED: chlorpromazine's sedation, anticholinergic effects and orthostasis are drawn at H₁, muscarinic and α₁ receptors — the card names the effects, not the receptors
D2 = ['halo', 'chlor', 'cloz', 'olan', 'risp']
BOX = [
  ('ml', 200, 230, 'D₂ · mesolimbic', 'VTA → nucleus accumbens', 'positive symptoms fall — the therapeutic effect', D2),
  ('mc', 740, 230, 'D₂ · mesocortical', 'VTA → prefrontal cortex', 'negative symptoms — little help', D2),
  ('ns', 1280, 230, 'D₂ · nigrostriatal', 'substantia nigra → striatum', 'extrapyramidal symptoms', D2),
  ('ti', 1820, 230, 'D₂ · tuberoinfundibular', 'dopamine inhibits prolactin', 'hyperprolactinemia: galactorrhea, amenorrhea', D2),
  ('s2', 200, 940, '5-HT₂A', 'atypicals block it too', 'lets dopamine back into the striatum — less EPS', ['cloz', 'olan', 'risp']),
  ('h1', 560, 940, 'Histamine H₁', '', 'sedation, weight gain', ['chlor', 'tca']),
  ('mu', 920, 940, 'Muscarinic', '', 'anticholinergic: confusion, retention', ['chlor', 'tca']),
  ('a1', 1280, 940, 'α₁', '', 'orthostatic hypotension', ['chlor', 'tca']),
  ('na', 1640, 940, 'Cardiac Na⁺ channel', '', 'wide QRS — arrhythmia in overdose', ['tca']),
  ('rt', 2000, 940, 'NE and 5-HT reuptake', 'NET · SERT', 'antidepressant effect', ['tca']),
]
for k, x, y, title, role, cons, who in BOX:
    w = 500 if y < 500 else 330
    add(f'<rect x="{x}" y="{y}" width="{w}" height="180" rx="20" class="dyn-soft"/>')
    add(f'<rect x="{x}" y="{y}" width="{w}" height="180" rx="20" style="fill:var(--bad);fill-opacity:.10;stroke:var(--bad);stroke-width:4"/>', when=O(*who))
    text(title, x + 20, y + 40, 'nf-l1')
    if role: text(role, x + 20, y + 66, 'nf-l2')
    words = cons.split(' ')
    half = len(cons) // 2 if w < 400 and len(cons) > 34 else None
    if half:
        cut = cons.rfind(' ', 0, half + 6)
        text(cons[:cut], x + 20, y + 110, 'nf-l1 dyn-tag', when=O(*who)); text(cons[cut + 1:], x + 20, y + 134, 'nf-l1 dyn-tag', when=O(*who))
    else:
        text(cons, x + 20, y + 110, 'nf-l1 dyn-tag', when=O(*who))
# aripiprazole: partial agonist at D₂
for k, x, y, *_ in BOX[:4]:
    add(f'<rect x="{x}" y="{y}" width="500" height="180" rx="20" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:4;stroke-dasharray:10 6"/>', when=O('arip'))
    text('partial agonist — part block, part stimulation', x + 20, y + 110, 'nf-l1', when=O('arip'))

# the drug
add(f'<circle cx="{CX}" cy="{CY}" r="120" style="fill:var(--dk9);fill-opacity:.14;stroke:var(--dk9);stroke-width:4"/>')
NAME = dict(halo=('Haloperidol', 'high-potency typical'), chlor=('Chlorpromazine', 'low-potency typical'), cloz=('Clozapine', 'atypical'),
            olan=('Olanzapine', 'atypical'), risp=('Risperidone', 'atypical'), arip=('Aripiprazole', 'D₂ partial agonist'),
            tca=('Amitriptyline', 'tricyclic antidepressant'))
for k, (a, b) in NAME.items():
    text(a, CX, CY - 4, 'dyn-big', 'middle', when=O(k)); text(b, CX, CY + 22, 'nf-l2', 'middle', when=O(k))
text('pick a drug', CX, CY + 6, 'nf-l1', 'middle', unless=[f'{SW}:*'])
# drug-specific tags (from the antipsychotics card), not receptors
TAGS = dict(halo='EPS · neuroleptic malignant syndrome', chlor='sedation, anticholinergic, orthostasis · corneal deposits',
            cloz='agranulocytosis (ANC checks) · seizures · myocarditis · weight gain', olan='most weight gain, hyperglycemia, dyslipidemia',
            risp='hyperprolactinemia', arip='severe akathisia', tca='overdose: convulsions, coma, cardiotoxicity — sodium bicarbonate')
for k, t in TAGS.items():
    text('This drug: ' + t, 200, 1180, 'nf-l1', when=O(k))

# ════════ motion ════════
flows = []
for k, x, y, title, role, cons, who in BOX:
    w = 500 if y < 500 else 330
    tx, ty = x + w // 2, (y + 180) if y < 500 else y
    sy = CY - 120 if y < 500 else CY + 120
    d = f'M{CX} {sy} C{CX} {(sy + ty) // 2} {tx} {(sy + ty) // 2} {tx} {ty}'
    flows.append(dict(d=d, len=round(abs(tx - CX) + abs(ty - sy) + 60), speed=120, r=7, base=dict(), when=O(*who, *(['arip'] if y < 500 else [])),
                      mods=[dict(when=O(*who, *(['arip'] if y < 500 else [])), set=dict(drug=4))]))
sites = [
  dict(x=1530, y=410, n=[0, -1], w=20, t='rec', l='', aria='Nigrostriatal D₂ — EPS', c='eps', ions=[]),
  dict(x=2070, y=410, n=[0, -1], w=20, t='rec', l='', aria='Tuberoinfundibular D₂ — prolactin', c='prolactinoma', ions=[]),
  dict(x=450, y=410, n=[0, -1], w=20, t='rec', l='', aria='Dopamine pathways', c='dapathways', ions=[]),
]

readouts = [
  dict(l='Positive symptoms', mods=[dict(when=O(*APS), d=-1)]),
  dict(l='EPS risk', mods=[dict(when=O('halo', 'arip'), d=1)]),
  dict(l='Prolactin', mods=[dict(when=O('halo', 'chlor', 'risp'), d=1)]),
  dict(l='Sedation · anticholinergic', mods=[dict(when=O('chlor', 'tca'), d=1)]),
  dict(l='Weight · glucose', mods=[dict(when=O('olan', 'cloz', 'tca'), d=1)]),
  dict(l='QRS in overdose', mods=[dict(when=O('tca'), d=1)]),
]

notes = {
  '': 'Antipsychotics block D₂ in all four dopamine pathways at once: mesolimbic blockade treats positive symptoms, and each of the '
      'other three explains a side effect. Off-target blockade of H₁, muscarinic and α₁ receptors explains the rest.',
  'rx:halo': 'Haloperidol, a high-potency typical, does little besides block D₂ — so it has the most extrapyramidal effects (and '
             'NMS), plus hyperprolactinemia from the tuberoinfundibular pathway.',
  'rx:chlor': 'Chlorpromazine, a low-potency typical: weaker at D₂ but sedating, anticholinergic and hypotensive — the H₁, muscarinic '
              'and α₁ pattern — with corneal deposits.',
  'rx:cloz': 'Clozapine, for treatment-resistant schizophrenia and suicidality: atypical (5-HT₂A as well as D₂), with agranulocytosis '
             '(frequent ANC checks), seizures, myocarditis and weight gain.',
  'rx:olan': 'Olanzapine, an atypical: 5-HT₂A blockade cuts EPS, but with clozapine it causes the most weight gain, hyperglycemia and '
             'dyslipidemia — monitor weight, glucose and lipids.',
  'rx:risp': 'Risperidone, an atypical best known for hyperprolactinemia — galactorrhea, amenorrhea, gynecomastia.',
  'rx:arip': 'Aripiprazole is a D₂ partial agonist rather than a blocker — and can cause severe akathisia.',
  'rx:tca': 'Amitriptyline blocks NE and 5-HT reuptake (the antidepressant effect) but also H₁, muscarinic and α₁ receptors and '
            'cardiac Na⁺ channels — sedation, anticholinergic effects, orthostasis, and a wide QRS in overdose.',
}

dyn = dict(
  kinds=dict(drug=['drug', '--dk9']), groups=[['drug', 'Drug']],
  switches=[dict(id=SW, label='Drug', type='one', options=[
    ['halo', 'Haloperidol', 'antipsychotics'], ['chlor', 'Chlorpromazine', 'antipsychotics'], ['cloz', 'Clozapine', 'antipsychotics'],
    ['olan', 'Olanzapine', 'antipsychotics'], ['risp', 'Risperidone', 'antipsychotics'], ['arip', 'Aripiprazole', 'antipsychotics'],
    ['tca', 'Amitriptyline (TCA)', 'tca']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 509, 577, 587, 591, 593 · Katzung ch 29, 30')

MAP = dict(
  id='rxsim', title='Psych Drugs at the Receptors', topic='behav', after='psyrxprin',
  sub='Pick an antipsychotic or a tricyclic and watch it reach every receptor it blocks — D₂ in the four dopamine pathways, 5-HT₂A, '
      'H₁, muscarinic, α₁, Na⁺ channels — with the effect each blockade causes and the drug’s own toxicities',
  w=3500, h=1560,
  fa='240, 243, 250, 509, 577, 587, 591, 593',
  src=[full('Katzung', 29), full('Katzung', 30), full('Kaplan & Sadock', 21), full('Kaplan & Sadock', 5)],
  lanes=[('rcDa', 'Dopamine', 'glycolysis'), ('rcOff', 'Off-target receptors', 'tca'), ('rcDrug', 'Drugs', 'gluconeo')],
  nodes=[
    ('rx1', 'The four dopamine pathways', 330, 1340, 'rcDa', 'one target, three side effects', ['dapathways'], 'hub'),
    ('rx2', 'EPS · tardive dyskinesia', 780, 1340, 'rcDa', 'nigrostriatal', ['eps']),
    ('rx3', 'Hyperprolactinemia', 1200, 1340, 'rcDa', 'tuberoinfundibular', ['prolactinoma']),
    ('rx4', 'Antipsychotics', 1600, 1340, 'rcDrug', 'typical · atypical', ['antipsychotics', 'nms']),
    ('rx5', 'Tricyclics', 2000, 1340, 'rcDrug', 'five targets', ['tca']),
    ('rx6', 'Anticholinergic · α₁ · H₁', 330, 1470, 'rcOff', 'the off-target effects', ['antimusc', 'alpha1drugs', 'h1blockers'])],
  panels=[
    (2420, PANY, 1000, 'Pathway → effect (First Aid p. 591)', [
      ('Mesolimbic', 'positive symptoms — the target'),
      ('Mesocortical', 'negative symptoms — little effect'),
      ('Nigrostriatal', 'extrapyramidal symptoms'),
      ('Tuberoinfundibular', 'hyperprolactinemia')])],
  dyn=dyn)
