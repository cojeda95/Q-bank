# m56 — Smell & Taste in Motion (dynamic map, kit data)
# A sagittal head facing left: the nasal cavity with the olfactory epithelium on its roof, the cribriform plate, the
# olfactory bulb on it and the olfactory tract running back to the medial temporal lobe (piriform cortex, amygdala,
# entorhinal) without touching the thalamus; below, the tongue (front ⅔, back ⅓, epiglottis) with VII (chorda tympani →
# geniculate ganglion), IX (petrosal ganglion) and X (nodose ganglion) running to the solitary nucleus in the medulla, and
# on up through VPMpc in the thalamus to the anterior insula / frontal operculum. Insets: the face (VII motor) and both
# optic discs (Foster Kennedy). One `one` switch in five `sections`: the two normal pathways, then 13 causes of smell or
# taste loss. Each option stops, thins or adds particles (odorants, smell signal, taste signal, CSF, amoebae, virus, a
# phantom odor), puts the ✕ where the lesion is and draws its sign. Seven readouts: smell, taste front ⅔, taste back ⅓,
# thalamic relay, LH · FSH, facial movement, gag reflex (↑ present/used · ↓ lost/skipped · ↔ normal · – not stated).
# chemvisc is the static map of the same pathways (a ⇄ pair is fine); cnrefsim (gag reflex, Bell), stemsim (Wallenberg),
# hpgsim / mensflow (Kallmann labs) and papezsim (limbic) are cross-linked, not re-taught.
#
# Sources (all read in the corpus; U+00A0 / U+00AD normalized):
#   First Aid 2025 p. 519 (CN I smell — only CN without a thalamic relay to cortex; VII taste anterior 2/3 via chorda
#     tympani, submandibular + sublingual salivation; IX taste and sensation posterior 1/3; gag reflex IX → X) · p. 508
#     (failure of GnRH neurons to migrate from the olfactory pit → Kallmann; thalamus relays all ascending sensation except
#     olfaction; VPM: trigeminal and gustatory pathway) · p. 364 (taste: anterior 2/3 CN VII, posterior 1/3 mainly IX,
#     extreme posterior X; NTS) · p. 656 (Kallmann: olfactory bulbs fail to develop, hyposmia/anosmia, ↓ GnRH, FSH, LH,
#     testosterone, failure to complete puberty, infertility) · p. 69 (zinc deficiency: dysgeusia, anosmia, delayed wound
#     healing, male hypogonadism, ↓ adult hair; acrodermatitis enteropathica) · p. 153 (Naegleria fowleri: warm freshwater,
#     enters the CNS through the olfactory nerve via the cribriform plate, rapidly fatal meningoencephalitis, amebas in CSF,
#     amphotericin B) · p. 169 (SARS-CoV-2: anosmia, dysgeusia among the symptoms) · p. 225 (aging: ↓ smell and taste) ·
#     p. 527 (PICA / lateral medullary: ↓ gag reflex, dysphagia, hoarseness) · p. 531 (aura may include odd smells or
#     tastes; focal seizures most often medial temporal) · p. 546 (Bell palsy: most common peripheral facial palsy, after
#     HSV reactivation, glucocorticoids ± acyclovir; LMN: upper and lower face; incomplete eye closure, hyperacusis, loss
#     of taste to the anterior tongue) · p. 576 (olfactory hallucinations: often an aura of temporal lobe epilepsy).
#   Fundamental Neuroscience ch 23 (flavor = smell + taste + somatosensation; most "taste" complaints are olfactory;
#     receptor neurons, basal cells, fila through the cribriform plate, bulb with glomeruli and mitral cells, lateral
#     olfactory tract → piriform cortex, amygdala, entorhinal; URI viruses can kill receptor cells; head trauma shears the
#     fila, partial or total, temporary or permanent loss; anterior skull-base fracture: dural tear → CSF rhinorrhea,
#     raccoon eyes, meningitis risk; COVID-19: ACE2 on the olfactory epithelium, anosmia/hyposmia for weeks to months;
#     olfactory groove meningioma from arachnoid cells along the cribriform plate: anosmia (one side; both when advanced),
#     optic nerve compression → optic atrophy and contralateral papilledema = Foster Kennedy; Alzheimer, Parkinson,
#     Huntington: central olfactory pathways, deficits very early, may be among the first signs; age-related decline,
#     gradual and unnoticed; uncinate fit = focal seizure of the uncal temporal lobe with a foul aura (cacosmia); taste:
#     chorda tympani (geniculate ganglion) fungiform papillae; IX lingual-tonsillar branch (petrosal ganglion) vallate +
#     posterior foliate; X superior laryngeal (nodose) epiglottis; rostral (gustatory) solitary nucleus → ipsilateral
#     central tegmental tract → VPMpc → posterior limb internal capsule → frontal operculum + anterior insula, exclusively
#     ipsilateral; reflex salivation and swallowing from the solitary nucleus; Bell palsy impairs taste (HSV suspected,
#     prednisone); chorda leaves VII just distal to the geniculate ganglion; ageusia rare, hypogeusia, dysgeusia — drugs
#     most often; taste buds decrease with age) · ch 11 (lateral medullary / PICA syndrome: loss of taste from the
#     ipsilateral half of the tongue — solitary tract and nucleus; contralateral body and ipsilateral face pain and
#     temperature, vertigo, nystagmus, hoarseness, dysphagia, Horner) · ch 14 (IX lesions rare alone, usually with X and XI
#     at the jugular foramen; diminished taste from the posterior third and loss of stylopharyngeus; the gag reflex depends
#     on IX and X) · ch 6 (Naegleria reaches the subarachnoid space through the nasal / olfactory route; rapidly
#     progressive, usually fatal amebic meningoencephalitis).
#   Guyton ch 54 (anterior 2/3 taste → lingual nerve → chorda tympani → facial nerve → tractus solitarius; circumvallate
#     and posterior mouth → IX; all taste fibers synapse in the solitary nuclei → VPM → gustatory cortex; taste → salivatory
#     nuclei; the bulb lies over the cribriform plate; the lateral olfactory area (prepyriform, pyriform, cortical amygdala)
#     feeds the paleocortex of the anteromedial temporal lobe — the only cortex reached without a thalamic relay).
#   Bootcamp.com Microbiology — Naegleria (supporting only: flagellates invade the olfactory mucosa, ascend the olfactory
#     nerve through the cribriform plate to the bulb). Kept out of `src`.
# Cut for lack of support in the corpus: a smell or taste arrow for Naegleria (no source says anosmia); a taste arrow for
#   cribriform fracture, meningioma, Kallmann or zinc (FA 69 says "dysgeusia" — a distortion, not ↓ → "–"); a taste arrow
#   for COVID-19 (FN reports hypogeusia, ageusia and distortion, no region → "–"); smell / taste-back arrows for Bell; facial
#   or gag arrows in the lateral medulla beyond FA's ↓ gag; ↓ saliva in Bell palsy (FN states it only for lesions of the
#   VII root); the dorsomedial-thalamus route to the orbitofrontal cortex (real, but would muddy "no thalamic relay" — kept
#   to the card); any arrow for the uncinate aura (a smell with no odor is neither ↑ nor ↓ smell).
# Source conflict for the owner: FA p. 508 sends VPM taste to the "1° somatosensory cortex (parietal lobe)"; Fundamental
#   Neuroscience ch 23 sends VPMpc to the anterior insula + frontal operculum (and the rostral tip of area 3b). The map
#   follows FN (insula / operculum) and the panel names both.
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

