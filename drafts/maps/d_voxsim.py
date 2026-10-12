# Larynx & Voice in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The glottis seen from above (thyroid cartilage in front, arytenoids behind) with the vocal folds, the nerves that move them
# (recurrent laryngeal from CN X looping under the aortic arch on the left and the subclavian on the right; external branch of
# the superior laryngeal to cricothyroid), and the resonators above. An `act` stepper moves the folds: breathe (posterior
# cricoarytenoids abduct), phonate (lateral cricoarytenoids + arytenoids adduct), whisper (arytenoids stay apart), strain/swallow
# (tight closure) and high pitch (cricothyroid tenses). An `lx` switch adds a lesion: left recurrent nerve palsy, external-branch
# injury, nodules, a polyp, papillomas. Schematic. 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

A = lambda *k: [f'act:{x}' for x in k]
L = lambda *k: [f'lx:{x}' for x in k]
PANY = 1180
GX, AY, PY = 900, 420, 1080          # anterior commissure (top) · arytenoids (bottom)

text('Larynx & voice — which muscle opens, closes and tenses the folds, and which nerve runs it', 180, 150, 'dyn-big')
text('glottis from above: front (thyroid cartilage) at the top, arytenoids at the bottom, patient’s right on screen left · schematic', 180, 176, 'dyn-cap')
add(f'<path d="M{GX - 300} {AY + 40} Q{GX} {AY - 160} {GX + 300} {AY + 40}" style="fill:none;stroke:var(--dk5);stroke-width:14;opacity:.5"/>')
text('thyroid cartilage', GX, AY - 110, 'nf-l2', 'middle')
add(f'<ellipse cx="{GX}" cy="{PY + 120}" rx="330" ry="70" style="fill:var(--dk5);fill-opacity:.08;stroke:var(--dk5);stroke-width:6"/>')
text('cricoid (signet ring)', GX, PY + 240, 'nf-l2', 'middle')
text('right fold', GX - 330, 760, 'nf-l2', 'end'); text('left fold', GX + 330, 760, 'nf-l2')

# right fold always normal; left fold changes with left RLN palsy
OK = '!lx:rln'
for k, dx in (('br', 170), ('ph', 6), ('wh', 6), ('va', 2), ('hi', 6)):
    for s, side in ((-1, 'R'), (1, 'L')):
        conds = [f'act:{k}'] if s < 0 else [f'act:{k}&{OK}']
        if k == 'wh':   # folds meet in front, arytenoids stay apart behind
            add(f'<path d="M{GX} {AY} L{GX + s * 10} {PY - 200} L{GX + s * 90} {PY}" style="fill:none;stroke:var(--dk4);stroke-width:24;stroke-linecap:round;stroke-linejoin:round"/>', when=conds)
        else:
            add(f'<path d="M{GX} {AY - (40 if k == "hi" else 0)} L{GX + s * dx} {PY}" style="stroke:var(--dk4);stroke-width:{14 if k == "hi" else 24};stroke-linecap:round"/>', when=conds)
        ax = 90 if k == 'wh' else dx
        add(f'<path d="M{GX + s * ax} {PY} l{s * 30} 50" style="stroke:var(--dk6);stroke-width:40;stroke-linecap:round"/>', when=conds)
# left RLN palsy: left fold stuck paramedian
add(f'<path d="M{GX} {AY} L{GX + 60} {PY}" style="stroke:var(--bad);stroke-width:24;stroke-linecap:round;stroke-dasharray:30 14"/>', when=L('rln'))
add(f'<path d="M{GX + 60} {PY} l30 50" style="stroke:var(--bad);stroke-width:40;stroke-linecap:round"/>', when=L('rln'))
text('arytenoids', GX, PY + 90, 'nf-l2', 'middle')
# Valsalva / swallow: inlet closed by the epiglottis
add(f'<path d="M{GX - 260} {AY + 120} Q{GX} {AY + 40} {GX + 260} {AY + 120}" style="fill:none;stroke:var(--dk11);stroke-width:18;opacity:.7"/>', when=A('va'))
text('in swallowing the inlet closes too · epiglottis = elastic cartilage', GX + 90, AY + 240, 'nf-l1', None, when=A('va'))
# lesions on the folds
for s in (-1, 1):
    add(f'<circle cx="{GX + s * 22}" cy="{AY + 220}" r="16" style="fill:var(--bad);opacity:.8"/>', when=L('nod'))
