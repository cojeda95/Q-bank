# Aqueous Humor & Retina in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A schematic eye: the ciliary processes make aqueous humor, which flows from the posterior chamber through the pupil into the
# anterior chamber and out through the trabecular meshwork to the canal of Schlemm (90%) or the uveoscleral route (10%);
# behind it the retina with the central retinal artery and vein, macula and optic disc. A `one` switch shows open-angle and
# acute angle-closure glaucoma, uveitis, cataract, dry and wet AMD, diabetic retinopathy, retinal artery and vein occlusion,
# retinal detachment, retinitis pigmentosa and retinopathy of prematurity; a second gives a glaucoma drug (or a mydriatic,
# contraindicated in angle closure). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
LESS = R('tim', 'brim', 'acz'); MORE = R('lat', 'pilo')
HIGH = D('oag', 'acg')

text('The eye — aqueous humor in front, retina behind', 180, 150, 'dyn-big')
text('schematic cross-section · anterior segment enlarged on the left', 180, 176, 'dyn-cap')

# ════════ anterior segment ════════
add('<path d="M600 300 C380 420 380 900 600 1020" style="fill:none;stroke:var(--dk2);stroke-width:8"/>'); text('cornea', 420, 300, 'nf-l1')
add('<path d="M600 300 C380 420 380 900 600 1020 L760 1020 V300 Z" style="fill:var(--nf-h2o);fill-opacity:.12"/>')
text('anterior chamber', 490, 660, 'nf-l2', 'middle')
add('<path d="M620 320 L700 560 M620 1000 L700 760" style="stroke:var(--dk5);stroke-width:18;stroke-linecap:round"/>', unless=D('acg') + R('mydr'))
add('<path d="M620 340 L640 560 M620 980 L640 760" style="stroke:var(--dk5);stroke-width:28;stroke-linecap:round"/>', when=D('acg') + R('mydr'))
text('iris', 720, 520, 'nf-l2')
add('<ellipse cx="830" cy="660" rx="90" ry="200" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:4"/>', unless=D('cat'))
add('<ellipse cx="830" cy="660" rx="90" ry="200" style="fill:var(--ink-3);fill-opacity:.55;stroke:var(--ink-3);stroke-width:4"/>', when=D('cat'))
text('lens', 830, 666, 'nf-l1', 'middle')
for y0, y1 in ((300, 440), (880, 1020)):
    add(f'<rect x="740" y="{y0}" width="80" height="{y1 - y0}" rx="20" style="fill:var(--dk7);fill-opacity:.25;stroke:var(--dk7);stroke-width:3"/>')
text('ciliary body', 780, 280, 'nf-l2', 'middle')
add('<circle cx="610" cy="300" r="18" style="fill:var(--dk3);fill-opacity:.4;stroke:var(--dk3);stroke-width:3"/>'); text('canal of Schlemm', 560, 250, 'nf-l2', 'middle')
add('<path d="M592 312 L640 330" style="stroke:var(--ink-2);stroke-width:6;stroke-dasharray:4 4"/>'); text('trabecular meshwork · angle', 380, 360, 'nf-l2')
add(X(625, 320, 12), when=D('acg') + R('mydr'))
text('angle closed — iris blocks the meshwork', 560, 1080, 'nf-l1 dyn-tag', 'middle', when=D('acg'))
text('mydriatic in a narrow angle: closes it — contraindicated', 560, 1080, 'nf-l1 dyn-tag', 'middle', when=R('mydr'))
text('open angle, meshwork resists outflow', 560, 1080, 'nf-l1 dyn-tag', 'middle', when=D('oag'))
for (x, y) in ((470, 940), (500, 950), (530, 955)):
    add(f'<circle cx="{x}" cy="{y}" r="12" style="fill:var(--dk10);opacity:.8"/>', when=D('uve'))
text('hypopyon', 470, 1000, 'nf-l1 dyn-tag', 'middle', when=D('uve'))

# ════════ posterior: retina ════════
add('<path d="M900 300 C1500 120 2200 300 2250 660 C2200 1020 1500 1200 900 1020" style="fill:var(--dk1);fill-opacity:.05;stroke:var(--dk1);stroke-width:10"/>', unless=D('det'))
add('<path d="M900 300 C1500 120 2200 300 2250 660 C2200 1020 1500 1200 900 1020" style="fill:var(--dk1);fill-opacity:.05;stroke:var(--dk1);stroke-width:4"/>'
    '<path d="M1600 210 C1900 330 2050 500 2080 640" style="fill:none;stroke:var(--dk1);stroke-width:10;stroke-dasharray:14 6"/>', when=D('det'))
