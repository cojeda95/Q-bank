# Swallowing & the Esophagus in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Pharynx → upper esophageal sphincter → esophagus → lower esophageal sphincter → stomach, with a bolus riding a
# peristaltic wave down (the squeeze shown as paired dots on the walls). A toggle swaps solids for liquids; a `one` switch
# shows achalasia, distal esophageal spasm, GERD, Barrett, a Schatzki ring, a stricture, a Plummer-Vinson web, a Zenker
# diverticulum and a Mallory-Weiss tear: the bolus sticks, piles up, refluxes or spills, as the cards say. 5 readouts.
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

O = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
EX, TOP, UES, LES, BOT = 900, 300, 420, 1140, 1240
W = 46                                            # half-width of the tube
STUCK_ANY = O('ach')                              # solids and liquids stop
STUCK_SOLID = ['dx:ring&!liq', 'dx:strict&!liq', 'dx:web&!liq']
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
text('transient LES relaxations', EX + W + 90, LES + 6, 'nf-l1 dyn-tag', when=O('gerd', 'barrett'))
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
# pile above a block
def pile(y, when):
    add(''.join(f'<circle cx="{EX + dx}" cy="{y + dy}" r="14" style="fill:var(--dk10);opacity:.85"/>'
                for dx, dy in ((-20, 0), (12, -6), (-4, -30), (22, -32), (-24, -58))), when=when)
