# Sex Differentiation in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The three decisions drawn left to right: (1) gonad — SRY makes a testis, otherwise an ovary (or a streak); (2) internal
# ducts — Sertoli AMH destroys the Müllerian duct, Leydig testosterone keeps the Wolffian duct; (3) external genitalia —
# 5α-reductase makes DHT, which acts on the androgen receptor. Hormone particles flow from the gonad to each target. One
# `one` switch picks the case (typical 46,XY and 46,XX, Swyer, androgen insensitivity, 5α-reductase deficiency,
# persistent Müllerian duct syndrome, 21-hydroxylase CAH in 46,XX, Turner, Klinefelter). 5 readouts. Facts from the
# pinned cards (sexdevreg, swyer, ais, reductase5a, pmds, cah21, turner, klinefelter, ductremnants); FA pages in `fa`.
# No new cards.
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


SW = 'dx'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 760
def X(cx, cy, s=20): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'

text('Sex differentiation — three decisions, three signals', 180, 150, 'dyn-big')
text('a defect at any step leaves the steps before it normal — read the anatomy backwards to find the level', 180, 176, 'dyn-cap')
for x0, x1, t, s in ((160, 700, '1 · Gonad', 'SRY → testis; otherwise ovary'), (740, 1500, '2 · Internal ducts', 'AMH destroys Müllerian · testosterone keeps Wolffian'),
                     (1540, 2340, '3 · External genitalia', 'testosterone → DHT (5α-reductase) → androgen receptor')):
    box(x0, 210, x1, 1150)
    text(t, x0 + 30, 250, 'dyn-big'); text(s, x0 + 30, 276, 'nf-l2')

# ════════ 1 · gonad ════════
KARY = dict(xy='46,XY · SRY present', xx='46,XX · no SRY', swyer='46,XY · SRY fails', ais='46,XY · SRY present', srd='46,XY · SRY present',
            pmds='46,XY · SRY present', cah='46,XX · no SRY', turner='45,X · no SRY', kline='47,XXY · SRY present')
for k, t in KARY.items():
    text(t, 430, 360, 'nf-l1', 'middle', when=O(k))
text('pick a case on the right', 430, 360, 'nf-l1', 'middle', unless=[f'{SW}:*'])
TESTIS, OVARY, STREAK = O('xy', 'ais', 'srd', 'pmds', 'kline'), O('xx', 'cah'), O('swyer', 'turner')
add('<ellipse cx="430" cy="560" rx="120" ry="80" style="fill:var(--dk1);fill-opacity:.25;stroke:var(--dk1);stroke-width:4"/>', when=TESTIS)
text('testis', 430, 566, 'nf-l1', 'middle', when=TESTIS)
text('Sertoli → AMH · Leydig → testosterone', 430, 680, 'nf-l2', 'middle', when=TESTIS)
text('small, firm — tubules fail', 430, 710, 'nf-l1 dyn-tag', 'middle', when=O('kline'))
add('<ellipse cx="430" cy="560" rx="100" ry="60" style="fill:var(--dk8);fill-opacity:.25;stroke:var(--dk8);stroke-width:4"/>', when=OVARY)
text('ovary — the default', 430, 566, 'nf-l1', 'middle', when=OVARY)
add('<path d="M330 560 H530" style="stroke:var(--ink-3);stroke-width:8;stroke-linecap:round"/>', when=STREAK)
text('streak gonad — no AMH, no testosterone, no estrogen', 430, 620, 'nf-l1 dyn-tag', 'middle', when=STREAK)
text('ovary forms, then loses its oocytes', 430, 650, 'nf-l2', 'middle', when=O('turner'))
add('<rect x="280" y="860" width="300" height="110" rx="20" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>', when=O('cah'))
text('adrenal — 21-hydroxylase blocked', 430, 900, 'nf-l1', 'middle', when=O('cah'))
text('precursors shunted to androgens', 430, 926, 'nf-l2', 'middle', when=O('cah'))

# ════════ 2 · ducts ════════
# UNVERIFIED: the Wolffian duct is drawn regressed in androgen insensitivity (no androgen action); the ais card doesn't state it
add('<path d="M800 420 C900 420 1000 560 1120 560 C1240 560 1300 620 1420 620" style="fill:none;stroke:var(--dk1);stroke-width:12;stroke-linecap:round"/>', when=O('xy', 'srd', 'pmds', 'kline'))
add('<path d="M800 420 C900 420 1000 560 1120 560 C1240 560 1300 620 1420 620" style="fill:none;stroke:var(--line-2);stroke-width:6;stroke-dasharray:6 10"/>', unless=O('xy', 'srd', 'pmds', 'kline'))
text('Wolffian (mesonephric) duct', 800, 400, 'nf-l1')
text('→ epididymis, vas deferens, seminal vesicles', 1000, 650, 'nf-l2', when=O('xy', 'srd', 'pmds', 'kline'))
MUL = O('xx', 'swyer', 'pmds', 'cah', 'turner')
add('<path d="M800 820 C900 820 1000 940 1120 940 C1240 940 1300 1000 1420 1000" style="fill:none;stroke:var(--dk8);stroke-width:12;stroke-linecap:round"/>', when=MUL)
add('<path d="M800 820 C900 820 1000 940 1120 940 C1240 940 1300 1000 1420 1000" style="fill:none;stroke:var(--line-2);stroke-width:6;stroke-dasharray:6 10"/>', unless=MUL)
text('Müllerian (paramesonephric) duct', 800, 800, 'nf-l1')
text('→ uterus, tubes, upper vagina', 1000, 1050, 'nf-l2', when=MUL)
text('uterus persists beside male structures', 1000, 1090, 'nf-l1 dyn-tag', when=O('pmds'))
add(X(800, 880), when=O('pmds'))

