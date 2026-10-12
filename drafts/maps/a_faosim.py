# Fatty Acid Oxidation in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A liver/muscle cell: fatty acids arrive from the blood, become acyl-CoA, cross into the mitochondrion on the carnitine
# shuttle (CPT-I → translocase → CPT-II), run the β-oxidation spiral to acetyl-CoA and on to ketone bodies (exported) and
# the ETC; the peroxisome beside it takes VLCFAs (ABCD1), branched phytanic acid (α-oxidation) and makes plasmalogens. A
# `fast` toggle (on by default) drives the flow; a `one` switch breaks a step: carnitine deficiency, valproate, CPT-II,
# MCAD, Zellweger, Refsum, X-ALD. 7 readouts. Fed state: malonyl-CoA ⊣ CPT-I. Fact-checked m47 (FA, Marks, Robbins, Katzung).
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

O = lambda *k: [f'dx:{x}' for x in k]
F = lambda *k: [f'fast&dx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def node(x, y, lab, w=230, cls='dyn-cell'):
    add(f'<rect x="{x - w // 2}" y="{y - 30}" width="{w}" height="60" rx="26" class="{cls}"/>'); text(lab, x, y + 6, 'nf-l1', 'middle')
def pile(x, y, when):
    add(''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="11" style="fill:var(--dk3);opacity:.8"/>'
                for dx, dy in ((-40, 0), (-14, -6), (12, -2), (38, 2), (-26, -24), (0, -28), (26, -24))), when=when)
SHUTTLE = O('carn', 'cpt2')
SPIRAL = SHUTTLE + O('mcad')
PEROX = O('xald', 'zell')

text('Fatty acid oxidation — the carnitine shuttle, the spiral and the peroxisome', 180, 150, 'dyn-big')
text('turn fasting off to see the fed state: little fat is burned and nothing goes wrong', 180, 176, 'dyn-cap')

# ════════ blood and cell ════════
add('<rect x="300" y="220" width="2000" height="70" rx="30" style="fill:var(--nf-blood);fill-opacity:.1"/>')
text('blood — fatty acids from adipose in · ketone bodies out to brain and muscle', 1300, 262, 'nf-l2', 'middle')
add('<rect x="300" y="320" width="2000" height="1080" rx="50" class="dyn-soft"/>')
text('cytosol', 340, 360, 'nf-l1')
node(1000, 450, 'Acyl-CoA')
# peroxisome
add('<circle cx="620" cy="700" r="200" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>', unless=O('zell'))
add('<circle cx="620" cy="700" r="200" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 10"/>', when=O('zell'))
text('Peroxisome', 620, 560, 'nf-l1', 'middle')
text('VLCFA → acyl-CoA oxidase → H₂O₂', 620, 640, 'nf-l2', 'middle')
text('1st step makes no ATP — chain-shortens, exports', 620, 668, 'nf-l2', 'middle')
text('phytanic acid: α-oxidation first', 620, 760, 'nf-l2', 'middle')
text('plasmalogens → myelin', 620, 840, 'nf-l2', 'middle')
text('peroxisome never assembles (PEX)', 620, 940, 'nf-l1 dyn-tag', 'middle', when=O('zell'))
# mitochondrion
add('<rect x="1150" y="520" width="1100" height="840" rx="120" style="fill:var(--dk9);fill-opacity:.06;stroke:var(--ink-3);stroke-width:4"/>')
add('<rect x="1210" y="580" width="980" height="720" rx="100" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:4 6"/>')
text('Mitochondrion', 2200, 560, 'nf-l1', 'end')
add('<circle cx="1650" cy="860" r="140" style="fill:none;stroke:var(--dk1);stroke-width:6;opacity:.6"/>')
text('β-oxidation spiral', 1650, 856, 'nf-l1', 'middle'); text('acyl-CoA dehydrogenases', 1650, 880, 'nf-l2', 'middle')
node(1650, 1100, 'Acetyl-CoA'); node(2020, 1100, 'Ketone bodies', w=200); node(2020, 720, 'FADH₂ · NADH → ATP', w=260)
text('(liver, via HMG-CoA)', 2020, 1150, 'nf-l2', 'middle'); text('acetoacetate · β-hydroxybutyrate', 2020, 1176, 'nf-l2', 'middle')

