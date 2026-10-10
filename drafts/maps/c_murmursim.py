# Murmurs & Maneuvers in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A chest with the auscultation areas (APT M and Erb point), a schematic heart with the abnormal jet moving, and a
# phonocardiogram (S1 — systole — S2 — diastole) with a cursor sweeping through the cycle. One `one` switch picks the lesion
# (AS, MR, TR, MVP, HCM, AR, MS, VSD, ASD); a second picks a bedside maneuver (standing/Valsalva, squatting, passive leg
# raise, handgrip, inspiration, expiration) and the murmur grows or shrinks, or the MVP click moves, as the cards say.
# 4 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

MM = lambda *k: [f'mm:{x}' for x in k]
MV = lambda *k: [f'mv:{x}' for x in k]
PANY = 1160
BY = 960                       # phonocardiogram baseline
S1, S2, S1B = 400, 1000, 1700
ACC = 'fill:var(--accent);fill-opacity:.32;stroke:var(--accent);stroke-width:3'

text('Murmurs — where, when, and what the maneuvers do', 180, 150, 'dyn-big')
text('pick a lesion, then a maneuver', 180, 176, 'dyn-cap')

# ════════ the chest: where to listen ════════
add('<rect x="300" y="230" width="620" height="500" rx="60" class="dyn-soft"/>')
add('<rect x="580" y="250" width="50" height="420" rx="18" class="dyn-cell"/>')
text('sternum', 605, 700, 'nf-l2', 'middle')
AREA = dict(aortic=(530, 330, 'Aortic', 'end'), pulm=(680, 330, 'Pulmonic', 'start'), erb=(680, 420, 'Erb point', 'start'),
            tric=(660, 540, 'Tricuspid', 'start'), mitral=(800, 630, 'Mitral (apex)', 'start'))
for k, (x, y, lab, an) in AREA.items():
    add(f'<circle cx="{x}" cy="{y}" r="14" style="fill:var(--ink-3);opacity:.5"/>')
    text(lab, x + (-50 if an == 'end' else 50), y + 5, 'nf-l2', an)
WHERE = dict(as_='aortic', hcm='erb', mr='mitral', mvp='mitral', ms='mitral', ar='erb', tr='tric', vsd='tric', asd='pulm')
for k, a in WHERE.items():
    x, y = AREA[a][:2]
    add(f'<circle cx="{x}" cy="{y}" r="40" style="fill:none;stroke:var(--accent);stroke-width:6"/>', when=MM(k.rstrip('_')))
text('radiates to the carotids', 400, 270, 'nf-l1 dyn-tag', 'middle', when=MM('as'))
text('radiates to the axilla', 820, 700, 'nf-l1 dyn-tag', 'middle', when=MM('mr'))

# ════════ the heart: which way the jet goes ════════
def room(x0, y0, x1, y1, lab):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="dyn-cell"/>')
    text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')
room(1100, 300, 1290, 440, 'RA'); room(1460, 300, 1650, 440, 'LA')
room(1100, 480, 1290, 660, 'RV'); room(1460, 480, 1650, 660, 'LV')
add('<path d="M1650 520 H1720 V220" style="fill:none;stroke:var(--dk1);stroke-width:26;stroke-linejoin:round;opacity:.45"/>')
add('<path d="M1100 520 H1040 V220" style="fill:none;stroke:var(--dk11);stroke-width:26;stroke-linejoin:round;opacity:.45"/>')
text('aorta', 1750, 250, 'nf-l2'); text('pulmonary artery', 1010, 250, 'nf-l2', 'end')
for (x, y, w, h) in ((1525, 452, 60, 8), (1165, 452, 60, 8), (1686, 490, 8, 60), (1056, 490, 8, 60)):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" style="fill:var(--ink-2)"/>')
text('valves', 1375, 470, 'nf-l2', 'middle')
add('<rect x="1440" y="480" width="40" height="180" rx="10" style="fill:var(--dk4);fill-opacity:.5"/>', when=MM('hcm'))
text('thick septum', 1375, 700, 'nf-l1 dyn-tag', 'middle', when=MM('hcm'))
add('<path d="M1290 560 H1460" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:6 6"/>', when=MM('vsd'))
add('<path d="M1290 370 H1460" style="stroke:var(--bad);stroke-width:5;stroke-dasharray:6 6"/>', when=MM('asd'))

