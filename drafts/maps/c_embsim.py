# Embryo Weeks 1–8 & Gut-Tube Defects in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A timeline of weeks 1–8 and the fetal period (`steps`, auto) with what happens each week and how a teratogen acts then
# (all-or-none before implantation, malformation in weeks 3–8, growth and function after). Below, the fetus in its
# amniotic sac with the fluid cycling: kidneys make urine → amniotic fluid → swallowed → gut. A `one` switch shows a defect
# — tracheoesophageal fistula, duodenal atresia, annular pancreas, gastroschisis, omphalocele, Potter sequence, horseshoe
# kidney, posterior urethral valves — and where the cycle breaks; a second picks a teratogen. 4 readouts. Facts from the
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

W = lambda *k: [f'wk:{x}' for x in k]
D = lambda *k: [f'dx:{x}' for x in k]
T = lambda *k: [f'tg:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def box(x0, y0, x1, y1, lab, cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="{cls}"/>'); text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')

text('Weeks 1–8 and the gut-tube defects', 180, 150, 'dyn-big')
text('top: the timeline · bottom: the amniotic fluid cycle and where each defect breaks it', 180, 176, 'dyn-cap')

# ════════ timeline ════════
WEEKS = [('w1', 'Week 1', 'blastocyst implants ~day 6 · hCG begins'), ('w2', 'Week 2', 'bilaminar disc: epiblast + hypoblast'),
         ('w3', 'Week 3', 'gastrulation: ectoderm, mesoderm, endoderm · notochord → neural plate'),
         ('w4', 'Week 4', 'neural tube closes · heart beats · limb buds'), ('w8', 'Week 8', 'genitalia look male or female'),
         ('fet', 'Fetal period', 'growth and maturation')]
X0, X1, TY = 320, 2300, 330
add(f'<path d="M{X0} {TY} H{X1}" style="stroke:var(--ink-3);stroke-width:6"/>')
add(f'<rect x="{X0 + 2 * 330}" y="{TY - 40}" width="{3 * 330}" height="80" rx="20" style="fill:var(--bad);fill-opacity:.08"/>')
text('weeks 3–8: organogenesis — teratogens do the most damage', X0 + 2 * 330 + 495, TY - 54, 'nf-l2', 'middle')
for i, (k, lab, sub) in enumerate(WEEKS):
    x = X0 + 160 + i * 330
    add(f'<circle cx="{x}" cy="{TY}" r="18" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:4"/>')
    add(f'<circle cx="{x}" cy="{TY}" r="18" style="fill:var(--accent)"/>', when=W(k))
    text(lab, x, TY + 52, 'nf-l1', 'middle')
    text(sub, 1310, 460, 'nf-l1 dyn-tag', 'middle', when=W(k))
EXP = {'w1': 'exposure now: all-or-none', 'w2': 'exposure now: all-or-none', 'w3': 'exposure now: malformation', 'w4': 'exposure now: malformation',
       'w8': 'exposure now: malformation', 'fet': 'exposure now: mainly growth and function'}
for k, t in EXP.items(): text(t, 1310, 494, 'nf-l2', 'middle', when=[f'wk:{k}&tg:*'])

