# m57 — Viral Hepatitis Serology in Motion (dynamic map, kit data)
# An infected hepatocyte releases virus and viral antigens into the sinusoid blood; a plasma cell answers with antibodies;
# both end up in the serum sample that is tested. Underneath, a schematic time course (drawn from the course text, not a
# copy of any figure) shows where on the curves each pattern sits. One `one` switch (10 options, 4 sections, teaching
# order): hepatitis A, E · acute HBV, window period, recovered, chronic, vaccinated · HDV coinfection, superinfection ·
# hepatitis C. Readouts are test results: ↑ positive · ↓ negative · "–" where no source commits. "Usually chronic":
# ↑ the usual course is chronic infection · ↓ the usual course is clearance.
#
# Sources (all read in the corpus; course text wins):
#   GI Exam 1 lecture notes, SDL 15 section 2 (corpus/gastro/course_exam1_lecture_notes.txt, pp. 83–85): HAV naked +ssRNA
#     picornavirus, TIM-1, fecal shedding late in incubation (2–6 wk), IgM anti-HAV at symptom onset, declines within 3–6
#     months, IgG for life, never chronic · HBV entry HBsAg→NTCP; HBsAg first, before symptoms, peaks in acute disease, gone
#     by 12–24 wk in resolving cases; HBeAg + HBV DNA shortly after HBsAg = replication, infectivity; IgM anti-HBc in the
#     window after HBsAg clears, before anti-HBs; anti-HBs after resolution = lifelong immunity, basis of the vaccine;
#     HBsAg > 6 months = chronic; adults 5–10% chronic, perinatal ~90% · HCV RNA 1–3 wk with ALT, anti-HCV 3–6 wk, RNA
#     > 6 months = chronic, 80–90% chronic, ~85% asymptomatic acute · HDV needs HBsAg envelope; HDV RNA + IgM anti-HDV in
#     acute disease; anti-HDV + HBsAg persist in chronic delta; coinfection usually self-limited, superinfection chronic
#     in > 80% · HEV naked +ssRNA, RNA in stool and serum late incubation (4–5 wk), IgM anti-HEV with symptoms, then IgG;
#     self-limited if immunocompetent; pregnancy mortality approaching 20%; chronic only if immunocompromised.
#   Robbins ch 18 (= course_sdl_15_19_patho.txt pp. 23–36): the same timings; anti-HBs not produced in cases that become
#     chronic; anti-HBe = infection waning; HBeAg persistence = continued replication; "healthy carrier" HBsAg + anti-HBe,
#     no HBeAg; HAV and HEV injury from the host response (CTL, NK for HAV), HBV injury mostly CD8⁺ T cells; HCV
#     fluctuating aminotransferases; anti-HCV may persist without RNA after clearance and may fade; HDV superinfection
#     suppresses HBV replication in its acute phase; Table 18.3 (incubation, chronic frequency).
#   First Aid 2025 p. 170 (families, transmission, HDV depends on the HBsAg coat, HEV pregnancy) · p. 171 (marker meanings:
#     IgM anti-HAV best test for acute HAV; HBsAg = infection; anti-HBs = immunity by vaccine or recovery; anti-HBc IgM
#     acute/recent, IgG prior or chronic, IgM may be the sole ⊕ marker in the window; HBeAg = replication; anti-HBe low
#     transmissibility; extrahepatic: HBV PAN, HCV cryoglobulinemia).
#   Bootcamp.com Microbiology — DNA Viruses (window: HBsAg −, anti-HBs −, IgM anti-HBc +; anti-HBc + = infection, past
#     or current; subunit vaccine contains HBsAg) · — Negative-sense RNA Viruses (HDV coat of HBsAg; coinfection vs
#     superinfection; vaccination against HBV protects against HDV).
# Arrows that were left "–" (no source commits): HBeAg in the window, in chronic HBV (positive only while replicating),
#   in recovery and in HDV; IgM anti-HBc in chronic HBV, recovery, superinfection; IgG anti-HBc in acute HBV and the
#   window; every HBV marker in the HAV, HEV and HCV patterns; IgM anti-HAV in HEV.
# Vaccinated: HBsAg ↓ (no infection — FA: HBsAg indicates infection) and IgG anti-HBc ↓ (the vaccine holds only HBsAg;
#   anti-HBc marks infection — Bootcamp).
# Cuts: HAV leaving the liver in bile (no source in the corpus says how the virus reaches the stool — the gut is drawn
#   on its own, with "shed in stool"); the spec's `entero` pin (Coxsackie/echovirus card — not about hepatitis).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

