# Bacterial Gene Transfer in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A donor and a recipient bacterium side by side, each with its chromosome; a `one` switch runs one route and the DNA moves:
# transformation (a lysed donor's naked fragments taken up by a competent cell — DNase blocks it), conjugation F⁺ × F⁻ (one
# plasmid strand across a sex-pilus bridge) and Hfr (chromosomal genes dragged across), generalized and specialized
# transduction (a phage carrying any gene vs only the genes beside its prophage, with lysogenic conversion), and a transposon
# hopping from chromosome to plasmid. A toggle adds DNase. 4 readouts. Facts from the pinned cards; FA pages in `fa`.
# No new cards.
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

D = lambda *k: [f'gx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
DX, RX, CY = 700, 1700, 640
def cell(x, lab, when=None, unless=None, lysed=False):
    st = 'stroke-dasharray:14 10;' if lysed else ''
    add(f'<rect x="{x - 300}" y="{CY - 200}" width="600" height="400" rx="200" style="fill:var(--dk2);fill-opacity:.07;stroke:var(--dk2);stroke-width:5;{st}"/>', when=when, unless=unless)
    text(lab, x, CY - 230, 'nf-l1', 'middle', when=when, unless=unless)

text('Bacterial gene transfer — four ways DNA moves between bacteria', 180, 150, 'dyn-big')
text('blue loop = chromosome · small ring = plasmid · red = the gene that moves', 180, 176, 'dyn-cap')
cell(DX, 'Donor', unless=D('tf')); cell(DX, 'Donor — lysed', when=D('tf'), lysed=True)
cell(RX, 'Recipient')
for x in (DX, RX):
    add(f'<ellipse cx="{x}" cy="{CY}" rx="180" ry="110" style="fill:none;stroke:var(--dk1);stroke-width:6"/>')
add(f'<path d="M{DX - 40} {CY - 110} a40 30 0 0 0 80 0" style="fill:none;stroke:var(--bad);stroke-width:10"/>')
text('gene', DX, CY - 140, 'nf-l2', 'middle')
# F plasmid in donor
add(f'<circle cx="{DX + 200}" cy="{CY + 120}" r="40" style="fill:none;stroke:var(--dk4);stroke-width:6"/>', when=D('f', 'tn'))
text('F plasmid', DX + 200, CY + 190, 'nf-l2', 'middle', when=D('f'))
add(f'<circle cx="{RX - 200}" cy="{CY + 120}" r="40" style="fill:none;stroke:var(--dk4);stroke-width:6;stroke-dasharray:8 6"/>', when=D('f'))
text('recipient becomes F⁺', RX - 200, CY + 190, 'nf-l1 dyn-tag', 'middle', when=D('f'))
add(f'<path d="M{DX + 180} {CY - 110} a30 20 0 0 0 60 0" style="fill:none;stroke:var(--dk4);stroke-width:10"/>', when=D('hfr'))
text('F integrated (Hfr)', DX + 210, CY - 150, 'nf-l2', 'middle', when=D('hfr'))
text('recipient stays F⁻ but gains chromosomal genes', RX, CY + 260, 'nf-l1 dyn-tag', 'middle', when=D('hfr'))
# pilus
add(f'<path d="M{DX + 300} {CY} H{RX - 300}" style="stroke:var(--dk4);stroke-width:14;opacity:.5"/>', when=D('f', 'hfr'))
text('sex pilus — mating bridge (live contact)', 1200, CY - 30, 'nf-l2', 'middle', when=D('f', 'hfr'))
# phage
def phage(x, y, when): add(f'<path d="M{x} {y} l30 -30 l30 30 l-30 30 z M{x + 30} {y + 30} v60 M{x + 10} {y + 90} l20 -20 l20 20" style="fill:var(--dk7);fill-opacity:.3;stroke:var(--dk7);stroke-width:4"/>', when=when)
phage(1170, 380, D('gen', 'spec'))
add(f'<path d="M{DX - 220} {CY + 20} a40 25 0 0 0 80 0" style="fill:none;stroke:var(--dk7);stroke-width:10"/>', when=D('spec'))
text('prophage (lysogenic)', DX - 180, CY + 80, 'nf-l2', 'middle', when=D('spec'))
text('generalized: a lytic phage packs ANY piece of host DNA by mistake', 1200, 300, 'nf-l1 dyn-tag', 'middle', when=D('gen'))
text('specialized: the prophage excises and takes only its neighbors', 1200, 300, 'nf-l1 dyn-tag', 'middle', when=D('spec'))
text('naked DNA fragments taken up by a competent cell — SHiN', 1200, 300, 'nf-l1 dyn-tag', 'middle', when=D('tf'))
add(X(1200, CY, 26), when=['gx:tf&dnase'])
text('DNase destroys free DNA — transformation blocked', 1200, CY + 60, 'nf-l1 dyn-tag', 'middle', when=['gx:tf&dnase'])
text('DNase does nothing — the DNA never leaves a cell or capsid', 1200, CY + 60, 'nf-l1 dyn-tag', 'middle', when=['dnase&!gx:tf'])
# transposon
add(f'<rect x="{DX + 100}" y="{CY + 60}" width="60" height="20" rx="6" style="fill:var(--bad)"/>', when=D('tn'))
text('transposase cuts or copies it into the plasmid — then the plasmid travels', 1200, 300, 'nf-l1 dyn-tag', 'middle', when=D('tn'))
EX = dict(tf='S. pneumoniae, H. influenzae type b, Neisseria — capsule and resistance genes', f='R plasmids spread β-lactamases, ESBLs, carbapenemases',
          hfr='Hfr: chromosomal genes beside the integrated F', gen='any bacterial gene can be carried',
          spec='lysogenic conversion — ABCD’S toxins: strep erythrogenic, botulinum, cholera, diphtheria, Shiga',
          tn='vanA on Tn1546 moved from Enterococcus into S. aureus — VRSA')
for k, t in EX.items(): text(t, 1200, 1060, 'nf-l1', 'middle', when=D(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d=f'M{DX} {CY - 110} C{DX + 300} {CY - 400} {RX - 300} {CY - 400} {RX} {CY - 110}', len=1300, speed=200, r=10, base=dict(dna=4),
       when=D('tf'), mods=[m(['dnase'], set=dict(dna=0))]),
  dict(d=f'M{DX + 240} {CY + 120} C{DX + 400} {CY + 40} {DX + 400} {CY} {DX + 300} {CY} H{RX - 300} C{RX - 260} {CY + 60} {RX - 240} {CY + 100} {RX - 240} {CY + 120}', len=1300, speed=200, r=9,
       base=dict(pl=4), when=D('f')),
  dict(d=f'M{DX + 210} {CY - 110} C{DX + 300} {CY - 60} {DX + 300} {CY} {DX + 320} {CY} H{RX - 300} C{RX - 200} {CY} {RX - 180} {CY - 60} {RX - 120} {CY - 100}', len=1200, speed=180, r=9,
       base=dict(dna=4), when=D('hfr')),
  dict(d=f'M{DX} {CY - 110} C{DX + 200} {CY - 300} 1000 {CY - 260} 1170 410 C1400 {CY - 260} {RX - 200} {CY - 300} {RX} {CY - 110}', len=1400, speed=200, r=10,
       base=dict(dna=3), when=D('gen')),
  dict(d=f'M{DX - 180} {CY + 20} C{DX - 100} {CY - 300} 1000 {CY - 300} 1170 410 C1400 {CY - 260} {RX - 200} {CY - 300} {RX} {CY - 110}', len=1500, speed=200, r=10,
       base=dict(dna=3), when=D('spec')),
  dict(d=f'M{DX + 130} {CY + 60} C{DX + 160} {CY + 100} {DX + 180} {CY + 110} {DX + 200} {CY + 120}', len=110, speed=40, r=9, base=dict(dna=2), when=D('tn')),
]
sites = [dict(x=DX, y=CY + 200, n=[0, 1], w=10, t='rec', l='', aria='Transformation', c='transform', ions=[]),
         dict(x=1200, y=CY, n=[0, 1], w=10, t='rec', l='', aria='Conjugation', c='conjugation', ions=[]),
         dict(x=1320, y=470, n=[1, 0], w=10, t='rec', l='', aria='Transduction', c='transduction', ions=[]),
         dict(x=RX, y=CY + 200, n=[0, 1], w=10, t='rec', l='', aria='Transposons', c='transposon', ions=[])]

readouts = [
  dict(l='Needs cell contact', mods=[dict(when=D('f', 'hfr'), d=1), dict(when=D('tf', 'gen', 'spec'), d=-1)]),
  dict(l='Blocked by DNase', mods=[dict(when=D('tf'), d=1), dict(when=D('f', 'hfr', 'gen', 'spec'), d=-1)]),
  dict(l='Phage needed', mods=[dict(when=D('gen', 'spec'), d=1), dict(when=D('tf', 'f', 'hfr'), d=-1)]),
  dict(l='Recipient becomes F⁺', mods=[dict(when=D('f'), d=1), dict(when=D('hfr'), d=-1)]),
]

notes = {
  '': 'Bacteria swap genes horizontally — how antibiotic resistance and toxin genes spread. Transformation takes up free DNA, conjugation '
      'passes it across a pilus, transduction carries it in a phage, and transposons move genes between molecules inside one cell.',
  'gx:tf': 'Transformation: a lysed cell spills naked DNA fragments; a competent cell (S. pneumoniae, H. influenzae type b, Neisseria — SHiN) '
           'binds them, pulls one strand in and recombines it. No contact, no phage — DNase blocks it.',
  'gx:f': 'Conjugation F⁺ × F⁻: the F plasmid codes for a sex pilus; one plasmid strand is copied across the bridge — the recipient becomes '
          'F⁺, no chromosomal DNA moves. The main route for spreading R plasmids.',
  'gx:hfr': 'Hfr × F⁻: with F integrated in the chromosome, the leading part drags flanking chromosomal genes across; the recipient stays F⁻.',
  'gx:gen': 'Generalized transduction: a lytic phage packs a piece of host chromosome by mistake — any gene can travel.',
  'gx:spec': 'Specialized transduction: a lysogenic prophage excises imprecisely and takes its neighboring genes — lysogenic conversion '
             'gives toxin genes (ABCD’S: erythrogenic, botulinum, cholera, diphtheria, Shiga).',
  'gx:tn': 'Transposons: transposase cuts or copies the element into another molecule (chromosome → plasmid); to leave the cell it rides a '
           'plasmid or phage. vanA (Tn1546) moved from Enterococcus into S. aureus.',
  'dnase': 'DNase destroys free DNA — it blocks transformation only.',
}

dyn = dict(
  kinds=dict(dna=['dna', '--bad'], pl=['dna', '--dk4']), groups=[['dna', 'DNA moving']],
  switches=[dict(id='gx', label='Route', type='one', options=[
              ['tf', 'Transformation', 'transform'], ['f', 'Conjugation F⁺ × F⁻', 'conjugation'], ['hfr', 'Conjugation Hfr', 'conjugation'],
              ['gen', 'Generalized transduction', 'transduction'], ['spec', 'Specialized transduction', 'transduction'], ['tn', 'Transposon', 'transposon']]),
            dict(id='dnase', label='Test', type='toggle', on='DNase added', off='Add DNase', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 128–129 · Robbins ch 8')
dyn['switches'][1]['def'] = dyn['switches'][1].pop('def_')

MAP = dict(
  id='gxsim', title='Bacterial Gene Transfer in Motion', topic='id', after='microlab',
  sub='Watch DNA move between bacteria — transformation of naked DNA, conjugation across a pilus (F⁺ and Hfr), generalized and specialized '
      'transduction by phage, and a transposon jumping onto a plasmid — and see which one DNase blocks',
  w=3600, h=1900,
  fa='128, 129',
  src=['Robbins ch 8 — Infectious diseases', 'Marks ch 16 — Use of Recombinant DNA Techniques in Medicine',
       'Katzung ch 43 — Beta-Lactam & Other Cell Wall- & Membrane-Active Antibiotics', 'Marks ch 14 — Translation: Synthesis of Proteins',
       'Marks ch 12 — Synthesis of DNA'],
  lanes=[('gxMov', 'Between cells', 'glycolysis'), ('gxIn', 'Within a cell', 'tca')],
  nodes=[
    ('gx1', 'Transformation', 330, 1660, 'gxMov', 'naked DNA · SHiN', ['transform'], 'hub'),
    ('gx2', 'Conjugation', 760, 1660, 'gxMov', 'F plasmid · Hfr', ['conjugation']),
    ('gx3', 'Transduction', 1200, 1660, 'gxMov', 'generalized vs specialized', ['transduction']),
    ('gx4', 'Transposons', 1640, 1660, 'gxIn', 'jumping genes · vanA', ['transposon'])],
  panels=[
    (2500, PANY, 1000, 'Which route? (First Aid p. 128)', [
      ('Free DNA, DNase-sensitive', 'transformation'), ('Cell contact, pilus', 'conjugation'),
      ('Phage, any gene', 'generalized transduction'), ('Phage, neighboring genes', 'specialized transduction'),
      ('Within one cell', 'transposon')])],
  dyn=dyn)
