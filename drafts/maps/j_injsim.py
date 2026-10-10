# Cell Injury & Death Simulator (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# One cell drawn through the stages of injury — reversible (swelling, blebs, ribosomes off, chromatin clumped) and
# irreversible (membrane broken, enzymes leak, Ca²⁺ in, nucleus pyknosis → karyorrhexis → karyolysis) — or through
# apoptosis (shrinks, blebs, apoptotic bodies eaten, no inflammation), beside a tissue patch drawn for each necrosis
# pattern (coagulative, liquefactive, caseous, fat, fibrinoid, gangrenous). One `one` switch picks the state.
# No new cards: facts restate the pinned cards (cellinjury, necrosis, apoptosis, celladapt, freeradical, mi, tb,
# acutepanc, pan — fact-checked against the corpus). Drawings are schematic. Sources: First Aid 2025 pp. 202–206.
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

TAG = 'nf-l2 dyn-tag'
I = lambda *k: ['inj:' + x for x in k]
NEC = I('coag', 'liq', 'cas', 'fat', 'fibr', 'gang')
DEAD = I('irrev') + NEC

# ════════ 1. the cell ════════
box(160, 130, 1300, 1160)
text('One cell', 180, 166, 'dyn-big')
text('schematic · what the cell does as the injury deepens', 180, 186, 'dyn-cap')
CX, CY = 730, 600
# normal / reversible / irreversible / apoptotic outlines
add(f'<ellipse cx="{CX}" cy="{CY}" rx="300" ry="220" class="dyn-cell"/>', unless=I('rev', 'irrev', 'apop') + NEC)
add(f'<ellipse cx="{CX}" cy="{CY}" rx="360" ry="270" class="dyn-cell" style="stroke:var(--dk7)"/>'
    + ''.join(f'<circle cx="{CX + dx}" cy="{CY + dy}" r="26" class="dyn-cell" style="stroke:var(--dk7)"/>' for dx, dy in [(350, -60), (-340, 90), (120, -270)]),
    when=I('rev'))
add(f'<path d="M{CX - 360} {CY} A360 270 0 0 1 {CX - 40} {CY - 270} M{CX + 60} {CY - 268} A360 270 0 0 1 {CX + 360} {CY} '
    f'A360 270 0 0 1 {CX + 30} {CY + 270} M{CX - 70} {CY + 268} A360 270 0 0 1 {CX - 360} {CY}" style="fill:none;stroke:var(--bad);stroke-width:6;stroke-dasharray:24 14"/>',
    when=DEAD)
add(f'<ellipse cx="{CX}" cy="{CY}" rx="170" ry="130" class="dyn-cell" style="stroke:var(--dk3)"/>'
    + ''.join(f'<circle cx="{CX + dx}" cy="{CY + dy}" r="{r}" class="dyn-cell" style="stroke:var(--dk3)"/>' for dx, dy, r in [(250, -120, 50), (290, 60, 40), (-260, 100, 46)]),
    when=I('apop'))
add(f'<ellipse cx="{CX}" cy="{CY}" rx="350" ry="260" style="fill:var(--bad);fill-opacity:.06;stroke:none"/>', when=DEAD)
# nucleus
add(f'<circle cx="{CX}" cy="{CY}" r="80" style="fill:var(--dk9);fill-opacity:.35;stroke:var(--dk9);stroke-width:3"/>', unless=I('irrev', 'apop') + NEC)
add(f'<circle cx="{CX}" cy="{CY}" r="80" style="fill:none;stroke:var(--dk9);stroke-width:3"/>'
    + ''.join(f'<circle cx="{CX + dx}" cy="{CY + dy}" r="12" style="fill:var(--dk9)"/>' for dx, dy in [(-30, -20), (20, 30), (35, -25), (-25, 35)]), when=I('rev'))
add(''.join(f'<circle cx="{CX + dx}" cy="{CY + dy}" r="14" style="fill:var(--dk9)"/>' for dx, dy in [(-40, -30), (30, 20), (50, -40), (-20, 40), (10, -5)]), when=DEAD)
add(f'<circle cx="{CX}" cy="{CY}" r="40" style="fill:var(--dk9)"/>', when=I('apop'))
text('nucleus', CX, CY + 110, 'nf-l2', 'middle', unless=I('apop'))
# what each stage shows
STAGE = dict(
  rev=['REVERSIBLE: ATP falls → Na⁺/K⁺ and Ca²⁺ pumps stop → the cell swells', 'blebs · ribosomes detach (↓ protein synthesis) · chromatin clumps · myelin figures',
       'myocytes stop contracting within 1–2 minutes of ischemia — still reversible'],
  irrev=['IRREVERSIBLE: the plasma membrane breaks — enzymes such as troponin leak out', 'Ca²⁺ floods in and activates degradative enzymes · mitochondria and lysosomes fail',
         'nucleus: pyknosis → karyorrhexis → karyolysis'],
  apop=['APOPTOSIS: ATP-dependent, through caspases — the cell shrinks and blebs', 'chromatin condenses (pyknosis), the nucleus fragments; apoptotic bodies are eaten',
        'the membrane stays intact, so there is little inflammation'])
