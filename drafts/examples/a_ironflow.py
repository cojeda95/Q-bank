# m40 — Iron in Motion (dynamic map, kit data)
# The duodenal enterocyte (duodenal cytochrome b + vitamin C reduce Fe³⁺, DMT1 carries Fe²⁺ in, heme taken up intact),
# ferroportin + hephaestin out to the plasma, transferrin to the liver (ferritin stores) and to the marrow's transferrin
# receptor, heme synthesis in the erythroblast's mitochondrion, red cells recycled by splenic macrophages, and hepcidin from
# the liver shutting ferroportin in gut and macrophage. One `one` switch picks a disorder; readouts are First Aid's iron
# studies (serum iron, TIBC, ferritin, % saturation) plus free erythrocyte protoporphyrin and the reticulocyte count.
# Sources: First Aid 2025 pp. 67, 209, 381, 402, 421, 423–425, 427, 430–431 · Robbins ch 14, 18 · Katzung ch 33, 57 ·
# Marks ch 42 · Bootcamp Hematology & Oncology (Microcytic Anemia).
import sys, math
sys.path.insert(0, '/Users/Alonso/Developer/atlas-review/batches/m18')
from common import card, full

RB14, RB18, KZ33, KZ57, MK42 = full('Robbins', 14), full('Robbins', 18), full('Katzung', 33), full('Katzung', 57), full('Marks', 42)
BC = 'Bootcamp.com Hematology & Oncology — Microcytic Anemia'

card('ironcycle', 'Iron absorption, transport & recycling', 'reg', 'ifGut',
 'Duodenal cytochrome b · DMT1 · ferroportin · transferrin · ferritin', 1,
 'There is <b>no regulated way to excrete iron</b> (losses are ~1 mg/day), so balance is set at absorption. In the duodenum, dietary '
 'Fe³⁺ is reduced to Fe²⁺ by a ferrireductase (<b>duodenal cytochrome b</b>; vitamin C helps) and carried in by <b>DMT1</b>; heme iron '
 'from meat is absorbed intact and its iron freed inside the cell. <b>Ferroportin</b> exports iron across the basolateral membrane while '
 '<b>hephaestin</b> (and ceruloplasmin) re-oxidize it to Fe³⁺ for <b>transferrin</b>, which delivers it to <b>transferrin receptors</b> on '
 'erythroid precursors. Stores sit in <b>ferritin</b> (liver, macrophages); <b>hepcidin</b> from the liver degrades ferroportin.',
 ['Absorbed mainly in the <b>duodenum</b> and proximal jejunum — “Iron fist, Bro” (iron duodenum, folate jejunum, B12 ileum)',
  'Heme iron (meat) is well absorbed; plant iron is held back by phytates, oxalates and tannates (tea); calcium also lowers uptake',
  'Erythroid cells endocytose the transferrin–receptor complex; Fe²⁺ leaves the endosome through DMT1 and the receptor recycles',
  'Macrophages in spleen, liver and marrow take back the iron of red cells after ~120 days — the main supply for new hemoglobin',
  'Hepcidin falls with low iron, hypoxia or brisk erythropoiesis (erythroferrone) and rises with iron loading and inflammation (IL-6)'],
 ['Transferrin is normally about one-third saturated; TIBC ≈ 300 μg/dL',
  'Serum ferritin is in equilibrium with storage ferritin — it estimates body iron stores'],
 ['Vitamin C reduces Fe³⁺ to the absorbable Fe²⁺'],
 [RB14, KZ33, MK42, BC],
 ['—'],
 ['iron absorption', 'ferroportin', 'divalent metal transporter', 'dmt1', 'transferrin receptor', 'hephaestin',
  'duodenal cytochrome b', '=transferrin'],
 fa='67, 209, 381, 423')

