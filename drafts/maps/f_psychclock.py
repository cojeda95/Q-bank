# m55 — Psychiatric Timelines (dynamic map, kit data)
# WHEN a psychiatric diagnosis fits — the duration rules (psychdx is the static ladder from diagnosis to treatment).
# One shared time axis (stretched so the first days and weeks are readable: 0 · 1 d · 3 d · 4 d · 1 wk · 2 wk · 1 mo ·
# 3 mo · 6 mo · 1 yr · 2 yr), drawn twice: on top a big "clock" for the picked disorder (its window, the cut-off lines,
# the event that starts the clock, captions), and below a ladder of 25 disorders in five `sections` (psychotic · mood ·
# trauma, stress & grief · anxiety · somatic), each with its own bar: light = symptoms present but not yet long enough,
# solid = the diagnosis fits, an arrow = "or longer", ◆ = the clock starts at an event (trauma, stressor, death, delivery).
# Picking a disorder lights its row AND its look-alikes the same way (so Name it is a real "tell them apart" question:
# the clock on top and the results decide), drops its cut-off lines through the whole ladder, and runs the clock.
# Readouts are criteria, read as ↑ needed / present · ↓ not needed / ruled out · ↔ either way: needs ≥ 1 month, needs
# ≥ 6 months, psychosis, a mood episode, distress or impairment, back to baseline, a stressor first.
#
# Sources (all read in the corpus; course text > First Aid > Kaplan on any conflict):
#   OCOM Psych — SDL 12 reading (Am Fam Physician 2016, PMS/PMDD): DSM-5 PMDD criteria — ≥ 5 symptoms in the final week
#     before menses in most cycles, improving within a few days of menses, minimal or absent the week after; most cycles of
#     the preceding year; clinically significant distress or interference; confirmed by prospective daily ratings over at
#     least two symptomatic cycles; not merely an exacerbation of MDD, panic, PDD; SSRIs first line (continuous or luteal).
#   First Aid 2025 p. 572 (grief: typical acute grief time limited, adaptations within 6 months, not a disorder; prolonged
#     grief disorder: intense, persistent, prolonged "at least 6–12 months", impairs functioning, not another disorder
#     such as MDD) · p. 574 (separation anxiety ≥ 4 weeks, normal up to age 3–4; selective mutism ≥ 1 month, onset
#     before 5; ODD ≥ 6 months; Tourette tics > 1 year, onset before 18) · p. 576 (psychosis definition; psychotic features
#     possible in mood episodes other than hypomania; schizoaffective: psychosis must occur by itself > 2 weeks) · p. 577
#     (schizophrenia ≥ 6 months with ≥ 1 month active, profound functional impairment, atypical antipsychotics first line;
#     brief psychotic 1 day–1 month, usually stress-related; schizophreniform 1–6 months; schizoaffective ≥ 2 weeks of
#     psychosis without a mood episode; delusional disorder > 1 month, no mood disorder, functioning otherwise unaffected;
#     manic episode ≥ 1 week or any duration if hospitalized, marked impairment) · p. 578 (hypomania ≥ 4 consecutive days,
#     no marked impairment, no psychotic features; bipolar: functioning usually normalizes between episodes; mood
#     stabilizers; cyclothymic ≥ 2 years, symptoms half the time, remission ≤ 2 months; MDD ≥ 2 weeks, 5 of 9, CBT + SSRIs;
#     MDD with psychotic features; PDD ≥ 2 years (≥ 1 year children), remission ≤ 2 months; seasonal pattern ≥ 2
#     consecutive years, light therapy) · p. 579 (peripartum onset during pregnancy or within 4 weeks of delivery;
#     postpartum blues starts 2–3 days after delivery, resolves within 2 weeks, supportive) · p. 580 (panic disorder: an
#     attack then ≥ 1 month of worry/behavior change, CBT/SSRIs/venlafaxine; phobias ≥ 6 months, CBT with exposure; GAD
#     most days ≥ 6 months, CBT/SSRIs/SNRIs) · p. 581 (adjustment within 3 months of a stressor, < 6 months once it ends,
#     reevaluate for MDD/GAD past 6 months, CBT; PTSD > 1 month, distress or impairment, CBT/SSRIs/venlafaxine, prazosin
#     for nightmares; acute stress disorder 3 days–1 month, CBT; the "Diagnostic criteria by symptom duration" chart) ·
#     p. 583 (somatic symptom disorder: complaints lasting months to years; illness anxiety disorder).
#   Kaplan & Sadock ch 5 (Table 5-3 schizophrenia ≥ 6 mo, functional impairment; Table 5-4 schizoaffective — meets MDE or
#     manic criteria, mood symptoms the majority of the illness, a 2-wk period of psychosis without mood symptoms,
#     functional impairment; schizophreniform ≥ 1 mo but < 6 mo, return to baseline, > 6 mo → consider schizophrenia;
#     Table 5-6 brief psychotic ≥ 1 day, < 1 mo with return to baseline, specifiers with/without marked stressors; Table
#     5-7 delusional ≥ 1 mo, no marked functional impairment) · ch 6 (manic 1 wk+, impaired functioning or hospitalization;
#     hypomanic 4 days+, no marked impairment; cyclothymic ≥ 2 yr, ≥ 1 yr children, symptoms ≥ 50% of the time, never an
#     MDE or manic episode, marked distress or impairment) · ch 7 (Table 7-2 MDD 2 wk, distress or impaired functioning;
#     Table 7-3 PDD 2+ yr, 1+ yr children, ≤ 2 mo symptom-free, MDE criteria may have been met; virtually no euthymic
#     periods; bereavement vs depression) · ch 8 (panic 1 mo of worry after an attack; agoraphobia, specific phobia, social
#     anxiety ≥ 6 mo with marked distress or impairment; GAD at least 6 months) · ch 10 (PTSD ≥ 1 mo / "more than a month",
#     marked distress and impairment; acute stress disorder 3 days to < 1 mo, nine symptoms, time course is what separates
#     it from PTSD; adjustment within 3 mo of a stressor, resolving within 6 mo of its end) · ch 12 (somatic symptom
#     disorder ≥ 6 mo, distress or impairment; illness anxiety disorder ≥ 6 mo) · ch 2 (separation anxiety ≥ 4 weeks).
# Printed as the sources print them; where they differ the higher source wins:
#   delusional disorder "> 1 month" (FA 577; Kaplan Table 5-7 prints ≥ 1 mo) · PTSD "> 1 month" (FA 581; Kaplan prints
#   ≥ 1 mo in the table, "more than a month" in the text) · prolonged grief "at least 6–12 months" (FA 572, the only source).
# Cut for lack of support in these sources: separation anxiety's adult duration; any duration for OCD, conversion,
#   postpartum psychosis or schizotypal personality (none printed); a schizophrenia "mood episode" arrow, MDD "back to
#   baseline" and normal grief's mood/psychosis arrows (sources don't commit); illness anxiety "impairment" (Kaplan's
#   Table 12-2 has no such row); Kaplan's GAD/social anxiety tables print "≤6 mo" (an OCR slip — the text says at least 6
#   months), so FA's ≥ 6 months is used.
import sys, math
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

