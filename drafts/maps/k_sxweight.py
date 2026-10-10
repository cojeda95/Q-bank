# Weight Loss (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it): appetite up (hyperthyroidism, type 1 diabetes) vs appetite down — night sweats (TB, Hodgkin), wasting
# (cachexia), adrenal insufficiency, malabsorption, mood and eating disorders. Readouts: appetite, TSH, glucose,
# Na⁺, K⁺. Clues come from the pinned cards (hyperthyroid, t1dm, tb, hodgkin, cachexia, addison, celiac, mdd,
# anorexia); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Unintended weight loss', 'is the appetite up or down?', None),
  ('up', 'r', 'eating more, still losing', 'Appetite up', 'burning or spilling fuel', None),
  ('hy', 'up', 'heat intolerance · tremor · palpitations', 'Hyperthyroidism', 'TSH ↓ · free T4 ↑', 'hyper'),
  ('dm', 'up', 'polyuria · polydipsia · young, thin', 'Type 1 diabetes', 'no insulin — glucose spilled', 't1dm'),
  ('dn', 'r', 'eating less', 'Appetite down', '', None),
  ('ns', 'dn', 'fever · night sweats', 'B symptoms', 'infection or lymphoma?', None),
  ('tb', 'ns', 'cough · hemoptysis · apical cavity', 'Tuberculosis', 'caseating granulomas', 'tb'),
  ('ho', 'ns', 'painless nodes · young adult', 'Hodgkin lymphoma', 'Reed-Sternberg cells', 'hodg'),
  ('cx', 'dn', 'known cancer or AIDS · muscle wasting', 'Cachexia', 'TNF-α from tumor and host', 'cach'),
  ('ad', 'dn', 'salt craving · dark creases · dizzy standing', 'Adrenal insufficiency', 'Na⁺ ↓ · K⁺ ↑', 'addi'),
  ('ce', 'dn', 'diarrhea · bloating · itchy vesicles', 'Celiac disease', 'malabsorption', 'celi'),
  ('ps', 'dn', 'mood or body image', 'Mind', '', None),
  ('md', 'ps', 'anhedonia · early waking · guilt', 'Major depressive disorder', 'SIG E CAPS', 'mdd'),
  ('an', 'ps', 'fear of weight gain · amenorrhea', 'Anorexia nervosa', 'BMI < 18.5', 'anor'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Weight loss — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'hyper': ['Hyperthyroidism — weight loss with a good appetite', 'heat intolerance, palpitations, tremor, anxiety, frequent stools', 'Graves: exophthalmos and pretibial myxedema · ↓ TSH, ↑ free T4'],
  't1dm': ['Type 1 diabetes — absolute insulin deficiency', 'polyuria, polydipsia, polyphagia and weight loss over weeks', 'glucose can’t enter muscle and fat; lipolysis runs on → ketones'],
  'tb': ['Tuberculosis', 'fever, night sweats, weight loss, cough, hemoptysis', 'reactivation favors the apices · caseating granulomas'],
  'hodg': ['Hodgkin lymphoma', 'B symptoms: fever, night sweats, weight loss · contiguous nodal spread', 'Reed-Sternberg cells, CD15 ⊕ CD30 ⊕ · bimodal age'],
  'cach': ['Cachexia — wasting driven by disease', 'cancer and AIDS: TNF-α and tumor factors waste muscle and fat', 'profound weakness, anorexia, anemia'],
  'addi': ['Adrenal insufficiency', 'fatigue, anorexia, weight loss, postural dizziness, salt craving', 'primary: hyperpigmentation · ↓ Na⁺, ↑ K⁺, hypoglycemia'],
  'celi': ['Celiac disease — malabsorption', 'diarrhea, bloating, weight loss; often only iron deficiency or osteoporosis', 'dermatitis herpetiformis · IgA anti-tTG (check total IgA)'],
  'mdd': ['Major depressive disorder', 'SIG E CAPS — Sleep, Interest, Guilt, Energy, Concentration, Appetite, Psychomotor, Suicide', 'check TSH and drugs that cause depression'],
  'anor': ['Anorexia nervosa', 'BMI under 18.5, fear of weight gain, distorted body image', 'amenorrhea (↓ GnRH), osteoporosis, lanugo, bradycardia'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='Appetite', mods=[dict(when=O('hyper', 't1dm'), d=1), dict(when=O('cach', 'addi'), d=-1)]),
  dict(l='TSH', mods=[dict(when=O('hyper'), d=-1)]),
  dict(l='Glucose', mods=[dict(when=O('t1dm'), d=1), dict(when=O('addi'), d=-1)]),
  dict(l='Na⁺', mods=[dict(when=O('addi'), d=-1)]),
  dict(l='K⁺', mods=[dict(when=O('addi'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Unintended weight loss: first ask whether the appetite is up (fuel burned or spilled — thyroid, diabetes) or down '
      '(infection, cancer, hormones, the gut, the mind). Night sweats point to TB or lymphoma.',
  'dx:hyper': 'Hyperthyroidism: weight loss with a good appetite, heat intolerance, palpitations, tremor and frequent stools. '
              '↓ TSH with ↑ free T4; exophthalmos and pretibial myxedema only in Graves.',
  'dx:t1dm': 'Type 1 diabetes: with no insulin, glucose can’t enter muscle and fat and lipolysis runs on — polyuria, polydipsia, '
             'polyphagia and weight loss over weeks, drifting toward DKA.',
  'dx:tb': 'Tuberculosis: fever, night sweats, weight loss, cough and hemoptysis; reactivation favors the apices and forms '
           'fibrocaseous cavities.',
  'dx:hodg': 'Hodgkin lymphoma: B symptoms (fever, night sweats, weight loss) with painless nodes spreading to contiguous groups. '
             'Reed-Sternberg cells are CD15 and CD30 positive.',
  'dx:cach': 'Cachexia: in cancer and AIDS, TNF-α and tumor factors waste muscle and fat — with anorexia, profound weakness and anemia.',
  'dx:addi': 'Adrenal insufficiency: fatigue, anorexia, weight loss, postural dizziness and salt craving. Primary disease adds '
             'hyperpigmentation, ↓ Na⁺, ↑ K⁺ and hypoglycemia; confirm with cosyntropin.',
  'dx:celi': 'Celiac disease: diarrhea, bloating and weight loss — or just iron deficiency or osteoporosis in an adult. Screen '
             'with IgA anti-tissue transglutaminase and check total IgA.',
  'dx:mdd': 'Major depressive disorder changes appetite and weight with depressed mood or anhedonia for 2 weeks or more '
            '(SIG E CAPS). Check TSH and the drug list.',
  'dx:anor': 'Anorexia nervosa: BMI under 18.5 with fear of weight gain. Starvation lowers leptin and GnRH — amenorrhea and '
             'bone loss — with lanugo, bradycardia and hypothermia.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['hyper', 'Hyperthyroidism', 'hyperthyroid'], ['t1dm', 'Type 1 diabetes', 't1dm'], ['tb', 'Tuberculosis', 'tb'],
    ['hodg', 'Hodgkin lymphoma', 'hodgkin'], ['cach', 'Cachexia (cancer, AIDS)', 'cachexia'], ['addi', 'Adrenal insufficiency', 'addison'],
    ['celi', 'Celiac disease', 'celiac'], ['mdd', 'Major depression', 'mdd'], ['anor', 'Anorexia nervosa', 'anorexia']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 106, 138, 346, 350, 353, 388, 434, 578, 584 (cards)')

MAP = dict(
  id='sxweight', title='Weight Loss', topic='sx', after='sxams',
  sub='Appetite up or down, then the clue that splits each branch — a dot follows the case down the tree to thyroid, '
      'diabetes, TB, lymphoma, cachexia, the adrenals, the gut or the mind, while the readouts show TSH, glucose, Na⁺ and K⁺',
  w=3500, h=1640,
  fa='106, 138, 172–173, 193, 197, 346, 350, 353, 388, 434, 578, 584',
  src=[full('Robbins', 24), full('Robbins', 8), full('Robbins', 13), full('Robbins', 7), full('Robbins', 17), full('Kaplan & Sadock', 7),
       full('Kaplan & Sadock', 13)],
  lanes=[('xwHorm', 'Hormones', 'glycolysis'), ('xwInf', 'Infection & cancer', 'tca'), ('xwGut', 'Gut & mind', 'gluconeo')],
  nodes=[
    ('xw1', 'Hyperthyroidism', 330, PY, 'xwHorm', 'good appetite', ['hyperthyroid'], 'hub'),
    ('xw2', 'Type 1 diabetes', 760, PY, 'xwHorm', 'polyuria · polydipsia', ['t1dm']),
    ('xw3', 'Adrenal insufficiency', 1180, PY, 'xwHorm', 'Na⁺ ↓ · K⁺ ↑', ['addison']),
    ('xw4', 'Tuberculosis', 1600, PY, 'xwInf', 'night sweats', ['tb']),
    ('xw5', 'Hodgkin · HIV', 2000, PY, 'xwInf', 'B symptoms', ['hodgkin', 'hiv']),
    ('xw6', 'Cachexia', 330, PY + 130, 'xwInf', 'TNF-α', ['cachexia']),
    ('xw7', 'Celiac · malabsorption', 760, PY + 130, 'xwGut', 'diarrhea', ['celiac', 'malabs']),
    ('xw8', 'Depression', 1180, PY + 130, 'xwGut', 'SIG E CAPS', ['mdd']),
    ('xw9', 'Anorexia nervosa', 1600, PY + 130, 'xwGut', 'BMI < 18.5', ['anorexia'])],
  panels=[
    (2420, PANY, 1000, 'One clue each (cards)', [
      ('Appetite up', 'hyperthyroidism · type 1 diabetes'),
      ('Night sweats', 'tuberculosis · Hodgkin lymphoma'),
      ('Salt craving, dark creases', 'primary adrenal insufficiency'),
      ('Itchy vesicles on extensors', 'celiac disease (dermatitis herpetiformis)')])],
  dyn=dyn)
