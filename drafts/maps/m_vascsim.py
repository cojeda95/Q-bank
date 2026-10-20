# m55 — Vasculitis by Vessel Size (dynamic map, kit data)
# A vessel-size LADDER across the top (aorta → large arteries → medium arteries → small arteries/arterioles → capillaries
# and venules, drawn as one tapering vessel with blood moving through it) above a BODY (head with the temporal artery,
# eyes, sinuses, mouth; the aortic arch and great vessels into the arms; lungs, heart with coronaries, kidneys with renal
# arteries, gut with the mesenteric artery, leg arteries, a peripheral nerve, knees, skin of the legs, fingers and toes,
# the shoulder and hip girdles) and a CASE CARD (classic patient · vessels · lesion · key tests · organs · treatment).
# One `one` switch picks a vasculitis, in `sections` by vessel size (large · medium · small ANCA · small immune complex ·
# any size · related, not vasculitis). Each option lights its rungs on the ladder and draws its wall lesion there
# (granulomas with giant cells, fibrinoid necrosis, immune-complex deposits, aneurysms / string of pearls, thrombus,
# a thickened narrowed wall, vasospasm), sends the right cells through the lumen (macrophages/T cells, ANCA-activated
# neutrophils, eosinophils, immune complexes), lights its organs on the body, and fills the case card.
# Readouts (↑ = raised or present, ↓ = negative or absent, ↔ = normal): ESR·CRP, PR3-ANCA, MPO-ANCA, granulomas,
# immune-complex deposits, aneurysms, palpable purpura.
#
# Sources (all read in the corpus, U+00A0/U+00AD normalized; FA = First Aid 2025 page). The rheum course texts in
# corpus/rheum (SDL 28 ch 6/9, SDL 38 Lyme/septic, SDL 47 Robbins 5) were searched and do not cover vasculitis, PMR or
# Raynaud, so FA + Robbins + Bootcamp are the sources.
#   FA 478 (vasculitides = type III or idiopathic; GCA: women > 50, unilateral headache, jaw claudication, temporal artery
#     tenderness, blindness from anterior ischemic optic neuropathy, granulomatous, temporal/vertebral/ophthalmic, PMR,
#     ↑↑ ESR/CRP, biopsy, high-dose glucocorticoids before biopsy · Takayasu: Asian women < 40, pulseless disease, fever,
#     night sweats, arthritis, myalgias, granulomatous thickening/narrowing of arch + proximal great vessels, ↑ ESR,
#     glucocorticoids · Buerger: heavy smokers, men < 40, claudication, gangrene, Raynaud, autoamputation, superficial
#     nodular phlebitis, segmental thrombosing vasculitis with vein + nerve involvement, smoking cessation · Kawasaki:
#     Asian children < 4, CRASH + fever ≥ 5 d, coronary aneurysms → thrombosis/rupture, IVIG + aspirin · PAN: middle-aged
#     men, 30% HBV, fever, weight loss, abdominal pain, melena, HTN, neurologic, cutaneous, renal; renal + visceral
#     vessels, spares lungs, transmural fibrinoid necrosis, string of pearls, glucocorticoids + cyclophosphamide, SKIN ·
#     MPA: middle-aged, lungs/kidneys/skin, pauci-immune GN, palpable purpura, MPO-ANCA/p-ANCA, cyclophosphamide +
#     glucocorticoids · EGPA: asthma, eosinophilia, peripheral neuropathy, granulomatous necrotizing, ↑ IgE)
#   FA 479 (GPA: men = women, middle-aged, upper airway / lower airway / renal triad, c-ANCA (PR3), glucocorticoids +
#     rituximab or cyclophosphamide · mixed cryoglobulinemia: viral, esp. HCV, purpura + weakness + arthralgias, neuropathy,
#     GN, IgG + IgM complexes that precipitate in the cold · IgA vasculitis: most common childhood vasculitis, after URI,
#     IgA immune complexes, hinge pain + stomach pain (intussusception) + purpura on buttocks/legs, IgA nephropathy,
#     supportive + glucocorticoids · cutaneous small-vessel vasculitis 7–10 d after penicillins, cephalosporins,
#     sulfonamides, phenytoin, allopurinol · Behçet: all-vessel, Turkish/Eastern Mediterranean, oral + genital ulcers,
#     uveitis, erythema nodosum, HSV or parvovirus, flares 1–4 weeks, HLA-B51)
#   FA 477 (PMR: proximal pain + stiffness, fever, malaise, weight loss, no weakness, women > 50, GCA; ↑ ESR ↑ CRP, normal
#     CK; low-dose glucocorticoids) · FA 480 (Raynaud: arteriolar (small vessel) vasospasm to cold or stress; white →
#     blue → red; fingers and toes; disease = 1°, syndrome = 2° to MCTD, SLE, CREST; digital ulcers in 2°; CCBs) ·
#     FA 481 (CREST includes Raynaud) · FA 323 (dihydropyridines for Raynaud) · FA 111 (type III examples: SLE, PAN, IgA
#     vasculitis) · FA 113 and 729 (MPO-ANCA: MPA, EGPA, UC, PSC; PR3-ANCA: GPA) · FA 360 (PTU and ANCA-positive
#     vasculitis) · FA 171 (HBV → PAN; HCV → mixed cryoglobulinemia, leukocytoclastic vasculitis) · FA 213 (granulomatous
#     vasculitis: GPA, EGPA, GCA, Takayasu) · FA 614 (pauci-immune crescentic GN: GPA, EGPA, MPA).
#   Robbins ch 11 "Blood vessels" (Table 11.4 sizes: large = aorta + major branches; medium = main visceral arteries,
#     aneurysms and stenoses; small = intraparenchymal arteries, arterioles, capillaries, venules · GCA: large to medium,
#     head, can involve the aorta, T-cell response, medial granulomas at the internal elastic lamina, giant cells in ~75%,
#     patchy so > 1 cm biopsy and a negative biopsy does not exclude, intimal thickening narrows the lumen, ocular symptoms
#     in ~50% · Takayasu: transmural fibrous thickening, arch + great vessels, pulmonary artery in half, coronary and renal,
#     renal → HTN in about half, ocular and neurologic deficits · Buerger: tibial and radial arteries, < 35, thrombus with
#     microabscesses, extends to veins and nerves, severe rest pain, instep claudication, early abstinence helps ·
#     PAN: small or medium muscular arteries, spares pulmonary circulation/glomeruli/arterioles/capillaries/venules, not
#     ANCA, a third HBsAg complexes, kidney > heart > liver > GI, transmural necrotizing + fibrinoid necrosis, aneurysm,
#     thrombosis, all stages coexist, motor neuritis · Kawasaki: 80% < 5, coronary aneurysms rupture/thrombose → MI,
#     fibrinoid necrosis less than PAN, IVIG + aspirin · ANCA: PR3 (c-ANCA) GPA; MPO (p-ANCA) MPA + EGPA, induced by PTU;
#     pauci-immune · MPA: capillaries, arterioles, venules; lesions the same age; GN 90%, pulmonary capillaritis;
#     hydralazine; no granulomas; leukocytoclastic · GPA: necrotizing granulomas of the upper/lower airway, small to medium
#     vessels, crescentic GN, PR3-ANCA up to 95%, cavitating nodules · EGPA: asthma, eosinophilia, granulomas + eosinophils,
#     purpura, GI bleeding, cardiomyopathy a major cause of death, MPO-ANCA 40–60% (75–100% with renal disease) · immune
#     complex vasculitis: IgA vasculitis = IgG with abnormally glycosylated IgA; cryoglobulins precipitate < 37 °C ·
#     Behçet: arteries and veins, oral + genital ulcers, average onset 30, leukocytoclastic dermal vasculitis, arterial
#     aneurysm, venous thrombosis → PE or Budd-Chiari, uveitis/hypopyon in ~50%, brainstem · Raynaud: arteries and
#     arterioles, cold or emotion, fingers/toes/nose/ears/lips; primary = young women, symmetric, no progression, intrinsic
#     smooth-muscle hyperreactivity, no structural change; secondary = SLE, scleroderma, Buerger, atherosclerosis,
#     asymmetric, progressive; ~10% later show an underlying disorder).
#   Bootcamp.com MSK — Vasculitides (fact slides only, no vignettes: GCA ↑ ESR/CRP; Takayasu ↑ ESR/CRP, MR angiography;
#     Buerger ESR/CRP normal; Kawasaki ↑ ESR, CRP, AST/ALT, WBC/platelets, echocardiogram; PAN ANCA ⊝, mononeuritis multiplex,
#     antivirals for HBV; Behçet ↑ ESR/CRP, ⊝ ANA/ANCA/RF, ⊕ pathergy, colchicine, topical steroids, immunosuppressants;
#     EGPA ↑ ESR/CRP, ↑ IgE, mononeuritis multiplex, mepolizumab; GPA saddle nose, cavitating nodules; IgA vasculitis normal
#     platelets, ↑ ESR/CRP, IgA + C3 deposits; MPA ↑ ESR/CRP; mixed cryoglobulinemia ↓ C4, RF ⊕, antivirals).
# Readout choices: "–" (no arrow) wherever no source gives a direction for that disease — e.g. ESR in PAN, GPA, cryo and
#   Raynaud; ANCA in GCA, Takayasu, Kawasaki, Buerger, IgA vasculitis and cryo (the static vasc map lists several of these
#   as ANCA-negative, but no corpus text says so); granulomas in Kawasaki, Buerger, IgA vasculitis, cryo, Behçet;
#   immune complexes in Behçet (Bootcamp says immune complexes, Robbins a Th17 response — textbook wins, no arrow).
#   EGPA MPO-ANCA is ↑ per FA 478/479 + Bootcamp; Robbins puts it at 40–60%, which the note and card say.
# CUT for lack of a corpus source: "corkscrew collaterals" in Buerger (only on the existing card); "no nasopharyngeal
#   disease" in MPA; ANA as the Raynaud work-up test; "avoid cold"; Buerger granulomas (Robbins mentions granulomatous
#   inflammation around the thrombus's microabscesses — left off the readout to keep "granulomas" meaning a granulomatous
#   vasculitis); hypocomplementemic urticarial vasculitis and cutaneous small-vessel vasculitis as options (FA only, no
#   textbook support for a full option — CSVV kept as one panel row); scleroderma as an option (a vasculopathy, not a
#   vasculitis — pinned with Raynaud instead); anti-TNF for GCA (Robbins only, not first line).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

