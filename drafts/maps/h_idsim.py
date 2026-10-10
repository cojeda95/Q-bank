# Immunodeficiency Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Where each primary immunodeficiency breaks the line: lymphocytes (common γ chain → pre-B cell (BTK) → B cell →
# class switch (CD40L) → plasma cell; thymus → CD4 Th1/Th17 (STAT3) and CD8; WASp in the cytoskeleton), the
# neutrophil's journey (rolling → firm adhesion (CD18) → into tissue → phagolysosome (LYST) → killing (NADPH
# oxidase)) and the membrane attack complex (C5–C9). One `one` switch picks a disorder: an ✕ lands on its step,
# the antibody bars are redrawn and readouts give the cell counts and immunoglobulins.
# No new cards: every fact restates the pinned cards (xla, cvid, igadef, hyperigm, digeorge, scidx, wiskott, jobsyn,
# lad1, chediak, cgd, c5c9 — fact-checked against the corpus). Arrows are "–" where a card gives "normal or ↓"
# or no direction. Sources: First Aid 2025 pp. 104–105, 113–115, 126.
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
def box(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-soft"/>')
def step(x, y, lab, sub, w=230):
    add(f'<rect x="{x - w // 2}" y="{y - 36}" width="{w}" height="72" rx="16" class="dyn-cell"/>')
    text(lab, x, y - 4, 'nf-l1', 'middle'); text(sub, x, y + 16, 'nf-l2', 'middle')
def arrow(x0, y0, x1, y1):
    add(f'<path d="M{x0} {y0} L{x1} {y1}" class="dyn-line" marker-end="url(#ah-idLym)"/>')

TAG = 'nf-l2 dyn-tag'
Z = lambda *k: ['id:' + x for x in k]

# ════════ 1. lymphocytes ════════
box(160, 130, 2340, 840)
text('Lymphocytes — made in the marrow, T cells finished in the thymus', 180, 166, 'dyn-big')
text('B line across the top · T line below it', 180, 186, 'dyn-cap')
step(320, 330, 'Lymphoid progenitor', 'common γ chain (IL-7)')
step(640, 330, 'Pre-B cell', 'BTK passes the pre-BCR signal')
step(960, 330, 'Mature B cell', 'IgM and IgD on the surface')
step(1280, 330, 'Class switch', 'needs CD40L from a T cell')
step(1600, 330, 'Plasma cell', 'secretes antibody')
for a, b in [(435, 525), (755, 845), (1075, 1165), (1395, 1485)]:
    arrow(a, 330, b, 330)
step(640, 590, 'Thymus', '3rd–4th pharyngeal pouches')
step(960, 520, 'CD4⁺ T cells', 'help B cells · Th1')
step(1280, 520, 'Th17', 'STAT3 · calls in neutrophils')
step(960, 680, 'CD8⁺ T cells', 'kill infected cells')
arrow(405, 360, 555, 570); arrow(755, 575, 845, 530); arrow(755, 605, 845, 670); arrow(1075, 520, 1165, 520)
add('<path d="M1060 484 Q1180 420 1240 372" class="dyn-dash"/>')
text('CD40L', 1150, 440, 'nf-l2')
# immunoglobulin bars
IGX, IGY, IGH = 1820, 640, 220
IG = ['IgM', 'IgG', 'IgA', 'IgE']
text('Antibody levels', 1760, 380, 'nf-l1')
text('dashed line = normal', 1760, 400, 'dyn-cap')
add(f'<path d="M{IGX - 20} {IGY - IGH // 2} H{IGX + 4 * 110}" class="dyn-dash"/><path d="M{IGX - 20} {IGY} H{IGX + 4 * 110}" class="dyn-line"/>')
for i, g in enumerate(IG):
    text(g, IGX + i * 110 + 40, IGY + 26, 'nf-l1', 'middle')
LV = dict(norm=[1, 1, 1, 1], xla=[.1, .1, .1, .1], cvid=[.4, .3, .3, 1], igadef=[1, 1, .05, 1], hyperigm=[1.6, .1, .1, .1],
          scid=[.1, .1, .1, .1], wiskott=[.4, 1, 1.6, 1.8], job=[1, 1, 1, 1.95])
def bars(lv, when=None, unless=None):
    add(''.join(f'<rect x="{IGX + i * 110 + 10}" y="{IGY - round(IGH // 2 * v)}" width="60" height="{round(IGH // 2 * v)}" rx="6" '
                f'style="fill:var(--dk9);fill-opacity:.7"/>' for i, v in enumerate(lv)), when, unless)
bars(LV['norm'], unless=Z(*[k for k in LV if k != 'norm']))
for k, lv in LV.items():
    if k != 'norm': bars(lv, when=Z(k))
text('bar heights are schematic — the direction is what matters', 1760, 720, 'dyn-cap')
# tags under the lymphocyte box
TAGS = dict(xla='no mature B cells → no antibody of any class', cvid='B cells present but no plasma cells',
            igadef='only IgA is missing', hyperigm='no class switch: IgM piles up, IgG/IgA/IgE never made',
            digeorge='no thymus → few T cells · no parathyroids → low Ca²⁺', scid='no T or NK cells; B cells cannot work alone',
            wiskott='WASp lost: T cells and platelets cannot remodel actin', job='no Th17 → neutrophils never called: cold abscesses')
for k, t in TAGS.items():
    text(t, 180, 800, TAG, when=Z(k))

# ════════ 2. the neutrophil's job ════════
box(160, 880, 2340, 1460)
text('Phagocytes — reach the tissue, swallow, kill', 180, 916, 'dyn-big')
shapes.append(dict(vessel='M200 1040 H900', w=60, color='--dk12'))
text('blood', 210, 1000, 'dyn-cap')
step(370, 1180, 'Rolling', 'selectins', 200)
step(640, 1180, 'Firm adhesion', 'CD18 integrin', 200)
step(910, 1180, 'Into the tissue', 'pus forms', 200)
step(1240, 1180, 'Phagolysosome', 'LYST: fusion', 220)
step(1570, 1180, 'Killing', 'NADPH oxidase → O₂⁻ → H₂O₂', 260)
for a, b in [(470, 540), (740, 810), (1010, 1130), (1350, 1440)]:
    arrow(a, 1180, b, 1180)
step(2030, 1180, 'Membrane attack complex', 'C5–C9 · lyses Neisseria', 300)
TAGS2 = dict(lad='neutrophils stuck in the blood: high count, no pus · delayed cord separation',
             chediak='giant granules · partial albinism · neuropathy',
             cgd='catalase-positive organisms: S. aureus, Serratia, Nocardia, Burkholderia, Aspergillus',
             c5c9='recurrent Neisseria — meningococcal meningitis and bacteremia')
for k, t in TAGS2.items():
    text(t, 180, 1420, TAG, when=Z(k))

# ════════ 3. infections ════════
box(160, 1500, 2340, 1700)
text('Infections that point to it', 180, 1536, 'dyn-big')
INF = dict(xla='boys at about 6 months: encapsulated bacteria (S. pneumoniae, H. influenzae) · enteroviruses',
           cvid='after puberty: sinopulmonary infections, bronchiectasis · Giardia',
           igadef='mostly none · airway and GI infections · anaphylaxis to IgA in blood products',
           hyperigm='pyogenic infections · Pneumocystis, Cryptosporidium, CMV',
           digeorge='viral and fungal infections · neonatal tetany',
           scid='failure to thrive, thrush · Candida, Pneumocystis, CMV, varicella',
           wiskott='thrombocytopenia (small platelets), eczema, recurrent infections — WATER',
           job='cold staphylococcal abscesses, retained baby teeth, eczema, fractures',
           lad='skin and mucosal bacterial infections with no pus',
           chediak='recurrent pyogenic infections · mild bleeding',
           cgd='recurrent infections and granulomas',
           c5c9='Neisseria')
for k, t in INF.items():
    text(t, 180, 1576, TAG, when=Z(k))
text('pick a disorder', 180, 1576, 'dyn-cap', unless=['id:*'])

# ════════ 4. sites — one per step, ✕ where the disorder breaks it ════════
def site(x, y, lab, card, keys):
    return dict(x=x, y=y - 36, n=[0, -1], w=12, t='rec', l='', aria=lab, ions=[], c=card, block=Z(*keys))
sites = [
  site(320, 330, 'Common γ chain — SCID', 'scidx', ['scid']),
  site(640, 330, 'BTK — Bruton', 'xla', ['xla']),
  site(1280, 330, 'CD40L class switch — hyper-IgM', 'hyperigm', ['hyperigm']),
  site(1350, 330, 'IgA class switching — selective IgA deficiency', 'igadef', ['igadef']),
  site(1600, 330, 'Plasma cells — CVID', 'cvid', ['cvid']),
  site(640, 590, 'Thymus — DiGeorge', 'digeorge', ['digeorge']),
  site(960, 680, 'T cells — Wiskott-Aldrich', 'wiskott', ['wiskott']),
  site(1280, 520, 'Th17 — Job syndrome', 'jobsyn', ['job']),
  site(640, 1180, 'CD18 — leukocyte adhesion deficiency', 'lad1', ['lad']),
  site(1240, 1180, 'LYST — Chédiak-Higashi', 'chediak', ['chediak']),
  site(1570, 1180, 'NADPH oxidase — CGD', 'cgd', ['cgd']),
  site(2030, 1180, 'C5–C9 — terminal complement', 'c5c9', ['c5c9']),
]
# SCID's ✕ also falls on the thymus-derived T cells
sites.append(dict(x=960, y=484, n=[0, -1], w=12, t='rec', l='', aria='CD4 T cells', ions=[], c='scidx', block=Z('scid')))

# ════════ 5. motion: neutrophils along the vessel and out ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M210 1040 H890', len=680, speed=110, r=7, base=dict(neu=4), mods=[m(Z('lad'), set=dict(neu=9)), m(Z('chediak'), set=dict(neu=2))]),
  dict(d='M640 1070 V1140', len=70, speed=40, r=7, base=dict(neu=2), mods=[m(Z('lad'), set=dict(neu=0))]),
  dict(d='M1700 360 L1780 600', len=250, speed=80, r=6, base=dict(ab=3), mods=[m(Z('xla', 'scid'), set=dict(ab=0)), m(Z('cvid'), set=dict(ab=1))]),
]