text('retina', 1580, 180, 'nf-l1', 'middle')
add('<circle cx="2210" cy="660" r="44" style="fill:var(--surface);stroke:var(--dk4);stroke-width:5"/>'); text('optic disc', 2210, 740, 'nf-l2', 'middle')
add('<circle cx="2210" cy="660" r="44" style="fill:none;stroke:var(--bad);stroke-width:5;stroke-dasharray:6 6"/>', when=HIGH)
text('disc cupping — optic nerve fibers die', 2210, 780, 'nf-l1 dyn-tag', 'middle', when=HIGH)
add('<circle cx="1980" cy="660" r="40" style="fill:var(--dk4);fill-opacity:.3"/>'); text('macula · fovea', 1980, 730, 'nf-l2', 'middle')
add('<circle cx="1980" cy="660" r="40" style="fill:var(--bad);fill-opacity:.5"/>', when=D('crao'))
text('cherry-red spot in a pale retina', 1980, 590, 'nf-l1 dyn-tag', 'middle', when=D('crao'))
for (x, y) in ((1950, 630), (2010, 690), (1990, 620)):
    add(f'<circle cx="{x}" cy="{y}" r="8" style="fill:var(--dk10)"/>', when=D('dry'))
text('drusen — central vision fades', 1980, 590, 'nf-l1 dyn-tag', 'middle', when=D('dry'))
add('<path d="M1950 700 q20 -40 40 0 t40 0" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=D('wet', 'dr', 'rop'))
text('choroidal new vessels leak and bleed — wavy lines', 1980, 590, 'nf-l1 dyn-tag', 'middle', when=D('wet'))
text('neovascularization → vitreous hemorrhage, traction', 1600, 1100, 'nf-l1 dyn-tag', 'middle', when=D('dr'))
text('hyperoxia stops vessel growth, then VEGF-driven new vessels', 1600, 1100, 'nf-l1 dyn-tag', 'middle', when=D('rop'))
text('“blood and thunder” — hemorrhages, dilated tortuous veins', 1600, 1100, 'nf-l1 dyn-tag', 'middle', when=D('crvo'))
text('flashes and floaters, then a dark curtain', 1600, 1100, 'nf-l1 dyn-tag', 'middle', when=D('det'))
for (x, y) in ((1200, 330), (1300, 1000), (1700, 1080), (1150, 980)):
    add(f'<path d="M{x} {y} l12 -18 l12 18 l-12 10 z" style="fill:var(--ink-2)"/>', when=D('rp'))
text('bone-spicule pigment — night blindness, periphery first', 1600, 1100, 'nf-l1 dyn-tag', 'middle', when=D('rp'))
text('hard lens — glare, worse at night, red reflex lost', 830, 1080, 'nf-l1 dyn-tag', 'middle', when=D('cat'))
VES = 'M2210 640 C2000 560 1700 420 1300 400'
VES2 = 'M2210 680 C2000 760 1700 900 1300 920'
add(f'<path d="{VES}" style="fill:none;stroke:var(--nf-blood);stroke-width:6;opacity:.45"/>'); text('central retinal artery', 1500, 420, 'nf-l2')
add(f'<path d="{VES2}" style="fill:none;stroke:var(--dk11);stroke-width:8;opacity:.45"/>'); text('central retinal vein', 1500, 950, 'nf-l2')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M760 440 C720 520 700 580 690 620', len=200, speed=50, r=8, base=dict(aq=3), mods=[m(LESS, set=dict(aq=1))]),
  dict(d='M690 640 C600 640 520 520 600 330', len=420, speed=70, r=8, base=dict(aq=3), mods=[m(D('acg') + R('mydr'), set=dict(aq=0)), m(D('oag'), set=dict(aq=1)), m(MORE, set=dict(aq=5))]),
  dict(d='M600 330 C560 260 520 240 470 240', len=150, speed=50, r=8, base=dict(aq=2), mods=[m(D('acg') + R('mydr'), set=dict(aq=0)), m(R('lat'), set=dict(aq=4))]),
  dict(d=VES, len=1000, speed=170, r=8, base=dict(bl=3), mods=[m(D('crao'), set=dict(bl=0))]),
  dict(d='M1300 920 C1700 900 2000 760 2210 680', len=1000, speed=170, r=8, base=dict(bl=3), mods=[m(D('crvo'), speed=0.25, set=dict(bl=6))]),
]
sites = [dict(x=610, y=318, n=[-1, 0], w=10, t='rec', l='', aria='Glaucoma', c='glaucoma', ions=[]),
         dict(x=780, y=1020, n=[0, 1], w=10, t='rec', l='', aria='Aqueous humor', c='aqueous', ions=[]),
         dict(x=820, y=440, n=[1, 0], w=10, t='rec', l='', aria='Glaucoma drugs', c='glaucomadrugs', ions=[]),
         dict(x=1930, y=660, n=[-1, 0], w=10, t='rec', l='', aria='Macular degeneration', c='amd', ions=[])]

