# Liver Tests Decoder (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Liver enzyme patterns drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot
# travels it): bilirubin alone (which fraction?), a hepatocellular pattern (how high, what ratio, which antibody?)
# or a cholestatic one (stone, PBC, PSC — or bone). Readouts: ALT/AST, AST:ALT, ALP, GGT, direct and indirect
# bilirubin — each arrow from the pinned card (lfts, jaundice, bilirubin, hemolysislabs, acetaminophen, hav, hbv,
# ald, masld, aih, gallstones, pbc, psc); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Abnormal liver tests', 'which numbers rose?', None),
  ('bi', 'r', 'bilirubin up, enzymes normal', 'Bilirubin only', 'which fraction?', None),
  ('gi', 'bi', 'unconjugated · fasting, illness, stress', 'Gilbert syndrome', 'mildly ↓ UGT — benign', 'gil'),
  ('he', 'bi', 'unconjugated · anemia · retics ↑', 'Hemolysis', 'too much bilirubin made', 'hemol'),
  ('dj', 'bi', 'conjugated · black liver', 'Dubin-Johnson syndrome', 'MRP2 excretion defect', 'dj'),
  ('hc', 'r', 'ALT and AST lead', 'Hepatocellular pattern', 'how high, what ratio?', None),
  ('ap', 'hc', 'thousands · after an overdose', 'Acetaminophen toxicity', 'NAPQI · glutathione gone', 'apap'),
  ('vi', 'hc', 'thousands · jaundice after a prodrome', 'Acute viral hepatitis', 'HAV · HBV', 'viral'),
  ('al', 'hc', 'AST : ALT > 2 · AST < 500', 'Alcoholic hepatitis', 'GGT ↑ · macrocytosis', 'alc'),
  ('ms', 'hc', 'ALT > AST, mild · obesity', 'MASLD', 'insulin resistance', 'masld'),
  ('ai', 'hc', 'anti-smooth muscle · ANA · IgG ↑', 'Autoimmune hepatitis', 'young woman', 'aih'),
  ('cs', 'r', 'ALP and GGT lead', 'Cholestatic pattern', 'where is bile stuck?', None),
  ('cd', 'cs', 'RUQ pain · stone on ultrasound', 'Choledocholithiasis', 'a stone in the CBD', 'stone'),
  ('pb', 'cs', 'middle-aged woman · itch · AMA', 'Primary biliary cholangitis', 'small ducts', 'pbc'),
  ('ps', 'cs', 'man with ulcerative colitis · beaded ducts', 'Primary sclerosing cholangitis', 'onion-skin fibrosis', 'psc'),
  ('bo', 'r', 'ALP up, GGT normal', 'Not the liver — bone', 'GGT stays normal', 'bone'),
]
pos, flows, ybot = tree(T, SW, Y0=260, DY=90)
text('Liver tests — read the pattern down the tree', 180, 160, 'dyn-big')
text('aminotransferases leak from hepatocytes · ALP and GGT rise when bile can’t flow · albumin and PT show what the liver still makes', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'gil': ['Gilbert syndrome', 'mildly ↓ UGT activity: jaundice with fasting, illness, stress, exertion', 'unconjugated bilirubin only; otherwise normal liver tests — benign'],
  'hemol': ['Hemolysis — prehepatic', 'more heme broken down than the liver can conjugate', 'unconjugated bilirubin, LDH and reticulocytes ↑'],
  'dj': ['Dubin-Johnson syndrome', 'defective hepatic excretion (MRP2) → conjugated hyperbilirubinemia', 'grossly black liver · Rotor is the same without the black liver'],
  'apap': ['Acetaminophen toxicity', 'nausea first; liver injury shows up days later', 'AST and ALT in the thousands, ↑ INR · N-acetylcysteine'],
  'viral': ['Acute viral hepatitis', 'HAV: jaundice, malaise, RUQ pain, ↑ ALT · HBV: serum sickness–like prodrome', 'IgM anti-HAV · HBsAg, anti-HBc IgM'],
  'alc': ['Alcoholic hepatitis', 'AST : ALT over 2 : 1, aminotransferases usually under 500', '↑ GGT, macrocytosis · Mallory bodies, neutrophils'],
  'masld': ['Steatotic liver disease (MASLD)', 'obesity, insulin resistance, high triglycerides, low HDL', 'mild ALT > AST · AST > ALT suggests advanced fibrosis'],
  'aih': ['Autoimmune hepatitis', 'ALT and AST ↑ · anti-smooth muscle or anti-LKM-1, ANA', 'hypergammaglobulinemia (IgG) · plasma cells in the infiltrate'],
  'stone': ['Choledocholithiasis — a stone in the common bile duct', '↑ ALP, GGT, direct bilirubin and aminotransferases', 'ultrasound first · can cause pancreatitis and cholangitis'],
  'pbc': ['Primary biliary cholangitis', 'middle-aged woman, pruritus and fatigue, jaundice later', 'antimitochondrial antibody · ↑ ALP, IgM, cholesterol'],
  'psc': ['Primary sclerosing cholangitis', 'middle-aged man with ulcerative colitis · beaded ducts on MRCP or ERCP', 'p-ANCA · ↑ cholangiocarcinoma risk'],
  'bone': ['ALP from bone, not liver', 'ALP up with a normal GGT points to bone', 'GGT rises only with cholestasis or infiltration'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 700

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='ALT · AST', mods=[dict(when=O('apap', 'viral', 'alc', 'masld', 'aih', 'stone'), d=1), dict(when=O('gil', 'dj'), d=0)]),
  dict(l='AST : ALT ratio', mods=[dict(when=O('alc'), d=1), dict(when=O('masld'), d=-1)]),
  dict(l='ALP', mods=[dict(when=O('stone', 'pbc', 'psc', 'bone'), d=1), dict(when=O('gil', 'dj'), d=0)]),
  dict(l='GGT', mods=[dict(when=O('stone', 'pbc', 'psc', 'alc'), d=1), dict(when=O('bone'), d=0)]),
  dict(l='Direct bilirubin', mods=[dict(when=O('dj', 'stone'), d=1), dict(when=O('gil', 'hemol'), d=0)]),
  dict(l='Indirect bilirubin', mods=[dict(when=O('gil', 'hemol'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Read liver tests as a pattern: aminotransferases leak from injured hepatocytes (hepatocellular), ALP and GGT rise when bile '
      'can’t flow (cholestatic), and bilirubin alone points before or after conjugation.',
  'dx:gil': 'Gilbert syndrome: mildly reduced UGT activity gives an isolated unconjugated hyperbilirubinemia with fasting, illness or '
            'stress — every other liver test is normal. Benign.',
  'dx:hemol': 'Hemolysis makes more bilirubin than the liver can conjugate — unconjugated bilirubin rises with LDH and reticulocytes, '
              'while the liver enzymes stay normal.',
  'dx:dj': 'Dubin-Johnson syndrome: hepatic excretion (MRP2) fails, so conjugated bilirubin rises with otherwise normal tests and a '
           'grossly black liver. Rotor syndrome looks the same without the black liver.',
  'dx:apap': 'Acetaminophen overdose: NAPQI builds up once glutathione runs out. Nausea first, then AST and ALT in the thousands '
             'with a rising INR days later. N-acetylcysteine replenishes glutathione.',
  'dx:viral': 'Acute viral hepatitis drives aminotransferases into the thousands, ALT usually above AST. IgM anti-HAV marks acute '
              'hepatitis A; HBsAg and anti-HBc IgM, acute hepatitis B.',
  'dx:alc': 'Alcoholic hepatitis: AST more than twice ALT, with aminotransferases only modestly raised (usually under 500), GGT up '
            'and macrocytosis — make a toAST with alcohol.',
  'dx:masld': 'MASLD: insulin resistance fills hepatocytes with fat — mild enzyme rises with ALT above AST. A flip to AST above ALT '
              'suggests advanced fibrosis.',
  'dx:aih': 'Autoimmune hepatitis: raised ALT and AST with anti-smooth muscle (type 1, with ANA) or anti-LKM-1 (type 2) antibodies, '
            'high IgG and plasma cells in the infiltrate.',
  'dx:stone': 'Choledocholithiasis: a stone in the common bile duct raises ALP, GGT, direct bilirubin and the aminotransferases. '
              'Ultrasound first; it can cause pancreatitis and cholangitis.',
  'dx:pbc': 'Primary biliary cholangitis: autoimmune destruction of small intralobular ducts in a middle-aged woman — itch and '
            'fatigue, antimitochondrial antibody, ↑ ALP and IgM.',
  'dx:psc': 'Primary sclerosing cholangitis: onion-skin fibrosis beads the large ducts in a man with ulcerative colitis — p-ANCA, '
            'cholestatic enzymes, cholangiocarcinoma risk.',
  'dx:bone': 'ALP rises with a normal GGT: the ALP is coming from bone. GGT rises only when bile flow is blocked or the liver is '
             'infiltrated.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['gil', 'Gilbert syndrome', 'bilirubin'], ['hemol', 'Hemolysis', 'hemolysislabs'], ['dj', 'Dubin-Johnson', 'bilirubin'],
    ['apap', 'Acetaminophen toxicity', 'acetaminophen'], ['viral', 'Acute viral hepatitis', 'hav'], ['alc', 'Alcoholic hepatitis', 'ald'],
    ['masld', 'MASLD', 'masld'], ['aih', 'Autoimmune hepatitis', 'aih'], ['stone', 'Choledocholithiasis', 'gallstones'],
    ['pbc', 'Primary biliary cholangitis', 'pbc'], ['psc', 'Primary sclerosing cholangitis', 'psc'], ['bone', 'Bone (ALP alone)', 'lfts']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 170, 397–403 (cards) · Robbins ch 18')

MAP = dict(
  id='lftsim', title='Liver Tests Decoder', topic='gi', after='liver',
  sub='Bilirubin alone, a hepatocellular pattern or a cholestatic one — pick an answer and a dot follows the pattern down '
      'the tree while the readouts show ALT/AST, the AST:ALT ratio, ALP, GGT and both bilirubin fractions',
  w=3500, h=1900,
  fa='73, 170–172, 222, 397–403, 425, 427, 495, 588',
  src=[full('Robbins', 18), full('Robbins', 14), full('Marks', 33), full('Katzung', 49)],
  lanes=[('lfBili', 'Bilirubin', 'glycolysis'), ('lfHep', 'Hepatocellular', 'tca'), ('lfChol', 'Cholestatic', 'gluconeo')],
  nodes=[
    ('lf1', 'Liver enzymes', 330, PY, 'lfHep', 'reading the pattern', ['lfts'], 'hub'),
    ('lf2', 'Jaundice', 740, PY, 'lfBili', 'which fraction?', ['jaundice', 'bilirubin']),
    ('lf3', 'Hemolysis', 1120, PY, 'lfBili', 'prehepatic', ['hemolysislabs']),
    ('lf4', 'Acetaminophen', 1500, PY, 'lfHep', 'thousands', ['acetaminophen']),
    ('lf5', 'Viral hepatitis', 1900, PY, 'lfHep', 'HAV · HBV', ['hav', 'hbv']),
    ('lf6', 'Alcohol · MASLD', 330, PY + 130, 'lfHep', 'the ratio', ['ald', 'masld']),
    ('lf7', 'Autoimmune hepatitis', 760, PY + 130, 'lfHep', 'anti-smooth muscle', ['aih']),
    ('lf8', 'Gallstones', 1180, PY + 130, 'lfChol', 'CBD stone', ['gallstones']),
    ('lf9', 'PBC · PSC', 1580, PY + 130, 'lfChol', 'AMA · p-ANCA', ['pbc', 'psc'])],
  panels=[
    (2420, PANY, 1000, 'The pattern (First Aid p. 397)', [
      ('ALT > AST', 'most liver disease'),
      ('AST > ALT, over 2 : 1', 'alcoholic liver disease'),
      ('Over 1000', 'acetaminophen · ischemia · acute viral or autoimmune'),
      ('ALP + GGT up', 'cholestasis or infiltration'),
      ('ALP up, GGT normal', 'bone'),
      ('↓ albumin · ↑ PT · ↓ platelets', 'advanced disease')])],
  dyn=dyn)
