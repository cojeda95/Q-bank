# Study Design Picker (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Study designs drawn as a decision tree (one `one` switch; the path to the design lights up and a dot travels it):
# did the investigators assign the exposure, then where does the study start — and which measure it yields
# (prevalence, odds ratio, relative risk) and the bias it is prone to. No readouts — the answers are designs, not
# arrows. Every step is from the pinned cards (studydesigns, rct, oddsratio, riskreduction, incprev, infobias,
# selectionbias, confounding); their FA pages are in `fa`. No new cards.
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
SW = 'des'
T = [
  ('r', None, '', 'A research question', 'did the investigators assign the exposure?', None),
  ('ex', 'r', 'yes — they intervened', 'Experimental', 'randomize, control, blind', None),
  ('rc', 'ex', 'groups randomized to treatments', 'Randomized controlled trial', 'intention-to-treat', 'rct'),
  ('co', 'ex', 'each subject gets both, random order', 'Crossover trial', 'their own control · washout', 'cross'),
  ('ob', 'r', 'no — they watched', 'Observational', 'where does the study start?', None),
  ('cs', 'ob', 'no comparison group', 'Case series', 'no risk association', 'series'),
  ('xs', 'ob', 'one moment in time — “what is happening?”', 'Cross-sectional', 'prevalence', 'xsec'),
  ('cc', 'ob', 'starts with disease, looks back at exposure', 'Case-control', 'odds ratio', 'cc'),
  ('ch', 'ob', 'starts with exposure, follows for disease', 'Cohort', 'incidence · relative risk', 'coh'),
  ('ec', 'ob', 'whole populations compared', 'Ecological', 'not for individuals', 'eco'),
]
pos, flows, ybot = tree(T, SW, Y0=280)
text('Study design — follow the question down the tree', 180, 160, 'dyn-big')
text('each box asks one question; the dot travels the path to the design you pick', 180, 186, 'dyn-cap')

# ════════ the clues ════════
C = {
  'rct': ['Randomized controlled trial', 'quality rises when it is randomized, controlled and double-blinded', 'analyze by intention-to-treat: once randomized, always analyzed'],
  'cross': ['Crossover trial', 'each subject receives the treatments in random order, with a washout between', 'every subject is their own control — it also reduces confounding'],
  'series': ['Case series', 'several patients with the same diagnosis or treatment', 'no comparison group, so no risk association'],
  'xsec': ['Cross-sectional study', 'disease and risk factors measured at one moment', 'gives prevalence · association, not causation'],
  'cc': ['Case-control study', 'people with and without the disease, asked about past exposure', 'odds ratio = ad / bc · prone to recall bias'],
  'coh': ['Cohort study', 'exposed and unexposed followed for disease — prospective or retrospective', 'incidence and relative risk = [a/(a+b)] ÷ [c/(c+d)] · attrition bias'],
  'eco': ['Ecological study', 'compares populations, not people', 'applying it to individuals is the ecological fallacy'],
}
cy = clues(C, SW, 180, ybot + 70, 2140, title='The design')
PY = cy + 110; PANY = 660

# ════════ notes ════════
notes = {
  '': 'The design decides which number you can calculate. First ask whether the investigators assigned the exposure (experimental) '
      'or only watched (observational); then ask where the study starts.',
  'des:rct': 'A randomized controlled trial assigns the intervention at random; randomization handles confounders, blinding handles '
             'observer bias. Analyze by intention-to-treat — once randomized, always analyzed.',
  'des:cross': 'In a crossover trial each subject gets the treatments in random order with a washout between, so each is their own '
               'control.',
  'des:series': 'A case series describes several patients with the same diagnosis or treatment. With no comparison group it can’t '
                'show a risk association.',
  'des:xsec': 'A cross-sectional study measures disease and risk factors at one moment — “what is happening?” It gives prevalence '
              'and shows association, not causation.',
  'des:cc': 'A case-control study starts from people with and without the disease and looks back at exposure — “what happened?” It '
            'gives an odds ratio (ad/bc) and is prone to recall bias.',
  'des:coh': 'A cohort study starts from exposed and unexposed people and follows them for disease, prospectively or retrospectively. '
             'It gives incidence and relative risk; loss to follow-up causes attrition bias.',
  'des:eco': 'An ecological study compares populations. Its findings can’t be applied to individuals — the ecological fallacy.',
}

dyn = dict(
  kinds=dict(pt=['pt', '--accent']), groups=[['pt', 'The question']],
  switches=[dict(id=SW, label='The design', type='one', options=[
    ['rct', 'Randomized controlled trial', 'rct'], ['cross', 'Crossover trial', 'rct'], ['series', 'Case series', 'studydesigns'],
    ['xsec', 'Cross-sectional', 'studydesigns'], ['cc', 'Case-control', 'oddsratio'], ['coh', 'Cohort', 'oddsratio'],
    ['eco', 'Ecological', 'studydesigns']])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=[],
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 256–263 (cards)')

MAP = dict(
  id='designsim', title='Study Design Picker', topic='stats', after='biostats',
  sub='Did the investigators assign the exposure, and where does the study start? Pick a design and a dot follows the '
      'questions down the tree to the measure it gives — prevalence, odds ratio or relative risk — and the bias it invites',
  w=3500, h=1470,
  fa='256–258, 261–263, 266',
  src=[],
  lanes=[('sdObs', 'Observational', 'glycolysis'), ('sdExp', 'Experimental', 'tca'), ('sdMeas', 'Measures & bias', 'gluconeo')],
  nodes=[
    ('sd1', 'Observational designs', 330, PY, 'sdObs', 'who, and which direction', ['studydesigns'], 'hub'),
    ('sd2', 'Clinical trials', 760, PY, 'sdExp', 'randomize · blind', ['rct']),
    ('sd3', 'Odds ratio · relative risk', 1200, PY, 'sdMeas', 'the 2 × 2 table', ['oddsratio']),
    ('sd4', 'Risk reduction · NNT', 1640, PY, 'sdMeas', 'differences', ['riskreduction']),
    ('sd5', 'Incidence · prevalence', 2040, PY, 'sdMeas', 'new vs all cases', ['incprev']),
    ('sd6', 'Recall · observer bias', 330, PY + 130, 'sdMeas', 'blinding', ['infobias']),
    ('sd7', 'Selection bias', 760, PY + 130, 'sdMeas', 'randomize', ['selectionbias']),
    ('sd8', 'Confounding', 1160, PY + 130, 'sdMeas', 'stratify', ['confounding'])],
  panels=[
    (2420, PANY, 1000, 'Which number (First Aid pp. 256–258)', [
      ('Cross-sectional', 'prevalence'),
      ('Case-control', 'odds ratio = ad / bc'),
      ('Cohort', 'relative risk = [a/(a+b)] ÷ [c/(c+d)]'),
      ('Rare disease', 'the odds ratio approximates the relative risk'),
      ('1 = no association', 'significant only if the 95% CI excludes 1')])],
  dyn=dyn)
