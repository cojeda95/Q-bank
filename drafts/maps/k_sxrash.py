# Fever & Rash (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A symptom work-up drawn as a decision tree (one `one` switch; the path to the answer lights up and a dot travels
# it), sorted by what the spots look like — vesicles, red macules and papules, a red tongue, palms and soles,
# petechiae, targets and rings. Readouts: platelets, ESR/CRP, ASO titer, RPR/VDRL. Clues come from the pinned cards
# (childrashes, hsvvzv, measles, rubella, roseola, gas, kawasaki, rmsf, syphilis, meningococcus, dic, sjs, lyme);
# their FA pages are in `fa`. No new cards.
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
  ('r', None, '', 'Fever and a rash', 'what do the spots look like?', None),
  ('ve', 'r', 'fluid-filled', 'Vesicles', '', None),
  ('vz', 've', 'trunk first · lesions in different stages', 'Chickenpox (VZV)', 'latent in sensory ganglia', 'vzv'),
  ('hf', 've', 'palms, soles and mouth', 'Hand-foot-mouth disease', 'coxsackievirus A', 'hfm'),
  ('mp', 'r', 'flat or raised red spots', 'Red macules & papules', 'which came first?', None),
  ('me', 'mp', 'cough, coryza, conjunctivitis · Koplik spots', 'Measles', 'hairline → down', 'meas'),
  ('ru', 'mp', 'postauricular nodes · arthralgias', 'Rubella', 'face → down, fine', 'rub'),
  ('ro', 'mp', 'days of high fever, then the rash', 'Roseola (HHV-6)', 'trunk first · infants', 'ros'),
  ('tg', 'r', 'strawberry tongue', 'Red tongue, peeling skin', 'strep or vasculitis?', None),
  ('sc', 'tg', 'sore throat · sandpaper · circumoral pallor', 'Scarlet fever', 'S pyogenes toxin', 'scar'),
  ('ka', 'tg', 'fever ≥ 5 days · red eyes · swollen hands', 'Kawasaki disease', 'coronary aneurysms', 'kawa'),
  ('ps', 'r', 'palms and soles', 'Palms & soles', 'tick or sex?', None),
  ('rm', 'ps', 'tick bite · wrists and ankles → in', 'Rocky Mountain spotted fever', 'Rickettsia', 'rmsf'),
  ('sy', 'ps', 'healed chancre · condylomata lata', 'Secondary syphilis', 'Treponema pallidum', 'syph'),
  ('pe', 'r', 'petechiae · shock — act now', 'Meningococcemia', 'DIC · adrenal hemorrhage', 'mening'),
  ('tr', 'r', 'targets or rings', 'Targets & rings', '', None),
  ('sj', 'tr', 'dusky targets · mucosa · after a drug', 'EM · SJS · TEN', 'sulfa · β-lactams · phenytoin', 'sjs'),
  ('ly', 'tr', 'expanding bull’s-eye after a tick', 'Lyme disease', 'erythema migrans', 'lyme'),
]
pos, flows, ybot = tree(T, SW, Y0=270, DY=92)
text('Fever & rash — follow the clue down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the answer you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'vzv': ['Chickenpox — varicella-zoster virus', 'vesicles start on the trunk; lesions in different stages', 'reactivates later as shingles along one dermatome'],
  'hfm': ['Hand-foot-mouth disease — coxsackievirus A', 'oval vesicles on the palms and soles', 'oral vesicles and ulcers (herpangina)'],
  'meas': ['Measles — paramyxovirus', 'the 3 Cs (cough, coryza, conjunctivitis), then Koplik spots on the buccal mucosa', 'rash from the hairline down · pneumonia is the commonest cause of death'],
  'rub': ['Rubella', 'fine rash from the face down · postauricular lymphadenopathy · arthralgias', 'in pregnancy: PDA, cataracts, deafness, blueberry-muffin rash'],
  'ros': ['Roseola — HHV-6', 'high fever for several days (febrile seizures), then a macular rash from the trunk', 'children under 2'],
  'scar': ['Scarlet fever — S pyogenes erythrogenic toxin', 'sandpaper rash neck → trunk, strawberry tongue, circumoral pallor', 'ASO and anti-DNase B show recent infection'],
  'kawa': ['Kawasaki disease — medium-vessel vasculitis', 'fever ≥ 5 days + CRASH: Conjunctivitis, Rash, Adenopathy, Strawberry tongue, Hand-foot edema', 'image the coronary arteries for aneurysms'],
  'rmsf': ['Rocky Mountain spotted fever', 'headache, fever, rash — wrists and ankles, then trunk, palms and soles', 'Dermacentor tick · treat on clinical grounds'],
  'syph': ['Secondary syphilis', 'rash including the palms and soles, condylomata lata, fever, lymphadenopathy', 'RPR/VDRL screen · FTA-ABS confirms'],
  'mening': ['Meningococcemia — N meningitidis', 'petechial hemorrhages, gangrene of the toes, shock, DIC', 'Waterhouse-Friderichsen: bilateral adrenal hemorrhage'],
  'sjs': ['Erythema multiforme → SJS → TEN', 'target lesions with a dusky center · SJS: fever, bullae, mucosa, Nikolsky +', 'drugs (sulfa, β-lactams, phenytoin), Mycoplasma, HSV'],
  'lyme': ['Lyme disease — Borrelia burgdorferi', 'erythema migrans: an expanding bull’s-eye rash after an Ixodes tick', 'diagnostic on its own · later carditis, facial palsy, arthritis'],
}
cy = clues(C, SW, 180, ybot + 70, 2140)
PY = cy + 110; PANY = 660

