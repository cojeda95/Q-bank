# Bleeding in Pregnancy in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A sagittal uterus with the cervix, the placenta, the spiral arteries feeding it, the fetus, and the bladder in front. A
# `dx` switch moves or breaks the placenta: previa (over the os, painless), vasa previa (fetal vessels over the os), abruption
# (separates — painful, DIC), uterine rupture (through a scar), accreta / increta / percreta (grows into myometrium, serosa,
# bladder), preeclampsia (spiral arteries not remodeled → sFlt-1 to the mother) and postpartum hemorrhage by the 4 Ts. A `rx`
# switch gives the labor drugs (magnesium, oxytocin, a tocolytic, an antihypertensive); each works only where its card says.
# Geometry schematic. 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
R = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
UX, UY = 900, 740
OK = ['dx:pe&rx:mg', 'dx:pe&rx:htn', 'dx:pph&rx:oxy', 'dx:ptl&rx:toco']

text('Bleeding in pregnancy — where the placenta sits, and what goes wrong', 180, 150, 'dyn-big')
text('side view of the uterus, cervix at the bottom, bladder in front (left) · schematic', 180, 176, 'dyn-cap')

# ════════ uterus ════════
add(f'<path d="M{UX - 380} {UY - 40} C{UX - 400} {UY - 460} {UX + 400} {UY - 460} {UX + 380} {UY - 40} C{UX + 360} {UY + 260} {UX + 120} {UY + 380} {UX + 60} {UY + 470} H{UX - 60} C{UX - 120} {UY + 380} {UX - 360} {UY + 260} {UX - 380} {UY - 40} Z" '
    'style="fill:var(--dk10);fill-opacity:.08;stroke:var(--dk10);stroke-width:30;stroke-opacity:.35"/>', unless=D('pph'))
add(f'<path d="M{UX - 420} {UY - 40} C{UX - 440} {UY - 500} {UX + 440} {UY - 500} {UX + 420} {UY - 40} C{UX + 400} {UY + 280} {UX + 120} {UY + 380} {UX + 60} {UY + 470} H{UX - 60} C{UX - 120} {UY + 380} {UX - 400} {UY + 280} {UX - 420} {UY - 40} Z" '
    'style="fill:var(--dk10);fill-opacity:.08;stroke:var(--dk10);stroke-width:12;stroke-opacity:.35"/>', when=D('pph'))
text('myometrium', UX + 420, UY - 300, 'nf-l2')
add(f'<rect x="{UX - 60}" y="{UY + 470}" width="120" height="120" rx="20" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>')
text('cervix · internal os', UX + 80, UY + 520, 'nf-l2')
add(f'<ellipse cx="{UX - 520}" cy="{UY + 300}" rx="90" ry="70" style="fill:var(--dk5);fill-opacity:.12;stroke:var(--dk5);stroke-width:3"/>'); text('bladder', UX - 520, UY + 400, 'nf-l2', 'middle')
# fetus
add(f'<ellipse cx="{UX - 20}" cy="{UY + 40}" rx="170" ry="220" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--dk2);stroke-width:3"/>', unless=D('pph'))
add(f'<circle cx="{UX - 20}" cy="{UY + 180}" r="70" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--dk2);stroke-width:3"/>', unless=D('pph', 'rupture'))
add(f'<circle cx="{UX + 480}" cy="{UY + 100}" r="70" style="fill:var(--dk2);fill-opacity:.15;stroke:var(--bad);stroke-width:4"/>', when=D('rupture'))
text('fetus', UX - 20, UY - 100, 'nf-l2', 'middle', unless=D('pph'))
# placenta positions
NORM = f'M{UX - 200} {UY - 360} C{UX - 100} {UY - 400} {UX + 100} {UY - 400} {UX + 200} {UY - 360} L{UX + 160} {UY - 300} C{UX + 60} {UY - 330} {UX - 60} {UY - 330} {UX - 160} {UY - 300} Z'
LOW = f'M{UX - 140} {UY + 400} C{UX - 60} {UY + 470} {UX + 60} {UY + 470} {UX + 140} {UY + 400} L{UX + 110} {UY + 350} C{UX + 40} {UY + 400} {UX - 40} {UY + 400} {UX - 110} {UY + 350} Z'
add(f'<path d="{NORM}" style="fill:var(--nf-blood);fill-opacity:.45;stroke:var(--nf-blood);stroke-width:3"/>', unless=D('previa', 'pph'))
add(f'<path d="{LOW}" style="fill:var(--nf-blood);fill-opacity:.55;stroke:var(--bad);stroke-width:4"/>', when=D('previa'))
add(f'<path d="M{UX - 180} {UY - 330} C{UX - 80} {UY - 290} {UX + 80} {UY - 290} {UX + 180} {UY - 330}" style="fill:none;stroke:var(--bad);stroke-width:30;opacity:.55"/>', when=D('abrupt'))
text('clot behind the separating placenta', UX, UY - 250, 'nf-l1 dyn-tag', 'middle', when=D('abrupt'))
for i, (depth, k) in enumerate(((40, 'accreta'), (80, 'increta'), (140, 'percreta'))):
    add(f'<path d="M{UX - 120} {UY - 380} V{UY - 380 - depth} M{UX} {UY - 395} V{UY - 395 - depth} M{UX + 120} {UY - 380} V{UY - 380 - depth}" style="stroke:var(--nf-blood);stroke-width:14;opacity:.7"/>', when=D(k))