# ════════ 6. readouts ════════
readouts = [
  dict(l='B cells', mods=[m(Z('xla'), d=-1), m(Z('cvid', 'hyperigm', 'digeorge'), d=0)]),
  dict(l='T cells', mods=[m(Z('digeorge', 'scid'), d=-1)]),
  dict(l='IgG', mods=[m(Z('xla', 'cvid', 'hyperigm', 'scid'), d=-1), m(Z('igadef'), d=0)]),
  dict(l='IgM', mods=[m(Z('xla', 'wiskott'), d=-1), m(Z('hyperigm'), d=1), m(Z('igadef'), d=0)]),
  dict(l='IgE', mods=[m(Z('job', 'wiskott'), d=1), m(Z('xla', 'hyperigm'), d=-1)]),
  dict(l='Neutrophils', mods=[m(Z('lad'), d=1), m(Z('chediak'), d=-1)]),
]

# ════════ 7. notes ════════
notes = {
  '': 'Each primary immunodeficiency breaks one step: making lymphocytes, finishing T cells in the thymus, switching or '
      'secreting antibody, getting neutrophils into tissue, killing what they swallow, or lysing with complement. The step '
      'predicts the infections. Pick a disorder.',
  'id:xla': 'Bruton agammaglobulinemia: BTK carries the pre-B-cell receptor signal, so B cells arrest at the pre-B stage — no '
            'mature B cells (absent CD19⁺) and no antibody of any class. Boys at about 6 months, when maternal IgG wears off; '
            'tiny tonsils and nodes. X-linked.',
  'id:cvid': 'Common variable immunodeficiency: B cells are made but do not become plasma cells — B-cell count normal, IgG low '
             'with low IgA or IgM. Presents after puberty; bronchiectasis, Giardia, and more autoimmune disease and lymphoma.',
  'id:igadef': 'Selective IgA deficiency — the most common primary immunodeficiency, usually silent. Low IgA with normal IgG and '
               'IgM; anaphylaxis to IgA in blood products; false-negative celiac serology.',
  'id:hyperigm': 'Hyper-IgM syndrome: without CD40L from helper T cells the B cell cannot class switch — IgM normal or high, IgG, '
                 'IgA and IgE low. Pyogenic and opportunistic infections (Pneumocystis, Cryptosporidium, CMV). Mostly X-linked.',
  'id:digeorge': 'DiGeorge syndrome (22q11.2): the 3rd and 4th pharyngeal pouches fail — no thymus (low T cells, absent thymic '
                 'shadow) and no parathyroids (low Ca²⁺, neonatal tetany), with conotruncal heart defects. CATCH-22.',
  'id:scid': 'SCID (X-linked common γ chain): IL-7 and IL-15 signals are lost, so T and NK cells fail and B cells cannot work '
             'without help — very low antibody. Failure to thrive, thrush, opportunistic infections; low TRECs on newborn screening.',
  'id:wiskott': 'Wiskott-Aldrich syndrome: WASp remodels actin for lymphocytes and platelets — thrombocytopenia with small '
                'platelets, eczema, recurrent infections (WATER). IgM low, IgA and IgE high. X-linked.',
  'id:job': 'Job syndrome (hyper-IgE, STAT3): no Th17 cells to call neutrophils to skin and mucosa — cold staphylococcal '
            'abscesses, retained baby teeth, coarse facies, eczema, fractures; very high IgE and eosinophilia.',
  'id:lad': 'Leukocyte adhesion deficiency: without CD18 neutrophils roll but cannot adhere and leave the blood — very high '
            'neutrophil count, no pus, delayed separation of the umbilical cord.',
  'id:chediak': 'Chédiak-Higashi syndrome: LYST loss stops phagosome–lysosome fusion — giant granules in neutrophils, '
                'neutropenia, partial albinism, neuropathy and mild bleeding.',
  'id:cgd': 'Chronic granulomatous disease: NADPH oxidase fails, so swallowed organisms are not killed. Catalase-positive '
            'organisms (S. aureus, Serratia, Nocardia, Burkholderia, Aspergillus) destroy their own H₂O₂. Abnormal DHR test; '
            'nitroblue tetrazolium stays yellow.',
  'id:c5c9': 'Terminal complement (C5–C9) deficiency: complement can opsonize but cannot lyse — recurrent Neisseria infection. '
             'CH50 low with a normal C3.',
}

