# Syncope (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree: one `one` switch picks the answer, the path to it lights up and a
# dot travels down it; a clue box shows the tell for that answer, and 4 readouts give the blood pressure on
# standing, heart rate, QT and the murmur's response to Valsalva. Every clue is taken from the pinned cards
# (syncope, aortstenosis, hcm, avblock, longqt, alpha1drugs, baroreflex, hypovshock, gtc), whose FA pages are in `fa`.
# No new cards.
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
  ('r', None, '', 'Transient loss of consciousness', 'brief · full recovery — or not syncope?', None),
  ('rx', 'r', 'a trigger, with a warning', 'Reflex syncope', 'the most common kind', None),
  ('vv', 'rx', 'warm, pale, nauseated first', 'Vasovagal', 'hot crowd · long standing', 'vaso'),
  ('si', 'rx', 'cough · micturition · defecation', 'Situational', 'during the act', 'situ'),
  ('cs', 'rx', 'tight collar · turning the head', 'Carotid sinus hypersensitivity', 'pressure on the sinus', 'carot'),
  ('oh', 'r', 'on standing up', 'Orthostatic hypotension', 'SBP ↓ ≥ 20 or DBP ↓ ≥ 10 by 3 min', None),
  ('hv', 'oh', 'bleeding · vomiting · diuresis', 'Volume loss', 'low preload', 'hypov'),
  ('dr', 'oh', 'a new α blocker', 'Drug — first-dose α₁ blockade', 'prazosin, terazosin, doxazosin', 'drug'),
  ('af', 'oh', 'diabetes · parkinsonism', 'Autonomic failure', 'no reflex squeeze', 'auto'),
  ('cd', 'r', 'exertion · palpitations · heart disease', 'Cardiac syncope', 'the dangerous kind', None),
  ('st', 'cd', 'murmur + syncope on exertion', 'Outflow obstruction', '', None),
  ('as', 'st', 'older · murmur to the carotids', 'Aortic stenosis', 'pulsus parvus et tardus', 'as'),
  ('hc', 'st', 'young athlete · louder with Valsalva', 'Hypertrophic cardiomyopathy', 'septum blocks outflow', 'hcm'),
  ('ar', 'cd', 'abnormal ECG', 'Arrhythmia', '', None),
  ('hb', 'ar', 'slow · P waves march through', 'Complete heart block', 'atria and ventricles dissociated', 'avb'),
  ('lq', 'ar', 'long QT · QT drug · low K⁺ or Mg²⁺', 'Torsades de pointes', 'polymorphic VT', 'lqt'),
  ('sz', 'r', 'jerking · tongue bitten · confused after', 'Not syncope — a seizure', 'postictal confusion', 'sz'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Syncope — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues (from the pinned cards) ════════
C = {
  'vaso': ['Vasovagal — the commonest faint', 'prodrome: warmth, pallor, nausea · short episode, rapid recovery', 'classic scene: standing in a hot crowd'],
  'situ': ['Situational — a reflex faint tied to an act', 'coughing, sneezing, swallowing, defecation, micturition'],
  'carot': ['Carotid sinus hypersensitivity', 'pressure on the sinus (a tight collar) mimics high pressure → reflex vagal slowing', 'carotid massage slows the AV node'],
  'hypov': ['Orthostatic — too little volume', 'systolic drop ≥ 20 or diastolic ≥ 10 mm Hg within 3 minutes of standing', 'the baroreflex answers with a faster heart'],
  'drug': ['Orthostatic — first-dose α₁ blockade', 'prazosin, terazosin, doxazosin: first-dose orthostatic hypotension, dizziness', 'α₁ blockade relaxes the vessels the reflex would squeeze'],
  'auto': ['Orthostatic — autonomic failure', 'the reflex arm that should constrict vessels on standing is lost', 'midodrine (α₁ agonist) treats postural hypotension from autonomic insufficiency'],
  'as': ['Aortic stenosis — SAD: syncope, angina, dyspnea on exertion', 'crescendo–decrescendo murmur at the base, to the carotids · soft S2', 'each symptom marks a sharp drop in survival → valve replacement'],
  'hcm': ['Hypertrophic cardiomyopathy', 'syncope during exercise, sudden death in young athletes', 'murmur louder with Valsalva and standing, softer with squatting'],
  'avb': ['Third-degree (complete) AV block', 'P waves march through independently · an escape rhythm sets the slow rate', 'infranodal block needs a pacemaker'],
  'lqt': ['Long QT → torsades de pointes', 'syncope or sudden death · ↓ K⁺, ↓ Mg²⁺, ↓ Ca²⁺ and bradycardia all prolong QT', 'QT drugs: class IA and III, macrolides, antipsychotics, TCAs, ondansetron'],
  'sz': ['A generalized tonic-clonic seizure, not a faint', 'stiffening then jerking, tongue biting, incontinence, postictal confusion', 'atonic “drop” seizures are the ones mistaken for fainting'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='BP on standing', mods=[dict(when=O('hypov', 'drug', 'auto'), d=-1)]),
  # UNVERIFIED: vasovagal bradycardia is standard teaching but not on the pinned syncope card
  dict(l='Heart rate', mods=[dict(when=O('hypov'), d=1), dict(when=O('avb', 'carot', 'vaso'), d=-1)]),
  dict(l='QT interval', mods=[dict(when=O('lqt'), d=1)]),
  dict(l='Murmur with Valsalva', mods=[dict(when=O('hcm'), d=1), dict(when=O('as'), d=-1)]),
]

# ════════ notes ════════
notes = {
  '': 'Syncope is a brief loss of consciousness from too little blood flow to the brain, with full recovery. Sort it three '
      'ways — reflex, orthostatic, cardiac — and first ask whether it was a faint at all.',
  'dx:vaso': 'Vasovagal syncope, the most common faint: a prodrome of warmth, pallor and nausea, a short episode and a quick '
             'recovery — classically while standing in a hot crowd.',
  'dx:situ': 'Situational syncope is a reflex faint during coughing, sneezing, swallowing, defecation or micturition.',
  'dx:carot': 'Carotid sinus hypersensitivity: pressure on the sinus (a tight collar) mimics high pressure, so the baroreflex '
              'slows the heart — the same reflex carotid massage uses to slow the AV node.',
  'dx:hypov': 'Orthostatic hypotension: a systolic fall of at least 20 or a diastolic fall of at least 10 mm Hg within 3 minutes '
              'of standing. With low volume the baroreflex speeds the heart, but output still falls.',
  'dx:drug': 'The first dose of a selective α₁ blocker (prazosin, terazosin, doxazosin) can cause orthostatic hypotension and '
             'dizziness — the vessels can’t constrict when the patient stands.',
  'dx:auto': 'Autonomic failure removes the reflex that tightens vessels on standing, so pressure falls with posture. '
             'Midodrine, an α₁ agonist, treats postural hypotension from autonomic insufficiency.',
  'dx:as': 'Aortic stenosis: syncope, angina and dyspnea on exertion (SAD), each a sharp drop in survival. Crescendo–'
           'decrescendo murmur radiating to the carotids, pulsus parvus et tardus — replace the valve once symptomatic.',
  'dx:hcm': 'Hypertrophic cardiomyopathy: syncope on exertion and sudden death in young athletes. The murmur gets louder with '
            'Valsalva and standing (a smaller LV), softer with squatting and handgrip.',
  'dx:avb': 'Complete heart block: the atria and ventricles beat independently and a slow escape rhythm sets the rate. '
            'Mobitz II can progress to it abruptly — both need a pacemaker.',
  'dx:lqt': 'Long QT lets early afterdepolarizations trigger torsades de pointes — syncope or sudden death. Low K⁺, Mg²⁺ or '
            'Ca²⁺, bradycardia and QT-prolonging drugs set it up; magnesium treats it.',
  'dx:sz': 'Tongue biting, incontinence and postictal confusion point to a generalized tonic-clonic seizure, not syncope. '
           'Atonic drop seizures are the ones most often mistaken for fainting.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['vaso', 'Vasovagal', 'syncope'], ['situ', 'Situational', 'syncope'], ['carot', 'Carotid sinus hypersensitivity', 'baroreflex'],
    ['hypov', 'Orthostatic — volume loss', 'hypovshock'], ['drug', 'Orthostatic — α₁ blocker', 'alpha1drugs'],
    ['auto', 'Orthostatic — autonomic failure', 'alpha1drugs'], ['as', 'Aortic stenosis', 'aortstenosis'],
    ['hcm', 'Hypertrophic cardiomyopathy', 'hcm'], ['avb', 'Complete heart block', 'avblock'],
    ['lqt', 'Long QT → torsades', 'longqt'], ['sz', 'Seizure (a mimic)', 'gtc']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 296, 299, 311–318 (cards) · Robbins ch 12 · Costanzo ch 4')

MAP = dict(
  id='sxsyncope', title='Syncope', topic='sx', after='sxchest',
  sub='Sort a faint as reflex, orthostatic or cardiac — pick an answer and a dot follows the clues down the tree, while '
      'the readouts show the blood pressure, heart rate, QT and murmur that go with it. Tap a card pin for the details',
  w=3500, h=1830,
  fa='144, 243, 296, 299, 308, 311–313, 315, 317–318, 531',
  src=[full('Robbins', 12), full('Costanzo', 4), full('Guyton', 18), full('Guyton', 23), full('Guyton', 13), full('Katzung', 10),
       full('Katzung', 14), full('Guyton', 24)],
  lanes=[('syRefl', 'Reflex & orthostatic', 'glycolysis'), ('syCard', 'Cardiac', 'tca'), ('syMimic', 'Mimics', 'gluconeo')],
  nodes=[
    ('sy1', 'Syncope', 330, PY, 'syRefl', 'reflex · orthostatic · cardiac', ['syncope'], 'hub'),
    ('sy2', 'Baroreceptor reflex', 760, PY, 'syRefl', 'the reflex behind it', ['baroreflex']),
    ('sy3', 'α₁ drugs', 1160, PY, 'syRefl', 'first-dose hypotension', ['alpha1drugs']),
    ('sy4', 'Hypovolemia', 1520, PY, 'syRefl', 'low preload', ['hypovshock']),
    ('sy5', 'Aortic stenosis · HCM', 1920, PY, 'syCard', 'syncope on exertion', ['aortstenosis', 'hcm']),
    ('sy6', 'AV block · sick sinus', 330, PY + 130, 'syCard', 'too slow', ['avblock', 'sicksinus']),
    ('sy7', 'Torsades · VT · Brugada', 760, PY + 130, 'syCard', 'too fast', ['longqt', 'vtach', 'brugada']),
    ('sy8', 'Seizure', 1160, PY + 130, 'syMimic', 'the mimic', ['gtc'])],
  panels=[
    (2420, PANY, 1000, 'Three kinds (First Aid p. 318)', [
      ('Reflex', 'vasovagal · situational · carotid sinus'),
      ('Orthostatic', 'hypovolemia · drugs · autonomic failure'),
      ('Cardiac', 'arrhythmia · structural disease (AS, HCM)'),
      ('Orthostatic test', 'SBP ↓ ≥ 20 or DBP ↓ ≥ 10 within 3 min')])],
  dyn=dyn)
