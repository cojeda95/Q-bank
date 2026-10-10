# Antiviral Drug Targets in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Four infected cells side by side, each with its replication cycle moving: herpes (drug → viral kinase → host kinases →
# triphosphate → viral DNA polymerase), hepatitis C (polyprotein → NS3/4A protease → NS5A complex → NS5B polymerase),
# hepatitis B (cccDNA → pregenomic RNA → reverse transcriptase → new virions) and influenza (cap-snatching PA endonuclease,
# neuraminidase release). A `one` switch gives a drug and its step is blocked downstream; a `steps` switch picks HSV or CMV
# and a toggle makes the herpes virus kinase-mutant (resistance). 4 readouts. Facts from the pinned cards; FA pages in `fa`.
# No new cards. HIV has its own map (hivflow).
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

D = lambda *k: [f'rx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=16): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def box(x0, y0, x1, y1, lab, cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="20" class="{cls}"/>')
    if lab: text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')
def panel(x0, y0, x1, y1, title):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="40" class="dyn-soft"/>'); text(title, x0 + 30, y0 + 44, 'dyn-big')
# herpes logic
HS_OK = ['rx:acv&hv:hsv&!tk', 'rx:gcv&hv:cmv&!tk'] + D('fos', 'cdv')
HS_KIN_FAIL = ['rx:acv&hv:cmv', 'rx:acv&tk', 'rx:gcv&tk']
HCV = D('previr', 'asvir', 'buvir')
HBV = D('tdf')
FLU = D('osel', 'balox')

text('Antiviral drug targets — where each drug breaks the cycle', 180, 150, 'dyn-big')
text('HIV has its own map · pick a drug, then try HSV vs CMV and a kinase-mutant virus', 180, 176, 'dyn-cap')

# ════════ herpes ════════
panel(300, 260, 1300, 820, 'Herpes (HSV · VZV · CMV)')
box(330, 390, 520, 450, 'Drug'); box(560, 390, 780, 450, 'Viral kinase'); box(820, 390, 1010, 450, 'Host kinases')
text('TK (HSV/VZV) · UL97 (CMV)', 670, 480, 'nf-l2', 'middle')
add('<circle cx="1000" cy="640" r="150" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--dk2);stroke-width:3"/>')
text('nucleus', 1000, 760, 'nf-l2', 'middle')
box(900, 610, 1100, 670, 'DNA polymerase')
add(X(800, 420, 12), when=HS_KIN_FAIL)
text('no viral kinase to activate it — CMV lacks TK', 700, 530, 'nf-l1 dyn-tag', 'middle', when=['rx:acv&hv:cmv&!tk'])
text('kinase-mutant virus — resistant', 700, 530, 'nf-l1 dyn-tag', 'middle', when=['rx:acv&tk', 'rx:gcv&tk'])
text('skips the viral kinase — works on mutants', 700, 530, 'nf-l1 dyn-tag', 'middle', when=D('fos', 'cdv'))
add(X(1000, 690), when=HS_OK)
text('virions out', 1240, 560, 'nf-l2', 'middle')

# ════════ hepatitis C ════════
panel(1350, 260, 2400, 820, 'Hepatitis C — RNA, no DNA stage')
box(1380, 390, 1560, 450, '+RNA genome')
add('<rect x="1600" y="400" width="520" height="40" rx="10" style="fill:var(--dk5);fill-opacity:.35"/>')
text('one long polyprotein', 1860, 426, 'nf-l2', 'middle')
for x in (1730, 1860, 1990): add(f'<path d="M{x} 392 V448" style="stroke:var(--ink-2);stroke-width:4;stroke-dasharray:5 5"/>', unless=D('previr'))
box(1600, 560, 1820, 620, 'NS5A complex'); box(1870, 560, 2110, 620, 'NS5B polymerase')
add(X(1860, 420), when=D('previr')); add(X(1710, 590), when=D('asvir')); add(X(1990, 590), when=D('buvir'))
text('no DNA, no nuclear reservoir — direct-acting antivirals cure it', 1875, 780, 'nf-l1', 'middle')
text('virions out', 2280, 560, 'nf-l2', 'middle')

