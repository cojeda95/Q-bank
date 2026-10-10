# Lung Cancer in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A front view of the chest — trachea, bronchi, lungs, apex, SVC, mediastinal nerves — with target organs to the right
# (brain, breast, adrenal, kidney, bone). A `one` switch grows each tumor where its card puts it — adenocarcinoma
# (peripheral), squamous (central), small cell (central, metastatic at diagnosis), large cell (peripheral), carcinoid
# (polyp in a bronchus) — and sends its card-stated hormones to their targets; two more options show local spread
# (Pancoast tumor, SVC syndrome). A toggle gives a matching kinase inhibitor to a driver-mutant adenocarcinoma. 4 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
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

D = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
TG = dict(brain=(2050, 360), breast=(2050, 620), adrenal=(2050, 860), kidney=(2050, 1060), bone=(2050, 1280))

text('Lung cancer — where each type grows, and what it sends out', 180, 150, 'dyn-big')
text('front view of the chest · target organs on the right', 180, 176, 'dyn-cap')

# ════════ chest ════════
add('<path d="M1000 260 V560" style="stroke:var(--dk5);stroke-width:46;opacity:.25;stroke-linecap:round"/>'); text('trachea', 1040, 300, 'nf-l2')
add('<path d="M1000 560 C960 600 900 620 840 660 M1000 560 C1040 600 1100 620 1160 660" style="fill:none;stroke:var(--dk5);stroke-width:30;opacity:.25"/>')
add('<path d="M560 420 C540 300 640 260 760 300 C880 340 900 500 880 700 C860 1000 820 1200 680 1240 C520 1260 460 1100 480 900 C490 700 520 520 560 420 Z" '
    'style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>')
add('<path d="M1440 420 C1460 300 1360 260 1240 300 C1120 340 1100 500 1120 700 C1140 1000 1180 1200 1320 1240 C1480 1260 1540 1100 1520 900 C1510 700 1480 520 1440 420 Z" '
    'style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>')
text('right lung', 640, 1300, 'nf-l1', 'middle'); text('left lung', 1360, 1300, 'nf-l1', 'middle')
add('<path d="M900 260 V700" style="stroke:var(--nf-h2o);stroke-width:30;opacity:.3"/>'); text('SVC', 880, 280, 'nf-l2', 'end')
add('<ellipse cx="1000" cy="800" rx="90" ry="120" style="fill:var(--nf-blood);fill-opacity:.1;stroke:var(--dk3);stroke-width:3"/>'); text('heart', 1000, 810, 'nf-l2', 'middle')
add('<path d="M1060 300 C1080 420 1080 520 1060 620" style="fill:none;stroke:var(--dk9);stroke-width:5"/>'); text('recurrent laryngeal', 1090, 460, 'nf-l2')
add('<path d="M940 600 C930 800 920 1000 920 1180" style="fill:none;stroke:var(--dk9);stroke-width:5;stroke-dasharray:10 6"/>'); text('phrenic', 860, 1160, 'nf-l2', 'end')
add('<path d="M620 300 C560 260 500 240 440 230" style="fill:none;stroke:var(--dk9);stroke-width:5"/>'); text('sympathetic chain · brachial plexus', 430, 210, 'nf-l2', 'end')
for k, (x, y) in TG.items():
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>')
    text(k, x + 60, y + 6, 'nf-l1')

# ════════ tumors ════════
def tum(x, y, r, when, unless=None):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--bad);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=when, unless=unless)
tum(1380, 1000, 70, D('adeno'), unless=['dx:adeno&tki']); tum(1380, 1000, 30, ['dx:adeno&tki'])
tum(830, 680, 80, D('scc')); tum(870, 640, 95, D('sclc')); tum(600, 1000, 80, D('large'))
add('<ellipse cx="880" cy="640" rx="34" ry="20" style="fill:var(--bad);fill-opacity:.6"/>', when=D('carcinoid'))
tum(620, 350, 60, D('pancoast')); tum(880, 480, 70, D('svc'))
for x, y in ((700, 560), (1240, 620), (760, 900)):
    tum(x, y, 22, D('sclc'))
TAG = dict(adeno='adenocarcinoma — peripheral, glands, TTF-1 · commonest, incl. never-smokers',
           scc='squamous — central, keratin pearls, smoking · PTHrP → hypercalcemia', sclc='small cell — central, almost all smokers, metastatic at diagnosis · ACTH, ADH',
           large='large cell — peripheral, anaplastic · hCG → gynecomastia', carcinoid='carcinoid — polyp in a bronchus · only ~10% give carcinoid syndrome',
           pancoast='Pancoast — apex invades the sympathetic plexus → Horner, ulnar pain', svc='SVC syndrome — head and arm congestion')