card('ironstudies', 'Iron studies — iron, TIBC, ferritin & saturation', 'reg', 'ifDz',
 'Four numbers that sort the microcytic anemias', 1,
 '<b>Serum iron</b> is the iron riding on transferrin; <b>TIBC</b> indirectly measures transferrin (all its binding sites); '
 '<b>ferritin</b>, the main storage protein, appears in serum in proportion to the stores; <b>% transferrin saturation</b> = serum iron ÷ '
 'TIBC, normally about one-third. Ferritin first: low means empty stores; high with a low serum iron means iron is being withheld '
 '(inflammation, via hepcidin).',
 ['<b>Iron deficiency</b>: iron ↓, TIBC ↑, ferritin ↓, saturation ↓↓ (below 15%)',
  '<b>Anemia of chronic disease</b>: iron ↓, TIBC ↓, ferritin ↑, saturation normal or ↓',
  '<b>Hemochromatosis</b>: iron ↑, TIBC ↓, ferritin ↑, saturation ↑↑',
  '<b>Pregnancy / OCP use</b>: TIBC ↑, saturation ↓, iron and ferritin normal',
  '<b>Sideroblastic anemia</b>: iron ↑, TIBC normal or ↓, ferritin ↑ · <b>thalassemia trait</b>: normal iron studies'],
 ['Free erythrocyte protoporphyrin ↑ in iron deficiency and lead poisoning — ferrochelatase lacks iron, or is blocked',
  'Ferritin is a positive and transferrin a negative acute-phase reactant — inflammation raises ferritin and lowers TIBC',
  'Mentzer index (MCV ÷ RBC count) < 13 suggests thalassemia trait, > 13 iron deficiency'],
 ['Low ferritin = iron deficiency', 'Low iron, low TIBC, high ferritin = chronic disease'],
 [RB14, KZ33, BC],
 ['—'],
 ['iron studies', 'total iron-binding capacity', 'tibc', 'transferrin saturation', 'serum ferritin',
  'free erythrocyte protoporphyrin', '=serum iron'],
 fa='209, 423–425')

F = lambda *k: ['fe:' + x for x in k]


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
def rrect(x0, y0, x1, y1, r):
    return (f'M{x0 + r} {y0} H{x1 - r} Q{x1} {y0} {x1} {y0 + r} V{y1 - r} Q{x1} {y1} {x1 - r} {y1} '
            f'H{x0 + r} Q{x0} {y1} {x0} {y1 - r} V{y0 + r} Q{x0} {y0} {x0 + r} {y0} Z')
TAG = 'nf-l2 dyn-tag'
def store(cx, cy, n, col='--dk5'):
    """a ferritin store: a cluster of n iron granules"""
    pts = [(0, 0), (22, -6), (-20, 8), (8, 20), (-6, -22), (30, 16), (-30, -12), (18, -26), (-26, 26), (40, -4), (-40, 4),
           (4, 38), (-14, -40), (44, 28), (-44, -28), (30, -36)][:n]
    return ''.join(f'<circle cx="{cx + x}" cy="{cy + y}" r="9" style="fill:var({col});opacity:.75"/>' for x, y in pts)

# ════════ the drawing ════════
ENT, LIV, MAR, MAC = (330, 240, 790, 1000), (1300, 240, 1900, 700), (1300, 860, 2300, 1450), (330, 1240, 790, 1860)
PX = 1060   # the plasma
# lumen
add('<rect class="dyn-soft" x="150" y="240" width="170" height="760" rx="24"/>')
text('Duodenal lumen', 150, 222, 'dyn-big')
text('non-heme Fe³⁺', 165, 300, 'nf-l2')
text('heme (meat)', 165, 640, 'nf-l2')
text('vitamin C helps;', 165, 940, 'dyn-cap')
text('tea, phytates hinder', 165, 958, 'dyn-cap')
text('oral iron tablets', 165, 318, TAG, when=F('tx'))
# cells
for (x0, y0, x1, y1), r in ((ENT, 40), (LIV, 40), (MAR, 40), (MAC, 60)):
    add(f'<path d="{rrect(x0, y0, x1, y1, r)}" class="dyn-cell"/>')
    shapes.append(dict(membrane=rrect(x0, y0, x1, y1, r), w=18))
