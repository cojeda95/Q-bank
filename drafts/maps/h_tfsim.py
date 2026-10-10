# Blood Transfusion in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Left: the blood bank bench — tubes where red cells meet serum, anti-A/anti-B sera and Coombs reagent. A `lab` switch runs ABO/Rh
# typing, the antibody screen (indirect antiglobulin), the crossmatch and the direct antiglobulin test, and shows which clump.
# Right: a unit running down a line into a patient. A `pt` switch picks the patient or the unit — fever last time, immunocompromised,
# IgA-deficient with anti-IgA, massive transfusion, a room-temperature platelet unit, an Rh-negative mother — and a `fix` toggle
# applies the matching answer (leukoreduce, irradiate, IgA-free, Rho(D) immune globulin). Schematic. 5 readouts. Facts from the
# pinned cards; FA pages in `fa`. No new cards.
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

LB = lambda *k: [f'lab:{x}' for x in k]
P = lambda *k: [f'pt:{x}' for x in k]
PANY = 1180

text('Blood transfusion — match it on the bench, then change the unit to fit the patient', 180, 150, 'dyn-big')
text('left: blood bank tubes · right: the unit, the line and the patient · schematic', 180, 176, 'dyn-cap')
# bench
add('<rect x="180" y="260" width="1060" height="1080" rx="30" style="fill:var(--surface-2);stroke:var(--line-2);stroke-width:3"/>')
text('blood bank bench', 210, 300, 'nf-l1')
TUBES = [(360, 'red cells'), (620, 'serum / reagent'), (880, 'Coombs'), (1100, 'result')]
for x, l in TUBES[:3]:
    add(f'<rect x="{x - 60}" y="420" width="120" height="380" rx="50" style="fill:none;stroke:var(--line-2);stroke-width:4"/>')
    text(l, x, 850, 'nf-l2', 'middle')
add('<path d="M420 600 H560 M680 600 H820 M940 600 H1030" style="stroke:var(--ink-3);stroke-width:4;stroke-dasharray:10 8"/>')
add('<circle cx="1100" cy="600" r="90" style="fill:none;stroke:var(--line-2);stroke-width:4"/>')
text('result', 1100, 720, 'nf-l2', 'middle')
CELLS = dict(type="patient's cells", screen='reagent cells (known antigens)', xm="donor's cells", dat="patient's cells")
SER = dict(type='anti-A · anti-B · anti-D sera', screen="patient's serum", xm="patient's serum", dat='(nothing — straight to Coombs)')
for k in CELLS:
    text(CELLS[k], 360, 900, 'nf-l1', 'middle', when=LB(k)); text(SER[k], 640, 940, 'nf-l1', 'middle', when=LB(k))
for i in range(6):
    add(f'<circle cx="{340 + (i % 2) * 40}" cy="{520 + i * 40}" r="16" style="fill:var(--nf-blood);opacity:.7"/>', when=LB('type', 'screen', 'xm', 'dat'))
for i in range(4):
    add(f'<path d="M{600 + (i % 2) * 40} {540 + i * 50} l-14 -20 m14 20 l14 -20 m-14 20 v24" style="fill:none;stroke:var(--dk3);stroke-width:5"/>', when=LB('type', 'screen', 'xm'))
for i in range(3):
    add(f'<path d="M{860 + (i % 2) * 40} {560 + i * 60} l-14 -20 m14 20 l14 -20 m-14 20 v24" style="fill:none;stroke:var(--dk9);stroke-width:5"/>', when=LB('screen', 'xm', 'dat'))
# results: clump vs smooth
for dx, dy in ((-20, -20), (10, -10), (-10, 15), (20, 20), (0, 0)):
    add(f'<circle cx="{1100 + dx}" cy="{600 + dy}" r="16" style="fill:var(--nf-blood);opacity:.85"/>', when=LB('type', 'dat'))
for dx, dy in ((-50, -40), (40, -50), (-40, 50), (50, 40), (0, -60), (0, 60)):
    add(f'<circle cx="{1100 + dx}" cy="{600 + dy}" r="12" style="fill:var(--nf-blood);opacity:.6"/>', when=LB('screen', 'xm'))
LTAG = dict(type='typing: clumps with anti-A only = A, anti-B only = B, both = AB, neither = O · D antigen alone sets Rh',
            screen='antibody screen (indirect): smooth = no unexpected alloantibody from an old transfusion or pregnancy',
            xm='crossmatch: patient serum + the actual donor cells — smooth = compatible unit',
            dat='direct: Coombs reagent on the patient’s own cells — clumps = IgG or C3 already on them (AIHA, hemolytic reaction, HDFN)')
