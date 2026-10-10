# Vertigo in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Both inner ears (semicircular canals, utricle and saccule, cochlea) send resting signals along CN VIII to the vestibular
# nuclei, which compare the two sides and drive the eyes through the MLF; the facial nerve leaves the same region. A `one`
# switch turns the head, runs a warm or cold caloric test, or shows BPPV, Ménière disease, vestibular neuritis,
# labyrinthitis, a vestibular schwannoma, an AICA or PICA stroke and Bell palsy. The pupils show the nystagmus: a slow drift
# then a jump (the fast phase it is named for). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
PANY = 1180
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
M = lambda x: 2500 - x          # the right ear mirrors the left around the midline (x 1250)
FAST_L = O('turnl', 'warm')
FAST_R = O('cold', 'neur', 'lab', 'schwan')   # UNVERIFIED: direction for a one-sided loss — derived (see notes)
VERT = O('aica', 'pica')
NYS = FAST_L + FAST_R + VERT

text('Vertigo — two inner ears, compared in the brainstem', 180, 150, 'dyn-big')
text('screen left = the patient’s left · lesions are drawn on the left', 180, 176, 'dyn-cap')

# ════════ the eyes ════════
EY = 300
for cx in (1130, 1370):
    add(f'<ellipse cx="{cx}" cy="{EY}" rx="70" ry="42" class="dyn-cell"/>')
    add(f'<circle cx="{cx}" cy="{EY}" r="20" style="fill:var(--dk9)"/>', unless=NYS)
text('the eyes: drift = slow phase · jump = fast phase', 180, 202, 'dyn-cap')
text('attacks: peripheral nystagmus — horizontal-torsional, one direction', 1250, 226, 'nf-l1 dyn-tag', 'middle', when=O('bppv', 'meniere'))
text('fast phase left — toward the turn', 1250, 226, 'nf-l1 dyn-tag', 'middle', when=FAST_L)
text('fast phase right — away from the weak left side', 1250, 226, 'nf-l1 dyn-tag', 'middle', when=FAST_R)
text('central: any direction, even purely vertical; fixation doesn’t stop it', 1250, 226, 'nf-l1 dyn-tag', 'middle', when=VERT)

# ════════ the brainstem ════════
add('<rect x="1040" y="470" width="420" height="490" rx="40" class="dyn-soft"/>')
text('brainstem', 1250, 940, 'nf-l2', 'middle')
add('<path d="M1130 660 L1370 360 M1370 660 L1130 360" class="dyn-line"/>')
text('vestibulo-ocular reflex (MLF)', 1490, 430, 'nf-l2')
for cx in (1130, 1370):
    add(f'<circle cx="{cx}" cy="660" r="26" style="fill:var(--dk2);fill-opacity:.35;stroke:var(--dk2);stroke-width:3"/>')
    add(f'<circle cx="{cx - 20 if cx < 1250 else cx + 20}" cy="780" r="16" style="fill:var(--dk7);fill-opacity:.35;stroke:var(--dk7);stroke-width:3"/>')
text('vestibular nuclei — compare the sides', 1250, 720, 'nf-l2', 'middle')
add('<circle cx="1090" cy="880" r="16" style="fill:var(--dk5);fill-opacity:.35;stroke:var(--dk5);stroke-width:3"/>')
text('VII nucleus', 1120, 885, 'nf-l2')

# ════════ the inner ears (left drawn, right mirrored) ════════
def ear(f, side):
    a = 'middle'
    add(f'<circle cx="{f(520)}" cy="480" r="75" style="fill:none;stroke:var(--nf-h2o);stroke-width:12;opacity:.7"/>')
    add(f'<circle cx="{f(380)}" cy="600" r="75" style="fill:none;stroke:var(--nf-h2o);stroke-width:12;opacity:.7"/>')
    add(f'<circle cx="{f(380)}" cy="780" r="75" style="fill:none;stroke:var(--nf-h2o);stroke-width:12;opacity:.7"/>')
    add(f'<ellipse cx="{f(560)}" cy="640" rx="75" ry="50" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--nf-h2o);stroke-width:3"/>')
    add(f'<path d="M{f(720)} 800 m-55 0 a55 55 0 1 0 110 0 a40 40 0 1 0 -80 0 a24 24 0 1 0 48 0" style="fill:none;stroke:var(--dk7);stroke-width:8"/>')
    text('semicircular canals', f(400), 380, 'nf-l2', a)
    text('utricle · saccule', f(560), 730, 'nf-l2', a)
    text('cochlea', f(720), 900, 'nf-l2', a)
    text('vestibular nerve (VIII)', f(850), 600, 'nf-l2', a)
    text(f'{side} ear', f(560), 300, 'nf-l1', a)
