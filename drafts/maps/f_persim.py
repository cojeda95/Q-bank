# m56 — Personality Disorders & Ego Defenses (dynamic map, kit data)
# WHO it is and HOW to tell it from its look-alike. On top, the three clusters as a board of ten tiles (A weird · B wild ·
# C worried); below them, the look-alikes that are NOT personality disorders (delusional disorder, schizophrenia, bipolar,
# conduct disorder, social anxiety disorder, OCD), each under the tiles it is confused with. Picking a disorder lights its
# tile AND its look-alike(s) the same way and runs particles along the "tell apart" line between them, and a case card fills
# in (cluster · core pattern · defense or tell-tale · look-alike and how to tell · therapy). Below, four defense scenes move:
# splitting (the same staff sorted all good / all bad), projection (one's own impulse seen in someone else), acting out
# (feeling → action, skipping words) and sublimation (the wish kept, the outlet made acceptable). Borderline lights the
# splitting scene, paranoid the projection scene.
# Readouts are criteria (↑ present · ↓ absent · ↔ either way): ego-syntonic, wants closeness, fears rejection or
# abandonment, odd thinking or perception, violates others' rights, needs age ≥ 18, mature defense.
#
# Sources (all read; OCOM Psych course texts win — the SDL 28–29 reading IS Kaplan & Sadock ch 19 (course PDF "SDL 28:29;
# Personality Disorders A,B,C"), with Osmosis Notes ch 98–100 (course PDFs "SDL 28; Cluster A/B", "SDL 29; Cluster C");
# the SDL 30 reading IS Kaplan ch 23 (corpus/psych/sdl30_psychotherapy.txt); the SDL 22 reading IS Kaplan ch 9):
#   First Aid 2025 p. 570 (acting out — actions rather than reflections or feelings, skips therapy example; displacement
#     vs projection; transference/countertransference; defenses voluntary or involuntary) · p. 571 (passive aggression;
#     projection — unacceptable internal impulse attributed to an external source, cheating-spouse example; reaction
#     formation vs sublimation; idealization; splitting — all good or all bad at different times, intolerance of ambiguity,
#     common in borderline; mature defenses SASH; sublimation — similar but socially acceptable action, aggression → sports)
#     · p. 574 (conduct disorder: aggression to people/animals, property destruction, theft; after 18 often reclassified as
#     antisocial PD; psychotherapy, eg CBT) · p. 580 (OCD: obsessions and/or compulsions, tic disorders, poor insight →
#     worse outcomes; CBT + SSRIs, clomipramine/venlafaxine second line; social anxiety disorder) · p. 582 (personality
#     disorders: inflexible, pervasive, distress/impairment, usually egosyntonic, present by early adulthood; clusters and
#     their genetic links; Cluster A "no psychosis"; each disorder's core; antisocial ≥ 18 with conduct disorder before 15,
#     M > F; borderline F > M, splitting, DBT; avoidant desires relationships vs schizoid; OCPD egosyntonic vs OCD).
#   Kaplan & Sadock ch 19 (course text): ego-syntonic, alloplastic; diagnose each PD that meets criteria; not limited to an
#     episode of another disorder; paranoid — projection, no fixed delusions (vs delusional disorder), no hallucinations or
#     formal thought disorder (vs schizophrenia), rarely tumultuous relationships, rarely serious criminality; schizoid —
#     withdrawal and fantasy, indifferent to praise and criticism, avoidant wish to participate; schizotypal — oddities
#     separate it from schizoid and avoidant, psychotic symptoms brief and fragmentary, paranoid lacks the odd behavior;
#     antisocial — ≥ 18, pattern since 15, conduct disorder before 15, charming veneer, stress interview, contingency
#     management/reward-based > CBT; borderline — splitting, projective identification, labile transferences, acts out
#     impulses in therapy, differs from mood disorders by the core borderline features, "can sometimes be associated with
#     criminality", DBT most empirical support, avoid benzodiazepines; histrionic — repression and dissociation, more
#     suicide attempts/identity diffusion/brief psychosis in borderline, psychoanalytically oriented psychotherapy;
#     narcissistic — rage at criticism, fragile self-esteem → depression, mania's episodic grandiosity with euphoria and
#     impairment, psychoanalytic or group therapy, lithium for mood swings, serotonergic antidepressants; narcissistic,
#     histrionic, paranoid "rarely include serious criminality and aggressiveness"; avoidant — strong guarantee of uncritical
#     acceptance, refusal → withdraws and hurt, social anxiety disorder avoids specific situations rather than interpersonal
#     contact in general, may co-occur, assertiveness training, group, β-blockers (atenolol); dependent — tolerates an abusive
#     spouse, folie à deux submissive partner, greater fear of abandonment than avoidant, one long-term relationship and not
#     manipulative (vs histrionic/borderline), treatment often successful (insight-oriented, behavioral, assertiveness, family,
#     group); OCPD — isolation, intellectualization, rationalization, reaction formation, undoing; recurrent obsessions or
#     compulsions → OCD; CBT supported, some seek help on their own; defense management — splitting (staff discuss it, gently
#     confront that no one is all good or all bad; can provoke staff to turn against the patient), projection (acknowledge
#     mistakes, no confrontation, counterprojection), acting out (patient has lost control, get attention, leave if afraid).
#   Osmosis Notes ch 98–100 (course text, SDL 28–29): schizotypal "maintain desire for relationships (unlike schizoid)";
#     OCD ego-dystonic, OCPD ego-syntonic; DBT for borderline; group/assertiveness for cluster C.
#   Kaplan & Sadock ch 23 (course text, SDL 30): DBT — most empirical support for BPD, weekly group skills + individual +
#     phone consultation + consultation team. · ch 9 (course text, SDL 22): only OCD has genuine obsessions and compulsions.
#   Kaplan & Sadock ch 2: conduct disorder — ≥ 3 of 15 behaviors in the past 12 months; diagnosed after 18 only if antisocial
#     PD criteria are not met; for some youth, a lifelong pattern culminating in antisocial PD.
# Source conflict for the owner: schizotypal "wants closeness" ↑ follows the Osmosis course text ("maintain desire for
#   relationships"); Kaplan ch 19 says only "pervasive discomfort with and inability to maintain close relationships", and FA
#   says "interpersonal awkwardness" — neither denies the wish.
# Cut for lack of support in these sources: projective identification as a switch (Kaplan-only, kept in the borderline note
#   and card row, not FA); a named signature defense for schizotypal, antisocial, narcissistic, avoidant, dependent (Kaplan
#   names none — those rows give a sourced tell-tale instead); any "wants closeness" or "fears rejection" arrow for paranoid,
#   histrionic, narcissistic, antisocial, OCPD (no source commits); a psychosis readout (FA "no psychosis" for Cluster A vs
#   Kaplan's brief stress psychoses in paranoid, schizoid, schizotypal and borderline — no clean arrow); medication lists
#   beyond what Kaplan names per disorder.
import sys
sys.path.insert(0, 'drafts/tools')   # run from the repo root
from common import full