for k, lines in STAGE.items():
    for j, t in enumerate(lines):
        text(t, 180, 940 + j * 28, TAG if j == 0 else 'nf-l2', when=I(k))
text('necrosis: the membrane breaks, contents leak, inflammation follows', 180, 940, TAG, when=NEC)
text('pick a stage or a necrosis pattern', 180, 940, 'dyn-cap', unless=['inj:*'])

# ════════ 2. the tissue patch ════════
box(1340, 130, 2340, 1160)
text('The tissue — necrosis patterns', 1360, 166, 'dyn-big')
text('schematic sketches of what each pattern looks like', 1360, 186, 'dyn-cap')
TX, TY, TW, TH = 1420, 260, 840, 520
add(f'<rect x="{TX}" y="{TY}" width="{TW}" height="{TH}" rx="20" class="dyn-cell"/>')
GRID = [(TX + 70 + i * 120, TY + 70 + j * 120) for i in range(7) for j in range(4)]
add(''.join(f'<rect x="{x - 40}" y="{y - 40}" width="80" height="80" rx="10" style="fill:none;stroke:var(--line-2);stroke-width:2"/>'
            f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--dk9);fill-opacity:.5"/>' for x, y in GRID), unless=NEC)
# coagulative: outlines kept, nuclei gone, pinker
add(f'<rect x="{TX}" y="{TY}" width="{TW}" height="{TH}" rx="20" style="fill:var(--bad);fill-opacity:.12"/>'
    + ''.join(f'<rect x="{x - 40}" y="{y - 40}" width="80" height="80" rx="10" style="fill:none;stroke:var(--line-2);stroke-width:2"/>' for x, y in GRID), when=I('coag'))
# liquefactive: a cavity of fluid with neutrophils
add(f'<ellipse cx="{TX + TW // 2}" cy="{TY + TH // 2}" rx="300" ry="190" style="fill:var(--dk2);fill-opacity:.2;stroke:var(--dk2);stroke-width:3"/>'
    + ''.join(f'<circle cx="{TX + TW // 2 + dx}" cy="{TY + TH // 2 + dy}" r="16" class="dyn-cell" style="stroke:var(--dk5)"/>' for dx, dy in [(-120, -40), (-40, 60), (60, -70), (140, 30), (0, 0), (-180, 70)]),
    when=I('liq'))
# caseous: cheesy center walled off by a granuloma
add(f'<circle cx="{TX + TW // 2}" cy="{TY + TH // 2}" r="200" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:30;stroke-opacity:.35"/>'
    f'<circle cx="{TX + TW // 2}" cy="{TY + TH // 2}" r="140" style="fill:var(--surface);fill-opacity:.8"/>', when=I('cas'))
# fat: chalky white deposits
add(''.join(f'<ellipse cx="{TX + 140 + i * 140}" cy="{TY + 160 + (i % 2) * 180}" rx="60" ry="44" style="fill:var(--surface);stroke:var(--dk2);stroke-width:4"/>' for i in range(5)), when=I('fat'))
# fibrinoid: a vessel with a bright wall
add(f'<circle cx="{TX + TW // 2}" cy="{TY + TH // 2}" r="160" style="fill:none;stroke:var(--bad);stroke-width:40;stroke-opacity:.45"/>'
    f'<circle cx="{TX + TW // 2}" cy="{TY + TH // 2}" r="110" style="fill:var(--dk12);fill-opacity:.25"/>', when=I('fibr'))
# gangrenous: dark distal tissue
add(f'<path d="M{TX} {TY + 20} Q{TX + 300} {TY + 260} {TX + 520} {TY + TH} L{TX + TW} {TY + TH} L{TX + TW} {TY} Z" style="fill:var(--ink);fill-opacity:.55"/>', when=I('gang'))
PAT = dict(
  coag=['Coagulative', 'ischemic infarcts in most tissues except the brain', 'proteins denatured — cell outlines stay, nuclei vanish, ↑ eosinophilia'],
  liq=['Liquefactive', 'bacterial abscesses and brain infarcts', 'neutrophil enzymes digest the tissue — later a cystic cavity'],
  cas=['Caseous', 'TB, systemic fungi (Histoplasma), Nocardia', 'cheeselike debris walled off in a granuloma'],
  fat=['Fat', 'acute pancreatitis (lipase) or trauma (breast)', 'fatty acids bind Ca²⁺ — saponification, chalky white'],
  fibr=['Fibrinoid', 'vasculitis (polyarteritis nodosa), hypertensive emergency, preeclampsia', 'eosinophilic protein in the vessel wall'],
  gang=['Gangrenous', 'distal limbs and the GI tract after chronic ischemia', 'dry = coagulative · wet = superinfected, liquefactive'])
for k, (h, where, how) in PAT.items():
    text(h, 1360, 860, 'dyn-big', when=I(k)); text(where, 1360, 890, 'nf-l1', when=I(k)); text(how, 1360, 916, TAG, when=I(k))
text('normal tissue — pick a necrosis pattern', 1360, 860, 'dyn-cap', unless=NEC)
text('brain infarcts liquefy; every other infarct coagulates', 1360, 1100, 'nf-l2')

# ════════ 3. motion: enzymes leaking out, Ca²⁺ in ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{CX + 200} {CY - 120} L{CX + 460} {CY - 300}', len=320, speed=70, r=6, base=dict(), mods=[m(DEAD, set=dict(enz=4))]),
  dict(d=f'M{CX - 470} {CY + 300} L{CX - 220} {CY + 120}', len=310, speed=70, r=6, base=dict(), mods=[m(DEAD, set=dict(ca=4))]),
  dict(d=f'M{CX - 470} {CY - 40} H{CX - 330}', len=140, speed=50, r=6, base=dict(), mods=[m(I('rev'), set=dict(na=3))]),
]

