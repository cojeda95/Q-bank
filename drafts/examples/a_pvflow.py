# m41 — Pressure–Volume Loop in Motion (dynamic map, kit data)
# A drawn left heart (pulmonary veins, LA, mitral valve, LV, aortic valve, aorta) with blood moving through the cycle,
# beside a large LV pressure–volume loop and a time strip (systole / diastole, S1–S4, where each murmur falls).
# A `steps` switch walks isovolumetric contraction → ejection → isovolumetric relaxation → filling: the loop segment
# lights up, the valves open and shut, the LV fills and empties. A `one` switch redraws the loop (red over the dashed
# normal) for a valve lesion, a load change or heart failure, adds the regurgitant jet and the murmur, and reads out
# EDV, ESV, SV, EF, peak LV pressure and LA pressure.
# Sources: First Aid 2025 pp. 289–290, 292–293, 295–296, 316 · Costanzo ch 4 · Guyton ch 9, 23 ·
# Bootcamp Cardiology (Pressure Volume Loops).
import sys, math
sys.path.insert(0, '/Users/Alonso/Developer/atlas-review/batches/m18')
from common import full

CO4, GY9, GY23 = full('Costanzo', 4), full('Guyton', 9), full('Guyton', 23)
BC_PV = 'Bootcamp.com Cardiology — Pressure Volume Loops'

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

PH = ['ivc', 'ej', 'ivr', 'fill']
P_ = lambda *k: ['ph:' + x for x in k]
Z = lambda *k: ['dz:' + x for x in k]
DZ = ['as', 'mr', 'ar', 'ms', 'pre', 'aft', 'ino', 'hfr', 'hfp']
BAD = 'stroke:var(--bad)'
f0 = lambda v: f'{v:.0f}'

# ════════ 1. the PV loop: geometry ════════
LX0, LY0 = 1300, 1150                          # origin (0 mL, 0 mm Hg)
X = lambda v: round(LX0 + 3.8 * v)             # 0–250 mL
Y = lambda p: round(LY0 - 4.3 * p)             # 0–200 mm Hg

# diastolic (passive filling) P–V curves: normal, stiff (hypertrophy), stiffer (HFpEF), dilated (HFrEF, AR, MR)
EDP = dict(norm=lambda v: 1 + 1.2 * math.exp((v - 40) / 50),
           stiff=lambda v: 1 + 2 * math.exp((v - 40) / 40),
           stiffer=lambda v: 1 + 2 * math.exp((v - 35) / 30),
           dil=lambda v: 1 + 1.2 * math.exp((v - 80) / 45),
           mr=lambda v: 1 + 1.2 * math.exp((v - 60) / 45))

def curve(fn, v0, v1, n=24):
    pts = [(v0 + (v1 - v0) * i / n) for i in range(n + 1)]
    return ' '.join(f'{"M" if i == 0 else "L"}{X(v)} {Y(fn(v))}' for i, v in enumerate(pts))

def loop(edv, esv, popen, peak, pend, edp='norm', c_end=None, r_end=None):
    """segments of one loop: c_end = volume where 'contraction' ends (MR: slants), r_end = where relaxation ends"""
    fn = EDP[edp]
    c_end = edv if c_end is None else c_end
    r_end = esv if r_end is None else r_end
    ped = fn(edv)
    d = c_end - esv
    seg = dict(
        ivc=f'M{X(edv)} {Y(ped)} L{X(c_end)} {Y(popen)}',
        ej=f'M{X(c_end)} {Y(popen)} C{X(c_end - .3 * d)} {Y(peak + 10)} {X(esv + .3 * d)} {Y(peak + 6)} {X(esv)} {Y(pend)}',
        ivr=f'M{X(esv)} {Y(pend)} L{X(r_end)} {Y(fn(r_end))}',
        fill=curve(fn, r_end, edv))
    full_ = seg['fill'] + ' ' + seg['ivc'].split(' ', 2)[2] + ' ' + seg['ej'].split(' ', 2)[2] + ' ' + seg['ivr'].split(' ', 2)[2]
    return seg, full_

NORM = dict(edv=120, esv=50, popen=80, peak=122, pend=100)          # Guyton ch 9: EDV ~120, ESV ~50, SV ~70, EF ~60%
LOOPS = dict(
    as_=dict(edv=120, esv=70, popen=85, peak=190, pend=150, edp='stiff'),
    mr=dict(edv=160, esv=36, popen=78, peak=108, pend=88, edp='mr', c_end=140),
    ar=dict(edv=190, esv=72, popen=66, peak=140, pend=112, edp='dil', r_end=92),
    ms=dict(edv=90, esv=40, popen=80, peak=116, pend=96),
    pre=dict(edv=150, esv=50, popen=80, peak=130, pend=100),
    aft=dict(edv=120, esv=70, popen=112, peak=160, pend=150),
    ino=dict(edv=120, esv=30, popen=80, peak=140, pend=130),
    hfr=dict(edv=180, esv=132, popen=70, peak=94, pend=86, edp='dil'),
    hfp=dict(edv=95, esv=40, popen=85, peak=126, pend=106, edp='stiffer'))
LOOPS['mr']['c_end'] = 140
LOOPS['mr']['r_end'] = 36
LOOPS['mr']['esv'] = 46          # ejection ends at 46 mL; volume keeps falling (leak) to 36 mL while pressure drops
key = lambda k: 'as_' if k == 'as' else k

