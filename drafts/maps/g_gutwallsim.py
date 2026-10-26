# m57 — Gut Wall by Segment in Motion (dynamic map, kit data) — coverage3 entry ★5.
# Left: the tube from esophagus to rectum (with the gallbladder on its duct), food moving along it; the picked segment lights up.
# Right: a cut through that segment's wall, lumen at the top — mucosa, muscularis mucosae, submucosa (Meissner plexus),
# muscularis externa (Auerbach plexus between circular and longitudinal), serosa or adventitia — redrawn for each segment:
# stratified squamous + glands proper + striated muscle (esophagus), the squamous–columnar junction and cardiac glands, fundic
# glands with parietal and chief cells, deep pits and pyloric glands with G cells, villi + Brunner glands, tall plicae, Peyer
# patches with M cells, crypts full of goblet cells + teniae, and the gallbladder with no muscularis mucosae or submucosa.
# What moves: mucus, H⁺, gastrin, HCO₃⁻, nutrients, antigens, water — each where that segment makes or takes it.
# One `one` switch (10 options, 4 sections). 7 readouts: ↑ = a hallmark of the segment, ↓ = few or none, "–" = not stated.
#
# Sources (all read in the corpus):
#   OCOM GI course text — Ross & Pawlina 9e ch 17 (course_sdl_2_3_histo_forgut_p2.txt): four layers and serosa vs adventitia
#     (p3, p10); villi only in the small intestine, submucosal glands only in the esophagus and duodenum (Fig 17.1, p2, p7);
#     Peyer patches in lamina propria + submucosa of the ileum, opposite the mesentery (p6, p61); muscularis mucosae (p6);
#     Meissner (p7) and Auerbach (p7) plexuses; striated muscle only in the proximal esophagus and external anal sphincter, inner
#     oblique layer in the stomach, teniae coli (p8); sphincters, NOS and pyloric stenosis (p9); thoracic esophagus, duodenum
#     2nd–4th, ascending/descending colon, rectum have adventitia (p10); esophagus: nonkeratinized stratified squamous (p12),
#     thirds of the muscularis, adventitia, glands proper (submucosa, upper half, slightly acidic viscous mucus, duct cysts) and
#     cardiac glands (lamina propria, terminal esophagus, neutral mucus vs reflux), nucleus ambiguus vs dorsal motor nucleus
#     (p14, p16); stomach regions by gland type, rugae, gastric pits, surface mucous cells (p17–21); mucus–bicarbonate barrier,
#     PGE and NO (p24); fundic glands, parietal cells (neck, eosinophilic, HCl + intrinsic factor), chief cells (deep, basophilic,
#     pepsinogen) (p25–31); cardiac glands mucous (p44); pyloric glands — deep pits ~ half the mucosa, coiled, wide lumen, occasional
#     parietal cells (p46); small intestine plicae (most in distal duodenum/proximal jejunum), villi, lacteal (p56–59); goblet cells
#     increase duodenum → ileum (p68); Paneth cells — base of crypts, lysozyme, α-defensins, normally absent in the colon (p70, p90);
#     M cells over Peyer patches (p73); Brunner glands, pH 8.1–9.3, bicarbonate (p79–82); colon: no plicae or villi, straight crypts,
#     more goblet cells than the small intestine, water + electrolytes, teniae (p86–95).
#   OCOM GI course text — Ross & Pawlina 9e ch 18 (course_sdl_2_3_12_13_histo_foreguy_p3.txt p56–60): gallbladder simple columnar
#     on deep folds, removes ~90% of the water and concentrates bile up to 10-fold; no muscularis mucosae or submucosa; randomly
#     oriented smooth muscle; adventitia on the liver side, serosa elsewhere; Rokitansky-Aschoff sinuses.
#   OCOM GI Exam 1 lecture notes (course_exam1_lecture_notes.txt) — agree with all of the above; add: parietal cells occasionally in
#     cardiac/pyloric glands; gastric glands strictly mucosal (no submucosal glands); G cells of the gastric antrum.
#   Robbins ch 17 (course_sdl_8_9_patho.txt p37–38): mucus, bicarbonate, phospholipid, blood flow, restitution; PGE/PGI and NSAIDs.
#   First Aid 2025 p. 369 (layers, MSMS, erosion vs ulcer, histology by segment), 378 (G cells antrum), 379 (secretory products,
#     parietal pink / chief basophilic), 381 (Peyer patches, M cells, IgA; B12 + bile salts in the terminal ileum), 386 (autoimmune
#     gastritis affects body/fundus).
# Readout arrows: "–" wherever no source states presence or absence (e.g. goblet cells in the duodenum and jejunum are present but
#   not the hallmark; Peyer patches outside the ileum; parietal cells in the cardia are "occasional" → ↓).
# CUT: rugae drawn as a fold (kept as words only); villus "leaf vs finger" by segment (no source per segment); spec's
#   "Antrum: parietal ↓ (absent)" changed to "few" — course: occasional parietal cells in pyloric glands.
import sys, math, re
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

PW17, PW18, RB17 = full('Pawlina', 17), full('Pawlina', 18), full('Robbins', 17)
# The GI course readings ARE Ross & Pawlina 9e ch 17–18 and Robbins ch 17, so `src` cites those titles (check.py accepts only OCOM
# titles already in the atlas, and no OCOM GI title exists yet); the Exam 1 lecture notes are named in dyn.src.

OPTS = ['layers', 'eso', 'card', 'fund', 'ant', 'duo', 'jej', 'ile', 'col', 'gb']
O = lambda *k: ['s:' + x for x in k]
STOM = O('card', 'fund', 'ant')
SMALL = O('duo', 'jej', 'ile')
GENERIC = ['!s:*', 's:layers']          # the plain wall: nothing picked, or "the layers"

shapes = []
def add(svg, when=None, unless=None):
    if when is None and unless is None: shapes.append(svg); return
    d = dict(svg=svg)
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def text(t, x, y, cls='nf-l2', anchor=None, when=None, unless=None):
    if x >= 1100 and 240 <= y <= 1140:      # on the wall drawing: a halo so the label stays readable over the tissue
        a = f' text-anchor="{anchor}"' if anchor else ''
        add(f'<text class="{cls}" x="{x}" y="{y}"{a} style="paint-order:stroke;stroke:var(--map-bg);stroke-width:5px;'
            f'stroke-linejoin:round">{t.replace("&", "&amp;")}</text>', when, unless); return
    d = dict(text=t, x=x, y=y, cls=cls)
    if anchor: d['anchor'] = anchor
    if when: d['when'] = when
    if unless: d['unless'] = unless
    shapes.append(d)
def lead(x0, y0, x1, y1, when=None, unless=None):
    add(f'<path d="M{x0} {y0} L{x1} {y1}" class="dyn-line" style="stroke-width:1.5;opacity:.7"/>', when, unless)
TAG = 'nf-l2 dyn-tag'
TAG1 = 'nf-l1 dyn-tag'

