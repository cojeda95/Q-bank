# m56 — The Mental Status Exam in Motion (dynamic map, kit data)
# ONE patient, the whole cross-sectional exam: pick a presentation and the MSE form fills in, row by row, in the order it is
# written (appearance & behavior · speech · mood & affect · thought process · thought content · suicidal ideation ·
# perception · sensorium & cognition · insight & judgment). Each row has a moving part: the words of the speech stream
# (pressured, sparse, jumbled), the train of thought from the question to its point (linear, flight of ideas, loose,
# fragmented, slowed), a mood marker, the OCD obsession → compulsion loop, the suicide ladder (ideation → intent → plan →
# means), the hallucination chips (auditory, visual, tactile…), and a 24-hour consciousness trace (flat and alert, waxing and
# waning, hyperalert). The strip at the bottom names the class — primary psychiatric · medical, neurologic or substance ·
# normal experience — and pins each disorder's card. A second switch overlays the safety questions (passive SI, a plan
# with means, command hallucinations) on any presentation.
# psychmse (static) lays out the interview and the parts of the MSE; this map runs the same form for each presentation —
# a natural ⇄ pair with psychmse. psychclock owns durations (none are drawn here); demsim owns the dementia types.
# Readouts: ↑ raised or present · ↓ lowered or lost · ↔ normal or absent · "–" no source commits.
#
# Sources (all read; Kaplan & Sadock ch 1 IS the OCOM Psych SDL 8–9 course reading — the course PDF "SDL 8:9; Psych interview
# and exam" is that chapter — so the course text and Kaplan ch 1 agree by construction):
#   Kaplan & Sadock ch 1 (course SDL 8–9): MSE = psychiatric equivalent of the physical exam, a snapshot, written in order;
#     appearance (dress, grooming, hygiene, eye contact), motor activity (slowed vs agitated, tics, tremor); speech (fluency,
#     amount, rate, tone, volume; increased amount often mania; decreased: anxiety to thought blocking or psychosis); mood
#     (patient's own words) vs affect (quality, quantity, range — restricted, normal, labile, flat in some schizophrenia —
#     appropriateness, congruence); thought content (obsessions ego-alien and resisted, compulsions to avoid anxiety,
#     delusions bizarre/nonbizarre, ideas of reference, paranoia; suicidality: ideation, intent, plan, preparation; passive SI
#     = thoughts without intent; plan specificity and access to means; hallucinations may compel self-harm without a wish
#     to die; ask what has kept them from acting); thought process (linear, organized, goal-directed; flight of ideas fast but
#     connected; circumstantial; tangential; loose; perseveration; blocking; word salad; neologisms; Table 1-4); perception
#     (auditory commonest in psychiatric settings; nonauditory = clue to a neurologic, medical or withdrawal cause; illusion =
#     misperception; hypnagogic may be normal — people without psychosis may hear their name or see flashes; ask about command
#     hallucinations and whether ever compelled to follow them); cognition (alertness, orientation, concentration, memory,
#     abstraction; Table 1-5); insight (none / partial / full; not a measure of severity) and judgment (real situations, danger,
#     taking part in care). Table 1-6 hints: unkempt in cognitive disorder; withdrawal and stooped posture in depression;
#     fixed posturing, odd behavior, minimal eye contact in schizophrenia; hyperactive with cocaine and in mania; psychomotor
#     retardation in depression; elation in mania; loss of prosody in cognitive disorder; pressured speech in mania, paucity
#     in depression, uneven or slurred speech in cognitive disorders; tactile hallucinations suggest cocaine, DTs;
#     mood-incongruent delusions point to schizophrenia; thought insertion characteristic of schizophrenia; illusions common in
#     delirium; loose associations → schizophrenia, flight of ideas → mania, inability to abstract → schizophrenia; delirium or
#     dementia: clouded or wandering sensorium; Alzheimer retains remote memory longer than recent; rule out a medical cause
#     for deficits vs depression (pseudodementia); judgment impaired in brain disease, schizophrenia, intoxication; insight
#     impaired in delirium, dementia, psychosis. Speech: slowed in depression; a slow, low-pitched, hoarse voice suggests
#     hypothyroidism.
#   Kaplan & Sadock ch 3: Table 3-5 delirium — altered (usually decreased) consciousness, inattention, disorientation
#     (especially time and space), rapid onset, marked fluctuations, sundowning, EEG diffuse slowing; Table 3-8 delirium vs
#     dementia (dementia usually alert, attention impaired to a lesser degree, rare hallucinations, may be paranoid, judgment
#     initially relatively intact, insidious, stable over the day; delirium prominent visual or tactile hallucinations,
#     grossly impaired judgment, acute, fluctuates); schizophrenia — hallucinations and delusions more constant and organized,
#     usually no change in consciousness or orientation; hypothyroidism "myxedema madness" (paranoia, depression, hypomania,
#     hallucinations; slowed thinking, delirium; weight gain, deep voice, thin dry hair, lost lateral eyebrow, facial
#     puffiness); high-dose exogenous corticosteroids → secondary mood disorder similar to mania, severe depression after
#     stopping; hyperthyroidism, Cushing, Addison psychiatric pictures.
#   Kaplan & Sadock ch 4: alcohol withdrawal — tremulousness the classic sign, autonomic hyperactivity, generally alert;
#     alcohol withdrawal delirium (DTs) within 1 week, Table 4-6 (delirium, confusion, disorientation, hallucinations —
#     tactile common — delusions, tachycardia, diaphoresis, fever, hypertension, anxiety, insomnia, fluctuating psychomotor
#     activity), untreated mortality 20%.
#   Kaplan & Sadock ch 5: Tables 5-3/5-7 exclusions (substance use, another medical condition); classically poor insight in
#     schizophrenia; Table 5-8 medical etiologies of delusional syndromes (corticosteroids, amphetamines, cocaine, alcohol,
#     hallucinogens, hypo-/hyperthyroidism…); pursue a medical cause with any variation in the level of consciousness.
#   Kaplan & Sadock ch 6: mania — orientation and memory grossly intact; impaired judgment a hallmark; little insight;
#     bright, outlandish clothing; Table 6-1 exclusions (medical condition, substance).
#   Kaplan & Sadock ch 7: psychotic depression — delusions or hallucinations, mood-congruent (guilt, sin, worthlessness,
#     poverty, failure, persecution, terminal illness); Table 7-2 exclusions (medical illness, substance).
#   Kaplan & Sadock ch 9: OCD — patients typically have good insight that the OCD beliefs are not real; some poor, few none.
#   DeGowin ch 15: less than fully alert = organic neurologic disorder until proven otherwise; Mini-Cog, SLUMS; mood normal /
#     depressed / elevated, depressed patients may have blunted affect with little range; hallucinations (auditory common in
#     schizophrenia, visual more typical of delirium); hypnagogic/hypnopompic hallucinations do not indicate pathology without
#     other symptoms; delirium (inattentiveness, fluctuating mental status, disorientation for time and place, illusions,
#     mostly visual hallucinations, fragmented thoughts, delusions, restless, picking at bedclothes, hypoactive form; causes
#     include steroids; often confused with a primary psychiatric disorder); suicide (specific plan, firearms already owned
#     → highest risk; every threat taken seriously; immediate psychiatric consultation; keep the patient safe).
#   First Aid 2025 p. 119 (glucocorticoid adverse effects include psychosis) · p. 534 (dementia: decline with intact
#     consciousness; reversible causes — depression/pseudodementia, hypothyroidism, B12, neurosyphilis, NPH) · p. 572 (grief:
#     guilt, sadness, yearning, somatic symptoms, hallucinations of the deceased, transient wishes to have died with or
#     instead of them; not a disorder; adapts within 6 months) · p. 575 (orientation; delirium: waxing and waning consciousness,
#     ↓ attention, ↓ arousal, disorganized thinking, hallucinations often visual, illusions, usually secondary, reversible) ·
#     p. 576 (psychosis = delusions, hallucinations and/or disorganized thought; delusion types; word salad, tangential,
#     derailed; hallucination types incl. hypnagogic/hypnopompic, sometimes narcolepsy; illusions) · p. 577 (schizophrenia:
#     ≥ 2 of delusions, hallucinations often auditory, disorganized speech, disorganized or catatonic behavior, negative
#     symptoms incl. blunted affect; cognitive symptoms incl. inattention; delusional disorder: no mood disorder or other
#     psychotic symptoms, functioning otherwise unaffected; folie à deux; manic episode DIG FAST) · p. 578 (MDD SIG E CAPS;
#     MDD with psychotic features: mood-congruent, only within the episode) · p. 579 (SAD PERSONS: organized plan, stated
#     future intent; firearms; anxiety disorders incl. OCD not attributable to a medical condition or substance) · p. 580
#     (OCD: obsessions, compulsions; poor insight linked to worse outcomes) · p. 587 (DTs 2–4 days after the last drink:
#     altered mental status, hallucinations, autonomic hyperactivity, anxiety, tremor, agitation) · p. 588 (alcohol withdrawal
#     tremor, diaphoresis, agitation; stimulants: mood elevation, psychomotor agitation; amphetamines: euphoria, grandiosity,
#     mydriasis, prolonged wakefulness, hyperalertness, paranoia, fever, meth mites) · p. 589 (cocaine: impaired judgment,
#     mydriasis, hallucinations incl. formication, paranoia; LSD: visual and auditory perceptual distortion,
#     depersonalization, anxiety, paranoia, psychosis, flashbacks, mydriasis).
# Conflicts for the owner (the higher source is printed):
#   Kaplan Table 1-6 says "Visual hallucinations suggest schizophrenia" — Kaplan's own text (ch 1), FA 576 and DeGowin all say
#     visual hallucinations point to delirium, dementia or intoxication; the text + FA version is used.
#   Alcoholic hallucinosis: FA 588 "usually visual"; Kaplan ch 4 describes mostly auditory voices with a clear sensorium.
#     This map shows DTs only (Kaplan Table 4-6: tactile common; FA 587), not hallucinosis.
#   Kaplan Table 3-8 prints dementia memory "more long-term than short-term" — opposite to Table 1-6 ("remote memory retained
#     longer than recent"); Table 1-6 is printed.
# Cut for lack of support: a thought-process arrow for MDD, OCD, DTs, stimulants, steroids or hypothyroidism (no source names
#   one); speech for delirium, OCD, LSD, steroids; a mood arrow for schizophrenia, delirium, dementia, DTs, LSD and
#   hypothyroidism (depression OR hypomania); psychosis for mania (only "possible"); insight for MDD, delusional disorder,
#   DTs, intoxications, grief and hypnagogic hallucinations; which orientation spheres are lost outside delirium; any arrow
#   for grief besides mood; a cause arrow for hypnagogic hallucinations (normal, or sometimes narcolepsy) and grief.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