text('Duodenal enterocyte', 420, 222, 'dyn-big')
text('hephaestin: Fe²⁺ → Fe³⁺', 560, 670, 'dyn-cap')
text('heme oxygenase frees Fe²⁺', 525, 795, 'nf-l2')
add(store(560, 905, 4))
text('mucosal ferritin — shed with the cell', 380, 968, 'nf-l2')
add(store(560, 905, 9), when=F('acd'))
text('iron trapped here, lost as cells slough', 380, 985, TAG, when=F('acd'))
# plasma
add(f'<rect x="{PX - 30}" y="250" width="60" height="1710" rx="30" style="fill:var(--dk2);opacity:.13"/>'
    f'<rect x="{PX - 30}" y="250" width="60" height="1710" rx="30" style="fill:none;stroke:var(--dk2);stroke-width:2;opacity:.5"/>')
text('Plasma', PX, 222, 'dyn-big', 'middle')
text('transferrin carries Fe³⁺', 860, 1170, 'nf-l2')
text('normally about ⅓ full', 860, 1186, 'dyn-cap')
# liver
text('Hepatocyte (liver)', 1560, 278, 'dyn-big')
add(store(1720, 410, 6))
text('ferritin store', 1690, 480, 'nf-l2')
add(store(1720, 410, 16), when=F('hh'))
text('hemosiderin: liver, pancreas, heart, skin', 1500, 640, TAG, when=F('hh'))
add(f'<g class="dyn-dim">{store(1720, 410, 6)}</g>', when=F('ida'))
text('stores empty', 1690, 498, TAG, when=F('ida'))
text('HFE + iron stores set hepcidin', 1500, 610, 'dyn-cap')
text('HFE mutant — too little hepcidin', 1500, 660, TAG, when=F('hh'))
text('IL-6 — infection, autoimmunity, cancer, CKD', 1930, 450, TAG, when=F('acd'))
# marrow
text('Erythroid precursor (bone marrow)', 1500, 900, 'dyn-big')
MITO = 'M1490 1110 A330 160 0 1 0 2150 1110 A330 160 0 1 0 1490 1110 Z'
add(f'<path d="{MITO}" style="fill:var(--dk5);opacity:.07"/>')
shapes.append(dict(membrane=MITO, w=12))
text('Mitochondrion', 1760, 984, 'dyn-cap')
text('heme + globin → hemoglobin', 2000, 1398, 'nf-l2')
text('globin chains short — iron use normal', 2000, 1418, TAG, when=F('thal'))
add('<circle cx="1400" cy="1330" r="52" style="fill:var(--dk4);opacity:.12;stroke:var(--dk4);stroke-width:2"/>')
text('nucleus', 1400, 1335, 'nf-l2', 'middle')
RING = ''.join(f'<circle cx="{1400 + 70 * math.cos(a / 9 * 6.283):.0f}" cy="{1330 + 70 * math.sin(a / 9 * 6.283):.0f}" r="8" style="fill:var(--dk3)"/>' for a in range(9))
add(RING, when=F('sidero', 'lead'))
text('ringed sideroblast', 1335, 1426, TAG, when=F('sidero', 'lead'))
text('iron piles up in mitochondria', 1640, 1235, TAG, when=F('sidero'))
text('protoporphyrin piles up (FEP ↑)', 1640, 1235, TAG, when=F('ida', 'lead'))
# macrophage
text('Splenic macrophage', 350, 1280, 'dyn-big')
add(store(560, 1500, 6))
text('ferritin store', 420, 1580, 'nf-l2')
add(store(560, 1500, 16), when=F('acd'))
add(f'<g class="dyn-dim">{store(560, 1500, 6)}</g>', when=F('ida'))
text('iron locked in — “starved amid plenty”', 360, 1620, TAG, when=F('acd'))
text('no stainable iron', 420, 1598, TAG, when=F('ida'))
text('heme oxygenase: heme → Fe²⁺', 360, 1700, 'nf-l2')
text('+ biliverdin → bilirubin', 360, 1716, 'dyn-cap')
text('red cells circulate ~120 days', 1300, 1982, 'dyn-cap')
text('fewer, smaller, paler red cells', 1300, 1982 - 18, TAG, when=F('ida', 'sidero', 'lead'))