for k, s in LTAG.items(): text(s, 710, 1000, 'nf-l1', 'middle', when=LB(k))
text('anti-A and anti-B appear in infancy without exposure · anti-D only after Rh-positive cells (transfusion, pregnancy)', 710, 1060, 'nf-l2', 'middle')
text('most acute hemolytic reactions are identification errors — wrong patient, mislabeled tube', 710, 1100, 'nf-l2', 'middle')

# unit → line → patient
BX, BY = 1500, 300
add(f'<rect x="{BX}" y="{BY}" width="220" height="300" rx="30" style="fill:var(--nf-blood);fill-opacity:.15;stroke:var(--nf-blood);stroke-width:4"/>')
text('unit', BX + 110, BY - 20, 'nf-l1', 'middle')
text('red cells · plasma', BX + 110, BY + 160, 'nf-l2', 'middle', when=['!pt:plt'])
text('platelets (room temp)', BX + 110, BY + 160, 'nf-l2', 'middle', when=P('plt'))
text('+ citrate (binds Ca²⁺)', BX + 110, BY + 200, 'nf-l2', 'middle')
LINE = f'M{BX + 110} {BY + 300} V{BY + 500} C{BX + 110} {BY + 700} {BX + 400} {BY + 700} {BX + 500} {BY + 760}'
add(f'<path d="{LINE}" style="fill:none;stroke:var(--line-2);stroke-width:10"/>')
PX, PY = 2150, 1060
add(f'<circle cx="{PX}" cy="{PY - 260}" r="80" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--line-2);stroke-width:4"/>')
add(f'<rect x="{PX - 130}" y="{PY - 170}" width="260" height="380" rx="80" style="fill:var(--dk2);fill-opacity:.1;stroke:var(--line-2);stroke-width:4"/>')
text('patient', PX, PY + 250, 'nf-l1', 'middle')
# contents of the unit
for i, (x, y) in enumerate(((BX + 50, BY + 60), (BX + 160, BY + 90), (BX + 80, BY + 240))):
    add(f'<circle cx="{x}" cy="{y}" r="20" style="fill:none;stroke:var(--dk9);stroke-width:5"/>', when=P('feb', 'ic'))
text('donor white cells', BX + 240, BY + 60, 'nf-l2', when=P('feb', 'ic'))
text('IgA in donor plasma', BX + 240, BY + 60, 'nf-l2', when=P('iga'))
text('bacteria (skin flora)', BX + 240, BY + 60, 'nf-l2', when=P('plt'))
text('lysed old cells → K⁺', BX + 240, BY + 60, 'nf-l2', when=P('mt'))
add(f'<path d="M{BX + 20} {BY + 20} L{BX + 200} {BY + 280}" style="stroke:var(--ok);stroke-width:10;opacity:.7"/>', when=['fix&pt:feb', 'fix&pt:ic', 'fix&pt:iga'])
# Rh mother
add(f'<circle cx="{PX}" cy="{PY + 50}" r="70" style="fill:var(--dk11);fill-opacity:.2;stroke:var(--dk11);stroke-width:4"/>', when=P('rh'))
text('Rh+ fetus', PX + 90, PY + 60, 'nf-l2', when=P('rh'))
PTAG = dict(feb='febrile nonhemolytic reaction last time — cytokines from donor white cells built up in storage',
            ic='immunocompromised — donor T cells could engraft and attack the host (transfusion-associated GVHD)',
            iga='IgA-deficient with anti-IgA — donor IgA triggers anaphylaxis',
            mt='massive transfusion — citrate binds Ca²⁺ (tetany), old cells leak K⁺, platelets diluted, volume overload (TACO)',
            plt='platelet unit — stored at room temperature, the usual home of bacterial contamination (~1 in 5000): fever, chills, hypotension',
            rh='Rh(D)-negative mother — Rh+ fetal cells cross at delivery or bleeding; her B cells could make anti-D')
for k, s in PTAG.items(): text(s, 1800, 1480, 'nf-l1 dyn-tag', 'middle', when=P(k))
FTAG = dict(feb='leukoreduced unit — fewer white cells, no fever', ic='irradiated unit — donor T cells cannot divide',
            iga='IgA-free (IgA-deficient donor) product', rh='Rho(D) immune globulin at ~28 wk and within 72 h of an Rh+ birth — clears fetal cells first',
            mt='give calcium · watch K⁺ · add platelets', plt='stop the unit, culture, start broad-spectrum antibiotics')
