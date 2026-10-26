# m56 — Childhood Disorders by Age (dynamic map, kit data)
# WHEN a childhood disorder can start and when it can be diagnosed — on one AGE axis (birth → 18 years → adult), not the
# symptom-duration clock of psychclock and not neurodev's static ADHD/autism detail (criteria lists, biology, stimulant side
# effects stay there). On top a big age bar for the picked disorder (its onset window, the age cut-offs, captions), below a
# ladder of 16 options in five `sections` (development & learning · autism & genetic syndromes · attention & tics · disruptive
# behavior & mood · mutism, attachment & elimination), each with its own bar: light = normal for age / too early to diagnose,
# dashed outline = the window onset must fall in, solid = the age it typically shows or is diagnosed, dark block = peak,
# arrow = can continue into adulthood. Picking one lights its row and its look-alikes (Name it = a real "tell them apart"),
# drops its age cut-offs through the ladder and runs the child along the axis.
# Readouts are criteria, read as ↑ needed / present · ↓ not needed / ruled out · ↔ either way: normal intelligence, ≥ 2
# settings, needs ≥ 6 months, restricted & repetitive behavior, a single known gene, medication first line.
#
# Sources (all read; OCOM Psych course texts win for this block):
#   OCOM Psych SDL 34–37 reading = Kaplan & Sadock ch 2 (the course PDF "Neurodev disorders" is that chapter) and SDL 34
#     reading = Kaplan & Sadock ch 14 (the course PDF "Eliminating Disorders"); SDL 37 reading: Felt et al., Diagnosis and
#     management of ADHD in children, Am Fam Physician 2014 (ADHD cannot be reliably diagnosed before 4; consider it from 4;
#     preschool treatment begins with behavioral management, older children with medication; psychostimulants first line,
#     atomoxetine/guanfacine/clonidine less effective; ≥ 5 symptoms from 17; several symptoms before 12).
#   Kaplan ch 2: ID begins before 18 (IQ drop after 18 = dementia only), delays in most areas vs a learning disorder's single
#     area; severity by adaptive functioning · SLD ≥ 6 mo, symptoms beginning in school-age years · expressive language
#     disorder recognizable by ~18 months when severe; sensory impairment excluded; stuttering appears 18 months–9 years,
#     peaks 2–3.5 and 5–7 years; speech sound disorder: spontaneous recovery rare after 8 · SPCD rarely diagnosed before 4,
#     mild cases not until adolescence, no restricted/repetitive behavior · ASD two domains, early developmental period,
#     typically evident in the second year, mild cases middle childhood, up to 25% lose some language, drugs treat
#     associated symptoms (irritability: risperidone, aripiprazole) not core features · Rett: females, normal development at
#     least 6 months, deterioration starting about 1 year, stereotyped hand-wringing, now classed with ASD in DSM-5 ·
#     fragile X: second commonest single cause of ID, Xq27.3, postpubertal macroorchidism, high rates of ADHD and autism ·
#     ADHD ≥ 6 mo, before 12, ≥ 6 symptoms (≥ 5 from 17), > 1 setting; often present by 3 but diagnosed at school;
#     pharmacologic treatment first line, stimulants first choice; persists into adulthood in ~60% · Tourette: multiple
#     motor + ≥ 1 vocal tic > 1 year, onset before 18, average onset 4–6, peak severity 10–12, half to two-thirds improve by
#     adolescence, habit reversal the most studied behavioral treatment · DMDD: outbursts ≥ 3/week, irritable between,
#     ≥ 12 months, ≥ 2 settings, onset before 10, not diagnosed before 6 or after 18, cannot co-occur with ODD; leads to
#     unipolar depression/anxiety rather than bipolar · ODD: ≥ 4 symptoms ≥ 6 months, one setting is enough (mild); can begin
#     as early as 3, typically noted by 8; normal oppositional peak 18–24 months; primary treatment is family intervention
#     (parent management training) · conduct disorder: ≥ 3 of 15 behaviors over 12 months; childhood-onset = a symptom before
#     10, adolescent-onset = none before 10; after 18 only if antisocial PD criteria are not met; very young children rarely
#     meet criteria, school-age children can · selective mutism: often begins before 5, onset 4–8, ≥ 1 month (not the first
#     month of school), speaks fluently at home · RAD: grossly pathogenic care, developmental age ≥ 9 months, begins before 5,
#     not due to ASD; DSED: overly familiar with strangers; treated by therapy with the caregivers.
#   Kaplan ch 14: no encopresis diagnosis before 4, no enuresis before 5; enuresis ≥ 2/week for ≥ 3 months; secondary
#     enuresis (after a dry year) usually begins 5–8; ~1% at 15; alarm the most effective; desmopressin, imipramine;
#     encopresis with constipation and overflow, laxatives (PEG) + behavioral; soiling usually begins by 4.
#   First Aid 2025 p. 60 (Rett: de novo MECP2, normal 6–18 months then regression, hand-wringing; fragile X: FMR1 CGG
#     > 200 repeats, most common inherited cause of ID, postpubertal macroorchidism, long face, large ears, autism, MVP) ·
#     p. 572 (milestones) · p. 574 (ADHD onset before 12, diagnosed only after 4, normal intelligence, ≥ 2 settings,
#     stimulants ± behavioral, atomoxetine, α₂ agonists; ASD onset early childhood, may have ID or above-average skills;
#     conduct disorder → antisocial PD after 18, CBT; DMDD onset before 10, diagnosed after 6; ID global vs SLD; ODD
#     ≥ 6 months; selective mutism onset before 5, ≥ 1 month, development not impaired, behavioral/family/play therapy,
#     SSRIs; SLD school-age onset ≥ 6 months, normal intelligence; Tourette before 18, > 1 year, psychoeducation and
#     behavioral therapy, drugs for intractable tics) · p. 585 (enuresis ≥ 5 years, ≥ 2/week for ≥ 3 months, behavioral
#     first, then alarm or desmopressin; encopresis ≥ 4 years, ≥ 1/month for ≥ 3 months, laxatives for constipation).
# Printed as the sources print them; where they differ the course text wins:
#   selective mutism onset — FA "before age 5"; Kaplan (course) "often begins before 5 … onset can range from 4 to 8": the
#   bar shows 4–8 with a 5-year line · Rett — FA "normal 6–18 months"; Kaplan "at least 6 months … deterioration starts at
#   about 1 year": the window shows 6–18 months · fragile X — FA "most common inherited cause", Kaplan "second most common
#   single cause" (Down syndrome first) — both kept, they agree.
# Cut for lack of support in these sources: a numeric age for puberty (fragile X shows "after puberty" in words only);
#   any age for SLD's school-age window beyond "school age" (drawn from 6, where FA/Kaplan's DMDD and school ages sit —
#   flagged for the owner); separation anxiety (psychclock owns it); ASD/ID percentages that conflict inside Kaplan
#   (one-third vs 70–75% with IQ < 70); drug-first arrows for DMDD, encopresis, SPCD, Rett, fragile X (no source commits).
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

