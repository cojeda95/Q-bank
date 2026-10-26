# Swallowing & the Esophagus in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Pharynx → upper esophageal sphincter → esophagus → lower esophageal sphincter → stomach, with a bolus riding a
# peristaltic wave down (the squeeze shown as paired dots on the walls). A toggle swaps solids for liquids; a `one` switch
# shows achalasia, distal esophageal spasm, GERD, Barrett, a Schatzki ring, a stricture, a Plummer-Vinson web, a Zenker
# diverticulum and a Mallory-Weiss tear: the bolus sticks, piles up, refluxes or spills, as the cards say. 5 readouts.
# Facts from the pinned cards; FA pages in `fa`. No new cards.
# m57: + eosinophilic esophagitis (stacked rings and furrows, solids impact), infectious esophagitis (Candida plaques, HSV and
#   CMV ulcers) and Boerhaave rupture (transmural, distal, air into the mediastinum). Sources: First Aid p. 384 (EoE: atopy,
#   rings, linear furrows; infectious: Candida white pseudomembranes, HSV-1 punched-out ulcers, CMV linear ulcers,
#   immunosuppression; Boerhaave: transmural, usually distal, violent retching; pneumomediastinum, crepitus) and Robbins ch 17
#   in the course text (course_sdl_8_9_patho pp. 14–15, 20: EoE atopy, food impaction, dysphagia, feline rings, strictures,
#   furrows, intraepithelial eosinophils, diet/PPI/topical steroids; HSV in healthy hosts, HSV/CMV/fungi in the
#   immunosuppressed, Candida commonest fungus, gray-white pseudomembranes, punched-out HSV ulcers with nuclear inclusions,
#   shallower CMV ulcers with endothelial inclusions, odynophagia; Boerhaave chest pain, tachypnea, shock, fatal untreated).
#   GI Exam 1 lecture notes (SDL 8, section 2) agree on every line and add EoE ≥ 15 eosinophils/HPF (used in the note).
#   Readouts: only "Dysphagia — solids ↑" for EoE (food impaction). Odynophagia is not a readout, so the infection and the
#   rupture change none.
# m58 pins (P6, P11): a second `one` switch, "Stage of the swallow" (oral, pharyngeal, UES, primary and secondary
#   peristalsis, swallowing center), all on the swallowing card — Guyton ch 64 (course_sdl_4_7_guyton_supplement_p2 pp. 2–6:
#   voluntary/pharyngeal/esophageal stages, soft palate, vocal cords, epiglottis, UES = upper 3–4 cm, relaxed in the swallow and
#   contracted between swallows, pharyngeal stage < 2 s, trigeminal + glossopharyngeal afferents to the tractus solitarius,
#   deglutition center in the medulla and lower pons, motor V IX X XII, respiration inhibited, primary wave 8–10 s (5–8 s
#   upright), secondary waves from distension via myenteric circuits and vagal reflexes). No readout arrows for the stages.
#   "Schatzki ring" relabelled "… · B ring · distal esophageal ring" (Robbins ch 17, course_sdl_8_9_patho p. 12; lecture notes
#   p. 40). Keys unchanged.
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

O = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
EX, TOP, UES, LES, BOT = 900, 300, 420, 1140, 1240
W = 46                                            # half-width of the tube
STUCK_ANY = O('ach')                              # solids and liquids stop
STUCK_SOLID = ['dx:ring&!liq', 'dx:strict&!liq', 'dx:web&!liq', 'dx:eoe&!liq']
STUCK = STUCK_ANY + STUCK_SOLID

text('Swallowing — the bolus, the wave and the sphincters', 180, 150, 'dyn-big')
text('paired dots on the walls = the peristaltic squeeze · big dot = the bolus', 180, 176, 'dyn-cap')

