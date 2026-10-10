# Platelets in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A vessel with an injured wall: exposed collagen, vWF bridging collagen to platelet GpIb (adhesion), ADP on P2Y12 and
# TXA₂ from COX-1 amplifying activation, and GpIIb/IIIa linking platelets through fibrinogen (aggregation) into a plug.
# Platelets and red cells stream through the lumen; one platelet is drawn close up with its receptors. A `one` switch
# shows ITP, TTP/HUS, DIC, von Willebrand disease, Bernard-Soulier, Glanzmann, uremia, aspirin, P2Y12 inhibitors,
# GpIIb/IIIa inhibitors and HIT. 5 readouts (platelet count, bleeding time, PT, PTT, schistocytes). Facts from the
# pinned cards; FA pages in `fa`. No new cards.
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

SW = 'dz'
O = lambda *k: [f'{SW}:{x}' for x in k]
PANY = 1150
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def plt(x, y, r=17, extra=''): return f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--dk10);fill-opacity:.55;stroke:var(--dk10);stroke-width:3{extra}"/>'
NO_ADH = O('vwd', 'bss')
NO_AGG = NO_ADH + O('glanz', 'gp2b3a')
SMALL = O('aspirin', 'p2y12', 'uremia', 'itp')

text('Primary hemostasis — collagen, vWF and the platelet plug', 180, 150, 'dyn-big')
text('adhesion (GpIb–vWF) → activation (ADP, TXA₂) → aggregation (GpIIb/IIIa–fibrinogen)', 180, 176, 'dyn-cap')

# ════════ the vessel ════════
LY0, LY1 = 420, 760
add(f'<rect x="300" y="{LY0}" width="1900" height="{LY1 - LY0}" style="fill:var(--nf-blood);fill-opacity:.07"/>')
add(f'<path d="M300 {LY0} H2200" style="stroke:var(--dk3);stroke-width:10;opacity:.5"/>')
add(f'<path d="M300 {LY1} H1000 M1500 {LY1} H2200" style="stroke:var(--dk3);stroke-width:10;opacity:.5"/>')
add(f'<path d="M1000 {LY1 + 20} l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16 l25 -16 l25 16" style="fill:none;stroke:var(--dk6);stroke-width:6"/>')
text('endothelium — PGI₂, NO: keeps blood from clotting', 640, LY1 + 50, 'nf-l2', 'middle')
text('injury: exposed collagen', 1250, LY1 + 90, 'nf-l1', 'middle')
text('blood flow →', 320, LY0 - 16, 'nf-l2')

# vWF strands from the collagen
for x in range(1040, 1480, 60):
    add(f'<path d="M{x} {LY1 + 10} q-10 -30 0 -60" style="fill:none;stroke:var(--dk7);stroke-width:4"/>', unless=O('vwd'))
# the plug: adhesion row, then aggregate rows
ROW1 = [(x, LY1 - 30) for x in range(1040, 1480, 40)]
ROW2 = [(x, LY1 - 64) for x in range(1080, 1440, 40)]
ROW3 = [(x, LY1 - 98) for x in range(1140, 1380, 40)]
add(''.join(plt(x, y) for x, y in ROW1), unless=NO_ADH + O('itp'))
add(''.join(plt(x, y) for x, y in ROW1[::2]), when=O('itp'))
add(''.join(plt(x, y) for x, y in ROW2), unless=NO_AGG + O('itp'))
add(''.join(plt(x, y) for x, y in ROW3), unless=NO_AGG + SMALL)
text('platelets stick but never link up', 1250, LY0 + 60, 'nf-l1 dyn-tag', 'middle', when=O('glanz', 'gp2b3a'))
text('no vWF bridge — nothing sticks', 1250, LY0 + 60, 'nf-l1 dyn-tag', 'middle', when=O('vwd'))
text('no GpIb receptor — nothing sticks; giant platelets', 1250, LY0 + 60, 'nf-l1 dyn-tag', 'middle', when=O('bss'))
text('weaker activation — a smaller plug', 1250, LY0 + 60, 'nf-l1 dyn-tag', 'middle', when=O('aspirin', 'p2y12', 'uremia'))
text('IgG-coated platelets eaten by splenic macrophages', 1250, LY0 + 60, 'nf-l1 dyn-tag', 'middle', when=O('itp'))