FN23, FN11, FN14, FN6 = (full('Fundamental Neuroscience', c) for c in (23, 11, 14, 6))
GY54 = full('Guyton', 54)
SRC = [FN23, FN11, FN14, FN6, GY54]

O = lambda *k: ['les:' + x for x in k]
DEF = ['!les:*']

def P(pts): return 'M' + ' L'.join(f'{x} {y}' for x, y in pts)
def plen(pts): return round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(pts, pts[1:])))

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
def XM(x, y, s=14):
    return (f'<circle cx="{x}" cy="{y}" r="{s + 9}" style="fill:var(--surface);opacity:.92"/>'
            f'<path class="dyn-lesion" d="M{x - s} {y - s} L{x + s} {y + s} M{x + s} {y - s} L{x - s} {y + s}"/>')

SMELL_LES = O('postviral', 'cribriform', 'naegleria', 'meningioma', 'kallmann', 'neurodeg', 'uncinate', 'zinc', 'aging', 'flavor')

# ════════ the drawing ════════
text('Smell and taste, side view of the head', 160, 60, 'dyn-big')
text('the face looks left · smell runs back from the nose roof to the temporal lobe · taste runs from the tongue to the medulla, thalamus and insula',
     160, 82, 'dyn-cap')

# skin outline: forehead → nose → lips → chin → neck; back of the head → neck
add('<path d="M400 150 C760 100 1500 96 1860 220 C2060 320 2130 600 2060 860 C2010 1040 1910 1150 1810 1220 L1790 1500" '
    'class="dyn-line" style="stroke-width:3;fill:none;opacity:.7"/>')
add('<path d="M400 150 C320 240 300 420 310 520 C300 560 290 580 280 600 L150 800 Q140 830 170 852 L225 872 '
    'Q212 905 215 935 Q232 960 222 985 Q205 1005 216 1030 Q236 1060 232 1140 C300 1260 600 1300 800 1320 L840 1500" '
    'class="dyn-line" style="stroke-width:3;fill:none;opacity:.7"/>')

# cerebrum (with the temporal pole), cerebellum, brainstem
add('<path d="M380 540 C330 330 600 200 1000 190 C1500 180 1850 300 1930 560 C1975 700 1880 810 1760 820 '
    'C1660 826 1620 760 1600 640 L1290 640 C1270 700 1310 790 1180 800 C1000 810 920 760 900 690 C880 620 800 560 720 548 Z" '
    'class="dyn-cell" style="stroke-width:3"/>')
add('<ellipse cx="1820" cy="1000" rx="120" ry="78" class="dyn-cell" style="stroke-width:3"/>'
    '<path d="M1720 990 Q1820 960 1920 990 M1730 1030 Q1820 1005 1910 1030" class="dyn-line" style="stroke-width:2;opacity:.4;fill:none"/>')
text('cerebellum', 1820, 1004, 'nf-l2', 'middle')
add('<path d="M1440 540 C1440 600 1460 640 1460 660 C1440 720 1450 790 1490 810 L1490 1150 L1590 1150 L1590 810 '
    'C1630 790 1640 700 1610 650 C1600 620 1600 580 1580 540 Z" class="dyn-cell" style="stroke-width:3"/>')
add('<path d="M1462 668 Q1540 700 1608 668 M1490 810 Q1540 826 1590 810" class="dyn-line" style="stroke-width:2;opacity:.4;fill:none"/>')
text('midbrain', 1630, 600, 'nf-l2')
text('pons', 1660, 728, 'nf-l2')
text('medulla', 1606, 968, 'nf-l2')

# thalamus (VPMpc), hypothalamus, pituitary, insula / frontal operculum
add('<ellipse cx="1440" cy="470" rx="112" ry="52" class="dyn-soft" style="stroke:var(--dk8);stroke-width:2.5"/>')
text('Thalamus', 1372, 508, 'nf-l1', 'middle')
add('<circle cx="1490" cy="490" r="12" class="dyn-cell" style="stroke:var(--dk5);stroke-width:3"/>')
text('VPMpc', 1474, 512, 'nf-l2', 'end')
add('<ellipse cx="1360" cy="604" rx="52" ry="22" class="dyn-soft"/>')
text('hypothalamus', 1360, 608, 'nf-l2', 'middle')
add('<path d="M1356 626 L1350 656" class="dyn-line" style="stroke-width:3"/><ellipse cx="1350" cy="670" rx="18" ry="14" class="dyn-cell"/>')
text('pituitary', 1376, 690, 'nf-l2')
add('<ellipse cx="1100" cy="378" rx="160" ry="46" class="dyn-soft" style="stroke:var(--dk5);stroke-width:2.5"/>')
text('Anterior insula · frontal operculum', 1100, 374, 'nf-l1', 'middle')
text('primary taste cortex', 1100, 392, 'nf-l2', 'middle')