K5, K6, K7, K8, K10, K12, K2 = (full('Kaplan & Sadock', c) for c in (5, 6, 7, 8, 10, 12, 2))
PMS = 'OCOM Psych — SDL 12 reading: Premenstrual syndrome and premenstrual dysphoric disorder (Am Fam Physician 2016)'

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
O = lambda *k: ['dx:' + x for x in k]

# ════════ the time axis ════════
AX0, AX1, END = 640, 2240, 2306          # 0 days · 2 years · the "or longer" arrow tip
D = dict(d0=0, d1=1, d2=2, d3=3, d4=4, w1=7, w2=14, w4=28, m1=30, m3=91, m6=182, y1=365, y2=730)
def X(days):
    return round(AX0 + (AX1 - AX0) * math.log10(days + 1) / math.log10(731))
def XX(k): return X(D[k]) if isinstance(k, str) else X(k)
TICKS = [('0', 'd0'), ('1 d', 'd1'), ('3 d', 'd3'), ('4 d', 'd4'), ('1 wk', 'w1'), ('2 wk', 'w2'), ('1 mo', 'm1'),
         ('3 mo', 'm3'), ('6 mo', 'm6'), ('1 yr', 'y1'), ('2 yr', 'y2')]

# lanes → colours (the lane colour of the node, as a --dk variable for the bars)
COL = dict(psPsy='--dk7', psMood='--dk1', psStress='--dk10', psAnx='--dk6')

