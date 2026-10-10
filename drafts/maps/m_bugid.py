# Name the Bug (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The bench work-up of common bacteria drawn as a decision tree (one `one` switch; the path to the organism lights
# up and a dot travels it): Gram stain and shape, then catalase → coagulase → novobiocin, hemolysis → optochin,
# bacitracin, 6.5% NaCl, maltose, lactose, oxidase, H₂S. Readouts are test results (↑ positive, ↓ negative):
# catalase, coagulase, lactose fermentation, oxidase. Every test result is from the pinned cards (gpid, gnid,
# catalasepos, and each organism's card); their FA pages are in `fa`. No new cards.
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
SW = 'bug'
T = [
  ('r', None, '', 'Gram stain', 'purple or pink — and what shape?', None),
  ('gp', 'r', 'purple · cocci', 'Gram-positive cocci', 'catalase?', None),
  ('st', 'gp', 'catalase + · clusters', 'Staphylococci', 'coagulase?', None),
  ('sa', 'st', 'coagulase +', 'S aureus', 'ferments mannitol', 'sau'),
  ('cn', 'st', 'coagulase −', 'Coagulase-negative', 'novobiocin?', None),
  ('se', 'cn', 'novobiocin sensitive', 'S epidermidis', 'biofilm on hardware', 'sep'),
  ('ss', 'cn', 'novobiocin resistant', 'S saprophyticus', 'cystitis, young women', 'ssa'),
  ('sr', 'gp', 'catalase − · pairs, chains', 'Streptococci', 'hemolysis on blood agar?', None),
  ('al', 'sr', 'α — partial, green', 'α-hemolytic', 'optochin?', None),
  ('sp', 'al', 'optochin sensitive · bile soluble', 'S pneumoniae', 'capsule · Quellung', 'spn'),
  ('vi', 'al', 'optochin resistant · bile insoluble', 'Viridans streptococci', 'dental work → SBE', 'vir'),
  ('be', 'sr', 'β — complete, clear', 'β-hemolytic', 'bacitracin?', None),
  ('ga', 'be', 'bacitracin sensitive · PYR +', 'Group A — S pyogenes', 'pharyngitis · scarlet fever', 'gas'),
  ('gb', 'be', 'bacitracin resistant · CAMP +', 'Group B — S agalactiae', 'neonatal sepsis', 'gbs'),
  ('gm', 'sr', 'γ — no hemolysis, grows in bile', 'γ-hemolytic', '6.5% NaCl?', None),
  ('en', 'gm', 'grows in 6.5% NaCl · PYR +', 'Enterococcus', 'UTI · VRE', 'ent'),
  ('bv', 'gm', 'no growth in salt', 'S gallolyticus (S bovis)', 'colon cancer', 'sbo'),
  ('gn', 'r', 'pink', 'Gram-negative', 'what shape?', None),
  ('dc', 'gn', 'diplococci', 'Neisseria', 'which sugars?', None),
  ('nm', 'dc', 'maltose and glucose', 'N meningitidis', 'capsule · meningitis', 'nme'),
  ('ng', 'dc', 'glucose only', 'N gonorrhoeae', 'no capsule', 'ngo'),
  ('rd', 'gn', 'rods', 'Gram-negative rods', 'lactose on MacConkey?', None),
  ('ec', 'rd', 'pink colonies — fast fermenter', 'E coli', 'green sheen on EMB', 'eco'),
  ('nf', 'rd', 'pale — nonfermenter', 'Lactose nonfermenter', 'oxidase? H₂S?', None),
  ('pa', 'nf', 'oxidase +', 'Pseudomonas', 'grapelike odor · pyocyanin', 'pse'),
  ('sl', 'nf', 'oxidase − · H₂S on TSI', 'Salmonella', 'rose spots · poultry', 'sal'),
  ('sh', 'nf', 'oxidase − · no H₂S', 'Shigella', 'dysentery · tiny dose', 'shi'),
]
pos, flows, ybot = tree(T, SW, Y0=250, DY=78, BW=360)
text('Name the bug — run the bench tests down the tree', 180, 150, 'dyn-big')
text('each box is one test; the dot travels the path to the organism you pick', 180, 176, 'dyn-cap')

