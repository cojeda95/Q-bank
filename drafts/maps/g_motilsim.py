# m57 — Gut Motility & Enteric Reflexes in Motion (dynamic map, kit data)
# Four drawn regions: the extrinsic nerves (medulla + vagus, the T5–L2 cord and the prevertebral ganglia), the stomach and
# duodenum (LES and diaphragm, orad and caudad stomach, pylorus), the colon down to the anal sphincters (with S2–S4, pelvic
# and pudendal nerves), and a long strip of small-intestine wall with every layer (mucosa with EC cells, submucosa +
# Meissner plexus, circular muscle, Auerbach plexus, longitudinal muscle) carrying a bolus. One `one` switch in four
# sections picks a circuit or a reflex: peristaltic reflex, myenteric plexus, submucosal plexus, slow waves; LES, receptive
# relaxation, pyloric pump, enterogastric reflex, fat/CCK; migrating motor complex, gastrocolic and defecation reflexes;
# parasympathetic and sympathetic drive. Six readouts. Three new cards (entericreflex, gastricmotility, les).
# `ansreg` is pinned as a node only, NOT put on the parasympathetic/sympathetic options (coverage3: it would open this gut
# map for 16 generic ANS questions in other blocks).
#
# Sources (all read in the corpus; the course text wins for this block):
#   OCOM GI Exam 1 lecture notes (corpus/gastro/course_exam1_lecture_notes.txt) pp. 12–13 (submucosal vs myenteric plexus
#     table: Meissner → secretion, absorption, local blood flow, muscularis mucosae; Auerbach → tone, rate and intensity of
#     rhythmic contractions, conduction velocity of peristalsis; inhibitory NO/VIP/ATP neurons relax LES, pyloric and
#     ileocecal sphincters) · pp. 23–26 (parasympathetic long preganglionic fibres to the plexuses, sympathetic T5–L2 short
#     preganglionic to celiac/SMG/IMG/hypogastric ganglia; parasympathetic ↑ contraction, relaxes sphincters, ↑ secretion,
#     secondarily ↑ local mucosal blood flow; sympathetic relaxes the wall, contracts sphincters, ↓ motility, inhibits
#     secretion, vasoconstricts; vagus to esophagus … ascending colon and proximal transverse colon, pelvic S2–S4 from the
#     distal transverse colon to the anal canal; vagus 75–80% afferent; vagovagal reflex NTS → dorsal motor nucleus;
#     receptive relaxation vagovagal, VIP and NO, up to 1.5 L; gastrocolic reflex = long-arc reflex → ↑ colonic motility and
#     mass movements; IPANs fired by 5-HT from enterochromaffin cells; excitatory ACh + substance P behind the bolus,
#     inhibitory VIP, NO, ATP ahead and at sphincters; NE inhibits transmitter release from enteric neurons) · pp. 33–35
#     (ICC slow waves 3–5/min caudad stomach; mixing waves from mid-stomach every 15–20 s; pyloric pump ~20% of the time,
#     50–70 cm H2O; pyloric sphincter 50–100% thicker, tonic, passes fluids, holds solids; retropulsion grinds to < 1 mm;
#     duodenal stimuli: distension, pH < 3.5–4, osmolality, protein/fat products, irritation; enterogastric reflexes within
#     30 s via myenteric, sympathetic (prevertebral ganglia) and vagal routes → inhibit the pyloric pump, ↑ pyloric tone;
#     CCK the most potent hormonal inhibitor of emptying, slows antral propulsion, ↑ pyloric tone; LES ~3 cm, ~30 mm Hg,
#     above the negative intrathoracic pressure; crura give pinch-valve reinforcement; 1–2 cm intra-abdominal segment →
#     flap-valve closure; transient LES relaxations → GERD).
#   Costanzo ch 8 (course_sdl_4_7_physio pp. 1–5, 13–22): wall layers and plexuses; vagus 75% afferent; four sympathetic
#     ganglia; Table 8.1 (ACh contracts the wall and relaxes sphincters, NE relaxes the wall and contracts sphincters);
#     slow waves from ICC, not changed by nerves or hormones, stomach 3, duodenum 12, ileum 9 per minute; phasic vs tonic;
#     receptive relaxation (vagovagal, VIP, vagotomy abolishes it, 1.5 L); parasympathetic/gastrin/motilin ↑ and
#     sympathetic/secretin/GIP ↓ gastric force; MMC every 90 min (motilin); emptying ~3 h, liquids > solids, isotonic first,
#     ≤ 1 mm, fat via CCK and H⁺ via ENS reflexes; peristaltic reflex (ECL cells, 5-HT, IPANs, reciprocal innervation);
#     mass movements 1–3/day; defecation (rectosphincteric reflex, urge at 25% capacity, voluntary external sphincter,
#     Valsalva); gastrocolic reflex (parasympathetic afferent limb, CCK/gastrin efferent limb).
#   Guyton ch 63 (course_sdl_4_7_guyton_supplement pp. 6–26): spikes on slow waves, Ca²⁺ entry; stretch/ACh depolarize,
#     NE hyperpolarizes; plexus functions; excitatory ACh/substance P/glutamate and inhibitory VIP/NO/ATP; sacral S2–S4 via
#     pelvic nerves to the distal colon and anus; sympathetic T5–L2, NE mainly inhibits the enteric neurons; vagus 80%
#     afferent; three reflex types (gastrocolic and enterogastric via prevertebral ganglia; defecation via the cord);
#     motilin, interdigestive complexes every 90 min; peristaltic (myenteric) reflex needs the myenteric plexus; atropine
#     blocks it; sympathetic → intense arteriolar vasoconstriction, ↓ splanchnic flow in exercise and shock; parasympathetic
#     to stomach and lower colon ↑ local blood flow with secretion.
#   Guyton ch 64 (course_sdl_4_7_guyton_supplement_p2 pp. 6–23): LES 3 cm, 30 mm Hg, valvelike closure; vagovagal
#     accommodation 0.8–1.5 L; mixing waves, retropulsion, pyloric pump, pylorus; enterogastric reflexes and stimuli; hormones
#     inhibit the pump and tighten the pylorus; motilin stops after food; mass movements, gastrocolic reflex needs extrinsic
#     nerves; defecation reflexes (intrinsic weak, sacral parasympathetic strong; pudendal external sphincter).
#   Pawlina ch 17 (course_sdl_2_3_histo_forgut_p2 p. 9): LES reinforced by the diaphragm. Moore ch 5: the right crus loops
#     around the esophagus (physiological inferior esophageal sphincter). Robbins ch 17 (course_sdl_8_9_patho pp. 17–20):
#     transient LES relaxation a major cause of GERD; sliding hiatal hernia spreads the crura.
#   First Aid 2025 p. 369 (layers, Meissner "secretes fluid", Auerbach "motility", slow waves from ICC duodenum > ileum >
#     stomach) · p. 377 (sliding hiatal hernia, GERD) · p. 378 (CCK ↓ gastric emptying; motilin → MMCs, ↑ fasting,
#     erythromycin agonist; VIP relaxes sphincters; NO relaxes the LES) · p. 383 (achalasia: lost NO/VIP myenteric
#     neurons) · p. 391 (Hirschsprung: no Auerbach/Meissner plexuses in the distal colon).
# Source conflicts: vagal afferent share — Costanzo 75%, Guyton 80%, lecture 75–80% (shown as "75–80%"). Gastrocolic
#   reflex efferent limb — Costanzo: CCK and gastrin; Guyton: via the prevertebral ganglia / autonomic nerves; lecture:
#   "long-arc vagovagal reflex" (the note says only "long-arc reflex through the extrinsic nerves"). Where the IPANs sit —
#   lecture: submucosa; Costanzo just "IPANs" (drawn in the submucosa).
# Cut for lack of support or because sources disagree: neuropeptide Y as an excitatory transmitter (Costanzo's text says
#   excitatory, his Table 8.1 says it relaxes); a gastric-emptying arrow for the sympathetic and parasympathetic options
#   (no source gives one) and a pyloric-tone arrow for the pyloric pump (Guyton: the pylorus both tightens as each wave
#   arrives and is inhibited by gastric stretch); a secretion arrow for the sympathetic option (lecture "inhibits",
#   Costanzo only ↑ saliva — left "–"); hunger contractions; colonic segmentation timing.
# m58 pins (P1): option labels now carry the names questions use (keys unchanged) — "Auerbach", "Meissner", "interstitial
#   cells of Cajal" (FA p. 369), "retropulsion · pyloric sphincter" and "enterogastric reflexes" (Guyton ch 64; lecture
#   notes pp. 33–35). " & " does not split label names; " · " does.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import card, full

