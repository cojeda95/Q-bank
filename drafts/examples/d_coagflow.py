# m39 — Coagulation Cascade in Motion (dynamic map, kit data)
# The injured vessel wall (vWF + platelets, tissue factor), the intrinsic arm (XII → XI → IX with VIII), the extrinsic
# arm (tissue factor + VIIa), the common path (X with V → thrombin → fibrin, XIII cross-links), the brakes
# (antithrombin, proteins C and S, tPA → plasmin) and the liver's vitamin K cycle. Activated factors flow down as
# particles. Two `one` switches — an anticoagulant and a disorder — block or turn down the right factors and read out
# PT, PTT, bleeding time, platelet count and D-dimer as First Aid's coagulation tables give them.
# Sources: First Aid 2025 pp. 417–419, 431–433, 440–442 · Katzung ch 34 · Robbins ch 4, 14, 18 ·
# Bootcamp Hematology & Oncology (Coagulation and Fibrinolysis).
import sys
sys.path.insert(0, '/Users/Alonso/Developer/atlas-review/batches/m18')
from common import full

KZ34, RB4, RB14, RB18 = full('Katzung', 34), full('Robbins', 4), full('Robbins', 14), full('Robbins', 18)
BC = 'Bootcamp.com Hematology & Oncology — Coagulation and Fibrinolysis'

shapes = []
def add(svg, when=None, unless=None):
    if when is None and unless is None: shapes.append(svg)
    else:
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

D = lambda *k: ['rx:' + x for x in k]      # drugs
Z = lambda *k: ['dz:' + x for x in k]      # disorders
TAG = 'nf-l2 dyn-tag'

# columns: intrinsic 380 · common 1000 · extrinsic 1560 · brakes 2000; labels sit to the right of each icon
XI_, XC, XE, XB = 380, 1000, 1560, 2000
WALL = 200

# ════════ 1. the injured vessel wall, vWF and platelets ════════
shapes.append(dict(membrane=f'M160 {WALL} H2440', w=24))
text('Injured vessel wall — collagen, vWF and tissue factor exposed', 180, 160, 'dyn-cap')
text('Blood', 180, 330, 'dyn-cap')
PLT = [(560, 252), (612, 262), (664, 250), (716, 264), (768, 252), (586, 286), (640, 290), (694, 288), (746, 290)]
plt = lambda pts, cls='dyn-soft': ''.join(f'<ellipse cx="{x}" cy="{y}" rx="24" ry="11" class="{cls}" style="stroke:var(--dk9)"/>' for x, y in pts)
add(plt(PLT), unless=Z('dic', 'liver', 'vwd'))
add(plt(PLT[:4]), when=Z('dic', 'liver'))
add(plt(PLT[:5]) + plt(PLT[5:], 'dyn-soft dyn-dim'), when=Z('vwd'))
text('platelet plug', 820, 262, 'nf-l2')
text('fewer platelets', 820, 282, TAG, when=Z('dic', 'liver'))
text('platelets can’t stick', 820, 282, TAG, when=Z('vwd'))

# ════════ 2. the cascade ════════
# vitamin K–dependent factors carry a "K" badge (FA p. 419)
def kbadge(x, y):
    return (f'<circle cx="{x - 22}" cy="{y}" r="11" style="fill:var(--dk10);stroke:var(--surface);stroke-width:2"/>'
            f'<text x="{x - 22}" y="{y + 4}" text-anchor="middle" style="font:700 11px var(--font-ui);fill:var(--surface)">K</text>')
KDEP = [(XI_, 680), (XE, 530), (XC, 900), (XC, 1040), (XB, 1100)]
add(''.join(kbadge(x, y) for x, y in KDEP))
add(''.join(f'<circle cx="{x - 22}" cy="{y}" r="16" class="dyn-hl"/>' for x, y in KDEP), when=D('warf') + Z('vitk'))
text('K = vitamin K–dependent', 180, 1080, 'nf-l2')

