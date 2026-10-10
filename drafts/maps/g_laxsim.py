# Laxatives in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A stretch of bowel: stool moving through the lumen, the epithelium with ClC-2, GC-C → CFTR and NHE3, and the enteric
# plexus with μ-opioid receptors. A `rx` switch gives one laxative — bulk fiber, docusate, mineral oil, osmotic (PEG,
# lactulose, magnesium), stimulant (senna, bisacodyl), lubiprostone, linaclotide, tenapanor or a peripheral opioid antagonist
# — and shows where it acts; an `opioid` toggle slows propulsion (μ receptors) so the PAMORA has something to undo. The
# small-bowel vs colon site of each channel is labelled only where the card names it. 3 readouts. Facts from the pinned
# cards; FA pages in `fa`. No new cards.
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

R = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
LY0, LY1 = 520, 760
CH = dict(clc=(800, 'ClC-2 (small intestine)'), gcc=(1100, 'GC-C → cGMP → CFTR'), nhe=(1400, 'NHE3'))

text('Laxatives — where each one makes stool move', 180, 150, 'dyn-big')
text('a stretch of bowel: lumen on top, epithelium, enteric plexus below', 180, 176, 'dyn-cap')

# ════════ bowel ════════
add(f'<rect x="300" y="{LY0}" width="1700" height="{LY1 - LY0}" rx="40" style="fill:var(--dk5);fill-opacity:.08;stroke:var(--dk5);stroke-width:4"/>')
text('lumen', 320, LY0 - 16, 'nf-l1')
for x in range(340, 2000, 80):
    add(f'<rect x="{x}" y="{LY1}" width="70" height="70" rx="10" style="fill:var(--dk2);fill-opacity:.12;stroke:var(--dk2);stroke-width:2"/>')
text('epithelium', 2020, LY1 + 40, 'nf-l2')
add(f'<path d="M300 {LY1 + 130} H2000" style="stroke:var(--dk7);stroke-width:8;opacity:.5"/>'); text('enteric plexus', 2020, LY1 + 136, 'nf-l2')
for k, (x, l) in CH.items():
    add(f'<rect x="{x - 14}" y="{LY1 - 6}" width="28" height="82" rx="8" style="fill:var(--dk9);opacity:.6"/>'); text(l, x, LY1 + 110, 'nf-l2', 'middle')
add(f'<circle cx="1700" cy="{LY1 + 130}" r="22" style="fill:var(--dk4);fill-opacity:.4;stroke:var(--dk4);stroke-width:3"/>'); text('μ receptors', 1700, LY1 + 180, 'nf-l2', 'middle')
add(f'<circle cx="1700" cy="{LY1 + 130}" r="22" style="fill:var(--bad);fill-opacity:.7"/>', when=['opioid'], unless=['opioid&rx:pamora'])
add(f'<path d="M1680 {LY1 + 110} l40 40 M1720 {LY1 + 110} l-40 40" class="nf-x"/>', when=['opioid&rx:pamora'])
# stool
add(f'<ellipse cx="1100" cy="640" rx="200" ry="90" style="fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:3"/>', unless=R('bulk'))
add(f'<ellipse cx="1100" cy="640" rx="280" ry="110" style="fill:var(--dk6);fill-opacity:.35;stroke:var(--dk6);stroke-width:3"/>', when=R('bulk'))
add(f'<ellipse cx="1100" cy="640" rx="200" ry="90" style="fill:var(--nf-h2o);fill-opacity:.35"/>', when=R('osm', 'lubi', 'lina', 'tena', 'docu'))
add(f'<ellipse cx="1100" cy="640" rx="210" ry="96" style="fill:none;stroke:var(--accent);stroke-width:8"/>', when=R('oil'))
for k, (x, _) in CH.items():
    add(f'<rect x="{x - 14}" y="{LY1 - 6}" width="28" height="82" rx="8" style="fill:var(--accent);opacity:.9"/>',
        when=R(dict(clc='lubi', gcc='lina', nhe='tena')[k]))
