# Chemo & DNA Repair in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A cell cycle wheel (G1 → S → G2 → M, with G0 and the G1/S and G2/M checkpoints) with cells travelling round it, a strip
# of DNA with nucleotides flowing in, a mitotic spindle, and the five repair pathways. A `one` switch gives a drug —
# antimetabolites (methotrexate, 5-FU, hydroxyurea, cytarabine), topoisomerase I and II inhibitors, anthracyclines,
# bleomycin, dactinomycin, alkylators and platinum, vinca alkaloids, taxanes — and the cells pile up at the phase it acts
# in (or are hit in any phase), the DNA shows the lesion and the tag gives the toxicity. A second `one` switch breaks a
# repair pathway: XP, Lynch, BRCA, ataxia-telangiectasia, Fanconi. 5 readouts. Facts from the pinned cards; FA pages in
# `fa`. No new cards.
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

import math
D = lambda *k: [f'rx:{x}' for x in k]
R = lambda *k: [f'rp:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
CX, CY, RR = 900, 820, 360
def pt(a, r=RR): t = math.radians(a); return round(CX + r * math.sin(t)), round(CY - r * math.cos(t))
def arc(a, b, r=RR):
    x0, y0 = pt(a, r); x1, y1 = pt(b, r)
    return f'M{x0} {y0} A{r} {r} 0 {1 if b - a > 180 else 0} 1 {x1} {y1}'
PH = dict(G1=(0, 160, '--dk2'), S=(160, 250, '--dk1'), G2=(250, 310, '--dk5'), M=(310, 360, '--dk7'))
S_DRUGS = D('mtx', 'fu', 'hu', 'cyta')
SG2 = D('topo1', 'topo2')
G2M = D('anthra', 'bleo')
M_DRUGS = D('vinca', 'taxane')
ANY = D('alk', 'plat', 'dact')
ALL = S_DRUGS + SG2 + G2M + M_DRUGS + ANY

text('Chemotherapy & DNA repair — where in the cycle, what in the DNA', 180, 150, 'dyn-big')
text('a stack = cells arrested in that phase · red marks = damage to DNA', 180, 176, 'dyn-cap')

# ════════ the cycle ════════
for k, (a, b, c) in PH.items():
    add(f'<path d="{arc(a, b)}" style="fill:none;stroke:var({c});stroke-width:28;opacity:.35"/>')
    mx, my = pt((a + b) / 2, RR + 80)
    text(k, mx, my + 8, 'nf-l1', 'middle')
text('DNA synthesis', *pt(205, RR - 80), 'nf-l2', 'middle')
text('mitosis', *pt(335, RR - 70), 'nf-l2', 'middle')
gx, gy = pt(70, RR + 200)
add(f'<circle cx="{gx}" cy="{gy}" r="60" class="dyn-soft"/>'); text('G0', gx, gy - 4, 'nf-l1', 'middle'); text('resting', gx, gy + 20, 'nf-l2', 'middle')
for a, lab in ((160, 'G1/S checkpoint'), (310, 'G2/M checkpoint')):
    x0, y0 = pt(a, RR - 40); x1, y1 = pt(a, RR + 40)
    add(f'<path d="M{x0} {y0} L{x1} {y1}" style="stroke:var(--ink);stroke-width:8"/>', unless=R('at'))
    add(f'<path d="M{x0} {y0} L{x1} {y1}" style="stroke:var(--bad);stroke-width:6;stroke-dasharray:6 8"/>', when=R('at'))
    lx, ly = pt(a, RR + 150); text(lab, lx, ly, 'nf-l2', 'middle')
text('ATM missing — damaged cells keep dividing', CX, CY + 50, 'nf-l1 dyn-tag', 'middle', when=R('at'))
text('acts in any phase (and on G0)', CX, CY + 6, 'nf-l1 dyn-tag', 'middle', when=ANY)
def pile(a, when):
    x, y = pt(a, RR - 60)
    add(''.join(f'<circle cx="{x + dx}" cy="{y + dy}" r="11" style="fill:var(--dk1);opacity:.8"/>'
                for dx, dy in ((-24, 0), (0, -6), (24, 0), (-12, -24), (12, -24), (0, 20))), when=when)
pile(165, S_DRUGS + SG2); pile(255, SG2 + G2M); pile(315, M_DRUGS)

# ════════ DNA strip ════════
DX0, DX1, DY = 1550, 2350, 470
add(f'<path d="M{DX0} {DY} H{DX1} M{DX0} {DY + 60} H{DX1}" style="stroke:var(--dk2);stroke-width:8;opacity:.6"/>')
for x in range(DX0 + 20, DX1, 40): add(f'<path d="M{x} {DY} V{DY + 60}" style="stroke:var(--ink-3);stroke-width:3"/>')
text('DNA', DX0, DY - 30, 'nf-l1')
for x in (1760, 1900, 2040):
    add(f'<path d="M{x} {DY - 6} V{DY + 66}" style="stroke:var(--bad);stroke-width:10"/>', when=D('alk', 'plat'))
    add(f'<rect x="{x - 14}" y="{DY + 14}" width="28" height="32" rx="4" style="fill:var(--bad);opacity:.8"/>', when=D('anthra', 'dact'))
    add(f'<rect x="{x - 14}" y="{DY - 10}" width="28" height="20" style="fill:var(--surface)"/>', when=D('bleo', 'anthra', 'topo1', 'topo2'))
    add(f'<rect x="{x - 14}" y="{DY + 50}" width="28" height="20" style="fill:var(--surface)"/>', when=D('bleo', 'anthra', 'topo2'))
add(f'<rect x="2120" y="{DY + 50}" width="230" height="20" style="fill:var(--surface)"/>', when=D('cyta'))
add(X(2110, DY + 60), when=D('cyta'))
LES = dict(alk='cross-links (guanine N-7) — any phase', plat='intra- and interstrand cross-links', anthra='intercalates + radicals + topo II poison',
           dact='intercalates — blocks RNA polymerase', bleo='free radicals break both strands', topo1='topo I can’t reseal one strand',
           topo2='topo II can’t reseal both strands', cyta='incorporated — chain terminates')
for k, t in LES.items(): text(t, (DX0 + DX1) // 2, DY + 110, 'nf-l1 dyn-tag', 'middle', when=D(k))
# nucleotide supply
add(f'<rect x="{DX0}" y="620" width="800" height="150" rx="24" class="dyn-soft"/>')
text('nucleotide supply', DX0 + 20, 650, 'nf-l1')
SUP = (('DHFR → THF → dTMP, purines', 'mtx', 1660), ('thymidylate synthase', 'fu', 1950), ('ribonucleotide reductase', 'hu', 2200))
for lab, k, x in SUP:
    text(lab, x, 720, 'nf-l2', 'middle'); add(X(x, 690, 14), when=D(k))
# spindle
add(f'<rect x="{DX0}" y="820" width="800" height="200" rx="24" class="dyn-soft"/>')
text('mitotic spindle', DX0 + 20, 850, 'nf-l1')
for dy in (-40, 0, 40):
    add(f'<path d="M1800 {920 + dy} Q1950 {920 + dy * 0.2} 2100 {920 + dy}" style="fill:none;stroke:var(--dk7);stroke-width:4"/>', unless=D('vinca', 'taxane'))
    add(f'<path d="M1800 {920 + dy} Q1950 {920 + dy * 0.2} 2100 {920 + dy}" style="fill:none;stroke:var(--bad);stroke-width:9"/>', when=D('taxane'))
add('<circle cx="1790" cy="920" r="14" style="fill:var(--ink-2)"/><circle cx="2110" cy="920" r="14" style="fill:var(--ink-2)"/>')
text('no spindle — tubulin can’t polymerize', 1950, 990, 'nf-l1 dyn-tag', 'middle', when=D('vinca'))
text('frozen spindle — can’t disassemble', 1950, 990, 'nf-l1 dyn-tag', 'middle', when=D('taxane'))
# toxicity tag
TOX = dict(mtx='leucovorin (folinic acid) rescues normal cells', fu='leucovorin enhances it', hu='also ↑ HbF in sickle cell', cyta='myelosuppression',
           topo1='severe myelosuppression · diarrhea (irinotecan)', topo2='myelosuppression · alopecia',
           anthra='dilated cardiomyopathy — dexrazoxane', bleo='pulmonary fibrosis · little myelosuppression', dact='myelosuppression',
           alk='cyclophosphamide: hemorrhagic cystitis — mesna', plat='cisplatin: kidney + cochlea — amifostine',
           vinca='vincristine: neuropathy · vinblastine: marrow', taxane='myelosuppression · neuropathy · hypersensitivity')
for k, t in TOX.items(): text(('' if k in ('mtx', 'fu', 'hu') else 'toxicity: ') + t, CX, 1420, 'nf-l1', 'middle', when=D(k))
# repair pathways
add(f'<rect x="{DX0}" y="1070" width="800" height="300" rx="24" class="dyn-soft"/>')
text('DNA repair', DX0 + 20, 1100, 'nf-l1')
REP = (('xp', 'nucleotide excision — UV pyrimidine dimers'), ('lynch', 'mismatch repair — replication errors'),
       ('brca', 'homologous recombination — double-strand breaks (S, G2)'), ('fanc', 'interstrand cross-link repair'),
       ('at', 'ATM — senses double-strand breaks, halts the cycle'))
for i, (k, lab) in enumerate(REP):
    y = 1150 + i * 46
    add(f'<circle cx="{DX0 + 40}" cy="{y - 6}" r="9" style="fill:var(--ok)"/>', unless=R(k))
    add(X(DX0 + 40, y - 6, 11), when=R(k))
    text(lab, DX0 + 70, y, 'nf-l2')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
def phase_flow(k, stop=None, low=None):
    a, b, c = PH[k]
    f = dict(d=arc(a, b), len=round(math.radians(b - a) * RR), speed=90, r=10, base=dict(cell=3), mods=[])
    if low: f['mods'].append(m(low, set=dict(cell=1)))
    if stop: f['mods'].append(m(stop, set=dict(cell=0)))
    return f
flows = [
  phase_flow('G1', low=ANY),
  phase_flow('S', stop=S_DRUGS, low=ANY + SG2),
  phase_flow('G2', stop=S_DRUGS + SG2, low=ANY + G2M),
  phase_flow('M', stop=S_DRUGS + SG2 + G2M + M_DRUGS, low=ANY),
  dict(d=f'M1950 770 V{DY + 66}', len=230, speed=70, r=8, base=dict(nt=3), mods=[m(D('mtx', 'fu', 'hu'), set=dict(nt=0))]),
  dict(d=f'M{DX0} {DY + 30} H{DX1}', len=800, speed=120, r=8, base=dict(pol=1), mods=[m(D('cyta'), set=dict(pol=0))]),
]
sites = [dict(x=CX, y=CY - RR, n=[0, -1], w=10, t='rec', l='', aria='Cell cycle', c='cytarabine', ions=[]),
         dict(x=DX1 - 30, y=1100, n=[0, 1], w=10, t='rec', l='', aria='Homologous recombination', c='brca', ions=[])]

readouts = [
  dict(l='Cells completing mitosis', mods=[dict(when=ALL, d=-1), dict(when=R('at'), d=1)]),
  dict(l='DNA damage', mods=[dict(when=D('alk', 'plat', 'anthra', 'bleo', 'dact', 'topo1', 'topo2', 'cyta') + R('xp', 'lynch', 'brca', 'fanc', 'at'), d=1)]),
  dict(l='dNTP supply', mods=[dict(when=D('mtx', 'fu', 'hu'), d=-1)]),
  dict(l='Mutations · cancer risk', mods=[dict(when=R('xp', 'lynch', 'brca', 'fanc', 'at'), d=1)]),
  dict(l='Microsatellite instability', mods=[dict(when=R('lynch'), d=1), dict(when=R('xp', 'brca'), d=0)]),
]

notes = {
  '': 'Cells cycle G1 → S (DNA synthesis) → G2 → M, with checkpoints at G1/S and G2/M. Phase-specific drugs catch cells in one phase; '
      'cell-cycle–nonspecific drugs damage DNA whatever the phase. Repair pathways fix the damage — lose one and mutations accumulate.',
  'rx:mtx': 'Methotrexate: competitive DHFR inhibitor — no THF, so no dTMP or purines; DNA synthesis stops. S phase. Leucovorin rescues.',
  'rx:fu': '5-FU: bioactivated to 5-FdUMP, which inhibits thymidylate synthase — no dTMP. S phase. Leucovorin enhances it.',
  'rx:hu': 'Hydroxyurea: blocks ribonucleotide reductase — no deoxyribonucleotides. S phase. Raises HbF in sickle cell disease.',
  'rx:cyta': 'Cytarabine: pyrimidine nucleoside analog incorporated into DNA — terminates the chain and inhibits DNA polymerase. S phase. AML.',
  'rx:topo1': 'Irinotecan, topotecan: inhibit topoisomerase I, which nicks one strand — strand breaks; arrest in S and G2.',
  'rx:topo2': 'Etoposide, teniposide: inhibit topoisomerase II, which cuts both strands — strand breaks; arrest in S and G2.',
  'rx:anthra': 'Doxorubicin, daunorubicin: intercalate, make iron-dependent free radicals and poison topoisomerase II. Considered G2/M. '
               'Dose-dependent dilated cardiomyopathy — dexrazoxane.',
  'rx:bleo': 'Bleomycin: binds DNA and iron, radicals break the strands. G2/M. Pulmonary fibrosis.',
  'rx:dact': 'Dactinomycin: intercalates and blocks RNA polymerase. Cell-cycle nonspecific. Wilms, Ewing, rhabdomyosarcoma.',
  'rx:alk': 'Cyclophosphamide, ifosfamide (and nitrosoureas): need hepatic P-450 activation, then cross-link DNA at guanine N-7. '
            'Cell-cycle nonspecific. Acrolein → hemorrhagic cystitis (mesna). Nitrosoureas cross the BBB.',
  'rx:plat': 'Cisplatin, carboplatin: intra- and interstrand cross-links, cell-cycle nonspecific. Cisplatin: nephrotoxicity and '
             'ototoxicity (amifostine).',
  'rx:vinca': 'Vincristine, vinblastine: bind β-tubulin and block polymerization — no spindle. M phase. Vincristine: neuropathy; '
              'vinblastine: marrow.',
  'rx:taxane': 'Paclitaxel, docetaxel: hyperstabilize microtubules — the spindle can’t disassemble. M phase.',
  'rp:xp': 'Xeroderma pigmentosum: no nucleotide excision repair, so UV pyrimidine dimers accumulate — severe sunburn, skin cancers young.',
  'rp:lynch': 'Lynch syndrome: no mismatch repair (MSH2, MLH1, MSH6, PMS2) — microsatellite instability; colorectal (proximal), '
              'endometrial, ovarian cancer.',
  'rp:brca': 'BRCA1/2: no homologous recombination (S and G2), so double-strand breaks go to error-prone end joining — breast, ovarian, '
             'prostate, pancreatic cancer.',
  'rp:fanc': 'Fanconi anemia: interstrand cross-links can’t be resolved — marrow failure, short stature, thumb and radial defects, AML.',
  'rp:at': 'Ataxia-telangiectasia: ATM doesn’t sense double-strand breaks, so the cycle isn’t halted — cerebellar ataxia, '
           'telangiectasias, IgA deficiency, lymphoma and leukemia.',
}

dyn = dict(
  kinds=dict(cell=['cells', '--dk2'], nt=['dna', '--dk5'], pol=['dna', '--dk1']),
  groups=[['cells', 'Cells in the cycle'], ['dna', 'Nucleotides · polymerase']],
  switches=[dict(id='rx', label='Drug', type='one', options=[
              ['mtx', 'Methotrexate', 'mtx'], ['fu', '5-Fluorouracil', 'fluorouracil'], ['hu', 'Hydroxyurea', 'hydroxyurea'],
              ['cyta', 'Cytarabine', 'cytarabine'], ['topo1', 'Irinotecan (topo I)', 'topo1'], ['topo2', 'Etoposide (topo II)', 'topo2'],
              ['anthra', 'Doxorubicin', 'anthracycline'], ['bleo', 'Bleomycin', 'bleomycin'], ['dact', 'Dactinomycin', 'dactinomycin'],
              ['alk', 'Cyclophosphamide', 'cyclophos'], ['plat', 'Cisplatin', 'platinum'], ['vinca', 'Vincristine', 'vinca'],
              ['taxane', 'Paclitaxel', 'taxane']]),
            dict(id='rp', label='Repair defect', type='one', options=[
              ['xp', 'Xeroderma pigmentosum', 'xp'], ['lynch', 'Lynch syndrome', 'lynch'], ['brca', 'BRCA1/2', 'brca'],
              ['fanc', 'Fanconi anemia', 'fanconi'], ['at', 'Ataxia-telangiectasia', 'ataxia']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 444–447 · Katzung ch 54 · Marks ch 12')

MAP = dict(
  id='chemosim', title='Chemo & DNA Repair in Motion', topic='heme', after='chemo',
  sub='Cells go round the cycle; give a drug and watch them pile up in its phase, see the lesion it leaves in DNA and its signature '
      'toxicity — then break a repair pathway: xeroderma pigmentosum, Lynch, BRCA, Fanconi, ataxia-telangiectasia',
  w=3600, h=1900,
  fa='37, 115, 190, 395, 427, 444, 445, 447',
  src=['Katzung ch 54 — Cancer Chemotherapy', 'Robbins ch 12 — The heart', 'Marks ch 12 — Synthesis of DNA',
       'Katzung ch 36 — Nonsteroidal Anti-Inflammatory Drugs, Disease-Modifying Antirheumatic Drugs, Nonopioid Analgesics, & Drugs Used in Gout',
       'Katzung ch 5 — Pharmacogenomics', 'Katzung ch 33 — Agents Used in Cytopenias; Hematopoietic Growth Factors',
       'Robbins ch 14 — Red blood cell and bleeding disorders', 'Robbins ch 7 — Neoplasia', 'Robbins ch 25 — The skin',
       'Robbins ch 17 — The gastrointestinal tract', 'Robbins ch 23 — The breast', 'Robbins ch 6 — Diseases of the immune system'],
  lanes=[('cxS', 'S-phase drugs', 'glycolysis'), ('cxDam', 'DNA-damaging drugs', 'tca'), ('cxM', 'M-phase drugs', 'ppp'), ('cxRep', 'Repair defects', 'gluconeo')],
  nodes=[
    ('cx1', 'Cytarabine', 330, 1620, 'cxS', 'chain termination', ['cytarabine'], 'hub'),
    ('cx2', 'Topoisomerase inhibitors', 760, 1620, 'cxDam', 'S and G2', ['topo1', 'topo2']),
    ('cx3', 'Anthracyclines · bleomycin', 1200, 1620, 'cxDam', 'G2/M · heart, lung', ['anthracycline', 'bleomycin']),
    ('cx4', 'Alkylators · platinum', 1640, 1620, 'cxDam', 'cross-links', ['cyclophos', 'nitrosourea', 'busulfan', 'procarbazine', 'platinum']),
    ('cx5', 'Dactinomycin', 2080, 1620, 'cxDam', 'blocks RNA polymerase', ['dactinomycin']),
    ('cx6', 'Vincas · taxanes', 330, 1760, 'cxM', 'assembly vs disassembly', ['vinca', 'taxane']),
    ('cx7', 'XP · Lynch', 760, 1760, 'cxRep', 'NER · mismatch', ['xp', 'lynch']),
    ('cx8', 'BRCA · Fanconi', 1200, 1760, 'cxRep', 'breaks · cross-links', ['brca', 'fanconi']),
    ('cx9', 'Ataxia-telangiectasia', 1640, 1760, 'cxRep', 'ATM', ['ataxia'])],
  panels=[
    (2500, PANY, 1000, 'Phase (First Aid pp. 444–447)', [
      ('S', 'methotrexate, 5-FU, hydroxyurea, cytarabine'),
      ('S and G2', 'topoisomerase I and II inhibitors'),
      ('G2/M', 'bleomycin, anthracyclines'),
      ('M', 'vinca alkaloids, taxanes'),
      ('Any phase', 'alkylators, platinum, dactinomycin')])],
  dyn=dyn)
