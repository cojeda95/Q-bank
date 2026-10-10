# Growth Signals & Targeted Drugs in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Growth factor → EGFR (or amplified HER2, which needs no ligand) → RAS (GTP on / GDP off, switched off by its own GTPase and
# by neurofibromin) → BRAF → MEK → ERK → nucleus → MYC → cell cycle, with the signal moving down. A `one` switch adds a
# mutation (EGFR-mutant, HER2 amplification, KRAS, NF1 loss, BRAF V600E, MYC translocation/amplification) so the pathway
# runs on its own; a second gives a drug (erlotinib/osimertinib, cetuximab, trastuzumab, vemurafenib + trametinib) and the
# map shows whether it stops the signal — and why anti-EGFR antibodies fail with KRAS. 3 readouts. Facts from the pinned
# cards; FA pages in `fa`. No new cards.
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

M = lambda *k: [f'mut:{x}' for x in k]
R = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(x, y, lab, sub='', w=260):
    add(f'<rect x="{x - w // 2}" y="{y - 36}" width="{w}" height="72" rx="28" class="dyn-cell"/>')
    text(lab, x, y + (0 if sub else 6), 'nf-l1', 'middle')
    if sub: text(sub, x, y + 22, 'nf-l2', 'middle')
# which step a drug blocks, and whether the signal reaches it
BLOCK = dict(tki='egfr', mab='egfr', trast='her2', braf='braf')
# a block works only if the driver sits at or above the blocked step
def works(drug, mut):   # only the drivers the cards pair each drug with
    return mut in dict(tki=('none', 'egfrm'), mab=('none', 'egfrm'), trast=('her2',), braf=('braf',))[drug]
MUTS = ['none', 'egfrm', 'her2', 'kras', 'nf1', 'braf', 'myc']
STOP = []
for d in BLOCK:
    for mu in MUTS:
        if works(d, mu):
            STOP.append(f'rx:{d}&!mut:*' if mu == 'none' else f'rx:{d}&mut:{mu}')
ON = ['mut:*']

text('Growth signals — EGFR/HER2 → RAS → BRAF → MEK → ERK → MYC', 180, 150, 'dyn-big')
text('a driver mutation keeps the pathway on by itself · each drug works on the driver it targets', 180, 176, 'dyn-cap')

add('<path d="M300 420 H2300" style="stroke:var(--dk3);stroke-width:14;opacity:.45"/>'); text('cell membrane', 320, 400, 'nf-l2')
add('<rect x="700" y="300" width="80" height="60" rx="16" style="fill:var(--dk4);fill-opacity:.5"/>'); text('growth factor', 740, 290, 'nf-l2', 'middle')
node(740, 470, 'EGFR', 'receptor tyrosine kinase')
node(1160, 470, 'HER2', 'no ligand of its own')
add('<rect x="1060" y="420" width="200" height="12" style="fill:var(--bad);opacity:.7"/>', when=M('her2'))
text('amplified — signals constantly', 1160, 560, 'nf-l1 dyn-tag', 'middle', when=M('her2'))
node(950, 680, 'RAS', 'GTP = on')
node(1500, 680, 'Neurofibromin (NF1)', 'GAP: speeds GTP hydrolysis', w=360)
node(950, 880, 'BRAF'); node(950, 1060, 'MEK'); node(950, 1240, 'ERK')
add('<ellipse cx="1650" cy="1150" rx="380" ry="230" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:3"/>')
text('nucleus', 1650, 960, 'nf-l1', 'middle')
node(1650, 1120, 'MYC', 'growth genes')
node(1650, 1290, 'Cell divides')
TAG = dict(egfrm='EGFR-mutant non-small cell lung cancer', kras='RAS stuck GTP-bound: ~90% pancreatic, ~½ colon, ~30% lung adenocarcinoma',
           nf1='both NF1 copies lost — RAS can’t be switched off (café-au-lait, neurofibromas, Lisch nodules)',
           braf='BRAF V600E signals to MEK without RAS: melanoma, hairy cell leukemia, papillary thyroid',
           myc='c-MYC t(8;14): Burkitt · N-MYC amplification: neuroblastoma', her2='HER2-amplified breast and gastric cancer')