add(f'<path d="M300 {LY1 + 130} H2000" style="stroke:var(--accent);stroke-width:14;opacity:.6"/>', when=R('stim'))
TAG = dict(bulk='fiber swells into a gel — stretches the colon so it propels · bloating, flatus',
           docu='docusate — surfactant lets water and fat soak into stool', oil='mineral oil — lubricates; aspiration → lipid pneumonitis; ↓ A D E K',
           osm='unabsorbed solute holds water · Mg (not in renal failure), lactulose (ferments; traps NH₄⁺), PEG (isotonic prep)',
           stim='senna, bisacodyl — excite the enteric nerves and colonic secretion · melanosis coli (senna)',
           lubi='lubiprostone opens ClC-2 — chloride and water into the lumen · nausea',
           lina='linaclotide — GC-C → cGMP → CFTR opens · diarrhea; not in children',
           tena='tenapanor blocks NHE3 — Na⁺ and water stay in the lumen',
           pamora='methylnaltrexone, naloxegol — block gut μ receptors, spare central analgesia')
for k, s in TAG.items(): text(s, 1150, 1100, 'nf-l1 dyn-tag', 'middle', when=R(k))
text('opioid: propulsion falls, tone rises — stool lingers and dries (no tolerance to this)', 1150, 1140, 'nf-l1', 'middle', when=['opioid'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FAST = R('bulk', 'osm', 'stim', 'lubi', 'lina', 'tena')
flows = [
  dict(d='M320 640 H1980', len=1660, speed=90, r=11, base=dict(stool=4),
       mods=[m(FAST, speed=1.8), m(['opioid'], speed=0.3), m(['opioid&rx:pamora'], speed=3.3)]),
  dict(d=f'M{CH["clc"][0]} {LY1 + 60} V{LY0 + 60}', len=240, speed=90, r=8, base=dict(cl=3), when=R('lubi')),
  dict(d=f'M{CH["gcc"][0]} {LY1 + 60} V{LY0 + 60}', len=240, speed=90, r=8, base=dict(cl=3), when=R('lina')),
  dict(d=f'M{CH["nhe"][0]} {LY0 + 60} V{LY1 - 20}', len=220, speed=90, r=8, base=dict(na=3), when=R('tena')),
  dict(d=f'M{CH["nhe"][0]} {LY0 + 60} V{LY1 + 60}', len=280, speed=90, r=8, base=dict(na=3), unless=R('tena')),
  dict(d=f'M500 {LY1 + 40} V{LY0 + 60}', len=240, speed=80, r=8, base=dict(h2o=3), when=R('osm', 'lubi', 'lina', 'tena', 'bulk')),
  dict(d=f'M300 {LY1 + 130} H2000', len=1700, speed=200, r=8, base=dict(nerve=4), when=R('stim')),
]
sites = [dict(x=1100, y=520, n=[0, -1], w=10, t='rec', l='', aria='Bulk-forming and softeners', c='bulklax', ions=[]),
         dict(x=500, y=520, n=[0, -1], w=10, t='rec', l='', aria='Osmotic laxatives', c='osmolax', ions=[]),
         dict(x=400, y=LY1 + 130, n=[-1, 0], w=10, t='rec', l='', aria='Stimulant laxatives', c='stimlax', ions=[]),
         dict(x=950, y=LY1 + 40, n=[0, 1], w=10, t='rec', l='', aria='Intestinal secretagogues', c='secretlax', ions=[]),
         dict(x=1760, y=LY1 + 130, n=[1, 0], w=10, t='rec', l='', aria='Peripheral opioid antagonists', c='pamora', ions=[])]

readouts = [
  dict(l='Stool water', mods=[dict(when=R('osm', 'lubi', 'lina', 'tena', 'docu', 'bulk'), d=1), dict(when=['opioid'], d=-1)]),
  dict(l='Transit speed', mods=[dict(when=FAST, d=1), dict(when=['opioid'], d=-1), dict(when=['opioid&rx:pamora'], d=1)]),
  dict(l='Bloating · flatus', mods=[dict(when=R('bulk', 'osm'), d=1)]),
]

notes = {
  '': 'Stool moves when the colon is stretched, the stool holds water, or the enteric nerves and epithelium are pushed. Fiber, '
      'fluid, exercise and answering the urge come before any drug.',
  'rx:bulk': 'Bulk-forming (psyllium, methylcellulose, polycarbophil): water-loving fiber swells into a gel that stretches the '
             'colon; bacteria ferment plant fiber → bloating, flatus.',
  'rx:docu': 'Docusate (emollient): a surfactant that lowers stool surface tension so water and fat soak in — common in '
             'hospitalized patients.',
  'rx:oil': 'Mineral oil: lubricates stool and slows water absorption; aspiration → lipid pneumonitis; long-term → poor A, D, E, K.',
  'rx:osm': 'Osmotic: unabsorbed solute holds water. Mg hydroxide (avoid in renal insufficiency); lactulose/sorbitol ferment '
            '(cramps) — lactulose traps NH₄⁺ in hepatic encephalopathy; PEG is isotonic for colonoscopy prep.',
  'rx:stim': 'Stimulants: act on the enteric nervous system and colonic secretion. Senna (6–12 h oral) → melanosis coli; '
             'bisacodyl (6–10 h oral, 30–60 min rectal).',
  'rx:lubi': 'Lubiprostone opens ClC-2 in the small intestine — chloride-rich fluid enters the lumen. Nausea; avoid if pregnancy '
             'possible.',
  'rx:lina': 'Linaclotide/plecanatide activate luminal guanylate cyclase-C → cGMP → CFTR opens → chloride and water out. Diarrhea; '
             'not in children. (ETEC heat-stable toxin uses the same messenger.)',
  'rx:tena': 'Tenapanor blocks NHE3 — Na⁺ and water stay in the lumen.',
  'rx:pamora': 'Methylnaltrexone (quaternary, cannot enter the brain), naloxegol, naldemedine block gut μ receptors — opioid '
               'constipation reverses without losing analgesia. Alvimopan: postoperative ileus.',
  'opioid': 'Opioids act on gut μ receptors: propulsive peristalsis falls, tone and nonpropulsive contractions rise — stool '
            'lingers and loses water. Tolerance never develops to this effect.',
}

dyn = dict(
  kinds=dict(stool=['mov', '--dk6'], cl=['mov', '--dk9'], na=['mov', '--dk4'], h2o=['mov', '--nf-h2o'], nerve=['mov', '--accent']),
  groups=[['mov', 'Stool · Cl⁻ · Na⁺ · water · nerve firing']],
  switches=[dict(id='rx', label='Laxative', type='one', options=[
              ['bulk', 'Bulk fiber', 'bulklax'], ['docu', 'Docusate', 'bulklax'], ['oil', 'Mineral oil', 'bulklax'],
              ['osm', 'Osmotic (PEG, lactulose, Mg)', 'osmolax'], ['stim', 'Stimulant (senna, bisacodyl)', 'stimlax'],
              ['lubi', 'Lubiprostone', 'secretlax'], ['lina', 'Linaclotide', 'secretlax'], ['tena', 'Tenapanor', 'secretlax'],
              ['pamora', 'Methylnaltrexone / naloxegol', 'pamora']]),
            dict(id='opioid', label='Patient', type='toggle', on='On opioids', off='Start an opioid', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Katzung ch 62')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='laxsim', title='Laxatives in Motion', topic='gi', after='gidrugs',
  sub='Move stool with fiber, softeners, osmotic agents, stimulants and secretagogues acting on ClC-2, GC-C and NHE3 — then give '
      'an opioid and undo its constipation with a peripheral μ antagonist',
  w=3600, h=1900,
  fa='130, 399, 408, 567',
  src=['Katzung ch 62 — Drugs Used in the Treatment of Gastrointestinal Diseases', 'Katzung ch 31 — Opioid Agonists & Antagonists'],
  lanes=[('lxStool', 'Change the stool', 'tca'), ('lxGut', 'Push the gut', 'glycolysis')],
  nodes=[
    ('lx1', 'Bulk-forming & softeners', 330, 1700, 'lxStool', 'fiber · docusate · oil', ['bulklax'], 'hub'),
    ('lx2', 'Osmotic laxatives', 760, 1700, 'lxStool', 'PEG · lactulose · Mg', ['osmolax']),
    ('lx3', 'Stimulant laxatives', 1200, 1700, 'lxGut', 'senna · bisacodyl', ['stimlax']),
    ('lx4', 'Intestinal secretagogues', 1640, 1700, 'lxGut', 'ClC-2 · GC-C · NHE3', ['secretlax']),
    ('lx5', 'Peripheral opioid antagonists', 2080, 1700, 'lxGut', 'gut μ only', ['pamora'])],
  panels=[
    (2500, PANY, 1000, 'Target of each (Katzung ch 62)', [
      ('Lubiprostone', 'ClC-2'), ('Linaclotide', 'GC-C → cGMP → CFTR'), ('Tenapanor', 'NHE3'), ('Methylnaltrexone', 'gut μ receptor'),
      ('Senna', 'enteric nerves')])],
  dyn=dyn)