K2, K9, K19, K23 = (full('Kaplan & Sadock', c) for c in (2, 9, 19, 23))

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
O = lambda *k: ['pd:' + x for x in k]
BAND = 'fill:var(--accent);fill-opacity:.10;stroke:var(--accent);stroke-opacity:.55;stroke-width:2'

# ════════ the options (teaching order) ════════
SECTIONS = [
  ('Cluster A', [('par', 'Paranoid', 'clustera'), ('szd', 'Schizoid', 'clustera'), ('szt', 'Schizotypal', 'clustera')]),
  ('Cluster B', [('asp', 'Antisocial', 'antisocial'), ('bpd', 'Borderline', 'borderline'), ('his', 'Histrionic', 'clusterb'),
                 ('nar', 'Narcissistic', 'clusterb')]),
  ('Cluster C', [('avd', 'Avoidant', 'clusterc'), ('dep', 'Dependent', 'clusterc'), ('ocpd', 'OCPD', 'clusterc')]),
  ('Look-alikes', [('ocd', 'OCD (vs OCPD)', 'ocd'), ('cond', 'Conduct disorder', 'conductodd')]),
  ('Defenses', [('split', 'Splitting', 'egodefenses'), ('proj', 'Projection', 'egodefenses'), ('act', 'Acting out', 'egodefenses'),
                ('sub', 'Sublimation', 'egodefenses')]),
]
KEYS = [k for _, opts in SECTIONS for k, _, _ in opts]
PDS = ['par', 'szd', 'szt', 'asp', 'bpd', 'his', 'nar', 'avd', 'dep', 'ocpd']

# ════════ 1. the cluster board ════════
add('<rect class="dyn-soft" x="140" y="110" width="2200" height="510" rx="28"/>')
text('Three clusters — pick one: it lights up with its look-alike, and the case card below fills in', 170, 150, 'dyn-big')
text('Personality disorders: inflexible, pervasive patterns, usually ego-syntonic, present by early adulthood (First Aid p. 582)',
     170, 172, 'dyn-cap')