# ════════ hepatitis B ════════
panel(300, 880, 1300, 1450, 'Hepatitis B — DNA via reverse transcription')
add('<circle cx="560" cy="1180" r="140" style="fill:var(--dk2);fill-opacity:.08;stroke:var(--dk2);stroke-width:3"/>')
text('nucleus', 560, 1300, 'nf-l2', 'middle')
add('<circle cx="560" cy="1160" r="44" style="fill:none;stroke:var(--dk1);stroke-width:8"/>'); text('cccDNA', 560, 1166, 'nf-l1', 'middle')
box(780, 1020, 1000, 1080, 'pregenomic RNA'); box(780, 1220, 1050, 1280, 'Reverse transcriptase')
add(X(915, 1250), when=HBV)
text('cccDNA stays — treatment is long-term; stopping can flare', 800, 1400, 'nf-l1 dyn-tag', 'middle', when=HBV)
text('virions out', 1220, 1120, 'nf-l2', 'middle')

# ════════ influenza ════════
panel(1350, 880, 2400, 1450, 'Influenza')
box(1380, 1010, 1600, 1070, 'host mRNA cap'); box(1650, 1010, 1900, 1070, 'PA endonuclease')
box(1950, 1010, 2150, 1070, 'viral mRNA')
add('<path d="M1400 1340 H2360" style="stroke:var(--dk3);stroke-width:8"/>'); text('cell membrane · sialic acid', 1880, 1380, 'nf-l2', 'middle')
add(X(1775, 1040), when=D('balox'))
for x in (1700, 1880, 2060):
    add(f'<circle cx="{x}" cy="1300" r="30" style="fill:var(--dk7);fill-opacity:.4;stroke:var(--dk7);stroke-width:3"/>', when=D('osel'))
text('virions stuck to sialic acid', 1880, 1250, 'nf-l1 dyn-tag', 'middle', when=D('osel'))
text('“cap-snatching”', 1775, 1110, 'nf-l2', 'middle')

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
flows = [
  dict(d='M520 420 H560', len=40, speed=30, r=8, base=dict(drug=2), when=D('acv', 'gcv')),
  dict(d='M780 420 H820', len=40, speed=30, r=8, base=dict(drug=2), when=D('acv', 'gcv', 'cdv'), unless=HS_KIN_FAIL),
  dict(d='M1010 420 C1060 460 1060 560 1010 610', len=220, speed=70, r=8, base=dict(drug=3), when=D('acv', 'gcv', 'cdv'), unless=HS_KIN_FAIL),
  dict(d='M425 450 C440 560 700 640 900 640', len=560, speed=110, r=8, base=dict(drug=3), when=D('fos')),
  dict(d='M425 450 C440 520 700 520 820 440', len=450, speed=110, r=8, base=dict(drug=3), when=D('cdv')),
  dict(d='M1100 640 H1240 V580', len=200, speed=90, r=9, base=dict(vir=3), unless=HS_OK),
  dict(d='M1560 420 H1600', len=40, speed=30, r=9, base=dict(vir=2)),
  dict(d='M1860 440 V500 H1710 V560', len=270, speed=60, r=9, base=dict(vir=2), unless=HCV),
  dict(d='M1820 590 H1870', len=50, speed=40, r=9, base=dict(vir=2), unless=HCV),
  dict(d='M2110 590 H2240 V580', len=150, speed=80, r=9, base=dict(vir=3), unless=HCV),
  dict(d='M604 1160 C680 1100 720 1060 780 1050', len=200, speed=70, r=9, base=dict(vir=3)),
  dict(d='M890 1080 V1220', len=140, speed=60, r=9, base=dict(vir=3)),
  dict(d='M1050 1250 C1150 1250 1220 1200 1220 1140', len=220, speed=80, r=9, base=dict(vir=3), unless=HBV),
  dict(d='M1600 1040 H1650', len=50, speed=30, r=9, base=dict(vir=2)),
  dict(d='M1900 1040 H1950', len=50, speed=30, r=9, base=dict(vir=2), unless=D('balox')),
  dict(d='M2050 1070 V1300 H2360', len=540, speed=110, r=9, base=dict(vir=3), unless=FLU),
]
sites = [
  dict(x=1000, y=610, n=[0, -1], w=10, t='rec', l='', aria='Acyclovir', c='acyclovir', ions=[]),
  dict(x=670, y=390, n=[0, -1], w=10, t='rec', l='', aria='Resistance', c='avresist', ions=[]),
  dict(x=1860, y=400, n=[0, -1], w=10, t='rec', l='', aria='NS3/4A protease', c='ns3', ions=[]),
  dict(x=1990, y=560, n=[0, -1], w=10, t='rec', l='', aria='NS5B — sofosbuvir', c='sofosbuvir', ions=[]),
  dict(x=915, y=1220, n=[0, -1], w=10, t='rec', l='', aria='HBV reverse transcriptase', c='hbvdrugs', ions=[]),
  dict(x=1880, y=1340, n=[0, 1], w=10, t='rec', l='', aria='Neuraminidase', c='nai', ions=[]),
]

