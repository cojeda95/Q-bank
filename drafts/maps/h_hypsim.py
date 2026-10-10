# Hypersensitivity Types in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Four columns, one per type, each drawn as its mechanism: I — allergen cross-links IgE on a mast cell, which
# degranulates; II — IgG/IgM on a cell (destroyed, inflamed, or its receptor blocked/stimulated); III — immune
# complexes deposit in a vessel wall, fix complement and draw neutrophils; IV — a T cell meets antigen and recruits
# macrophages (or kills directly). A timeline below marks when each reaction appears. One `one` switch picks a
# classic example; its type lights up with the example's own tag.
# No new cards: the facts restate the pinned cards (hs1–hs4, igadef, asthma, warmaiha, mg, hyperthyroid,
# goodpasture, sle, eczema, tb — fact-checked against the corpus). Sources: First Aid 2025 pp. 110–111.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

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

TAG = 'nf-l2 dyn-tag'
E = lambda *k: ['ex:' + x for x in k]
T1, T2, T3, T4 = E('anaph', 'asthma', 'iga'), E('aiha', 'mg', 'graves', 'goodp'), E('sle', 'serum', 'arthus'), E('contact', 'ppd', 'gvhd')
X0 = [160, 710, 1260, 1810]; CW = 530; Y0, Y1 = 130, 1100
def ab(x, y, rot=0, col='--dk9'):   # an antibody, a Y, its stem at (x, y)
    return (f'<g transform="rotate({rot} {x} {y})" style="stroke:var({col});stroke-width:5;fill:none;stroke-linecap:round">'
            f'<path d="M{x} {y} V{y - 22} M{x} {y - 22} L{x - 14} {y - 40} M{x} {y - 22} L{x + 14} {y - 40}"/></g>')

for i, (title, sub, grp) in enumerate([
    ('Type I — immediate', 'IgE on mast cells · minutes', T1), ('Type II — antibody on a cell', 'IgG or IgM against a fixed antigen', T2),
    ('Type III — immune complexes', 'antigen + antibody + complement', T3), ('Type IV — delayed, T cells', 'no antibody · 24–48 h', T4)]):
    x = X0[i]
    add(f'<rect x="{x}" y="{Y0}" width="{CW}" height="{Y1 - Y0}" rx="24" class="dyn-soft"/>')
    add(f'<rect x="{x}" y="{Y0}" width="{CW}" height="{Y1 - Y0}" rx="24" class="dyn-hl" style="fill:none"/>', when=grp)
    text(title, x + 20, Y0 + 36, 'dyn-big'); text(sub, x + 20, Y0 + 58, 'dyn-cap')

