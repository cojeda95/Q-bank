# Zoonoses & Bites in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Sources across the top (rat and prairie dog, flea, body louse, cattle and sheep, contaminated water, dog and cat, snake,
# black widow and scorpion) and a body below with lymph nodes, skin (trunk vs palms and soles), lungs, heart valve, liver,
# kidney, calves, eyes, blood clotting and pancreas. A `dx` switch sends one organism or venom along the route its card
# names: plague, endemic and epidemic typhus, relapsing fever, brucellosis, leptospirosis (and Weil disease), Q fever,
# Pasteurella / Bartonella bites, pit viper and coral snake, black widow and scorpion. A `rx` toggle gives the card’s drug or
# antivenom where one is named. 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
SRC = dict(rat=(300, 340, 'rats · prairie dogs'), flea=(560, 340, 'flea'), louse=(820, 340, 'body louse'), cattle=(1080, 340, 'cattle · sheep'),
           water=(1340, 340, 'water with animal urine'), dog=(1600, 340, 'dog · cat'), snake=(1860, 340, 'snake'), spider=(2120, 340, 'black widow · scorpion'))
BX = 1200
ORG = dict(node=(BX - 160, 700, 'lymph node'), trunk=(BX, 820, 'trunk skin'), palm=(BX + 260, 1000, 'palms · soles'), lung=(BX - 80, 760, 'lungs'),
           valve=(BX + 60, 780, 'heart valve'), liver=(BX - 60, 940, 'liver'), kidney=(BX + 90, 960, 'kidneys'), calf=(BX - 90, 1260, 'calves'),
           eye=(BX + 40, 560, 'eyes'), clot=(BX + 260, 760, 'clotting (DIC)'), panc=(BX + 20, 1060, 'pancreas'), wound=(BX - 280, 900, 'bite wound'),
           syn=(BX + 260, 880, 'nerve terminals'))
ROUTE = dict(plague=('rat', 'flea', ['node']), endty=('flea', 'flea', ['trunk']), epity=('louse', 'louse', ['trunk']), relap=('louse', 'louse', ['valve']),
             bruc=('cattle', 'cattle', ['liver']), lepto=('water', 'water', ['calf', 'eye', 'liver', 'kidney']), qfev=('cattle', 'cattle', ['lung', 'valve', 'liver']),
             bite=('dog', 'dog', ['wound']), pit=('snake', 'snake', ['wound', 'clot']), coral=('snake', 'snake', ['wound']),
             widow=('spider', 'spider', ['syn']), scorp=('spider', 'spider', ['panc']))
RX = dict(plague='streptomycin', endty='doxycycline', epity='doxycycline', qfev='doxycycline', bruc='streptomycin (sometimes)',
          pit='crotalid polyvalent immune Fab', coral='equine antivenin within 4 h', widow='antivenin if symptomatic', scorp='scorpion immune F(ab′)₂')
TREAT = [f'dx:{k}&rx' for k in RX]

text('Zoonoses & bites — from the animal to the organ', 180, 150, 'dyn-big')
text('sources across the top · the body below · follow one route', 180, 176, 'dyn-cap')
for k, (x, y, l) in SRC.items():
    add(f'<rect x="{x - 100}" y="{y - 40}" width="200" height="80" rx="20" style="fill:var(--dk6);fill-opacity:.12;stroke:var(--dk6);stroke-width:3"/>')
    text(l, x, y + 8, 'nf-l1', 'middle')
add(f'<circle cx="{BX}" cy="560" r="90" style="fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:4"/>')
add(f'<path d="M{BX - 180} 660 H{BX + 180} L{BX + 210} 1180 H{BX - 210} Z" style="fill:var(--dk2);fill-opacity:.04;stroke:var(--dk2);stroke-width:4"/>')
add(f'<path d="M{BX - 120} 1180 V1320 M{BX + 120} 1180 V1320" style="stroke:var(--dk2);stroke-width:60;opacity:.1;stroke-linecap:round"/>')
for k, (x, y, l) in ORG.items():
    add(f'<circle cx="{x}" cy="{y}" r="26" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>')
    hit = [d for d, (_, _, ts) in ROUTE.items() if k in ts]
    if hit: add(f'<circle cx="{x}" cy="{y}" r="34" style="fill:var(--bad);fill-opacity:.4"/>', when=D(*hit), unless=TREAT)
    right = x >= BX
    text(l, x + (40 if right else -40), y + 6, 'nf-l2', None if right else 'end')