K1, K3, K4, K5, K6, K7, K9 = (full('Kaplan & Sadock', c) for c in (1, 3, 4, 5, 6, 7, 9))
DG15 = 'DeGowin ch 15 — The Mental Status, Psychiatric, and Social Evaluations'

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
O = lambda *k: ['p:' + x for x in k]
RK = lambda *k: ['risk:' + x for x in k]
TAG = 'nf-l2 dyn-tag'

# ════════ the presentations ════════
# key, chip label, card, class (pri · sec · norm), node label, node subtitle, extra cards on the node
PRES = [
  ('norm', 'Normal adult', 'mse', None, None, None, []),
  ('schizo', 'Acute schizophrenia', 'schizo', 'pri', 'Schizophrenia', 'loose · voices · poor insight', []),
  ('mania', 'Mania', 'bipolar', 'pri', 'Mania (bipolar I)', 'pressured · flight of ideas', []),
  ('mddp', 'MDD with psychotic features', 'mdd', 'pri', 'MDD, psychotic features', 'mood-congruent delusions', []),
  ('delus', 'Delusional disorder', 'delusional', 'pri', 'Delusional disorder', 'one belief · rest intact', []),
  ('ocd', 'OCD (insight kept)', 'ocd', 'pri', 'OCD', 'obsessions · insight kept', []),
  ('delir', 'Delirium', 'delirium', 'sec', 'Delirium', 'waxes and wanes · visual', []),
  ('ncd', 'Major neurocognitive (Alzheimer)', 'alzheimer', 'sec', 'Major NCD (Alzheimer)', 'alert · memory lost', ['dementiarev']),
  ('dts', 'Alcohol withdrawal → DTs', 'alcoholwd', 'sec', 'Delirium tremens', 'tremor · tactile · autonomic', []),
  ('stim', 'Stimulant intoxication', 'cocaine', 'sec', 'Stimulant intoxication', 'hyperalert · bugs on skin', ['stimulants']),
  ('lsd', 'LSD intoxication', 'hallucinogens', 'sec', 'LSD (hallucinogen)', 'visual distortion', []),
  ('ster', 'High-dose corticosteroids', 'mimics', 'sec', 'Steroid-induced', 'mania-like · psychosis', []),
  ('hypot', 'Hypothyroidism', 'hypothyroid', 'sec', 'Hypothyroidism', 'slowed · “myxedema madness”', []),
  ('hypna', 'Hypnagogic hallucination', 'perception', 'norm', 'Hypnagogic hallucination', 'falling asleep · no psychosis', ['narcolepsy']),
  ('grief', 'Normal grief', 'grief', 'norm', 'Normal grief', 'may sense the deceased', []),
]
INFO = {p[0]: p for p in PRES}
KEYS = [p[0] for p in PRES]
SEC = [('Baseline', ['norm']),
       ('Primary psychiatric', ['schizo', 'mania', 'mddp', 'delus', 'ocd']),
       ('Medical, neurologic or substance', ['delir', 'ncd', 'dts', 'stim', 'lsd', 'ster', 'hypot']),
       ('Normal experiences', ['hypna', 'grief'])]
