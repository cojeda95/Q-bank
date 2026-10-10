# Lab Techniques in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A bench that runs one technique at a time (`tech` switch) through three steps (`ph`, auto): PCR (denature → anneal →
# elongate), Southern / Northern / Western blots (gel → membrane → probe; DNA, RNA or protein), ELISA (antigen or antibody →
# enzyme-linked antibody → color), flow cytometry (fluorescent tags, cells read one at a time), karyotype (colchicine arrests
# mitosis), FISH (one locus lights — or does not, in a microdeletion) and CRISPR/Cas9 (guide RNA → cut → NHEJ knock-out or
# HDR knock-in). Drawings are schematic. 2 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

T = lambda *k: [f'tech:{x}' for x in k]
def TP(t, *p): return [f'tech:{t}&ph:{x}' for x in p]
PANY = 1180
BLOT = ('south', 'north', 'west')

text('Lab techniques — what each one does, step by step', 180, 150, 'dyn-big')
text('pick a technique, then step through it · drawings schematic', 180, 176, 'dyn-cap')
add('<rect x="300" y="260" width="1700" height="1060" rx="40" class="dyn-soft"/>')
STEP = dict(pcr=('denature — heat separates the strands', 'anneal — cool; primers bind', 'elongate — heat-stable polymerase adds dNTPs'),
            blot=('gel electrophoresis separates by size', 'transfer to a membrane', 'probe finds the target'),
            elisa=('antigen (direct) or antibody (indirect) on the well', 'enzyme-linked antibody binds', 'substrate → color'),
            flow=('tag cells with fluorescent antibodies', 'cells pass the laser one at a time', 'each cell’s markers are counted'),
            karyo=('culture the cells', 'colchicine disrupts the spindle — arrested in mitosis', 'stain and order the chromosomes'),
            fish=('fluorescent probe for one locus', 'probe hybridizes', 'microdeletion: one copy lights, the other does not'),
            crispr=('guide RNA leads Cas9 to its target', 'Cas9 cuts both strands', 'NHEJ → knock-out · donor DNA + HDR → knock-in'))
for k, (a, b, c) in STEP.items():
    ts = T(*BLOT) if k == 'blot' else T(k)
    for p, s in (('s1', a), ('s2', b), ('s3', c)):
        text(s, 1150, 1280, 'nf-l1 dyn-tag', 'middle', when=[f'{t}&ph:{p}' for t in ts])

# ════════ PCR ════════
for p, (y1, y2) in dict(s1=(470, 650), s2=(470, 650), s3=(470, 650)).items():
    add(f'<path d="M500 {y1} H1700 M500 {y2} H1700" style="stroke:var(--dk2);stroke-width:12"/>', when=TP('pcr', p))
add('<path d="M500 540 H1700 M500 580 H1700" style="stroke:var(--dk2);stroke-width:12;opacity:.25"/>', when=T('pcr'))
text('double-stranded template (before)', 520, 520, 'nf-l2', when=T('pcr'))
add('<path d="M600 490 H760 M1440 630 H1600" style="stroke:var(--accent);stroke-width:14"/>', when=TP('pcr', 's2', 's3'))
text('primers', 680, 470, 'nf-l2', 'middle', when=TP('pcr', 's2', 's3'))
add('<path d="M760 490 H1300 M1440 630 H900" style="stroke:var(--dk9);stroke-width:14"/>', when=TP('pcr', 's3'))
text('neonatal HIV · herpes encephalitis', 1100, 820, 'nf-l1', 'middle', when=T('pcr'))

# ════════ blots ════════
add('<rect x="500" y="400" width="500" height="700" rx="10" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3"/>', when=T(*BLOT))
text('gel', 750, 380, 'nf-l1', 'middle', when=T(*BLOT))
for i, x in enumerate((560, 680, 800, 920)):
    for j, y in enumerate((520, 640, 800, 960)):
        if (i + j) % 2 == 0:
            add(f'<rect x="{x - 40}" y="{y}" width="80" height="16" rx="4" style="fill:var(--dk5);opacity:.7"/>', when=[f'tech:{t}&ph:{p}' for t in BLOT for p in ('s1', 's2', 's3')])
add('<rect x="1250" y="400" width="500" height="700" rx="10" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>', when=[f'tech:{t}&ph:{p}' for t in BLOT for p in ('s2', 's3')])
text('membrane', 1500, 380, 'nf-l1', 'middle', when=[f'tech:{t}&ph:{p}' for t in BLOT for p in ('s2', 's3')])
for i, x in enumerate((1310, 1430, 1550, 1670)):
    for j, y in enumerate((520, 640, 800, 960)):
        if (i + j) % 2 == 0:
            add(f'<rect x="{x - 40}" y="{y}" width="80" height="16" rx="4" style="fill:var(--ink-3);opacity:.5"/>', when=[f'tech:{t}&ph:{p}' for t in BLOT for p in ('s2', 's3')])