for k, s in TAG.items(): text(s, 1000, 1400, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('EGFR/ALK/ROS1/MET inhibitor — shrinks a driver-mutant adenocarcinoma', 1000, 1440, 'nf-l1', 'middle', when=['dx:adeno&tki'])

# ════════ motion ════════
def hf(src, tgt, k, when):
    (x0, y0), (x1, y1) = src, TG[tgt]
    return dict(d=f'M{x0} {y0} C{x0 + 300} {y0} {x1 - 300} {y1} {x1 - 44} {y1}', len=1300, speed=140, r=9, base={k: 3}, when=when)
flows = [
  hf((870, 640), 'adrenal', 'acth', D('sclc')), hf((870, 640), 'kidney', 'adh', D('sclc')),
  hf((830, 680), 'bone', 'pthrp', D('scc')), hf((600, 1000), 'breast', 'hcg', D('large')),
  hf((870, 640), 'brain', 'met', D('sclc')),
  dict(d='M900 300 V660', len=360, speed=110, r=9, base=dict(blood=3), mods=[dict(when=D('svc'), speed=0.1, set=dict(blood=6))]),
  dict(d='M620 300 C560 260 500 240 440 230', len=200, speed=60, r=8, base=dict(met=2), when=D('pancoast')),
]
sites = [dict(x=1460, y=1000, n=[1, 0], w=10, t='rec', l='', aria='Adenocarcinoma', c='lcadeno', ions=[]),
         dict(x=760, y=740, n=[-1, 1], w=10, t='rec', l='', aria='Squamous cell carcinoma', c='lcscc', ions=[]),
         dict(x=960, y=560, n=[1, -1], w=10, t='rec', l='', aria='Small cell carcinoma', c='lcsclc', ions=[]),
         dict(x=520, y=1000, n=[-1, 0], w=10, t='rec', l='', aria='Large cell carcinoma', c='lclarge', ions=[]),
         dict(x=820, y=600, n=[-1, -1], w=10, t='rec', l='', aria='Carcinoid tumor', c='lccarcinoid', ions=[]),
         dict(x=560, y=320, n=[-1, -1], w=10, t='rec', l='', aria='Local spread', c='lclocal', ions=[]),
         dict(x=2050, y=1350, n=[0, 1], w=10, t='rec', l='', aria='Paraneoplastic syndromes', c='lcparaneo', ions=[]),
         dict(x=1480, y=1080, n=[1, 1], w=10, t='rec', l='', aria='Targeted therapy', c='lctarget', ions=[])]

readouts = [
  dict(l='Serum sodium', mods=[dict(when=D('sclc'), d=-1)]),
  dict(l='Cortisol', mods=[dict(when=D('sclc'), d=1)]),
  dict(l='Calcium', mods=[dict(when=D('scc'), d=1)]),
  dict(l='Head & arm venous pressure', mods=[dict(when=D('svc'), d=1)]),
]

notes = {
  '': 'Lung carcinomas differ by where they grow, who gets them and what they secrete. Any type can make any hormone, but ACTH '
      'and ADH come mostly from small cell and hypercalcemia mostly from squamous carcinoma.',
  'dx:adeno': 'Adenocarcinoma: commonest in both sexes and in never-smokers; peripheral, TTF-1 ⊕. About a third carry targetable '
              'drivers — EGFR (more in nonsmoking Asian women), ALK, ROS1, MET, RET, BRAF; KRAS ~30% (worse, almost never in '
              'never-smokers).',
  'dx:scc': 'Squamous cell: smoking, men; central in segmental bronchi → obstruction, atelectasis; keratin pearls, p40; spreads '
            'outside the thorax later. PTHrP → hypercalcemia; cavitation.',
  'dx:sclc': 'Small cell: neuroendocrine, ~1% in nonsmokers, metastatic at diagnosis, almost always fatal. Salt-and-pepper '
             'chromatin, nuclear molding; chromogranin, synaptophysin, CD56. Commonest ectopic hormone maker — ACTH (Cushing), '
             'ADH (SIADH). Very chemo- and radiosensitive.',
  'dx:large': 'Large cell: undifferentiated, peripheral, anaplastic, tobacco-related; may make hCG → gynecomastia; poor chemo '
              'response — resect; poor prognosis.',
  'dx:carcinoid': 'Bronchial carcinoid: low-grade neuroendocrine, under 60, 20–40% nonsmokers; polyp into a mainstem bronchus '
                  '(cough, hemoptysis, obstruction). Only ~10% cause the carcinoid syndrome. Resect.',
  'dx:pancoast': 'Pancoast (superior sulcus) tumor: an apical cancer invades the cervical sympathetic plexus and nearby nerves — '
                 'ulnar-distribution pain and ipsilateral Horner syndrome.',
  'dx:svc': 'SVC syndrome: venous congestion and edema of the head and arms. Local spread can also cause hoarseness (recurrent '
            'laryngeal), dysphagia, phrenic paralysis, effusions, tamponade.',
  'tki': 'Matching kinase inhibitors (EGFR: erlotinib, gefitinib, afatinib, osimertinib; ALK: crizotinib → alectinib, lorlatinib) '
         'prolong survival in driver-mutant adenocarcinoma; resistance mutations appear at recurrence.',
}

dyn = dict(
  kinds=dict(acth=['mov', '--dk4'], adh=['mov', '--nf-h2o'], pthrp=['mov', '--dk6'], hcg=['mov', '--dk7'], met=['mov', '--bad'],
             blood=['mov', '--nf-h2o']),
  groups=[['mov', 'Hormones · metastases · venous blood']],
  switches=[dict(id='dx', label='Tumor', type='one', options=[
              ['adeno', 'Adenocarcinoma', 'lcadeno'], ['scc', 'Squamous cell', 'lcscc'], ['sclc', 'Small cell', 'lcsclc'],
              ['large', 'Large cell', 'lclarge'], ['carcinoid', 'Carcinoid', 'lccarcinoid'], ['pancoast', 'Pancoast tumor', 'lclocal'],
              ['svc', 'SVC syndrome', 'lclocal']]),
            dict(id='tki', label='Drug', type='toggle', on='Kinase inhibitor given', off='Kinase inhibitor (adeno)', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 15')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='lcsim', title='Lung Cancer in Motion', topic='pulmo', after='lungcancer',
  sub='Grow each lung cancer where it lives — peripheral adenocarcinoma and large cell, central squamous and small cell, a '
      'bronchial carcinoid, a Pancoast tumor — and watch ACTH, ADH, PTHrP and hCG reach their targets',
  w=3600, h=1900,
  fa='224, 352, 446, 703, 704',
  src=['Robbins ch 15 — The lung', 'Katzung ch 54 — Cancer Chemotherapy'],
  lanes=[('lcNsc', 'Non-small cell', 'tca'), ('lcNe', 'Neuroendocrine', 'glycolysis'), ('lcSys', 'Spread & therapy', 'gluconeo')],
  nodes=[
    ('lc1', 'Adenocarcinoma', 330, 1700, 'lcNsc', 'peripheral · drivers', ['lcadeno'], 'hub'),
    ('lc2', 'Squamous cell carcinoma', 760, 1700, 'lcNsc', 'central · PTHrP', ['lcscc']),
    ('lc3', 'Large cell carcinoma', 1200, 1700, 'lcNsc', 'peripheral · hCG', ['lclarge']),
    ('lc4', 'Small cell carcinoma', 1640, 1700, 'lcNe', 'ACTH · ADH', ['lcsclc']),
    ('lc5', 'Bronchial carcinoid', 2080, 1700, 'lcNe', 'polyp · low grade', ['lccarcinoid']),
    ('lc6', 'Local spread', 2520, 1700, 'lcSys', 'Pancoast · SVC', ['lclocal']),
    ('lc7', 'Paraneoplastic syndromes', 2960, 1700, 'lcSys', 'hormones · antibodies', ['lcparaneo']),
    ('lc8', 'Targeted therapy', 330, 1840, 'lcSys', 'EGFR · ALK', ['lctarget'])],
  panels=[
    (2500, PANY, 1000, 'Hormone → syndrome (Robbins ch 15)', [
      ('ADH', 'SIADH, hyponatremia'), ('ACTH', 'Cushing syndrome'), ('PTHrP', 'hypercalcemia'), ('hCG', 'gynecomastia'),
      ('Serotonin, bradykinin', 'carcinoid syndrome')])],
  dyn=dyn)