CLS = {k: INFO[k][3] for k in KEYS}

# ════════ the MSE form: rows ════════
FX, WX0, WX1 = 590, 1590, 2320           # findings text x · widget band x
ROWS = [  # key, y centre, half-height, node label, node subtitle, cards
  ('app', 262, 40, 'Appearance & behavior', 'dress · grooming · motor', ['mse']),
  ('spe', 350, 40, 'Speech', 'amount · rate · tone · volume', ['mse']),
  ('moo', 440, 42, 'Mood & affect', 'reported vs observed', ['moodaffect']),
  ('pro', 556, 62, 'Thought process', 'how ideas connect', ['thoughtproc']),
  ('con', 690, 60, 'Thought content', 'delusions · obsessions', ['thoughtcont']),
  ('si', 808, 48, 'Suicidal ideation', 'ideation · intent · plan · means', ['suicideassess', 'suicide']),
  ('per', 906, 42, 'Perception', 'hallucination vs illusion', ['perception']),
  ('sen', 1018, 62, 'Sensorium & cognition', 'alert? oriented? attending?', ['cogscreen']),
  ('ins', 1134, 40, 'Insight & judgment', 'knowing vs deciding', ['insightjudg', 'capacity']),
]
RY = {r[0]: r[1] for r in ROWS}

# header
add('<rect class="dyn-soft" x="140" y="104" width="2200" height="104" rx="26"/>')
text('One patient, one exam — the MSE, written top to bottom', 170, 140, 'dyn-big')
text('Pick a presentation: every row fills in and its moving part changes. Names: the strip at the bottom.', 170, 164, 'dyn-cap')
text('Results: ↑ raised or present · ↓ lowered or lost · ↔ normal or absent · – no source commits', 170, 186, 'dyn-cap')
VERD = dict(pri=('Primary psychiatric', 'still rule out a medical cause first'),
            sec=('Medical, neurologic or substance', 'treat the cause — the psychiatric picture is secondary'),
            norm=('A normal experience', 'not a disorder on its own'))
text('Verdict', 1600, 140, 'nf-l2')
text('Pick a presentation', 1600, 162, 'dyn-big', unless=['p:*'])
text('the class appears here', 1600, 184, 'nf-l2', unless=['p:*'])
text('Normal exam', 1600, 162, 'dyn-big', when=O('norm'))
text('the reference for every other row', 1600, 184, 'nf-l2', when=O('norm'))
for c, (h, s) in VERD.items():
    ks = [k for k in KEYS if CLS[k] == c]
    text(h, 1600, 162, 'dyn-big', when=O(*ks))
    text(s, 1600, 184, 'nf-l2', when=O(*ks))

nodes = []
for i, (k, y, hh, lab, sub, cards) in enumerate(ROWS):
    add(f'<rect x="140" y="{y - hh}" width="2200" height="{2 * hh}" rx="14" '
        f'style="fill:var(--surface-2);fill-opacity:{.55 if i % 2 == 0 else .2};stroke:var(--line-2);stroke-width:1.5"/>')
    nodes.append((f'ms{len(nodes) + 1}', lab, 340, y, 'msExam', sub, cards))