# ════════ the disorders ════════
# key: (label, subtitle, lane, card, bar spec)
# bar spec: list of segments (kind, start, end) — kinds: lead (light: not yet long enough), fit (solid: the diagnosis fits),
#   open (solid with an arrow: or longer), win (dashed outline: an onset window), cap (fit that stops with a bar ⊣),
#   thin (a thin second stripe under the bar), tick (a short block at a day count), plus flags: ev (◆ event at 0)
ROWS = [
  ('Psychotic disorders', [
    ('brief', 'Brief psychotic disorder', '≥ 1 day, < 1 month · then baseline', 'psPsy', 'briefpsych',
     [('lead', 'd0', 'd1'), ('cap', 'd1', 'm1')]),
    ('sfm', 'Schizophreniform disorder', '≥ 1 month, < 6 months', 'psPsy', 'briefpsych',
     [('lead', 'd0', 'm1'), ('cap', 'm1', 'm6')]),
    ('schizo', 'Schizophrenia', '≥ 6 months · ≥ 1 month active', 'psPsy', 'schizo',
     [('lead', 'd0', 'm6'), ('thin', 'd0', 'm1'), ('open', 'm6', None)]),
    ('sad', 'Schizoaffective disorder', 'psychosis alone ≥ 2 weeks', 'psPsy', 'schizoaffective',
     [('open', 'd0', None), ('thin', 'w2', 'end')]),
    ('delus', 'Delusional disorder', 'one delusion > 1 month', 'psPsy', 'delusional',
     [('lead', 'd0', 'm1'), ('open', 'm1', None)]),
  ]),
  ('Mood disorders', [
    ('mdd', 'Major depressive disorder', '≥ 2 weeks · 5 of 9 symptoms', 'psMood', 'mdd',
     [('lead', 'd0', 'w2'), ('open', 'w2', None)]),
    ('pdd', 'Persistent depressive', '≥ 2 years (≥ 1 year in children)', 'psMood', 'dysthymia',
     [('lead', 'd0', 'y2'), ('open', 'y2', None)]),
    ('seas', 'MDD, seasonal pattern', '≥ 2 consecutive years', 'psMood', 'depspec',
     [('lead', 'd0', 'y2'), ('open', 'y2', None)]),
    ('mania', 'Manic episode', '≥ 1 week, or any if hospitalized', 'psMood', 'bipolar',
     [('win', 'd0', 'w1'), ('open', 'w1', None)]),
    ('hypo', 'Hypomanic episode', '≥ 4 consecutive days', 'psMood', 'bipolar',
     [('lead', 'd0', 'd4'), ('open', 'd4', None)]),
    ('cyclo', 'Cyclothymic disorder', '≥ 2 years · symptoms half the time', 'psMood', 'bipolar',
     [('lead', 'd0', 'y2'), ('open', 'y2', None)]),
    ('pmdd', 'PMDD', 'the week before menses · most cycles', 'psMood', 'pmdd',
     [('tick', 30 * k, None) for k in range(1, 13)]),
    ('blues', 'Postpartum blues', 'starts day 2–3 · gone by 2 weeks', 'psMood', 'peripartum',
     [('ev',), ('lead', 'd0', 'd2'), ('cap', 'd2', 'w2')]),
    ('ppmdd', 'MDD, peripartum onset', 'onset ≤ 4 weeks after delivery', 'psMood', 'peripartum',
     [('ev',), ('win', 'd0', 'w4'), ('open', 'w2', None)]),
  ]),
  ('Trauma, stress & grief', [
    ('asd', 'Acute stress disorder', '3 days to 1 month after trauma', 'psStress', 'ptsd',
     [('ev',), ('lead', 'd0', 'd3'), ('cap', 'd3', 'm1')]),
    ('ptsd', 'PTSD', '> 1 month after the trauma', 'psStress', 'ptsd',
     [('ev',), ('lead', 'd0', 'm1'), ('open', 'm1', None)]),
    ('adj', 'Adjustment disorder', 'starts ≤ 3 months · ends by 6', 'psStress', 'adjustment',
     [('ev',), ('win', 'd0', 'm3'), ('cap', 'd0', 'm6')]),
    ('grief', 'Normal grief', 'adapts within 6 months', 'psStress', 'grief',
     [('ev',), ('cap', 'd0', 'm6')]),
    ('pgd', 'Prolonged grief disorder', 'at least 6–12 months', 'psStress', 'grief',
     [('ev',), ('lead', 'd0', 'm6'), ('win', 'm6', 'y1'), ('open', 'm6', None)]),
  ]),
  ('Anxiety disorders', [
    ('panic', 'Panic disorder', '≥ 1 month of worry after an attack', 'psAnx', 'panic',
     [('spike',), ('lead', 'd0', 'm1'), ('open', 'm1', None)]),
    ('gad', 'Generalized anxiety', 'most days for ≥ 6 months', 'psAnx', 'gad',
     [('lead', 'd0', 'm6'), ('open', 'm6', None)]),
    ('phob', 'Phobias', 'specific · social · agoraphobia ≥ 6 mo', 'psAnx', 'phobia',
     [('lead', 'd0', 'm6'), ('open', 'm6', None)]),
    ('sep', 'Separation anxiety', '≥ 4 weeks (children)', 'psAnx', 'separation',
     [('lead', 'd0', 'w4'), ('open', 'w4', None)]),
  ]),
  ('Somatic symptom disorders', [
    ('som', 'Somatic symptom disorder', '≥ 6 months (FA: months to years)', 'psAnx', 'somaticsx',
     [('lead', 'd0', 'm6'), ('open', 'm6', None)]),
    ('ill', 'Illness anxiety disorder', '≥ 6 months', 'psAnx', 'somaticsx',
     [('lead', 'd0', 'm6'), ('open', 'm6', None)]),
  ]),
]
INFO = {r[0]: r for _, rows in ROWS for r in rows}
KEYS = [r[0] for _, rows in ROWS for r in rows]