for k, s in FTAG.items(): text(s, 1800, 1520, 'nf-l1', 'middle', when=[f'fix&pt:{k}'])

# ════════ motion ════════
flows = [dict(d=LINE, len=900, speed=110, r=10, base=dict(rbc=4)),
         dict(d=LINE, len=900, speed=110, r=8, base=dict(wbc=2), when=['pt:feb&!fix', 'pt:ic&!fix']),
         dict(d=LINE, len=900, speed=110, r=8, base=dict(bug=3), when=['pt:plt&!fix']),
         dict(d=LINE, len=900, speed=150, r=7, base=dict(ion=4), when=P('mt')),
         dict(d=f'M{PX} {PY + 50} C{PX - 100} {PY - 100} {PX - 60} {PY - 200} {PX} {PY - 120}', len=400, speed=60, r=8,
              base=dict(rbc=2), when=P('rh')),
         dict(d=f'M{PX - 100} {PY - 120} C{PX - 200} {PY} {PX - 120} {PY + 80} {PX - 60} {PY + 60}', len=300, speed=60, r=7,
              base=dict(ab=3), when=['pt:rh&!fix']),
         dict(d='M420 600 H1020', len=600, speed=100, r=7, base=dict(rbc=2), when=LB('type', 'screen', 'xm', 'dat'))]
sites = [dict(x=1100, y=470, n=[1, -1], w=10, t='rec', l='', aria='Antiglobulin (Coombs) test', c='antiglobulin', ions=[]),
         dict(x=230, y=420, n=[-1, -1], w=10, t='rec', l='', aria='Pretransfusion testing', c='pretransfuse', ions=[]),
         dict(x=PX + 200, y=PY + 120, n=[1, 1], w=10, t='rec', l='', aria='Rho(D) immune globulin', c='rhig', ions=[]),
         dict(x=BX - 60, y=BY + 120, n=[-1, -1], w=10, t='rec', l='', aria='Modified blood products', c='prodmod', ions=[]),
         dict(x=BX + 300, y=BY + 640, n=[1, 1], w=10, t='rec', l='', aria='Massive transfusion', c='massivetx', ions=[]),
         dict(x=BX - 60, y=BY + 420, n=[-1, 1], w=10, t='rec', l='', aria='Transfusion-transmitted infection', c='txinfect', ions=[])]

readouts = [
  dict(l='Reaction risk', mods=[dict(when=['pt:feb&!fix', 'pt:ic&!fix', 'pt:iga&!fix', 'pt:plt&!fix'], d=1),
                                dict(when=['pt:feb&fix', 'pt:ic&fix', 'pt:iga&fix'], d=-1)]),
  dict(l='Ionized Ca²⁺', mods=[dict(when=['pt:mt&!fix'], d=-1)]),
  dict(l='K⁺', mods=[dict(when=P('mt'), d=1)]),
  dict(l='Platelets', mods=[dict(when=['pt:mt&!fix'], d=-1)]),
  dict(l='Maternal anti-D', mods=[dict(when=['pt:rh&!fix'], d=1), dict(when=['pt:rh&fix'], d=-1)]),
]

notes = {
  '': 'Before red cells are hung, donor and recipient are ABO and Rh typed and the recipient’s serum meets reagent cells and then the '
      'donor’s own cells. Coombs reagent (anti-human globulin) links antibody-coated cells so they clump: direct = antibody on the '
      'patient’s cells, indirect = antibody free in the serum.',
  'lab:type': 'Typing: red cells against anti-A and anti-B sera. The D antigen alone decides Rh positive. Plasma runs the other way: AB '
              'plasma can go to anyone, and a type O recipient can take any plasma.',
  'lab:screen': 'Antibody screen = an indirect antiglobulin test: the patient’s serum against reagent cells of known antigens finds '
                'alloantibodies from an earlier transfusion or pregnancy; it also detects maternal anti-D.',
  'lab:xm': 'Crossmatch: recipient serum against the actual donor cells; no agglutination means compatible. Warm AIHA autoantibodies make '
            'a compatible crossmatch hard to find.',
  'lab:dat': 'Direct antiglobulin test: positive in warm AIHA (IgG), cold agglutinin disease (C3), drug-induced hemolysis (penicillin, '
             'cephalosporins, α-methyldopa), hemolytic transfusion reactions and the infant in HDFN. Febrile, TRALI and anaphylactic '
             'reactions are DAT negative.',
  'pt:feb': 'Febrile nonhemolytic reactions come from cytokines that build up from donor white cells in storage — leukoreduce after a first one.',
  'pt:ic': 'Transfusion-associated GVHD: donor T cells attack an immunocompromised host — irradiate the unit.',
  'pt:iga': 'IgA-deficient patients with anti-IgA antibodies can have anaphylaxis — give IgA-free products.',
  'pt:mt': 'Massive transfusion: citrate in stored blood binds Ca²⁺ faster than the liver clears it → tetany; old lysed cells add K⁺; '
           'platelets are diluted; the volume can overload the circulation (TACO).',
  'pt:plt': 'Platelets are stored at room temperature, so skin bacteria from collection grow — up to ~1 in 5000 platelet transfusions. Viral '
            'risk per unit is about 1 in a million (HBV, HCV, HIV); hepatitis C is the classic transfusion virus; CMV can also pass.',
  'pt:rh': 'Rho(D) immune globulin is passive anti-D IgG given to an unsensitized Rh(D)-negative mother: ~28 weeks, within 72 h after an '
           'Rh-positive birth, and after miscarriage, abortion, ectopic, trauma or bleeding. Useless once she already makes anti-D.',
}