# ════════ the tube ════════
add(f'<path d="M{EX - 120} {TOP - 60} Q{EX} {TOP - 120} {EX + 120} {TOP - 60} L{EX + W} {TOP + 40}" style="fill:none;stroke:var(--ink-3);stroke-width:4"/>')
text('pharynx', EX - 140, TOP - 70, 'nf-l1', 'end')
add(f'<path d="M{EX - W} {TOP} V{LES} M{EX + W} {TOP} V{LES}" style="stroke:var(--dk3);stroke-width:10;opacity:.55"/>', unless=O('ach'))
add(f'<path d="M{EX - W} {TOP} V{UES + 100} C{EX - 150} {UES + 300} {EX - 150} {LES - 200} {EX - 14} {LES} M{EX + W} {TOP} V{UES + 100} C{EX + 150} {UES + 300} {EX + 150} {LES - 200} {EX + 14} {LES}" style="fill:none;stroke:var(--dk3);stroke-width:10;opacity:.55"/>', when=O('ach'))
text('dilated esophagus, “bird’s beak”', EX + 180, 760, 'nf-l1 dyn-tag', when=O('ach'))
add(f'<path d="M{EX - 260} {LES + 20} C{EX - 300} {BOT + 260} {EX + 340} {BOT + 260} {EX + 320} {LES + 40} C{EX + 200} {LES - 20} {EX + 80} {LES + 20} {EX + W} {LES + 20}" style="fill:var(--dk5);fill-opacity:.1;stroke:var(--dk5);stroke-width:4"/>')
text('stomach', EX + 40, BOT + 120, 'nf-l1', 'middle')
for y, lab, sub in ((UES, 'UES', 'cricopharyngeus'), (LES, 'LES', 'relaxes for the bolus')):
    add(f'<rect x="{EX - W - 30}" y="{y - 8}" width="30" height="16" rx="4" style="fill:var(--dk7)"/><rect x="{EX + W}" y="{y - 8}" width="30" height="16" rx="4" style="fill:var(--dk7)"/>')
    text(lab, EX - W - 50, y + 6, 'nf-l1', 'end'); text(sub, EX - W - 50, y + 30, 'nf-l2', 'end')
