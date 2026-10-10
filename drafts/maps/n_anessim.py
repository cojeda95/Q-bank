# Anesthetics in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Gas moves alveolus → blood → brain, with partial-pressure bars filling over `t` (steps, auto: early → later) and a MAC
# line on the brain bar. A `one` switch picks the agent: nitrous oxide (low blood solubility — brain follows fast; very weak,
# so its MAC line sits high), a volatile agent (potent — low MAC line; depresses brain, breathing and myocardium, raises
# cerebral blood flow), propofol (GABA-A + NMDA, hypotension) or etomidate (hemodynamically neutral, adrenal suppression).
# Toggles add succinylcholine to a volatile (malignant hyperthermia, RYR1 → dantrolene) and a pneumothorax to N₂O. Bar
# heights are schematic — the cards give no numbers. 6 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

G = lambda *k: [f'ag:{x}' for x in k]
def GT(g, *t): return [f'ag:{g}&t:{x}' for x in t]
PANY = 1180
BY = 1300

text('Anesthetics — from the lung to the brain, and what they do on the way', 180, 150, 'dyn-big')
text('bar heights schematic · MAC = alveolar concentration that keeps 50% from moving at skin incision', 180, 176, 'dyn-cap')

# ════════ compartments ════════
BOX = dict(alv=(380, 'alveolus'), blood=(760, 'blood'), brain=(1140, 'brain'))
for k, (x, l) in BOX.items():
    add(f'<rect x="{x}" y="{BY - 500}" width="160" height="500" rx="20" style="fill:var(--surface);stroke:var(--dk3);stroke-width:4"/>')
    text(l, x + 80, BY + 40, 'nf-l1', 'middle')
add(f'<path d="M540 {BY - 250} H760 M920 {BY - 250} H1140" style="stroke:var(--ink-3);stroke-width:4;stroke-dasharray:10 8"/>')
H = {('n2o', 'early'): (380, 320, 300), ('n2o', 'late'): (420, 400, 390), ('vol', 'early'): (380, 160, 120), ('vol', 'late'): (420, 330, 300)}
for (g, t), hs in H.items():
    for (k, (x, _)), h in zip(BOX.items(), hs):
        add(f'<rect x="{x + 10}" y="{BY - 10 - h}" width="140" height="{h}" rx="12" style="fill:var(--dk9);fill-opacity:.45"/>', when=GT(g, t))
add(f'<path d="M1120 {BY - 470} H1320" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:10 6"/>', when=G('n2o'))
text('MAC — very high (weak)', 1330, BY - 464, 'nf-l1', when=G('n2o'))
add(f'<path d="M1120 {BY - 200} H1320" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:10 6"/>', when=G('vol'))
text('MAC — low (potent)', 1330, BY - 194, 'nf-l1', when=G('vol'))
text('low blood solubility — blood saturates, brain follows fast', 760, BY - 560, 'nf-l1 dyn-tag', 'middle', when=G('n2o'))
text('high lipid solubility — potent', 760, BY - 560, 'nf-l1 dyn-tag', 'middle', when=G('vol'))
add('<path d="M840 420 V780" style="stroke:var(--ink-2);stroke-width:10"/>', when=G('prop', 'etom'))
add('<rect x="800" y="360" width="80" height="60" rx="10" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>', when=G('prop', 'etom'))
text('IV induction', 900, 400, 'nf-l1', when=G('prop', 'etom'))
# targets
TG = dict(heart=(1700, 520, 'heart · blood pressure'), lungs=(1700, 760, 'breathing drive'), adrenal=(1700, 1000, 'adrenal (cortisol)'),
          muscle=(1700, 1240, 'skeletal muscle'))
for k, (x, y, l) in TG.items():
    add(f'<circle cx="{x}" cy="{y}" r="50" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:3"/>'); text(l, x + 70, y + 6, 'nf-l1')