K2, K14 = full('Kaplan & Sadock', 2), full('Kaplan & Sadock', 14)
AFP = 'OCOM Psych — SDL 37 reading: Diagnosis and management of ADHD in children (Am Fam Physician 2014)'

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
O = lambda *k: ['dz:' + x for x in k]

# ════════ the age axis (square-root scale, so infancy is readable) ════════
AX0, AX1, END = 640, 2240, 2306           # birth · 18 years · the "into adulthood" arrow tip
def X(age):
    return round(AX0 + (AX1 - AX0) * math.sqrt(min(age, 18) / 18))
TICKS = [('birth', 0), ('6 mo', 0.5), ('1', 1), ('1½', 1.5), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('8', 8),
         ('10', 10), ('12', 12), ('15', 15), ('18 yr', 18)]

COL = dict(ndvDev='--dk1', ndvAsd='--dk7', ndvAtt='--dk6', ndvBeh='--dk10', ndvOth='--dk3')

# ════════ the options ════════
# key: (label, subtitle, lane, card, bar spec)
# bar spec segments: lead (light: normal for age / too early), win (dashed: onset must fall here), fit (solid, ends ⊣),
#   open (solid with an arrow: can continue into adulthood), peak (dark block), dot (a milestone)
ROWS = [
  ('Development & learning', [
    ('miles', 'Normal milestones', 'smile 2 mo · walks 12–18 mo · sentences 4 yr', 'ndvDev', 'milestones',
     [('dot', a) for a in (2 / 12, 0.5, 0.75, 10 / 12, 1, 1.5, 2, 3, 4)]),
    ('id', 'Intellectual disability', 'begins before 18 · a global deficit', 'ndvDev', 'intellectual',
     [('win', 0, 18), ('thinopen', 0, None)]),
    ('sld', 'Specific learning disorder', 'school-age onset · ≥ 6 months', 'ndvDev', 'intellectual',
     [('lead', 0, 6), ('win', 6, 18)]),
    ('comm', 'Language & speech disorders', 'stuttering starts 18 mo – 9 yr', 'ndvDev', 'commdz',
     [('win', 1.5, 9), ('peak', 2, 3.5), ('peak', 5, 7)]),
    ('spcd', 'Social (pragmatic) comm.', 'rarely diagnosed before 4', 'ndvDev', 'spcd',
     [('lead', 0, 4), ('open', 4, None)]),
  ]),
  ('Autism & genetic syndromes', [
    ('asd', 'Autism spectrum disorder', 'evident in the second year of life', 'ndvAsd', 'autism',
     [('win', 1, 2), ('open', 1, None)]),
    ('rett', 'Rett syndrome', 'normal 6–18 mo, then regression', 'ndvAsd', 'autism',
     [('lead', 0, 0.5), ('win', 0.5, 1.5), ('open', 0.5, None)]),
    ('fxs', 'Fragile X syndrome', 'CGG repeats · big testes after puberty', 'ndvAsd', 'fragilex',
     [('open', 0, None)]),
  ]),
  ('Attention & tics', [
    ('adhd', 'ADHD', 'symptoms before 12 · diagnosed from 4', 'ndvAtt', 'adhd',
     [('win', 0, 12), ('lead', 0, 4), ('open', 4, None)]),
    ('tic', 'Tourette syndrome', 'onset 4–6 · peak 10–12 · before 18', 'ndvAtt', 'tourette',
     [('win', 0, 18), ('fit', 4, 6), ('lead', 6, 18), ('peak', 10, 12)]),
  ]),
  ('Disruptive behavior & mood', [
    ('odd', 'Oppositional defiant', 'from age 3 · usually noted by 8', 'ndvBeh', 'conductodd',
     [('lead', 1.5, 2), ('fit', 3, 8)]),
    ('cd', 'Conduct disorder', 'onset subtype at 10 · ASPD after 18', 'ndvBeh', 'conductodd',
     [('win', 0, 10), ('lead', 0, 6), ('fit', 6, 18)]),
    ('dmdd', 'DMDD', 'onset before 10 · diagnosed 6–18', 'ndvBeh', 'conductodd',
     [('win', 0, 10), ('fit', 6, 18)]),
  ]),
  ('Mutism, attachment & elimination', [
    ('mute', 'Selective mutism', 'onset 4–8, often before 5', 'ndvOth', 'separation',
     [('win', 4, 8)]),
    ('rad', 'Reactive attachment', 'developmental age ≥ 9 mo · before 5', 'ndvOth', 'rad',
     [('lead', 0, 0.75), ('win', 0.75, 5)]),
    ('enur', 'Enuresis', 'from 5 yr · 2×/week for 3 months', 'ndvOth', 'enuresis',
     [('lead', 0, 5), ('fit', 5, 18), ('win', 5, 8)]),
    ('enco', 'Encopresis', 'from 4 yr · monthly for 3 months', 'ndvOth', 'enuresis',
     [('lead', 0, 4), ('fit', 4, 18)]),
  ]),
]
INFO = {r[0]: r for _, rows in ROWS for r in rows}
KEYS = [r[0] for _, rows in ROWS for r in rows]