CZ8, GY63, GY64 = full('Costanzo', 8), full('Guyton', 63), full('Guyton', 64)
PW17, RB17, MO5 = full('Pawlina', 17), full('Robbins', 17), full('Moore', 5)

# ── drawing helpers ──
shapes = []
def add(svg, when=None, unless=None):
    if when is None and unless is None: shapes.append(svg); return
    d = dict(svg) if isinstance(svg, dict) else dict(svg=svg)
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
def X(cx, cy, s=14): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def arrow(d, lane='moExt', dash=False, w=2.5, when=None):
    add(f'<path d="{d}" class="{"dyn-dash" if dash else "dyn-line"}" style="stroke-width:{w}" marker-end="url(#ah-{lane})"/>', when=when)

O = lambda *k: ['r:' + x for x in k]
DEF = ['!r:*']

text('Gut motility — the wall’s own nerves, the stomach, the colon and the nerves from outside', 180, 150, 'dyn-big')
text('big dots = chyme or stool · small dots on the wall = the contraction · coloured dots = transmitters, nerve signals, hormones',
     180, 176, 'dyn-cap')

# ════════ region boxes ════════
box(150, 200, 560, 1080); text('Extrinsic nerves', 172, 236, 'dyn-big')
box(590, 200, 1570, 1080); text('Stomach & duodenum', 612, 236, 'dyn-big')
box(1600, 200, 2340, 1080); text('Colon, rectum & anus', 1622, 236, 'dyn-big')
box(150, 1105, 2340, 1770); text('Small intestine — the wall up close (orad on the left, caudad on the right)', 172, 1141, 'dyn-big')

# ════════ extrinsic nerves: medulla, cord, ganglia ════════
add('<rect x="180" y="280" width="160" height="100" rx="40" class="dyn-cell"/>')
text('Medulla', 260, 322, 'nf-l1', 'middle'); text('NTS · dorsal motor X', 260, 344, 'nf-l2', 'middle')
add('<rect x="200" y="560" width="90" height="320" rx="30" class="dyn-cell"/>')
text('cord T5–L2', 245, 545, 'nf-l1', 'middle'); text('sympathetic', 245, 905, 'nf-l2', 'middle')
GANG = [(620, 'celiac'), (720, 'sup. mesenteric'), (820, 'inf. mesenteric')]
for y, nm in GANG:
    add(f'<path d="M290 {y - 20} L384 {y}" class="dyn-line"/>')
    add(f'<circle cx="400" cy="{y}" r="16" style="fill:var(--dk1);fill-opacity:.25;stroke:var(--dk1);stroke-width:3"/>')
    text(nm, 400, y + 36, 'nf-l2', 'middle')
text('prevertebral ganglia', 400, 575, 'nf-l1', 'middle')
text('→ distal colon', 400, 872, 'nf-l2', 'middle')
VAGUS = 'M340 330 C 600 330 820 290 1060 292 L1088 300 L1088 430'
add(f'<path d="{VAGUS}" style="fill:none;stroke:var(--dk9);stroke-width:5;stroke-linecap:round"/>')
text('vagus (CN X) · 75–80% afferent', 470, 300, 'nf-l1')
add(f'<path d="{VAGUS}" class="dyn-hl"/>', when=O('para', 'recep'))
CEL = 'M416 620 C 640 600 840 640 1010 650'
SMG = 'M416 720 C 540 740 575 900 575 1078'
add(f'<path d="{CEL}" style="fill:none;stroke:var(--dk1);stroke-width:4;stroke-dasharray:10 6"/>')
add(f'<path d="{SMG}" style="fill:none;stroke:var(--dk1);stroke-width:4;stroke-dasharray:10 6"/>')
add(f'<path d="{CEL}" class="dyn-hl"/><path d="{SMG}" class="dyn-hl"/>', when=O('sym'))
add('<rect x="200" y="560" width="90" height="320" rx="30" class="dyn-hl"/>', when=O('sym'))
text('NE', 760, 600, 'nf-l1', 'middle', when=O('sym'))
text('NE → small bowel', 560, 1050, 'nf-l1', 'end', when=O('sym'))

# ════════ stomach & duodenum ════════
add('<path d="M880 330 H1072 M1104 330 H1330" style="stroke:var(--dk5);stroke-width:12;stroke-linecap:round;opacity:.7"/>')
text('diaphragm', 1342, 336, 'nf-l2')
add('<path d="M1088 210 V385" class="nf-wall" style="stroke-width:44"/><path d="M1088 210 V385" class="nf-lumen" style="stroke-width:28"/>')
text('esophagus', 1122, 270, 'nf-l2')
STOM = ('M1072 380 C 1072 520 1062 640 980 700 L822 700 L822 772 C 900 842 1100 902 1250 862 '
        'C 1420 800 1470 600 1420 450 C 1380 300 1180 280 1104 380 Z')