add('<circle cx="1700" cy="520" r="50" style="fill:var(--bad);fill-opacity:.25"/>', when=G('vol', 'prop'))
add('<circle cx="1700" cy="760" r="50" style="fill:var(--bad);fill-opacity:.25"/>', when=G('vol', 'prop'))
add('<circle cx="1700" cy="1000" r="50" style="fill:var(--bad);fill-opacity:.35"/>', when=G('etom'))
add('<circle cx="1700" cy="1240" r="50" style="fill:var(--bad);fill-opacity:.45"/>', when=['ag:vol&sux'])
text('RYR1 — rigidity, hypercapnia, tachycardia, hyperthermia → dantrolene', 1700, 1330, 'nf-l1 dyn-tag', 'middle', when=['ag:vol&sux'])
add('<ellipse cx="460" cy="650" rx="70" ry="50" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3;stroke-dasharray:6 6"/>', when=['ptx'], unless=G('n2o'))
add('<ellipse cx="460" cy="650" rx="120" ry="80" style="fill:var(--surface);stroke:var(--bad);stroke-width:5"/>', when=['ag:n2o&ptx'])
text('pneumothorax', 460, 560, 'nf-l1', 'middle', when=['ptx'])
text('N₂O diffuses in and expands it — never with a pneumothorax', 460, 760, 'nf-l1 dyn-tag', 'middle', when=['ag:n2o&ptx'])
TAG = dict(prop='propofol — GABA-A + NMDA block; rapid, short; hypotension, respiratory depression',
           etom='etomidate — hemodynamically neutral (unstable patient), but suppresses the adrenals',
           vol='volatile — depresses brain, breathing, myocardium; ↑ cerebral blood flow (↑ ICP); PONV',
           n2o='nitrous oxide — fast, very weak')
