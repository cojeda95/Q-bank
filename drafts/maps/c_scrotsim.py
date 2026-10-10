# The Scrotum in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Front view: aorta, IVC, both kidneys, the testicular arteries and the gonadal veins — the left gonadal vein meets the left
# renal vein at a right angle, the right one drains straight into the IVC. A close-up testis with the epididymis behind it and
# the tunica vaginalis around it. A `one` switch shows torsion (bell clapper), epididymitis, left varicocele, right varicocele
# (IVC obstruction, e.g. renal cell carcinoma), hydrocele, spermatocele, cryptorchidism and a germ cell tumor; two toggles
# run the bedside tests — lift the scrotum (Prehn sign) and shine a light (transillumination). 5 readouts. The descent path
# is drawn as a schematic only — no card gives its stages. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

text('The scrotum — veins, the testis in its tunica, and the bedside tests', 180, 150, 'dyn-big')
text('front view (patient’s left on your right) · close-up of one testis from the side', 180, 176, 'dyn-cap')

# ════════ front view ════════
IVC, AO = 820, 960
add(f'<path d="M{IVC} 300 V1000" style="stroke:var(--nf-h2o);stroke-width:34;opacity:.35"/>'); text('IVC', IVC, 280, 'nf-l1', 'middle')
add(f'<path d="M{AO} 300 V1000" style="stroke:var(--nf-blood);stroke-width:30;opacity:.35"/>'); text('aorta', AO, 280, 'nf-l1', 'middle')
add('<ellipse cx="560" cy="500" rx="70" ry="110" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/>')
add('<ellipse cx="1320" cy="480" rx="70" ry="110" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/>')
text('R kidney', 560, 640, 'nf-l2', 'middle'); text('L kidney', 1320, 620, 'nf-l2', 'middle')
add(f'<path d="M630 520 H{IVC}" style="stroke:var(--nf-h2o);stroke-width:16;opacity:.5"/>')
add(f'<path d="M1250 480 H{IVC}" style="stroke:var(--nf-h2o);stroke-width:16;opacity:.5"/>'); text('left renal vein', 1100, 460, 'nf-l2', 'middle')
# gonadal veins
add(f'<path d="M760 1240 C740 1000 790 820 {IVC} 760" style="fill:none;stroke:var(--nf-h2o);stroke-width:8;opacity:.6"/>')
add('<path d="M1100 1240 C1150 1000 1200 700 1200 480" style="fill:none;stroke:var(--nf-h2o);stroke-width:8;opacity:.6"/>')
text('R gonadal → IVC', 660, 900, 'nf-l2', 'end'); text('L gonadal → renal vein at a right angle', 1230, 820, 'nf-l2')
add('<path d="M1200 488 v-16 h16" style="fill:none;stroke:var(--ink-2);stroke-width:3"/>')
# scrotum + testes
add('<path d="M640 1160 C620 1480 1220 1480 1220 1160 Z" style="fill:var(--dk3);fill-opacity:.08;stroke:var(--dk3);stroke-width:4"/>')
text('scrotum', 930, 1480, 'nf-l1', 'middle')
add('<ellipse cx="760" cy="1300" rx="60" ry="80" style="fill:var(--dk4);fill-opacity:.3;stroke:var(--dk4);stroke-width:4"/>')
add('<ellipse cx="1100" cy="1300" rx="60" ry="80" style="fill:var(--dk4);fill-opacity:.3;stroke:var(--dk4);stroke-width:4"/>', unless=D('crypt'))
add('<ellipse cx="1100" cy="1300" rx="60" ry="80" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:6 6"/>', when=D('crypt'))
add('<ellipse cx="1180" cy="960" rx="50" ry="66" style="fill:var(--dk4);fill-opacity:.3;stroke:var(--bad);stroke-width:4"/>', when=D('crypt'))
add('<path d="M1300 640 C1300 820 1220 900 1120 1220" style="fill:none;stroke:var(--ink-3);stroke-width:3;stroke-dasharray:4 10"/>')
text('descent path (schematic)', 1320, 700, 'nf-l2')
text('stopped short — kept at body temperature', 1250, 1000, 'nf-l1 dyn-tag', when=D('crypt'))
# varicocele bag of worms
for i in range(5):
    add(f'<path d="M{1060 + i * 18} 1220 c-14 -30 14 -50 0 -80 c-14 -30 14 -50 0 -80" style="fill:none;stroke:var(--nf-h2o);stroke-width:7"/>', when=D('varic'))
    add(f'<path d="M{720 + i * 18} 1220 c-14 -30 14 -50 0 -80 c-14 -30 14 -50 0 -80" style="fill:none;stroke:var(--nf-h2o);stroke-width:7"/>', when=D('rvaric'))