RB18 = full('Robbins', 18)
BC_DNA = 'Bootcamp.com Microbiology — DNA Viruses'
BC_NEG = 'Bootcamp.com Microbiology — Negative-sense RNA Viruses'
SRC = [RB18, BC_DNA, BC_NEG]

O = lambda *k: ['v:' + x for x in k]
HBVIN = O('hbac', 'hbch', 'hdco', 'hdsu')            # HBV replicating in the cell
FECAL = O('hav', 'hev')
HBVGRAPH_OFF = O('hav', 'hev', 'hcv', 'vax')         # the HBV time course gives way to these

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
TAG = 'nf-l2 dyn-tag'

# ════════ 1. the hepatocyte ════════
add('<rect x="340" y="270" width="540" height="470" rx="60" class="dyn-cell"/>')
shapes.append(dict(membrane='M400 270 H820 Q880 270 880 330 V680 Q880 740 820 740 H400 Q340 740 340 680 V330 Q340 270 400 270 Z', w=18))
text('Hepatocyte', 340, 236, 'dyn-big')
add('<ellipse cx="580" cy="500" rx="120" ry="88" class="dyn-soft"/>')
text('nucleus', 580, 610, 'dyn-cap', 'middle')
add('<circle cx="580" cy="490" r="28" fill="none" style="stroke:var(--dk1);stroke-width:6"/>', when=HBVIN)
text('cccDNA', 580, 548, 'nf-l1', 'middle', when=HBVIN)
CELL = dict(
  hav='HAV replicates — not cytopathic; T cells and NK cells do the damage',
  hev='HEV replicates — the damage comes from the host response',
  hbac='HBV genome kept in the nucleus as cccDNA; copied back through RNA',
  win='HBsAg already gone — the infection is being cleared',
  hbre='virus cleared — immunity remains',
  hbch='HBsAg still made after 6 months — chronic infection',
  vax='never infected',
  hdco='HBV and HDV arrive together',
  hdsu='HDV lands on a chronic HBsAg carrier',
  hcv='+RNA copied in the cytoplasm — no DNA stage')
for k, s in CELL.items(): text(s, 610, 700, TAG, 'middle', when=O(k))

# ════════ 2. the sinusoid → blood → the serum sample ════════
VES = 'M880 380 H2180 V452'
shapes.append(dict(vessel=VES, w=56))
text('sinusoid → central vein → the blood', 1300, 336, 'nf-l2')
add('<path d="M2140 452 V690 Q2140 730 2180 730 Q2220 730 2220 690 V452" class="dyn-line" style="stroke-width:4"/>'
    '<path d="M2144 560 H2216 V690 Q2216 726 2180 726 Q2144 726 2144 690 Z" fill="var(--dk10)" opacity=".25"/>')
text('Serum sample', 2180, 770, 'nf-l1', 'middle')
text('the tests read it', 2180, 788, 'nf-l2', 'middle')
BLOOD = dict(
  hav='brief viremia · IgM anti-HAV rises with the symptoms',
  hev='HEV RNA in serum and stool · IgM anti-HEV with the symptoms',
  hbac='Dane particles · spare HBsAg spheres · secreted HBeAg · IgM anti-HBc',
  win='no HBsAg, no anti-HBs yet — only IgM anti-HBc',
  hbre='anti-HBs (protective) · IgG anti-HBc (marks the past infection)',
  hbch='HBsAg for over 6 months · IgG anti-HBc · no anti-HBs',
  vax='anti-HBs only — no HBsAg, no anti-HBc',
  hdco='HBV + HDV in HBsAg coats · IgM anti-HBc · IgM anti-HDV',
  hdsu='HDV in HBsAg coats · HBsAg · IgG anti-HBc · anti-HDV',
  hcv='HCV RNA from 1–3 weeks · anti-HCV from 3–6 weeks')
for k, s in BLOOD.items(): text(s, 1000, 466, TAG, when=O(k))

# ════════ 3. the immune side: a CD8⁺ T cell and a plasma cell ════════
add('<circle cx="980" cy="650" r="36" class="dyn-cell" style="stroke:var(--dk2)"/><circle cx="986" cy="646" r="16" fill="var(--dk2)" opacity=".5"/>')
text('CD8⁺ T cell', 1030, 646, 'nf-l1')
text('kills infected hepatocytes — the liver injury', 1030, 664, 'nf-l2', when=O('hav', 'hbac', 'hbch', 'hdco', 'hdsu'))
add('<ellipse cx="1560" cy="720" rx="150" ry="90" class="dyn-cell" style="stroke:var(--dk6)"/>'
    '<path d="M1450 690 Q1500 676 1540 690 M1446 744 Q1500 760 1540 744 M1600 672 Q1640 660 1676 676" class="dyn-line" style="stroke:var(--dk6);stroke-width:2;opacity:.6"/>'
    '<circle cx="1620" cy="722" r="26" fill="var(--dk6)" opacity=".3"/>')
