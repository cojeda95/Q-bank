# Pneumonia in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# An airway with the mucociliary escalator carrying trapped particles up, alveoli with macrophages, and a lobe that passes
# through the four stages of lobar pneumonia (`st` steps, auto): congestion → red hepatization → gray hepatization →
# resolution, with the exudate changing. A `one` switch breaks a defense (lost cough reflex → aspiration, smoking/viral
# ciliary damage, impaired macrophages, retained secretions) or shows mycoplasma attachment and a right-sided aspiration
# abscess. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
S = lambda *k: [f'st:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'

text('Pneumonia — the defenses, the stages, and how they fail', 180, 150, 'dyn-big')
text('left: airway and alveoli · right: one lobe through the four stages of lobar pneumonia', 180, 176, 'dyn-cap')

# ════════ airway ════════
add('<path d="M400 260 V900" style="stroke:var(--dk3);stroke-width:120;opacity:.15;stroke-linecap:round"/>')
add('<path d="M340 260 V900" style="stroke:var(--dk5);stroke-width:14"/>'); text('mucous blanket on cilia', 300, 600, 'nf-l2', 'end')
for y in range(300, 900, 40):
    add(f'<path d="M352 {y} l18 -14" style="stroke:var(--dk7);stroke-width:4"/>', unless=D('cilia'))
    add(f'<path d="M352 {y} l18 4" style="stroke:var(--ink-3);stroke-width:4"/>', when=D('cilia'))
text('airway', 400, 240, 'nf-l1', 'middle')
add('<path d="M340 600 h-20" style="stroke:var(--dk5);stroke-width:30"/>', when=D('retain'))
text('mucus plug — CF, bronchial obstruction', 620, 1280, 'nf-l1 dyn-tag', 'middle', when=D('retain'))
text('cilia damaged — smoke, viral infection, immotile cilia', 620, 1280, 'nf-l1 dyn-tag', 'middle', when=D('cilia'))
# alveoli
for (x, y) in ((560, 1000), (720, 1080), (560, 1160)):
    add(f'<circle cx="{x}" cy="{y}" r="70" style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:3"/>')
add('<path d="M400 900 C420 960 480 990 500 1000" style="fill:none;stroke:var(--dk3);stroke-width:30;opacity:.15"/>')
add('<circle cx="720" cy="1080" r="26" style="fill:var(--dk4);fill-opacity:.5;stroke:var(--dk4);stroke-width:3"/>', unless=D('macro'))
add('<circle cx="720" cy="1080" r="26" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:5 5"/>', when=D('macro'))
text('alveolar macrophage', 820, 1086, 'nf-l2')
text('macrophages impaired — alcohol, smoke, anoxia, O₂ toxicity', 620, 1280, 'nf-l1 dyn-tag', 'middle', when=D('macro'))
text('no cough or gag — gastric contents aspirated', 620, 1280, 'nf-l1 dyn-tag', 'middle', when=D('asp'))
text('P1 adhesin grips the epithelium — escapes clearance', 620, 1280, 'nf-l1 dyn-tag', 'middle', when=D('myco'))
for y in (420, 520, 640): add(f'<ellipse cx="368" cy="{y}" rx="10" ry="6" style="fill:var(--bad)"/>', when=D('myco'))

# ════════ lobe through the stages ════════
LX, LY = 1600, 700
LOBE = f'M{LX - 380} {LY - 300} C{LX - 100} {LY - 420} {LX + 300} {LY - 360} {LX + 380} {LY - 100} C{LX + 420} {LY + 200} {LX + 200} {LY + 360} {LX - 100} {LY + 340} C{LX - 380} {LY + 300} {LX - 460} {LY} {LX - 380} {LY - 300} Z'
add(f'<path d="{LOBE}" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:5"/>', unless=['st:*'])
FILL = dict(cong=('--nf-blood', .25), red=('--nf-blood', .6), gray=('--ink-3', .5), res=('--dk2', .08))
for k, (c, o) in FILL.items():
    add(f'<path d="{LOBE}" style="fill:var({c});fill-opacity:{o};stroke:var(--dk2);stroke-width:5"/>', when=S(k))
text('one lobe', LX, LY - 420, 'nf-l1', 'middle')
ST = dict(cong=('Congestion — days 1–2', 'heavy, boggy, red; edema fluid, few neutrophils, many bacteria'),
          red=('Red hepatization — days 3–4', 'neutrophils, red cells and fibrin fill the alveoli; firm, airless, liver-like'),
          gray=('Gray hepatization — days 5–7', 'red cells break down; fibrinosuppurative exudate persists — grayish-brown'),
          res=('Resolution — day 8+', 'exudate digested, resorbed, eaten by macrophages, coughed up'))
for k, (a, b) in ST.items():
    text(a, LX, LY + 440, 'nf-l1 dyn-tag', 'middle', when=S(k)); text(b, LX, LY + 472, 'nf-l2', 'middle', when=S(k))
# abscess on the right lung
add('<circle cx="1050" cy="1150" r="70" style="fill:var(--dk10);fill-opacity:.4;stroke:var(--bad);stroke-width:5"/>', when=D('abscess'))
text('aspiration abscess — usually right-sided and single (right main bronchus more vertical)', 1500, 1300, 'nf-l1 dyn-tag', 'middle', when=D('abscess'))
text('oral anaerobes: Bacteroides, Fusobacterium, Peptococcus — clindamycin', 1500, 1330, 'nf-l2', 'middle', when=D('abscess'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M360 900 V270', len=630, speed=90, r=9, base=dict(par=4), mods=[m(D('cilia', 'retain'), set=dict(par=1), speed=0.2)]),
  dict(d='M400 260 V900 C420 960 480 990 560 1000', len=800, speed=140, r=8, base=dict(bug=1), mods=[m(D('asp', 'cilia', 'retain', 'macro'), set=dict(bug=5))]),
  dict(d='M560 1000 C620 1020 680 1050 700 1070', len=170, speed=60, r=8, base=dict(bug=2), unless=D('macro')),
  dict(d=f'M{LX - 300} {LY} C{LX - 100} {LY - 200} {LX + 100} {LY + 200} {LX + 300} {LY}', len=700, speed=100, r=9, base=dict(neu=2),
       mods=[m(S('red', 'gray'), set=dict(neu=7)), m(S('res'), set=dict(neu=1))], when=['st:*']),
]
sites = [dict(x=340, y=260, n=[-1, 0], w=10, t='rec', l='', aria='Lung defenses', c='lungdefense', ions=[]),
         dict(x=LX, y=LY - 300, n=[0, -1], w=10, t='rec', l='', aria='Lobar pneumonia stages', c='lobarstages', ions=[]),
         dict(x=1050, y=1080, n=[0, -1], w=10, t='rec', l='', aria='Lung abscess', c='lungabscess', ions=[]),
         dict(x=400, y=1000, n=[0, 1], w=10, t='rec', l='', aria='Mycoplasma', c='mycolab', ions=[])]

readouts = [
  dict(l='Clearance', mods=[dict(when=D('cilia', 'retain', 'macro', 'asp', 'myco'), d=-1)]),
  dict(l='Lobe airless (consolidated)', mods=[dict(when=S('red', 'gray'), d=1), dict(when=S('res'), d=-1)]),
  dict(l='Neutrophils in alveoli', mods=[dict(when=S('red', 'gray'), d=1)]),
  dict(l='Gram stain helps', mods=[dict(when=D('myco'), d=-1)]),
]

notes = {
  '': 'Inhaled microbes are trapped in the mucous blanket and swept up the mucociliary escalator; those reaching the alveoli are eaten by '
      'alveolar macrophages, which carry them up or call in neutrophils. Pneumonia follows when these defenses fail.',
  'st:cong': 'Congestion (days 1–2): vascular engorgement, intra-alveolar edema, a few neutrophils and many bacteria.',
  'st:red': 'Red hepatization (days 3–4): neutrophils, red cells and fibrin fill the alveoli — red, firm, airless, liver-like.',
  'st:gray': 'Gray hepatization (days 5–7): red cells disintegrate, the fibrinosuppurative exudate persists.',
  'st:res': 'Resolution (day 8+): the exudate is digested, resorbed, eaten by macrophages or coughed up.',
  'dx:asp': 'Lost cough reflex (coma, anesthesia, neuromuscular disease, drugs, chest pain) → aspiration of gastric contents.',
  'dx:cilia': 'Mucociliary dysfunction: cigarette smoke, hot or corrosive gases, viral infection, immotile cilia. Viral damage to ciliated '
              'epithelium opens the way for S aureus after influenza or measles.',
  'dx:macro': 'Impaired alveolar macrophages: alcohol, tobacco smoke, anoxia, oxygen toxicity.',
  'dx:retain': 'Retained secretions: cystic fibrosis, bronchial obstruction.',
  'dx:myco': 'Mycoplasma: no cell wall (invisible on Gram stain, untouched by β-lactams); the P1 adhesin binds respiratory epithelium and '
             'protects it from clearance; cilia deteriorate. Macrolide, tetracycline or fluoroquinolone.',
  'dx:abscess': 'Lung abscess: suppurative necrosis, most often from aspiration with a depressed cough or gag — usually right-sided and '
                'single; oral anaerobes. Clindamycin, drain if needed.',
}

dyn = dict(
  kinds=dict(par=['mov', '--dk5'], bug=['mov', '--bad'], neu=['mov', '--dk4']), groups=[['mov', 'Particles · bacteria · neutrophils']],
  switches=[dict(id='st', label='Lobar stage', type='steps', auto=3, options=[
              ['cong', 'Congestion'], ['red', 'Red hepatization'], ['gray', 'Gray hepatization'], ['res', 'Resolution']]),
            dict(id='dx', label='Defense fails', type='one', options=[
              ['asp', 'No cough reflex (aspiration)', 'lungdefense'], ['cilia', 'Cilia damaged', 'lungdefense'],
              ['macro', 'Macrophages impaired', 'lungdefense'], ['retain', 'Retained secretions', 'lungdefense'],
              ['myco', 'Mycoplasma attachment', 'mycolab'], ['abscess', 'Aspiration abscess', 'lungabscess']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 15')

MAP = dict(
  id='pnasim', title='Pneumonia in Motion', topic='pulmo', after='respinf',
  sub='Watch the mucociliary escalator and macrophages clear the lung, break each defense, and step a lobe through congestion, red and '
      'gray hepatization and resolution — plus mycoplasma and a right-sided aspiration abscess',
  w=3600, h=1900,
  fa='125, 134, 148, 188, 680, 702',
  src=['Robbins ch 15 — The lung'],
  lanes=[('pnDef', 'Defenses', 'glycolysis'), ('pnDz', 'Pneumonia', 'tca')],
  nodes=[
    ('pn1', 'Lung host defenses', 330, 1660, 'pnDef', 'escalator · macrophages', ['lungdefense'], 'hub'),
    ('pn2', 'Pneumococcal carriage', 760, 1660, 'pnDef', '20% of adults', ['pneumocarriage']),
    ('pn3', 'Lobar pneumonia stages', 1200, 1660, 'pnDz', 'red → gray hepatization', ['lobarstages']),
    ('pn4', 'Lung abscess', 1640, 1660, 'pnDz', 'right, single, anaerobes', ['lungabscess']),
    ('pn5', 'Mycoplasma', 2080, 1660, 'pnDz', 'no wall · P1', ['mycolab'])],
  panels=[
    (2500, PANY, 1000, 'Lobar pneumonia by day (Robbins ch 15)', [
      ('Days 1–2', 'congestion'), ('Days 3–4', 'red hepatization'), ('Days 5–7', 'gray hepatization'), ('Day 8+', 'resolution')])],
  dyn=dyn)