# the cut-off lines for each disorder (day counts, label)
CUT = dict(brief=[('d1', '1 day'), ('m1', '1 month')], sfm=[('m1', '1 month'), ('m6', '6 months')],
           schizo=[('m1', '1 mo active'), ('m6', '6 months')], sad=[('w2', '2 weeks alone')], delus=[('m1', '1 month')],
           mdd=[('w2', '2 weeks')], pdd=[('y1', 'children'), ('y2', '2 years')], seas=[('y2', '2 years')],
           mania=[('w1', '1 week')], hypo=[('d4', '4 days')], cyclo=[('y1', 'children'), ('y2', '2 years')],
           pmdd=[(60, '2 cycles rated')], blues=[('d2', 'day 2–3'), ('w2', '2 weeks')], ppmdd=[('w2', '2 weeks'), ('w4', '4 weeks')],
           asd=[('d3', '3 days'), ('m1', '1 month')], ptsd=[('m1', '1 month')], adj=[('m3', 'onset by 3 mo'), ('m6', '6 months')],
           grief=[('m6', '6 months')], pgd=[('m6', '6'), ('y1', '12 months')], panic=[('m1', '1 month')], gad=[('m6', '6 months')],
           phob=[('m6', '6 months')], sep=[('w4', '4 weeks')], som=[('m6', '6 months')], ill=[('m6', '6 months')])

# the look-alikes each disorder must be told apart from (lit the same way, so the reader decides from the clock + results)
NEAR = dict(brief=['sfm', 'asd'], sfm=['brief', 'schizo'], schizo=['sfm', 'sad', 'delus'], sad=['schizo', 'mdd', 'mania'],
            delus=['schizo', 'sfm'], mdd=['pdd', 'grief', 'adj', 'sad'], pdd=['mdd', 'cyclo'], seas=['mdd', 'pdd'],
            mania=['hypo', 'sad'], hypo=['mania', 'cyclo'], cyclo=['hypo', 'pdd'], pmdd=['mdd', 'pdd'], blues=['ppmdd'],
            ppmdd=['blues', 'mdd'], asd=['ptsd', 'adj', 'brief'], ptsd=['asd', 'adj'], adj=['asd', 'mdd', 'gad'],
            grief=['pgd', 'mdd'], pgd=['grief', 'mdd'], panic=['gad', 'phob'], gad=['panic', 'adj'], phob=['panic', 'gad'],
            sep=['gad', 'phob'], som=['ill'], ill=['som'])
LIT = {k: [k] + NEAR[k] for k in KEYS}
def lit_by(row):           # the options that light this row
    return O(*[k for k in KEYS if row in LIT[k]])

# ════════ 1. header + the big clock on top ════════
add('<rect class="dyn-soft" x="140" y="110" width="2200" height="330" rx="28"/>')
text('The clock — how long the symptoms have lasted', 170, 150, 'dyn-big')
text('◆ = the clock starts at an event (trauma, stressor, death, delivery) · the scale stretches the first days and weeks',
     170, 172, 'dyn-cap')
text('Results: ↑ needed or present · ↓ not needed or ruled out · ↔ either way', 170, 192, 'dyn-cap')
YA = 330                                   # the big clock's bar
text('Pick a disorder: its clock runs here.', AX0, 262, 'nf-l1', unless=['dx:*'])
text('Light = symptoms, not long enough yet · solid = the diagnosis fits · arrow = or longer · dashed = an onset window',
     AX0, 284, 'nf-l2', unless=['dx:*'])
add(f'<path d="M{AX0} {YA} H{END}" class="dyn-line" style="opacity:.5"/>', unless=['dx:*'])

def segs(key, y, h, big):
    """the bar for one disorder at height y (h = bar thickness)"""
    lane = INFO[key][3]; c = COL[lane]; out = []
    for s in INFO[key][5]:
        k = s[0]
        if k == 'ev':
            r = 13 if big else 8
            out.append(f'<path d="M{AX0} {y - r} L{AX0 + r} {y} L{AX0} {y + r} L{AX0 - r} {y} Z" style="fill:var(--ink-2)"/>')
            continue
        if k == 'spike':
            r = 14 if big else 9
            out.append(f'<path d="M{AX0 - r} {y + r} L{AX0 - 3} {y - r} L{AX0 + 3} {y + r * .3} L{AX0 + r} {y - r}" class="dyn-line" style="stroke:var(--ink-2);stroke-width:{3 if big else 2.5}"/>')
            continue
        x0 = XX(s[1]); x1 = END if s[2] is None else AX1 + 30 if s[2] == 'end' else XX(s[2])
        if k == 'lead':
            out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{max(4, x1 - x0)}" height="{h}" rx="{h / 2}" style="fill:var({c});fill-opacity:.16"/>')
        elif k == 'win':
            out.append(f'<rect x="{x0}" y="{y - h / 2 - 5}" width="{max(6, x1 - x0)}" height="{h + 10}" rx="{h / 2 + 4}" '
                       f'style="fill:none;stroke:var({c});stroke-width:2.5;stroke-dasharray:6 5"/>')
        elif k in ('fit', 'cap', 'open'):
            tip = h * .9 if k == 'open' else 0
            out.append(f'<rect x="{x0}" y="{y - h / 2}" width="{max(6, x1 - x0 - tip)}" height="{h}" rx="{min(6, h / 2)}" style="fill:var({c});fill-opacity:.75"/>')
            if k == 'open':
                out.append(f'<path d="M{x1 - tip - 1} {y - h / 2 - 5} L{x1} {y} L{x1 - tip - 1} {y + h / 2 + 5} Z" style="fill:var({c});fill-opacity:.75"/>')
            else:
                out.append(f'<path d="M{x1} {y - h / 2 - 6} V{y + h / 2 + 6}" class="dyn-line" style="stroke:var({c});stroke-width:4"/>')
        elif k == 'thin':
            out.append(f'<rect x="{x0}" y="{y + h / 2 + 3}" width="{max(6, x1 - x0)}" height="{max(4, h / 3)}" rx="2" style="fill:var(--ink-2);fill-opacity:.7"/>')
        elif k == 'tick':
            out.append(f'<rect x="{x0 - 4}" y="{y - h / 2}" width="9" height="{h}" rx="3" style="fill:var({c});fill-opacity:.8"/>')
    return ''.join(out)

