# Liver Blood Flow in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Left: the portal system — SMV and splenic vein → portal vein → liver → hepatic veins → IVC — with the three
# portosystemic anastomoses (esophagus, umbilicus, rectum). Right: one lobule — portal triad → zone 1 → 2 → 3 → central vein,
# with bile running the other way. A `dx` switch blocks or injures it: cirrhosis (inside the liver), portal vein thrombosis
# (before), Budd-Chiari (after — nutmeg liver), TIPS, and zone hits (viral hepatitis zone 1, yellow fever zone 2, ischemia and
# acetaminophen zone 3). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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
PORTAL_HTN = D('cirr', 'pvt', 'bc')

text('Liver blood flow — the portal system, its back roads, and the lobule zones', 180, 150, 'dyn-big')
text('left: portal vein in, hepatic veins out · right: one lobule, triad to central vein', 180, 176, 'dyn-cap')

# ════════ portal system ════════
LV = (700, 520)
add(f'<path d="M{LV[0] - 260} {LV[1] - 60} C{LV[0] - 200} {LV[1] - 200} {LV[0] + 220} {LV[1] - 200} {LV[0] + 260} {LV[1] - 40} C{LV[0] + 200} {LV[1] + 120} {LV[0] - 200} {LV[1] + 140} {LV[0] - 260} {LV[1] - 60} Z" '
    'style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>', unless=D('cirr', 'bc'))
add(f'<path d="M{LV[0] - 220} {LV[1] - 50} C{LV[0] - 170} {LV[1] - 160} {LV[0] + 180} {LV[1] - 160} {LV[0] + 220} {LV[1] - 40} C{LV[0] + 170} {LV[1] + 90} {LV[0] - 170} {LV[1] + 110} {LV[0] - 220} {LV[1] - 50} Z" '
    'style="fill:var(--dk6);fill-opacity:.2;stroke:var(--bad);stroke-width:5"/>', when=D('cirr'))
add(f'<path d="M{LV[0] - 300} {LV[1] - 60} C{LV[0] - 240} {LV[1] - 240} {LV[0] + 260} {LV[1] - 240} {LV[0] + 300} {LV[1] - 40} C{LV[0] + 240} {LV[1] + 160} {LV[0] - 240} {LV[1] + 180} {LV[0] - 300} {LV[1] - 60} Z" '
    'style="fill:var(--nf-blood);fill-opacity:.15;stroke:var(--bad);stroke-width:5"/>', when=D('bc'))
for x, y in ((620, 470), (720, 540), (800, 460), (660, 580)):
    add(f'<circle cx="{x}" cy="{y}" r="26" style="fill:none;stroke:var(--ink-3);stroke-width:5"/>', when=D('cirr'))
text('liver', LV[0], LV[1] - 230, 'nf-l1', 'middle')
add('<path d="M980 220 V1300" style="stroke:var(--nf-h2o);stroke-width:34;opacity:.25"/>'); text('IVC', 1000, 240, 'nf-l2')
add(f'<path d="M{LV[0] + 150} {LV[1] - 100} C850 380 920 360 980 360" style="fill:none;stroke:var(--nf-h2o);stroke-width:14;opacity:.5"/>'); text('hepatic veins', 860, 340, 'nf-l2', 'middle')
add('<path d="M870 330 l30 30 M900 330 l-30 30" class="nf-x"/>', when=D('bc'))
add('<path d="M700 640 V900" style="stroke:var(--dk9);stroke-width:24;opacity:.35"/>'); text('portal vein', 720, 760, 'nf-l2')
add('<path d="M690 760 h20" style="stroke:var(--bad);stroke-width:30"/>', when=D('pvt'))
add('<path d="M700 900 C600 950 520 1000 420 1020" style="fill:none;stroke:var(--dk9);stroke-width:16;opacity:.35"/>'); text('splenic v.', 420, 1000, 'nf-l2', 'end')
add('<ellipse cx="360" cy="1040" rx="70" ry="44" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>', unless=PORTAL_HTN)
add('<ellipse cx="340" cy="1040" rx="110" ry="70" style="fill:var(--dk10);fill-opacity:.25;stroke:var(--bad);stroke-width:4"/>', when=PORTAL_HTN)
text('spleen', 360, 1130, 'nf-l2', 'middle')
add('<path d="M700 900 V1200" style="fill:none;stroke:var(--dk9);stroke-width:16;opacity:.35"/>'); text('SMV (gut)', 720, 1180, 'nf-l2')
add('<path d="M700 900 C760 900 900 820 980 700" style="fill:none;stroke:var(--accent);stroke-width:14;opacity:.7"/>', when=D('tips'))
text('TIPS', 870, 820, 'nf-l1', when=D('tips'))
ANA = dict(eso=((520, 300), 'esophagus — left gastric ↔ esophageal (azygos): varices'), umb=((520, 860), 'umbilicus — paraumbilical ↔ epigastric: caput medusae'),
           rec=((520, 1280), 'rectum — superior ↔ middle/inferior rectal: anorectal varices'))