# the age cut-off lines for each option (age, label)
CUT = dict(miles=[], id=[(18, '18 years')], sld=[(6, 'school age')], comm=[(1.5, '18 mo'), (8, 'speech: 8 yr'), (9, '9 yr')],
           spcd=[(4, '4 years')], asd=[(1, '1 yr'), (2, '2 yr')], rett=[(0.5, '6 mo'), (1.5, '18 mo')], fxs=[],
           adhd=[(4, '4: diagnosable'), (12, 'before 12'), (17, '17: 5 symptoms')], tic=[(4, '4–6 onset'), (10, '10–12 peak'), (18, 'before 18')],
           odd=[(3, '3 years'), (8, '8 years')], cd=[(10, '10: childhood vs adolescent'), (18, '18: ASPD')],
           dmdd=[(6, '6 years'), (10, 'onset by 10'), (18, '18 years')], mute=[(4, '4'), (5, '5 (FA)'), (8, '8 years')],
           rad=[(0.75, '9 mo'), (5, 'before 5')], enur=[(5, '5 years'), (8, 'secondary: 5–8')], enco=[(4, '4 years')])

# look-alikes (lit the same way, so the reader decides from the bar on top + the results)
NEAR = dict(miles=[], id=['sld', 'fxs'], sld=['id', 'adhd'], comm=['asd', 'mute'], spcd=['asd'], asd=['spcd', 'rad', 'rett'],
            rett=['asd'], fxs=['id', 'asd'], adhd=['sld', 'odd'], tic=['adhd'], odd=['cd', 'dmdd'], cd=['odd'],
            dmdd=['odd'], mute=['comm'], rad=['asd'], enur=['enco'], enco=['enur'])
