# The Sacrum in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# The sacrum from behind between the ilia, with L5 above, both sacral sulci, both ILAs and the two oblique axes. `walk`
# (steps, auto) alternates left and right stance: the sacrum turns forward about the left then the right oblique axis. A
# `one` switch holds a dysfunction — left-on-left, left-on-right, left unilateral flexion, right unilateral extension,
# bilateral flexion, bilateral extension — and shows the sulci (deep/shallow) and ILAs (posterior/inferior) as the cards
# give them; a `sphinx` toggle shows how each responds to the sphinx test. Only the card-stated patterns are drawn (no
# mirrored right-on-right or right-on-left landmark sets). 2 readouts. fa '' — the cards cite no First Aid pages. No new cards.
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
W = lambda *k: [f'walk:{x}' for x in k]
PANY = 1180
SL, SR, IL, IR = (900, 560), (1300, 560), (980, 1000), (1220, 1000)

text('The sacrum — walking on oblique axes, and where it gets stuck', 180, 150, 'dyn-big')
text('posterior view — patient’s left on your left · thumbs on the sulci (base) and the ILAs', 180, 176, 'dyn-cap')

# ════════ bones ════════
add('<path d="M560 420 C420 600 460 1000 640 1180 L800 1000 L800 520 Z" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>')
add('<path d="M1640 420 C1780 600 1740 1000 1560 1180 L1400 1000 L1400 520 Z" style="fill:var(--dk6);fill-opacity:.1;stroke:var(--dk6);stroke-width:4"/>')
text('left ilium', 520, 400, 'nf-l2'); text('right ilium', 1680, 400, 'nf-l2', 'end')
add('<path d="M820 500 H1380 L1100 1160 Z" style="fill:var(--dk2);fill-opacity:.12;stroke:var(--dk2);stroke-width:5;stroke-linejoin:round"/>')
text('sacrum', 1100, 760, 'nf-l1', 'middle')
add('<rect x="960" y="330" width="280" height="130" rx="20" style="fill:var(--dk3);fill-opacity:.15;stroke:var(--dk3);stroke-width:4"/>')
text('L5', 1100, 405, 'nf-l1', 'middle')
add(f'<path d="M{SL[0] - 40} {SL[1] - 40} L{IR[0] + 60} {IR[1] + 70}" style="stroke:var(--accent);stroke-width:4;stroke-dasharray:12 8"/>')
add(f'<path d="M{SR[0] + 40} {SR[1] - 40} L{IL[0] - 60} {IL[1] + 70}" style="stroke:var(--dk9);stroke-width:4;stroke-dasharray:12 8"/>')
text('left oblique axis', SL[0] - 50, SL[1] - 60, 'nf-l2', 'end'); text('right oblique axis', SR[0] + 50, SR[1] - 60, 'nf-l2')
add(f'<path d="M{SL[0] - 40} {SL[1] - 40} L{IR[0] + 60} {IR[1] + 70}" style="stroke:var(--accent);stroke-width:12;opacity:.6"/>', when=['walk:ls&!dx:*'] + D('lol'))
add(f'<path d="M{SR[0] + 40} {SR[1] - 40} L{IL[0] - 60} {IL[1] + 70}" style="stroke:var(--dk9);stroke-width:12;opacity:.6"/>', when=['walk:rs&!dx:*'] + D('lor'))
text('left stance → turns forward on the left oblique axis (left-on-left)', 1100, 1260, 'nf-l1 dyn-tag', 'middle', when=W('ls'), unless=['dx:*'])
text('right stance → right-on-right', 1100, 1260, 'nf-l1 dyn-tag', 'middle', when=W('rs'), unless=['dx:*'])

# ════════ landmarks ════════
def sul(p, kind, when=None, unless=None):
    r, sty = dict(deep=(34, 'fill:var(--ink);fill-opacity:.75'), shallow=(18, 'fill:var(--surface);stroke:var(--ink-2);stroke-width:4'),
                  n=(24, 'fill:var(--ink-3);fill-opacity:.5'))[kind]
    add(f'<circle cx="{p[0]}" cy="{p[1]}" r="{r}" style="{sty}"/>', when=when, unless=unless)
def ila(p, kind, when=None, unless=None):
    dy, r = dict(pi=(40, 34), i=(60, 26), n=(0, 22))[kind]
    add(f'<rect x="{p[0] - r}" y="{p[1] + dy - r}" width="{2 * r}" height="{2 * r}" rx="8" style="fill:var(--dk10);fill-opacity:{.85 if kind != "n" else .4}"/>',
        when=when, unless=unless)
