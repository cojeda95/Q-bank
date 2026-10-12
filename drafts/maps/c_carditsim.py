# Heart Infection & Inflammation in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A four-chamber heart with its four valves, the lungs above, the throat and joints to the left and the embolic targets to
# the right (brain, retina, kidney, fingers). A `one` switch grows a lesion: acute endocarditis (S aureus, big vegetation),
# subacute (viridans, small, abnormal valve), tricuspid endocarditis in injection drug use (emboli to the lungs), acute
# rheumatic fever (anti-M-protein antibodies from the throat to the heart, joints, skin, brain) and chronic rheumatic
# stenosis, NBTE / Libman-Sacks, myocarditis, and an atrial myxoma ball-valving the mitral valve. 5 readouts. Facts from
# the pinned cards; FA pages in `fa`. No new cards.
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
TG = dict(brain=(1900, 300), retina=(1900, 500), kidney=(1900, 760), fingers=(1900, 1020))
V = dict(tri=(960, 860), mit=(1240, 860), aor=(1240, 700), pul=(960, 700))

text('Heart infection & inflammation — vegetations, antibodies and emboli', 180, 150, 'dyn-big')
text('front view · right heart on your left · embolic targets on the right', 180, 176, 'dyn-cap')

# ════════ heart ════════
add('<rect x="800" y="240" width="600" height="120" rx="50" style="fill:var(--nf-h2o);fill-opacity:.08;stroke:var(--dk1);stroke-width:4"/>'); text('lungs', 1100, 310, 'nf-l1', 'middle')
CH = dict(RA=(820, 720), LA=(1120, 720), RV=(820, 880), LV=(1120, 880))
for k, (x, y) in CH.items():
    sty = 'fill:var(--surface);stroke:var(--dk3);stroke-width:4'
    add(f'<rect x="{x}" y="{y}" width="260" height="150" rx="30" style="{sty}"/>', unless=D('myo') if k[1] == 'V' else None)
    if k[1] == 'V':
        add(f'<rect x="{x}" y="{y}" width="260" height="150" rx="30" style="fill:var(--bad);fill-opacity:.2;stroke:var(--bad);stroke-width:5"/>', when=D('myo'))
    text(k, x + 130 + (-70 if k[0] == 'R' else 70), y + 90, 'nf-l1', 'middle')
for k, (x, y) in V.items():
    if k in ('tri', 'mit'):
        add(f'<path d="M{x - 60} {y} H{x + 60}" style="stroke:var(--dk4);stroke-width:8"/>')
    text(dict(tri='tricuspid', mit='mitral', aor='aortic', pul='pulmonic')[k], x, y + (30 if k in ('tri', 'mit') else -24), 'nf-l2', 'middle')
add('<path d="M1240 720 V560 C1240 460 1500 460 1560 520 V1200" style="fill:none;stroke:var(--nf-blood);stroke-width:26;opacity:.2"/>'); text('aorta', 1580, 560, 'nf-l2')
add('<path d="M960 720 C960 560 1000 440 1000 360" style="fill:none;stroke:var(--nf-h2o);stroke-width:22;opacity:.25"/>')
add('<path d="M1150 360 C1150 500 1150 620 1160 720" style="fill:none;stroke:var(--nf-blood);stroke-width:18;opacity:.2"/>')   # pulmonary veins → LA
text('pulm. artery', 950, 600, 'nf-l2', 'end'); text('pulm. veins', 1140, 600, 'nf-l2', 'end')
# arteries from the aorta to each embolic target — the emboli ride these
ARCH = 'M1240 860 V560 C1240 460 1500 460 1560 520'
BR = dict(brain=' C1600 400 1700 300 1856 300', retina=' V560 C1650 540 1750 500 1856 500', kidney=' V760 H1856', fingers=' V1020 H1856')
for k, b in BR.items():
    st = b.replace(' V560', 'M1560 560').replace(' V760', 'M1560 760').replace(' V1020', 'M1560 1020')
    if k == 'brain': st = 'M1560 520' + b
    add(f'<path d="{st}" style="fill:none;stroke:var(--nf-blood);stroke-width:14;opacity:.2;stroke-linecap:round"/>')