text('Results: ↑ present or needed · ↓ absent or not needed · ↔ either way', 170, 194, 'dyn-cap')
COLS = [  # (x, w, title, caption, node x, [(key, label, sub, lane, card, y)])
  (150, 710, 'Cluster A — weird', 'odd, eccentric · genetic link to schizophrenia', 500, [
    ('par', 'Paranoid', 'distrusts everyone · holds grudges', 'peA', 'clustera', 320),
    ('szt', 'Schizotypal', 'magical thinking · odd · eccentric', 'peA', 'clustera', 400),
    ('szd', 'Schizoid', 'a loner by choice · constricted affect', 'peA', 'clustera', 480)]),
  (875, 735, 'Cluster B — wild', 'dramatic, erratic · mood and substance use disorders', 1210, [
    ('his', 'Histrionic', 'attention-seeking · shallow, dramatic', 'peB', 'clusterb', 320),
    ('bpd', 'Borderline', 'unstable · fears abandonment · self-harm', 'peB', 'borderline', 400),
    ('nar', 'Narcissistic', 'grandiose · entitled · fragile inside', 'peB', 'clusterb', 480),
    ('asp', 'Antisocial', 'no remorse · ≥ 18, conduct before 15', 'peB', 'antisocial', 560)]),
  (1625, 705, 'Cluster C — worried', 'anxious, fearful · anxiety disorders', 1950, [
    ('ocpd', 'Obsessive-compulsive (PD)', 'order, perfection, control', 'peC', 'clusterc', 320),
    ('dep', 'Dependent', 'clingy · submissive · cannot decide', 'peC', 'clusterc', 400),
    ('avd', 'Avoidant', 'wants friends · fears rejection', 'peC', 'clusterc', 480)]),
]
NODEPOS = {}
nodes = []
for (cx, cw, title, cap, nx, rows) in COLS:
    add(f'<rect x="{cx}" y="214" width="{cw}" height="396" rx="20" style="fill:none;stroke:var(--line-2);stroke-width:2"/>')
    text(title, cx + 20, 248, 'dyn-big')
    text(cap, cx + 20, 270, 'dyn-cap')
    for (k, lab, sub, lane, cid, y) in rows:
        NODEPOS[k] = ('tile', nx, y, cx, cw)
        nodes.append((f'pe{len(nodes) + 1}', lab, nx, y, lane, sub, [cid]))

# ════════ 2. the look-alikes that are not personality disorders ════════
add('<rect class="dyn-soft" x="140" y="640" width="2200" height="172" rx="28"/>')
text('Look-alikes outside the personality disorders', 170, 676, 'dyn-big')
LOOK = [  # (key, label, sub, card, x)
  ('delus', 'Delusional disorder', 'a fixed delusion > 1 month', 'delusional', 330),
  ('schz', 'Schizophrenia', 'sustained psychosis', 'schizo', 690),
  ('bip', 'Bipolar disorder', 'mood comes in episodes', 'bipolar', 1050),
  ('cond', 'Conduct disorder', 'the same pattern under 18', 'conductodd', 1410),
  ('sad', 'Social anxiety disorder', 'fears specific situations', 'phobia', 1770),
  ('ocd', 'Obsessive-compulsive disorder', 'unwanted obsessions, compulsions', 'ocd', 2130),
]
YL = 740
for (k, lab, sub, cid, x) in LOOK:
    NODEPOS[k] = ('look', x, YL, None, None)
    nodes.append((f'pe{len(nodes) + 1}', lab, x, YL, 'peL', sub, [cid]))

# who lights with whom (the pick + its look-alikes, lit the same way)
NEAR = dict(par=['delus'], szd=['avd'], szt=['schz'], asp=['cond'], bpd=['bip', 'his'], his=['bpd'], nar=['bip'],
            avd=['szd', 'sad'], dep=['avd'], ocpd=['ocd'], ocd=['ocpd'], cond=['asp'],
            split=['bpd'], proj=['par'], act=['bpd'], sub=[])
DEFENSE = {'split', 'proj', 'act', 'sub'}
def lit_by(node):
    return O(*[k for k in KEYS if node == k or node in NEAR[k]])

for node, (kind, x, y, cx, cw) in NODEPOS.items():
    lb = lit_by(node)
    if not lb: continue
    if kind == 'tile':
        add(f'<rect x="{cx + 8}" y="{y - 30}" width="{cw - 16}" height="60" rx="16" style="{BAND}"/>', when=lb)
        if node in KEYS: text('▶ this one', cx + 20, y + 4, TAG, when=O(node))
        near = [q for q in KEYS if node in NEAR[q] and q not in DEFENSE]
        if near: text('look-alike', cx + 20, y + 4, 'nf-l2', when=O(*near))
        users = [q for q in KEYS if node in NEAR[q] and q in DEFENSE]
        if users: text('uses it', cx + 20, y + 4, 'nf-l2', when=O(*users))
    else:
        add(f'<rect x="{x - 172}" y="{y - 32}" width="344" height="64" rx="16" style="{BAND}"/>', when=lb)
        if node in KEYS: text('▶ this one', x, 798, TAG, 'middle', when=O(node))
        near = [q for q in KEYS if node in NEAR[q]]
        if near: text('look-alike', x, 798, 'nf-l2', 'middle', when=O(*near))