# ════════ what goes wrong ════════
add(X(1400, 580), when=O('cpt2'))
text('malonyl-CoA ⊣ CPT-I (fed: insulin)', 1380, 440, 'nf-l1 dyn-tag', 'end', when=['!fast'])
add('<circle cx="1650" cy="860" r="170" class="dyn-hl" style="fill:none"/>', when=O('valp'))
text('valproate is β-oxidized here too (20–40%)', 1650, 1050, 'nf-l2', 'middle', when=O('valp'))
pile(1250, 400, O('carn')); pile(1400, 650, O('cpt2')); pile(1650, 760, O('mcad'))
add(X(1650, 1000), when=O('mcad'))
pile(620, 470, PEROX); pile(420, 760, O('refsum'))
TAG = dict(carn='no carnitine — long-chain fats can’t get in', valp='valproate — itself a branched fatty acid',
           cpt2='acylcarnitine can’t be turned back to acyl-CoA', mcad='spiral stalls at medium chain length',
           refsum='phytanic acid can’t lose its β-methyl', xald='VLCFAs can’t enter the peroxisome (ABCD1)',
           zell='no peroxisome: VLCFA ↑, plasmalogens ↓')
for k, t in TAG.items(): text(t, 1300, 1450, 'nf-l1 dyn-tag', 'middle', when=O(k))
WHO = dict(carn='hypoketotic hypoglycemia · dilated cardiomyopathy', valp='↑ ammonia (may respond to L-carnitine) · hepatotoxicity',
           cpt2='rhabdomyolysis after prolonged exercise or fasting', mcad='hypoglycemia WITHOUT ketones after a fast or illness',
           refsum='retinitis pigmentosa · anosmia · ataxia · ichthyosis', xald='adrenal insufficiency + demyelination in a boy',
           zell='floppy newborn · seizures · hepatomegaly')