add(f'<ellipse cx="{GX - 40}" cy="{AY + 300}" rx="34" ry="26" style="fill:var(--bad);opacity:.7"/>', when=L('pol'))
for x, y in ((GX - 30, AY + 160), (GX + 40, AY + 260), (GX - 50, AY + 380), (GX + 20, AY + 470), (GX + 60, AY - 60)):
    add(f'<circle cx="{x}" cy="{y}" r="24" style="fill:var(--dk2);fill-opacity:.55;stroke:var(--bad);stroke-width:3"/>', when=L('pap'))
add(f'<path d="M{GX - 300} {AY - 20} L{GX - 380} {AY - 120}" style="stroke:var(--bad);stroke-width:10"/>', when=L('ext'))

# nerves
NX = 1550
add(f'<path d="M{NX} 260 V1400" style="stroke:var(--dk7);stroke-width:8"/>'); text('vagus (CN X)', NX, 240, 'nf-l1', 'middle')
add(f'<path d="M{NX} 330 C{NX - 120} 340 {NX - 260} 360 {GX + 360} {AY - 20}" style="fill:none;stroke:var(--dk7);stroke-width:5"/>')
text('superior laryngeal n.', NX - 30, 310, 'nf-l2', 'end')
text('internal: sensory above folds · external: cricothyroid', NX - 220, 400, 'nf-l2', 'middle')
add(f'<path d="M{NX} 1250 C{NX} 1360 {NX + 140} 1360 {NX + 140} 1250 C{NX + 140} 1100 {GX + 500} 1150 {GX + 320} {PY + 60}" style="fill:none;stroke:var(--dk7);stroke-width:6"/>')
add(f'<path d="M{NX - 60} 1300 C{NX + 40} 1380 {NX + 220} 1380 {NX + 230} 1290" style="fill:none;stroke:var(--nf-blood);stroke-width:30;opacity:.35"/>')
text('aortic arch (left recurrent loops under it)', NX + 260, 1300, 'nf-l2')
text('left recurrent laryngeal n. → all other intrinsic muscles', NX + 160, 1180, 'nf-l2')
add(f'<path d="M{NX} 1250 C{NX} 1360 {NX + 140} 1360 {NX + 140} 1250 C{NX + 140} 1100 {GX + 500} 1150 {GX + 320} {PY + 60}" style="fill:none;stroke:var(--bad);stroke-width:10;stroke-dasharray:20 14"/>', when=L('rln'))
add(f'<path d="M{NX} 330 C{NX - 120} 340 {NX - 260} 360 {GX + 360} {AY - 20}" style="fill:none;stroke:var(--bad);stroke-width:9;stroke-dasharray:20 14"/>', when=L('ext'))

# resonators
RX = 2150
for i, (l, y) in enumerate((('sinuses · nose', 400), ('mouth · pharynx', 620), ('chest', 840))):
    add(f'<rect x="{RX}" y="{y - 60}" width="220" height="110" rx="20" style="fill:var(--dk9);fill-opacity:.1;stroke:var(--dk9);stroke-width:3"/>')
    text(l, RX + 110, y + 6, 'nf-l1', 'middle')
text('resonators', RX + 110, 300, 'nf-l1', 'middle'); text('lips · tongue · soft palate articulate', RX + 110, 1000, 'nf-l2', 'middle')

TAG = dict(br='deep breath in — posterior cricoarytenoids (the only abductors) swing the arytenoids apart',
           ph='phonate — lateral cricoarytenoids + arytenoids bring the folds together; air sets them vibrating',
           wh='whisper — folds meet in front but the arytenoids stay apart: air rushes through, no tone',
           va='strain or swallow — stronger adduction seals the glottis (Valsalva); in swallowing the inlet closes',
           hi='high pitch — cricothyroid (external branch of superior laryngeal n.) stretches and tenses the folds')
for k, s in TAG.items(): text(s, 1100, 1480, 'nf-l1 dyn-tag', 'middle', when=A(k))
LTAG = dict(rln='left recurrent laryngeal palsy — left fold motionless, can’t meet the other: hoarse (thyroidectomy, Pancoast, lung cancer, big left atrium)',
            ext='external branch injury (superior thyroid pedicle tied) — cricothyroid lost: monotonous voice, loss of vocal tenor',
            nod='vocal fold nodules — bilateral, from voice strain and smoking: hoarse; cancer risk almost nil',
            pol='vocal fold polyp — unilateral, same causes as nodules: hoarse',
            pap='laryngeal papillomas — HPV-6/11, possibly picked up at birth: glottic → hoarse, supraglottic → dysphagia')