# the "tell apart" lines (each pair drawn once, lit for both partners)
PATHS = {
  ('par', 'delus'): ('M500 320 C190 330 190 700 330 740', 560),
  ('szt', 'schz'): ('M500 400 C760 420 760 650 690 740', 460),
  ('szd', 'avd'): ('M500 480 C560 640 1890 640 1950 480', 1600),
  ('avd', 'sad'): ('M1950 480 C1950 620 1770 620 1770 740', 320),
  ('dep', 'avd'): ('M2100 400 C2250 400 2250 480 2100 480', 260),
  ('ocpd', 'ocd'): ('M2100 320 C2320 330 2320 640 2130 740', 620),
  ('his', 'bpd'): ('M1350 320 C1520 320 1520 400 1350 400', 300),
  ('bpd', 'bip'): ('M1070 400 C930 420 930 680 1050 740', 440),
  ('nar', 'bip'): ('M1070 480 C960 500 960 690 1050 740', 340),
  ('asp', 'cond'): ('M1300 575 C1400 610 1410 660 1410 740', 230),
}
def path_for(a, b):
    return PATHS.get((a, b)) or PATHS.get((b, a))
flows = []
for k in KEYS:
    if k in DEFENSE: continue
    for q in NEAR[k]:
        d, ln = path_for(k, q)
        add(f'<path d="{d}" style="fill:none;stroke:var(--dk5);stroke-width:3;stroke-dasharray:9 7;opacity:.8"/>', when=O(k))
        flows.append(dict(d=d, len=ln, speed=150, r=6, when=O(k), base=dict(cmp=max(3, round(ln / 160)))))

# ════════ 3. the case card ════════
add('<rect class="dyn-soft" x="140" y="832" width="2200" height="250" rx="28"/>')
text('Pick a disorder or a defense — its case card fills in here', 170, 870, 'dyn-big', unless=['pd:*'])
text('Each disorder lights its look-alike: the case card says how to tell them apart.', 470, 940, 'nf-l2', unless=['pd:*'])
ROWL = ['Cluster', 'Core pattern', 'Defense · tell-tale', 'Look-alike — how to tell', 'Therapy · what to do']
RY = [906, 940, 974, 1008, 1042]
for lab, y in zip(ROWL, RY):
    text(lab, 170, y, 'nf-l1', when=['pd:*'])