# medial temporal lobe: piriform cortex, amygdala, entorhinal (the uncus)
add('<ellipse cx="1110" cy="738" rx="150" ry="40" class="dyn-soft" style="stroke:var(--dk1);stroke-width:2.5"/>')
text('Piriform · amygdala · entorhinal', 1110, 736, 'nf-l1', 'middle')
text('olfactory cortex — medial temporal lobe (uncus)', 1110, 754, 'nf-l2', 'middle')

# nasal cavity: roof epithelium, cribriform plate, conchae, hard + soft palate
add('<path d="M290 612 L800 612 L840 700 L840 900 L240 900" class="dyn-line" style="stroke-width:2;opacity:.35;fill:none"/>')
add('<path d="M800 735 Q560 712 420 742 Q470 770 800 760 M800 815 Q520 795 330 832 Q400 858 800 845" '
    'class="dyn-cell" style="stroke-width:2;opacity:.8"/>')
text('conchae', 600, 790, 'nf-l2', 'middle')
add('<path d="M240 902 L770 906" class="dyn-line" style="stroke-width:7;opacity:.45"/>'
    '<path d="M770 906 Q840 914 880 956 Q884 976 868 972" class="dyn-line" style="stroke-width:6;opacity:.45;fill:none"/>')
text('palate', 500, 896, 'nf-l2', 'middle')
# cribriform plate with holes
add('<rect x="380" y="598" width="350" height="10" rx="3" style="fill:var(--ink-3);opacity:.75"/>')
for hx in range(420, 700, 40):
    add(f'<rect x="{hx}" y="596" width="8" height="14" style="fill:var(--surface)"/>')
# epithelium band and receptor neurons (fila up through the holes)
add('<rect x="390" y="612" width="330" height="14" rx="6" style="fill:var(--dk1);opacity:.35"/>')
for hx in range(424, 700, 40):
    add(f'<path d="M{hx} 626 L{hx} 590" class="dyn-line" style="stroke:var(--dk1);stroke-width:2;opacity:.8"/>')
add('<rect x="390" y="612" width="330" height="14" rx="6" class="dyn-dim" style="fill:var(--ink-3);opacity:.5"/>',
    when=O('postviral', 'zinc', 'aging'))
text('Olfactory epithelium', 470, 652, 'nf-l1', 'middle')
text('receptor neurons · basal cells', 470, 668, 'nf-l2', 'middle')
text('cribriform plate', 730, 652, 'nf-l2', 'middle')
# olfactory bulb (absent in Kallmann) and tract
BULB = ('<ellipse cx="560" cy="572" rx="125" ry="17" class="dyn-cell" style="stroke:var(--dk1);stroke-width:3"/>'
        + ''.join(f'<circle cx="{x}" cy="578" r="6" style="fill:var(--dk1);opacity:.45"/>' for x in (470, 520, 570, 620))
        + ''.join(f'<path d="M{x} 570 l-5 -8 h10 z" style="fill:var(--dk1);opacity:.8"/>' for x in (495, 545, 595)))
add(BULB, unless=O('kallmann'))
add('<ellipse cx="560" cy="572" rx="125" ry="17" class="dyn-cell dyn-dim" style="stroke:var(--bad);stroke-width:2.5;stroke-dasharray:6 5"/>',
    when=O('kallmann'))
text('Olfactory bulb', 470, 538, 'nf-l1', 'middle')
text('glomeruli → mitral cells', 650, 538, 'nf-l2', 'middle', unless=O('meningioma', 'kallmann'))
TRACT = [(684, 572), (860, 600), (960, 665), (1030, 712)]
add(f'<path d="{P(TRACT)}" class="dyn-line" style="stroke:var(--dk1);stroke-width:7;opacity:.4;fill:none;stroke-linecap:round"/>',
    unless=O('kallmann'))
text('lateral olfactory tract', 900, 580, 'nf-l2', 'start', unless=O('kallmann'))

# tongue: front ⅔ (VII), back ⅓ (IX), epiglottis (X)
add('<path d="M252 1005 C300 975 500 955 700 965 C820 975 880 1020 890 1090 L860 1160 C700 1180 400 1122 262 1042 Z" '
    'class="dyn-cell" style="stroke-width:3"/>')
add('<path d="M252 1005 C300 975 500 955 640 962 L640 1146 C500 1120 380 1100 262 1042 Z" style="fill:var(--dk3);opacity:.18"/>')
add('<path d="M640 962 C760 966 860 1000 890 1090 L860 1160 C780 1168 700 1160 640 1146 Z" style="fill:var(--dk7);opacity:.18"/>')
add('<path d="M640 962 L640 1060" class="dyn-dash" style="stroke-width:2.5"/>')
add('<path d="M905 1170 Q930 1110 955 1124 Q950 1160 925 1190 Z" style="fill:var(--dk10);opacity:.5;stroke:var(--ink-3);stroke-width:2"/>')
text('epiglottis', 968, 1128, 'nf-l2')
for bx in (330, 420, 520, 600):
    add(f'<circle cx="{bx}" cy="{988 if bx > 300 else 1000}" r="6" style="fill:var(--dk3);opacity:.85"/>')
for bx in (700, 780):
    add(f'<circle cx="{bx}" cy="{982 if bx == 700 else 1000}" r="8" style="fill:var(--dk7);opacity:.85"/>')
text('front ⅔', 340, 1050, 'nf-l1', 'middle')
text('back ⅓', 760, 1080, 'nf-l1', 'middle')