# ════════ the phonocardiogram ════════
add(f'<path d="M300 {BY} H1900" class="dyn-line"/>')
for x, lab in ((S1, 'S1'), (S2, 'S2'), (S1B, 'S1')):
    add(f'<rect x="{x - 5}" y="{BY - 70}" width="10" height="140" rx="3" style="fill:var(--ink-2)"/>', unless=MM('asd') if x == S2 else None)
    text(lab, x, BY - 90, 'nf-l1', 'middle')
add(f'<rect x="{S2 - 30}" y="{BY - 70}" width="10" height="140" rx="3" style="fill:var(--ink-2)"/><rect x="{S2 + 20}" y="{BY - 70}" width="10" height="140" rx="3" style="fill:var(--ink-2)"/>', when=MM('asd'))
text('systole', 700, BY + 120, 'nf-l2', 'middle'); text('diastole', 1350, BY + 120, 'nf-l2', 'middle')

LEVEL = {'up': 100, 'normal': 60, 'down': 28}
def murmur(k, A, cx=700):
    if k in ('as', 'hcm'): return f'M440 {BY} L700 {BY - A} L960 {BY} L700 {BY + A} Z'
    if k == 'asd': return f'M460 {BY} L700 {BY - A * 0.6} L940 {BY} L700 {BY + A * 0.6} Z'
    if k in ('mr', 'tr', 'vsd'): return f'M420 {BY - A} H980 V{BY + A} H420 Z'
    if k == 'mvp': return f'M{cx + 20} {BY} L980 {BY - A} V{BY + A} Z'
    if k == 'ar': return f'M1020 {BY - A} L1400 {BY} L1020 {BY + A} Z'
    if k == 'ms': return f'M1180 {BY} L1300 {BY - A * 0.6} L1650 {BY - A} V{BY + A} L1300 {BY + A * 0.6} Z'
# what each maneuver does to each murmur — from the maneuvers card and the lesion cards; blank = no source says
# UNVERIFIED: the card's general rules ("most murmurs" softer/louder; expiration: left-sided louder) are applied to each lesion
# that has no lesion-specific line (TR, MS, VSD for standing/squatting; MS, MVP for expiration)
RULE = {
  'stand': dict(hcm='up', as_='down', mr='down', ar='down', vsd='down', tr='down', ms='down'),
  'squat': dict(hcm='down', as_='up', mr='up', ar='up', vsd='up', tr='up', ms='up'),
  'leg':   dict(hcm='down', as_='up', mr='up', ar='up', vsd='up', tr='up', ms='up'),
  'grip':  dict(mr='up', ar='up', vsd='up', as_='down', hcm='down'),
  'insp':  dict(tr='up'),
  'exp':   dict(as_='up', mr='up', mvp='up', ar='up', hcm='up', ms='up'),
}
KS = ['as', 'hcm', 'mr', 'tr', 'vsd', 'asd', 'mvp', 'ar', 'ms']
def lvl(k, v): return RULE[v].get(k + '_' if k == 'as' else k, 'normal')
for k in KS:
    changed = {L: [f'mm:{k}&mv:{v}' for v in RULE if lvl(k, v) == L] for L in ('up', 'down')}
    clicks = {'stand': 580, 'squat': 820, 'leg': 820} if k == 'mvp' else {}
    for L in ('up', 'down'):
        if changed[L]: add(f'<path d="{murmur(k, LEVEL[L])}" style="{ACC}"/>', when=changed[L])
    plain = [f'mm:{k}'] ; moved = [f'mm:{k}&mv:{v}' for v in clicks]
    add(f'<path d="{murmur(k, LEVEL["normal"])}" style="{ACC}"/>', when=plain, unless=changed['up'] + changed['down'] + moved)
    for v, cx in clicks.items():
        add(f'<path d="{murmur(k, LEVEL["normal"], cx)}" style="{ACC}"/>', when=[f'mm:{k}&mv:{v}'])