shapes.append(dict(vessel='M1560 632 V408', w=12, color='--dk6'))
text('Plasma cell', 1500, 718, 'nf-l1', 'middle')
text('makes the antibodies', 1500, 736, 'nf-l2', 'middle')
# vaccine (recombinant HBsAg)
add('<rect x="1150" y="858" width="150" height="30" rx="6" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M1300 873 L1420 790" class="dyn-line" style="stroke:var(--dk8);stroke-width:3"/>'
    '<path d="M1150 873 H1112 M1112 858 V888" class="dyn-line" style="stroke:var(--dk8);stroke-width:4"/>', when=O('vax'))
text('Recombinant HBsAg vaccine', 1112, 922, 'nf-l1', when=O('vax'))

# ════════ 4. the gut (A and E) ════════
GUT = 'M200 870 C300 810 420 930 520 870 S720 810 840 870'
add(f'<path d="{GUT}" class="nf-wall" stroke-width="46" style="stroke:var(--dk9)"/><path d="{GUT}" class="nf-lumen" stroke-width="34"/>', when=FECAL)
text('Gut — swallowed (fecal-oral), then shed in stool late in the incubation', 200, 950, TAG, when=FECAL)

# ════════ 5. the time course (schematic) ════════
def smooth(u): u = max(0.0, min(1.0, u)); return u * u * (3 - 2 * u)
def hump(a, p, b, h): return lambda t: 0 if t <= a or t >= b else h * (smooth((t - a) / (p - a)) if t < p else smooth((b - t) / (b - p)))
def rise(a, b, h): return lambda t: 0 if t <= a else h * smooth((t - a) / (b - a))
def wave(a, h, amp): return lambda t: 0 if t <= a else min(1, (t - a) / 0.06) * (h + amp * __import__('math').sin((t - a) * 38))
PANELS = dict(L=(160, 1080, 1020, 660), R=(1220, 1080, 1020, 660))
def geo(p):
    x0, y0, w, h = PANELS[p]; base = y0 + h - 60; ph = h - 150
    return (lambda t: x0 + 50 + t * (w - 90)), (lambda v: base - v * ph), base
def curve(p, f, a, b, col, when=None, unless=None, dash=False):
    X, Y, _ = geo(p); n = 80
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    d = 'M' + ' L'.join(f'{x:.0f} {y:.0f}' for x, y in pts)
    add(f'<path d="{d}" fill="none" style="stroke:var({col});stroke-width:5;stroke-linejoin:round;stroke-linecap:round'
        + (';stroke-dasharray:10 7' if dash else '') + '"/>', when=when, unless=unless)
def lab(p, t, v, s, anchor='middle', when=None, unless=None, cls='nf-l1'):
    X, Y, _ = geo(p); text(s, round(X(t)), round(Y(v)), cls, anchor, when=when, unless=unless)
def frame(p, title, when=None, unless=None, axes=True):
    x0, y0, w, h = PANELS[p]; X, Y, base = geo(p)
    if not axes:
        add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="22" class="dyn-soft"/>', when=when, unless=unless)
        text(title, x0 + 26, y0 + 36, 'dyn-big', when=when, unless=unless); return
    add(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="22" class="dyn-soft"/>'
        f'<path d="M{X(0):.0f} {Y(1.02):.0f} V{base} H{X(1):.0f}" class="dyn-line" style="stroke-width:2"/>', when=when, unless=unless)
    text(title, x0 + 26, y0 + 36, 'dyn-big', when=when, unless=unless)
    text('exposure', round(X(0)), base + 24, 'nf-l2', 'middle', when=when, unless=unless)
    text('time →', round(X(1)), base + 24, 'nf-l2', 'end', when=when, unless=unless)
def band(p, a, b, s, when):
    X, Y, base = geo(p)
    add(f'<rect x="{X(a):.0f}" y="{Y(1.02):.0f}" width="{X(b) - X(a):.0f}" height="{base - Y(1.02):.0f}" fill="var(--accent)" opacity=".13"/>'
        f'<path d="M{X(a):.0f} {Y(1.02):.0f} H{X(b):.0f}" class="dyn-hl"/>', when=when)
    text(s, round((X(a) + X(b)) / 2), round(Y(1.02)) - 12, TAG, 'middle', when=when)