# axes + grid
text('Left ventricular pressure–volume loop', 1180, 168, 'dyn-big')
text('one beat runs counter-clockwise · width = stroke volume · area = stroke work', 1180, 190, 'dyn-cap')
ax = f'<path d="M{LX0} {Y(205)} V{LY0} H{X(255)}" class="dyn-line"/>'
for p in (40, 80, 120, 160, 200):
    ax += f'<path d="M{LX0 - 8} {Y(p)} H{LX0}" class="dyn-line"/><path d="M{LX0} {Y(p)} H{X(250)}" class="dyn-dash" style="opacity:.18"/>'
for v in (50, 100, 150, 200, 250):
    ax += f'<path d="M{X(v)} {LY0} V{LY0 + 8}" class="dyn-line"/>'
add(ax)
for p in (0, 40, 80, 120, 160, 200):
    text(str(p), LX0 - 14, Y(p) + 4, 'nf-l2', 'end')
for v in (50, 100, 150, 200, 250):
    text(str(v), X(v), LY0 + 26, 'nf-l2', 'middle')
text('LV volume (mL)', X(250), LY0 + 52, 'nf-l1', 'end')
text('LV pressure', LX0 - 14, Y(205) - 22, 'nf-l1', 'end')
text('(mm Hg)', LX0 - 14, Y(205) - 6, 'nf-l2', 'end')

# the systolic and diastolic P–V curves (Costanzo ch 4)
ES = lambda v0, slope, vmax=250: f'M{X(v0)} {Y(0)} L{X(min(vmax, v0 + 200 / slope))} {Y(min(200, slope * (vmax - v0)))}'
add(f'<path d="{ES(10, 2.25)}" class="dyn-dash" style="opacity:.55"/>')
text('systolic P–V curve: the most pressure the', X(78) + 14, Y(200) + 4, 'nf-l2')
text('LV can make at each volume (contractility)', X(78) + 14, Y(200) + 20, 'nf-l2')
add(f'<path d="{curve(EDP["norm"], 20, 236)}" class="dyn-dash" style="opacity:.55"/>')
text('diastolic P–V curve: passive filling', X(236) - 10, Y(EDP['norm'](236)) - 24, 'nf-l2', 'end')
text('(its steepness = stiffness)', X(236) - 10, Y(EDP['norm'](236)) - 8, 'nf-l2', 'end')
# contractility changes the systolic curve; stiffness changes the diastolic one
add(f'<path d="{ES(10, 6)}" class="dyn-dash" style="{BAD};opacity:.8"/>', when=Z('ino'))
text('steeper systolic curve', X(35) + 14, Y(176), 'nf-l1 dyn-tag', when=Z('ino'))
add(f'<path d="{ES(10, 0.66)}" class="dyn-dash" style="{BAD};opacity:.8"/>', when=Z('hfr'))
text('flatter systolic curve — weak LV', X(208), Y(132), 'nf-l1 dyn-tag', 'middle', when=Z('hfr'))
add(f'<path d="{curve(EDP["stiffer"], 20, 112)}" class="dyn-dash" style="{BAD};opacity:.8"/>', when=Z('hfp'))
text('steeper diastolic curve — stiff LV', X(112) + 12, Y(EDP['stiffer'](112)) + 4, 'nf-l1 dyn-tag', when=Z('hfp'))
add(f'<path d="{curve(EDP["stiff"], 20, 138)}" class="dyn-dash" style="{BAD};opacity:.8"/>', when=Z('as'))

# the normal loop: solid alone, a dashed ghost under a disease
NSEG, NFULL = loop(**NORM)
add(f'<path d="{NFULL}" class="dyn-trace"/>', unless=['dz:*'])
add(f'<path d="{NFULL}" class="dyn-trace" style="stroke-dasharray:9 7;opacity:.45"/>', when=['dz:*'])
for p in PH:
    add(f'<path d="{NSEG[p]}" class="dyn-hl"/>', when=P_(p), unless=['dz:*'])
SEGS = {}
for k in DZ:
    seg, full_ = loop(**LOOPS[key(k)])
    SEGS[k] = seg
    add(f'<path d="{full_}" class="dyn-trace" style="{BAD}"/>', when=Z(k))
    for p in PH:
        add(f'<path d="{seg[p]}" class="dyn-hl"/>', when=[f'dz:{k}&ph:{p}'])
text('dashed = normal · red = changed', X(250), Y(205) - 6, 'nf-l2', 'end', when=['dz:*'])

