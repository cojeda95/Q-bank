# Negative-Strand Viruses in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A body: brain, airway from larynx and trachea down to the small airways, parotids, pancreas, testes, a limb with a bite
# and its nerve, and the blood vessels. A `one` switch follows one − ssRNA virus from entry to target: rabies (bite →
# nicotinic AChR → retrograde up the nerve → brain; a `pep` toggle gives immune globulin + vaccine before it arrives),
# RSV (small airways, syncytia; palivizumab), parainfluenza croup (subglottic narrowing, steeple sign), mumps (respiratory
# tract → parotids, testes, meninges, pancreas) and Ebola (vessels leak, hemorrhage, DIC). 5 readouts. Facts from the
# pinned cards; FA pages in `fa`. No new cards.
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
P = dict(brain=(1000, 300), larynx=(1000, 520), trachea=(1000, 640), bronch=(1100, 820), parotid=(900, 430), pancreas=(1050, 1000),
         testis=(1000, 1250), bite=(1500, 1180), meninges=(1000, 230))

text('Negative-strand viruses — where each one goes', 180, 150, 'dyn-big')
text('all enveloped − ssRNA · follow one from its way in', 180, 176, 'dyn-cap')

# ════════ body ════════
add('<circle cx="1000" cy="320" r="110" style="fill:var(--dk2);fill-opacity:.06;stroke:var(--dk2);stroke-width:4"/>'); text('brain', 1130, 300, 'nf-l2')
add('<path d="M1000 230 C940 230 900 260 890 300 M1000 230 C1060 230 1100 260 1110 300" style="fill:none;stroke:var(--dk7);stroke-width:4"/>')
add('<path d="M860 470 H1140 L1180 1180 H820 Z" style="fill:var(--dk2);fill-opacity:.04;stroke:var(--dk2);stroke-width:4;stroke-linejoin:round"/>')
add('<path d="M1000 470 V720" style="stroke:var(--dk5);stroke-width:30;opacity:.3"/>', unless=D('croup'))
add('<path d="M1000 470 V530 M1000 560 V720" style="stroke:var(--dk5);stroke-width:30;opacity:.3"/>', when=D('croup'))
add('<path d="M1000 530 V560" style="stroke:var(--bad);stroke-width:10"/>', when=D('croup'))
text('larynx · trachea', 1040, 600, 'nf-l2')
add('<path d="M1000 720 C960 780 920 840 900 900 M1000 720 C1040 780 1080 840 1100 900" style="fill:none;stroke:var(--dk5);stroke-width:14;opacity:.3"/>')
for x in (880, 920, 1080, 1120):
    add(f'<circle cx="{x}" cy="910" r="14" style="fill:var(--nf-h2o);fill-opacity:.3;stroke:var(--dk1);stroke-width:2"/>')
    add(f'<circle cx="{x}" cy="910" r="22" style="fill:var(--bad);fill-opacity:.4"/>', when=D('rsv'))
text('small airways', 1150, 920, 'nf-l2')
for x in (880, 1120):
    add(f'<ellipse cx="{x}" cy="430" rx="34" ry="24" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>')
    add(f'<ellipse cx="{x}" cy="430" rx="54" ry="38" style="fill:var(--bad);fill-opacity:.4"/>', when=D('mumps'))
text('parotid', 820, 420, 'nf-l2', 'end')
add('<ellipse cx="1050" cy="1000" rx="70" ry="22" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>'); text('pancreas', 1130, 1006, 'nf-l2')
add('<ellipse cx="1050" cy="1000" rx="80" ry="30" style="fill:var(--bad);fill-opacity:.35"/>', when=D('mumps'))
for x in (970, 1030):
    add(f'<ellipse cx="{x}" cy="1250" rx="24" ry="32" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>')
    add(f'<ellipse cx="{x}" cy="1250" rx="34" ry="44" style="fill:var(--bad);fill-opacity:.4"/>', when=D('mumps'))