ear(lambda x: x, 'Left'); ear(M, 'Right')

# ════════ the face (left) ════════
add('<path d="M1076 890 C900 980 760 1080 640 1130" class="dyn-line"/>')
text('facial nerve (VII)', 760, 1010, 'nf-l2', 'middle')
add('<circle cx="540" cy="1180" r="90" class="dyn-cell"/>')
add('<path d="M500 1120 h80 M500 1136 h80" style="stroke:var(--ink-3);stroke-width:3"/>', unless=O('bell', 'aica'))
add('<path d="M495 1225 Q540 1250 585 1225" style="fill:none;stroke:var(--ink-2);stroke-width:4"/>', unless=O('bell', 'aica'))
add('<path d="M495 1240 Q540 1240 585 1222" style="fill:none;stroke:var(--bad);stroke-width:4"/>', when=O('bell', 'aica'))
text('left face', 540, 1300, 'nf-l2', 'middle')
text('whole left face weak, forehead too — LMN', 540, 1330, 'nf-l1 dyn-tag', 'middle', when=O('bell', 'aica'))

# ════════ lesions ════════
for (x, y) in ((360, 650), (372, 660), (384, 648)):
    add(f'<circle cx="{x}" cy="{y}" r="7" style="fill:var(--ink-2)"/>', when=O('bppv'))
