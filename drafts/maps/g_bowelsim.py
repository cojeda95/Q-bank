# Bowel Blockages in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A front view of the gut as one tube — stomach → duodenum → small bowel loops → ileocecal junction → cecum and appendix →
# ascending, transverse (splenic flexure), descending and sigmoid colon → rectum — with the aorta and SMA. Contents move
# along it. A `one` switch blocks or starves it: small bowel obstruction (dilated above, collapsed below), ileus (no
# movement, no transition), intussusception, midgut and sigmoid volvulus, acute mesenteric ischemia (SMA embolus),
# watershed colonic ischemia, appendicitis (pain migrates periumbilical → McBurney), Hirschsprung and NEC. 5 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
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
SB1 = 'M1050 600 C1300 650 1300 750 1050 750 C800 750 800 850 1050 850'
SB2 = 'M1050 850 C1300 850 1300 950 1050 950 C900 950 800 1000 750 1050 H660'
COL1 = 'M660 1050 V500 H1620'
COL2 = 'M1620 500 V1100 C1650 1250 1400 1200 1300 1260'
REC = 'M1300 1260 C1200 1320 1160 1380 1150 1450'
DUO = 'M1300 420 C1250 470 1150 470 1100 520 C1060 560 1050 580 1050 600'

text('Bowel blockages — where the gut stops, twists or starves', 180, 150, 'dyn-big')
text('front view, patient’s right on your left · contents flow from stomach to rectum', 180, 176, 'dyn-cap')

def tube(d, w, col='--dk5', op=.25, when=None, unless=None):
    add(f'<path d="{d}" style="fill:none;stroke:var({col});stroke-width:{w};opacity:{op};stroke-linecap:round;stroke-linejoin:round"/>', when=when, unless=unless)