# normal-loop labels: valve events, phases, volumes (FA p. 292; Costanzo ch 4; Guyton ch 9)
n = NORM
text('mitral valve closes', X(n['edv']) + 14, Y(EDP['norm'](n['edv'])) + 22, 'nf-l2', unless=['dz:*'])
text('aortic valve opens', X(n['edv']) + 14, Y(n['popen']) + 4, 'nf-l2', unless=['dz:*'])
text('aortic valve closes', X(n['esv']) - 14, Y(n['pend']) - 8, 'nf-l2', 'end', unless=['dz:*'])
text('mitral valve opens', X(n['esv']) - 14, Y(3) - 14, 'nf-l2', 'end', unless=['dz:*'])
text('isovolumetric', X(n['edv']) + 14, Y(48), 'nf-l1', unless=['dz:*'])
text('contraction', X(n['edv']) + 14, Y(48) + 16, 'nf-l2', unless=['dz:*'])
text('isovolumetric', X(n['esv']) - 14, Y(56), 'nf-l1', 'end', unless=['dz:*'])
text('relaxation', X(n['esv']) - 14, Y(56) + 16, 'nf-l2', 'end', unless=['dz:*'])
text('ejection', X(85), Y(n['peak'] + 18), 'nf-l1', 'middle', unless=['dz:*'])
text('filling', X(85), Y(3) + 34, 'nf-l1', 'middle', unless=['dz:*'])
# EDV / ESV / SV markers
mk = lambda v, cls='dyn-line', st='': f'<path d="M{X(v)} {LY0 - 2} V{LY0 - 26}" class="{cls}" style="stroke-width:4;{st}"/>'
add(mk(n['esv']) + mk(n['edv']), unless=['dz:*'])
text('ESV ≈ 50', X(n['esv']), LY0 + 44, 'nf-l1', 'middle', unless=['dz:*'])
text('EDV ≈ 120', X(n['edv']), LY0 + 44, 'nf-l1', 'middle', unless=['dz:*'])
SVY = Y(30)
add(f'<path d="M{X(n["esv"])} {SVY} H{X(n["edv"])} M{X(n["esv"])} {SVY - 8} V{SVY + 8} M{X(n["edv"])} {SVY - 8} V{SVY + 8}" class="dyn-line"/>', unless=['dz:*'])
text('stroke volume ≈ 70 mL · EF ≈ 60%', X(85), SVY - 10, 'nf-l2', 'middle', unless=['dz:*'])
for k in DZ:
    L = LOOPS[key(k)]
    lo = min(L['esv'], L.get('r_end', L['esv']))
    add(mk(lo, 'dyn-line', BAD) + mk(L['edv'], 'dyn-line', BAD), when=Z(k))
    text('ESV', X(lo), LY0 + 44, 'nf-l1 dyn-tag', 'middle', when=Z(k))
    text('EDV', X(L['edv']), LY0 + 44, 'nf-l1 dyn-tag', 'middle', when=Z(k))

# what each change does to the loop — short red tags beside it
TAGS = dict(
    as_=[('tall loop: LV pressure far above aortic', X(120) + 16, Y(190), 'start'), ('ESV ↑ · SV ↓', X(120) + 16, Y(190) + 18, 'start')],
    mr=[('no true isovolumetric phases', X(160) + 16, Y(80), 'start'), ('EDV ↑ · ESV ↓ · total SV ↑', X(160) + 16, Y(80) + 18, 'start')],
    ar=[('no true isovolumetric relaxation', X(190) + 16, Y(125), 'start'), ('EDV ↑ · SV ↑', X(190) + 16, Y(125) + 18, 'start')],
    ms=[('small loop: the LV cannot fill', X(120), Y(150), 'middle'), ('EDV ↓ · ESV ↓ · SV ↓', X(120), Y(150) + 18, 'middle')],
    pre=[('EDV moves right · SV ↑', X(150) + 16, Y(30), 'start')],
    aft=[('valve opens later, at a higher pressure', X(120) + 16, Y(165), 'start'), ('ESV ↑ · SV ↓', X(120) + 16, Y(165) + 18, 'start')],
    ino=[('ESV moves left · SV ↑ · EF ↑', X(120) + 16, Y(140), 'start')],
    hfr=[('dilated, weak LV: EDV ↑ · ESV ↑', X(180) + 16, Y(34), 'start'), ('SV ↓ · EF ↓', X(180) + 16, Y(34) + 18, 'start')],
    hfp=[('stiff LV: higher filling pressure', X(112) + 12, Y(72), 'start'), ('EDV ↓ · SV ↓ · EF normal', X(112) + 12, Y(72) + 18, 'start')])
for k, tags in TAGS.items():
    for t, x, y, an in tags:
        text(t, x, y, 'nf-l1 dyn-tag', an, when=Z('as' if k == 'as_' else k))

# ════════ 2. the drawn left heart ════════
text('The left heart', 170, 168, 'dyn-big')
text('blood: lungs → LA → mitral → LV → aortic → aorta', 170, 190, 'dyn-cap')
# pulmonary veins → LA
for y in (296, 366):
    shapes.append(dict(vessel=f'M170 {y} H300', w=30, color='--dk2'))
text('pulmonary veins', 170, 410, 'nf-l2')
# LA
add('<ellipse cx="430" cy="330" rx="170" ry="100" style="fill:var(--dk2);fill-opacity:.12;stroke:var(--dk2);stroke-width:14;stroke-opacity:.45"/>')
text('Left atrium', 430, 300, 'nf-l1', 'middle')
text('LA', 430, 318, 'nf-l2', 'middle')
add('<ellipse cx="430" cy="330" rx="200" ry="122" style="fill:none;stroke:var(--dk5);stroke-width:5;stroke-dasharray:10 7"/>', when=Z('ms', 'mr'))
text('LA pressure ↑ — LA enlarges', 170, 436, 'nf-l1 dyn-tag', when=Z('ms', 'mr'))
# aorta
AO = 'M700 446 V260 Q700 150 830 150 Q960 150 960 260 V900'
shapes.append(dict(vessel=AO, w=92, color='--dk2', mods=[dict(when=Z('ar'), d=14)]))
add(f'<path d="{AO}" style="fill:none;stroke:var(--surface);stroke-width:66;opacity:.75"/>')
text('Aorta', 1040, 300, 'nf-l1')
text('pressure ≈ 80 → 120 mm Hg', 1040, 318, 'nf-l2')
text('backflow into the LV', 1040, 344, 'nf-l1 dyn-tag', when=Z('ar'))