add('<rect x="1270" y="796" width="100" height="24" rx="6" style="fill:var(--bad)"/>', when=[f'tech:{t}&ph:s3' for t in BLOT])
PR = dict(south='Southern — DNA, labeled DNA probe · e.g. CGG repeats in FMR1 (fragile X)', north='Northern — RNA · mRNA level, size, splicing errors',
          west='Western — protein, labeled antibody · confirms what ELISA screens')
for k, s in PR.items(): text(s, 1150, 1180, 'nf-l1', 'middle', when=T(k))

# ════════ ELISA ════════
add('<path d="M800 500 V900 C800 1000 1400 1000 1400 900 V500" style="fill:none;stroke:var(--ink-2);stroke-width:6"/>', when=T('elisa'))
add('<circle cx="1100" cy="920" r="20" style="fill:var(--dk10)"/>', when=T('elisa'))
add('<path d="M1100 900 V820 M1100 820 l-30 -40 M1100 820 l30 -40" style="stroke:var(--dk4);stroke-width:10"/>', when=TP('elisa', 's2', 's3'))
add('<circle cx="1100" cy="760" r="18" style="fill:var(--accent)"/>', when=TP('elisa', 's2', 's3'))
add('<path d="M810 720 V900 C810 990 1390 990 1390 900 V720 Z" style="fill:var(--accent);fill-opacity:.25"/>', when=TP('elisa', 's3'))
text('sensitive but less specific than Western — screens for HIV', 1100, 1180, 'nf-l1', 'middle', when=T('elisa'))

# ════════ flow ════════
add('<path d="M500 700 H1700" style="stroke:var(--nf-h2o);stroke-width:40;opacity:.25;stroke-linecap:round"/>', when=T('flow'))
add('<path d="M1100 400 V680" style="stroke:var(--bad);stroke-width:6"/>', when=TP('flow', 's2', 's3')); text('laser', 1120, 420, 'nf-l2', when=T('flow'))
text('leukemia immunophenotype · PNH · fetal cells in maternal blood · CD4 count', 1100, 1180, 'nf-l1', 'middle', when=T('flow'))

# ════════ karyotype / FISH ════════
for i, x in enumerate(range(520, 1700, 110)):
    add(f'<path d="M{x} 600 l20 60 l-20 60 M{x + 40} 600 l-20 60 l20 60" style="fill:none;stroke:var(--dk7);stroke-width:12;stroke-linecap:round"/>', when=TP('karyo', 's2', 's3'))
text('trisomies · sex-chromosome disorders — blood, marrow, amniotic fluid, placenta', 1100, 1180, 'nf-l1', 'middle', when=T('karyo'))
for x in (900, 1300):
    add(f'<path d="M{x} 500 V900" style="stroke:var(--dk7);stroke-width:40;opacity:.3;stroke-linecap:round"/>', when=T('fish'))
add('<circle cx="900" cy="620" r="26" style="fill:var(--accent)"/>', when=TP('fish', 's2', 's3'))
add('<circle cx="1300" cy="620" r="26" style="fill:var(--accent)"/>', when=TP('fish', 's2'))
add('<circle cx="1300" cy="620" r="26" style="fill:none;stroke:var(--ink-3);stroke-width:4;stroke-dasharray:6 6"/>', when=TP('fish', 's3'))
text('microdeletions, translocations, duplications', 1100, 1180, 'nf-l1', 'middle', when=T('fish'))

# ════════ CRISPR ════════
add('<path d="M500 600 H1700 M500 660 H1700" style="stroke:var(--dk2);stroke-width:12"/>', when=TP('crispr', 's1'))
add('<path d="M500 600 H1080 M500 660 H1080 M1120 600 H1700 M1120 660 H1700" style="stroke:var(--dk2);stroke-width:12"/>', when=TP('crispr', 's2', 's3'))
add('<ellipse cx="1100" cy="560" rx="90" ry="60" style="fill:var(--dk4);fill-opacity:.35;stroke:var(--dk4);stroke-width:4"/>', when=TP('crispr', 's1', 's2'))
text('Cas9 + guide RNA', 1100, 480, 'nf-l1', 'middle', when=TP('crispr', 's1', 's2'))
add('<rect x="1060" y="590" width="80" height="80" style="fill:var(--accent);opacity:.7"/>', when=TP('crispr', 's3'))
text('insert (HDR) or scar (NHEJ)', 1100, 720, 'nf-l1', 'middle', when=TP('crispr', 's3'))

# ════════ motion ════════
flows = [
  dict(d='M760 490 H1300', len=540, speed=100, r=8, base=dict(dntp=4), when=TP('pcr', 's3')),
  dict(d='M1440 630 H900', len=540, speed=100, r=8, base=dict(dntp=4), when=TP('pcr', 's3')),
  dict(d='M750 430 V1060', len=630, speed=80, r=8, base=dict(mol=4), when=[f'tech:{t}&ph:s1' for t in BLOT]),
  dict(d='M1000 750 H1250', len=250, speed=80, r=8, base=dict(mol=4), when=[f'tech:{t}&ph:s2' for t in BLOT]),
  dict(d='M1500 300 C1450 500 1350 700 1320 800', len=560, speed=90, r=9, base=dict(probe=3), when=[f'tech:{t}&ph:s3' for t in BLOT]),
  dict(d='M500 700 H1700', len=1200, speed=160, r=12, base=dict(cell=5), when=T('flow')),
  dict(d='M1100 400 V560', len=160, speed=60, r=9, base=dict(probe=3), when=TP('crispr', 's1')),
]
sites = [dict(x=480, y=490, n=[-1, 0], w=10, t='rec', l='', aria='PCR', c='pcr', ions=[]),
         dict(x=480, y=750, n=[-1, 0], w=10, t='rec', l='', aria='Blots', c='blots', ions=[]),
         dict(x=1420, y=900, n=[1, 0], w=10, t='rec', l='', aria='ELISA and flow cytometry', c='elisaflow', ions=[]),
         dict(x=1720, y=620, n=[1, 0], w=10, t='rec', l='', aria='Karyotype, FISH and CRISPR', c='cytogen', ions=[])]

