# m57 — Liver Lobule & Sinusoid in Motion (dynamic map, kit data)
# Left: one classic lobule — a hexagon of one-cell-thick hepatocyte plates radiating from the central vein, a portal triad
# (portal vein, hepatic artery, bile duct) at each corner; blood runs inward along the sinusoids, bile outward in the plates.
# Right: the boxed spot magnified — two hepatocyte plates with a bile canaliculus between neighbouring cells, the space of
# Disse with microvilli and a stellate (Ito) cell, the fenestrated endothelium, a Kupffer cell built into the lining, and the
# sinusoid lumen with red cells and gut bacteria. Below: the blood path (triad → sinusoid → central vein → … → IVC) and the
# bile path (canaliculus → canal of Hering → ductule → interlobular duct). One `one` switch, "Look at one part", in three
# sections plus injury, lights one part, changes its traffic, and reads out six arrows. Zones 1–3 stay on `portsim`
# (Liver Blood Flow in Motion) — not duplicated here.
#
# Sources (all read in the corpus; the course text wins for this block):
#   Course (SDL 2/3/12/13 histology, Pawlina ch 18 printout, corpus/gastro/course_sdl_2_3_12_13_histo_foreguy_p3.txt,
#     printout pp. 11–55): dual supply, portal vein about 75% / hepatic artery the remaining 25%, mixing before the
#     hepatocytes; portal triad = portal vein + hepatic artery + bile duct, a misnomer because lymphatics always travel with
#     it; nerves ramify in the portal canals with the triad; classic lobule, plates one cell thick (two cells thick up to
#     age 6), central vein = terminal hepatic venule → sublobular veins → hepatic veins → IVC; sublobular and hepatic veins
#     travel alone, no valves; blood centripetal, bile centrifugal; discontinuous endothelium: large fenestrae without
#     diaphragms, large gaps, basal lamina absent over large areas; Kupffer cells part of the lining, no junctions with
#     endothelium, ~15% of liver cells, 80–90% of the body's tissue macrophages, first line vs microorganisms and endotoxin
#     from portal blood (PRRs, TLRs), remove damaged/senescent RBCs and recover iron (ferritin, ferroportin → transferrin);
#     space of Disse between endothelium/Kupffer cells and hepatocytes, microvilli raise surface up to 6×, the site of
#     exchange, proteins and lipoproteins enter blood here — the route for secretions other than bile; hepatic lymph starts
#     in Disse → space of Mall → lymphatics of the triad; stellate (Ito) cells: mesenchymal, main hepatic vitamin A store
#     as retinyl esters in lipid droplets, release retinol bound to RBP; in chronic inflammation/cirrhosis they lose vitamin
#     A storage, become myofibroblasts (desmin, smooth muscle α-actin), deposit type I and III collagen in Disse; their
#     contraction raises sinusoid resistance → portal hypertension; hepatocytes ~80% of liver cells, life span ~5 months,
#     regenerate; surfaces facing Disse = basal, facing canaliculi = apical; canaliculi = grooves of adjacent hepatocytes
#     sealed by tight junctions (+ zonulae adherentes, desmosomes) → canals of Hering (hepatocytes + cholangiocytes) →
#     bile ductules → interlobular bile ducts of the triad.
#   Course (SDL 15/19 pathology, Robbins ch 18 printout, course_sdl_15_19_patho.txt pp. 3–9): fenestrated endothelium,
#     Kupffer cells, lipid-containing stellate cells in Disse, canaliculi sealed by tight junctions → canals of Hering →
#     ductules → interlobular ducts; ALP and GGT = canalicular membrane enzymes, ↑; stellate cells the principal scar
#     cell: quiescent = vitamin A storage; activated by TNF-α (Kupffer cells), PDGF, TGF-β → myofibroblasts; matrix in
#     the space of Disse with loss of fenestration = sinusoidal capillarization; septa + regenerative nodules = cirrhosis.
#   Course (SDL 19, Robbins ch 19 printout, course_sdl_19_patho.txt p. 13): TGF-β and PDGF activate pancreatic stellate
#     cells (periacinar myofibroblasts) → collagen, fibrosis in chronic pancreatitis.
#   Course (Guyton ch 71 supplement, course_sdl_4_7_14_guyton_spplemental_p6.txt pp. 3, 6): pores almost 1 µm; plasma —
#     even plasma proteins — moves freely into Disse; Disse drains to lymphatics; Kupffer cells: < 1% of portal bacteria
#     pass the liver.
#   First Aid 2025 p. 374 (lobule, triad incl. lymphatics, apical surface → canaliculi, basolateral → sinusoids, Kupffer
#     cells clear bacteria and damaged/senescent RBCs, stellate cells store vitamin A when quiescent and make ECM when
#     activated; portal ~80% — the course's 75% wins, shown as "about 75% (First Aid: 80%)") · p. 396 (cirrhosis: bridging
#     fibrosis via stellate cells, regenerative nodules) · p. 397 (ALP, GGT in the canalicular membrane) · p. 401 (sinusoid,
#     Disse, Kupffer cell, conjugated bilirubin → canalicular lumen) · p. 413 (Kupffer cells = liver macrophages).
#   Course (GI Exam 1 lecture notes, corpus/gastro/course_exam1_lecture_notes.txt, SDL 12 pp. 66–69 and SDL 15): every
#     fact above re-checked against it — portal vein ~70–75%, hepatic artery ~25–30%; Kupffer cells "attached to the
#     luminal face or incorporated into the lining"; TNF-α, TGF-β (ROS) from activated Kupffer cells and injured
#     hepatocytes activate stellate cells, PDGF drives proliferation; collagen I/III in Disse → loss of fenestrae
#     (capillarization); α-smooth muscle actin constricts sinusoids → portal hypertension; canaliculi 0.5–1 µm.
# Source conflicts (course wins): portal share 70–75% (lecture notes; Pawlina 75%) vs 80% (FA 374). Kupffer cells "form part of the lining"
#   (Pawlina) vs "attached to the luminal face of endothelial cells" (Robbins); the lecture notes give both — written as
#   "on or built into the lining", drawn in the lining.
#   Canaliculus diameter 0.5 µm (Pawlina) vs 1–2 µm (Robbins) — no number shown.
# Cut for lack of a stated direction: "plasma ↔ hepatocyte exchange ↓" in fibrosis (sdl12_q24's explanation says
#   capillarization blocks it, but no corpus source — lecture notes included — states the consequence — readout left "–", the motion only thins the
#   crossing at the closed fenestrae); collagen in Disse for quiescent stellate cells (Pawlina mentions sparse fibers — no
#   arrow); zone 1–3 injury patterns (on portsim).
# m58 pins (P10): "Classic hepatic lobule" and "Liver acinus" options in "Blood in & out" (Pawlina ch 18 in the course text,
#   course_sdl_2_3_12_13_histo_foreguy_p3.txt pp. 14–22: three descriptions — classic lobule, portal lobule, liver acinus;
#   classic lobule roughly hexagonal around the terminal hepatic venule with portal canals at the angles; acinus lozenge
#   shaped, smallest functional unit, short axis = terminal triad branches on the border of two classic lobules, long axis =
#   the two nearest central veins, zones 1–3 from the short axis). The far central vein is drawn closer than true scale.
#   No readout arrows. The optional "Canals of Hering" option was not added (no card, no gain).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