RB11 = full('Robbins', 11)
BC_V = 'Bootcamp.com MSK — Vasculitides'
SRC = [RB11, BC_V]

OPTS = ['gca', 'tak', 'pan', 'kaw', 'bue', 'gpa', 'mpa', 'egpa', 'igav', 'cryo', 'beh', 'pmr', 'ray']
O = lambda *k: ['vx:' + x for x in k]
ALL = O(*OPTS)

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

# organ outlines in a 100 × 100 box (the atlas's organ library), scaled into place; flip mirrors left–right
import re
ORG = {
  'kidney': 'M60 4 C86 4 98 28 96 52 C94 78 82 96 60 96 C44 96 34 86 36 72 C37 64 44 60 44 50 C44 40 37 36 36 28 C34 14 44 4 60 4 Z',
  'lungs': 'M44 24 C30 22 10 44 8 78 C7 92 16 98 30 96 C40 94 46 88 46 76 Z M56 24 C70 22 92 44 94 78 C95 92 86 98 72 96 '
           'C64 94 60 90 60 84 C66 78 66 68 58 64 Z M47 2 H53 V18 L58 26 L55 28 L50 21 L45 28 L42 26 L47 18 Z',
  'heart': 'M26 30 C14 34 8 50 14 62 C22 76 46 90 74 98 C80 90 88 76 90 60 C92 44 84 32 72 28 C60 24 40 26 26 30 Z',
}
DETAIL = {
  'kidney': 'M44 50 C34 52 28 58 26 70 M44 40 C52 44 52 56 44 60',
  'lungs': 'M10 62 C22 58 34 54 45 48 M26 57 C34 54 40 54 46 55 M92 66 C80 60 68 52 58 46',
  'heart': 'M48 27 C46 8 70 4 74 20 M32 30 V6 M58 28 C60 18 64 14 70 18 M56 32 C54 56 60 80 74 98',
}
def scaled(d, x, y, w, h, flip=False):
    out = []
    fx = (lambda v: x + (100 - v) * w / 100) if flip else (lambda v: x + v * w / 100)
    for cmd, nums in re.findall(r'([MLCHVZ])([^MLCHVZ]*)', d):
        v = [float(t) for t in nums.split()]
        if cmd == 'H': out.append(f'H{fx(v[0]):.0f}')
        elif cmd == 'V': out.append(f'V{y + v[0] * h / 100:.0f}')
        elif cmd == 'Z': out.append('Z')
        else: out.append(cmd + ' '.join(f'{fx(v[i]):.0f} {y + v[i + 1] * h / 100:.0f}' for i in range(0, len(v), 2)))
    return ' '.join(out)

# ════════ 1. the vessel-size ladder ════════
Y = 330
SEG = [  # key, x0, x1, lumen width, label, examples
  ('s1', 230, 640, 110, 'Aorta', 'arch · thoracic · abdominal aorta'),
  ('s2', 640, 1030, 72, 'Large arteries', 'carotid · subclavian · vertebral · temporal'),
  ('s3', 1030, 1420, 44, 'Medium arteries', 'coronary · renal · mesenteric · tibial · radial'),
  ('s4', 1420, 1800, 22, 'Small arteries · arterioles', 'intraparenchymal arteries · arterioles'),
  ('s5', 1800, 2290, 12, 'Capillaries · venules', 'glomeruli · alveolar capillaries · dermal venules'),
]
LIT = {'s1': O('gca', 'tak', 'beh'), 's2': O('gca', 'tak', 'beh'), 's3': O('pan', 'kaw', 'bue', 'beh'),
       's4': O('gpa', 'mpa', 'egpa', 'igav', 'cryo', 'beh', 'ray'), 's5': O('gpa', 'mpa', 'egpa', 'igav', 'cryo', 'beh')}
text('The vessel-size ladder', 180, 150, 'dyn-big')
text('blood runs from the aorta down to the capillaries and out through the venules — each vasculitis has its favourite rung',
     180, 172, 'dyn-cap')
for k, x0, x1, w, lab, ex in SEG:   # highlight bands first, under the vessel
    add(f'<rect x="{x0 + 6}" y="205" width="{x1 - x0 - 12}" height="268" rx="26" class="dyn-hl"/>', when=LIT[k])
add('<rect x="190" y="205" width="2140" height="268" rx="26" class="dyn-dim" style="fill:var(--surface-2);stroke:none"/>',
    when=O('pmr'))