dyn = dict(
  kinds=dict(neu=['neu', '--dk5'], ab=['ab', '--dk9']),
  groups=[['neu', 'Neutrophils'], ['ab', 'Antibody']],
  switches=[dict(id='id', label='Pick an immunodeficiency', type='one',
                 options=[['xla', 'Bruton agammaglobulinemia', 'xla'], ['cvid', 'CVID', 'cvid'], ['igadef', 'Selective IgA deficiency', 'igadef'],
                          ['hyperigm', 'Hyper-IgM syndrome', 'hyperigm'], ['digeorge', 'DiGeorge syndrome', 'digeorge'], ['scid', 'SCID', 'scidx'],
                          ['wiskott', 'Wiskott-Aldrich', 'wiskott'], ['job', 'Job syndrome (hyper-IgE)', 'jobsyn'],
                          ['lad', 'Leukocyte adhesion deficiency', 'lad1'], ['chediak', 'Chédiak-Higashi', 'chediak'],
                          ['cgd', 'Chronic granulomatous disease', 'cgd'], ['c5c9', 'Terminal complement (C5–C9)', 'c5c9']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 104–105, 113–115, 126')

MAP = dict(
  id='idsim', title='Immunodeficiency Simulator', topic='immuno', after='hypimm',
  sub='Lymphocytes from marrow to plasma cell and thymus, the neutrophil’s path from blood to killing, and the membrane attack '
      'complex — pick a primary immunodeficiency to see the step it breaks, the antibody pattern and the infections that give '
      'it away. Tap a step for its card',
  w=3500, h=2100,
  fa='104–105, 113–115, 126', src=[],
  lanes=[('idLym', 'Lymphocytes', 'glycolysis'), ('idPhag', 'Phagocytes & complement', 'tca'), ('idDx', 'Clues', 'gluconeo')],
  nodes=[
    ('id1', 'B-cell defects', 380, 1800, 'idLym', 'Bruton · CVID · IgA', ['xla', 'cvid', 'igadef']),
    ('id2', 'Class switching', 820, 1800, 'idLym', 'hyper-IgM', ['hyperigm']),
    ('id3', 'T-cell & combined', 1260, 1800, 'idLym', 'DiGeorge · SCID · WAS', ['digeorge', 'scidx', 'wiskott']),
    ('id4', 'Th17', 1700, 1800, 'idLym', 'Job syndrome', ['jobsyn']),
    ('id5', 'Neutrophil defects', 2140, 1800, 'idPhag', 'LAD · Chédiak · CGD', ['lad1', 'chediak', 'cgd', 'mpo']),
    ('id6', 'Complement', 380, 1940, 'idPhag', 'C5–C9 · C1 inhibitor', ['c5c9', 'hae']),
    ('id7', 'Catalase-positive bugs', 820, 1940, 'idDx', 'CGD organisms', ['catalasepos']),
    ('id8', 'Asplenia', 1260, 1940, 'idDx', 'encapsulated organisms', ['asplenia'])],
  panels=[
    (2420, 860, 1000, 'Which defect, which infections (First Aid pp. 113–115)', [
      ('B cells / antibody', 'encapsulated bacteria (sinopulmonary) · enteroviruses · Giardia'),
      ('T cells', 'viruses, fungi, Pneumocystis — opportunists'),
      ('Combined (SCID)', 'everything, from the first months'),
      ('Neutrophils', 'S. aureus and catalase-positives (CGD) · no pus (LAD)'),
      ('Terminal complement', 'Neisseria')]),
    (2420, 1100, 1000, 'Labs that decide it (First Aid pp. 114–115, 126)', [
      ('Bruton vs CVID', 'absent CD19⁺ B cells vs normal B-cell count'),
      ('Hyper-IgM', 'IgM normal or ↑ · IgG, IgA, IgE ↓'),
      ('SCID', 'low TRECs on newborn screening'),
      ('CGD', 'abnormal DHR flow cytometry · NBT stays yellow'),
      ('C5–C9', 'CH50 ↓ with normal C3')])],
  dyn=dyn)