readouts = [
  dict(l='Amplifies the target', mods=[dict(when=T('pcr'), d=1)]),
  dict(l='Specificity', mods=[dict(when=T('west'), d=1), dict(when=T('elisa'), d=-1)]),
]

notes = {
  '': 'Pick a technique and step through it.',
  'tech:pcr': 'PCR amplifies a chosen fragment: heat to separate (denature), cool so primers bind (anneal), warm so a '
              'heat-stable DNA polymerase adds dNTPs (elongate) — repeat. Neonatal HIV, herpes encephalitis.',
  'tech:south': 'Southern blot: gel, membrane, labeled DNA probe — sizes a sequence (CGG repeats in FMR1). SNoW DRoP.',
  'tech:north': 'Northern blot: RNA — mRNA level and size; splicing errors.',
  'tech:west': 'Western blot: protein, found with a labeled antibody — confirms what ELISA screens.',
  'tech:elisa': 'ELISA: antigen (direct) or antibody (indirect) detected with an enzyme-linked antibody — sensitive, less specific '
                'than Western; HIV screening.',
  'tech:flow': 'Flow cytometry: fluorescent antibodies, cells read one at a time — leukemia immunophenotype, PNH, fetal red cells '
               'in maternal blood, CD4 count.',
  'tech:karyo': 'Karyotype: colchicine disrupts the spindle and arrests cultured cells in mitosis; stained chromosomes are '
                'ordered — trisomies, sex-chromosome disorders.',
  'tech:fish': 'FISH: a fluorescent probe lights one locus — in a microdeletion one copy fluoresces and the other does not; also '
               'translocations, duplications.',
  'tech:crispr': 'CRISPR/Cas9: a guide RNA takes Cas9 to the target and it cuts; NHEJ knocks a gene out, donor DNA with HDR '
                 'knocks a sequence in. (Cloning makes insulin, growth hormone in bacteria.)',
}

dyn = dict(
  kinds=dict(dntp=['mov', '--dk9'], mol=['mov', '--dk5'], probe=['mov', '--bad'], cell=['mov', '--dk4']),
  groups=[['mov', 'dNTPs · molecules · probe · cells']],
  switches=[dict(id='tech', label='Technique', type='one', options=[
              ['pcr', 'PCR', 'pcr'], ['south', 'Southern blot', 'blots'], ['north', 'Northern blot', 'blots'], ['west', 'Western blot', 'blots'],
              ['elisa', 'ELISA', 'elisaflow'], ['flow', 'Flow cytometry', 'elisaflow'], ['karyo', 'Karyotype', 'cytogen'],
              ['fish', 'FISH', 'cytogen'], ['crispr', 'CRISPR/Cas9', 'cytogen']]),
            dict(id='ph', label='Step', type='steps', auto=3, options=[['s1', 'Step 1'], ['s2', 'Step 2'], ['s3', 'Step 3']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Marks ch 16')

MAP = dict(
  id='labsim', title='Lab Techniques in Motion', topic='bio', after='molbio',
  sub='Step through PCR, Southern, Northern and Western blots, ELISA, flow cytometry, karyotyping, FISH and CRISPR — one move at a time',
  w=3600, h=1900,
  fa='50, 51, 52, 53',
  src=['Marks ch 16 — Use of Recombinant DNA Techniques in Medicine'],
  lanes=[('lbNuc', 'Nucleic acids', 'tca'), ('lbProt', 'Proteins & cells', 'glycolysis')],
  nodes=[
    ('lb1', 'PCR', 330, 1700, 'lbNuc', 'denature · anneal · elongate', ['pcr'], 'hub'),
    ('lb2', 'Southern, Northern & Western', 760, 1700, 'lbNuc', 'SNoW DRoP', ['blots']),
    ('lb3', 'ELISA & flow cytometry', 1200, 1700, 'lbProt', 'screen · cell by cell', ['elisaflow']),
    ('lb4', 'Karyotype, FISH & CRISPR', 1640, 1700, 'lbNuc', 'chromosome · locus · cut', ['cytogen'])],
  panels=[
    (2500, PANY, 1000, 'SNoW DRoP (Marks ch 16)', [
      ('Southern', 'DNA'), ('Northern', 'RNA'), ('Western', 'protein')])],
  dyn=dyn)
