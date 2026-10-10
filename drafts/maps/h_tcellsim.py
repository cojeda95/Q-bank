# T-Cell Activation in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A dendritic cell presents peptide on MHC II to a naive CD4 T cell: signal 1 (TCR–MHC) plus signal 2 (B7–CD28) →
# calcineurin → NFAT → IL-2 gene → IL-2 back onto its own receptor (CD25) → mTOR → the cell divides. The brakes
# CTLA-4 and PD-1 sit on the same membrane. One `one` switch breaks or boosts a step: signal 1 alone (anergy), a
# superantigen, cyclosporine/tacrolimus, abatacept/belatacept, basiliximab, sirolimus, a checkpoint inhibitor, bare
# lymphocyte syndrome — with ✕ on the blocked molecule and the flows stopping downstream. 4 readouts. Facts from the
# pinned cards (tcellact, tcrcd3, superag, calcineurin, ctla4ig, il2drugs, mtor, checkpoint, blsyn, thelperreg);
# FA pages in `fa`. No new cards.
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


SW = 'x'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 800
NO_NFAT = ['anergy', 'csa', 'abat', 'bls']
NO_IL2R = NO_NFAT + ['bas']
NO_PROL = NO_IL2R + ['siro']
BOOST = ['sag', 'cpi']

text('T-cell activation — two signals, then IL-2', 180, 150, 'dyn-big')
text('every step from the synapse to division is a drug target in transplantation', 180, 176, 'dyn-cap')
# APC
add('<path d="M200 300 Q260 220 420 260 Q560 200 700 290 L800 300 V1000 L700 1020 Q520 1090 380 1030 Q220 1000 200 900 Z" class="dyn-cell"/>')
text('Dendritic cell', 470, 330, 'nf-l1', 'middle')
text('(antigen-presenting cell)', 470, 356, 'nf-l2', 'middle')
# T cell
add('<ellipse cx="1590" cy="680" rx="720" ry="430" class="dyn-cell"/>')
text('Naive CD4 T cell', 1590, 300, 'nf-l1', 'middle')
# synapse pairs: APC side label, T side label, y
# UNVERIFIED: PD-L1 is drawn on the APC for one picture; the checkpoint card places it on tumor cells
PAIRS = [('MHC II + peptide', 'TCR–CD3 (+ CD4)', 430, 'signal 1'), ('B7 (CD80/86)', 'CD28', 600, 'signal 2'),
         ('B7', 'CTLA-4 (brake)', 770, ''), ('PD-L1 (tumor cells too)', 'PD-1 (brake)', 920, '')]
for a, b, y, s in PAIRS:
    add(f'<rect x="760" y="{y - 22}" width="60" height="44" rx="12" style="fill:var(--dk5);fill-opacity:.6"/>')
    text(a, 740, y + 6, 'nf-l2', 'end')
    text(b, 960, y + 6, 'nf-l1')
    if s: text(s, 960, y + 30, 'nf-l2')