# ════════ transferrin gauge — cups = TIBC, filled = serum iron ════════
GX, GY = 1300, 1560
text('Transferrin in a drop of plasma', GX, GY - 22, 'dyn-big')
def cups(total, full, dim=False):
    s = ''
    for i in range(total):
        x = GX + i * 60
        s += f'<rect x="{x}" y="{GY}" width="46" height="56" rx="10" style="fill:var(--surface);stroke:var(--dk5);stroke-width:2.5"/>'
        if i < full: s += f'<rect x="{x + 5}" y="{GY + 5}" width="36" height="46" rx="7" style="fill:var(--dk5);opacity:.85"/>'
    return f'<g class="dyn-dim">{s}</g>' if dim else s
GAUGE = dict(ida=(13, 1, 'iron deficiency: more transferrin, little iron — saturation below 15%'),
             acd=(6, 1, 'chronic disease: less transferrin and less iron'),
             hh=(6, 5, 'hemochromatosis: few empty sites — saturation very high'),
             sidero=(7, 5, 'sideroblastic: iron high, TIBC normal or low — saturation high'),
             preg=(13, 3, 'pregnancy / OCP: more transferrin, same iron — saturation falls'))
for k, (t, f, cap) in GAUGE.items():
    add(cups(t, f), when=F(k)); text(cap, GX, GY + 100, 'dyn-cap', when=F(k))
add(cups(9, 3), unless=F(*GAUGE, 'lead', 'tx'))
text('normal: about one-third of the sites hold iron', GX, GY + 100, 'dyn-cap', unless=F(*GAUGE, 'thal', 'lead', 'tx'))
text('thalassemia trait: normal — globin, not iron, is short', GX, GY + 100, 'dyn-cap', when=F('thal'))
add(cups(9, 3, True), when=F('lead', 'tx'))
text('lead: First Aid gives FEP ↑ but no iron-study pattern', GX, GY + 100, 'dyn-cap', when=F('lead'))
text('on oral iron: reticulocytes rise first; stores refill over 3–6 months', GX, GY + 100, 'dyn-cap', when=F('tx'))
text('each cup = binding capacity (TIBC) · filled = serum iron · filled ÷ all = % saturation', GX, GY + 80, 'nf-l2')

# ════════ particles ════════
kinds = dict(fe3=['fe3', '--dk5'], fe2=['fe2', '--dk3'], heme=['heme', '--dk2'], ppx=['heme', '--dk7'], hep=['hep', '--dk4'],
             il6=['hep', '--dk11'], rbc=['rbc', '--dk2'])