# taste nerves (VII under, crossing IX and X with a bridge)
N = dict(
  p7a=[(430, 990), (430, 1030), (520, 1190), (980, 1240), (1100, 1150), (1140, 950)],
  p7c=[(1140, 950), (1150, 900), (1190, 852)],
  p7b=[(1190, 852), (1420, 832), (1508, 872)],
  p9a=[(780, 1000), (790, 1032), (940, 1050), (1020, 1040)],
  p9c=[(1020, 1040), (1278, 1000)],
  p9b=[(1278, 1000), (1508, 892)],
  p10a=[(930, 1150), (1080, 1190), (1288, 1142)],
  p10b=[(1288, 1142), (1512, 906)],
  up=[(1530, 880), (1546, 720), (1506, 560), (1490, 492)],
  ctx=[(1490, 492), (1250, 420), (1150, 392)],
)
COL = dict(p7a='--dk3', p7c='--dk3', p7b='--dk3', p9a='--dk7', p9c='--dk7', p9b='--dk7', p10a='--dk10', p10b='--dk10', up='--dk5', ctx='--dk5')
for k in ('p9a', 'p9c', 'p9b', 'p10a', 'p10b', 'up', 'ctx'):
    add(f'<path d="{P(N[k])}" class="dyn-line" style="stroke:var({COL[k]});stroke-width:4;opacity:.7;fill:none;stroke-linejoin:round"/>')
for k in ('p7a', 'p7c', 'p7b'):
    add(f'<path d="{P(N[k])}" class="dyn-line" style="stroke:var(--surface);stroke-width:12;fill:none;stroke-linejoin:round"/>')
    add(f'<path d="{P(N[k])}" class="dyn-line" style="stroke:var(--dk3);stroke-width:4;opacity:.8;fill:none;stroke-linejoin:round"/>')
for (x, y, c, lab, lx, ly, an) in ((1190, 852, '--dk3', 'geniculate g.', 1172, 840, 'end'),
                                   (1278, 1000, '--dk7', 'petrosal g.', 1262, 982, 'end'),
                                   (1288, 1142, '--dk10', 'nodose g.', 1288, 1178, 'middle')):
    add(f'<ellipse cx="{x}" cy="{y}" rx="14" ry="10" class="dyn-cell" style="stroke:var({c});stroke-width:3"/>')
    text(lab, lx, ly, 'nf-l2', an)
text('VII · chorda tympani', 760, 1262, 'nf-l2', 'middle')
add('<circle cx="1530" cy="880" r="15" class="dyn-cell" style="stroke:var(--dk5);stroke-width:3"/>')

# highlights for the two normal pathways
add(f'<path d="{P(TRACT)}" class="dyn-hl" style="opacity:.35"/>'
    '<ellipse cx="560" cy="572" rx="132" ry="24" class="dyn-hl" style="opacity:.3"/>'
    '<ellipse cx="1110" cy="738" rx="156" ry="46" class="dyn-hl" style="opacity:.3"/>', when=O('smell'))
text('smell skips the thalamus', 1300, 448, TAG, 'end', when=O('smell'))
add(''.join(f'<path d="{P(N[k])}" class="dyn-hl" style="opacity:.3"/>' for k in N)
    + '<ellipse cx="1440" cy="470" rx="118" ry="58" class="dyn-hl" style="opacity:.25"/>'
    + '<ellipse cx="1100" cy="378" rx="166" ry="52" class="dyn-hl" style="opacity:.3"/>', when=O('taste'))
text('every taste fiber relays in VPMpc — same side all the way', 1300, 448, TAG, 'end', when=O('taste'))

# ── lesions and their signs ──
TX, TY = 410, 506                                  # tag spot for smell lesions (frontal lobe)
# cribriform plate fracture + CSF rhinorrhea
add('<path d="M540 586 L556 600 L546 612 L566 628" class="dyn-lesion" style="fill:none"/>' + XM(600, 604, 12), when=O('cribriform'))
text('plate fractured: fila sheared, dura torn → CSF out of the nose', TX, TY, TAG, when=O('cribriform'))
# olfactory groove meningioma
add('<path d="M600 560 C590 520 640 500 690 512 C740 524 744 566 720 590 C690 600 630 596 600 560 Z" '
    'style="fill:var(--bad);opacity:.55;stroke:var(--bad);stroke-width:2.5"/>', when=O('meningioma'))
text('meningioma on the cribriform plate presses the bulb and tract', TX, TY - 26, TAG, when=O('meningioma'))
text('→ and the optic nerve (inset below)', TX, TY - 8, TAG, when=O('meningioma'))
# post-viral
text('virus kills olfactory receptor cells (SARS-CoV-2 enters by ACE2)', TX, TY, TAG, when=O('postviral'))
# Naegleria: warm freshwater at the nostril
add('<path d="M20 920 q20 -10 40 0 t40 0 t40 0 M20 945 q20 -10 40 0 t40 0 t40 0" class="dyn-line" style="stroke:var(--nf-h2o);stroke-width:3;fill:none"/>',
    when=O('naegleria'))
text('warm fresh water', 20, 975, 'nf-l2', when=O('naegleria'))
text('amoebae climb the olfactory nerve through the plate into the brain', TX, TY, TAG, when=O('naegleria'))
# Kallmann: GnRH neurons never leave the olfactory pit
add('<path d="M720 618 C900 560 1150 560 1308 600" class="dyn-dash" style="stroke:var(--dk11);stroke-width:3;fill:none"/>' + XM(820, 580, 11),
    when=O('kallmann'))
text('no bulb · GnRH neurons never reach the hypothalamus', TX, TY, TAG, when=O('kallmann'))
# Parkinson / Alzheimer
add('<ellipse cx="560" cy="572" rx="130" ry="22" class="dyn-dim" style="fill:var(--ink-3);opacity:.35"/>'
    f'<path d="{P(TRACT)}" class="dyn-dim" style="stroke:var(--ink-3);stroke-width:12;opacity:.35;fill:none"/>'
    '<ellipse cx="1110" cy="738" rx="150" ry="40" class="dyn-dim" style="fill:var(--ink-3);opacity:.25"/>', when=O('neurodeg'))
text('central olfactory pathways degenerate — often the first sign', TX, TY, TAG, when=O('neurodeg'))
# uncinate fit
add('<ellipse cx="1110" cy="738" rx="156" ry="46" class="dyn-hl"><animate attributeName="opacity" values=".1;.6;.1" dur="0.9s" repeatCount="indefinite"/></ellipse>',
    when=O('uncinate'))