LIT = {k: [k] + NEAR[k] for k in KEYS}
def lit_by(row):
    return O(*[k for k in KEYS if row in LIT[k]])

# ════════ 1. header + the big age bar on top ════════
add('<rect class="dyn-soft" x="140" y="110" width="2200" height="340" rx="28"/>')
text('The age bar — when it can start, when it can be diagnosed', 170, 150, 'dyn-big')
text('Light = normal for age or too early · dashed = onset must fall here · solid = typical age · dark = peak · arrow = into adulthood',
     170, 172, 'dyn-cap')
text('Results: ↑ needed or present · ↓ not needed or ruled out · ↔ either way · the scale stretches the first years', 170, 192, 'dyn-cap')
YA = 330
text('Pick a disorder: the child runs along its age bar here.', AX0, 262, 'nf-l1', unless=['dz:*'])
text('Its age cut-offs drop through the ladder below, and its look-alikes light up.', AX0, 284, 'nf-l2', unless=['dz:*'])
add(f'<path d="M{AX0} {YA} H{END}" class="dyn-line" style="opacity:.5"/>', unless=['dz:*'])

def segs(key, y, h, big):
    lane = INFO[key][3]; c = COL[lane]; out = []
    for s in INFO[key][5]:
        k = s[0]
        if k == 'dot':
            r = 9 if big else 6
            out.append(f'<circle cx="{X(s[1])}" cy="{y}" r="{r}" style="fill:var({c});fill-opacity:.85"/>')
            continue
        x0 = X(s[1]); x1 = END if s[2] is None else X(s[2])
        if k == 'lead':
            out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{max(4, x1 - x0)}" height="{h}" rx="{h / 2}" style="fill:var({c});fill-opacity:.16"/>')
        elif k == 'win':
            out.append(f'<rect x="{x0}" y="{y - h / 2 - 5}" width="{max(6, x1 - x0)}" height="{h + 10}" rx="{h / 2 + 4}" '
                       f'style="fill:none;stroke:var({c});stroke-width:2.5;stroke-dasharray:6 5"/>')
        elif k == 'peak':
            out.append(f'<rect x="{x0}" y="{y - h / 2 - 2}" width="{max(6, x1 - x0)}" height="{h + 4}" rx="4" style="fill:var(--ink-2);fill-opacity:.75"/>')
        elif k == 'thinopen':
            tip = 10
            out.append(f'<rect x="{x0}" y="{y + h / 2 + 3}" width="{x1 - x0 - tip}" height="{max(4, h / 3)}" rx="2" style="fill:var({c});fill-opacity:.6"/>'
                       f'<path d="M{x1 - tip} {y + h / 2 - 1} L{x1} {y + h / 2 + 3 + max(4, h / 3) / 2} L{x1 - tip} {y + h / 2 + 7 + max(4, h / 3)} Z" style="fill:var({c});fill-opacity:.6"/>')
        elif k in ('fit', 'open'):
            tip = h * .9 if k == 'open' else 0
            out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{max(6, x1 - x0 - tip)}" height="{h}" rx="{min(6, h / 2)}" style="fill:var({c});fill-opacity:.75"/>')
            if k == 'open':
                out.append(f'<path d="M{x1 - tip - 1} {y - h / 2 - 5} L{x1} {y} L{x1 - tip - 1} {y + h / 2 + 5} Z" style="fill:var({c});fill-opacity:.75"/>')
            else:
                out.append(f'<path d="M{x1} {y - h / 2 - 6} V{y + h / 2 + 6}" class="dyn-line" style="stroke:var({c});stroke-width:4"/>')
    return ''.join(out)