groups = [['fe3', 'Fe³⁺ (on transferrin)'], ['fe2', 'Fe²⁺'], ['heme', 'Heme · protoporphyrin'], ['hep', 'Hepcidin · IL-6'], ['rbc', 'Red cells']]
def m(when, **kw): return dict(when=when, **kw)
UP = F('ida', 'hh', 'preg', 'tx')
flows = [
  dict(d='M240 255 V360 H296', len=161, speed=90, base=dict(fe3=3), mods=[m(F('tx'), set=dict(fe3=6))]),
  dict(d='M190 255 V760 H296', len=611, speed=110, base=dict(heme=2)),
  dict(d='M375 556 C520 600 640 600 768 600', len=405, base=dict(fe2=3), mods=[m(UP, set=dict(fe2=5)), m(F('acd'), set=dict(fe2=1))]),
  dict(d='M375 790 H515', len=140, speed=90, base=dict(heme=1)),
  dict(d='M700 790 C760 775 768 700 768 616', len=200, speed=90, base=dict(fe2=1)),
  dict(d=f'M812 600 H{PX} V1000 H1288', len=876, base=dict(fe3=3),
       mods=[m(F('ida', 'acd'), set=dict(fe3=1)), m(F('hh'), set=dict(fe3=6)), m(F('tx'), set=dict(fe3=4))]),
  dict(d=f'M812 1450 H{PX} V1020 H1288', len=906, base=dict(fe3=4),
       mods=[m(F('acd'), set=dict(fe3=1)), m(F('ida'), set=dict(fe3=1)), m(F('hh'), set=dict(fe3=5))]),
  dict(d=f'M{PX} 600 V380 H1288', len=448, speed=100, base=dict(fe3=1), mods=[m(F('hh'), set=dict(fe3=4)), m(F('ida'), set=dict(fe3=0))]),
  dict(d='M1262 560 H826 V588', len=464, speed=110, r=7, base=dict(hep=1), mods=[m(F('acd'), set=dict(hep=4)), m(F('hh', 'ida'), set=dict(hep=0))]),
  dict(d='M1262 576 H1140 V1426 H826 V1438', len=1298, speed=150, r=7, base=dict(hep=2),
       mods=[m(F('acd'), set=dict(hep=6)), m(F('hh', 'ida'), set=dict(hep=0))]),
  dict(d='M2280 470 H1915', len=365, speed=100, when=F('acd'), base=dict(il6=4)),
  dict(d='M1360 1010 H1700 Q2000 1010 2040 1050', len=690, base=dict(fe2=3),
       mods=[m(F('ida', 'acd'), set=dict(fe2=1)), m(F('sidero'), set=dict(fe2=5))]),
  dict(d='M1560 1180 Q1560 1330 1700 1330 H1960 Q2090 1330 2062 1080', len=740, speed=110, r=6, base=dict(ppx=3),
       mods=[m(F('sidero'), set=dict(ppx=0)), m(F('ida', 'lead'), set=dict(ppx=6))]),
  dict(d='M2080 1070 Q2230 1080 2240 1200 V1440', len=420, speed=110, base=dict(heme=2),
       mods=[m(F('ida', 'acd', 'sidero', 'lead'), set=dict(heme=1))]),
  dict(d='M2240 1440 V2000 H560 V1902', len=2338, speed=220, r=10, base=dict(rbc=7)),
  dict(d='M560 1770 V1560 Q560 1450 768 1450', len=470, speed=110, base=dict(fe2=2), mods=[m(F('ida'), set=dict(fe2=1))]),
]
COL = dict(fe3=('--dk5', 'ifBlood'), fe2=('--dk3', 'ifGut'), heme=('--dk2', 'ifBlood'), ppx=('--dk7', 'ifBlood'),
           hep=('--dk4', 'ifStore'), il6=('--dk11', 'ifStore'), rbc=('--dk2', 'ifBlood'))
for f in flows:
    k = next(iter(f['base'])); col, lane = COL[k]
    dash = ';stroke-dasharray:8 6' if k in ('hep', 'il6') else ''
    tr = f'<path d="{f["d"]}" class="dyn-line" style="stroke:var({col});stroke-width:3;opacity:.4{dash}" marker-end="url(#ah-{lane})"/>'
    shapes.append(dict(svg=tr, when=f["when"]) if f.get("when") else tr)

