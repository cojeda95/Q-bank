# Low Back Pain in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A lumbar spine from the side (L1–L5, discs, canal, a nerve root, sacrum) beside a pelvis-and-legs view from behind, with
# the root signal and the posture moving. A `pos` switch (steps, auto) flexes, holds neutral and extends; a `one` switch
# shows disc herniation (protrusion → extrusion), spinal stenosis (worse in extension), spondylolysis/listhesis, psoas
# syndrome (L1/L2 FRS key lesion), short leg syndrome and iliolumbar ligament syndrome, each with the OMT the card gives.
# 4 readouts. Facts from the pinned cards (Foundations ch 42, 93; OCOM OMM); no First Aid pages. No new cards.
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
P = lambda *k: [f'pos:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'

text('Low back pain — what moves, what pinches, what to avoid', 180, 150, 'dyn-big')
text('left: lumbar spine from the side (front = left) · right: pelvis and legs from behind', 180, 176, 'dyn-cap')

# ════════ lumbar spine, side view ════════
LV = ['L1', 'L2', 'L3', 'L4', 'L5']
Y0, DY, BX = 320, 170, 700
def spine(tilt, when=None, unless=None, slip=False):
    out = []
    for i, lv in enumerate(LV):
        y = Y0 + i * DY; dx = round(tilt * (i - 2))
        sx = 40 if (slip and lv == 'L5') else 0
        out.append(f'<rect x="{BX - 110 + dx - sx}" y="{y}" width="220" height="110" rx="16" style="fill:var(--dk10);fill-opacity:.2;stroke:var(--dk10);stroke-width:4"/>')
        out.append(f'<rect x="{BX + 150 + dx - sx}" y="{y + 20}" width="70" height="70" rx="12" style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:3"/>')
        if i < 4: out.append(f'<rect x="{BX - 100 + dx}" y="{y + 115}" width="200" height="50" rx="20" style="fill:var(--dk7);fill-opacity:.3"/>')
    add(''.join(out), when=when, unless=unless)
spine(0, unless=P('flex', 'ext') + D('spondy'))
spine(-14, when=['pos:flex&!dx:spondy'])
spine(14, when=['pos:ext&!dx:spondy'])
spine(0, when=D('spondy'), slip=True)
for i, lv in enumerate(LV): text(lv, BX - 150, Y0 + i * DY + 62, 'nf-l1', 'end')
add(f'<path d="M{BX + 120} {Y0} V{Y0 + 5 * DY}" style="stroke:var(--nf-h2o);stroke-width:26;opacity:.35"/>', unless=['dx:sten&pos:ext'])
add(f'<path d="M{BX + 120} {Y0} V{Y0 + 5 * DY}" style="stroke:var(--nf-h2o);stroke-width:8;opacity:.5"/>', when=['dx:sten&pos:ext'])
add(f'<path d="M{BX + 120} {Y0} V{Y0 + 5 * DY}" style="stroke:var(--nf-h2o);stroke-width:16;opacity:.45"/>', when=['dx:sten&!pos:ext'])
text('canal', BX + 120, Y0 - 20, 'nf-l2', 'middle')
add(f'<rect x="{BX - 140}" y="{Y0 + 5 * DY + 10}" width="380" height="140" rx="40" style="fill:var(--dk10);fill-opacity:.12;stroke:var(--dk10);stroke-width:4"/>')
text('sacrum', BX + 50, Y0 + 5 * DY + 90, 'nf-l1', 'middle')
# root
RY = Y0 + 3 * DY + 140
add(f'<path d="M{BX + 120} {RY} C{BX + 200} {RY + 40} {BX + 260} {RY + 160} {BX + 320} {RY + 300}" style="fill:none;stroke:var(--dk2);stroke-width:8"/>')
text('nerve root', BX + 330, RY + 330, 'nf-l2')
add(f'<path d="M{BX + 100} {RY} q40 -10 60 20 q-10 30 -60 20 z" style="fill:var(--dk7);fill-opacity:.6;stroke:var(--bad);stroke-width:4"/>', when=D('disc'))
text('posterolateral herniation compresses the root', 1250, 300, 'nf-l1 dyn-tag', 'middle', when=D('disc'))
text('canal narrows further in extension — neurogenic claudication', 1250, 300, 'nf-l1 dyn-tag', 'middle', when=D('sten'))
add(X(BX + 180, Y0 + 4 * DY + 55, 14), when=D('spondy'))
text('L5 pars fracture → forward slip; palpable step-off', 1250, 300, 'nf-l1 dyn-tag', 'middle', when=D('spondy'))
add(f'<path d="M{BX - 110} {Y0 + 40} C{BX - 300} {Y0 + 300} {BX - 300} {Y0 + 700} {BX - 160} {Y0 + 900}" style="fill:none;stroke:var(--bad);stroke-width:14;opacity:.6"/>', when=D('psoas'))
text('iliopsoas spasm', BX - 330, Y0 + 500, 'nf-l1 dyn-tag', 'end', when=D('psoas'))
text('L1/L2 Type II FRS toward the tight psoas — the key lesion', 1250, 300, 'nf-l1 dyn-tag', 'middle', when=D('psoas'))

# ════════ pelvis and legs from behind ════════
PX, PY = 1700, 760
tilt = dict(lld=-8, psoas=6)
def pelvis(rot, when=None, unless=None):
    add(f'<g transform="rotate({rot} {PX} {PY})"><path d="M{PX - 300} {PY - 80} C{PX - 340} {PY + 80} {PX - 160} {PY + 160} {PX} {PY + 160} C{PX + 160} {PY + 160} {PX + 340} {PY + 80} {PX + 300} {PY - 80} Z" '
        f'style="fill:var(--dk10);fill-opacity:.15;stroke:var(--dk10);stroke-width:4"/>'
        f'<path d="M{PX - 60} {PY - 120} L{PX + 60} {PY - 120} L{PX + 20} {PY + 120} L{PX - 20} {PY + 120} Z" style="fill:var(--dk7);fill-opacity:.25;stroke:var(--dk7);stroke-width:3"/></g>', when=when, unless=unless)
pelvis(0, unless=D('lld', 'psoas'))
pelvis(-6, when=D('lld')); pelvis(5, when=D('psoas'))
add(f'<path d="M{PX - 180} {PY + 140} V{PY + 600} M{PX + 180} {PY + 140} V{PY + 600}" style="stroke:var(--dk10);stroke-width:40;opacity:.35;stroke-linecap:round"/>', unless=D('lld'))
add(f'<path d="M{PX - 180} {PY + 140} V{PY + 600} M{PX + 180} {PY + 180} V{PY + 600}" style="stroke:var(--dk10);stroke-width:40;opacity:.35;stroke-linecap:round"/>', when=D('lld'))
text('left', PX - 180, PY + 650, 'nf-l1', 'middle'); text('right', PX + 180, PY + 650, 'nf-l1', 'middle')
text('right leg short → sacral base tilts, the spine compensates', PX, PY - 240, 'nf-l1 dyn-tag', 'middle', when=D('lld'))
add(f'<circle cx="{PX - 260}" cy="{PY - 140}" r="26" style="fill:var(--bad);fill-opacity:.5"/>', when=D('ilio'))
text('tender ~1 inch above and lateral to the PSIS · refers to groin, trochanter', PX, PY - 240, 'nf-l1 dyn-tag', 'middle', when=D('ilio'))
text('list toward the tight psoas, pelvis shifts away', PX, PY - 240, 'nf-l1 dyn-tag', 'middle', when=D('psoas'))
add(f'<path d="M{PX - 100} {PY - 400} V{PY - 160}" style="stroke:var(--dk10);stroke-width:30;opacity:.3"/>', unless=D('lld', 'psoas'))
add(f'<path d="M{PX - 100} {PY - 400} C{PX - 60} {PY - 300} {PX - 140} {PY - 220} {PX - 100} {PY - 160}" style="fill:none;stroke:var(--dk10);stroke-width:30;opacity:.3"/>', when=D('lld', 'psoas'))
TX = dict(disc='no HVLA at that level with radiculopathy — counterstrain for the protective spasm',
          sten='avoid forcing extension; release the psoas', spondy='no HVLA at the unstable level; indirect OMT above and below; TLSO brace',
          psoas='release L1/L2 first (HVLA or MET), counterstrain psoas and iliacus, then the pelvis; cold, not heat',
          lld='OMT to maximize compensation, then a heel lift', ilio='counterstrain first; treat L5 and pelvic shears')
for k, t in TX.items(): text('OMT: ' + t, 1300, 1480, 'nf-l1', 'middle', when=D(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{BX + 120} {RY} C{BX + 200} {RY + 40} {BX + 260} {RY + 160} {BX + 320} {RY + 300}', len=360, speed=90, r=8, base=dict(sig=2),
       mods=[m(D('disc') + ['dx:sten&pos:ext'], set=dict(pain=5, sig=0))]),
  dict(d=f'M{BX + 120} {RY} C{BX + 200} {RY + 40} {BX + 260} {RY + 160} {BX + 320} {RY + 300}', len=360, speed=140, r=8, base=dict(pain=4),
       when=D('disc') + ['dx:sten&pos:ext']),
  dict(d=f'M{PX + 180} {PY + 600} V{PY + 180}', len=420, speed=80, r=9, base=dict(load=3), when=D('lld')),
]
sites = [dict(x=BX, y=Y0 + 3 * DY + 140, n=[-1, 0], w=10, t='rec', l='', aria='Disc herniation', c='discdz', ions=[]),
         dict(x=BX + 120, y=Y0 - 50, n=[0, -1], w=10, t='rec', l='', aria='Spinal stenosis', c='spinalstenosis', ions=[]),
         dict(x=BX - 110, y=Y0 + 55, n=[-1, 0], w=10, t='rec', l='', aria='Psoas syndrome', c='psoassyn', ions=[]),
         dict(x=PX, y=PY + 160, n=[0, 1], w=10, t='rec', l='', aria='Short leg syndrome', c='lld', ions=[])]

readouts = [
  dict(l='Leg pain', mods=[dict(when=D('disc') + ['dx:sten&pos:ext'], d=1), dict(when=['dx:sten&pos:flex'], d=-1)]),
  dict(l='HVLA at that level OK', mods=[dict(when=D('disc', 'spondy', 'sten'), d=-1), dict(when=D('psoas'), d=1)]),
  dict(l='Lordosis', mods=[dict(when=D('spondy'), d=1), dict(when=D('disc', 'sten'), d=-1)]),
  dict(l='Hamstrings tight', mods=[dict(when=D('disc', 'spondy', 'psoas'), d=1)]),
]

notes = {
  '': 'The lumbar spine flexes and extends over the sacrum; the canal and the exiting roots change size with posture. Each low back '
      'syndrome has a posture that worsens it and a technique to avoid.',
  'pos:flex': 'Flexion — bending forward relieves stenosis symptoms.', 'pos:ext': 'Extension — the canal narrows further.',
  'dx:disc': 'Disc herniation: protrusion (annulus intact) → extrusion (nucleus through a torn annulus) → sequestration. Posterolateral is '
             'commonest and hits a root. Flattened lordosis, tight hamstrings. No HVLA at that level with radiculopathy.',
  'dx:sten': 'Lumbar spinal stenosis: the canal narrows further in extension — neurogenic claudication, relieved by sitting or bending '
             'forward; positive Kemp sign. Avoid forcing extension.',
  'dx:spondy': 'Spondylolysis: pars stress fracture, L5 in ~95%; spondylolisthesis: forward slip — step-off, hyperlordosis, tight '
               'hamstrings, pain with extension. No HVLA at the unstable level.',
  'dx:psoas': 'Psoas syndrome: iliopsoas spasm flexes the lumbar spine; L1/L2 holds a Type II FRS toward the tight psoas — release it first '
              'or the findings recur. List toward the psoas, pelvic shift away.',
  'dx:lld': 'Short leg syndrome: anatomic or functional leg-length difference tilts the sacral base; pain worse as the day goes on. '
            'Maximize compensation with OMT, then a heel lift.',
  'dx:ilio': 'Iliolumbar ligament syndrome: strain from a short leg or microtrauma — exquisite tenderness ~1 inch superior and lateral to '
             'the PSIS, referring to the groin or trochanter.',
}

dyn = dict(
  kinds=dict(sig=['nerve', '--dk2'], pain=['nerve', '--bad'], load=['nerve', '--dk4']), groups=[['nerve', 'Root signal · load']],
  switches=[dict(id='pos', label='Posture', type='steps', auto=3, options=[['flex', 'Flexion'], ['neut', 'Neutral'], ['ext', 'Extension']]),
            dict(id='dx', label='Syndrome', type='one', options=[
              ['disc', 'Disc herniation', 'discdz'], ['sten', 'Spinal stenosis', 'spinalstenosis'], ['spondy', 'Spondylolisthesis', 'spondy'],
              ['psoas', 'Psoas syndrome', 'psoassyn'], ['lld', 'Short leg syndrome', 'lld'], ['ilio', 'Iliolumbar ligament', 'iliolumbar']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Foundations of Osteopathic Medicine ch 42, 93 · OCOM OMM')

MAP = dict(
  id='lbpsim', title='Low Back Pain in Motion', topic='omm', after='lbp',
  sub='Flex and extend the lumbar spine and watch the canal and root respond — disc herniation, spinal stenosis, spondylolisthesis, psoas '
      'syndrome, short leg and iliolumbar ligament syndrome, each with the technique to use and the one to avoid',
  w=3600, h=1900,
  fa='',
  src=['OCOM OMM — OMS2 written midterm study guide', 'Foundations of Osteopathic Medicine ch 93 — Osteopathic Considerations in the Patient With Low Back Pain',
       'Foundations of Osteopathic Medicine (4e) ch 42 — Acute Low Back Pain'],
  lanes=[('lbSpine', 'Spine', 'glycolysis'), ('lbPelv', 'Muscle & pelvis', 'tca')],
  nodes=[
    ('lb1', 'Disc herniation', 330, 1660, 'lbSpine', 'posterolateral', ['discdz'], 'hub'),
    ('lb2', 'Spinal stenosis', 760, 1660, 'lbSpine', 'worse in extension', ['spinalstenosis']),
    ('lb3', 'Spondylolisthesis', 1200, 1660, 'lbSpine', 'L5 pars', ['spondy']),
    ('lb4', 'Psoas syndrome', 330, 1790, 'lbPelv', 'L1/L2 key lesion', ['psoassyn']),
    ('lb5', 'Short leg syndrome', 760, 1790, 'lbPelv', 'heel lift', ['lld']),
    ('lb6', 'Iliolumbar ligament', 1200, 1790, 'lbPelv', 'above the PSIS', ['iliolumbar'])],
  panels=[
    (2500, PANY, 1000, 'Better or worse?', [
      ('Stenosis', 'worse extending, better bending forward'), ('Spondylolisthesis', 'worse with extension'),
      ('Degenerative disc', 'worse sitting/standing, better moving'), ('Short leg', 'worse as the day goes on')])],
  dyn=dyn)
