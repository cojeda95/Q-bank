# GI Bleeding (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it): above or below the ligament of Treitz, then the clue that names the source. Readouts: BUN:Cr, hemoglobin,
# platelets, PT. Clues come from the pinned cards (gibleed, pud, cirrhosis, mallorywb, diverticular, angiodysplasia,
# meckel, hemorrhoids, crc, crohn); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Blood from the gut', 'above or below the ligament of Treitz?', None),
  ('up', 'r', 'hematemesis · melena · BUN:Cr > 20', 'Upper GI bleed', 'esophagus, stomach, duodenum', None),
  ('pu', 'up', 'epigastric pain · NSAIDs · H pylori', 'Peptic ulcer', 'the commonest complication', 'pud'),
  ('va', 'up', 'cirrhosis · caput medusae · splenomegaly', 'Esophageal varices', 'portal hypertension', 'var'),
  ('mw', 'up', 'after violent retching', 'Mallory-Weiss tear', 'mucosal, at the GE junction', 'mw'),
  ('lo', 'r', 'hematochezia', 'Lower GI bleed', 'colon, rectum, anus — or Meckel', None),
  ('pl', 'lo', 'no pain', 'Painless bleeding', 'how old? what else?', None),
  ('dv', 'pl', 'over 60 · low-fiber diet', 'Diverticulosis', 'sigmoid · vasa recta', 'div'),
  ('ag', 'pl', 'aortic stenosis · ESRD · von Willebrand', 'Angiodysplasia', 'right colon', 'angio'),
  ('me', 'pl', 'a young child', 'Meckel diverticulum', 'ectopic gastric mucosa', 'meck'),
  ('ih', 'pl', 'bright red on the paper', 'Internal hemorrhoids', 'above the pectinate line', 'hem'),
  ('ot', 'lo', 'with anemia, weight loss or diarrhea', 'Bleeding with a story', '', None),
  ('cr', 'ot', 'over 50 · iron deficiency · weight loss', 'Colorectal cancer', 'right: occult · left: obstruction', 'crc'),
  ('uc', 'ot', 'bloody diarrhea · from the rectum up', 'Ulcerative colitis', 'continuous, mucosal', 'uc'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('GI bleeding — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'pud': ['Peptic ulcer disease', 'H pylori or NSAIDs · bleeding is the commonest complication', 'posterior duodenal ulcer → gastroduodenal artery · lesser curvature → left gastric'],
  'var': ['Esophageal varices — portal hypertension', 'cirrhosis: caput medusae, splenomegaly, ascites, spider angiomas', 'nonselective β-blockers prevent the bleed · low platelets, long PT'],
  'mw': ['Mallory-Weiss tear', 'longitudinal mucosal tear at the GE junction after retching → hematemesis', 'alcohol use disorder, bulimia · Boerhaave is the full-thickness rupture'],
  'div': ['Diverticulosis — diverticular bleeding', 'painless hematochezia; about half of people over 60 have diverticula', 'false diverticula where the vasa recta pierce the wall · diverticulitis rarely bleeds'],
  'angio': ['Angiodysplasia', 'painless hematochezia from dilated submucosal vessels, often the right colon', 'with aortic stenosis, end-stage renal disease, von Willebrand disease'],
  'meck': ['Meckel diverticulum', 'painless hematochezia or melena in a child under 2', 'ectopic gastric mucosa ulcerates the ileum · technetium-99m pertechnetate scan'],
  'hem': ['Internal hemorrhoids', 'painless bleeding — above the pectinate line, visceral innervation', 'external hemorrhoids and fissures (below the line) hurt'],
  'crc': ['Colorectal cancer', 'right side: occult bleeding, iron deficiency anemia, weight loss', 'left side: obstruction, hematochezia, narrow stools · iron deficiency in a man → colonoscopy'],
  'uc': ['Ulcerative colitis', 'continuous mucosal inflammation from the rectum up · bloody diarrhea', 'crypt abscesses, pseudopolyps · PSC, p-ANCA · ↑ platelets in activity'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
ALL = O('pud', 'var', 'mw', 'div', 'angio', 'meck', 'hem', 'crc', 'uc')
readouts = [
  dict(l='BUN : creatinine', mods=[dict(when=O('pud', 'var', 'mw'), d=1)]),
  dict(l='Hemoglobin', mods=[dict(when=ALL, d=-1)]),
  dict(l='Platelets', mods=[dict(when=O('var'), d=-1), dict(when=O('uc'), d=1)]),
  dict(l='PT', mods=[dict(when=O('var'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'GI bleeding: the ligament of Treitz divides upper (hematemesis, melena, BUN:Cr over 20) from lower (hematochezia). '
      'Then age, pain and the company the bleeding keeps name the source.',
  'dx:pud': 'Peptic ulcer disease is the classic upper bleed — H pylori or NSAIDs. A posterior duodenal ulcer erodes the '
            'gastroduodenal artery; a lesser-curvature gastric ulcer, the left gastric.',
  'dx:var': 'Esophageal varices: portal hypertension from cirrhosis opens portosystemic collaterals. Low platelets (spleen) and a '
            'long PT (lost synthesis) come with it; nonselective β-blockers prevent the bleed.',
  'dx:mw': 'Mallory-Weiss tear: violent retching tears the mucosa at the GE junction → hematemesis. A full-thickness rupture with '
           'mediastinal air is Boerhaave syndrome.',
  'dx:div': 'Diverticulosis: painless hematochezia in an older adult from false diverticula where the vasa recta enter the wall. '
            'Diverticulitis — LLQ pain, fever — rarely bleeds.',
  'dx:angio': 'Angiodysplasia: painless, intermittent bleeding from dilated submucosal vessels, often in the right colon — linked '
              'to aortic stenosis, end-stage renal disease and von Willebrand disease.',
  'dx:meck': 'Meckel diverticulum: painless bleeding in a young child from ectopic gastric mucosa ulcerating the ileum — the rule '
             'of 2s; a technetium-99m pertechnetate scan finds it.',
  'dx:hem': 'Internal hemorrhoids sit above the pectinate line, where innervation is visceral — so they bleed painlessly. External '
            'hemorrhoids and anal fissures lie below it and hurt.',
  'dx:crc': 'Colorectal cancer: right-sided tumors bleed occultly (iron deficiency, weight loss); left-sided ones obstruct and '
            'cause hematochezia. Iron deficiency in a man or postmenopausal woman means colonoscopy.',
  'dx:uc': 'Ulcerative colitis: continuous mucosal inflammation from the rectum upward with bloody diarrhea, crypt abscesses and '
           'pseudopolyps; reactive thrombocytosis marks activity.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['pud', 'Peptic ulcer', 'pud'], ['var', 'Esophageal varices', 'cirrhosis'], ['mw', 'Mallory-Weiss tear', 'mallorywb'],
    ['div', 'Diverticulosis', 'diverticular'], ['angio', 'Angiodysplasia', 'angiodysplasia'], ['meck', 'Meckel diverticulum', 'meckel'],
    ['hem', 'Internal hemorrhoids', 'hemorrhoids'], ['crc', 'Colorectal cancer', 'crc'], ['uc', 'Ulcerative colitis', 'crohn']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 373, 384, 387–397 (cards) · Robbins ch 17')

MAP = dict(
  id='sxgibleed', title='GI Bleeding', topic='sx', after='sxabdpain',
  sub='Above or below the ligament of Treitz, then the clue that names the source — a dot follows the case down the tree '
      'while the readouts show BUN:Cr, hemoglobin, platelets and PT',
  w=3500, h=1640,
  fa='244, 372–373, 384, 386–387, 389–391, 393, 395–397, 423–424',
  src=[full('Robbins', 17), full('Robbins', 18), full('Costanzo', 8), full('Robbins', 14)],
  lanes=[('xgUp', 'Upper GI', 'glycolysis'), ('xgLow', 'Lower GI', 'tca'), ('xgWork', 'Work-up', 'gluconeo')],
  nodes=[
    ('xg1', 'Upper vs lower bleeding', 330, PY, 'xgWork', 'ligament of Treitz', ['gibleed'], 'hub'),
    ('xg2', 'Peptic ulcer · gastritis', 780, PY, 'xgUp', 'H pylori · NSAIDs', ['pud', 'gastritis']),
    ('xg3', 'Varices', 1200, PY, 'xgUp', 'portal hypertension', ['cirrhosis']),
    ('xg4', 'Mallory-Weiss', 1600, PY, 'xgUp', 'after retching', ['mallorywb']),
    ('xg5', 'Diverticulosis', 2000, PY, 'xgLow', 'painless, older', ['diverticular']),
    ('xg6', 'Angiodysplasia · Meckel', 330, PY + 130, 'xgLow', 'painless', ['angiodysplasia', 'meckel']),
    ('xg7', 'Hemorrhoids', 780, PY + 130, 'xgLow', 'pectinate line', ['hemorrhoids']),
    ('xg8', 'Colorectal cancer', 1200, PY + 130, 'xgLow', 'iron deficiency', ['crc', 'ida']),
    ('xg9', 'IBD', 1600, PY + 130, 'xgLow', 'bloody diarrhea', ['crohn'])],
  panels=[
    (2420, PANY, 1000, 'Upper vs lower (First Aid p. 387)', [
      ('Upper', 'hematemesis, melena · BUN:Cr > 20'),
      ('Lower', 'hematochezia'),
      ('Upper sources', 'ulcer · varices · Mallory-Weiss · gastritis'),
      ('Lower sources', 'diverticula · angiodysplasia · IBD · cancer · Meckel')])],
  dyn=dyn)
