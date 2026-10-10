# Bacterial Toxins in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# Three schematic scenes the toxins hit: a gut cell (Gs, Gi, adenylyl cyclase, guanylyl cyclase C, cAMP/cGMP → CFTR →
# chloride and water into the lumen; the ribosome with EF-2; the lecithin membrane), two synapses (motor nerve → muscle,
# inhibitory interneuron → motor neuron) and an APC–T-cell pair (MHC II, TCR). A `one` switch sends one toxin in and the
# scene answers: cholera, E. coli LT and ST, pertussis, diphtheria, Pseudomonas exotoxin A, C. perfringens α-toxin,
# botulinum, tetanus and a superantigen (TSST-1). 5 readouts. Facts from the pinned cards; FA pages in `fa`. No new cards.
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

O = lambda *k: [f'tx:{x}' for x in k]
PANY = 1180
def X(cx, cy, s=18): return f'<path d="M{cx - s} {cy - s} L{cx + s} {cy + s} M{cx + s} {cy - s} L{cx - s} {cy + s}" class="nf-x"/>'
def box(x0, y0, x1, y1, lab, sub='', cls='dyn-cell'):
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="18" class="{cls}"/>')
    text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + (0 if sub else 6), 'nf-l1', 'middle')
    if sub: text(sub, (x0 + x1) // 2, (y0 + y1) // 2 + 22, 'nf-l2', 'middle')
CAMP = O('cholera', 'lt', 'pert')
SECRETE = O('cholera', 'lt', 'st')
EF2 = O('diph', 'pseudo')

text('Bacterial toxins — what each one breaks', 180, 150, 'dyn-big')
text('pick a toxin: it enters from the top and hits its target', 180, 176, 'dyn-cap')

# ════════ scene 1: a gut cell ════════
add('<rect x="330" y="330" width="270" height="680" style="fill:var(--nf-h2o);fill-opacity:.1"/>')
text('gut lumen', 465, 1040, 'nf-l1', 'middle')
add('<rect x="600" y="330" width="900" height="680" rx="40" class="dyn-soft"/>', unless=O('perf'))
add('<rect x="600" y="330" width="900" height="680" rx="40" style="fill:none;stroke:var(--bad);stroke-width:6;stroke-dasharray:14 12"/>', when=O('perf'))
text('target cell (gut epithelium for the diarrhea toxins)', 1050, 316, 'nf-l2', 'middle')
box(760, 720, 900, 790, 'Gs', 'switches AC on')
box(760, 840, 900, 910, 'Gi', 'switches AC off')
box(990, 770, 1170, 850, 'adenylyl cyclase')
box(1100, 560, 1260, 630, 'cAMP')
box(1260, 860, 1440, 960, 'ribosome', 'EF-2 elongates')
add(X(892, 728, 12), when=O('cholera', 'lt'))
text('Gs locked ON (ADP-ribosylated)', 830, 700, 'nf-l1 dyn-tag', 'middle', when=O('cholera', 'lt'))
add(X(892, 848, 12), when=O('pert'))
text('Gi disabled (ADP-ribosylated) — cAMP stays high', 830, 950, 'nf-l1 dyn-tag', 'middle', when=O('pert'))
add(X(1430, 870, 12), when=EF2)
text('EF-2 ADP-ribosylated — protein synthesis stops', 1350, 990, 'nf-l1 dyn-tag', 'middle', when=EF2)
text('lecithinase splits the membrane — the cell lyses', 1050, 400, 'nf-l1 dyn-tag', 'middle', when=O('perf'))
text('heat-stable toxin → guanylyl cyclase C → cGMP', 1050, 400, 'nf-l1 dyn-tag', 'middle', when=O('st'))
text('rice-water stool: Cl⁻ and water pour out', 465, 300, 'nf-l1 dyn-tag', 'middle', when=SECRETE)

# ════════ scene 2: two synapses ════════
box(1700, 330, 2150, 450, 'Motor nerve terminal', 'ACh vesicles')
box(1700, 560, 2150, 630, 'Skeletal muscle')
box(1700, 740, 2150, 860, 'Inhibitory interneuron', 'GABA · glycine (Renshaw)')
box(1700, 970, 2150, 1040, 'Motor neuron → muscle')
text('flaccid, descending paralysis', 1925, 680, 'nf-l1 dyn-tag', 'middle', when=O('botu'))
text('spastic: lockjaw, risus sardonicus, opisthotonos', 1925, 1090, 'nf-l1 dyn-tag', 'middle', when=O('tet'))

# ════════ scene 3: APC and T cell ════════
box(330, 1180, 760, 1380, 'Antigen-presenting cell', 'MHC class II')
box(1070, 1180, 1500, 1380, 'T cell', 'TCR Vβ')
add('<rect x="760" y="1250" width="40" height="60" rx="8" style="fill:var(--dk6);fill-opacity:.6"/><rect x="1030" y="1250" width="40" height="60" rx="8" style="fill:var(--dk2);fill-opacity:.6"/>')
add('<path d="M800 1240 Q915 1180 1030 1240 M800 1320 Q915 1380 1030 1320" style="fill:none;stroke:var(--bad);stroke-width:10"/>', when=O('super'))
text('clamped outside the groove — up to a fifth of all T cells fire', 915, 1430, 'nf-l1 dyn-tag', 'middle', when=O('super'))
text('normally only a matching TCR responds', 915, 1430, 'nf-l2', 'middle', unless=O('super'))

# ════════ motion ════════
def m(when, **kw): return dict(when=when, **kw)
TOX_TO = dict(cholera='M1050 230 V700 H900', lt='M1050 230 V700 H900', pert='M1050 230 V880 H900', st='M1050 230 V420 H640',
              diph='M1050 230 V500 H1350 V860', pseudo='M1050 230 V500 H1350 V860', perf='M1050 230 V330',
              botu='M1925 230 V330', tet='M2200 230 V800 H2150', super='M915 1100 V1270')
flows = [dict(d=d, len=600, speed=150, r=10, base=dict(tox=3), when=O(k)) for k, d in TOX_TO.items()]
flows += [
  dict(d='M1080 770 C1080 700 1150 660 1180 630', len=200, speed=80, r=8, base=dict(camp=1), mods=[m(CAMP, set=dict(camp=5))]),
  dict(d='M1100 595 C900 560 750 500 615 500', len=520, speed=120, r=8, base=dict(camp=1), mods=[m(CAMP, set=dict(camp=5))]),
  dict(d='M640 790 C700 700 690 560 615 520', len=320, speed=90, r=8, base=dict(cgmp=4), when=O('st')),
  dict(d='M600 520 H340', len=260, speed=110, r=9, base=dict(h2o=1), mods=[m(SECRETE, set=dict(h2o=7))]),
  dict(d='M1440 910 H1490', len=60, speed=30, r=7, base=dict(prot=2), mods=[m(EF2, set=dict(prot=0))]),
  dict(d='M1925 450 V560', len=110, speed=60, r=8, base=dict(nt=4), mods=[m(O('botu'), set=dict(nt=0))]),
  dict(d='M1925 860 V970', len=110, speed=60, r=8, base=dict(nt=4), mods=[m(O('tet'), set=dict(nt=0))]),
  dict(d='M1500 1280 H1700', len=200, speed=90, r=8, base=dict(cyt=1), mods=[m(O('super'), set=dict(cyt=7))]),
]
sites = [
  dict(x=600, y=500, n=[-1, 0], w=12, t='ch', l='CFTR', s='Cl⁻ out', ions=[['cl', 'out', 2]], c='vibrio', boost=SECRETE, la='end', lx=555, ly=470),
  dict(x=600, y=790, n=[-1, 0], w=12, t='rec', l='guanylyl cyclase C', s='heat-stable toxin', ions=[], c='etectox',
       boost=O('st'), la='end', lx=555, ly=790),
  dict(x=1925, y=450, n=[0, 1], w=10, t='rec', l='', aria='SNAREs — botulinum', c='botulinum', ions=[], block=O('botu')),
  dict(x=1925, y=860, n=[0, 1], w=10, t='rec', l='', aria='Synaptobrevin — tetanus', c='tetanus', ions=[], block=O('tet')),
  dict(x=915, y=1280, n=[0, 1], w=10, t='rec', l='', aria='Superantigen', c='superag', ions=[]),
]

readouts = [
  dict(l='Cell cAMP', mods=[dict(when=CAMP, d=1)]),
  dict(l='Watery diarrhea', mods=[dict(when=SECRETE, d=1)]),
  dict(l='Protein synthesis', mods=[dict(when=EF2, d=-1)]),
  dict(l='Muscle tone', mods=[dict(when=O('botu'), d=-1), dict(when=O('tet'), d=1)]),
  dict(l='Cytokine release', mods=[dict(when=O('super'), d=1)]),
]

notes = {
  '': 'Exotoxins act on a precise target. Several are ADP-ribosylating enzymes (cholera, E. coli LT, pertussis, diphtheria, '
      'Pseudomonas exotoxin A); botulinum and tetanus are proteases of the SNARE machinery; C. perfringens α-toxin is a lecithinase; '
      'superantigens cross-link MHC II to the TCR.',
  'tx:cholera': 'Cholera toxin ADP-ribosylates Gs, locking adenylyl cyclase on: cAMP opens CFTR, chloride and water pour into the gut '
                '— rice-water stool, liters a day, without invasion. Oral rehydration.',
  'tx:lt': 'E. coli heat-labile toxin works exactly like cholera toxin (Gαs → ↑ cAMP) — traveler’s diarrhea. Labile in the Air '
           '(adenylate cyclase).',
  'tx:st': 'E. coli heat-stable toxin mimics guanylin and switches on guanylyl cyclase C — ↑ cGMP opens CFTR the same way. Stable on '
           'the Ground (guanylate cyclase).',
  'tx:pert': 'Pertussis toxin ADP-ribosylates Gi, so the brake on adenylyl cyclase is gone and cAMP stays high — disabled phagocytes '
             'and lymphocytosis. Whooping cough.',
  'tx:diph': 'Diphtheria toxin (β-prophage gene) ADP-ribosylates EF-2 and stops protein synthesis — a pseudomembrane locally, '
             'myocarditis and neuropathy at a distance.',
  'tx:pseudo': 'Pseudomonas exotoxin A ADP-ribosylates EF-2, like diphtheria toxin.',
  'tx:perf': 'C. perfringens α-toxin is a lecithinase (phospholipase C): it splits lecithin in membranes and lyses muscle, red cells '
             'and platelets — gas gangrene.',
  'tx:botu': 'Botulinum toxin cleaves the SNAREs an ACh vesicle needs, so no ACh is released — descending flaccid paralysis: diplopia, '
             'dysarthria, dysphagia, dyspnea. Antitoxin.',
  'tx:tet': 'Tetanus toxin climbs the motor axon and cleaves synaptobrevin in inhibitory interneurons — no GABA or glycine, so the '
            'motor neurons fire unchecked: spastic paralysis, trismus, risus sardonicus.',
  'tx:super': 'Superantigens (TSST-1, staph enterotoxins, strep pyrogenic exotoxins) clamp MHC II to the TCR Vβ outside the groove, '
              'so up to a fifth of all T cells fire — IL-1, IL-2, IFN-γ, TNF-α and shock.',
}

dyn = dict(
  kinds=dict(tox=['tox', '--bad'], camp=['msg', '--dk2'], cgmp=['msg', '--dk5'], cl=['ion', '--dk1'], h2o=['ion', '--nf-h2o'],
             prot=['msg', '--dk3'], nt=['msg', '--dk7'], cyt=['msg', '--dk4']),
  groups=[['tox', 'Toxin'], ['msg', 'Signals and products'], ['ion', 'Chloride and water']],
  switches=[dict(id='tx', label='Toxin', type='one', options=[
    ['cholera', 'Cholera toxin', 'vibrio'], ['lt', 'E. coli heat-labile (LT)', 'etectox'], ['st', 'E. coli heat-stable (ST)', 'etectox'],
    ['pert', 'Pertussis toxin', 'pertussis'], ['diph', 'Diphtheria toxin', 'diphtheria'], ['pseudo', 'Pseudomonas exotoxin A', 'pseudomonas'],
    ['perf', 'C. perfringens α-toxin', 'cperfringens'], ['botu', 'Botulinum toxin', 'botulinum'], ['tet', 'Tetanus toxin', 'tetanus'],
    ['super', 'Superantigen (TSST-1)', 'superag']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 130–131, 136–137, 141, 143–144 · Robbins ch 8')

MAP = dict(
  id='toxinsim', title='Bacterial Toxins in Motion', topic='id', after='toxins',
  sub='Send a toxin into its target and watch what breaks: cholera, E. coli LT and ST, pertussis, diphtheria, Pseudomonas exotoxin A, '
      'C. perfringens α-toxin, botulinum, tetanus and a superantigen',
  w=3600, h=1900,
  fa='130, 131, 136, 137, 141, 143, 144, 175',
  src=['Robbins ch 8 — Infectious diseases', 'Robbins ch 6 — Diseases of the immune system',
       'Katzung ch 44 — Tetracyclines, Macrolides, Clindamycin, Chloramphenicol, Streptogramins, Oxazolidinones, & Pleuromutilins',
       'Marks ch 14 — Translation: Synthesis of Proteins', 'Katzung ch 43 — Beta-Lactam & Other Cell Wall- & Membrane-Active Antibiotics',
       'Katzung ch 51 — Clinical Use of Antimicrobial Agents', 'Robbins ch 17 — The gastrointestinal tract',
       'Marks ch 10 — Cell Structure and Signaling by Chemical Messengers', 'Fundamental Neuroscience ch 4 — Chemical Signaling in the Nervous System',
       'Pawlina ch 2 — Cell Cytoplasm', 'Robbins ch 27 — Peripheral nerves and skeletal muscles', 'Katzung ch 27 — Skeletal Muscle Relaxants'],
  lanes=[('txAdp', 'ADP-ribosylating toxins', 'glycolysis'), ('txNerve', 'Nerve toxins', 'tca'), ('txOther', 'Membranes and superantigens', 'gluconeo')],
  nodes=[
    ('tx1', 'Cholera', 330, 1620, 'txAdp', 'Gs locked on', ['vibrio'], 'hub'),
    ('tx2', 'E. coli LT · ST', 760, 1620, 'txAdp', 'cAMP vs cGMP', ['etectox']),
    ('tx3', 'Pertussis', 1200, 1620, 'txAdp', 'Gi disabled', ['pertussis']),
    ('tx4', 'Diphtheria · exotoxin A', 1640, 1620, 'txAdp', 'EF-2', ['diphtheria', 'pseudomonas']),
    ('tx5', 'Botulinum toxin', 330, 1760, 'txNerve', 'flaccid', ['botulinum']),
    ('tx6', 'Tetanus toxin', 760, 1760, 'txNerve', 'spastic', ['tetanus']),
    ('tx7', 'C. perfringens', 1200, 1760, 'txOther', 'lecithinase', ['cperfringens']),
    ('tx8', 'Superantigens', 1640, 1760, 'txOther', 'TSST-1 · scarlet fever', ['superag'])],
  panels=[
    (2500, PANY, 1000, 'Same trick, different target (First Aid pp. 130–131)', [
      ('ADP-ribosylate Gs', 'cholera, E. coli LT — ↑ cAMP'),
      ('ADP-ribosylate Gi', 'pertussis — ↑ cAMP'),
      ('ADP-ribosylate EF-2', 'diphtheria, Pseudomonas exotoxin A'),
      ('Cleave SNAREs', 'botulinum (ACh) · tetanus (GABA, glycine)'),
      ('Botulism vs tetanus', 'flaccid vs spastic')])],
  dyn=dyn)
