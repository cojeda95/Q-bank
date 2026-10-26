# Vomiting & Antiemetics in Motion (dynamic map, kit data) — m57.
# The four inputs to the vomiting center drawn as one picture: the blood → chemoreceptor trigger zone (area postrema, no
# blood–brain barrier; D₂ · 5-HT₃ · NK₁), the vestibular labyrinth → CN VIII → the solitary nucleus (M₁ · H₁), gut
# enterochromaffin cells → 5-HT → 5-HT₃ on vagal afferents, and the cortex (anxiety, anticipation). The vomiting center
# drives the vomiting act (diaphragm + abdominal wall squeeze the stomach, vomitus rises up the esophagus). One `e` switch
# gives one antiemetic: its ✕ lands on the receptor it blocks, that input goes quiet, and its side effect is drawn
# (QT on a mini-ECG, LES tone and gastric emptying for metoclopramide). 7 readouts. No new cards.
#
# SOURCES (course wins): OCOM Gastro Exam 1 lecture notes, SDL 10 §3 "Antiemetic drug classes" (corpus/gastro/
# course_exam1_lecture_notes.txt p57–58) · Katzung ch 62 "Antiemetic agents" (the course pharm text, course_sdl_10_20_pharm.txt)
# · Katzung ch 16 (H₁ blockers: motion sickness, doxylamine + pyridoxine), ch 29 (olanzapine prolactin/EPS), ch 63
# (dronabinol CB₁) · Guyton ch 67 (vomiting act; CTZ drugs: apomorphine, morphine, digitalis) · FA 2025 pp. 407 (antiemetics
# table), 506 (vomiting center, five receptors), 240 (scopolamine), 247 (ondansetron QT), 705 (first-generation H₁ blockers).
# Readout rules: ↑ = sourced block/effect; ↔ only where a source says "no effect" (5-HT₃ antagonists: no D₂ block, no
# esophageal or gastric motility effect — Katzung; NK₁ antagonists: no serotonin or dopamine affinity — Katzung); "–" otherwise.
# CUTS: "metoclopramide contraindicated in bowel obstruction" (on the prokinetic card, not in course text/FA here) ·
# opioid receptors in the CTZ (Katzung, but no option uses them) · palonosetron no-QT detail · Guyton's vestibular →
# cerebellum → CTZ relay (drawn as CN VIII → solitary nucleus, as FA 506 and the lecture notes: "vestibular apparatus and
# solitary nucleus") · olanzapine EPS/prolactin arrow (see CONFLICTS) · QT arrow for olanzapine.
# CONFLICTS for the owner: (1) Lecture notes list the D₂-antagonist class (metoclopramide, prochlorperazine, promethazine,
# olanzapine) with EPS, hyperprolactinemia and QT prolongation; Katzung ch 29 says olanzapine causes "no or minimal"
# prolactin rise and less EPS. Shown: EPS·prolactin ↑ and QT ↑ for metoclopramide and prochlorperazine (lecture class
# list; FA 407 gives their EPS/hyperprolactinemia), "–" for olanzapine. (2) Dexamethasone mechanism: Katzung "unknown";
# lecture "incompletely understood; likely central anti-inflammatory effects and reduced blood–brain barrier
# permeability to emetogenic toxins" — note gives both as "likely".
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

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

E = lambda *k: [f'e:{x}' for x in k]
ANY = ['e:*']
PANX, PANY = 2500, 1290

text('Vomiting — four inputs, one center, five receptors', 180, 150, 'dyn-big')
text('pick an antiemetic: its ✕ lands on the receptor it blocks and that input goes quiet', 180, 176, 'dyn-cap')

# ════════ cortex (top) ════════
add('<path d="M1010 470 C960 380 1000 290 1100 258 C1200 226 1380 226 1470 270 C1560 318 1580 420 1530 480 '
    'C1500 515 1450 528 1405 515 C1370 552 1300 556 1255 532 C1190 548 1070 540 1010 470 Z" '
    'style="fill:var(--dk7);fill-opacity:.12;stroke:var(--dk7);stroke-width:4"/>')