# ════════ findings, row by row ════════
# (headline, detail) per row; None = nothing sourced → a dash
B = dict(  # the blank form: what you record (Kaplan ch 1)
  app=('What to note: dress, grooming, hygiene, eye contact, motor activity', 'slowed or agitated? tics, tremor, restlessness — clues to depression vs mania or a drug side effect'),
  spe=('Fluency · amount · rate · tone · volume', 'an increased amount often (not always) means mania; a decreased amount ranges from anxiety to thought blocking or psychosis'),
  moo=('Mood in the patient’s own words · affect as you see it', 'affect: quality, intensity, range (restricted, labile, flat), appropriateness, congruence with the mood'),
  pro=('How the ideas connect — normal is linear, organized, goal-directed', 'circumstantial · tangential · loose · flight of ideas · perseveration · thought blocking · word salad'),
  con=('What the patient thinks about', 'obsessions and compulsions, delusions, ideas of reference, paranoia — patients may not volunteer them, so ask'),
  si=('Asked in every initial interview — “are you suicidal?” is not enough', 'get ideation, intent, plan and preparation; homicidal ideation belongs here too'),
  per=('Hallucination = no stimulus · illusion = a real stimulus misread', 'nonauditory hallucinations are clues to a neurologic, medical or withdrawal cause'),
  sen=('Alertness · orientation · concentration · memory · abstraction', 'serial 7s, months backward, 3-word recall · MMSE, SLUMS, Mini-Cog (recall + clock drawing)'),
  ins=('Insight: does the patient know they are ill? · judgment: do they decide well?', 'the two need not match, and insight does not measure how severe the illness is'),
)
F = dict(
  norm=dict(
    app=('Appears stated age, groomed, cooperative', 'normal motor activity; eye contact made through the interview'),
    spe=('Fluent — normal amount, rate and volume', None),
    moo=('Mood “fine” · affect euthymic, full range', 'congruent with the mood, appropriate to the content'),
    pro=('Linear, organized, goal-directed', 'every answer reaches the point of the question'),
    con=('No delusions, obsessions or paranoia', None),
    si=('Denies suicidal and homicidal ideation', 'asked directly, as in every initial interview'),
    per=('No hallucinations or illusions', None),
    sen=('Alert · oriented to person, place, time, situation', 'attends through serial 7s; recalls 3 words after a few minutes'),
    ins=('Full insight · judgment intact', 'nothing dangerous; takes part in their own care')),
  schizo=dict(
    app=('Odd behavior, fixed posturing, minimal eye contact', 'disorganized or catatonic behavior is one of the five criteria'),
    spe=('Disorganized speech — word salad, neologisms', 'incoherent, repetitive language; invented words'),
    moo=('Affect flat or blunted — a negative symptom', 'with apathy, anhedonia, alogia, asocial behavior'),
    pro=('Loose associations — no visible link between ideas', 'cannot abstract: proverbs answered concretely'),
    con=('Delusions — mood-incongruent; thought insertion', 'mood-incongruent delusions point to schizophrenia; thought insertion is characteristic'),
    si=(None, 'suicide risk is raised in schizophrenia — ask'),
    per=('Auditory hallucinations — voices', 'auditory: more often psychiatric illness than neurologic disease'),
    sen=('Alert and oriented — consciousness unchanged', 'cognitive symptoms: poor working memory, inattention'),
    ins=('Poor insight · judgment impaired', 'classically poor insight into the nature and severity of the illness')),
  mania=dict(
    app=('Hyperactive; bright, outlandish clothing and jewelry', '↑ goal-directed activity or psychomotor agitation'),
    spe=('Pressured, talkative — more and faster', None),
    moo=('Elevated, expansive or irritable mood', 'elation; decreased need for sleep'),
    pro=('Flight of ideas — fast, but every idea connects', 'racing thoughts; distractible'),
    con=('Grandiosity — can grow into grandiose delusions', 'grandiose delusions with elated mood are mood-congruent; psychotic features possible'),
    si=(None, 'high suicide risk in bipolar disorder'),
    per=(None, 'hallucinations only with psychotic features'),
    sen=('Orientation and memory grossly intact', 'some patients are so euphoric they answer orientation questions wrongly'),
    ins=('Little insight · impaired judgment is a hallmark', 'spending, sexual indiscretion, impulsive acts')),
  mddp=dict(
    app=('Withdrawn, stooped posture, psychomotor retardation', 'or psychomotor agitation'),
    spe=('Paucity of speech, slowed', None),
    moo=('Depressed mood · blunted affect, little range', 'SIG E CAPS: sleep, interest, guilt, energy, concentration, appetite, psychomotor, suicidal ideation'),
    pro=(None, None),
    con=('Mood-congruent delusions — guilt, sin, worthlessness, disease', 'psychosis only inside the depressive episode (vs schizoaffective disorder)'),
    si=(None, 'about two-thirds of depressed patients contemplate suicide — ask'),
    per=('Hallucinations possible — mood-congruent', 'MDD + hallucinations or delusions'),
    sen=('Poor concentration — can mimic dementia', '“pseudodementia”: rule out a medical cause for any deficit'),
    ins=(None, None)),
  delus=dict(
    app=('Often unremarkable — functioning largely spared', 'daily life is affected only by the fixed belief'),
    spe=(None, None),
    moo=('No mood disorder', None),
    pro=('Organized — no disorganized speech', 'normal thought process can carry delusional content'),
    con=('One or more delusions for > 1 month', 'erotomanic, grandiose, jealous, persecutory, somatic; can be shared (folie à deux)'),
    si=(None, None),
    per=('No other psychotic symptoms', None),
    sen=(None, None),
    ins=(None, None)),
  ocd=dict(
    app=('Compulsions — repetitive, ritualized behaviors', None),
    spe=(None, None),
    moo=('Anxious — the ritual relieves it', 'compulsions are performed to avoid rising anxiety or a dreaded outcome'),
    pro=(None, None),
    con=('Obsessions — intrusive, unwelcome, ego-alien, resisted', 'the loop on the right: obsession → anxiety → compulsion → relief'),
    si=(None, None),
    per=(None, None),
    sen=(None, None),
    ins=('Insight usually kept — knows the beliefs are not real', 'some have poor or absent insight, which is linked to worse outcomes')),
  delir=dict(
    app=('Restless, picking at the bedclothes — or hypoactive', 'agitation; a quiet, hypoactive form also occurs'),
    spe=(None, None),
    moo=('Affective changes', None),
    pro=('Disorganized, fragmented — loses the train of thought', None),
    con=('May be paranoid; delusions', None),
    si=(None, None),
    per=('Visual hallucinations and illusions', 'poor attention misreads people and events'),
    sen=('Waxing and waning consciousness · inattention', 'disoriented to time and place; acute onset (hours to days); worse at night; EEG diffuse slowing'),
    ins=('Insight and judgment impaired', 'judgment grossly impaired')),
  ncd=dict(
    app=('May be unkempt and disheveled', None),
    spe=('Uneven or slurred speech possible', None),
    moo=('Affect: loss of prosody', None),
    pro=(None, None),
    con=('May be paranoid', None),
    si=(None, None),
    per=('Hallucinations rare', None),
    sen=('Alert — consciousness intact · memory lost', 'recent memory goes before remote; slow, insidious, stable over the day; screen: MMSE, SLUMS, Mini-Cog'),
    ins=('Insight impaired · judgment intact at first', 'judgment worsens with time')),
  dts=dict(
    app=('Tremor, sweating, agitation', 'autonomic hyperactivity: tachycardia, hypertension, fever'),
    spe=(None, None),
    moo=('Anxious', None),
    pro=('Confused', None),
    con=('Delusions possible', None),
    si=(None, None),
    per=('Hallucinations — tactile common', None),
    sen=('Delirium — disoriented, fluctuating', '2–4 days after the last drink; untreated mortality about 20%'),
    ins=(None, None)),
  stim=dict(
    app=('Hyperactive, agitated · dilated pupils', 'tachycardia, hypertension, fever; skin excoriations with methamphetamine'),
    spe=(None, None),
    moo=('Euphoric, elevated mood', 'grandiosity (amphetamines); anxiety'),
    pro=(None, None),
    con=('Paranoia', None),
    si=(None, None),
    per=('Tactile hallucinations — “cocaine crawlies”, “meth mites”', None),
    sen=('Hyperalert — prolonged wakefulness', None),
    ins=('Impaired judgment', None)),
  lsd=dict(
    app=('Dilated pupils', None),
    spe=(None, None),
    moo=('Anxious', None),
    pro=(None, None),
    con=('Paranoia', None),
    si=(None, None),
    per=('Perceptual distortion — visual and auditory', 'depersonalization; flashbacks later'),
    sen=(None, None),
    ins=(None, None)),
  ster=dict(
    app=(None, None),
    spe=(None, None),
    moo=('Mania-like mood — a secondary mood disorder', 'severe depression can follow stopping the steroid'),
    pro=(None, None),
    con=('Psychosis possible', None),
    si=(None, None),
    per=(None, None),
    sen=(None, 'steroids are also a cause of delirium'),
    ins=(None, None)),
  hypot=dict(
    app=('Weight gain, puffy face, thin dry hair, lost outer eyebrow', None),
    spe=('Slow, low-pitched, hoarse voice', None),
    moo=('Depression — or hypomania', None),
    pro=('Slowed thinking', None),
    con=('Paranoia', '“myxedema madness” in its most severe form'),
    si=(None, None),
    per=('Hallucinations', None),
    sen=('Delirium can occur', None),
    ins=(None, None)),
  hypna=dict(
    app=(None, None),
    spe=(None, None),
    moo=(None, None),
    pro=(None, None),
    con=('No delusions — this is not psychosis', None),
    si=(None, None),
    per=('Hypnagogic (falling asleep) · hypnopompic (waking)', 'may hear one’s name called or see flashes or shadows; sometimes narcolepsy'),
    sen=(None, None),
    ins=(None, None)),
  grief=dict(
    app=('Somatic symptoms possible', None),
    spe=(None, None),
    moo=('Sadness, guilt, yearning', 'no fixed series of stages; varies with each person and loss'),
    pro=(None, None),
    con=('Fleeting wishes to have died with or instead of the loved one', None),
    si=(None, None),
    per=('May hear or see the deceased', None),
    sen=(None, None),
    ins=(None, None)),
)
DASH = '—'
for k, y, hh, *_ in ROWS:
    un = ['risk:*'] if k == 'si' else []          # the safety overlay writes its own text in this row
    h, d = B[k]
    text(h, FX, y - 4, 'nf-l1', unless=['p:*'] + un)
    text(d, FX, y + 16, 'nf-l2', unless=['p:*'] + un)
    for p in KEYS:
        h, d = F[p][k]
        if h is None and d is None:
            text(DASH + '  no typical finding named', FX, y + 4, 'dyn-cap', when=O(p), unless=un or None)
            continue
        if h is None:
            text(d, FX, y + 4, 'nf-l2', when=O(p), unless=un or None)
            continue
        text(h, FX, y - 4 if d else y + 5, 'nf-l1', when=O(p), unless=un or None)
        if d: text(d, FX, y + 16, 'nf-l2', when=O(p), unless=un or None)