# ── path length (M L H V C) — flows need it ──
def plen(d):
    toks = re.findall(r'[MLHVCZ]|-?\d+(?:\.\d+)?', d); i = 0; x = y = 0; L = 0.0; cmd = None
    while i < len(toks):
        t = toks[i]
        if t.isalpha(): cmd = t; i += 1; continue
        if cmd == 'M': x, y = float(toks[i]), float(toks[i + 1]); i += 2; cmd = 'L'
        elif cmd == 'L': nx, ny = float(toks[i]), float(toks[i + 1]); L += math.hypot(nx - x, ny - y); x, y = nx, ny; i += 2
        elif cmd == 'H': nx = float(toks[i]); L += abs(nx - x); x = nx; i += 1
        elif cmd == 'V': ny = float(toks[i]); L += abs(ny - y); y = ny; i += 1
        elif cmd == 'C':
            p = [(x, y)] + [(float(toks[i + k]), float(toks[i + k + 1])) for k in (0, 2, 4)]; i += 6
            px, py = x, y
            for s in range(1, 41):
                u = s / 40; a = (1 - u) ** 3; b = 3 * u * (1 - u) ** 2; c = 3 * u * u * (1 - u); e = u ** 3
                qx = a * p[0][0] + b * p[1][0] + c * p[2][0] + e * p[3][0]; qy = a * p[0][1] + b * p[1][1] + c * p[2][1] + e * p[3][1]
                L += math.hypot(qx - px, qy - py); px, py = qx, qy
            x, y = p[3]
        else: i += 1
    return round(L)
def flow(d, kind, n, speed=90, r=6, when=None, unless=None):
    f = dict(d=d, len=plen(d), speed=speed, r=r, base={kind: n})
    if when: f['when'] = when
    if unless: f['unless'] = unless
    return f

# ════════ title ════════
text('The gut wall, segment by segment', 160, 140, 'dyn-big')
text('left: where along the tube · right: a cut through that wall, lumen at the top', 160, 162, 'dyn-cap')

# ════════ LEFT — the tube (anterior view; the patient’s right is on the left) ════════
ESO = 'M440 240 V470'
STOM_C = 'M440 470 C470 520 560 540 580 620 C590 700 520 745 450 748 L386 755'
DUO = 'M386 755 C320 755 282 790 282 850 C282 915 330 945 400 945 L470 935'
JEJ = 'M470 935 C520 960 570 1000 600 1040 C630 1085 560 1110 480 1100 C400 1090 320 1110 330 1160'
ILE = 'M330 1160 C340 1210 460 1200 560 1212 C640 1222 640 1290 560 1300 C480 1310 360 1300 300 1292 L240 1290'
COL = 'M210 1290 V990 C210 975 225 970 240 970 H660 C680 970 700 985 700 1000 V1320 C700 1370 640 1400 560 1400 C500 1400 470 1410 462 1440'
CENTER = ESO + ' ' + STOM_C[STOM_C.index('C'):] + ' ' + DUO[DUO.index('C'):] + ' ' + JEJ[JEJ.index('C'):] + ' ' + \
    ILE[ILE.index('C'):] + ' L210 1290 ' + COL[COL.index('V'):]
STOMACH = ('M426 470 C418 428 470 400 522 420 C602 452 642 540 622 640 C607 722 540 772 470 772 L392 772 C374 772 366 752 378 742 '
           'C392 730 420 730 450 726 C510 718 540 680 540 622 C540 560 502 508 454 486 Z')
GB = 'M186 602 C166 640 186 702 228 702 C258 702 270 662 256 622 C246 596 208 586 186 602 Z'
DUCT = 'M238 702 C246 742 262 772 284 806'

add(f'<path d="{GB}" style="fill:var(--dk3);fill-opacity:.22;stroke:var(--dk3);stroke-width:3"/>')
add(f'<path d="{DUCT}" style="fill:none;stroke:var(--dk3);stroke-width:7;stroke-linecap:round;opacity:.7"/>')
shapes.append(dict(tube=ESO, w=22))
add(f'<path d="{STOMACH}" class="nf-wall" style="fill:var(--surface-2);stroke-width:12;stroke-linejoin:round"/>')
add(f'<path d="{STOMACH}" style="fill:var(--surface-2);stroke:none"/>')
shapes.append(dict(tube=DUO, w=22))
shapes.append(dict(tube=JEJ, w=22))
shapes.append(dict(tube=ILE, w=20))
shapes.append(dict(tube=COL, w=36, color='--dk10'))
for y in range(1040, 1300, 60):                    # haustra
    add(f'<path d="M188 {y} h44 M678 {y} h44" style="stroke:var(--dk10);stroke-width:3;opacity:.6"/>')
for x in range(290, 660, 60):
    add(f'<path d="M{x} 948 v44" style="stroke:var(--dk10);stroke-width:3;opacity:.6"/>')
text('Esophagus', 470, 300, 'nf-l1')
text('Stomach', 640, 520, 'nf-l1')
text('Duodenum', 380, 862, 'nf-l1', 'middle')
text('Gallbladder', 150, 580, 'nf-l1')
text('Jejunum', 620, 1105, 'nf-l1')
text('Ileum', 460, 1250, 'nf-l1', 'middle')
text('Colon', 740, 1150, 'nf-l1')
text('food moves top to bottom', 160, 1470, 'dyn-cap')

# the picked segment
HL = {'eso': f'<path d="{ESO}" class="dyn-hl" style="stroke-width:14"/>',
      'card': '<ellipse cx="452" cy="486" rx="34" ry="26" class="dyn-hl"/>',
      'fund': '<path d="M440 440 C470 410 560 420 600 480 C640 540 630 620 610 680" class="dyn-hl" style="stroke-width:14"/>',
      'ant': '<path d="M560 700 C530 750 470 772 392 762" class="dyn-hl" style="stroke-width:14"/>',
      'duo': f'<path d="{DUO}" class="dyn-hl" style="stroke-width:14"/>',
      'jej': f'<path d="{JEJ}" class="dyn-hl" style="stroke-width:14"/>',
      'ile': f'<path d="{ILE}" class="dyn-hl" style="stroke-width:14"/>',
      'col': f'<path d="{COL}" class="dyn-hl" style="stroke-width:14"/>',
      'gb': f'<path d="{GB}" class="dyn-hl"/>'}