add(f'<path d="{STOM}" style="fill:var(--dk10);fill-opacity:.08;stroke:var(--dk3);stroke-width:7;stroke-linejoin:round"/>')
add('<path d="M1060 640 C 1180 560 1320 520 1450 520" class="dyn-dash" style="opacity:.6"/>')
text('orad', 1300, 410, 'nf-l1', 'middle'); text('fundus · upper body: stores', 1300, 430, 'nf-l2', 'middle')
text('caudad', 1150, 770, 'nf-l1', 'middle'); text('lower body · antrum: grinds, empties', 1150, 790, 'nf-l2', 'middle')
add('<rect x="812" y="694" width="22" height="84" rx="5" style="fill:var(--dk7)"/>')
add('<rect x="806" y="686" width="34" height="100" rx="6" style="fill:var(--dk7)"/>', when=O('eg', 'empt', 'sym'))
text('pylorus', 800, 676, 'nf-l1', 'end')
text('tightens', 800, 658, 'nf-l2 dyn-tag', 'end', when=O('eg', 'empt', 'sym'))
# LES band
add('<rect x="1060" y="342" width="56" height="34" rx="6" style="fill:var(--dk7)"/>', unless=O('recep'))
add('<rect x="1060" y="342" width="12" height="34" rx="4" style="fill:var(--dk7)"/><rect x="1104" y="342" width="12" height="34" rx="4" style="fill:var(--dk7)"/>', when=O('recep'))
text('LES', 1046, 366, 'nf-l1', 'end')
DUO = 'M820 735 H700 Q640 735 640 800 V960 Q640 1030 720 1030 H860'
add(dict(tube=DUO, w=34, color='--dk3'))
text('duodenum', 676, 880, 'nf-l1')
text('to jejunum ›', 872, 1036, 'nf-l2')

# les: the antireflux barrier
add('<path d="M1060 330 C 1040 300 1040 300 1088 286 C 1136 300 1136 300 1116 330" style="fill:none;stroke:var(--dk5);stroke-width:9"/>', when=O('les'))
add('<rect x="1056" y="338" width="64" height="42" rx="8" class="dyn-hl"/>', when=O('les'))
text('LES: ~3 cm of tonic circular muscle', 1040, 300 - 40, 'nf-l1 dyn-tag', 'end', when=O('les'))
text('≈ 30 mm Hg at rest', 1040, 300 - 20, 'nf-l2', 'end', when=O('les'))
text('crura: pinch valve', 1150, 300, 'nf-l1 dyn-tag', when=O('les'))
add('<path d="M1016 412 L1060 402 M1160 412 L1116 402" style="stroke:var(--bad);stroke-width:4" marker-end="url(#ah-moStom)"/>', when=O('les'))
text('abdominal pressure squeezes', 1000, 398, 'nf-l2', 'end', when=O('les'))
text('the 1–2 cm abdominal segment shut', 1000, 414, 'nf-l2', 'end', when=O('les'))
# recep: orad stomach balloons
add('<path d="M1104 380 C 1180 250 1440 240 1490 450 C 1530 620 1440 740 1300 790" style="fill:none;stroke:var(--accent);stroke-width:4;stroke-dasharray:12 8"/>', when=O('recep'))
text('orad stomach relaxes: pressure ↓, volume ↑ (to ~1.5 L)', 1230, 560, 'nf-l1 dyn-tag', 'middle', when=O('recep'))
text('vagovagal reflex · VIP, NO', 700, 400, 'nf-l1 dyn-tag', when=O('recep'))
# pump: antral ring + retropulsion
text('pyloric pump: 50–70 cm H₂O', 1060, 940, 'nf-l1 dyn-tag', 'middle', when=O('pump'))
text('retropulsion grinds solids to < 1 mm', 1290, 706, 'nf-l1 dyn-tag', 'middle', when=O('pump'))
add('<path d="M930 760 Q1050 680 1220 660" class="dyn-line" marker-end="url(#ah-moStom)"/>', when=O('pump'))
# eg: duodenal receptors and the three routes
for y in (850, 920):
    add(f'<circle cx="640" cy="{y}" r="9" style="fill:var(--nf-h)"/>', when=O('eg'))
text('duodenal receptors: acid · fat · osmolality · stretch', 676, 960, 'nf-l2', when=O('eg'))
add('<path d="M660 760 Q 740 720 800 735" class="dyn-dash" marker-end="url(#ah-moStom)"/>', when=O('eg'))
text('1 · myenteric', 676, 795, 'nf-l2', when=O('eg'))
add('<path d="M628 860 C 560 800 470 700 418 630" class="dyn-dash" marker-end="url(#ah-moExt)"/>', when=O('eg'))
text('2 · sympathetic', 455, 688, 'nf-l2', 'end', when=O('eg'))
add('<path d="M628 900 C 540 700 420 480 300 384" class="dyn-dash" marker-end="url(#ah-moExt)"/>', when=O('eg'))
text('3 · vagal: drive withdrawn', 340, 470, 'nf-l2', when=O('eg'))
add(X(960, 800), when=O('eg', 'empt'))
# empt: fat → CCK through the blood
add(dict(vessel='M660 1000 C 760 1060 980 1000 1060 900', w=10, color='--nf-blood', cls='nf-art'), when=O('empt'))
text('fat → I cells → CCK (blood)', 676, 960, 'nf-l2', when=O('empt'))
# mmc
text('fasting: a strong wave every ~90 min', 1150, 500, 'nf-l1 dyn-tag', 'middle', when=O('mmc'))
text('motilin (upper duodenum)', 676, 960, 'nf-l2', when=O('mmc'))
# gc: stomach full → colon
add('<path d="M1460 560 C 1530 520 1580 440 1650 380" class="dyn-dash" style="stroke-width:3" marker-end="url(#ah-moCol)"/>', when=O('gc'))
text('stomach stretched', 1300, 470, 'nf-l1 dyn-tag', 'middle', when=O('gc'))