# ════════ widgets (x 1590 → 2320) ════════
kinds = dict(word=['speech', '--dk1'], idea=['thought', '--dk7'], cyc=['thought', '--dk7'],
             loc=['alert', '--dk2'], risk=['risk', '--bad'])
groups = [['speech', 'Words'], ['thought', 'Ideas'], ['alert', 'Consciousness'], ['risk', 'Risk']]
flows = []

# — speech stream —
ys = RY['spe']
SPEECH = dict(  # variant: (keys, path, n, speed, caption)
  norm=(['norm', 'delus', 'grief'], None, 5, 140, 'normal rate'),
  fast=(['mania'], None, 13, 360, 'pressured — more, faster'),
  slow=(['mddp', 'hypot'], None, 2, 50, 'slowed — sparse'),
  salad=(['schizo'], f'M{WX0 + 20} {ys} L1700 {ys - 22} L1780 {ys + 18} L1850 {ys - 14} L1930 {ys + 24} L2010 {ys - 20} L2090 {ys + 14} L2170 {ys - 22} L2290 {ys}', 7, 130, 'jumbled — word salad'),
  uneven=(['ncd'], None, 4, 80, 'uneven or slurred'),
)
SP_KEYS = [k for v in SPEECH.values() for k in v[0]]
add(f'<path d="M{WX0 + 20} {ys + 30} H{WX1 - 30}" class="dyn-line" style="opacity:.25"/>')
add(f'<path d="M{WX1 - 30} {ys - 20} L{WX1 - 10} {ys} L{WX1 - 30} {ys + 20}" class="dyn-line" style="opacity:.5"/>')
for name, (ks, path, n, sp, cap) in SPEECH.items():
    d = path or f'M{WX0 + 20} {ys} H{WX1 - 40}'
    ln = 760 if path else WX1 - 40 - WX0 - 20
    flows.append(dict(d=d, len=ln, speed=sp, r=6, when=[f'p:{x}' for x in ks] + (['!p:*'] if name == 'norm' else []), base=dict(word=n)))
    text(cap, WX0 + 20, ys - 24, 'nf-l2', when=O(*ks))
text('words per breath', WX0 + 20, ys - 24, 'nf-l2', unless=['p:*'])
nosp = [k for k in KEYS if k not in SP_KEYS]
add(f'<path d="M{WX0 + 20} {ys} H{WX1 - 40}" class="dyn-dash" style="opacity:.5"/>', when=O(*nosp))
text('rate not the clue here', WX0 + 20, ys - 24, 'dyn-cap', when=O(*nosp))

# — mood scale —
ym = RY['moo']
MX = dict(dep=1700, eu=1955, el=2210)
add(f'<path d="M{MX["dep"]} {ym + 4} H{MX["el"]}" class="dyn-line"/>' +
    ''.join(f'<path d="M{x} {ym - 6} V{ym + 14}" class="dyn-line"/>' for x in MX.values()))
for lab, x in (('depressed', MX['dep']), ('euthymic', MX['eu']), ('elevated', MX['el'])):
    text(lab, x, ym + 34, 'nf-l2', 'middle')
MOOD = dict(dep=['mddp', 'grief'], eu=['norm', 'delus'], el=['mania', 'stim', 'ster'])
for pos, ks in MOOD.items():
    add(f'<circle cx="{MX[pos]}" cy="{ym + 4}" r="15" style="fill:var(--accent);stroke:var(--surface);stroke-width:3"/>', when=O(*ks))
nomood = [k for k in KEYS if not any(k in v for v in MOOD.values())]
text('no direction named in the sources', MX['eu'], ym - 16, 'dyn-cap', 'middle', when=O(*nomood))
text('where the mood sits', MX['eu'], ym - 16, 'nf-l2', 'middle', unless=['p:*'])

# — thought process: from the question to its point —
yp = RY['pro']
QX, AX = WX0 + 30, WX1 - 40
add(f'<circle cx="{QX}" cy="{yp}" r="18" class="dyn-cell"/><circle cx="{AX}" cy="{yp}" r="18" class="dyn-cell"/>')
text('Q', QX, yp + 5, 'nf-l1', 'middle'); text('point', AX, yp + 5, 'nf-l1', 'middle')
text('the question', QX - 18, yp + 40, 'nf-l2'); text('its answer', AX + 18, yp + 40, 'nf-l2', 'end')
PROC = dict(  # variant: keys, [(path, len)], n per path, speed, caption, draw track
  lin=(['norm', 'delus'], [(f'M{QX + 20} {yp} H{AX - 20}', AX - QX - 40)], 5, 150, 'linear — straight to the point'),
  flight=(['mania'], [(f'M{QX + 20} {yp} L1700 {yp - 38} L1780 {yp + 34} L1860 {yp - 40} L1940 {yp + 30} L2020 {yp - 36} L2100 {yp + 28} L2180 {yp - 42} L2240 {yp - 44}', 820)],
          9, 340, 'flight of ideas — fast, every link visible, drifts off the point'),
  loose=(['schizo'], [(f'M{QX + 30} {yp - 6} L1720 {yp - 30}', 100), (f'M1790 {yp + 30} L1880 {yp + 8}', 95),
                      (f'M1950 {yp - 40} L2030 {yp - 14}', 85), (f'M2100 {yp + 38} L2190 {yp + 22}', 92)],
         2, 90, 'loose associations — fragments with no visible link'),
  frag=(['delir'], [(f'M{QX + 30} {yp + 4} L1760 {yp - 10}', 140), (f'M1850 {yp + 20} L1960 {yp + 34}', 112),
                    (f'M2040 {yp - 24} L2110 {yp - 32}', 72)],
        1, 60, 'fragmented — the train of thought keeps breaking'),
  slow=(['hypot'], [(f'M{QX + 20} {yp} H{AX - 20}', AX - QX - 40)], 2, 45, 'slowed thinking'),
)
PR_KEYS = [k for v in PROC.values() for k in v[0]]
for name, (ks, paths, n, sp, cap) in PROC.items():
    when = O(*ks) + (['!p:*'] if name == 'lin' else [])
    for d, ln in paths:
        add(f'<path d="{d}" class="dyn-line" style="opacity:.45"/>', when=when)
        flows.append(dict(d=d, len=ln, speed=sp, r=7, when=when, base=dict(idea=n)))
    text(cap, QX + 30, yp - 46 if name != 'flight' else yp - 50, 'nf-l2', when=O(*ks))