add('<path d="M1290 250 C1270 320 1300 370 1270 430 M1120 470 C1200 440 1300 450 1400 488 M1060 330 q40 30 90 10 '
    'M1380 300 q40 40 100 20 M1150 400 q50 -30 100 0 M1350 400 q40 -25 90 5" '
    'style="fill:none;stroke:var(--dk7);stroke-width:3;opacity:.55"/>')
text('cortex', 1200, 300, 'nf-l1', 'middle')
text('anxiety · anticipatory vomiting', 1290, 625, 'nf-l2')
add('<path d="M1260 540 V690" class="dyn-line" marker-end="url(#ah-emIn)"/>')

# ════════ medulla: vomiting center (NTS) + CTZ ════════
add('<rect x="940" y="650" width="1270" height="390" rx="40" class="dyn-soft"/>')
text('medulla', 1600, 690, 'dyn-cap', 'middle')
add('<rect x="1000" y="700" width="500" height="300" rx="24" style="fill:var(--dk9);fill-opacity:.12;stroke:var(--dk9);stroke-width:4"/>')
text('Vomiting center', 1250, 760, 'dyn-big', 'middle')
text('nucleus tractus solitarius', 1250, 784, 'nf-l2', 'middle')
add('<rect x="1700" y="700" width="450" height="300" rx="24" style="fill:var(--dk4);fill-opacity:.12;stroke:var(--dk4);stroke-width:4"/>')
text('CTZ · area postrema', 1830, 740, 'nf-l1', 'middle')
text('no blood–brain barrier', 1830, 760, 'nf-l2', 'middle')
add('<path d="M1700 900 H1515" class="dyn-line" marker-end="url(#ah-emIn)"/>')
text('CTZ → center', 1600, 880, 'nf-l2', 'middle')
# CB₁ (dronabinol) and dexamethasone markers
add('<circle cx="1300" cy="940" r="20" style="fill:var(--accent);opacity:.85"/>', when=E('dro'))
text('CB₁ agonist', 1330, 946, 'nf-l1', when=E('dro'))
text('fewer toxins cross?', 1830, 980, 'nf-l2', 'middle', when=E('dex'))

# ════════ blood vessel → CTZ ════════
shapes.append({'vessel': 'M2290 600 V1160', 'w': 34})
text('blood', 2290, 588, 'nf-l1', 'middle')
text('chemotherapy · morphine', 2290, 1190, 'nf-l2', 'middle')
text('digitalis · toxins', 2290, 1208, 'nf-l2', 'middle')

# ════════ vestibular labyrinth (left) ════════
add('<path d="M420 760 a70 70 0 1 1 90 -10 M450 820 a80 60 0 1 1 -110 10 M480 800 a60 80 0 1 0 60 -110" '
    'style="fill:none;stroke:var(--dk5);stroke-width:12;stroke-linecap:round"/>')
add('<ellipse cx="470" cy="820" rx="60" ry="40" style="fill:var(--dk5);fill-opacity:.3;stroke:var(--dk5);stroke-width:4"/>')
add('<path d="M440 860 c-80 20 -90 110 -20 120 c60 8 70 -60 20 -66 c-30 -3 -34 30 -10 30" '
    'style="fill:none;stroke:var(--dk5);stroke-width:10;stroke-linecap:round"/>')
text('vestibular labyrinth', 450, 1030, 'nf-l1', 'middle')
text('motion', 450, 1050, 'nf-l2', 'middle')
add('<path d="M530 850 H950" class="dyn-line"/>')
text('CN VIII', 760, 822, 'nf-l1', 'middle')

# ════════ stomach, esophagus, duodenum (bottom) ════════
STOM = ('M640 1180 V1290 C500 1280 470 1470 600 1560 C760 1670 1230 1660 1440 1520 L1500 1480 L1500 1400 L1440 1400 '
        'C1250 1470 980 1450 860 1340 C820 1300 760 1290 740 1290 V1180 Z')
