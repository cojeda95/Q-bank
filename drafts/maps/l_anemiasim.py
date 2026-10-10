# Anemia Work-Up (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The anemia algorithm drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot
# travels it): MCV first, then iron studies (microcytic), the reticulocyte index (normocytic) or methylmalonic acid
# (macrocytic). Readouts: MCV, reticulocyte index, ferritin, TIBC, LDH, methylmalonic acid — each arrow is the one
# on the pinned card (anemiaapproach, ironstudies, reticindex, ida, acd, betathal, lead, sidero, aplastic,
# ckdanemia, hemolysislabs, hs, g6pd, warmaiha, b12def, b9def); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Anemia', 'MCV first', None),
  ('mi', 'r', 'MCV < 80 fL', 'Microcytic', 'heme or globin failed — iron studies', None),
  ('id', 'mi', 'ferritin ↓ · TIBC ↑', 'Iron deficiency', 'look for GI or menstrual loss', 'ida'),
  ('cd', 'mi', 'ferritin ↑ · TIBC ↓', 'Anemia of chronic disease', 'hepcidin locks iron away', 'acd'),
  ('th', 'mi', 'iron studies normal · target cells', 'β-Thalassemia minor', 'HbA2 ↑ · Mentzer < 13', 'thal'),
  ('pb', 'mi', 'basophilic stippling · colic', 'Lead poisoning', 'ALA dehydratase + ferrochelatase', 'lead'),
  ('sb', 'mi', 'iron ↑ · ringed sideroblasts', 'Sideroblastic anemia', 'ALA synthase · alcohol, isoniazid', 'sidero'),
  ('no', 'r', 'MCV 80–100 fL', 'Normocytic', 'too few — reticulocyte index?', None),
  ('lo', 'no', 'index < 2', 'Marrow not keeping up', '', None),
  ('ap', 'lo', 'pancytopenia · no splenomegaly', 'Aplastic anemia', 'empty, fatty marrow', 'aplastic'),
  ('ck', 'lo', 'low GFR · EPO low for the anemia', 'Chronic kidney disease', 'EPO not made', 'ckd'),
  ('hi', 'no', 'index > 3 · LDH ↑ · indirect bili ↑', 'Hemolysis', '', None),
  ('hs', 'hi', 'spherocytes · Coombs negative', 'Hereditary spherocytosis', 'spectrin, ankyrin', 'hs'),
  ('g6', 'hi', 'days after an oxidant · bite cells', 'G6PD deficiency', 'Heinz bodies', 'g6pd'),
  ('ai', 'hi', 'spherocytes · Coombs positive', 'Warm autoimmune hemolysis', 'IgG on the red cell', 'aiha'),
  ('ma', 'r', 'MCV > 100 fL', 'Macrocytic', 'DNA synthesis failed — methylmalonic acid?', None),
  ('b1', 'ma', 'MMA ↑ · neuro signs', 'B12 deficiency', 'subacute combined degeneration', 'b12'),
  ('fo', 'ma', 'MMA normal · no neuro signs', 'Folate deficiency', 'alcohol · pregnancy · drugs', 'fol'),
]
pos, flows, ybot = tree(T, SW, Y0=260, DY=88)
text('Anemia — MCV first, then the test that splits each branch', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'ida': ['Iron deficiency anemia', 'ferritin ↓, serum iron ↓, TIBC ↑, saturation ↓↓ · ↑ RDW, ↑ FEP', 'men and postmenopausal women: look for occult GI bleeding'],
  'acd': ['Anemia of chronic disease', 'IL-6 → hepcidin → ferroportin degraded → iron locked in macrophages', 'ferritin ↑, TIBC ↓ · normocytic early, microcytic late'],
  'thal': ['β-Thalassemia minor', 'mild microcytic anemia with normal iron studies · target cells', 'HbA2 ↑ (4–8%) · Mentzer index under 13'],
  'lead': ['Lead poisoning', 'inhibits ALA dehydratase and ferrochelatase · basophilic stippling', 'children: encephalopathy, Burton lines · adults: colic, wrist and foot drop'],
  'sidero': ['Sideroblastic anemia', 'ALA synthase fails (X-linked, alcohol, lead, isoniazid) — iron stranded in mitochondria', 'ringed sideroblasts · iron, ferritin and saturation ↑'],
  'aplastic': ['Aplastic anemia', 'pancytopenia: fatigue, bleeding, infection · no splenomegaly', 'hypocellular, fatty marrow · drugs, viruses, radiation, Fanconi'],
  'ckd': ['Anemia of chronic kidney disease', 'peritubular fibroblasts make too little erythropoietin', 'normocytic, ↓ reticulocytes · check iron too'],
  'hs': ['Hereditary spherocytosis — extravascular hemolysis', 'spherocytes, ↑ MCHC, splenomegaly, pigment gallstones', 'EMA binding ↓ · Coombs negative'],
  'g6pd': ['G6PD deficiency — oxidant hemolysis', 'a few days after an oxidant: back pain, dark urine', 'Heinz bodies, bite cells · ↓ haptoglobin'],
  'aiha': ['Warm autoimmune hemolytic anemia', 'IgG coats the red cell — SLE, CLL, drugs (α-methyldopa, β-lactams)', 'direct Coombs positive · spherocytes'],
  'b12': ['B12 deficiency', 'megaloblastic anemia, hypersegmented neutrophils, glossitis', 'subacute combined degeneration · MMA ↑ and homocysteine ↑'],
  'fol': ['Folate deficiency', 'megaloblastic anemia without neurologic findings', 'homocysteine ↑ with normal MMA · stores last 3–4 months'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 700

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='MCV', mods=[dict(when=O('ida', 'acd', 'thal', 'lead', 'sidero'), d=-1), dict(when=O('aplastic', 'ckd', 'hs', 'g6pd', 'aiha'), d=0),
                      dict(when=O('b12', 'fol'), d=1)]),
  dict(l='Reticulocyte index', mods=[dict(when=O('ida', 'aplastic', 'ckd'), d=-1), dict(when=O('hs', 'g6pd', 'aiha'), d=1)]),
  dict(l='Ferritin', mods=[dict(when=O('ida'), d=-1), dict(when=O('acd', 'sidero'), d=1), dict(when=O('thal'), d=0)]),
  dict(l='TIBC', mods=[dict(when=O('ida'), d=1), dict(when=O('acd'), d=-1), dict(when=O('thal'), d=0)]),
  dict(l='LDH', mods=[dict(when=O('hs', 'g6pd', 'aiha'), d=1)]),
  dict(l='Methylmalonic acid', mods=[dict(when=O('b12'), d=1), dict(when=O('fol'), d=0)]),
]