# ════════ sites ════════
sites = [
  dict(x=330, y=360, n=[1, 0], w=18, t='ex', l='Duodenal cytochrome b', s='Fe³⁺ → Fe²⁺ (a ferrireductase)', ions=[['fe2', 'out', 1]],
       cross=True, reach=30, c='ironcycle', boost=F('ida', 'hh', 'tx')),
  dict(x=330, y=520, n=[1, 0], w=18, t='co', l='DMT1', s='carries Fe²⁺ in', ions=[['fe2', 'out', 2]], cross=True, reach=30,
       c='ironcycle', boost=UP),
  dict(x=330, y=760, n=[1, 0], w=18, t='co', l='Heme carrier', s='meat heme enters intact', ions=[['heme', 'out', 1]], cross=True, reach=30,
       c='ironcycle'),
  dict(x=790, y=600, n=[1, 0], w=18, t='ch', l='Ferroportin', s='exports iron', ions=[['fe2', 'out', 1]], cross=True, reach=30,
       c='hemochrom', low=F('acd'), boost=UP, sfx=dict(low=' — fewer', boost=' — more')),
  dict(x=1300, y=380, n=[1, 0], w=18, t='rec', l='Transferrin receptor', s='brings iron in to be stored', ions=[['fe3', 'out', 1]],
       cross=True, reach=30, c='ironcycle', boost=F('hh'), low=F('ida'), sfx=dict(boost=' — loading')),
  dict(x=1300, y=560, n=[1, 0], w=18, t='ch', l='Hepcidin', s='degrades ferroportin in gut and macrophages', ions=[['hep', 'in', 1]],
       cross=True, reach=30, c='hemochrom', boost=F('acd'), low=F('hh', 'ida'), sfx=dict(boost=' — raised (IL-6)', low=' — low')),
  dict(x=1300, y=1010, n=[1, 0], w=18, t='rec', l='Transferrin receptor', s='endocytosed · DMT1 frees Fe²⁺', ions=[['fe3', 'out', 2]],
       cross=True, reach=30, c='ironcycle', low=F('ida', 'acd'), sfx=dict(low=' — little iron arrives')),
  dict(x=1540, y=1160, n=[1, 0], w=4, t='pump', l='ALA synthase', s='succinyl-CoA + glycine · B6 · rate-limiting', ions=[],
       c='sidero', block=F('sidero'), sfx=dict(block=' — defective')),
  dict(x=1800, y=1330, n=[0, 1], w=4, t='pump', l='ALA dehydratase', s='ALA → porphobilinogen → … → protoporphyrin', ions=[],
       c='lead', block=F('lead')),
  dict(x=2060, y=1060, n=[-1, 0], w=4, t='pump', l='Ferrochelatase', s='Fe²⁺ + protoporphyrin → heme', ions=[], c='ida',
       unless=F('sidero'), block=F('lead'), stop=F('ida'), sfx=dict(stop=' — no iron to insert')),
  dict(x=2060, y=1060, n=[-1, 0], w=4, t='pump', l='Ferrochelatase', s='Fe²⁺ + protoporphyrin → heme', ions=[], c='ida',
       when=F('sidero'), stop=F('sidero'), sfx=dict(stop=' — too little protoporphyrin')),
  dict(x=790, y=1450, n=[1, 0], w=18, t='ch', l='Ferroportin', s='releases recycled iron', ions=[['fe2', 'out', 2]], cross=True,
       reach=30, c='hemochrom', low=F('acd'), boost=F('hh'), sfx=dict(low=' — fewer', boost=' — more')),
  dict(x=560, y=1860, n=[0, -1], w=18, t='rec', l='Phagocytosis', s='old red cells taken in', ions=[['rbc', 'out', 1]], cross=True,
       reach=30, c='macrophage'),
]

# ════════ readouts — First Aid p. 423 table; pp. 424–425, 427; Bootcamp; Robbins ch 14; Katzung ch 33 ════════
R = lambda l, *mm: dict(l=l, mods=[dict(when=F(*w) if isinstance(w, tuple) else F(w), d=d) for w, d in mm])
readouts = [
  R('Serum iron', (('ida', 'acd'), -1), (('hh', 'sidero'), 1), (('thal', 'preg'), 0)),
  R('TIBC', (('ida', 'preg'), 1), (('acd', 'hh', 'sidero'), -1), ('thal', 0)),
  R('Ferritin', ('ida', -1), (('acd', 'hh', 'sidero'), 1), (('thal', 'preg'), 0)),
  R('% saturation', (('ida', 'acd', 'preg'), -1), (('hh', 'sidero'), 1), ('thal', 0)),
  R('FEP', (('ida', 'lead'), 1)),
  R('Reticulocytes', (('ida', 'acd'), -1), ('tx', 1)),
]

