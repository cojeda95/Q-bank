# Protozoa in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A body with the organs these protozoa reach — brain and cribriform plate, eye, neck nodes, heart, esophagus and colon,
# liver and spleen, skin, red cells in the blood, and the genital tract — with each parasite's way in on the left. A `one`
# switch follows one parasite from entry to target: Naegleria (nose → olfactory nerve → brain), T brucei (blood and lymph,
# waves of parasitemia, then CNS), Babesia (Ixodes tick → red cells; an `asplenic` toggle), T cruzi (kissing bug → heart
# and gut ganglia), Leishmania (sandfly → macrophages of skin or liver/spleen) and Trichomonas (sexual only). A `treat`
# toggle gives each card's drug. Vectors are named only where the card names them. 5 readouts. Facts from the pinned cards;
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

D = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
T = dict(brain=(1000, 300), nose=(950, 380), eye=(1050, 360), node=(1090, 470), heart=(1050, 640), eso=(1000, 600),
         liver=(920, 790), spleen=(1100, 790), colon=(1000, 960), skin=(1300, 760), rbc=(700, 880), gen=(1000, 1090))

text('Protozoa — how each gets in, and where it goes', 180, 150, 'dyn-big')
text('way in on the left · target organs in the body', 180, 176, 'dyn-cap')

# ════════ body ════════
add('<circle cx="1000" cy="340" r="110" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:4"/>')
add('<path d="M860 470 H1140 L1180 1120 H820 Z" style="fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:4;stroke-linejoin:round"/>')
add('<path d="M1140 500 L1320 820" style="stroke:var(--dk2);stroke-width:40;opacity:.12;stroke-linecap:round"/>')
add('<path d="M980 300 C960 330 955 360 950 380" style="fill:none;stroke:var(--dk7);stroke-width:5"/>'); text('olfactory n. · cribriform', 930, 400, 'nf-l2', 'end')
add('<path d="M1000 520 V720" style="stroke:var(--dk5);stroke-width:18;opacity:.3"/>'); text('esophagus', 980, 540, 'nf-l2', 'end')
add('<path d="M900 900 C900 1010 1100 1010 1100 900 V860" style="fill:none;stroke:var(--dk5);stroke-width:22;opacity:.3"/>'); text('colon', 1120, 1000, 'nf-l2')
for k in ('heart', 'liver', 'spleen', 'node', 'eye'):
    x, y = T[k]; r = dict(heart=56, liver=60, spleen=44, node=18, eye=18)[k]
    add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>')
text('heart', 1120, 640, 'nf-l2'); text('liver', 860, 800, 'nf-l2', 'end'); text('spleen', 1160, 800, 'nf-l2'); text('neck node', 1120, 476, 'nf-l2')
text('skin', 1320, 820, 'nf-l2', 'middle')
add('<path d="M560 880 H900" style="stroke:var(--nf-blood);stroke-width:40;opacity:.15;stroke-linecap:round"/>'); text('blood · red cells', 560, 850, 'nf-l2')
add('<circle cx="1000" cy="1090" r="30" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>'); text('genital tract', 1050, 1100, 'nf-l2')
# entries
EN = dict(naeg=('warm fresh water, swimming', 330), tryp=('blood and lymph', 520), bab=('Ixodes tick bite', 700),
          chag=('kissing bug feces → bite or eye', 470), leish=('sandfly → promastigotes', 760), trich=('sexual contact only', 1090))
for k, (s, y) in EN.items(): text(s, 300, y, 'nf-l1 dyn-tag', when=D(k))
# lesions
def blob(k, when, r=26):
    x, y = T[k]; add(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--bad);fill-opacity:.5;stroke:var(--bad);stroke-width:3"/>', when=when, unless=['treat'])
blob('brain', D('naeg', 'tryp'), 60); blob('node', D('tryp')); blob('eye', D('chag'))
blob('heart', D('chag'), 50); blob('liver', D('leish'), 70); blob('spleen', D('leish'), 56); blob('gen', D('trich'))
add('<path d="M1000 520 V720" style="stroke:var(--bad);stroke-width:40;opacity:.35"/>', when=D('chag'), unless=['treat'])
add('<path d="M900 900 C900 1010 1100 1010 1100 900 V860" style="fill:none;stroke:var(--bad);stroke-width:44;opacity:.35"/>', when=D('chag'), unless=['treat'])
blob('skin', D('leish'), 30)
for x in (640, 720, 800):
    add(f'<circle cx="{x}" cy="880" r="18" style="fill:var(--nf-blood);fill-opacity:.4;stroke:var(--bad);stroke-width:3"/>', when=D('bab'), unless=['treat'])
    add(f'<path d="M{x - 6} 874 h12 M{x - 6} 886 h12" style="stroke:var(--ink);stroke-width:3"/>', when=D('bab'), unless=['treat'])