text('testes', 1080, 1260, 'nf-l2')
add('<path d="M1140 520 L1520 1180" style="stroke:var(--dk2);stroke-width:46;opacity:.1;stroke-linecap:round"/>')
add('<path d="M1080 360 C1180 500 1350 800 1500 1160" style="fill:none;stroke:var(--dk7);stroke-width:6"/>'); text('peripheral nerve', 1340, 720, 'nf-l2')
add('<circle cx="1500" cy="1180" r="22" style="fill:var(--bad);opacity:.7"/>', when=D('rabies')); text('bite', 1540, 1190, 'nf-l1', when=D('rabies'))
add('<path d="M820 470 C760 700 760 1000 820 1180 M1180 470 C1240 700 1240 1000 1180 1180" style="fill:none;stroke:var(--nf-blood);stroke-width:8;opacity:.35"/>', unless=D('ebola'))
add('<path d="M820 470 C760 700 760 1000 820 1180 M1180 470 C1240 700 1240 1000 1180 1180" style="fill:none;stroke:var(--bad);stroke-width:14;stroke-dasharray:10 10;opacity:.7"/>', when=D('ebola'))
text('vessels', 740, 820, 'nf-l2', 'end')
add('<circle cx="1000" cy="320" r="110" style="fill:var(--bad);fill-opacity:.2"/>', when=['dx:rabies&!pep'])
add('<path d="M890 290 C930 250 1070 250 1110 290" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=D('mumps'))
TAG = dict(rabies='binds the nicotinic AChR at the bite → retrograde up the axon → brain · weeks to months, by distance',
           rsv='F protein fuses airway cells into syncytia — infant bronchiolitis', croup='subglottic narrowing — barking cough, stridor, steeple sign',
           mumps='parotitis, orchitis, aseptic meningitis, pancreatitis — POM-Poms · ↑ amylase',
           ebola='capillary leak, hemorrhage, DIC — shock, multiorgan failure')
for k, s in TAG.items(): text(s, 1000, 1400, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('reached the brain: hydrophobia, agitation, paralysis — almost always fatal · Negri bodies', 1000, 1440, 'nf-l1', 'middle', when=['dx:rabies&!pep'])
text('wound care + rabies immune globulin + killed vaccine — stopped before the brain', 1000, 1440, 'nf-l1', 'middle', when=['dx:rabies&pep'])
text('palivizumab (anti-F) prophylaxis for premature infants', 1000, 1440, 'nf-l1', 'middle', when=['dx:rsv&pep'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M1500 1160 C1350 800 1180 500 1080 360', len=1000, speed=60, r=10, base=dict(vir=3), when=D('rabies'),
       mods=[m(['dx:rabies&pep'], set=dict(vir=0))]),
  dict(d='M1000 200 V720 C1040 780 1080 840 1100 900', len=750, speed=120, r=9, base=dict(vir=3), when=D('rsv'), mods=[m(['dx:rsv&pep'], set=dict(vir=1))]),
  dict(d='M1000 200 V540', len=340, speed=90, r=9, base=dict(vir=3), when=D('croup')),
  dict(d='M1000 200 V520 C960 480 920 450 900 430', len=400, speed=110, r=9, base=dict(vir=3), when=D('mumps')),
  dict(d='M900 430 C800 700 900 1000 1000 1240', len=900, speed=110, r=9, base=dict(vir=2), when=D('mumps')),
  dict(d='M900 430 C860 380 900 300 950 250', len=230, speed=90, r=9, base=dict(vir=2), when=D('mumps')),
  dict(d='M820 470 C760 700 760 1000 820 1180', len=760, speed=110, r=9, base=dict(blood=4), mods=[m(D('ebola'), set=dict(blood=7), speed=0.5)]),
  dict(d='M790 700 C740 710 700 720 660 740', len=140, speed=60, r=8, base=dict(blood=3), when=D('ebola')),
]
sites = [dict(x=1560, y=1120, n=[1, 0], w=10, t='rec', l='', aria='Rabies', c='rabies', ions=[]),
         dict(x=1180, y=880, n=[1, 0], w=10, t='rec', l='', aria='RSV', c='rsv', ions=[]),
         dict(x=960, y=520, n=[-1, 0], w=10, t='rec', l='', aria='Croup', c='parainfl', ions=[]),
         dict(x=820, y=480, n=[-1, 1], w=10, t='rec', l='', aria='Mumps', c='mumps', ions=[]),
         dict(x=740, y=900, n=[-1, 0], w=10, t='rec', l='', aria='Ebola', c='ebola', ions=[])]

readouts = [
  dict(l='CNS infection', mods=[dict(when=['dx:rabies&!pep'] + D('mumps'), d=1)]),
  dict(l='Airway narrowing', mods=[dict(when=D('croup', 'rsv'), d=1)]),
  dict(l='Serum amylase', mods=[dict(when=D('mumps'), d=1)]),
  dict(l='Bleeding · DIC', mods=[dict(when=D('ebola'), d=1)]),
  dict(l='Fatality', mods=[dict(when=['dx:rabies&!pep'] + D('ebola'), d=1)]),
]

notes = {
  '': 'All five are enveloped negative-sense single-stranded RNA viruses. Pick one to follow it.',
  'dx:rabies': 'Rabies (rhabdovirus, bullet-shaped): bat, raccoon, skunk or fox bite; binds the nicotinic AChR and climbs by '
               'retrograde axonal transport — incubation weeks to months by distance. Fever, agitation, hydrophobia, '
               'hypersalivation, paralysis, coma; Negri bodies. Post-exposure: wound care, immune globulin + killed vaccine.',
  'dx:rsv': 'RSV (pneumovirus): infant small airways — bronchiolitis, pneumonia; F protein fuses cells into syncytia. Palivizumab '
            '(anti-F) prophylaxis for premature infants; ribavirin for severe disease (benefit unproven).',
  'dx:croup': 'Croup (parainfluenza): larynx and trachea inflamed, subglottic airway narrows — barking cough, stridor, hoarseness; '
              'steeple sign.',
  'dx:mumps': 'Mumps (paramyxovirus): droplets → respiratory tract → glands and meninges: parotitis, orchitis (infertility after '
              'puberty), aseptic meningitis, pancreatitis; ↑ amylase. MMR prevents it.',
  'dx:ebola': 'Ebola, Marburg (filoviruses): body fluids, bats — vessel damage, capillary leak, hemorrhage, DIC, shock; RT-PCR; '
              'supportive care, isolation, vaccinate contacts.',
  'pep': 'Prophylaxis: rabies immune globulin + vaccine after a bite; palivizumab for premature infants against RSV.',
}

dyn = dict(
  kinds=dict(vir=['mov', '--bad'], blood=['mov', '--nf-blood']), groups=[['mov', 'Virus · blood']],
  switches=[dict(id='dx', label='Virus', type='one', options=[
              ['rabies', 'Rabies', 'rabies'], ['rsv', 'RSV', 'rsv'], ['croup', 'Parainfluenza (croup)', 'parainfl'],
              ['mumps', 'Mumps', 'mumps'], ['ebola', 'Ebola / Marburg', 'ebola']]),
            dict(id='pep', label='Prevent', type='toggle', on='Prophylaxis given', off='Give prophylaxis', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 8')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='negsim', title='Negative-Strand Viruses in Motion', topic='id', after='virus',
  sub='Follow rabies up a nerve to the brain, RSV into the small airways, parainfluenza to the larynx, mumps to the parotids and '
      'testes and Ebola into leaking vessels — and give prophylaxis',
  w=3600, h=1900,
  fa='164, 166, 167, 169',
  src=['Robbins ch 8 — Infectious diseases', 'Katzung ch 49 — Antiviral Agents'],
  lanes=[('ngResp', 'Respiratory & glands', 'tca'), ('ngSys', 'Nerve & blood', 'glycolysis')],
  nodes=[
    ('ng1', 'Rabies', 330, 1700, 'ngSys', 'retrograde · nicotinic AChR', ['rabies'], 'hub'),
    ('ng2', 'RSV', 760, 1700, 'ngResp', 'syncytia · palivizumab', ['rsv']),
    ('ng3', 'Croup', 1200, 1700, 'ngResp', 'steeple sign', ['parainfl']),
    ('ng4', 'Mumps', 1640, 1700, 'ngResp', 'POM-Poms', ['mumps']),
    ('ng5', 'Ebola & Marburg', 2080, 1700, 'ngSys', 'hemorrhage · DIC', ['ebola'])],
  panels=[
    (2500, PANY, 1000, 'Prevention (Robbins ch 8)', [
      ('Rabies', 'immune globulin + killed vaccine'), ('RSV', 'palivizumab (premature)'), ('Mumps', 'MMR'), ('Ebola', 'isolation, vaccinate contacts')])],
  dyn=dyn)