# the big clock for each disorder: bar, title (hidden while naming it), captions under the bar
CAP = dict(  # captions under the big bar — (x in days or key, text)
  brief=[('d1', 'from 1 day — full return to baseline before 1 month')],
  sfm=[('m1', 'from 1 month — still under 6 months')],
  schizo=[('d0', 'active symptoms ≥ 1 month (dark stripe) within ≥ 6 months of illness')],
  sad=[('d0', 'psychosis throughout'), ('w2', 'mood episodes (dark stripe) for most of the illness — but ≥ 2 weeks of psychosis alone')],
  delus=[('m1', 'often nonbizarre — no mood disorder, no other psychotic symptoms')],
  mdd=[('w2', 'from 2 weeks — depressed mood or anhedonia + 4 more')],
  pdd=[('d0', 'depressed most days — any remission ≤ 2 months · children: 1 year')],
  seas=[('d0', 'episodes only in one season (usually winter), 2 years running')],
  mania=[('d0', 'dashed: any length if hospitalized'), ('w1', 'from 1 week — DIG FAST, marked impairment')],
  hypo=[('d4', 'from 4 consecutive days — no marked impairment, no psychosis')],
  cyclo=[('d0', 'mild highs and lows half the time — any remission ≤ 2 months · children: 1 year')],
  pmdd=[('d0', 'each block = the week before menses · in most cycles of the past year · confirmed over 2 cycles')],
  blues=[('d2', 'tearful from day 2–3 after delivery — resolves within 2 weeks')],
  ppmdd=[('d0', 'dashed: onset in pregnancy or ≤ 4 weeks after delivery · then full MDD criteria (≥ 2 weeks)')],
  asd=[('d3', 'from 3 days to 1 month after the trauma')],
  ptsd=[('m1', 'beyond 1 month — intrusions, avoidance, mood change, arousal')],
  adj=[('d0', 'dashed: starts within 3 months · solid: gone within 6 months after the stressor ends')],
  grief=[('d0', 'yearning, sadness — adapting within about 6 months · not a disorder')],
  pgd=[('m6', 'dashed: still intense at 6–12 months, impairing')],
  panic=[('d0', 'an attack'), ('m1', 'then ≥ 1 month of worry or changed behavior')],
  gad=[('m6', 'worry about many things, most days, ≥ 6 months')],
  phob=[('m6', 'fear of a specific object or situation, ≥ 6 months')],
  sep=[('w4', 'fear of separation ≥ 4 weeks — normal up to age 3–4')],
  som=[('m6', 'bodily complaints + excessive worry about them')],
  ill=[('m6', 'fear of having an illness — few or no symptoms')],
)
for k in KEYS:
    _, lab, sub, lane, cid, spec = INFO[k]
    add(f'<path d="M{AX0} {YA} H{END}" class="dyn-line" style="opacity:.45"/>' + segs(k, YA, 30, True), when=O(k))
    text(lab, AX0, 262, 'dyn-big', when=O(k))
    text(sub, AX0, 284, 'nf-l2', when=O(k))
    for i, (at, t) in enumerate(CAP[k]):
        x = XX(at) if at != 'd0' else AX0
        if len(CAP[k]) > 1 and i == 0: text(t, x, 394, TAG, when=O(k))
        else: text(t, x, 394 if len(CAP[k]) == 1 else 416, TAG, when=O(k))

# ════════ 2. the axis ════════
YT = 476                                    # tick labels
YB0 = 492                                   # ladder top
for lab, k in TICKS:
    x = XX(k)
    text(lab, x, YT, 'nf-l2', 'middle')
add(f'<path d="M{AX0} {YT + 10} H{END}" class="dyn-line"/>' +
    ''.join(f'<path d="M{XX(k)} {YT + 4} V{YT + 16}" class="dyn-line"/>' for _, k in TICKS))

# ════════ 3. the ladder ════════
PITCH, HEAD = 54, 50
y = YB0 + 36
nodes = []
ROWY = {}
for si, (sec, rows) in enumerate(ROWS):
    text(sec, 150, y + 6, 'dyn-big')
    add(f'<path d="M{150 + len(sec) * 8.6 + 16} {y} H{END}" class="dyn-line" style="opacity:.35"/>')
    y += HEAD
    for (k, lab, sub, lane, cid, spec) in rows:
        ROWY[k] = y
        nodes.append((f'pc{len(nodes) + 1}', lab, 370, y, lane, sub, [cid]))
        y += PITCH
    y += 6
