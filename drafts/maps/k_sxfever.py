# Fever & Hyperthermia (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it): a reset set point (fever) vs heat made or kept (hyperthermia) — the drug syndromes, toxidromes, heat stroke
# and thyroid storm. Readouts: hypothalamic set point, CK, sweating, pupil size, reflexes. Clues come from the
# pinned cards (acutephase, nms, serotoninsyndrome, mhyper, antimusc, toxidromes, cocaine, heatstroke,
# hyperthyroid); their FA pages are in `fa`. No new cards.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

# ── the decision tree (shared by the work-up maps; plain kit shapes and one flow per answer) ──
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

def tree(T, sw, X0=180, X1=2320, Y0=250, DY=96, BW=430):
    """T: [(id, parent, answer on the way in, label, subtitle, option key or None)] in reading order.
    Draws the tree left → right (one column per question), highlights the path to the chosen answer
    and sends a dot down it. Returns ({id: (x, y)}, flows, bottom y)."""
    kids, row = {}, {}
    for nid, par, *_ in T: kids.setdefault(par, []).append(nid)
    depth = {}
    for nid, par, *_ in T: depth[nid] = 0 if par is None else depth[par] + 1
    D = max(depth.values())
    step = (X1 - X0 - BW) / max(D, 1)
    pos, n = {}, [0]
    def place(nid):
        ch = kids.get(nid, [])
        for c in ch: place(c)
        y = (pos[ch[0]][1] + pos[ch[-1]][1]) / 2 if ch else Y0 + n[0] * DY
        if not ch: n[0] += 1
        pos[nid] = (round(X0 + depth[nid] * step), round(y))
    place(T[0][0])
    info = {r[0]: r for r in T}
    first = len(shapes)
    seg = {}
    for nid, par, ans, lab, sub, opt in T:
        x, y = pos[nid]
        if par is not None:
            px, py = pos[par]; sx = px + BW; mx = round(sx + (x - sx) * 0.4)
            seg[nid] = (f'M{sx} {py} H{mx} V{y} H{x}', (mx - sx) + abs(y - py) + (x - mx))
            add(f'<path d="{seg[nid][0]}" class="dyn-line"/>')
    for nid, par, ans, lab, sub, opt in T:
        x, y = pos[nid]
        leaf = opt is not None
        add(f'<rect x="{x}" y="{y - 26}" width="{BW}" height="52" rx="{10 if leaf else 26}" class="dyn-soft"/>')
        if ans: text(ans, x + 14, y - 34, 'dyn-cap')
        if sub:
            text(lab, x + 18, y - 4, 'nf-l1'); text(sub, x + 18, y + 16, 'nf-l2')
        else:
            text(lab, x + 18, y + 6, 'nf-l1')
    flows = []
    for nid, par, ans, lab, sub, opt in T:
        if opt is None: continue
        x, y = pos[nid]; W = [f'{sw}:{opt}']
        chain, c = [], nid
        while info[c][1] is not None: chain.append(c); c = info[c][1]
        chain.reverse()
        # one continuous path: root's right edge → … → this answer, passing through each box in between
        parts, ln = [], 0
        for i, c in enumerate(chain):
            p = info[c][1]; px, py = pos[p]
            if i: parts.append(f'H{px + BW}')
            parts.append(seg[c][0] if i == 0 else seg[c][0][seg[c][0].index(' H') + 1:])
            ln += seg[c][1] + (BW if i else 0)
        d = ' '.join(parts)
        shapes.insert(first, dict(svg=f'<path d="{d}" style="fill:none;stroke:var(--accent);stroke-width:7;stroke-linecap:round;stroke-linejoin:round;opacity:.55"/>', when=W))   # under the boxes
        add(f'<rect x="{x}" y="{y - 26}" width="{BW}" height="52" rx="10" style="fill:var(--accent);fill-opacity:.16;stroke:var(--accent);stroke-width:4"/>', when=W)
        flows.append(dict(d=d, len=round(ln), speed=170, r=8, base=dict(pt=3), when=W))
    bottom = max(y for x, y in pos.values()) + 26
    return pos, flows, bottom

def clues(C, sw, x, y, w, title='The tell'):
    """a box under the tree: the chosen answer's clues, one line each"""
    h = 64 + 26 * max(len(v) for v in C.values())
    box(x, y, x + w, y + h)
    text(title, x + 20, y + 36, 'dyn-big')
    text('pick an answer on the right — or press Tour — and follow the dot down the tree', x + 20, y + 64, 'dyn-cap', unless=[f'{sw}:*'])
    for k, lines in C.items():
        for i, t in enumerate(lines):
            text(t, x + 20, y + 66 + 26 * i, 'nf-l2' if i else 'nf-l1', when=[f'{sw}:{k}'])
    return y + h