pile(LES - 30, STUCK_ANY); pile(LES - 340, ['dx:strict&!liq']); pile(LES - 76, ['dx:ring&!liq']); pile(UES + 50, ['dx:web&!liq'])
pile(UES - 70, O('zenker'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def stop_at(y): return f'M{EX} {TOP} V{y}'
flows = [
  dict(d=f'M{EX} {TOP} V{LES + 60}', len=LES + 60 - TOP, speed=110, r=22, base=dict(bol=1), unless=STUCK + O('zenker')),
  dict(d=stop_at(LES - 40), len=LES - 40 - TOP, speed=110, r=22, base=dict(bol=1), when=STUCK_ANY),
  dict(d=stop_at(LES - 350), len=LES - 350 - TOP, speed=110, r=22, base=dict(bol=1), when=['dx:strict&!liq']),
  dict(d=stop_at(LES - 86), len=LES - 86 - TOP, speed=110, r=22, base=dict(bol=1), when=['dx:ring&!liq']),
  dict(d=stop_at(UES + 40), len=UES + 40 - TOP, speed=60, r=22, base=dict(bol=1), when=['dx:web&!liq']),
  dict(d=f'M{EX} {TOP} V{UES - 110} C{EX - 120} {UES - 120} {EX - 180} {UES - 60} {EX - 120} {UES - 70}', len=360, speed=80, r=22, base=dict(bol=1), when=O('zenker')),
  dict(d=f'M{EX - W} {TOP} V{LES}', len=LES - TOP, speed=110, r=10, base=dict(wave=1), unless=O('ach', 'des')),
  dict(d=f'M{EX + W} {TOP} V{LES}', len=LES - TOP, speed=110, r=10, base=dict(wave=1), unless=O('ach', 'des')),
  dict(d=f'M{EX - W} {UES + 60} V{LES - 60}', len=600, speed=300, r=10, base=dict(wave=5), when=O('des')),
  dict(d=f'M{EX + W} {LES - 60} V{UES + 60}', len=600, speed=260, r=10, base=dict(wave=5), when=O('des')),
  dict(d=f'M{EX} {LES + 80} V{LES - 240}', len=320, speed=90, r=9, base=dict(acid=4), when=O('gerd', 'barrett')),
  dict(d=f'M{EX - W + 6} {LES + 20} C{EX - 150} {LES + 120} {EX - 150} {LES + 200} {EX - 120} {BOT + 60}', len=300, speed=80, r=8, base=dict(bl=4), when=O('mw')),
]
sites = [dict(x=EX + W + 30, y=LES, n=[1, 0], w=10, t='rec', l='', aria='Lower esophageal sphincter', c='achalasia', ions=[]),
         dict(x=EX + W + 30, y=UES, n=[1, 0], w=10, t='rec', l='', aria='Swallowing', c='swallowing', ions=[])]

readouts = [
  dict(l='Dysphagia — solids', mods=[dict(when=STUCK + O('zenker', 'des'), d=1)]),
  dict(l='Dysphagia — liquids', mods=[dict(when=O('ach'), d=1), dict(when=['dx:ring&liq', 'dx:strict&liq'], d=0)]),
  dict(l='LES resting pressure', mods=[dict(when=O('ach'), d=1), dict(when=O('des'), d=0)]),
  dict(l='Peristalsis', mods=[dict(when=O('ach', 'des'), d=-1)]),
  dict(l='Cancer risk', mods=[dict(when=O('barrett', 'ach', 'web'), d=1)]),
]

notes = {
  '': 'Swallowing starts voluntarily, then the medullary swallowing center takes over: the UES relaxes, the pharyngeal constrictors '
      'contract top to bottom, and primary peristalsis carries the bolus to the stomach in 8–10 seconds as the LES relaxes.',
  'liq': 'Liquids: a mechanical narrowing (ring, stricture, web) lets them through — dysphagia starts with solids. Achalasia stops both.',
  'dx:ach': 'Achalasia: the inhibitory (NO, VIP) neurons of the myenteric plexus degenerate, so the LES can’t relax and peristalsis fails — '
            'dysphagia to solids AND liquids from the start, bird’s beak, ↑ LES pressure on manometry, ↑ cancer risk. Chagas is a cause.',
  'dx:des': 'Distal esophageal spasm: uncoordinated contractions with a normal LES — corkscrew esophagus, chest pain. Nitrates, CCBs.',
  'dx:gerd': 'GERD: transient LES relaxations let acid reflux — heartburn, regurgitation, cough, hoarseness; erosive esophagitis, '
             'stricture, Barrett. Sliding hiatal hernia.',
  'dx:barrett': 'Barrett esophagus: years of reflux replace the distal squamous lining with columnar epithelium with goblet cells '
                '(intestinal metaplasia) — can progress through dysplasia to adenocarcinoma.',
  'dx:ring': 'Schatzki ring: a circumferential band narrowing the distal esophagus — dysphagia and regurgitation; hiatal hernia, GERD.',
  'dx:strict': 'Stricture: healing lays down fibrous submucosa until the lumen narrows (reflux, irradiation, caustics) — progressive '
               'dysphagia that starts with solids; weight kept if benign.',
  'dx:web': 'Esophageal web: a semicircumferential ledge; an upper web is part of Plummer-Vinson syndrome (iron deficiency anemia, '
            'glossitis, cheilosis) with ↑ squamous cell carcinoma risk. Non-progressive dysphagia to poorly chewed food.',
  'dx:zenker': 'Zenker diverticulum: mucosa pushed out through Killian triangle above the cricopharyngeus — a false diverticulum. '
               'Dysphagia, gurgling, regurgitated undigested food, halitosis, aspiration.',
  'dx:mw': 'Mallory-Weiss tear: violent retching (alcohol, bulimia) tears the mucosa at the GE junction — hematemesis. A transmural '
           'rupture is Boerhaave (pneumomediastinum, crepitus).',
}

dyn = dict(
  kinds=dict(bol=['food', '--dk10'], wave=['wave', '--dk3'], acid=['acid', '--bad'], bl=['acid', '--nf-blood']),
  groups=[['food', 'Bolus'], ['wave', 'Peristaltic wave'], ['acid', 'Acid · blood']],
  switches=[dict(id='liq', label='Swallow', type='toggle', on='Liquids', off='Solids', def_=False),
            dict(id='dx', label='What goes wrong', type='one', options=[
              ['ach', 'Achalasia', 'achalasia'], ['des', 'Distal esophageal spasm', 'achalasia'], ['gerd', 'GERD', 'gerd'],
              ['barrett', 'Barrett esophagus', 'barrett'], ['ring', 'Schatzki ring', 'schatzki'], ['strict', 'Stricture', 'esostricture'],
              ['web', 'Plummer-Vinson web', 'esophagitis'], ['zenker', 'Zenker diverticulum', 'zenker'], ['mw', 'Mallory-Weiss tear', 'mallorywb']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 377, 384–385 · Robbins ch 17 · Guyton ch 64')
dyn['switches'][0]['def'] = dyn['switches'][0].pop('def_')

MAP = dict(
  id='esosim', title='Swallowing in Motion', topic='gi', after='gitract',
  sub='Watch a bolus ride the peristaltic wave through both sphincters, switch solids for liquids, then see it stick, reflux or spill — '
      'achalasia, esophageal spasm, GERD, Barrett, Schatzki ring, stricture, Plummer-Vinson web, Zenker and Mallory-Weiss',
  w=3600, h=1900,
  fa='377, 384, 385, 391',
  src=['Robbins ch 17 — The gastrointestinal tract', 'Katzung ch 62 — Drugs Used in the Treatment of Gastrointestinal Diseases',
       'Robbins ch 8 — Infectious diseases', 'Moore ch 8 — Neck', 'Bootcamp.com Gastroenterology — Esophagus',
       'Guyton ch 64 — Propulsion and Mixing of Food in the Alimentary Tract', 'Costanzo ch 8 — Gastrointestinal physiology'],
  lanes=[('eoMot', 'Motility', 'glycolysis'), ('eoMuc', 'Reflux & mucosa', 'tca'), ('eoObs', 'Narrowing & pouches', 'gluconeo')],
  nodes=[
    ('es1', 'Swallowing', 330, 1660, 'eoMot', 'reflex · peristalsis', ['swallowing'], 'hub'),
    ('es2', 'Achalasia · spasm', 760, 1660, 'eoMot', 'bird’s beak · corkscrew', ['achalasia']),
    ('es3', 'GERD', 1200, 1660, 'eoMuc', 'transient LES relaxation', ['gerd']),
    ('es4', 'Barrett esophagus', 1640, 1660, 'eoMuc', 'goblet cells', ['barrett']),
    ('es5', 'Esophagitis · webs', 2080, 1660, 'eoMuc', 'pill, Candida, Plummer-Vinson', ['esophagitis']),
    ('es6', 'Schatzki ring', 330, 1790, 'eoObs', 'distal ring', ['schatzki']),
    ('es7', 'Stricture', 760, 1790, 'eoObs', 'solids first', ['esostricture']),
    ('es8', 'Zenker diverticulum', 1200, 1790, 'eoObs', 'Killian triangle', ['zenker']),
    ('es9', 'Mallory-Weiss · Boerhaave', 1640, 1790, 'eoMuc', 'tear vs rupture', ['mallorywb'])],
  panels=[
    (2500, PANY, 1000, 'Dysphagia: solids or liquids? (First Aid p. 384)', [
      ('Solids AND liquids from the start', 'achalasia (motility)'),
      ('Solids first, progressive', 'stricture, cancer (obstruction)'),
      ('Solids, non-progressive', 'web, ring'),
      ('Pain on swallowing', 'esophagitis (pill, Candida, HSV, CMV)')])],
  dyn=dyn)