YEND = y - 6
# grid lines (behind everything, so first in the list)
grid = ''.join(f'<path d="M{XX(k)} 214 V{YEND}" class="dyn-line" style="stroke-dasharray:2 8;opacity:.4"/>' for _, k in TICKS[1:])
shapes.insert(0, grid)
# each row: track, bar; lit (the pick + its look-alikes): a band; the pick: ▶, the look-alikes: "look-alike"
for k in KEYS:
    yy = ROWY[k]
    add(f'<rect x="146" y="{yy - 26}" width="2184" height="52" rx="16" style="fill:var(--accent);fill-opacity:.09;stroke:var(--accent);stroke-opacity:.5;stroke-width:2"/>',
        when=lit_by(k))
    add(f'<path d="M{AX0} {yy} H{END}" class="dyn-line" style="opacity:.25"/>' + segs(k, yy, 14, False))
    text('▶ this one', 160, yy + 4, TAG, when=O(k))
    of = [q for q in KEYS if k in NEAR[q]]
    if of: text('look-alike', 160, yy + 4, 'nf-l2', when=O(*of))

# the cut-off lines through the ladder + their labels on the big clock
for k in KEYS:
    svg = ''
    for at, lab in CUT[k]:
        x = XX(at)
        svg += f'<path d="M{x} 300 V{YEND}" style="fill:none;stroke:var(--bad);stroke-width:2.5;stroke-dasharray:8 6;opacity:.75"/>'
    add(svg, when=O(k))
    for i, (at, lab) in enumerate(CUT[k]):
        x = XX(at)
        text(lab, x + 6, 308 if i % 2 == 0 else 360, 'nf-l1', when=O(k))

# ════════ particles: the clock running ════════
kinds = dict(clock=['clock', '--dk2'], lit=['clock', '--ink-3'])
groups = [['clock', 'Clock']]
def run_end(k):
    ends = [s for s in INFO[k][5] if s[0] in ('fit', 'cap', 'open')]
    if not ends: return 2000
    s = ends[-1]
    return END if s[2] is None else XX(s[2])
flows = [dict(d=f'M{AX0} {YA} H{END}', len=END - AX0, speed=160, unless=['dx:*'], base=dict(clock=4))]
for k in KEYS:
    e = run_end(k)
    flows.append(dict(d=f'M{AX0} {YA} H{e}', len=e - AX0, speed=150, r=8, when=O(k), base=dict(clock=max(2, round((e - AX0) / 320)))))
for k in KEYS:     # the lit rows in the ladder
    e = run_end(k); yy = ROWY[k]
    flows.append(dict(d=f'M{AX0} {yy} H{e}', len=e - AX0, speed=130, r=5, when=lit_by(k), base=dict(lit=2)))