notes = {
  '': 'Dietary Fe³⁺ is reduced to Fe²⁺ (duodenal cytochrome b, helped by vitamin C) and carried in by DMT1; heme iron enters intact. '
      'Ferroportin exports it, hephaestin re-oxidizes it, and transferrin (about one-third full) takes it to the liver’s stores and to the '
      'marrow, where ferrochelatase puts Fe²⁺ into protoporphyrin. Macrophages recycle old red cells. Hepcidin shuts ferroportin. Pick a disorder.',
  'fe:ida': 'Iron deficiency — chronic blood loss (GI bleeding, heavy menses), poor intake or absorption, or ↑ demand (pregnancy). Stores '
            'empty first (ferritin ↓), hepcidin falls so the gut absorbs harder, transferrin rises (TIBC ↑) and saturation drops below 15%. '
            'Ferrochelatase has no iron, so protoporphyrin builds up (FEP ↑): microcytic, hypochromic cells. Older adult → look for GI bleeding.',
  'fe:acd': 'Anemia of chronic disease — IL-6 from infection, autoimmunity (RA, SLE), cancer or CKD raises hepcidin, which degrades '
            'ferroportin in enterocytes and macrophages: less iron absorbed, more locked in stores. Serum iron ↓ and TIBC ↓, ferritin ↑ '
            '(also an acute-phase reactant), saturation normal or ↓. Normocytic, can turn microcytic. Treat the cause; EPO in CKD.',
  'fe:hh': 'Hereditary hemochromatosis — HFE mutations (chromosome 6, autosomal recessive) leave hepcidin too low, so ferroportin stays '
           'open and the gut over-absorbs: iron ↑, ferritin ↑, saturation ↑↑, TIBC ↓. Iron loads liver, pancreas, skin, heart, joints — '
           'cirrhosis, diabetes, bronze skin, HCC. Chronic transfusion (β-thalassemia major) overloads iron too. Phlebotomy; chelators.',
  'fe:sidero': 'Sideroblastic anemia — heme synthesis fails (X-linked ALA synthase defect; or alcohol, B6 deficiency from isoniazid, '
               'copper deficiency, myelodysplasia, lead), so iron brought to the mitochondria has nowhere to go: iron-laden mitochondria '
               'ring the nucleus (ringed sideroblasts, Prussian blue). Iron ↑, ferritin ↑, TIBC normal or ↓. Treat with pyridoxine (B6).',
  'fe:lead': 'Lead poisoning — lead blocks ALA dehydratase and ferrochelatase: ALA and protoporphyrin pile up (FEP ↑), less heme is made '
             '→ microcytic anemia, basophilic stippling, ringed sideroblasts. Burton lines, encephalopathy, abdominal colic, wrist and foot '
             'drop. Old paint (homes before 1978), batteries, ammunition. Chelate with succimer, EDTA or dimercaprol.',
  'fe:thal': 'Thalassemia trait (α or β minor) — globin chains are short, not iron: mild microcytic anemia with target cells (HbA2 ↑ in β '
             'minor), but iron, TIBC and ferritin are normal and iron pills don’t help. RBC count is often ↑; a Mentzer index (MCV ÷ RBC '
             'count) below 13 favors trait over iron deficiency. Matters for genetic counseling.',
  'fe:preg': 'Pregnancy or OCP use — transferrin rises (TIBC ↑) while serum iron and ferritin stay normal, so % saturation falls without '
             'true iron deficiency. Pregnancy also raises iron needs (absorption climbs to 3–4 mg/day), so real iron deficiency is common — '
             'serum ferritin, the store, is the number to check.',
  'fe:tx': 'Treating iron deficiency — oral ferrous salts (sulfate, gluconate, fumarate) correct it as fast as IV iron if absorption is normal; '
           'reticulocytes rise in about 5–7 days, then hemoglobin climbs. Keep going 3–6 months after the cause is fixed to refill stores. '
           'GI upset, black stools. IV iron for malabsorption or CKD on EPO. Find the bleeding source.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='fe', label='Pick one disorder', type='one', options=[
      ['ida', 'Iron deficiency', 'ida'], ['acd', 'Anemia of chronic disease', 'acd'], ['hh', 'Hemochromatosis', 'hemochrom'],
      ['sidero', 'Sideroblastic anemia', 'sidero'], ['lead', 'Lead poisoning', 'lead'], ['thal', 'Thalassemia trait', 'betathal'],
      ['preg', 'Pregnancy · OCP use', 'ironstudies'], ['tx', 'Iron deficiency on oral iron', 'ironrx']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2460, y=110, w=1000),
  src='First Aid pp. 67, 209, 381, 402, 423–425, 427, 430–431 · Robbins ch 14, 18 · Katzung ch 33 · Marks ch 42 · Bootcamp Heme/Onc')

