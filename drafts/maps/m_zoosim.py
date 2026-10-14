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
# where each target sits on the figure (patient's right on the viewer's left); flows aim at these points
ORG = dict(node=(BX - 105, 1168, 'groin nodes (buboes)'), trunk=(BX + 60, 900, 'trunk skin'), palm=(BX + 300, 1090, 'palms · soles'),
           lung=(BX - 80, 770, 'lungs'), valve=(BX + 35, 820, 'heart valve'), liver=(BX - 70, 940, 'liver'), kidney=(BX + 105, 1030, 'kidneys'),
           calf=(BX - 82, 1300, 'calves'), eye=(BX + 26, 512, 'eyes'), clot=(BX + 330, 700, 'clotting (DIC)'), panc=(BX + 35, 995, 'pancreas'),
           wound=(BX - 262, 960, 'bite wound'), syn=(BX + 262, 905, 'nerve terminals'))
ROUTE = dict(plague=('rat', 'flea', ['node']), endty=('flea', 'flea', ['trunk']), epity=('louse', 'louse', ['trunk']), relap=('louse', 'louse', ['liver']),
             bruc=('cattle', 'cattle', ['liver']), lepto=('water', 'water', ['calf', 'eye', 'liver', 'kidney']), qfev=('cattle', 'cattle', ['lung', 'valve', 'liver']),
             bite=('dog', 'dog', ['wound']), pit=('snake', 'snake', ['wound', 'clot']), coral=('snake', 'snake', ['wound']),
             widow=('spider', 'spider', ['syn']), scorp=('spider', 'spider', ['panc']))
RX = dict(plague='streptomycin', endty='doxycycline', epity='doxycycline', qfev='doxycycline', bruc='streptomycin (sometimes)',
          pit='crotalid polyvalent immune Fab', relap='doxycycline or penicillin G',
          lepto='doxycycline · IV penicillin G for Weil disease', coral='equine antivenin within 4 h', widow='antivenin if symptomatic', scorp='scorpion immune F(ab′)₂')
TREAT = [f'dx:{k}&rx' for k in RX]

text('Zoonoses & bites — from the animal to the organ', 180, 150, 'dyn-big')
text('sources across the top · the body below · follow one route', 180, 176, 'dyn-cap')
# ── source icons (a 100 × 60 unit box, scaled into each card) ──
ICON = dict(
  rat=('M20 40 C20 22 44 16 62 22 C72 14 86 18 88 28 L96 32 L88 36 C84 44 70 46 62 44 C50 50 28 50 20 40 Z', 'M20 42 C10 44 4 50 2 58 M80 20 L78 12 M40 46 L38 56 M66 46 L66 56'),
  flea=('M28 32 C28 14 58 8 72 22 C84 36 72 52 50 52 C36 52 28 44 28 32 Z', 'M40 50 L30 60 M52 52 L50 60 M64 48 L76 60 M74 26 L90 16 M80 34 L96 30'),
  louse=('M50 6 C64 6 70 20 68 32 C66 48 60 56 50 56 C40 56 34 48 32 32 C30 20 36 6 50 6 Z', 'M34 24 L18 16 M33 34 L16 36 M35 44 L20 54 M66 24 L82 16 M67 34 L84 36 M65 44 L80 54 M36 30 H64 M37 40 H63'),
  cattle=('M18 20 H72 C80 20 84 24 86 30 L96 26 L98 38 L88 40 C86 44 82 46 76 46 L72 46 V58 H66 V46 H28 V58 H22 V46 C14 44 12 38 12 30 C12 24 14 20 18 20 Z', 'M86 28 L90 18 M12 28 L4 40'),
  water=('M50 4 C60 22 72 34 72 46 C72 58 62 62 50 62 C38 62 28 58 28 46 C28 34 40 22 50 4 Z', 'M2 58 C14 50 22 66 34 58 M66 58 C78 50 86 66 98 58'),
  dog=('M14 28 C14 22 20 20 26 22 L66 22 C70 16 76 10 84 12 L88 8 L90 18 C96 20 98 26 92 28 L84 30 L82 40 H76 V58 H70 V42 H34 V58 H28 V42 C20 40 16 36 14 32 L6 22 Z', ''),
  snake=('M84 18 C92 14 99 20 96 27 C93 33 86 32 84 28 Z', 'M6 50 C20 28 34 56 50 36 C64 18 74 40 86 26'),
  spider=('M40 30 C40 20 60 20 60 30 C60 40 40 40 40 30 Z M44 46 C44 38 56 38 56 46 C56 56 44 56 44 46 Z', 'M42 28 L20 12 L8 22 M41 32 L16 30 L4 40 M43 36 L22 46 L12 60 M45 40 L30 58 M58 28 L80 12 L92 22 M59 32 L84 30 L96 40 M57 36 L78 46 L88 60 M55 40 L70 58'))