text('carotid', 1690, 330, 'nf-l2', 'end'); text('ophthalmic', 1740, 490, 'nf-l2', 'middle'); text('renal', 1700, 745, 'nf-l2', 'middle')
text('to the hands', 1700, 1005, 'nf-l2', 'middle')
text('anti-M-protein antibodies in the blood', 640, 560, 'nf-l2', 'middle', when=D('rf'))
for k, (x, y) in TG.items():
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>'); text(k, x + 60, y + 6, 'nf-l1')
add('<circle cx="500" cy="340" r="54" style="fill:var(--dk9);fill-opacity:.15;stroke:var(--dk9);stroke-width:3"/>'); text('throat (GAS)', 500, 270, 'nf-l1', 'middle')
add('<circle cx="500" cy="1180" r="54" style="fill:var(--dk6);fill-opacity:.15;stroke:var(--dk6);stroke-width:3"/>'); text('joints · skin · brain', 500, 1270, 'nf-l1', 'middle')

# ════════ lesions ════════
def veg(x, y, r, col, when):
    add(f'<path d="M{x - r} {y} c{r * .3} -{r * 1.4} {r * 1.4} -{r * 1.4} {r * 2} 0 c-{r * .4} {r * .8} -{r * 1.6} {r * .8} -{r * 2} 0 Z" '
        f'style="fill:var({col});fill-opacity:.8;stroke:var(--ink-2);stroke-width:2"/>', when=when)
veg(1240, 860, 46, '--bad', D('acute')); veg(1240, 860, 20, '--bad', D('subacute')); veg(960, 860, 34, '--bad', D('ivdu'))
veg(1240, 860, 22, '--ink-3', D('nbte'))
add('<path d="M1180 860 H1300" style="stroke:var(--dk4);stroke-width:22"/>', when=D('rhd'))
add('<rect x="1104" y="702" width="292" height="170" rx="36" class="dyn-dash" style="fill:none"/>', when=D('rhd'))   # dilated LA
add('<circle cx="1350" cy="752" r="14" style="fill:var(--ink-2);opacity:.8"/>', when=D('rhd'))   # mural thrombus
add('<circle cx="1220" cy="770" r="40" style="fill:var(--dk5);fill-opacity:.7;stroke:var(--ink-2);stroke-width:3"/>', when=D('myxoma'))
add('<circle cx="1240" cy="845" r="22" style="fill:var(--dk5);fill-opacity:.4"/>', when=D('myxoma'))
for x, y in ((1150, 950), (1300, 980), (900, 960)):
    add(f'<circle cx="{x}" cy="{y}" r="8" style="fill:var(--dk4)"/>', when=D('myo'))
TAG = dict(acute='S aureus — large destructive vegetation on a normal valve, rapid',
           subacute='viridans strep — small vegetation on an abnormal valve, after dental work',
           ivdu='injection drug use — tricuspid vegetation, septic emboli to the lungs',
           rf='anti-M-protein antibodies cross-react: J♥NES — mitral > aortic, regurgitant early',
           rhd='years later — fish-mouth mitral stenosis · the left atrium dilates, mural thrombus', nbte='sterile platelet thrombi — cancer (pancreas) or SLE (Libman-Sacks) · cultures negative',
           myo='lymphocytes and necrosis in the muscle — arrhythmia, heart block, dilated cardiomyopathy',
           myxoma='left atrial myxoma — ball-valves the mitral valve: syncope, tumor plop, emboli, IL-6 fever')
