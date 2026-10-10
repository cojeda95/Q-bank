# Complement in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The three entry pathways (classical, lectin, alternative) drawn feeding one C3 hub, which drives the three
# effector arms (C3b opsonization, C3a/C5a inflammation, the C5b–C9 membrane attack complex), with the two brakes
# underneath (DAF/CD59 on our own red cells, C1 esterase inhibitor). One `one` switch breaks a piece: early
# component deficiency, C3 deficiency, C5–C9 deficiency, eculizumab, hereditary angioedema, PNH — an ✕ on the
# broken step, the flow stops or misfires, and a note names the disease. 5 readouts. Facts from the pinned cards
# (complementreg, c3def, c5c9, c5drugs, hae, pnh, sle, meningococcus, chemokines, macrophage); FA pages in `fa`.
# No new cards.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

# ── drawing helpers ──
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


SW = 'def'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 700
def X(cx, cy, s=26):
    return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def tbox(x0, y0, x1, y1):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="20" class="dyn-soft"/>')

text('Complement — three ways in, one hub, three jobs', 180, 160, 'dyn-big')
text('C3 is the hub: above it is how the cascade starts, below it the shared effector arm', 180, 186, 'dyn-cap')

# ════════ the three entries ════════
ENT = [('cl', 230, 'Classical', 'C1 binds IgG or IgM already on antigen', '→ C4, C2 → C3 convertase'),
       ('le', 470, 'Lectin', 'mannose-binding lectin on microbial sugars', '→ C4, C2 → C3 convertase'),
       ('al', 710, 'Alternative', 'spontaneous C3 cleavage, amplified on microbes', 'no antibody needed')]
for k, y, a, b, c in ENT:
    tbox(200, y, 700, y + 160)
    text(a, 224, y + 40, 'nf-l1'); text(b, 224, y + 66, 'nf-l2'); text(c, 224, y + 90, 'nf-l2')
# a drawn antibody on a bacterium (classical)
add('<ellipse cx="600" cy="350" rx="70" ry="26" style="fill:var(--dk4);fill-opacity:.4;stroke:var(--dk4);stroke-width:2"/>'
    '<path d="M600 324 V292 M600 292 L578 268 M600 292 L622 268" style="stroke:var(--dk9);stroke-width:6;stroke-linecap:round"/>')
add(X(450, 330), when=O('early'))
text('C1q, C4 or C2 missing', 224, 380, 'nf-l1 dyn-tag', when=O('early'))

# ════════ the hub ════════
HX, HY = 1000, 550
add(f'<circle cx="{HX}" cy="{HY}" r="105" style="fill:var(--dk9);fill-opacity:.16;stroke:var(--dk9);stroke-width:4"/>')
text('C3', HX, HY + 8, 'dyn-big', 'middle')
text('C3 convertase', HX, HY + 34, 'nf-l2', 'middle')
add(X(HX, HY, 46), when=O('c3'))
text('C3 missing — every arm fails', HX, HY + 150, 'nf-l1 dyn-tag', 'middle', when=O('c3'))

# ════════ the three jobs ════════
JOB = [('op', 230, 'Opsonization — C3b', 'coats microbes for phagocytes', 'and helps clear immune complexes'),
       ('in', 470, 'Inflammation — C3a, C4a, C5a', 'anaphylatoxins', 'C5a also recruits neutrophils'),
       ('ma', 710, 'Membrane attack complex — C5b–C9', 'punches holes in membranes', 'what neutralizes Neisseria')]
for k, y, a, b, c in JOB:
    tbox(1340, y, 2300, y + 160)
    text(a, 1364, y + 40, 'nf-l1'); text(b, 1364, y + 66, 'nf-l2'); text(c, 1364, y + 90, 'nf-l2')
# drawn targets: a phagocyte, a neutrophil, a pierced membrane
add('<ellipse cx="2160" cy="310" rx="90" ry="54" class="dyn-cell"/><circle cx="2210" cy="310" r="18" style="fill:var(--dk4);fill-opacity:.6"/>')
add('<circle cx="2160" cy="550" r="52" class="dyn-cell"/><path d="M2140 540 q10 -14 20 0 q10 14 20 0" style="fill:none;stroke:var(--dk9);stroke-width:5"/>')
add('<path d="M2060 790 H2260" style="stroke:var(--dk4);stroke-width:16;stroke-linecap:round"/>'
    '<rect x="2146" y="770" width="28" height="40" rx="6" style="fill:var(--surface);stroke:var(--bad);stroke-width:4"/>', unless=O('mac', 'ecu', 'c3'))