for k, s in LTAG.items(): text(s, 1100, 1520, 'nf-l1', 'middle', when=L(k))

# ════════ motion ════════
def air(x, n, when, speed=150):
    return dict(d=f'M{x} {PY + 300} V{AY - 250}', len=1000, speed=speed, r=8, base=dict(air=n), when=when)
flows = [air(GX - 40, 4, A('br')), air(GX + 40, 4, ['act:br&!lx:rln']), air(GX + 70, 2, ['act:br&lx:rln']),
         air(GX, 2, A('ph', 'hi'), speed=90), air(GX, 3, A('wh')), air(GX - 60, 2, A('wh'))]
for y in (400, 620, 840):
    flows.append(dict(d=f'M{GX + 40} {AY - 40} C{GX + 600} {AY - 200} {RX - 200} {y} {RX} {y}', len=1300, speed=140, r=7,
                      base=dict(tone=2), when=A('ph', 'hi')))
flows += [dict(d=f'M{NX} 280 V1250', len=970, speed=180, r=6, base=dict(sig=2)),
          dict(d=f'M{NX} 1250 C{NX} 1360 {NX + 140} 1360 {NX + 140} 1250 C{NX + 140} 1100 {GX + 500} 1150 {GX + 320} {PY + 60}', len=1000,
               speed=150, r=6, base=dict(sig=2), when=['!lx:rln']),
          dict(d=f'M{NX} 330 C{NX - 120} 340 {NX - 260} 360 {GX + 360} {AY - 20}', len=400, speed=110, r=6, base=dict(sig=2),
               when=['act:hi&!lx:ext'])]
sites = [dict(x=GX - 260, y=PY - 40, n=[-1, 1], w=10, t='rec', l='', aria='Laryngeal muscles', c='larynxmus', ions=[]),
         dict(x=RX + 260, y=620, n=[1, 1], w=10, t='rec', l='', aria='Speech: tone, articulation, resonance', c='vocalize', ions=[]),
         dict(x=GX - 130, y=AY + 230, n=[-1, -1], w=10, t='rec', l='', aria='Vocal fold nodules & polyps', c='vcnodule', ions=[]),
         dict(x=NX + 60, y=720, n=[1, 1], w=10, t='rec', l='', aria='Laryngeal nerves', c='laryngealnerves', ions=[]),
         dict(x=GX + 160, y=AY + 120, n=[1, -1], w=10, t='rec', l='', aria='Laryngeal papillomas', c='laryngealpap', ions=[])]

readouts = [
  dict(l='Glottic opening', mods=[dict(when=['act:br&!lx:rln'], d=1), dict(when=A('va'), d=-1)]),
  dict(l='Voice (tone)', mods=[dict(when=A('wh'), d=-1), dict(when=['act:ph&!lx:*', 'act:hi&!lx:*', 'act:ph&lx:ext', 'act:hi&lx:ext'], d=1),
                               dict(when=['act:ph&lx:rln', 'act:ph&lx:nod', 'act:ph&lx:pol', 'act:ph&lx:pap',
                                          'act:hi&lx:rln', 'act:hi&lx:nod', 'act:hi&lx:pol', 'act:hi&lx:pap'], d=-1)]),
  dict(l='Pitch', mods=[dict(when=['act:hi&!lx:ext'], d=1), dict(when=['act:hi&lx:ext'], d=0)]),
  dict(l='Swallowing', mods=[dict(when=L('pap', 'rln'), d=-1)]),
]