# cofactor connectors (dashed): VIIIa joins the intrinsic tenase, Va joins prothrombinase
add(f'<path d="M653 782 V816" class="dyn-dash"/><path d="M1300 990 H1030" class="dyn-dash"/>')
text('intrinsic tenase: IXa + VIIIa', 470, 812, 'dyn-cap')
text('extrinsic tenase: VIIa + tissue factor', 1180, 812, 'dyn-cap')
text('prothrombinase: Xa + Va', 1100, 1078, 'dyn-cap')

# the fibrin clot
MESH = ''.join(f'<path d="M{870 + i * 40} 1440 L{950 + i * 40} 1540" class="dyn-line" style="stroke:var(--dk3)"/>' for i in range(6)) + \
       ''.join(f'<path d="M{950 + i * 40} 1440 L{870 + i * 40} 1540" class="dyn-line" style="stroke:var(--dk3)"/>' for i in range(6))
add(MESH, unless=D('tpa'))
add(f'<g class="dyn-dim">{MESH}</g>', when=D('tpa'))
text('Stable fibrin clot', 1140, 1486, 'nf-l1')
text('the platelet plug, reinforced', 1140, 1502, 'nf-l2')
text('clot being dissolved', 1140, 1522, TAG, when=D('tpa'))
text('microthrombi everywhere — then bleeding', 1140, 1522, TAG, when=Z('dic'))

# the liver's vitamin K cycle (FA p. 419)
add('<rect class="dyn-soft" x="170" y="1130" width="640" height="250" rx="22"/>')
text('Liver', 190, 1162, 'dyn-big')
text('makes most factors (VIII comes from endothelium)', 190, 1184, 'nf-l2')

# brakes labels
text('THE BRAKES', XB - 20, 836, 'nf-h')

# ════════ 3. factors, cofactors and brakes as tap targets ════════
sites = []
def fac(x, y, l, s, c, **kw):
    sites.append(dict(dict(x=x, y=y, n=[1, 0], w=20, t='rec', l=l, s=s, ions=[], c=c), **kw))
fac(XI_, 380, 'XII → XIIa', 'contact activation (Hageman factor)', 'coagreg', low=Z('liver'))
fac(XI_, 530, 'XI → XIa', 'missing in hemophilia C', 'factorxi', low=Z('liver'), need=['!dz:hemc'], closed='missing')
fac(XI_, 680, 'IX → IXa', 'Christmas factor', 'hemophilia', low=D('warf') + Z('vitk', 'liver'), need=['!dz:hemb'], closed='missing')
fac(640, 760, 'VIII → VIIIa', 'cofactor · carried by vWF', 'hemophilia', low=Z('vwd', 'dic'), need=['!dz:hema'], closed='missing')
fac(XE, 530, 'VII → VIIa', 'binds tissue factor · shortest half-life', 'coagreg', low=D('warf') + Z('vitk', 'liver'))
fac(XC, 900, 'X → Xa', 'the two arms meet here', 'doac', block=D('xa'), low=['rx:warf', 'rx:ufh&!dz:atd', 'rx:lmwh&!dz:atd'] + Z('vitk', 'liver'))
fac(1300, 990, 'V → Va', 'cofactor for Xa', 'factorv', low=Z('dic', 'liver'), boost=Z('fvl', 'protc'))
fac(XC, 1040, 'II → IIa (thrombin)', 'prothrombin · also activates V, VIII, XI, XIII', 'doac', block=D('dti'),
    low=['rx:warf', 'rx:ufh&!dz:atd'] + Z('vitk', 'liver'), boost=Z('fvl', 'atd', 'protc'))
fac(XC, 1180, 'I → Ia (fibrin)', 'fibrinogen, cut by thrombin', 'dic', low=Z('dic', 'liver'))
fac(XC, 1320, 'XIII → XIIIa', 'cross-links the fibrin mesh', 'coagreg')
fac(XB, 900, 'Antithrombin', '⊣ thrombin and Xa (also IXa, XIa, XIIa)', 'heparin', boost=D('ufh', 'lmwh'), need=['!dz:atd'], closed='missing')
fac(XB, 1100, 'Protein C + protein S', '⊣ Va and VIIIa · activated via thrombin', 'factorv', low=D('warf') + Z('vitk', 'liver'),
    need=['!dz:protc'], closed='missing')