for k, s in TAG.items(): text(s, 1000, 1440, 'nf-l1', 'middle', when=G(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M200 {BY - 250} H460', len=260, speed=120, r=9, base=dict(gas=3), when=G('n2o', 'vol')),
  dict(d=f'M540 {BY - 250} H840', len=300, speed=120, r=9, base=dict(gas=3), when=G('n2o', 'vol'), mods=[m(G('n2o'), speed=1.8)]),
  dict(d=f'M920 {BY - 250} H1220', len=300, speed=120, r=9, base=dict(gas=3), when=G('n2o', 'vol'), mods=[m(G('n2o'), speed=1.8)]),
  dict(d='M840 420 V780 C840 820 1000 820 1220 800', len=760, speed=150, r=9, base=dict(iv=3), when=G('prop', 'etom')),
  dict(d='M1300 800 C1450 700 1550 560 1650 520', len=500, speed=110, r=8, base=dict(eff=2), when=G('vol', 'prop')),
  dict(d='M1300 800 C1450 800 1550 780 1650 760', len=400, speed=110, r=8, base=dict(eff=2), when=G('vol', 'prop')),
  dict(d='M1300 800 C1450 900 1550 980 1650 1000', len=400, speed=110, r=8, base=dict(eff=2), when=G('etom')),
  dict(d='M520 650 C500 640 480 640 460 650', len=80, speed=40, r=8, base=dict(gas=3), when=['ag:n2o&ptx']),
]
sites = [dict(x=1220, y=760, n=[1, -1], w=10, t='rec', l='', aria='Solubility and MAC', c='genanes', ions=[]),
         dict(x=460, y=760, n=[-1, 1], w=10, t='rec', l='', aria='Inhaled anesthetics', c='inhaledanes', ions=[]),
         dict(x=760, y=380, n=[-1, 0], w=10, t='rec', l='', aria='Propofol', c='propofol', ions=[]),
         dict(x=1760, y=1060, n=[1, 1], w=10, t='rec', l='', aria='Etomidate', c='etomidate', ions=[])]

readouts = [
  dict(l='Blood pressure', mods=[dict(when=G('vol', 'prop'), d=-1), dict(when=G('etom'), d=0)]),
  dict(l='Respiratory drive', mods=[dict(when=G('vol', 'prop'), d=-1)]),
  dict(l='Cerebral blood flow (ICP)', mods=[dict(when=G('vol'), d=1)]),
  dict(l='Cortisol', mods=[dict(when=G('etom'), d=-1)]),
  dict(l='Temperature', mods=[dict(when=['ag:vol&sux'], d=1)]),
  dict(l='Pneumothorax size', mods=[dict(when=['ag:n2o&ptx'], d=1)]),
]

notes = {
  '': 'CNS drugs must be lipid-soluble to cross the blood-brain barrier. Inhaled agents: low blood solubility → blood saturates '
      'quickly and the brain follows (fast in, fast out); high lipid solubility → potent. Potency = 1/MAC.',
  'ag:n2o': 'Nitrous oxide: fast but very weak (very high MAC); it diffuses into gas-filled spaces and expands them — a '
            'pneumothorax or bowel gas.',
  'ag:vol': 'Sevoflurane, desflurane, isoflurane: depress the brain, respiratory drive and myocardium (↓ BP); ↑ cerebral blood '
            'flow (↑ ICP) with ↓ metabolic rate; ↓ muscle tone; PONV. Isoflurane = high lipid solubility, high potency.',
  'ag:prop': 'Propofol: the commonest IV induction agent — enhances GABA-A, blocks NMDA; rapid and short; hypotension and '
             'respiratory depression.',
  'ag:etom': 'Etomidate: GABA-A potentiator that is hemodynamically neutral — for the hypotensive patient — but can cause acute '
             'adrenal insufficiency; PONV.',
  'sux': 'Volatile anesthetic + succinylcholine in an RYR1-susceptible patient → malignant hyperthermia: hypercapnia, '
         'tachycardia, rigidity, rhabdomyolysis, hyperthermia. Dantrolene.',
  'ptx': 'Never give N₂O with a pneumothorax — it expands it.',
}

dyn = dict(
  kinds=dict(gas=['mov', '--dk9'], iv=['mov', '--dk4'], eff=['mov', '--bad']), groups=[['mov', 'Gas · IV drug · effects']],
  switches=[dict(id='ag', label='Agent', type='one', options=[
              ['n2o', 'Nitrous oxide', 'inhaledanes'], ['vol', 'Volatile (sevo/des/iso)', 'inhaledanes'],
              ['prop', 'Propofol', 'propofol'], ['etom', 'Etomidate', 'etomidate']]),
            dict(id='t', label='Time', type='steps', auto=3, options=[['early', 'Early'], ['late', 'Later']]),
            dict(id='sux', label='Add', type='toggle', on='Succinylcholine given', off='Succinylcholine', def_=False),
            dict(id='ptx', label='Patient', type='toggle', on='Pneumothorax', off='Pneumothorax', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Katzung ch 25')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='anessim', title='Anesthetics in Motion', topic='pharm', after='anesth',
  sub='Breathe nitrous oxide or a volatile agent from alveolus to brain against its MAC line, or push propofol or etomidate — '
      'and watch blood pressure, breathing, ICP, cortisol, malignant hyperthermia and a pneumothorax respond',
  w=3600, h=1900,
  fa='565, 566',
  src=['Katzung ch 25 — General Anesthetics'],
  lanes=[('anInh', 'Inhaled', 'tca'), ('anIv', 'Intravenous', 'glycolysis')],
  nodes=[
    ('an1', 'Solubility & MAC', 330, 1720, 'anInh', 'potency = 1/MAC', ['genanes'], 'hub'),
    ('an2', 'Inhaled anesthetics', 760, 1720, 'anInh', 'N₂O · volatiles · MH', ['inhaledanes']),
    ('an3', 'Propofol', 1200, 1720, 'anIv', 'GABA-A · NMDA', ['propofol']),
    ('an4', 'Etomidate', 1640, 1720, 'anIv', 'neutral BP · adrenals', ['etomidate'])],
  panels=[
    (2500, PANY, 1000, 'Solubility rules (Katzung ch 25)', [
      ('Low blood:gas', 'fast in, fast out (N₂O)'), ('High oil:gas', 'potent (isoflurane)'), ('Potency', '1 / MAC')])],
  dyn=dyn)