# ════════ the clues ════════
C = {
  'sau': ['Staphylococcus aureus', 'catalase +, coagulase +, ferments mannitol · β-hemolytic', 'abscesses, osteomyelitis, acute endocarditis, toxic shock, scalded skin'],
  'sep': ['Staphylococcus epidermidis', 'catalase +, coagulase −, novobiocin sensitive', 'biofilm on prosthetic joints and valves, catheters, shunts'],
  'ssa': ['Staphylococcus saprophyticus', 'catalase +, coagulase −, novobiocin resistant', 'cystitis in a sexually active young woman'],
  'spn': ['Streptococcus pneumoniae', 'α-hemolytic, optochin sensitive, bile soluble · capsule (Quellung)', 'community pneumonia, adult meningitis, otitis media'],
  'vir': ['Viridans streptococci', 'α-hemolytic, optochin resistant, bile insoluble', 'subacute endocarditis on damaged valves after dental work · caries'],
  'gas': ['Streptococcus pyogenes (group A)', 'β-hemolytic, bacitracin sensitive, PYR +', 'pharyngitis, impetigo, scarlet fever · rheumatic fever, PSGN'],
  'gbs': ['Streptococcus agalactiae (group B)', 'β-hemolytic, bacitracin resistant, CAMP + and hippurate +', 'pneumonia, meningitis and sepsis in newborns'],
  'ent': ['Enterococcus', 'γ (or α), grows in bile and 6.5% NaCl, PYR +', 'UTI, biliary infection, endocarditis after GI/GU procedures · VRE'],
  'sbo': ['Streptococcus gallolyticus (S bovis)', 'γ, grows in bile but not in 6.5% NaCl', 'bacteremia or endocarditis → colonoscopy (colorectal cancer)'],
  'nme': ['Neisseria meningitidis', 'gram-negative diplococcus · acid from maltose and glucose', 'meningitis in barracks and dorms · petechiae, Waterhouse-Friderichsen'],
  'ngo': ['Neisseria gonorrhoeae', 'gram-negative diplococcus · acid from glucose only · no capsule', 'urethritis, PID, septic arthritis, newborn conjunctivitis'],
  'eco': ['Escherichia coli', 'fast lactose fermenter — pink on MacConkey, green sheen on EMB', 'commonest cause of UTI · neonatal meningitis · EHEC → HUS'],
  'pse': ['Pseudomonas aeruginosa', 'lactose nonfermenter, oxidase +, grapelike odor', 'CF and ventilator pneumonia, burns, otitis externa, hot tub folliculitis'],
  'sal': ['Salmonella', 'lactose nonfermenter, oxidase −, H₂S on TSI agar', 'poultry, eggs, reptiles · typhoid: rose spots · osteomyelitis in sickle cell'],
  'shi': ['Shigella', 'lactose nonfermenter, oxidase −, no H₂S', 'bloody mucoid dysentery, tenesmus · very low infectious dose'],
}
cy = clues(C, SW, 180, ybot + 70, 2140, title='The organism')
PY = cy + 110; PANY = 760

# ════════ readouts — test results (↑ positive · ↓ negative) ════════
O = lambda *k: [f'{SW}:{x}' for x in k]
STAPH, STREP = O('sau', 'sep', 'ssa'), O('spn', 'vir', 'gas', 'gbs', 'ent', 'sbo')
readouts = [
  dict(l='Catalase', mods=[dict(when=STAPH, d=1), dict(when=STREP, d=-1)]),
  dict(l='Coagulase', mods=[dict(when=O('sau'), d=1), dict(when=O('sep', 'ssa'), d=-1)]),
  dict(l='Lactose fermentation', mods=[dict(when=O('eco'), d=1), dict(when=O('pse', 'sal', 'shi'), d=-1)]),
  dict(l='Oxidase', mods=[dict(when=O('pse'), d=1), dict(when=O('sal', 'shi'), d=-1)]),
]