A = 'A — odd, eccentric ("weird") · genetic link to schizophrenia'
B = 'B — dramatic, emotional, erratic ("wild") · genetic link to mood and substance use disorders'
C = 'C — anxious, fearful ("worried") · genetic link to anxiety disorders'
CASE = dict(
  par=('Paranoid personality disorder', [A,
    'Pervasive distrust and suspiciousness — reads hidden threats in others, holds grudges, doubts a partner’s fidelity',
    'Projection: attributes to others the impulses they cannot accept in themselves',
    'Delusional disorder has fixed delusions — paranoid PD does not · schizophrenia adds hallucinations or thought disorder',
    'Psychotherapy is the treatment of choice — straightforward and professional, not overly warm; admit mistakes honestly']),
  szd=('Schizoid personality disorder', [A,
    'Lifelong social withdrawal by preference — solitary pursuits, constricted affect, indifferent to praise or criticism',
    'Withdrawal and fantasy: an inner, imaginary life — the aloofness rests on a fear of intimacy',
    'Avoidant PD wants relationships but fears rejection; schizoid prefers to be alone · schizotypal adds odd thinking',
    'Psychotherapy as for paranoid PD; in group therapy they may stay silent, yet the group can become their only social contact']),
  szt=('Schizotypal personality disorder', [A + ' · on the schizophrenia spectrum',
    'Eccentric appearance, odd beliefs or magical thinking, ideas of reference, odd speech, few if any close friends',
    'Under stress: brief psychotic symptoms — then back to the baseline oddness',
    'Schizophrenia has sustained psychosis; in schizotypal PD psychotic symptoms are absent or brief and fragmentary',
    'Psychotherapy — never ridicule or judge the odd beliefs; antipsychotics may help ideas of reference']),
  asp=('Antisocial personality disorder', [B,
    'Disregard for others’ rights without remorse — lies, impulsivity, aggression, criminality · males > females',
    'A charming, credible veneer — a stress interview confronting inconsistencies may reveal the hostility beneath',
    'Conduct disorder is the same pattern under 18 · antisocial PD needs age ≥ 18 with conduct disorder before 15',
    'Limited evidence: contingency management and other reward-based programs work better than CBT']),
  bpd=('Borderline personality disorder', [B,
    'Unstable mood, self-image and relationships, fear of abandonment, impulsivity, self-mutilation, suicidality, emptiness · F > M',
    'Splitting (all good or all bad) · projective identification · labile transferences; acts out impulses in therapy',
    'Bipolar or depressive disorder lacks the abandonment fear, splitting, emptiness and identity diffusion · histrionic: fewer suicide attempts',
    'Dialectical behavior therapy (the most evidence); drugs for target symptoms only — avoid benzodiazepines']),
  his=('Histrionic personality disorder', [B,
    'Attention-seeking, dramatic speech and emotion, shallow labile affect, sexually provocative, uses appearance to draw attention',
    'Repression and dissociation: unaware of their true feelings; reality testing slips under stress',
    'Borderline PD: suicide attempts, identity diffusion and brief psychotic episodes are more likely there',
    'Psychoanalytically oriented psychotherapy — clarifying their real feelings']),
  nar=('Narcissistic personality disorder', [B,
    'Grandiosity and entitlement, needs admiration, lacks empathy, envious; demands the best · fragile self-esteem',
    'Criticism → rage or defensiveness; blows to self-esteem → depressed mood, dysthymia or major depression',
    'Mania: its grandiosity comes in episodes, with euphoria and functional impairment · borderline: more anxiety, more chaos',
    'Hard to treat: psychoanalytic approaches or group therapy; lithium for mood swings, serotonergic antidepressants']),
  avd=('Avoidant personality disorder', [C,
    'Hypersensitive to rejection and criticism, socially inhibited, timid, feels inadequate — yet desires relationships',
    'Needs a strong guarantee of uncritical acceptance; refusal of any request → withdraws and feels hurt',
    'Schizoid PD wants to be alone · social anxiety disorder avoids specific situations, not contact in general — they may co-occur',
    'Psychotherapy built on alliance, group therapy, assertiveness training; β-blockers (atenolol) for autonomic arousal']),
  dep=('Dependent personality disorder', [C,
    'Excessive need to be taken care of — clingy, submissive, cannot decide alone, low self-confidence',
    'Tolerates an abusive or unfaithful partner to keep the attachment · in folie à deux, often the submissive partner',
    'Avoidant PD is similar, but dependent fears abandonment more · borderline and histrionic depend on a series of people',
    'Often successful: insight-oriented, behavioral, assertiveness, family and group therapy']),
  ocpd=('Obsessive-compulsive personality disorder', [C,
    'Preoccupied with order, rules, perfectionism and control — rigid, stubborn, indecisive, cannot delegate · ego-syntonic',
    'Isolation of affect, intellectualization, rationalization, reaction formation, undoing',
    'OCD: only OCD has genuine obsessions and compulsions, and the patient finds them unwanted (ego-dystonic)',
    'Cognitive or cognitive behavioral therapy; unlike most PDs, some seek help on their own']),
  ocd=('Obsessive-compulsive disorder', ['Not a personality disorder — an obsessive-compulsive and related disorder',
    'Intrusive obsessions and/or compulsions that relieve the distress — the patient finds them unwanted (ego-dystonic)',
    'Associated with tic disorders; poor insight is linked to worse outcomes',
    'OCPD: order and perfectionism the patient agrees with — no genuine obsessions or compulsions',
    'CBT and SSRIs; clomipramine and venlafaxine second line']),
  cond=('Conduct disorder', ['Not a personality disorder — a disruptive behavior disorder of childhood',
    'Repetitive aggression to people or animals, destruction of property, theft or deceit — ≥ 3 behaviors in the past 12 months',
    'For some youth, a lifelong pattern culminating in antisocial PD — after 18 often reclassified',
    'Antisocial PD needs age ≥ 18; conduct disorder is diagnosed after 18 only if antisocial PD criteria are not met',
    'Psychotherapy (eg, CBT)']),
  split=('Splitting', ['Immature defense — common in borderline personality disorder',
    'Believes people are all good or all bad at different times — an intolerance of ambiguity',
    'On a ward: idealizes some staff and disparages others — it can provoke the staff to turn against the patient',
    'Idealization keeps only the all-good half — extremely positive thoughts, the flaws ignored',
    'Staff anticipate it, discuss it in meetings, and gently confront: no one is all good or all bad']),
  proj=('Projection', ['Immature defense — typical of paranoid personality disorder',
    'Attributes an unacceptable internal impulse to someone else',
    'Wants to be unfaithful → accuses the spouse of cheating',
    'Displacement redirects the feeling onto a neutral person or object; projection relocates the impulse itself',
    'Admit even minor mistakes; never argue or confront — counterprojection credits the patient’s feelings']),
  act=('Acting out', ['Immature defense — borderline patients act out their impulses in therapy',
    'Copes with a stressor or conflict through action instead of reflection or feelings',
    'Skips the next therapy session after a painful one · tantrums, apparently motiveless assaults',
    'Passive aggression shows hostility indirectly (repeatedly late) — acting out is direct action',
    'The patient has lost control: first get their attention; if frightened, leave and call for help']),
  sub=('Sublimation', ['Mature defense — mature adults wear a SASH: sublimation, altruism, suppression, humor',
    'Replaces an unacceptable wish with a similar course of action that is socially acceptable',
    'Aggression toward demanding parents channeled into excelling at sports',
    'Reaction formation replaces the feeling with its opposite (overprotecting a resented child) — sublimation keeps the drive',
    'A mature defense — nothing to undo']),
)
for k in KEYS:
    title, vals = CASE[k]
    text(title, 170, 870, 'dyn-big', when=O(k))
    for v, y in zip(vals, RY):
        text(v, 470, y, 'nf-l2', when=O(k))