readouts = [
  dict(l='Viral replication', mods=[dict(when=HS_OK + HCV + HBV + FLU, d=-1), dict(when=HS_KIN_FAIL, d=0)]),
  dict(l='Cure possible', mods=[dict(when=HCV, d=1), dict(when=HBV, d=-1)]),
  dict(l='Kidney toxicity', mods=[dict(when=D('fos', 'cdv', 'gcv', 'acv'), d=1)]),
  dict(l='Myelosuppression', mods=[dict(when=D('gcv'), d=1)]),
]

notes = {
  '': 'Antivirals hit steps the host cell doesn’t share: a viral kinase or polymerase, a viral protease, reverse transcriptase, or the '
      'enzymes that make and release new virions. Error-prone viral polymerases mean resistant variants exist before treatment.',
  'hv:hsv': 'HSV and VZV carry thymidine kinase (TK) — the first, virus-only activation step for acyclovir.',
  'hv:cmv': 'CMV has no TK; its UL97 kinase activates ganciclovir instead. Disease when cell-mediated immunity fails (AIDS, transplant).',
  'tk': 'Kinase-mutant virus: TK-deficient HSV resists acyclovir, UL97-mutant CMV resists ganciclovir — switch to foscarnet or cidofovir.',
  'rx:acv': 'Acyclovir (valacyclovir, famciclovir): a guanosine analogue phosphorylated first by viral TK, then host kinases; the '
            'triphosphate inhibits viral DNA polymerase and ends the chain. HSV and VZV; weak against CMV. IV: crystal nephropathy — hydrate.',
  'rx:gcv': 'Ganciclovir (valganciclovir): activated by CMV UL97, then host kinases — CMV retinitis, colitis, transplant prophylaxis. '
            'Myelosuppression, kidney toxicity.',
  'rx:fos': 'Foscarnet: a pyrophosphate analogue that binds the polymerase directly — no kinase needed, so it works on TK- and UL97-mutant '
            'virus. Nephrotoxicity, calcium and phosphate shifts → seizures.',
  'rx:cdv': 'Cidofovir: a nucleotide analogue activated by host kinases only — skips the viral kinase. Nephrotoxicity (probenecid, saline).',
  'rx:previr': 'NS3/4A protease inhibitors (-previr: glecaprevir, grazoprevir): the polyprotein isn’t cut, so no working viral proteins.',
  'rx:asvir': 'NS5A inhibitors (-asvir: velpatasvir, ledipasvir, pibrentasvir): no replication complex, no virion assembly.',
  'rx:buvir': 'Sofosbuvir (-buvir): a uridine analogue built into new RNA by NS5B — the chain stops. Backbone of HCV regimens; avoid '
              'with amiodarone (bradycardia).',
  'rx:tdf': 'Tenofovir, entecavir: stop HBV reverse transcription. None removes cccDNA, so therapy is long-term and stopping can cause a '
            'flare. With HIV, use a regimen active against both.',
  'rx:osel': 'Oseltamivir (zanamivir, peramivir): block neuraminidase, so new virions stay stuck to sialic acid. Influenza A and B, best '
             'within 48 hours.',
  'rx:balox': 'Baloxavir: blocks the PA cap-dependent endonuclease — no cap-snatching, no viral mRNA. Acts earlier than neuraminidase inhibitors.',
}