add(f'<rect x="{IVC - 30}" y="500" width="60" height="44" rx="10" style="fill:var(--bad);opacity:.7"/>', when=D('rvaric'))
text('tumor in the renal vein / IVC (renal cell carcinoma)', IVC - 50, 590, 'nf-l1 dyn-tag', 'end', when=D('rvaric'))
text('bag of worms — worse standing and with Valsalva', 1250, 1120, 'nf-l1 dyn-tag', when=D('varic'))
text('right-sided — look for IVC obstruction', 600, 1120, 'nf-l1 dyn-tag', 'end', when=D('rvaric'))

# ════════ close-up testis ════════
CX, CY = 1960, 960
add(f'<ellipse cx="{CX}" cy="{CY}" rx="250" ry="300" style="fill:var(--surface);stroke:var(--dk7);stroke-width:4;stroke-dasharray:10 6"/>', unless=D('hydro'))
add(f'<ellipse cx="{CX}" cy="{CY}" rx="290" ry="340" style="fill:var(--nf-h2o);fill-opacity:.3;stroke:var(--dk7);stroke-width:5"/>', when=D('hydro'))
text('tunica vaginalis', CX - 270, CY - 300, 'nf-l2', 'end')
add(f'<ellipse cx="{CX}" cy="{CY}" rx="140" ry="200" style="fill:var(--dk4);fill-opacity:.3;stroke:var(--dk4);stroke-width:5"/>', unless=D('torsion'))
add(f'<ellipse cx="{CX}" cy="{CY - 40}" rx="200" ry="130" style="fill:var(--dk10);fill-opacity:.45;stroke:var(--bad);stroke-width:5"/>', when=D('torsion'))
text('testis', CX - 40, CY + 10, 'nf-l1', 'middle', unless=D('torsion'))
add(f'<path d="M{CX + 150} {CY - 190} C{CX + 230} {CY - 100} {CX + 220} {CY + 120} {CX + 140} {CY + 200}" style="fill:none;stroke:var(--dk5);stroke-width:30;stroke-linecap:round;opacity:.6"/>', unless=D('epi'))
add(f'<path d="M{CX + 150} {CY - 190} C{CX + 230} {CY - 100} {CX + 220} {CY + 120} {CX + 140} {CY + 200}" style="fill:none;stroke:var(--bad);stroke-width:46;stroke-linecap:round;opacity:.6"/>', when=D('epi'))
text('epididymis (posterior)', CX + 260, CY + 30, 'nf-l2')
# cord
add(f'<path d="M{CX + 60} 420 V{CY - 200}" style="stroke:var(--dk6);stroke-width:26;opacity:.4"/>', unless=D('torsion'))
add(f'<path d="M{CX + 60} 420 c-40 30 40 60 0 90 c-40 30 40 60 0 90 c-40 30 40 60 0 90" style="fill:none;stroke:var(--bad);stroke-width:22;opacity:.6"/>', when=D('torsion'))
text('spermatic cord', CX + 100, 440, 'nf-l2')
text('bell clapper — testis lies horizontal and spins on its cord', CX, 1360, 'nf-l1 dyn-tag', 'middle', when=D('torsion'))
add(f'<circle cx="{CX + 190}" cy="{CY - 250}" r="60" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--dk5);stroke-width:4"/>', when=D('sperm'))
text('spermatocele — cyst of an epididymal duct', CX, 1360, 'nf-l1 dyn-tag', 'middle', when=D('sperm'))
text('hydrocele — serous fluid in the tunica vaginalis', CX, 1360, 'nf-l1 dyn-tag', 'middle', when=D('hydro'))
add(f'<path d="M{CX - 70} {CY + 20} c30 -60 110 -40 100 20 c-10 60 -90 70 -100 -20 Z" style="fill:var(--ink-3);fill-opacity:.7;stroke:var(--ink-2);stroke-width:3"/>', when=D('tumor'))
text('germ cell tumor — firm, painless mass', CX, 1360, 'nf-l1 dyn-tag', 'middle', when=D('tumor'))
text('epididymis tender behind the testis', CX, 1360, 'nf-l1 dyn-tag', 'middle', when=D('epi'))
# bedside tests
add(f'<circle cx="{CX}" cy="{CY}" r="300" style="fill:var(--accent);fill-opacity:.25"/>', when=['light&dx:hydro'])
add(f'<circle cx="{CX + 190}" cy="{CY - 250}" r="80" style="fill:var(--accent);fill-opacity:.35"/>', when=['light&dx:sperm'])
text('lights up — transilluminates', CX, 1400, 'nf-l1', 'middle', when=['light&dx:hydro', 'light&dx:sperm'])
text('does not transilluminate', CX, 1400, 'nf-l1', 'middle', when=['light&dx:tumor', 'light&dx:varic', 'light&dx:rvaric'])
text('Prehn negative — lifting does not ease the pain', CX, 1440, 'nf-l1', 'middle', when=['lift&dx:torsion'])
text('Prehn positive — lifting eases the pain', CX, 1440, 'nf-l1', 'middle', when=['lift&dx:epi'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{AO} 600 C{AO} 900 1080 1000 1100 1220', len=680, speed=120, r=8, base=dict(art=3), unless=D('crypt')),
  dict(d=f'M{AO} 600 C{AO} 900 760 1000 760 1220', len=680, speed=120, r=8, base=dict(art=3)),
  dict(d=f'M760 1240 C740 1000 790 820 {IVC} 760', len=520, speed=100, r=8, base=dict(ven=3), mods=[m(D('rvaric'), set=dict(ven=6), speed=0.15)]),
  dict(d=f'M1100 1240 C1150 1000 1200 700 1200 480 H{IVC}', len=1150, speed=100, r=8, base=dict(ven=4), unless=D('crypt'),
       mods=[m(D('varic'), set=dict(ven=8), speed=0.2)]),
  dict(d=f'M{IVC} 1000 V300', len=700, speed=120, r=9, base=dict(ven=4), mods=[m(D('rvaric'), speed=0.2)]),
  dict(d=f'M{CX + 60} 420 V{CY - 160}', len=380, speed=90, r=8, base=dict(art=2), mods=[m(D('torsion'), set=dict(art=0))]),
]
sites = [dict(x=CX + 60, y=500, n=[-1, 0], w=10, t='rec', l='', aria='Testicular torsion', c='torsion', ions=[]),
         dict(x=CX + 230, y=CY + 100, n=[1, 0], w=10, t='rec', l='', aria='Epididymitis', c='epididymitis', ions=[]),
         dict(x=1200, y=600, n=[1, 0], w=10, t='rec', l='', aria='Varicocele', c='varicocele', ions=[]),
         dict(x=CX - 250, y=CY + 120, n=[-1, 0], w=10, t='rec', l='', aria='Hydrocele', c='hydrocele', ions=[]),
         dict(x=1300, y=760, n=[1, 0], w=10, t='rec', l='', aria='Cryptorchidism', c='cryptorchid', ions=[]),
         dict(x=CX - 140, y=CY - 60, n=[-1, 0], w=10, t='rec', l='', aria='Germ cell tumor', c='testisgct', ions=[])]

readouts = [
  dict(l='Testis blood flow', mods=[dict(when=D('torsion'), d=-1)]),
  dict(l='Cremasteric reflex', mods=[dict(when=D('torsion'), d=-1)]),
  dict(l='Transilluminates', mods=[dict(when=D('hydro', 'sperm'), d=1), dict(when=D('tumor', 'varic', 'rvaric'), d=-1)]),
  dict(l='Testis temperature', mods=[dict(when=D('varic', 'rvaric', 'crypt'), d=1)]),
  dict(l='Spermatogenesis', mods=[dict(when=D('varic', 'crypt'), d=-1)]),
]

notes = {
  '': 'Each testis gets a testicular artery from the aorta. The right gonadal vein drains straight into the IVC; the left one meets '
      'the left renal vein at a right angle, so left-sided pressure is higher. Pick a problem, then lift the scrotum or shine a light.',
  'dx:torsion': 'Torsion: poorly fixed to the tunica vaginalis (bell clapper), the testis lies horizontally and twists — veins block '
                'first, then the artery. Boys 12–18, sudden pain, high-riding testis, no cremasteric reflex, Prehn negative. '
                'Detorsion and orchiopexy of both sides within 6 hours.',
  'dx:epi': 'Epididymitis: bacteria ascend from the urethra — Chlamydia and gonorrhea in young men, E coli and Pseudomonas in older '
            'men. Tender posterior testis; Prehn positive. Mumps can cause orchitis.',
  'dx:varic': 'Left varicocele: dilated pampiniform plexus — bag of worms, worse standing and with Valsalva, does not '
              'transilluminate. The warm pooled blood impairs spermatogenesis. Commonest cause of scrotal enlargement in adult men.',
  'dx:rvaric': 'Right varicocele: the right gonadal vein drains straight into the IVC, so a right-sided one suggests IVC obstruction — '
               'such as a renal cell carcinoma growing into the renal vein.',
  'dx:hydro': 'Hydrocele: serous fluid in the tunica vaginalis. Congenital ones come from a processus vaginalis that never closed — '
              'common in infants, most resolve within a year. Transilluminates.',
  'dx:sperm': 'Spermatocele: a cyst of a dilated epididymal duct or rete testis — a separate fluctuant nodule. Transilluminates.',
  'dx:crypt': 'Cryptorchidism: the testis never finishes descending. At body temperature Sertoli cells (heat-sensitive) fail — '
              'subfertility, ↓ inhibin B, ↑ FSH — while Leydig cells keep testosterone normal if unilateral. ↑ germ cell tumor '
              'risk. Orchiopexy before age 2.',
  'dx:tumor': 'Germ cell tumor: young man, painless firm mass that does not transilluminate. Radical orchiectomy — never a '
              'scrotal biopsy. Seminoma PLAP · yolk sac AFP · choriocarcinoma hCG.',
  'lift': 'Prehn sign: lifting the scrotum eases epididymitis pain but not torsion pain.',
  'light': 'Transillumination: fluid lights up (hydrocele, spermatocele); solid tumors and varicoceles do not.',
}

dyn = dict(
  kinds=dict(art=['mov', '--nf-blood'], ven=['mov', '--nf-h2o']), groups=[['mov', 'Arterial · venous blood']],
  switches=[dict(id='dx', label='Problem', type='one', options=[
              ['torsion', 'Torsion', 'torsion'], ['epi', 'Epididymitis', 'epididymitis'], ['varic', 'Left varicocele', 'varicocele'],
              ['rvaric', 'Right varicocele', 'varicocele'], ['hydro', 'Hydrocele', 'hydrocele'], ['sperm', 'Spermatocele', 'hydrocele'],
              ['crypt', 'Cryptorchidism', 'cryptorchid'], ['tumor', 'Germ cell tumor', 'testisgct']]),
            dict(id='lift', label='Test', type='toggle', on='Scrotum lifted', off='Lift the scrotum', def_=False),
            dict(id='light', label='Test', type='toggle', on='Light on', off='Shine a light', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 21')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='scrotsim', title='The Scrotum in Motion', topic='devrepro', after='malerepro',
  sub='Follow the testicular arteries and gonadal veins, then twist a testis, inflame the epididymis, dilate the pampiniform plexus, '
      'fill the tunica, leave a testis undescended or grow a tumor — and run the Prehn and transillumination tests',
  w=3600, h=1900,
  fa='669, 670, 671',
  src=['Robbins ch 21 — The lower urinary tract and male genital system', 'Moore ch 5 — Abdomen'],
  lanes=[('scAcute', 'Acute scrotum', 'tca'), ('scMass', 'Scrotal masses', 'glycolysis')],
  nodes=[
    ('sc1', 'Testicular torsion', 330, 1660, 'scAcute', 'Prehn −, no cremasteric', ['torsion'], 'hub'),
    ('sc2', 'Epididymitis & orchitis', 760, 1660, 'scAcute', 'Prehn +', ['epididymitis']),
    ('sc3', 'Varicocele', 1200, 1660, 'scMass', 'left · bag of worms', ['varicocele']),
    ('sc4', 'Hydrocele & spermatocele', 1640, 1660, 'scMass', 'transilluminate', ['hydrocele']),
    ('sc5', 'Cryptorchidism', 2080, 1660, 'scMass', 'heat · tumor risk', ['cryptorchid']),
    ('sc6', 'Germ cell tumors', 2520, 1660, 'scMass', 'firm · no light', ['testisgct'])],
  panels=[
    (2500, PANY, 1000, 'Bedside tests (Robbins ch 21)', [
      ('Prehn −', 'torsion'), ('Prehn +', 'epididymitis'), ('Lights up', 'hydrocele, spermatocele'),
      ('No light', 'tumor, varicocele')])],
  dyn=dyn)