# ════════ fetus and fluid cycle ════════
add('<ellipse cx="1050" cy="1050" rx="560" ry="380" style="fill:var(--nf-h2o);fill-opacity:.12;stroke:var(--nf-h2o);stroke-width:4"/>')
text('amniotic fluid', 620, 760, 'nf-l1')
add('<ellipse cx="1050" cy="1050" rx="560" ry="380" style="fill:var(--nf-h2o);fill-opacity:.25"/>', when=D('tef', 'annular'))
text('polyhydramnios', 1050, 1460, 'nf-l1 dyn-tag', 'middle', when=D('tef', 'annular'))
add('<ellipse cx="1050" cy="1050" rx="560" ry="380" style="fill:var(--surface);fill-opacity:.7"/>', when=D('potter', 'puv'))
text('oligohydramnios — the fetus is compressed, lungs can’t grow', 1050, 1460, 'nf-l1 dyn-tag', 'middle', when=D('potter', 'puv'))
box(900, 760, 1200, 830, 'Mouth · esophagus')
box(900, 870, 1200, 940, 'Stomach'); box(900, 980, 1200, 1050, 'Duodenum'); box(900, 1090, 1200, 1160, 'Bowel')
box(1300, 870, 1520, 940, 'Lungs')
box(620, 1090, 820, 1160, 'Kidneys'); box(620, 1220, 820, 1290, 'Bladder · urethra')
add('<rect x="1240" y="1060" width="60" height="60" rx="10" style="fill:var(--ink-3)"/>'); text('umbilicus', 1320, 1096, 'nf-l2')
# defects
add(X(1050, 850, 12), when=D('tef'))
add('<path d="M1200 800 C1260 820 1280 860 1300 880" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=D('tef'))
text('esophageal atresia + distal fistula from the trachea', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('tef'))
add(X(1050, 1015), when=D('duod'))
text('duodenal atresia: failed recanalization — double bubble, Down syndrome', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('duod'))
add('<ellipse cx="1050" cy="1015" rx="170" ry="48" style="fill:none;stroke:var(--dk5);stroke-width:12"/>', when=D('annular'))
text('annular pancreas: ventral bud rings the 2nd part of the duodenum', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('annular'))
add('<path d="M1300 1120 C1360 1180 1420 1180 1460 1130" style="fill:none;stroke:var(--dk3);stroke-width:18"/>', when=D('gastro'))
text('gastroschisis: right of the umbilicus, no sac — good prognosis', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('gastro'))
add('<circle cx="1330" cy="1090" r="70" style="fill:var(--dk3);fill-opacity:.25;stroke:var(--ink-2);stroke-width:4"/>', when=D('omph'))
text('omphalocele: through the umbilical ring, sac-covered — trisomy 13/18, Beckwith-Wiedemann', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('omph'))
add(X(800, 1100, 12), when=D('potter'))
text('renal agenesis → no fetal urine → Potter sequence', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('potter'))
add('<path d="M640 1125 Q720 1190 800 1125" style="fill:none;stroke:var(--dk5);stroke-width:12"/>', when=D('horse'))
text('horseshoe kidney: fused lower poles caught under the IMA', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('horse'))
add(X(800, 1270, 12), when=D('puv'))
text('posterior urethral valves: male outlet obstruction — bilateral hydronephrosis', 1700, 800, 'nf-l1 dyn-tag', 'middle', when=D('puv'))
TG = dict(valp='valproate, carbamazepine, phenytoin: neural tube, cardiac defects, cleft palate', iso='isotretinoin: craniofacial, CNS, cardiac, thymic',
          thal='thalidomide: phocomelia', li='lithium: Ebstein anomaly', warf='warfarin: stippled epiphyses, nasal hypoplasia — use heparin',
          ace='ACE inhibitors: renal failure, oligohydramnios, hypocalvaria', alc='alcohol: smooth philtrum, thin lip, small palpebral fissures, microcephaly')
for k, t in TG.items(): text(t, 1310, 560, 'nf-l1', 'middle', when=T(k))
add('<ellipse cx="1050" cy="1050" rx="560" ry="380" style="fill:var(--surface);fill-opacity:.6"/>', when=T('ace'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
CYCLE_URINE = D('potter', 'puv') + T('ace')
CYCLE_SWALLOW = D('tef', 'annular')
flows = [
  dict(d='M720 1160 V1220', len=60, speed=30, r=8, base=dict(w=2), mods=[m(D('potter'), set=dict(w=0))]),
  dict(d='M720 1290 C700 1360 600 1300 560 1100 C540 900 700 760 900 790', len=900, speed=140, r=9, base=dict(w=4), mods=[m(CYCLE_URINE, set=dict(w=0))]),
  dict(d='M1050 830 V870', len=40, speed=25, r=8, base=dict(w=2), mods=[m(D('tef'), set=dict(w=0))]),
  dict(d='M1050 940 V980', len=40, speed=25, r=8, base=dict(w=2), mods=[m(D('tef'), set=dict(w=0))]),
  dict(d='M1050 1050 V1090', len=40, speed=25, r=8, base=dict(w=2), mods=[m(D('tef', 'duod', 'annular'), set=dict(w=0))]),
  dict(d='M1200 1125 C1300 1100 1360 1000 1400 940', len=260, speed=80, r=8, base=dict(w=2), mods=[m(CYCLE_URINE, set=dict(w=0))]),
  dict(d=f'M{X0 + 160} {TY} H{X1 - 160}', len=1650, speed=300, r=10, base=dict(t=1)),
]
sites = [dict(x=1050, y=760, n=[0, -1], w=10, t='rec', l='', aria='Tracheoesophageal fistula', c='tef', ions=[]),
         dict(x=720, y=1220, n=[-1, 0], w=10, t='rec', l='', aria='Potter sequence', c='potter', ions=[]),
         dict(x=X0 + 40, y=TY + 100, n=[0, 1], w=10, t='rec', l='', aria='Weeks 1–8', c='earlydev', ions=[]),
         dict(x=X1 - 40, y=TY + 100, n=[0, 1], w=10, t='rec', l='', aria='Teratogens', c='teratogens', ions=[])]

readouts = [
  dict(l='Amniotic fluid', mods=[dict(when=CYCLE_SWALLOW, d=1), dict(when=CYCLE_URINE, d=-1)]),
  dict(l='Lung growth', mods=[dict(when=D('potter', 'puv'), d=-1)]),
  dict(l='Vomiting after the first feeds', mods=[dict(when=D('tef', 'duod', 'annular'), d=1)]),
  dict(l='Maternal serum AFP', mods=[dict(when=D('gastro', 'omph'), d=1)]),
]

notes = {
  '': 'The embryonic period (weeks 3–8) builds every organ. Late in pregnancy the fetus cycles amniotic fluid: kidneys make urine, which '
      'becomes most of the amniotic fluid, and the fetus swallows it into the gut. Break the urine side and fluid runs low; break the '
      'swallowing side and it builds up.',
  'wk:w1': 'Week 1: the blastocyst implants about day 6 and hCG secretion begins. Before implantation, injury is all-or-none.',
  'wk:w2': 'Week 2: bilaminar disc — epiblast and hypoblast.',
  'wk:w3': 'Week 3: gastrulation through the primitive streak forms ectoderm, mesoderm and endoderm; the notochord induces the neural plate.',
  'wk:w4': 'Week 4: the neural tube closes, the heart beats, limb buds appear.',
  'wk:w8': 'Week 8: genitalia look male or female.',
  'wk:fet': 'Fetal period: after week 8 exposures mainly affect growth and function.',
  'dx:tef': 'Esophageal atresia with distal TEF (commonest): the fetus can’t swallow → polyhydramnios; the newborn drools, chokes and '
            'vomits with the first feed; an NG tube won’t pass; air-filled stomach.',
  'dx:duod': 'Duodenal atresia: failed recanalization of the solid-cord stage — bilious vomiting, double bubble; Down syndrome.',
  'dx:annular': 'Annular pancreas: the two halves of the ventral bud migrate opposite ways and ring the 2nd part of the duodenum — '
                'polyhydramnios, vomiting; Down syndrome.',
  'dx:gastro': 'Gastroschisis: failed lateral fold closure beside the umbilicus (right), no covering sac; rarely chromosomal, good prognosis. ↑ AFP.',
  'dx:omph': 'Omphalocele: through the umbilical ring, covered by peritoneum and amnion — trisomies 13 and 18, Beckwith-Wiedemann, '
             'cardiac, GU and neural tube defects. ↑ AFP.',
  'dx:potter': 'Renal agenesis → no fetal urine → oligohydramnios → Potter sequence: pulmonary hypoplasia (kills), twisted face and skin, '
               'extremity defects, renal failure.',
  'dx:horse': 'Horseshoe kidney: fused lower poles caught under the inferior mesenteric artery during ascent — hydronephrosis, stones, '
              'infection; Turner, trisomies.',
  'dx:puv': 'Posterior urethral valves: the commonest bladder outlet obstruction in male infants — bilateral hydronephrosis, thick '
            'bladder, oligohydramnios.',
  'tg:ace': 'ACE inhibitors in pregnancy: fetal renal failure, oligohydramnios, hypocalvaria.',
}

dyn = dict(
  kinds=dict(w=['fluid', '--nf-h2o'], t=['time', '--accent']), groups=[['fluid', 'Amniotic fluid'], ['time', 'Time']],
  switches=[dict(id='wk', label='When', type='steps', auto=3, options=[[k, l] for k, l, _ in WEEKS]),
            dict(id='dx', label='Defect', type='one', options=[
              ['tef', 'Esophageal atresia / TEF', 'tef'], ['duod', 'Duodenal atresia', 'atresia'], ['annular', 'Annular pancreas', 'annularpanc'],
              ['gastro', 'Gastroschisis', 'walldefects'], ['omph', 'Omphalocele', 'walldefects'], ['potter', 'Renal agenesis (Potter)', 'potter'],
              ['horse', 'Horseshoe kidney', 'horseshoe'], ['puv', 'Posterior urethral valves', 'horseshoe']]),
            dict(id='tg', label='Teratogen', type='one', options=[
              ['valp', 'Antiepileptics', 'teratogens'], ['iso', 'Isotretinoin', 'teratogens'], ['thal', 'Thalidomide', 'teratogens'],
              ['li', 'Lithium', 'teratogens'], ['warf', 'Warfarin', 'teratogens'], ['ace', 'ACE inhibitors', 'teratogens'], ['alc', 'Alcohol', 'fas']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 365–367, 596–597, 630–635 · Langman ch 5–9, 15–16')

MAP = dict(
  id='embsim', title='Embryo & Gut-Tube Defects in Motion', topic='devrepro', after='embryo',
  sub='Step through weeks 1–8 and see how a teratogen acts at each stage, then watch the fetus cycle amniotic fluid and break it — '
      'TEF, duodenal atresia, annular pancreas, gastroschisis, omphalocele, Potter, horseshoe kidney, posterior urethral valves',
  w=3600, h=1900,
  fa='365, 366, 367, 501, 596, 597, 630, 631, 632, 633, 635',
  src=['Langman ch 5 — Third Week of Development: Trilaminar Germ Disc', 'Langman ch 6 — Third to Eighth Weeks: The Embryonic Period',
       'Langman ch 9 — Birth Defects and Prenatal Diagnosis', 'Langman ch 18 — Central Nervous System',
       'Katzung ch 59 — Special Aspects of Perinatal & Pediatric Pharmacology', 'Robbins ch 10 — Diseases of infancy and childhood',
       'Fundamental Neuroscience ch 5 — Development of the Nervous System', 'Langman ch 8 — Third Month to Birth: The Fetus and Placenta',
       'Robbins ch 22 — The female genital tract', 'Robbins ch 17 — The gastrointestinal tract', 'Langman ch 14 — Respiratory System',
       'Langman ch 15 — Digestive System', 'Langman ch 7 — The Gut Tube and the Body Cavities', 'Langman ch 16 — Urogenital System',
       'Moore ch 5 — Abdomen', 'Robbins ch 20 — The kidney', 'Robbins ch 19 — The pancreas', 'Bootcamp.com Gastroenterology — Embryology'],
  lanes=[('ebWk', 'Weeks 1–8', 'glycolysis'), ('ebGut', 'Gut & wall', 'tca'), ('ebUro', 'Kidney & urinary', 'gluconeo')],
  nodes=[
    ('eb1', 'Weeks 1–8', 330, 1660, 'ebWk', 'organogenesis', ['earlydev'], 'hub'),
    ('eb2', 'Germ layers', 760, 1660, 'ebWk', 'EMO PASSES', ['germlayers']),
    ('eb3', 'Teratogens · FAS', 1200, 1660, 'ebWk', 'weeks 3–8', ['teratogens', 'fas']),
    ('eb4', 'Morphogenesis · twins', 1640, 1660, 'ebWk', 'sequence, deformation', ['morpherrors', 'twins']),
    ('eb5', 'TEF · atresia', 2080, 1660, 'ebGut', 'can’t swallow', ['tef', 'atresia']),
    ('eb6', 'Gastroschisis · omphalocele', 330, 1790, 'ebGut', 'sac or no sac', ['walldefects']),
    ('eb7', 'Annular pancreas · VACTERL', 760, 1790, 'ebGut', 'ring · mesoderm', ['annularpanc', 'vacterl']),
    ('eb8', 'Potter sequence', 1200, 1790, 'ebUro', 'no urine', ['potter']),
    ('eb9', 'Horseshoe · valves', 1640, 1790, 'ebUro', 'IMA · male outlet', ['horseshoe'])],
  panels=[
    (2500, PANY, 1000, 'Amniotic fluid tells you which side broke', [
      ('Polyhydramnios', 'can’t swallow — TEF, annular pancreas'),
      ('Oligohydramnios', 'no urine — renal agenesis, valves, ACE inhibitors'),
      ('↑ Maternal AFP', 'gastroschisis, omphalocele')])],
  dyn=dyn)