TAG = dict(naeg='rapidly fatal meningoencephalitis days later · motile amoebas in CSF', tryp='antigenic variation → waves of fever · nodes, then somnolence, coma',
           bab='ring forms and Maltese crosses · hemolysis', chag='Romaña sign · later dilated cardiomyopathy, megaesophagus, megacolon',
           leish='amastigotes in macrophages · kala-azar: fever, hepatosplenomegaly, pancytopenia · or skin ulcers',
           trich='frothy green discharge, strawberry cervix, pH > 4.5 — no cyst form')
for k, s in TAG.items(): text(s, 1000, 1220, 'nf-l1 dyn-tag', 'middle', when=D(k))
RX = dict(naeg='amphotericin B (a few survive)', tryp='suramin (blood) · melarsoprol (CNS)', bab='atovaquone + azithromycin',
          chag='benznidazole or nifurtimox', leish='amphotericin B, sodium stibogluconate', trich='metronidazole — patient and partners')
for k, s in RX.items(): text('treat: ' + s, 1000, 1260, 'nf-l1', 'middle', when=[f'dx:{k}&treat'])
text('no spleen — infected red cells are not cleared: severe', 700, 950, 'nf-l1 dyn-tag', 'middle', when=['dx:bab&asplen'])

# ════════ motion ════════
def go(d, k, when, n=3, speed=110):
    return dict(d=d, len=900, speed=speed, r=9, base={k: n}, when=when, mods=[dict(when=['treat'], set={k: 0})])
flows = [
  go('M300 380 C600 380 900 390 950 380 C970 350 990 320 1000 300', 'par', D('naeg')),
  go('M300 520 C500 500 700 880 900 880 C1000 860 1060 600 1090 470', 'par', D('tryp')),
  go('M1090 470 C1060 420 1030 360 1000 300', 'par', D('tryp'), 2, 60),
  go('M300 700 C400 760 500 880 600 880 H880', 'par', D('bab')),
  go('M300 470 C600 420 900 380 1050 360', 'par', D('chag')),
  go('M1050 360 C1060 450 1060 560 1050 640', 'par', D('chag'), 2),
  go('M1050 640 C1020 700 1000 760 1000 900', 'par', D('chag'), 2),
  go('M300 760 C700 760 1100 700 1300 760', 'par', D('leish')),
  go('M300 760 C600 790 800 790 920 790', 'par', D('leish'), 2),
  go('M920 790 H1100', 'par', D('leish'), 2),
  go('M300 1090 H1000', 'par', D('trich')),
]
flows.append(dict(d='M560 880 H900', len=340, speed=120, r=8, base=dict(rbc=3), mods=[dict(when=D('bab'), set=dict(rbc=1)),
             dict(when=['dx:bab&asplen'], set=dict(rbc=0))]))
sites = [dict(x=900, y=330, n=[-1, -1], w=10, t='rec', l='', aria='Naegleria', c='naegleria', ions=[]),
         dict(x=1140, y=440, n=[1, -1], w=10, t='rec', l='', aria='African sleeping sickness', c='trypbrucei', ions=[]),
         dict(x=640, y=820, n=[0, -1], w=10, t='rec', l='', aria='Babesiosis', c='babesia', ions=[]),
         dict(x=1120, y=580, n=[1, -1], w=10, t='rec', l='', aria='Chagas disease', c='chagas', ions=[]),
         dict(x=860, y=720, n=[-1, -1], w=10, t='rec', l='', aria='Leishmaniasis', c='leish', ions=[]),
         dict(x=940, y=1120, n=[-1, 1], w=10, t='rec', l='', aria='Trichomoniasis', c='trichomonas', ions=[])]

readouts = [
  dict(l='CNS infection', mods=[dict(when=D('naeg', 'tryp'), d=1)]),
  dict(l='Hemolysis', mods=[dict(when=D('bab'), d=1)]),
  dict(l='Hepatosplenomegaly', mods=[dict(when=D('leish'), d=1)]),
  dict(l='Heart & gut dilation', mods=[dict(when=D('chag'), d=1)]),
  dict(l='Fever', mods=[dict(when=D('tryp', 'bab', 'leish'), d=1)]),
]