# ════════ 4. the defense scenes ════════
add('<rect class="dyn-soft" x="140" y="1102" width="2200" height="384" rx="28"/>')
text('Defenses in play — what each one does with an unwanted feeling (First Aid pp. 570–571)', 170, 1140, 'dyn-big')
text('immature: splitting, projection, acting out · mature: sublimation (SASH) · borderline lights splitting, paranoid lights projection',
     170, 1162, 'dyn-cap')
SX = dict(split=150, proj=700, act=1250, sub=1800)
SLIT = dict(split=O('split', 'bpd'), proj=O('proj', 'par'), act=O('act'), sub=O('sub'))
SCENE = dict(split=('Splitting', 'immature · borderline PD'), proj=('Projection', 'immature · paranoid PD'),
             act=('Acting out', 'immature · action, not words'), sub=('Sublimation', 'mature · the SASH'))
for s, x0 in SX.items():
    add(f'<rect x="{x0}" y="1180" width="530" height="296" rx="20" style="fill:none;stroke:var(--line-2);stroke-width:2"/>')
    add(f'<rect x="{x0}" y="1180" width="530" height="296" rx="20" style="{BAND}"/>', when=SLIT[s])
    nodes.append((f'pe{len(nodes) + 1}', SCENE[s][0], x0 + 140, 1218, 'peD', SCENE[s][1], ['egodefenses']))

def fig(x, y, dim=False):
    """a person: head + body (y = shoulders)"""
    st = 'stroke:var(--ink-2);stroke-width:3;fill:none;stroke-linecap:round'
    return (f'<circle cx="{x}" cy="{y - 22}" r="12" style="fill:var(--surface);stroke:var(--ink-2);stroke-width:3"/>'
            f'<path d="M{x} {y - 10} V{y + 22} M{x - 16} {y + 2} H{x + 16} M{x} {y + 22} L{x - 12} {y + 44} M{x} {y + 22} L{x + 12} {y + 44}" style="{st}"/>')
def box(x, y, w, h, dash=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2.5'
            + (';stroke-dasharray:7 6' if dash else '') + '"/>')
# — splitting: the patient sorts the same staff into all good / all bad
add(fig(410, 1345) + fig(230, 1300) + fig(230, 1390) + fig(590, 1300) + fig(590, 1390))
text('all good', 230, 1258, 'nf-l1', 'middle')
text('all bad', 590, 1258, 'nf-l1', 'middle')
text('patient', 410, 1412, 'nf-l2', 'middle')
text('the same staff, sorted into all good or all bad', 170, 1462, 'dyn-cap', when=SLIT['split'])
SPL = [('M392 1338 L252 1302', 'good'), ('M392 1352 L252 1388', 'good'), ('M428 1338 L568 1302', 'bad'), ('M428 1352 L568 1388', 'bad')]
# — projection: one's own impulse is seen in someone else
add(fig(800, 1345) + fig(1130, 1345) +
    '<ellipse cx="880" cy="1268" rx="80" ry="24" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2.5"/>'
    '<circle cx="826" cy="1302" r="6" style="fill:var(--surface);stroke:var(--ink-3);stroke-width:2"/>')
text('my own impulse', 880, 1272, 'nf-l2', 'middle')
text('self', 800, 1412, 'nf-l2', 'middle')
text('someone else', 1130, 1412, 'nf-l2', 'middle')
text('the impulse is attributed to the other person', 720, 1462, 'dyn-cap', when=SLIT['proj'])
PRJ = 'M955 1276 C1020 1250 1080 1270 1118 1316'
# — acting out: feeling → action, skipping the words
add(box(1270, 1322, 165, 50) + box(1455, 1236, 170, 50, dash=True) + box(1640, 1322, 120, 50) +
    '<path d="M1395 1322 L1475 1288 M1610 1288 L1690 1322" style="fill:none;stroke:var(--ink-3);stroke-width:2.5;stroke-dasharray:6 6"/>')
text('painful feeling', 1352, 1352, 'nf-l1', 'middle')
text('words · reflection', 1540, 1266, 'nf-l1', 'middle')
text('action', 1700, 1352, 'nf-l1', 'middle')
add('<path d="M1423 1293 L1447 1317 M1447 1293 L1423 1317" style="fill:none;stroke:var(--bad);stroke-width:4;stroke-linecap:round"/>',
    when=SLIT['act'])