fac(XB, 1320, 'tPA → plasmin', 'cuts fibrin → D-dimer', 'tpa', boost=D('tpa') + Z('dic'))
sites.append(dict(x=300, y=1290, n=[1, 0], w=20, t='ex', l='Vitamin K epoxide reductase', s='recycles vitamin K so II, VII, IX, X, C, S get γ-carboxylated',
                  ions=[], c='warfarin', block=D('warf'), need=['!dz:vitk'], closed='no vitamin K', low=Z('liver')))
# the wall: vWF bridges collagen to platelets; tissue factor starts the extrinsic arm
sites.append(dict(x=XI_, y=WALL, n=[0, 1], w=24, t='rec', l='vWF', s='collagen → platelet GpIb', ions=[], c='vwd',
                  need=['!dz:vwd'], closed='low'))
sites.append(dict(x=XE, y=WALL, n=[0, 1], w=24, t='rec', l='Tissue factor (III)', s='starts the extrinsic arm', ions=[], c='coagreg'))

# ════════ 4. what flows ════════
K = lambda *k: k
def flow(d, ln, base, mods=(), speed=110, when=None):
    f = dict(d=d, len=ln, speed=speed, base=base, mods=[dict(when=w, **m) for w, m in mods])
    if when: f['when'] = when
    return f
LIVER, VITK = Z('liver'), Z('vitk')
flows = [
  # intrinsic: XIIa → XI → IX → (with VIIIa) X
  flow(f'M{XI_ + 13} 402 V508', 106, dict(intr=2), [(LIVER, dict(set=dict(intr=1)))]),
  flow(f'M{XI_ + 13} 552 V658', 106, dict(intr=2), [(LIVER, dict(set=dict(intr=1))), (Z('hemc'), dict(set=dict(intr=0)))]),
  flow(f'M{XI_ + 13} 702 V780 Q{XI_ + 13} 820 {XI_ + 53} 820 H{XC - 27} Q{XC + 13} 820 {XC + 13} 868', 718, dict(intr=5),
       [(D('warf') + VITK + LIVER, dict(set=dict(intr=2))), (Z('hema', 'hemb'), dict(set=dict(intr=0))), (Z('vwd'), dict(set=dict(intr=3)))]),
  # extrinsic: tissue factor → VII → X
  flow(f'M{XE + 13} 296 V508', 212, dict(extr=2)),
  flow(f'M{XE + 13} 552 V780 Q{XE + 13} 820 {XE - 27} 820 H{XC + 53} Q{XC + 13} 820 {XC + 13} 868', 640, dict(extr=4),
       [(D('warf') + VITK + LIVER, dict(set=dict(extr=1)))]),
  # common: Xa → II, thrombin → I, fibrin → XIII → clot
  flow(f'M{XC + 13} 922 V1018', 96, dict(xa=2), [(D('xa'), dict(set=dict(xa=0))), (['rx:warf', 'rx:ufh&!dz:atd', 'rx:lmwh&!dz:atd'] + VITK + LIVER, dict(set=dict(xa=1)))]),
  flow(f'M{XC + 13} 1062 V1158', 96, dict(thr=2), [(D('dti', 'xa'), dict(set=dict(thr=0))), (['rx:warf', 'rx:ufh&!dz:atd', 'rx:lmwh&!dz:atd'] + VITK + LIVER, dict(set=dict(thr=1))),
                                                   (Z('fvl', 'atd', 'protc'), dict(set=dict(thr=4)))]),
  flow(f'M{XC + 13} 1202 V1298', 96, dict(fib=2), [(D('dti', 'xa'), dict(set=dict(fib=0))), (Z('fvl', 'atd', 'protc'), dict(set=dict(fib=3)))]),
  flow(f'M{XC + 13} 1342 V1430', 88, dict(fib=2), [(D('dti', 'xa', 'tpa'), dict(set=dict(fib=0)))]),
  # the brakes
  flow(f'M{XB} 920 H1380', 620, dict(at=2), [(D('ufh', 'lmwh'), dict(set=dict(at=6))), (Z('atd'), dict(set=dict(at=0)))]),
  flow(f'M{XB} 1120 H1640 Q1600 1120 1600 1080 V1000', 600, dict(apc=2), [(Z('protc', 'fvl'), dict(set=dict(apc=0)))]),
  flow(f'M{XB} 1340 V1400 Q{XB} 1440 {XB - 40} 1440 H1330 Q1290 1440 1290 1480 H1240', 900, dict(pl=1),
       [(D('tpa') + Z('dic'), dict(set=dict(pl=5)))]),
]
# draw each flow's track under its particles
COL = dict(intr=('--dk1', 'cfIntr'), extr=('--dk5', 'cfExtr'), xa=('--dk4', 'cfCommon'), thr=('--dk2', 'cfCommon'), fib=('--dk3', 'cfCommon'),
           at=('--dk6', 'cfBrake'), apc=('--dk7', 'cfBrake'), pl=('--dk10', 'cfBrake'))