# LV: a bag hanging from the base (mitral opening x 360–500, aortic x 650–750), apex below
def lv(H, w):
    return f'M310 452 C{310 - w} {452 + .5 * H:.0f} {380} {452 + H} {560} {452 + H} C{720} {452 + H} {790 + w} {452 + .5 * H:.0f} {790} 452'
LVS = {  # (big = end-diastole, small = end-systole, wall thickness)
    'n': ((520, 70), (420, 10), 34), 'as': ((470, 40), (430, 10), 64), 'mr': ((600, 80), (400, 0), 34),
    'ar': ((640, 90), (500, 40), 40), 'ms': ((450, 30), (390, 0), 34), 'pre': ((580, 75), (420, 10), 34),
    'aft': ((520, 70), (460, 30), 34), 'ino': ((520, 70), (380, -10), 34), 'hfr': ((620, 90), (560, 70), 28),
    'hfp': ((420, 20), (370, -10), 64)}
for k, (big, small, wall) in LVS.items():
    cond = (lambda ph: [f'dz:{k}&ph:{p}' for p in ph]) if k != 'n' else (lambda ph: P_(*ph))
    unl = None if k != 'n' else ['dz:*']
    for ph, sz, ghost in ((('ivc', 'fill'), big, small), (('ej', 'ivr'), small, big)):
        body = (f'<path d="{lv(*sz)} Z" style="fill:var(--dk2);fill-opacity:.12;stroke:none"/>'
                f'<path d="{lv(*sz)}" style="fill:none;stroke:var(--dk2);stroke-width:{wall};stroke-opacity:.45;stroke-linecap:round"/>')
        g = f'<path d="{lv(*ghost)}" class="dyn-dash" style="opacity:.5"/>'
        add(body, when=cond(ph), unless=unl)
        add(g, when=cond(('fill',) if ph[0] == 'ivc' else ('ej',)), unless=unl)
text('Left ventricle', 560, 760, 'nf-l1', 'middle')
text('LV', 560, 778, 'nf-l2', 'middle')
text('dashed = where the wall started this phase', 560, 1150, 'dyn-cap', 'middle', when=P_('ej', 'fill'))
text('concentric hypertrophy — thick, stiff wall', 560, 1130, 'nf-l1 dyn-tag', 'middle', when=Z('as', 'hfp'))
text('eccentric dilation — big chamber', 560, 1130, 'nf-l1 dyn-tag', 'middle', when=Z('ar', 'mr', 'hfr'))

# valves: leaflets open or shut by phase (FA p. 292)
LF = 'fill:none;stroke:var(--ink-2);stroke-width:7;stroke-linecap:round'
LFT = 'fill:none;stroke:var(--ink-2);stroke-width:15;stroke-linecap:round'
MIT = dict(shut='M360 452 Q395 448 428 446 M500 452 Q465 448 432 446', open='M360 452 Q362 500 372 546 M500 452 Q498 500 488 546',
           leak='M360 452 Q392 448 414 446 M500 452 Q468 448 446 446', narrow='M362 452 Q394 494 418 524 M498 452 Q466 494 442 524')
AOV = dict(shut='M650 452 Q680 462 698 470 M750 452 Q720 462 702 470', open='M650 452 Q652 400 660 360 M750 452 Q748 400 740 360',
           leak='M650 452 Q676 462 688 468 M750 452 Q724 462 712 468', narrow='M652 452 Q680 412 692 386 M748 452 Q720 412 708 386')
# mitral
add(f'<path d="{MIT["open"]}" style="{LF}"/>', when=P_('fill'), unless=Z('ms'))
add(f'<path d="{MIT["narrow"]}" style="{LFT}"/>', when=['dz:ms&ph:fill'])
add(f'<path d="{MIT["shut"]}" style="{LF}"/>', when=P_('ivc', 'ej', 'ivr'), unless=Z('mr', 'ms'))
add(f'<path d="{MIT["shut"]}" style="{LFT}"/>', when=['dz:ms&ph:ivc', 'dz:ms&ph:ej', 'dz:ms&ph:ivr'])
add(f'<path d="{MIT["leak"]}" style="{LF}"/>', when=['dz:mr&ph:ivc', 'dz:mr&ph:ej', 'dz:mr&ph:ivr'])
# aortic
add(f'<path d="{AOV["open"]}" style="{LF}"/>', when=P_('ej'), unless=Z('as'))
add(f'<path d="{AOV["narrow"]}" style="{LFT}"/>', when=['dz:as&ph:ej'])
add(f'<path d="{AOV["shut"]}" style="{LF}"/>', when=P_('ivc', 'ivr', 'fill'), unless=Z('ar', 'as'))
add(f'<path d="{AOV["shut"]}" style="{LFT}"/>', when=['dz:as&ph:ivc', 'dz:as&ph:ivr', 'dz:as&ph:fill'])
add(f'<path d="{AOV["leak"]}" style="{LF}"/>', when=['dz:ar&ph:ivc', 'dz:ar&ph:ivr', 'dz:ar&ph:fill'])
# jets
text('regurgitant jet into the LA', 430, 412, 'nf-l1 dyn-tag', 'middle', when=['dz:mr&ph:ej', 'dz:mr&ph:ivc'])
text('jet back into the LV', 740, 640, 'nf-l1 dyn-tag', 'end', when=['dz:ar&ph:ivr', 'dz:ar&ph:fill'])
text('fast jet through a narrow valve', 830, 88, 'nf-l1 dyn-tag', 'middle', when=['dz:as&ph:ej'])
text('fish-mouth valve — slow filling', 610, 600, 'nf-l1 dyn-tag', when=['dz:ms&ph:fill'])