readouts = [
  dict(l='Intraocular pressure', mods=[dict(when=HIGH + R('mydr'), d=1), dict(when=LESS + MORE, d=-1)]),
  dict(l='Aqueous production', mods=[dict(when=LESS, d=-1)]),
  dict(l='Aqueous outflow', mods=[dict(when=D('acg', 'oag') + R('mydr'), d=-1), dict(when=MORE, d=1)]),
  dict(l='Central vision', mods=[dict(when=D('dry', 'wet', 'crao', 'cat'), d=-1), dict(when=D('rp', 'oag'), d=0)]),
  dict(l='Peripheral vision', mods=[dict(when=D('oag', 'rp'), d=-1), dict(when=D('dry', 'wet'), d=0)]),
]

notes = {
  '': 'The ciliary processes secrete aqueous humor into the posterior chamber; it flows through the pupil into the anterior chamber and '
      'leaves through the trabecular meshwork into the canal of Schlemm (~90%) or the uveoscleral route (~10%). Normal pressure is '
      'about 15 mm Hg. Behind, the central retinal artery feeds the inner retina through end arteries.',
  'dx:oag': 'Open-angle glaucoma: the angle is open but the meshwork resists outflow — painless, found on screening; disc cupping, '
            'peripheral field loss first.',
  'dx:acg': 'Acute angle closure: the iris blocks the angle — sudden painful red eye, halos, headache, nausea, fixed mid-dilated pupil. '
            'Emergency: β-blocker, α₂ agonist, pilocarpine, acetazolamide, mannitol, then laser iridotomy. No mydriatics.',
  'dx:uve': 'Uveitis: inflamed iris, ciliary body or choroid — painful red eye, photophobia, hypopyon; HLA-B27, sarcoid, Behçet, JIA.',
  'dx:cat': 'Cataract: a cloudy lens — painless gradual loss with glare, worse at night; age, smoking, steroids, diabetes (sorbitol), '
            'galactosemia, rubella.',
  'dx:dry': 'Dry AMD: drusen under the retina, gradual loss of central vision; peripheral vision stays.',
  'dx:wet': 'Wet AMD: choroidal neovascularization leaks and bleeds — rapid loss, metamorphopsia. Anti-VEGF injections.',
  'dx:dr': 'Diabetic retinopathy: leaky, closing vessels (microaneurysms, hemorrhages, cotton-wool spots, exudates); the ischemic retina '
           'makes VEGF → proliferative new vessels, vitreous hemorrhage, tractional detachment.',
  'dx:crao': 'Central retinal artery occlusion: an embolus (usually carotid) — sudden painless monocular blindness, pale retina with a '
             'cherry-red spot at the fovea. Emergency: find the source.',
  'dx:crvo': 'Retinal vein occlusion: blood backs up into the retina — painless loss, blood-and-thunder fundus.',
  'dx:det': 'Retinal detachment: the neurosensory retina separates from the pigment epithelium and loses its choroidal supply — flashes, '
            'floaters, a dark curtain. High myopia, age, trauma. Surgical emergency.',
  'dx:rp': 'Retinitis pigmentosa: photoreceptors degenerate — night blindness and peripheral loss first; bone-spicule pigment.',
  'dx:rop': 'Retinopathy of prematurity: relative hyperoxia halts vessel growth; the avascular retina then makes VEGF and grows abnormal '
            'vessels → tractional detachment.',
  'rx:tim': 'Timolol (β-blocker): less aqueous made.', 'rx:brim': 'Brimonidine (α₂ agonist): less aqueous made.',
  'rx:acz': 'Acetazolamide, dorzolamide (carbonic anhydrase inhibitors): less aqueous made.',
  'rx:lat': 'Latanoprost (PGF₂α analogue): more uveoscleral outflow — darkens the iris, lengthens the lashes.',
  'rx:pilo': 'Pilocarpine, carbachol (M₃): ciliary muscle contraction opens the trabecular meshwork — used in acute angle closure.',
  'rx:mydr': 'Epinephrine and other mydriatics are contraindicated in closed-angle glaucoma.',
}