for f in flows:
    k = next(iter(f['base'])); col, lane = COL[k]
    shapes.insert(1, f'<path d="{f["d"]}" class="dyn-line" style="stroke:var({col});stroke-width:3.5;opacity:.45" marker-end="url(#ah-{lane})"/>')
text('INTRINSIC ARM — the PTT', XI_ - 40, 345, 'nf-h')
text('EXTRINSIC ARM — the PT', XE - 40, 345, 'nf-h')
text('COMMON PATH — PT and PTT', XC + 90, 870, 'nf-h')
text('antithrombin ⊣ Xa and thrombin', 1400, 940, 'dyn-cap')
text('heparin speeds it ~1000×', 1400, 958, TAG, when=D('ufh', 'lmwh'), unless=Z('atd'))
text('no antithrombin — heparin has nothing to work through', 1400, 958, TAG, when=['dz:atd&rx:ufh', 'dz:atd&rx:lmwh'])
text('no antithrombin', 1400, 958, TAG, when=Z('atd'), unless=D('ufh', 'lmwh'))
text('activated protein C ⊣ Va', 1620, 1104, 'dyn-cap')
text('Va resists protein C', 1620, 1140, TAG, when=Z('fvl'))
text('no protein C or S', 1620, 1140, TAG, when=Z('protc'))
text('plasmin → fibrin split products (D-dimer)', 1340, 1432, 'dyn-cap')

# drug / disorder tags on the drawing
text('synthesis blocked', XI_ + 56, 712, TAG, when=D('warf') + Z('vitk'))
text('none made', XI_ + 56, 712, TAG, when=Z('hemb'))
text('none made', 696, 792, TAG, when=Z('hema'))
text('unprotected — falls', 696, 792, TAG, when=Z('vwd'))
text('no XI', XI_ + 56, 562, TAG, when=Z('hemc'))

# ════════ 5. readouts — First Aid pp. 431–433, 441–442; Bootcamp table; Katzung ch 34; Robbins ch 14, 18 ════════
R = lambda l, *m: dict(l=l, mods=[dict(when=w, d=d) for w, d in m])
readouts = [
  R('PT', (D('warf'), 1), (D('tpa'), 1), (Z('hema', 'hemb', 'hemc', 'vwd', 'atd'), 0), (Z('vitk', 'dic', 'liver'), 1)),
  R('PTT', (D('ufh', 'dti', 'tpa'), 1), (Z('hema', 'hemb', 'hemc', 'vitk', 'vwd', 'dic', 'liver'), 1), (Z('atd'), 0), (['dz:atd&rx:ufh'], -1)),
  R('Bleeding time', (Z('hema', 'hemb', 'hemc', 'vitk'), 0), (Z('vwd', 'dic'), 1)),
  R('Platelet count', (D('tpa'), 0), (Z('hema', 'hemb', 'hemc', 'vwd'), 0), (Z('dic', 'liver'), -1)),
  R('D-dimer', (Z('hema', 'hemb', 'hemc', 'vwd'), 0), (Z('dic'), 1))]