add('<rect x="760" y="408" width="60" height="44" rx="12" style="fill:var(--surface);stroke:var(--bad);stroke-width:3"/>', when=O('bls'))
text('no MHC II', 740, 470, 'nf-l1 dyn-tag', 'end', when=O('bls'))
add('<rect x="760" y="578" width="60" height="44" rx="12" style="fill:var(--surface);stroke:var(--line-2);stroke-width:3"/>', when=O('anergy'))
text('no B7 on this cell', 740, 650, 'nf-l1 dyn-tag', 'end', when=O('anergy'))
add('<rect x="700" y="570" width="60" height="60" rx="12" style="fill:var(--dk11);fill-opacity:.7"/>', when=O('abat'))
text('CTLA-4-Ig covers B7', 680, 650, 'nf-l1 dyn-tag', 'end', when=O('abat'))
add('<path d="M770 390 Q860 330 930 400" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=O('sag'))
text('superantigen clamps MHC II to TCR Vβ — outside the groove', 740, 380, 'nf-l1 dyn-tag', 'end', when=O('sag'))
# inside
add('<circle cx="1640" cy="720" r="170" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:3"/>')
text('Nucleus — IL-2 gene', 1640, 726, 'nf-l1', 'middle')
text('Calcineurin', 1280, 470, 'nf-l1', 'middle')
text('NFAT', 1440, 560, 'nf-l2', 'middle')
text('CD25 (IL-2 receptor α)', 1980, 330, 'nf-l1', 'middle')
text('mTOR', 2030, 626, 'nf-l1', 'end')
text('cell cycle → clones', 2060, 1000, 'nf-l1', 'middle')
for i, (dx, dy) in enumerate(((0, 0), (90, 40), (-80, 50), (20, 100))):
    add(f'<circle cx="{2060 + dx}" cy="{870 + dy}" r="36" class="dyn-cell"/>', unless=O(*NO_PROL))
add('<circle cx="2060" cy="900" r="36" class="dyn-cell"/>', when=O(*NO_PROL))
text('anergy — signal 1 without signal 2', 1590, 1060, 'nf-l1 dyn-tag', 'middle', when=O('anergy', 'abat'))
text('massive polyclonal activation — cytokine storm, shock', 1590, 1060, 'nf-l1 dyn-tag', 'middle', when=O('sag'))
text('brakes off — T cells attack the tumor (and sometimes self)', 1590, 1060, 'nf-l1 dyn-tag', 'middle', when=O('cpi'))
text('no CD4 lineage — combined immunodeficiency', 1590, 1060, 'nf-l1 dyn-tag', 'middle', when=O('bls'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M960 440 C1100 440 1200 470 1240 480', len=300, speed=90, r=7, base=dict(s=4), mods=[m(O('bls'), set=dict(s=0)), m(O(*BOOST), set=dict(s=7))]),
  dict(d='M1300 490 C1400 540 1460 600 1500 640', len=230, speed=90, r=7, base=dict(s=4), mods=[m(O(*NO_NFAT), set=dict(s=0)), m(O(*BOOST), set=dict(s=7))]),
  dict(d='M1780 640 C1900 540 1960 440 1980 360', len=340, speed=110, r=7, base=dict(il2=5), mods=[m(O(*NO_NFAT), set=dict(il2=0)), m(O(*BOOST), set=dict(il2=9))]),
  dict(d='M2000 360 C2060 420 2070 500 2060 580', len=240, speed=90, r=7, base=dict(il2=4), mods=[m(O(*NO_IL2R), set=dict(il2=0)), m(O(*BOOST), set=dict(il2=7))]),
  dict(d='M2060 620 V830', len=210, speed=80, r=7, base=dict(s=3), mods=[m(O(*NO_PROL), set=dict(s=0)), m(O(*BOOST), set=dict(s=6))]),
  dict(d='M1640 890 C1500 1000 1200 1000 1000 980', len=700, speed=150, r=8, base=dict(), when=O('sag'), mods=[m(O('sag'), set=dict(cyt=10))]),
]
sites = [
  dict(x=900, y=430, n=[1, 0], w=30, t='rec', l='', aria='TCR–CD3', c='tcrcd3', ions=[], block=O('bls'), boost=O(*BOOST)),
  dict(x=900, y=600, n=[1, 0], w=30, t='rec', l='', aria='CD28 — costimulation', c='tcellact', ions=[], stop=O('anergy', 'abat')),
  dict(x=900, y=770, n=[1, 0], w=30, t='rec', l='', aria='CTLA-4', c='checkpoint', ions=[], block=O('cpi')),
  dict(x=900, y=920, n=[1, 0], w=30, t='rec', l='', aria='PD-1', c='checkpoint', ions=[], block=O('cpi')),
  dict(x=1280, y=500, n=[0, 1], w=30, t='md', l='', aria='Calcineurin', c='calcineurin', ions=[], block=O('csa')),
  dict(x=1980, y=300, n=[0, -1], w=30, t='rec', l='', aria='CD25 — IL-2 receptor', c='il2drugs', ions=[], block=O('bas')),
  dict(x=2060, y=620, n=[1, 0], w=30, t='md', l='', aria='mTOR', c='mtor', ions=[], block=O('siro')),
]

readouts = [
  dict(l='IL-2', mods=[dict(when=O(*NO_NFAT), d=-1), dict(when=O(*BOOST), d=1)]),
  dict(l='T-cell proliferation', mods=[dict(when=O(*NO_PROL), d=-1), dict(when=O(*BOOST), d=1)]),
  dict(l='Systemic cytokines (fever, shock)', mods=[dict(when=O('sag'), d=1)]),
  dict(l='CD4 count', mods=[dict(when=O('bls'), d=-1)]),
]

notes = {
  '': 'A naive T cell needs two signals: its TCR recognizing peptide on MHC (signal 1) and B7 on the APC binding CD28 (signal 2). '
      'Then calcineurin activates NFAT, IL-2 is transcribed and acts on the cell’s own CD25, and mTOR drives division.',
  'x:anergy': 'Signal 1 without signal 2: the T cell sees its antigen but gets no costimulation, so it becomes anergic — a mechanism '
              'of peripheral tolerance.',
  'x:sag': 'Superantigens (TSST-1, staph enterotoxins, streptococcal pyrogenic exotoxins) clamp the outside of MHC II to the TCR Vβ '
           'region without processing, firing up to a fifth of all T cells — IL-1, IL-2, IFN-γ, TNF-α and shock.',
  'x:csa': 'Cyclosporine (with cyclophilin) and tacrolimus (with FKBP) block calcineurin, so NFAT isn’t activated and IL-2 isn’t '
           'transcribed. Nephrotoxicity, hypertension, neurotoxicity; CYP3A4 interactions.',
  'x:abat': 'Abatacept and belatacept (CTLA-4-Ig) bind B7, so CD28 gets no costimulation — signal 1 without signal 2. Abatacept for '
            'rheumatoid arthritis, belatacept for kidney transplants.',
  'x:bas': 'Basiliximab blocks CD25, the IL-2 receptor α chain: IL-2 is still made but can’t drive the cell — transplant induction.',
  'x:siro': 'Sirolimus blocks mTOR, the step between the IL-2 receptor and the cell cycle — so IL-2 is made and bound, but the cell '
            'doesn’t divide.',
  'x:cpi': 'Checkpoint inhibitors release the brakes: anti-CTLA-4 (ipilimumab) and anti-PD-1 (pembrolizumab, nivolumab) let T cells '
           'attack the tumor — with immune-related adverse events (colitis, hepatitis, pneumonitis, thyroiditis).',
  'x:bls': 'Bare lymphocyte syndrome (MHC class II deficiency): without MHC II, CD4 cells are never positively selected and antigen '
           'can’t be presented to them — low CD4 count, combined immunodeficiency.',
}

dyn = dict(
  kinds=dict(s=['sig', '--dk9'], il2=['il2', '--dk2'], cyt=['il2', '--bad']), groups=[['sig', 'Signals'], ['il2', 'IL-2 & cytokines']],
  switches=[dict(id=SW, label='Break or boost a step', type='one', options=[
    ['anergy', 'Signal 1 only — anergy', 'tcellact'], ['sag', 'Superantigen', 'superag'], ['csa', 'Cyclosporine · tacrolimus', 'calcineurin'],
    ['abat', 'Abatacept · belatacept', 'ctla4ig'], ['bas', 'Basiliximab (anti-CD25)', 'il2drugs'], ['siro', 'Sirolimus (mTOR)', 'mtor'],
    ['cpi', 'Checkpoint inhibitor', 'checkpoint'], ['bls', 'Bare lymphocyte syndrome', 'blsyn']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 100–101, 118–119, 131, 218, 446 · Katzung ch 55')

MAP = dict(
  id='tcellsim', title='T-Cell Activation in Motion', topic='immuno', after='immune',
  sub='MHC II–TCR (signal 1) and B7–CD28 (signal 2) switch on calcineurin, NFAT and IL-2, which drives the T cell to divide — '
      'remove signal 2, add a superantigen, or block calcineurin, B7, CD25, mTOR or the brakes and watch where activation stops',
  w=3500, h=1440,
  fa='100–101, 118–119, 131, 218, 446',
  src=[full('Katzung', 55), full('Robbins', 6)],
  lanes=[('tcSig', 'The signals', 'glycolysis'), ('tcDrug', 'Drugs on the pathway', 'tca'), ('tcDz', 'Disease', 'gluconeo')],
  nodes=[
    ('tc1', 'T-cell activation', 330, 1230, 'tcSig', 'two signals', ['tcellact'], 'hub'),
    ('tc2', 'TCR complex · T-helper fork', 760, 1230, 'tcSig', 'CD3 · Th1, Th2, Th17', ['tcrcd3', 'thelperreg']),
    ('tc3', 'Calcineurin inhibitors', 1200, 1230, 'tcDrug', 'no IL-2', ['calcineurin']),
    ('tc4', 'CTLA-4-Ig · anti-CD25', 1620, 1230, 'tcDrug', 'no signal 2 · no receptor', ['ctla4ig', 'il2drugs']),
    ('tc5', 'Sirolimus', 2020, 1230, 'tcDrug', 'mTOR', ['mtor']),
    ('tc6', 'Checkpoint inhibitors', 330, 1360, 'tcDrug', 'brakes off', ['checkpoint']),
    ('tc7', 'Superantigens', 760, 1360, 'tcDz', 'outside the groove', ['superag']),
    ('tc8', 'Bare lymphocyte syndrome', 1180, 1360, 'tcDz', 'no MHC II', ['blsyn'])],
  panels=[
    (2420, PANY, 1000, 'The pathway as drug targets (cards)', [
      ('B7 → CD28', 'abatacept, belatacept'),
      ('Calcineurin → NFAT', 'cyclosporine, tacrolimus'),
      ('IL-2 → CD25', 'basiliximab'),
      ('mTOR', 'sirolimus'),
      ('CTLA-4, PD-1 brakes', 'ipilimumab, pembrolizumab, nivolumab')])],
  dyn=dyn)
