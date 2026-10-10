# Who Decides? — Consent & Capacity (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The consent questions drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot
# travels it): emergency → adult with capacity → advance directive → surrogate order → minors and their exceptions.
# No readouts — the answers are people, not arrows. Every step is from the pinned cards (consent, capacity, advdir,
# surrogate, minors, ethprinciples, confid); their FA pages are in `fa`. No new cards.
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
SW = 'who'
T = [
  ('r', None, '', 'A treatment decision', 'who gets to decide?', None),
  ('em', 'r', 'life-threatening · no one to ask', 'Emergency', 'implied consent — treat', 'emerg'),
  ('ad', 'r', 'patient 18 or older', 'Adult', 'capacity for THIS decision?', None),
  ('ca', 'ad', 'understands, appreciates, reasons, chooses', 'Has capacity', '', None),
  ('pt', 'ca', 'agrees or refuses after full disclosure', 'The patient decides', 'informed consent — revocable', 'pt'),
  ('tp', 'ca', 'disclosure would severely harm', 'Therapeutic privilege', 'a narrow exception', 'priv'),
  ('nc', 'ad', 'can’t do one of the four', 'Lacks capacity', 'did they leave instructions?', None),
  ('dr', 'nc', 'living will · medical power of attorney', 'Follow the directive', 'or the named agent', 'dir'),
  ('su', 'nc', 'no directive', 'Surrogate', 'what would the patient want?', 'surr'),
  ('mi', 'r', 'under 18', 'Minor', 'parents — with exceptions', None),
  ('sd', 'mi', 'contraception · STI · prenatal care · drugs', 'The minor consents', 'sex, drugs, rock and roll', 'sdr'),
  ('ea', 'mi', 'married · self-supporting · military', 'Emancipated minor', 'consents as an adult', 'eman'),
  ('pa', 'mi', 'everything else', 'Parents consent', 'seek the child’s assent', 'par'),
  ('jw', 'mi', 'parent refuses blood for a bleeding child', 'Treat the child', 'transfuse', 'jw'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Who decides? — consent and capacity down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'emerg': ['Emergency — implied consent', 'the E of WIPE: Waiver, legally Incompetent, therapeutic Privilege, Emergency', 'treat now; explain afterward'],
  'pt': ['The patient decides — informed consent', 'disclosure (interpreter if needed), understanding, capacity, voluntariness', 'a process, not a signature — revocable at any time, even orally'],
  'priv': ['Therapeutic privilege', 'withhold information only if disclosing it would severely harm the patient', 'a family asking you to hide a result is not a reason — explore why'],
  'dir': ['Follow the advance directive', 'living will: specific interventions · medical power of attorney: an agent decides', 'a DNR means no CPR — not no intubation, feeding or chemotherapy'],
  'surr': ['The surrogate — substituted judgment', 'spouse → adult children → parents → adult siblings → other relatives', 'what the patient would have wanted, not what the surrogate prefers'],
  'sdr': ['Minors consent for themselves', 'contraception, STIs, prenatal care (usually not abortion), substance use treatment', 'emergencies and trauma too'],
  'eman': ['Emancipated minors', 'married, self-supporting or in the military', 'consent for themselves, like adults'],
  'par': ['Parents consent for a minor', 'laws vary by state · seek the minor’s assent even when not required', 'a pregnant 15-year-old decides about her own child'],
  'jw': ['Transfuse the bleeding child', 'a Jehovah’s Witness parent can’t refuse blood for a minor in an emergency', 'an adult with capacity who refuses blood is not transfused'],
}
cy = clues(C, SW, 180, ybot + 70, 2140, title='The rule')
PY = cy + 110; PANY = 660

# ════════ notes ════════
notes = {
  '': 'Who decides depends on three questions: is it an emergency, is the patient an adult, and does the patient have capacity for '
      'this decision now? Capacity is a physician’s judgment about one decision; competence is a judge’s.',
  'who:emerg': 'In an emergency with no one to ask, consent is implied — treat. Emergency is one of the WIPE exceptions to informed '
               'consent (Waiver, legally Incompetent, therapeutic Privilege, Emergency).',
  'who:pt': 'An adult with capacity decides — even to refuse. Consent needs disclosure, understanding, capacity and voluntariness, and '
            'the patient can revoke it at any time, even orally.',
  'who:priv': 'Therapeutic privilege lets you withhold information only when disclosure itself would severely harm the patient — not '
              'because the family asks.',
  'who:dir': 'Without capacity, follow the advance directive: a living will names specific interventions; a medical power of attorney '
             'names an agent and is more flexible. A DNR covers CPR only.',
  'who:surr': 'With no directive, a surrogate uses substituted judgment — what the patient would have wanted. Order: spouse, adult '
              'children, parents, adult siblings, other relatives.',
  'who:sdr': 'Minors can consent on their own for contraception, STIs, prenatal care (usually not abortion), substance use treatment, '
             'and emergencies — sex, drugs, rock and roll.',
  'who:eman': 'Emancipated minors — married, self-supporting or in the military — consent for themselves.',
  'who:par': 'Otherwise a parent consents for a minor, and the minor’s assent is still sought. A pregnant teenager decides about her '
             'own child, even if her parents disagree.',
  'who:jw': 'A parent can’t refuse lifesaving blood for a bleeding child — transfuse. An adult Jehovah’s Witness with capacity who '
            'refuses is not transfused.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='Who decides', type='one', options=[
    ['emerg', 'Emergency — implied consent', 'consent'], ['pt', 'Adult with capacity', 'consent'], ['priv', 'Therapeutic privilege', 'consent'],
    ['dir', 'Advance directive', 'advdir'], ['surr', 'Surrogate', 'surrogate'], ['sdr', 'Minor — sex, drugs, rock and roll', 'minors'],
    ['eman', 'Emancipated minor', 'minors'], ['par', 'Parents', 'minors'], ['jw', 'Parent refuses blood', 'minors']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=[],
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 267–273 (cards) · Kaplan & Sadock ch 27')

MAP = dict(
  id='ethicsim', title='Who Decides? Consent & Capacity', topic='stats', after='ethics',
  sub='Emergency, adult or minor, capacity or not, a directive or a surrogate — pick an answer and a dot follows the consent '
      'questions down the tree to who decides. Tap a card pin for the rule',
  w=3500, h=1660,
  fa='267–269, 272–273',
  src=[full('Kaplan & Sadock', 27), full('Kaplan & Sadock', 28), full('Kaplan & Sadock', 29)],
  lanes=[('ewAdult', 'Adults', 'glycolysis'), ('ewMinor', 'Minors', 'tca'), ('ewCore', 'Principles', 'gluconeo')],
  nodes=[
    ('ew1', 'Core ethical principles', 330, PY, 'ewCore', 'autonomy first', ['ethprinciples'], 'hub'),
    ('ew2', 'Informed consent', 760, PY, 'ewAdult', 'WIPE exceptions', ['consent']),
    ('ew3', 'Capacity', 1160, PY, 'ewAdult', 'four parts', ['capacity']),
    ('ew4', 'Advance directives', 1560, PY, 'ewAdult', 'living will · POA', ['advdir']),
    ('ew5', 'Surrogates', 1960, PY, 'ewAdult', 'substituted judgment', ['surrogate']),
    ('ew6', 'Minors', 330, PY + 130, 'ewMinor', 'exceptions', ['minors']),
    ('ew7', 'Confidentiality', 760, PY + 130, 'ewCore', 'SAVED exceptions', ['confid'])],
  panels=[
    (2420, PANY, 1000, 'Capacity (First Aid pp. 267–268)', [
      ('Four components', 'understanding · appreciation · reasoning · a choice'),
      ('Judged by', 'a physician, for one specific decision'),
      ('Competence', 'a legal ruling by a judge'),
      ('Mental illness', 'excludes capacity only if it impairs this decision')])],
  dyn=dyn)