for k, t in WHO.items(): text(t, 1300, 1480, 'nf-l2', 'middle', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def fl(d, n, stop=None, k='fa', length=300, low=None):
    f = dict(d=d, len=length, speed=90, r=8, base={k: n}, mods=[m(['!fast'], set={k: 1})])
    if low: f['mods'].append(m(low, set={k: 1}))
    if stop: f['mods'].append(m(stop, set={k: 0}))
    return f
flows = [
  fl('M700 290 C780 340 860 400 885 440', 4, length=220),
  fl('M1115 450 H1400 V600', 4, stop=O('carn')),
  fl('M1400 620 C1420 700 1480 780 1510 830', 4, stop=SHUTTLE, length=240),
  dict(d='M1790 860 A140 140 0 1 1 1789.9 859', len=880, speed=160, r=8, base=dict(fa=4),
       mods=[m(['!fast'], set=dict(fa=1)), m(O('mcad'), set=dict(fa=1)), m(SHUTTLE, set=dict(fa=0))]),
  fl('M1650 1000 V1070', 3, stop=SPIRAL, k='ac', length=80),
  fl('M1765 1100 H1920', 3, stop=SPIRAL, k='ac', length=160),
  fl('M2120 1100 H2280 V260 H1900', 3, stop=SPIRAL, k='ket', length=1300),
  fl('M1760 780 C1820 740 1860 720 1890 720', 3, stop=SPIRAL, k='ac', length=160),
  fl('M560 290 C560 400 600 460 620 500', 3, stop=PEROX, k='vl', length=220),
  fl('M800 640 C900 600 1100 560 1400 520', 2, stop=PEROX, k='vl', length=820),
  fl('M330 760 H500', 2, stop=O('refsum', 'zell'), k='vl', length=170),
]
sites = [
  dict(x=1400, y=520, n=[0, -1], w=10, t='co', l='CPT-I', s='+ carnitine', c='carndef', ions=[], stop=O('carn'), low=['!fast'],
       sfx=dict(stop=' — idle, no carnitine', low=' — inhibited (malonyl-CoA)'),
       la='end', lx=1380, ly=496),
  dict(x=1400, y=580, n=[0, 1], w=10, t='co', l='CPT-II', s='matrix side', c='cpt2', ions=[], block=O('cpt2'),
       la='start', lx=1440, ly=620),
  dict(x=1790, y=860, n=[1, 0], w=10, t='rec', l='MCAD', s='medium chain', c='mcad', ions=[], block=O('mcad'), lx=1830, ly=860, la='start'),
  dict(x=620, y=500, n=[0, -1], w=10, t='co', l='ABCD1', s='VLCFA in', c='xald', ions=[], block=O('xald', 'zell'), lx=700, ly=470, la='start'),
  dict(x=420, y=700, n=[0, -1], w=10, t='rec', l='', aria='Refsum — α-oxidation', c='refsum', ions=[], block=O('refsum', 'zell')),
]

readouts = [
  dict(l='Blood glucose (fasting)', mods=[dict(when=F('carn', 'mcad'), d=-1)]),
  dict(l='Ketones (fasting)', mods=[dict(when=F('carn', 'mcad'), d=-1), dict(when=['fast&!dx:*'], d=1)]),
  dict(l='Free carnitine', mods=[dict(when=O('carn', 'cpt2', 'mcad'), d=-1)]),
  dict(l='Acylcarnitines', mods=[dict(when=O('cpt2', 'mcad'), d=1)]),
  dict(l='CK (attacks)', mods=[dict(when=O('cpt2'), d=1)]),
  dict(l='VLCFA', mods=[dict(when=PEROX, d=1), dict(when=O('refsum'), d=0)]),
  dict(l='Phytanic acid', mods=[dict(when=O('refsum'), d=1)]),
]

notes = {
  '': 'Fasting: fatty acids come from adipose, become acyl-CoA and ride the carnitine shuttle (CPT-I → CPT-II) into the matrix, where '
      'the β-oxidation spiral cuts them to acetyl-CoA — for the ETC and, in the liver, for ketone bodies. The peroxisome pre-processes '
      'what mitochondria can’t: VLCFAs, branched phytanic acid (α-oxidation), and it makes plasmalogens.',
  '!fast': 'Fed: insulin turns on acetyl-CoA carboxylase, and its product malonyl-CoA inhibits CPT-I, so little fat enters the '
           'mitochondrion — these disorders stay silent until a fast or an illness.',
  'dx:carn': 'Primary carnitine deficiency: no cellular uptake of carnitine, so CPT-I has nothing to load and long-chain fatty acids pile up in '
             'the cytosol — β-oxidation and hepatic ketogenesis fail with fasting: weakness, hypotonia, hypoketotic hypoglycemia, dilated '
             'cardiomyopathy. Treat: avoid fasting, oral carnitine.',
  'dx:valp': 'Valproate is itself a short branched fatty acid — 20–40% of a dose goes through mitochondrial β-oxidation (Katzung). It can '
             'raise ammonia by interfering with urea formation, and that hyperammonemia may respond to L-carnitine (Kaplan & Sadock); also '
             'hepatotoxicity.',
  'dx:cpt2': 'CPT-II deficiency: acylcarnitine can’t be turned back into acyl-CoA in the matrix. Muscle that relies on fat during prolonged '
             'exercise or fasting breaks down — myalgia, myoglobinuria; ↑ CK and long-chain acylcarnitines, ↓ free carnitine. The most '
             'common lipid cause of episodic muscle damage (Robbins).',
  'dx:mcad': 'MCAD deficiency (one of the most common inborn errors): the spiral stalls at medium chain length, so no acetyl-CoA for '
             'ketogenesis — hypoglycemia WITHOUT ketones after a fast or illness; can present as sudden infant death. ↑ acylcarnitines, '
             'dicarboxylic acids.',
  'dx:refsum': 'Refsum disease: dietary phytanic acid has a β-methyl that blocks β-oxidation, so α-oxidation must go first; one enzyme of it '
               '(phytanoyl-CoA hydroxylase) is missing and phytanic acid builds up — retinitis pigmentosa, anosmia, ataxia, ichthyosis. '
               'VLCFA oxidation is intact.',
  'dx:xald': 'X-linked adrenoleukodystrophy: ABCD1 can’t carry VLCFAs into the peroxisome; they accumulate in the adrenal glands and CNS '
             'white matter — a young male with behavioral change and adrenal insufficiency, then progressive demyelination. ↑ VLCFA.',
  'dx:zell': 'Zellweger syndrome: PEX genes — the peroxisome never assembles, so every peroxisomal job fails: ↑ VLCFA and ↓ plasmalogens '
             '(white-matter lipid) — floppy newborn, seizures, hepatomegaly, early death.',
}

dyn = dict(
  kinds=dict(fa=['fat', '--dk1'], vl=['fat', '--dk6'], ac=['prod', '--dk2'], ket=['prod', '--dk5']),
  groups=[['fat', 'Fatty acids'], ['prod', 'Acetyl-CoA · ketones · ATP']],
  switches=[dict(id='fast', label='State', type='toggle', on='Fasting', off='Fed', def_=True),
            dict(id='dx', label='What goes wrong', type='one', options=[
              ['carn', 'Carnitine deficiency', 'carndef'], ['valp', 'Valproate', 'valproate'], ['cpt2', 'CPT-II deficiency', 'cpt2'],
              ['mcad', 'MCAD deficiency', 'mcad'], ['refsum', 'Refsum disease', 'refsum'], ['xald', 'X-linked ALD', 'xald'],
              ['zell', 'Zellweger syndrome', 'zellweger']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 46, 71, 87 · Marks ch 30 · Robbins ch 27–28 · Katzung ch 24 · Bootcamp Biochemistry')
dyn['switches'][0]['def'] = dyn['switches'][0].pop('def_')

MAP = dict(
  id='faosim', title='Fatty Acid Oxidation in Motion', topic='bio', after='lipid',
  sub='Fast, and watch fat cross the carnitine shuttle, spin down the β-oxidation spiral and leave as ketones, with the peroxisome '
      'handling VLCFAs and phytanic acid — then break carnitine, CPT-II, MCAD, the peroxisome (Zellweger), Refsum or ABCD1',
  w=3600, h=1900,
  fa='46, 71, 76, 87, 353',
  src=['Marks ch 30 — Oxidation of Fatty Acids and Ketone Bodies', 'Robbins ch 27 — Peripheral nerves and skeletal muscles',
       'Pawlina ch 2 — Cell Cytoplasm', 'Marks ch 46 — Metabolism of the Nervous System', 'Marks ch 44 — Liver Metabolism',
       'Robbins ch 10 — Diseases of infancy and childhood',
       'Robbins ch 28 — The central nervous system', 'Katzung ch 24 — Antiseizure Medications', 'Kaplan & Sadock ch 21 — Psychopharmacology'],
  lanes=[('foMito', 'Mitochondrial β-oxidation', 'glycolysis'), ('foPerox', 'Peroxisome', 'tca')],
  nodes=[
    ('fo1', 'Fatty acid oxidation disorders', 330, 1620, 'foMito', 'hypoketotic hypoglycemia', ['faoxpattern'], 'hub'),
    ('fo2', 'Carnitine deficiency', 760, 1620, 'foMito', 'shuttle fails', ['carndef', 'valproate']),
    ('fo3', 'CPT-II deficiency', 1200, 1620, 'foMito', 'rhabdo after exercise', ['cpt2']),
    ('fo4', 'MCAD deficiency', 1640, 1620, 'foMito', 'no ketones', ['mcad']),
    ('fo5', 'Peroxisome vs mitochondrion', 330, 1760, 'foPerox', 'H₂O₂ vs FADH₂', ['peroxreg']),
    ('fo6', 'Zellweger syndrome', 760, 1760, 'foPerox', 'no peroxisome', ['zellweger']),
    ('fo7', 'Refsum disease', 1200, 1760, 'foPerox', 'phytanic acid', ['refsum']),
    ('fo8', 'X-linked ALD', 1640, 1760, 'foPerox', 'adrenal + white matter', ['xald'])],
  panels=[
    (2500, PANY, 1000, 'Which test? (First Aid pp. 46, 87 · Marks ch 30)', [
      ('Hypoglycemia + no ketones', 'β-oxidation or carnitine defect'),
      ('↑ VLCFA', 'X-ALD, Zellweger'),
      ('↑ VLCFA + ↓ plasmalogens', 'Zellweger'),
      ('↑ Phytanic acid, VLCFA normal', 'Refsum'),
      ('↑ CK after prolonged exercise', 'CPT-II')])],
  dyn=dyn)