for k, s in HL.items(): add(s, when=O(k))
# esophagus thirds
for (y0, y1, lab, op) in ((240, 317, 'striated', 1), (317, 393, 'mixed', .55), (393, 470, 'smooth', .2)):
    add(f'<rect x="408" y="{y0 + 4}" width="14" height="{y1 - y0 - 8}" rx="4" style="fill:var(--dk2);opacity:{op}"/>', when=O('eso'))
    text(lab, 398, (y0 + y1) // 2 + 5, 'nf-l2', 'end', when=O('eso'))
text('cardia · fundus · body · antrum · pylorus', 640, 544, 'nf-l2', when=STOM)

# ════════ RIGHT — the cut through the wall ════════
X0, X1 = 1110, 2300
SURF, MMT, MMB, SUBB, CIRB, PLX, LONB, SERB = 430, 640, 662, 830, 950, 956, 1036, 1056
LX = 1088                                     # layer labels, right-aligned
NOTGB = O('gb')
TITLE = {'layers': 'The four coats (a small-bowel wall)', 'eso': 'Esophagus', 'card': 'Cardia — the gastroesophageal junction',
         'fund': 'Fundus · body of the stomach', 'ant': 'Antrum · pylorus', 'duo': 'Duodenum', 'jej': 'Jejunum',
         'ile': 'Ileum', 'col': 'Colon', 'gb': 'Gallbladder'}
text('A cut through the wall — pick a segment', X0, 205, 'dyn-big', unless=['s:*'])
for k, t in TITLE.items(): text(t, X0, 205, 'dyn-big', when=O(k))
text('lumen', X1 - 10, 250, 'dyn-cap', 'end')

# shared bands (every segment but the gallbladder)
add(f'<rect x="{X0}" y="{SURF}" width="{X1 - X0}" height="{MMT - SURF}" class="dyn-soft" style="stroke:none"/>', unless=NOTGB)
add(f'<rect x="{X0}" y="{MMT}" width="{X1 - X0}" height="{MMB - MMT}" style="fill:var(--dk2);opacity:.45"/>', unless=NOTGB)
add(f'<rect x="{X0}" y="{MMB}" width="{X1 - X0}" height="{SUBB - MMB}" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:2"/>', unless=NOTGB)
add(f'<rect x="{X0}" y="{SUBB}" width="{X1 - X0}" height="{CIRB - SUBB}" style="fill:var(--dk2);opacity:.28"/>', unless=NOTGB)
add(f'<rect x="{X0}" y="{PLX + 6}" width="{X1 - X0}" height="{LONB - PLX - 6}" style="fill:var(--dk2);opacity:.2"/>', unless=NOTGB)
add(''.join(f'<ellipse cx="{x}" cy="{(SUBB + CIRB) // 2 + (12 if (x // 50) % 2 else -14)}" rx="20" ry="8" style="fill:var(--dk2);opacity:.35"/>'
            for x in range(X0 + 40, X1, 50)), unless=NOTGB + O('eso'))           # circular fibres, cut across
add(''.join(f'<path d="M{X0 + 10} {y} H{X1 - 10}" style="stroke:var(--dk2);stroke-width:3;opacity:.35"/>'
            for y in (978, 1000, 1022)), unless=NOTGB + O('eso'))                # longitudinal fibres
# vessels in the submucosa
add(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--nf-blood);opacity:.55"/>'
            for x, y, r in ((1240, 780, 13), (1290, 784, 10), (2180, 772, 12), (2220, 790, 9))), unless=NOTGB)