# ════════ notes ════════
notes = {
  '': 'Anemia is a number, not a diagnosis. The MCV sorts it: microcytic (hemoglobin synthesis failed), normocytic (too few '
      'correct cells — is the marrow failing or racing?) or macrocytic (DNA synthesis failed).',
  'dx:ida': 'Iron deficiency: stores empty first (ferritin ↓), then serum iron; the liver makes more transferrin, so TIBC rises — '
            'the best discriminator from chronic disease. In men and postmenopausal women, look for GI blood loss.',
  'dx:acd': 'Anemia of chronic disease: IL-6 drives hepcidin, which degrades ferroportin and locks iron inside macrophages. '
            'Ferritin is high, TIBC low — normocytic early, microcytic only if it persists.',
  'dx:thal': 'β-Thalassemia minor: a mild microcytic anemia with normal iron studies, target cells and a raised HbA2. A Mentzer '
             'index (MCV ÷ RBC count) under 13 favors thalassemia.',
  'dx:lead': 'Lead blocks ALA dehydratase and ferrochelatase and leaves ribosomal remnants — basophilic stippling. Children get '
             'encephalopathy and Burton lines; adults get colic and wrist or foot drop.',
  'dx:sidero': 'Sideroblastic anemia: ALA synthase, the first heme step, fails, so iron is stranded in mitochondria as ringed '
               'sideroblasts. Iron, ferritin and saturation are high — the opposite of iron deficiency.',
  'dx:aplastic': 'Aplastic anemia: stem cells fail — pancytopenia with a hypocellular, fatty marrow and a low reticulocyte count, '
                 'and no splenomegaly or lymphadenopathy.',
  'dx:ckd': 'Anemia of chronic kidney disease: peritubular fibroblasts make too little erythropoietin, so a normocytic anemia '
            'deepens as GFR falls; reticulocytes are low.',
  'dx:hs': 'Hereditary spherocytosis: spectrin or ankyrin defects make spherocytes that the spleen removes — extravascular '
           'hemolysis, ↑ MCHC, Coombs negative, ↓ EMA binding.',
  'dx:g6pd': 'G6PD deficiency: without NADPH, red cells can’t handle an oxidant — hemolysis a few days later with Heinz bodies, bite '
             'cells, ↑ LDH and ↓ haptoglobin.',
  'dx:aiha': 'Warm autoimmune hemolytic anemia: IgG on the red cell, a positive direct Coombs test and spherocytes — with SLE, CLL '
             'or drugs such as α-methyldopa.',
  'dx:b12': 'B12 deficiency: methionine synthase fails (megaloblastic anemia) and methylmalonyl-CoA mutase fails (MMA ↑, myelin '
            'damage) — subacute combined degeneration.',
  'dx:fol': 'Folate deficiency: the same megaloblastic anemia but no neurologic signs and a normal MMA (homocysteine still rises). '
            'Stores last only months — alcohol, pregnancy, phenytoin, methotrexate.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['ida', 'Iron deficiency', 'ida'], ['acd', 'Anemia of chronic disease', 'acd'], ['thal', 'β-Thalassemia minor', 'betathal'],
    ['lead', 'Lead poisoning', 'lead'], ['sidero', 'Sideroblastic anemia', 'sidero'], ['aplastic', 'Aplastic anemia', 'aplastic'],
    ['ckd', 'Chronic kidney disease', 'ckdanemia'], ['hs', 'Hereditary spherocytosis', 'hs'], ['g6pd', 'G6PD deficiency', 'g6pd'],
    ['aiha', 'Warm AIHA', 'warmaiha'], ['b12', 'B12 deficiency', 'b12def'], ['fol', 'Folate deficiency', 'b9def']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 67, 422–430 (cards) · Robbins ch 14')

MAP = dict(
  id='anemiasim', title='Anemia Work-Up', topic='heme', after='rbc',
  sub='MCV first, then iron studies, the reticulocyte index or methylmalonic acid — pick an answer and a dot follows the '
      'algorithm down the tree while the readouts show the MCV, reticulocytes, ferritin, TIBC, LDH and MMA that go with it',
  w=3500, h=1830,
  fa='67, 77, 96, 209, 402, 413, 420, 422–430',
  src=[full('Robbins', 14), full('Katzung', 33), full('Marks', 42)],
  lanes=[('anMicro', 'Microcytic', 'glycolysis'), ('anNormo', 'Normocytic', 'tca'), ('anMacro', 'Macrocytic', 'gluconeo')],
  nodes=[
    ('an1', 'Classifying anemia', 330, PY, 'anNormo', 'MCV · reticulocytes', ['anemiaapproach', 'reticindex'], 'hub'),
    ('an2', 'Iron studies', 760, PY, 'anMicro', 'ferritin first', ['ironstudies', 'ida', 'acd']),
    ('an3', 'Thalassemias', 1180, PY, 'anMicro', 'globin chains', ['betathal', 'alphathal']),
    ('an4', 'Lead · sideroblastic', 1600, PY, 'anMicro', 'heme synthesis', ['lead', 'sidero']),
    ('an5', 'Underproduction', 2000, PY, 'anNormo', 'index < 2', ['aplastic', 'ckdanemia']),
    ('an6', 'Hemolysis', 330, PY + 130, 'anNormo', 'index > 3', ['hemolysislabs', 'hs', 'g6pd', 'warmaiha']),
    ('an7', 'B12 · folate', 780, PY + 130, 'anMacro', 'megaloblastic', ['b12def', 'b9def'])],
  panels=[
    (2420, PANY, 1000, 'Iron studies (First Aid pp. 423–425)', [
      ('Iron deficiency', 'iron ↓ · TIBC ↑ · ferritin ↓ · saturation ↓↓'),
      ('Chronic disease', 'iron ↓ · TIBC ↓ · ferritin ↑'),
      ('Sideroblastic', 'iron ↑ · ferritin ↑ · saturation ↑'),
      ('Thalassemia trait', 'normal'),
      ('Hemochromatosis', 'iron ↑ · TIBC ↓ · ferritin ↑ · saturation ↑↑')])],
  dyn=dyn)