PW18, RB18, RB19, GY71 = full('Pawlina', 18), full('Robbins', 18), full('Robbins', 19), full('Guyton', 71)

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

O = lambda *k: [f'c:{x}' for x in k]
FIB = O('fib')

text('One liver lobule, and one sinusoid magnified', 160, 80, 'dyn-big')
text('blood runs in from the portal triads to the central vein · bile runs out the other way · the box is enlarged on the right',
     160, 104, 'dyn-cap')

# ════════ the classic lobule ════════
CX, CY, R = 660, 790, 420
def pol(r, a): return CX + r * math.cos(math.radians(a)), CY + r * math.sin(math.radians(a))
VERT = [pol(R, a) for a in range(0, 360, 60)]
HEX = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in VERT) + ' Z'
add(f'<path d="{HEX}" style="fill:var(--dk6);fill-opacity:.07;stroke:var(--ink-3);stroke-width:2.5;stroke-dasharray:9 7"/>')
# fibrous septa joining the triads (cirrhosis)
add(f'<path d="{HEX}" style="fill:none;stroke:var(--dk8);stroke-width:22;stroke-opacity:.55;stroke-linejoin:round"/>', when=FIB)
# hepatocyte plates (one cell thick) radiating from the central vein; sinusoids are the gaps between them
for a in range(15, 360, 30):
    x0, y0 = pol(62, a); x1, y1 = pol(368, a)
    add(f'<path d="M{x0:.0f} {y0:.0f} L{x1:.0f} {y1:.0f}" style="stroke:var(--dk6);stroke-width:30;stroke-opacity:.26;stroke-linecap:round"/>')