text('seizure focus in the uncus: a foul smell with no odor', 1110, 818, TAG, 'middle', when=O('uncinate'))
# zinc, aging, flavor
text('zinc deficiency: anosmia and dysgeusia', TX, TY, TAG, when=O('zinc'))
text('fewer receptor cells and taste buds with age', TX, TY, TAG, when=O('aging'))
add('<circle cx="430" cy="960" r="20" style="fill:var(--dk11);opacity:.45"/>', when=O('flavor'))
text('food aroma rises behind the palate — retronasal smell', TX, TY, TAG, when=O('flavor'))
text('smell lost: food “has no taste”, yet taste buds work', 300, 1100, TAG, when=O('flavor'))
# taste nerve lesions (✕ drawn by the sites); tags
text('Bell palsy: VII in the facial canal', 1118, 958, TAG, 'end', when=O('bell'))
text('IX cut (jugular foramen)', 1000, 1078, TAG, 'end', when=O('cn9'))
text('PICA infarct: solitary nucleus lost', 1606, 1060, TAG, when=O('latmed'))

# ── what the patient shows ──
SIGN = [('smell', 'normal smell: odorant → receptor neuron → bulb → piriform cortex, no thalamus'),
        ('taste', 'normal taste: tongue → VII, IX, X → solitary nucleus → VPMpc → insula'),
        ('postviral', 'anosmia after a cold or COVID-19 — weeks to months, sometimes for good'),
        ('cribriform', 'anosmia after head trauma · clear nasal drip (CSF) · raccoon eyes'),
        ('naegleria', 'swimmer, days later: headache, fever, stiff neck → coma'),
        ('meningioma', 'anosmia (one side first) · optic atrophy + papilledema opposite'),
        ('kallmann', 'no puberty · anosmia · low GnRH, LH, FSH'),
        ('neurodeg', 'hyposmia years before the tremor or the memory loss'),
        ('uncinate', 'brief foul smell (burnt rubber) → then the seizure'),
        ('bell', 'whole half of the face weak · taste lost on the front of the tongue'),
        ('cn9', 'taste lost on the back third · weak gag on that side'),
        ('latmed', 'ipsilateral taste loss · hoarse · dysphagia · ↓ gag · vertigo'),
        ('zinc', 'poor wound healing · hair loss · hypogonadism · smell and taste off'),
        ('aging', 'gradual, unnoticed loss · adds more sugar and salt'),
        ('flavor', 'complains of taste · the taste test is normal · the smell test is not')]
for k, s in SIGN:
    text(s, 160, 1500, TAG, when=O(k))
text('Pick a pathway or a lesion — the sign shows here', 160, 1500, 'nf-l2', when=DEF)

# ── tongue key ──
add('<rect x="160" y="1340" width="560" height="120" rx="18" class="dyn-soft"/>')
text('Taste by region (First Aid p. 364)', 180, 1368, 'nf-l1')
for i, (c, t) in enumerate((('--dk3', 'front ⅔ · fungiform · VII chorda tympani'),
                            ('--dk7', 'back ⅓ · vallate, foliate · IX'),
                            ('--dk10', 'epiglottis · X (superior laryngeal)'))):
    add(f'<circle cx="192" cy="{1392 + i * 24}" r="7" style="fill:var({c})"/>')
    text(t, 208, 1396 + i * 24, 'nf-l2')

# ── face inset (CN VII motor) ──
FX, FY = 1120, 1720
add(f'<rect x="{FX - 200}" y="1560" width="400" height="330" rx="22" class="dyn-soft"/>')
text('Face (VII motor)', FX - 180, 1590, 'nf-l1')
add(f'<ellipse cx="{FX}" cy="{FY + 20}" rx="105" ry="130" class="dyn-cell" style="stroke-width:3"/>')
def face(droop):
    d = 14 if droop else 0
    out = (f'<path d="M{FX - 70} {FY - 40} q25 -14 50 0" class="dyn-line" style="stroke-width:4;fill:none"/>'
           f'<path d="M{FX + 20} {FY - 40 + d} q25 {-14 + d // 2} 50 0" class="dyn-line" style="stroke-width:4;fill:none"/>'
           f'<ellipse cx="{FX - 45}" cy="{FY - 12}" rx="16" ry="{4 if not droop else 4}" style="fill:var(--dyn-lost)"/>'
           f'<ellipse cx="{FX + 45}" cy="{FY - 12 + d // 2}" rx="16" ry="{4 if not droop else 10}" style="fill:var(--dyn-lost)"/>'
           f'<path d="M{FX} {FY} l-8 36 h16" class="dyn-line" style="stroke-width:2.5;fill:none"/>'
           f'<path d="M{FX - 45} {FY + 70} Q{FX} {FY + 90} {FX + 45} {FY + 70 + d}" class="dyn-line" style="stroke-width:4;fill:none"/>')
    return out
add(face(False), unless=O('bell'))
add(face(True), when=O('bell'))
text('patient’s left: brow, lid and mouth sag', FX, 1878, TAG, 'middle', when=O('bell'))

# ── optic discs inset (Foster Kennedy) ──
DX = 1560
add(f'<rect x="{DX - 180}" y="1560" width="640" height="330" rx="22" class="dyn-soft"/>')
text('Optic discs (fundus)', DX - 160, 1590, 'nf-l1')
for i, x in enumerate((DX, DX + 280)):
    add(f'<circle cx="{x}" cy="1720" r="90" class="dyn-cell" style="stroke-width:3"/>')
    add(f'<circle cx="{x}" cy="1720" r="26" style="fill:var(--dk3);opacity:.6"/>', unless=O('meningioma'))
    add(f'<path d="M{x} 1694 q-40 -30 -70 -20 M{x} 1746 q-40 30 -70 20 M{x + 20} 1700 q30 -30 60 -24 M{x + 20} 1740 q30 30 60 24" '
        f'class="dyn-line" style="stroke:var(--bad);stroke-width:3;opacity:.6;fill:none"/>')