for k, ((x, y), l) in ANA.items():
    add(f'<circle cx="{x}" cy="{y}" r="22" style="fill:var(--nf-h2o);fill-opacity:.35;stroke:var(--dk9);stroke-width:3"/>', unless=PORTAL_HTN)
    add(f'<circle cx="{x}" cy="{y}" r="38" style="fill:var(--bad);fill-opacity:.35;stroke:var(--bad);stroke-width:4"/>', when=PORTAL_HTN)
    text(l, x - 40, y + 6, 'nf-l2', 'end')

# ════════ lobule ════════
LX, LY = 1720, 780
for r, z in ((330, 1), (220, 2), (110, 3)):
    add(f'<circle cx="{LX}" cy="{LY}" r="{r}" style="fill:var(--dk4);fill-opacity:{.06 + .05 * z};stroke:var(--dk4);stroke-width:2;stroke-dasharray:8 8"/>')
text('zone 1 periportal', LX + 270, LY - 300, 'nf-l2'); text('zone 2', LX + 170, LY - 190, 'nf-l2'); text('zone 3 pericentral', LX + 40, LY - 90, 'nf-l2')
add(f'<circle cx="{LX}" cy="{LY}" r="30" style="fill:var(--nf-h2o);fill-opacity:.4;stroke:var(--nf-h2o);stroke-width:3"/>'); text('central vein', LX, LY + 60, 'nf-l2', 'middle')
for a in (0, 120, 240):
    import math
    x, y = LX + 330 * math.cos(math.radians(a)), LY + 330 * math.sin(math.radians(a))
    add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="26" style="fill:var(--dk9);fill-opacity:.35;stroke:var(--dk9);stroke-width:3"/>')
text('portal triad', LX + 360, LY + 10, 'nf-l2')
ZH = dict(z1=(330, 220), z2=(220, 110), z3=(110, 30))
for d, zk in (('viral', 'z1'), ('yf', 'z2'), ('isch', 'z3'), ('apap', 'z3')):
    ro, ri = ZH[zk]
    add(f'<circle cx="{LX}" cy="{LY}" r="{(ro + ri) / 2:.0f}" style="fill:none;stroke:var(--bad);stroke-width:{ro - ri};stroke-opacity:.35"/>', when=D(d))
add(f'<circle cx="{LX}" cy="{LY}" r="70" style="fill:none;stroke:var(--nf-blood);stroke-width:80;stroke-opacity:.35"/>', when=D('bc'))
TAG = dict(cirr='cirrhosis — stellate-cell fibrosis around nodules; resistance inside the liver', pvt='portal vein thrombosis — block before the liver; liver not enlarged',
           bc='Budd-Chiari — hepatic veins blocked: congested zone 3 (nutmeg), big painful liver, ascites, no JVD',
           tips='TIPS — portal vein to hepatic vein, bypassing the liver: can precipitate encephalopathy',
           viral='zone 1 — viral hepatitis, ingested toxins (cocaine)', yf='zone 2 — yellow fever',
           isch='zone 3 — ischemia (congestive hepatopathy): least oxygen', apap='zone 3 — acetaminophen: CYP2E1 makes NAPQI; N-acetylcysteine')