add(X(1820, 800), when=O('mac', 'ecu', 'c3'))
add(X(1820, 320), when=O('c3'))
add(X(1820, 560), when=O('c3'))
text('C5–C9 missing — no MAC', 1364, 850, 'nf-l1 dyn-tag', when=O('mac'))
text('eculizumab binds C5 — no MAC', 1364, 850, 'nf-l1 dyn-tag', when=O('ecu'))

# ════════ the brakes ════════
text('The brakes', 180, 950, 'dyn-big')
tbox(200, 980, 1180, 1260)
text('DAF (CD55) and CD59 on our own cells', 224, 1020, 'nf-l1')
text('held on by a GPI anchor — stop complement attacking self', 224, 1046, 'nf-l2')
add('<ellipse cx="1010" cy="1150" rx="110" ry="60" style="fill:var(--bad);fill-opacity:.18;stroke:var(--bad);stroke-width:3"/>')
text('red cell', 1010, 1156, 'nf-l2', 'middle')
add(X(780, 1150), when=O('pnh'))
text('PIGA mutation — no GPI anchor, no DAF or CD59', 224, 1100, 'nf-l1 dyn-tag', when=O('pnh'))
text('complement lyses the red cell', 224, 1126, 'nf-l2', when=O('pnh'))
tbox(1340, 980, 2300, 1260)
text('C1 esterase inhibitor', 1364, 1020, 'nf-l1')
text('restrains C1 — and kallikrein in the kinin pathway', 1364, 1046, 'nf-l2')
add(X(1820, 1150), when=O('hae'))
text('missing — kallikrein makes bradykinin: swelling', 1364, 1100, 'nf-l1 dyn-tag', when=O('hae'))
text('C4 is chronically consumed', 1364, 1126, 'nf-l2', when=O('hae'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = []
for k, y, *_ in ENT:
    flows.append(dict(d=f'M700 {y + 80} C820 {y + 80} 840 {HY} {HX - 105} {HY}', len=round(330 + abs(y + 80 - HY) * 0.7), speed=120, r=7,
                      base=dict(c=4), mods=[m(O('early'), set=dict(c=0))] if k == 'cl' else []))
for k, y, *_ in JOB:
    kind = 'mac' if k == 'ma' else 'c'
    mods = [m(O('c3'), set={kind: 0})] + ([m(O('mac', 'ecu'), set=dict(mac=0))] if k == 'ma' else [])
    flows.append(dict(d=f'M{HX + 105} {HY} C1180 {HY} 1200 {y + 80} 1340 {y + 80}', len=round(330 + abs(y + 80 - HY) * 0.7), speed=120, r=7,
                      base={kind: 4}, mods=mods))
flows.append(dict(d=f'M{HX} {HY + 105} C{HX} 900 1000 1000 1010 1090', len=560, speed=110, r=7, base=dict(mac=5), when=O('pnh')))
flows.append(dict(d='M1400 1200 H2260', len=860, speed=150, r=7, base=dict(bk=8), when=O('hae')))

sites = [
  dict(x=HX, y=HY - 105, n=[0, -1], w=20, t='rec', l='', aria='C3 — the complement cascade', c='complementreg', ions=[]),
  dict(x=2160, y=740, n=[0, -1], w=20, t='ch', l='', aria='Membrane attack complex', c='c5c9', ions=[]),
]

# ════════ readouts ════════
readouts = [
  dict(l='C3', mods=[dict(when=O('c3'), d=-1), dict(when=O('mac', 'hae'), d=0)]),
  dict(l='C4', mods=[dict(when=O('hae'), d=-1)]),
  dict(l='CH50', mods=[dict(when=O('early', 'c3', 'mac'), d=-1)]),
  dict(l='LDH', mods=[dict(when=O('pnh'), d=1)]),
  dict(l='Haptoglobin', mods=[dict(when=O('pnh'), d=-1)]),
]

notes = {
  '': 'Three triggers converge on C3: the classical pathway (C1 on antibody), the lectin pathway (MBL on microbial sugars) and '
      'the alternative pathway (spontaneous C3 cleavage). From C3: opsonization, anaphylatoxins and the membrane attack complex.',
  # UNVERIFIED: the cards give early-component deficiency as an SLE risk; "cleared poorly" is the inferred mechanism
  'def:early': 'Early classical components (C1q, C4, C2) missing: immune complexes are cleared poorly — a recognized risk factor '
               'for systemic lupus erythematosus.',
  'def:c3': 'C3 deficiency removes opsonization, the anaphylatoxins and the MAC at once — serious, recurrent pyogenic infections '
            '(sinopulmonary, sepsis, meningitis) and immune complex glomerulonephritis. C3 low, CH50 abnormal.',
  'def:mac': 'Terminal (C5–C9) deficiency: complement still opsonizes but can’t lyse, and the MAC is what neutralizes Neisseria — '
             'recurrent meningococcal and disseminated gonococcal infection. CH50 low with a normal C3.',
  'def:ecu': 'Eculizumab and ravulizumab bind C5 so the MAC can’t form — they stop the hemolysis of PNH, at the price of the same '
             'life-threatening meningococcal risk as inherited C5–C9 deficiency.',
  'def:hae': 'Hereditary angioedema: without C1 esterase inhibitor, kallikrein runs on and makes bradykinin — recurrent swelling of '
             'face, larynx and gut, not histamine-driven. Low C4 is the screening test; C3 is normal.',
  'def:pnh': 'PNH: a PIGA mutation in a stem cell removes the GPI anchor, so DAF (CD55) and CD59 are lost and complement lyses the '
             'red cells — intravascular hemolysis (LDH ↑, haptoglobin ↓) and venous thrombosis. Flow cytometry for CD55/CD59.',
}

dyn = dict(
  kinds=dict(c=['comp', '--dk9'], mac=['comp', '--bad'], bk=['kin', '--dk5']),
  groups=[['comp', 'Complement'], ['kin', 'Bradykinin']],
  switches=[dict(id=SW, label='Break a piece', type='one', options=[
    ['early', 'Early components (C1q, C4, C2)', 'sle'], ['c3', 'C3 deficiency', 'c3def'], ['mac', 'C5–C9 deficiency', 'c5c9'],
    ['ecu', 'Eculizumab (anti-C5)', 'c5drugs'], ['hae', 'C1 esterase inhibitor — HAE', 'hae'], ['pnh', 'No DAF/CD59 — PNH', 'pnh']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 104–105, 113, 140, 427–428 · Robbins ch 3, 6 · Katzung ch 55')

MAP = dict(
  id='complsim', title='Complement in Motion', topic='immuno', after='innate',
  sub='Classical, lectin and alternative pathways feed one C3 hub that opsonizes, inflames and punches holes — break a piece '
      '(early components, C3, C5–C9, eculizumab, C1 inhibitor, DAF/CD59) and watch what stops and what disease follows',
  w=3500, h=1580,
  fa='104–106, 113, 140, 427–428, 476, 676',
  src=[full('Robbins', 3), full('Robbins', 6), full('Robbins', 14), full('Katzung', 55)],
  lanes=[('cpPath', 'The cascade', 'glycolysis'), ('cpDef', 'Deficiencies', 'tca'), ('cpBrake', 'Brakes & drugs', 'gluconeo')],
  nodes=[
    ('cp1', 'The complement cascade', 330, 1360, 'cpPath', 'C3 is the hub', ['complementreg'], 'hub'),
    ('cp2', 'Phagocytes · neutrophils', 760, 1360, 'cpPath', 'opsonins · C5a', ['macrophage', 'chemokines']),
    ('cp3', 'C3 deficiency', 1180, 1360, 'cpDef', 'pyogenic infections', ['c3def']),
    ('cp4', 'C5–C9 deficiency', 1580, 1360, 'cpDef', 'Neisseria', ['c5c9', 'meningococcus']),
    ('cp5', 'Early components · SLE', 1990, 1360, 'cpDef', 'C1q, C4, C2', ['sle']),
    ('cp6', 'Hereditary angioedema', 330, 1490, 'cpBrake', 'C1 inhibitor', ['hae']),
    ('cp7', 'PNH', 760, 1490, 'cpBrake', 'CD55 · CD59', ['pnh']),
    ('cp8', 'Eculizumab', 1180, 1490, 'cpBrake', 'anti-C5', ['c5drugs'])],
  panels=[
    (2420, PANY, 1000, 'Reading C3 and C4 (complement cascade card)', [
      ('Low C3, low C4', 'classical activation'),
      ('Low C3, normal C4', 'alternative activation'),
      ('Low C4, normal C3', 'hereditary angioedema'),
      ('Low CH50, normal C3', 'terminal (C5–C9) deficiency')])],
  dyn=dyn)
