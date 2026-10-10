# The Foot in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A medial side view of the foot — calcaneus, Achilles tendon and retrocalcaneal bursa, the plantar fascia as a bowstring
# under the arch, metatarsal heads and the MTP/PIP/DIP joints — with a top view of the forefoot. `st` (steps, auto) moves
# body weight heel → midfoot → metatarsal heads. A `one` switch adds a problem: plantar fasciitis (a `morning` toggle for the
# first-step pain), retrocalcaneal bursitis, Sever disease, Morton neuroma (3rd web space), bunion, hammer toe, claw toe,
# metatarsus adductus. Geometry is schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
GY = 960

text('The foot — where the weight goes, and what hurts', 180, 150, 'dyn-big')
text('left: medial side view · right: top view of the forefoot · schematic', 180, 176, 'dyn-cap')

# ════════ side view ════════
add(f'<path d="M400 {GY + 10} H1560" style="stroke:var(--ink-3);stroke-width:4"/>'); text('ground', 400, GY + 44, 'nf-l2')
add('<ellipse cx="560" cy="860" rx="110" ry="80" style="fill:var(--dk6);fill-opacity:.2;stroke:var(--dk6);stroke-width:4"/>'); text('calcaneus', 470, 780, 'nf-l2', 'end')
add('<path d="M650 820 C760 700 960 680 1120 760 C1220 810 1280 860 1320 900" style="fill:none;stroke:var(--dk6);stroke-width:46;opacity:.2;stroke-linecap:round"/>')
text('arch', 900, 680, 'nf-l2', 'middle')
add('<path d="M600 800 C620 640 640 520 650 380" style="fill:none;stroke:var(--dk4);stroke-width:26;opacity:.4"/>'); text('Achilles', 670, 420, 'nf-l2')
add('<circle cx="640" cy="790" r="20" style="fill:var(--nf-h2o);fill-opacity:.3;stroke:var(--dk9);stroke-width:3"/>'); text('bursa', 690, 800, 'nf-l2')
add('<circle cx="640" cy="790" r="34" style="fill:var(--bad);fill-opacity:.5"/>', when=D('bursa'))
add('<path d="M580 935 C780 930 1100 935 1300 935" style="fill:none;stroke:var(--dk9);stroke-width:10"/>'); text('plantar fascia', 900, 975, 'nf-l2', 'middle')
add('<circle cx="590" cy="930" r="30" style="fill:var(--bad);fill-opacity:.5"/>', when=D('pf'))
add('<circle cx="590" cy="930" r="44" style="fill:var(--bad);fill-opacity:.7"/>', when=['dx:pf&morning'])
add('<path d="M620 790 C630 830 640 860 650 880" style="stroke:var(--bad);stroke-width:12"/>', when=D('sever'))
text('Achilles traction on the growth plate', 540, 700, 'nf-l1 dyn-tag', 'end', when=D('sever'))
add('<circle cx="1310" cy="905" r="30" style="fill:var(--dk6);fill-opacity:.3;stroke:var(--dk6);stroke-width:3"/>'); text('MT heads', 1310, 860, 'nf-l2', 'middle')
# toes
TOE = dict(nl=('M1330 905 L1410 905 L1460 905 L1500 905',), ham=('M1330 905 L1380 860 L1430 910 L1480 905',),
           claw=('M1330 905 L1380 860 L1420 905 L1440 950',))