notes = {
  'rx:warf': 'Warfarin blocks vitamin K epoxide reductase, so II, VII, IX, X, C and S leave the liver uncarboxylated and inactive. VII has the shortest half-life, so the PT/INR rises first; protein C falls before II and X — an early clotting window (skin necrosis), so bridge with heparin. Crosses the placenta. Reverse: vitamin K (slow), PCC or FFP (fast).',
  'rx:ufh': 'Unfractionated heparin makes antithrombin work far faster against thrombin and Xa. Immediate onset; monitor the PTT; safe in pregnancy. Reverse with protamine sulfate. HIT type 2 (day 5–10): IgG against heparin–PF4 → platelets fall while clots form — stop heparin, start argatroban.',
  'rx:lmwh': 'LMWH (enoxaparin, dalteparin) also works through antithrombin but mainly against Xa; fondaparinux acts only on Xa. No routine monitoring (anti-Xa levels in renal failure, obesity, pregnancy); renally cleared, so caution in renal insufficiency. Protamine reverses LMWH only partly and fondaparinux not at all. Fondaparinux is safe in HIT.',
  'rx:xa': 'Direct Xa inhibitors (apixaban, rivaroxaban, edoxaban — “xa-ban”) bind Xa itself, no antithrombin needed. Oral; no routine lab monitoring. DVT/PE and stroke prevention in nonvalvular atrial fibrillation. Reverse with andexanet alfa.',
  'rx:dti': 'Direct thrombin inhibitors (dabigatran oral; argatroban, bivalirudin IV) bind thrombin directly — used in HIT. Argatroban is followed by the PTT; dabigatran prolongs the PTT but needs no routine monitoring. Reverse dabigatran with idarucizumab.',
  'rx:tpa': 'Thrombolytics (alteplase, reteplase, tenecteplase) turn plasminogen into plasmin, which cuts the fibrin of a formed clot: PT and PTT rise, platelet count does not change. Early MI, early ischemic stroke, high-risk PE. Contraindicated with active bleeding, past intracranial bleed, recent surgery, severe hypertension. Reverse: aminocaproic or tranexamic acid, cryoprecipitate, FFP, PCC.',
  'dz:hema': 'Hemophilia A — factor VIII deficiency, X-linked recessive: the intrinsic tenase fails, so PTT ↑ with a normal PT, platelet count and bleeding time; a mixing study corrects. Deep bleeds — hemarthrosis, muscle hematomas, bleeding after surgery or dental work. Treat: factor VIII, desmopressin (mild), emicizumab.',
  'dz:hemb': 'Hemophilia B (Christmas disease) — factor IX deficiency, X-linked recessive: clinically identical to hemophilia A, PTT ↑ with a normal PT; only a factor assay tells them apart. Treat with factor IX concentrate (desmopressin does not help).',
  'dz:hemc': 'Hemophilia C — factor XI deficiency, autosomal recessive (so girls are affected too): PTT ↑ with a normal PT; a mixing study corrects. Treat with factor XI concentrate.',
  'dz:vitk': 'Vitamin K deficiency — II, VII, IX, X, C and S are not γ-carboxylated: PT and PTT both rise, bleeding time stays normal. Newborns (sterile gut — hence the injection at birth), broad-spectrum antibiotics, fat malabsorption. Vitamin K corrects it (unlike liver failure).',
  'dz:vwd': 'von Willebrand disease — the most common inherited bleeding disorder, mostly autosomal dominant. Low vWF: platelets can’t adhere (bleeding time ↑, count normal) and factor VIII loses its carrier (PTT normal or ↑; PT normal). Mucosal bleeding — epistaxis, menorrhagia. Ristocetin test abnormal. Treat: desmopressin, vWF concentrates.',
  'dz:dic': 'DIC — widespread activation consumes platelets and factors (↓ fibrinogen, ↓ V and VIII) while plasmin works overtime: platelets ↓, bleeding time, PT and PTT ↑, D-dimer ↑, schistocytes. Clots and bleeds at once. Causes: sepsis, trauma, obstetric complications, pancreatitis, malignancy, snake bite, heat stroke, transfusion. Treat the cause.',
  'dz:liver': 'Liver failure — hepatocytes stop making fibrinogen, II, V, VII, IX, X, XI, XII and proteins C and S (VIII is made by endothelium): PT ↑ first (VII), then PTT ↑. Portal hypertension sequesters platelets in a big spleen (platelets ↓). Vitamin K doesn’t correct it.',
  'dz:fvl': 'Factor V Leiden — the commonest inherited thrombophilia: a point mutation (Arg506Gln) leaves Va resistant to activated protein C, so the brake on prothrombinase fails and thrombin keeps forming. DVT, cerebral vein thrombosis, recurrent pregnancy loss. Autosomal dominant. A clotting problem, not a bleeding one.',
  'dz:atd': 'Antithrombin deficiency — thrombin and Xa run unchecked: venous clots. No effect on PT or PTT, but heparin barely raises the PTT (heparin works only through antithrombin) — add heparin to see it. Inherited, or lost in the urine in nephrotic syndrome. Direct thrombin inhibitors still work.',
  'dz:protc': 'Protein C or S deficiency — Va and VIIIa can’t be switched off, so clots form. Starting warfarin drops protein C before II and X (shorter half-life): warfarin-induced skin necrosis — bridge with heparin. Protein C Cancels, protein S Stops coagulation.',
  '': 'Injury exposes tissue factor and collagen: the extrinsic arm (VIIa + tissue factor, measured by the PT) and the intrinsic arm (XII → XI → IX with VIII, measured by the PTT) both activate X; Xa with Va turns prothrombin into thrombin, thrombin turns fibrinogen into fibrin, XIIIa cross-links it. Pick a drug or a disorder. Tap any factor for its card.'}