add(f'<path d="{STOM}" style="fill:var(--dk6);fill-opacity:.14;stroke:var(--dk6);stroke-width:5"/>')
shapes.append({'tube': 'M1500 1440 H1720 V1640', 'w': 46, 'color': '--dk6'})
text('stomach', 760, 1560, 'dyn-big', 'middle')
text('esophagus', 620, 1200, 'nf-l1', 'end')
text('duodenum', 1750, 1600, 'nf-l1')
add('<rect x="634" y="1272" width="112" height="22" rx="8" style="fill:var(--dk6);opacity:.55"/>')
text('LES', 620, 1290, 'nf-l2', 'end', unless=E('meto'))
add('<rect x="628" y="1266" width="124" height="34" rx="10" style="fill:var(--accent);opacity:.85"/>', when=E('meto'))
text('LES tone ↑', 620, 1290, 'nf-l1', 'end', when=E('meto'))
for x, y in [(1020, 1450), (1080, 1458), (1180, 1458), (1240, 1448)]:
    add(f'<rect x="{x - 12}" y="{y - 2}" width="24" height="18" rx="6" style="fill:var(--dk9);opacity:.6"/>')
text('EC cells: chemo · radiation · gastroenteritis', 1000, 1515, 'nf-l2', 'middle')
# vagal afferent + efferent drive
add('<path d="M1124 1420 V1015" class="dyn-line" marker-end="url(#ah-emIn)"/>')
text('vagal afferents (CN X)', 1104, 1120, 'nf-l1', 'end')
add('<path d="M1420 1005 V1385" class="dyn-line" marker-end="url(#ah-emOut)"/>')
text('vomiting act', 1440, 1150, 'nf-l1')
text('diaphragm + abdominal wall squeeze', 1440, 1170, 'nf-l2')
text('the stomach; the LES opens', 1440, 1188, 'nf-l2')
text('emptying faster', 1610, 1385, 'nf-l1', 'middle', when=E('meto'))

# ════════ mini ECG (QT) ════════
EX0, EY = 1830, 1360
text('ECG', EX0, 1290, 'nf-l1')
NORM = f'M{EX0} {EY} h50 q15 -25 30 0 h40 l10 15 l15 -110 l15 125 l10 -30 h40 q30 -45 60 0 h270'
LONG = f'M{EX0} {EY} h50 q15 -25 30 0 h40 l10 15 l15 -110 l15 125 l10 -30 h130 q30 -45 60 0 h180'
QTE = ['e:ond', 'e:meto', 'e:pcp']
add(f'<path d="{NORM}" class="dyn-trace"/>', unless=QTE)
add(f'<path d="{LONG}" class="dyn-trace"/>', when=QTE)
add(f'<path d="M{EX0 + 120} {EY + 40} H{EX0 + 290}" class="dyn-line"/>', unless=QTE)
add(f'<path d="M{EX0 + 120} {EY + 40} H{EX0 + 380}" style="stroke:var(--bad);stroke-width:5"/>', when=QTE)
text('QT', EX0 + 205, EY + 66, 'nf-l2', 'middle', unless=QTE)
text('QT prolonged', EX0 + 250, EY + 66, 'nf-l1', 'middle', when=QTE)

# ════════ one tag per drug ════════
TAG = dict(ond='5-HT₃ block on vagal afferents (and centrally) · headache, constipation, QT ↑, serotonin syndrome',
           nk1='NK₁ (substance P) block in the area postrema · delayed vomiting · CYP3A4 — halve dexamethasone',
           dex='no receptor blocked — boosts 5-HT₃ and NK₁ antagonists · insomnia, hyperglycemia',
           olz='D₂ + 5-HT₃ block · fourth drug for highly emetogenic chemotherapy · weight gain',
           meto='D₂ block in the CTZ and the gut · LES tone ↑, emptying ↑ · EPS, tardive dyskinesia, prolactin ↑',
           pcp='D₂ + M₁ + H₁ block · sedating · EPS, prolactin ↑',
           scop='M₁ block on the vestibular route · patch before the trip · dry mouth, cycloplegia, retention',
           mec='H₁ block on the vestibular route · motion sickness, vertigo · dimenhydrinate is more anticholinergic',
           dox='H₁ block · doxylamine + pyridoxine for nausea and vomiting of pregnancy',
           dro='CB₁ agonist in and around the vomiting center · refractory chemo vomiting, AIDS cachexia',
           lor='quiets the cortex · anticipatory and anxiety vomiting before chemotherapy')