# ════════ colon, rectum, anus ════════
COLON = 'M1660 330 H2160 V640 Q2160 720 2080 740 Q2000 760 2000 830 V990'
add(dict(tube=COLON, w=46, color='--dk5'))
text('transverse colon', 1800, 292, 'nf-l2', 'middle')
text('descending', 2196, 480, 'nf-l2')
text('sigmoid', 2040, 700, 'nf-l2', 'end')
text('rectum', 1966, 870, 'nf-l1', 'end')
add('<path d="M1880 296 V364" style="stroke:var(--ink-3);stroke-width:3;stroke-dasharray:6 5"/>')
text('vagus ← · → pelvic nerves', 1880, 392, 'nf-l2', 'middle')
add('<rect x="1966" y="930" width="68" height="16" rx="5" style="fill:var(--dk7)"/>', unless=O('def'))
add('<rect x="1966" y="930" width="18" height="16" rx="5" style="fill:var(--dk7)"/><rect x="2016" y="930" width="18" height="16" rx="5" style="fill:var(--dk7)"/>', when=O('def'))
add('<rect x="1952" y="962" width="96" height="18" rx="5" style="fill:var(--dk4)"/>')
text('internal anal sphincter (smooth)', 1940, 944, 'nf-l2', 'end')
text('external anal sphincter (voluntary)', 1940, 978, 'nf-l2', 'end')
add('<rect x="2240" y="770" width="80" height="120" rx="26" class="dyn-cell"/>')
text('S2–S4', 2280, 834, 'nf-l1', 'middle')
add('<path d="M2240 800 C 2150 800 2080 830 2032 850" style="fill:none;stroke:var(--dk9);stroke-width:4"/>')
add('<path d="M2240 870 C 2170 900 2100 950 2050 968" style="fill:none;stroke:var(--dk4);stroke-width:4"/>')
text('pelvic n.', 2140, 792, 'nf-l2', 'middle')
text('pudendal n.', 2160, 940, 'nf-l2')
add('<path d="M2240 800 C 2150 800 2080 830 2032 850" class="dyn-hl"/>', when=O('para', 'def'))
text('mass movements', 1910, 380 + 50, 'nf-l1 dyn-tag', 'middle', when=O('gc'))
text('rectum stretched → contracts; internal sphincter opens', 2300, 1048, 'nf-l1 dyn-tag', 'end', when=O('def'))
add(''.join(f'<circle cx="{2000 + dx}" cy="{850 + dy}" r="13" style="fill:var(--dk10);opacity:.85"/>'
            for dx, dy in ((-8, 0), (10, 20), (-6, 40), (8, 60))), when=O('def'))

# ════════ the small-intestine wall strip ════════
X0, X1 = 520, 2300
TOPL, MYT, CIRT, SUBT, MUCT = (1180, 1205), 1215, (1225, 1275), 1295, 1345
BOTL, MYB, CIRB, SUBB, MUCB = (1595, 1620), 1585, (1525, 1575), 1505, 1455
LUM = 1400
def band(y0, y1, color, op=.35):
    add(f'<rect x="{X0}" y="{y0}" width="{X1 - X0}" height="{y1 - y0}" style="fill:var({color});fill-opacity:{op}"/>')