text('tumor side', DX, 1836, 'nf-l2', 'middle')
text('other eye', DX + 280, 1836, 'nf-l2', 'middle')
add(f'<circle cx="{DX}" cy="1720" r="26" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:3"/>', when=O('meningioma'))
add(f'<circle cx="{DX + 280}" cy="1720" r="40" style="fill:var(--dk3);opacity:.45"/>'
    f'<circle cx="{DX + 280}" cy="1720" r="48" class="dyn-dash" style="stroke:var(--bad);stroke-width:3;fill:none"/>', when=O('meningioma'))
text('optic atrophy (pale)', DX, 1860, TAG, 'middle', when=O('meningioma'))
text('papilledema (swollen)', DX + 280, 1860, TAG, 'middle', when=O('meningioma'))

# ════════ particles ════════
kinds = {'od': ['od', '--dk6'], 'food': ['food', '--dk11'], 'olf': ['olf', '--dk1'], 'tst': ['tst', '--dk5'],
         'csf': ['csf', '--nf-h2o'], 'amb': ['amb', '--dk2'], 'vir': ['vir', '--dk12'], 'ph': ['ph', '--dk9']}
groups = [['od', 'Odorants'], ['food', 'Food aroma'], ['olf', 'Smell signal'], ['tst', 'Taste signal'], ['csf', 'CSF'],
          ['amb', 'Amoebae'], ['vir', 'Virus'], ['ph', 'Phantom odor']]
flows = []
def fl(pts, kind, n, when=None, unless=None, mods=None, sp=120, r=6):
    f = dict(d=P(pts), len=plen(pts), speed=sp, r=r, base={kind: n})
    if when: f['when'] = when
    if unless: f['unless'] = unless
    if mods: f['mods'] = mods
    flows.append(f)
NOSM = O('taste')
NOTS = O('smell')
fl([(60, 850), (205, 860), (330, 760), (470, 632)], 'od', 3, unless=NOSM)
fl([(60, 872), (212, 868), (400, 780), (620, 632)], 'od', 3, unless=NOSM + O('flavor'))
fl([(430, 955), (800, 952), (920, 890), (872, 720), (680, 632)], 'food', 4, when=O('flavor'))
LOW_EP = O('postviral', 'zinc', 'aging')
fl([(470, 620), (480, 596), (560, 574), (684, 572)], 'olf', 3, unless=NOSM + O('cribriform', 'kallmann', 'flavor'),
   mods=[dict(when=LOW_EP, set={'olf': 1})])
fl(TRACT, 'olf', 4, unless=NOSM + O('cribriform', 'kallmann', 'flavor', 'meningioma'),
   mods=[dict(when=LOW_EP + O('neurodeg'), set={'olf': 1})])
fl([(600, 548), (600, 640), (420, 790), (215, 868), (190, 960)], 'csf', 6, when=O('cribriform'), sp=90, r=7)
fl([(40, 912), (205, 866), (380, 760), (560, 624), (560, 572), (700, 470), (920, 380)], 'amb', 5, when=O('naegleria'), sp=70, r=8)
fl([(420, 640), (700, 640), (700, 690), (420, 690), (420, 640)], 'vir', 5, when=O('postviral'), sp=60, r=6)
fl([(1110, 738), (1020, 650)], 'ph', 2, when=O('uncinate'), sp=50)
fl([(1110, 738), (1220, 650)], 'ph', 2, when=O('uncinate'), sp=50)
TLOW = [dict(when=O('aging'), set={'tst': 1})]
fl(N['p7a'], 'tst', 4, unless=NOTS, mods=TLOW)
fl(N['p7c'] + N['p7b'][1:], 'tst', 2, unless=NOTS + O('bell'), mods=TLOW)
fl(N['p9a'], 'tst', 2, unless=NOTS, mods=TLOW)
fl(N['p9c'] + N['p9b'][1:], 'tst', 3, unless=NOTS + O('cn9'), mods=TLOW)
fl(N['p10a'] + N['p10b'][1:], 'tst', 3, unless=NOTS, mods=TLOW)
fl(N['up'] + N['ctx'][1:], 'tst', 4, unless=NOTS + O('latmed'), mods=TLOW)

# ════════ sites (tap targets) ════════
sites = [
  dict(x=560, y=626, n=[0, 1], w=8, t='rec', l='', s='', ions=[], c='olfactpath', aria='Olfactory epithelium',
       low=LOW_EP, stop=O('flavor')),
  dict(x=600, y=604, n=[0, 1], w=8, t='rec', l='', s='', ions=[], c='smelldisorders', aria='Cribriform plate', block=O('cribriform')),
  dict(x=420, y=572, n=[0, -1], w=16, t='rec', l='', s='', ions=[], c='olfactpath', aria='Olfactory bulb',
       block=O('kallmann'), low=O('neurodeg')),
  dict(x=1110, y=702, n=[0, -1], w=10, t='rec', l='', s='', ions=[], c='olfactpath', aria='Piriform cortex',
       boost=O('uncinate')),
  dict(x=520, y=988, n=[0, -1], w=10, t='rec', l='', s='', ions=[], c='tastepath', aria='Taste buds, front of the tongue', low=O('aging')),
  dict(x=780, y=1000, n=[0, -1], w=10, t='rec', l='', s='', ions=[], c='tongueanat', aria='Taste buds, back of the tongue', low=O('aging')),
  dict(x=1140, y=950, n=[1, 0], w=8, t='rec', l='', s='', ions=[], c='bell', aria='Facial nerve in the facial canal', block=O('bell')),
  dict(x=1020, y=1040, n=[0, 1], w=8, t='rec', l='', s='', ions=[], c='jugfor', aria='Glossopharyngeal nerve', block=O('cn9')),
  dict(x=1530, y=880, n=[1, 0], w=26, t='rec', l='Solitary nucleus', s='rostral part = taste', ions=[], c='nts',
       lx=1610, ly=876, la='start', block=O('latmed')),
  dict(x=1490, y=490, n=[1, 0], w=20, t='rec', l='', s='', ions=[], c='thalnuc', aria='VPMpc of the thalamus', stop=O('latmed')),
  dict(x=1100, y=334, n=[0, -1], w=8, t='rec', l='', s='', ions=[], c='tastepath', aria='Gustatory cortex', stop=O('latmed')),
]