def vline(p, t, s, when=None, unless=None):
    X, Y, base = geo(p)
    add(f'<path d="M{X(t):.0f} {base} V{Y(1.02):.0f}" class="dyn-dash"/>', when=when, unless=unless)
    text(s, round(X(t)) + 8, round(Y(0.98)), 'nf-l2', when=when, unless=unless)
def symp(p, a, b, s, when=None, unless=None):
    X, Y, base = geo(p)
    add(f'<rect x="{X(a):.0f}" y="{base + 34}" width="{X(b) - X(a):.0f}" height="8" rx="4" fill="var(--ink-3)" opacity=".5"/>', when=when, unless=unless)
    text(s, round((X(a) + X(b)) / 2), base + 26, 'nf-l2', 'middle', when=when, unless=unless)

U = dict(unless=HBVGRAPH_OFF)
# — acute HBV that resolves (left) —
frame('L', 'Acute hepatitis B that resolves', **U)
curve('L', hump(0.08, 0.30, 0.50, 0.85), 0.08, 0.50, '--dk3', **U); lab('L', 0.30, 0.88, 'HBsAg', **U)
curve('L', hump(0.12, 0.27, 0.42, 0.50), 0.12, 0.42, '--dk5', **U); lab('L', 0.17, 0.42, 'HBeAg', 'end', **U)
curve('L', hump(0.22, 0.40, 0.80, 0.60), 0.22, 0.80, '--dk4', **U); lab('L', 0.66, 0.46, 'IgM anti-HBc', 'start', **U)
curve('L', rise(0.28, 0.60, 0.74), 0.28, 1, '--dk6', **U); lab('L', 1, 0.78, 'IgG anti-HBc', 'end', **U)
curve('L', rise(0.42, 0.66, 0.30), 0.42, 1, '--dk12', **U); lab('L', 1, 0.20, 'anti-HBe', 'end', **U)
curve('L', rise(0.60, 0.85, 0.55), 0.60, 1, '--dk8', **U); lab('L', 1, 0.59, 'anti-HBs', 'end', **U)
X, Y, BASE = geo('L')
text('window', round((X(0.50) + X(0.60)) / 2), round(Y(0.05)), 'nf-l2', 'middle', **U)
add(f'<path d="M{X(0.50):.0f} {BASE} V{Y(0.95):.0f} M{X(0.60):.0f} {BASE} V{Y(0.95):.0f}" class="dyn-dash" style="opacity:.6"/>', **U)
symp('L', 0.22, 0.45, 'symptoms · ALT ↑', **U)
# HDV coinfection on the acute curves
curve('L', hump(0.24, 0.34, 0.50, 0.30), 0.24, 0.50, '--dk2', when=O('hdco'), dash=True)
lab('L', 0.34, 0.16, 'HDV RNA · IgM anti-HDV', 'middle', when=O('hdco'), cls='nf-l2')
# — chronic HBV (right) —
frame('R', 'Chronic hepatitis B', **U)
curve('R', rise(0.08, 0.30, 0.85), 0.08, 1, '--dk3', **U); lab('R', 0.97, 0.89, 'HBsAg', 'end', **U)
curve('R', rise(0.12, 0.30, 0.50), 0.12, 1, '--dk5', dash=True, **U); lab('R', 0.97, 0.54, 'HBeAg (while replicating)', 'end', **U)
curve('R', hump(0.22, 0.40, 0.75, 0.38), 0.22, 0.75, '--dk4', **U); lab('R', 0.40, 0.41, 'IgM anti-HBc', 'middle', **U)
curve('R', rise(0.28, 0.60, 0.70), 0.28, 1, '--dk6', **U); lab('R', 0.97, 0.74, 'IgG anti-HBc', 'end', **U)
lab('R', 0.97, 0.10, 'no anti-HBs', 'end', cls='nf-l2', **U)
vline('R', 0.55, '6 months', **U)
curve('R', rise(0.66, 0.80, 0.28), 0.66, 1, '--dk2', when=O('hdsu'), dash=True)
lab('R', 0.80, 0.33, 'HDV arrives · anti-HDV', 'middle', when=O('hdsu'), cls='nf-l2')
# — hepatitis A or E (left) —
F = dict(when=FECAL)
frame('L', 'Acute hepatitis A or E — self-limited', **F)
curve('L', hump(0.06, 0.22, 0.36, 0.50), 0.06, 0.36, '--dk9', **F)
lab('L', 0.16, 0.56, 'HAV in stool', when=O('hav')); lab('L', 0.16, 0.56, 'HEV RNA in stool + serum', when=O('hev'))
curve('L', hump(0.24, 0.36, 0.78, 0.75), 0.24, 0.78, '--dk4', **F)
lab('L', 0.36, 0.79, 'IgM anti-HAV', when=O('hav')); lab('L', 0.36, 0.79, 'IgM anti-HEV', when=O('hev'))
curve('L', rise(0.36, 0.70, 0.55), 0.36, 1, '--dk6', **F)
lab('L', 1, 0.59, 'IgG anti-HAV — lifelong', 'end', when=O('hav')); lab('L', 1, 0.59, 'IgG anti-HEV', 'end', when=O('hev'))
symp('L', 0.24, 0.45, 'symptoms · ALT ↑', **F)
frame('R', 'No chronic phase', axes=False, **F)
x0, y0 = PANELS['R'][:2]
text('no carrier state — the infection always ends', x0 + 40, y0 + 120, 'nf-l1', when=O('hav'))
text('HAV: recovery within 3 months in nearly all; acute liver failure 0.1–0.3%', x0 + 40, y0 + 150, 'nf-l2', when=O('hav'))
text('self-limited in immunocompetent hosts', x0 + 40, y0 + 120, 'nf-l1', when=O('hev'))
text('chronic HEV only with immunosuppression (transplant, AIDS)', x0 + 40, y0 + 150, 'nf-l2', when=O('hev'))
text('pregnant: mortality approaching 20%', x0 + 40, y0 + 200, 'nf-l1 dyn-tag', when=O('hev'))
# — hepatitis C (left clears, right chronic) —
C = dict(when=O('hcv'))
frame('L', 'Hepatitis C that clears — the 10–20%', **C)
curve('L', hump(0.03, 0.15, 0.45, 0.70), 0.03, 0.45, '--dk7', **C); lab('L', 0.15, 0.74, 'HCV RNA', **C)
curve('L', rise(0.12, 0.35, 0.55), 0.12, 1, '--dk10', **C); lab('L', 1, 0.59, 'anti-HCV — may fade', 'end', **C)
frame('R', 'Chronic hepatitis C — 80–90%', **C)
curve('R', rise(0.03, 0.15, 0.70), 0.03, 1, '--dk7', **C); lab('R', 0.97, 0.74, 'HCV RNA', 'end', **C)
curve('R', rise(0.12, 0.35, 0.48), 0.12, 1, '--dk10', **C); lab('R', 0.97, 0.53, 'anti-HCV', 'end', **C)
curve('R', wave(0.05, 0.24, 0.06), 0.05, 1, '--ink-3', dash=True, **C); lab('R', 0.97, 0.08, 'ALT fluctuates', 'end', cls='nf-l2', **C)
vline('R', 0.55, '6 months — RNA still there = chronic', **C)
# — vaccinated (left) —
V = dict(when=O('vax'))
frame('L', 'Vaccinated against hepatitis B', **V)
curve('L', rise(0.15, 0.45, 0.65), 0.15, 1, '--dk8', **V); lab('L', 1, 0.69, 'anti-HBs', 'end', **V)
lab('L', 0.05, 0.10, 'vaccine', 'start', cls='nf-l2', **V)
frame('R', 'What stays negative', axes=False, **V)
text('HBsAg — no infection', x0 + 40, y0 + 120, 'nf-l1', **V)
text('anti-HBc — the vaccine holds only HBsAg, so no antibody to the core', x0 + 40, y0 + 150, 'nf-l2', **V)
text('anti-HBs alone = vaccinated · anti-HBs + IgG anti-HBc = recovered', x0 + 40, y0 + 200, 'nf-l1 dyn-tag', **V)
# — where this pattern sits —
band('L', 0.22, 0.42, 'acute', O('hbac', 'hdco'))
band('L', 0.50, 0.60, 'here', O('win'))
band('L', 0.86, 1.0, 'recovered', O('hbre'))
band('R', 0.70, 0.97, 'chronic', O('hbch', 'hdsu', 'hcv'))
band('L', 0.24, 0.45, 'acute', FECAL)
band('L', 0.60, 1.0, 'immune', O('vax'))
text('Schematic, from the timings in the course notes (SDL 15) and Robbins ch 18', 160, 1770, 'dyn-cap')