# ════════ 4. sites ════════
sites = [
  dict(x=CX + 300, y=CY, n=[1, 0], w=14, t='pump', l='', aria='Na⁺/K⁺-ATPase — reversible injury', ions=[], c='cellinjury',
       low=I('rev'), stop=DEAD),
  dict(x=CX, y=CY - 220, n=[0, -1], w=14, t='ex', l='', aria='Apoptosis', ions=[], c='apoptosis'),
  dict(x=TX + TW - 30, y=TY + 30, n=[0, 1], w=14, t='ex', l='', aria='Necrosis patterns', ions=[], c='necrosis'),
]

# ════════ 5. readouts ════════
readouts = [
  dict(l='Cell volume', mods=[m(I('rev', 'irrev'), d=1), m(I('apop'), d=-1)]),
  dict(l='Membrane integrity', mods=[m(I('rev', 'apop'), d=0), m(DEAD, d=-1)]),
  dict(l='Inflammation', mods=[m(I('apop'), d=0), m(DEAD, d=1)]),
  dict(l='Serum enzymes (troponin)', mods=[m(I('rev'), d=0), m(I('irrev'), d=1)]),
]
# UNVERIFIED: "cell volume ↑" for irreversible injury (swelling continues) — the cellinjury card describes swelling as the reversible sign

# ════════ 6. notes ════════
notes = {
  '': 'A cell under stress first adapts, then is injured. Injury is reversible while only the pumps fail and the cell swells; '
      'it becomes irreversible when membranes break. Death is either necrosis (membrane breaks, inflammation) or apoptosis '
      '(programmed, membrane intact). Pick a stage or pattern.',
  'inj:rev': 'Reversible injury: ATP falls, the Na⁺/K⁺ and Ca²⁺ pumps stop and the cell swells — the earliest visible change. '
             'Blebs, ribosome detachment, chromatin clumping and myelin figures; function is lost fast but the cell can recover.',
  'inj:irrev': 'Irreversible injury: the plasma membrane breaks (troponin leaks into the blood), Ca²⁺ floods in and activates '
               'degradative enzymes, mitochondria and lysosomes fail; the nucleus goes through pyknosis, karyorrhexis and karyolysis.',
  'inj:apop': 'Apoptosis: programmed, ATP-dependent death through caspases (intrinsic/mitochondrial, extrinsic/Fas–TNF, or '
              'perforin–granzyme). The cell shrinks, condenses and breaks into apoptotic bodies that macrophages eat — the '
              'membrane stays intact, so there is little inflammation.',
  'inj:coag': 'Coagulative necrosis: ischemic infarcts everywhere except the brain — proteins denature, so cell outlines remain '
              'while nuclei disappear.',
  'inj:liq': 'Liquefactive necrosis: bacterial abscesses and brain infarcts — neutrophil enzymes digest the tissue, leaving a '
             'cavity.',
  'inj:cas': 'Caseous necrosis: TB, systemic fungi such as Histoplasma, and Nocardia — cheeselike debris walled off in a granuloma.',
  'inj:fat': 'Fat necrosis: lipase in acute pancreatitis (or trauma, as in the breast) frees fatty acids that bind Ca²⁺ — '
             'saponification, chalky white.',
  'inj:fibr': 'Fibrinoid necrosis: immune vasculitis (polyarteritis nodosa) or hypertensive emergency and preeclampsia — '
              'eosinophilic protein in the vessel wall.',
  'inj:gang': 'Gangrenous necrosis: distal limbs and the GI tract after chronic ischemia — dry gangrene is coagulative; wet '
              'gangrene is superinfected and liquefactive.',
}