# ════════ the tree ════════
SW = 'dx'
T = [
  ('r', None, '', 'Core temperature up', 'reset thermostat, or heat it can’t shed?', None),
  ('fv', 'r', 'infection or inflammation', 'Fever — set point raised', 'IL-1 → PGE₂ at the hypothalamus', 'fever'),
  ('hy', 'r', 'set point normal', 'Hyperthermia', 'heat made or kept', None),
  ('dg', 'hy', 'after a drug', 'A drug syndrome', 'which drug, which signs?', None),
  ('nm', 'dg', 'antipsychotic · lead-pipe rigidity', 'Neuroleptic malignant syndrome', 'CK ↑↑ · myoglobinuria', 'nms'),
  ('ss', 'dg', 'two serotonergic drugs · clonus', 'Serotonin syndrome', 'within hours · diarrhea', 'ss'),
  ('mh', 'dg', 'inhaled anesthetic · succinylcholine', 'Malignant hyperthermia', 'end-tidal CO₂ ↑ · RYR1', 'mh'),
  ('ac', 'dg', 'hot, dry, flushed · big pupils', 'Anticholinergic toxicity', 'atropine · TCAs · diphenhydramine', 'ach'),
  ('sy', 'dg', 'sweating · big pupils · BP ↑', 'Sympathomimetic toxicity', 'cocaine · amphetamines', 'symp'),
  ('hs', 'hy', 'heat, humidity, exertion', 'Heat stroke', 'core > 40 °C · confused', 'heat'),
  ('ts', 'hy', 'Graves + infection or surgery', 'Thyroid storm', 'delirium · tachyarrhythmia', 'storm'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Fever & hyperthermia — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'fever': ['Fever — the thermostat is reset', 'IL-1 (the endogenous pyrogen) raises hypothalamic PGE₂, which resets the set point', 'NSAIDs and aspirin block that step'],
  'nms': ['Neuroleptic malignant syndrome — after an antipsychotic', 'FEVER: Myoglobinuria, Fever, Encephalopathy, Vitals unstable, Enzymes (CK ↑), Rigidity', 'stop the drug · cooling · dantrolene, bromocriptine'],
  'ss': ['Serotonin syndrome — two serotonergic drugs together', 'Activity (clonus, hyperreflexia), Autonomic (hyperthermia, sweating, diarrhea), Altered mental status', 'onset in hours · cyproheptadine if supportive care fails'],
  'mh': ['Malignant hyperthermia — a RYR1 mutation meets the trigger', 'during anesthesia: rising end-tidal CO₂, tachycardia, masseter rigidity, hyperthermia', 'rhabdomyolysis, hyperkalemia · dantrolene'],
  'ach': ['Anticholinergic toxicity', 'hot as a hare, dry as a bone, red as a beet, blind as a bat, mad as a hatter', 'dry skin separates it from sympathomimetic toxicity · physostigmine'],
  'symp': ['Sympathomimetic toxicity — cocaine, amphetamines', 'mydriasis, sweating, tachycardia, hypertension, hyperthermia, agitation', 'chest pain or MI in a young patient'],
  'heat': ['Heat stroke — heat that can’t be shed', 'core temperature over 40 °C with confusion or delirium', 'rhabdomyolysis, AKI, DIC · rapid external cooling'],
  'storm': ['Thyroid storm', 'agitation, delirium, fever, diarrhea, tachyarrhythmia (the cause of death)', 'after acute stress — infection, trauma, surgery'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='Hypothalamic set point', mods=[dict(when=O('fever'), d=1), dict(when=O('heat'), d=0)]),
  dict(l='Creatine kinase', mods=[dict(when=O('nms', 'mh', 'heat'), d=1)]),
  dict(l='Sweating', mods=[dict(when=O('ss', 'symp'), d=1), dict(when=O('ach'), d=-1)]),
  dict(l='Pupil size', mods=[dict(when=O('ss', 'ach', 'symp'), d=1)]),
  dict(l='Reflexes · clonus', mods=[dict(when=O('ss'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'A high temperature is either fever — cytokines reset the hypothalamic set point — or hyperthermia, where the set point is '
      'normal but heat is made or kept faster than it is lost. Ask about drugs first.',
  'dx:fever': 'Fever: IL-1, the endogenous pyrogen, raises PGE₂ in the hypothalamus and resets the set point upward — the step '
              'NSAIDs and aspirin block. IL-6 drives the liver’s acute-phase response.',
  'dx:nms': 'Neuroleptic malignant syndrome follows an antipsychotic: lead-pipe rigidity, fever, encephalopathy, unstable vitals and '
            'a very high CK with myoglobinuria. Stop the drug; cool; dantrolene or bromocriptine.',
  'dx:ss': 'Serotonin syndrome comes on within hours of combining serotonergic drugs: clonus and hyperreflexia, hyperthermia, '
           'sweating, diarrhea and mydriasis. Stop the drugs; benzodiazepines; cyproheptadine.',
  'dx:mh': 'Malignant hyperthermia: a mutant RYR1 releases calcium when exposed to inhaled anesthetics or succinylcholine — rising '
           'end-tidal CO₂, rigidity, hyperthermia, hyperkalemia. Dantrolene blocks RYR1.',
  'dx:ach': 'Anticholinergic toxicity (atropine, TCAs, first-generation antihistamines, jimsonweed): hot, dry, flushed, mydriatic, '
            'delirious, with urinary retention. Dry skin separates it from sympathomimetic toxicity.',
  'dx:symp': 'Sympathomimetic toxicity (cocaine, amphetamines): mydriasis, sweating, tachycardia, hypertension, hyperthermia and '
             'agitation — the sweating is the difference from anticholinergic toxicity.',
  'dx:heat': 'Heat stroke is a failure to shed heat, not a reset set point: core temperature over 40 °C with CNS dysfunction, '
             'rhabdomyolysis, AKI and DIC. Cool rapidly from outside.',
  'dx:storm': 'Thyroid storm: agitation, delirium, fever, diarrhea and a tachyarrhythmia — the cause of death — set off by '
              'infection, trauma or surgery in a thyrotoxic patient.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['fever', 'Fever (set point reset)', 'acutephase'], ['nms', 'Neuroleptic malignant syndrome', 'nms'],
    ['ss', 'Serotonin syndrome', 'serotoninsyndrome'], ['mh', 'Malignant hyperthermia', 'mhyper'],
    ['ach', 'Anticholinergic toxicity', 'antimusc'], ['symp', 'Sympathomimetic toxicity', 'cocaine'],
    ['heat', 'Heat stroke', 'heatstroke'], ['storm', 'Thyroid storm', 'hyperthyroid']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 106, 239–241, 346, 530, 566, 587 (cards) · Guyton ch 74 · Katzung ch 58')

MAP = dict(
  id='sxfever', title='Fever & Hyperthermia', topic='sx', after='sxams',
  sub='A reset thermostat or heat that can’t be shed — pick an answer and a dot follows the clues down the tree to the drug '
      'syndromes, toxidromes, heat stroke and thyroid storm, while the readouts show set point, CK, sweating, pupils and reflexes',
  w=3500, h=1540,
  fa='106, 209, 225, 239–241, 243, 346, 433, 530, 566, 587, 589',
  src=[full('Guyton', 74), full('Katzung', 58), full('Katzung', 29), full('Katzung', 16), full('Katzung', 25), full('Katzung', 8),
       full('Katzung', 32), full('Robbins', 9)],
  lanes=[('xfFever', 'Fever', 'glycolysis'), ('xfDrug', 'Drug & toxin syndromes', 'tca'), ('xfHeat', 'Heat & hormones', 'gluconeo')],
  nodes=[
    ('xf1', 'Acute-phase response', 330, PY, 'xfFever', 'IL-1 · IL-6 · TNF-α', ['acutephase', 'sepsistnf'], 'hub'),
    ('xf2', 'Neuroleptic malignant syndrome', 800, PY, 'xfDrug', 'antipsychotics', ['nms']),
    ('xf3', 'Serotonin syndrome', 1260, PY, 'xfDrug', 'clonus', ['serotoninsyndrome']),
    ('xf4', 'Malignant hyperthermia', 1660, PY, 'xfDrug', 'RYR1', ['mhyper']),
    ('xf5', 'Toxidromes', 2020, PY, 'xfDrug', 'wet or dry?', ['toxidromes', 'antimusc', 'cocaine']),
    ('xf6', 'Heat illness', 330, PY + 130, 'xfHeat', 'cramps → stroke', ['heatstroke', 'heatillness']),
    ('xf7', 'Thyroid storm', 800, PY + 130, 'xfHeat', 'Graves under stress', ['hyperthyroid'])],
  panels=[
    (2420, PANY, 1000, 'Telling them apart (First Aid pp. 240, 587)', [
      ('Lead-pipe rigidity, CK ↑↑', 'neuroleptic malignant syndrome'),
      ('Clonus, hyperreflexia', 'serotonin syndrome — hours'),
      ('Hot and DRY skin', 'anticholinergic'),
      ('Hot and SWEATY skin', 'sympathomimetic'),
      ('In the operating room', 'malignant hyperthermia')])],
  dyn=dyn)