TAG = dict(plague='Yersinia pestis — flea bite → painful buboes', endty='endemic typhus (R typhi, fleas) — rash starts on the trunk, spares palms and soles',
           epity='epidemic typhus (R prowazekii, body louse) — central rash spreading out, palms and soles spared',
           relap='relapsing fever (B recurrentis, louse) — fevers return as surface antigens change; Jarisch-Herxheimer with antibiotics',
           bruc='brucellosis — unpasteurized dairy or animal tissue; intracellular coccobacillus; undulant fever',
           lepto='leptospirosis — surfers, tropics: calf myalgia, conjunctival suffusion, jaundice · Weil: liver + kidney failure',
           qfev='Q fever (Coxiella) — inhaled from birth fluids, no vector, no rash: atypical pneumonia, hepatitis, culture-negative endocarditis',
           bite='Pasteurella — cellulitis, osteomyelitis after a dog or cat bite · cat scratch: Bartonella', pit='pit viper — venom coagulopathy (DIC)',
           coral='coral snake — equine antivenin', widow='black widow α-latrotoxin — explosive transmitter release; myocarditis',
           scorp='scorpion sting — acute pancreatitis (the S in I GET SMASHED)')
for k, s in TAG.items(): text(s, BX, 1460, 'nf-l1 dyn-tag', 'middle', when=D(k))
for k, s in RX.items(): text('treat: ' + s, BX, 1500, 'nf-l1', 'middle', when=[f'dx:{k}&rx'])

# ════════ motion ════════
flows = []
for d, (s1, s2, ts) in ROUTE.items():
    x0, y0, _ = SRC[s1]; x1, y1, _ = SRC[s2]
    if s1 != s2: flows.append(dict(d=f'M{x0 + 100} {y0} H{x1 - 100}', len=60, speed=40, r=8, base=dict(bug=2), when=D(d)))
    for t in ts:
        tx, ty, _ = ORG[t]
        flows.append(dict(d=f'M{x1} {y1 + 40} C{x1} {ty - 120} {tx} {y1 + 200} {tx} {ty - 30}', len=800, speed=130, r=9, base=dict(bug=3),
                          when=D(d), mods=[dict(when=[f'dx:{d}&rx'], set=dict(bug=0))]))
sites = [dict(x=ORG['node'][0], y=ORG['node'][1] - 50, n=[-1, -1], w=10, t='rec', l='', aria='Plague', c='plague', ions=[]),
         dict(x=BX + 200, y=640, n=[1, -1], w=10, t='rec', l='', aria='Typhus', c='typhus', ions=[]),
         dict(x=ORG['valve'][0] + 40, y=ORG['valve'][1] - 50, n=[1, -1], w=10, t='rec', l='', aria='Relapsing fever', c='relapsing', ions=[]),
         dict(x=ORG['liver'][0] - 70, y=ORG['liver'][1] + 40, n=[-1, 1], w=10, t='rec', l='', aria='Brucellosis', c='brucella', ions=[]),
         dict(x=ORG['calf'][0], y=ORG['calf'][1] + 50, n=[0, 1], w=10, t='rec', l='', aria='Leptospirosis', c='lepto', ions=[]),
         dict(x=ORG['lung'][0] - 70, y=ORG['lung'][1] - 40, n=[-1, -1], w=10, t='rec', l='', aria='Q fever', c='qfever', ions=[]),
         dict(x=ORG['wound'][0] - 50, y=ORG['wound'][1] + 50, n=[-1, 1], w=10, t='rec', l='', aria='Dog and cat bites', c='animalbite', ions=[]),
         dict(x=ORG['clot'][0] + 60, y=ORG['clot'][1] - 40, n=[1, -1], w=10, t='rec', l='', aria='Snake envenomation', c='snakebite', ions=[]),
         dict(x=ORG['syn'][0] + 60, y=ORG['syn'][1] + 40, n=[1, 1], w=10, t='rec', l='', aria='Black widow and scorpion', c='venom', ions=[])]

readouts = [
  dict(l='Lymph nodes', mods=[dict(when=D('plague'), d=1)]),
  dict(l='Rash (palms/soles spared)', mods=[dict(when=D('endty', 'epity'), d=1)]),
  dict(l='Jaundice', mods=[dict(when=D('lepto'), d=1)]),
  dict(l='Clotting factors', mods=[dict(when=D('pit'), d=-1)]),
  dict(l='Recurring fevers', mods=[dict(when=D('relap', 'bruc'), d=1)]),
]

