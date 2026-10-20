# m55 — Testicular Axis Lab Simulator (dynamic map, kit data)
# The hypothalamic–pituitary–testicular axis drawn for READING LAB PATTERNS (sexsim covers sex differentiation, gonadsim the
# tumors, mensflow the female cycle): GnRH neuron (pulses, with a trace of what reaches the pituitary) → portal veins →
# gonadotroph (LH + FSH) → testis: the Leydig cell (LH → testosterone, 17α-hydroxylase/17,20-lyase) and a seminiferous tubule
# with its Sertoli cell (FSH → spermatogenesis, ABP, inhibin B) → testosterone up a trunk to the hypothalamus and pituitary
# (⊣ GnRH, ⊣ LH) and out to the tissues: a target cell (5α-reductase → DHT → androgen receptor) and adipose/liver (aromatase →
# estradiol); inhibin B back to the pituitary (⊣ FSH); sperm out to the epididymis. One `one` switch picks a pattern, grouped in
# `sections` (primary testicular · central · drugs & hormones · receptor & enzyme), and reads out LH, FSH, testosterone,
# inhibin B, estradiol, DHT and sperm count.
#
# Sources (all read in the corpus; U+00A0/U+00AD normalized):
#   First Aid 2025 p. 332 (GnRH ↑ FSH, LH; suppressed by hyperprolactinemia; tonic analog (leuprolide) suppresses the axis,
#     pulsatile → puberty, fertility; prolactinoma → hypogonadism) · p. 334 (prolactin inhibits spermatogenesis by inhibiting
#     GnRH; men: gynecomastia, infertility, ↓ libido, impotence; dopamine agonists treat prolactinoma; antipsychotics raise it)
#     · p. 645 (erection parasympathetic S2–S4, NO → cGMP; emission sympathetic T11–L2; expulsion pudendal; PDE-5 inhibitors)
#     · p. 646 (Sertoli: inhibin B ⊣ FSH, ABP keeps local testosterone, aromatase, temperature sensitive — ↓ sperm and
#     ↓ inhibin B with ↑ temperature, varicocele and cryptorchidism; Leydig: testosterone with LH, unaffected by temperature)
#     · p. 653 (DHT > testosterone potency; testosterone vs DHT functions; 5α-reductase inhibited by finasteride; aromatase
#     primarily in adipose and testes; anabolic steroids → axis inhibition → ↓ intratesticular testosterone, small testes,
#     ↓ sperm count/azoospermia, acne, gynecomastia, erythrocytosis) · p. 654 (1° vs 2° hypogonadism causes; Leydig cell tumor
#     in peripheral precocious puberty) · p. 655 (Klinefelter: ↓ inhibin B → ↑ FSH; ↓ testosterone → ↑ LH; small firm testes,
#     azoospermia, gynecomastia) · p. 656 (testosterone/LH table: ↑↑ AIS, ↑↓ tumor or exogenous androgenic steroids, ↓↑ 1°,
#     ↓↓ 2°; AIS ↑ testosterone, estrogen, LH; 5α-reductase deficiency: testosterone/estrogen normal, LH "normal or ↑";
#     Kallmann ↓ GnRH, FSH, LH, testosterone, low sperm count) · p. 667 (gynecomastia causes incl. Klinefelter, spironolactone)
#     · p. 669 (cryptorchidism ↓ inhibin B, ↑ FSH, ↑ LH, testosterone ↓ in bilateral / normal in unilateral; varicocele left
#     side, left gonadal → left renal vein, infertility from ↑ temperature, bag of worms) · p. 674 (GnRH analogs: continuous →
#     transient flare then down-regulated receptor → ↓ FSH, ↓ LH, ↓ testosterone; degarelix no flare) · p. 676 (finasteride,
#     flutamide/bicalutamide, ketoconazole 17α-hydroxylase/17,20-lyase, spironolactone AR + 17α-hydroxylase; testosterone).
#   Costanzo ch 10 (GnRH decapeptide, arcuate nuclei, portal blood; continuous GnRH down-regulates receptors (prostate cancer);
#     FSH → Sertoli, LH → Leydig; testosterone ⊣ GnRH and LH, lowers GnRH pulse frequency and amplitude; inhibin ⊣ FSH; ↓ T
#     (testes removed) → ↑ frequency and amplitude of GnRH, FSH, LH pulses; GnRH deficiency + pulsatile analog → puberty and
#     reproductive function, long-acting analog → none; 98% of testosterone bound, only free acts; testosterone vs DHT table;
#     AIS case: mildly ↑ testosterone, ↑ LH, testes make estradiol driven by high LH; 5α-reductase case: high-normal
#     testosterone, low DHT; finasteride for BPH and hair loss).
#   Guyton ch 81 (pulsatile GnRH every 1–3 h, continuous → receptor down-regulation; tubules fail → FSH ↑ markedly; inhibin;
#     heat stops spermatogenesis; cryptorchid testis forms no sperm; Leydig cell tumors up to 100× testosterone; estrogen in the
#     male mostly from liver and other tissues; Klinefelter commonest primary hypogonadism).
#   Katzung ch 40 (exogenous androgens suppress gonadotropins → atrophy; supraphysiologic doses → azoospermia, small testes;
#     GnRH analogs suppress when continuous; ketoconazole inhibits gonadal steroid synthesis, ↑ estradiol:testosterone ratio,
#     gynecomastia; finasteride ↓ DHT; flutamide competitive AR antagonist, gynecomastia; spironolactone competes at the AR
#     and lowers testosterone; aromatase in adipose tissue, liver, hypothalamus; ~2% of testosterone free).
#   Bootcamp.com (comment only, not in src): Reproduction — Fetal development: Klinefelter labs ↑ LH, ↑ FSH, ↑ estradiol,
#     ↓ testosterone (the only source for Klinefelter estradiol ↑); Reproduction — Male pathology: cryptorchidism labs as FA;
#     Endocrinology — Anterior and posterior pituitary: hyperprolactinemia ↓ GnRH → ↓ FSH, ↓ LH → ↓ testosterone,
#     ↓ spermatogenesis in males.
# Arrows deliberately left "–" (no source gives a direction): 5α-reductase deficiency LH ("normal or ↑", FA 656);
#   varicocele LH/FSH (no source prints them); tumor/exogenous FSH except where Katzung's "gonadotropins" covers exogenous
#   androgens; estradiol in exogenous androgens, cryptorchidism, ketoconazole (ratio only); testosterone with finasteride;
#   every arrow for flutamide (no source gives labs); inhibin B outside Klinefelter, cryptorchidism and varicocele.
# Cut for lack of support: aging (Costanzo: gonadotropins rise in senescence; Katzung: most older men with low testosterone
#   have low or inappropriately normal LH — the sources disagree, no clean pattern); obesity / aromatase excess (no source
#   gives a male lab pattern); Sertoli-cell-only syndrome (not in FA or the textbooks read); hCG-secreting tumors (gonadsim's
#   scope); erection / PDE5 as a switch (kept as a sourced panel instead).
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