# ════════ particles ════════
# each kind is its own "Show" group, so the chips double as the colour key (the drafts check.py takes 2-element kinds)
KL = [('vir', '--dk1', 'Dane particle'), ('hbs', '--dk3', 'HBsAg'), ('hbe', '--dk5', 'HBeAg'), ('hdv', '--dk2', 'HDV'),
      ('hcv', '--dk7', 'HCV'), ('hav', '--dk9', 'HAV · HEV'), ('igm', '--dk4', 'IgM'), ('igg', '--dk6', 'IgG anti-HBc'),
      ('ahbs', '--dk8', 'Anti-HBs'), ('ahcv', '--dk10', 'Anti-HCV'), ('ahdv', '--dk11', 'Anti-HDV')]
kinds = {k: [k, c] for k, c, _ in KL}
groups = [[k, l] for k, _, l in KL]
def m(when, **kw): return dict(when=when if isinstance(when, list) else [when], **kw)
flows = [
  # what the hepatocyte puts into the blood
  dict(d=VES, len=1372, base={}, mods=[
      m(O('hbac'), set=dict(vir=3, hbs=6, hbe=3)), m(O('hbch'), set=dict(vir=3, hbs=6, hbe=2)),
      m(O('hdco'), set=dict(vir=2, hbs=5, hbe=2, hdv=3)), m(O('hdsu'), set=dict(vir=1, hbs=5, hdv=4)),
      m(O('hcv'), set=dict(hcv=6)), m(FECAL, set=dict(hav=1))]),
  # antibodies from the plasma cell
  dict(d='M1560 612 V380 H2180 V452', len=912, speed=120, base={}, mods=[
      m(FECAL + O('hbac', 'win'), set=dict(igm=5)), m(O('hbch'), set=dict(igg=4)), m(O('hbre'), set=dict(igg=3, ahbs=4)),
      m(O('vax'), set=dict(ahbs=5)), m(O('hdco'), set=dict(igm=4, ahdv=2)), m(O('hdsu'), set=dict(igg=4, ahdv=2)),
      m(O('hcv'), set=dict(ahcv=4))]),
  # the gut: swallowed, then shed in the stool
  dict(d=GUT, len=700, speed=90, when=FECAL, base=dict(hav=5)),
  # the vaccine's HBsAg to the plasma cell
  dict(d='M1300 873 L1420 790', len=146, speed=70, when=O('vax'), base=dict(hbs=3)),
]