band(*TOPL, '--dk3', .25); band(*BOTL, '--dk3', .25)
band(*CIRT, '--dk3', .45); band(*CIRB, '--dk3', .45)
band(1280, 1312, '--dk10', .12); band(1490, 1522, '--dk10', .12)
add(f'<path d="M{X0} {MUCT} ' + ' '.join(f'q15 -22 30 0' for _ in range((X1 - X0) // 30)) + '" style="fill:var(--dk11);fill-opacity:.25;stroke:var(--dk11);stroke-width:2"/>')
add(f'<path d="M{X0} {MUCB} ' + ' '.join(f'q15 22 30 0' for _ in range((X1 - X0) // 30)) + '" style="fill:var(--dk11);fill-opacity:.25;stroke:var(--dk11);stroke-width:2"/>')
for y, r in ((MYT, 9), (MYB, 9), (SUBT, 6), (SUBB, 6)):
    add(f'<path d="M{X0} {y} H{X1}" style="stroke:var(--dk9);stroke-width:2.5"/>' +
        ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" style="fill:var(--dk9)"/>' for x in range(X0 + 60, X1, 120)))
add(f'<path d="M{X0} {MYT} H{X1} M{X0} {MYB} H{X1}" class="dyn-hl"/>', when=O('myen', 'per'))
add(f'<path d="M{X0} {SUBT} H{X1} M{X0} {SUBB} H{X1}" class="dyn-hl"/>', when=O('subm'))
for y, lab in ((1197, 'longitudinal muscle'), (1222, 'myenteric (Auerbach) plexus'), (1254, 'circular muscle'),
               (1300, 'submucosal (Meissner) plexus'), (1338, 'mucosa · EC cells'), (1406, 'lumen')):
    text(lab, X0 - 14, y, 'nf-l2', 'end')
# the default bolus + a ring of contraction just behind it
STRIPMOVE = O('per', 'mmc')
add('<path d="M1350 1275 Q1420 1395 1490 1275 M1350 1525 Q1420 1405 1490 1525" style="fill:var(--dk3);fill-opacity:.6;stroke:var(--dk3);stroke-width:4"/>', when=O('per'))
add('<circle cx="1560" cy="1400" r="36" style="fill:var(--dk10);opacity:.9"/>', when=O('per'))
add('<path d="M1640 1345 Q1730 1310 1820 1345 M1640 1455 Q1730 1490 1820 1455" style="fill:none;stroke:var(--accent);stroke-width:4;stroke-dasharray:8 6"/>', when=O('per'))
add('<rect x="1548" y="1336" width="24" height="16" rx="4" style="fill:var(--dk11)"/>', when=O('per'))
add('<circle cx="1560" cy="1300" r="13" style="fill:var(--accent)"/>', when=O('per'))
text('behind: circular contracts, longitudinal relaxes (ACh · substance P)', 1410, 1664, 'nf-l1 dyn-tag', 'middle', when=O('per'))
text('ahead: circular relaxes, longitudinal contracts (VIP · NO · ATP)', 1780, 1700, 'nf-l1 dyn-tag', 'middle', when=O('per'))
text('5-HT from the EC cell fires the IPAN', 1600, 1736, 'nf-l2', 'middle', when=O('per'))
text('stimulated: tone ↑ · stronger, slightly faster contractions · faster peristalsis', 1410, 1680, 'nf-l1 dyn-tag', 'middle', when=O('myen'))
text('inner wall of each segment: secretion · absorption · blood flow · mucosal folds', 1410, 1680, 'nf-l1 dyn-tag', 'middle', when=O('subm'))
text('fasting: the migrating motor complex sweeps the bowel clean', 1410, 1680, 'nf-l1 dyn-tag', 'middle', when=O('mmc'))
text('weaker contractions · sphincters tighten · arterioles constrict', 1410, 1680, 'nf-l1 dyn-tag', 'middle', when=O('sym'))
text('stronger contractions · sphincters relax · more secretion', 1410, 1680, 'nf-l1 dyn-tag', 'middle', when=O('para'))
# a submucosal arteriole
add(dict(vessel=f'M{X0 + 40} 1508 H{X1 - 40}', w=8, color='--nf-blood', cls='nf-art', mods=[dict(when=O('sym'), d=-5), dict(when=O('para'), d=4)]))
# slow waves: ICC stars + a trace
for x in range(X0 + 120, X1, 240):
    add(f'<path d="M{x} {MYT - 12} L{x + 4} {MYT - 3} L{x + 13} {MYT} L{x + 4} {MYT + 3} L{x} {MYT + 12} L{x - 4} {MYT + 3} L{x - 13} {MYT} L{x - 4} {MYT - 3} Z" style="fill:var(--accent)"/>', when=O('slow'))
text('ICC = pacemaker', X0 + 134, MYT - 18, 'nf-l2', when=O('slow'))
def slowtrace():
    pts = []; x = 640
    d = f'M{x} 1730'
    for i in range(6):
        pk = 1652 if i % 2 == 0 else 1692       # every other wave stays below threshold: no spikes, weak contraction
        d += f' C{x + 40} 1730 {x + 50} {pk} {x + 90} {pk} C{x + 130} {pk} {x + 140} 1730 {x + 180} 1730 L{x + 260} 1730'
        if i % 2 == 0: pts.append(x + 90)
        x += 260
    sp = ''.join(f'<path d="M{p - 24} 1652 l6 -26 l6 26 l6 -26 l6 26 l6 -26 l6 26 l6 -26 l6 26" class="dyn-trace" style="stroke:var(--bad)"/>' for p in pts)
    return f'<path d="{d}" class="dyn-trace"/>' + sp + '<path d="M620 1674 H2220" class="dyn-dash"/>'
add(slowtrace(), when=O('slow'))
text('threshold', 2230, 1679, 'nf-l2', when=O('slow'))
text('spikes (Ca²⁺) on a wave that reaches threshold → contraction', 1410, 1750, 'nf-l2', 'middle', when=O('slow'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
EMPTY = 'M1300 560 Q1150 720 950 740 L820 735 H700 Q640 735 640 800 V960 Q640 1030 720 1030 H860'
flows = [
  # stomach: mixing loop, emptying into the duodenum
  dict(d='M1120 600 a160 100 0 1 0 320 0 a160 100 0 1 0 -320 0', len=830, speed=60, r=10, base=dict(food=4), unless=O('mmc'),
       mods=[m(O('gc'), add=dict(food=3)), m(O('para', 'pump'), speed=1.6), m(O('sym'), speed=0.5)]),
  dict(d=EMPTY, len=1130, speed=80, r=9, base=dict(food=4), unless=O('eg', 'mmc'),
       mods=[m(O('empt', 'sym'), add=dict(food=-2), speed=0.45), m(O('pump'), add=dict(food=2), speed=1.4), m(O('para'), speed=1.3)]),
  dict(d='M1300 560 Q1150 720 900 740', len=430, speed=60, r=9, base=dict(food=3), when=O('eg')),
  dict(d='M1150 790 Q1000 800 860 745 Q980 650 1200 640', len=720, speed=170, r=9, base=dict(food=4), when=O('pump')),
  dict(d='M1250 862 Q1100 900 870 790', len=420, speed=140, r=9, base=dict(wave=1), when=O('pump')),
  dict(d='M1060 640 Q1000 700 870 700', len=230, speed=77, r=9, base=dict(wave=1), when=O('pump')),
  dict(d='M1350 420 Q1250 750 900 745 L820 735 H700 Q640 735 640 800 V960 Q640 1030 720 1030 H860', len=1450, speed=200, r=11, base=dict(wave=2), when=O('mmc')),
  dict(d='M660 960 C 700 800 760 760 820 740', len=300, speed=90, r=7, base=dict(mot=3), when=O('mmc')),
  dict(d='M1088 214 V420', len=206, speed=60, r=18, base=dict(food=1), when=O('recep')),
  dict(d='M1300 430 C 1000 250 600 360 345 345', len=1000, speed=220, r=7, base=dict(sig=3), when=O('recep')),
  dict(d=VAGUS, len=800, speed=220, r=7, base=dict(sig=3), when=O('recep')),
  dict(d=VAGUS, len=800, speed=200, r=7, base=dict(ach=4), when=O('para')),
  dict(d='M640 870 C 600 790 520 700 418 632', len=320, speed=160, r=7, base=dict(sig=2), when=O('eg')),
  dict(d='M640 900 C 540 700 420 480 300 384', len=640, speed=200, r=7, base=dict(sig=2), when=O('eg')),
  dict(d='M660 760 Q 740 720 800 735', len=150, speed=80, r=7, base=dict(sig=1), when=O('eg')),
  dict(d='M680 990 C 760 1050 980 1000 1060 900', len=470, speed=120, r=7, base=dict(cck=4), when=O('empt')),
  dict(d='M680 900 V990', len=90, speed=50, r=8, base=dict(fat=2), when=O('empt')),
  dict(d=CEL, len=620, speed=200, r=7, base=dict(ne=3), when=O('sym')),
  dict(d=SMG, len=520, speed=200, r=7, base=dict(ne=3), when=O('sym')),
  dict(d='M1460 560 C 1530 520 1580 440 1650 380', len=270, speed=140, r=7, base=dict(sig=2), when=O('gc')),
  # colon
  dict(d=COLON, len=1150, speed=40, r=11, base=dict(food=3), unless=O('def'),
       mods=[m(O('gc'), add=dict(food=4), speed=4), m(O('para'), speed=1.6), m(O('sym'), speed=0.5)]),
  dict(d='M2000 860 V1060', len=200, speed=60, r=11, base=dict(food=2), when=O('def')),
  dict(d='M2240 800 C 2150 800 2080 830 2032 850', len=230, speed=120, r=7, base=dict(ach=2), when=O('def', 'para')),
  # the small-intestine strip: bolus + contraction ring behind it
  dict(d=f'M700 {LUM} H{X1 - 20}', len=X1 - 720, speed=90, r=26, base=dict(food=1), unless=STRIPMOVE,
       mods=[m(O('para', 'myen'), speed=1.6), m(O('sym'), speed=0.4)]),
  dict(d=f'M560 {CIRT[1] - 6} H{X1 - 170}', len=X1 - 730, speed=90, r=9, base=dict(wave=1), unless=STRIPMOVE,
       mods=[m(O('para', 'myen'), speed=1.6), m(O('sym'), speed=0.4)]),
  dict(d=f'M560 {CIRB[0] + 6} H{X1 - 170}', len=X1 - 730, speed=90, r=9, base=dict(wave=1), unless=STRIPMOVE,
       mods=[m(O('para', 'myen'), speed=1.6), m(O('sym'), speed=0.4)]),
  dict(d=f'M560 {CIRT[1] - 6} H{X1 - 20}', len=X1 - 580, speed=320, r=10, base=dict(wave=2), when=O('mmc')),
  dict(d=f'M560 {CIRB[0] + 6} H{X1 - 20}', len=X1 - 580, speed=320, r=10, base=dict(wave=2), when=O('mmc')),
  dict(d=f'M{X0} {MYT} H{X1}', len=X1 - X0, speed=260, r=7, base=dict(sig=5), when=O('myen')),
  # peristaltic reflex: 5-HT up to the IPAN, ACh/SP behind, VIP/NO ahead
  dict(d='M1560 1338 V1302', len=36, speed=20, r=6, base=dict(ht=2), when=O('per')),
  dict(d='M1560 1300 C 1520 1260 1480 1230 1420 1215', len=170, speed=90, r=6, base=dict(sig=2), when=O('per')),
  dict(d='M1560 1300 C 1610 1260 1660 1230 1730 1215', len=200, speed=90, r=6, base=dict(sig=2), when=O('per')),
  dict(d='M1420 1215 V1270', len=55, speed=30, r=6, base=dict(ach=2), when=O('per')),
  dict(d='M1730 1215 V1270', len=55, speed=30, r=6, base=dict(vip=2), when=O('per')),
  # submucosal: water secreted into the lumen
] + [dict(d=f'M{x} {SUBT} V{LUM - 20}', len=LUM - 20 - SUBT, speed=40, r=6, base=dict(h2o=1), when=O('subm', 'para')) for x in range(700, 2200, 240)]

sites = [
  dict(x=1088, y=360, n=[-1, 0], w=10, t='rec', l='', aria='Lower esophageal sphincter', c='les', ions=[]),
  dict(x=822, y=736, n=[1, 0], w=10, t='rec', l='', aria='Pylorus and gastric emptying', c='gastricmotility', ions=[]),
  dict(x=1560, y=1300, n=[0, -1], w=10, t='rec', l='', aria='Peristaltic reflex', c='entericreflex', ions=[]),
  dict(x=X0 + 60, y=MYT, n=[0, -1], w=10, t='rec', l='', aria='Myenteric and submucosal plexuses', c='gutwall', ions=[]),
]

readouts = [
  dict(l='Gut contractions (force)', mods=[dict(when=O('para', 'myen', 'mmc', 'gc', 'def', 'pump'), d=1),
                                           dict(when=O('sym', 'eg', 'empt'), d=-1)]),
  dict(l='Gastric emptying', mods=[dict(when=O('pump'), d=1), dict(when=O('eg', 'empt'), d=-1)]),
  dict(l='Pyloric sphincter tone', mods=[dict(when=O('eg', 'empt', 'sym'), d=1), dict(when=O('para'), d=-1)]),
  dict(l='Orad stomach pressure', mods=[dict(when=O('recep'), d=-1)]),
  dict(l='Mucosal secretion', mods=[dict(when=O('subm', 'para'), d=1)]),
  dict(l='Gut blood flow', mods=[dict(when=O('sym'), d=-1), dict(when=O('para'), d=1)]),
]

notes = {
  '': 'The gut moves itself. Slow waves from the interstitial cells of Cajal set the rhythm, the enteric nervous system in the '
      'wall runs the reflexes (myenteric plexus for motility, submucosal plexus for secretion), and the vagus, pelvic and '
      'sympathetic nerves turn it up or down. Pick a circuit or a reflex.',
  'r:per': 'Peristaltic reflex: the bolus makes enterochromaffin cells release 5-HT, which fires intrinsic primary afferent '
           'neurons (IPANs). Behind the bolus, excitatory neurons (ACh, substance P) contract the circular muscle as the '
           'longitudinal relaxes; ahead, inhibitory neurons (VIP, NO, ATP) relax it — the two layers are reciprocally '
           'innervated. Without the myenteric plexus there is no peristaltic reflex.',
  'r:myen': 'Myenteric (Auerbach) plexus, between the circular and longitudinal layers, runs the whole length of the gut and '
            'controls motility: stimulated, it raises tone, strengthens and slightly speeds rhythmic contractions and speeds '
            'the peristaltic wave. Its inhibitory neurons relax the sphincters. It is absent in Hirschsprung disease, and its '
            'inhibitory neurons are lost in achalasia.',
  'r:subm': 'Submucosal (Meissner) plexus, in the submucosa, controls the inner wall of each short segment: local secretion '
            '(it secretes fluid), absorption, local blood flow and the folding of the mucosa by the muscularis mucosae. Sensory '
            'signals from the epithelium are integrated here.',
  'r:slow': 'Slow waves are not action potentials: rhythmic depolarizations started by the interstitial cells of Cajal, the '
            'pacemaker, spread to the muscle through gap junctions. Only a wave that reaches threshold fires spikes (Ca²⁺ '
            'entry) and a strong contraction, so the slow-wave rate caps the contraction rate: duodenum 12 > ileum 9 > '
            'stomach 3 per minute. Nerves and hormones change the spikes and force, not the slow-wave rate.',
  'r:les': 'Lower esophageal sphincter: the last ~3 cm of esophageal circular muscle stays tonically closed at about 30 mm Hg, '
           'above both the intrathoracic esophagus and the stomach. The diaphragmatic crura add a pinch valve, and rising '
           'abdominal pressure squeezes the 1–2 cm abdominal segment shut. A sliding hiatal hernia lifts the junction above '
           'the crura; transient LES relaxations are a major cause of GERD.',
  'r:recep': 'Receptive relaxation: as the swallow arrives, the LES and the orad stomach (fundus and upper body) relax together, '
             'so orad pressure falls and the stomach takes up to about 1.5 L without its pressure rising. It is a vagovagal '
             'reflex — afferent and efferent limbs both in the vagus, transmitters VIP and NO — so vagotomy abolishes it.',
  'r:pump': 'Mixing waves start in the mid-stomach every 15–20 s and strengthen toward the antrum. The ring closes the pylorus '
            'as it arrives, so most chyme squirts back toward the body (retropulsion) and solids are ground below 1 mm. About '
            '20% of the time the waves become the pyloric pump (50–70 cm H₂O), which empties a few milliliters at a time; '
            'liquids leave faster than solids.',
  'r:eg': 'Enterogastric reflexes: distension, irritation, acid (pH below about 3.5–4), abnormal osmolality or protein and fat '
          'products in the duodenum slow the stomach within about 30 s — through the myenteric plexus, through sympathetics via '
          'the prevertebral ganglia, and through the vagus (its excitatory drive is withdrawn). They inhibit the pyloric pump '
          'and tighten the pylorus, so gastric emptying slows.',
  'r:empt': 'Fat in the duodenum releases CCK from I cells; carried in the blood, it slows antral contractions and tightens the '
            'pylorus, so gastric emptying slows while bile and pancreatic enzymes digest the fat — CCK is the strongest '
            'hormonal brake. Acid slows emptying through enteric reflexes instead. Isotonic liquids empty fastest.',
  'r:mmc': 'Migrating motor complex: during fasting, motilin from the upper duodenum sets off strong contractions about every '
           '90 minutes that sweep residual chyme out of the stomach and small intestine. Eating stops motilin secretion. '
           'Erythromycin, a motilin agonist, is used to stimulate the gut.',
  'r:gc': 'Gastrocolic reflex: a meal stretching the stomach increases colonic motility and the mass movements (1–3 a day) that '
          'push stool toward the rectum — the urge to defecate soon after eating. It is a long-arc reflex through the '
          'extrinsic nerves: it barely works when the colon’s autonomic nerves are cut.',
  'r:def': 'Defecation reflex: stool entering the rectum stretches it; a weak intrinsic myenteric reflex starts peristalsis and '
           'relaxes the internal anal sphincter, and the sacral parasympathetic reflex (pelvic nerves, S2–S4) makes it '
           'powerful. The external anal sphincter is striated and voluntary (pudendal nerve), so defecation waits until it '
           'relaxes; a Valsalva adds abdominal pressure.',
  'r:para': 'Parasympathetic: the vagus (esophagus to the proximal transverse colon) and the pelvic nerves (S2–S4, the rest of '
            'the colon to the anal canal) send long preganglionic fibers to the plexuses in the gut wall. ACh and peptides '
            'excite the enteric nervous system: stronger contractions, relaxed sphincters, more secretion and, with it, more '
            'local blood flow.',
  'r:sym': 'Sympathetic: short preganglionic fibers from T5–L2 synapse outside the gut, in the celiac and mesenteric ganglia; '
           'postganglionic fibers release norepinephrine, which mainly inhibits the enteric neurons — weaker contractions, '
           'contracted sphincters — and constricts the arterioles, so gut blood flow falls (shunted away in exercise and shock).',
}

dyn = dict(
  kinds=dict(food=['food', '--dk10'], fat=['food', '--dk10'], h2o=['h2o', '--nf-h2o'], wave=['wave', '--dk3'],
             sig=['sig', '--dk9'], ach=['ach', '--dk4'], vip=['vip', '--dk6'], ht=['ht', '--dk11'], ne=['ne', '--dk1'],
             cck=['horm', '--dk8'], mot=['horm', '--dk8']),
  groups=[['food', 'Chyme · stool'], ['h2o', 'Water'], ['wave', 'Contraction'], ['sig', 'Nerve signals'],
          ['ach', 'ACh · substance P'], ['vip', 'VIP · NO · ATP'], ['ht', '5-HT'], ['ne', 'Norepinephrine'],
          ['horm', 'Hormones (CCK, motilin)']],
  switches=[dict(id='r', label='Pick a circuit or a reflex', type='one', options=[
      ['per', 'Peristaltic reflex', 'entericreflex'], ['myen', 'Myenteric plexus · Auerbach plexus', 'gutwall'],
      ['subm', 'Submucosal plexus · Meissner plexus', 'gutwall'], ['slow', 'Slow waves (ICC) · interstitial cells of Cajal', 'gutwall'],
      ['les', 'Lower esophageal sphincter', 'les'], ['recep', 'Receptive relaxation', 'vip'],
      ['pump', 'Pyloric pump · retropulsion · pyloric sphincter', 'gastricmotility'], ['eg', 'Enterogastric reflexes', 'gastricmotility'],
      ['empt', 'Gastric emptying — fat & CCK', 'cck'],
      ['mmc', 'Migrating motor complex', 'motilin'], ['gc', 'Gastrocolic reflex', 'entericreflex'],
      ['def', 'Defecation reflex', 'entericreflex'],
      ['para', 'Parasympathetic (ACh) — speeds the gut'], ['sym', 'Sympathetic (NE) — slows the gut']],
      sections=[['The wall’s own nerves', ['per', 'myen', 'subm', 'slow']],
                ['Stomach', ['les', 'recep', 'pump', 'eg', 'empt']],
                ['Fasting & colon', ['mmc', 'gc', 'def']],
                ['Extrinsic nerves', ['para', 'sym']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='GI Exam 1 lecture notes · Costanzo ch 8 · Guyton ch 63–64 · Pawlina ch 17 · Robbins ch 17 · First Aid pp. 369, 377, 378, 383, 391')

# ════════ the three new cards ════════
card('entericreflex', 'Enteric reflexes — the peristaltic reflex, transmitters & vagal afferents', 'reg', 'moWall',
     'Stretch → 5-HT → IPANs → contract behind, relax ahead', 1,
     'A bolus stretches the wall and makes <b>enterochromaffin cells</b> release <b>5-HT</b>, which fires <b>intrinsic primary '
     'afferent neurons (IPANs)</b>. The myenteric plexus then contracts the segment behind the bolus and relaxes the segment '
     'ahead of it — the <b>peristaltic (myenteric) reflex</b>, which does not occur without the myenteric plexus.',
     ['Excitatory motor neurons: <b>ACh, substance P</b> (also glutamate) — contract the muscle behind the bolus',
      'Inhibitory motor neurons: <b>VIP, nitric oxide, ATP</b> — relax the muscle ahead of the bolus and the sphincters (pyloric, ileocecal)',
      'Circular and longitudinal muscle are <b>reciprocally innervated</b>: behind the bolus the circular layer contracts while the longitudinal relaxes; ahead, the reverse',
      'Vagus: about 75–80% afferent; mechano- and chemoreceptor signals reach the NTS and return as <b>vagovagal reflexes</b>. Vagal territory runs to the proximal transverse colon; pelvic nerves (S2–S4) supply the rest to the anal canal',
      '<b>Gastrocolic reflex</b>: a stretched stomach → ↑ colonic motility and mass movements. <b>Defecation reflex</b>: rectal stretch → weak myenteric reflex, made strong by the sacral parasympathetic (pelvic nerve) reflex',
      'Sympathetic norepinephrine (T5–L2 via the prevertebral ganglia) mainly inhibits the enteric neurons → less motility, tighter sphincters'],
     ['—'],
     ['ACh and substance P behind the bolus; VIP, NO and ATP ahead of it'],
     [CZ8, GY63, GY64],
     ['—'],
     ['peristaltic reflex', 'enterochromaffin cells', 'intrinsic primary afferent', 'gastrocolic reflex', 'vagovagal',
      'excitatory enteric', 'inhibitory enteric', 'vagal territory', 'reciprocally innervated', 'vagal fibers', 'defecation reflex'],
     fa='369')

card('gastricmotility', 'Gastric motility & emptying — retropulsion, pyloric pump & enterogastric reflexes', 'reg', 'moStom',
     'Mixing waves grind; the pyloric pump empties; the duodenum brakes', 1,
     'Weak <b>mixing waves</b> start in the mid-stomach every 15–20 s and strengthen toward the antrum. The ring closes the '
     'pylorus as it arrives, so most antral contents squirt back toward the body (<b>retropulsion</b>) and solids are ground '
     'down. About 20% of the time the waves become the strong <b>pyloric pump</b> that empties chyme.',
     ['Pyloric sphincter: circular muscle 50–100% thicker than the antrum and tonically contracted — lets fluids through, holds solids until they are fluid chyme',
      'Pyloric pump contractions reach 50–70 cm H₂O, about six times the mixing waves; caudad slow waves 3–5 per minute',
      'Solids must be 1 mm or less to pass (Costanzo); liquids empty faster than solids, isotonic faster than hypo- or hypertonic',
      '<b>Enterogastric reflexes</b>: duodenal distension, irritation, acid (pH below 3.5–4), osmolality, protein and fat products → inhibit the pump and ↑ pyloric tone within about 30 s',
      'Three routes: the myenteric plexus, sympathetics via the prevertebral ganglia, the vagus to the brainstem',
      'Hormonal brake: <b>CCK</b> (fat) is the strongest; secretin and GIP are weaker'],
     ['—'],
     ['Fat and acid in the duodenum slow the stomach'],
     [GY64, CZ8],
     ['—'],
     ['gastric emptying', 'pyloric pump', 'retropulsion', 'antral retropulsion', 'enterogastric reflex', 'pyloric sphincter',
      'mixing waves'],
     fa='378')

card('les', 'Lower esophageal sphincter — tone & the antireflux barrier', 'reg', 'moStom',
     'Tonic circular muscle, ~3 cm, ~30 mm Hg', 1,
     'The LES is circular smooth muscle at the lower end of the esophagus that stays <b>tonically contracted</b>, so its '
     'pressure sits above both the intrathoracic esophagus and the stomach and acid stays down. It relaxes ahead of a '
     'swallow (VIP and NO from vagal peptidergic fibers), together with receptive relaxation of the orad stomach.',
     ['Extends about 3 cm above the gastroesophageal junction; resting pressure about 30 mm Hg',
      '<b>Diaphragmatic crura</b> surround it at the hiatus and add a pinch valve during inspiration, coughing and straining',
      'A 1–2 cm segment lies in the abdomen: rising intra-abdominal pressure squeezes it shut (flap-valve closure)',
      '<b>Sliding hiatal hernia</b> spreads the crura and lifts the junction into the thorax → LES incompetence; <b>transient LES relaxations</b> are a major cause of GERD',
      'The opposite failure is achalasia: inhibitory (NO, VIP) neurons are lost and the LES cannot relax'],
     ['Manometry: a zone of pressure higher than the esophagus and the stomach'],
     ['Tonic LES plus crura plus the abdominal segment keep acid down'],
     [GY64, CZ8, PW17, MO5, RB17],
     ['—'],
     ['lower esophageal sphincter', 'diaphragmatic crura', 'resting les', 'antireflux barrier'],
     fa='377, 378, 383')

MAP = dict(
  id='motilsim', title='Gut Motility & Enteric Reflexes in Motion', topic='gi', after='gut',
  sub='Watch a bolus ride the peristaltic reflex along the gut wall, then pick a circuit or a reflex — the two plexuses, '
      'slow waves, the LES, receptive relaxation, the pyloric pump, enterogastric reflexes and CCK, the migrating motor '
      'complex, the gastrocolic and defecation reflexes, and parasympathetic vs sympathetic drive. Tap a pin for its card',
  w=3500, h=2150,
  fa='369, 377, 378, 383, 391', src=[CZ8, GY63, GY64, PW17, MO5, RB17],
  lanes=[('moWall', 'Enteric nervous system', 'glycolysis'), ('moStom', 'Stomach & sphincters', 'tca'),
         ('moCol', 'Fasting & colon', 'gluconeo'), ('moExt', 'Extrinsic nerves', 'ppp'), ('moDz', 'When it fails', 'glycogen')],
  nodes=[
    ('mo1', 'Gut wall & plexuses', 330, 1830, 'moWall', 'Auerbach motility · Meissner secretion', ['gutwall'], 'hub'),
    ('mo2', 'Enteric reflexes', 760, 1830, 'moWall', '5-HT · IPANs · ACh vs VIP/NO', ['entericreflex'], 'hub'),
    ('mo3', 'Gastric motility', 1200, 1830, 'moStom', 'retropulsion · pyloric pump', ['gastricmotility']),
    ('mo4', 'Lower esophageal sphincter', 1640, 1830, 'moStom', '30 mm Hg · crura', ['les']),
    ('mo5', 'Swallowing', 2080, 1830, 'moStom', 'primary · secondary peristalsis', ['swallowing']),
    ('mo6', 'VIP · nitric oxide', 330, 1950, 'moStom', 'relaxes sphincters', ['vip']),
    ('mo7', 'CCK', 760, 1950, 'moStom', 'fat slows emptying', ['cck']),
    ('mo8', 'Motilin · MMC', 1200, 1950, 'moCol', 'fasting sweeps · erythromycin', ['motilin']),
    ('mo9', 'Autonomic wiring', 1640, 1950, 'moExt', 'ACh · NE', ['ansreg']),
    ('mo10', 'Solitary nucleus', 2080, 1950, 'moExt', 'vagal afferents land here', ['nts']),
    ('mo11', 'Visceral afferents', 330, 2070, 'moExt', 'stretch · chemoreceptors', ['viscafferent']),
    ('mo12', 'Ganglion inhibition (OMT)', 760, 2070, 'moExt', 'celiac · SMG · IMG', ['ganglioninh']),
    ('mo13', 'Hirschsprung disease', 1200, 2070, 'moDz', 'no plexuses distally', ['hirschsprung']),
    ('mo14', 'Achalasia', 1640, 2070, 'moDz', 'lost NO/VIP neurons', ['achalasia']),
    ('mo15', 'GERD', 2080, 2070, 'moDz', 'transient LES relaxations', ['gerd']),
  ],
  panels=[
    (2420, 900, 1000, 'Transmitters in the gut wall (lecture notes · Costanzo ch 8 · Guyton ch 63)', [
      ('Excitatory enteric', 'ACh · substance P — contract'),
      ('Inhibitory enteric', 'VIP · nitric oxide · ATP — relax muscle and sphincters'),
      ('Parasympathetic (ACh)', 'wall contracts · sphincters relax'),
      ('Sympathetic (NE)', 'wall relaxes · sphincters contract · vessels constrict')]),
    (2420, 1130, 1000, 'Slow waves set the top rate (First Aid p. 369 · Costanzo ch 8)', [
      ('Duodenum', '12 per minute'), ('Ileum', '9 per minute'), ('Stomach', '3 per minute (caudad 3–5)'),
      ('Pacemaker', 'interstitial cells of Cajal')]),
  ],
  dyn=dyn,
)