# ════════ notes ════════
notes = {
  '': 'Gram stain and shape first, then a short run of bench tests. In the readouts ↑ means the test is positive and ↓ negative — '
      'hide them with Predict and call each result before you check.',
  'bug:sau': 'S aureus: catalase-positive cocci in clusters that clot plasma (coagulase) and ferment mannitol — abscesses, '
             'osteomyelitis, acute endocarditis and the toxin diseases.',
  'bug:sep': 'S epidermidis: coagulase-negative and novobiocin-sensitive; its biofilm makes it the organism of prosthetic joints and '
             'valves, catheters and shunts.',
  'bug:ssa': 'S saprophyticus: coagulase-negative and novobiocin-resistant — cystitis in a sexually active young woman.',
  'bug:spn': 'S pneumoniae: α-hemolytic, optochin-sensitive and bile-soluble, with a capsule (Quellung) — the commonest cause of '
             'community-acquired pneumonia and adult meningitis.',
  'bug:vir': 'Viridans streptococci: α-hemolytic but optochin-resistant and bile-insoluble — subacute endocarditis on damaged '
             'valves after dental work.',
  'bug:gas': 'Group A strep (S pyogenes): β-hemolytic, bacitracin-sensitive, PYR-positive — pharyngitis, impetigo and scarlet fever, '
             'then rheumatic fever or glomerulonephritis.',
  'bug:gbs': 'Group B strep (S agalactiae): β-hemolytic, bacitracin-resistant, CAMP- and hippurate-positive — sepsis, pneumonia and '
             'meningitis in newborns.',
  'bug:ent': 'Enterococcus grows in bile and 6.5% NaCl and is PYR-positive — UTI and endocarditis after GI or GU procedures; VRE '
             'swaps D-Ala-D-Ala for D-Ala-D-Lac.',
  'bug:sbo': 'S gallolyticus (S bovis) grows in bile but not in 6.5% NaCl. Its bacteremia or endocarditis means colonoscopy — it is '
             'strongly associated with colorectal cancer.',
  'bug:nme': 'N meningitidis makes acid from maltose and glucose; its capsule and endotoxin give meningitis and meningococcemia in '
             'close quarters.',
  'bug:ngo': 'N gonorrhoeae ferments glucose only and has no capsule — urethritis, PID, septic arthritis and newborn conjunctivitis.',
  'bug:eco': 'E coli is a fast lactose fermenter — pink on MacConkey, a green sheen on EMB. The commonest cause of UTI; EHEC O157:H7 '
             'causes HUS.',
  'bug:pse': 'Pseudomonas: a lactose nonfermenter that is oxidase-positive with a grapelike odor — CF and ventilator pneumonia, burns, '
             'otitis externa, hot tub folliculitis.',
  'bug:sal': 'Salmonella: a lactose nonfermenter, oxidase-negative, that makes H₂S on TSI agar — poultry and eggs; typhoid with rose '
             'spots; osteomyelitis in sickle cell disease.',
  'bug:shi': 'Shigella: a lactose nonfermenter with no H₂S — bloody, mucoid dysentery from a very small infectious dose.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The sample']],
  switches=[dict(id=SW, label='The organism', type='one', options=[
    ['sau', 'S aureus', 'saureus'], ['sep', 'S epidermidis', 'sepi'], ['ssa', 'S saprophyticus', 'ssapro'],
    ['spn', 'S pneumoniae', 'spneumo'], ['vir', 'Viridans strep', 'viridans'], ['gas', 'Group A strep', 'gas'],
    ['gbs', 'Group B strep', 'gbsstrep'], ['ent', 'Enterococcus', 'enterococcus'], ['sbo', 'S gallolyticus', 'sbovis'],
    ['nme', 'N meningitidis', 'meningococcus'], ['ngo', 'N gonorrhoeae', 'gonococcus'], ['eco', 'E coli', 'ecoli'],
    ['pse', 'Pseudomonas', 'pseudomonas'], ['sal', 'Salmonella', 'salmonella'], ['shi', 'Shigella', 'shigella']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 123–143 (cards) · Robbins ch 8')

MAP = dict(
  id='bugid', title='Name the Bug', topic='id', after='microlab',
  sub='Gram stain and shape, then catalase, coagulase, novobiocin, hemolysis, optochin, bacitracin, salt, sugars, lactose, '
      'oxidase and H₂S — pick an organism and a dot runs the bench tests down the tree; the readouts give each result',
  w=3500, h=1960,
  fa='123, 125–126, 132–135, 139–143, 179, 181',
  src=[full('Robbins', 8), full('Katzung', 43), full('Katzung', 51)],
  lanes=[('bgPos', 'Gram-positive', 'glycolysis'), ('bgNeg', 'Gram-negative', 'tca'), ('bgLab', 'The tests', 'gluconeo')],
  nodes=[
    ('bg1', 'Gram stain', 330, PY, 'bgLab', 'wall decides the color', ['gramstain'], 'hub'),
    ('bg2', 'Gram-positive cocci', 760, PY, 'bgLab', 'catalase → coagulase', ['gpid', 'catalasepos']),
    ('bg3', 'Gram-negative ID', 1180, PY, 'bgLab', 'shape → lactose → oxidase', ['gnid']),
    ('bg4', 'Staphylococci', 1600, PY, 'bgPos', 'clusters', ['saureus', 'sepi', 'ssapro']),
    ('bg5', 'Streptococci', 2020, PY, 'bgPos', 'pairs and chains', ['spneumo', 'viridans', 'gas', 'gbsstrep']),
    ('bg6', 'Enterococcus · S bovis', 330, PY + 130, 'bgPos', 'group D', ['enterococcus', 'sbovis']),
    ('bg7', 'Neisseria', 760, PY + 130, 'bgNeg', 'diplococci', ['meningococcus', 'gonococcus']),
    ('bg8', 'Lactose fermenters', 1180, PY + 130, 'bgNeg', 'pink on MacConkey', ['ecoli', 'klebsiella']),
    ('bg9', 'Nonfermenters', 1600, PY + 130, 'bgNeg', 'oxidase · H₂S', ['pseudomonas', 'salmonella', 'shigella'])],
  panels=[
    (2420, PANY, 1000, 'The tests (First Aid pp. 132–135, 142)', [
      ('Catalase', 'bubbles in H₂O₂ — staph +, strep −'),
      ('Coagulase', 'clots plasma — S aureus'),
      ('Optochin', 'S pneumoniae sensitive'),
      ('Bacitracin', 'group A sensitive, group B resistant'),
      ('Novobiocin', 'S saprophyticus resistant'),
      ('6.5% NaCl', 'Enterococcus grows'),
      ('MacConkey', 'lactose fermenters turn pink')])],
  dyn=dyn)