MAP = dict(
  id='ironflow', title='Iron in Motion', topic='heme', after='rbc',
  sub='Iron absorbed in the duodenum, carried on transferrin, built into heme in the marrow and recycled by macrophages — while hepcidin '
      'from the liver closes ferroportin. Pick a disorder to see where iron gets stuck and read the iron studies. Tap a transporter for its card',
  w=3500, h=2120,
  fa='67, 209, 381, 402, 421, 423–425, 427, 430–431', src=[RB14, RB18, KZ33, KZ57, MK42, BC],
  lanes=[('ifGut', 'Absorption', 'glycogen'), ('ifBlood', 'Transport & heme', 'glycolysis'), ('ifStore', 'Stores & hepcidin', 'ppp'),
         ('ifDz', 'Iron disorders', 'tca')],
  comps=[],
  nodes=[
    ('if1', 'Iron absorption', 560, 1120, 'ifGut', 'duodenum · DMT1 · ferroportin', ['ironcycle', 'nutabsorb', 'scurvy'], 'hub'),
    ('if2', 'Hepcidin & HFE', 2110, 300, 'ifStore', 'the off switch for ferroportin', ['hemochrom', 'acutephase']),
    ('if3', 'Iron deficiency', 2110, 640, 'ifDz', 'blood loss until proven otherwise', ['ida', 'ironrx']),
    ('if4', 'Anemia of chronic disease', 2110, 760, 'ifDz', 'hepcidin ↑', ['acd', 'ckdanemia', 'esa']),
    ('if5', 'Iron studies', 1400, 1800, 'ifDz', 'iron · TIBC · ferritin · saturation', ['ironstudies', 'anemiaapproach'], 'hub'),
    ('if6', 'Heme synthesis defects', 1760, 1800, 'ifBlood', 'ALA synthase · lead', ['sidero', 'lead', 'b6', 'aip']),
    ('if7', 'Thalassemia trait', 2120, 1800, 'ifDz', 'normal iron studies', ['alphathal', 'betathal']),
    ('if8', 'Red cell recycling', 1400, 1910, 'ifBlood', 'macrophages · reticulocytes', ['macrophage', 'reticindex', 'hemolysislabs']),
    ('if9', 'Pregnancy · OCP', 1760, 1910, 'ifDz', 'TIBC ↑', ['pregphys', 'ocp']),
    ('if10', 'Iron overload drugs', 2120, 1910, 'ifStore', 'phlebotomy · chelators', ['chelators', 'ironrx']),
  ],
  panels=[
    (2460, 600, 1000, 'Iron studies (First Aid pp. 423, 425; Bootcamp)', [
      ('Iron deficiency', 'iron ↓ · TIBC ↑ · ferritin ↓ · saturation ↓↓ · FEP ↑'),
      ('Chronic disease', 'iron ↓ · TIBC ↓ · ferritin ↑ · saturation normal or ↓'),
      ('Hemochromatosis', 'iron ↑ · TIBC ↓ · ferritin ↑ · saturation ↑↑'),
      ('Pregnancy / OCP use', 'iron normal · TIBC ↑ · ferritin normal · saturation ↓'),
      ('Sideroblastic anemia', 'iron ↑ · TIBC normal or ↓ · ferritin ↑'),
      ('Thalassemia trait', 'normal iron studies · Mentzer index < 13')]),
    (2460, 830, 1000, 'Iron drugs (Katzung ch 33, 57; First Aid pp. 402, 425, 431)', [
      ('Ferrous sulfate, gluconate', 'oral, first line · GI upset, black stools · 3–6 months'),
      ('IV iron (dextran, sucrose…)', 'malabsorption, CKD on EPO · anaphylaxis risk (iron dextran)'),
      ('Deferoxamine', 'IV chelator · acute iron poisoning (charcoal does not bind iron)'),
      ('Deferasirox, deferiprone', 'oral chelators · transfusional overload · deferiprone: agranulocytosis'),
      ('Phlebotomy', 'first line for hereditary hemochromatosis without anemia'),
      ('Succimer, EDTA, dimercaprol', 'chelators for lead poisoning')]),
  ],
  dyn=dyn,
)