# ════════ sites ════════
sites = [
  dict(x=720, y=270, n=[0, -1], w=18, t='co', l='NTCP', s='HBV entry receptor — binds HBsAg', ions=[['vir', 'in', 1]], reach=40,
       c='hbv', when=O('hbac', 'hbch')),
  dict(x=720, y=270, n=[0, -1], w=18, t='co', l='NTCP', s='HDV enters wearing HBsAg', ions=[['vir', 'in', 1], ['hdv', 'in', 1]], reach=40,
       c='hbv', when=O('hdco', 'hdsu')),
  dict(x=880, y=380, n=[1, 0], w=18, t='ex', l='Released', s='into the sinusoid', ions=[['hbs', 'out', 2], ['hbe', 'out', 1]], cross=True,
       reach=30, lx=900, ly=300, la='start', c='hbv', when=O('hbac', 'hbch', 'hdco')),
  dict(x=880, y=380, n=[1, 0], w=18, t='ex', l='Released', s='into the sinusoid', ions=[['hbs', 'out', 1], ['hdv', 'out', 1]], cross=True,
       reach=30, lx=900, ly=300, la='start', c='hbv', when=O('hdsu')),
  dict(x=880, y=380, n=[1, 0], w=18, t='ex', l='Released', s='into the sinusoid', ions=[['hcv', 'out', 2]], cross=True,
       reach=30, lx=900, ly=300, la='start', c='hcv', when=O('hcv')),
  dict(x=880, y=380, n=[1, 0], w=18, t='ex', l='Released', s='brief viremia', ions=[['hav', 'out', 1]], cross=True,
       reach=30, lx=900, ly=300, la='start', c='hav', when=FECAL),
  dict(x=1560, y=630, n=[0, -1], w=18, t='ex', l='Antibodies out', s='IgM first, then IgG', ions=[['igm', 'out', 1]], reach=30,
       lx=1590, ly=566, la='start', c='hav', when=FECAL),
  dict(x=1560, y=630, n=[0, -1], w=18, t='ex', l='Antibodies out', s='IgM anti-HBc = acute', ions=[['igm', 'out', 1]], reach=30,
       lx=1590, ly=566, la='start', c='hbv', when=O('hbac', 'win', 'hdco')),
  dict(x=1560, y=630, n=[0, -1], w=18, t='ex', l='Antibodies out', s='IgG anti-HBc = past or chronic', ions=[['igg', 'out', 1]], reach=30,
       lx=1590, ly=566, la='start', c='hbv', when=O('hbch', 'hdsu')),
  dict(x=1560, y=630, n=[0, -1], w=18, t='ex', l='Antibodies out', s='anti-HBs = immune', ions=[['ahbs', 'out', 1]], reach=30,
       lx=1590, ly=566, la='start', c='hbv', when=O('hbre', 'vax')),
  dict(x=1560, y=630, n=[0, -1], w=18, t='ex', l='Antibodies out', s='anti-HCV — variants escape it', ions=[['ahcv', 'out', 1]], reach=30,
       lx=1590, ly=566, la='start', c='hcv', when=O('hcv')),
]