add(f'<rect x="{EX - 20}" y="{LES - 8}" width="40" height="16" rx="4" style="fill:var(--bad)"/>', when=O('ach'))
text('LES won’t relax', EX + W + 90, LES + 6, 'nf-l1 dyn-tag', when=O('ach'))
text('transient drops in LES tone', EX + W + 90, LES + 6, 'nf-l1 dyn-tag', when=O('gerd', 'barrett'))
text('weak LES, distal peristalsis lost — reflux', EX + W + 90, LES + 6, 'nf-l1 dyn-tag', when=O('scl'))
add(f'<rect x="{EX - W - 34}" y="{LES - 12}" width="{2 * W + 68}" height="24" style="fill:var(--surface);opacity:.7"/>', when=O('scl'))   # LES faded
add(f'<path d="M{EX - W} {LES - 420} V{LES - 20} M{EX + W} {LES - 420} V{LES - 20}" style="stroke:var(--surface);stroke-width:6;stroke-dasharray:14 12"/>', when=O('scl'))   # fibrosed distal wall
text('liquid swallow', EX + 170, TOP - 76, 'nf-l1', when=['liq'])
# lesions
add(f'<rect x="{EX - W}" y="{LES - 140}" width="{2 * W}" height="120" style="fill:var(--bad);fill-opacity:.35"/>', when=O('barrett'))
text('columnar + goblet cells above the Z line → adenocarcinoma', EX + W + 50, LES - 80, 'nf-l1 dyn-tag', when=O('barrett'))
add(f'<path d="M{EX - W} {LES - 60} q{W * 0.8} 10 0 20 M{EX + W} {LES - 60} q{-W * 0.8} 10 0 20" style="fill:var(--dk3);stroke:var(--dk3);stroke-width:8"/>', when=O('ring'))
text('Schatzki ring — distal, circumferential', EX + W + 50, LES - 50, 'nf-l1 dyn-tag', when=O('ring'))
add(f'<path d="M{EX - W} {LES - 320} C{EX - 14} {LES - 280} {EX - 14} {LES - 160} {EX - W} {LES - 120} M{EX + W} {LES - 320} C{EX + 14} {LES - 280} {EX + 14} {LES - 160} {EX + W} {LES - 120}" style="fill:none;stroke:var(--dk3);stroke-width:12"/>', when=O('strict'))
text('stricture — scarred submucosa (reflux, caustic, radiation)', EX + W + 50, LES - 220, 'nf-l1 dyn-tag', when=O('strict'))
add(f'<path d="M{EX - W} {UES + 70} h{W * 1.1}" style="stroke:var(--dk3);stroke-width:10"/>', when=O('web'))
text('upper web — Plummer-Vinson: iron deficiency, glossitis', EX + W + 50, UES + 76, 'nf-l1 dyn-tag', when=O('web'))
add(f'<path d="M{EX - W} {UES - 150} C{EX - 200} {UES - 160} {EX - 220} {UES - 20} {EX - W} {UES - 60}" style="fill:var(--dk3);fill-opacity:.2;stroke:var(--dk3);stroke-width:5"/>', when=O('zenker'))
text('Zenker: false diverticulum through Killian triangle', EX - 240, UES + 100, 'nf-l1 dyn-tag', 'end', when=O('zenker'))
text('regurgitates undigested food · halitosis', EX - 240, UES + 128, 'nf-l2', 'end', when=O('zenker'))
add(f'<path d="M{EX - W + 6} {LES - 10} v50" style="stroke:var(--bad);stroke-width:8"/>', when=O('mw'))
text('mucosal tear at the GE junction after retching — hematemesis', EX + W + 50, LES + 40, 'nf-l1 dyn-tag', when=O('mw'))
text('uncoordinated contractions — “corkscrew”, chest pain', EX + W + 50, 700, 'nf-l1 dyn-tag', when=O('des'))
# eosinophilic esophagitis: stacked circular rings ("feline") and linear furrows along the tube
add(''.join(f'<path d="M{EX - W} {y} h16 M{EX + W} {y} h-16" style="stroke:var(--dk3);stroke-width:7"/>' for y in range(UES + 120, LES - 20, 56))
    + f'<path d="M{EX - 14} {UES + 130} V{LES - 40} M{EX + 14} {UES + 130} V{LES - 40}" style="stroke:var(--dk3);stroke-width:3;stroke-dasharray:22 14;opacity:.7"/>',
    when=O('eoe'))
text('stacked rings + linear furrows — eosinophils in the lining', EX + W + 50, 700, 'nf-l1 dyn-tag', when=O('eoe'))
text('atopy (asthma, eczema) · food impaction', EX + W + 50, 728, 'nf-l2', when=O('eoe'))
# infectious esophagitis: Candida pseudomembranes, herpes punched-out ulcers, CMV shallow linear ulcers
add(''.join(f'<ellipse cx="{EX + dx}" cy="{y}" rx="12" ry="7" style="fill:var(--dk11);fill-opacity:.55;stroke:var(--dk11);stroke-width:2"/>'
            for dx, y in ((-28, 560), (26, 600), (-30, 660), (28, 720)))
    + ''.join(f'<circle cx="{EX + dx}" cy="{y}" r="9" style="fill:var(--surface);stroke:var(--bad);stroke-width:4"/>' for dx, y in ((-30, 860), (30, 900), (-30, 960)))
    + f'<path d="M{EX + 32} {LES - 110} v60" style="stroke:var(--bad);stroke-width:5"/>', when=O('inf'))