if True:
    for v, cx in (('', 700), ('stand', 580), ('squat', 820), ('leg', 820)):
        w = [f'mm:mvp&mv:{v}'] if v else ['mm:mvp']
        u = None if v else [f'mm:mvp&mv:{q}' for q in ('stand', 'squat', 'leg')]
        add(f'<rect x="{cx - 4}" y="{BY - 50}" width="8" height="100" rx="3" style="fill:var(--bad)"/>', when=w, unless=u)
    text('click earlier', 580, BY - 110, 'nf-l1 dyn-tag', 'middle', when=['mm:mvp&mv:stand'])
    text('click later', 820, BY - 110, 'nf-l1 dyn-tag', 'middle', when=['mm:mvp&mv:squat', 'mm:mvp&mv:leg'])
add(f'<rect x="1095" y="{BY - 50}" width="8" height="100" rx="3" style="fill:var(--bad)"/>', when=MM('ms'))
text('opening snap', 1100, BY - 110, 'nf-l1 dyn-tag', 'middle', when=MM('ms'))
text('wide, fixed split S2', S2, BY - 110, 'nf-l1 dyn-tag', 'middle', when=MM('asd'))
TAG = dict(stand='↓ preload: most murmurs softer — HCM louder, MVP click earlier',
           squat='↑ preload and ↑ afterload: most murmurs louder — HCM softer, MVP click later',
           leg='↑ preload: most murmurs louder — HCM softer, MVP click later',
           grip='↑ afterload: MR, AR and VSD louder — AS and HCM softer',
           insp='inspiration: right-sided murmurs louder', exp='expiration: left-sided murmurs louder')