add(f'<path d="M{UX - 380} {UY + 140} C{UX - 440} {UY + 200} {UX - 460} {UY + 250} {UX - 470} {UY + 280}" style="stroke:var(--nf-blood);stroke-width:14;opacity:.7"/>', when=D('percreta'))
add(f'<path d="M{UX + 330} {UY + 40} l40 -30 l-20 50 l40 -20" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=D('rupture'))
for x in (-30, 0, 30):
    add(f'<path d="M{UX + x} {UY - 300} C{UX + x + 20} {UY} {UX + x - 20} {UY + 300} {UX + x} {UY + 520}" style="fill:none;stroke:var(--nf-h2o);stroke-width:6;opacity:.8"/>', when=D('vasa'))
# spiral arteries
for x in (-150, -50, 50, 150):
    add(f'<path d="M{UX + x} {UY - 470} c-20 20 20 30 0 50 c-20 20 20 30 0 50" style="fill:none;stroke:var(--nf-blood);stroke-width:12;opacity:.5"/>', unless=D('pe'))
    add(f'<path d="M{UX + x} {UY - 470} c-20 20 20 30 0 50 c-20 20 20 30 0 50" style="fill:none;stroke:var(--bad);stroke-width:4"/>', when=D('pe'))
text('spiral arteries', UX + 200, UY - 470, 'nf-l2')
text('not remodeled — narrow, placenta ischemic → sFlt-1 into the mother', UX, 1480, 'nf-l1 dyn-tag', 'middle', when=D('pe'))
# mother's organs (preeclampsia targets)
for x, y, l in ((1700, 380, 'brain'), (1700, 640, 'liver'), (1700, 900, 'kidney')):
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'); text(l, x + 60, y + 6, 'nf-l1')
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--bad);fill-opacity:.3"/>', when=D('pe'), unless=['dx:pe&rx:mg'] if l == 'brain' else None)
text('mother', 1700, 300, 'nf-l1', 'middle')
TAG = dict(previa='previa — over the internal os: painless third-trimester bleeding', vasa='vasa previa — fetal vessels over the os tear at rupture of membranes: fetal bradycardia',
           abrupt='abruption — painful bleeding, fetal distress, shock, DIC · hypertension, cocaine, smoking, trauma',
           rupture='uterine rupture — through an old scar in labor: fetal parts palpable, station lost',
           accreta='accreta — attaches to myometrium', increta='increta — into the myometrium', percreta='percreta — through serosa into bladder: hematuria',
           pe='preeclampsia — > 140/90 after 20 weeks with proteinuria or organ damage · HELLP · eclampsia = seizures',
           pph='postpartum hemorrhage — Tone (boggy uterus), Trauma, Tissue, Thrombin', ptl='preterm labor — buy time for steroids')