dyn = dict(
  kinds=dict(aq=['fluid', '--nf-h2o'], bl=['fluid', '--nf-blood']), groups=[['fluid', 'Aqueous · retinal blood']],
  switches=[dict(id='dx', label='Disease', type='one', options=[
              ['oag', 'Open-angle glaucoma', 'glaucoma'], ['acg', 'Acute angle closure', 'glaucoma'], ['uve', 'Uveitis', 'uveitis'],
              ['cat', 'Cataract', 'cataract'], ['dry', 'Dry AMD', 'amd'], ['wet', 'Wet AMD', 'amd'], ['dr', 'Diabetic retinopathy', 'retinopathy'],
              ['crao', 'Retinal artery occlusion', 'retinalocc'], ['crvo', 'Retinal vein occlusion', 'retinalocc'],
              ['det', 'Retinal detachment', 'retinaldetach'], ['rp', 'Retinitis pigmentosa', 'retinitispig'], ['rop', 'Retinopathy of prematurity', 'rop']]),
            dict(id='rx', label='Drug', type='one', options=[
              ['tim', 'Timolol', 'glaucomadrugs'], ['brim', 'Brimonidine', 'glaucomadrugs'], ['acz', 'Acetazolamide', 'glaucomadrugs'],
              ['lat', 'Latanoprost', 'glaucomadrugs'], ['pilo', 'Pilocarpine', 'glaucomadrugs'], ['mydr', 'Mydriatic (epinephrine)', 'glaucomadrugs']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 549–553, 557 · Robbins ch 29 · Katzung ch 7, 10')

MAP = dict(
  id='aqsim', title='Aqueous Humor & Retina in Motion', topic='eent', after='eyesim',
  sub='Follow aqueous humor from the ciliary body to the canal of Schlemm, close the angle or clog the meshwork, give glaucoma drugs — '
      'then look behind at cataract, AMD, diabetic retinopathy, artery and vein occlusion, detachment, RP and ROP',
  w=3600, h=1900,
  fa='475, 549, 550, 551, 552, 553, 557, 568',
  src=['Katzung ch 10 — Adrenoceptor Antagonist Drugs', 'Pawlina ch 24 — Eye', 'Robbins ch 29 — The eye',
       'Katzung ch 7 — Cholinoceptor-Activating & Cholinesterase-Inhibiting Drugs',
       'Katzung ch 18 — The Eicosanoids: Prostaglandins, Thromboxanes, Leukotrienes, & Related Compounds',
       'Guyton ch 50 — The Eye: I. Optics of Vision', 'Robbins ch 5 — Genetic disorders', 'Robbins ch 26 — Bones, joints, and soft tissue tumors',
       'Katzung ch 55 — Immunopharmacology', 'Katzung ch 60 — Special Aspects of Geriatric Pharmacology', 'Robbins ch 24 — The endocrine system',
       'Robbins ch 11 — Blood vessels', 'Moore ch 9 — Head', 'Robbins ch 10 — Diseases of infancy and childhood'],
  lanes=[('aqFront', 'Front of the eye', 'glycolysis'), ('aqRet', 'Retina', 'tca')],
  nodes=[
    ('aq1', 'Aqueous humor', 330, 1660, 'aqFront', '90% trabecular', ['aqueous'], 'hub'),
    ('aq2', 'Glaucoma · drugs', 760, 1660, 'aqFront', 'open vs closed', ['glaucoma', 'glaucomadrugs']),
    ('aq3', 'Uveitis', 1200, 1660, 'aqFront', 'hypopyon', ['uveitis']),
    ('aq4', 'Cataract', 1640, 1660, 'aqFront', 'cloudy lens', ['cataract']),
    ('aq5', 'Macular degeneration', 330, 1790, 'aqRet', 'drusen · anti-VEGF', ['amd']),
    ('aq6', 'Diabetic retinopathy', 760, 1790, 'aqRet', 'VEGF', ['retinopathy']),
    ('aq7', 'Retinal vessel occlusion', 1200, 1790, 'aqRet', 'cherry-red spot', ['retinalocc']),
    ('aq8', 'Detachment · RP · ROP', 1640, 1790, 'aqRet', 'curtain · spicules', ['retinaldetach', 'retinitispig', 'rop'])],
  panels=[
    (2500, PANY, 1000, 'Glaucoma drugs (First Aid p. 551)', [
      ('Less aqueous made', 'timolol, brimonidine, acetazolamide'),
      ('More outflow', 'latanoprost (uveoscleral), pilocarpine (trabecular)'),
      ('Acute angle closure', 'β-blocker, α₂, pilocarpine, acetazolamide, mannitol'),
      ('Never in angle closure', 'mydriatics (epinephrine)')])],
  dyn=dyn)