dyn = dict(
  kinds=dict(rbc=['cell', '--nf-blood'], wbc=['cell', '--dk9'], bug=['bad', '--bad'], ion=['ion', '--dk7'], ab=['bad', '--dk3']),
  groups=[['cell', 'Red & white cells'], ['bad', 'Bacteria · antibody'], ['ion', 'Citrate · K⁺']],
  switches=[dict(id='lab', label='Bench test', type='one', options=[
              ['type', 'ABO & Rh typing', 'pretransfuse'], ['screen', 'Antibody screen (IAT)', 'antiglobulin'],
              ['xm', 'Crossmatch', 'pretransfuse'], ['dat', 'Direct antiglobulin (DAT)', 'antiglobulin']]),
            dict(id='pt', label='Patient · unit', type='one', options=[
              ['feb', 'Fever last time', 'prodmod'], ['ic', 'Immunocompromised', 'prodmod'], ['iga', 'IgA-deficient', 'prodmod'],
              ['mt', 'Massive transfusion', 'massivetx'], ['plt', 'Platelet unit', 'txinfect'], ['rh', 'Rh-negative mother', 'rhig']]),
            dict(id='fix', label='Answer', type='toggle', on='Fixed', off='Apply the fix', def_=False)],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 14 · Guyton ch 36–37 · Katzung ch 55')
for s in dyn['switches']:
    if 'def_' in s: s['def'] = s.pop('def_')

MAP = dict(
  id='tfsim', title='Blood Transfusion in Motion', topic='heme', after='transfuse',
  sub='Run typing, the screen, the crossmatch and the Coombs tests on the bench, then hang a unit for a patient who needs it changed — '
      'leukoreduced, irradiated, IgA-free — or a massive transfusion, a platelet unit, or an Rh-negative mother',
  w=3600, h=1900,
  fa='110, 112, 117, 162, 170, 249, 411, 416, 434, 731',
  src=['Robbins ch 14 — Red blood cell and bleeding disorders', 'Guyton ch 36 — Blood Types, Transfusion, and Tissue and Organ Transplantation',
       'Guyton ch 37 — Hemostasis and Blood Coagulation', 'Katzung ch 55 — Immunopharmacology'],
  lanes=[('tsLab', 'Bench tests', 'tca'), ('tsUnit', 'The unit & patient', 'glycolysis')],
  nodes=[
    ('ts1', 'Pretransfusion testing', 280, 1720, 'tsLab', 'type · screen · crossmatch', ['pretransfuse'], 'hub'),
    ('ts2', 'Coombs: direct vs indirect', 680, 1720, 'tsLab', 'on cells · in serum', ['antiglobulin']),
    ('ts3', 'Modified blood products', 1080, 1720, 'tsUnit', 'leuko · irradiated · IgA-free', ['prodmod']),
    ('ts4', 'Massive transfusion', 1480, 1720, 'tsUnit', '↓Ca²⁺ ↑K⁺ ↓plt', ['massivetx']),
    ('ts5', 'Transfusion infection', 1880, 1720, 'tsUnit', 'platelets · HCV', ['txinfect']),
    ('ts6', 'Rho(D) immune globulin', 2280, 1720, 'tsUnit', 'Rh− mother', ['rhig'])],
  panels=[
    (2500, PANY, 1000, 'Change the unit (Robbins ch 14)', [
      ('Fever last time', 'leukoreduce'), ('Immunocompromised', 'irradiate'), ('IgA-deficient', 'IgA-free product'),
      ('Rh− mother', 'Rho(D) immune globulin')])],
  dyn=dyn)