CZ10, GY81, KZ40 = full('Costanzo', 10), full('Guyton', 81), full('Katzung', 40)
SRC = [CZ10, GY81, KZ40]

O = lambda *k: ['hpg:' + x for x in k]
T_LOW = O('klin', 'crypt', 'kall', 'prl', 'gnrhc', 'keto', 'spiro')     # serum testosterone low
T_HIGH = O('aas', 'tumor', 'ais')                                        # serum testosterone high
GN_HIGH = O('klin', 'crypt', 'ais')                                      # LH (and FSH) high
GN_LOW = O('kall', 'prl', 'gnrhc', 'aas', 'tumor')                       # LH low
FSH_HIGH = O('klin', 'crypt')
FSH_LOW = O('kall', 'prl', 'gnrhc', 'aas')
INH_LOW = O('klin', 'crypt', 'varico')
SPERM_LOW = O('klin', 'crypt', 'varico', 'kall', 'prl', 'aas')

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
def rrect(x0, y0, x1, y1, r):
    return (f'M{x0 + r} {y0} H{x1 - r} Q{x1} {y0} {x1} {y0 + r} V{y1 - r} Q{x1} {y1} {x1 - r} {y1} '
            f'H{x0 + r} Q{x0} {y1} {x0} {y1 - r} V{y0 + r} Q{x0} {y0} {x0 + r} {y0} Z')
TAG = 'nf-l2 dyn-tag'