# captions under the big bar — (age, text); first at y 394, second at 416
CAP = dict(
  id=[(0, 'delays in most areas, with impaired adaptive function — must begin before 18 (later IQ loss = dementia only)')],
  sld=[(0, 'not apparent before school'), (6, 'one academic skill — reading, writing or math — despite help, ≥ 6 months')],
  comm=[(0, 'severe language disorder shows by ~18 months'), (1.5, 'stuttering: onset 18 mo – 9 yr, peaks at 2–3½ and 5–7 (dark)')],
  spcd=[(0, 'too early to call before 4'), (4, 'social use of language impaired — no repetitive behavior · mild cases surface in adolescence')],
  asd=[(1, 'evident in the 2nd year — severe cases in the 1st, mild ones in middle childhood · lifelong')],
  rett=[(0, 'normal at first'), (0.5, 'regression 6–18 months — loses speech and hand use, hand-wringing · girls')],
  fxs=[(0, 'CGG expansion in FMR1 from birth — intellectual disability, autism, ADHD · macroorchidism after puberty')],
  adhd=[(0, 'light: not reliably diagnosed before 4 · dashed: symptoms must start before 12'),
        (4, 'solid: diagnosable from 4 · persists into adulthood in about 60%')],
  tic=[(0, 'dashed: onset before 18'), (4, 'tics start at 4–6 (solid), are worst at 10–12 (dark), and often fade by adolescence')],
  odd=[(1.5, 'normal defiance peaks at 18–24 months'), (3, 'ODD can begin at 3 and is usually noticed by 8')],
  cd=[(0, 'dashed: a symptom before 10 = childhood-onset type'), (6, 'school-age children can bully, fight, set fires · after 18 → antisocial PD')],
  dmdd=[(0, 'dashed: outbursts must start before 10'), (6, 'solid: diagnosed only from 6 to 18 · leads to depression and anxiety, not bipolar')],
  mute=[(4, 'onset 4–8, often before 5 — silent at school, fluent at home, ≥ 1 month (not the first month of school)')],
  rad=[(0, 'needs a developmental age of 9 months'), (0.75, 'begins before 5 — after grossly neglectful care')],
  enur=[(0, 'light: bladder control not expected yet'), (5, 'from 5: wetting ≥ 2×/week for 3 months · dashed: secondary enuresis starts 5–8')],
  enco=[(0, 'light: bowel control not expected yet'), (4, 'from 4: soiling ≥ 1×/month for 3 months — often constipation with overflow')],
)
# the milestones on the big bar: (age, label, y)
MILE = [(2 / 12, 'social smile · 2 mo', 430), (0.5, 'stranger anxiety · 6 mo', 408),
        (0.75, 'separation anxiety, object permanence · 9 mo', 386), (10 / 12, '“mama”, “dada”, pincer grasp · 10 mo', 364),
        (1, 'walks · 12–18 mo', 306), (2, '50–200 words, kicks a ball · 2 yr', 306), (3, 'tricycle, 300+ words · 3 yr', 386),
        (4, 'hops on one foot, sentences · 4 yr', 364)]
for k in KEYS:
    lab, sub = INFO[k][1], INFO[k][2]
    add(f'<path d="M{AX0} {YA} H{END}" class="dyn-line" style="opacity:.45"/>' + segs(k, YA, 30, True), when=O(k))
    text(lab, AX0, 262, 'dyn-big', when=O(k))
    text(sub, AX0, 284, 'nf-l2', when=O(k))
    for i, (at, t) in enumerate(CAP.get(k, [])):
        text(t, X(at), 394 if i == 0 else 416, TAG, when=O(k))
for a, t, y in MILE:
    x = X(a)
    add(f'<path d="M{x} {YA + (12 if y > YA else -12)} V{y + (-14 if y > YA else 6)}" class="dyn-line" style="opacity:.5"/>', when=O('miles'))
    text(t, x - 6, y, TAG, when=O('miles'))