for k, s in TAG.items(): text(s, 1100, 1300, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('Janeway (painless) · Osler (painful) · Roth spots · glomerulonephritis', 1100, 1340, 'nf-l2', 'middle', when=D('acute', 'subacute'))

# ════════ motion ════════
def to(src, tgt, k, when, n=3):
    return dict(d=ARCH + BR[tgt], len=dict(brain=1000, retina=900, kidney=1000, fingers=1250)[tgt], speed=150, r=10, base={k: n}, when=when)
EMB = D('acute', 'subacute', 'nbte', 'myxoma')
flows = [
  dict(d='M960 860 V720 C960 560 1000 440 1000 360', len=520, speed=110, r=8, base=dict(blood=3)),
  dict(d='M1150 360 C1150 500 1150 620 1160 720 C1170 780 1240 800 1240 860', len=520, speed=110, r=8, base=dict(blood=3), mods=[dict(when=D('rhd', 'myxoma'), speed=0.3)]),
  dict(d='M1300 880 V780', len=100, speed=60, r=8, base=dict(blood=2), when=D('acute', 'subacute', 'rf')),
  dict(d='M1020 880 V780', len=100, speed=60, r=8, base=dict(blood=2), when=D('ivdu')),
  dict(d='M960 860 V720 C960 560 1000 440 1000 360', len=520, speed=140, r=11, base=dict(emb=2), when=D('ivdu')),
  to((1240, 860), 'brain', 'emb', EMB), to((1240, 860), 'kidney', 'emb', D('acute', 'subacute', 'myxoma')),
  to((1240, 860), 'fingers', 'emb', D('acute', 'subacute'), 2), to((1240, 860), 'retina', 'emb', D('acute', 'subacute'), 1),
  dict(d='M500 400 C640 600 900 700 1180 860', len=820, speed=110, r=9, base=dict(ab=3), when=D('rf')),
  dict(d='M500 400 C460 700 460 900 500 1120', len=720, speed=110, r=9, base=dict(ab=3), when=D('rf')),
]
sites = [dict(x=1320, y=840, n=[1, 0], w=10, t='rec', l='', aria='Infective endocarditis', c='endocarditis', ions=[]),
         dict(x=560, y=340, n=[1, 0], w=10, t='rec', l='', aria='Rheumatic fever', c='rheumfever', ions=[]),
         dict(x=1180, y=900, n=[0, 1], w=10, t='rec', l='', aria='NBTE', c='nbte', ions=[]),
         dict(x=820, y=1000, n=[-1, 0], w=10, t='rec', l='', aria='Myocarditis', c='myocarditis', ions=[]),
         dict(x=1150, y=740, n=[-1, -1], w=10, t='rec', l='', aria='Cardiac tumors', c='myxoma', ions=[])]

readouts = [
  dict(l='Valve regurgitation', mods=[dict(when=D('acute', 'subacute', 'ivdu', 'rf'), d=1)]),
  dict(l='Valve obstruction', mods=[dict(when=D('rhd', 'myxoma'), d=1)]),
  dict(l='Systemic emboli', mods=[dict(when=EMB, d=1)]),
  dict(l='Blood cultures positive', mods=[dict(when=D('acute', 'subacute', 'ivdu'), d=1), dict(when=D('nbte'), d=-1)]),
  dict(l='Arrhythmia risk', mods=[dict(when=D('myo'), d=1)]),
]

notes = {
  '': 'Endothelial injury lets platelets and fibrin gather on a valve; microbes can seed it. Vegetations wreck valves and throw '
      'emboli — to the body from the left heart, to the lungs from the right. Pick a lesion.',
  'dx:acute': 'Acute endocarditis: S aureus — large destructive vegetations on previously normal valves, rapid onset; mitral > '
              'aortic. Septic emboli, petechiae, splinter hemorrhages, Janeway lesions; immune: Osler nodes, Roth spots, GN. '
              'Several blood cultures + echo; long (≥ 6 wk) antibiotics and/or valve replacement.',
  'dx:subacute': 'Subacute endocarditis: viridans streptococci — smaller vegetations on abnormal valves, after dental procedures. '
                 'Prosthetic valve → S epidermidis; GI/GU → Enterococcus; colon cancer → S gallolyticus.',
  'dx:ivdu': 'Injection drug use: tricuspid endocarditis (S aureus, Pseudomonas, Candida) — right-sided, so the septic emboli go '
            'to the lungs, not the body.',
  'dx:rf': 'Acute rheumatic fever: after group A strep pharyngitis, antibodies to M protein cross-react (type II) — J♥NES: '
           'migratory polyarthritis, pancarditis, nodules, erythema marginatum, Sydenham chorea. Mitral > aortic >> tricuspid; '
           'regurgitant early. Aschoff bodies, Anitschkow cells; ↑ ASO, anti-DNase B. Penicillin.',
  'dx:rhd': 'Chronic rheumatic heart disease: years later the mitral leaflets thicken and the commissures fuse — "fish-mouth" '
           'mitral stenosis. The left atrium dilates and may hold mural thrombi that embolize.',
  'dx:nbte': 'NBTE: a hypercoagulable state lays sterile platelet thrombi on the mitral or aortic valve; loosely attached, they '
             'embolize (infarcts in the brain, heart). Advanced cancer (pancreatic) or SLE (Libman-Sacks). Cultures negative.',
  'dx:myo': 'Myocarditis: lymphocytic infiltrate with focal necrosis (viral — coxsackie B, adenovirus, parvovirus B19…; also '
            'T cruzi, Borrelia, diphtheria, doxorubicin, cocaine, Kawasaki, SLE). Under-40 sudden death, tachycardia out of '
            'proportion to fever; ↑ troponin.',
  'dx:myxoma': 'Myxoma: commonest primary adult cardiac tumor, 90% atrial, mostly left — ball-valve obstruction of the mitral '
               'valve, syncope, early diastolic tumor plop (mimics mitral stenosis), emboli, IL-6 fever. Children: '
               'rhabdomyoma (tuberous sclerosis). Commonest cardiac tumor overall is a metastasis.',
}

dyn = dict(
  kinds=dict(blood=['mov', '--nf-blood'], emb=['mov', '--bad'], ab=['mov', '--dk9']),
  groups=[['mov', 'Blood · emboli · antibodies']],
  switches=[dict(id='dx', label='Lesion', type='one', options=[
              ['acute', 'Acute endocarditis', 'endocarditis'], ['subacute', 'Subacute endocarditis', 'endocarditis'],
              ['ivdu', 'Tricuspid (IV drug use)', 'endocarditis'], ['rf', 'Acute rheumatic fever', 'rheumfever'],
              ['rhd', 'Chronic rheumatic stenosis', 'rheumfever'], ['nbte', 'NBTE / Libman-Sacks', 'nbte'],
              ['myo', 'Myocarditis', 'myocarditis'], ['myxoma', 'Atrial myxoma', 'myxoma']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 318–320 · Robbins ch 12')

MAP = dict(
  id='carditsim', title='Heart Infection & Inflammation in Motion', topic='cardio', after='valves',
  sub='Grow vegetations on the valves and follow their emboli, send strep antibodies to the heart and joints, inflame the muscle '
      'and drop a myxoma into the mitral valve',
  w=3600, h=1900,
  fa='318, 319, 320',
  src=['Robbins ch 12 — The heart', 'Robbins ch 8 — Infectious diseases'],
  lanes=[('cdEndo', 'Endocardium & valves', 'tca'), ('cdMyo', 'Muscle & tumor', 'glycolysis')],
  nodes=[
    ('cd1', 'Infective endocarditis', 330, 1700, 'cdEndo', 'S aureus · viridans', ['endocarditis'], 'hub'),
    ('cd2', 'Rheumatic fever', 760, 1700, 'cdEndo', 'J♥NES · mitral', ['rheumfever']),
    ('cd3', 'Nonbacterial endocarditis', 1200, 1700, 'cdEndo', 'sterile · cancer · SLE', ['nbte']),
    ('cd4', 'Myocarditis', 1640, 1700, 'cdMyo', 'lymphocytes · arrhythmia', ['myocarditis']),
    ('cd5', 'Cardiac tumors', 2080, 1700, 'cdMyo', 'myxoma · rhabdomyoma', ['myxoma'])],
  panels=[
    (2500, PANY, 1000, 'Vegetation by cause (Robbins ch 12)', [
      ('S aureus', 'large, normal valve, acute'), ('Viridans strep', 'small, abnormal valve'), ('IV drug use', 'tricuspid'),
      ('NBTE', 'small, sterile, loosely attached'), ('Libman-Sacks (SLE)', 'small, either side of the leaflet'),
      ('Rheumatic fever', 'small, warty, along the line of closure')])],
  dyn=dyn)