text('normal: linear, organized, goal-directed', QX + 30, yp - 46, 'nf-l2', unless=['p:*'])
nopr = [k for k in KEYS if k not in PR_KEYS]
add(f'<path d="M{QX + 20} {yp} H{AX - 20}" class="dyn-dash" style="opacity:.4"/>', when=O(*nopr))
text('no typical change named — the content is the clue', QX + 30, yp - 46, 'dyn-cap', when=O(*nopr))

# — thought content: the OCD loop —
yc = RY['con']
CX, CRX, CRY = 1960, 300, 34
ell = f'M{CX - CRX} {yc} A{CRX} {CRY} 0 1 1 {CX + CRX} {yc} A{CRX} {CRY} 0 1 1 {CX - CRX} {yc}'
add(f'<path d="{ell}" class="dyn-line" style="opacity:.6"/>', when=O('ocd'))
flows.append(dict(d=ell, len=1350, speed=170, r=7, when=O('ocd'), base=dict(cyc=6)))
for lab, x, y, an in (('obsession', CX - CRX - 12, yc + 5, 'end'), ('anxiety ↑', CX, yc - CRY - 10, 'middle'),
                      ('compulsion', CX + CRX + 12, yc + 5, 'start'), ('relief — briefly', CX, yc + CRY + 22, 'middle')):
    text(lab, x, y, 'nf-l1', an, when=O('ocd'))
DEL = ['schizo', 'mddp', 'delus', 'delir', 'dts', 'hypot', 'stim', 'lsd']
add(f'<rect x="{CX - 230}" y="{yc - 26}" width="460" height="52" rx="26" style="fill:var(--accent);fill-opacity:.12;stroke:var(--accent);stroke-width:2.5"/>',
    when=O(*DEL))
DEL_T = dict(schizo='fixed false belief — mood-incongruent', mddp='fixed false belief — mood-congruent (guilt, ruin)',
             delus='one fixed belief — the rest intact', delir='paranoid ideas that come and go',
             dts='delusions with the delirium', hypot='paranoia — myxedema madness', stim='paranoia', lsd='paranoia')
for k, t in DEL_T.items():
    text(t, CX, yc + 5, 'nf-l1', 'middle', when=O(k))
text('fixed, false, not shared by the culture = a delusion', CX, yc + 5, 'nf-l2', 'middle', unless=['p:*'])

# — suicidal ideation: the ladder (risk overlay) —
yr = RY['si']
STEPS = [('ideation', 1660), ('intent', 1830), ('plan', 2000), ('means', 2170)]
for i, (lab, x) in enumerate(STEPS):
    add(f'<rect x="{x - 72}" y="{yr - 20}" width="144" height="40" rx="12" class="dyn-soft"/>')
    if i: add(f'<path d="M{x - 98} {yr} H{x - 76}" class="dyn-line"/>')
    text(lab, x, yr + 5, 'nf-l1', 'middle')
LIT = dict(pass_=(['pass'], [0]), plan=(['plan'], [0, 1, 2, 3]))
for ks, idx in LIT.values():
    for i in idx:
        x = STEPS[i][1]
        add(f'<rect x="{x - 72}" y="{yr - 20}" width="144" height="40" rx="12" style="fill:var(--bad);fill-opacity:.18;stroke:var(--bad);stroke-width:3"/>',
            when=RK(*ks))
flows.append(dict(d=f'M1600 {yr + 30} H2250', len=650, speed=120, r=6, when=RK('plan'), base=dict(risk=4)))
text('passive: thoughts, no intent to act', 2262, yr + 5, TAG, 'start', when=RK('pass'))
text('highest risk', 2262, yr + 5, TAG, 'start', when=RK('plan'))
text('voices order it', 2262, yr + 5, TAG, 'start', when=RK('cmd'))
RISK_T = dict(
  pass_=('Passive suicidal ideation: “life isn’t worth living” — no intent', 'still ask about intent, plan and means, and what has kept them from acting'),
  plan=('A specific plan with access to the means (a gun already owned)', 'highest-risk group: keep the patient safe and get psychiatric evaluation now'),
  cmd=('Command hallucinations ordering self-harm', 'ask what the voices order and whether they have ever felt compelled to obey'))
for key, (h, d) in RISK_T.items():
    key = key.rstrip('_')
    text(h, FX, yr - 4, 'nf-l1', when=RK(key))
    text(d, FX, yr + 16, 'nf-l2', when=RK(key))
# — perception: the chips —
yv = RY['per']
CHIPS = [('Auditory', 'aud'), ('Visual', 'vis'), ('Tactile', 'tac'), ('Olfactory', 'olf'), ('Illusion', 'ill'), ('Hypnagogic', 'hyp')]
CW, CG = 112, 10
CHX = {c: WX0 + i * (CW + CG) for i, (_, c) in enumerate(CHIPS)}
LITC = dict(aud=['schizo', 'lsd', 'cmd'], vis=['delir', 'lsd'], tac=['dts', 'stim'], ill=['delir'], hyp=['hypna'])
for lab, c in CHIPS:
    x = CHX[c]
    add(f'<rect x="{x}" y="{yv - 18}" width="{CW}" height="36" rx="18" class="dyn-soft"/>')
    ks = LITC.get(c, [])
    when = [('risk:cmd' if k == 'cmd' else 'p:' + k) for k in ks]
    if when:
        add(f'<rect x="{x}" y="{yv - 18}" width="{CW}" height="36" rx="18" style="fill:var(--accent);fill-opacity:.25;stroke:var(--accent);stroke-width:3"/>', when=when)
    text(lab, x + CW / 2, yv + 5, 'nf-l1', 'middle')