for k, s in TAG.items(): text(s, 1280, 1760, 'nf-l1 dyn-tag', 'middle', when=E(k))
text('untreated: all four inputs drive the vomiting center', 1280, 1760, 'nf-l1', 'middle', unless=ANY)

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M2290 600 V1160', len=560, speed=110, r=8, base=dict(tox=4), mods=[m(E('dex'), add=dict(tox=-2))]),
  dict(d='M1700 900 H1515', len=185, speed=70, r=8, base=dict(sig=3),
       mods=[m(E('meto', 'pcp', 'olz', 'nk1'), set=dict(sig=1)), m(E('olz'), set=dict(sig=0)), m(E('dex'), set=dict(sig=2))]),
  dict(d='M530 850 H950', len=420, speed=110, r=8, base=dict(sig=3),
       mods=[m(E('scop', 'pcp'), set=dict(sig=1)), m(E('mec', 'dox'), set=dict(sig=1))]),
  dict(d='M1124 1420 V1015', len=405, speed=110, r=8, base=dict(sig=3), mods=[m(E('ond', 'olz'), set=dict(sig=0))]),
  dict(d='M1260 540 V690', len=150, speed=60, r=8, base=dict(sig=2), mods=[m(E('lor'), set=dict(sig=0))]),
  dict(d='M1420 1005 V1385', len=380, speed=110, r=9, base=dict(drive=4), mods=[m(ANY, set=dict(drive=1))]),
  dict(d='M690 1330 V1150', len=180, speed=60, r=10, base=dict(vom=3), mods=[m(ANY, set=dict(vom=0))]),
  dict(d='M760 1500 C1000 1580 1300 1540 1480 1440 H1720 V1630', len=1170, speed=50, r=9, base=dict(chyme=3),
       mods=[m(E('meto'), speed=2.5)]),
]
sites = [
  dict(x=2150, y=800, n=[-1, 0], w=10, t='rec', l='D₂', s='dopamine', c='d2emetic', cross=True, reach=110,
       ions=[['tox', 'out', 1]], block=E('meto', 'pcp', 'olz'), low=E('dex')),
  dict(x=2150, y=870, n=[-1, 0], w=10, t='rec', l='5-HT₃', s='serotonin', c='serodrugs', cross=True, reach=110,
       ions=[['tox', 'out', 1]], block=E('ond', 'olz'), low=E('dex')),
  dict(x=2150, y=940, n=[-1, 0], w=10, t='rec', l='NK₁', s='substance P', c='antiemetic', cross=True, reach=110,
       ions=[['tox', 'out', 1]], block=E('nk1'), low=E('dex')),
  dict(x=1000, y=830, n=[1, 0], w=10, t='rec', l='M₁', s='muscarinic', c='motionrx', cross=True,
       ions=[['sig', 'out', 1]], block=E('scop', 'pcp')),
  dict(x=1000, y=900, n=[1, 0], w=10, t='rec', l='H₁', s='histamine', c='h1blockers', cross=True,
       ions=[['sig', 'out', 1]], block=E('mec', 'dox', 'pcp')),
  dict(x=1124, y=1438, n=[0, -1], w=10, t='rec', l='5-HT₃', s='on the vagal terminal', c='serodrugs', cross=True,
       lx=1104, ly=1395, la='end', ions=[['ht', 'out', 2]], block=E('ond', 'olz')),
  dict(x=1001, y=1634, n=[0, 1], w=10, t='rec', l='D₂', s='dopamine brakes ACh', c='prokinetic', ions=[], block=E('meto')),
]

readouts = [
  dict(l='5-HT₃ blocked', mods=[dict(when=E('ond', 'olz'), d=1), dict(when=E('nk1'), d=0)]),
  dict(l='D₂ blocked', mods=[dict(when=E('meto', 'pcp', 'olz'), d=1), dict(when=E('ond', 'nk1'), d=0)]),
  dict(l='NK₁ blocked', mods=[dict(when=E('nk1'), d=1)]),
  dict(l='H₁ · M₁ blocked', mods=[dict(when=E('scop', 'mec', 'dox', 'pcp'), d=1)]),
  dict(l='QT interval', mods=[dict(when=QTE, d=1)]),
  dict(l='EPS · prolactin', mods=[dict(when=E('meto', 'pcp'), d=1)]),
  dict(l='Gastric emptying · LES tone', mods=[dict(when=E('meto'), d=1), dict(when=E('ond'), d=0)]),
]