# ════════ 2. the axis ════════
YT = 486
YB0 = 502
for lab, a in TICKS:
    text(lab, X(a), YT, 'nf-l2', 'middle')
text('adult', END, YT, 'nf-l2', 'middle')
add(f'<path d="M{AX0} {YT + 10} H{END}" class="dyn-line"/>' +
    ''.join(f'<path d="M{X(a)} {YT + 4} V{YT + 16}" class="dyn-line"/>' for _, a in TICKS))

# ════════ 3. the ladder ════════
PITCH, HEAD = 54, 50
y = YB0 + 36
ROWY = {}
NODEPINS = dict(asd=['autism', 'asddx', 'asdbio', 'asdtx'], adhd=['adhd', 'adhddx', 'stimmech', 'stimside', 'atomox'],
                fxs=['fragilex'], tic=['tourette'])
nodes = []
for sec, rows in ROWS:
    text(sec, 150, y + 6, 'dyn-big')
    add(f'<path d="M{150 + len(sec) * 8.6 + 16} {y} H{END}" class="dyn-line" style="opacity:.35"/>')
    y += HEAD
    for (k, lab, sub, lane, cid, spec) in rows:
        ROWY[k] = y
        nodes.append((f'nv{len(nodes) + 1}', lab, 370, y, lane, sub, NODEPINS.get(k, [cid])))
        y += PITCH
    y += 6
YEND = y - 6
grid = ''.join(f'<path d="M{X(a)} 214 V{YEND}" class="dyn-line" style="stroke-dasharray:2 8;opacity:.4"/>' for _, a in TICKS[1:])
shapes.insert(0, grid)
for k in KEYS:
    yy = ROWY[k]
    add(f'<rect x="146" y="{yy - 26}" width="2184" height="52" rx="16" style="fill:var(--accent);fill-opacity:.09;stroke:var(--accent);stroke-opacity:.5;stroke-width:2"/>',
        when=lit_by(k))
    add(f'<path d="M{AX0} {yy} H{END}" class="dyn-line" style="opacity:.25"/>' + segs(k, yy, 14, False))
    text('▶ this one', 160, yy + 4, TAG, when=O(k))
    of = [q for q in KEYS if k in NEAR[q]]
    if of: text('look-alike', 160, yy + 4, 'nf-l2', when=O(*of))

# the age cut-off lines through the ladder + their labels on the big bar
for k in KEYS:
    if not CUT[k]: continue
    add(''.join(f'<path d="M{X(a)} 300 V{YEND}" style="fill:none;stroke:var(--bad);stroke-width:2.5;stroke-dasharray:8 6;opacity:.75"/>'
                for a, _ in CUT[k]), when=O(k))
    for i, (a, lab) in enumerate(CUT[k]):
        text(lab, X(a) + 6, 308 if i % 2 == 0 else 360, 'nf-l1', when=O(k))

# ════════ particles: the child growing along the axis ════════
kinds = dict(child=['age', '--dk2'], lit=['age', '--ink-3'])
groups = [['age', 'Age']]
def run_end(k):
    xs = [END if s[2] is None else X(s[2]) for s in INFO[k][5] if s[0] != 'dot']
    return max(xs) if xs else X(4) + 40
flows = [dict(d=f'M{AX0} {YA} H{END}', len=END - AX0, speed=160, unless=['dz:*'], base=dict(child=4))]
for k in KEYS:
    e = run_end(k)
    flows.append(dict(d=f'M{AX0} {YA} H{e}', len=e - AX0, speed=150, r=8, when=O(k), base=dict(child=max(2, round((e - AX0) / 320)))))
for k in KEYS:
    e = run_end(k); yy = ROWY[k]
    flows.append(dict(d=f'M{AX0} {yy} H{e}', len=e - AX0, speed=130, r=5, when=lit_by(k), base=dict(lit=2)))