add(f'<path d="{TOE["nl"][0]}" style="fill:none;stroke:var(--dk6);stroke-width:22;stroke-linecap:round;stroke-linejoin:round;opacity:.5"/>', unless=D('ham', 'claw'))
add(f'<path d="{TOE["ham"][0]}" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-linecap:round;stroke-linejoin:round;opacity:.6"/>', when=D('ham'))
add(f'<path d="{TOE["claw"][0]}" style="fill:none;stroke:var(--bad);stroke-width:22;stroke-linecap:round;stroke-linejoin:round;opacity:.6"/>', when=D('claw'))
text('MTP · PIP · DIP', 1420, 820, 'nf-l2', 'middle')
LOAD = dict(heel=(590, 'heel strike'), mid=(950, 'midfoot'), push=(1310, 'metatarsal heads — push-off'))
for k, (x, l) in LOAD.items():
    add(f'<path d="M{x} 560 V{GY - 40}" style="stroke:var(--accent);stroke-width:14;opacity:.6"/>', when=[f'st:{k}'])
    add(f'<path d="M{x - 24} {GY - 70} L{x} {GY - 30} L{x + 24} {GY - 70}" style="fill:none;stroke:var(--accent);stroke-width:10"/>', when=[f'st:{k}'])
    text(l, x, 540, 'nf-l1', 'middle', when=[f'st:{k}'])

# ════════ top view ════════
TX, TY = 2000, 1000
add(f'<rect x="{TX - 260}" y="{TY - 640}" width="560" height="760" rx="30" class="dyn-soft"/>'); text('top view (left foot)', TX - 240, TY - 660, 'nf-l1')
add(f'<path d="M{TX - 120} {TY} C{TX - 160} {TY - 160} {TX - 150} {TY - 300} {TX - 100} {TY - 380} M{TX + 140} {TY} C{TX + 150} {TY - 150} {TX + 140} {TY - 280} {TX + 120} {TY - 360}" '
    'style="fill:none;stroke:var(--dk6);stroke-width:6;opacity:.4"/>', unless=D('ma'))
add(f'<path d="M{TX - 120} {TY} C{TX - 180} {TY - 160} {TX - 220} {TY - 280} {TX - 260} {TY - 360} M{TX + 140} {TY} C{TX + 120} {TY - 150} {TX + 60} {TY - 260} {TX - 20} {TY - 330}" '
    'style="fill:none;stroke:var(--bad);stroke-width:6;opacity:.7"/>', when=D('ma'))
text('forefoot turned in, hindfoot normal — crease on the medial border', TX + 20, TY + 100, 'nf-l1 dyn-tag', 'middle', when=D('ma'))
XS = [TX - 100, TX - 40, TX + 20, TX + 70, TX + 115]
for i, x in enumerate(XS):
    add(f'<path d="M{x} {TY - 80} V{TY - 380}" style="stroke:var(--dk6);stroke-width:18;opacity:.35;stroke-linecap:round"/>', unless=D('ma') if True else None)
    add(f'<circle cx="{x}" cy="{TY - 430}" r="20" style="fill:var(--dk6);fill-opacity:.2;stroke:var(--dk6);stroke-width:3"/>', unless=D('ma'))
    text(str(i + 1), x, TY - 60, 'nf-l2', 'middle')
text('medial', TX - 230, TY - 200, 'nf-l2')
add(f'<path d="M{TX - 100} {TY - 80} L{TX - 130} {TY - 380}" style="stroke:var(--bad);stroke-width:18;opacity:.6;stroke-linecap:round"/>', when=D('bunion'))
add(f'<path d="M{TX - 130} {TY - 380} L{TX - 80} {TY - 460}" style="stroke:var(--bad);stroke-width:18;opacity:.6;stroke-linecap:round"/>', when=D('bunion'))
add(f'<circle cx="{TX - 140}" cy="{TY - 380}" r="26" style="fill:var(--bad);fill-opacity:.5"/>', when=D('bunion'))
add(f'<ellipse cx="{TX + 45}" cy="{TY - 390}" rx="16" ry="30" style="fill:var(--dk9);fill-opacity:.8"/>', when=D('morton'))
text('3rd web space — common digital nerve', TX + 45, TY - 500, 'nf-l1 dyn-tag', 'middle', when=D('morton'))
TAG = dict(pf='plantar fasciitis — calcaneal attachment; worst on the first steps in the morning · heel spur is a result, not the cause',
           bursa='retrocalcaneal bursitis — posterior heel, worse with dorsiflexion; with Achilles tendinosis',
           sever='Sever disease — calcaneal apophysitis in running children (boys ~8, girls ~6)',
           morton='Morton neuroma — “pebble in the shoe”, worse in high heels; sensory only',
           bunion='bunion — big toe deviates laterally, 1st metatarsal medially · medial prominence at the MTP',
           ham='hammer toe — MTP extended, PIP flexed, DIP often extended · usually 2nd toe',
           claw='claw toe — MTP hyperextended, PIP and DIP flexed · lateral four toes · neuropathic foot',
           ma='metatarsus adductus — commonest newborn foot deformity; usually corrects by 12–18 months')