notes = {
  '': 'Viral hepatitis is read from the blood. An infected hepatocyte releases virus and viral antigens into the sinusoid; '
      'plasma cells answer with antibodies, IgM first and IgG later. Which markers are positive, and which antibody class, '
      'names the virus and the stage. Pick a pattern. In the results ↑ means positive, ↓ negative.',
  'v:hav': 'Hepatitis A: a naked +ssRNA picornavirus, spread fecal-orally and shed in stool late in the 2–6 week incubation. '
           'IgM anti-HAV appears with the symptoms and is the test for acute infection; it fades within 3–6 months, and IgG '
           'anti-HAV stays for life. Never chronic, no carrier state.',
  'v:hev': 'Hepatitis E: a naked +ssRNA hepevirus, waterborne and fecal-oral (also undercooked pork). IgM anti-HEV rises with '
           'the symptoms, then IgG. It is self-limited in healthy hosts, chronic only with immunosuppression, but mortality '
           'approaches 20% in pregnant patients.',
  'v:hbac': 'Acute hepatitis B: HBsAg appears first, before symptoms, and peaks in the acute illness. HBeAg follows (active '
            'replication, high infectivity) and IgM anti-HBc marks a recent infection. Anti-HBs is not there yet. Most adults '
            'clear it; 5–10% become chronic.',
  'v:win': 'Window period: HBsAg has cleared but anti-HBs has not yet appeared, so both are negative. IgM anti-HBc may be the '
           'only positive marker — the test that catches an acute infection here.',
  'v:hbre': 'Recovered hepatitis B: HBsAg is gone, anti-HBs has risen and protects for life, and IgG anti-HBc stays as the '
            'record of a real infection. The anti-HBc is what tells recovery from vaccination.',
  'v:hbch': 'Chronic hepatitis B: HBsAg persisting beyond 6 months defines it. Anti-HBs never forms and anti-HBc is IgG. '
            'HBeAg stays positive while the virus replicates (infectious); a carrier with HBsAg and anti-HBe but no HBeAg '
            'replicates little. Risk of cirrhosis and HCC.',
  'v:vax': 'Vaccinated: the vaccine is recombinant HBsAg, so the only antibody made is anti-HBs. HBsAg and anti-HBc stay '
           'negative — anti-HBs alone means vaccinated, not infected. HBV vaccination also protects against HDV.',
  'v:hdco': 'HDV coinfection: HBV and HDV arrive together. HDV is a defective RNA virus that borrows the HBsAg coat to enter '
            'and leave hepatocytes. It looks like acute hepatitis B (HBsAg, IgM anti-HBc) plus HDV RNA and IgM anti-HDV, and '
            'usually clears.',
  'v:hdsu': 'HDV superinfection: HDV infects someone already carrying HBsAg (chronic HBV, so IgG anti-HBc). About 30–50 days '
            'later comes a severe acute hepatitis or a flare, and chronic HDV follows in more than 80%, speeding cirrhosis and HCC.',
  'v:hcv': 'Hepatitis C: HCV RNA is in the blood within 1–3 weeks with the ALT rise; anti-HCV follows at 3–6 weeks, but '
           'new variants escape it. 80–90% stay chronic — RNA still present after 6 months (GI course; Robbins 4–6 months) — with fluctuating ALT. Screen with anti-HCV, '
           'confirm with HCV RNA.',
}