for k, x0, x1, w, lab, ex in SEG:
    if k == 's5':
        shapes.append(dict(tube=f'M{x0} {Y} H2030', w=8, color='--dk12'))
        shapes.append(dict(tube=f'M2030 {Y} H{x1}', w=18, color='--dk1'))
        text('capillaries', 1915, 372, 'dyn-cap', 'middle'); text('venules', 2160, 378, 'dyn-cap', 'middle')
    elif k == 's4':
        shapes.append(dict(tube=f'M{x0} {Y} H{x1}', w=w, color='--dk12', mods=[dict(when=O('ray'), d=-14)]))
    else:
        shapes.append(dict(tube=f'M{x0} {Y} H{x1}', w=w, color='--dk12'))
    text(lab, (x0 + x1) // 2, 226, 'nf-l1', 'middle')
    text(ex, (x0 + x1) // 2, 452, 'nf-l2', 'middle')

# lesion pieces
def gran(x, y, r=20):
    """a granuloma: a multinucleated giant cell ringed by epithelioid macrophages and lymphocytes"""
    ring = ''.join(f'<circle cx="{x + (r + 9) * c:.0f}" cy="{y + (r + 9) * s:.0f}" r="7" fill="var(--surface)" '
                   f'stroke="var(--dk9)" stroke-width="2.5"/>'
                   for c, s in ((1, 0), (.7, .7), (0, 1), (-.7, .7), (-1, 0), (-.7, -.7), (0, -1), (.7, -.7)))
    nuc = ''.join(f'<circle cx="{x + r * .5 * c:.0f}" cy="{y + r * .5 * s:.0f}" r="3.6" fill="var(--dk9)"/>'
                  for c, s in ((1, 0), (0, 1), (-1, 0), (0, -1), (.7, .7)))
    return (ring + f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--surface-2)" stroke="var(--dk9)" stroke-width="3.5"/>' + nuc)
def fib(x0, x1, y):
    """fibrinoid necrosis: a ragged bright band in the wall"""
    pts = ' '.join(f'L{x} {y + (5 if i % 2 else -5)}' for i, x in enumerate(range(x0 + 12, x1, 12)))
    return f'<path d="M{x0} {y} {pts}" class="dyn-lesion" style="stroke-width:6"/>'
def bulge(x, y, r):
    """an aneurysm: the wall balloons out and the lumen with it"""
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="var(--nf-lumen)" stroke="var(--dk12)" stroke-width="6"/>'
def thromb(x, y, rx, ry, abscess=False):
    s = f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="var(--dk8)" stroke="var(--ink-3)" stroke-width="2"/>'
    if abscess: s += ''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="4" fill="var(--dk5)"/>' for dx, dy in ((-22, -4), (2, 5), (24, -3)))
    return s
def deposits(x0, x1, ytop, ybot, step=26):
    return ''.join(f'<circle cx="{x}" cy="{ytop}" r="4.5" fill="var(--dk7)"/><circle cx="{x + step // 2}" cy="{ybot}" r="4.5" fill="var(--dk7)"/>'
                   for x in range(x0, x1, step))
WALLTOP = {k: Y - (w + 12) / 2 for k, x0, x1, w, *_ in SEG}
WALLBOT = {k: Y + (w + 12) / 2 for k, x0, x1, w, *_ in SEG}

# GCA: granulomas at the internal elastic lamina, patchy (skip lesions); the intima thickens and narrows the lumen
add(f'<path d="M660 {Y} H1010" style="fill:none;stroke:var(--dk12);stroke-width:84;stroke-linecap:round"/>'
    f'<path d="M660 {Y} H1010" style="fill:none;stroke:var(--nf-lumen);stroke-width:34;stroke-linecap:round"/>', when=O('gca'))
add(gran(720, 290) + gran(940, 290) + gran(470, 271), when=O('gca'))
# Takayasu: transmural fibrous thickening of the arch and its branches — the lumens narrow
add(f'<path d="M250 {Y} H630" style="fill:none;stroke:var(--dk12);stroke-width:122;stroke-linecap:round"/>'
    f'<path d="M250 {Y} H630" style="fill:none;stroke:var(--nf-lumen);stroke-width:44;stroke-linecap:round"/>'
    f'<path d="M660 {Y} H1010" style="fill:none;stroke:var(--dk12);stroke-width:84;stroke-linecap:round"/>'
    f'<path d="M660 {Y} H1010" style="fill:none;stroke:var(--nf-lumen);stroke-width:24;stroke-linecap:round"/>', when=O('tak'))
add(gran(360, 271) + gran(560, 271) + gran(820, 290), when=O('tak'))
# PAN: transmural fibrinoid necrosis + a string of microaneurysms (lesions of every age)
add(''.join(bulge(x, WALLTOP['s3'] - 2 if i % 2 == 0 else WALLBOT['s3'] + 2, 15) for i, x in enumerate(range(1075, 1400, 58)))
    + fib(1120, 1330, WALLTOP['s3'] + 2), when=O('pan'))
# Kawasaki: one big coronary aneurysm
add(bulge(1225, WALLTOP['s3'] - 14, 38), when=O('kaw'))
# Buerger: a thrombus fills the lumen; the neighbouring vein and nerve are inflamed too
add(thromb(1235, Y, 62, 21, abscess=True), when=O('bue'))
shapes.append(dict(tube='M1050 398 H1400', w=20, color='--dk1', when=O('bue')))
add('<path d="M1050 430 H1400" style="fill:none;stroke:var(--dk5);stroke-width:6;stroke-linecap:round"/>'
    '<path d="M1050 430 H1400" class="dyn-hl" style="stroke-width:3;opacity:.6"/>', when=O('bue'))
text('vein', 1424, 402, 'dyn-cap', when=O('bue')); text('nerve', 1424, 434, 'dyn-cap', when=O('bue'))
# ANCA trio and the small-vessel lesions
add(gran(1560, WALLTOP['s4'] - 14, 17) + fib(1640, 1780, WALLTOP['s4']) + fib(1820, 2010, WALLTOP['s5']), when=O('gpa'))
add(fib(1440, 1780, WALLTOP['s4']) + fib(1820, 2010, WALLTOP['s5']) + fib(2050, 2270, WALLTOP['s5'] - 4), when=O('mpa'))
add(gran(1640, WALLTOP['s4'] - 14, 17) + fib(1820, 2010, WALLTOP['s5']), when=O('egpa'))
# immune complexes lodged in small-vessel walls
add(deposits(1440, 1790, WALLTOP['s4'], WALLBOT['s4']) + deposits(1815, 2025, WALLTOP['s5'], WALLBOT['s5'], 22)
    + deposits(2045, 2280, Y - 18, Y + 18, 22), when=O('igav', 'cryo'))
text('in the cold, IgG + IgM complexes precipitate', 1610, 290, 'dyn-cap', 'middle', when=O('cryo'))
# Behçet: arteries and veins of any size — an arterial aneurysm, a venous thrombosis
add(bulge(835, WALLTOP['s2'] - 8, 30) + thromb(2160, Y, 46, 10), when=O('beh'))
# Raynaud: the arterioles clamp down (vasospasm), no inflammation
add(''.join(f'<path d="M{x - 9} 296 L{x} 308 L{x + 9} 296 M{x - 9} 364 L{x} 352 L{x + 9} 364" '
            f'style="fill:none;stroke:var(--dk1);stroke-width:4;stroke-linecap:round"/>' for x in (1480, 1610, 1740)), when=O('ray'))

# one line under the ladder: what this option does to the wall
LADDER = {
  'gca': 'giant cell arteritis — granulomas with giant cells at the internal elastic lamina, in patches (skip lesions); the thickened intima narrows the lumen; it can reach the aorta',
  'tak': 'Takayasu — granulomatous thickening and fibrosis of the arch and its branches: the lumens narrow, so less blood reaches the arms',
  'pan': 'PAN — transmural fibrinoid necrosis of medium arteries, early and late lesions side by side; the weakened wall bulges into a string of microaneurysms',
  'kaw': 'Kawasaki — transmural arteritis of the coronary arteries; the damaged wall balloons into an aneurysm that can thrombose or rupture',
  'bue': 'Buerger — a thrombus with tiny neutrophil abscesses blocks the artery, and the inflammation spreads to the neighbouring vein and nerve',
  'gpa': 'GPA — PR3-ANCA turns neutrophils on small vessels (fibrinoid necrosis), with necrotizing granulomas beside them; no immune deposits (pauci-immune)',
  'mpa': 'MPA — MPO-ANCA turns neutrophils on arterioles, capillaries and venules: fibrinoid necrosis, all lesions the same age, no granulomas, no deposits',
  'egpa': 'EGPA — eosinophil-rich, necrotizing granulomatous inflammation of small to medium vessels',
  'igav': 'IgA vasculitis — IgA immune complexes lodge in the walls of small vessels and fix complement (IgA and C3 on biopsy)',
  'cryo': 'mixed cryoglobulinemia — IgG + IgM immune complexes that precipitate in the cold deposit in small-vessel walls and fix complement',
  'beh': 'Behçet — arteries and veins of any size: leukocytoclastic vasculitis of dermal vessels, arterial aneurysms, venous thrombosis',
  'pmr': 'polymyalgia rheumatica — no vessel lesion of its own, but it travels with giant cell arteritis',
  'ray': 'Raynaud — the small arteries and arterioles clamp down in cold or stress; the wall itself is normal',
}
for k, t in LADDER.items(): text(t, 200, 496, TAG, when=O(k))

# ════════ 2. the body ════════
text('Where it strikes', 180, 650, 'dyn-big')
text('lit organs are the ones this vasculitis typically hits', 180, 672, 'dyn-cap')
BODY = ('M732 885 C690 888 640 892 612 912 C596 924 598 960 604 1000 L620 1160 C614 1250 606 1330 616 1405 '
        'L904 1405 C914 1330 906 1250 900 1160 L916 1000 C922 960 924 924 908 912 C880 892 830 888 788 885 Z')
ARM_R = 'M612 912 C584 922 572 950 570 990 L548 1385 L584 1388 L604 1010 C606 990 612 975 622 962 Z'
mirror = lambda d: re.sub(r'(?<![\d.])(\d+(?:\.\d+)?) (\d+(?:\.\d+)?)', lambda m: f'{1520 - float(m.group(1)):.0f} {m.group(2)}', d)
ARM_L = mirror(ARM_R)
LEGS = 'M616 1405 L636 1880 L700 1880 L748 1450 L772 1450 L820 1880 L884 1880 L904 1405 Z'
add(f'<path d="{LEGS}" class="dyn-cell"/><path d="{ARM_R}" class="dyn-cell"/><path d="{ARM_L}" class="dyn-cell"/>'
    f'<path d="{BODY}" class="dyn-cell"/>'
    '<rect x="732" y="830" width="56" height="62" class="dyn-cell"/>'
    '<ellipse cx="760" cy="755" rx="66" ry="82" class="dyn-cell"/>'
    '<ellipse cx="566" cy="1410" rx="22" ry="26" class="dyn-cell"/><ellipse cx="954" cy="1410" rx="22" ry="26" class="dyn-cell"/>'
    + ''.join(f'<path d="M{x} 1428 L{x + dx} 1456" style="fill:none;stroke:var(--dyn-cell-line);stroke-width:8;stroke-linecap:round"/>'
              for x, dx in ((550, -3), (560, -1), (571, 1), (581, 4), (939, -4), (949, -1), (960, 1), (970, 3)))
    + '<ellipse cx="668" cy="1892" rx="40" ry="13" class="dyn-cell"/><ellipse cx="852" cy="1892" rx="40" ry="13" class="dyn-cell"/>')
# face: sinuses, eyes, nose, mouth
add('<ellipse cx="740" cy="777" rx="11" ry="8" class="dyn-soft"/><ellipse cx="780" cy="777" rx="11" ry="8" class="dyn-soft"/>'
    + ''.join(f'<ellipse cx="{x}" cy="742" rx="11" ry="6.5" fill="var(--surface)" stroke="var(--ink-2)" stroke-width="2.5"/>'
              f'<circle cx="{x}" cy="742" r="3.2" fill="var(--ink-2)"/>' for x in (737, 783))
    + '<path d="M760 750 L752 786 L767 788" class="dyn-line"/><path d="M740 808 Q760 822 780 808" class="dyn-line"/>')
# lungs, then the arteries, then the heart over the ascending aorta
LUNGS = scaled(ORG['lungs'], 640, 930, 240, 210)
add(f'<path d="{LUNGS}" class="dyn-cell" style="stroke:var(--dk9)"/>'
    f'<path d="{scaled(DETAIL["lungs"], 640, 930, 240, 210)}" class="dyn-line" style="stroke-width:1.5"/>')
ARCH = 'M770 1045 V985 C770 950 812 948 812 985 V1395'
CAROTID_R = 'M780 962 L748 925 L738 848 L716 830 C700 808 692 790 700 772 C708 754 694 738 700 720 C704 708 712 700 720 694'
TEMPORAL = 'M716 830 C700 808 692 790 700 772 C708 754 694 738 700 720 C704 708 712 700 720 694'
CAROTID_L = 'M796 955 L784 846'
SUBCL_R = 'M748 925 L640 930 L600 1000 L566 1385'
SUBCL_L = 'M808 962 L880 930 L920 1000 L954 1385'
RENAL = 'M812 1250 H738 M812 1250 H848'
MESENT = 'M812 1290 C800 1300 790 1306 780 1316'
LEG_R = 'M812 1395 C760 1410 690 1420 684 1460 L670 1868'
LEG_L = 'M812 1395 C830 1420 840 1440 840 1460 L852 1868'
for d, w in ((ARCH, 16), (CAROTID_R, 6), (CAROTID_L, 6), (SUBCL_R, 7), (SUBCL_L, 7), (RENAL, 6), (MESENT, 5), (LEG_R, 7), (LEG_L, 7)):
    shapes.append(dict(vessel=d, w=w))
HEART = scaled(ORG['heart'], 722, 1035, 120, 105)
add(f'<path d="{HEART}" class="dyn-cell" style="stroke:var(--dk2)"/>'
    f'<path d="{scaled(DETAIL["heart"], 722, 1035, 120, 105)}" class="dyn-line" style="stroke-width:1.5"/>'
    '<path d="M752 1062 C744 1086 752 1112 776 1128 M800 1062 C812 1084 818 1104 820 1122" class="nf-art" style="stroke-width:4"/>')
KID_R, KID_L = scaled(ORG['kidney'], 690, 1210, 50, 82, flip=True), scaled(ORG['kidney'], 848, 1210, 50, 82)
add(f'<path d="{KID_R}" class="dyn-cell" style="stroke:var(--dk2)"/><path d="{KID_L}" class="dyn-cell" style="stroke:var(--dk2)"/>'
    f'<path d="{scaled(DETAIL["kidney"], 690, 1210, 50, 82, flip=True)}" class="dyn-line" style="stroke-width:1.5"/>'
    f'<path d="{scaled(DETAIL["kidney"], 848, 1210, 50, 82)}" class="dyn-line" style="stroke-width:1.5"/>')
GUT = 'M690 1322 C690 1298 832 1298 832 1322 C832 1346 690 1346 690 1370 C690 1394 840 1394 840 1370'
shapes.append(dict(tube=GUT, w=12, color='--dk10'))
NERVE = 'M878 1440 L866 1860'
add(f'<path d="{NERVE}" style="fill:none;stroke:var(--dk5);stroke-width:4;stroke-dasharray:9 6"/>')
add('<circle cx="676" cy="1640" r="20" class="dyn-soft"/><circle cx="846" cy="1640" r="20" class="dyn-soft"/>')

# what each option lights on the body
ORGHL = {
  'temporal': (O('gca'), f'<path d="{TEMPORAL}" class="dyn-hl"/>'),
  'eye': (O('gca', 'tak', 'beh'), '<ellipse cx="737" cy="742" rx="19" ry="14" class="dyn-hl"/><ellipse cx="783" cy="742" rx="19" ry="14" class="dyn-hl"/>'),
  'sinus': (O('gpa'), '<ellipse cx="760" cy="779" rx="38" ry="18" class="dyn-hl"/>'),
  'mouth': (O('beh', 'kaw'), '<ellipse cx="760" cy="812" rx="32" ry="13" class="dyn-hl"/>'),
  'arch': (O('tak'), f'<path d="M770 1045 V985 C770 950 812 948 812 985 V1060 M748 925 L640 930 L600 1000 L566 1385 M808 962 L880 930 L920 1000 L954 1385" class="dyn-hl"/>'),
  'lungs': (O('gpa', 'mpa', 'egpa'), f'<path d="{LUNGS}" class="dyn-hl" style="stroke-width:5"/>'),
  'heart': (O('kaw', 'egpa'), f'<path d="{HEART}" class="dyn-hl"/>'),
  'kidney': (O('pan', 'gpa', 'mpa', 'egpa', 'igav', 'cryo', 'tak'), f'<path d="{KID_R}" class="dyn-hl"/><path d="{KID_L}" class="dyn-hl"/>'),
  'gut': (O('pan', 'igav', 'egpa'), f'<path d="{GUT}" class="dyn-hl"/>'),
  'nerve': (O('pan', 'egpa', 'cryo', 'mpa', 'bue'), f'<path d="{NERVE}" class="dyn-hl"/>'),
  'skin': (O('mpa', 'egpa', 'igav', 'cryo', 'pan', 'beh'), '<path d="M650 1700 L660 1860 M870 1700 L860 1860" class="dyn-hl" style="opacity:.5"/>'),
  'fingers': (O('bue', 'ray', 'kaw'), '<ellipse cx="566" cy="1428" rx="36" ry="44" class="dyn-hl"/><ellipse cx="954" cy="1428" rx="36" ry="44" class="dyn-hl"/>'),
  'toes': (O('bue', 'ray', 'kaw'), '<ellipse cx="668" cy="1892" rx="54" ry="24" class="dyn-hl"/><ellipse cx="852" cy="1892" rx="54" ry="24" class="dyn-hl"/>'),
  'joints': (O('igav', 'cryo', 'tak'), '<circle cx="676" cy="1640" r="30" class="dyn-hl"/><circle cx="846" cy="1640" r="30" class="dyn-hl"/>'),
  'girdle': (O('pmr'), '<path d="M592 985 C590 930 630 900 672 902 M928 985 C930 930 890 900 848 902 M612 1360 C616 1420 650 1446 700 1444 M908 1360 C904 1420 870 1446 820 1444" class="dyn-hl"/>'),
  'genital': (O('beh'), '<ellipse cx="760" cy="1440" rx="24" ry="14" class="dyn-hl"/>'),
  'legart': (O('bue'), f'<path d="M684 1500 L670 1868 M840 1500 L852 1868" class="dyn-hl"/>'),
}
for key, (when, svg) in ORGHL.items(): add(svg, when=when)
# disease marks on the body
add(''.join(f'<circle cx="{x}" cy="{y}" r="5.5" fill="var(--dk4)"/>' for x, y in (
    (650, 1712), (664, 1738), (652, 1770), (668, 1800), (656, 1832), (674, 1852), (872, 1712), (858, 1742), (870, 1774),
    (854, 1806), (866, 1836), (850, 1856), (640, 1430), (654, 1452), (880, 1430), (866, 1452))),
    when=O('mpa', 'egpa', 'igav', 'cryo'))
text('palpable purpura', 760, 1980 - 220, 'dyn-cap', 'middle', when=O('mpa', 'egpa', 'igav', 'cryo'))
add(''.join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="7" fill="var(--dk2)" opacity=".75"/>' for x, y in ((660, 1730), (664, 1800), (862, 1745), (858, 1815))),
    when=O('beh', 'pan'))
text('skin nodules', 760, 1760, 'dyn-cap', 'middle', when=O('beh', 'pan'))
add('<circle cx="749" cy="814" r="4" fill="var(--bad)"/><circle cx="771" cy="815" r="4" fill="var(--bad)"/>'
    '<circle cx="752" cy="1438" r="4" fill="var(--bad)"/><circle cx="768" cy="1440" r="4" fill="var(--bad)"/>', when=O('beh'))
add('<circle cx="760" cy="814" r="5" fill="var(--bad)"/>', when=O('kaw'))
# fingertips and toes: gangrene (Buerger) · white → blue → red (Raynaud)
add(''.join(f'<circle cx="{x + dx}" cy="1458" r="5.5" fill="var(--ink)"/>' for x, dx in ((550, -3), (560, -1), (571, 1), (581, 4), (939, -4), (949, -1), (960, 1), (970, 3)))
    + ''.join(f'<circle cx="{x}" cy="1900" r="6" fill="var(--ink)"/>' for x in (636, 650, 664, 678, 692, 828, 842, 856, 870, 884)),
    when=O('bue'))
text('gangrene of the digits', 760, 1940, 'dyn-cap', 'middle', when=O('bue'))
add(''.join(f'<circle cx="{x + dx}" cy="1458" r="6" fill="var({c})" stroke="var(--ink-3)" stroke-width="1.5"/>'
            for (x, dx), c in zip(((550, -3), (560, -1), (571, 1), (581, 4), (939, -4), (949, -1), (960, 1), (970, 3)),
                                  ('--surface', '--surface', '--dk1', '--dk2', '--surface', '--dk1', '--dk1', '--dk2'))),
    when=O('ray'))
text('white → blue → red', 760, 1940, 'dyn-cap', 'middle', when=O('ray'))
text('weak arm pulses', 1100, 1200, TAG, when=O('tak'))
text('jaw claudication · sudden vision loss', 1000, 720, TAG, when=O('gca'))
text('saddle nose · septal perforation', 1000, 720, TAG, when=O('gpa'))
text('oral ulcers · uveitis', 1000, 720, TAG, when=O('beh'))
text('strawberry tongue · red eyes', 1000, 720, TAG, when=O('kaw'))
text('coronary aneurysm', 1000, 1118, TAG, when=O('kaw'))
text('eosinophilic cardiomyopathy', 1000, 1118, TAG, when=O('egpa'))
text('renal artery → hypertension', 1000, 1272, TAG, when=O('pan', 'tak'))
text('pauci-immune crescentic GN', 1000, 1272, TAG, when=O('gpa', 'mpa'))
text('IgA nephropathy · hematuria', 1000, 1272, TAG, when=O('igav'))
text('membranoproliferative GN', 1000, 1272, TAG, when=O('cryo'))
text('belly pain · intussusception', 1000, 1362, TAG, when=O('igav'))
text('belly pain · melena', 1000, 1362, TAG, when=O('pan'))
text('GI bleeding', 1000, 1362, TAG, when=O('egpa'))
text('mononeuritis multiplex', 1000, 1622, TAG, when=O('pan', 'egpa', 'mpa'))
text('peripheral neuropathy', 1000, 1622, TAG, when=O('cryo'))
text('severe rest pain', 1000, 1622, TAG, when=O('bue'))
text('stiff, painful — not weak', 1000, 1432, TAG, when=O('pmr'))
text('hemoptysis · cavitating nodules', 300, 1082, TAG, when=O('gpa'))
text('pulmonary capillaritis · hemoptysis', 300, 1082, TAG, when=O('mpa'))
text('asthma · lung infiltrates', 300, 1082, TAG, when=O('egpa'))

# static organ labels with leader lines; a lit organ's leader turns to the accent colour
LBL = [  # text, x, y, anchor, leader end, lit by
  ('Temporal artery', 520, 704, 'end', (701, 724), 'temporal'),
  ('Eye · ophthalmic artery', 520, 748, 'end', (722, 744), 'eye'),
  ('Nose · sinuses', 520, 792, 'end', (729, 779), 'sinus'),
  ('Carotid · subclavian arteries', 520, 932, 'end', (700, 928), 'arch'),
  ('Lungs', 520, 1052, 'end', (668, 1052), 'lungs'),
  ('Kidney · renal artery', 520, 1256, 'end', (692, 1252), 'kidney'),
  ('Fingers', 520, 1470, 'end', (546, 1458), 'fingers'),
  ('Knee · joints', 520, 1644, 'end', (654, 1642), 'joints'),
  ('Skin of the legs · buttocks', 520, 1792, 'end', (650, 1790), 'skin'),
  ('Mouth', 1000, 808, 'start', (784, 810), 'mouth'),
  ('Shoulder girdle', 1000, 906, 'start', (930, 912), 'girdle'),
  ('Aortic arch', 1000, 960, 'start', (814, 960), 'arch'),
  ('Heart · coronary arteries', 1000, 1098, 'start', (838, 1094), 'heart'),
  ('Gut · mesenteric artery', 1000, 1340, 'start', (842, 1346), 'gut'),
  ('Hip girdle', 1000, 1410, 'start', (908, 1404), 'girdle'),
  ('Genitals', 1000, 1470, 'start', (776, 1446), 'genital'),
  ('Peripheral nerve', 1000, 1600, 'start', (874, 1600), 'nerve'),
  ('Toes', 1000, 1896, 'start', (894, 1894), 'toes'),
]
for t, x, y, an, (ex, ey), key in LBL:
    sx = x + 6 if an == 'end' else x - 6
    add(f'<path d="M{sx} {y - 4} L{ex} {ey}" class="dyn-line" style="stroke-width:1.5"/>')
    add(f'<path d="M{sx} {y - 4} L{ex} {ey}" style="fill:none;stroke:var(--accent);stroke-width:3.5"/>', when=ORGHL[key][0])
    text(t, x, y, 'nf-l2', an)

# ════════ 3. the case card ════════
add('<rect x="1240" y="640" width="1080" height="820" rx="26" class="dyn-soft"/>')
text('The case card', 1270, 690, 'dyn-big')
text('Pick a vasculitis on the right: its rungs light on the ladder, its organs on the body, and this card fills in.',
     1270, 760, 'nf-l2', unless=ALL)
ROWS = [('pt', 'Classic patient'), ('ves', 'Vessels'), ('les', 'Lesion'), ('tst', 'Key tests'), ('org', 'Organs hit'),
        ('tx', 'First-line treatment')]
CASE = {
  'gca': dict(pt='Woman over 50 — a new one-sided headache, jaw claudication, a tender temporal artery; often with polymyalgia rheumatica',
              ves='Large to medium arteries of the head — temporal, vertebral and ophthalmic; it can also involve the aorta',
              les='Granulomatous inflammation with giant cells centred on the internal elastic lamina; patchy skip lesions',
              tst='ESR and CRP very high · temporal artery biopsy (over 1 cm long) — a negative biopsy does not rule it out',
              org='Eye (anterior ischemic optic neuropathy → sudden blindness), scalp, jaw; shoulders and hips when PMR comes with it',
              tx='High-dose glucocorticoids at once — before the biopsy'),
  'tak': dict(pt='Asian woman under 40 — fever, night sweats, arthritis and myalgias, then weak arm pulses ("pulseless disease")',
              ves='The aortic arch and its proximal great vessels; the pulmonary artery in half, the coronary and renal arteries too',
              les='Granulomatous inflammation, then transmural fibrous thickening — the branch lumens narrow or close',
              tst='ESR ↑ · angiography (e.g. MR angiography) shows the narrowed arch branches',
              org='Arms (weak pulses, lower blood pressure), eyes (visual loss), brain; renal arteries → hypertension in about half',
              tx='Glucocorticoids'),
  'pan': dict(pt='Middle-aged man, about 30% hepatitis B positive — fever, weight loss, belly pain, melena, hypertension, neuropathy',
              ves='Medium (and small) muscular arteries of the kidney and viscera — spares the lungs, glomeruli, capillaries and venules',
              les='Segmental transmural inflammation with fibrinoid necrosis, aneurysms and thrombosis; early and late lesions coexist',
              tst='Angiography: microaneurysms like a "string of pearls" · ANCA negative · test for hepatitis B',
              org='PAN hits the SKIN: Skin, Kidneys (renal artery, not GN), Intestines, Nerves (mostly motor) — never the lungs',
              tx='Glucocorticoids and cyclophosphamide; antivirals when hepatitis B drives it'),
  'kaw': dict(pt='Asian child under 4 — fever 5 days or more + CRASH: Conjunctivitis, Rash, Adenopathy, Strawberry tongue, Hands and feet',
              ves='Medium arteries — above all the coronary arteries',
              les='Dense transmural inflammation (less fibrinoid necrosis than PAN); the damaged wall forms an aneurysm',
              tst='ESR, CRP, white cells, platelets and AST/ALT ↑ · echocardiogram for coronary aneurysms',
              org='Heart: coronary aneurysms that thrombose or rupture → MI or sudden death; eyes, mouth, skin, cervical nodes',
              tx='IV immunoglobulin and aspirin'),
  'bue': dict(pt='Heavy smoker, man under 40 — claudication of the hands and feet, Raynaud, superficial nodular phlebitis',
              ves='Medium arteries of the limbs (tibial, radial) — the inflammation spreads to the neighbouring veins and nerves',
              les='Segmental thrombosing vasculitis: thrombus with microabscesses fills the lumen; artery, vein and nerve scar together',
              tst='ESR and CRP normal · arteriography: segmental occlusions without atherosclerosis',
              org='Fingers and toes: severe rest pain, ulcers, gangrene, autoamputation',
              tx='Smoking cessation — early on it can stop further attacks'),
  'gpa': dict(pt='Middle-aged adult (men as often as women) — chronic sinusitis, otitis, nasal ulcers, hemoptysis, hematuria',
              ves='Small to medium vessels — capillaries, venules, arterioles and arteries of the airways, lungs and kidneys',
              les='Necrotizing granulomas of the upper and lower airway + necrotizing vasculitis; pauci-immune (no deposits)',
              tst='PR3-ANCA (c-ANCA) in up to 95% · chest imaging: cavitating nodules · biopsy: necrotizing granulomas',
              org='Nose and sinuses (septal perforation, saddle nose), lungs (cavitating nodules), kidneys (crescentic GN)',
              tx='Glucocorticoids with rituximab or cyclophosphamide'),
  'mpa': dict(pt='Middle-aged adult — hemoptysis, hematuria and palpable purpura; drugs such as hydralazine can trigger it',
              ves='Small vessels — capillaries, arterioles and venules; medium and larger arteries are spared',
              les='Segmental fibrinoid necrosis, all lesions the same age; no granulomas; pauci-immune; leukocytoclastic in venules',
              tst='MPO-ANCA (p-ANCA) · biopsy without granulomas',
              org='Kidneys (necrotizing GN in 90%), lungs (pulmonary capillaritis → hemoptysis), skin (palpable purpura)',
              tx='Cyclophosphamide and glucocorticoids'),
  'egpa': dict(pt='Adult with asthma and allergic rhinitis — eosinophilia, lung infiltrates, purpura, mononeuritis multiplex',
               ves='Small to medium vessels',
               les='Necrotizing granulomas with eosinophil-rich infiltrates in the vessels and tissues',
               tst='Eosinophilia · IgE ↑ · MPO-ANCA (p-ANCA) in 40–60% (75–100% with kidney disease) — a negative ANCA does not exclude it',
               org='Lungs (asthma), nerves, skin, gut (bleeding), kidneys; heart — eosinophilic cardiomyopathy, a major cause of death',
               tx='Glucocorticoids, with mepolizumab (anti-IL-5), methotrexate or rituximab to spare steroids'),
  'igav': dict(pt='Child — the most common vasculitis of childhood, often a week or so after an upper respiratory infection',
               ves='Small vessels of the skin, gut, joints and glomeruli',
               les='IgA immune complexes (IgG bound to abnormally glycosylated IgA) deposit in the wall and fix complement',
               tst='Platelets normal — the purpura is vascular · skin biopsy: leukocytoclastic vasculitis with IgA and C3',
               org='Palpable purpura on the buttocks and legs, colicky belly pain (intussusception), arthralgias, hematuria (IgA nephropathy)',
               tx='Supportive care; glucocorticoids if severe'),
  'cryo': dict(pt='Adult with chronic hepatitis C — palpable purpura, weakness and arthralgias',
               ves='Small vessels',
               les='Mixed IgG + IgM cryoglobulins precipitate in the cold, deposit in small-vessel walls and fix complement',
               tst='Cryoglobulins · hepatitis C positive · C4 ↓ · rheumatoid factor may be positive',
               org='Skin (purpura), joints, peripheral nerves, kidneys (membranoproliferative GN)',
               tx='Treat the hepatitis C with antivirals; immunosuppression or plasmapheresis when severe'),
  'beh': dict(pt='Young adult (onset around 30) of Turkish or Eastern Mediterranean descent, HLA-B51; flares last 1–4 weeks',
              ves='Arteries and veins of any size',
              les='Leukocytoclastic vasculitis of dermal vessels · arterial aneurysms · venous thrombosis (→ pulmonary embolism, Budd-Chiari)',
              tst='Clinical diagnosis · ESR/CRP ↑ but ANA, ANCA and RF negative · positive pathergy test',
              org='Recurrent painful oral and genital ulcers, uveitis (about half; hypopyon), erythema nodosum, brainstem lesions',
              tx='Colchicine and topical steroids for ulcers; immunosuppressants and high-dose steroids in severe disease'),
  'pmr': dict(pt='Woman over 50 — pain and stiffness of the shoulders and hips, with fever, malaise and weight loss',
              ves='No vasculitis of its own — but it is associated with giant cell arteritis',
              les='Pain and stiffness of the proximal muscles without true weakness; the muscle enzymes stay normal',
              tst='ESR and CRP ↑ · CK normal',
              org='Shoulder and hip girdles',
              tx='Low-dose glucocorticoids — the response is rapid'),
  'ray': dict(pt='Primary: young woman, symmetric, does not progress · Secondary (SLE, scleroderma/CREST, Buerger): asymmetric, worsens',
              ves='Small arteries and arterioles of the fingers and toes (sometimes the nose, ears or lips)',
              les='Vasospasm in cold or stress — intrinsic smooth-muscle hyperreactivity; no inflammation, no structural change',
              tst='Evaluate any new case — about 10% later show an underlying disorder; digital ulcers point to secondary disease',
              org='Digits turn white (ischemia) → blue (hypoxia) → red (reperfusion)',
              tx='Dihydropyridine calcium channel blockers (e.g. nifedipine)'),
}
def wrap(t, n=150):
    out, cur = [], ''
    for wd in t.split(' '):
        if len((cur + ' ' + wd).strip()) > n: out.append(cur.strip()); cur = wd
        else: cur += ' ' + wd
    out.append(cur.strip()); return out
RY = [745, 860, 975, 1090, 1205, 1320]
for (rk, rl), y in zip(ROWS, RY):
    text(rl, 1270, y, 'nf-l1', when=ALL)
    for k, row in CASE.items():
        for i, ln in enumerate(wrap(row[rk])): text(ln, 1270, y + 24 + i * 19, 'nf-l2', when=O(k))

# ════════ 4. lesion key ════════
add('<rect x="1240" y="1490" width="1080" height="470" rx="26" class="dyn-soft"/>')
text('Wall lesions on the ladder', 1270, 1532, 'dyn-big')
KEY = [
  (gran(1300, 1590, 12), 'Granuloma with giant cells — macrophages and T cells: giant cell arteritis, Takayasu, GPA, EGPA'),
  (fib(1278, 1322, 1650), 'Fibrinoid necrosis of the wall — PAN, the ANCA vasculitides'),
  (deposits(1280, 1322, 1702, 1716, 14), 'Immune-complex deposits — IgA vasculitis, mixed cryoglobulinemia, PAN (hepatitis B antigen)'),
  (bulge(1300, 1768, 16), 'Aneurysm — PAN (string of pearls), Kawasaki (coronary), Behçet'),
  (thromb(1300, 1828, 24, 10), 'Thrombus in the lumen — Buerger (artery, vein and nerve), Behçet (veins)'),
  ('<path d="M1291 1872 L1300 1884 L1309 1872 M1291 1906 L1300 1894 L1309 1906" style="fill:none;stroke:var(--dk1);stroke-width:4;stroke-linecap:round"/>',
   'Vasospasm with a normal wall — Raynaud phenomenon'),
]
for i, (svg, t) in enumerate(KEY):
    add(svg); text(t, 1345, 1595 + i * 60, 'nf-l2')

# ════════ particles ════════
kinds = dict(rbc=['rbc', '--nf-blood'], mac=['mac', '--dk9'], neu=['neu', '--dk5'], eos=['eos', '--dk3'], ic=['ic', '--dk7'])
groups = [['rbc', 'Red cells'], ['mac', 'Macrophages · T cells'], ['neu', 'Neutrophils (ANCA)'], ['eos', 'Eosinophils'],
          ['ic', 'Immune complexes']]
def m(when, **kw): return dict(when=when if isinstance(when, list) else [when], **kw)
seg = {k: (x0, x1) for k, x0, x1, *_ in SEG}
P = lambda x0, x1: (f'M{x0} {Y} H{x1}', x1 - x0)
flows = []
for k, n, r, sp, mods in (
    ('s1', 4, 8, 170, []),
    ('s2', 4, 7, 150, [m(O('gca', 'tak'), set=dict(rbc=2), speed=.6)]),
    ('s3', 4, 6, 120, [m(O('bue'), set=dict(rbc=2), speed=.4)]),
    ('s4', 3, 5, 90, [m(O('bue'), set=dict(rbc=1)), m(O('ray'), set=dict(rbc=1), speed=.35)]),
):
    d, L = P(*seg[k]); flows.append(dict(d=d, len=L, speed=sp, r=r, base=dict(rbc=n), mods=mods))
flows.append(dict(d=f'M1800 {Y} H2030', len=230, speed=45, r=4, base=dict(rbc=2), mods=[m(O('bue', 'ray'), set=dict(rbc=0))]))
flows.append(dict(d=f'M2030 {Y} H2290', len=260, speed=60, r=5, base=dict(rbc=3), mods=[m(O('bue', 'ray'), set=dict(rbc=1))]))
# the inflammatory cells in the lit rungs
for d, L, when, kind, n, r in (
    ('M250 330 H630', 380, O('gca', 'tak'), 'mac', 3, 7), ('M660 330 H1010', 350, O('gca', 'tak'), 'mac', 3, 7),
    ('M1440 330 H1790', 350, O('gpa', 'egpa'), 'mac', 2, 6),
    ('M1440 330 H1790', 350, O('gpa', 'mpa', 'egpa'), 'neu', 3, 6), ('M1810 330 H2280', 470, O('gpa', 'mpa'), 'neu', 3, 5),
    ('M1440 330 H1790', 350, O('egpa'), 'eos', 3, 6), ('M1810 330 H2280', 470, O('egpa'), 'eos', 3, 5),
    ('M1440 330 H1790', 350, O('igav', 'cryo'), 'ic', 3, 5), ('M1810 330 H2280', 470, O('igav', 'cryo'), 'ic', 4, 5),
    ('M1050 330 H1400', 350, O('pan'), 'ic', 2, 6),
):
    flows.append(dict(d=d, len=L, speed=70, r=r, base={kind: n}, when=when))
# blood in the body's arteries
for d, L, n, mods in (
    (ARCH, 540, 5, []),
    ('M748 925 L640 930 L600 1000 L566 1385', 575, 3, [m(O('tak'), set=dict(rbc=1), speed=.5)]),
    ('M808 962 L880 930 L920 1000 L954 1385', 470, 3, [m(O('tak'), set=dict(rbc=1), speed=.5)]),
    ('M780 962 L748 925 L738 848 L716 830 C700 808 692 790 700 772 C708 754 694 738 700 720', 270, 2, [m(O('gca', 'tak'), set=dict(rbc=1), speed=.5)]),
    (LEG_R, 560, 3, [m(O('bue'), set=dict(rbc=1), speed=.5)]),
    (LEG_L, 520, 3, [m(O('bue'), set=dict(rbc=1), speed=.5)]),
):
    flows.append(dict(d=d, len=L, speed=110, r=5, base=dict(rbc=n), mods=mods))

notes = {
  '': 'Vessels shrink from the aorta to the capillaries, and each vasculitis has its favourite size: large (giant cell, Takayasu), '
      'medium (PAN, Kawasaki, Buerger) or small (the ANCA trio and the immune-complex diseases). Pick one: its rungs light, its '
      'organs light, and the results read ↑ for raised or present, ↓ for negative or absent.',
  'vx:gca': 'Giant cell arteritis: granulomatous arteritis of large to medium arteries of the head (temporal, vertebral, ophthalmic) '
            'in a woman over 50 — one-sided headache, jaw claudication, a very high ESR. Ophthalmic involvement can blind suddenly, '
            'so high-dose glucocorticoids start before the biopsy, which can miss its patchy lesions.',
  'vx:tak': 'Takayasu arteritis: granulomatous thickening and fibrosis of the aortic arch and its great vessels in an Asian woman '
            'under 40. The narrowed branches weaken the arm pulses (pulseless disease) and cause visual and neurologic deficits; '
            'renal artery narrowing raises blood pressure in about half. ESR ↑; glucocorticoids.',
  'vx:pan': 'Polyarteritis nodosa: segmental transmural necrotizing inflammation with fibrinoid necrosis of medium arteries of the '
            'kidney and viscera — never the lungs, and ANCA-negative. About a third carry hepatitis B (HBsAg immune complexes). '
            'The weakened walls bulge into microaneurysms: a string of pearls on angiography.',
  'vx:kaw': 'Kawasaki disease: medium-vessel arteritis of young children — fever 5 days or more with conjunctivitis, rash, a cervical '
            'node, strawberry tongue and red, swollen hands and feet. Its danger is the coronary arteries: aneurysms that thrombose '
            'or rupture, causing MI or sudden death. IV immunoglobulin and aspirin cut that risk.',
  'vx:bue': 'Buerger disease: in a young heavy smoker, segmental thrombosing inflammation of the tibial and radial arteries spreads '
            'into the neighbouring veins and nerves — claudication, severe rest pain, Raynaud, nodular phlebitis, then ulcers and '
            'gangrene of the digits. ESR and CRP stay normal. Stopping smoking is the treatment.',
  'vx:gpa': 'Granulomatosis with polyangiitis: PR3-ANCA (c-ANCA) turns neutrophils on small to medium vessels, beside necrotizing '
            'granulomas of the airway. The triad: upper airway (sinusitis, otitis, septal perforation), lungs (cavitating '
            'nodules, hemoptysis) and kidneys (pauci-immune crescentic GN).',
  'vx:mpa': 'Microscopic polyangiitis: MPO-ANCA (p-ANCA) drives necrotizing vasculitis of capillaries, arterioles and venules — '
            'lesions all the same age, no granulomas, no immune deposits. Necrotizing GN (90%), pulmonary capillaritis with '
            'hemoptysis, palpable purpura; hydralazine can trigger it.',
  'vx:egpa': 'Eosinophilic granulomatosis with polyangiitis (Churg-Strauss): asthma, allergic rhinitis and eosinophilia, then '
             'necrotizing granulomatous vasculitis of small to medium vessels full of eosinophils. Neuropathy, purpura, GI '
             'bleeding; eosinophilic cardiomyopathy is a major cause of death. IgE ↑; MPO-ANCA in about half.',
  'vx:igav': 'IgA vasculitis (Henoch-Schönlein purpura): the most common vasculitis of childhood, often after an upper respiratory '
             'infection. IgA immune complexes lodge in small vessels — palpable purpura on the buttocks and legs, belly pain '
             '(intussusception), arthralgias, hematuria from IgA nephropathy. Platelets are normal.',
  'vx:cryo': 'Mixed cryoglobulinemia: in chronic hepatitis C, mixed IgG and IgM complexes that precipitate in the cold deposit in '
             'small vessels and fix complement (C4 ↓). Palpable purpura, weakness and arthralgias, with neuropathy and '
             'membranoproliferative GN. Treat the hepatitis C.',
  'vx:beh': 'Behçet syndrome: vasculitis of arteries and veins of any size, commoner with Turkish or Eastern Mediterranean descent '
            'and HLA-B51. Recurrent painful oral and genital ulcers, uveitis, erythema nodosum; arterial aneurysms and venous '
            'thrombosis. ESR ↑ but ANA, ANCA and RF negative; pathergy test positive.',
  'vx:pmr': 'Polymyalgia rheumatica: not a vasculitis but its companion — a woman over 50 with pain and stiffness of the shoulders '
            'and hips, fever and weight loss, yet no true weakness. ESR and CRP ↑, CK normal; low-dose glucocorticoids work fast. '
            'It is associated with giant cell arteritis.',
  'vx:ray': 'Raynaud phenomenon: vasospasm, not inflammation, of the small arteries and arterioles of the digits in cold or stress — '
            'white, then blue, then red. Primary: young women, symmetric, benign. Secondary to SLE, scleroderma (CREST) or Buerger: '
            'asymmetric, worsening, with digital ulcers. Dihydropyridine calcium channel blockers.',
}

R = lambda when, d: dict(when=when, d=d)
readouts = [
  dict(l='ESR · CRP', mods=[R(O('gca', 'tak', 'kaw', 'mpa', 'egpa', 'igav', 'beh', 'pmr'), 1), R(O('bue'), 0)]),
  dict(l='PR3-ANCA (c-ANCA)', mods=[R(O('gpa'), 1), R(O('pan', 'beh'), -1)]),
  dict(l='MPO-ANCA (p-ANCA)', mods=[R(O('mpa', 'egpa'), 1), R(O('pan', 'beh'), -1)]),
  dict(l='Granulomas', mods=[R(O('gca', 'tak', 'gpa', 'egpa'), 1), R(O('mpa', 'pan'), -1)]),
  dict(l='Immune-complex deposits', mods=[R(O('igav', 'cryo', 'pan'), 1), R(O('gpa', 'mpa', 'egpa'), -1)]),
  dict(l='Aneurysms', mods=[R(O('pan', 'kaw', 'beh'), 1)]),
  dict(l='Palpable purpura', mods=[R(O('mpa', 'egpa', 'igav', 'cryo'), 1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='vx', label='Vasculitis', type='one', options=[
      ['gca', 'Giant cell (temporal) arteritis', 'gca'], ['tak', 'Takayasu arteritis', 'takayasu'],
      ['pan', 'Polyarteritis nodosa', 'pan'], ['kaw', 'Kawasaki disease', 'kawasaki'], ['bue', 'Buerger disease', 'buerger'],
      ['gpa', 'Granulomatosis with polyangiitis', 'gpa'], ['mpa', 'Microscopic polyangiitis', 'mpa'],
      ['egpa', 'Eosinophilic GPA (Churg-Strauss)', 'egpa'],
      ['igav', 'IgA vasculitis (HSP)', 'igav'], ['cryo', 'Mixed cryoglobulinemia', 'cryo'],
      ['beh', 'Behçet syndrome', 'behcet'],
      ['pmr', 'Polymyalgia rheumatica', 'pmr'], ['ray', 'Raynaud phenomenon', 'raynaud']],
      sections=[['Large vessels', ['gca', 'tak']], ['Medium vessels', ['pan', 'kaw', 'bue']],
                ['Small vessels — ANCA, pauci-immune', ['gpa', 'mpa', 'egpa']],
                ['Small vessels — immune complex', ['igav', 'cryo']], ['Any size', ['beh']],
                ['Related — not a vasculitis', ['pmr', 'ray']]])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 111, 113, 171, 213, 323, 477–481, 614 · Robbins ch 11 · Bootcamp MSK — Vasculitides')

MAP = dict(
  id='vascsim', title='Vasculitis by Vessel Size Simulator', topic='cardio', after='vasc',
  sub='A vessel-size ladder from the aorta to the capillaries above a body — pick a vasculitis and its rung lights with its wall '
      'lesion (granulomas, fibrinoid necrosis, immune complexes, aneurysms, thrombus, vasospasm), its organs light, and the '
      'case card and results (ESR, PR3- and MPO-ANCA, granulomas, deposits, aneurysms, purpura) fill in. Tap a pin for its card',
  w=3500, h=2000,
  fa='111, 113, 171, 213, 323, 360, 477–481, 614', src=SRC,
  lanes=[('vsLarge', 'Large vessels', 'tca'), ('vsMed', 'Medium vessels', 'glycogen'), ('vsSmall', 'Small vessels', 'ppp'),
         ('vsRel', 'Related & lesions', 'sugars')],
  comps=[],
  nodes=[
    ('vs1', 'Large-vessel vasculitis', 520, 552, 'vsLarge', 'granulomatous · over vs under 50', ['gca', 'takayasu', 'pmr', 'subclavsteal'], 'hub'),
    ('vs2', 'Medium-vessel vasculitis', 1225, 552, 'vsMed', 'PAN · Kawasaki · Buerger', ['pan', 'kawasaki', 'buerger', 'hbv']),
    ('vs3', 'ANCA vasculitis', 1610, 552, 'vsSmall', 'pauci-immune', ['gpa', 'mpa', 'egpa', 'rpgn']),
    ('vs4', 'Immune-complex vasculitis', 2030, 552, 'vsSmall', 'IgA · cryoglobulins', ['igav', 'cryo', 'igan', 'hcv', 'mpgn']),
    ('vs5', 'Raynaud phenomenon', 290, 1545, 'vsRel', 'primary vs secondary', ['raynaud', 'sclero', 'ccbs']),
    ('vs6', 'Behçet syndrome', 290, 1880, 'vsRel', 'any size · ulcers · uveitis', ['behcet', 'oralpath', 'uveitis', 'erythnodosum']),
    ('vs7', 'Lesion types', 1960, 1528, 'vsRel', 'granuloma · necrosis · type III', ['chronicinflam', 'necrosis', 'hs3']),
    ('vs8', 'Treatments', 2090, 1420, 'vsRel', 'steroids · cytotoxics · CD20', ['cortico', 'cyclophos', 'rituximab', 'aspirin']),
  ],
  panels=[
    (2420, 1330, 1000, 'Antibodies, granulomas, deposits (First Aid pp. 111, 113, 213, 360, 614)', [
      ('PR3-ANCA · c-ANCA', 'granulomatosis with polyangiitis'),
      ('MPO-ANCA · p-ANCA', 'microscopic polyangiitis, EGPA — also ulcerative colitis, primary sclerosing cholangitis'),
      ('Drug-induced ANCA', 'propylthiouracil (PTU)'),
      ('Granulomatous', 'giant cell arteritis, Takayasu, GPA, EGPA'),
      ('Pauci-immune GN', 'GPA, EGPA, MPA — no immune deposits'),
      ('Type III (immune complex)', 'PAN, IgA vasculitis, SLE')]),
    (2420, 1560, 1000, 'Infections and drugs behind vasculitis (First Aid pp. 171, 479; Robbins ch 11)', [
      ('Hepatitis B', 'polyarteritis nodosa — HBsAg–antibody complexes in about a third'),
      ('Hepatitis C', 'mixed cryoglobulinemia · leukocytoclastic vasculitis'),
      ('Drugs, 7–10 days on', 'cutaneous small-vessel vasculitis: penicillins, cephalosporins, sulfonamides, phenytoin, allopurinol'),
      ('Behçet flares', 'triggered by HSV or parvovirus')]),
  ],
  dyn=dyn,
)