# ════════ readouts ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
readouts = [
  dict(l='Platelets', mods=[dict(when=O('kawa'), d=1), dict(when=O('mening'), d=-1)]),
  dict(l='ESR · CRP', mods=[dict(when=O('kawa'), d=1)]),
  dict(l='ASO titer', mods=[dict(when=O('scar'), d=1)]),
  dict(l='RPR · VDRL', mods=[dict(when=O('syph'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Fever with a rash: sort by what the spots look like and where they started — vesicles, red macules and papules, a red '
      'tongue, palms and soles, petechiae, targets or rings. Petechiae with shock is the emergency.',
  'dx:vzv': 'Chickenpox: vesicles that start on the trunk, in different stages at once. The virus stays latent in sensory ganglia '
            'and can return as shingles.',
  'dx:hfm': 'Hand-foot-mouth disease (coxsackievirus A): oval vesicles on the palms and soles with oral vesicles and ulcers.',
  'dx:meas': 'Measles: cough, coryza and conjunctivitis, then Koplik spots, then a maculopapular rash from the hairline down. '
             'Pneumonia is the commonest cause of death; SSPE can follow years later.',
  'dx:rub': 'Rubella: a fine rash from the face down with postauricular lymphadenopathy and arthralgias. In pregnancy: PDA, '
            'cataracts and deafness in the baby.',
  'dx:ros': 'Roseola (HHV-6): several days of high fever — sometimes a febrile seizure — then a macular rash that starts on the '
            'trunk, in a child under 2.',
  'dx:scar': 'Scarlet fever: the erythrogenic toxin of S pyogenes gives a sandpaper rash, a strawberry tongue and circumoral '
             'pallor after pharyngitis. ASO and anti-DNase B show recent infection.',
  'dx:kawa': 'Kawasaki disease: fever for at least 5 days plus CRASH — conjunctivitis, rash, adenopathy, strawberry tongue, '
             'hand-foot changes. ESR, CRP and platelets rise; image the coronaries for aneurysms.',
  'dx:rmsf': 'Rocky Mountain spotted fever: headache, fever and a rash that begins at the wrists and ankles and spreads to the '
             'trunk, palms and soles. Treat on clinical grounds — don’t wait for serology.',
  'dx:syph': 'Secondary syphilis: a rash that includes the palms and soles, condylomata lata, fever and lymphadenopathy. '
             'Nontreponemal tests (RPR, VDRL) screen; FTA-ABS confirms.',
  'dx:mening': 'Meningococcemia: petechiae and purpura with shock and DIC (platelets fall); bilateral adrenal hemorrhage is '
               'Waterhouse-Friderichsen syndrome. Gram-negative diplococci.',
  'dx:sjs': 'Erythema multiforme gives target lesions; SJS adds fever, bullae, mucosal involvement and a positive Nikolsky sign '
            '(under 10% of body surface; TEN over 30%). Sulfa drugs, β-lactams, phenytoin, Mycoplasma, HSV.',
  'dx:lyme': 'Lyme disease: erythema migrans, an expanding bull’s-eye rash after an Ixodes tick bite, is diagnostic on its own. '
             'Untreated: AV block, facial palsy, migratory arthralgias, then arthritis.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The case']],
  switches=[dict(id=SW, label='The answer', type='one', options=[
    ['vzv', 'Chickenpox', 'hsvvzv'], ['hfm', 'Hand-foot-mouth', 'childrashes'], ['meas', 'Measles', 'measles'],
    ['rub', 'Rubella', 'rubella'], ['ros', 'Roseola', 'roseola'], ['scar', 'Scarlet fever', 'gas'], ['kawa', 'Kawasaki disease', 'kawasaki'],
    ['rmsf', 'Rocky Mountain spotted fever', 'rmsf'], ['syph', 'Secondary syphilis', 'syphilis'],
    ['mening', 'Meningococcemia', 'meningococcus'], ['sjs', 'EM · SJS · TEN', 'sjs'], ['lyme', 'Lyme disease', 'lyme']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 134, 140, 144–148, 162–167, 177, 251, 478 (cards)')

MAP = dict(
  id='sxrash', title='Fever & Rash', topic='sx', after='sxams',
  sub='Sort a febrile rash by what the spots look like — vesicles, red macules, a red tongue, palms and soles, petechiae, '
      'targets — and a dot follows the clues down the tree, while the readouts show platelets, ESR/CRP, ASO and RPR',
  w=3500, h=1880,
  fa='134, 140, 144–146, 148, 162–163, 166–167, 177, 251, 432–433, 478, 490',
  src=[full('Robbins', 8), full('Robbins', 10), full('Robbins', 11), full('Robbins', 25), full('Katzung', 51)],
  lanes=[('xrVir', 'Viral exanthems', 'glycolysis'), ('xrBact', 'Bacteria & ticks', 'tca'), ('xrImm', 'Immune & drug', 'gluconeo')],
  nodes=[
    ('xr1', 'Red rashes of childhood', 330, PY, 'xrVir', 'agent → pattern', ['childrashes'], 'hub'),
    ('xr2', 'Measles · rubella', 760, PY, 'xrVir', 'head → down', ['measles', 'rubella']),
    ('xr3', 'Roseola · VZV', 1160, PY, 'xrVir', 'trunk first', ['roseola', 'hsvvzv']),
    ('xr4', 'Scarlet fever', 1560, PY, 'xrBact', 'S pyogenes', ['gas']),
    ('xr5', 'Meningococcemia', 1960, PY, 'xrBact', 'petechiae · DIC', ['meningococcus', 'dic']),
    ('xr6', 'RMSF · Lyme', 330, PY + 130, 'xrBact', 'ticks', ['rmsf', 'lyme']),
    ('xr7', 'Syphilis', 760, PY + 130, 'xrBact', 'palms and soles', ['syphilis']),
    ('xr8', 'Kawasaki disease', 1160, PY + 130, 'xrImm', 'CRASH and burn', ['kawasaki']),
    ('xr9', 'EM · SJS · TEN', 1560, PY + 130, 'xrImm', 'targets · mucosa', ['sjs'])],
  panels=[
    (2420, PANY, 1000, 'Rash on the palms and soles (cards)', [
      ('Rocky Mountain spotted fever', 'wrists and ankles first'),
      ('Secondary syphilis', 'with condylomata lata'),
      ('Hand-foot-mouth disease', 'vesicles + oral ulcers'),
      ('Kawasaki disease', 'red, swollen hands and feet')])],
  dyn=dyn)