# ════════ notes ════════
notes = {
  '': 'Childhood disorders are told apart by age as much as by symptoms: when they may start, and the youngest age at which they '
      'can be called. Pick one — its age bar runs on top, its cut-offs drop through the ladder, and its look-alikes light up.',
  'dz:miles': 'Normal milestones are ranges: social smile by 2 months, stranger anxiety by 6, separation anxiety and object '
              'permanence by 9, walking by 12–18 months, sentences by 4 years. Missing several, or losing skills, needs assessment.',
  'dz:id': 'Intellectual disability: deficits in reasoning and learning with impaired adaptive function, beginning before age 18. '
           'Severity is graded by adaptive functioning, not IQ; a learning disorder, by contrast, delays one area only.',
  'dz:sld': 'Specific learning disorder: reading (dyslexia), writing or math far below expected for ≥ 6 months despite focused help, '
            'starting in the school years, with normal intelligence. Treatment is academic support, not medication.',
  'dz:comm': 'Language disorder shows by about 18 months when severe; hearing loss must be excluded. Stuttering begins between '
             '18 months and 9 years, peaking at 2–3½ and 5–7; a speech sound disorder rarely clears on its own after 8.',
  'dz:spcd': 'Social (pragmatic) communication disorder: trouble using language socially — greetings, turn-taking, tone, implied '
             'meaning — without the restricted, repetitive behavior of autism. It is rarely diagnosed before age 4.',
  'dz:asd': 'Autism spectrum disorder: social communication deficits plus restricted, repetitive behavior from early childhood, '
            'typically evident in the second year. Behavioral programs treat the core; risperidone or aripiprazole treat irritability.',
  'dz:rett': 'Rett syndrome: a girl develops normally for 6–18 months, then loses speech and purposeful hand use, with '
             'hand-wringing, seizures, ataxia and scoliosis — a de novo MECP2 mutation on the X chromosome, lethal in males.',
  'dz:fxs': 'Fragile X syndrome: CGG repeat expansion (> 200) in FMR1 — the most common inherited cause of intellectual disability, '
            'with autism and ADHD traits, a long face, large ears and macroorchidism after puberty.',
  'dz:adhd': 'ADHD: inattention and/or hyperactivity-impulsivity in ≥ 2 settings for ≥ 6 months, starting before 12, but not '
             'reliably diagnosed before 4. Preschoolers start with behavioral therapy; older children with a stimulant.',
  'dz:tic': 'Tourette syndrome: multiple motor tics plus at least one vocal tic for more than a year, starting before 18 — usually at '
            '4–6, worst at 10–12, often easing by adolescence. Psychoeducation and habit reversal come first.',
  'dz:odd': 'Oppositional defiant disorder: angry, argumentative, defiant behavior toward authority figures for ≥ 6 months; one '
            'setting is enough. It can begin at 3 and is usually noticed by 8. Parent management training is the main treatment.',
  'dz:cd': 'Conduct disorder: ≥ 3 violations of others’ rights or major rules (aggression, destruction, theft, truancy) over 12 '
           'months. A symptom before 10 marks the childhood-onset type; after 18 it becomes antisocial personality disorder.',
  'dz:dmdd': 'DMDD: severe temper outbursts ≥ 3 times a week with constant irritability between, for ≥ 12 months, in ≥ 2 settings; '
             'onset before 10, diagnosed only between 6 and 18. It leads to depression and anxiety, not bipolar disorder.',
  'dz:mute': 'Selective mutism: a child who speaks fluently at home stays silent at school for ≥ 1 month (not just the first month), '
             'usually starting at 4–8, often before 5. It is an anxiety disorder; behavioral therapy, with SSRIs if needed.',
  'dz:rad': 'Reactive attachment disorder: a withdrawn child who rarely seeks comfort after grossly neglectful care; it needs a '
            'developmental age of 9 months, begins before 5, and is not autism. Therapy repairs the caregiver bond.',
  'dz:enur': 'Enuresis: wetting ≥ 2 times a week for ≥ 3 months at age 5 or older, usually at night. Behavioral measures first; '
             'then a bedwetting alarm or desmopressin. Secondary enuresis, after a dry year, usually starts at 5–8.',
  'dz:enco': 'Encopresis: soiling ≥ once a month for ≥ 3 months at age 4 or older — often constipation with overflow. Toilet '
             'training and behavioral therapy plus laxatives such as polyethylene glycol.',
}