dyn = dict(
  kinds=dict(drug=['drug', '--accent'], vir=['virus', '--dk7']),
  groups=[['drug', 'Drug activation'], ['virus', 'Viral replication']],
  switches=[dict(id='hv', label='Herpesvirus', type='steps', options=[['hsv', 'HSV · VZV'], ['cmv', 'CMV']]),
            dict(id='tk', label='Resistance', type='toggle', on='Kinase-mutant virus', off='Wild-type virus', def_=False),
            dict(id='rx', label='Drug', type='one', options=[
              ['acv', 'Acyclovir', 'acyclovir'], ['gcv', 'Ganciclovir', 'ganciclovir'], ['fos', 'Foscarnet', 'foscarnet'],
              ['cdv', 'Cidofovir', 'foscarnet'], ['previr', 'Glecaprevir (NS3/4A)', 'ns3'], ['asvir', 'Velpatasvir (NS5A)', 'ns5a'],
              ['buvir', 'Sofosbuvir (NS5B)', 'sofosbuvir'], ['tdf', 'Tenofovir · entecavir (HBV)', 'hbvdrugs'],
              ['osel', 'Oseltamivir', 'nai'], ['balox', 'Baloxavir', 'baloxavir']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 196–199 · Katzung ch 49')
dyn['switches'][1]['def'] = dyn['switches'][1].pop('def_')

MAP = dict(
  id='avsim', title='Antiviral Targets in Motion', topic='id', after='antiviral',
  sub='Herpes, hepatitis C, hepatitis B and influenza replicating side by side — give acyclovir, ganciclovir, foscarnet, cidofovir, '
      'a -previr, -asvir or -buvir, tenofovir, oseltamivir or baloxavir and see which step stops, and why kinase mutants resist',
  w=3600, h=1900,
  fa='162, 170, 171, 172, 173, 180, 196, 197, 199',
  src=['Katzung ch 49 — Antiviral Agents', 'Katzung ch 51 — Clinical Use of Antimicrobial Agents', 'Robbins ch 8 — Infectious diseases',
       'Robbins ch 18 — Liver and gallbladder', 'Katzung Appendix 1 — Vaccines, Immune Globulins, & Other Complex Biologic Products'],
  lanes=[('avHerp', 'Herpesviruses', 'glycolysis'), ('avHep', 'Hepatitis B and C', 'tca'), ('avFlu', 'Influenza', 'gluconeo')],
  nodes=[
    ('av1', 'Acyclovir family', 330, 1620, 'avHerp', 'viral TK first', ['acyclovir'], 'hub'),
    ('av2', 'Ganciclovir · CMV', 760, 1620, 'avHerp', 'UL97 · marrow', ['ganciclovir', 'cmv']),
    ('av3', 'Foscarnet · cidofovir', 1200, 1620, 'avHerp', 'no viral kinase', ['foscarnet']),
    ('av4', 'Antiviral resistance', 1640, 1620, 'avHerp', 'kinase mutants', ['avresist']),
    ('av5', 'Hepatitis C drugs', 330, 1760, 'avHep', '-previr · -asvir · -buvir', ['hcv', 'ns3', 'ns5a', 'sofosbuvir']),
    ('av6', 'Hepatitis B drugs', 760, 1760, 'avHep', 'cccDNA stays', ['hbvdrugs']),
    ('av7', 'Influenza drugs', 1200, 1760, 'avFlu', 'neuraminidase · PA', ['nai', 'baloxavir'])],
  panels=[
    (2500, PANY, 1000, 'Target → drug (First Aid pp. 196–199)', [
      ('Viral kinase first', 'acyclovir (TK), ganciclovir (UL97)'),
      ('Polymerase, no kinase', 'foscarnet, cidofovir'),
      ('HCV', 'NS3/4A -previr · NS5A -asvir · NS5B -buvir'),
      ('HBV reverse transcriptase', 'tenofovir, entecavir'),
      ('Influenza', 'neuraminidase: oseltamivir · PA: baloxavir')])],
  dyn=dyn)