for k, t in TAG.items(): text(t, 1300, 1480, 'nf-l1 dyn-tag', 'middle', when=M(k))
add(f'<rect x="820" y="644" width="260" height="72" rx="28" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=M('kras', 'nf1'))
add(f'<rect x="820" y="844" width="260" height="72" rx="28" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=M('braf'))
add(f'<rect x="1520" y="1084" width="260" height="72" rx="28" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=M('myc'))
add(f'<rect x="610" y="434" width="260" height="72" rx="28" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=M('egfrm'))
add(X(1500, 680, 14), when=M('nf1'))
# drugs
DRUG = dict(tki=(740, 430, 'erlotinib / osimertinib — kinase domain'), mab=(740, 330, 'cetuximab — blocks ligand binding'),
            trast=(1160, 400, 'trastuzumab — outside domain'), braf=(950, 880, 'vemurafenib + trametinib — BRAF and MEK'))
for k, (x, y, t) in DRUG.items():
    add(f'<circle cx="{x + 150}" cy="{y}" r="22" style="fill:var(--accent);opacity:.8"/>', when=R(k))
    text(t, x + 180, y + 6, 'nf-l2', when=R(k))
text('signal stopped', 1300, 1530, 'nf-l1', 'middle', when=STOP)
text('this drug’s target isn’t what drives the pathway — the signal goes on', 1300, 1530, 'nf-l1 dyn-tag', 'middle', when=['rx:*'], unless=STOP)
text('anti-EGFR antibodies don’t work in KRAS-mutant colon cancer', 1300, 1560, 'nf-l2', 'middle', when=['rx:mab&mut:kras', 'rx:tki&mut:kras'])
text('alone, a BRAF inhibitor meets resistance and paradoxically turns the pathway on in normal cells — so with MEK', 1300, 1560, 'nf-l2', 'middle', when=['rx:braf&mut:braf'])
text('cardiotoxicity — check the ejection fraction', 1300, 1560, 'nf-l2', 'middle', when=R('trast'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
SEG = [('M740 330 V434', 104, 'egfr'), ('M740 506 C740 600 900 620 950 644', 200, 'egfr'), ('M1160 506 C1160 600 1000 620 950 644', 200, 'her2'),
       ('M950 716 V844', 128, 'ras'), ('M950 916 V1024', 108, 'braf'), ('M950 1096 V1204', 108, 'mek'),
       ('M1080 1240 C1300 1240 1400 1140 1520 1120', 470, 'erk'), ('M1650 1156 V1254', 98, 'myc')]
LEVEL = dict(egfr=0, her2=0, ras=1, braf=2, mek=3, erk=4, myc=5)
DRV = dict(egfrm=0, her2=0, kras=1, nf1=1, braf=2, myc=5)
flows = []
for d, L, step in SEG:
    lv = LEVEL[step]
    on_driver = [f'mut:{k}' for k, v in DRV.items() if v <= lv and not (step == 'egfr' and k == 'her2') and not (step == 'her2' and k != 'her2')]
    stop_here = [s for s in STOP if dict(tki=0, mab=0, trast=0, braf=2)[s.split('&')[0][3:]] <= lv]
    flows.append(dict(d=d, len=L, speed=90, r=9, base=dict(sig=1 if step != 'her2' else 0),
                      mods=[m(on_driver, set=dict(sig=4)), m(stop_here, set=dict(sig=0))]))
flows.append(dict(d='M1320 680 H1120', len=200, speed=70, r=8, base=dict(gap=2), mods=[m(M('nf1'), set=dict(gap=0))]))
sites = [dict(x=740, y=506, n=[0, 1], w=10, t='rec', l='', aria='EGFR inhibitors', c='egfr', ions=[]),
         dict(x=1160, y=506, n=[0, 1], w=10, t='rec', l='', aria='HER2', c='her2', ions=[]),
         dict(x=1080, y=680, n=[1, 0], w=10, t='rec', l='', aria='RAS', c='kras', ions=[]),
         dict(x=1500, y=716, n=[0, 1], w=10, t='rec', l='', aria='NF1', c='nf1', ions=[]),
         dict(x=950, y=916, n=[1, 0], w=10, t='rec', l='', aria='BRAF and MEK inhibitors', c='braf', ions=[]),
         dict(x=1780, y=1120, n=[1, 0], w=10, t='rec', l='', aria='MYC', c='mycamp', ions=[])]

readouts = [
  dict(l='Signal without growth factor', mods=[dict(when=ON, d=1)]),
  dict(l='Cell proliferation', mods=[dict(when=STOP, d=-1), dict(when=ON, d=1)]),
  dict(l='Drug effective', mods=[dict(when=STOP, d=1), dict(when=['rx:*'], d=-1)]),
]

notes = {
  '': 'A growth factor activates EGFR; the signal passes to RAS (on with GTP, off when its own GTPase hydrolyzes it, sped up by '
      'neurofibromin), then BRAF → MEK → ERK → MYC, which switches on the genes for growth and cell-cycle entry.',
  'mut:egfrm': 'EGFR-mutant non-small cell lung cancer: the receptor signals on its own — EGFR kinase inhibitors work.',
  'mut:her2': 'HER2 has no ligand; amplified, it signals constantly — breast and gastric cancer. Trastuzumab (outside domain), lapatinib '
              '(kinase), T-DM1 (payload). Cardiotoxicity, often reversible.',
  'mut:kras': 'RAS activating mutations wreck its GTPase, so RAS stays on and drives RAF–MEK–ERK with no growth factor — the most common '
              'oncogenic aberration. Anti-EGFR antibodies are useless in KRAS-mutant colorectal cancer.',
  'mut:nf1': 'NF1: neurofibromin is a RAS GAP; losing both copies leaves RAS on in neural-crest cells — CICLOPSS.',
  'mut:braf': 'BRAF V600E signals to MEK without RAS — melanoma (~60%), hairy cell leukemia (nearly 100%), papillary thyroid, LCH. '
              'Vemurafenib/dabrafenib with trametinib/cobimetinib.',
  'mut:myc': 'MYC sits at the end: t(8;14) next to an immunoglobulin enhancer in Burkitt, N-MYC amplification in neuroblastoma — nothing '
             'upstream can switch it off.',
  'rx:tki': 'Erlotinib, gefitinib, afatinib, osimertinib block the EGFR kinase — EGFR-mutant NSCLC. Rash, diarrhea.',
  'rx:mab': 'Cetuximab, panitumumab block ligand binding — RAS wild-type colorectal and head and neck cancer. Acneiform rash, hypomagnesemia.',
  'rx:trast': 'Trastuzumab binds HER2’s outside domain — HER2-amplified breast and gastric cancer.',
  'rx:braf': 'BRAF + MEK inhibitors together; a BRAF inhibitor alone meets resistance fast and paradoxically switches the pathway on in '
             'normal cells.',
}

dyn = dict(
  kinds=dict(sig=['sig', '--dk1'], gap=['sig', '--dk6']), groups=[['sig', 'Signal']],
  switches=[dict(id='mut', label='Driver', type='one', options=[
              ['egfrm', 'EGFR mutation', 'egfr'], ['her2', 'HER2 amplification', 'her2'], ['kras', 'KRAS mutation', 'kras'],
              ['nf1', 'NF1 loss', 'nf1'], ['braf', 'BRAF V600E', 'braf'], ['myc', 'MYC activation', 'mycamp']]),
            dict(id='rx', label='Drug', type='one', options=[
              ['tki', 'Erlotinib / osimertinib', 'egfr'], ['mab', 'Cetuximab', 'egfr'], ['trast', 'Trastuzumab', 'her2'],
              ['braf', 'Vemurafenib + trametinib', 'braf']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 220, 443, 446–447 · Robbins ch 7 · Katzung ch 54')

MAP = dict(
  id='mapksim', title='Growth Signals in Motion', topic='heme', after='carcino',
  sub='Run the EGFR/HER2 → RAS → BRAF → MEK → ERK → MYC pathway, switch on a driver (EGFR, HER2, KRAS, NF1, BRAF, MYC) and see which '
      'targeted drug can still stop it — and why cetuximab fails with KRAS',
  w=3600, h=1900,
  fa='220, 443, 446, 447, 539',
  src=['Katzung ch 54 — Cancer Chemotherapy', 'Katzung ch 55 — Immunopharmacology', 'Robbins ch 7 — Neoplasia', 'Robbins ch 23 — The breast',
       'Marks ch 17 — The Molecular Biology of Cancer', 'Robbins ch 27 — Peripheral nerves and skeletal muscles',
       'Robbins ch 13 — Diseases of white blood cells, lymph nodes, spleen, and thymus'],
  lanes=[('mkRec', 'Receptors', 'glycolysis'), ('mkRas', 'RAS & below', 'tca'), ('mkNuc', 'Nucleus', 'gluconeo')],
  nodes=[
    ('mk1', 'EGFR inhibitors', 330, 1700, 'mkRec', 'kinase vs antibody', ['egfr'], 'hub'),
    ('mk2', 'HER2 · trastuzumab', 760, 1700, 'mkRec', 'cardiotoxic', ['her2']),
    ('mk3', 'RAS mutations', 1200, 1700, 'mkRas', 'stuck on', ['kras']),
    ('mk4', 'Neurofibromatosis 1', 1640, 1700, 'mkRas', 'lost brake', ['nf1']),
    ('mk5', 'BRAF · MEK inhibitors', 2080, 1700, 'mkRas', 'V600E', ['braf']),
    ('mk6', 'MYC', 330, 1820, 'mkNuc', 'Burkitt · neuroblastoma', ['mycamp'])],
  panels=[
    (2500, PANY, 1000, 'Genotype before you treat', [
      ('EGFR-mutant lung', 'EGFR kinase inhibitor'), ('RAS wild-type colon', 'cetuximab, panitumumab'),
      ('KRAS-mutant colon', 'anti-EGFR antibody won’t work'), ('HER2 3+ / FISH', 'trastuzumab'), ('BRAF V600E', 'BRAF + MEK inhibitors')])],
  dyn=dyn)