# ════════ readouts ════════
R = lambda keys, d: dict(when=O(*keys), d=d)
readouts = [
  dict(l='Smell', mods=[R(['smell'], 0), R(['flavor', 'postviral', 'cribriform', 'meningioma', 'kallmann', 'neurodeg', 'zinc', 'aging'], -1)]),
  dict(l='Taste · front ⅔', mods=[R(['taste', 'flavor'], 0), R(['bell', 'latmed', 'aging'], -1)]),
  dict(l='Taste · back ⅓', mods=[R(['taste', 'flavor'], 0), R(['cn9', 'latmed', 'aging'], -1)]),
  dict(l='Thalamic relay', mods=[R(['taste'], 1), R(['smell'], -1)]),
  dict(l='LH · FSH', mods=[R(['kallmann'], -1)]),
  dict(l='Facial movement', mods=[R(['bell'], -1)]),
  dict(l='Gag reflex', mods=[R(['cn9', 'latmed'], -1)]),
]

notes = {
  '': 'Smell (left, top) and taste (left, bottom) on one side of the head. Pick a pathway or a cause of smell or taste loss and '
      'watch where the signal stops. ↑ present or used · ↓ lost or skipped · ↔ normal · – not stated by the sources.',
  'les:smell': 'Smell: odorants dissolve on the epithelium in the roof of the nose; receptor neurons (renewed from basal cells) '
               'send their fila through the cribriform plate to glomeruli in the bulb, and mitral-cell axons run in the lateral '
               'olfactory tract to the piriform cortex, amygdala and entorhinal cortex. CN I is the only cranial nerve with no '
               'thalamic relay to cortex.',
  'les:taste': 'Taste: the front two-thirds of the tongue sends taste in the chorda tympani of VII, the back third in IX, the '
               'epiglottis in X. All three end in the rostral (gustatory) solitary nucleus, which projects to VPMpc of the thalamus '
               'and on to the anterior insula and frontal operculum — on the same side all the way.',
  'les:postviral': 'Post-viral anosmia: the viruses of a cold can kill olfactory receptor cells, and SARS-CoV-2 uses ACE2, which the '
                   'olfactory epithelium expresses richly. Smell is lost or reduced for weeks to months, in some for good; COVID-19 '
                   'can also distort taste.',
  'les:cribriform': 'Anterior skull-base fracture: the bulb shears against the cribriform plate and the olfactory fila tear — partial '
                    'or total anosmia, temporary or permanent. A torn dura leaks CSF out of the nose (rhinorrhea), opening a path for '
                    'meningitis; raccoon eyes may appear.',
  'les:naegleria': 'Naegleria fowleri: after swimming in warm fresh water, the amoeba enters the nose and climbs the olfactory nerve '
                   'through the cribriform plate into the brain — a rapidly fatal meningoencephalitis with amoebae in the CSF. '
                   'Amphotericin B has saved a few.',
  'les:meningioma': 'Olfactory groove meningioma arises from arachnoid cells along the cribriform plate. It costs smell on one side, '
                    'both when large, and pressing the optic nerve gives optic atrophy on that side with papilledema in the other eye '
                    '— the Foster Kennedy syndrome.',
  'les:kallmann': 'Kallmann syndrome: GnRH neurons fail to migrate from the olfactory pit and the olfactory bulbs never form. '
                  'Anosmia or hyposmia with hypogonadotropic hypogonadism — ↓ GnRH, LH, FSH and sex steroids, so puberty does not '
                  'complete. The labs are on the HPG axis map.',
  'les:neurodeg': 'Alzheimer and Parkinson disease (also Lewy body disease and Huntington chorea) damage the central olfactory '
                  'pathways. The hyposmia comes very early and may be among the first signs of the disease.',
  'les:uncinate': 'Uncinate fit: a focal seizure arising in the uncus of the medial temporal lobe begins with an unpleasant smell '
                  'that has no source (cacosmia, a phantosmia) — the aura of a temporal lobe seizure.',
  'les:bell': 'Bell palsy: the facial nerve swells in the facial canal (HSV reactivation suspected). The chorda tympani leaves VII '
              'below the geniculate ganglion, so a lesion here costs taste on the front two-thirds plus the whole half of the face, '
              'forehead included, and hyperacusis. Glucocorticoids, ± acyclovir.',
  'les:cn9': 'Glossopharyngeal (IX) lesion — rare alone, usually with X and XI at the jugular foramen. Taste is lost on the back '
             'third of the tongue, and the gag reflex weakens because IX is its afferent limb.',
  'les:latmed': 'Lateral medullary (Wallenberg) syndrome, PICA or vertebral artery: the solitary tract and nucleus are infarcted, so '
                'taste is lost from the whole ipsilateral half of the tongue, with ↓ gag, hoarseness, dysphagia, vertigo, Horner '
                'and crossed pain–temperature loss.',
  'les:zinc': 'Zinc deficiency: anosmia and dysgeusia, with delayed wound healing, hair loss, male hypogonadism and suppressed '
              'immunity; the inherited form is acrodermatitis enteropathica.',
  'les:aging': 'Aging: smell and taste both fall — receptor cells and taste buds decline and transduction weakens. The loss is '
               'gradual and usually unnoticed, so older patients salt and sweeten food more.',
  'les:flavor': 'Flavor is smell + taste + touch. Food aroma reaches the epithelium from behind the palate (retronasal), so when '
                'smell is lost the patient says food has no taste — yet the five basic tastes test normal. Most “taste” complaints '
                'are smell problems.',
}

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='les', label='Pathway or cause — pick one', type='one', options=[
      ['smell', 'Smell pathway', 'olfactpath'], ['taste', 'Taste pathway', 'tastepath'],
      ['postviral', 'Post-viral (cold, COVID-19)', 'corona'], ['cribriform', 'Cribriform plate fracture', 'smelldisorders'],
      ['naegleria', 'Naegleria fowleri', 'naegleria'], ['meningioma', 'Olfactory groove meningioma', 'meningioma'],
      ['kallmann', 'Kallmann syndrome', 'kallmann'], ['neurodeg', 'Early Parkinson or Alzheimer', 'parkinson'],
      ['uncinate', 'Uncinate fit (aura)', 'focalseiz'],
      ['bell', 'Bell palsy (VII)', 'bell'], ['cn9', 'CN IX lesion', 'jugfor'], ['latmed', 'Lateral medulla (PICA)', 'wallenberg'],
      ['zinc', 'Zinc deficiency', 'zinc'], ['aging', 'Aging', 'normalaging'], ['flavor', '“Taste” loss that is smell', 'smelldisorders']],
      sections=[['Normal pathways', ['smell', 'taste']],
                ['Smell — nose and cribriform plate', ['postviral', 'cribriform', 'naegleria', 'meningioma']],
                ['Smell — bulb and brain', ['kallmann', 'neurodeg', 'uncinate']],
                ['Taste — nerves and brainstem', ['bell', 'cn9', 'latmed']],
                ['Whole body and look-alikes', ['zinc', 'aging', 'flavor']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 69, 153, 169, 225, 364, 508, 519, 527, 531, 546, 576, 656 · Fundamental Neuroscience ch 6, 11, 14, 23 · Guyton ch 54')

MAP = dict(
  id='smellsim', title='Smell & Taste in Motion', topic='neuro', after='chemvisc',
  sub='Odorants to the olfactory epithelium, through the cribriform plate to the bulb and the piriform cortex with no thalamus; '
      'taste from the tongue in VII, IX and X to the solitary nucleus, VPMpc and the insula — then what stops each: viruses, '
      'a fractured plate, Naegleria, a meningioma, Kallmann, early neurodegeneration, an uncinate fit, Bell palsy, IX, the '
      'lateral medulla, zinc, age and the flavor mix-up. Tap a pin for its card',
  w=3500, h=2120,
  fa='69, 153, 169, 225, 364, 508, 519, 527, 531, 546, 576, 656', src=SRC,
  lanes=[('smOlf', 'Smell', 'glycolysis'), ('smTst', 'Taste', 'tca'), ('smDz', 'Disorders', 'glycogen')],
  comps=[],
  nodes=[
    ('sm1', 'Olfactory pathway', 2640, 1500, 'smOlf', 'epithelium · bulb · piriform', ['olfactpath'], 'hub'),
    ('sm2', 'Smell loss & flavor', 2640, 1580, 'smOlf', 'anosmia · parosmia · CSF leak', ['smelldisorders'], 'hub'),
    ('sm3', 'Kallmann syndrome', 2640, 1660, 'smDz', 'no bulb, no GnRH', ['kallmann']),
    ('sm4', 'Meningioma', 2640, 1740, 'smDz', 'olfactory groove · Foster Kennedy', ['meningioma']),
    ('sm5', 'Naegleria fowleri', 2640, 1820, 'smDz', 'up the olfactory nerve', ['naegleria']),
    ('sm6', 'COVID-19', 2640, 1900, 'smDz', 'ACE2 on the epithelium', ['corona']),
    ('sm7', 'Parkinson · Alzheimer', 2640, 1980, 'smDz', 'hyposmia comes first', ['parkinson', 'alzheimer']),
    ('sm8', 'Uncinate fit', 2640, 2060, 'smDz', 'focal seizure · olfactory aura', ['focalseiz', 'perception']),
    ('sm9', 'Taste pathway', 3110, 1500, 'smTst', 'buds · VII IX X · VPMpc · insula', ['tastepath'], 'hub'),
    ('sm10', 'Tongue innervation', 3110, 1580, 'smTst', 'taste VII/IX · touch V3/IX', ['tongueanat']),
    ('sm11', 'Solitary nucleus · VPM', 3110, 1660, 'smTst', 'rostral = gustatory', ['nts', 'thalnuc']),
    ('sm12', 'Saliva', 3110, 1740, 'smTst', 'taste drives salivation', ['salivaphys']),
    ('sm13', 'Bell palsy', 3110, 1820, 'smDz', 'VII · front ⅔ taste', ['bell']),
    ('sm14', 'CN IX · gag reflex', 3110, 1900, 'smDz', 'back ⅓ taste · jugular foramen', ['jugfor']),
    ('sm15', 'Lateral medullary syndrome', 3110, 1980, 'smDz', 'PICA · solitary nucleus', ['wallenberg']),
    ('sm16', 'Zinc · aging', 3110, 2060, 'smDz', 'anosmia, dysgeusia · ↓ smell, taste', ['zinc', 'normalaging']),
  ],
  panels=[
    (2420, 1060, 1000, 'Two chemical senses, two routes (First Aid pp. 364, 508, 519; Fund. Neurosci. ch 23)', [
      ('Smell (CN I)', 'bulb → piriform · amygdala · entorhinal — no thalamus'),
      ('Taste, front ⅔', 'fungiform papillae · VII chorda tympani'),
      ('Taste, back ⅓', 'vallate and foliate papillae · IX'),
      ('Epiglottis', 'X (superior laryngeal nerve)'),
      ('All taste', 'rostral solitary nucleus → VPMpc → insula'),
      ('Taste cortex', 'FN: insula + frontal operculum · FA: “1° somatosensory”')]),
    (2420, 1270, 1000, 'Naming the loss (Fund. Neurosci. ch 23)', [
      ('Anosmia · hyposmia', 'no smell · less smell'),
      ('Parosmia · phantosmia', 'a smell distorted · a smell with no odor'),
      ('Ageusia', 'all taste lost — rare: three nerves carry it'),
      ('Hypogeusia · dysgeusia', 'less taste · distorted taste (drugs most often)'),
      ('Olfactory agnosia', 'detects a smell but cannot name it')]),
  ],
  dyn=dyn,
)
