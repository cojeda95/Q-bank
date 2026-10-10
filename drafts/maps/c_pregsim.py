# Pregnancy Hormones in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Top: a 40-week chart of hCG, progesterone and estriol with a cursor at the current stage (a `steps` switch, auto):
# implantation → hCG peak and corpus luteum rescue → the luteal–placental shift → delivery and lactation. Bottom: the
# corpus luteum, the placenta and the fetus, with the hormones flowing between them — hCG to the corpus luteum, and the
# fetoplacental unit making estriol. A `one` switch redraws hCG and estriol for ectopic pregnancy, hydatidiform mole,
# twins, trisomy 21 and trisomy 18. The curves are schematic (the cards give timing and direction, not values).
# 3 readouts. Facts from the pinned cards (hcghpl, lutealshift, fpunit, p4preg, lactphys, ectopic, gtd); FA pages in
# `fa`. No new cards.
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


ST = 'wk'
S = lambda *k: [f'{ST}:{x}' for x in k]
D = lambda *k: [f'dx:{x}' for x in k]
PANY = 780

# ════════ the 40-week chart ════════
box(160, 130, 2340, 760)
text('Forty weeks of hormones', 190, 170, 'dyn-big')
text('schematic curves: the cards give timing and direction, not concentrations', 190, 196, 'dyn-cap')
CX0, CX1, CY0, CY1 = 320, 2240, 260, 680
wx = lambda w: round(CX0 + (CX1 - CX0) * w / 40)
cy = lambda v: round(CY1 - (CY1 - CY0) * v)
add(f'<path d="M{CX0} {CY0 - 10} V{CY1} H{CX1}" class="dyn-line"/>')
for w in range(0, 41, 4):
    text(str(w), wx(w), CY1 + 30, 'nf-l2', 'middle')
text('weeks', CX1, CY1 + 56, 'nf-l2', 'end')
def curve(f, w0=0, w1=40):
    return 'M' + ' L'.join(f'{wx(w / 4)} {cy(f(w / 4))}' for w in range(int(w0 * 4), int(w1 * 4) + 1))
import math
def hcg(w, k=1.0, late=0.28):
    if w < 1.5: return 0
    if w <= 9: return k * (0.95 * ((w - 1.5) / 7.5) ** 1.6)
    if w <= 18: return k * (0.95 - (0.95 - late) * (w - 9) / 9)
    return k * late