for k, s in TAG.items(): text(s, UX, 1520, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('this drug is the card’s answer here', UX, 1560, 'nf-l1', 'middle', when=OK)
text('accreta spectrum: placenta won’t separate — removal bleeds torrentially · hysterectomy', UX, 1560, 'nf-l2', 'middle', when=D('accreta', 'increta', 'percreta'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{UX - 50} {UY - 520} V{UY - 380}', len=140, speed=80, r=8, base=dict(blood=3), mods=[m(D('pe'), set=dict(blood=1), speed=0.3)]),
  dict(d=f'M{UX + 50} {UY - 520} V{UY - 380}', len=140, speed=80, r=8, base=dict(blood=3), mods=[m(D('pe'), set=dict(blood=1), speed=0.3)]),
  dict(d=f'M{UX} {UY + 420} V{UY + 640}', len=220, speed=110, r=10, base=dict(bleed=4), when=D('previa', 'abrupt', 'vasa', 'rupture')),
  dict(d=f'M{UX} {UY + 420} V{UY + 640}', len=220, speed=140, r=11, base=dict(bleed=6), when=D('pph'), mods=[m(['dx:pph&rx:oxy'], set=dict(bleed=1))]),
  dict(d=f'M{UX + 200} {UY - 360} C{UX + 600} {UY - 500} 1500 400 1650 380', len=900, speed=110, r=9, base=dict(sflt=3), when=D('pe')),
  dict(d=f'M{UX + 200} {UY - 360} C{UX + 600} {UY - 300} 1500 640 1650 640', len=850, speed=110, r=9, base=dict(sflt=2), when=D('pe')),
  dict(d=f'M{UX + 200} {UY - 360} C{UX + 600} {UY - 100} 1500 880 1650 900', len=900, speed=110, r=9, base=dict(sflt=2), when=D('pe')),
]
sites = [dict(x=UX - 160, y=UY + 440, n=[-1, 1], w=10, t='rec', l='', aria='Placenta previa', c='previa', ions=[]),
         dict(x=UX + 260, y=UY - 340, n=[1, -1], w=10, t='rec', l='', aria='Abruption and rupture', c='abruption', ions=[]),
         dict(x=UX - 260, y=UY - 380, n=[-1, -1], w=10, t='rec', l='', aria='Accreta spectrum', c='accreta', ions=[]),
         dict(x=UX - 200, y=UY - 480, n=[-1, -1], w=10, t='rec', l='', aria='Preeclampsia', c='preeclampsia', ions=[]),
         dict(x=1700, y=980, n=[0, 1], w=10, t='rec', l='', aria='Gestational hypertension', c='gesthtn', ions=[]),
         dict(x=UX + 160, y=UY + 600, n=[1, 1], w=10, t='rec', l='', aria='Postpartum hemorrhage', c='pph', ions=[]),
         dict(x=UX - 440, y=UY - 100, n=[-1, 0], w=10, t='rec', l='', aria='Labor drugs', c='labordrugs', ions=[])]

readouts = [
  dict(l='Painful bleeding', mods=[dict(when=D('abrupt', 'rupture'), d=1), dict(when=D('previa', 'vasa'), d=-1)]),
  dict(l='Fetal heart rate', mods=[dict(when=D('vasa', 'rupture', 'abrupt'), d=-1)]),
  dict(l='Clotting factors (DIC)', mods=[dict(when=D('abrupt'), d=-1)]),
  dict(l='Maternal BP', mods=[dict(when=D('pe'), d=1), dict(when=['dx:pe&rx:htn'], d=-1)]),
  dict(l='Seizure risk', mods=[dict(when=D('pe'), d=1), dict(when=['dx:pe&rx:mg'], d=-1)]),
]

notes = {
  '': 'Normally the placenta implants high in the uterus, fed by remodeled spiral arteries, and comes away after delivery while '
      'the uterus clamps down. Pick what goes wrong.',
  'dx:previa': 'Placenta previa: implanted over the internal os — painless third-trimester bleeding. Prior C-section, multiparity. '
               'Low-lying: within 2 cm of the os.',
  'dx:vasa': 'Vasa previa: unprotected fetal vessels over the os tear at rupture of membranes — the blood is the baby’s: fetal '
             'bradycardia, exsanguination. Velamentous insertion, bilobed placenta.',
  'dx:abrupt': 'Abruption: early separation — painful bleeding, fetal distress, maternal shock; the injured placenta releases '
               'tissue factor → DIC. Hypertension, preeclampsia, smoking, cocaine, trauma.',
  'dx:rupture': 'Uterine rupture: full-thickness tear, usually through an old C-section scar in labor — painful bleeding, fetal '
                'bradycardia, easily palpable fetal parts, loss of station.',
  'dx:accreta': 'Accreta: scarring stops decidualization; the placenta attaches to myometrium and will not separate.',
  'dx:increta': 'Increta: partly invades the myometrium.',
  'dx:percreta': 'Percreta: through myometrium and serosa, sometimes into the bladder (hematuria). Hysterectomy.',
  'dx:pe': 'Preeclampsia: spiral arteries not remodeled → ischemic placenta releases sFlt-1 → maternal endothelial injury: '
           'hypertension after 20 weeks with proteinuria or organ damage; HELLP; eclampsia. Delivery cures; IV magnesium; '
           'hydralazine, α-methyldopa, labetalol, nifedipine; aspirin prophylaxis in high risk.',
  'dx:pph': 'Postpartum hemorrhage: the uterus must contract to clamp the spiral arteries — Tone (atony, commonest), Trauma, '
            'Tissue (retained, accreta), Thrombin (DIC). Massage + oxytocin. Sheehan syndrome after severe loss.',
  'dx:ptl': 'Preterm labor: tocolytics (terbutaline, indomethacin, nifedipine) buy time for glucocorticoids or transfer.',
  'rx:mg': 'Magnesium sulfate prevents and treats eclamptic seizures.',
  'rx:oxy': 'Oxytocin contracts the uterus — postpartum hemorrhage, induction.',
  'rx:toco': 'Tocolytics — keep the baby in the TIN: Terbutaline, Indomethacin, Nifedipine.',
  'rx:htn': 'Safe in pregnancy: hydralazine, α-methyldopa, labetalol, nifedipine. ACE inhibitors are contraindicated.',
}

dyn = dict(
  kinds=dict(blood=['mov', '--nf-blood'], bleed=['mov', '--bad'], sflt=['mov', '--dk9']), groups=[['mov', 'Maternal blood · bleeding · sFlt-1']],
  switches=[dict(id='dx', label='Problem', type='one', options=[
              ['previa', 'Placenta previa', 'previa'], ['vasa', 'Vasa previa', 'previa'], ['abrupt', 'Abruption', 'abruption'],
              ['rupture', 'Uterine rupture', 'abruption'], ['accreta', 'Accreta', 'accreta'], ['increta', 'Increta', 'accreta'],
              ['percreta', 'Percreta', 'accreta'], ['pe', 'Preeclampsia', 'preeclampsia'], ['ptl', 'Preterm labor', 'labordrugs'],
              ['pph', 'Postpartum hemorrhage', 'pph']]),
            dict(id='rx', label='Drug', type='one', options=[
              ['mg', 'Magnesium sulfate', 'labordrugs'], ['oxy', 'Oxytocin', 'labordrugs'], ['toco', 'Tocolytic', 'labordrugs'],
              ['htn', 'Pregnancy-safe antihypertensive', 'gesthtn']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 22')

MAP = dict(
  id='placsim', title='Bleeding in Pregnancy in Motion', topic='devrepro', after='obgyn',
  sub='Move the placenta over the os, tear its vessels, separate it, let it invade, starve it of spiral-artery flow — and give '
      'magnesium, oxytocin, a tocolytic or a safe antihypertensive where each belongs',
  w=3600, h=1900,
  fa='343, 433, 657, 658, 660, 675',
  src=['Robbins ch 22 — The female genital tract', 'Katzung ch 11 — Antihypertensive Agents'],
  lanes=[('plPlac', 'Placenta', 'tca'), ('plMat', 'Mother & labor', 'glycolysis')],
  nodes=[
    ('pl1', 'Placenta previa & vasa previa', 330, 1760, 'plPlac', 'painless', ['previa'], 'hub'),
    ('pl2', 'Abruption & uterine rupture', 760, 1760, 'plPlac', 'painful · DIC', ['abruption']),
    ('pl3', 'Placenta accreta spectrum', 1200, 1760, 'plPlac', 'won’t separate', ['accreta']),
    ('pl4', 'Preeclampsia & eclampsia', 1640, 1760, 'plMat', 'sFlt-1 · Mg', ['preeclampsia']),
    ('pl5', 'Gestational hypertension', 2080, 1760, 'plMat', 'no proteinuria', ['gesthtn']),
    ('pl6', 'Postpartum hemorrhage', 2520, 1760, 'plMat', '4 Ts', ['pph']),
    ('pl7', 'Drugs in labor', 2960, 1760, 'plMat', 'TIN · oxytocin · Mg', ['labordrugs'])],
  panels=[
    (2500, PANY, 1000, 'Third-trimester bleeding (Robbins ch 22)', [
      ('Painless', 'placenta previa'), ('Painful + DIC', 'abruption'), ('At membrane rupture + bradycardia', 'vasa previa'),
      ('Scar + fetal parts palpable', 'uterine rupture')])],
  dyn=dyn)