for k, s in TAG.items(): text(s, 1150, 1480, 'nf-l1 dyn-tag', 'middle', when=D(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
SLOW = m(PORTAL_HTN, speed=0.25, set=dict(pv=5))
flows = [
  dict(d='M700 1200 V900 V640', len=560, speed=120, r=9, base=dict(pv=4), mods=[SLOW, m(D('tips'), set=dict(pv=1))]),
  dict(d='M420 1020 C520 1000 600 950 700 900', len=300, speed=120, r=9, base=dict(pv=2), mods=[SLOW]),
  dict(d=f'M{LV[0] + 150} {LV[1] - 100} C850 380 920 360 980 360 V240', len=420, speed=120, r=9, base=dict(hv=3), mods=[m(D('bc', 'cirr', 'pvt'), set=dict(hv=1))]),
  dict(d='M700 900 C760 900 900 820 980 700', len=330, speed=140, r=9, base=dict(pv=4), when=D('tips')),
] + [dict(d=f'M680 {y0} C620 {y0} 580 {y1} 540 {y1}', len=170, speed=90, r=8, base=dict(pv=3), when=PORTAL_HTN)
      for y0, y1 in ((640, 300), (880, 860), (1180, 1280))]
for a in (0, 120, 240):
    x, y = LX + 330 * math.cos(math.radians(a)), LY + 330 * math.sin(math.radians(a))
    flows.append(dict(d=f'M{x:.0f} {y:.0f} L{LX} {LY}', len=330, speed=80, r=8, base=dict(pv=2), mods=[m(D('bc'), speed=0.2)]))
    flows.append(dict(d=f'M{LX + 40 * math.cos(math.radians(a + 60)):.0f} {LY + 40 * math.sin(math.radians(a + 60)):.0f} L{x + 30 * math.cos(math.radians(a + 60)):.0f} {y + 30 * math.sin(math.radians(a + 60)):.0f}',
                      len=300, speed=60, r=6, base=dict(bile=2)))
sites = [dict(x=LV[0] - 300, y=LV[1] - 120, n=[-1, -1], w=10, t='rec', l='', aria='Liver zones', c='liverzones', ions=[]),
         dict(x=560, y=1060, n=[1, 1], w=10, t='rec', l='', aria='Portosystemic anastomoses', c='portosys', ions=[]),
         dict(x=900, y=300, n=[1, -1], w=10, t='rec', l='', aria='Budd-Chiari', c='buddchiari', ions=[]),
         dict(x=LV[0] + 300, y=LV[1] + 40, n=[1, 0], w=10, t='rec', l='', aria='Cirrhosis', c='cirrhosis', ions=[]),
         dict(x=760, y=1240, n=[1, 1], w=10, t='rec', l='', aria='Gut arteries', c='gutarteries', ions=[]),
         dict(x=LX - 360, y=LY, n=[-1, 0], w=10, t='rec', l='', aria='Acetaminophen', c='acetaminophen', ions=[])]

readouts = [
  dict(l='Portal pressure', mods=[dict(when=PORTAL_HTN, d=1), dict(when=D('tips'), d=-1)]),
  dict(l='Varices · caput medusae', mods=[dict(when=PORTAL_HTN, d=1)]),
  dict(l='Liver size', mods=[dict(when=D('bc'), d=1), dict(when=D('cirr'), d=-1)]),
  dict(l='Encephalopathy risk', mods=[dict(when=D('tips', 'cirr'), d=1)]),
  dict(l='Transaminases', mods=[dict(when=D('viral', 'yf', 'isch', 'apap', 'bc'), d=1)]),
]

notes = {
  '': 'About 80% of liver blood comes by the portal vein, 20% by the hepatic artery; it crosses each lobule from the portal triad '
      '(zone 1) to the central vein (zone 3), so oxygen falls along the way while bile runs the other direction.',
  'dx:cirr': 'Cirrhosis: stellate cells lay down bridging fibrosis around regenerative nodules — resistance inside the liver → '
             'portal hypertension: varices, caput medusae, anorectal varices, splenomegaly, ascites.',
  'dx:pvt': 'Portal vein thrombosis: the block is before the liver, so the liver is not enlarged; portal hypertension, pain, '
            'bowel ischemia if it reaches the SMV. Cirrhosis, malignancy, pancreatitis, sepsis.',
  'dx:bc': 'Budd-Chiari: hepatic vein thrombosis or compression backs blood into the liver — centrilobular congestion (nutmeg), '
           'painful hepatomegaly, ascites, varices; no JVD. Polycythemia vera, hypercoagulability, postpartum, HCC.',
  'dx:tips': 'TIPS joins the portal vein to a hepatic vein, bypassing the liver — lowers portal pressure, can precipitate hepatic '
             'encephalopathy.',
  'dx:viral': 'Zone 1 (periportal): first hit by viral hepatitis and ingested toxins such as cocaine; best oxygenated.',
  'dx:yf': 'Zone 2 (intermediate): yellow fever.',
  'dx:isch': 'Zone 3 (pericentral): least oxygen — first hit by ischemia (congestive hepatopathy); site of alcoholic hepatitis.',
  'dx:apap': 'Acetaminophen: zone 3 is richest in CYP450 (CYP2E1) — overdose saturates conjugation, NAPQI outruns glutathione. '
             'Alcohol lowers the threshold. N-acetylcysteine.',
}

dyn = dict(
  kinds=dict(pv=['mov', '--dk9'], hv=['mov', '--nf-h2o'], bile=['mov', '--dk5']), groups=[['mov', 'Portal blood · hepatic venous · bile']],
  switches=[dict(id='dx', label='Problem', type='one', options=[
              ['cirr', 'Cirrhosis', 'cirrhosis'], ['pvt', 'Portal vein thrombosis', 'buddchiari'], ['bc', 'Budd-Chiari', 'buddchiari'],
              ['tips', 'TIPS', 'portosys'], ['viral', 'Zone 1 — viral hepatitis', 'liverzones'], ['yf', 'Zone 2 — yellow fever', 'liverzones'],
              ['isch', 'Zone 3 — ischemia', 'liverzones'], ['apap', 'Zone 3 — acetaminophen', 'acetaminophen']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 18')

MAP = dict(
  id='portsim', title='Liver Blood Flow in Motion', topic='gi', after='liver',
  sub='Send gut blood up the portal vein, through the lobule from zone 1 to zone 3 and out the hepatic veins — then block it before, '
      'inside or after the liver, open the back roads, place a TIPS, and see which zone each injury hits',
  w=3600, h=1900,
  fa='73, 244, 370, 371, 372, 374, 396, 397, 495',
  src=['Robbins ch 18 — Liver and gallbladder', 'Moore ch 5 — Abdomen'],
  lanes=[('pvFlow', 'Flow', 'glycolysis'), ('pvDz', 'Block & injury', 'tca')],
  nodes=[
    ('pv1', 'Liver lobule zones', 330, 1720, 'pvFlow', 'zone 1 → 3', ['liverzones'], 'hub'),
    ('pv2', 'Gut arteries', 760, 1720, 'pvFlow', 'celiac · SMA · IMA', ['gutarteries']),
    ('pv3', 'Portosystemic anastomoses', 1200, 1720, 'pvFlow', 'gut, butt, caput', ['portosys']),
    ('pv4', 'Cirrhosis & portal HTN', 1640, 1720, 'pvDz', 'intrahepatic', ['cirrhosis']),
    ('pv5', 'Budd-Chiari & PVT', 2080, 1720, 'pvDz', 'post- vs prehepatic', ['buddchiari']),
    ('pv6', 'Acetaminophen toxicity', 2520, 1720, 'pvDz', 'zone 3 · NAC', ['acetaminophen'])],
  panels=[
    (2500, PANY, 1000, 'Zone → injury (Robbins ch 18)', [
      ('Zone 1', 'viral hepatitis, ingested toxins'), ('Zone 2', 'yellow fever'), ('Zone 3', 'ischemia, acetaminophen, alcohol')])],
  dyn=dyn)