NEUT = dict(unless=['dx:*'])
for p in (SL, SR): sul(p, 'n', **NEUT); sul(p, 'n', when=['dx:lol&sphinx'])
for p in (IL, IR): ila(p, 'n', **NEUT); ila(p, 'n', when=['dx:lol&sphinx'])
ST = dict(lol=('n', 'deep', 'pi', 'n'), lor=('n', 'deep', 'pi', 'n'), luf=('deep', 'n', 'i', 'n'),
          rue=('n', 'shallow', 'pi', 'n'), bf=('deep', 'deep', 'n', 'n'), be=('shallow', 'shallow', 'n', 'n'))
for k, (a, b, c, d) in ST.items():
    un = ['dx:lol&sphinx'] if k == 'lol' else None
    sul(SL, a, when=D(k), unless=un); sul(SR, b, when=D(k), unless=un); ila(IL, c, when=D(k), unless=un); ila(IR, d, when=D(k), unless=un)
add(f'<circle cx="{SR[0]}" cy="{SR[1]}" r="52" style="fill:none;stroke:var(--bad);stroke-width:5"/>', when=['dx:lor&sphinx'])
text('sulcus', SL[0], SL[1] + 70, 'nf-l2', 'middle'); text('sulcus', SR[0], SR[1] + 70, 'nf-l2', 'middle')
text('ILA', IL[0] - 60, IL[1] + 10, 'nf-l2', 'end'); text('ILA', IR[0] + 60, IR[1] + 10, 'nf-l2')
text('● deep  ○ shallow  ■ ILA posterior / inferior', 1100, 1330, 'nf-l2', 'middle')
TAG = dict(lol='left-on-left — seated flexion + right · spring − · lordosis ↑ · L5 rotated right',
           lor='left-on-right — seated flexion + left · spring + · lordosis ↓ · L5 FRS right',
           luf='left unilateral flexion — seated flexion + left · ILA more inferior than posterior · spring −',
           rue='right unilateral extension — seated flexion + right · shallow right sulcus · spring +',
           bf='bilateral flexion — both sulci deep · lordosis ↑ · spring −',
           be='bilateral extension — both sulci shallow · lordosis ↓ · spring + · seated flexion equivocal')
for k, s in TAG.items(): text(s, 1100, 290, 'nf-l1 dyn-tag', 'middle', when=D(k))
text('sphinx: landmarks more symmetric', 1100, 1390, 'nf-l1', 'middle', when=['dx:lol&sphinx'])
text('sphinx: landmarks more asymmetric', 1100, 1390, 'nf-l1', 'middle', when=['dx:lor&sphinx'])
text('sphinx: stays asymmetric or unchanged', 1100, 1390, 'nf-l1', 'middle', when=['dx:luf&sphinx', 'dx:rue&sphinx'])

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{SR[0]} {SR[1] - 90} C{SR[0] - 80} {SR[1] - 140} {SL[0] + 80} {SL[1] - 140} {SL[0]} {SL[1] - 90}', len=480, speed=80, r=9,
       base=dict(rot=3), when=W('ls'), unless=['dx:*']),
  dict(d=f'M{SL[0]} {SL[1] - 90} C{SL[0] + 80} {SL[1] - 140} {SR[0] - 80} {SR[1] - 140} {SR[0]} {SR[1] - 90}', len=480, speed=80, r=9,
       base=dict(rot=3), when=W('rs'), unless=['dx:*']),
  dict(d=f'M1100 820 C1100 700 1100 600 1100 470', len=350, speed=50, r=8, base=dict(rot=2), when=D('bf', 'luf')),
  dict(d=f'M1100 470 C1100 600 1100 700 1100 820', len=350, speed=50, r=8, base=dict(rot=2), when=D('be', 'rue')),
]
sites = [dict(x=1100, y=1100, n=[0, 1], w=10, t='rec', l='', aria='Sacral axes', c='sacmotion', ions=[]),
         dict(x=SL[0] - 120, y=SL[1] + 200, n=[-1, 0], w=10, t='rec', l='', aria='Forward torsion', c='fwdtorsion', ions=[]),
         dict(x=SR[0] + 120, y=SR[1] + 200, n=[1, 0], w=10, t='rec', l='', aria='Backward torsion', c='bwdtorsion', ions=[]),
         dict(x=IL[0] - 140, y=IL[1] + 120, n=[-1, 1], w=10, t='rec', l='', aria='Unilateral flexion and extension', c='sacshear', ions=[]),
         dict(x=IR[0] + 140, y=IR[1] + 120, n=[1, 1], w=10, t='rec', l='', aria='Bilateral flexion and extension', c='sacbilat', ions=[])]

readouts = [
  dict(l='Spring test positive', mods=[dict(when=D('lor', 'rue', 'be'), d=1), dict(when=D('lol', 'luf', 'bf'), d=-1)]),
  dict(l='Lumbar lordosis', mods=[dict(when=D('lol', 'bf'), d=1), dict(when=D('lor', 'be'), d=-1)]),
]