for k, s in TAG.items(): text(s, 1000, 1240, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('overnight the foot plantarflexes and the fascia shortens — the first step stretches it', 1000, 1280, 'nf-l1', 'middle', when=['dx:pf&morning'])

# ════════ motion ════════
flows = [
  dict(d='M560 940 C800 950 1100 950 1320 935', len=780, speed=120, r=10, base=dict(load=3)),
  dict(d='M580 935 C780 930 1100 935 1300 935', len=720, speed=60, r=8, base=dict(pain=2), when=['dx:pf&morning']),
  dict(d=f'M{TX + 45} {TY - 390} C{TX + 45} {TY - 430} {TX + 45} {TY - 460} {TX + 45} {TY - 500}', len=110, speed=60, r=8, base=dict(pain=2), when=D('morton')),
]
sites = [dict(x=520, y=950, n=[-1, 1], w=10, t='rec', l='', aria='Plantar fasciitis', c='plantarfasc', ions=[]),
         dict(x=700, y=740, n=[1, -1], w=10, t='rec', l='', aria='Retrocalcaneal bursitis and Sever', c='heelpain', ions=[]),
         dict(x=TX + 140, y=TY - 430, n=[1, 0], w=10, t='rec', l='', aria='Morton neuroma', c='morton', ions=[]),
         dict(x=TX - 180, y=TY - 430, n=[-1, 0], w=10, t='rec', l='', aria='Bunions', c='bunions', ions=[]),
         dict(x=1520, y=860, n=[1, -1], w=10, t='rec', l='', aria='Claw and hammer toe', c='clawtoe', ions=[]),
         dict(x=TX - 180, y=TY - 40, n=[-1, 1], w=10, t='rec', l='', aria='Metatarsus adductus', c='metadduct', ions=[])]

readouts = [
  dict(l='Heel pain', mods=[dict(when=D('pf', 'bursa', 'sever'), d=1)]),
  dict(l='Forefoot pain', mods=[dict(when=D('morton'), d=1)]),
  dict(l='Toe numbness', mods=[dict(when=D('morton'), d=1)]),
  dict(l='Toe or forefoot deformity', mods=[dict(when=D('bunion', 'ham', 'claw', 'ma'), d=1)]),
]

notes = {
  '': 'Weight lands on the heel, rolls through the midfoot and pushes off from the metatarsal heads; the plantar fascia holds '
      'up the arch like a bowstring. Add a problem to see where it hurts or bends.',
  'dx:pf': 'Plantar fasciitis: inflamed calcaneal attachment; over 40, men > women; worst on the first morning steps. NSAIDs, '
           'fascia and Achilles stretches, heel pads, night splints; injection can atrophy the fat pad.',
  'dx:bursa': 'Retrocalcaneal bursitis: between the posterior calcaneus and the Achilles — overuse; tender, swollen, worse with '
              'dorsiflexion; tied to Achilles tendinosis. Often confused with plantar fasciitis.',
  'dx:sever': 'Sever disease: calcaneal apophysitis — Achilles traction at the growth plate from running and jumping; two-thirds '
              'bilateral; lasts 3–4 years; heel cushioning, less activity.',
  'dx:morton': 'Morton neuroma: metatarsal heads rub the common digital nerve, most in the 3rd web space (MT 4 and 5 move together '
               'on the cuboid). Pebble feeling, tingling; wide low shoes, metatarsal pad, injection, resection (sensory only).',
  'dx:bunion': 'Bunion: the proximal phalanx deviates laterally and the 1st metatarsal medially — medial MTP prominence. Wide toe '
               'box; osteotomy if needed.',
  'dx:ham': 'Hammer toe: MTP extended, PIP flexed, DIP often extended, usually the 2nd toe — weak lumbricals and interossei.',
  'dx:claw': 'Claw toe: MTP hyperextended, PIP and DIP flexed, lateral four toes; corns on top, calluses under the heads; the '
             'neuropathic (diabetic) foot; Charcot-Marie-Tooth.',
  'dx:ma': 'Metatarsus adductus: forefoot turned in at the midtarsal apex, hindfoot and ankle dorsiflexion normal (unlike '
           'clubfoot); usually flexible; resolves by 12–18 months; more often with hip dysplasia.',
}

dyn = dict(
  kinds=dict(load=['mov', '--accent'], pain=['mov', '--bad']), groups=[['mov', 'Weight · pain']],
  switches=[dict(id='st', label='Step', type='steps', auto=3, options=[['heel', 'Heel strike'], ['mid', 'Midfoot'], ['push', 'Push-off']]),
            dict(id='dx', label='Problem', type='one', options=[
              ['pf', 'Plantar fasciitis', 'plantarfasc'], ['bursa', 'Retrocalcaneal bursitis', 'heelpain'], ['sever', 'Sever disease', 'heelpain'],
              ['morton', 'Morton neuroma', 'morton'], ['bunion', 'Bunion', 'bunions'], ['ham', 'Hammer toe', 'clawtoe'],
              ['claw', 'Claw toe', 'clawtoe'], ['ma', 'Metatarsus adductus', 'metadduct']]),
            dict(id='morning', label='When', type='toggle', on='First step of the morning', off='First morning step', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='OCOM Ortho SDL 7')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='footsim', title='The Foot in Motion', topic='msk', after='footleg',
  sub='Roll body weight from heel to metatarsal heads, then add plantar fasciitis, heel bursitis, Sever disease, Morton neuroma, '
      'a bunion, hammer or claw toes or metatarsus adductus',
  w=3600, h=1900,
  fa='465, 491, 538, 545',
  src=['OCOM Ortho — SDL 7 lecture: Foot and ankle pain and injury', 'Moore ch 7 — Lower Limb'],
  lanes=[('ftHeel', 'Heel', 'tca'), ('ftFore', 'Forefoot & toes', 'glycolysis')],
  nodes=[
    ('ft1', 'Plantar fasciitis', 330, 1700, 'ftHeel', 'first morning step', ['plantarfasc'], 'hub'),
    ('ft2', 'Heel bursitis & Sever', 760, 1700, 'ftHeel', 'posterior heel', ['heelpain']),
    ('ft3', 'Morton neuroma', 1200, 1700, 'ftFore', '3rd web space', ['morton']),
    ('ft4', 'Bunions, hammertoes & corns', 1640, 1700, 'ftFore', 'medial MTP', ['bunions']),
    ('ft5', 'Claw vs hammer toe', 2080, 1700, 'ftFore', 'MTP · PIP · DIP', ['clawtoe']),
    ('ft6', 'Metatarsus adductus', 2520, 1700, 'ftFore', 'self-correcting', ['metadduct'])],
  panels=[
    (2500, PANY, 1000, 'Toe deformities (OCOM Ortho SDL 7)', [
      ('Claw toe', 'MTP ext · PIP flex · DIP flex'), ('Hammer toe', 'MTP ext · PIP flex · DIP ext'),
      ('Bunion', 'phalanx lateral · 1st MT medial')])],
  dyn=dyn)