dyn = dict(
  kinds=dict(intr=['intr', '--dk1'], extr=['extr', '--dk5'], xa=['common', '--dk4'], thr=['common', '--dk2'], fib=['fib', '--dk3'],
             at=['brake', '--dk6'], apc=['brake', '--dk7'], pl=['brake', '--dk10']),
  groups=[['intr', 'Intrinsic (PTT)'], ['extr', 'Extrinsic (PT)'], ['common', 'Xa · thrombin'], ['fib', 'Fibrin'], ['brake', 'Antithrombin · protein C · plasmin']],
  switches=[dict(id='rx', label='Add one anticoagulant', type='one',
                 options=[['warf', 'Warfarin'], ['ufh', 'Heparin (unfractionated)'], ['lmwh', 'LMWH · fondaparinux'], ['xa', 'Direct Xa inhibitor'],
                          ['dti', 'Direct thrombin inhibitor'], ['tpa', 'tPA (thrombolytic)']]),
            dict(id='dz', label='Pick one disorder', type='one',
                 options=[['hema', 'Hemophilia A'], ['hemb', 'Hemophilia B'], ['hemc', 'Hemophilia C'], ['vitk', 'Vitamin K deficiency'], ['vwd', 'von Willebrand disease'],
                          ['dic', 'DIC'], ['liver', 'Liver failure'], ['fvl', 'Factor V Leiden'], ['atd', 'Antithrombin deficiency'], ['protc', 'Protein C or S deficiency']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2520, y=110, w=1000),
  src='First Aid pp. 417–419, 431–433, 440–442 · Katzung ch 34 · Robbins ch 4, 14, 18 · Bootcamp Heme/Onc')

MAP = dict(
  id='coagflow', title='Coagulation Cascade in Motion', topic='heme', after='hemostasis',
  sub='Tissue factor and contact activation start two arms that meet at factor X — thrombin makes fibrin while antithrombin, protein C '
      'and plasmin hold it back. Add an anticoagulant or pick a disorder to see which factors fail and what the PT, PTT, bleeding time and '
      'platelet count do. Tap a factor for its card',
  w=3600, h=1700,
  fa='417–419, 431–433, 440–442', src=[KZ34, RB4, RB14, RB18, BC],
  lanes=[('cfIntr', 'Intrinsic arm', 'glycolysis'), ('cfExtr', 'Extrinsic arm', 'glycogen'), ('cfCommon', 'Common path', 'ppp'),
         ('cfBrake', 'The brakes', 'sugars')],
  nodes=[
    ('cf1', 'Hemophilia A · B · C', 760, 380, 'cfIntr', 'VIII · IX · XI', ['hemophilia', 'factorxi']),
    ('cf2', 'PT vs PTT', 700, 960, 'cfIntr', 'which arm is broken', ['coagreg']),
    ('cf11', 'Tissue factor + VIIa', 1880, 640, 'cfExtr', 'the in-vivo starter', ['coagreg']),
    ('cf3', 'von Willebrand disease', 1080, 262, 'cfIntr', 'vWF carries VIII', ['vwd']),
    ('cf4', 'Warfarin · low vitamin K', 470, 1350, 'cfIntr', 'II, VII, IX, X, C, S', ['warfarin', 'vitkdef']),
    ('cf5', 'Liver disease', 640, 1170, 'cfIntr', 'PT first', ['liverdz']),
    ('cf6', 'Direct Xa / IIa inhibitors', 1480, 1230, 'cfCommon', 'no antithrombin needed', ['doac', 'anticoagrev']),
    ('cf7', 'DIC', 1500, 1530, 'cfCommon', 'consumes everything', ['dic']),
    ('cf8', 'Heparin · LMWH', 2200, 830, 'cfBrake', 'antithrombin ×1000', ['heparin']),
    ('cf9', 'Thrombophilias', 2260, 1210, 'cfBrake', 'Leiden · protein C/S · AT', ['factorv']),
    ('cf10', 'tPA · antifibrinolytics', 2220, 1420, 'cfBrake', 'tPA ↔ tranexamic acid', ['tpa', 'txadrug'])],
  panels=[
    (2520, 720, 1000, 'Coagulation tests (First Aid p. 431)', [
      ('PT', 'extrinsic + common path: I, II, V, VII, X · INR follows warfarin'),
      ('PTT', 'intrinsic + common path: every factor except VII and XIII · heparin'),
      ('Bleeding time', 'the platelet plug — platelets and vWF (Bootcamp)'),
      ('Mixing study', 'corrects = factor deficiency · fails to correct = inhibitor'),
      ('Thrombin time', 'fibrinogen → fibrin · ↑ with anticoagulants, DIC, liver disease')]),
    (2520, 916, 1000, 'Bleeding disorders at a glance (First Aid pp. 431–433; Bootcamp)', [
      ('Hemophilia A, B, C', 'PT normal · PTT ↑ · platelet count and bleeding time normal'),
      ('Vitamin K deficiency', 'PT ↑ · PTT ↑ · bleeding time normal'),
      ('von Willebrand disease', 'PT normal · PTT normal or ↑ · bleeding time ↑ · count normal'),
      ('DIC', 'PT ↑ · PTT ↑ · bleeding time ↑ · count ↓ · D-dimer ↑, fibrinogen ↓'),
      ('TTP / HUS', 'count ↓ but PT and PTT normal — factors are not consumed')]),
    (2520, 1112, 1000, 'Anticoagulants — monitor and reverse (First Aid pp. 440–442)', [
      ('Unfractionated heparin', 'PTT · protamine sulfate'),
      ('LMWH · fondaparinux', 'no routine monitoring · not easily reversed'),
      ('Warfarin', 'PT/INR · vitamin K (slow), PCC or FFP (fast)'),
      ('Dabigatran', 'no routine monitoring · idarucizumab'),
      ('Apixaban, rivaroxaban', 'no routine monitoring · andexanet alfa'),
      ('Thrombolytics', 'aminocaproic or tranexamic acid, platelets, cryo, FFP, PCC')]),
    (2520, 1330, 1000, 'Heparin vs warfarin (First Aid p. 441)', [
      ('Route', 'heparin IV or SC · warfarin oral'),
      ('Acts in', 'the blood · the liver'),
      ('Onset', 'seconds · days (limited by factor half-lives)'),
      ('Monitor', 'PTT (intrinsic) · PT/INR (extrinsic)'),
      ('Placenta', 'heparin does not cross · warfarin crosses (teratogenic)')])],
  dyn=dyn)