# valve sites — tap targets whose labels say open / closed
VB = dict(n=[-1, 0], w=8, t='ch', ions=[])
sites = []
sites.append(dict(VB, x=430, y=452, l='Mitral valve', s='opens when LV < LA', lx=290, ly=480, la='end', c='heartsounds',
                  need=P_('fill'), closed='closed', unless=Z('mr', 'ms')))
sites.append(dict(VB, x=430, y=452, l='Mitral valve', s='leaks back in systole', lx=290, ly=480, la='end', c='mitralregurg',
                  need=P_('fill'), closed='incompetent', when=Z('mr')))
sites.append(dict(VB, x=430, y=452, l='Mitral valve', s='narrowed — opening snap', lx=290, ly=480, la='end', c='mitralsten',
                  need=P_('fill'), closed='closed', when=Z('ms')))
AVB = dict(VB, n=[1, 0], x=700, y=452, lx=1030, ly=470, la='start')
sites.append(dict(AVB, l='Aortic valve', s='opens when LV > aorta', c='s2split', need=P_('ej'), closed='closed', unless=Z('as', 'ar')))
sites.append(dict(AVB, l='Aortic valve', s='calcified — narrow opening', c='aortstenosis', need=P_('ej'), closed='closed', when=Z('as')))
sites.append(dict(AVB, l='Aortic valve', s='leaks back in diastole', c='aortregurg', need=P_('ej'), closed='incompetent', when=Z('ar')))

# ════════ 3. blood in motion ════════
PV1, PV2 = 'M170 296 H330', 'M170 366 H330'
INFLOW = 'M430 330 V460 Q440 620 520 760'
OUT = 'M600 820 Q690 640 700 452 V260 Q700 150 830 150 Q960 150 960 260 V900'
RUN = 'M830 150 Q960 150 960 260 V900'
flows = [
  dict(d=PV1, len=160, speed=70, r=7, base=dict(bl=2), mods=[dict(when=Z('ms'), speed=.5)]),
  dict(d=PV2, len=160, speed=70, r=7, base=dict(bl=2), mods=[dict(when=Z('ms'), speed=.5)]),
  dict(d=INFLOW, len=440, speed=170, r=8, base=dict(bl=6), when=P_('fill'),
       mods=[dict(when=Z('ms'), set=dict(bl=3), speed=.5), dict(when=Z('pre', 'ar', 'mr'), add=dict(bl=2)), dict(when=Z('hfp'), set=dict(bl=4))]),
  dict(d=OUT, len=1560, speed=260, r=8, base=dict(bl=9), when=P_('ej'),
       mods=[dict(when=Z('as'), set=dict(bl=5), speed=1.6), dict(when=Z('aft', 'hfr', 'ms', 'hfp'), set=dict(bl=6)),
             dict(when=Z('ino', 'pre', 'ar'), add=dict(bl=3)), dict(when=Z('mr'), set=dict(bl=7))]),
  dict(d=RUN, len=840, speed=110, r=7, base=dict(bl=4), unless=P_('ej')),
  # regurgitation
  dict(d='M470 700 Q440 560 430 452 V360', len=360, speed=200, r=7, base=dict(bk=5), when=['dz:mr&ph:ej', 'dz:mr&ph:ivc']),
  dict(d='M700 300 V452 Q690 600 620 760', len=480, speed=170, r=7, base=dict(bk=5), when=['dz:ar&ph:ivr', 'dz:ar&ph:fill']),
]
# the moving point on the loop: runs along the highlighted segment
SEGLEN = dict(ivc=lambda L: abs(L['popen'] - 8) * 4.3 + 20, ej=lambda L: (L.get('c_end', L['edv']) - L['esv']) * 3.8 + 140,
              ivr=lambda L: L['pend'] * 4.3, fill=lambda L: (L['edv'] - L['esv']) * 3.8 + 40)
for p in PH:
    flows.append(dict(d=NSEG[p], len=round(SEGLEN[p](NORM)), speed=round(SEGLEN[p](NORM) / 2.4), r=11, base=dict(now=1), when=P_(p), unless=['dz:*']))
    for k in DZ:
        L = LOOPS[key(k)]
        flows.append(dict(d=SEGS[k][p], len=round(SEGLEN[p](L)), speed=round(SEGLEN[p](L) / 2.4), r=11, base=dict(now=1), when=[f'dz:{k}&ph:{p}']))

