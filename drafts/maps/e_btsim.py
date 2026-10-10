# Brain Tumors in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A midline (sagittal) schematic: cerebrum, corpus callosum, ventricles, aqueduct, 4th ventricle, pineal, sella, cerebellum,
# brainstem, tentorium and spinal cord, with CSF flowing through the ventricles. A `one` switch grows each tumor where its card
# puts it (glioblastoma butterfly, IDH-mutant astrocytoma, oligodendroglioma, meningioma, vestibular schwannoma at the CPA,
# hemangioblastoma, pilocytic astrocytoma, medulloblastoma with drop metastases, ependymoma, pineal germ cell tumor,
# craniopharyngioma); masses that block CSF dilate the ventricles. A second `one` switch highlights the tumors the cards tie
# to children or adults. The CPA is drawn on the midline view but labelled lateral. 6 readouts. Facts from the pinned cards;
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

T = lambda *k: [f'tu:{x}' for x in k]
G = lambda *k: [f'ag:{x}' for x in k]
BLOCK = ('medullo', 'ependy', 'pineal', 'cranio')
PANY = 1180
def mass(x, y, r, when, col='--bad'):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var({col});fill-opacity:.45;stroke:var({col});stroke-width:4"/>', when=when)

text('Brain tumors — where each one grows, and what it blocks', 180, 150, 'dyn-big')
text('midline view, face to the left · supratentorial above the tentorium, posterior fossa below', 180, 176, 'dyn-cap')

# ════════ anatomy ════════
add('<ellipse cx="1000" cy="600" rx="720" ry="360" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:5"/>')
add('<path d="M640 560 C760 470 1180 470 1300 560" style="fill:none;stroke:var(--dk6);stroke-width:22;opacity:.5;stroke-linecap:round"/>')
text("corpus callosum", 1320, 540, "nf-l2")
add('<path d="M720 620 C820 560 1120 560 1200 640 C1120 610 840 610 720 620 Z" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:3"/>',
    unless=[f'tu:{b}' for b in BLOCK])
add('<path d="M700 640 C800 520 1150 520 1230 650 C1120 680 830 690 700 640 Z" style="fill:var(--nf-h2o);fill-opacity:.55;stroke:var(--bad);stroke-width:4"/>',
    when=[f'tu:{b}' for b in BLOCK])
text('lateral ventricle', 640, 680, 'nf-l2', 'end')
add('<ellipse cx="1010" cy="800" rx="34" ry="70" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:3"/>')
text('3rd', 1010, 900, 'nf-l2', 'middle')
add('<path d="M1060 860 L1250 1000" style="stroke:var(--nf-h2o);stroke-width:12;opacity:.7"/>'); text('aqueduct', 1210, 900, 'nf-l2')
add('<path d="M1250 990 L1360 1060 L1260 1120 Z" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:3"/>')
text('4th', 1300, 1150, 'nf-l2', 'middle')
add('<path d="M1110 900 C1090 1000 1110 1200 1150 1500" style="fill:none;stroke:var(--dk3);stroke-width:110;opacity:.15;stroke-linecap:round"/>')
text('brainstem → spinal cord', 1230, 1460, 'nf-l2')
add('<ellipse cx="1520" cy="1100" rx="230" ry="150" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:4"/>')
text('cerebellum', 1620, 1280, 'nf-l1', 'middle')
add('<path d="M1080 960 L1760 940" style="stroke:var(--ink-2);stroke-width:5;stroke-dasharray:14 8"/>'); text('tentorium', 1760, 920, 'nf-l2', 'end')
add('<circle cx="1090" cy="830" r="16" style="fill:var(--dk7);opacity:.7"/>'); text('pineal', 1080, 790, 'nf-l2', 'end')
add('<path d="M840 1010 a50 40 0 0 0 100 0" style="fill:none;stroke:var(--ink-3);stroke-width:4"/>'); text('sella', 790, 1050, 'nf-l2', 'end')
add('<ellipse cx="860" cy="950" rx="40" ry="14" style="fill:var(--dk9);opacity:.6"/>'); text('chiasm', 780, 940, 'nf-l2', 'end')
text('CPA (lateral to the pons)', 870, 1130, 'nf-l2', 'end')
text('frontal', 420, 560, 'nf-l1', 'middle')

# ════════ tumors ════════
add('<path d="M800 540 C760 420 920 400 980 500 C1040 400 1200 420 1160 540 C1140 620 1040 600 980 560 C920 600 820 620 800 540 Z" '
    'style="fill:var(--bad);fill-opacity:.5;stroke:var(--bad);stroke-width:4"/>', when=T('gbm'))