# ════════ gut ════════
add('<rect x="320" y="260" width="1620" height="1300" rx="80" class="dyn-soft"/>')
add('<path d="M1460 300 V1450" style="stroke:var(--nf-blood);stroke-width:20;opacity:.2"/>'); text('aorta', 1480, 320, 'nf-l2')
add('<path d="M1460 620 C1380 680 1300 720 1250 790" style="stroke:var(--nf-blood);stroke-width:10;opacity:.35"/>'); text('SMA', 1400, 600, 'nf-l2')
add('<ellipse cx="1360" cy="380" rx="120" ry="70" style="fill:var(--dk5);fill-opacity:.15;stroke:var(--dk5);stroke-width:4"/>'); text('stomach', 1360, 300, 'nf-l2', 'middle')
tube(DUO, 30)
SBD = D('sbo', 'ileus', 'midvolv')
tube(SB1, 30, unless=SBD + D('ami')); tube(SB1, 64, op=.35, when=SBD)
tube(SB2, 30, unless=D('sbo', 'ileus', 'ami', 'midvolv')); tube(SB2, 12, op=.4, when=D('sbo')); tube(SB2, 64, op=.35, when=D('ileus'))
tube(SB2, 30, col='--dk10', op=.6, when=D('midvolv'))
tube(SB1, 34, col='--dk10', op=.6, when=D('ami')); tube(SB2, 34, col='--dk10', op=.6, when=D('ami'))
text('small bowel', 1310, 700, 'nf-l2')
tube(COL1, 40, unless=D('ileus', 'hirsch')); tube(COL1, 76, op=.35, when=D('ileus', 'hirsch'))
tube(COL2, 40, unless=D('ileus', 'hirsch', 'sigvolv')); tube(COL2, 76, op=.35, when=D('ileus', 'hirsch', 'sigvolv'))
tube(REC, 40, unless=D('hirsch')); tube(REC, 14, col='--bad', op=.6, when=D('hirsch'))
text('rectum', 1170, 1500, 'nf-l2')
text('cecum', 600, 1110, 'nf-l2', 'end'); text('splenic flexure', 1660, 470, 'nf-l2')
text('sigmoid', 1450, 1290, 'nf-l2')
add('<path d="M640 1080 C640 1140 630 1170 620 1210" style="stroke:var(--dk5);stroke-width:14;opacity:.4;stroke-linecap:round"/>', unless=D('app'))
add('<path d="M640 1080 C640 1140 630 1170 620 1210" style="stroke:var(--bad);stroke-width:24;opacity:.7;stroke-linecap:round"/>', when=D('app'))
text('appendix', 600, 1240, 'nf-l2', 'end')
# lesions
add('<path d="M1020 820 L1080 880 M1080 820 L1020 880" class="nf-x"/>', when=D('sbo'))
text('adhesion · hernia · tumor — air-fluid levels above, collapsed below', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('sbo'))
text('ileus — no blockage, nothing moves, no transition zone', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('ileus'))
for r in (40, 28, 16):
    add(f'<circle cx="700" cy="1050" r="{r}" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=D('intus'))
text('ileum telescopes into the cecum — target sign · currant jelly stool', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('intus'))
add('<path d="M1000 760 c60 40 -60 60 0 100 c60 40 -60 60 0 100" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=D('midvolv'))
text('midgut volvulus — infant with bilious vomiting: surgical emergency', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('midvolv'))
add('<path d="M1500 1180 c40 -40 80 0 40 40 c-40 40 0 80 40 40" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=D('sigvolv'))
text('sigmoid volvulus — older adult · coffee bean sign', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('sigvolv'))
add('<circle cx="1250" cy="790" r="20" style="fill:var(--bad)"/>', when=D('ami'))
text('SMA embolus (AF, recent MI) — pain out of proportion to the exam', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('ami'))
for x, y in ((1620, 500), (1340, 1240)):
    add(f'<circle cx="{x}" cy="{y}" r="50" style="fill:var(--dk10);fill-opacity:.5;stroke:var(--bad);stroke-width:4"/>', when=D('colisch'))
text('watershed: splenic flexure and rectosigmoid — pain, then hematochezia', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('colisch'))
text('periumbilical first (T8–T10 visceral) → McBurney point', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('app'))
text('aganglionic rectum cannot relax — megacolon above · RET · Down syndrome', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('hirsch'))
for x, y in ((720, 1040), (800, 1000), (660, 950), (660, 860)):
    add(f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>', when=D('nec'))
text('premature, formula-fed — gas in the bowel wall (pneumatosis)', 1100, 1640, 'nf-l1 dyn-tag', 'middle', when=D('nec'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
STOP = lambda *k: m(D(*k), set=dict(food=0))
flows = [
  dict(d=DUO + ' ' + SB1.replace('M1050 600', 'L1050 600'), len=1100, speed=110, r=9, base=dict(food=5),
       mods=[m(D('sbo'), set=dict(food=8), speed=0.15), m(D('ileus'), speed=0.03), m(D('midvolv'), set=dict(food=0))]),
  dict(d=SB2, len=900, speed=110, r=9, base=dict(food=4), mods=[STOP('sbo', 'midvolv'), m(D('ileus'), speed=0.03), m(D('intus'), set=dict(food=1), speed=0.2)]),
  dict(d=COL1, len=1550, speed=100, r=10, base=dict(food=5), mods=[STOP('sbo', 'midvolv', 'intus'), m(D('ileus'), speed=0.03), m(D('hirsch'), set=dict(food=9), speed=0.2)]),
  dict(d=COL2, len=900, speed=100, r=10, base=dict(food=3), mods=[STOP('sbo', 'midvolv', 'intus'), m(D('ileus'), speed=0.03),
       m(D('hirsch', 'sigvolv'), set=dict(food=7), speed=0.15)]),
  dict(d=REC, len=260, speed=100, r=10, base=dict(food=2), mods=[STOP('sbo', 'midvolv', 'intus', 'hirsch', 'sigvolv'), m(D('ileus'), speed=0.03)]),
  dict(d='M1460 400 V620 C1380 680 1300 720 1250 790', len=450, speed=120, r=10, base=dict(emb=2), when=D('ami')),
  dict(d='M1050 820 C950 900 800 1050 700 1130', len=450, speed=60, r=10, base=dict(pain=2), when=D('app')),
]
sites = [dict(x=1110, y=880, n=[1, 1], w=10, t='rec', l='', aria='Small bowel obstruction', c='sbo', ions=[]),
         dict(x=700, y=980, n=[0, -1], w=10, t='rec', l='', aria='Intussusception', c='intussusception', ions=[]),
         dict(x=1580, y=1150, n=[1, 0], w=10, t='rec', l='', aria='Volvulus', c='volvulus', ions=[]),
         dict(x=1300, y=810, n=[1, 0], w=10, t='rec', l='', aria='Mesenteric ischemia', c='mesenteric', ions=[]),
         dict(x=560, y=1200, n=[-1, 0], w=10, t='rec', l='', aria='Appendicitis', c='appendicitis', ions=[]),
         dict(x=1100, y=1450, n=[-1, 0], w=10, t='rec', l='', aria='Hirschsprung disease', c='hirschsprung', ions=[]),
         dict(x=620, y=880, n=[-1, 0], w=10, t='rec', l='', aria='Necrotizing enterocolitis', c='nec', ions=[])]

readouts = [
  dict(l='Distension', mods=[dict(when=D('sbo', 'ileus', 'midvolv', 'sigvolv', 'hirsch'), d=1)]),
  dict(l='Flatus & stool', mods=[dict(when=D('sbo', 'ileus', 'midvolv', 'sigvolv', 'hirsch', 'intus'), d=-1)]),
  dict(l='Bowel ischemia', mods=[dict(when=D('ami', 'colisch', 'midvolv', 'sigvolv', 'intus', 'nec'), d=1)]),
  dict(l='Blood in stool', mods=[dict(when=D('intus', 'ami', 'colisch'), d=1)]),
  dict(l='Bowel sounds', mods=[dict(when=D('ileus'), d=-1)]),
]

notes = {
  '': 'Contents move from stomach to rectum, driven by the enteric plexuses, fed by the celiac, SMA and IMA. Block the tube, '
      'stop its motion, twist it or cut its blood, and see what backs up.',
  'dx:sbo': 'Small bowel obstruction: fluid and gas build up above the block, the bowel collapses below. Adhesions, hernias, '
            'tumors; meconium ileus in CF newborns. Dilated loops with air-fluid levels and a transition zone. Decompress, '
            'fluids, bowel rest; surgery if strangulated.',
  'dx:ileus': 'Ileus: hypomotility with no blockage — no flatus or stool, distension, ↓ bowel sounds, no transition zone. After '
              'surgery, opioids, hypokalemia, sepsis. Correct K⁺.',
  'dx:intus': 'Intussusception: proximal bowel telescopes into distal, usually at the ileocecal junction — colicky pain, '
              'currant jelly stools, sausage mass, target sign. Children: Peyer patch hypertrophy, Meckel, IgA vasculitis; '
              'adults: a tumor lead point.',
  'dx:midvolv': 'Midgut volvulus: malrotation leaves a narrow mesentery and Ladd bands; the loop twists and loses its blood supply. '
                'Bilious vomiting in an infant is a surgical emergency.',
  'dx:sigvolv': 'Sigmoid volvulus: older adults — coffee bean sign.',
  'dx:ami': 'Acute mesenteric ischemia: usually an SMA embolus (AF, recent MI, heart failure) — pain out of proportion to the '
            'exam, currant jelly stools. Chronic form: postprandial pain, fear of eating, weight loss.',
  'dx:colisch': 'Colonic ischemia: watershed areas fail first — splenic flexure, rectosigmoid; crampy pain then hematochezia; '
                'thumbprinting.',
  'dx:app': 'Appendicitis: obstructed lumen → closed loop. Visceral T8–T10 pain is periumbilical, then parietal peritoneum '
            'localizes it to McBurney point; psoas, obturator, Rovsing signs; may perforate. Appendectomy.',
  'dx:hirsch': 'Hirschsprung: neural crest cells fail to reach the distal colon — no Auerbach or Meissner plexus, so it cannot '
               'relax; megacolon above a transition zone. No meconium in 48 h; squirt sign; suction biopsy shows no ganglion '
               'cells. RET; Down syndrome. Resect the segment.',
  'dx:nec': 'Necrotizing enterocolitis: premature, formula-fed infant; terminal ileum and proximal colon necrose — pneumatosis '
            'intestinalis, portal venous gas, pneumoperitoneum.',
}

dyn = dict(
  kinds=dict(food=['mov', '--dk5'], emb=['mov', '--bad'], pain=['mov', '--accent']), groups=[['mov', 'Gut contents · embolus · pain']],
  switches=[dict(id='dx', label='Problem', type='one', options=[
              ['sbo', 'Small bowel obstruction', 'sbo'], ['ileus', 'Ileus', 'sbo'], ['intus', 'Intussusception', 'intussusception'],
              ['midvolv', 'Midgut volvulus', 'volvulus'], ['sigvolv', 'Sigmoid volvulus', 'volvulus'],
              ['ami', 'Acute mesenteric ischemia', 'mesenteric'], ['colisch', 'Colonic ischemia', 'mesenteric'],
              ['app', 'Appendicitis', 'appendicitis'], ['hirsch', 'Hirschsprung', 'hirschsprung'], ['nec', 'NEC', 'nec']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 17')

MAP = dict(
  id='bowelsim', title='Bowel Blockages in Motion', topic='gi', after='gitract',
  sub='Run contents from stomach to rectum, then obstruct, paralyze, telescope, twist or starve the bowel — SBO, ileus, '
      'intussusception, volvulus, mesenteric and colonic ischemia, appendicitis, Hirschsprung and NEC',
  w=3600, h=2000,
  fa='61, 390, 391, 392, 393',
  src=['Robbins ch 17 — The gastrointestinal tract', 'Robbins ch 10 — Diseases of infancy and childhood'],
  lanes=[('bwObs', 'Obstruction', 'tca'), ('bwIsch', 'Ischemia & inflammation', 'glycolysis')],
  nodes=[
    ('bw1', 'Bowel obstruction & ileus', 330, 1840, 'bwObs', 'transition zone', ['sbo'], 'hub'),
    ('bw2', 'Intussusception', 760, 1840, 'bwObs', 'target · currant jelly', ['intussusception']),
    ('bw3', 'Volvulus & malrotation', 1200, 1840, 'bwObs', 'bilious vomiting', ['volvulus']),
    ('bw4', 'Hirschsprung disease', 1640, 1840, 'bwObs', 'no ganglion cells', ['hirschsprung']),
    ('bw5', 'Mesenteric ischemia', 2080, 1840, 'bwIsch', 'pain > exam', ['mesenteric']),
    ('bw6', 'Appendicitis', 2520, 1840, 'bwIsch', 'McBurney', ['appendicitis']),
    ('bw7', 'Necrotizing enterocolitis', 2960, 1840, 'bwIsch', 'pneumatosis', ['nec'])],
  panels=[
    (2500, PANY, 1000, 'Imaging signs (Robbins ch 17)', [
      ('Air-fluid levels', 'small bowel obstruction'), ('Target sign', 'intussusception'), ('Coffee bean', 'sigmoid volvulus'),
      ('Thumbprinting', 'colonic ischemia'), ('Pneumatosis', 'NEC')])],
  dyn=dyn)