# ════════ notes ════════
notes = {
  '': 'Most psychiatric diagnoses turn on the clock: the same symptoms get a different name at 1 day, 1 month, 6 months or 2 '
      'years. Pick a disorder — its window runs on top, its cut-offs drop through the ladder, and its look-alikes light up.',
  'dx:brief': 'Brief psychotic disorder: at least one positive symptom (delusions, hallucinations, disorganized speech) for 1 day to '
              'under 1 month, often after a stressor, with a full return to baseline. Past 1 month it becomes schizophreniform.',
  'dx:sfm': 'Schizophreniform disorder: the schizophrenia picture (≥ 2 symptoms) for at least 1 month but under 6 months, then back '
            'to baseline. If the illness passes 6 months, the diagnosis becomes schizophrenia — most patients do progress.',
  'dx:schizo': 'Schizophrenia: ≥ 2 of delusions, hallucinations, disorganized speech, disorganized or catatonic behavior, negative '
               'symptoms (one from the first three) — illness ≥ 6 months with ≥ 1 month of active symptoms, profound impairment. '
               'Atypical antipsychotics are first line.',
  'dx:sad': 'Schizoaffective disorder: full MDE or manic episodes for most of the illness, yet ≥ 2 weeks of psychosis with no mood '
            'episode. Psychosis only inside mood episodes is a mood disorder with psychotic features instead.',
  'dx:delus': 'Delusional disorder: one or more delusions for more than 1 month, without a mood disorder or other psychotic '
              'symptoms; apart from the belief, functioning is largely spared. It can be shared by a close companion (folie à deux).',
  'dx:mdd': 'Major depressive disorder: ≥ 5 of 9 symptoms (SIG E CAPS), including depressed mood or anhedonia, for ≥ 2 weeks with '
            'distress or impairment. Psychotic features can occur. Screen for past mania or hypomania; CBT and SSRIs are first line.',
  'dx:pdd': 'Persistent depressive disorder (dysthymia): milder depressive symptoms (≥ 2) most days for ≥ 2 years — ≥ 1 year in '
            'children — with any remission lasting ≤ 2 months. Full MDE criteria may be met along the way.',
  'dx:seas': 'MDD with seasonal pattern: major depressive episodes only in one season, usually winter, for ≥ 2 consecutive years '
             'and in most years. Atypical symptoms are common; add light therapy to standard MDD treatment.',
  'dx:mania': 'Manic episode: elevated or irritable mood with more energy and ≥ 3 DIG FAST symptoms for ≥ 1 week — or any length '
              'if hospitalization is needed — with marked impairment. Psychotic features are possible. One manic episode = bipolar I.',
  'dx:hypo': 'Hypomanic episode: the same symptoms for ≥ 4 consecutive days, but not severe enough for marked impairment or '
             'hospitalization, and never psychotic. Hypomania plus a major depressive episode = bipolar II.',
  'dx:cyclo': 'Cyclothymic disorder: mild hypomanic and depressive symptoms that never reach a full episode, present at least half '
              'the time for ≥ 2 years (≥ 1 year in children), with any remission lasting ≤ 2 months.',
  'dx:pmdd': 'Premenstrual dysphoric disorder: ≥ 5 symptoms in the week before menses, easing within days of menses and gone the week '
             'after, in most cycles of the past year, with distress or impairment — confirmed by daily ratings over 2 cycles. SSRIs first.',
  'dx:blues': 'Postpartum blues: tearfulness, depressed affect and fatigue starting 2–3 days after delivery and resolving within 2 '
              'weeks (50–85% of mothers). Supportive care, with follow-up to check for MDD with peripartum onset.',
  'dx:ppmdd': 'MDD with peripartum onset: full MDD criteria (≥ 2 weeks) with onset during pregnancy or within 4 weeks after delivery '
              '(10–15%). CBT and SSRIs are first line; the blues, by contrast, resolve within 2 weeks.',
  'dx:asd': 'Acute stress disorder: after a trauma, PTSD-type symptoms (≥ 9 from any domain) lasting 3 days to 1 month. The time '
            'course is what separates it from PTSD. CBT; medication usually not needed.',
  'dx:ptsd': 'PTSD: after a life-threatening trauma, intrusive re-experiencing, avoidance, negative mood or cognition and '
             'hyperarousal lasting more than 1 month, with distress or impairment. CBT, SSRIs, venlafaxine; prazosin for nightmares.',
  'dx:adj': 'Adjustment disorder: emotional or behavioral symptoms within 3 months of an identifiable stressor that fall short of '
            'another disorder and fade within 6 months after the stressor ends. Beyond that, look again for MDD or GAD. CBT first.',
  'dx:grief': 'Normal grief after a death: sadness, yearning, guilt, even hallucinations of the deceased, adapting within about '
              '6 months. It is not a disorder; MDD is diagnosed only if its own criteria are met.',
  'dx:pgd': 'Prolonged grief disorder: grief that stays intense and impairing for at least 6–12 months, beyond cultural norms, and '
            'is not better explained by another disorder such as MDD.',
  'dx:panic': 'Panic disorder: recurrent panic attacks (peak within about 10 minutes, ≥ 4 symptoms) followed by ≥ 1 month of '
              'worry about more attacks or a change in behavior. CBT, SSRIs or venlafaxine; benzodiazepines only acutely.',
  'dx:gad': 'Generalized anxiety disorder: excessive worry about many everyday things on most days for ≥ 6 months, with ≥ 3 of '
            'restlessness, fatigue, poor concentration, irritability, muscle tension, poor sleep. CBT, SSRIs, SNRIs first line.',
  'dx:phob': 'Phobias — specific, social anxiety, agoraphobia: fear or avoidance of a particular object or situation lasting ≥ 6 '
             'months, out of proportion and causing distress. CBT with exposure; SSRIs for social anxiety and agoraphobia.',
  'dx:sep': 'Separation anxiety disorder: overwhelming fear of separation from home or an attachment figure for ≥ 4 weeks — which '
            'can be normal up to age 3–4. CBT, play therapy and family therapy.',
  'dx:som': 'Somatic symptom disorder: ≥ 1 bodily complaint with excessive, persistent thoughts and anxiety about it, ≥ 6 months by '
            'DSM-5 (months to years). Not feigned. Regular visits with the same physician; avoid needless tests.',
  'dx:ill': 'Illness anxiety disorder: ≥ 6 months of preoccupation with having or getting a serious illness despite evaluation, '
            'with few or no somatic symptoms — the opposite balance from somatic symptom disorder.',
}