def sc(d, x, y, w, h):
    return re.sub(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', lambda m: f'{x + float(m.group(1)) * w / 100:.0f} {y + float(m.group(2)) * h / 100:.0f}',
                  re.sub(r'([HV])(-?\d+\.?\d*)', lambda m: f'{m.group(1)}{(x + float(m.group(2)) * w / 100) if m.group(1) == "H" else (y + float(m.group(2)) * h / 100):.0f}', d))
import re
for k, (x, y, l) in SRC.items():
    add(f'<rect x="{x - 105}" y="{y - 70}" width="210" height="140" rx="22" style="fill:var(--dk6);fill-opacity:.08;stroke:var(--dk6);stroke-width:3"/>')
    body, lines = ICON[k]
    add(f'<path d="{sc(body, x - 60, y - 60, 120, 72)}" style="fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:3;stroke-linejoin:round"/>'
        + (f'<path d="{sc(lines, x - 60, y - 60, 120, 72)}" style="fill:none;stroke:var(--dk6);stroke-width:{9 if k == "snake" else 3};stroke-linecap:round"/>' if lines else ''))
    text(l, x, y + 50, 'nf-l2', 'middle')

# ── the figure ──
FIG = 'fill:var(--dk2);fill-opacity:.05;stroke:var(--dk2);stroke-width:4;stroke-linejoin:round'
add(f'<ellipse cx="{BX}" cy="520" rx="68" ry="80" style="{FIG}"/>')
add(f'<path d="M{BX - 30} 596 V636 M{BX + 30} 596 V636" style="stroke:var(--dk2);stroke-width:4"/>')
add(f'<path d="M{BX - 190} 650 C{BX - 120} 636 {BX + 120} 636 {BX + 190} 650 L{BX + 170} 1060 L{BX + 175} 1170 H{BX - 175} L{BX - 170} 1060 Z" style="{FIG}"/>')   # trunk
LIMB = 'fill:none;stroke:var(--dk2);stroke-width:46;stroke-linecap:round;stroke-linejoin:round;opacity:.16'
add(f'<path d="M{BX - 185} 670 L{BX - 262} 900 L{BX - 300} 1070 M{BX + 185} 670 L{BX + 262} 900 L{BX + 300} 1070" style="{LIMB}"/>')   # arms
add(f'<path d="M{BX - 90} 1170 L{BX - 82} 1300 L{BX - 90} 1405 H{BX - 150} M{BX + 90} 1170 L{BX + 82} 1300 L{BX + 90} 1405 H{BX + 150}" style="{LIMB}"/>')   # legs
FACE = 'fill:none;stroke:var(--dk2);stroke-width:3;stroke-linecap:round'
add(f'<path d="M{BX - 40} 512 Q{BX - 26} 502 {BX - 12} 512 Q{BX - 26} 520 {BX - 40} 512 Z M{BX + 12} 512 Q{BX + 26} 502 {BX + 40} 512 Q{BX + 26} 520 {BX + 12} 512 Z'
    f' M{BX} 520 L{BX - 6} 542 H{BX + 4} M{BX - 22} 562 Q{BX} 576 {BX + 22} 562" style="{FACE}"/>')
# organs, as outlines (same shapes as the atlas organ library); each lights red on its own outline when a route reaches it
OUT = dict(
  lungs=('M44 24 C30 22 10 44 8 78 C7 92 16 98 30 96 C40 94 46 88 46 76 Z M56 24 C70 22 92 44 94 78 C95 92 86 98 72 96 C64 94 60 90 60 84 C66 78 66 68 58 64 Z M47 2 H53 V18 L58 26 L55 28 L50 21 L45 28 L42 26 L47 18 Z', (BX - 165, 640, 330, 250)),
  heart=('M26 30 C14 34 8 50 14 62 C22 76 46 90 74 98 C80 90 88 76 90 60 C92 44 84 32 72 28 C60 24 40 26 26 30 Z', (BX - 25, 780, 120, 105)),
  liver=('M6 70 C2 44 10 18 30 10 C50 2 76 4 92 14 C98 18 99 26 94 30 C84 36 72 46 62 58 L58 62 C54 60 50 62 48 66 C42 80 30 94 18 92 C10 90 7 82 6 70 Z', (BX - 165, 885, 230, 120)),
  pancreas=('M6 60 C4 44 16 36 28 42 C40 48 54 44 70 36 C82 30 94 26 97 32 C99 40 88 46 76 52 C60 60 46 64 34 66 C30 76 22 84 14 80 C8 76 7 68 6 60 Z', (BX - 30, 975, 150, 50)),
  kidney_r=('M40 4 C14 4 2 28 4 52 C6 78 18 96 40 96 C56 96 66 86 64 72 C63 64 56 60 56 50 C56 40 63 36 64 28 C66 14 56 4 40 4 Z', (BX - 150, 990, 52, 85)),
  kidney_l=('M60 4 C86 4 98 28 96 52 C94 78 82 96 60 96 C44 96 34 86 36 72 C37 64 44 60 44 50 C44 40 37 36 36 28 C34 14 44 4 60 4 Z', (BX + 98, 990, 52, 85)))