notes = {
  '': 'Posterior cricoarytenoids are the only muscles that open the glottis. Lateral cricoarytenoids and the arytenoid muscles close '
      'it; cricothyroid tenses the folds. Recurrent laryngeal n. (6th arch) runs every intrinsic muscle except cricothyroid, which '
      'gets the external branch of the superior laryngeal n. (4th arch). Both come from CN X.',
  'act:br': 'Deep inspiration: posterior cricoarytenoids rotate the arytenoids outward and the glottis opens wide. In quiet breathing the '
            'muscles relax and the glottis is a narrow slit.',
  'act:ph': 'Phonation: the folds come together and air from the lungs vibrates them. The larynx makes the tone; lips, tongue and '
            'soft palate articulate it; mouth, nose, sinuses, pharynx and chest resonate it — block the nose and you hear the cold voice.',
  'act:wh': 'Whispering: lateral cricoarytenoids bring the folds together in front, but the arytenoid muscles relax and the arytenoids stay '
            'apart, so air passes between them without making a tone.',
  'act:va': 'Valsalva and swallowing: a stronger adduction seals the glottis, and in swallowing the laryngeal inlet closes too.',
  'act:hi': 'Pitch rises when cricothyroid tilts the thyroid cartilage and stretches the folds.',
  'lx:rln': 'Recurrent laryngeal injury: the paralyzed fold can’t move to meet the normal one — hoarseness, and dysphagia after a '
            'thyroidectomy injury. Risks include thyroidectomy (near the inferior thyroid a.), Pancoast tumor, '
            'lung cancer and Ortner syndrome (a big left atrium in mitral stenosis). The left nerve loops under the aortic arch, the right '
            'under the subclavian.',
  'lx:ext': 'External branch injury, usually when the superior thyroid pedicle is tied: cricothyroid can’t vary the folds’ length and '
            'tension, so the voice is monotonous and loses its tenor — noticed by singers and speakers. Pitch can’t rise.',
  'lx:nod': 'Nodules are bilateral, in smokers and people who strain their voice (singer’s nodules): progressive hoarseness, almost no cancer risk.',
  'lx:pol': 'A polyp is by convention unilateral, with the same causes and look as nodules — hoarseness, almost no cancer risk.',
  'lx:pap': 'Laryngeal papillomas: HPV-6/11, in children possibly acquired during delivery. On or below the folds they cause hoarseness; '
            'above them, dysphagia.',
}

dyn = dict(
  kinds=dict(air=['mov', '--nf-h2o'], tone=['mov', '--dk9'], sig=['mov', '--dk7']),
  groups=[['mov', 'Air · sound · nerve signal']],
  switches=[dict(id='act', label='Larynx is…', type='steps', options=[
              ['br', 'Deep breath in', 'larynxmus'], ['ph', 'Speaking', 'vocalize'], ['wh', 'Whispering', 'larynxmus'],
              ['va', 'Straining · swallowing', 'larynxmus'], ['hi', 'Singing high', 'larynxmus']]),
            dict(id='lx', label='Lesion', type='one', options=[
              ['rln', 'Left recurrent laryngeal palsy', 'laryngealnerves'], ['ext', 'External branch injury', 'laryngealnerves'],
              ['nod', 'Vocal fold nodules', 'vcnodule'], ['pol', 'Vocal fold polyp', 'vcnodule'], ['pap', 'Laryngeal papillomas', 'laryngealpap']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 286, 288, 347, 638, 690, 703–704 · Moore ch 8 · Guyton ch 38 · Robbins ch 16')

MAP = dict(
  id='voxsim', title='Larynx & Voice in Motion', topic='eent', after='larynx',
  sub='Breathe, speak, whisper, strain and sing high, and watch which muscle moves the vocal folds and which nerve runs it — then cut a '
      'recurrent or superior laryngeal nerve, or grow nodules, a polyp or papillomas',
  w=3600, h=1900,
  fa='286, 288, 347, 638, 690, 703, 704',
  src=['Moore ch 8 — Neck', 'Guyton ch 38 — Pulmonary Ventilation', 'Robbins ch 16 — Head and neck'],
  lanes=[('vxMus', 'Muscles & voice', 'tca'), ('vxNrv', 'Nerves & lesions', 'glycolysis')],
  nodes=[
    ('vx1', 'Laryngeal muscles', 300, 1720, 'vxMus', 'abduct · adduct · tense', ['larynxmus'], 'hub'),
    ('vx2', 'Voice: tone & resonance', 700, 1720, 'vxMus', 'larynx · mouth · sinuses', ['vocalize']),
    ('vx3', 'Laryngeal nerves', 1100, 1720, 'vxNrv', 'recurrent · superior', ['laryngealnerves']),
    ('vx4', 'Vocal fold nodules & polyps', 1500, 1720, 'vxNrv', 'hoarseness', ['vcnodule']),
    ('vx5', 'Laryngeal papillomas', 1900, 1720, 'vxNrv', 'HPV-6/11', ['laryngealpap'])],
  panels=[
    (2500, PANY, 1000, 'Who moves the folds (Moore ch 8)', [
      ('Open', 'posterior cricoarytenoid'), ('Close', 'lateral cricoarytenoid, arytenoids'), ('Tense', 'cricothyroid · ext. sup. laryngeal'),
      ('All the rest', 'recurrent laryngeal')])],
  dyn=dyn)