# ════════ readouts: criteria (↑ needed or present · ↓ not needed or ruled out · ↔ either way) ════════
R = lambda keys, d: dict(when=O(*keys), d=d)
readouts = [
  dict(l='Needs ≥ 1 month', mods=[R(['sfm', 'schizo', 'delus', 'pdd', 'seas', 'cyclo', 'ptsd', 'pgd', 'panic', 'gad', 'phob', 'som', 'ill'], 1),
                                  R(['brief', 'mdd', 'mania', 'hypo', 'blues', 'ppmdd', 'asd'], -1)]),
  dict(l='Needs ≥ 6 months', mods=[R(['schizo', 'pdd', 'seas', 'cyclo', 'pgd', 'gad', 'phob', 'som', 'ill'], 1),
                                   R(['brief', 'sfm', 'delus', 'mdd', 'mania', 'hypo', 'blues', 'ppmdd', 'asd', 'ptsd', 'adj', 'panic', 'sep'], -1)]),
  dict(l='Psychosis', mods=[R(['brief', 'sfm', 'schizo', 'sad', 'delus'], 1), R(['hypo'], -1), R(['mdd', 'mania'], 0)]),
  dict(l='Mood episode', mods=[R(['sad', 'mdd', 'seas', 'mania', 'hypo', 'ppmdd'], 1), R(['delus', 'cyclo', 'adj', 'pgd'], -1), R(['pdd'], 0)]),
  dict(l='Distress or impairment', mods=[R(['schizo', 'sad', 'mdd', 'seas', 'pdd', 'mania', 'cyclo', 'pmdd', 'ppmdd', 'asd', 'ptsd', 'adj',
                                            'pgd', 'gad', 'phob', 'som'], 1), R(['delus', 'hypo'], -1)]),
  dict(l='Back to baseline', mods=[R(['brief', 'sfm', 'mania', 'hypo', 'pmdd', 'blues', 'adj', 'grief'], 1),
                                   R(['schizo', 'pdd', 'cyclo', 'pgd'], -1)]),
  dict(l='Stressor first', mods=[R(['asd', 'ptsd', 'adj', 'grief', 'pgd'], 1), R(['brief'], 0)]),
]

OPT = dict(brief='Brief psychotic', sfm='Schizophreniform', schizo='Schizophrenia', sad='Schizoaffective', delus='Delusional',
           mdd='Major depressive', pdd='Persistent depressive', seas='Seasonal pattern', mania='Manic episode', hypo='Hypomanic episode',
           cyclo='Cyclothymic', pmdd='PMDD', blues='Postpartum blues', ppmdd='Peripartum MDD', asd='Acute stress', ptsd='PTSD',
           adj='Adjustment', grief='Normal grief', pgd='Prolonged grief', panic='Panic', gad='GAD', phob='Phobias',
           sep='Separation anxiety', som='Somatic symptom', ill='Illness anxiety')
dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='dx', label='Disorder', type='one', options=[[k, OPT[k], INFO[k][4]] for k in KEYS],
                 sections=[[sec.split(' disorders')[0].replace('Somatic symptom', 'Somatic'), [r[0] for r in rows]] for sec, rows in ROWS])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM Psych SDL 12 (PMDD) · First Aid pp. 572, 574, 576–581, 583 · Kaplan & Sadock ch 2, 5–8, 10, 12')

MAP = dict(
  id='psychclock', title='Psychiatric Timelines', topic='behav', after='psychdx',
  sub='The duration rules on one clock — brief psychotic → schizophreniform → schizophrenia, MDD vs persistent depressive, mania vs '
      'hypomania, acute stress vs PTSD, adjustment, grief, anxiety and somatic disorders: pick one, watch its window, cut-offs '
      'and look-alikes, and read the criteria (↑ needed · ↓ ruled out · ↔ either). Tap a disorder for its card',
  w=3500, h=YEND + 60,
  fa='572, 574, 576–581, 583', src=[PMS, K2, K5, K6, K7, K8, K10, K12],
  lanes=[('psPsy', 'Psychotic disorders', 'sugars'), ('psMood', 'Mood disorders', 'glycolysis'),
         ('psStress', 'Trauma, stress & grief', 'glycogen'), ('psAnx', 'Anxiety & somatic', 'ppp')],
  comps=[],
  nodes=nodes,
  panels=[
    (2420, 920, 1000, 'When the clock runs out (First Aid pp. 572, 577, 581; Kaplan ch 5, 10)', [
      ('Brief psychotic > 1 mo', 'now schizophreniform'),
      ('Schizophreniform > 6 mo', 'now schizophrenia (Kaplan ch 5)'),
      ('Acute stress > 1 mo', 'PTSD — the time course is the difference (Kaplan ch 10)'),
      ('Adjustment > 6 mo', 'after the stressor ends: re-evaluate for MDD or GAD'),
      ('Grief at 6–12 mo', 'still intense and impairing: prolonged grief disorder')]),
    (2420, 1110, 1000, 'Children run on different clocks (First Aid pp. 574, 578; Kaplan ch 6)', [
      ('Persistent depressive', '≥ 1 year in children (≥ 2 in adults)'),
      ('Cyclothymic', '≥ 1 year in children (Kaplan ch 6)'),
      ('Separation anxiety', '≥ 4 weeks · can be normal up to age 3–4'),
      ('Selective mutism', '≥ 1 month · onset before age 5'),
      ('Oppositional defiant', '≥ 6 months'),
      ('Tourette syndrome', 'tics for > 1 year · onset before 18')]),
  ],
  dyn=dyn,
)
