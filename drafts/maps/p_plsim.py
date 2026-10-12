# Pleural Fluid in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The pleural space between lung and chest wall, with a capillary on one side and a lymphatic draining it. A `mech` switch
# picks one of the five ways fluid collects — raised hydrostatic pressure (heart failure), leaky vessels (pneumonia), low oncotic
# pressure (nephrotic syndrome), stronger negative pressure (atelectasis), blocked lymph (mediastinal carcinomatosis) — and an
# `fl` switch shows what fills the space: clear transudate, blood, chyle, pus or a tumor-laden effusion.
# Schematic. 7 readouts. Robbins ch 15 + Guyton ch 39; FA 698–699 (Light's criteria, exam signs). No new cards.
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

M = lambda *k: [f'mech:{x}' for x in k]
F = lambda *k: [f'fl:{x}' for x in k]
PANY = 1180
LX, SX, WX = 500, 1000, 1500     # lung edge · pleural space centre · chest wall
TOP, BOT = 300, 1300

text('Pleural fluid — five ways in, and what the fluid tells you', 180, 150, 'dyn-big')
text('lung on the left, chest wall on the right, the pleural space between · normally ≤ 15 mL of clear fluid · schematic', 180, 176, 'dyn-cap')
add(f'<rect x="200" y="{TOP}" width="{LX - 200}" height="{BOT - TOP}" rx="40" style="fill:var(--dk11);fill-opacity:.08;stroke:var(--dk11);stroke-width:4"/>')
text('lung', 350, TOP - 20, 'nf-l1', 'middle')
add(f'<path d="M{LX} {TOP} V{BOT}" style="stroke:var(--dk11);stroke-width:8"/>'); text('visceral pleura', LX + 20, TOP + 30, 'nf-l2')
add(f'<path d="M{WX} {TOP} V{BOT}" style="stroke:var(--dk5);stroke-width:8"/>'); text('parietal pleura', WX - 20, TOP + 30, 'nf-l2', 'end')
add(f'<rect x="{WX}" y="{TOP}" width="400" height="{BOT - TOP}" style="fill:var(--dk5);fill-opacity:.08"/>')
text('chest wall', WX + 200, TOP - 20, 'nf-l1', 'middle')
# capillary and lymphatic in the chest wall
add(f'<path d="M{WX + 120} {TOP + 60} V{BOT - 400}" style="stroke:var(--nf-blood);stroke-width:40;opacity:.3;stroke-linecap:round"/>')
text('capillary', WX + 160, TOP + 80, 'nf-l2')
add(f'<path d="M{WX + 260} {BOT - 300} V{BOT}" style="stroke:var(--dk7);stroke-width:30;opacity:.3;stroke-linecap:round"/>')
text('lymphatic → thoracic duct', WX + 300, BOT - 20, 'nf-l2')
add(f'<circle cx="{WX + 30}" cy="{BOT - 220}" r="20" style="fill:none;stroke:var(--dk7);stroke-width:4"/>'); text('stoma', WX + 60, BOT - 260, 'nf-l2')
# fluid level: tiny normally, rises with any mechanism or fluid
add(f'<rect x="{LX + 4}" y="{BOT - 30}" width="{WX - LX - 8}" height="26" style="fill:var(--nf-h2o);opacity:.25"/>', when=['!mech:*&!fl:*'])
COL = dict(hy=('--nf-h2o', .35), he=('--nf-blood', .55), ch=('--surface-2', .95), em=('--dk10', .45), mt=('--nf-blood', .3))
add(f'<rect x="{LX + 4}" y="{BOT - 500}" width="{WX - LX - 8}" height="496" style="fill:var(--nf-h2o);opacity:.35"/>', when=['mech:*&!fl:*'])
for k, (c, o) in COL.items():
    add(f'<rect x="{LX + 4}" y="{BOT - 500}" width="{WX - LX - 8}" height="496" style="fill:var({c});opacity:{o};stroke:var(--line-2);stroke-width:3"/>', when=F(k))
text('meniscus', SX, BOT - 520, 'nf-l2', 'middle', when=['mech:*', 'fl:*'])
# details per fluid
for x, y in ((700, BOT - 300), (900, BOT - 200), (1150, BOT - 380), (1300, BOT - 150), (800, BOT - 420)):
    add(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--dk10);opacity:.9"/>', when=F('em'))
    add(f'<circle cx="{x}" cy="{y}" r="18" style="fill:var(--bad);opacity:.6;stroke:var(--ink);stroke-width:2"/>', when=F('mt'))
add(f'<path d="M{LX + 4} {BOT - 470} C{SX - 200} {BOT - 380} {SX + 200} {BOT - 420} {WX - 4} {BOT - 470} M{LX + 4} {BOT - 260} C{SX} {BOT - 180} {SX} {BOT - 320} {WX - 4} {BOT - 240}" '
    'style="fill:none;stroke:var(--dk10);stroke-width:8;opacity:.8"/>', when=F('em'))
