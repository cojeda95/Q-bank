# Edema (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it), a clue box, and the four Starling forces as readouts: capillary hydrostatic pressure (Pc), plasma oncotic
# pressure (πc), capillary permeability (Kf) and interstitial oncotic pressure (πi) — the cause list per force is
# the capfluid card's. Clues come from the pinned cards (capfluid, hf, nephrotic, cirrhosis, kwashiorkor, dvt,
# lymphedema, ccbs); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Edema', 'excess fluid in the interstitium', None),
  ('lo', 'r', 'one limb or one region', 'Localized', '', None),
  ('dv', 'lo', 'warm, red, painful leg', 'Deep venous thrombosis', 'Virchow triad', 'dvt'),
  ('ly', 'lo', 'after node removal · filariasis', 'Lymphedema', 'lymph can’t drain', 'lymph'),
  ('ge', 'r', 'both legs or everywhere', 'Generalized', 'which Starling force changed?', None),
  ('pc', 'ge', 'JVD · crackles · S3', 'Pushed out — ↑ Pc', '', None),
  ('hf', 'pc', 'JVD · hepatomegaly · orthopnea', 'Heart failure', 'right-sided → peripheral edema', 'hf'),
  ('cc', 'pc', 'new amlodipine or nifedipine', 'Dihydropyridine CCB', 'ankle edema, flushing', 'ccb'),
  ('al', 'ge', 'low serum albumin', 'Not held in — ↓ πc', '', None),
  ('ne', 'al', 'frothy urine · protein > 3.5 g/day', 'Nephrotic syndrome', 'periorbital edema · anasarca', 'neph'),
  ('ci', 'al', 'ascites · spider angiomas', 'Cirrhosis', 'albumin not made', 'cirr'),
  ('kw', 'al', 'carbohydrate-only diet · flaky-paint skin', 'Kwashiorkor', 'protein, not calories, missing', 'kwash'),
  ('kf', 'ge', 'burns · sepsis · toxins', 'Leaky wall — ↑ Kf', 'protein escapes with the fluid', 'leak'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Edema — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'dvt': ['Deep venous thrombosis — one swollen leg', 'swelling, redness, warmth and pain · stasis, hypercoagulability, endothelial damage', 'D-dimer rules it out when probability is low · compression ultrasound confirms'],
  'lymph': ['Lymphedema — fluid and protein trapped', 'after axillary node removal or irradiation (arm) · filariasis (legs, genitals)', 'trapped protein raises interstitial oncotic pressure, pulling out more fluid'],
  'hf': ['Heart failure — backed-up venous pressure', 'right-sided: JVD, hepatomegaly with nutmeg liver, peripheral edema, ascites', 'left-sided failure is its most common cause · BNP ↑'],
  'ccb': ['Dihydropyridine calcium channel blocker', 'amlodipine, nifedipine: peripheral edema, flushing, dizziness, gingival hyperplasia', 'a drug cause — check the medication list before a work-up'],
  'neph': ['Nephrotic syndrome — albumin lost in the urine', 'proteinuria > 3.5 g/day, frothy urine · periorbital edema, anasarca', 'hyperlipidemia, fatty casts · hypercoagulable (antithrombin lost)'],
  'cirr': ['Cirrhosis — albumin not made', 'portal hypertension: ascites, varices, caput medusae, splenomegaly', 'low albumin and a long PT mark lost synthetic function'],
  'kwash': ['Kwashiorkor — protein out of proportion to calories', 'MEALS: Malnutrition, Edema, Anemia, Liver (fatty), Skin lesions', 'the edema hides how much weight is lost'],
  'leak': ['Leaky capillaries — permeability ↑', 'toxins, infections and burns raise Kf', 'protein leaks out with the fluid'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts — the Starling forces (capfluid card) ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  # UNVERIFIED: ↑ Pc for DVT (venous obstruction) and for dihydropyridine CCBs is standard physiology but not on the pinned cards
  dict(l='Pc — capillary pressure', mods=[dict(when=O('hf', 'dvt', 'ccb'), d=1)]),
  dict(l='πc — plasma oncotic', mods=[dict(when=O('neph', 'cirr', 'kwash'), d=-1)]),
  dict(l='Kf — permeability', mods=[dict(when=O('leak'), d=1)]),
  dict(l='πi — interstitial oncotic', mods=[dict(when=O('lymph'), d=1)]),
  dict(l='Serum albumin', mods=[dict(when=O('neph', 'cirr', 'kwash'), d=-1)]),
]

# ════════ notes ════════
notes = {
  '': 'Edema is excess interstitial fluid. Two forces push fluid out of a capillary (Pc, πi) and two pull it back (πc, Pi) — '
      'first ask whether it is one limb or everywhere, then find the force that changed.',
  'dx:dvt': 'Deep venous thrombosis: one swollen, red, warm, painful leg after stasis (surgery, a long flight), '
            'hypercoagulability or endothelial damage. Proximal leg clots are the source of pulmonary emboli.',
  'dx:lymph': 'Lymphedema: blocked or removed lymphatics leave fluid and protein in the tissue, so interstitial oncotic pressure '
              'rises and pulls out still more — after axillary node dissection, or from filariasis.',
  'dx:hf': 'Heart failure raises venous and capillary hydrostatic pressure (Pc). Right-sided failure gives JVD, hepatomegaly and '
           'peripheral edema; its most common cause is left-sided failure.',
  'dx:ccb': 'Dihydropyridine calcium channel blockers (amlodipine, nifedipine) list peripheral edema among their adverse effects — '
            'with flushing, dizziness and gingival hyperplasia.',
  'dx:neph': 'Nephrotic syndrome: podocyte injury lets more than 3.5 g of protein a day into the urine. Low albumin lowers plasma '
             'oncotic pressure (πc) — periorbital edema, then anasarca.',
  'dx:cirr': 'Cirrhosis: the failing liver makes too little albumin (↓ πc) and portal hypertension adds ascites. Low albumin and a '
             'long PT mark the lost synthetic function.',
  'dx:kwash': 'Kwashiorkor: protein lacking out of proportion to calories. Low albumin lowers πc and causes edema, which hides how '
              'much weight has been lost — MEALS.',
  'dx:leak': 'Toxins, infections and burns damage the capillary wall and raise its permeability (Kf), so protein-rich fluid leaks '
             'into the tissue.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['dvt', 'Deep venous thrombosis', 'dvt'], ['lymph', 'Lymphedema', 'lymphedema'], ['hf', 'Heart failure', 'hf'],
    ['ccb', 'Dihydropyridine CCB', 'ccbs'], ['neph', 'Nephrotic syndrome', 'nephrotic'], ['cirr', 'Cirrhosis', 'cirrhosis'],
    ['kwash', 'Kwashiorkor', 'kwashiorkor'], ['leak', 'Leaky capillaries (burns, sepsis)', 'capfluid']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 69, 299, 301, 316, 321, 323, 396–397, 613 · Guyton ch 16 · Robbins ch 4')

MAP = dict(
  id='sxedema', title='Edema', topic='sx', after='sxdyspnea',
  sub='One leg or everywhere, then which Starling force moved — pick an answer and a dot follows the clues down the tree, '
      'while the readouts show capillary pressure, plasma and interstitial oncotic pressure and permeability. Tap a card pin '
      'for the details',
  w=3500, h=1540,
  fa='69, 156, 244, 299, 301, 316, 321, 323, 372, 396, 397, 486, 613, 655',
  src=[full('Robbins', 4), full('Guyton', 16), full('Guyton', 25), full('Costanzo', 4), full('Katzung', 11), full('Robbins', 20),
       full('Robbins', 18), full('Robbins', 9)],
  lanes=[('xeLocal', 'Localized', 'glycolysis'), ('xeForce', 'Starling forces', 'tca'), ('xeCause', 'Generalized causes', 'gluconeo')],
  nodes=[
    ('ed1', 'Starling forces', 330, PY, 'xeForce', 'two push out, two pull in', ['capfluid', 'edemasafe'], 'hub'),
    ('ed2', 'Deep venous thrombosis', 780, PY, 'xeLocal', 'Virchow triad', ['dvt']),
    ('ed3', 'Lymphedema', 1200, PY, 'xeLocal', 'πi ↑', ['lymphedema']),
    ('ed4', 'Heart failure', 1600, PY, 'xeCause', 'Pc ↑', ['hf']),
    ('ed5', 'Dihydropyridine CCBs', 2010, PY, 'xeCause', 'a drug cause', ['ccbs']),
    ('ed6', 'Nephrotic syndrome', 330, PY + 130, 'xeCause', 'albumin lost', ['nephrotic']),
    ('ed7', 'Cirrhosis', 780, PY + 130, 'xeCause', 'albumin not made', ['cirrhosis']),
    ('ed8', 'Kwashiorkor', 1200, PY + 130, 'xeCause', 'albumin not eaten', ['kwashiorkor'])],
  panels=[
    (2420, PANY, 1000, 'One force per cause (First Aid p. 301)', [
      ('↑ Pc', 'heart failure'),
      ('↓ πc', 'nephrotic syndrome · liver failure · protein malnutrition'),
      ('↑ Kf', 'toxins · infections · burns'),
      ('↑ πi', 'lymphatic blockage')])],
  dyn=dyn)