notes = {
  '': 'The vomiting center around the nucleus tractus solitarius has four inputs: the chemoreceptor trigger zone in the area '
      'postrema (outside the blood–brain barrier), the vestibular system, vagal afferents from the gut and the cortex. Each '
      'input uses its own receptors, so choose the antiemetic that blocks the input doing the firing.',
  'e:ond': 'Ondansetron and granisetron block 5-HT₃, mainly on gut vagal afferents (chemotherapy, radiation and surgery release '
           'mucosal serotonin) and also centrally. First line for acute chemotherapy, postoperative and radiation vomiting; '
           'useless for motion sickness. Headache, constipation, QT prolongation, serotonin syndrome with SSRIs.',
  'e:nk1': 'Aprepitant (IV fosaprepitant) crosses the blood–brain barrier and blocks NK₁, the substance P receptor, in the area '
           'postrema. With a 5-HT₃ antagonist and dexamethasone it controls acute and delayed (after 24 h) chemotherapy '
           'vomiting. It inhibits CYP3A4, so the dexamethasone dose is halved.',
  'e:dex': 'Dexamethasone blocks none of the five receptors; its antiemetic action is not fully understood (likely central '
           'anti-inflammatory effects and less toxin entry across the blood–brain barrier). It strengthens 5-HT₃ and NK₁ '
           'antagonists against acute and delayed chemotherapy vomiting and postoperative vomiting.',
  'e:olz': 'Olanzapine blocks D₂, 5-HT₂C and 5-HT₃ receptors. It is the fourth drug in high-risk chemotherapy prophylaxis, '
           'further cutting acute and delayed vomiting, and it is used for breakthrough vomiting. Weight gain is common.',
  'e:meto': 'Metoclopramide blocks D₂ in the trigger zone (antiemetic) and in the gut, where dopamine brakes cholinergic muscle '
            'stimulation, so LES tone and gastric emptying rise — diabetic gastroparesis. Central D₂ block: dystonia, '
            'akathisia, tardive dyskinesia with long use, hyperprolactinemia.',
  'e:pcp': 'Prochlorperazine, a phenothiazine, blocks D₂ in the trigger zone and also M₁ and H₁ receptors, so it sedates. '
           'Like metoclopramide it can cause extrapyramidal symptoms (acute dystonia → benztropine or diphenhydramine) and '
           'hyperprolactinemia.',
  'e:scop': 'Scopolamine blocks M₁ receptors on the vestibular route to the solitary nucleus — one of the best drugs to prevent '
            'motion sickness. The transdermal patch, put on before the trip, is far better tolerated than oral doses: dry '
            'mouth, blurred vision, urinary retention, confusion.',
  'e:mec': 'Meclizine blocks H₁ with little sedation or anticholinergic action — motion sickness and vertigo from labyrinth '
           'disease. Dimenhydrinate (a diphenhydramine salt) blocks H₁ and is strongly anticholinergic and sedating. Both '
           'work best before motion sickness begins.',
  'e:dox': 'Doxylamine, a sedating first-generation H₁ blocker, combined with pyridoxine (vitamin B₆) treats nausea and '
           'vomiting of pregnancy; large studies found no rise in birth defects. H₁ antagonists also treat hyperemesis gravidarum.',
  'e:dro': 'Dronabinol (synthetic THC) and nabilone are CB₁ agonists in and around the vomiting center. Second line, for '
           'chemotherapy vomiting that fails other drugs, and for appetite in AIDS cachexia. Euphoria or dysphoria, '
           'sedation, hallucinations, tachycardia, orthostatic hypotension.',
  'e:lor': 'Lorazepam or diazepam given before chemotherapy reduces anticipatory vomiting and vomiting from anxiety — the '
           'cortical input to the vomiting center.',
}