notes = {
  '': 'Pick a protozoan to follow it from its way in to the organ it damages; then treat it.',
  'dx:naeg': 'Naegleria fowleri: enters the nose while swimming in warm fresh water and follows the olfactory nerve through the '
             'cribriform plate to the brain — rapidly fatal meningoencephalitis; motile amoebas in CSF. Amphotericin B.',
  'dx:tryp': 'T brucei (African sleeping sickness): trypanosomes multiply in blood and lymph, then invade the CNS; antigenic '
             'variation of the surface glycoprotein gives waves of parasitemia and fever. Nodes, then somnolence and coma. '
             'Suramin for blood-borne disease, melarsoprol for CNS.',
  'dx:bab': 'Babesia: Ixodes ticks put it into red cells → hemolysis; ring forms and Maltese cross tetrads. Severe without a '
            'spleen; co-infection with Lyme or Anaplasma. Atovaquone + azithromycin.',
  'dx:chag': 'T cruzi (Chagas): the kissing bug defecates near its bite; parasites enter the wound or eye (Romaña sign). They '
             'destroy cardiac muscle and gut autonomic ganglia — dilated cardiomyopathy, megaesophagus, megacolon years later. '
             'Benznidazole or nifurtimox.',
  'dx:leish': 'Leishmania: sandflies inject promastigotes that become amastigotes in macrophages of skin (ulcers) or '
              'reticuloendothelial organs (kala-azar: fever, hepatosplenomegaly, pancytopenia). Amphotericin B, stibogluconate.',
  'dx:trich': 'Trichomonas: flagellated, no cyst form, so it cannot survive outside the body — sexual spread only. Frothy green '
              'discharge, strawberry cervix, motile trophozoites, pH > 4.5. Metronidazole for patient and partners.',
}

dyn = dict(
  kinds=dict(par=['mov', '--bad'], rbc=['mov', '--nf-blood']), groups=[['mov', 'Parasites · red cells']],
  switches=[dict(id='dx', label='Parasite', type='one', options=[
              ['naeg', 'Naegleria', 'naegleria'], ['tryp', 'T brucei', 'trypbrucei'], ['bab', 'Babesia', 'babesia'],
              ['chag', 'T cruzi (Chagas)', 'chagas'], ['leish', 'Leishmania', 'leish'], ['trich', 'Trichomonas', 'trichomonas']]),
            dict(id='asplen', label='Host', type='toggle', on='Asplenic', off='Remove the spleen', def_=False),
            dict(id='treat', label='Treat', type='toggle', on='Drug given', off='Give the drug', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 8')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='protosim', title='Protozoa in Motion', topic='id', after='fungpar',
  sub='Follow Naegleria up the olfactory nerve, trypanosomes through blood to brain, Babesia into red cells, T cruzi to heart and '
      'gut, Leishmania into macrophages and Trichomonas — then treat each',
  w=3600, h=1900,
  fa='153, 154, 155',
  src=['Robbins ch 8 — Infectious diseases', 'Katzung ch 52 — Antiprotozoal Drugs'],
  lanes=[('ptBlood', 'Blood & tissue', 'tca'), ('ptOther', 'CNS & genital', 'glycolysis')],
  nodes=[
    ('pt1', 'Naegleria fowleri', 330, 1700, 'ptOther', 'nose → brain', ['naegleria'], 'hub'),
    ('pt2', 'African sleeping sickness', 760, 1700, 'ptBlood', 'waves of fever', ['trypbrucei']),
    ('pt3', 'Babesiosis', 1200, 1700, 'ptBlood', 'red cells · asplenia', ['babesia']),
    ('pt4', 'Chagas disease', 1640, 1700, 'ptBlood', 'heart · megacolon', ['chagas']),
    ('pt5', 'Leishmaniasis', 2080, 1700, 'ptBlood', 'macrophages', ['leish']),
    ('pt6', 'Trichomoniasis', 2520, 1700, 'ptOther', 'sexual · no cyst', ['trichomonas'])],
  panels=[
    (2500, PANY, 1000, 'Drug for each (Katzung ch 52)', [
      ('Naegleria', 'amphotericin B'), ('T brucei', 'suramin · melarsoprol (CNS)'), ('Babesia', 'atovaquone + azithromycin'),
      ('T cruzi', 'benznidazole, nifurtimox'), ('Leishmania', 'amphotericin B, stibogluconate'), ('Trichomonas', 'metronidazole')])],
  dyn=dyn)