notes = {
  '': 'Each zoonosis has its reservoir, its route into people and the organ it goes for. Pick one and follow it; then treat.',
  'dx:plague': 'Plague: Yersinia pestis lives in rats and prairie dogs; flea bites carry it to people, and the bite drains to '
               'painful, enlarged buboes. Streptomycin.',
  'dx:endty': 'Endemic typhus: Rickettsia typhi by fleas — rash starts on the trunk and spreads out, sparing palms and soles (the '
              'opposite of RMSF). Doxycycline.',
  'dx:epity': 'Epidemic typhus: Rickettsia prowazekii, person to person by the human body louse; same central rash. Doxycycline.',
  'dx:relap': 'Relapsing fever: Borrelia recurrentis, human body louse — fevers recur as surface antigens change; seen on Wright or '
              'Giemsa stain; Jarisch-Herxheimer reaction after antibiotics start.',
  'dx:bruc': 'Brucellosis: facultative intracellular coccobacilli from unpasteurized dairy or animal tissue and fluids — undulant '
             'fever. Streptomycin is sometimes used.',
  'dx:lepto': 'Leptospirosis: hook-ended spirochete in water with animal urine (surfers, tropics) — calf myalgias, conjunctival '
              'suffusion, jaundice; Weil disease: liver and kidney failure, hemorrhage, anemia.',
  'dx:qfev': 'Q fever: Coxiella burnetii inhaled from cattle or sheep birth fluids — no vector, no rash; atypical pneumonia, '
             'hepatitis, culture-negative endocarditis. Doxycycline.',
  'dx:bite': 'Dog and cat bites: Pasteurella multocida cellulitis and osteomyelitis; cat scratch → Bartonella. Rabies and tetanus '
             'prophylaxis by the rules.',
  'dx:pit': 'Pit viper: venom coagulopathy (a cause of DIC) — crotalid polyvalent immune Fab, repeated until control.',
  'dx:coral': 'Coral snake: equine antivenin within 4 hours; more than 7 vials → serum sickness in almost everyone.',
  'dx:widow': 'Black widow: α-latrotoxin causes explosive release of transmitter from cholinergic and adrenergic vesicles; a toxic '
              'cause of myocarditis. Antivenin only if symptomatic.',
  'dx:scorp': 'Scorpion sting: a cause of acute pancreatitis (the S in I GET SMASHED). Scorpion immune F(ab′)₂ if symptomatic.',
  'rx': 'Treatment from each card: streptomycin (plague), doxycycline (typhus, Q fever), antivenoms for snakes, black widow, scorpion.',
}

dyn = dict(
  kinds=dict(bug=['mov', '--bad']), groups=[['mov', 'Organism or venom']],
  switches=[dict(id='dx', label='Exposure', type='one', options=[
              ['plague', 'Plague', 'plague'], ['endty', 'Endemic typhus', 'typhus'], ['epity', 'Epidemic typhus', 'typhus'],
              ['relap', 'Relapsing fever', 'relapsing'], ['bruc', 'Brucellosis', 'brucella'], ['lepto', 'Leptospirosis', 'lepto'],
              ['qfev', 'Q fever', 'qfever'], ['bite', 'Dog or cat bite', 'animalbite'], ['pit', 'Pit viper', 'snakebite'],
              ['coral', 'Coral snake', 'snakebite'], ['widow', 'Black widow', 'venom'], ['scorp', 'Scorpion', 'venom']]),
            dict(id='rx', label='Treat', type='toggle', on='Treatment given', off='Give the treatment', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 8')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='zoosim', title='Zoonoses & Bites in Motion', topic='id', after='zoonoses',
  sub='Follow plague, typhus, relapsing fever, brucellosis, leptospirosis, Q fever, animal bites, snakes, black widow and scorpion '
      'from the animal to the organ — then treat',
  w=3600, h=2000,
  fa='123, 125, 139, 144, 145, 147, 148, 320, 404, 433, 701',
  src=['Robbins ch 8 — Infectious diseases', 'Katzung Appendix 1 — Vaccines, Immune Globulins, & Other Complex Biologic Products'],
  lanes=[('zoVec', 'Vectors & animals', 'tca'), ('zoVen', 'Bites & venom', 'glycolysis')],
  nodes=[
    ('zo1', 'Plague', 330, 1720, 'zoVec', 'flea · buboes', ['plague'], 'hub'),
    ('zo2', 'Typhus', 760, 1720, 'zoVec', 'flea · louse', ['typhus']),
    ('zo3', 'Relapsing fever', 1200, 1720, 'zoVec', 'louse · antigens', ['relapsing']),
    ('zo4', 'Brucellosis', 1640, 1720, 'zoVec', 'dairy', ['brucella']),
    ('zo5', 'Leptospirosis', 2080, 1720, 'zoVec', 'water · Weil', ['lepto']),
    ('zo6', 'Q fever', 2520, 1720, 'zoVec', 'no vector · no rash', ['qfever']),
    ('zo7', 'Dog & cat bites', 330, 1850, 'zoVen', 'Pasteurella', ['animalbite']),
    ('zo8', 'Snake envenomation', 760, 1850, 'zoVen', 'DIC · antivenom', ['snakebite']),
    ('zo9', 'Black widow & scorpion', 1200, 1850, 'zoVen', 'latrotoxin · pancreatitis', ['venom'])],
  panels=[
    (2500, PANY, 1000, 'Reservoir → disease (Robbins ch 8)', [
      ('Flea', 'plague, endemic typhus'), ('Body louse', 'epidemic typhus, relapsing fever'), ('Dairy, livestock', 'brucellosis, Q fever'),
      ('Water with urine', 'leptospirosis'), ('Dog, cat', 'Pasteurella, Bartonella')])],
  dyn=dyn)