# ── type I: mast cell with IgE, an allergen bridging two, granules leaving ──
cx, cy = X0[0] + 265, 520
add(f'<ellipse cx="{cx}" cy="{cy}" rx="170" ry="130" class="dyn-cell"/>')
text('mast cell', cx, cy + 6, 'nf-l1', 'middle')
add(ab(cx - 40, cy - 128) + ab(cx + 40, cy - 128))
add(f'<path d="M{cx - 54} {cy - 172} Q{cx} {cy - 200} {cx + 54} {cy - 172}" style="stroke:var(--bad);stroke-width:8;fill:none;stroke-linecap:round"/>')
text('allergen cross-links IgE', cx, cy - 214, 'nf-l2', 'middle')
add(''.join(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="11" class="dyn-soft" style="stroke:var(--dk7);stroke-width:3"/>' for dx, dy in [(-90, 40), (-50, 70), (60, 60), (100, 20), (-10, 90)]))
text('histamine, tryptase, leukotrienes — within minutes', X0[0] + 20, 760)
text('late phase (hours): eosinophils recruited', X0[0] + 20, 784)
text('sensitized first: IgE already on the cells', X0[0] + 20, 808, 'dyn-cap')
text('bee sting, peanut — anaphylaxis', X0[0] + 20, 1040, TAG, when=E('anaph'))
text('allergic asthma', X0[0] + 20, 1040, TAG, when=E('asthma'))
text('IgA-deficient patient given blood', X0[0] + 20, 1040, TAG, when=E('iga'))

# ── type II: a cell with antibody on it, and the three outcomes ──
cx, cy = X0[1] + 265, 460
add(f'<ellipse cx="{cx}" cy="{cy}" rx="120" ry="90" class="dyn-cell" style="stroke:var(--bad)"/>')
text('a cell or basement membrane', cx, cy + 6, 'nf-l2', 'middle')
add(ab(cx - 60, cy - 84) + ab(cx + 60, cy - 84) + ab(cx - 110, cy + 30, -70) + ab(cx + 110, cy + 30, 70))
text('antibody binds an antigen fixed on the cell', X0[1] + 20, 620)
OUT = [('destruction', 'opsonized, eaten, or lysed by complement', E('aiha')),
       ('inflammation', 'complement and Fc receptors activated', E('goodp')),
       ('dysfunction', 'the antibody blocks or stimulates a receptor', E('mg', 'graves'))]
for j, (h, s, w) in enumerate(OUT):
    y = 690 + j * 70
    add(f'<rect x="{X0[1] + 20}" y="{y - 24}" width="490" height="56" rx="12" class="dyn-soft"/>')
    add(f'<rect x="{X0[1] + 20}" y="{y - 24}" width="490" height="56" rx="12" class="dyn-hl" style="fill:none"/>', when=w)
    text(h, X0[1] + 36, y, 'nf-l1'); text(s, X0[1] + 36, y + 20)
text('IgG on red cells → warm autoimmune hemolytic anemia', X0[1] + 20, 1040, TAG, when=E('aiha'))
text('blocks the ACh receptor → weakness', X0[1] + 20, 1040, TAG, when=E('mg'))
text('stimulates the TSH receptor → hyperthyroidism', X0[1] + 20, 1040, TAG, when=E('graves'))
text('anti–type IV collagen in lung and kidney', X0[1] + 20, 1040, TAG, when=E('goodp'))

# ── type III: complexes in a vessel, deposited, complement + neutrophils ──
x = X0[2]
shapes.append(dict(vessel=f'M{x + 90} 360 H{x + 440}', w=110, color='--dk12'))
add(f'<path d="M{x + 30} 430 H{x + 500}" style="stroke:var(--line-2);stroke-width:14"/>')
text('vessel wall · glomerulus · joint', x + 20, 470, 'nf-l2')
add(''.join(f'<rect x="{x + 80 + k * 90}" y="420" width="34" height="16" rx="6" style="fill:var(--dk9);opacity:.8"/>' for k in range(5)))
text('complexes deposit and fix complement', x + 20, 520, 'nf-l1')
add(''.join(f'<circle cx="{x + 110 + k * 120}" cy="590" r="30" class="dyn-cell" style="stroke:var(--dk5)"/><text class="nf-l2" x="{x + 110 + k * 120}" y="595" text-anchor="middle">N</text>' for k in range(4)))
text('neutrophils drawn in — their enzymes damage the tissue', x + 20, 660)
text('complement falls (C3, C4) while active', x + 20, 690, 'dyn-cap')
text('vasculitis · glomerulonephritis · arthritis', x + 20, 760)
text('SLE — complexes in kidney, joints, skin', x + 20, 1040, TAG, when=E('sle'))
text('1–2 weeks after a foreign protein: fever, rash, joint pain', x + 20, 1040, TAG, when=E('serum'))
text('local, at an injection site — a booster in someone with high IgG', x + 20, 1040, TAG, when=E('arthus'))

# ── type IV: T cell meets antigen, recruits macrophages; or CD8 kills ──
x = X0[3]
add(f'<circle cx="{x + 150}" cy="420" r="70" class="dyn-cell" style="stroke:var(--dk3)"/>')
text('CD4⁺ Th1', x + 150, 425, 'nf-l1', 'middle')
add(f'<ellipse cx="{x + 390}" cy="560" rx="100" ry="70" class="dyn-cell" style="stroke:var(--dk5)"/>')
text('macrophage', x + 390, 565, 'nf-l1', 'middle')
add(f'<circle cx="{x + 150}" cy="660" r="60" class="dyn-cell" style="stroke:var(--dk3)"/>')
text('CD8⁺', x + 150, 665, 'nf-l1', 'middle')
text('kills the antigen-bearing cell directly', x + 20, 760)
text('cytokines recruit and activate macrophages', x + 20, 784)
text('24–48 hours to develop', x + 20, 808, 'dyn-cap')
text('poison ivy, nickel — contact dermatitis', x + 20, 1040, TAG, when=E('contact'))
text('induration over 24–48 hours after a PPD', x + 20, 1040, TAG, when=E('ppd'))
text('donor T cells attack the host', x + 20, 1040, TAG, when=E('gvhd'))

# ════════ the timeline ════════
add('<rect x="160" y="1140" width="2180" height="400" rx="24" class="dyn-soft"/>')
text('When the reaction appears after exposure', 180, 1176, 'dyn-big')
LX0, LX1, LY = 300, 2240, 1330
add(f'<path d="M{LX0} {LY} H{LX1}" class="dyn-line" style="stroke-width:3"/>')
TICKS = [('minutes', 0.02), ('hours', 0.22), ('1–2 days', 0.42), ('3 days', 0.58), ('1–2 weeks', 0.85)]
for lab, f in TICKS:
    x = round(LX0 + f * (LX1 - LX0))
    add(f'<path d="M{x} {LY - 10} V{LY + 10}" class="dyn-line"/>'); text(lab, x, LY + 34, 'nf-l2', 'middle')
def mark(f, lab, when):
    x = round(LX0 + f * (LX1 - LX0))
    add(f'<circle cx="{x}" cy="{LY}" r="14" style="fill:var(--accent);stroke:var(--surface);stroke-width:3"/>', when=when)
    text(lab, x, LY - 30, TAG, 'middle', when=when)
mark(0.02, 'minutes', T1)
mark(0.42, '24–48 hours', E('contact', 'ppd'))
mark(0.85, '1–2 weeks after the foreign protein', E('serum'))
text('type II and III autoimmune disease: ongoing, as long as the antibody is made', 180, 1440, TAG, when=E('aiha', 'mg', 'graves', 'goodp', 'sle'))
text('pick an example to place it on the timeline', 180, 1440, 'dyn-cap', unless=['ex:*'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{X0[0] + 265} 520 Q{X0[0] + 160} 640 {X0[0] + 60} 700', len=300, speed=90, r=6, base=dict(med=1), mods=[m(T1, set=dict(med=6))]),
  dict(d=f'M{X0[0] + 265} 520 Q{X0[0] + 380} 640 {X0[0] + 470} 700', len=300, speed=90, r=6, base=dict(med=1), mods=[m(T1, set=dict(med=6))]),
  dict(d=f'M{X0[2] + 90} 360 H{X0[2] + 440}', len=350, speed=80, r=7, base=dict(ic=2), mods=[m(T3, set=dict(ic=6))]),
  dict(d=f'M{X0[3] + 220} 440 Q{X0[3] + 300} 470 {X0[3] + 320} 520', len=140, speed=60, r=6, base=dict(cyt=1), mods=[m(T4, set=dict(cyt=4))]),
]

# ════════ sites (tap targets) ════════
sites = [
  dict(x=X0[0] + 265, y=390, n=[0, -1], w=20, t='rec', l='', aria='IgE on the mast cell — type I', ions=[], c='hs1'),
  dict(x=X0[1] + 265, y=370, n=[0, -1], w=20, t='rec', l='', aria='Antibody on a cell — type II', ions=[], c='hs2'),
  dict(x=X0[2] + 265, y=428, n=[0, -1], w=20, t='rec', l='', aria='Immune complexes — type III', ions=[], c='hs3'),
  dict(x=X0[3] + 220, y=420, n=[1, 0], w=20, t='rec', l='', aria='T cell — type IV', ions=[], c='hs4'),
]

# ════════ readouts ════════
readouts = [
  dict(l='Serum tryptase', mods=[m(E('anaph', 'iga'), d=1)]),
  dict(l='Allergen-specific IgE', mods=[m(E('anaph', 'asthma'), d=1)]),
  dict(l='Complement (C3, C4)', mods=[m(E('serum', 'sle'), d=-1)]),
  dict(l='Direct Coombs', mods=[m(E('aiha'), d=1)]),
]

# ════════ notes ════════
notes = {
  '': 'Four ways the immune system injures the host. Types I–III use antibody: IgE on mast cells (I), IgG or IgM on a fixed '
      'antigen (II), or circulating antigen–antibody complexes (III). Type IV is T cells alone, and slow. Pick an example.',
  'ex:anaph': 'Anaphylaxis (type I): a sensitized person’s IgE on mast cells is cross-linked by the allergen and within minutes the '
              'cells release histamine, tryptase and leukotrienes. Serum tryptase marks the mast-cell activation. First and fast.',
  'ex:asthma': 'Allergic asthma (type I): allergen cross-links IgE in the airway; the immediate phase is followed hours later by '
               'a late phase as eosinophils are recruited. Skin prick tests or allergen-specific IgE confirm the sensitivity.',
  'ex:iga': 'Selective IgA deficiency: the patient makes anti-IgA antibodies, so blood products containing IgA can cause '
            'anaphylaxis — give washed or IgA-deficient blood.',
  'ex:aiha': 'Warm autoimmune hemolytic anemia (type II, destruction): IgG coats red cells, which are opsonized and removed. '
             'The direct Coombs test finds the antibody on the red-cell surface.',
  'ex:mg': 'Myasthenia gravis (type II, dysfunction): antibodies block the postsynaptic nicotinic ACh receptor — no cell is '
           'destroyed, the receptor just fails.',
  'ex:graves': 'Graves disease (type II, dysfunction): antibodies stimulate the TSH receptor, driving the thyroid — the receptor is '
               'turned on rather than blocked.',
  'ex:goodp': 'Goodpasture syndrome (type II, inflammation): antibodies against type IV collagen in the lung and glomerular '
              'basement membranes activate complement and Fc receptors.',
  'ex:sle': 'SLE (type III, plus type II autoantibodies): immune complexes deposit in glomeruli, joints and skin, fix complement '
            'and draw neutrophils; complement falls during active disease.',
  'ex:serum': 'Serum sickness (type III): 1–2 weeks after a foreign protein (horse antithymocyte globulin, monoclonal antibodies, '
              'penicillin as a hapten) — fever, urticaria, arthralgia, proteinuria, lymphadenopathy, with low C3 and C4.',
  'ex:arthus': 'Arthus reaction (type III, local): an injected antigen (a booster vaccine) meets high IgG at the site — immune '
               'complexes form there, with edema and fibrinoid necrosis.',
  'ex:contact': 'Contact dermatitis (type IV): poison ivy or nickel on the skin; sensitized T cells respond over 24–48 hours. '
                'No antibody — the 4 Ts: T cells, Transplant rejection, TB skin test, Touching.',
  'ex:ppd': 'PPD (type IV): Th1 cells recognize the tuberculin and release cytokines that recruit macrophages — induration '
            'develops over 24–48 hours.',
  'ex:gvhd': 'Graft-versus-host disease (type IV): donor T cells attack the host’s tissues.',
}

dyn = dict(
  kinds=dict(med=['med', '--dk7'], ic=['ic', '--dk9'], cyt=['cyt', '--dk3']),
  groups=[['med', 'Mast-cell mediators'], ['ic', 'Immune complexes'], ['cyt', 'Cytokines']],
  switches=[dict(id='ex', label='Pick an example', type='one',
                 options=[['anaph', 'Anaphylaxis', 'hs1'], ['asthma', 'Allergic asthma', 'asthma'], ['iga', 'Blood in IgA deficiency', 'igadef'],
                          ['aiha', 'Warm autoimmune hemolytic anemia', 'warmaiha'], ['mg', 'Myasthenia gravis', 'mg'],
                          ['graves', 'Graves disease', 'hyperthyroid'], ['goodp', 'Goodpasture syndrome', 'goodpasture'],
                          ['sle', 'SLE', 'sle'], ['serum', 'Serum sickness', 'hs3'], ['arthus', 'Arthus reaction', 'hs3'],
                          ['contact', 'Contact dermatitis', 'eczema'], ['ppd', 'PPD skin test', 'tb'], ['gvhd', 'Graft-versus-host disease', 'gvhd']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 110–111')

MAP = dict(
  id='hypsim', title='Hypersensitivity Types in Motion', topic='immuno', after='hypimm',
  sub='The four hypersensitivity types drawn as mechanisms — IgE on mast cells, antibody on a cell, immune complexes in a vessel, '
      'and T cells — with a timeline of when each appears. Pick a classic example to see its type, its tag and its labs. '
      'Tap a type for its card',
  w=3500, h=2100,
  fa='110–111', src=[],
  lanes=[('hyAb', 'Antibody-mediated (I–III)', 'glycolysis'), ('hyT', 'T-cell mediated (IV)', 'tca'), ('hyEx', 'Examples', 'gluconeo')],
  nodes=[
    ('hy1', 'Type I', 380, 1800, 'hyAb', 'first and fast', ['hs1', 'asthma']),
    ('hy2', 'Type II', 820, 1800, 'hyAb', 'destruction · inflammation · dysfunction', ['hs2', 'warmaiha', 'mg']),
    ('hy3', 'Type III', 1260, 1800, 'hyAb', 'immune complexes', ['hs3', 'sle', 'psgn']),
    ('hy4', 'Type IV', 1700, 1800, 'hyT', 'the 4 Ts', ['hs4', 'eczema', 'tb']),
    ('hy5', 'Receptor antibodies', 2140, 1800, 'hyEx', 'MG · Graves', ['hyperthyroid', 'goodpasture']),
    ('hy6', 'Transplant reactions', 380, 1940, 'hyEx', 'hyperacute · GVHD', ['hyperacute', 'gvhd']),
    ('hy7', 'IgA deficiency', 820, 1940, 'hyEx', 'anaphylaxis to blood', ['igadef'])],
  panels=[
    (2420, 760, 1000, 'The four types (First Aid pp. 110–111)', [
      ('Type I', 'IgE cross-linked on mast cells → histamine · minutes · anaphylaxis, asthma'),
      ('Type II', 'IgG/IgM on a fixed antigen · AIHA, ITP, Goodpasture, MG, Graves'),
      ('Type III', 'immune complexes + complement · SLE, PSGN, serum sickness, Arthus'),
      ('Type IV', 'T cells, no antibody · 24–48 h · contact dermatitis, PPD, GVHD')]),
    (2420, 960, 1000, 'Tests (First Aid pp. 110–111)', [
      ('Type I', 'skin prick test · allergen-specific IgE · tryptase'),
      ('Type II', 'direct Coombs (on the cell) · indirect (free in serum)'),
      ('Type III', 'complement falls during active disease'),
      ('Type IV', 'PPD · patch testing · Candida skin test for T-cell function')])],
  dyn=dyn)