add('<ellipse cx="560" cy="700" rx="170" ry="120" style="fill:var(--ink-3);fill-opacity:.35;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:8 8"/>', when=T('astro'))
mass(560, 700, 60, T('astro'), '--ink-3')
mass(440, 620, 80, T('oligo'))
for dx_, dy_ in ((-30, -20), (20, 10), (-5, 35)): add(f'<circle cx="{440 + dx_}" cy="{620 + dy_}" r="7" style="fill:var(--ink)"/>', when=T('oligo'))
add('<path d="M900 242 a100 90 0 0 0 200 0 Z" style="fill:var(--bad);fill-opacity:.45;stroke:var(--bad);stroke-width:4"/>', when=T('mening'))
add('<path d="M1100 242 C1150 244 1200 248 1240 254" style="stroke:var(--bad);stroke-width:6"/>', when=T('mening'))
mass(1010, 1110, 50, T('schwan'))
mass(1540, 1100, 60, T('hemangio'))
add('<circle cx="1540" cy="1100" r="90" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--dk4);stroke-width:4"/>', when=T('pilo'))
mass(1480, 1060, 28, T('pilo'))
mass(1390, 1070, 70, T('medullo'))
mass(1300, 1060, 40, T('ependy'))
mass(1100, 840, 46, T('pineal'))
add('<circle cx="890" cy="930" r="62" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=T('cranio'))
for dx_ in (-20, 10, 30): add(f'<circle cx="{890 + dx_}" cy="{910 + abs(dx_)}" r="7" style="fill:var(--ink)"/>', when=T('cranio'))
TAG = dict(gbm='butterfly across the corpus callosum — pseudopalisading necrosis, GFAP ⊕',
           astro='diffuse, infiltrates beyond the visible lesion — IDH + TP53 + ATRX',
           oligo='frontal, calcified — fried-egg cells, chicken-wire capillaries',
           mening='dural-based, extra-axial, dural tail — whorls, psammoma bodies',
           schwan='CN VIII at the CPA — hearing loss, tinnitus · bilateral = NF2',
           hemangio='cerebellar, thin-walled capillaries — EPO → polycythemia · VHL',
           pilo='cerebellar cyst with a mural nodule — Rosenthal fibers',
           medullo='vermis → truncal ataxia · blocks the 4th ventricle · drop metastases',
           ependy='in the 4th ventricle — blocks CSF · perivascular pseudorosettes',
           pineal='compresses the aqueduct and dorsal midbrain — Parinaud syndrome',
           cranio='suprasellar — bitemporal hemianopia, growth failure, DI')
for k, s in TAG.items(): text(s, 1000, 1360, 'nf-l1 dyn-tag', 'middle', when=T(k))
text('noncommunicating hydrocephalus — ventricles dilate', 1000, 1400, 'nf-l1', 'middle', when=T('medullo', 'ependy', 'pineal'))
# age highlights
for x, y in ((1540, 1100), (1390, 1070), (1300, 1060), (890, 930)):
    add(f'<circle cx="{x}" cy="{y}" r="100" style="fill:none;stroke:var(--accent);stroke-width:5;stroke-dasharray:10 8"/>', when=G('ch'))
for x, y in ((980, 520), (440, 620), (890, 930)):
    add(f'<circle cx="{x}" cy="{y}" r="110" style="fill:none;stroke:var(--accent);stroke-width:5;stroke-dasharray:10 8"/>', when=G('ad'))
text('children: pilocytic (commonest primary), medulloblastoma (commonest malignant), ependymoma, craniopharyngioma',
     1000, 1320, 'nf-l1', 'middle', when=G('ch'))
text('adults: glioblastoma, oligodendroglioma · craniopharyngioma again at 65+', 1000, 1320, 'nf-l1', 'middle', when=G('ad'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M760 610 C900 580 1000 620 1010 760 L1010 840 L1250 1000 L1300 1060 L1320 1200 C1300 1300 1200 1380 1170 1500', len=1350,
       speed=110, r=8, base=dict(csf=4), mods=[m([f'tu:{b}' for b in BLOCK], set=dict(csf=6), speed=0.05)]),
  dict(d='M1390 1100 C1300 1250 1190 1380 1160 1500', len=480, speed=90, r=9, base=dict(met=3), when=T('medullo')),
  dict(d='M1540 1100 C1700 1200 1800 1300 1900 1400', len=500, speed=90, r=8, base=dict(rbc=4), when=T('hemangio')),
]
sites = [dict(x=980, y=430, n=[0, -1], w=10, t='rec', l='', aria='Glioblastoma', c='gbm', ions=[]),
         dict(x=560, y=800, n=[0, 1], w=10, t='rec', l='', aria='Astrocytoma, IDH-mutant', c='astroidh', ions=[]),
         dict(x=380, y=640, n=[-1, 0], w=10, t='rec', l='', aria='Oligodendroglioma', c='oligo', ions=[]),
         dict(x=1000, y=200, n=[0, -1], w=10, t='rec', l='', aria='Meningioma', c='meningioma', ions=[]),
         dict(x=960, y=1130, n=[-1, 0], w=10, t='rec', l='', aria='Schwannoma', c='schwannoma', ions=[]),
         dict(x=1600, y=1160, n=[1, 1], w=10, t='rec', l='', aria='Hemangioblastoma', c='hemangioblastoma', ions=[]),
         dict(x=1740, y=1090, n=[1, 0], w=10, t='rec', l='', aria='Pilocytic astrocytoma', c='pilocytic', ions=[]),
         dict(x=1420, y=1000, n=[0, -1], w=10, t='rec', l='', aria='Medulloblastoma', c='medullo', ions=[]),
         dict(x=1360, y=1110, n=[1, 1], w=10, t='rec', l='', aria='Ependymoma', c='ependymoma', ions=[]),
         dict(x=1140, y=800, n=[1, -1], w=10, t='rec', l='', aria='Pineal tumors', c='pineal', ions=[]),
         dict(x=900, y=1000, n=[0, 1], w=10, t='rec', l='', aria='Craniopharyngioma', c='craniopharyngioma', ions=[])]

readouts = [
  dict(l='Hydrocephalus', mods=[dict(when=T(*BLOCK), d=1)]),
  dict(l='Malignant', mods=[dict(when=T('gbm', 'medullo'), d=1), dict(when=T('pilo', 'mening', 'schwan'), d=-1)]),
  dict(l='Upward gaze', mods=[dict(when=T('pineal'), d=-1)]),
  dict(l='Hearing (one ear)', mods=[dict(when=T('schwan'), d=-1)]),
  dict(l='Temporal visual fields', mods=[dict(when=T('cranio'), d=-1)]),
  dict(l='Hematocrit', mods=[dict(when=T('hemangio'), d=1)]),
]

notes = {
  '': 'CSF flows from the lateral ventricles through the 3rd ventricle and the aqueduct into the 4th ventricle and out around the '
      'brain and cord. Pick a tumor to see where it grows; masses that block this path cause noncommunicating hydrocephalus.',
  'tu:gbm': 'Glioblastoma: the common, highly malignant adult primary, from astrocytes in the hemispheres; crosses the corpus '
            'callosum (butterfly). GFAP ⊕, pseudopalisading necrosis, EGFR amplification. Median survival about a year.',
  'tu:astro': 'Astrocytoma, IDH-mutant: diffusely infiltrating glioma — IDH1/2 + TP53 + ATRX. CNS WHO grade 2–4; even grade 4 '
              'does far better than IDH-wildtype glioblastoma. CDKN2A deletion makes it grade 4.',
  'tu:oligo': 'Oligodendroglioma: rare, slow-growing, frontal, often calcified. Fried-egg cells, chicken-wire capillaries; '
              'IDH-mutant with 1p/19q codeletion; chemosensitive (PCV).',
  'tu:mening': 'Meningioma: arachnoid cap cells; extra-axial, dural-based with a dural tail; pushes rather than invades. Whorls, '
               'psammoma bodies.',
  'tu:schwan': 'Vestibular schwannoma: Schwann cells on CN VIII at the cerebellopontine angle — unilateral sensorineural hearing '
               'loss, tinnitus; large ones hit CN V and VII. S-100 ⊕. Bilateral = NF2 (merlin, chromosome 22).',
  'tu:hemangio': 'Hemangioblastoma: cerebellar, closely packed thin-walled capillaries. With retinal angiomas → von Hippel-Lindau. '
                 'Can secrete EPO → secondary polycythemia.',
  'tu:pilo': 'Pilocytic astrocytoma: the commonest primary brain tumor of childhood; posterior fossa, cyst with a mural nodule. '
             'GFAP ⊕, Rosenthal fibers. Resection often curative.',
  'tu:medullo': 'Medulloblastoma: the commonest malignant brain tumor of childhood — small round blue cells, Homer-Wright rosettes. '
                'Vermis → truncal ataxia; compresses the 4th ventricle → hydrocephalus; seeds CSF → drop metastases.',
  'tu:ependy': 'Ependymoma: ependymal cells lining the ventricles, most often the 4th ventricle of children → hydrocephalus. '
               'Perivascular pseudorosettes. Poor prognosis.',
  'tu:pineal': 'Pineal germ cell tumor (like seminoma): compresses the aqueduct (hydrocephalus) and the dorsal midbrain — Parinaud: '
               'upward gaze palsy, convergence-retraction nystagmus, light-near dissociation.',
  'tu:cranio': 'Craniopharyngioma: Rathke pouch remnant above the sella — bitemporal hemianopia, growth failure, DI, hydrocephalus; '
               'calcified, cystic "machinery oil". Ages 5–15 and 65+.',
  'ag:ch': 'Children (card wording): pilocytic astrocytoma is the commonest primary brain tumor, medulloblastoma the commonest '
           'malignant one, ependymoma in the 4th ventricle, craniopharyngioma the commonest supratentorial tumor.',
  'ag:ad': 'Adults (card wording): glioblastoma is the common, highly malignant primary; oligodendroglioma in adults; '
           'craniopharyngioma has a second peak at 65 or older.',
}

dyn = dict(
  kinds=dict(csf=['mov', '--nf-h2o'], met=['mov', '--bad'], rbc=['mov', '--nf-blood']),
  groups=[['mov', 'CSF · tumor cells · red cells']],
  switches=[dict(id='tu', label='Tumor', type='one', options=[
              ['gbm', 'Glioblastoma', 'gbm'], ['astro', 'Astrocytoma, IDH-mutant', 'astroidh'], ['oligo', 'Oligodendroglioma', 'oligo'],
              ['mening', 'Meningioma', 'meningioma'], ['schwan', 'Schwannoma', 'schwannoma'],
              ['hemangio', 'Hemangioblastoma', 'hemangioblastoma'], ['pilo', 'Pilocytic astrocytoma', 'pilocytic'],
              ['medullo', 'Medulloblastoma', 'medullo'], ['ependy', 'Ependymoma', 'ependymoma'], ['pineal', 'Pineal tumor', 'pineal'],
              ['cranio', 'Craniopharyngioma', 'craniopharyngioma']]),
            dict(id='ag', label='Age', type='one', options=[['ch', 'Children', 'pilocytic'], ['ad', 'Adults', 'gbm']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 28')

MAP = dict(
  id='btsim', title='Brain Tumors in Motion', topic='heme', after='tumcns',
  sub='Grow each brain tumor where it lives — hemispheres, dura, CPA, cerebellum, 4th ventricle, pineal, sella — watch the ones that '
      'block CSF dilate the ventricles, and see which belong to children and which to adults',
  w=3600, h=1900,
  fa='539, 540, 542',
  src=['Robbins ch 28 — The central nervous system'],
  lanes=[('btSup', 'Supratentorial & dura', 'glycolysis'), ('btPf', 'Posterior fossa & midline', 'tca')],
  nodes=[
    ('bt1', 'Glioblastoma', 330, 1600, 'btSup', 'butterfly · EGFR', ['gbm'], 'hub'),
    ('bt2', 'Astrocytoma, IDH-mutant', 760, 1600, 'btSup', 'IDH + TP53 + ATRX', ['astroidh']),
    ('bt3', 'Oligodendroglioma', 1200, 1600, 'btSup', 'frontal · fried egg', ['oligo']),
    ('bt4', 'Meningioma', 1640, 1600, 'btSup', 'dural tail', ['meningioma']),
    ('bt5', 'Craniopharyngioma', 2080, 1600, 'btSup', 'suprasellar', ['craniopharyngioma']),
    ('bt6', 'Pilocytic astrocytoma', 330, 1780, 'btPf', 'cyst + nodule', ['pilocytic']),
    ('bt7', 'Medulloblastoma', 760, 1780, 'btPf', 'drop metastases', ['medullo']),
    ('bt8', 'Ependymoma', 1200, 1780, 'btPf', '4th ventricle', ['ependymoma']),
    ('bt9', 'Hemangioblastoma', 1640, 1780, 'btPf', 'VHL · EPO', ['hemangioblastoma']),
    ('bt10', 'Schwannoma', 2080, 1780, 'btPf', 'CPA · CN VIII', ['schwannoma']),
    ('bt11', 'Pineal tumors', 2520, 1780, 'btPf', 'Parinaud', ['pineal']),
    ('bt12', 'Neurofibromatosis type 2', 2520, 1600, 'btPf', 'bilateral schwannomas', ['nf2'])],
  panels=[
    (2500, PANY, 1000, 'Hallmark histology (Robbins ch 28)', [
      ('Glioblastoma', 'pseudopalisading necrosis'), ('Oligodendroglioma', 'fried-egg cells'), ('Meningioma', 'whorls, psammoma'),
      ('Pilocytic', 'Rosenthal fibers'), ('Medulloblastoma', 'Homer-Wright rosettes'), ('Ependymoma', 'perivascular pseudorosettes')])],
  dyn=dyn)