text('commands', CHX['aud'] + CW / 2, yv + 34, TAG, 'middle', when=RK('cmd'))
text('possible, mood-congruent — type not named', WX0, yv - 26, 'dyn-cap', when=O('mddp'))
text('hallucinations of the deceased', WX0, yv - 26, 'dyn-cap', when=O('grief'))
text('type not named', WX0, yv - 26, 'dyn-cap', when=O('hypot'))
text('the sense it comes through', WX0, yv - 26, 'nf-l2', unless=['p:*'])

# — sensorium: 24 hours of consciousness —
yl = RY['sen']
LV = dict(hyper=yl - 38, alert=yl - 8, cloud=yl + 34)
LX0, LX1 = WX0 + 120, WX1 - 20
for lab, k in (('hyperalert', 'hyper'), ('alert', 'alert'), ('clouded', 'cloud')):
    add(f'<path d="M{LX0} {LV[k]} H{LX1}" class="dyn-line" style="stroke-dasharray:3 7;opacity:.5"/>')
    text(lab, LX0 - 12, LV[k] + 4, 'nf-l2', 'end')
text('24 hours →', LX1, yl + 56, 'nf-l2', 'end')
def wave():
    pts = []; n = 8; dx = (LX1 - LX0) / n
    d = f'M{LX0} {LV["alert"]}'
    for i in range(n):
        x0 = LX0 + i * dx
        lo = LV['cloud'] + (6 if i % 3 == 1 else 0)
        d += f' C{x0 + dx * .3:.0f} {LV["alert"]} {x0 + dx * .3:.0f} {lo} {x0 + dx * .5:.0f} {lo} S{x0 + dx * .8:.0f} {LV["alert"]} {x0 + dx:.0f} {LV["alert"]}'
    return d
TR = dict(  # variant: keys, path, len, caption
  flat=(['norm', 'schizo', 'ncd'], f'M{LX0} {LV["alert"]} H{LX1}', LX1 - LX0, 'steady and alert'),
  wave=(['delir', 'dts'], wave(), int((LX1 - LX0) * 1.5), 'waxes and wanes — lucid, then clouded'),
  hyper=(['stim'], f'M{LX0} {LV["hyper"]} H{LX1}', LX1 - LX0, 'hyperalert — no sleep'),
)
TR_KEYS = [k for v in TR.values() for k in v[0]]
for name, (ks, d, ln, cap) in TR.items():
    add(f'<path d="{d}" class="dyn-trace"/>', when=O(*ks))
    flows.append(dict(d=d, len=ln, speed=160, r=7, when=O(*ks), base=dict(loc=3)))
    text(cap, LX0, yl - 50, 'nf-l2', when=O(*ks))
notr = [k for k in KEYS if k not in TR_KEYS]
text('no change in consciousness named', LX0, yl - 50, 'dyn-cap', when=O(*notr))
text('less than fully alert = organic until proven otherwise', LX0, yl - 50, 'nf-l2', unless=['p:*'])

# ════════ the strip: what is it? ════════
YS0 = 1196
add(f'<path d="M140 {YS0} H2340" class="dyn-line" style="opacity:.35"/>')
text('What is it? — tap a presentation for its card', 160, YS0 + 30, 'dyn-big')
YA, YB = YS0 + 104, YS0 + 204
text('Primary psychiatric', 160, YA - 46, 'nf-l1')
text('Normal experiences', 1740, YA - 46, 'nf-l1')
text('Medical, neurologic or substance — the psychiatric picture is secondary', 160, YB - 46, 'nf-l1')
POS = {}
for i, k in enumerate(['schizo', 'mania', 'mddp', 'delus', 'ocd']): POS[k] = (290 + i * 300, YA)
for i, k in enumerate(['hypna', 'grief']): POS[k] = (1890 + i * 300, YA)
for i, k in enumerate(['delir', 'ncd', 'dts', 'stim', 'lsd', 'ster', 'hypot']): POS[k] = (290 + i * 300, YB)
LANE = dict(pri='msPri', sec='msSec', norm='msNorm')
for k, (x, y) in POS.items():
    _, _, card, c, lab, sub, extra = INFO[k]
    add(f'<rect x="{x - 140}" y="{y - 30}" width="280" height="60" rx="18" class="dyn-hl"/>', when=O(k))
    nodes.append((f'ms{len(nodes) + 1}', lab, x, y, LANE[c], sub, [card] + extra))
YEND = YB + 50