# ════════ 4. the time strip: systole, diastole, sounds, murmurs ════════
T0, T1 = 300, 2400
TX = lambda t: round(T0 + (T1 - T0) * t / 0.8)        # one 0.8-s beat
BND = dict(ivc=(0, .05), ej=(.05, .32), ivr=(.32, .40), fill=(.40, .80))
SY = 1330
text('One beat in time — where the sounds and murmurs fall', 170, SY - 40, 'dyn-big')
text('S1 = mitral (and tricuspid) closure · S2 = aortic (and pulmonic) closure', 170, SY - 20, 'dyn-cap')
NAMES = dict(ivc='isovol. contraction', ej='ejection', ivr='isovol. relax.', fill='filling')
for p, (a, b) in BND.items():
    add(f'<rect x="{TX(a)}" y="{SY + 30}" width="{TX(b) - TX(a)}" height="44" class="dyn-soft"/>')
    add(f'<rect x="{TX(a)}" y="{SY + 30}" width="{TX(b) - TX(a)}" height="44" style="fill:var(--accent);opacity:.28"/>', when=P_(p))
for p, x, an in (('ivc', TX(.025), 'middle'), ('ej', TX(.185), 'middle'), ('ivr', TX(.36), 'middle'), ('fill', TX(.6), 'middle')):
    if p == 'ivc':
        text('IVC', x, SY + 58, 'nf-l2', an)
    elif p == 'ivr':
        text('IVR', x, SY + 58, 'nf-l2', an)
    else:
        text(NAMES[p], x, SY + 58, 'nf-l1', an)
add(f'<path d="M{TX(0)} {SY + 18} H{TX(.32)} M{TX(0)} {SY + 12} V{SY + 24} M{TX(.32)} {SY + 12} V{SY + 24}" class="dyn-line"/>'
    f'<path d="M{TX(.32) + 6} {SY + 18} H{TX(.8)} M{TX(.8)} {SY + 12} V{SY + 24}" class="dyn-line"/>')
text('SYSTOLE — S1 to S2', TX(.16), SY + 8, 'nf-l1', 'middle')
text('DIASTOLE — S2 to the next S1', TX(.56), SY + 8, 'nf-l1', 'middle')
text('IVC = isovolumetric contraction · IVR = isovolumetric relaxation', T1, SY + 98, 'dyn-cap', 'end')
# heart sounds row
HY = SY + 150
text('Sounds', 170, HY + 4, 'nf-l1')
add(f'<path d="M{T0} {HY} H{T1}" class="dyn-line" style="opacity:.4"/>')
def snd(t, lab, h=34, when=None, unless=None, cls='dyn-line', st=''):
    add(f'<path d="M{TX(t) - 5} {HY - h} V{HY + h} M{TX(t) + 5} {HY - h * .7:.0f} V{HY + h * .7:.0f}" class="{cls}" style="stroke-width:4;{st}"/>', when, unless)
    text(lab, TX(t), HY - h - 10, 'nf-l1', 'middle', when=when, unless=unless)
snd(0.004, 'S1')
snd(0.32, 'S2', unless=Z('as'))
snd(0.32, 'S2 soft', h=16, when=Z('as'))
snd(0.44, 'S3', h=22, when=Z('hfr', 'mr', 'ar'), st=BAD)
snd(0.75, 'S4', h=22, when=Z('hfp'), st=BAD)
snd(0.40, 'OS', h=22, when=Z('ms'), st=BAD)
# murmur row
MY = HY + 130
text('Murmur', 170, MY - 26, 'nf-l1')
add(f'<path d="M{T0} {MY} H{T1}" class="dyn-line" style="opacity:.4"/>')
MF = 'fill:var(--bad);fill-opacity:.28;stroke:var(--bad);stroke-width:2.5'
add(f'<path d="M{TX(.06)} {MY} L{TX(.17)} {MY - 70} L{TX(.30)} {MY} Z" style="{MF}"/>', when=Z('as'))
add(f'<path d="M{TX(.012)} {MY} V{MY - 52} H{TX(.31)} V{MY} Z" style="{MF}"/>', when=Z('mr'))
add(f'<path d="M{TX(.325)} {MY} V{MY - 62} L{TX(.62)} {MY} Z" style="{MF}"/>', when=Z('ar'))
rum = ''.join(f'L{TX(.42 + i * .0095)} {MY - (14 if i % 2 else 34) - (18 if i > 31 else 0)} ' for i in range(39))
add(f'<path d="M{TX(.42)} {MY} {rum}L{TX(.79)} {MY} Z" style="{MF}"/>', when=Z('ms'))
MUR = dict(as_=('crescendo-decrescendo systolic ejection murmur · heart base → carotids', .17),
           mr=('holosystolic, high-pitched blowing · apex → axilla', .16),
           ar=('early diastolic decrescendo blowing · left sternal border', .47),
           ms=('opening snap, then a mid-to-late diastolic rumble · apex', .6))
for k, (t, at) in MUR.items():
    text(t, TX(at), MY + 26, 'nf-l1 dyn-tag', 'middle', when=Z('as' if k == 'as_' else k))
