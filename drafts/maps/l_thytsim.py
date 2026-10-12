# Thyroid Tumors in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A thyroid lobe with follicles and C cells, its capsule, the neck nodes and lymphatics, the veins, and the structures
# around it (trachea, esophagus, recurrent laryngeal nerve), with distant organs (lungs, bone, liver, brain). A `dx` switch
# grows a tumor and sends it the way its card says: follicular adenoma (capsule intact), follicular carcinoma (through the
# capsule into veins → blood), papillary (lymphatics → cervical nodes), anaplastic (straight into neck structures and lungs)
# and medullary (C cells → calcitonin, amyloid; RET/MEN2). An `fna` toggle shows what a needle aspirate can and cannot tell.
# Schematic. 4 readouts. Facts from the pinned cards; FA page in `fa`. No new cards.
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
TX, TY = 800, 760
DIST = dict(lung=(1700, 360, 'lungs'), bone=(1700, 560, 'bone'), liver=(1700, 760, 'liver'), brain=(1700, 960, 'brain'))

text('Thyroid tumors — through the capsule, into lymph or blood, or straight through the neck', 180, 150, 'dyn-big')
text('one thyroid lobe with its capsule · nodes and veins · distant organs on the right · schematic', 180, 176, 'dyn-cap')
add(f'<ellipse cx="{TX}" cy="{TY}" rx="320" ry="380" style="fill:var(--dk10);fill-opacity:.06;stroke:var(--dk10);stroke-width:8"/>')
text('capsule', TX + 330, TY - 330, 'nf-l2')
for i in range(5):
    for j in range(4):
        x, y = TX - 200 + i * 100, TY - 220 + j * 140
        add(f'<circle cx="{x}" cy="{y}" r="34" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:2"/>')
text('follicles', TX - 260, TY - 290, 'nf-l2')
for x, y in ((TX - 150, TY + 150), (TX + 150, TY - 80), (TX - 50, TY + 290)):
    add(f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--dk7);opacity:.7"/>')
text('C cells (calcitonin)', TX + 150, TY - 5, 'nf-l2')
add(f'<path d="M{TX - 520} 300 V1300" style="stroke:var(--dk5);stroke-width:60;opacity:.12;stroke-linecap:round"/>'); text('trachea', TX - 520, 280, 'nf-l2', 'middle')
add(f'<path d="M{TX - 420} 300 V1300" style="stroke:var(--dk6);stroke-width:40;opacity:.12;stroke-linecap:round"/>'); text('esophagus', TX - 420, 1340, 'nf-l2', 'middle')
add(f'<path d="M{TX - 360} 400 C{TX - 350} 700 {TX - 360} 1000 {TX - 370} 1300" style="fill:none;stroke:var(--dk7);stroke-width:5"/>'); text('recurrent laryngeal n.', TX - 340, 1260, 'nf-l2')
for y in (420, 620, 820):
    add(f'<ellipse cx="{TX + 520}" cy="{y}" rx="40" ry="28" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>')
text('cervical nodes', TX + 520, 360, 'nf-l1', 'middle')
add(f'<path d="M{TX + 320} {TY + 100} C{TX + 420} {TY + 80} {TX + 460} 980 {TX + 520} 1100 V1300" style="fill:none;stroke:var(--nf-h2o);stroke-width:16;opacity:.35"/>'); text('veins', TX + 540, 1260, 'nf-l2')
for k, (x, y, l) in DIST.items():
    add(f'<circle cx="{x}" cy="{y}" r="50" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'); text(l, x + 70, y + 6, 'nf-l1')