# ════════ notes ════════
notes = {
  '': 'The mental status exam is a cross-sectional snapshot, written in a fixed order from appearance to judgment. Pick a '
      'presentation to fill in the form — then ask the exam’s real question: primary psychiatric, or secondary to a medical, '
      'neurologic or substance cause?',
  'p:norm': 'A normal MSE: groomed and cooperative, fluent speech, euthymic mood with a full-range affect, a linear and '
            'goal-directed thought process, no delusions, suicidal ideation or hallucinations, alert and oriented, with full '
            'insight and intact judgment. Every other presentation is read against this one.',
  'p:schizo': 'Acute schizophrenia: disorganized speech and loose associations, delusions (mood-incongruent, thought insertion), '
              'auditory hallucinations and a flat affect — yet alert and oriented, with poor insight. A clear sensorium with '
              'psychosis points to a primary psychotic disorder.',
  'p:mania': 'Mania: pressured speech, elevated or irritable mood, flight of ideas (fast, but each idea connects), grandiosity and '
             'hyperactivity, with little insight and badly impaired judgment. Orientation and memory stay grossly intact.',
  'p:mddp': 'MDD with psychotic features: stooped, slowed and sparse in speech, depressed mood with a blunted affect, and '
            'mood-congruent delusions of guilt, sin or disease that occur only inside the depressive episode. Poor '
            'concentration can mimic dementia (pseudodementia).',
  'p:delus': 'Delusional disorder: one or more fixed false beliefs for more than a month, with organized thinking, no mood '
             'disorder and no other psychotic symptoms — apart from the belief, the patient functions largely normally.',
  'p:ocd': 'OCD: intrusive, unwelcome obsessions drive anxiety, and repetitive compulsions relieve it — briefly. Most patients '
           'keep insight that the beliefs are not real; poor insight predicts a worse outcome.',
  'p:delir': 'Delirium: an acute, waxing and waning disturbance of consciousness and attention — disoriented to time and place, '
             'fragmented thinking, visual hallucinations and illusions, worse at night. It is often mistaken for a primary '
             'psychiatric disorder; find and treat the medical cause.',
  'p:ncd': 'Major neurocognitive disorder (Alzheimer): alert, with intact consciousness, but memory is lost — recent before remote — '
           'with a slow, insidious course that is stable across the day; hallucinations are rare and insight is impaired. '
           'Look for reversible causes: depression, hypothyroidism, B12, neurosyphilis, NPH.',
  'p:dts': 'Delirium tremens: 2–4 days after the last drink — tremor, sweating, tachycardia, hypertension and fever with '
           'delirium, disorientation and hallucinations, often tactile. A medical emergency (about 20% mortality untreated); '
           'longer-acting benzodiazepines.',
  'p:stim': 'Stimulant intoxication (cocaine, amphetamines): hyperactive and hyperalert with dilated pupils, euphoria or '
            'grandiosity, paranoia, and tactile hallucinations — “cocaine crawlies”, “meth mites”. A tactile hallucination is '
            'a clue to a substance, not a primary psychosis.',
  'p:lsd': 'LSD intoxication: visual and auditory perceptual distortion, depersonalization, anxiety and paranoia, with dilated '
           'pupils; flashbacks can follow. Psychosis from a substance is secondary, not schizophrenia.',
  'p:ster': 'High-dose corticosteroids: a secondary mood disorder that looks like mania, sometimes psychosis — and severe '
            'depression can follow stopping them. Always check the medication list before diagnosing a primary disorder.',
  'p:hypot': 'Hypothyroidism: slowed thinking and a slow, low-pitched, hoarse voice, depression (or hypomania), and in its most '
             'severe form paranoia and hallucinations — “myxedema madness”. Look for weight gain, a puffy face and thin dry hair.',
  'p:hypna': 'Hypnagogic hallucinations (falling asleep) and hypnopompic ones (waking) can be normal: people without psychosis may '
             'hear their name called or see shadows. Without other symptoms they are not pathology — sometimes narcolepsy.',
  'p:grief': 'Normal grief: sadness, guilt and yearning, somatic symptoms, even hearing or seeing the deceased and fleeting wishes '
             'to have died with them. It is not a disorder and adapts within about 6 months; diagnose MDD only if its criteria are met.',
  'risk:pass': 'Passive suicidal ideation — thoughts that life is not worth living without intent to act. Still ask about intent, '
               'a plan, access to means and what has kept the patient from acting.',
  'risk:plan': 'A specific plan with access to the means (a firearm already owned) puts the patient in the highest-risk group. '
               'Take every threat seriously: keep the patient safe and get psychiatric evaluation immediately.',
  'risk:cmd': 'Command hallucinations: ask what the voices order, whether they include harming oneself or others, and whether the '
              'patient has ever felt compelled to obey — voices can push self-harm even without a wish to die.',
}

# ════════ readouts ════════
R = lambda keys, d: dict(when=O(*keys), d=d)
readouts = [
  dict(l='Mood', mods=[R(['mania', 'stim', 'ster'], 1), R(['mddp', 'grief'], -1), R(['norm', 'delus'], 0)]),
  dict(l='Disordered thought process', mods=[R(['schizo', 'mania', 'delir'], 1), R(['norm', 'delus'], 0)]),
  dict(l='Psychosis', mods=[R(['schizo', 'mddp', 'delus', 'delir', 'dts', 'stim', 'lsd', 'ster', 'hypot'], 1), R(['norm', 'hypna'], 0)]),
  dict(l='Level of consciousness', mods=[R(['stim'], 1), R(['delir', 'dts'], -1), R(['norm', 'schizo', 'ncd'], 0)]),
  dict(l='Insight', mods=[R(['schizo', 'mania', 'delir', 'ncd'], -1), R(['norm', 'ocd'], 0)]),
  dict(l='Medical, neurologic or substance cause', mods=[R(['delir', 'ncd', 'dts', 'stim', 'lsd', 'ster', 'hypot'], 1),
                                                       R(['norm', 'schizo', 'mania', 'mddp', 'delus', 'ocd'], 0)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[
    dict(id='p', label='Presentation', type='one', options=[[k, INFO[k][1], INFO[k][2]] for k in KEYS],
         sections=[[s, ks] for s, ks in SEC]),
    dict(id='risk', label='Safety questions (add to any)', type='one',
         options=[['pass', 'Passive suicidal ideation', 'suicideassess'], ['plan', 'Suicidal plan + means', 'suicide'],
                  ['cmd', 'Command hallucination to self-harm', 'perception']]),
  ],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='Kaplan & Sadock ch 1 (OCOM Psych SDL 8–9), 3–7, 9 · DeGowin ch 15 · First Aid pp. 119, 534, 572, 575–580, 587–589')

MAP = dict(
  id='msesim', title='The Mental Status Exam in Motion', topic='behav', after='psychmse',
  sub='One MSE form run for 15 presentations — schizophrenia, mania, psychotic depression, delusional disorder, OCD, delirium, '
      'dementia, DTs, stimulants, LSD, steroids, hypothyroidism, hypnagogic hallucinations and grief — each row moves '
      '(speech, the train of thought, mood, the OCD loop, hallucination type, 24-hour consciousness), with suicide-risk '
      'overlays and the verdict: primary vs secondary. Tap a row or a presentation for its card',
  w=3500, h=YEND + 60,
  fa='119, 534, 572, 575–580, 587–589', src=[K1, K3, K4, K5, K6, K7, K9, DG15],
  lanes=[('msExam', 'The MSE, row by row', 'glycolysis'), ('msPri', 'Primary psychiatric', 'sugars'),
         ('msSec', 'Medical, neurologic or substance', 'tca'), ('msNorm', 'Normal experiences', 'gluconeo')],
  comps=[],
  nodes=nodes,
  panels=[
    (2420, 1040, 1000, 'Clues to a secondary cause (DeGowin ch 15; Kaplan ch 1, 3, 5)', [
      ('Not fully alert', 'assume an organic neurologic disorder until proven otherwise'),
      ('Nonauditory hallucinations', 'visual, tactile, olfactory: neurologic, medical or withdrawal'),
      ('Consciousness varies', 'pursue an undiagnosed medical condition'),
      ('Older, many drugs', 'the highest risk of delirium'),
      ('Endocrine', 'hypo- or hyperthyroidism, Cushing, Addison, steroids')]),
    (2420, 1230, 1000, 'Delirium vs dementia vs schizophrenia (Kaplan ch 3, Table 3-8)', [
      ('Onset', 'delirium acute · dementia insidious'),
      ('Over the day', 'delirium fluctuates · dementia stable'),
      ('Consciousness', 'delirium episodes of ↓ · dementia alert · schizophrenia unchanged'),
      ('Hallucinations', 'delirium prominent, visual or tactile · dementia rare'),
      ('Schizophrenia', 'hallucinations and delusions more constant, better organized')]),
  ],
  dyn=dyn,
)