dyn = dict(
  kinds=dict(tox=['blood', '--dk4'], sig=['nerve', '--accent'], ht=['ht', '--dk9'], drive=['drive', '--bad'],
             vom=['gut', '--dk6'], chyme=['gut', '--dk6']),
  groups=[['blood', 'Emetic drug in blood'], ['nerve', 'Nerve signal'], ['ht', '5-HT'], ['drive', 'Vomiting drive'],
          ['gut', 'Vomitus · chyme']],
  switches=[dict(id='e', label='Antiemetic', type='one', options=[
              ['ond', 'Ondansetron · granisetron (5-HT₃)', 'serodrugs'], ['nk1', 'Aprepitant (NK₁)', 'antiemetic'],
              ['dex', 'Dexamethasone', 'cortico'], ['olz', 'Olanzapine', 'antipsychotics'],
              ['meto', 'Metoclopramide (D₂)', 'prokinetic'], ['pcp', 'Prochlorperazine (D₂)', 'd2emetic'],
              ['scop', 'Scopolamine', 'motionrx'], ['mec', 'Meclizine · dimenhydrinate (H₁)', 'motionrx'],
              ['dox', 'Doxylamine · pyridoxine', 'h1blockers'], ['dro', 'Dronabinol', 'cannabis'],
              ['lor', 'Lorazepam (anticipatory)', 'benzos']],
            sections=[['Chemotherapy', ['ond', 'nk1', 'dex', 'olz']], ['D₂ blockers', ['meto', 'pcp']],
                      ['Motion sickness', ['scop', 'mec']], ['Pregnancy & other', ['dox', 'dro', 'lor']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=PANX, y=110, w=1000),
  src='Course SDL 10 lecture notes · Katzung ch 16, 29, 62, 63 · Guyton ch 67 · First Aid pp. 240, 247, 407, 506, 705')

MAP = dict(
  id='emesim', title='Vomiting & Antiemetics in Motion', topic='gi', after='gidrugs',
  sub='Four inputs drive the vomiting center — trigger zone, vestibular system, gut vagal afferents, cortex; give one '
      'antiemetic and watch which receptor it blocks and what it costs (QT, EPS, prolactin). Tap a receptor for its card',
  w=3600, h=2000,
  fa='240, 247, 407, 506, 705',
  src=[full('Katzung', 62), full('Katzung', 16),
       full('Katzung', 29), full('Katzung', 63), full('Guyton', 67)],
  lanes=[('emIn', 'Vomiting inputs', 'glycolysis'), ('emOut', 'Antiemetics', 'gluconeo'), ('emAe', 'Adverse effects', 'tca')],
  nodes=[
    ('em1', 'Vomiting pathways', 280, 1880, 'emIn', 'four inputs · five receptors', ['emesisrx', 'bbbcvo'], 'hub'),
    ('em2', '5-HT₃ & NK₁ antagonists', 610, 1880, 'emOut', 'ondansetron · aprepitant', ['serodrugs', 'antiemetic']),
    ('em3', 'Chemo add-ons', 940, 1880, 'emOut', 'dexamethasone · olanzapine', ['cortico', 'gcmech', 'antipsychotics']),
    ('em4', 'D₂ antagonists', 1270, 1880, 'emOut', 'metoclopramide · prochlorperazine', ['d2emetic', 'prokinetic']),
    ('em5', 'H₁ & M₁ antagonists', 1600, 1880, 'emOut', 'scopolamine · meclizine', ['motionrx', 'h1blockers', 'antimusc']),
    ('em6', 'Cannabinoids & benzos', 1930, 1880, 'emOut', 'dronabinol · lorazepam', ['cannabis', 'benzos']),
    ('em7', 'QT · EPS · prolactin', 2260, 1880, 'emAe', 'the cost of D₂ and 5-HT₃ block', ['longqt', 'eps', 'prolactinoma'])],
  panels=[
    (PANX, PANY, 1000, 'Receptor by input (FA 506 · lecture notes · Katzung ch 62)', [
      ('Trigger zone (area postrema)', 'D₂ · 5-HT₃ · NK₁'), ('Vestibular → solitary nucleus', 'M₁ · H₁'),
      ('Gut vagal afferents', '5-HT₃'), ('Cortex', 'anxiety → benzodiazepine'),
      ('Highly emetogenic chemo', '5-HT₃ + NK₁ + dexamethasone (+ olanzapine)'),
      ('Motion sickness', 'scopolamine, meclizine — not ondansetron')])],
  dyn=dyn)