ORGOUT = dict(lung=['lungs'], valve=['heart'], liver=['liver'], panc=['pancreas'], kidney=['kidney_r', 'kidney_l'])
for nm, (d, (x, y, w, h)) in OUT.items():
    add(f'<path d="{sc(d, x, y, w, h)}" style="fill:var(--dk10);fill-opacity:.14;stroke:var(--dk10);stroke-width:3"/>')
for k, nms in ORGOUT.items():
    hit = [dd for dd, (_, _, ts) in ROUTE.items() if k in ts]
    if hit:
        for nm in nms:
            d, (x, y, w, h) = OUT[nm]
            add(f'<path d="{sc(d, x, y, w, h)}" style="fill:var(--bad);fill-opacity:.38;stroke:var(--bad);stroke-width:4"/>', when=D(*hit), unless=TREAT)
add(f'<circle cx="{ORG["valve"][0]}" cy="{ORG["valve"][1]}" r="9" style="fill:var(--surface);stroke:var(--dk10);stroke-width:3"/>')   # the valve, inside the heart
# small sites: nodes, skin, palms, calves, eyes, wound, nerve terminal, blood
for x, y in ((BX - 112, 1160), (BX - 92, 1176), (BX + 92, 1176)): add(f'<ellipse cx="{x}" cy="{y}" rx="11" ry="7" style="fill:var(--dk9);fill-opacity:.4;stroke:var(--dk9);stroke-width:2"/>')
add(f'<path d="M{ORG["clot"][0]} {ORG["clot"][1] - 34} C{ORG["clot"][0] + 18} {ORG["clot"][1] - 10} {ORG["clot"][0] + 22} {ORG["clot"][1] + 4} {ORG["clot"][0]} {ORG["clot"][1] + 20} C{ORG["clot"][0] - 22} {ORG["clot"][1] + 4} {ORG["clot"][0] - 18} {ORG["clot"][1] - 10} {ORG["clot"][0]} {ORG["clot"][1] - 34} Z" style="fill:var(--nf-blood);fill-opacity:.3;stroke:var(--nf-blood);stroke-width:3"/>')
SPOT = dict(node=24, trunk=30, palm=24, calf=26, eye=22, wound=24, syn=22, clot=30)
for k, rr in SPOT.items():
    hit = [dd for dd, (_, _, ts) in ROUTE.items() if k in ts]
    x, y, _ = ORG[k]
    if k == 'trunk':   # a rash: dots over the trunk, palms and soles left clear
        add(''.join(f'<circle cx="{BX + dx}" cy="{yy}" r="9" style="fill:var(--bad);opacity:.55"/>' for dx, yy in ((-90, 720), (60, 700), (-30, 800), (110, 840), (-120, 880), (20, 900), (90, 960), (-70, 1000), (130, 1060), (-20, 1080))),
            when=D('endty', 'epity'), unless=TREAT)
        continue
    if k == 'palm':
        continue   # no zoonosis here lights the palms — the label marks that typhus spares them
    if hit:
        pts = [(x, y)] + ([(BX + 82, 1300)] if k == 'calf' else []) + ([(BX - 26, 512)] if k == 'eye' else [])
        add(''.join(f'<circle cx="{px}" cy="{py}" r="{rr}" style="fill:var(--bad);fill-opacity:.42"/>' for px, py in pts), when=D(*hit), unless=TREAT)
LBL = dict(node=(BX - 210, 1186, 'end'), trunk=(BX + 210, 960, None), palm=(BX + 330, 1094, None), lung=(BX - 210, 760, 'end'), valve=(BX + 210, 830, None),
           liver=(BX - 210, 940, 'end'), kidney=(BX + 210, 1036, None), calf=(BX - 130, 1306, 'end'), eye=(BX + 90, 506, None), clot=(BX + 330, 760, 'middle'),
           panc=(BX + 210, 998, None), wound=(BX - 310, 968, 'end'), syn=(BX + 300, 900, None))
for k, (lx, ly, an) in LBL.items(): text(ORG[k][2], lx, ly, 'nf-l2', an)
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
    if s1 != s2: flows.append(dict(d=f'M{x0 + 105} {y0} H{x1 - 105}', len=60, speed=40, r=8, base=dict(bug=2), when=D(d)))
    for t in ts:
        tx, ty, _ = ORG[t]
        flows.append(dict(d=f'M{x1} {y1 + 70} C{x1} {ty - 120} {tx} {y1 + 200} {tx} {ty}', len=800, speed=130, r=9, base=dict(bug=3),
                          when=D(d), mods=[dict(when=[f'dx:{d}&rx'], set=dict(bug=0))] if d in RX else []))