text('loose otoconia in a canal', 380, 560, 'nf-l1 dyn-tag', 'middle', when=O('bppv'))
add('<ellipse cx="560" cy="640" rx="95" ry="66" style="fill:var(--nf-h2o);fill-opacity:.5;stroke:var(--bad);stroke-width:4"/>', when=O('meniere'))
text('too much endolymph', 560, 560, 'nf-l1 dyn-tag', 'middle', when=O('meniere'))
add(X(850, 628), when=O('neur', 'lab'))
add('<path d="M720 800 m-60 0 a60 60 0 1 0 120 0" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=O('lab', 'meniere'))
add('<ellipse cx="985" cy="650" rx="44" ry="38" style="fill:var(--dk4);fill-opacity:.55;stroke:var(--dk4);stroke-width:3"/>', when=O('schwan'))
text('schwannoma at the CPA', 985, 720, 'nf-l1 dyn-tag', 'middle', when=O('schwan'))
add(X(560, 640) + X(1090, 880), when=O('aica'))
text('AICA — lateral pons + labyrinthine artery', 1250, 1040, 'nf-l1 dyn-tag', 'middle', when=O('aica'))
add(X(1130, 660), when=O('pica'))
text('PICA — lateral medulla: hoarseness, dysphagia, crossed pain loss, Horner', 1250, 1040, 'nf-l1 dyn-tag', 'middle', when=O('pica'))
add(X(900, 1012), when=O('bell'))
text('warm water →', 300, 470, 'nf-l1 dyn-tag', 'end', when=O('warm'))
text('cold water →', 300, 470, 'nf-l1 dyn-tag', 'end', when=O('cold'))
text('↶ head turns left', 1250, 1040, 'nf-l1 dyn-tag', 'middle', when=O('turnl'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
VN = 'M635 630 C800 620 950 640 1104 655'
CN = 'M760 790 C880 780 960 770 1090 780'
VNR = f'M{M(635)} 630 C{M(800)} 620 {M(950)} 640 {M(1104)} 655'
CNR = f'M{M(760)} 790 C{M(880)} 780 {M(960)} 770 {M(1090)} 780'
LOW_L = O('cold', 'neur', 'lab', 'schwan', 'aica')
flows = [
  dict(d=VN, len=480, speed=150, r=7, base=dict(sig=3), mods=[m(FAST_L, set=dict(sig=6)), m(LOW_L, set=dict(sig=1))]),
  dict(d=VNR, len=480, speed=150, r=7, base=dict(sig=3), mods=[m(O('turnl'), set=dict(sig=1))]),
  dict(d=CN, len=340, speed=130, r=7, base=dict(snd=3), mods=[m(O('meniere', 'lab', 'schwan', 'aica'), set=dict(snd=1))]),
  dict(d=CNR, len=340, speed=130, r=7, base=dict(snd=3)),
  dict(d='M1076 890 C900 980 760 1080 640 1130', len=500, speed=150, r=7, base=dict(mot=3), mods=[m(O('bell', 'aica'), set=dict(mot=0))]),
]
for cx in (1130, 1370):
    flows += [dict(d=f'M{cx - 24} {EY} H{cx + 24}', len=48, speed=32, r=20, base=dict(eye=1), when=FAST_L),
              dict(d=f'M{cx + 24} {EY} H{cx - 24}', len=48, speed=32, r=20, base=dict(eye=1), when=FAST_R),
              dict(d=f'M{cx} {EY - 20} V{EY + 20}', len=40, speed=28, r=20, base=dict(eye=1), when=VERT)]
sites = [
  dict(x=1250, y=800, n=[0, 1], w=10, t='rec', l='', aria='Vestibular system', c='vestibular', ions=[]),
  dict(x=720, y=800, n=[0, 1], w=10, t='rec', l='', aria='Hearing loss', c='hearingloss', ions=[]),
  dict(x=540, y=1180, n=[0, 1], w=10, t='rec', l='', aria='Facial nerve', c='bell', ions=[]),
]

readouts = [
  dict(l='Vertigo', mods=[dict(when=O('bppv', 'meniere', 'neur', 'lab', 'aica'), d=1)]),
  dict(l='Left hearing', mods=[dict(when=O('meniere', 'lab', 'schwan', 'aica'), d=-1), dict(when=O('bppv', 'neur', 'bell'), d=0)]),
  dict(l='Left vestibular nerve firing', mods=[dict(when=FAST_L, d=1), dict(when=LOW_L, d=-1)]),
  dict(l='Left facial movement', mods=[dict(when=O('bell', 'aica'), d=-1), dict(when=O('meniere', 'neur', 'bppv'), d=0)]),
  dict(l='Other brainstem signs', mods=[dict(when=VERT, d=1), dict(when=O('bppv', 'meniere', 'neur', 'lab'), d=0)]),
]

notes = {
  '': 'Three semicircular canals sense turning and the utricle and saccule sense tilt and linear motion. Both vestibular nerves '
      'fire at rest; the vestibular nuclei compare the two sides and drive the eyes through the MLF (the vestibulo-ocular reflex).',
  'dx:turnl': 'Turning the head left excites the left horizontal canal and inhibits the right. The eyes drift right to hold gaze '
              '(slow phase), then jump left, the way the head turns (fast phase) — nystagmus is named for the fast phase.',
  'dx:warm': 'Caloric test, warm water in the left ear: with the head tilted back 60° the endolymph moves as if the head had turned — '
             'nystagmus toward the treated side. COWS: cold opposite, warm same.',
  'dx:cold': 'Caloric test, cold water in the left ear: nystagmus toward the untreated (right) side. COWS: cold opposite, warm same.',
  'dx:bppv': 'BPPV: loose otoconia drift into a semicircular canal and move with gravity, so rolling over, looking up or lying back '
             'brings a minute or less of vertigo. No hearing loss. Dix-Hallpike reproduces it; the Epley maneuver repositions the debris.',
  'dx:meniere': 'Ménière disease: too much endolymph distends the membranous labyrinth — episodic vertigo, sensorineural hearing loss '
                'and tinnitus (“men wear vests”), with peripheral-type nystagmus during attacks.',
  'dx:neur': 'Vestibular neuritis: the inflamed left nerve fires less, and the nuclei read the imbalance as a head turn away from the '
             'weak side — sudden severe continuous vertigo and vomiting, hearing intact, no central signs.',
  'dx:lab': 'Labyrinthitis: the whole labyrinth is inflamed, so the same vertigo comes with sensorineural hearing loss — viral (mumps, '
            'rubella) or bacterial (meningitis).',
  'dx:schwan': 'Vestibular schwannoma: a benign Schwann-cell tumor on CN VIII at the cerebellopontine angle — one-sided '
               'sensorineural hearing loss, tinnitus and an unsteady gait; large ones reach CN V and VII. Bilateral = NF2.',
  'dx:aica': 'AICA stroke (lateral pons): the facial nucleus (whole-face LMN weakness, specific to AICA), vestibular and cochlear nuclei, '
             'and through the labyrinthine artery the inner ear — deafness, vertigo, nystagmus — plus crossed pain loss, Horner, ataxia.',
  'dx:pica': 'PICA or vertebral stroke (lateral medulla, Wallenberg): nucleus ambiguus (hoarseness, dysphagia), spinal trigeminal '
             'nucleus, spinothalamic tract, sympathetics, vestibular nuclei and inferior cerebellar peduncle.',
  'dx:bell': 'Bell palsy: the facial nerve itself (LMN), so the whole left face is weak, forehead included; hyperacusis and lost taste '
             'on the front of the tongue. A stroke (UMN) would spare the forehead. Hearing and balance are untouched.',
}

dyn = dict(
  kinds=dict(sig=['nerve', '--dk2'], snd=['nerve', '--dk7'], mot=['nerve', '--dk5'], eye=['eyes', '--dk9']),
  groups=[['nerve', 'Nerve signals'], ['eyes', 'Eye movement']],
  switches=[dict(id=SW, label='Test · what goes wrong (left side)', type='one', options=[
    ['turnl', 'Head turns left', 'vestibular'], ['warm', 'Warm water, left ear', 'nystagmus'],
    ['cold', 'Cold water, left ear', 'nystagmus'], ['bppv', 'BPPV', 'bppv'], ['meniere', 'Ménière disease', 'meniere'],
    ['neur', 'Vestibular neuritis', 'vestneuritis'], ['lab', 'Labyrinthitis', 'vestneuritis'],
    ['schwan', 'Vestibular schwannoma', 'schwannoma'], ['aica', 'AICA stroke', 'aicastroke'],
    ['pica', 'PICA stroke (Wallenberg)', 'wallenberg'], ['bell', 'Bell palsy', 'bell']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 526–527, 540, 546–548 · Costanzo ch 3 · Fundamental Neuroscience ch 22')

MAP = dict(
  id='vestsim', title='Vertigo in Motion', topic='eent', after='cochflow',
  sub='Two inner ears compared in the brainstem: turn the head, run a caloric test, then watch the eyes beat in BPPV, Ménière '
      'disease, vestibular neuritis, labyrinthitis, a vestibular schwannoma, AICA and PICA strokes and Bell palsy',
  w=3600, h=1900,
  fa='166, 240, 506, 526, 527, 540, 546, 547, 548, 705',
  src=['Costanzo ch 3 — Neurophysiology', 'Fundamental Neuroscience ch 22 — The Vestibular System',
       'Fundamental Neuroscience ch 28 — Visual Motor Systems', 'Pawlina ch 25 — Ear', 'Katzung ch 15 — Diuretic Agents',
       'Fundamental Neuroscience ch 21 — The Auditory System', 'Robbins ch 27 — Peripheral nerves and skeletal muscles',
       'Robbins ch 28 — The central nervous system', 'Fundamental Neuroscience ch 14 — A Synopsis of Cranial Nerves of the Brainstem',
       'Fundamental Neuroscience ch 10 — An Overview of the Brainstem', 'Moore ch 9 — Head', 'Robbins ch 8 — Infectious diseases',
       'Moore ch 10 — Cranial Nerves', 'Guyton ch 53 — The Sense of Hearing',
       'Katzung ch 62 — Drugs Used in the Treatment of Gastrointestinal Diseases',
       'Katzung ch 16 — Histamine, Serotonin, Anti-Obesity Drugs, & the Ergot Alkaloids', 'Katzung ch 8 — Cholinoceptor-Blocking Drugs',
       'Guyton ch 67 — Physiology of Gastrointestinal Disorders', 'Bootcamp.com Pharmacology — Autonomic system',
       'Bootcamp.com Neurology — Vertigo'],
  lanes=[('vbNorm', 'How balance works', 'glycolysis'), ('vbPer', 'Inner ear causes', 'tca'), ('vbCen', 'Nerve & brainstem causes', 'gluconeo')],
  nodes=[
    ('vs1', 'Vestibular system', 330, 1620, 'vbNorm', 'canals · otoliths · VOR', ['vestibular', 'nystagmus'], 'hub'),
    ('vs2', 'Peripheral vs central', 760, 1620, 'vbNorm', 'who else is sick?', ['vertigo']),
    ('vs3', 'Hearing loss', 1200, 1620, 'vbNorm', 'Weber · Rinne', ['hearingloss']),
    ('vs4', 'Motion sickness drugs', 1640, 1620, 'vbNorm', 'scopolamine · meclizine', ['motionrx']),
    ('vs5', 'BPPV', 330, 1760, 'vbPer', 'rolls over → spins', ['bppv']),
    ('vs6', 'Ménière disease', 760, 1760, 'vbPer', 'men wear vests', ['meniere']),
    ('vs7', 'Vestibular neuritis', 1200, 1760, 'vbPer', 'hearing intact', ['vestneuritis']),
    ('vs8', 'Vestibular schwannoma', 1640, 1760, 'vbCen', 'CPA · NF2', ['schwannoma']),
    ('vs9', 'AICA · PICA strokes', 2080, 1760, 'vbCen', 'face vs hoarseness', ['aicastroke', 'wallenberg']),
    ('vs10', 'Bell palsy', 2080, 1620, 'vbCen', 'forehead involved', ['bell'])],
  panels=[
    (2500, PANY, 1000, 'Peripheral vs central nystagmus (First Aid p. 548)', [
      ('Inner ear', 'horizontal-torsional, one direction'),
      ('', 'suppressed by visual fixation'),
      ('Brainstem · cerebellum', 'any direction, even purely vertical'),
      ('', 'not suppressed; diplopia, ataxia, dysmetria'),
      ('Caloric test', 'COWS: cold opposite, warm same')])],
  dyn=dyn)