# ════════ 1. hypothalamus: the GnRH neuron and a trace of the GnRH that reaches the pituitary ════════
add('<rect class="dyn-soft" x="540" y="120" width="760" height="340" rx="40"/>')
text('Hypothalamus', 570, 165, 'dyn-big')
text('arcuate nucleus', 570, 185, 'dyn-cap')
add('<path d="M900 350 V468" class="dyn-line" stroke-width="7"/><circle cx="900" cy="470" r="11" class="dyn-cell"/>')
add(f'<path d="{rrect(790, 230, 1010, 350, 30)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(790, 230, 1010, 350, 30), w=18))
text('GnRH neuron', 900, 286, 'nf-l1', 'middle')
text('GnRH: a decapeptide', 900, 304, 'nf-l2', 'middle')
add(f'<path d="{rrect(790, 230, 1010, 350, 30)}" class="dyn-dim" fill="var(--surface)"/>', when=O('kall', 'gnrhp'))
add('<path d="M820 250 L980 330 M980 250 L820 330" class="dyn-lesion"/>', when=O('kall', 'gnrhp'))
text('GnRH ↑ — testosterone feedback lost', 880, 410, TAG, 'end', when=O('klin', 'crypt'))
text('neurons never arrived · no sense of smell', 880, 410, TAG, 'end', when=O('kall', 'gnrhp'))
text('prolactin ⊣ GnRH', 880, 410, TAG, 'end', when=O('prl'))
text('pulses slower and smaller', 880, 410, TAG, 'end', when=O('aas', 'tumor'))
text('GnRH reaching the pituitary', 1040, 354, 'nf-l2')
def pulses(xs, top):
    return 'M1040 440 ' + ''.join(f'H{x - 9} L{x} {top} L{x + 9} 440 ' for x in xs) + 'H1270'
TR_BIG, TR_SMALL, TR_OFF = O('klin', 'crypt'), O('aas', 'tumor', 'prl'), O('kall', 'gnrhc')
add(f'<path d="{pulses((1075, 1135, 1195, 1250), 392)}" class="dyn-trace"/>', unless=TR_BIG + TR_SMALL + TR_OFF)
add(f'<path d="{pulses((1062, 1102, 1142, 1182, 1222, 1258), 372)}" class="dyn-trace"/>', when=TR_BIG)
add(f'<path d="{pulses((1100, 1210), 418)}" class="dyn-trace"/>', when=TR_SMALL)
add('<path d="M1040 440 H1270" class="dyn-trace"/>', when=O('kall'))
add('<path d="M1040 440 L1050 372 L1062 392 H1270" class="dyn-trace"/>', when=O('gnrhc'))

# GnRH pump (pulsatile GnRH for Kallmann · continuous leuprolide)
add('<rect x="600" y="540" width="180" height="50" rx="16" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M780 565 H886" class="dyn-dash"/>', when=O('gnrhp', 'gnrhc'))
text('GnRH pump — pulses', 690, 570, 'nf-l1', 'middle', when=O('gnrhp'))
text('leuprolide — continuous', 690, 570, 'nf-l1', 'middle', when=O('gnrhc'))

# ════════ 2. portal veins and the anterior pituitary ════════
shapes.append(dict(vessel='M900 482 V676', w=20))
text('Hypophyseal portal veins', 920, 520, 'nf-l2')
add('<ellipse class="dyn-soft" cx="900" cy="840" rx="340" ry="165"/>')
text('Anterior pituitary', 645, 735, 'dyn-big')
add(f'<path d="{rrect(780, 760, 1020, 920, 34)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(780, 760, 1020, 920, 34), w=18))
text('Gonadotroph', 900, 832, 'nf-l1', 'middle')
text('makes LH and FSH', 900, 852, 'nf-l2', 'middle')
# lactotroph adenoma (hyperprolactinemia)
add('<ellipse cx="660" cy="880" rx="55" ry="40" class="dyn-cell" style="stroke:var(--dk12)"/>'
    '<ellipse cx="660" cy="880" rx="68" ry="53" class="dyn-lesion"/>', when=O('prl'))
add('<path d="M605 880 H560 V300 H776" class="dyn-dash" style="stroke:var(--dk12)"/>', when=O('prl'))
text('lactotroph adenoma', 660, 960, 'nf-l1', 'middle', when=O('prl'))
text('LH and FSH ↑ — no brake', 880, 1040, TAG, 'end', when=O('klin', 'crypt'))
text('LH ↑ — testosterone can’t act', 880, 1040, TAG, 'end', when=O('ais'))
text('no GnRH — LH and FSH ↓', 880, 1040, TAG, 'end', when=O('kall'))
text('LH and FSH ↓', 880, 1040, TAG, 'end', when=O('prl'))
text('receptors down-regulated — LH, FSH ↓', 880, 1040, TAG, 'end', when=O('gnrhc'))
text('pulses restore LH and FSH', 880, 1040, TAG, 'end', when=O('gnrhp'))
text('LH and FSH ↓ — suppressed', 880, 1040, TAG, 'end', when=O('aas'))
text('LH ↓ — suppressed by the tumor’s testosterone', 880, 1040, TAG, 'end', when=O('tumor'))

# ════════ 3. LH and FSH down to the testis ════════
shapes.append(dict(vessel='M900 936 V1080 H700 V1310', w=18, mods=[dict(when=GN_HIGH, d=8), dict(when=GN_LOW, d=-8)]))
shapes.append(dict(vessel='M900 1080 H1030 V1236', w=18, mods=[dict(when=FSH_HIGH, d=8), dict(when=FSH_LOW, d=-8)]))
text('LH', 682, 1160, 'nf-l1', 'end')
text('FSH', 1012, 1140, 'nf-l1', 'end')

# ════════ 4. the testis: Leydig cell in the interstitium, a seminiferous tubule with its Sertoli cell ════════
add('<path d="M900 1160 C1110 1160 1280 1270 1280 1420 C1280 1570 1110 1680 900 1680 C690 1680 520 1570 520 1420 '
    'C520 1270 690 1160 900 1160 Z" class="dyn-cell" style="stroke:var(--dk6)"/>')
text('Testis', 545, 1150, 'dyn-big')
# varicocele: dilated pampiniform veins above the testis
add(''.join(f'<path d="M{x} 1095 C{x - 18} 1115 {x + 18} 1130 {x} 1150" class="dyn-line" style="stroke:var(--dk10);stroke-width:7"/>'
            for x in (1150, 1185, 1220, 1255)), when=O('varico'))
text('dilated pampiniform plexus', 1150, 1080, 'nf-l1', when=O('varico'))
# Leydig cell (and a Leydig cell tumor)
add(f'<path d="{rrect(610, 1325, 790, 1455, 28)}" class="dyn-cell" style="stroke:var(--dk5)"/>')
text('Leydig cell', 700, 1385, 'nf-l1', 'middle')
text('in the interstitium', 700, 1403, 'nf-l2', 'middle')
add(f'<path d="{rrect(592, 1310, 808, 1470, 40)}" class="dyn-lesion"/>', when=O('tumor'))
add('<path d="M640 1350 L760 1430 M760 1350 L640 1430" class="dyn-lesion"/>', when=O('keto', 'spiro'))
# seminiferous tubule: wall of germ cells, lumen, the Sertoli cell
add('<circle cx="1080" cy="1420" r="175" class="dyn-soft"/>')
add('<circle cx="1080" cy="1420" r="50" class="dyn-cell"/>')
import math
def _germ():
    out = []
    for r, sz, a0 in ((150, 10, 0.0), (112, 8, 0.2), (80, 6, 0.1)):
        for i in range(16):
            a = a0 + i * 2 * math.pi / 16
            x, y = 1080 + r * math.cos(a), 1420 + r * math.sin(a)
            if abs(x - 1080) < 85 and y < 1395: continue      # the Sertoli cell sits here
            if abs(x - 1080) < 30 and y > 1440: continue      # the sperm exit
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{sz}" fill="var(--dk3)" opacity=".55"/>')
    return ''.join(out)
GERM = _germ()
add(GERM, unless=O('klin'))
add('<circle cx="1080" cy="1420" r="175" fill="var(--surface)" opacity=".7"/>', when=O('klin'))
add('<path d="M1012 1262 Q1080 1240 1148 1262 L1112 1372 Q1080 1384 1048 1372 Z" class="dyn-cell" style="stroke:var(--dk9)"/>')
text('Sertoli', 1080, 1310, 'nf-l1', 'middle')
text('ABP', 1080, 1328, 'nf-l2', 'middle')
text('lumen', 1080, 1425, 'dyn-cap', 'middle')
text('Seminiferous tubule', 1060, 1628, 'nf-l2', 'end')
text('local testosterone', 798, 1372, 'nf-l2')

# ════════ 5. testosterone: the trunk up to both feedback sites and out to the tissues; inhibin B back to the pituitary ════════
TW = [dict(when=T_LOW, d=-8), dict(when=T_HIGH, d=8)]
shapes.append(dict(vessel='M700 1470 V1775 H1450 V290 H1028', w=22, color='--dk5', mods=TW))
shapes.append(dict(vessel='M1450 800 H1038', w=14, color='--dk5', mods=TW))
shapes.append(dict(vessel='M1450 1130 H1745', w=14, color='--dk5', mods=TW))
shapes.append(dict(vessel='M1450 1490 H1745', w=14, color='--dk5', mods=TW))
shapes.append(dict(vessel='M1130 1236 V1130 H1340 V890 H1038', w=14, color='--dk2',
                   mods=[dict(when=INH_LOW, d=-7)]))
text('testosterone in the blood', 1468, 680, 'nf-l2')
text('98% bound (SHBG, albumin)', 1468, 698, 'dyn-cap')
text('inhibin B', 1358, 1030, 'nf-l2')
text('sperm → epididymis', 1300, 1725, 'nf-l2')
# exogenous testosterone
add('<rect x="1520" y="1688" width="170" height="28" rx="10" class="dyn-cell" style="stroke:var(--dk8)"/>'
    '<path d="M1690 1702 H1720 M1520 1702 H1458" class="dyn-line" style="stroke:var(--dk8)"/>', when=O('aas'))
text('testosterone or anabolic steroid', 1520, 1672, 'nf-l1', when=O('aas'))

# testis tags (under the trunk)
text('Klinefelter: dysgenetic tubules (inhibin B ↓) and failing Leydig cells (testosterone ↓) — small, firm testes', 545, 1815, TAG, when=O('klin'))
text('both testes undescended: heat stops sperm and inhibin B; with both affected testosterone falls too', 545, 1815, TAG, when=O('crypt'))
text('the warm testis: Sertoli cells make fewer sperm and less inhibin B; heat-resistant Leydig cells carry on', 545, 1815, TAG, when=O('varico'))
text('Leydig cell tumor — makes testosterone on its own', 545, 1815, TAG, when=O('tumor'))
text('no LH or FSH drive — testosterone and sperm fall', 545, 1815, TAG, when=O('kall', 'prl', 'gnrhc'))
text('intratesticular testosterone ↓ — small testes, azoospermia', 545, 1815, TAG, when=O('aas'))
text('steroid synthesis blocked at 17α-hydroxylase / 17,20-lyase', 545, 1815, TAG, when=O('keto', 'spiro'))
text('testes driven by the high LH make more testosterone and estradiol', 545, 1815, TAG, when=O('ais'))

# ════════ 6. the tissues: a DHT target cell; adipose tissue and liver (aromatase) ════════
add('<rect class="dyn-soft" x="1520" y="960" width="810" height="340" rx="26"/>')
text('Target cell', 1545, 1000, 'dyn-big')
text('prostate, skin, hair follicle — muscle uses testosterone itself', 1545, 1020, 'dyn-cap')
add(f'<path d="{rrect(1600, 1060, 2310, 1260, 30)}" class="dyn-cell"/>')
shapes.append(dict(membrane=rrect(1600, 1060, 2310, 1260, 30), w=16))
add('<ellipse cx="2210" cy="1150" rx="70" ry="55" class="dyn-soft"/>')
text('nucleus', 2210, 1155, 'dyn-cap', 'middle')
text('DHT', 1950, 1115, 'nf-l1', 'middle')
text('no DHT — atypical genitalia until puberty', 1545, 1290, TAG, when=O('srd'))
text('DHT ↓ — the prostate shrinks (BPH), hair loss slows', 1545, 1290, TAG, when=O('fin'))
text('receptor defective — the tissues ignore androgen', 1545, 1290, TAG, when=O('ais'))
text('flutamide competes at the receptor', 1545, 1290, TAG, when=O('flut'))
text('spironolactone competes at the receptor too', 1545, 1290, TAG, when=O('spiro'))

add('<rect class="dyn-soft" x="1520" y="1360" width="810" height="300" rx="26"/>')
text('Adipose tissue · liver', 1545, 1400, 'dyn-big')
text('most of a man’s estradiol is made here', 1545, 1420, 'dyn-cap')
add(f'<path d="{rrect(1600, 1440, 2310, 1590, 30)}" class="dyn-cell" style="stroke:var(--dk7)"/>')
text('estradiol', 1960, 1478, 'nf-l1', 'middle')
text('→ breast', 2200, 1478, 'nf-l1', 'middle')
text('estradiol ↑ → gynecomastia', 1545, 1640, TAG, when=O('klin', 'ais'))

# ════════ particles ════════
kinds = dict(gnrh=['gnrh', '--dk4'], lh=['lh', '--dk1'], fsh=['fsh', '--dk9'], t=['t', '--dk5'], inh=['inh', '--dk2'],
             dht=['dht', '--dk11'], e2=['e2', '--dk7'], prl=['prl', '--dk12'], sperm=['sperm', '--dk3'])
groups = [['gnrh', 'GnRH'], ['lh', 'LH'], ['fsh', 'FSH'], ['t', 'Testosterone'], ['inh', 'Inhibin B'], ['dht', 'DHT'],
          ['e2', 'Estradiol'], ['prl', 'Prolactin'], ['sperm', 'Sperm']]

def m(when, **kw):
    return dict(when=when if isinstance(when, list) else [when], **kw)
flows = [
  # GnRH: neuron → axon → portal veins → gonadotroph
  dict(d='M900 352 V745', len=393, speed=110, base=dict(gnrh=3), mods=[
      m(TR_BIG, set=dict(gnrh=6)), m(TR_SMALL, set=dict(gnrh=1)), m(O('kall', 'gnrhp'), set=dict(gnrh=0))]),
  # the pump into the portal vein
  dict(d='M780 565 H900 V745', len=300, speed=160, when=O('gnrhc'), base=dict(gnrh=8)),
  dict(d='M780 565 H900 V745', len=300, speed=110, when=O('gnrhp'), base=dict(gnrh=3)),
  # prolactin from the adenoma up to the GnRH neuron
  dict(d='M605 880 H560 V300 H776', len=841, speed=150, when=O('prl'), base=dict(prl=6)),
  # LH → Leydig cell; FSH → Sertoli cell
  dict(d='M900 936 V1080 H700 V1310', len=574, base=dict(lh=3), mods=[
      m(GN_HIGH, set=dict(lh=7)), m(GN_LOW, set=dict(lh=1)), m(O('kall'), set=dict(lh=0))]),
  dict(d='M900 936 V1080 H1030 V1236', len=430, base=dict(fsh=3), mods=[
      m(FSH_HIGH, set=dict(fsh=7)), m(FSH_LOW, set=dict(fsh=1)), m(O('kall'), set=dict(fsh=0))]),
  # inhibin B: Sertoli cell → pituitary
  dict(d='M1130 1236 V1130 H1340 V890 H1036', len=860, speed=120, base=dict(inh=4), mods=[m(INH_LOW, set=dict(inh=1))]),
  # testosterone next door to the Sertoli cell (intratesticular)
  dict(d='M792 1390 H922', len=130, speed=60, base=dict(t=2), mods=[
      m(T_LOW, set=dict(t=1)), m(O('aas'), set=dict(t=0)), m(O('tumor', 'ais'), set=dict(t=3))]),
  # the testosterone trunk to the GnRH neuron
  dict(d='M700 1470 V1775 H1450 V290 H1028', len=2962, base=dict(t=8), mods=[
      m(T_LOW, set=dict(t=3)), m(T_HIGH, set=dict(t=16)), m(O('kall'), set=dict(t=2))]),
  # to the gonadotroph
  dict(d='M1450 800 H1036', len=414, base=dict(t=2), mods=[m(T_LOW, set=dict(t=1)), m(T_HIGH, set=dict(t=4))]),
  # to the target cell and to adipose tissue / liver
  dict(d='M1450 1130 H1745', len=295, base=dict(t=2), mods=[m(T_LOW, set=dict(t=1)), m(T_HIGH, set=dict(t=4))]),
  dict(d='M1450 1490 H1745', len=295, base=dict(t=2), mods=[m(T_LOW, set=dict(t=1)), m(T_HIGH, set=dict(t=4))]),
  # DHT to the androgen receptor; estradiol to the breast
  dict(d='M1775 1130 H2125', len=350, speed=110, base=dict(dht=3), mods=[
      m(O('srd'), set=dict(dht=0)), m(O('fin'), set=dict(dht=1)), m(T_LOW, set=dict(dht=1))]),
  dict(d='M1775 1490 H2160', len=385, speed=110, base=dict(e2=2), mods=[m(O('klin', 'ais'), set=dict(e2=6))]),
  # sperm out of the tubule
  dict(d='M1080 1470 V1720 H1290', len=460, speed=60, base=dict(sperm=6), mods=[
      m(SPERM_LOW, set=dict(sperm=1)), m(O('klin'), set=dict(sperm=0)), m(O('gnrhc'), set=dict(sperm=2))]),
  # injected testosterone into the blood
  dict(d='M1690 1702 H1450', len=240, speed=110, when=O('aas'), base=dict(t=5)),
]

# ════════ sites ════════
AR_SHUT = ['!hpg:ais']
sites = [
  dict(x=790, y=300, n=[-1, 0], w=18, t='rec', l='Prolactin ⊣ GnRH', s='', ions=[['prl', 'in', 1]], reach=30,
       lx=775, ly=262, la='end', c='prolactinoma', when=O('prl'), boost=O('prl'), sfx=dict(boost='')),
  dict(x=1010, y=290, n=[1, 0], w=18, t='rec', l='Androgen receptor', s='testosterone ⊣ GnRH pulses', ions=[['t', 'in', 1]], cross=True, reach=34,
       lx=1040, ly=246, la='start', c='hptfeedback', need=AR_SHUT, closed='defective', stop=O('kall', 'gnrhp'),
       boost=T_HIGH, low=T_LOW, sfx=dict(stop=' — no neurons')),
  dict(x=900, y=760, n=[0, -1], w=18, t='rec', l='GnRH receptor', s='pulses → LH + FSH release', ions=[['gnrh', 'in', 1]], reach=40,
       lx=930, ly=712, la='start', c='gnrhanalogues', need=['!hpg:gnrhc'], closed='down-regulated', stop=O('kall'),
       boost=TR_BIG, low=TR_SMALL),
  dict(x=1020, y=800, n=[1, 0], w=18, t='rec', l='Androgen receptor', s='testosterone ⊣ LH', ions=[['t', 'in', 1]], cross=True, reach=34,
       lx=1050, ly=756, la='start', c='hptfeedback', need=AR_SHUT, closed='defective', boost=T_HIGH, low=T_LOW),
  dict(x=1020, y=890, n=[1, 0], w=18, t='rec', l='Inhibin B ⊣ FSH', s='the Sertoli cell’s own brake', ions=[['inh', 'in', 1]], cross=True, reach=34,
       lx=1050, ly=934, la='start', c='malehpg', low=INH_LOW),
  dict(x=700, y=1325, n=[0, -1], w=16, t='rec', l='LH receptor', s='→ testosterone', ions=[['lh', 'in', 1]], reach=28,
       lx=720, ly=1286, la='start', c='malehpg', stop=O('kall'), boost=GN_HIGH, low=GN_LOW),
  dict(x=700, y=1455, n=[0, 1], w=16, t='ex', l='Testosterone made', s='17α-hydroxylase · 17,20-lyase', ions=[['t', 'out', 2]], reach=30,
       lx=720, ly=1500, la='start', c='malehpg', block=O('keto', 'spiro'), boost=O('tumor', 'ais'),
       low=O('klin', 'crypt', 'kall', 'prl', 'gnrhc', 'aas')),
  dict(x=1030, y=1252, n=[0, -1], w=14, t='rec', l='FSH receptor', s='Sertoli cell → sperm', ions=[['fsh', 'in', 1]], reach=26,
       lx=1015, ly=1192, la='end', c='spermatogenesis', stop=O('kall'), boost=FSH_HIGH, low=FSH_LOW),
  dict(x=1130, y=1252, n=[0, -1], w=14, t='ex', l='Inhibin B out', s='tracks sperm output', ions=[['inh', 'out', 1]], reach=26,
       lx=1150, ly=1192, la='start', c='malehpg', low=INH_LOW),
  dict(x=1760, y=1130, n=[0, 1], w=14, t='ex', l='5α-reductase', s='testosterone → DHT', ions=[], c='reductase5a',
       lx=1760, ly=1190, la='middle', block=O('fin'), need=['!hpg:srd'], closed='absent'),
  dict(x=2140, y=1150, n=[-1, 0], w=14, t='rec', l='Androgen receptor', s='→ gene transcription', ions=[['dht', 'in', 1]], reach=24,
       lx=2150, ly=1226, la='middle', c='steroidrec', block=O('flut', 'spiro'), need=AR_SHUT, closed='defective',
       low=O('srd', 'fin')),
  dict(x=1760, y=1490, n=[0, 1], w=14, t='ex', l='Aromatase', s='testosterone → estradiol', ions=[], c='aromatasedef',
       lx=1760, ly=1550, la='middle', boost=O('klin', 'ais')),
]

notes = {
  '': 'Normal: pulsatile GnRH reaches the gonadotrophs through the portal veins. LH drives the Leydig cells to make testosterone; '
      'FSH drives the Sertoli cells, which nurse sperm and secrete inhibin B. Testosterone feeds back on the hypothalamus and '
      'pituitary (⊣ GnRH, LH), inhibin B on FSH. In the tissues 5α-reductase makes DHT and aromatase makes estradiol. Pick a pattern.',
  'hpg:klin': 'Klinefelter syndrome (47,XXY), the commonest primary hypogonadism: dysgenetic tubules make less inhibin B, so FSH '
              'rises; failing Leydig cells make less testosterone, so LH rises. Small firm testes, azoospermia, gynecomastia with a '
              'high estradiol.',
  'hpg:crypt': 'Bilateral cryptorchidism: sperm develop best below 37 °C, so undescended testes make few sperm and less inhibin B '
               '(FSH ↑). Leydig cells are mostly spared by heat, yet with both testes affected testosterone falls and LH rises; a '
               'unilateral case keeps a normal testosterone. Germ cell tumor risk is higher.',
  'hpg:varico': 'Varicocele: dilated pampiniform veins (usually on the left, where the gonadal vein drains into the renal vein) warm '
                'the testis. Heat-sensitive Sertoli cells make fewer sperm and less inhibin B, while heat-resistant Leydig cells keep '
                'testosterone normal — a cause of infertility; a “bag of worms” that grows with Valsalva.',
  'hpg:tumor': 'Testosterone-secreting (Leydig cell) tumor: the tumor makes testosterone on its own — up to 100 times normal — so '
               'feedback suppresses LH. High testosterone with low LH, the same pattern as exogenous androgens; in a child it causes '
               'peripheral precocious puberty.',
  'hpg:kall': 'Kallmann syndrome: the GnRH neurons fail to migrate and the olfactory bulbs fail to develop, so there is no GnRH and '
              'no sense of smell. GnRH, LH, FSH and testosterone are all low — hypogonadotropic (secondary) hypogonadism, with '
              'failure to complete puberty and a low sperm count.',
  'hpg:prl': 'Hyperprolactinemia (a prolactinoma, or a dopamine antagonist such as an antipsychotic): prolactin suppresses GnRH, so '
             'LH, FSH and testosterone fall — a hypogonadotropic pattern. Men notice decreased libido, impotence, infertility, '
             'sometimes gynecomastia; dopamine agonists (cabergoline, bromocriptine) treat a prolactinoma.',
  'hpg:gnrhp': 'Kallmann syndrome treated with pulsatile GnRH: a pump given in pulses replaces the missing hypothalamic rhythm, so the '
               'pituitary releases LH and FSH again, testosterone returns, and puberty and fertility follow. A long-acting '
               '(continuous) analog would not start puberty.',
  'hpg:gnrhc': 'Continuous leuprolide (a GnRH agonist): after a transient flare it down-regulates the pituitary GnRH receptors, so '
               'LH, FSH and testosterone fall — medical castration for prostate cancer. Adverse effects: hypogonadism, low libido, '
               'erectile dysfunction. Degarelix, a GnRH antagonist, has no flare.',
  'hpg:aas': 'Exogenous testosterone or anabolic steroids: blood testosterone is high, so feedback suppresses LH and FSH; '
             'intratesticular testosterone falls, the testes shrink and the sperm count drops, even to azoospermia. Also acne, '
             'gynecomastia, erythrocytosis, aggression.',
  'hpg:keto': 'Ketoconazole inhibits 17α-hydroxylase/17,20-lyase, blocking adrenal and gonadal steroid synthesis, so testosterone '
              'falls. Men often develop reversible gynecomastia as the estradiol-to-testosterone ratio rises.',
  'hpg:spiro': 'Spironolactone competes with DHT at the androgen receptor and also lowers 17α-hydroxylase activity, so plasma '
               'testosterone falls. Gynecomastia is its classic side effect in men; in women it treats hirsutism (PCOS).',
  'hpg:ais': 'Androgen insensitivity (46,XY): a defective androgen receptor leaves testosterone with nothing to act on. Testosterone, '
             'estrogen and LH are all high — the testes, driven by the high LH, make estradiol, so breasts develop; external genitalia '
             'look female, hair is scant and there is no uterus.',
  'hpg:flut': 'Flutamide or bicalutamide competes with testosterone and DHT at the androgen receptor — used for prostate cancer, often '
              'with a GnRH analog to block its flare. Side effects: gynecomastia and sexual dysfunction.',
  'hpg:srd': '5α-reductase deficiency (46,XY, autosomal recessive): testosterone cannot become DHT. Testosterone and estrogen are '
             'normal (LH normal or high) and DHT is low; the internal male ducts form, but the external genitalia are atypical until '
             'puberty, when rising testosterone masculinizes them.',
  'hpg:fin': 'Finasteride inhibits 5α-reductase and lowers DHT, which the prostate and hair follicles depend on — so it treats benign '
             'prostatic hyperplasia and male-pattern hair loss. Adverse effects: gynecomastia, sexual dysfunction.',
}

R = lambda when, d: dict(when=when if isinstance(when, list) else [when], d=d)
readouts = [
  dict(l='LH', mods=[R(O('klin', 'crypt', 'ais'), 1), R(O('kall', 'prl', 'gnrhc', 'aas', 'tumor'), -1), R(O('gnrhp'), 0)]),
  dict(l='FSH', mods=[R(O('klin', 'crypt'), 1), R(O('kall', 'prl', 'gnrhc', 'aas'), -1), R(O('gnrhp'), 0)]),
  dict(l='Testosterone', mods=[R(O('aas', 'tumor', 'ais'), 1), R(O('klin', 'crypt', 'kall', 'prl', 'gnrhc', 'keto', 'spiro'), -1),
                               R(O('varico', 'srd', 'gnrhp'), 0)]),
  dict(l='Inhibin B', mods=[R(O('klin', 'crypt', 'varico'), -1)]),
  # Klinefelter estradiol ↑: Bootcamp Reproduction (FA and textbooks name gynecomastia only)
  dict(l='Estradiol', mods=[R(O('klin', 'ais'), 1), R(O('srd'), 0)]),
  dict(l='DHT', mods=[R(O('srd', 'fin'), -1)]),
  dict(l='Sperm count', mods=[R(O('klin', 'crypt', 'varico', 'kall', 'prl', 'aas'), -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='hpg', label='Pattern', type='one', options=[
                ['klin', 'Klinefelter (47,XXY)', 'klinefelter'], ['crypt', 'Bilateral cryptorchidism', 'cryptorchid'],
                ['varico', 'Varicocele', 'varicocele'], ['tumor', 'Testosterone-secreting tumor', 'testisstromal'],
                ['kall', 'Kallmann syndrome', 'kallmann'], ['prl', 'Hyperprolactinemia', 'prolactinoma'],
                ['gnrhp', 'Pulsatile GnRH (Kallmann)', 'gnrhanalogues'], ['gnrhc', 'Continuous leuprolide', 'gnrhanalogues'],
                ['aas', 'Exogenous testosterone · steroids', 'anabolic'],
                ['keto', 'Ketoconazole', 'antiandrogens'], ['spiro', 'Spironolactone', 'antiandrogens'],
                ['ais', 'Androgen insensitivity', 'ais'], ['flut', 'Flutamide · bicalutamide', 'antiandrogens'],
                ['srd', '5α-reductase deficiency', 'reductase5a'], ['fin', 'Finasteride', 'antiandrogens']],
                 sections=[['Primary — the testis', ['klin', 'crypt', 'varico', 'tumor']],
                           ['Central — hypothalamus or pituitary', ['kall', 'prl']],
                           ['Drugs & hormones', ['gnrhp', 'gnrhc', 'aas', 'keto', 'spiro']],
                           ['Receptor & enzyme', ['ais', 'flut', 'srd', 'fin']]])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='First Aid pp. 332, 334, 645–646, 653–656, 667, 669, 674, 676 · Costanzo ch 10 · Guyton ch 81 · Katzung ch 40')

PY = 700   # info panels start under the switches + notes
MAP = dict(
  id='hpgsim', title='Testicular Axis Lab Simulator', topic='devrepro', after='androgen',
  sub='Pulsatile GnRH → LH on Leydig cells (testosterone) and FSH on Sertoli cells (sperm, inhibin B) → testosterone feeding back on '
      'the hypothalamus and pituitary, inhibin B on FSH, DHT and estradiol made in the tissues — pick a pattern (primary, central, '
      'a drug, a receptor or enzyme defect) and read LH, FSH, testosterone, inhibin B, estradiol, DHT and sperm count. Tap a '
      'receptor for its card',
  w=3500, h=1880,
  fa='332, 334, 645–646, 653–656, 667, 669, 674, 676', src=SRC,
  lanes=[('hpAxis', 'Hypothalamus & pituitary', 'ppp'), ('hpTestis', 'Testis', 'glycogen'), ('hpPeri', 'Tissues & drugs', 'sugars'),
         ('hpDz', 'Patterns', 'tca')],
  comps=[],
  nodes=[
    ('hp1', 'GnRH pulses & feedback', 330, 230, 'hpAxis', 'pulsatile vs continuous', ['hptfeedback', 'gnrhanalogues'], 'hub'),
    ('hp2', 'Kallmann syndrome', 330, 380, 'hpDz', 'no GnRH · anosmia', ['kallmann']),
    ('hp3', 'Gonadotroph · portal veins', 330, 700, 'hpAxis', 'LH, FSH share the α subunit', ['pitportal', 'glycoprot', 'pitcells']),
    ('hp4', 'Prolactinoma', 330, 860, 'hpDz', 'prolactin ⊣ GnRH', ['prolactinoma']),
    ('hp5', 'Sertoli & Leydig cells', 330, 1250, 'hpTestis', 'who makes what', ['malehpg', 'spermatogenesis'], 'hub'),
    ('hp6', 'Klinefelter syndrome', 330, 1370, 'hpDz', '47,XXY · primary', ['klinefelter']),
    ('hp7', 'Cryptorchidism · varicocele', 330, 1480, 'hpDz', 'heat hurts Sertoli cells', ['cryptorchid', 'varicocele']),
    ('hp8', 'Leydig cell tumor', 330, 1590, 'hpDz', 'testosterone ↑ · LH ↓', ['testisstromal']),
    ('hp9', 'Reading testosterone + LH', 330, 1700, 'hpDz', 'primary vs secondary', ['gonadpanel', 'axisreg'], 'hub'),
    ('hp10', 'Testosterone vs DHT', 1900, 915, 'hpPeri', 'the androgen receptor', ['androgenact', 'steroidrec']),
    ('hp11', 'AIS · 5α-reductase deficiency', 1980, 1330, 'hpDz', 'receptor · enzyme', ['ais', 'reductase5a']),
    ('hp12', 'Aromatase', 2150, 1640, 'hpPeri', 'androgen → estrogen', ['aromatasedef']),
    ('hp13', 'Anabolic steroids', 1880, 1760, 'hpPeri', 'high T, low LH', ['anabolic']),
    ('hp14', 'Antiandrogens', 1880, 1845, 'hpPeri', 'synthesis · 5α-reductase · receptor', ['antiandrogens']),
    ('hp15', 'Erection · ED · PDE5', 2190, 1790, 'hpPeri', 'point, squeeze, shoot', ['erection', 'ed', 'pde5']),
  ],
  panels=[
    (2420, PY, 1000, 'Read testosterone with LH (First Aid pp. 646, 655–656)', [
      ('T ↑ · LH ↑', 'androgen insensitivity'),
      ('T ↑ · LH ↓', 'testosterone-secreting tumor, or exogenous androgens'),
      ('T ↓ · LH ↑', 'primary (hypergonadotropic) — Klinefelter, bilateral cryptorchidism'),
      ('T ↓ · LH ↓', 'secondary (hypogonadotropic) — Kallmann, hyperprolactinemia, leuprolide'),
      ('Inhibin B ↓ · FSH ↑', 'the tubules are failing — Sertoli cells are temperature sensitive')]),
    (2420, PY + 200, 1000, 'Which androgen acts where (Costanzo ch 10; First Aid p. 653)', [
      ('Testosterone', 'epididymis, vas deferens, seminal vesicles · muscle · growth spurt · voice · sperm · libido'),
      ('DHT', 'fetal penis, scrotum, prostate · prostate growth, male hair, baldness, sebaceous glands'),
      ('Estradiol', 'made by aromatase (adipose, testes) · closes the epiphyses'),
      ('In the blood', 'about 98% bound to SHBG and albumin — only free testosterone acts')]),
    (2420, PY + 380, 1000, 'Male sexual response (First Aid p. 645)', [
      ('Erection', 'parasympathetic — pelvic splanchnic nerves S2–S4 · NO → cGMP → vasodilation'),
      ('Emission', 'sympathetic — hypogastric nerve, T11–L2'),
      ('Expulsion', 'visceral and somatic nerves — pudendal'),
      ('PDE-5 inhibitors', 'sildenafil — slows cGMP breakdown')]),
  ],
  dyn=dyn,
)