notes = {
  '': 'The sacrum moves only 2–4° between the ilia but acts as the body’s differential. Nutation (base forward) comes with lumbar '
      'extension; counternutation (base back) with lumbar flexion. The axes are a teaching model — research finds no fixed axes.',
  'walk:ls': 'Walking (shown when nothing is stuck) — left stance: the sacrum turns forward about the left oblique axis (named for its superior pole — upper left SI joint '
             'to lower right) — left-on-left.',
  'walk:rs': 'Walking (shown when nothing is stuck) — right stance: right-on-right about the right oblique axis.',
  'dx:lol': 'Left-on-left (forward torsion): normal gait motion stuck to one side, often from a short leg (short right leg → more '
            'left stance). Deep right sulcus, left ILA posterior and inferior; seated flexion positive on the right; spring '
            'negative; lordosis increased; lumbar convex right, L5 neutral rotated right; left leg looks short supine.',
  'dx:lor': 'Left-on-right (backward torsion): nonphysiologic — lumbar flexed and side bent, the sacrum counternutates and locks. '
            'Same landmarks as left-on-left, but seated flexion positive on the left, spring positive, lordosis reduced, sphinx '
            'worsens; L5 FRS right; crests level.',
  'dx:luf': 'Left unilateral flexion (commoner on the left): seated flexion positive left, deep left sulcus, left ILA more inferior '
            'than posterior, spring negative.',
  'dx:rue': 'Right unilateral extension (commoner on the right): seated flexion positive right, shallow right sulcus, left ILA '
            'posterior and inferior, spring positive.',
  'dx:bf': 'Bilateral flexion: both sulci deep, more lordosis, spring negative — near-physiologic, rarely diagnosed.',
  'dx:be': 'Bilateral extension: both sulci shallow, less lordosis, spring positive; destabilizes the pelvis — after lithotomy '
           'deliveries or repeated forward bending; pain worse bending backward. Seated flexion equivocal; PSISs rise early.',
  'sphinx': 'Sphinx test: forward torsions become more symmetric, backward torsions more asymmetric, unilateral lesions stay '
            'asymmetric or unchanged.',
}

dyn = dict(
  kinds=dict(rot=['mov', '--accent']), groups=[['mov', 'Sacral motion (base up = flexion, down = extension, schematic)']],
  switches=[dict(id='walk', label='Walking', type='steps', auto=3, options=[['ls', 'Left stance'], ['rs', 'Right stance']]),
            dict(id='dx', label='Stuck', type='one', options=[
              ['lol', 'Left-on-left', 'fwdtorsion'], ['lor', 'Left-on-right', 'bwdtorsion'], ['luf', 'Left unilateral flexion', 'sacshear'],
              ['rue', 'Right unilateral extension', 'sacshear'], ['bf', 'Bilateral flexion', 'sacbilat'], ['be', 'Bilateral extension', 'sacbilat']]),
            dict(id='sphinx', label='Test', type='toggle', on='Sphinx position', off='Sphinx test', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Foundations ch 38')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='sacsim', title='The Sacrum in Motion', topic='omm', after='ommmech',
  sub='Walk the sacrum around its oblique axes, then lock it in a forward or backward torsion, a unilateral or a bilateral '
      'lesion — and read the sulci, ILAs, spring and sphinx tests',
  w=3600, h=1900,
  fa='',
  src=['Foundations of Osteopathic Medicine ch 38 — Functional Anatomy and Diagnosis of the Sacrum',
       'OCOM OMM — OMS2 written midterm study guide'],
  lanes=[('saAxis', 'Axes', 'glycolysis'), ('saDys', 'Dysfunctions', 'tca')],
  nodes=[
    ('sa1', 'Sacral axes & nutation', 330, 1700, 'saAxis', 'oblique axes · gait', ['sacmotion'], 'hub'),
    ('sa2', 'Forward sacral torsion', 760, 1700, 'saDys', 'spring −, sphinx better', ['fwdtorsion']),
    ('sa3', 'Backward sacral torsion', 1200, 1700, 'saDys', 'spring +, sphinx worse', ['bwdtorsion']),
    ('sa4', 'Unilateral flexion/extension', 1640, 1700, 'saDys', 'ILA inferior', ['sacshear']),
    ('sa5', 'Bilateral flexion/extension', 2080, 1700, 'saDys', 'both sulci', ['sacbilat'])],
  panels=[
    (2500, PANY, 1000, 'Spring and sphinx (Foundations ch 38)', [
      ('Forward torsion', 'spring − · sphinx more symmetric'), ('Backward torsion', 'spring + · sphinx more asymmetric'),
      ('Unilateral', 'sphinx unchanged'), ('Bilateral extension', 'spring + · both sulci shallow')])],
  dyn=dyn)