add(f'<g>' + ''.join(f'<path d="M{pol(62, a)[0]:.0f} {pol(62, a)[1]:.0f} L{pol(368, a)[0]:.0f} {pol(368, a)[1]:.0f}" class="dyn-hl" style="stroke-width:34;opacity:.35"/>'
                     for a in range(15, 360, 30)) + '</g>', when=O('plate'))
# central vein
add(f'<circle cx="{CX}" cy="{CY}" r="44" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:4"/>')
add(f'<circle cx="{CX}" cy="{CY}" r="62" class="dyn-hl"/>', when=O('cv'))
# portal triads at the six corners: portal vein (big, thin wall), hepatic artery (small, thick wall), bile duct (ring)
def triad(x, y):
    return (f'<circle cx="{x - 10:.0f}" cy="{y + 4:.0f}" r="21" style="fill:var(--dk9);fill-opacity:.4;stroke:var(--dk9);stroke-width:3"/>'
            f'<circle cx="{x + 18:.0f}" cy="{y - 16:.0f}" r="9" style="fill:var(--nf-blood);fill-opacity:.55;stroke:var(--nf-blood);stroke-width:4"/>'
            f'<circle cx="{x + 20:.0f}" cy="{y + 16:.0f}" r="9" style="fill:var(--surface);stroke:var(--dk5);stroke-width:5"/>')