R = lambda when, d: dict(when=when if isinstance(when, list) else [when], d=d)
readouts = [
  dict(l='HBsAg', mods=[R(O('hbac', 'hbch', 'hdco', 'hdsu'), 1), R(O('win', 'hbre', 'vax'), -1)]),
  dict(l='Anti-HBs', mods=[R(O('hbre', 'vax'), 1), R(O('hbac', 'win', 'hbch'), -1)]),
  dict(l='HBeAg', mods=[R(O('hbac'), 1)]),
  dict(l='IgM anti-HBc', mods=[R(O('hbac', 'win', 'hdco'), 1)]),
  dict(l='IgG anti-HBc', mods=[R(O('hbch', 'hbre', 'hdsu'), 1), R(O('vax'), -1)]),
  dict(l='IgM anti-HAV', mods=[R(O('hav'), 1)]),
  dict(l='Usually chronic', mods=[R(O('hbch', 'hdsu', 'hcv'), 1), R(O('hav', 'hev', 'hbac', 'hbre', 'hdco'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='v', label='Pattern', type='one', options=[
                ['hav', 'Hepatitis A', 'hav'], ['hev', 'Hepatitis E', 'hav'],
                ['hbac', 'Acute hepatitis B', 'hbv'], ['win', 'Window period', 'hbv'], ['hbre', 'Recovered hepatitis B', 'hbv'],
                ['hbch', 'Chronic hepatitis B', 'hbv'], ['vax', 'HBV vaccinated', 'hbv'],
                ['hdco', 'HDV coinfection', 'hbv'], ['hdsu', 'HDV superinfection', 'hbv'],
                ['hcv', 'Hepatitis C', 'hcv']],
                 sections=[['Fecal-oral — A and E', ['hav', 'hev']],
                           ['Hepatitis B serology', ['hbac', 'win', 'hbre', 'hbch', 'vax']],
                           ['Hepatitis D — needs HBsAg', ['hdco', 'hdsu']],
                           ['Hepatitis C', ['hcv']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2340, y=110, w=1000),
  src='GI Exam 1 lecture notes (SDL 15) · Robbins ch 18 · First Aid pp. 170–171 · Bootcamp Microbiology')

MAP = dict(
  id='hepvirsim', title='Viral Hepatitis Serology in Motion', topic='id', after='virus',
  sub='An infected hepatocyte sends virus and antigens into the blood, a plasma cell answers with IgM then IgG, and a time '
      'course shows where each pattern sits — pick hepatitis A, E, a stage of hepatitis B (acute, window, recovered, chronic, '
      'vaccinated), HDV co- or superinfection, or hepatitis C, and read the markers. Tap a receptor for its card',
  w=3400, h=2010,
  fa='170–171', src=SRC,
  lanes=[('hvLiver', 'Hepatitis viruses', 'tca'), ('hvTx', 'Treatment', 'gluconeo'), ('hvEnd', 'Outcomes', 'glycogen')],
  comps=[],
  nodes=[
    ('hv1', 'Hepatitis B', 280, 1010, 'hvLiver', 'HBsAg · anti-HBc · HBeAg', ['hbv', 'vxsub'], 'hub'),
    ('hv2', 'Hepatitis A & E', 600, 1010, 'hvLiver', 'fecal-oral · never chronic', ['hav']),
    ('hv3', 'Hepatitis C', 920, 1010, 'hvLiver', 'RNA, then anti-HCV', ['hcv']),
    ('hv4', 'Antivirals', 1240, 1010, 'hvTx', 'HBV: tenofovir · HCV: -buvir', ['hbvdrugs', 'sofosbuvir']),
    ('hv5', 'Where chronic leads', 1560, 1010, 'hvEnd', 'cirrhosis · HCC', ['cirrhosis', 'hcc']),
    ('hv6', 'Immune complexes', 1880, 1010, 'hvEnd', 'PAN (HBV) · cryo (HCV)', ['pan', 'cryo']),
    ('hv7', 'Liver enzymes', 2180, 1010, 'hvEnd', 'ALT, AST ↑', ['lfts']),
  ],
  panels=[
    (140, 1800, 2100, 'The five viruses (course notes SDL 15; Robbins ch 18; First Aid p. 170)', [
      ('HAV', 'naked +ssRNA picornavirus · fecal-oral · incubation 2–6 weeks · never chronic'),
      ('HBV', 'enveloped, partly double-stranded DNA hepadnavirus · blood, sex, birth · 4–26 weeks · chronic in 5–10% of adults, ~90% of infants infected at birth'),
      ('HCV', 'enveloped +ssRNA flavivirus · blood, injection drug use · 4–26 weeks · chronic in 80–90%'),
      ('HDV', 'defective RNA virus that needs the HBsAg coat · coinfection usually clears · superinfection chronic in over 80%'),
      ('HEV', 'naked +ssRNA hepevirus · waterborne, fecal-oral · 4–5 weeks · mortality approaching 20% in pregnancy')]),
    (2340, 1300, 1000, 'Reading the HBV markers (First Aid p. 171)', [
      ('HBsAg', 'infected now · over 6 months = chronic'),
      ('Anti-HBs', 'immune — vaccine or recovery'),
      ('IgM anti-HBc', 'acute or recent · may be the only marker in the window'),
      ('IgG anti-HBc', 'past or chronic infection — never from the vaccine'),
      ('HBeAg', 'replicating · highly transmissible'),
      ('Anti-HBe', 'low transmissibility')]),
  ],
  dyn=dyn,
)