text('loculated · walled off by fibrosis', SX, BOT - 560, 'nf-l1', 'middle', when=F('em'))
# mechanism visuals
add(f'<path d="M{WX + 120} {TOP + 60} V{BOT - 400}" style="stroke:var(--nf-blood);stroke-width:70;opacity:.4;stroke-linecap:round"/>', when=M('hf'))
for y in (TOP + 200, TOP + 400, TOP + 600):
    add(f'<path d="M{WX + 100} {y} h-30 m60 0 h-10" style="stroke:var(--bad);stroke-width:8"/>', when=M('pna'))
add(f'<path d="M{WX + 260} {BOT - 300} V{BOT}" style="stroke:var(--bad);stroke-width:12;stroke-dasharray:18 12"/>', when=M('ly'))
add(f'<rect x="200" y="{TOP + 300}" width="{LX - 200}" height="400" rx="40" style="fill:var(--dk11);fill-opacity:.35"/>', when=M('at'))
text('collapsed lung', 350, TOP + 520, 'nf-l1', 'middle', when=M('at'))
MTAG = dict(hf='↑ hydrostatic pressure — heart failure (with pulmonary congestion) → transudate',
            pna='↑ vascular permeability — pneumonia and other inflammation → exudate',
            ne='↓ plasma oncotic pressure — nephrotic syndrome, cirrhosis, renal failure → transudate',
            at='↑ negative intrapleural pressure — atelectasis pulls fluid in',
            ly='↓ lymphatic drainage — mediastinal carcinomatosis')
for k, s in MTAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=M(k))
FTAG = dict(hy='hydrothorax — clear straw-colored, noninflammatory (heart failure, renal failure, cirrhosis)',
            he='hemothorax — blood: trauma, surgery, ruptured aortic aneurysm (almost always fatal)',
            ch='chylothorax — milky lymph rich in fat: thoracic duct trauma or a tumor blocking a major lymphatic',
            em='empyema — yellow-green pus, usually spread from the lung; organizes into adhesions that can encase the lung',
            mt='malignant effusion — lung and breast metastases: serous or bloody, tumor cells on cytology')
for k, s in FTAG.items(): text(s, 1100, 1520, 'nf-l1', 'middle', when=F(k))

# ════════ motion ════════
def leak(y, n, when, sp=90):
    return dict(d=f'M{WX + 100} {y} C{WX + 20} {y} {WX - 100} {y + 80} {WX - 200} {y + 300}', len=450, speed=sp, r=8, base=dict(h2o=n), when=when)
flows = [leak(TOP + 300, 1, ['!mech:*']), leak(TOP + 300, 3, M('hf', 'ne', 'at'), 120), leak(TOP + 500, 3, M('hf', 'at')),
         leak(TOP + 400, 3, M('pna')),
         dict(d=f'M{WX + 120} {TOP + 450} C{WX + 40} {TOP + 450} {WX - 80} {TOP + 520} {WX - 160} {TOP + 700}', len=450, speed=80, r=9,
              base=dict(prot=3), when=M('pna')),
         dict(d=f'M{WX - 200} {BOT - 100} C{WX - 100} {BOT - 200} {WX} {BOT - 220} {WX + 260} {BOT - 280} V{BOT}', len=700, speed=110, r=8,
              base=dict(h2o=2), when=['!mech:ly']),
         dict(d=f'M{WX + 120} {TOP + 60} V{BOT - 400}', len=640, speed=140, r=8, base=dict(rbc=3))]
sites = [dict(x=WX - 120, y=TOP + 180, n=[-1, -1], w=10, t='rec', l='', aria='Why pleural fluid collects', c='effmech', ions=[]),
         dict(x=SX - 250, y=BOT - 640, n=[-1, -1], w=10, t='rec', l='', aria='Inflammatory pleuritis & empyema', c='pleuritis', ions=[]),
         dict(x=SX + 250, y=BOT - 640, n=[1, -1], w=10, t='rec', l='', aria='Hydrothorax, hemothorax & chylothorax', c='hydrothorax', ions=[])]

readouts = [
  dict(l='Capillary hydrostatic pressure', mods=[dict(when=M('hf'), d=1)]),
  dict(l='Capillary permeability', mods=[dict(when=M('pna'), d=1)]),
  dict(l='Plasma oncotic pressure', mods=[dict(when=M('ne'), d=-1)]),
  dict(l='Lymph drainage', mods=[dict(when=M('ly'), d=-1)]),
  dict(l='Pleural fluid', mods=[dict(when=['mech:*', 'fl:*'], d=1)]),
  dict(l='Tactile fremitus · breath sounds', mods=[dict(when=['mech:*', 'fl:*'], d=-1)]),
  dict(l="Light's ratios (protein, LDH)", mods=[dict(when=M('hf', 'ne'), d=0), dict(when=M('pna') + F('em', 'mt', 'ch'), d=1)]),
]