text('no murmur — a normal beat has only S1 and S2', TX(.4), MY + 26, 'nf-l2', 'middle', unless=Z('as', 'mr', 'ar', 'ms'))

# ════════ 5. readouts (FA pp. 289–290, 293, 316; Costanzo ch 4; Guyton ch 9, 23; Bootcamp) ════════
def ro(label, **d):
    return dict(l=label, mods=[dict(when=Z(k.rstrip('_')), d=v) for k, v in d.items()])
readouts = [
  ro('EDV', as_=0, mr=1, ar=1, ms=-1, pre=1, aft=0, ino=0, hfr=1, hfp=-1),
  ro('ESV', as_=1, mr=-1, ms=-1, aft=1, ino=-1, hfr=1),
  ro('Stroke volume', as_=-1, mr=1, ar=1, ms=-1, pre=1, aft=-1, ino=1, hfr=-1, hfp=-1),
  ro('Ejection fraction', aft=-1, ino=1, hfr=-1, hfp=0),
  ro('Peak LV pressure', as_=1, aft=1, ino=1),
  ro('LA pressure', mr=1, ms=1, hfr=1, hfp=1)]

notes = {
  'ph:ivc': 'Isovolumetric contraction: the mitral valve has just shut (S1) and the aortic valve is still shut, so the LV squeezes '
            'without changing volume — pressure climbs to aortic pressure (~80 mm Hg). The phase of highest O₂ consumption.',
  'ph:ej': 'Ejection: LV pressure passes aortic pressure, the aortic valve opens and the stroke volume leaves — volume falls from '
           'EDV to ESV while pressure peaks. SV = EDV − ESV; EF = SV / EDV, normally 50–70%.',
  'ph:ivr': 'Isovolumetric relaxation: LV pressure falls below aortic pressure, the aortic valve shuts (S2) and the mitral valve is '
            'still shut — pressure drops with the volume held at ESV.',
  'ph:fill': 'Filling: LV pressure falls below LA pressure, the mitral valve opens and blood pours in — rapid filling first (where '
             'an S3 falls), the atrial kick last (where an S4 falls). Volume climbs to EDV along the diastolic curve.',
  'dz:as': 'Aortic stenosis: the LV must make far more pressure to push blood through a calcified valve — a tall loop, ESV ↑, SV ↓ '
           '(EDV unchanged if mild); hypertrophy stiffens the LV, so filling pressure rises. Crescendo-decrescendo systolic murmur '
           'at the base radiating to the carotids, soft S2. Clue: older patient with syncope, angina, dyspnea on exertion; '
           'pulsus parvus et tardus.',
  'dz:mr': 'Mitral regurgitation: blood leaks back into the LA during systole, so there is no true isovolumetric phase. ESV ↓; the '
           'LA returns the extra blood, so EDV ↑ and total SV ↑ (part of it goes backward). Holosystolic blowing murmur at the apex '
           'radiating to the axilla; tall LA v wave. Clue: after an MI, MVP, LV dilation, rheumatic fever.',
  'dz:ar': 'Aortic regurgitation: blood falls back from the aorta into the LV during diastole — no true isovolumetric phase, EDV ↑ '
           'and SV ↑ as the chamber dilates. Early diastolic decrescendo blowing murmur at the left sternal border. Clue: wide '
           'pulse pressure, bounding pulses, head bobbing; BEAR — bicuspid valve, endocarditis, aortic root dilation, rheumatic fever.',
  'dz:ms': 'Mitral stenosis: the narrowed valve holds back filling — EDV, ESV and SV fall while LA pressure rises (LA ≫ LV in '
           'diastole). Opening snap after S2, then a mid-to-late diastolic rumble at the apex; a shorter S2–OS interval means more '
           'severe. Clue: rheumatic fever; a big LA → atrial fibrillation, dysphagia, hoarseness (Ortner), hemoptysis.',
  'dz:pre': '↑ Preload (more venous return — IV fluids, volume): the LV fills further along its diastolic curve, so EDV ↑ and, by '
            'Frank-Starling, SV ↑. Bedside: a passive leg raise ↑ preload and makes most murmurs louder, but MVP and HCM softer.',
  'dz:aft': '↑ Afterload (higher aortic pressure — hypertension, phenylephrine): the LV must reach a higher pressure before the aortic '
            'valve opens, so less contraction is left for ejection — SV ↓, ESV ↑; chronically the LV hypertrophies. Hand grip ↑ '
            'afterload: AR, MR and VSD murmurs get louder, AS and HCM softer.',
  'dz:ino': '↑ Contractility (β₁ catecholamines, dobutamine, milrinone, digoxin): the systolic P–V curve steepens, so the LV ejects '
            'to a smaller ESV at a higher pressure — SV ↑ and EF ↑. Negative inotropes (β-blockers, non-dihydropyridine Ca²⁺ '
            'blockers) and loss of myocardium (MI, heart failure) do the reverse.',
  'dz:hfr': 'Systolic heart failure (HFrEF — after an MI, dilated cardiomyopathy): contractility falls, the systolic curve flattens, '
            'ESV ↑ and SV ↓, so EF ↓. The LV dilates (EDV ↑) — Frank-Starling partly compensates. An S3 in early diastole. Clue: '
            'dyspnea, orthopnea, rales, JVD, edema.',
  'dz:hfp': 'Diastolic heart failure (HFpEF — usually hypertrophy): the stiff LV fills along a steeper diastolic curve, so filling '
            'pressure rises for any volume while EDV and SV fall (Bootcamp); EF stays normal. An S4 — the atrial kick into a stiff LV. Clue: '
            'older hypertensive patient with dyspnea and a normal EF.',
  '': 'Step through the four phases, then change one thing. Tap a valve for its card.'}