for v, t in TAG.items(): text(t, 1100, BY + 180, 'nf-l1', 'middle', when=MV(v))
text('dashed outline = where the murmur would be at rest', 1100, BY + 210, 'dyn-cap', 'middle', when=['mv:*'])
for k in KS:
    if any(lvl(k, v) != 'normal' for v in RULE):
        add(f'<path d="{murmur(k, LEVEL["normal"])}" style="fill:none;stroke:var(--ink-3);stroke-width:2;stroke-dasharray:6 6"/>', when=[f'mm:{k}&mv:*'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
JET = dict(as_='M1600 600 H1690 V240', hcm='M1600 600 H1690 V240', mr='M1555 600 V340', mvp='M1555 600 V340',
           tr='M1195 600 V340', ar='M1720 240 V520 H1600', ms='M1555 340 V600', vsd='M1500 570 H1250', asd='M1500 370 H1250')
flows = [dict(d=f'M300 {BY} H1900', len=1600, speed=420, r=10, base=dict(t=1))]
for k, d in JET.items():
    k = k.rstrip('_')
    flows.append(dict(d=d, len=360, speed=150 if k != 'ms' else 70, r=8, base=dict(jet=4), when=MM(k),
                      mods=[m([f'mm:{k}&mv:{v}' for v in RULE if lvl(k, v) == 'up'], set=dict(jet=7)),
                            m([f'mm:{k}&mv:{v}' for v in RULE if lvl(k, v) == 'down'], set=dict(jet=2))]))
sites = [dict(x=605, y=460, n=[0, 1], w=10, t='rec', l='', aria='Auscultation areas', c='auscareas', ions=[]),
         dict(x=S1, y=BY + 60, n=[0, 1], w=10, t='rec', l='', aria='Heart sounds', c='heartsounds', ions=[]),
         dict(x=1375, y=420, n=[0, 1], w=10, t='rec', l='', aria='Bedside maneuvers', c='maneuvers', ions=[])]

def rd(k_up, k_dn): return [dict(when=k_up, d=1), dict(when=k_dn, d=-1)]
readouts = [
  dict(l='Preload (venous return)', mods=rd(MV('squat', 'leg'), MV('stand'))),
  dict(l='Afterload', mods=[dict(when=MV('squat', 'grip'), d=1)]),
  dict(l='This murmur', mods=rd([f'mm:{k}&mv:{v}' for k in KS for v in RULE if lvl(k, v) == 'up'],
                                 [f'mm:{k}&mv:{v}' for k in KS for v in RULE if lvl(k, v) == 'down'])),
]

notes = {
  '': 'S1 is the mitral and tricuspid valves closing, S2 the aortic and pulmonic. Systolic murmurs sit between S1 and S2, diastolic '
      'murmurs after S2. Each valve is heard best downstream: aortic and pulmonic at the 2nd spaces, tricuspid at the lower left '
      'sternal border, mitral at the apex, and aortic regurgitation at Erb point.',
  'mm:as': 'Aortic stenosis: a crescendo-decrescendo ejection murmur at the right upper sternal border, radiating to the carotids; '
           'pulsus parvus et tardus; syncope, angina, dyspnea. Louder with squatting and leg raise, softer with handgrip and Valsalva.',
  'mm:hcm': 'Hypertrophic cardiomyopathy: a thick septum obstructs outflow, worse whenever the LV gets smaller — so the systolic murmur '
            'at the left sternal border gets louder with Valsalva and standing and softer with squatting and handgrip.',
  'mm:mr': 'Mitral regurgitation: the leaky valve regurgitates through all of systole — a holosystolic blowing murmur at the apex, '
           'radiating to the axilla. Louder with handgrip and squatting. New after an MI → papillary muscle rupture.',
  'mm:tr': 'Tricuspid regurgitation: holosystolic at the tricuspid area, louder with inspiration — RV dilation, pacemaker leads, '
           'endocarditis in injection drug users.',
  'mm:vsd': 'VSD: blood shunts from the high-pressure LV to the RV — a harsh holosystolic murmur at the left lower sternal border. '
            'Louder with handgrip.',
  'mm:asd': 'ASD: a systolic ejection murmur (extra flow across the pulmonic valve) with a wide, fixed split S2.',
  'mm:mvp': 'Mitral valve prolapse: the chordae snap tight as the floppy leaflets billow back — a midsystolic click, then a late '
            'systolic murmur. A smaller LV (standing, Valsalva) lets them prolapse sooner, so the click comes earlier.',
  'mm:ar': 'Aortic regurgitation: an early diastolic decrescendo blowing murmur at Erb point, with a wide pulse pressure and bounding '
           'pulses. Louder with handgrip.',
  'mm:ms': 'Mitral stenosis: an opening snap, then a delayed low-pitched mid-to-late diastolic rumble at the apex — the shorter the '
           'S2-to-snap interval, the worse the stenosis. Almost always rheumatic.',
  'mv:stand': 'Standing or Valsalva lowers preload: most murmurs get softer. The exceptions depend on a small LV: HCM gets louder and '
              'the MVP click comes earlier.',
  'mv:squat': 'Squatting raises preload and afterload: most murmurs get louder; HCM softer, the MVP click later.',
  'mv:leg': 'Passive leg raise raises preload: most murmurs get louder; HCM softer, the MVP click later.',
  'mv:grip': 'Handgrip raises afterload: MR, AR and VSD get louder; AS and HCM softer.',
  'mv:insp': 'Inspiration: right-sided murmurs (tricuspid regurgitation) get louder.',
  'mv:exp': 'Expiration: left-sided murmurs get louder.',
}

dyn = dict(
  kinds=dict(t=['time', '--accent'], jet=['jet', '--bad']),
  groups=[['time', 'Cursor through the cycle'], ['jet', 'Abnormal flow']],
  switches=[dict(id='mm', label='Lesion', type='one', options=[
              ['as', 'Aortic stenosis', 'aortstenosis'], ['hcm', 'Hypertrophic cardiomyopathy', 'hcm'],
              ['mr', 'Mitral regurgitation', 'mitralregurg'], ['tr', 'Tricuspid regurgitation', 'mitralregurg'],
              ['vsd', 'VSD', 'vsd'], ['asd', 'ASD', 'asd'], ['mvp', 'Mitral valve prolapse', 'mvp'],
              ['ar', 'Aortic regurgitation', 'aortregurg'], ['ms', 'Mitral stenosis', 'mitralsten']]),
            dict(id='mv', label='Maneuver', type='one', options=[
              ['stand', 'Standing · Valsalva', 'maneuvers'], ['squat', 'Squatting', 'maneuvers'],
              ['leg', 'Passive leg raise', 'maneuvers'], ['grip', 'Handgrip', 'maneuvers'],
              ['insp', 'Inspiration', 'maneuvers'], ['exp', 'Expiration', 'maneuvers']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 292, 295–296 · Robbins ch 12 · Guyton ch 23')

MAP = dict(
  id='murmursim', title='Murmurs & Maneuvers in Motion', topic='cardio', after='valves',
  sub='Pick a murmur and see where it is heard, when in the cycle it falls and which way the blood leaks — then stand, squat, '
      'raise the legs, squeeze or breathe and watch it get louder or softer',
  w=3600, h=1900,
  fa='292, 294, 295, 296, 298, 303, 315, 525',
  src=['Robbins ch 12 — The heart', 'Guyton ch 23 — Heart Valves and Heart Sounds; Valvular and Congenital Heart Defects',
       'Costanzo ch 4 — Cardiovascular physiology', 'Moore ch 4 — Thorax', 'Bootcamp.com Cardiology — Cardiac Cycle',
       'Bootcamp.com Cardiology — Valvular Disease', 'Robbins ch 5 — Genetic disorders', 'Langman ch 13 — Cardiovascular System'],
  lanes=[('muNorm', 'Sounds & maneuvers', 'glycolysis'), ('muSys', 'Systolic murmurs', 'tca'), ('muDia', 'Diastolic murmurs & shunts', 'gluconeo')],
  nodes=[
    ('mu1', 'Heart sounds · where to listen', 330, 1620, 'muNorm', 'S1–S4 · APT M', ['heartsounds', 'auscareas'], 'hub'),
    ('mu2', 'Bedside maneuvers', 760, 1620, 'muNorm', 'preload · afterload', ['maneuvers']),
    ('mu3', 'Aortic stenosis', 1200, 1620, 'muSys', 'to the carotids', ['aortstenosis']),
    ('mu4', 'MR · TR', 1640, 1620, 'muSys', 'holosystolic', ['mitralregurg']),
    ('mu5', 'Mitral valve prolapse', 2080, 1620, 'muSys', 'midsystolic click', ['mvp']),
    ('mu6', 'Hypertrophic cardiomyopathy', 330, 1760, 'muSys', 'louder with Valsalva', ['hcm']),
    ('mu7', 'Aortic regurgitation', 760, 1760, 'muDia', 'wide pulse pressure', ['aortregurg']),
    ('mu8', 'Mitral stenosis', 1200, 1760, 'muDia', 'opening snap', ['mitralsten']),
    ('mu9', 'VSD · ASD', 1640, 1760, 'muDia', 'fixed split S2', ['vsd', 'asd'])],
  panels=[
    (2500, PANY, 1000, 'Where to listen (First Aid p. 295)', [
      ('Aortic — right 2nd space', 'aortic stenosis'),
      ('Pulmonic — left 2nd space', 'pulmonic stenosis, ASD flow'),
      ('Erb point — left 3rd space', 'aortic regurgitation'),
      ('Tricuspid — lower left sternal border', 'TR, VSD'),
      ('Mitral — apex', 'MR, MVP, MS')])],
  dyn=dyn)