# ════════ readouts: criteria (↑ needed or present · ↓ not needed or ruled out · ↔ either way) ════════
R = lambda keys, d: dict(when=O(*keys), d=d)
readouts = [
  dict(l='Normal intelligence', mods=[R(['sld', 'adhd'], 1), R(['id', 'fxs', 'rett'], -1), R(['asd'], 0)]),
  dict(l='≥ 2 settings', mods=[R(['adhd', 'dmdd'], 1), R(['odd', 'mute'], -1)]),
  dict(l='Needs ≥ 6 months', mods=[R(['sld', 'adhd', 'tic', 'odd', 'cd', 'dmdd'], 1), R(['mute', 'enur', 'enco'], -1)]),
  dict(l='Restricted, repetitive', mods=[R(['asd', 'rett'], 1), R(['spcd'], -1)]),
  dict(l='Single known gene', mods=[R(['rett', 'fxs'], 1)]),
  dict(l='Medication first line', mods=[R(['adhd'], 1), R(['id', 'sld', 'comm', 'asd', 'tic', 'odd', 'cd', 'mute', 'rad', 'enur'], -1)]),
]

OPT = dict(miles='Normal milestones', id='Intellectual disability', sld='Learning disorder', comm='Language & speech',
           spcd='Social communication', asd='Autism spectrum', rett='Rett syndrome', fxs='Fragile X', adhd='ADHD',
           tic='Tourette', odd='ODD', cd='Conduct disorder', dmdd='DMDD', mute='Selective mutism', rad='Reactive attachment',
           enur='Enuresis', enco='Encopresis')
SEC = ['Development', 'Autism & genes', 'Attention & tics', 'Disruptive & mood', 'Mutism, attachment, elimination']
dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='dz', label='Disorder', type='one', options=[[k, OPT[k], INFO[k][4]] for k in KEYS],
                 sections=[[SEC[i], [r[0] for r in rows]] for i, (_, rows) in enumerate(ROWS)])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM Psych SDL 34–37 (Kaplan & Sadock ch 2, 14; Am Fam Physician 2014 ADHD) · First Aid pp. 60, 572, 574, 585')

MAP = dict(
  id='neurodevsim', title='Childhood Disorders by Age', topic='behav', after='neurodev',
  sub='When each childhood disorder can start and when it can be diagnosed — milestones, intellectual and learning disorders, '
      'autism, Rett, fragile X, ADHD, Tourette, ODD vs conduct vs DMDD, selective mutism, attachment, enuresis and encopresis on '
      'one age bar: pick one, watch its window and age cut-offs, and read the criteria (↑ needed · ↓ ruled out · ↔ either). '
      'Tap a disorder for its card',
  w=3500, h=YEND + 60,
  fa='60, 572, 574, 585', src=[K2, K14],   # + AFP (SDL 37 course reading) once its title is known to the Mac-side tooling
  lanes=[('ndvDev', 'Development & learning', 'glycolysis'), ('ndvAsd', 'Autism & genetic syndromes', 'sugars'),
         ('ndvAtt', 'Attention & tics', 'ppp'), ('ndvBeh', 'Disruptive behavior & mood', 'tca'),
         ('ndvOth', 'Mutism, attachment & elimination', 'glycogen')],
  comps=[],
  nodes=nodes,
  panels=[
    (2420, 760, 1000, 'Tell them apart (Kaplan & Sadock ch 2; First Aid p. 574)', [
      ('Autism vs SPCD', 'restricted, repetitive behavior only in autism'),
      ('Autism vs RAD', 'RAD follows neglect and is not due to autism'),
      ('ODD vs conduct', 'conduct disorder violates others’ rights'),
      ('ODD vs DMDD', 'DMDD: ≥ 2 settings, constant irritability — never both'),
      ('Mutism vs language', 'selective mutism: fluent at home'),
      ('ID vs learning disorder', 'global vs one academic skill')]),
    (2420, 990, 1000, 'First line (First Aid pp. 574, 585; Kaplan ch 2, 14; AFP 2014)', [
      ('ADHD', 'preschool: behavioral · older: stimulant'),
      ('Autism', 'behavioral programs · irritability: risperidone'),
      ('Tourette', 'psychoeducation, habit reversal'),
      ('ODD', 'parent management training'),
      ('Enuresis', 'behavioral → alarm or desmopressin'),
      ('Encopresis', 'toilet training + laxatives')]),
  ],
  dyn=dyn,
)