text('the reflection is skipped', 1540, 1306, 'nf-l2', 'middle', when=SLIT['act'])
text('feeling straight into action — skips the next session', 1270, 1462, 'dyn-cap', when=SLIT['act'])
ACT = 'M1435 1347 H1640'
# — sublimation: the wish kept, the outlet made acceptable
add(box(1820, 1322, 180, 50) + box(2130, 1322, 180, 50))
text('unacceptable wish', 1910, 1352, 'nf-l1', 'middle')
text('acceptable outlet', 2220, 1352, 'nf-l1', 'middle')
text('aggression', 1910, 1398, 'nf-l2', 'middle')
text('excelling at sports', 2220, 1398, 'nf-l2', 'middle')
text('the same drive, a socially acceptable form', 1820, 1462, 'dyn-cap', when=SLIT['sub'])
SUB = 'M2000 1347 H2130'

# scene particles: a calm trickle in the default state, a stronger stream when that scene is lit
for d, kd in SPL:
    flows.append(dict(d=d, len=150, speed=90, r=6, unless=['pd:*'], base={kd: 1}))
    flows.append(dict(d=d, len=150, speed=110, r=7, when=SLIT['split'], base={kd: 3}))
for s, d, ln in (('proj', PRJ, 200), ('act', ACT, 205), ('sub', SUB, 130)):
    flows.append(dict(d=d, len=ln, speed=90, r=6, unless=['pd:*'], base=dict(imp=2)))
    flows.append(dict(d=d, len=ln, speed=120, r=7, when=SLIT[s], base=dict(imp=max(3, round(ln / 55)))))

kinds = dict(cmp=['tell', '--dk5'], imp=['imp', '--dk9'], good=['good', '--ok'], bad=['bad', '--bad'])
# one colour per group, so each colour is named by its Show chip (the drafts check.py takes 2-element kinds only)
groups = [['tell', 'Tell apart'], ['imp', 'Impulse or feeling'], ['good', 'All good'], ['bad', 'All bad']]

# ════════ notes ════════
notes = {
  '': 'Personality disorders are inflexible, pervasive patterns that are usually ego-syntonic — the person rarely sees a problem. '
      'Pick one: it lights with its look-alike, the line between them carries the tell, and the case card fills in.',
  'pd:par': 'Paranoid PD: pervasive distrust and suspicion, grudges, doubts about a partner’s fidelity — through projection. '
            'No fixed delusions (vs delusional disorder) and no hallucinations (vs schizophrenia). Psychotherapy: straightforward, '
            'professional, honest about mistakes.',
  'pd:szd': 'Schizoid PD: a loner by choice — constricted affect, indifferent to praise or criticism, an inner life of fantasy. '
            'Avoidant PD is just as isolated but wants relationships; schizotypal adds odd thinking.',
  'pd:szt': 'Schizotypal PD: odd beliefs, magical thinking, ideas of reference, eccentric appearance — on the schizophrenia '
            'spectrum. Any psychotic symptoms are brief and fragmentary; sustained psychosis means schizophrenia.',
  'pd:asp': 'Antisocial PD: disregard for others’ rights without remorse — lying, impulsivity, aggression, crime. It needs age '
            '≥ 18 with conduct disorder before 15; under 18 the diagnosis is conduct disorder. Reward-based programs beat CBT.',
  'pd:bpd': 'Borderline PD: unstable mood, self-image and relationships, fear of abandonment, self-harm and emptiness, with '
            'splitting as the major defense. Mood disorders lack those core features. Dialectical behavior therapy is first line.',
  'pd:his': 'Histrionic PD: attention-seeking, dramatic, shallow and labile emotion, sexually provocative — defended by repression '
            'and dissociation. Suicide attempts and identity diffusion point to borderline instead.',
  'pd:nar': 'Narcissistic PD: grandiosity, entitlement, need for admiration, no empathy — and rage at criticism over a fragile '
            'self-esteem. Grandiosity that comes in episodes with euphoria and impairment is mania.',
  'pd:avd': 'Avoidant PD: hypersensitive to rejection, timid, feels inadequate — but wants relationships (schizoid does not). '
            'Social anxiety disorder fears specific situations rather than contact in general; the two can co-occur.',
  'pd:dep': 'Dependent PD: clingy, submissive, cannot decide alone, and often stays with an abusive partner. Close to avoidant, '
            'but the fear of abandonment is greater. Treatment is often successful (assertiveness, insight-oriented, group).',
  'pd:ocpd': 'Obsessive-compulsive PD: order, rules, perfection and control, ego-syntonic — the patient thinks the rules are right. '
             'Defenses: isolation of affect, intellectualization, reaction formation, undoing. CBT.',
  'pd:ocd': 'OCD is not a personality disorder: genuine obsessions and compulsions the patient finds unwanted (ego-dystonic). OCPD '
            'has the perfectionism without them. OCD: CBT and SSRIs, clomipramine second line.',
  'pd:cond': 'Conduct disorder: repeated aggression, destruction, theft or deceit in a child or adolescent. After 18 it is often '
             'reclassified as antisocial PD — which needs conduct disorder before 15. Psychotherapy (CBT).',
  'pd:split': 'Splitting: people are all good or all bad at different times — the borderline patient idealizes some staff and '
              'disparages others. Staff discuss it together and gently confront: no one is all good or all bad.',
  'pd:proj': 'Projection: one’s own unacceptable impulse is attributed to someone else — the man who wants to cheat accuses his '
             'wife. Typical of paranoid PD; meet it with honesty, not argument.',
  'pd:act': 'Acting out: a conflict is discharged in action instead of words or feelings — skipping therapy after a painful '
            'session, tantrums. The patient has lost control; get their attention first.',
  'pd:sub': 'Sublimation, a mature defense: an unacceptable wish becomes a similar, socially acceptable action — aggression '
            'channeled into sport. Reaction formation, by contrast, turns the feeling into its opposite.',
}