# plexuses
def ganglia(y, xs, when=None, unless=None):
    add(f'<path d="M{X0 + 10} {y} H{X1 - 10}" style="stroke:var(--dk5);stroke-width:3;stroke-dasharray:3 6"/>' +
        ''.join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="8" style="fill:var(--dk5)"/>' for x in xs), when, unless)
ganglia(810, range(X0 + 160, X1, 260), unless=NOTGB)
ganglia(PLX, range(X0 + 90, X1, 230), unless=NOTGB)
add(f'<rect x="{X0}" y="{MMB + 4}" width="{X1 - X0}" height="{SUBB - MMB - 8}" class="dyn-hl" style="stroke-width:4;fill:none;opacity:.5"/>', when=O('layers'))
add(f'<path d="M{X0} {PLX} H{X1}" class="dyn-hl" style="stroke-width:5;opacity:.6"/>', when=O('layers'))
# serosa (mesothelium) or adventitia
add(f'<rect x="{X0}" y="{LONB}" width="{X1 - X0}" height="{SERB - LONB}" style="fill:var(--dk8);opacity:.45"/>', unless=NOTGB + O('eso'))
add(f'<rect x="{X0}" y="{LONB}" width="{X1 - X0}" height="34" style="fill:var(--surface-2)"/>'
    f'<path d="M{X0} {LONB + 34} ' + ''.join(f'q15 10 30 0 ' for _ in range((X1 - X0) // 30)) + '" style="fill:none;stroke:var(--line-2);stroke-width:2"/>',
    when=O('eso'))

# layer labels on the left of the cut
GEN_LAB = [('Mucosa', 500, 'nf-l1'), ('epithelium · lamina propria', 520, 'nf-l2'), ('muscularis mucosae', 656, 'nf-l2'),
           ('Submucosa', 742, 'nf-l1'), ('Meissner plexus', 812, 'nf-l2'), ('Muscularis externa', 880, 'nf-l1'),
           ('inner circular', 900, 'nf-l2'), ('Auerbach plexus', 958, 'nf-l2'), ('outer longitudinal', 1006, 'nf-l2')]
for t, y, c in GEN_LAB: text(t, LX, y, c, 'end', unless=NOTGB)
text('Serosa', LX, 1056, 'nf-l1', 'end', unless=NOTGB + O('eso', 'duo', 'col'))
text('Serosa or adventitia', LX, 1056, 'nf-l1', 'end', when=O('duo', 'col'))
text('Adventitia', LX, 1056, 'nf-l1', 'end', when=O('eso'))
text('Lumen', LX, 300, 'nf-l1', 'end')

# ── drawing helpers for the mucosa ──
CELL = 'class="dyn-cell" style="stroke-width:2"'
def villus(x, base, top, w=44, goblets=0):
    s = (f'<path d="M{x - w / 2} {base} V{top + w / 2} A{w / 2} {w / 2} 0 0 1 {x + w / 2} {top + w / 2} V{base}" {CELL}/>'
         f'<path d="M{x} {base - 6} V{top + w / 2 + 6}" style="stroke:var(--dk9);stroke-width:4;opacity:.7"/>')
    for g in range(goblets):
        yy = top + w / 2 + 18 + g * ((base - top - w / 2 - 30) / max(1, goblets))
        side = -1 if g % 2 else 1
        s += f'<ellipse cx="{x + side * (w / 2 - 5)}" cy="{yy:.0f}" rx="5" ry="9" style="fill:var(--surface);stroke:var(--dk6);stroke-width:2"/>'
    return s
def crypt(x, top, bot, paneth=True, goblets=0, w=26):
    s = f'<rect x="{x - w / 2}" y="{top}" width="{w}" height="{bot - top}" rx="{w / 2}" {CELL}/>' \
        f'<path d="M{x} {top} V{bot - 12}" style="stroke:var(--surface-2);stroke-width:5"/>'
    for g in range(goblets):
        yy = top + 18 + g * (bot - top - 40) / max(1, goblets - 1)
        s += f'<ellipse cx="{x + (-7 if g % 2 else 7)}" cy="{yy:.0f}" rx="5" ry="8" style="fill:var(--surface);stroke:var(--dk6);stroke-width:2"/>'
    if paneth:
        s += ''.join(f'<circle cx="{x + dx}" cy="{bot - 9}" r="5" style="fill:var(--dk2)"/>' for dx in (-6, 6))
    return s
def surface(x0, x1, y, pits=(), pitdepth=0):
    """a simple columnar sheet with pits dipping into it"""
    s = f'<rect x="{x0}" y="{y - 22}" width="{x1 - x0}" height="22" {CELL}/>'
    s += ''.join(f'<path d="M{x} {y - 22} v22" style="stroke:var(--dyn-cell-line);stroke-width:1.2;opacity:.6"/>' for x in range(x0 + 14, x1, 14))
    for px in pits:
        s += f'<path d="M{px - 16} {y - 22} V{y + pitdepth} A16 16 0 0 0 {px + 16} {y + pitdepth} V{y - 22}" {CELL}/>' \
             f'<path d="M{px} {y - 22} V{y + pitdepth + 6}" style="stroke:var(--surface-2);stroke-width:6"/>'
    return s

# ── default / layers: a plain small-bowel-like mucosa + erosion and ulcer ──
g = ''.join(crypt(x, 480, 630, paneth=False) for x in range(X0 + 70, X1 - 20, 110))
g += ''.join(villus(x, 480, 320, 46) for x in range(X0 + 125, X1 - 40, 110))
g += f'<rect x="{X0}" y="470" width="{X1 - X0}" height="14" {CELL}/>'
add(g, when=GENERIC)
add(f'<path d="M1470 470 Q1500 520 1530 470" style="fill:var(--surface);stroke:var(--bad);stroke-width:4"/>', when=O('layers'))
text('erosion — mucosa only', 1500, 410, TAG1, 'middle', when=O('layers'))
add(f'<path d="M1880 470 C1880 620 1900 880 1960 880 C2020 880 2040 620 2040 470 Z" style="fill:var(--surface);stroke:var(--bad);stroke-width:4"/>', when=O('layers'))
text('ulcer — into the submucosa or muscle', 1960, 410, TAG1, 'middle', when=O('layers'))

# ── esophagus ──
ES_TOP, ES_BOT = 300, 470
g = f'<path d="M{X0} {ES_TOP} H{X1} V{ES_BOT} ' + ''.join(f'Q{x - 30} {ES_BOT + 34} {x - 60} {ES_BOT} ' for x in range(X1, X0, -60)) + 'Z" style="fill:var(--dyn-cell);stroke:var(--dyn-cell-line);stroke-width:2"/>'
for i, y in enumerate(range(ES_TOP + 14, ES_BOT, 26)):
    g += ''.join(f'<ellipse cx="{x + (20 if i % 2 else 0)}" cy="{y}" rx="{18 - i * 1.5 if i < 4 else 12}" ry="{4 + i * 1.5:.0f}" '
                 f'style="fill:none;stroke:var(--dyn-cell-line);stroke-width:1.5;opacity:.7"/>' for x in range(X0 + 30, X1 - 20, 44))
add(g, when=O('eso'))
text('nonkeratinized stratified squamous — many layers, flat on top', X0 + 20, ES_TOP - 14, TAG1, when=O('eso'))
# glands proper in the submucosa, with a duct to the lumen
GP = (1560, 745)
add(''.join(f'<circle cx="{GP[0] + dx}" cy="{GP[1] + dy}" r="17" style="fill:var(--dk6);opacity:.75;stroke:var(--surface);stroke-width:2"/>'
            for dx, dy in ((-30, -10), (0, -22), (30, -8), (-14, 18), (18, 20), (44, 16), (-46, 16)))
    + f'<path d="M{GP[0]} {GP[1] - 30} C{GP[0] + 10} 600 {GP[0] - 10} 480 {GP[0]} {ES_TOP}" style="fill:none;stroke:var(--dk6);stroke-width:9;opacity:.6"/>',
    when=O('eso'))
text('esophageal glands proper (submucosa)', GP[0] + 80, 728, 'nf-l1', when=O('eso'))
text('viscous, slightly acidic mucus — lubricates', GP[0] + 80, 748, 'nf-l2', when=O('eso'))
CG = (2120, 560)
add(''.join(f'<circle cx="{CG[0] + dx}" cy="{CG[1] + dy}" r="12" style="fill:var(--dk6);opacity:.55"/>' for dx, dy in ((-18, 0), (0, -16), (18, 0), (0, 16))),
    when=O('eso'))
text('cardiac glands (lamina propria, lower end)', CG[0] + 30, 610, 'nf-l2', 'end', when=O('eso'))
text('neutral mucus — against reflux', CG[0] + 30, 628, 'nf-l2', 'end', when=O('eso'))
# striated (upper third) vs smooth muscle
SPLIT = 1640
add(f'<rect x="{X0}" y="{SUBB}" width="{SPLIT - X0}" height="{CIRB - SUBB}" style="fill:var(--dk2);opacity:.45"/>'
    f'<rect x="{X0}" y="{PLX + 6}" width="{SPLIT - X0}" height="{LONB - PLX - 6}" style="fill:var(--dk2);opacity:.45"/>'
    + ''.join(f'<path d="M{x} {SUBB + 6} V{CIRB - 6} M{x} {PLX + 12} V{LONB - 6}" style="stroke:var(--surface);stroke-width:2;opacity:.8"/>'
              for x in range(X0 + 12, SPLIT, 14)), when=O('eso'))
add(''.join(f'<ellipse cx="{x}" cy="{(SUBB + CIRB) // 2}" rx="20" ry="8" style="fill:var(--dk2);opacity:.35"/>' for x in range(SPLIT + 40, X1, 50))
    + ''.join(f'<path d="M{SPLIT + 10} {y} H{X1 - 10}" style="stroke:var(--dk2);stroke-width:3;opacity:.35"/>' for y in (978, 1000, 1022)), when=O('eso'))
text('upper third: striated (vagus, nucleus ambiguus)', (X0 + SPLIT) // 2, 1090, TAG1, 'middle', when=O('eso'))
text('lower third: smooth (dorsal motor nucleus)', (SPLIT + X1) // 2, 1090, 'nf-l1', 'middle', when=O('eso'))
text('no serosa in the thorax — the outer coat blends into the mediastinum', X0 + 20, 1124, 'nf-l2', when=O('eso'))

# ── stomach (shared): inner oblique layer ──
add(f'<rect x="{X0}" y="{SUBB}" width="{X1 - X0}" height="34" style="fill:var(--dk4);opacity:.3"/>'
    + ''.join(f'<path d="M{x} {SUBB + 32} l26 -30" style="stroke:var(--dk4);stroke-width:3;opacity:.6"/>' for x in range(X0 + 10, X1 - 30, 30)), when=STOM)
text('inner oblique layer — stomach only', X1 - 10, SUBB + 22, 'nf-l1', 'end', when=STOM)

# ── cardia ──
CJ = 1380                                      # the squamous–columnar junction
g = f'<rect x="{X0}" y="330" width="{CJ - X0}" height="140" style="fill:var(--dyn-cell);stroke:var(--dyn-cell-line);stroke-width:2"/>'
g += ''.join(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="5" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:1.5;opacity:.7"/>'
             for x in range(X0 + 24, CJ - 10, 40) for y in range(348, 470, 26))
g += surface(CJ, X1, 400, pits=range(CJ + 90, X1 - 40, 150), pitdepth=40)
for px in range(CJ + 90, X1 - 40, 150):   # tortuous cardiac glands below each pit
    g += (f'<path d="M{px} 456 C{px - 30} 490 {px + 30} 520 {px} 550 C{px - 30} 580 {px + 20} 610 {px} 625" '
          f'style="fill:none;stroke:var(--dk6);stroke-width:22;stroke-linecap:round;opacity:.55"/>')
add(g, when=O('card'))
add(f'<path d="M{CJ} 300 V480" class="dyn-hl" style="stroke-width:5"/>', when=O('card'))
text('squamous ends abruptly', CJ - 10, 290, TAG1, 'end', when=O('card'))
text('simple columnar · shallow pits', CJ + 10, 290, 'nf-l1', when=O('card'))
text('cardiac glands — mucous cells', X1 - 10, 600, 'nf-l1', 'end', when=O('card'))

# ── fundus · body ──
g = surface(X0, X1, 380, pits=range(X0 + 70, X1 - 20, 120), pitdepth=24)
for px in range(X0 + 70, X1 - 20, 120):
    g += f'<rect x="{px - 15}" y="420" width="30" height="210" rx="15" {CELL}/>' \
         f'<path d="M{px} 420 V620" style="stroke:var(--surface-2);stroke-width:5"/>'
    for i, y in enumerate((440, 478, 516, 554)):    # parietal cells: pink triangles bulging out of the neck
        sd = -1 if i % 2 else 1
        g += f'<path d="M{px + sd * 14} {y - 14} L{px + sd * 34} {y} L{px + sd * 14} {y + 14} Z" style="fill:var(--dk7);opacity:.85"/>'
    g += ''.join(f'<rect x="{px + sd * 15 - (16 if sd < 0 else 0)}" y="{y}" width="16" height="18" rx="4" style="fill:var(--dk11);opacity:.85"/>'
                 for y in (578, 604) for sd in (-1, 1))
add(g, when=O('fund'))
text('surface mucous cells line the surface and the pits', X0 + 20, 340, 'nf-l1', when=O('fund'))
text('parietal cells (pink) — neck', X1 - 10, 470, 'nf-l1', 'end', when=O('fund'))
text('chief cells (basophilic) — base', X1 - 10, 600, 'nf-l1', 'end', when=O('fund'))

# ── antrum · pylorus ──
g = surface(X0, X1, 380, pits=range(X0 + 80, X1 - 20, 140), pitdepth=150)
for px in range(X0 + 80, X1 - 20, 140):
    g += (f'<path d="M{px} 540 C{px - 40} 560 {px + 40} 590 {px} 625" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:30;stroke-linecap:round;opacity:.35"/>'
          f'<path d="M{px} 540 C{px - 40} 560 {px + 40} 590 {px} 625" style="fill:none;stroke:var(--surface-2);stroke-width:12;stroke-linecap:round"/>')
    g += ''.join(f'<circle cx="{px + dx}" cy="{dy}" r="7" style="fill:var(--dk5)"/>' for dx, dy in ((-18, 566), (16, 598)))
add(g, when=O('ant'))
add(f'<path d="M{X0 + 10} 618 H{X1 - 10}" style="stroke:var(--nf-blood);stroke-width:5;opacity:.45"/>', when=O('ant'))   # capillary
add(f'<rect x="{X0}" y="{SUBB + 34}" width="{X1 - X0}" height="{CIRB - SUBB - 34}" style="fill:var(--dk2);opacity:.3"/>', when=O('ant'))
text('deep pits — about half the mucosa', X0 + 20, 340, 'nf-l1', when=O('ant'))
text('coiled pyloric glands, wide lumen · G cells (gold)', X1 - 10, 520, 'nf-l1', 'end', when=O('ant'))
text('circular layer thickens into the pyloric sphincter', X1 - 10, 925, 'nf-l1', 'end', when=O('ant'))

# ── duodenum · jejunum · ileum ──
def small_mucosa(villi_top, base=470, gob=1, skip=(), cskip=()):
    s = ''.join(crypt(x, base + 10, 630, paneth=True) for x in range(X0 + 70, X1 - 20, 110) if not any(a <= x <= b for a, b in cskip))
    s += ''.join(villus(x, base + 10, villi_top, 46, goblets=gob) for x in range(X0 + 125, X1 - 40, 110) if not any(a <= x <= b for a, b in skip))
    for a, b in [(X0, X1)] if not cskip else [(X0, cskip[0][0]), (cskip[0][1], X1)]:
        s += f'<rect x="{a}" y="{base}" width="{b - a}" height="14" {CELL}/>'
    return s
add(small_mucosa(310, gob=1), when=O('duo'))
BR = [(1330, 740), (1700, 750), (2060, 742)]
add(''.join(''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="15" style="fill:var(--dk6);opacity:.8;stroke:var(--surface);stroke-width:2"/>'
                    for dx, dy in ((-26, -8), (0, -18), (26, -6), (-12, 14), (14, 16), (38, 14), (-38, 14)))
            + f'<path d="M{x} {y - 26} V{MMT - 4}" style="stroke:var(--dk6);stroke-width:8;opacity:.6"/>' for x, y in BR), when=O('duo'))
text('Brunner glands (submucosa) — alkaline mucus, HCO₃⁻', 1700, 694, 'nf-l1', 'middle', when=O('duo'))
# jejunum: a tall plica circularis — a fold with a submucosal core
PL0, PL1, PLT = 1480, 1920, 360
add(f'<path d="M{PL0} {SUBB - 10} C{PL0 + 40} 500 {PL0 + 120} {PLT} {(PL0 + PL1) // 2} {PLT} C{PL1 - 120} {PLT} {PL1 - 40} 500 {PL1} {SUBB - 10} Z" '
    'class="dyn-soft" style="stroke:var(--dyn-cell-line);stroke-width:6"/>'
    f'<path d="M{PL0 + 90} {SUBB - 10} C{PL0 + 120} 560 {PL0 + 170} {PLT + 110} {(PL0 + PL1) // 2} {PLT + 110} C{PL1 - 170} {PLT + 110} {PL1 - 120} 560 {PL1 - 90} {SUBB - 10} Z" '
    'style="fill:var(--surface-2);stroke:var(--dk2);stroke-width:10;stroke-opacity:.45"/>', when=O('jej'))
g = small_mucosa(300, gob=1, skip=((PL0 - 20, PL1 + 20),), cskip=((PL0 + 20, PL1 - 20),))
for i, x in enumerate(range(PL0 + 80, PL1 - 40, 70)):
    t = (x - (PL0 + PL1) / 2) / ((PL1 - PL0) / 2)
    y = PLT + 120 * t * t + 10
    g += villus(x, y + 40, y - 120, 40)
add(g, when=O('jej'))
text('tallest, most numerous plicae circulares — submucosal core', (PL0 + PL1) // 2, 250, 'nf-l1', 'middle', when=O('jej'))
# ileum: goblet cells + a Peyer patch with M cells
PP = (1760, 600)
add(small_mucosa(330, gob=3, skip=((PP[0] - 200, PP[0] + 200),), cskip=((PP[0] - 170, PP[0] + 170),)), when=O('ile'))
add(f'<path d="M{PP[0] - 190} 470 C{PP[0] - 150} 380 {PP[0] + 150} 380 {PP[0] + 190} 470" style="fill:var(--dyn-cell);stroke:var(--dk4);stroke-width:4"/>'
    + ''.join(f'<circle cx="{PP[0] + dx}" cy="{PP[1] + dy}" r="{r}" style="fill:var(--dk4);opacity:.4;stroke:var(--dk4);stroke-width:3"/>'
              for dx, dy, r in ((-80, -40, 62), (70, -36, 64), (0, 100, 70))), when=O('ile'))
add(''.join(f'<rect x="{PP[0] + dx - 9}" y="{400 + abs(dx) * 0.25:.0f}" width="18" height="20" rx="4" style="fill:var(--dk4)"/>' for dx in (-120, -40, 40, 120)), when=O('ile'))
text('Peyer patch — lymphoid nodules in the lamina propria and submucosa', PP[0], 296, 'nf-l1', 'middle', when=O('ile'))
text('M cells on the dome sample antigens', PP[0], 322, 'nf-l2', 'middle', when=O('ile'))
text('goblet cells (white) — most in the small bowel', X0 + 20, 262, 'nf-l1', when=O('ile'))

text('Paneth cells (red) at the crypt bases', X1 - 10, 600, 'nf-l1', 'end', when=SMALL)

# ── colon ──
g = surface(X0, X1, 400)
g += ''.join(crypt(x, 400, 632, paneth=False, goblets=6, w=34) for x in range(X0 + 50, X1 - 20, 80))
add(g, when=O('col'))
add(f'<rect x="1640" y="{PLX + 6}" width="300" height="{LONB - PLX - 6}" rx="6" style="fill:var(--dk2);opacity:.55"/>', when=O('col'))
text('teniae coli — the longitudinal layer gathered into 3 bands', 1790, 1110, 'nf-l1', 'middle', when=O('col'))
text('no villi, no plicae — straight crypts packed with goblet cells', X0 + 20, 340, 'nf-l1', when=O('col'))

# ── gallbladder ──
GB_MT, GB_MB, GB_CT = 560, 860, 1000
g = f'<rect x="{X0}" y="430" width="{X1 - X0}" height="{GB_MT - 430}" class="dyn-soft" style="stroke:none"/>'
for x in range(X0 + 60, X1 - 40, 120):          # deep branching mucosal folds
    g += (f'<path d="M{x - 22} {GB_MT} C{x - 22} 420 {x - 40} 360 {x - 10} 330 C{x + 10} 310 {x + 30} 360 {x + 22} 420 C{x + 18} 470 {x + 22} 520 {x + 22} {GB_MT}" {CELL}/>')
g += f'<rect x="{X0}" y="{GB_MT}" width="{X1 - X0}" height="{GB_MB - GB_MT}" style="fill:var(--dk2);opacity:.12"/>'
for i in range(48):                              # randomly oriented smooth-muscle bundles
    x = X0 + 30 + (i * 97) % (X1 - X0 - 60); y = GB_MT + 30 + (i * 53) % (GB_MB - GB_MT - 60); a = (i * 47) % 180
    g += f'<ellipse cx="{x}" cy="{y}" rx="34" ry="9" transform="rotate({a} {x} {y})" style="fill:var(--dk2);opacity:.4"/>'
g += f'<rect x="{X0}" y="{GB_MB}" width="{X1 - X0}" height="{GB_CT - GB_MB}" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:2"/>'
g += f'<rect x="{X0}" y="{GB_CT}" width="{X1 - X0}" height="16" style="fill:var(--dk8);opacity:.45"/>'
g += f'<path d="M2040 {GB_MT - 2} C2030 640 2070 720 2060 800 C2056 830 2100 830 2096 800 C2090 720 2124 640 2112 {GB_MT - 2}" {CELL}/>'   # R-A sinus
add(g, when=O('gb'))
for t, y, c in (('Mucosa', 450, 'nf-l1'), ('simple columnar on deep folds', 470, 'nf-l2'), ('Muscularis externa', 700, 'nf-l1'),
                ('random smooth-muscle bundles', 720, 'nf-l2'), ('Perimuscular', 920, 'nf-l1'), ('connective tissue', 940, 'nf-l2'),
                ('Serosa · adventitia', 1016, 'nf-l1'), ('(adventitia on the liver side)', 1036, 'nf-l2')):
    text(t, LX, y, c, 'end', when=O('gb'))
text('no muscularis mucosae, no submucosa — lamina propria sits on the muscle', X0 + 20, 590, TAG1, when=O('gb'))
text('Rokitansky-Aschoff sinus', 2140, 820, 'nf-l1', when=O('gb'))

text('Readouts: ↑ a hallmark of this segment · ↓ few or none · – not stated', X0, 1170, 'dyn-cap')

# ════════ motion ════════
flows = [
  flow(CENTER, 'chy', 9, speed=120, r=9),
  flow(DUCT, 'bile', 2, speed=50, r=6),
  # layers: plexus signals
  flow(f'M{X0 + 20} 810 H{X1 - 20}', 'ap', 4, speed=220, r=6, when=O('layers')),
  flow(f'M{X0 + 20} {PLX} H{X1 - 20}', 'ap', 4, speed=220, r=6, when=O('layers')),
  # esophagus: mucus up the duct of a gland proper, food sliding past
  flow(f'M{GP[0]} {GP[1] - 30} C{GP[0] + 10} 600 {GP[0] - 10} 480 {GP[0]} {ES_TOP} V250', 'muc', 4, speed=60, when=O('eso')),
  flow(f'M{X0 + 20} 262 H{X1 - 20}', 'chy', 4, speed=120, r=10, when=O('eso')),
  # cardia: mucus out of the cardiac glands
  *[flow(f'M{px} 610 V250', 'muc', 2, speed=60, when=O('card')) for px in range(CJ + 90, X1 - 40, 300)],
  # fundus: acid up the glands
  *[flow(f'M{px} 560 V250', 'h', 3, speed=80, when=O('fund')) for px in range(X0 + 70, X1 - 20, 240)],
  # antrum: gastrin down into the lamina propria capillary
  *[flow(f'M{px - 18} 566 L{px - 40} 618 H{px - 130}', 'gas', 2, speed=50, when=O('ant')) for px in range(X0 + 220, X1 - 20, 280)],
  flow(f'M{X0 + 20} 262 H{X1 - 20}', 'chy', 4, speed=100, r=10, when=STOM),
  # duodenum: bicarbonate from Brunner glands up their ducts
  *[flow(f'M{x} {y - 26} V250', 'hco3', 3, speed=70, when=O('duo')) for x, y in BR],
  # jejunum: nutrients into the villi
  *[flow(f'M{x} 250 V460', 'nut', 2, speed=70, when=O('jej', 'duo')) for x in range(X0 + 125, X1 - 40, 220)],
  # ileum: antigens through the M cells into the patch
  *[flow(f'M{PP[0] + dx} 250 V{PP[1] - 20}', 'ag', 2, speed=60, when=O('ile')) for dx in (-120, 40)],
  # colon: water taken back; gallbladder: water out of the bile
  *[flow(f'M{x} 250 V560', 'w', 2, speed=70, when=O('col')) for x in range(X0 + 90, X1 - 20, 240)],
  *[flow(f'M{x} 260 V{GB_MT + 40}', 'w', 2, speed=70, when=O('gb')) for x in range(X0 + 120, X1 - 40, 240)],
]
KL = [('chy', '--dk10', 'Food'), ('bile', '--dk3', 'Bile'), ('muc', '--dk6', 'Mucus'), ('h', '--nf-h', 'H⁺'),
      ('gas', '--dk5', 'Gastrin'), ('hco3', '--nf-hco3', 'HCO₃⁻'), ('nut', '--nf-glu', 'Nutrients'), ('w', '--nf-h2o', 'Water'),
      ('ag', '--dk4', 'Antigen'), ('ap', '--dk1', 'Plexus signal')]
kinds = {k: [k, c] for k, c, _ in KL}          # one colour per group, so each chip names its colour
groups = [[k, l] for k, _, l in KL]

# ════════ tap targets ════════
def st(x, y, c, aria, when=None, n=(0, -1)):
    s = dict(x=x, y=y, n=list(n), w=10, t='rec', l='', aria=aria, c=c, ions=[])
    if when: s['when'] = when
    return s
sites = [
  st(1180, PLX, 'gutwall', 'Myenteric (Auerbach) plexus'),
  st(GP[0], GP[1], 'esohisto', 'Esophageal glands proper', O('eso')),
  st(1300, 360, 'strsq', 'Stratified squamous epithelium', O('eso')),
  st(CJ + 240, 520, 'gastricglands', 'Cardiac glands', O('card')),
  st(X0 + 310, 470, 'gastricacid', 'Parietal cell', O('fund')),
  st(X0 + 310, 600, 'gastricglands', 'Fundic gland', O('fund')),
  st(X0 + 342, 566, 'gastrin', 'G cell', O('ant')),
  st(1700, 750, 'mucosaldef', 'Brunner glands', O('duo')),
  st(X0 + 345, 380, 'nutabsorb', 'Villus', O('duo', 'jej')),
  st(PP[0], PP[1], 'smallmucosa', 'Peyer patch', O('ile')),
  st(X0 + 290, 520, 'simcol', 'Colonic crypt', O('col')),
  st(1500, 400, 'simcol', 'Gallbladder epithelium', O('gb')),
]
sites[0].pop('when', None)
sites[0]['unless'] = O('gb')

notes = {
  '': 'From esophagus to anus the wall has the same four coats — mucosa, submucosa, muscularis externa, and serosa or adventitia — '
      'and most of what tells the segments apart sits in the mucosa. Pick a segment to see its signature and what moves there.',
  's:layers': 'Inside to out (MSMS): mucosa — epithelium, lamina propria, muscularis mucosae; submucosa — vessels, occasional glands, the '
              'submucosal (Meissner) plexus; muscularis externa — inner circular and outer longitudinal muscle with the myenteric '
              '(Auerbach) plexus between them, for motility; serosa if intraperitoneal, adventitia if attached. An erosion stays in the '
              'mucosa; an ulcer reaches the submucosa or deeper.',
  's:eso': 'Esophagus: nonkeratinized stratified squamous epithelium resists abrasion. Glands proper in the submucosa make a viscous, slightly '
           'acidic mucus that lubricates; cardiac glands in the lamina propria near the stomach make neutral mucus against reflux. The '
           'muscle is striated in the upper third (vagus, nucleus ambiguus), mixed in the middle and smooth below; the thoracic part has '
           'adventitia, not serosa.',
  's:card': 'Cardia: at the gastroesophageal junction the stratified squamous lining stops abruptly and simple columnar epithelium begins. '
            'Shallow pits lead into tortuous cardiac glands made almost entirely of mucus-secreting cells, which help protect the '
            'esophagus from refluxed acid. As everywhere in the stomach, an inner oblique muscle layer is added.',
  's:fund': 'Fundus and body: gastric pits open into long, straight fundic (gastric) glands. Eosinophilic parietal cells, crowded in the '
            'neck, secrete HCl and intrinsic factor; basophilic chief cells in the base secrete pepsinogen. Autoimmune gastritis '
            'targets this region — achlorhydria and pernicious anemia.',
  's:ant': 'Antrum and pylorus: deep pits fill about half the mucosa and open into coiled pyloric glands with wide lumina — mucous cells, G '
           'cells that release gastrin into the blood, and only occasional parietal cells. The circular muscle thickens into the pyloric '
           'sphincter, which hypertrophies in pyloric stenosis.',
  's:duo': 'Duodenum: villi and microvilli enlarge the absorptive surface; the crypts of Lieberkühn hold stem cells and Paneth cells. Its '
           'signature is Brunner glands in the submucosa — alkaline (pH 8.1–9.3), bicarbonate-rich mucus that neutralizes acid chyme and '
           'brings it near the pH pancreatic enzymes need.',
  's:jej': 'Jejunum: the tallest and most numerous plicae circulares — permanent folds with a core of submucosa — carry the villi, giving the '
           '“feathered” look on oral contrast and the largest surface for absorption. No Brunner glands in its submucosa.',
  's:ile': 'Ileum: Peyer patches — unencapsulated lymphoid nodules in the lamina propria and submucosa, opposite the mesentery — are covered '
           'by M cells that sample antigens; their B cells become IgA plasma cells. It has the most goblet cells of the small bowel, and '
           'the terminal ileum absorbs B12 and bile salts.',
  's:col': 'Colon: no villi and no plicae — a smooth surface of straight crypts packed with goblet cells, whose mucus eases ever more solid '
           'contents along, while absorptive cells take back water and electrolytes. Paneth cells are normally absent; the outer '
           'longitudinal muscle gathers into three teniae coli.',
  's:gb': 'Gallbladder: simple columnar cells on deep mucosal folds pump salt and water back, concentrating bile up to 10- to 20-fold. The wall has '
          'no muscularis mucosae and no submucosa — the lamina propria rests directly on randomly oriented smooth muscle. '
          'Rokitansky-Aschoff sinuses are mucosal outpouchings through that muscle.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='Villi', mods=[R(SMALL, 1), R(O('eso', 'card', 'fund', 'ant', 'col'), -1)]),
  dict(l='Goblet cells', mods=[R(O('ile', 'col'), 1)]),
  dict(l='Submucosal glands', mods=[R(O('eso', 'duo'), 1), R(O('card', 'fund', 'ant', 'jej', 'ile', 'col', 'gb'), -1)]),
  dict(l='Peyer patches', mods=[R(O('ile'), 1)]),
  dict(l='Parietal cells', mods=[R(O('fund'), 1), R(O('card', 'ant'), -1)]),
  dict(l='Striated muscle', mods=[R(O('eso'), 1), R(O('card', 'fund', 'ant', 'duo', 'jej', 'ile', 'col', 'gb'), -1)]),
  dict(l='Serosa', mods=[R(O('card', 'fund', 'ant', 'jej', 'ile'), 1), R(O('eso'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='s', label='Pick a segment', type='one', options=[
      ['layers', 'Mucosa · submucosa · muscularis · serosa', 'gutwall'],
      ['eso', 'Esophagus', 'esohisto'], ['card', 'Cardia', 'gastricglands'], ['fund', 'Fundus · body', 'gastricacid'],
      ['ant', 'Antrum · pylorus', 'gastrin'],
      ['duo', 'Duodenum', 'mucosaldef'], ['jej', 'Jejunum', 'nutabsorb'], ['ile', 'Ileum', 'smallmucosa'],
      ['col', 'Colon', 'simcol'], ['gb', 'Gallbladder', 'simcol']],
      sections=[['The layers', ['layers']], ['Esophagus & stomach', ['eso', 'card', 'fund', 'ant']],
                ['Small bowel', ['duo', 'jej', 'ile']], ['Colon & gallbladder', ['col', 'gb']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM GI course text (Ross & Pawlina 9e ch 17–18) and Exam 1 lecture notes · First Aid pp. 369, 378–379, 381, 386 · Robbins ch 17')

# ════════ the three new cards (cardgap #3, #7, #16) ════════
card('gastricglands', 'Gastric glands — cardiac, fundic & pyloric regions', 'reg', 'gwUp', 'The gland type, not the gross region, defines each zone', 1,
     'Histologically the stomach has three regions, named for their glands: <b>cardiac glands</b> around the esophageal opening, '
     '<b>pyloric glands</b> just before the pyloric sphincter, and <b>fundic (gastric) glands</b> everywhere between (fundus and body). '
     'All are mucosal glands in the lamina propria that open into the bases of the <b>gastric pits</b>.',
     ['Cardiac glands: tubular, tortuous, almost all <b>mucus-secreting</b> cells — with the esophageal cardiac glands they protect '
      'against reflux',
      'Fundic glands: long and straight — <b>parietal cells</b> (eosinophilic; HCl, intrinsic factor) crowd the neck, <b>chief cells</b> '
      '(basophilic; pepsinogen) the deep part',
      'Pyloric glands: <b>deep pits</b> (about half the mucosa), coiled glands with wide lumina, mucous cells and <b>G cells</b>; only '
      'occasional parietal cells',
      '<b>Surface mucous cells</b> line the surface and pits; <b>rugae</b> are longitudinal mucosal–submucosal folds that let the '
      'stomach distend; the muscularis adds an <b>inner oblique layer</b>',
      'Barrier: mucus gel with trapped bicarbonate, phospholipid, mucosal blood flow and epithelial <b>restitution</b> — '
      'prostaglandins E and I support nearly all of them, so NSAIDs weaken nearly all of them'],
     ['—'],
     ['Oblique muscle layer = stomach only'],
     [PW17, RB17],
     ['—'],
     ['gastric glands', 'cardiac glands', 'pyloric glands', 'pyloric region', 'gastric pits', 'oblique layer', 'restitution', 'mucus gel'],
     fa='369, 378, 379')
card('esohisto', 'Esophagus wall — glands, muscle & coats', 'reg', 'gwUp', 'Squamous lining, two mucous glands, striated above and smooth below', 1,
     'The esophagus is lined by <b>nonkeratinized stratified squamous</b> epithelium and has two kinds of mucous gland: '
     '<b>esophageal glands proper</b> in the submucosa and <b>esophageal cardiac glands</b> in the lamina propria.',
     ['Glands proper: submucosa, small compound tubuloalveolar, more in the upper half; slightly acidic, <b>viscous</b> mucus lubricates '
      'the lumen (viscous enough that transient cysts form in the ducts)',
      'Cardiac glands: lamina propria of the terminal (and often the initial) esophagus; <b>neutral mucus</b> protects against refluxed '
      'gastric contents',
      'Muscularis externa: upper third <b>striated</b>, middle third mixed, lower third <b>smooth</b>',
      'Striated part: somatic motor neurons of the vagus from the <b>nucleus ambiguus</b>; smooth part: visceral motor vagal neurons '
      'from the <b>dorsal motor nucleus</b>',
      'Outer coat: <b>adventitia</b> along the thoracic esophagus (no serosa); serosa only on the short (1–2 cm) abdominal segment'],
     ['—'],
     ['Upper third striated, lower third smooth'],
     [PW17],
     ['—'],
     ['esophageal glands proper', 'esophageal cardiac glands', 'esophageal cardiac gland', 'thoracic esophagus', 'upper third of the esophagus'],
     fa='369')
card('smallmucosa', 'Small-bowel mucosa — villi, crypts, Paneth cells & Peyer patches', 'reg', 'gwSm', 'Folds, villi and microvilli; crypts with stem and Paneth cells', 1,
     'Plicae circulares (folds with a submucosal core), <b>villi</b> (mucosal projections with a lacteal) and microvilli multiply the '
     'absorptive surface. Between the villi, <b>crypts of Lieberkühn</b> hold the stem cells that renew the lining every few days and '
     '<b>Paneth cells</b> at their bases.',
     ['<b>Paneth cells</b>: base of the crypts, bright acidophilic granules — lysozyme, α-defensins, TNF (innate immunity); normally '
      'absent from the human colon',
      '<b>Peyer patches</b> (ileum): unencapsulated lymphoid nodules in the lamina propria and submucosa, opposite the mesentery; '
      '<b>M cells</b> on the dome sample antigens; their B cells become IgA plasma cells',
      'Goblet cells increase from duodenum to ileum — the ileum has the most in the small bowel',
      'Duodenum: <b>Brunner glands</b> in the submucosa · jejunum: tallest, most numerous plicae (“feathered” on contrast)'],
     ['—'],
     ['Paneth cells at the crypt base; Peyer patches in the ileum'],
     [PW17],
     ['—'],
     ['paneth cells', 'paneth cell', 'peyer patches', 'peyer patch', 'crypts of lieberkuhn'],
     fa='369, 381')

MAP = dict(
  id='gutwallsim', title='Gut Wall by Segment in Motion', topic='gi', after='gitract',
  sub='Pick a segment — esophagus, cardia, fundus, antrum, duodenum, jejunum, ileum, colon or gallbladder — and the cut through its wall '
      'redraws: epithelium, glands, villi, Peyer patches, the muscle and the outer coat, with mucus, acid, gastrin, bicarbonate, '
      'nutrients, antigens or water moving where that segment makes or takes them. Tap a structure for its card',
  w=3480, h=1780,
  fa='369, 378, 379, 381, 386', src=[PW17, PW18, RB17],
  lanes=[('gwLay', 'Layers & epithelia', 'glycolysis'), ('gwUp', 'Esophagus & stomach', 'tca'), ('gwSm', 'Small bowel, colon & gallbladder', 'gluconeo')],
  comps=[],
  nodes=[
    ('gw1', 'Gut wall layers', 260, 1560, 'gwLay', 'MSMS · plexuses', ['gutwall'], 'hub'),
    ('gw2', 'Esophagus wall', 540, 1560, 'gwUp', 'glands · striated → smooth', ['esohisto']),
    ('gw3', 'Stratified squamous', 820, 1560, 'gwLay', 'nonkeratinized', ['strsq']),
    ('gw4', 'Barrett · metaplasia', 1100, 1560, 'gwUp', 'columnar + goblet cells', ['barrett', 'epimeta']),
    ('gw5', 'Gastric glands', 1380, 1560, 'gwUp', 'cardiac · fundic · pyloric', ['gastricglands']),
    ('gw6', 'Parietal & chief cells', 1660, 1560, 'gwUp', 'acid · autoimmune gastritis', ['gastricacid', 'gastritis']),
    ('gw7', 'G cells · gastrin', 1940, 1560, 'gwUp', 'antrum', ['gastrin']),
    ('gw8', 'Pyloric stenosis', 2220, 1560, 'gwUp', 'circular muscle', ['pyloric']),
    ('gw9', 'Brunner glands · HCO₃⁻', 260, 1690, 'gwSm', 'duodenal submucosa', ['mucosaldef']),
    ('gw10', 'Villi, crypts, Peyer', 540, 1690, 'gwSm', 'Paneth · M cells', ['smallmucosa']),
    ('gw11', 'Absorption by segment', 820, 1690, 'gwSm', 'iron · folate · B12', ['nutabsorb']),
    ('gw12', 'Simple columnar', 1100, 1690, 'gwLay', 'stomach to rectum · gallbladder', ['simcol']),
    ('gw13', 'Microvilli · junctions', 1380, 1690, 'gwLay', 'brush border · tight junctions', ['apical', 'celljunctions']),
    ('gw14', 'Serosa · lamina propria', 1660, 1690, 'gwLay', 'mesothelium · loose CT', ['simsq', 'ctproper']),
  ],
  panels=[
    (2420, 900, 1000, 'Name the segment (First Aid p. 369 · Ross & Pawlina ch 17–18)', [
      ('Stratified squamous + submucosal glands', 'esophagus'),
      ('Pits and glands, no villi', 'stomach — parietal cells: fundus/body'),
      ('Villi + Brunner glands', 'duodenum'),
      ('Tallest plicae circulares', 'jejunum'),
      ('Peyer patches, most goblet cells', 'ileum'),
      ('Crypts and goblet cells, no villi', 'colon'),
      ('No muscularis mucosae or submucosa', 'gallbladder')])],
  dyn=dyn,
)