# TTP: ultra-large vWF multimers and microthrombi in the lumen
for x0 in (420, 1650):
    add(f'<path d="M{x0} 560 q40 -40 80 0 t80 0 t80 0 t80 0" style="fill:none;stroke:var(--dk7);stroke-width:6"/>' + plt(x0 + 100, 548, 14) + plt(x0 + 210, 572, 14), when=O('ttp'))
text('no ADAMTS13 — ultra-large vWF grabs platelets in flowing blood', 1250, LY0 - 16, 'nf-l1 dyn-tag', 'middle', when=O('ttp'))
# DIC: clots everywhere, oozing at the injury
for (x, y) in ((520, 640), (1800, 520), (2050, 680)):
    add(f'<ellipse cx="{x}" cy="{y}" rx="46" ry="26" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:3"/>', when=O('dic', 'hit'))
text('clotting and bleeding at the same time', 1250, LY0 - 16, 'nf-l1 dyn-tag', 'middle', when=O('dic'))
text('IgG to heparin–PF4: platelets fall at day 5–10 and the patient clots', 1250, LY0 - 16, 'nf-l1 dyn-tag', 'middle', when=O('hit'))

# ════════ one platelet, close up ════════
PX, PY, PR = 1250, 1180, 170
add(f'<path d="M1250 {LY1 + 110} V{PY - PR - 60}" style="stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 8"/>')
add(f'<circle cx="{PX}" cy="{PY}" r="{PR}" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/>')
add(f'<circle cx="{PX}" cy="{PY}" r="{PR + 40}" style="fill:none;stroke:var(--dk10);stroke-width:3;stroke-dasharray:8 8"/>', when=O('bss'))
text('one platelet, close up', PX, PY + 6, 'nf-l1', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
FEW = O('itp', 'ttp', 'dic', 'bss', 'hit')
flows = [dict(d=f'M300 {y} H2200', len=1900, speed=220, r=9, base=dict(plt=3), mods=[m(FEW, set=dict(plt=1))]) for y in (520, 620, 700)]
flows += [dict(d='M300 470 H2200', len=1900, speed=220, r=12, base=dict(rbc=4)),
          dict(d=f'M1180 {LY1 - 40} V{LY1 + 120}', len=160, speed=60, r=8, base=dict(rbc=3), when=O('vwd', 'bss', 'glanz', 'gp2b3a', 'dic', 'itp')),
          dict(d=f'M{PX - 120} {PY - 120} L{PX} {PY - PR - 30}', len=200, speed=80, r=7, base=dict(adp=3), unless=O('p2y12'))]
sites = [
  dict(x=PX - PR, y=PY, n=[-1, 0], w=12, t='rec', l='GpIb', s='binds vWF → adhesion', c='bernardsoulier', ions=[],
       block=O('bss'), stop=O('vwd')),
  dict(x=PX + PR, y=PY, n=[1, 0], w=12, t='rec', l='GpIIb/IIIa', s='binds fibrinogen → aggregation', c='glanzmann', ions=[],
       block=O('glanz', 'gp2b3a'), low=O('aspirin', 'p2y12'), sfx=dict(block=' — blocked / missing')),
  dict(x=PX, y=PY - PR, n=[0, -1], w=12, t='rec', l='P2Y12', s='ADP amplifies activation', c='p2y12', ions=[],
       block=O('p2y12')),
  dict(x=PX, y=PY + PR, n=[0, 1], w=12, t='ch', l='COX-1 → TXA₂', s='aspirin: irreversible, 7–10 days', c='aspirin', ions=[],
       block=O('aspirin')),
  dict(x=1250, y=LY1 + 20, n=[0, 1], w=10, t='rec', l='', aria='von Willebrand factor', c='vwd', ions=[]),
]

readouts = [
  dict(l='Platelet count', mods=[dict(when=FEW, d=-1), dict(when=O('vwd', 'glanz', 'uremia'), d=0)]),
  dict(l='Bleeding time', mods=[dict(when=O('vwd', 'bss', 'glanz', 'aspirin', 'uremia'), d=1)]),
  dict(l='PT', mods=[dict(when=O('dic'), d=1), dict(when=O('itp', 'ttp', 'aspirin'), d=0)]),
  dict(l='PTT', mods=[dict(when=O('dic', 'vwd'), d=1), dict(when=O('itp', 'ttp', 'aspirin'), d=0)]),
  dict(l='Schistocytes', mods=[dict(when=O('ttp', 'dic'), d=1), dict(when=O('itp'), d=0)]),
]

notes = {
  '': 'A healthy endothelium is an anticoagulant organ (PGI₂, NO). Expose collagen and primary hemostasis starts in seconds: vWF '
      'bridges collagen to platelet GpIb (adhesion), released ADP (P2Y12) and TXA₂ amplify activation, and GpIIb/IIIa binds fibrinogen '
      'to cross-link one platelet to the next (aggregation).',
  'dz:itp': 'ITP: IgG against platelet glycoproteins (anti-GpIIb/IIIa) tags platelets for splenic macrophages. Isolated low platelets, '
            'normal PT and PTT, no schistocytes. Steroids or IVIG for bleeding.',
  'dz:ttp': 'TTP/HUS: without ADAMTS13, ultra-large vWF multimers grab platelets out of flowing blood into microthrombi, consuming '
            'platelets and shredding red cells — schistocytes with NORMAL PT and PTT. HUS: the same triad after Shiga toxin diarrhea.',
  'dz:dic': 'DIC: a massive stimulus (sepsis, trauma, obstetric, APL) activates coagulation everywhere — platelets and every factor '
            'are consumed, so the patient clots and bleeds at once: ↓ platelets, ↑ PT and PTT, ↓ fibrinogen, ↑ D-dimer.',
  'dz:vwd': 'von Willebrand disease: no vWF bridge, so platelets cannot adhere — mucocutaneous bleeding, long bleeding time with a '
            'normal count; PTT often long too, because vWF also protects factor VIII. Desmopressin releases stored vWF.',
  'dz:bss': 'Bernard-Soulier: the GpIb receptor is missing, so platelets cannot stick even with vWF present; giant platelets and a '
            'LOW count. Ristocetin fails, as in vWD.',
  'dz:glanz': 'Glanzmann thrombasthenia: no GpIIb/IIIa, so platelets adhere but never link up — long bleeding time with a NORMAL '
              'count and size; ristocetin normal.',
  'dz:uremia': 'Uremia: retained toxins impair platelet function — bleeding with a normal count and a long bleeding time. Dialysis; '
               'desmopressin for uremic bleeding.',
  'dz:aspirin': 'Aspirin acetylates COX-1 irreversibly, cutting TXA₂ for the platelet’s 7–10 day life — long bleeding time, no effect '
                'on PT or PTT.',
  'dz:p2y12': 'P2Y12 inhibitors (clopidogrel, prasugrel, ticagrelor) block the ADP amplification loop that puts GpIIb/IIIa on the '
              'surface — a different amplifier from aspirin, so the two are combined after stenting.',
  'dz:gp2b3a': 'GpIIb/IIIa inhibitors (abciximab, eptifibatide, tirofiban) block the final common step of aggregation — a '
               'pharmacologic Glanzmann. Risks: bleeding and thrombocytopenia.',
  'dz:hit': 'HIT (type 2): IgG against heparin–PF4 complexes — platelets drop about 5–10 days in and the patient paradoxically clots. '
            'Stop heparin; switch to argatroban (fondaparinux is safe).',
}

dyn = dict(
  kinds=dict(plt=['blood', '--dk10'], rbc=['blood', '--nf-blood'], adp=['signal', '--dk2']),
  groups=[['blood', 'Platelets and red cells'], ['signal', 'ADP']],
  switches=[dict(id=SW, label='Disorder · drug', type='one', options=[
    ['itp', 'ITP', 'itp'], ['ttp', 'TTP / HUS', 'ttp'], ['dic', 'DIC', 'dic'], ['vwd', 'von Willebrand disease', 'vwd'],
    ['bss', 'Bernard-Soulier', 'bernardsoulier'], ['glanz', 'Glanzmann thrombasthenia', 'glanzmann'], ['uremia', 'Uremia', 'uremia'],
    ['aspirin', 'Aspirin', 'aspirin'], ['p2y12', 'Clopidogrel (P2Y12)', 'p2y12'], ['gp2b3a', 'Abciximab (GpIIb/IIIa)', 'gp2b3a'],
    ['hit', 'Heparin-induced thrombocytopenia', 'heparin']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 417, 432–433, 440–442 · Robbins ch 4, 14 · Katzung ch 34')

MAP = dict(
  id='pltsim', title='Platelets in Motion', topic='heme', after='coagflow',
  sub='Watch platelets stick to exposed collagen through vWF and GpIb, amplify with ADP and TXA₂ and link through GpIIb/IIIa — then '
      'break each step: ITP, TTP/HUS, DIC, von Willebrand, Bernard-Soulier, Glanzmann, uremia, aspirin, clopidogrel, abciximab and HIT',
  w=3600, h=1900,
  fa='254, 319, 417, 432, 433, 440, 441, 442, 496, 621, 693',
  src=['Robbins ch 4 — Hemodynamic disorders, thromboembolic disease, and shock',
       'Marks ch 43 — Blood Plasma Proteins, Coagulation, and Fibrinolysis', 'Katzung ch 34 — Drugs Used in Disorders of Coagulation',
       'Robbins ch 14 — Red blood cell and bleeding disorders', 'Robbins ch 20 — The kidney',
       'Katzung ch 37 — Hypothalamic & Pituitary Hormones'],
  lanes=[('plNorm', 'Primary hemostasis', 'glycolysis'), ('plDz', 'Platelet disorders', 'tca'), ('plRx', 'Antiplatelet & heparin', 'gluconeo')],
  nodes=[
    ('pl1', 'Endothelium & collagen', 330, 1620, 'plNorm', 'injury starts it', ['endothreg'], 'hub'),
    ('pl2', 'ITP', 760, 1620, 'plDz', 'isolated low count', ['itp']),
    ('pl3', 'TTP · HUS', 1200, 1620, 'plDz', 'schistocytes, normal PT/PTT', ['ttp']),
    ('pl4', 'DIC', 1640, 1620, 'plDz', 'clots and bleeds', ['dic']),
    ('pl5', 'von Willebrand disease', 2080, 1620, 'plDz', 'adhesion fails', ['vwd']),
    ('pl6', 'Bernard-Soulier · Glanzmann', 330, 1760, 'plDz', 'GpIb vs GpIIb/IIIa', ['bernardsoulier', 'glanzmann']),
    ('pl7', 'Uremic bleeding', 760, 1760, 'plDz', 'normal count', ['uremia']),
    ('pl8', 'Aspirin · P2Y12 inhibitors', 1200, 1760, 'plRx', 'TXA₂ vs ADP', ['aspirin', 'p2y12']),
    ('pl9', 'GpIIb/IIIa inhibitors', 1640, 1760, 'plRx', 'drug Glanzmann', ['gp2b3a']),
    ('pl10', 'Heparin · HIT', 2080, 1760, 'plRx', 'day 5–10 drop', ['heparin'])],
  panels=[
    (2500, PANY, 1000, 'Schistocytes? Check the PT and PTT (First Aid p. 432)', [
      ('TTP / HUS', 'normal PT and PTT — platelet consumption'),
      ('DIC', 'prolonged PT and PTT, ↓ fibrinogen, ↑ D-dimer'),
      ('ITP', 'no schistocytes — isolated low platelets'),
      ('Ristocetin', 'fails in vWD and Bernard-Soulier, normal in Glanzmann')])],
  dyn=dyn)