text('Candida — white pseudomembranes (commonest)', EX + W + 50, 620, 'nf-l1 dyn-tag', when=O('inf'))
text('HSV — punched-out ulcers · CMV — shallow linear ulcers', EX + W + 50, 900, 'nf-l1 dyn-tag', when=O('inf'))
text('immunosuppressed · pain on swallowing (odynophagia)', EX + W + 50, 928, 'nf-l2', when=O('inf'))
# Boerhaave: the whole wall torn, distally — air out into the mediastinum
add(f'<rect x="{EX - W - 14}" y="{LES - 150}" width="28" height="70" style="fill:var(--surface)"/>'
    f'<path d="M{EX - W - 14} {LES - 150} l14 18 l-10 16 l14 18 l-10 18" style="fill:none;stroke:var(--bad);stroke-width:6"/>', when=O('boer'))
text('transmural rupture, distal — after violent retching', EX + W + 50, LES - 130, 'nf-l1 dyn-tag', when=O('boer'))
text('air in the mediastinum · neck crepitus · chest pain, shock', EX + W + 50, LES - 102, 'nf-l2', when=O('boer'))
text('mediastinum', EX - 330, LES - 250, 'nf-l2', 'end', when=O('boer'))
# stages of the swallow (switch `stg`, m58) — tags on the left, out of the way of the dx tags on the right
G = lambda *k: [f'stg:{x}' for x in k]
SX = EX - 120
PHX = f'M{EX - 120} {TOP - 60} Q{EX} {TOP - 120} {EX + 120} {TOP - 60}'
add(f'<path d="{PHX}" style="fill:none;stroke:var(--accent);stroke-width:12;opacity:.5"/>', when=G('oral', 'phar'))
text('tongue rolls the bolus back against the palate', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('oral'))
text('voluntary — after this, automatic', SX, 668, 'nf-l2', 'end', when=G('oral'))
text('soft palate shuts the nose · vocal cords close', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('phar'))
text('epiglottis tips back · UES opens · < 2 s', SX, 668, 'nf-l2', 'end', when=G('phar'))
add(f'<rect x="{EX - W - 40}" y="{UES - 18}" width="{2 * W + 80}" height="36" rx="10" style="fill:none;stroke:var(--accent);stroke-width:5"/>', when=G('ues', 'phar'))
text('upper 3–4 cm: relaxes as the larynx rises', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('ues'))
text('shut between swallows — keeps air out', SX, 668, 'nf-l2', 'end', when=G('ues'))
add(f'<path d="M{EX - W - 14} {UES + 20} V{LES - 20} M{EX + W + 14} {UES + 20} V{LES - 20}" style="stroke:var(--accent);stroke-width:5;stroke-dasharray:16 12;opacity:.7"/>', when=G('prim'))
text('the pharyngeal wave runs on to the stomach', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('prim'))
text('pharynx → stomach in 8–10 s', SX, 668, 'nf-l2', 'end', when=G('prim'))
text('food left behind stretches the wall', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('sec'))
text('→ a new wave from there (myenteric + vagal)', SX, 668, 'nf-l2', 'end', when=G('sec'))
add(f'<rect x="300" y="210" width="330" height="64" rx="18" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--accent);stroke-width:4"/>'
    f'<path d="M630 242 C700 250 740 260 {EX - 120} {TOP - 60}" class="dyn-dash"/>', when=G('center'))
text('swallowing center', 465, 238, 'nf-l1', 'middle', when=G('center'))
text('medulla · lower pons', 465, 262, 'nf-l2', 'middle', when=G('center'))
text('in: V, IX → tractus solitarius', SX, 640, 'nf-l1 dyn-tag', 'end', when=G('center'))
text('out: V, IX, X, XII · breathing paused', SX, 668, 'nf-l2', 'end', when=G('center'))

# pile above a block
def pile(y, when):
    add(''.join(f'<circle cx="{EX + dx}" cy="{y + dy}" r="14" style="fill:var(--dk10);opacity:.85"/>'
                for dx, dy in ((-20, 0), (12, -6), (-4, -30), (22, -32), (-24, -58))), when=when)