dyn = dict(
  kinds=dict(enz=['enz', '--dk7'], ca=['ca', '--nf-ca'], na=['na', '--nf-na']),
  groups=[['enz', 'Leaking enzymes'], ['ca', 'Ca²⁺'], ['na', 'Na⁺ and water']],
  switches=[dict(id='inj', label='Pick a stage or a necrosis pattern', type='one',
                 options=[['rev', 'Reversible injury', 'cellinjury'], ['irrev', 'Irreversible injury', 'cellinjury'], ['apop', 'Apoptosis', 'apoptosis'],
                          ['coag', 'Coagulative necrosis', 'necrosis'], ['liq', 'Liquefactive necrosis', 'necrosis'], ['cas', 'Caseous necrosis', 'tb'],
                          ['fat', 'Fat necrosis', 'acutepanc'], ['fibr', 'Fibrinoid necrosis', 'pan'], ['gang', 'Gangrenous necrosis', 'necrosis']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 202–206')

MAP = dict(
  id='injsim', title='Cell Injury & Death Simulator', topic='path', after='genpath',
  sub='A cell taken from reversible to irreversible injury, or through apoptosis, beside a tissue patch for each necrosis pattern — '
      'coagulative, liquefactive, caseous, fat, fibrinoid and gangrenous. Tap the cell, the pump or the tissue for its card',
  w=3500, h=2100,
  fa='202–206', src=[],
  lanes=[('ijCell', 'The cell', 'glycolysis'), ('ijDeath', 'Death', 'tca'), ('ijEx', 'Examples', 'gluconeo')],
  nodes=[
    ('ij1', 'Adaptations', 380, 1300, 'ijCell', 'hypertrophy → dysplasia', ['celladapt', 'epimeta']),
    ('ij2', 'Reversible vs irreversible', 820, 1300, 'ijCell', 'swelling vs membrane breaks', ['cellinjury', 'freeradical']),
    ('ij3', 'Apoptosis', 1260, 1300, 'ijDeath', 'caspases · Bcl-2 · Fas', ['apoptosis', 'p53']),
    ('ij4', 'Necrosis patterns', 1700, 1300, 'ijDeath', 'six kinds', ['necrosis', 'ischemiavuln']),
    ('ij5', 'Infarcts', 380, 1440, 'ijEx', 'heart · kidney · brain', ['mi', 'atn', 'mitimeline']),
    ('ij6', 'Caseous & fat', 820, 1440, 'ijEx', 'TB · pancreatitis', ['tb', 'acutepanc']),
    ('ij7', 'Fibrinoid', 1260, 1440, 'ijEx', 'vasculitis · malignant HTN', ['pan', 'malignephro'])],
  panels=[
    (2420, 800, 1000, 'Necrosis vs apoptosis (First Aid pp. 204–205)', [
      ('Necrosis', 'exogenous injury · membrane breaks · contents leak · inflammation'),
      ('Apoptosis', 'ATP-dependent · caspases · membrane intact · little inflammation'),
      ('Apoptosis histology', 'eosinophilic cytoplasm · pyknosis · karyorrhexis · DNA laddering'),
      ('Bcl-2', 'blocks apoptosis — overexpressed in follicular lymphoma, t(14;18)')]),
    (2420, 1010, 1000, 'Reversible vs irreversible (First Aid p. 203)', [
      ('Reversible', 'swelling · blebs · ribosomes detach · chromatin clumps · myelin figures'),
      ('Irreversible', 'membrane breaks · Ca²⁺ in · mitochondria and lysosomes fail'),
      ('Nucleus', 'pyknosis → karyorrhexis → karyolysis')])],
  dyn=dyn)
