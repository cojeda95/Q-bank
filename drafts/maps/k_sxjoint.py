# Joint Pain (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it): one hot joint → tap it (pus or crystals), or many joints → RA, OA, the HLA-B27 family and lupus. Readouts:
# synovial fluid WBC, ESR/CRP, RF/anti-CCP, HLA-B27, ANA. Clues come from the pinned cards (septicarth, synfluid,
# goutclin, cppd, ra, oa, ankspond, psa, reactive, sle); their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Joint pain', 'one hot joint, or many?', None),
  ('mo', 'r', 'one hot, swollen joint', 'Monoarthritis — tap it', 'Gram stain, culture, count, crystals', None),
  ('se', 'mo', 'pus · WBC > 50,000 · fever', 'Septic arthritis', 'S aureus · gonococcus', 'sep'),
  ('go', 'mo', 'needle-shaped, negatively birefringent', 'Gout', 'urate crystals', 'gout'),
  ('pg', 'mo', 'rhomboid, positively birefringent · knee', 'Pseudogout (CPPD)', 'chondrocalcinosis', 'cppd'),
  ('po', 'r', 'several joints', 'Polyarthritis', 'pattern and stiffness?', None),
  ('ra', 'po', 'symmetric MCP, PIP, wrist · stiff > 1 h', 'Rheumatoid arthritis', 'spares the DIP', 'ra'),
  ('oa', 'po', 'weight-bearing · worse with use · DIP nodes', 'Osteoarthritis', 'no systemic symptoms', 'oa'),
  ('b2', 'po', 'young · back, eyes, skin or gut', 'Seronegative — HLA-B27', 'RF negative', None),
  ('as', 'b2', 'back stiff in the morning, better with exercise', 'Ankylosing spondylitis', 'bamboo spine · uveitis', 'as'),
  ('ps', 'b2', 'DIP · sausage digits · nail pits', 'Psoriatic arthritis', 'pencil-in-cup', 'psa'),
  ('re', 'b2', 'after GI or GU infection · eyes, urethra', 'Reactive arthritis', 'can’t see, pee or bend', 'rea'),
  ('sl', 'po', 'young woman · malar rash · ulcers', 'Systemic lupus erythematosus', 'nonerosive arthritis', 'sle'),
]
pos, flows, ybot = tree(T, SW, Y0=270)
text('Joint pain — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'sep': ['Septic arthritis — an emergency', 'hot, red, swollen joint, usually one; fever · S aureus most often in adults', 'purulent fluid, WBC > 50,000 · drain the joint + antibiotics'],
  'gout': ['Gout', 'attacks after a purine-rich meal, alcohol, surgery, dehydration or diuresis', 'needle-shaped, negatively birefringent crystals · urate can be normal in an attack'],
  'cppd': ['Pseudogout — calcium pyrophosphate', 'acute monoarthritis, most often the knee, over 50', 'rhomboid, weakly positively birefringent crystals · chondrocalcinosis · check iron, PTH'],
  'ra': ['Rheumatoid arthritis', 'symmetric MCP, PIP and wrist (spares DIP) · morning stiffness > 1 hour', 'RF, anti-CCP (more specific) · marginal erosions on x-ray'],
  'oa': ['Osteoarthritis', 'weight-bearing joints, worse with use · Heberden (DIP) and Bouchard (PIP) nodes', 'noninflammatory fluid (WBC < 2000) · osteophytes, asymmetric narrowing'],
  'as': ['Ankylosing spondylitis — HLA-B27', 'inflammatory back pain: morning stiffness, better with exercise · sacroiliitis', 'bamboo spine, uveitis, aortic regurgitation, Achilles enthesitis'],
  'psa': ['Psoriatic arthritis — HLA-B27', 'asymmetric, patchy, DIP · dactylitis (sausage fingers)', 'nail pitting, onycholysis · pencil-in-cup deformity'],
  'rea': ['Reactive arthritis — HLA-B27', 'conjunctivitis, urethritis, arthritis after Shigella, Campylobacter, Salmonella, Chlamydia, Yersinia', 'sterile joint fluid · keratoderma blennorrhagicum'],
  'sle': ['Systemic lupus erythematosus', 'RASH OR PAIN — nonerosive arthritis with rash, serositis, ulcers, renal disease', 'ANA (sensitive), anti-dsDNA and anti-Sm (specific) · ↓ C3, C4 in flares'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='Synovial fluid WBC', mods=[dict(when=O('sep', 'ra'), d=1), dict(when=O('oa'), d=0)]),
  dict(l='ESR · CRP', mods=[dict(when=O('ra', 'as', 'sle'), d=1)]),
  dict(l='RF · anti-CCP', mods=[dict(when=O('ra'), d=1)]),
  dict(l='HLA-B27', mods=[dict(when=O('as', 'psa', 'rea'), d=1)]),
  dict(l='ANA', mods=[dict(when=O('sle'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Joint pain: one hot joint means tap it — pus or crystals decide it. Many joints: read the pattern (symmetric small joints, '
      'weight-bearing joints, the spine and DIP) and the stiffness.',
  'dx:sep': 'Septic arthritis: a hot, red, swollen joint with fever — purulent fluid with WBC over 50,000. S aureus is the commonest '
            'adult cause; gonococcus in sexually active young adults. Drain it and give antibiotics.',
  'dx:gout': 'Gout: needle-shaped, negatively birefringent urate crystals. Attacks follow purine-rich meals, alcohol, surgery, '
             'dehydration or diuresis — and serum urate can be normal during one.',
  'dx:cppd': 'Pseudogout: rhomboid, weakly positively birefringent calcium pyrophosphate crystals, most often in the knee after 50, '
             'with chondrocalcinosis. Look for hemochromatosis and hyperparathyroidism.',
  'dx:ra': 'Rheumatoid arthritis: symmetric MCP, PIP and wrist synovitis sparing the DIP, with morning stiffness over an hour. RF and '
           'the more specific anti-CCP; the fluid is mildly inflammatory.',
  'dx:oa': 'Osteoarthritis: weight-bearing joints that hurt after use and ease with rest, Heberden and Bouchard nodes, no systemic '
           'symptoms — and noninflammatory fluid (WBC under 2000).',
  'dx:as': 'Ankylosing spondylitis: inflammatory back pain that is stiff in the morning and better with exercise, sacroiliitis and '
           'a bamboo spine — with uveitis and aortic regurgitation. HLA-B27.',
  'dx:psa': 'Psoriatic arthritis: asymmetric DIP arthritis, sausage digits, nail pitting and a pencil-in-cup deformity — HLA-B27, '
            'RF negative.',
  'dx:rea': 'Reactive arthritis: conjunctivitis, urethritis and arthritis after a GI or genitourinary infection — can’t see, can’t '
            'pee, can’t bend my knee. The joint fluid is sterile.',
  'dx:sle': 'Lupus: a nonerosive arthritis with rash, serositis, ulcers, cytopenias or renal disease. ANA is the sensitive screen; '
            'anti-dsDNA and anti-Smith are specific; complement falls in flares.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['sep', 'Septic arthritis', 'septicarth'], ['gout', 'Gout', 'goutclin'], ['cppd', 'Pseudogout (CPPD)', 'cppd'],
    ['ra', 'Rheumatoid arthritis', 'ra'], ['oa', 'Osteoarthritis', 'oa'], ['as', 'Ankylosing spondylitis', 'ankspond'],
    ['psa', 'Psoriatic arthritis', 'psa'], ['rea', 'Reactive arthritis', 'reactive'], ['sle', 'Lupus', 'sle']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 113, 472–476 (cards) · Robbins ch 26')

MAP = dict(
  id='sxjoint', title='Joint Pain', topic='sx', after='sxams',
  sub='One hot joint or many — tap it for pus or crystals, or read the pattern; a dot follows the case down the tree while '
      'the readouts show the synovial fluid WBC, ESR/CRP, RF and anti-CCP, HLA-B27 and ANA',
  w=3500, h=1640,
  fa='113, 472–476',
  src=[full('Robbins', 26), full('Robbins', 6), full('Katzung', 36)],
  lanes=[('xjMono', 'One hot joint', 'glycolysis'), ('xjPoly', 'Many joints', 'tca'), ('xjB27', 'HLA-B27 & lupus', 'gluconeo')],
  nodes=[
    ('xj1', 'Septic arthritis', 330, PY, 'xjMono', 'tap before antibiotics', ['septicarth', 'synfluid'], 'hub'),
    ('xj2', 'Gout', 760, PY, 'xjMono', 'needles, negative', ['goutclin']),
    ('xj3', 'Pseudogout', 1160, PY, 'xjMono', 'rhomboids, positive', ['cppd']),
    ('xj4', 'Rheumatoid arthritis', 1580, PY, 'xjPoly', 'symmetric · spares DIP', ['ra']),
    ('xj5', 'Osteoarthritis', 2000, PY, 'xjPoly', 'wear and tear', ['oa']),
    ('xj6', 'Ankylosing spondylitis', 330, PY + 130, 'xjB27', 'back · eyes · aorta', ['ankspond']),
    ('xj7', 'Psoriatic · reactive', 780, PY + 130, 'xjB27', 'seronegative', ['psa', 'reactive']),
    ('xj8', 'Lupus', 1180, PY + 130, 'xjB27', 'RASH OR PAIN', ['sle'])],
  panels=[
    (2420, PANY, 1000, 'Synovial fluid WBC (First Aid pp. 472–474)', [
      ('Osteoarthritis', 'under 2,000/mm³ — noninflammatory'),
      ('Rheumatoid arthritis', 'about 5,000–50,000/mm³'),
      ('Septic arthritis', 'over 50,000/mm³ — purulent')])],
  dyn=dyn)