dyn = dict(
  kinds=dict(bl=['bl', '--dk2'], bk=['bk', '--dk5'], now=['now', '--accent']),
  groups=[['bl', 'Blood'], ['bk', 'Backflow'], ['now', 'Where the beat is']],
  switches=[dict(id='ph', label='One beat, phase by phase', type='steps', auto=3,
                 options=[['ivc', 'Isovolumetric contraction'], ['ej', 'Ejection'], ['ivr', 'Isovolumetric relaxation'], ['fill', 'Filling']]),
            dict(id='dz', label='Change one thing', type='one',
                 options=[['as', 'Aortic stenosis', 'aortstenosis'], ['mr', 'Mitral regurgitation', 'mitralregurg'],
                          ['ar', 'Aortic regurgitation', 'aortregurg'], ['ms', 'Mitral stenosis', 'mitralsten'],
                          ['pre', '↑ Preload', 'starling'], ['aft', '↑ Afterload', 'starling'], ['ino', '↑ Contractility (inotrope)', 'pressors'],
                          ['hfr', 'Systolic HF (HFrEF)', 'hf'], ['hfp', 'Diastolic HF (HFpEF)', 'hf']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2520, y=110, w=1000),
  src='First Aid pp. 289–290, 292–293, 295–296, 316 · Costanzo ch 4 · Guyton ch 9, 23 · Bootcamp Cardiology')

MAP = dict(
  id='pvflow', title='Pressure–Volume Loop in Motion', topic='cardio', after='cardcycle',
  sub='A drawn left heart beside its pressure–volume loop and a one-beat time strip — step through the four phases to watch the '
      'valves open and shut and the loop trace itself, then add a valve lesion, a load change or heart failure to see the loop, '
      'the murmur and EDV, ESV, SV and EF change. Tap a valve for its card',
  w=3600, h=1900,
  fa='289–290, 292–293, 295–296, 316', src=[CO4, GY9, GY23, BC_PV],
  lanes=[('pvHeart', 'The left heart', 'tca'), ('pvLoop', 'The loop', 'glycolysis'), ('pvSound', 'Sounds and murmurs', 'ppp')],
  nodes=[
    ('pv1', 'Mitral valve lesions', 300, 560, 'pvHeart', 'stenosis · regurgitation · MVP', ['mitralsten', 'mitralregurg', 'mvp']),
    ('pv2', 'Aortic valve lesions', 1090, 400, 'pvHeart', 'stenosis · regurgitation', ['aortstenosis', 'aortregurg']),
    ('pv3', 'Ventricular failure', 250, 1000, 'pvHeart', 'HFrEF · HFpEF · cardiomyopathy', ['hf', 'dcm', 'hcm', 'hfdrugs']),
    ('pv4', 'Pressure–volume loops', 1650, 1250, 'pvLoop', 'normal · valve disease', ['pvloop', 'pvvalve']),
    ('pv5', 'Preload, afterload', 2120, 1250, 'pvLoop', 'contractility · SV, EF', ['starling', 'cardiaceq', 'pressors', 'digoxin']),
    ('pv6', 'Heart sounds', 600, 1790, 'pvSound', 'S1–S4 · splitting', ['heartsounds', 's2split', 'jvp']),
    ('pv7', 'Murmur maneuvers', 1100, 1790, 'pvSound', 'preload · afterload · breathing', ['maneuvers'])],
  panels=[
    (2520, 1020, 1000, 'Valve lesions on the loop (First Aid p. 293)', [
      ('Aortic stenosis', '↑ LV pressure · ↑ ESV · ↓ SV · EDV unchanged if mild'),
      ('Mitral regurgitation', 'no true isovolumetric phase · ↑ EDV · ↓ ESV · ↑ total SV'),
      ('Aortic regurgitation', 'no true isovolumetric phase · ↑ EDV · ↑ SV'),
      ('Mitral stenosis', '↑ LA pressure · ↓ EDV · ↓ ESV · ↓ SV')]),
    (2520, 1200, 1000, 'Heart sounds (First Aid p. 292)', [
      ('S1', 'mitral + tricuspid closure · loudest at the mitral area'),
      ('S2', 'aortic + pulmonic closure · left upper sternal border'),
      ('S3', 'early diastole, rapid filling · ↑ filling pressure (MR, AR, HF)'),
      ('S4', 'late diastole, atrial kick into a stiff LV (hypertrophy)')]),
    (2520, 1380, 1000, 'Maneuvers (First Aid p. 295)', [
      ('Standing, Valsalva', '↓ preload: most murmurs softer · MVP and HCM louder'),
      ('Passive leg raise', '↑ preload: most murmurs louder · MVP and HCM softer'),
      ('Hand grip', '↑ afterload: AR, MR, VSD louder · AS and HCM softer'),
      ('Inspiration', 'right-sided murmurs louder (left-sided: expiration)')])],
  dyn=dyn)