for x, y in VERT:
    add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:2"/>' + triad(x, y))
    add(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="50" class="dyn-hl"/>', when=O('tri'))
# labels around the lobule
text('portal triad', VERT[5][0] + 40, VERT[5][1] - 52, 'nf-l1')
text('portal vein · hepatic artery · bile duct', VERT[5][0] + 40, VERT[5][1] - 34, 'nf-l2')
text('hepatocyte plates', VERT[4][0] - 40, VERT[4][1] - 52, 'nf-l1', 'end')
text('one cell thick, sinusoids between', VERT[4][0] - 40, VERT[4][1] - 34, 'nf-l2', 'end')
text('central vein', CX, 1262, 'nf-l1', 'middle')
text('(terminal hepatic venule)', CX, 1280, 'nf-l2', 'middle')
add(f'<path d="M{CX} {CY + 48} V1244" class="dyn-dash"/>')
text('classic lobule', VERT[3][0] - 10, VERT[3][1] - 60, 'nf-l1', 'start')
# m58: the classic lobule outlined, and one liver acinus (diamond: short axis = the triad-to-triad border, long axis = the two
# nearest central veins — the far one belongs to the next lobule, drawn schematically closer than it is)
add(f'<path d="{HEX}" style="fill:none;stroke:var(--accent);stroke-width:7;stroke-linejoin:round"/>', when=O('lob'))
FARCV = (CX, 200)
ACIN = f'M{VERT[4][0]:.0f} {VERT[4][1]:.0f} L{CX} {CY - 44} L{VERT[5][0]:.0f} {VERT[5][1]:.0f} L{FARCV[0]} {FARCV[1] + 30} Z'
add(f'<path d="{ACIN}" style="fill:var(--accent);fill-opacity:.12;stroke:var(--accent);stroke-width:6;stroke-linejoin:round"/>'
    f'<path d="M{VERT[4][0]:.0f} {VERT[4][1]:.0f} H{VERT[5][0]:.0f}" style="stroke:var(--accent);stroke-width:3;stroke-dasharray:8 6"/>'
    f'<circle cx="{FARCV[0]}" cy="{FARCV[1]}" r="30" style="fill:var(--nf-h2o);fill-opacity:.45;stroke:var(--nf-h2o);stroke-width:4"/>', when=O('acinus'))
for zy, zl in ((470, 'zone 1'), (590, 'zone 2'), (700, 'zone 3')):
    text(zl, CX + 24, zy, 'nf-l1', when=O('acinus'))
text('central vein of the next lobule', FARCV[0] + 44, FARCV[1] + 6, 'nf-l2', when=O('acinus'))
# the magnified spot (on the right side of the lobule) and its leader lines to the enlargement
BX, BY = pol(230, -15)
add(f'<rect x="{BX - 46:.0f}" y="{BY - 34:.0f}" width="92" height="68" rx="8" style="fill:none;stroke:var(--accent);stroke-width:3"/>')
add(f'<path d="M{BX + 46:.0f} {BY - 34:.0f} L1240 240 M{BX + 46:.0f} {BY + 34:.0f} L1240 1180" style="fill:none;stroke:var(--accent);stroke-width:1.5;stroke-dasharray:5 6;opacity:.7"/>')

# ════════ the magnified sinusoid ════════
ZX0, ZX1 = 1240, 2330
add(f'<rect x="{ZX0}" y="230" width="{ZX1 - ZX0}" height="950" rx="24" class="dyn-soft"/>')
text('the boxed spot, magnified', ZX0 + 30, 262, 'nf-l1')
text('two plates of hepatocytes with one sinusoid between them', ZX0 + 30, 280, 'nf-l2')
X0, X1 = 1290, 2290
# hepatocytes: upper plate (y 300–500), lower plate (y 890–1090); a bile canaliculus between neighbouring cells
UP, LO = (300, 500), (890, 1090)
CANX = 1790
for (y0, y1) in (UP, LO):
    for (a, b, off) in ((X0, CANX - 10, -60), (CANX + 10, X1, 110)):
        add(f'<rect x="{a}" y="{y0}" width="{b - a}" height="{y1 - y0}" rx="22" class="dyn-cell"/>')
        add(f'<circle cx="{(a + b) // 2 + off}" cy="{(y0 + y1) // 2}" r="34" style="fill:var(--dk6);fill-opacity:.18;stroke:var(--dk6);stroke-width:2.5"/>')
    add(f'<rect x="{X0 - 12}" y="{y0 - 12}" width="{X1 - X0 + 24}" height="{y1 - y0 + 24}" rx="28" class="dyn-hl"/>', when=O('plate'))
text('hepatocyte', 1640, 344, 'nf-l1', 'middle'); text('hepatocyte', 2150, 344, 'nf-l1', 'middle')
text('hepatocyte', 1640, 1050, 'nf-l1', 'middle'); text('hepatocyte', 2140, 1050, 'nf-l1', 'middle')
text('apical side → canaliculus · basal side → Disse', 1340, 470, 'nf-l2', when=O('plate'))
for cy in ((UP[0] + UP[1]) // 2, (LO[0] + LO[1]) // 2):
    add(f'<circle cx="{CANX}" cy="{cy}" r="15" style="fill:var(--dk5);fill-opacity:.25;stroke:var(--dk5);stroke-width:3"/>'
        f'<path d="M{CANX - 9} {cy - 26} h18 M{CANX - 9} {cy + 26} h18" style="stroke:var(--ink-2);stroke-width:4"/>')
    add(f'<circle cx="{CANX}" cy="{cy}" r="32" class="dyn-hl"/>', when=O('can'))
text('bile canaliculus', CANX + 44, 410, 'nf-l1')
text('sealed by tight junctions', CANX + 44, 428, 'nf-l2')
# microvilli into the space of Disse
add('<g>' + ''.join(f'<path d="M{x} 500 v26 M{x} 890 v-26" style="stroke:var(--dk6);stroke-width:3;opacity:.6"/>' for x in range(1310, 2290, 24)) + '</g>')
# space of Disse bands
for (y0, y1) in ((500, 572), (818, 890)):
    add(f'<rect x="{X0}" y="{y0}" width="{X1 - X0}" height="{y1 - y0}" style="fill:var(--nf-h2o);fill-opacity:.08"/>')
    add(f'<rect x="{X0 - 6}" y="{y0 - 4}" width="{X1 - X0 + 12}" height="{y1 - y0 + 8}" rx="10" class="dyn-hl"/>', when=O('disse'))
    # collagen (types I and III) laid down by activated stellate cells
    add('<g>' + ''.join(f'<path d="M{x} {y1 - 6} l26 {-(y1 - y0 - 18)}" style="stroke:var(--dk8);stroke-width:4;opacity:.75"/>' for x in range(1300, 2270, 22)) + '</g>', when=FIB)
text('space of Disse', 2140, 548, 'nf-l1', 'middle')
# endothelium: discontinuous — fenestrae (gaps) every 240 px; closed in capillarization
FEN = (1410, 1650, 1890, 2130)
def endo(y):
    xs = [X0] + [v for f in FEN for v in (f - 14, f + 14)] + [X1]
    return ''.join(f'<path d="M{a} {y} H{b}" style="stroke:var(--dk1);stroke-width:12;stroke-linecap:round"/>' for a, b in zip(xs[::2], xs[1::2]))
for y in (578, 812):
    add(endo(y))
    add(f'<path d="M{X0} {y} H{X1}" style="stroke:var(--dk1);stroke-width:12"/>', when=FIB)
    add(f'<path d="M{X0} {y} H{X1}" class="dyn-hl" style="stroke-width:24;opacity:.4"/>', when=O('endo'))
text('fenestrated endothelium', X0 + 20, 606, 'nf-l1')
text('fenestrae lost — sinusoidal capillarization', X0 + 230, 606, 'nf-l2 dyn-tag', when=FIB)
text('sinusoid: portal + arterial blood →', X0 + 20, 634, 'nf-l2')
text('to the central vein', X1 - 10, 640, 'nf-l2', 'end')
# Kupffer cell — part of the lower lining, processes reaching into the lumen
KX = 1990
KUP = f'M{KX - 90} 812 C{KX - 90} 786 {KX - 50} 766 {KX - 14} 760 L{KX + 6} 732 L{KX + 20} 760 C{KX + 60} 764 {KX + 96} 786 {KX + 92} 812 C{KX + 60} 842 {KX - 60} 842 {KX - 90} 812 Z'
add(f'<path d="{KUP}" style="fill:var(--dk11);fill-opacity:.28;stroke:var(--dk11);stroke-width:3"/><circle cx="{KX}" cy="790" r="18" style="fill:var(--dk11);fill-opacity:.4"/>')
add(f'<path d="{KUP}" class="dyn-hl"/>', when=O('kup'))
text('Kupffer cell', KX, 872, 'nf-l1', 'middle')
# stellate (Ito) cell in the lower space of Disse; quiescent = vitamin A droplets; activated = spindle myofibroblast
SX = 1530
add(f'<ellipse cx="{SX}" cy="852" rx="78" ry="24" style="fill:var(--dk10);fill-opacity:.22;stroke:var(--dk10);stroke-width:3"/>'
    + ''.join(f'<circle cx="{SX + dx}" cy="{852 + dy}" r="{r}" style="fill:var(--dk10);fill-opacity:.75"/>' for dx, dy, r in ((-44, 0, 11), (-18, -4, 13), (10, 4, 9), (34, -2, 10), (56, 2, 7))),
    unless=FIB)
add(f'<path d="M{SX - 150} 852 C{SX - 80} 836 {SX + 80} 836 {SX + 150} 852 C{SX + 80} 868 {SX - 80} 868 {SX - 150} 852 Z" style="fill:var(--dk8);fill-opacity:.35;stroke:var(--dk8);stroke-width:3"/>',
    when=FIB)
add(f'<ellipse cx="{SX}" cy="852" rx="100" ry="40" class="dyn-hl"/>', when=O('ito'))
add(f'<ellipse cx="{SX}" cy="852" rx="168" ry="34" class="dyn-hl"/>', when=FIB)
text('stellate (Ito) cell · vitamin A', SX, 796, 'nf-l2', 'middle', unless=FIB)
text('myofibroblast · collagen I + III', SX, 796, 'nf-l2', 'middle', when=FIB)
add(f'<path d="M{KX - 96} 830 C{KX - 200} 850 {SX + 260} 852 {SX + 172} 852" style="fill:none;stroke:var(--bad);stroke-width:3;stroke-dasharray:6 5" marker-end="url(#ah-lbDz)"/>', when=FIB)
text('TNF-α · TGF-β · PDGF', KX - 210, 760, 'nf-l2 dyn-tag', 'middle', when=FIB)

# ════════ the two paths ════════
def chain(y, title, items, hl):
    text(title, 160, y + 5, 'nf-l1')
    xs = [380, 720, 1060, 1400, 1740, 2080]
    for i, (lab, keys) in enumerate(items):
        x = xs[i]
        text(lab, x, y + 5, 'nf-l2', 'middle')
        if i < len(items) - 1: text('→', (x + xs[i + 1]) // 2, y + 5, 'nf-l2', 'middle')
        if keys:
            w = len(lab) * 7 + 30
            add(f'<rect x="{x - w / 2:.0f}" y="{y - 16}" width="{w:.0f}" height="30" rx="14" class="dyn-hl"/>', when=O(*keys))
chain(1360, 'Blood', [('portal vein + hepatic artery', ['tri']), ('sinusoids', ['endo', 'kup']), ('central vein', ['cv']),
                      ('sublobular veins', ['cv']), ('hepatic veins', ['cv']), ('inferior vena cava', ['cv'])], None)
chain(1420, 'Bile', [('hepatocyte', ['plate']), ('bile canaliculus', ['can']), ('canal of Hering', ['can']),
                     ('bile ductule', ['can']), ('interlobular bile duct', ['can', 'tri']), ('hepatic ducts', [])], None)
text('Plasma and secreted proteins cross the space of Disse; bile never enters the blood side — it leaves through the canaliculi.',
     160, 1472, 'dyn-cap')

TAG = dict(tri='portal triad — portal vein · hepatic artery · bile duct, plus lymphatics and nerves',
           cv='central vein → sublobular veins → hepatic veins → inferior vena cava',
           endo='sinusoidal endothelium — fenestrae without diaphragms, gaps, patchy basal lamina',
           disse='space of Disse — where plasma meets the hepatocyte; hepatic lymph starts here',
           kup='Kupffer cells — catch gut bacteria from portal blood, clear old red cells',
           ito='stellate (Ito) cells — vitamin A stored as retinyl esters in lipid droplets',
           plate='hepatocyte plates — one cell thick, a sinusoid on each side',
           can='bile canaliculi — bile flows outward, central vein → portal triad',
           fib='activated stellate cells → myofibroblasts: collagen in Disse, fenestrae lost, resistance up',
           acinus='liver acinus — a diamond across two lobules: triads on the short axis, central veins at the poles',
           lob='classic lobule — a hexagon: central vein in the middle, portal triads at the corners')
for k, s in TAG.items(): text(s, 160, 150, 'nf-l1 dyn-tag', when=O(k))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = []
for a in range(0, 360, 30):                       # blood: inward along every sinusoid
    r0 = 392 if a % 60 == 0 else 352
    x0, y0 = pol(r0, a); x1, y1 = pol(54, a)
    flows.append(dict(d=f'M{x0:.0f} {y0:.0f} L{x1:.0f} {y1:.0f}', len=r0 - 54, speed=70, r=6, base=dict(bl=2)))
for a in range(15, 360, 60):                      # bile: outward inside the plates
    x0, y0 = pol(70, a); x1, y1 = pol(366, a)
    flows.append(dict(d=f'M{x0:.0f} {y0:.0f} L{x1:.0f} {y1:.0f}', len=296, speed=50, r=5, base=dict(bile=1), mods=[m(O('can'), add=dict(bile=2))]))
flows += [
  dict(d=f'M{X0 + 10} 660 H{X1 - 10}', len=980, speed=120, r=10, base=dict(bl=5)),
  dict(d=f'M{X0 + 10} 730 H{X1 - 10}', len=980, speed=105, r=10, base=dict(bl=4)),
  # gut bacteria in portal blood, caught by the Kupffer cell
  dict(d=f'M{X0 + 10} 696 L{KX - 120} 700 Q{KX - 30} 704 {KX} 770', len=860, speed=110, r=7, base=dict(bact=2), mods=[m(O('kup'), add=dict(bact=2))]),
]
FENU = [dict(x=f, y=578, n=[0, -1], w=12, t='para', l='', aria='Fenestra — plasma into the space of Disse', c='liverzones',
             ions=[['pl', 'out', 1], ['prot', 'in', 1]], cross=True, reach=34, low=FIB, boost=O('endo', 'disse')) for f in FEN]
FENL = [dict(x=f, y=812, n=[0, 1], w=12, t='para', l='', aria='Fenestra — plasma into the space of Disse', c='liverzones',
             ions=[['pl', 'out', 1]], cross=True, reach=34, low=FIB, boost=O('endo', 'disse')) for f in (1410, 1650, 2190)]
sites = FENU + FENL + [
  dict(x=1530, y=500, n=[0, 1], w=8, t='ex', l='', aria='Hepatocyte secretes proteins into the space of Disse', c='liverzones',
       ions=[['prot', 'out', 1]], cross=True, reach=30, boost=O('disse', 'plate')),
  dict(x=2010, y=500, n=[0, 1], w=8, t='ex', l='', aria='Hepatocyte secretes lipoproteins into the space of Disse', c='liverzones',
       ions=[['prot', 'out', 1]], cross=True, reach=30, boost=O('disse', 'plate')),
  dict(x=CANX - 24, y=400, n=[1, 0], w=8, t='pump', l='', aria='Hepatocyte secretes bile into the canaliculus', c='bilicycle',
       ions=[['bile', 'out', 1]], cross=True, reach=14, boost=O('can')),
  dict(x=CANX + 24, y=990, n=[-1, 0], w=8, t='pump', l='', aria='Hepatocyte secretes bile into the canaliculus', c='bilicycle',
       ions=[['bile', 'out', 1]], cross=True, reach=14, boost=O('can')),
  dict(x=KX, y=812, n=[0, 1], w=10, t='rec', l='', aria='Kupffer cell', c='macrophage', ions=[], ),
  dict(x=SX, y=828, n=[0, 1], w=8, t='rec', l='', aria='Stellate (Ito) cell — vitamin A store', c='vitadef', ions=[], unless=FIB),
  dict(x=SX, y=828, n=[0, 1], w=8, t='rec', l='', aria='Activated stellate cell — fibrosis', c='cirrhosis', ions=[], when=FIB),
  dict(x=CX + 44, y=CY, n=[1, 0], w=8, t='rec', l='', aria='Central vein → hepatic veins → IVC', c='ivcanat', ions=[]),
  dict(x=VERT[5][0] - 40, y=VERT[5][1], n=[-1, 0], w=8, t='rec', l='', aria='Portal triad', c='giligaments', ions=[]),
]

# ════════ readouts ════════
R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Vitamin A stored', mods=[R(O('ito'), 1), R(FIB, -1)]),
  dict(l='Collagen in space of Disse', mods=[R(FIB, 1)]),
  dict(l='Sinusoid fenestrae', mods=[R(O('endo'), 1), R(FIB, -1)]),
  dict(l='Plasma ↔ hepatocyte exchange', mods=[R(O('disse'), 1)]),
  dict(l='Bacteria · old RBCs cleared', mods=[R(O('kup'), 1)]),
  dict(l='Sinusoid resistance', mods=[R(FIB, 1)]),
]

notes = {
  '': 'The classic lobule: one-cell-thick hepatocyte plates radiate from the central vein, with a portal triad at each corner. '
      'Mixed portal and arterial blood runs inward along the sinusoids; bile runs outward in canaliculi to the triads. Pick a part. '
      'Zones 1–3 are on Liver Blood Flow in Motion. ↑ present or more · ↓ lost or less · – not stated.',
  'c:tri': 'Portal triad: a portal vein branch, a hepatic artery branch and an interlobular bile duct, with lymphatics (so “triad” '
           'is a misnomer) and nerves, in the portal canal. The portal vein brings about 70–75% of the liver’s blood (First Aid: 80%), '
           'rich in nutrients but low in oxygen; the hepatic artery the other 25–30%. They mix in the sinusoids.',
  'c:cv': 'Central vein = terminal hepatic venule. Sinusoids drain into it; it empties into sublobular veins, which join the hepatic '
          'veins, which enter the inferior vena cava. Sublobular and hepatic veins travel alone, not in a triad, and have no valves.',
  'c:endo': 'Sinusoidal endothelium is discontinuous: large fenestrae without diaphragms, wide gaps between cells, and a basal lamina '
            'absent over large areas. There is no real barrier — plasma, even its proteins, passes freely into the space of Disse.',
  'c:disse': 'Space of Disse: between the endothelium and the hepatocytes, filled with hepatocyte microvilli that raise the surface up '
             'to sixfold. Here blood and hepatocyte exchange; albumin and lipoproteins enter the blood this way — every secretion but '
             'bile. Its excess fluid drains to the space of Mall and becomes hepatic lymph.',
  'c:kup': 'Kupffer cells: resident macrophages on or built into the sinusoid lining, about 15% of liver cells and 80–90% of the body’s '
           'tissue macrophages. They catch gut bacteria and endotoxin in portal blood (under 1% of portal bacteria get through) and '
           'remove damaged or old red cells, recycling their iron.',
  'c:ito': 'Hepatic stellate (Ito) cells sit in the space of Disse. Quiescent, they are the liver’s main vitamin A store — retinyl '
           'esters in lipid droplets — and release retinol bound to retinol-binding protein when blood levels fall.',
  'c:plate': 'Hepatocytes, about 80% of liver cells, form plates one cell thick in the adult (two cells thick until about age 6), a '
             'sinusoid on each side. The side facing the space of Disse is basolateral; the sides facing bile canaliculi are apical. '
             'They live about 5 months and regenerate well.',
  'c:can': 'Bile canaliculi: grooves between neighbouring hepatocytes, sealed by tight junctions, into which hepatocytes secrete bile, '
           'conjugated bilirubin included. Bile flows outward, against the blood: canals of Hering → bile ductules → interlobular '
           'ducts of the triad. ALP and GGT sit in this membrane and rise in cholestasis.',
  'c:acinus': 'The liver acinus is the smallest functional unit and fits perfusion, metabolism and disease best: a lozenge whose '
              'short axis is the terminal branches of the portal triads on the border between two classic lobules and whose long '
              'axis joins the two nearest central veins. Zone 1 lies next to the short axis (the incoming blood), zone 3 next to '
              'the central vein, zone 2 between.',
  'c:lob': 'The classic hepatic lobule is a roughly hexagonal mass of hepatocyte plates around a central vein (terminal hepatic '
           'venule), with portal triads at its corners; it follows the blood from the portal vein and hepatic artery to the '
           'central vein. The portal lobule and the liver acinus are the other two ways to describe the unit.',
  'c:fib': 'Chronic injury: TNF-α, TGF-β and PDGF from activated Kupffer cells and injured hepatocytes turn stellate cells into '
           'myofibroblasts. They lose their vitamin A, lay type I and III collagen in the space of Disse, the fenestrae close '
           '(capillarization), and their contraction raises sinusoid resistance → portal hypertension. Pancreatic stellate cells do '
           'the same in chronic pancreatitis.',
}

dyn = dict(
  kinds=dict(bl=['bl', '--nf-blood'], bact=['bact', '--dk4'], pl=['pl', '--nf-h2o'], prot=['prot', '--dk7'], bile=['bile', '--dk5']),
  groups=[['bl', 'Red cells'], ['bact', 'Gut bacteria'], ['pl', 'Plasma'], ['prot', 'Albumin · lipoproteins'], ['bile', 'Bile']],
  switches=[dict(id='c', label='Look at one part', type='one', options=[
      ['tri', 'Portal triad', 'giligaments'], ['cv', 'Central vein', 'ivcanat'],
      ['lob', 'Classic hepatic lobule', 'liverzones'], ['acinus', 'Liver acinus', 'liverzones'],
      ['endo', 'Sinusoidal endothelium', 'liverzones'], ['disse', 'Space of Disse', 'liverzones'],
      ['kup', 'Kupffer cells', 'macrophage'], ['ito', 'Stellate (Ito) cells', 'liverzones'],
      ['plate', 'Hepatocyte plates', 'liverzones'], ['can', 'Bile canaliculi'],
      ['fib', 'Stellate activation · fibrosis', 'cirrhosis']],
      sections=[['Blood in & out', ['tri', 'cv', 'lob', 'acinus']], ['The sinusoid', ['endo', 'disse', 'kup', 'ito']],
                ['Hepatocyte & bile', ['plate', 'can']], ['Injury', ['fib']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Course histology (Pawlina ch 18) and pathology (Robbins ch 18–19) texts · Guyton ch 71 · First Aid pp. 374, 396–397, 401, 413')

MAP = dict(
  id='lobulesim', title='Liver Lobule & Sinusoid in Motion', topic='gi', after='liver',
  sub='One classic lobule and one sinusoid magnified: blood in from the portal triad to the central vein, bile out through the '
      'canaliculi, plasma across the fenestrated endothelium into the space of Disse, Kupffer cells catching gut bacteria, '
      'stellate cells storing vitamin A — then activated into the fibrosis of cirrhosis. Tap a pin for its card',
  w=3500, h=1720,
  fa='374, 396, 397, 401, 413',
  src=[PW18, RB18, RB19, GY71],
  lanes=[('lbFlow', 'Blood & bile', 'glycolysis'), ('lbCell', 'Sinusoid cells', 'ppp'), ('lbDz', 'Injury', 'tca')],
  nodes=[
    ('lb1', 'Liver lobule', 300, 1560, 'lbFlow', 'lobule · sinusoid · zones', ['liverzones'], 'hub'),
    ('lb2', 'Portal triad (in ligament)', 740, 1560, 'lbFlow', 'hepatoduodenal ligament', ['giligaments']),
    ('lb3', 'Central vein → IVC', 1180, 1560, 'lbFlow', 'hepatic veins', ['ivcanat']),
    ('lb4', 'Bile canaliculi', 1620, 1560, 'lbFlow', 'bilirubin out · tight junctions', ['bilicycle', 'celljunctions']),
    ('lb5', 'Kupffer cells', 2060, 1560, 'lbCell', 'liver macrophages', ['macrophage']),
    ('lb6', 'Iron recycling', 300, 1650, 'lbCell', 'old RBCs → ferritin', ['ironcycle']),
    ('lb7', 'Vitamin A', 740, 1650, 'lbCell', 'stored in stellate cells', ['vitadef']),
    ('lb8', 'Cirrhosis', 1180, 1650, 'lbDz', 'stellate cells → fibrosis', ['cirrhosis']),
    ('lb9', 'Collagen I & III · repair', 1620, 1650, 'lbDz', 'scar', ['collagentypes', 'woundheal']),
  ],
  panels=[
    (2420, 1180, 1000, 'The lobule’s parts (course: Pawlina ch 18 · First Aid p. 374)', [
      ('Hepatocytes', 'about 80% of liver cells · plates one cell thick'),
      ('Kupffer cells', 'about 15% of liver cells · 80–90% of body macrophages'),
      ('Stellate (Ito) cells', 'space of Disse · vitamin A as retinyl esters'),
      ('Sinusoidal endothelium', 'fenestrae without diaphragms · gaps · patchy basal lamina'),
      ('Bile canaliculi', 'between hepatocytes · sealed by tight junctions'),
      ('Blood supply', 'portal vein 70–75% (First Aid: 80%) · hepatic artery 25–30%')]),
  ],
  dyn=dyn,
)