notes = {
  '': 'Normally no more than 15 mL of clear serous fluid lubricates the pleura; lymphatics opening on the parietal pleura drain any excess. '
      'It collects when the balance tips: more pushed out of capillaries, more leaking through them, less held back by plasma proteins, '
      'more sucked in, or less drained by lymph. Any effusion: dull percussion, ↓ breath sounds and ↓ tactile fremitus.',
  'mech:hf': 'Heart failure raises hydrostatic pressure — the commonest cause of hydrothorax, usually with pulmonary congestion. Pressure '
             'and oncotic causes give transudates (clear, hypocellular; Light’s ratios not raised).',
  'mech:pna': 'Inflammation (pneumonia, TB, infarction, abscess, bronchiectasis, RA, lupus, uremia, metastases, radiation) makes vessels '
              'leaky: serous, serofibrinous or fibrinous pleuritis — an exudate (pleural/serum protein > 0.5 or LDH > 0.6).',
  'mech:ne': 'Low plasma oncotic pressure — nephrotic syndrome; also the generalized edema of renal failure and cirrhosis.',
  'mech:at': 'Atelectasis makes intrapleural pressure more negative and draws fluid in.',
  'mech:ly': 'Mediastinal carcinomatosis blocks lymphatic drainage.',
  'fl:hy': 'Hydrothorax: noninflammatory clear straw-colored fluid.',
  'fl:he': 'Hemothorax: blood — usually trauma or surgery, sometimes a ruptured aortic aneurysm (almost always fatal). Bloody exudate '
           '(hemorrhagic pleuritis) instead suggests a bleeding disorder, rickettsiae or tumor.',
  'fl:ch': 'Chylothorax: milky lymph rich in emulsified fat (chylomicron triglycerides) — thoracic duct trauma or a malignancy obstructing '
           'a major lymphatic duct. FA counts it with the exudates.',
  'fl:em': 'Empyema: loculated yellow-green pus of neutrophils from bacterial or fungal seeding, usually from the lung (rarely through the '
           'diaphragm from a liver or subdiaphragmatic abscess, more often on the right). It organizes into adhesions; pleural glucose and pH fall. Drain it.',
  'fl:mt': 'Metastatic implants, most often lung and breast, give serous or serosanguineous effusions with tumor cells — cytology helps. An exudate, often with low glucose.',
}

dyn = dict(
  kinds=dict(h2o=['fl', '--nf-h2o'], prot=['fl', '--dk9'], rbc=['bl', '--nf-blood']),
  groups=[['fl', 'Water · protein'], ['bl', 'Blood in the capillary']],
  switches=[dict(id='mech', label='Mechanism', type='one', options=[
              ['hf', 'Heart failure', 'effmech'], ['pna', 'Pneumonia (leaky)', 'effmech'], ['ne', 'Nephrotic (low protein)', 'effmech'],
              ['at', 'Atelectasis (suction)', 'effmech'], ['ly', 'Lymph blocked', 'effmech']]),
            dict(id='fl', label='What fills it', type='one', options=[
              ['hy', 'Clear fluid', 'hydrothorax'], ['he', 'Blood', 'hydrothorax'], ['ch', 'Milky chyle', 'hydrothorax'],
              ['em', 'Pus', 'pleuritis'], ['mt', 'Tumor cells', 'effmech']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 15 · Guyton ch 39 · First Aid pp. 698–699')

MAP = dict(
  id='plsim', title='Pleural Fluid in Motion', topic='pulmo', after='pleural',
  sub='Raise capillary pressure, make vessels leak, drop plasma protein, collapse the lung or block the lymph, and watch the pleural space '
      'fill — then see it as clear fluid, blood, chyle, pus or a malignant effusion',
  w=3600, h=1900,
  fa='698–699',
  src=['Robbins ch 15 — The lung', 'Guyton ch 39 — Pulmonary Circulation, Pulmonary Edema, and Pleural Fluid'],
  lanes=[('pfMech', 'Mechanism', 'tca'), ('pfFluid', 'The fluid', 'glycolysis')],
  nodes=[
    ('pf1', 'Five ways fluid collects', 400, 1720, 'pfMech', 'pressure · leak · lymph', ['effmech'], 'hub'),
    ('pf2', 'Hydro-, hemo-, chylothorax', 950, 1720, 'pfFluid', 'clear · blood · milky', ['hydrothorax']),
    ('pf3', 'Pleuritis & empyema', 1500, 1720, 'pfFluid', 'exudate · pus', ['pleuritis'])],
  panels=[
    (2500, PANY, 1000, 'Transudate or exudate (Robbins ch 15)', [
      ('Heart failure', 'transudate (pressure)'), ('Nephrotic, cirrhosis', 'transudate (oncotic)'), ('Pneumonia, TB, tumor', 'exudate (inflammation)'),
      ('Milky', 'thoracic duct')])],
  dyn=dyn)