pile(LES - 30, STUCK_ANY); pile(LES - 340, ['dx:strict&!liq']); pile(LES - 76, ['dx:ring&!liq']); pile(UES + 50, ['dx:web&!liq'])
pile(UES - 70, O('zenker')); pile(790, ['dx:eoe&!liq']); pile(700, G('sec'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def stop_at(y): return f'M{EX} {TOP} V{y}'
flows = [
  dict(d=f'M{EX} {TOP} V{LES + 60}', len=LES + 60 - TOP, speed=110, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], unless=STUCK + O('zenker')),
  dict(d=stop_at(LES - 40), len=LES - 40 - TOP, speed=110, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=STUCK_ANY),
  dict(d=stop_at(LES - 350), len=LES - 350 - TOP, speed=110, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=['dx:strict&!liq']),
  dict(d=stop_at(LES - 86), len=LES - 86 - TOP, speed=110, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=['dx:ring&!liq']),
  dict(d=stop_at(780), len=780 - TOP, speed=110, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=['dx:eoe&!liq']),
  dict(d=stop_at(UES + 40), len=UES + 40 - TOP, speed=60, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=['dx:web&!liq']),
  dict(d=f'M{EX} {TOP} V{UES - 110} C{EX - 120} {UES - 120} {EX - 180} {UES - 60} {EX - 120} {UES - 70}', len=360, speed=80, r=22, base=dict(bol=1), mods=[m(['liq'], set=dict(bol=0, liqd=1))], when=O('zenker')),
  dict(d=f'M{EX - W} {TOP} V{LES}', len=LES - TOP, speed=110, r=10, base=dict(wave=1), unless=O('ach', 'des', 'scl')),
  dict(d=f'M{EX + W} {TOP} V{LES}', len=LES - TOP, speed=110, r=10, base=dict(wave=1), unless=O('ach', 'des', 'scl')),
  dict(d=f'M{EX - W} {TOP} V{LES - 420}', len=LES - 420 - TOP, speed=110, r=10, base=dict(wave=1), when=O('scl')),   # proximal (striated) wave only
  dict(d=f'M{EX + W} {TOP} V{LES - 420}', len=LES - 420 - TOP, speed=110, r=10, base=dict(wave=1), when=O('scl')),
  dict(d=f'M{EX - W} {UES + 60} V{LES - 60}', len=600, speed=300, r=10, base=dict(wave=5), when=O('des')),
  dict(d=f'M{EX + W} {LES - 60} V{UES + 60}', len=600, speed=260, r=10, base=dict(wave=5), when=O('des')),
  dict(d=f'M{EX} {LES + 80} V{LES - 240}', len=320, speed=90, r=9, base=dict(acid=4), when=O('gerd', 'barrett', 'scl')),
  dict(d=f'M{EX - W + 6} {LES + 20} C{EX - 150} {LES + 120} {EX - 150} {LES + 200} {EX - 120} {BOT + 60}', len=300, speed=80, r=8, base=dict(bl=4), when=O('mw')),
  dict(d=f'M{EX - W} 720 V{LES}', len=LES - 720, speed=110, r=10, base=dict(wave=1), when=G('sec')),
  dict(d=f'M{EX + W} 720 V{LES}', len=LES - 720, speed=110, r=10, base=dict(wave=1), when=G('sec')),
] + [dict(d=f'M{EX - W - 6} {LES - 115} C{EX - 120} {LES - 140} {EX - 200} {LES - 190 + dy} {EX - 320} {LES - 230 + dy}', len=300, speed=70, r=8,
          base=dict(air=3), when=O('boer')) for dy in (0, 70)]
sites = [dict(x=EX + W + 30, y=LES, n=[1, 0], w=10, t='rec', l='', aria='Lower esophageal sphincter', c='achalasia', ions=[]),
         dict(x=EX + W + 30, y=UES, n=[1, 0], w=10, t='rec', l='', aria='Swallowing', c='swallowing', ions=[])]

readouts = [
  dict(l='Dysphagia — solids', mods=[dict(when=O('ach', 'ring', 'strict', 'web', 'zenker', 'des', 'scl', 'eoe'), d=1)]),
  dict(l='Dysphagia — liquids', mods=[dict(when=O('ach'), d=1), dict(when=O('ring', 'strict', 'web'), d=0)]),
  dict(l='LES resting pressure', mods=[dict(when=O('ach'), d=1), dict(when=O('des'), d=0), dict(when=O('scl'), d=-1)]),
  dict(l='Coordinated peristalsis', mods=[dict(when=O('ach', 'des', 'scl'), d=-1)]),
  dict(l='Cancer risk', mods=[dict(when=O('barrett', 'ach', 'web'), d=1)]),
]

notes = {
  '': 'Swallowing starts voluntarily, then the medullary swallowing center takes over: the UES relaxes, the pharyngeal constrictors '
      'contract top to bottom, and primary peristalsis carries the bolus to the stomach in 8–10 seconds as the LES relaxes.',
  'liq': 'Liquids: a mechanical narrowing (ring, stricture, web) lets them through — dysphagia starts with solids. Achalasia, a motility '
         'problem, stops both.',
  'stg:oral': 'Oral (voluntary) stage: the tongue squeezes or rolls the bolus up and back against the palate into the pharynx. '
              'From here on, swallowing is automatic and ordinarily cannot be stopped.',
  'stg:phar': 'Pharyngeal stage, a reflex of under 2 seconds: the soft palate closes the nasal passages, the vocal cords close '
              'and the larynx rises so the epiglottis swings back over it, the UES relaxes, and a fast wave from the top of the '
              'pharynx drives the bolus into the esophagus. Breathing pauses.',
  'stg:ues': 'Upper esophageal sphincter (pharyngoesophageal sphincter): the upper 3–4 cm of the esophageal wall. It relaxes as '
             'the larynx rises during the pharyngeal stage, and between swallows stays strongly contracted so air does not enter '
             'the esophagus with each breath.',
  'stg:prim': 'Primary peristalsis: the continuation of the pharyngeal wave, running from the pharynx to the stomach in about '
              '8–10 seconds. Upright, food arrives a little faster (5–8 s) because gravity helps.',
  'stg:sec': 'Secondary peristalsis: if the primary wave leaves food behind, the stretched esophagus starts new waves at that point '
             'until it is empty — through the myenteric plexus and through vagal reflexes via the medulla.',
  'stg:center': 'Swallowing (deglutition) center: neurons of the reticular substance of the medulla and lower pons. Touch on the '
                'tonsillar pillars and pharynx reaches it by the trigeminal and glossopharyngeal nerves (tractus solitarius); it fires '
                'the sequence through cranial nerves V, IX, X and XII, and inhibits the respiratory center meanwhile.',
  'dx:ach': 'Achalasia: the inhibitory (NO, VIP) neurons of the myenteric plexus degenerate, so the LES can’t relax and peristalsis fails — '
            'dysphagia to solids AND liquids (an obstruction is mainly solids), bird’s beak, ↑ LES pressure on manometry, ↑ cancer risk. Chagas is a cause.',
  'dx:des': 'Distal esophageal spasm: uncoordinated contractions with a normal LES — corkscrew esophagus, chest pain. Nitrates, CCBs.',
  'dx:gerd': 'GERD: transient drops in LES tone let acid reflux — heartburn, regurgitation, cough, hoarseness; erosive esophagitis, '
             'stricture, Barrett. Sliding hiatal hernia.',
  'dx:scl': 'Scleroderma (CREST): smooth-muscle atrophy and fibrosis — ↓ LES pressure and lost distal peristalsis, the reverse of '
            'achalasia. Acid refluxes: dysphagia, then stricture, Barrett esophagus and aspiration.',
  'dx:barrett': 'Barrett esophagus: years of reflux replace the distal squamous lining with columnar epithelium with goblet cells '
                '(intestinal metaplasia) — can progress through dysplasia to adenocarcinoma.',
  'dx:eoe': 'Eosinophilic esophagitis: an immune-mediated, allergic (Th2) disorder of atopic patients — asthma, eczema, allergic '
            'rhinitis. Eosinophils crowd the squamous lining (≥ 15 per high-power field); the esophagus shows stacked circular rings (feline esophagus), '
            'linear furrows and strictures. Food impaction, dysphagia and GERD-like symptoms. Diet elimination, PPIs, topical steroids.',
  'dx:inf': 'Infectious esophagitis: HSV in otherwise healthy people; HSV, CMV or fungi in the immunosuppressed. Candida, the '
            'commonest fungus, lays down adherent gray-white pseudomembranes; HSV makes punched-out ulcers (nuclear inclusions '
            'in multinucleate cells at the edge); CMV makes shallower, linear ulcers. Pain on swallowing (odynophagia).',
  'dx:ring': 'Schatzki ring: a circumferential band narrowing the distal esophagus — dysphagia and regurgitation; hiatal hernia, GERD. '
             'A B ring sits at the squamocolumnar junction (cardia-type mucosa beneath); an A ring lies just above the GE junction.',
  'dx:strict': 'Stricture: healing lays down fibrous submucosa until the lumen narrows (reflux, irradiation, caustics) — progressive '
               'dysphagia that starts with solids; weight kept if benign.',
  'dx:web': 'Esophageal web: a semicircumferential ledge; an upper web is part of Plummer-Vinson syndrome (iron deficiency anemia, '
            'glossitis, cheilosis) with ↑ squamous cell carcinoma risk. Non-progressive dysphagia to poorly chewed food.',
  'dx:zenker': 'Zenker diverticulum: mucosa pushed out through Killian triangle above the cricopharyngeus — a false diverticulum. '
               'Dysphagia, gurgling, regurgitated undigested food, halitosis, aspiration.',
  'dx:mw': 'Mallory-Weiss tear: violent retching (alcohol, bulimia) tears the mucosa at the GE junction — hematemesis. A transmural '
           'rupture is Boerhaave (pneumomediastinum, crepitus).',
  'dx:boer': 'Boerhaave syndrome: violent retching or straining raises intraesophageal pressure against a negative intrathoracic '
             'pressure and tears the whole wall, usually distally. Air escapes into the mediastinum (pneumomediastinum, crepitus '
             'in the neck); sudden chest pain, tachypnea, shock that mimic an MI. Fatal untreated. A Mallory-Weiss tear stays in the mucosa.',
}

dyn = dict(
  kinds=dict(bol=['food', '--dk10'], liqd=['food', '--nf-h2o'], wave=['wave', '--dk3'], acid=['acid', '--bad'], bl=['acid', '--nf-blood'], air=['acid', '--dk8']),
  groups=[['food', 'Bolus'], ['wave', 'Peristaltic wave'], ['acid', 'Acid · blood · air']],
  switches=[dict(id='liq', label='Swallow', type='toggle', on='Liquids', off='Solids', def_=False),
            dict(id='dx', label='What goes wrong', type='one', options=[
              ['ach', 'Achalasia', 'achalasia'], ['des', 'Distal esophageal spasm', 'achalasia'], ['scl', 'Scleroderma esophagus', 'achalasia'], ['gerd', 'GERD', 'gerd'],
              ['barrett', 'Barrett esophagus', 'barrett'], ['eoe', 'Eosinophilic esophagitis', 'esophagitis'],
              ['inf', 'Infectious esophagitis — Candida · HSV · CMV', 'esophagitis'], ['ring', 'Schatzki ring · B ring · distal esophageal ring', 'schatzki'], ['strict', 'Stricture', 'esostricture'],
              ['web', 'Plummer-Vinson web', 'esophagitis'], ['zenker', 'Zenker diverticulum', 'zenker'], ['mw', 'Mallory-Weiss tear', 'mallorywb'],
              ['boer', 'Boerhaave rupture', 'mallorywb']]),
            dict(id='stg', label='Stage of the swallow', type='one', options=[
              ['oral', 'Oral (voluntary) stage', 'swallowing'], ['phar', 'Pharyngeal stage', 'swallowing'],
              ['ues', 'Upper esophageal sphincter · UES', 'swallowing'], ['prim', 'Primary peristalsis', 'swallowing'],
              ['sec', 'Secondary peristalsis · secondary peristaltic wave', 'swallowing'],
              ['center', 'Swallowing center · medulla', 'swallowing']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 377, 383–385, 391 · Robbins ch 17 · Guyton ch 64 · Bootcamp GI')
dyn['switches'][0]['def'] = dyn['switches'][0].pop('def_')

MAP = dict(
  id='esosim', title='Swallowing in Motion', topic='gi', after='gitract',
  sub='Watch a bolus ride the peristaltic wave through both sphincters, switch solids for liquids, then see it stick, reflux or spill — '
      'achalasia, esophageal spasm, GERD, Barrett, eosinophilic and infectious esophagitis, Schatzki ring, stricture, Plummer-Vinson web, '
      'Zenker, Mallory-Weiss and Boerhaave',
  w=3600, h=1900,
  fa='377, 383, 384, 385, 391',
  src=['Robbins ch 17 — The gastrointestinal tract', 'Katzung ch 62 — Drugs Used in the Treatment of Gastrointestinal Diseases',
       'Robbins ch 8 — Infectious diseases', 'Moore ch 8 — Neck', 'Bootcamp.com Gastroenterology — Esophagus',
       'Guyton ch 64 — Propulsion and Mixing of Food in the Alimentary Tract', 'Costanzo ch 8 — Gastrointestinal physiology'],
  lanes=[('eoMot', 'Motility', 'glycolysis'), ('eoMuc', 'Reflux & mucosa', 'tca'), ('eoObs', 'Narrowing & pouches', 'gluconeo')],
  nodes=[
    ('es1', 'Swallowing', 330, 1660, 'eoMot', 'reflex · peristalsis', ['swallowing'], 'hub'),
    ('es2', 'Achalasia · spasm', 760, 1660, 'eoMot', 'bird’s beak · corkscrew · CREST', ['achalasia']),
    ('es3', 'GERD', 1200, 1660, 'eoMuc', 'transient LES relaxation', ['gerd']),
    ('es4', 'Barrett esophagus', 1640, 1660, 'eoMuc', 'goblet cells', ['barrett']),
    ('es5', 'Esophagitis · webs', 2080, 1660, 'eoMuc', 'pill, Candida, Plummer-Vinson', ['esophagitis']),
    ('es6', 'Schatzki ring', 330, 1790, 'eoObs', 'distal ring', ['schatzki']),
    ('es7', 'Stricture', 760, 1790, 'eoObs', 'solids first', ['esostricture']),
    ('es8', 'Zenker diverticulum', 1200, 1790, 'eoObs', 'Killian triangle', ['zenker']),
    ('es9', 'Mallory-Weiss · Boerhaave', 1640, 1790, 'eoMuc', 'tear vs rupture', ['mallorywb'])],
  panels=[
    (2500, PANY, 1000, 'Dysphagia: solids or liquids? (First Aid pp. 383–385 · Robbins ch 17)', [
      ('Solids AND liquids', 'achalasia (motility)'),
      ('Solids first, progressive', 'stricture, cancer (obstruction)'),
      ('Solids, non-progressive', 'web, ring'),
      ('Pain on swallowing', 'esophagitis (pill, Candida, HSV, CMV)')])],
  dyn=dyn)