# tumors
add(f'<circle cx="{TX}" cy="{TY}" r="110" style="fill:var(--dk4);fill-opacity:.35;stroke:var(--ink-2);stroke-width:8"/>', when=D('aden'))
add(f'<circle cx="{TX + 200}" cy="{TY + 120}" r="110" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=D('fca'))
add(f'<path d="M{TX + 290} {TY + 60} l40 20" style="stroke:var(--bad);stroke-width:16"/>', when=D('fca'))
add(f'<circle cx="{TX - 40}" cy="{TY - 60}" r="100" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=D('pap'))
for x, y in ((TX - 70, TY - 80), (TX - 10, TY - 30), (TX - 40, TY - 100)):
    add(f'<circle cx="{x}" cy="{y}" r="10" style="fill:none;stroke:var(--ink);stroke-width:4"/>', when=D('pap'))
add(f'<path d="M{TX - 260} {TY - 300} C{TX - 100} {TY - 420} {TX + 300} {TY - 300} {TX + 300} {TY} C{TX + 300} {TY + 300} {TX} {TY + 420} {TX - 300} {TY + 260} C{TX - 420} {TY} {TX - 380} {TY - 200} {TX - 260} {TY - 300} Z" '
    'style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:6"/>', when=D('ana'))
add(f'<circle cx="{TX - 150}" cy="{TY + 150}" r="90" style="fill:var(--dk7);fill-opacity:.4;stroke:var(--bad);stroke-width:4"/>', when=D('med'))
for y in (420, 620, 820):
    add(f'<ellipse cx="{TX + 520}" cy="{y}" rx="50" ry="36" style="fill:var(--bad);fill-opacity:.4"/>', when=D('pap'))
SPREAD = dict(fca=('lung', 'bone', 'liver', 'brain'), ana=('lung',))
for d, ks in SPREAD.items():
    for k in ks:
        x, y, _ = DIST[k]; add(f'<circle cx="{x}" cy="{y}" r="50" style="fill:var(--bad);fill-opacity:.35"/>', when=D(d))
add(f'<path d="M{TX - 520} 700 v120" style="stroke:var(--bad);stroke-width:30;opacity:.5"/>', when=D('ana'))
TAG = dict(aden='follicular adenoma — uniform follicles inside an intact capsule; does not recur or spread',
           fca='follicular carcinoma — through the capsule into veins → bone, lungs, liver, brain; nodes usually spared',
           pap='papillary — clear grooved nuclei, psammoma bodies; lymphatics → cervical nodes · ~85%, radiation · RET/PTC, BRAF',
           ana='anaplastic — rapidly enlarging bulky mass into trachea, esophagus, nerve: dyspnea, dysphagia, hoarseness; death within a year',
           med='medullary — C cells → calcitonin → amyloid (Congo red) · RET: MEN2A/2B → prophylactic thyroidectomy')
for k, s in TAG.items(): text(s, 1000, 1480, 'nf-l1 dyn-tag', 'middle', when=D(k))
add(f'<path d="M{TX + 60} {TY - 470} L{TX - 20} {TY - 80}" style="stroke:var(--ink-2);stroke-width:6;stroke-linecap:round"/>'
    f'<rect x="{TX + 44}" y="{TY - 550}" width="36" height="80" rx="6" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:4"/>', when=['fna'])
text('FNA needle', TX + 96, TY - 505, 'nf-l1', when=['fna'])
text('FNA cannot tell follicular adenoma from carcinoma — the capsule must be examined after excision', 1000, 1520, 'nf-l1', 'middle', when=['fna&dx:aden', 'fna&dx:fca'])
text('FNA: clear grooved nuclei ± psammoma bodies make the diagnosis', 1000, 1520, 'nf-l1', 'middle', when=['fna&dx:pap'])

# ════════ motion ════════
def go(d, x0, y0, x1, y1, kind='tum', n=3):
    return dict(d=f'M{x0} {y0} C{(x0 + x1) / 2:.0f} {y0} {(x0 + x1) / 2:.0f} {y1} {x1} {y1}', len=900, speed=120, r=9, base={kind: n}, when=D(d))
flows = [go('pap', TX + 40, TY - 60, TX + 480, 620), go('pap', TX + 40, TY - 60, TX + 480, 420, n=2),
         go('fca', TX + 330, TY + 80, TX + 520, 1100)] + \
        [go('fca', TX + 520, 1100, x - 50, y, n=2) for k, (x, y, _) in DIST.items()] + \
        [go('ana', TX - 300, TY, TX - 500, TY + 40), go('ana', TX + 300, TY - 300, 1650, 360),
         dict(d=f'M{TX - 150} {TY + 150} C{TX - 100} {TY + 300} {TX} {TY + 400} {TX + 100} {TY + 500}', len=400, speed=80, r=8, base=dict(calc=4), when=D('med'))]
sites = [dict(x=TX - 120, y=TY - 160, n=[-1, -1], w=10, t='rec', l='', aria='Papillary carcinoma', c='papca', ions=[]),
         dict(x=TX + 320, y=TY + 180, n=[1, 1], w=10, t='rec', l='', aria='Follicular neoplasms', c='follneo', ions=[]),
         dict(x=TX - 320, y=TY + 300, n=[-1, 1], w=10, t='rec', l='', aria='Anaplastic carcinoma', c='anapca', ions=[]),
         dict(x=TX - 240, y=TY + 230, n=[-1, 1], w=10, t='rec', l='', aria='Medullary carcinoma', c='medullary', ions=[])]

readouts = [
  dict(l='Cervical node spread', mods=[dict(when=D('pap'), d=1), dict(when=D('fca', 'aden'), d=0)]),
  dict(l='Blood-borne metastases', mods=[dict(when=D('fca', 'ana'), d=1), dict(when=D('aden'), d=0)]),
  dict(l='Calcitonin', mods=[dict(when=D('med'), d=1)]),
  dict(l='Airway & swallowing', mods=[dict(when=D('ana'), d=-1)]),
]

notes = {
  '': 'Follicular cells line the follicles; C cells between them make calcitonin; a capsule surrounds the lobe. Thyroid cancers '
      'differ in how they escape: follicular by blood, papillary by lymph, anaplastic by direct invasion.',
  'dx:aden': 'Follicular adenoma: a solitary circumscribed nodule of uniform follicles with an intact capsule — no invasion; usually '
             'a cold nodule; does not recur or metastasize.',
  'dx:fca': 'Follicular carcinoma: capsular and/or vascular invasion; veins carry it to bone, lungs, liver, brain; nodes usually '
            'spared. Widely invasive: up to half die in 10 years; minimally invasive: > 90% survive.',
  'dx:pap': 'Papillary carcinoma: ~85%, ages 25–50, radiation; clear (Orphan Annie) grooved nuclei with pseudoinclusions, psammoma '
            'bodies; lymphatic spread to cervical nodes in up to half; RET/PTC, BRAF. Thyroidectomy ± radioiodine.',
  'dx:ana': 'Anaplastic carcinoma: undifferentiated, often arising from a differentiated cancer; rapidly enlarging bulky neck mass '
            'already in neck structures or lungs — dyspnea, dysphagia, hoarseness; death usually within a year.',
  'dx:med': 'Medullary carcinoma: parafollicular C cells make calcitonin, which forms stromal amyloid; germline RET in MEN2A/2B → '
            'prophylactic thyroidectomy; occasionally VIP or ACTH paraneoplastic syndromes.',
  'fna': 'Fine-needle aspiration reads nuclei, not capsules — it diagnoses papillary carcinoma but cannot separate a follicular '
         'adenoma from a minimally invasive carcinoma.',
}

dyn = dict(
  kinds=dict(tum=['mov', '--bad'], calc=['mov', '--dk7']), groups=[['mov', 'Tumor cells · calcitonin']],
  switches=[dict(id='dx', label='Tumor', type='one', options=[
              ['aden', 'Follicular adenoma', 'follneo'], ['fca', 'Follicular carcinoma', 'follneo'], ['pap', 'Papillary carcinoma', 'papca'],
              ['ana', 'Anaplastic carcinoma', 'anapca'], ['med', 'Medullary carcinoma', 'medullary']]),
            dict(id='fna', label='Test', type='toggle', on='Needle aspirate', off='Do an FNA', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 347, 356 · Robbins ch 24')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='thytsim', title='Thyroid Tumors in Motion', topic='endo', after='thyroid',
  sub='Grow a follicular adenoma or carcinoma, a papillary, anaplastic or medullary cancer, and watch each leave the thyroid its own '
      'way — blood, lymph, straight through the neck, or calcitonin — then see what a needle can tell',
  w=3600, h=1900,
  fa='347, 356',
  src=['Robbins ch 24 — The endocrine system'],
  lanes=[('ttFol', 'Follicular cell', 'tca'), ('ttC', 'C cell', 'glycolysis')],
  nodes=[
    ('tt1', 'Papillary thyroid carcinoma', 330, 1720, 'ttFol', 'lymph · psammoma', ['papca'], 'hub'),
    ('tt2', 'Follicular adenoma & carcinoma', 760, 1720, 'ttFol', 'capsule · blood', ['follneo']),
    ('tt3', 'Anaplastic thyroid carcinoma', 1200, 1720, 'ttFol', 'local invasion', ['anapca']),
    ('tt4', 'Medullary thyroid carcinoma', 1640, 1720, 'ttC', 'calcitonin · RET', ['medullary'])],
  panels=[
    (2500, PANY, 1000, 'How each spreads (Robbins ch 24)', [
      ('Papillary', 'lymph → cervical nodes'), ('Follicular', 'blood → bone, lung, liver, brain'), ('Anaplastic', 'direct into neck'),
      ('Medullary', 'calcitonin, amyloid')])],
  dyn=dyn)