# ════════ readouts (↑ present or needed · ↓ absent or not needed · ↔ either way) ════════
R = lambda keys, d: dict(when=O(*keys), d=d)
readouts = [
  dict(l='Ego-syntonic', mods=[R(PDS, 1), R(['ocd'], -1)]),
  dict(l='Wants closeness', mods=[R(['avd', 'dep', 'bpd', 'szt'], 1), R(['szd'], -1)]),
  dict(l='Fears rejection or abandonment', mods=[R(['avd', 'dep', 'bpd'], 1), R(['szd'], -1)]),
  dict(l='Odd thinking or perception', mods=[R(['szt'], 1), R(['par', 'szd', 'avd'], -1)]),
  dict(l='Violates others’ rights', mods=[R(['asp', 'cond'], 1), R(['nar', 'his', 'par'], -1), R(['bpd'], 0)]),
  dict(l='Needs age ≥ 18', mods=[R(['asp'], 1), R(['cond'], -1)]),
  dict(l='Mature defense', mods=[R(['sub'], 1), R(['split', 'proj', 'act'], -1)]),
]

dyn = dict(
  kinds=kinds, groups=groups,
  switches=[dict(id='pd', label='Pick one', type='one', options=[[k, l, c] for _, opts in SECTIONS for k, l, c in opts],
                 sections=[[sec, [k for k, _, _ in opts]] for sec, opts in SECTIONS])],
  notes=notes, shapes=shapes, flows=flows, sites=[], readouts=readouts,
  panel=dict(x=2420, y=110, w=1000),
  src='OCOM Psych SDL 28–30 (Kaplan & Sadock ch 19, 23; Osmosis ch 98–100) · First Aid pp. 570–571, 574, 580, 582 · Kaplan & Sadock ch 2, 9')

MAP = dict(
  id='persim', title='Personality Disorders & Ego Defenses', topic='behav', after='psychsom',
  sub='The ten personality disorders by cluster (A weird · B wild · C worried) beside the look-alikes that are not personality '
      'disorders — OCD vs OCPD, conduct disorder → antisocial — and four defenses in motion: splitting, projection, acting out, '
      'sublimation. Pick one: it lights with its look-alike, the case card says how to tell them apart and what to do. Tap a tile for its card',
  w=3500, h=1546,
  fa='570–571, 574, 580, 582', src=[K19, K23, K9, K2],
  lanes=[('peA', 'Cluster A — odd', 'sugars'), ('peB', 'Cluster B — dramatic', 'tca'), ('peC', 'Cluster C — anxious', 'glycogen'),
         ('peL', 'Look-alikes', 'glycolysis'), ('peD', 'Ego defenses', 'ppp')],
  comps=[],
  nodes=nodes,
  panels=[
    (2420, 1000, 1000, 'Every personality disorder (First Aid p. 582; Kaplan ch 19)', [
      ('Pattern', 'inflexible, pervasive, maladaptive · distress or impairment'),
      ('Insight', 'usually ego-syntonic — the person is not aware of a problem'),
      ('Onset', 'usually present by early adulthood'),
      ('Treatment', 'psychotherapy first; drugs for target symptoms'),
      ('Two or more fit?', 'diagnose each one that meets criteria'),
      ('Only in an episode?', 'not a personality disorder')]),
    (2420, 1240, 1000, 'Ego defenses (First Aid pp. 570–571)', [
      ('Mature — SASH', 'sublimation, altruism, suppression, humor'),
      ('Displacement', 'feeling redirected to a neutral target (vs projection)'),
      ('Repression', 'involuntary forgetting (vs suppression: intentional)'),
      ('Transference', 'patient projects feelings about others onto the physician'),
      ('Countertransference', 'physician projects onto the patient')]),
  ],
  dyn=dyn,
)