prog = lambda w: 0.1 + 0.75 * (w / 40) ** 1.3
estr = lambda w, k=1.0: k * 0.85 * (w / 40) ** 2
add(f'<path d="{curve(lambda w: hcg(w))}" style="fill:none;stroke:var(--dk9);stroke-width:5"/>', unless=D('mole', 'ect', 'twin', 't21', 't18'))
add(f'<path d="{curve(lambda w: hcg(w, 0.55, 0.15), 0, 8)}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=D('ect'))
add(f'<path d="{curve(lambda w: min(1.0, hcg(w, 1.6, 0.6)), 0, 20)}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=D('mole'))
add(f'<path d="{curve(lambda w: min(1.0, hcg(w, 1.25, 0.36)))}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=D('twin', 't21'))
add(f'<path d="{curve(lambda w: hcg(w, 0.7, 0.18))}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:12 6"/>', when=D('t18'))
add(f'<path d="{curve(lambda w: hcg(w))}" style="fill:none;stroke:var(--dk9);stroke-width:3;opacity:.4"/>', when=D('mole', 'ect', 'twin', 't21', 't18'))
add(f'<path d="{curve(prog, 2, 40)}" style="fill:none;stroke:var(--dk3);stroke-width:5"/>', unless=D('ect', 'mole'))
add(f'<path d="{curve(estr, 2, 40)}" style="fill:none;stroke:var(--dk8);stroke-width:5"/>', unless=D('t21', 't18', 'ect', 'mole'))
add(f'<path d="{curve(lambda w: estr(w, 0.6), 2, 40)}" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:4 6"/>', when=D('t21', 't18'))
text('hCG', wx(9), cy(0.95) - 14, 'nf-l1', 'middle')
text('progesterone', wx(36), cy(prog(36)) - 16, 'nf-l1', 'middle', unless=D('ect', 'mole'))
text('estriol', wx(38), cy(estr(38)) + 34, 'nf-l1', 'middle', unless=D('ect', 'mole'))
DXT = dict(ect='ectopic: hCG rises less than expected — no intrauterine pregnancy', mole='mole: hCG very high, uterus larger than dates',
           twin='twins: hCG higher', t21='trisomy 21: hCG ↑, estriol ↓', t18='trisomy 18: hCG ↓, estriol ↓')
for k, t in DXT.items():
    text(t, 1240, 236, 'nf-l1 dyn-tag', 'middle', when=D(k))
# the cursor
for k, w in (('imp', 3), ('peak', 9), ('shift', 16), ('term', 40)):
    add(f'<path d="M{wx(w)} {CY0 - 20} V{CY1}" style="stroke:var(--accent);stroke-width:4;stroke-dasharray:8 6"/>', when=S(k))

# ════════ who makes what ════════
box(160, 800, 2340, 1380)
text('Who makes what', 190, 840, 'dyn-big')
add('<ellipse cx="420" cy="1060" rx="150" ry="100" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3"/>')
text('Ovary', 420, 940, 'nf-l1', 'middle')
add('<circle cx="420" cy="1060" r="60" style="fill:var(--dk5);fill-opacity:.55"/>', when=S('imp'))
add('<circle cx="420" cy="1060" r="85" style="fill:var(--dk5);fill-opacity:.65"/>', when=S('peak'))
add('<circle cx="420" cy="1060" r="40" style="fill:var(--dk5);fill-opacity:.25"/>', when=S('shift', 'term'))
text('corpus luteum', 420, 1066, 'nf-l2', 'middle')
add('<path d="M800 1160 C900 940 1300 940 1420 1160 Z" style="fill:var(--dk11);fill-opacity:.18;stroke:var(--dk11);stroke-width:3"/>', unless=S('term'))
text('Placenta (syncytiotrophoblast)', 1110, 1210, 'nf-l1', 'middle', unless=S('term'))
text('placenta delivered', 1110, 1060, 'nf-l1 dyn-tag', 'middle', when=S('term'))
add('<rect x="1640" y="900" width="560" height="300" rx="60" class="dyn-cell"/>')
text('Fetus', 1920, 940, 'nf-l1', 'middle')
add('<rect x="1700" y="980" width="200" height="80" rx="20" class="dyn-soft"/><rect x="1940" y="980" width="200" height="80" rx="20" class="dyn-soft"/>')
text('adrenal: DHEA-S', 1800, 1026, 'nf-l2', 'middle'); text('liver: 16-OH', 2040, 1026, 'nf-l2', 'middle')
STEP = dict(imp='hCG appears 8–9 days after ovulation and rescues the corpus luteum',
            peak='hCG peaks (about weeks 8–10); the corpus luteum makes the progesterone',
            shift='the placenta takes over progesterone; estriol needs the fetus too',
            term='estrogen and progesterone fall → prolactin → milk; suckling → oxytocin')
for k, t in STEP.items():
    text(t, 190, 1350, 'nf-l1', when=S(k))

def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M820 1080 C700 1080 600 1060 505 1060', len=330, speed=90, r=7, base=dict(), when=S('imp', 'peak'), mods=[m(S('imp'), set=dict(hcg=3)), m(S('peak'), set=dict(hcg=6))]),
  dict(d='M1110 1000 C1300 860 1600 900 1700 1020 H1940 C2000 1150 1500 1250 1300 1150', len=1500, speed=130, r=7, base=dict(),
       when=S('shift'), mods=[m(S('shift'), set=dict(e3=6))]),
  dict(d='M1110 990 V860', len=130, speed=60, r=7, base=dict(), when=S('shift'), mods=[m(S('shift'), set=dict(p4=4))]),
  dict(d='M420 1000 V860', len=140, speed=60, r=7, base=dict(), when=S('imp', 'peak'), mods=[m(S('imp', 'peak'), set=dict(p4=3))]),
]
sites = [dict(x=1110, y=1000, n=[0, -1], w=20, t='rec', l='', aria='Placenta — hCG and hPL', c='hcghpl', ions=[]),
         dict(x=1800, y=980, n=[0, -1], w=20, t='rec', l='', aria='Fetoplacental unit', c='fpunit', ions=[])]

readouts = [
  dict(l='hCG for dates', mods=[dict(when=D('mole', 'twin', 't21'), d=1), dict(when=D('ect', 't18'), d=-1)]),
  dict(l='Estriol', mods=[dict(when=D('t21', 't18'), d=-1)]),
  dict(l='Uterus size for dates', mods=[dict(when=D('mole'), d=1)]),
]

notes = {
  '': 'hCG from the syncytiotrophoblast keeps the corpus luteum making progesterone until the placenta can; estriol needs mother, '
      'placenta and fetus together. Step through the weeks, then compare an abnormal pregnancy.',
  'wk:imp': 'Implantation: the syncytiotrophoblast secretes hCG, measurable 8–9 days after ovulation — the basis of pregnancy tests. '
            'hCG acts like LH and rescues the corpus luteum.',
  'wk:peak': 'hCG peaks late in the first trimester (about weeks 8–10); the rescued corpus luteum doubles in size and keeps making '
             'progesterone and estrogen. Removing it before about week 7 almost always ends the pregnancy.',
  'wk:shift': 'The luteal–placental shift: hCG falls to a plateau by weeks 16–20, the placenta makes progesterone from maternal '
              'cholesterol, and estriol comes from the fetal adrenal (DHEA-S) and liver (16-OH) through the placenta.',
  'wk:term': 'After the placenta is delivered, estrogen and progesterone fall, prolactin is disinhibited and milk production '
             'starts; suckling raises prolactin and oxytocin (letdown and uterine contraction).',
  'dx:ect': 'Ectopic pregnancy: hCG rises less than expected and ultrasound shows no intrauterine pregnancy — amenorrhea, then '
            'bleeding or pain; rupture brings shock.',
  'dx:mole': 'Hydatidiform mole: very high hCG — uterus larger than dates, hyperemesis, early preeclampsia, hyperthyroidism (hCG '
             'resembles TSH), theca-lutein cysts; snowstorm on ultrasound.',
  'dx:twin': 'Multifetal gestation raises hCG.',
  'dx:t21': 'Down syndrome (trisomy 21) on second-trimester screening: hCG high, estriol low.',
  'dx:t18': 'Edwards syndrome (trisomy 18): hCG and estriol both low.',
}

dyn = dict(
  kinds=dict(hcg=['h', '--dk9'], p4=['h', '--dk3'], e3=['h', '--dk8']), groups=[['h', 'Hormones']],
  switches=[dict(id=ST, label='Stage', type='steps', auto=4, options=[['imp', 'Weeks 2–4 · implantation'], ['peak', 'Weeks 8–10 · hCG peak'],
                                                                         ['shift', 'Weeks 12–20 · placenta takes over'], ['term', 'Delivery · lactation']]),
            dict(id='dx', label='Compare', type='one', options=[['ect', 'Ectopic pregnancy', 'ectopic'], ['mole', 'Hydatidiform mole', 'gtd'],
                                                                ['twin', 'Twins', 'hcghpl'], ['t21', 'Trisomy 21', 'fpunit'], ['t18', 'Trisomy 18', 'hcghpl']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 648, 651–653, 658–659 · Costanzo ch 10 · Guyton ch 83')

MAP = dict(
  id='pregsim', title='Pregnancy Hormones in Motion', topic='devrepro', after='placenta',
  sub='Step through pregnancy — hCG rescuing the corpus luteum, the placenta taking over, estriol from the fetoplacental unit, '
      'delivery and lactation — then compare ectopic pregnancy, a mole, twins and trisomies 21 and 18',
  w=3500, h=1700,
  fa='61, 648, 651–653, 658–659',
  src=[full('Costanzo', 10), full('Guyton', 83)],
  lanes=[('pzHorm', 'Hormones', 'glycolysis'), ('pzDz', 'When it goes wrong', 'tca'), ('pzAfter', 'After delivery', 'gluconeo')],
  nodes=[
    ('pg1', 'hCG & hPL', 330, 1480, 'pzHorm', 'syncytiotrophoblast', ['hcghpl'], 'hub'),
    ('pg2', 'Corpus luteum rescue', 760, 1480, 'pzHorm', 'the luteal–placental shift', ['lutealshift']),
    ('pg3', 'Fetoplacental unit', 1180, 1480, 'pzHorm', 'estriol', ['fpunit']),
    ('pg4', 'Progesterone in pregnancy', 1620, 1480, 'pzHorm', 'quiets the uterus', ['p4preg']),
    ('pg5', 'Ectopic pregnancy', 330, 1610, 'pzDz', 'hCG too low', ['ectopic']),
    ('pg6', 'Molar pregnancy', 800, 1610, 'pzDz', 'hCG very high', ['gtd']),
    ('pg7', 'Lactation', 1280, 1610, 'pzAfter', 'prolactin · oxytocin', ['lactphys', 'posteriorpit'])],
  panels=[
    (2420, PANY, 1000, 'hCG (First Aid p. 652)', [
      ('↑ hCG', 'multiple gestation, mole, choriocarcinoma, Down syndrome'),
      ('↓ hCG', 'ectopic or failing pregnancy, Edwards, Patau'),
      ('Peak', 'late first trimester, about weeks 8–10'),
      ('Quad screen', 'hCG, inhibin A, estriol, AFP')])],
  dyn=dyn)