# ════════ 3 · external ════════
EXT = dict(xy=('Male', 'DHT acts on the androgen receptor'), xx=('Female', 'no androgen — the default'),
           swyer=('Female', 'no testosterone at all'), ais=('Female', 'androgens made but the receptor is missing'),
           srd=('Ambiguous at birth', 'no DHT — masculinizes at puberty'), pmds=('Male', 'fully virilized'),
           cah=('Virilized (ambiguous)', 'adrenal androgens act on a 46,XX fetus'), turner=('Female', 'no testosterone'),
           kline=('Male', 'later: gynecomastia, sparse hair'))
for k, (a, b) in EXT.items():
    text(a, 1940, 560, 'dyn-big', 'middle', when=O(k)); text(b, 1940, 590, 'nf-l2', 'middle', when=O(k))
add('<rect x="1700" y="760" width="480" height="90" rx="20" class="dyn-soft"/>')
text('androgen receptor', 1940, 812, 'nf-l1', 'middle')
add(X(2120, 805), when=O('ais'))
add('<rect x="1700" y="420" width="480" height="70" rx="20" class="dyn-soft"/>')
text('5α-reductase: testosterone → DHT', 1940, 462, 'nf-l1', 'middle')
add(X(2120, 455), when=O('srd'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
T_ON = O('xy', 'ais', 'srd', 'pmds', 'kline')
AMH_ON = O('xy', 'ais', 'srd', 'kline')
flows = [
  dict(d='M550 560 C650 560 700 480 800 440', len=300, speed=90, r=7, base=dict(), when=T_ON, mods=[m(T_ON, set=dict(t=4))]),
  dict(d='M550 590 C650 640 700 780 800 840', len=360, speed=90, r=7, base=dict(), when=O(*['xy', 'ais', 'srd', 'kline', 'pmds']),
       mods=[m(AMH_ON, set=dict(amh=4)), m(O('pmds'), set=dict(amh=1))]),
  dict(d='M550 520 C900 300 1500 300 1700 455', len=1300, speed=140, r=7, base=dict(), when=T_ON, mods=[m(T_ON, set=dict(t=5))]),
  dict(d='M2140 490 V760', len=270, speed=90, r=7, base=dict(), when=O('xy', 'ais', 'pmds', 'kline'), mods=[m(O('xy', 'ais', 'pmds', 'kline'), set=dict(dht=4))]),
  dict(d='M580 915 C900 1120 1500 1120 1700 805', len=1400, speed=140, r=7, base=dict(), when=O('cah'), mods=[m(O('cah'), set=dict(t=6))]),
]
sites = [dict(x=1760, y=760, n=[0, -1], w=40, t='rec', l='', aria='Androgen receptor', c='ais', ions=[]),
         dict(x=1700, y=455, n=[-1, 0], w=40, t='md', l='', aria='5α-reductase', c='reductase5a', ions=[])]

readouts = [
  dict(l='Androgens', mods=[dict(when=O('ais', 'cah'), d=1), dict(when=O('kline'), d=-1), dict(when=O('pmds'), d=0)]),
  dict(l='DHT', mods=[dict(when=O('srd'), d=-1)]),
  dict(l='LH', mods=[dict(when=O('ais', 'swyer', 'turner', 'kline'), d=1)]),
  dict(l='FSH', mods=[dict(when=O('swyer', 'turner', 'kline'), d=1)]),
  dict(l='Estradiol', mods=[dict(when=O('ais', 'kline'), d=1), dict(when=O('swyer', 'turner'), d=-1)]),
]

notes = {
  '': 'Three steps, three signals: SRY makes a testis; the testis’s AMH destroys the Müllerian duct and its testosterone keeps the '
      'Wolffian duct; 5α-reductase turns testosterone into DHT, which masculinizes the external genitalia. With no signal, the '
      'female pattern develops.',
  'dx:xy': 'Typical 46,XY: SRY → testis → AMH regresses the Müllerian duct, testosterone keeps the Wolffian duct, and DHT makes the '
           'external genitalia male.',
  'dx:xx': 'Typical 46,XX: no SRY, so an ovary — no AMH (the Müllerian duct becomes uterus and tubes) and no testosterone (the '
           'Wolffian duct regresses). The female pattern needs no hormone.',
  'dx:swyer': 'Swyer syndrome (46,XY, SRY fails): only a streak gonad, which makes neither AMH nor testosterone — so a uterus and '
              'female genitalia; primary amenorrhea with high FSH and LH at puberty.',
  'dx:ais': 'Androgen insensitivity (46,XY, X-linked receptor defect): testes make AMH (no uterus) and plenty of testosterone that '
            'can’t act — female external genitalia, breasts from aromatization, scant hair; testosterone, estrogen and LH high.',
  'dx:srd': '5α-reductase deficiency (46,XY): testosterone keeps the internal male structures, but without DHT the external '
            'genitalia are ambiguous until puberty masculinizes them. High testosterone-to-DHT ratio.',
  'dx:pmds': 'Persistent Müllerian duct syndrome (46,XY): AMH or its receptor fails, so a fully virilized boy also has a uterus and '
             'tubes — often found at hernia or cryptorchidism surgery.',
  'dx:cah': '21-hydroxylase deficiency in a 46,XX fetus: precursors are shunted to adrenal androgens, which virilize the external '
            'genitalia while the internal organs stay female; salt wasting and high 17-hydroxyprogesterone.',
  'dx:turner': 'Turner syndrome (45,X): the ovaries form but lose their oocytes, leaving streaks; the uterus is normal. Primary '
               'amenorrhea, short stature, high FSH and LH, low estradiol.',
  'dx:kline': 'Klinefelter syndrome (47,XXY): SRY makes a testis, but the tubules fail — small firm testes, infertility, '
              'gynecomastia; FSH rises first, LH rises, testosterone falls, estrogen rises.',
}

dyn = dict(
  kinds=dict(t=['h', '--dk1'], amh=['h', '--dk9'], dht=['h', '--dk11']), groups=[['h', 'Hormones']],
  switches=[dict(id=SW, label='The case', type='one', options=[
    ['xy', 'Typical 46,XY', 'sexdevreg'], ['xx', 'Typical 46,XX', 'sexdevreg'], ['swyer', 'Swyer (46,XY, no SRY)', 'swyer'],
    ['ais', 'Androgen insensitivity', 'ais'], ['srd', '5α-reductase deficiency', 'reductase5a'], ['pmds', 'Persistent Müllerian duct', 'pmds'],
    ['cah', '21-hydroxylase CAH (46,XX)', 'cah21'], ['turner', 'Turner (45,X)', 'turner'], ['kline', 'Klinefelter (47,XXY)', 'klinefelter']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 339, 639–640, 653, 655–656 · Langman ch 16')

MAP = dict(
  id='sexsim', title='Sex Differentiation in Motion', topic='devrepro', after='sexdev',
  sub='SRY makes the gonad, AMH and testosterone sort the ducts, DHT shapes the external genitalia — pick a case (Swyer, androgen '
      'insensitivity, 5α-reductase, PMDS, CAH, Turner, Klinefelter) and watch which signal is missing and what develops',
  w=3500, h=1480,
  fa='339, 353, 639–640, 653, 655–656',
  src=[full('Langman', 16), full('Pawlina', 22)],
  lanes=[('sxGonad', 'Gonad & karyotype', 'glycolysis'), ('sxHorm', 'Hormone signals', 'tca'), ('sxDuct', 'Ducts', 'gluconeo')],
  nodes=[
    ('sx1', 'How sex differentiation runs', 330, 1270, 'sxHorm', 'SRY → AMH + T → DHT', ['sexdevreg'], 'hub'),
    ('sx2', 'Swyer · Turner', 760, 1270, 'sxGonad', 'streak gonads', ['swyer', 'turner']),
    ('sx3', 'Klinefelter', 1160, 1270, 'sxGonad', '47,XXY', ['klinefelter']),
    ('sx4', 'Androgen insensitivity', 1560, 1270, 'sxHorm', 'no receptor', ['ais']),
    ('sx5', '5α-reductase deficiency', 1990, 1270, 'sxHorm', 'no DHT', ['reductase5a']),
    ('sx6', 'Persistent Müllerian duct', 330, 1400, 'sxDuct', 'no AMH effect', ['pmds', 'ductremnants']),
    ('sx7', '21-hydroxylase deficiency', 780, 1400, 'sxHorm', 'adrenal androgens', ['cah21'])],
  panels=[
    (2420, PANY, 1000, 'Read it backwards (sex differentiation card)', [
      ('Uterus present', 'AMH never acted — no testis, or AMH failed'),
      ('No uterus, female outside', 'AMH worked, androgen didn’t'),
      ('Male inside, female outside', 'testosterone → DHT failed')])],
  dyn=dyn)