sites = [dict(x=ORG['node'][0], y=ORG['node'][1] - 50, n=[-1, -1], w=10, t='rec', l='', aria='Plague', c='plague', ions=[]),
         dict(x=BX + 200, y=640, n=[1, -1], w=10, t='rec', l='', aria='Typhus', c='typhus', ions=[]),
         dict(x=ORG['liver'][0] + 10, y=ORG['liver'][1] + 55, n=[0, 1], w=10, t='rec', l='', aria='Relapsing fever', c='relapsing', ions=[]),
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
  dict(l='Serum lipase', mods=[dict(when=D('scorp'), d=1)]),
]

notes = {
  '': 'Each zoonosis has its reservoir, its route into people and the organ it goes for. Pick one and follow it; then treat.',
  'dx:plague': 'Plague: Yersinia pestis lives in rats and prairie dogs; flea bites carry it to people, and the bite drains to '
               'painful, enlarged buboes. Streptomycin.',
  'dx:endty': 'Endemic typhus: Rickettsia typhi by fleas — rash starts on the trunk and spreads out, sparing palms and soles (the '
              'opposite of RMSF). Doxycycline.',
  'dx:epity': 'Epidemic typhus: Rickettsia prowazekii, person to person by the human body louse; same central rash. Doxycycline.',
  'dx:relap': 'Relapsing fever: Borrelia recurrentis, human body louse — fevers recur as surface antigens change; seen on Wright or '
              'Giemsa stain; hepatosplenomegaly, thrombocytopenia. Doxycycline or penicillin G — a Jarisch-Herxheimer reaction can follow.',
  'dx:bruc': 'Brucellosis: facultative intracellular coccobacilli from unpasteurized dairy or animal tissue and fluids — undulant '
             'fever. Streptomycin is sometimes used.',
  'dx:lepto': 'Leptospirosis: hook-ended spirochete in water with animal urine (surfers, tropics) — calf myalgias, conjunctival '
              'suffusion, jaundice; Weil disease: liver and kidney failure, hemorrhage, anemia. Doxycycline; IV penicillin G for Weil.',
  'dx:qfev': 'Q fever: Coxiella burnetii inhaled from cattle or sheep birth fluids — no vector, no rash; atypical pneumonia, '
             'hepatitis, culture-negative endocarditis. Doxycycline.',
  'dx:bite': 'Dog and cat bites: Pasteurella multocida cellulitis and osteomyelitis; cat scratch → Bartonella. Rabies and tetanus '
             'prophylaxis by the rules.',
  'dx:pit': 'Pit viper: venom coagulopathy (a cause of DIC) — crotalid polyvalent immune Fab, repeated until control.',
  'dx:coral': 'Coral snake: equine antivenin within 4 hours; more than 7 vials → serum sickness in almost everyone.',
  'dx:widow': 'Black widow: α-latrotoxin causes explosive release of transmitter from cholinergic and adrenergic vesicles; a toxic '
              'cause of myocarditis. Antivenin only if symptomatic.',
  'dx:scorp': 'Scorpion sting: a cause of acute pancreatitis (the S in I GET SMASHED) — lipase rises. Scorpion immune F(ab′)₂ if '
             'symptomatic.',
  'rx': 'Treatment: streptomycin (plague), doxycycline (typhus, Q fever, relapsing fever, leptospirosis), antivenoms for snakes, '
        'black widow, scorpion. No drug is drawn for bites (wound care, rabies and tetanus rules).',
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
  src='First Aid pp. 125, 144–148, 320, 404, 433 · Katzung ch 6, 45, Appendix 1 · Bootcamp Microbiology')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='zoosim', title='Zoonoses & Bites in Motion', topic='id', after='zoonoses',
  sub='Follow plague, typhus, relapsing fever, brucellosis, leptospirosis, Q fever, animal bites, snakes, black widow and scorpion '
      'from the animal to the organ — then treat',
  w=3600, h=2000,
  fa='123, 125, 139, 144, 145, 147, 148, 320, 404, 433, 701',
  src=['Robbins ch 8 — Infectious diseases', 'Katzung Appendix 1 — Vaccines, Immune Globulins, & Other Complex Biologic Products',
       full('Katzung', 45), full('Katzung', 6)],
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
    (2500, PANY, 1000, 'Reservoir → disease (First Aid p 147)', [
      ('Flea', 'plague, endemic typhus'), ('Body louse', 'epidemic typhus, relapsing fever'), ('Dairy, livestock', 'brucellosis, Q fever'),
      ('Water with urine', 'leptospirosis'), ('Dog, cat', 'Pasteurella, Bartonella')])],
  dyn=dyn)
