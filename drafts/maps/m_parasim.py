# Parasite Life Cycles in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# A schematic body (brain, lungs, liver, blood and red cells, muscle, small bowel, colon, venous plexuses, bladder, skin of
# the feet) with the ways in (mosquito, food and water, soil and fresh water). A `one` switch picks a parasite; it travels
# its route through the body, the organs it damages light up and a tag gives the finding and the drug: malaria
# (falciparum, vivax/ovale), hookworm, Strongyloides, Ascaris, pinworm, Giardia, Entamoeba, Cryptosporidium, Toxoplasma,
# Trichinella, Taenia (tapeworm, cysticercosis), Schistosoma mansoni and haematobium. 5 readouts. Facts from the pinned
# cards; FA pages in `fa`. No new cards.
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
O = lambda *k: [f'p:{x}' for x in k]
PANY = 1180
B = dict(mos=(300, 260, 560, 340, 'Mosquito'), food=(300, 820, 600, 900, 'Food · water'), soil=(300, 1300, 600, 1380, 'Soil · fresh water'),
         skin=(820, 1390, 1080, 1450, 'Skin (feet)'), brain=(1100, 230, 1400, 320, 'Brain'), lung=(1000, 380, 1400, 540, 'Lungs'),
         liver=(1000, 620, 1300, 760, 'Liver'), rbc=(1500, 620, 1800, 760, 'Blood · red cells'), sb=(1000, 840, 1400, 980, 'Small bowel'),
         colon=(1000, 1040, 1400, 1160, 'Colon'), muscle=(1600, 380, 1900, 500, 'Muscle'), veins=(1500, 840, 1800, 980, 'Venous plexuses'),
         bladder=(1600, 1040, 1900, 1160, 'Bladder'))
C = {k: ((v[0] + v[2]) // 2, (v[1] + v[3]) // 2) for k, v in B.items()}
C['anus'] = (1200, 1240)

text('Parasite life cycles — the way in, the route, the damage', 180, 150, 'dyn-big')
text('pick a parasite and follow it through the body', 180, 176, 'dyn-cap')
for k, (x0, y0, x1, y1, lab) in B.items():
    add(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="24" class="{"dyn-soft" if k in ("mos", "food", "soil") else "dyn-cell"}"/>')
    text(lab, (x0 + x1) // 2, (y0 + y1) // 2 + 6, 'nf-l1', 'middle')
add('<circle cx="1200" cy="1240" r="22" class="dyn-cell"/>'); text('anus', 1240, 1246, 'nf-l2')

ROUTE = dict(
  falc=['mos', 'liver', 'rbc'], vivax=['mos', 'liver', 'rbc'],
  hook=['soil', 'skin', 'lung', 'sb'], strong=['soil', 'skin', 'lung', 'sb'], asc=['food', 'sb', 'lung', 'sb'],
  pin=['food', 'sb', 'colon', 'anus', 'food'], giar=['food', 'sb'], ent=['food', 'colon', 'liver'], cryp=['food', 'sb'],
  toxo=['food', 'sb', 'brain'], trich=['food', 'sb', 'muscle'], taen=['food', 'sb'], cyst=['food', 'sb', 'brain'],
  schm=['soil', 'skin', 'veins', 'liver'], schh=['soil', 'skin', 'veins', 'bladder'])
HIT = dict(falc=['rbc', 'brain'], vivax=['rbc', 'liver'], hook=['sb', 'skin'], strong=['sb', 'lung', 'skin'], asc=['sb', 'lung'],
           pin=['anus'], giar=['sb'], ent=['colon', 'liver'], cryp=['sb'], toxo=['brain'], trich=['muscle'], taen=['sb'],
           cyst=['brain'], schm=['liver'], schh=['bladder'])
TAG = dict(
  falc=('P. falciparum: infected red cells stick to capillaries — cerebral malaria', 'IV artesunate or quinine if severe'),
  vivax=('P. vivax/ovale: 48-h fevers; dormant hypnozoites in the liver relapse', 'chloroquine + primaquine for hypnozoites'),
  hook=('larvae through the feet → lungs → small bowel; sucks blood → iron deficiency', 'bendazoles or pyrantel pamoate'),
  strong=('skin → lungs → duodenum; autoinfection → hyperinfection with steroids, HTLV-1', 'ivermectin or bendazoles'),
  asc=('eggs hatch in the gut, larvae through the lungs (Löffler), ileocecal obstruction', 'bendazoles'),
  pin=('females lay eggs around the anus at night — itching, scratching, back to the mouth', 'bendazoles, pyrantel pamoate'),
  giar=('cysts in stream water; trophozoites coat the duodenum — fatty, foul, nonbloody diarrhea', 'tinidazole, nitazoxanide, metronidazole'),
  ent=('flask-shaped colonic ulcers — bloody diarrhea; portal vein → anchovy-paste liver abscess', 'metronidazole; paromomycin for cyst passers'),
  cryp=('chlorine-resistant oocysts — mild watery diarrhea; severe and chronic in AIDS', 'filter water; nitazoxanide'),
  toxo=('undercooked meat, cat feces; latent in brain — ring-enhancing lesions in AIDS', 'sulfadiazine + pyrimethamine (+ leucovorin)'),
  trich=('undercooked pork; larvae encyst in skeletal muscle — periorbital edema, myalgia', 'bendazoles'),
  taen=('larvae in undercooked pork → intestinal tapeworm (usually mild)', 'praziquantel'),
  cyst=('eggs from a human carrier → larvae encyst in the brain — seizures', 'albendazole for neurocysticercosis'),
  schm=('cercariae through the skin; eggs trapped in the liver — periportal fibrosis, portal HTN', 'praziquantel'),
  schh=('eggs in the bladder wall — hematuria, squamous cell carcinoma of the bladder', 'praziquantel'))
for k, hits in HIT.items():
    add(''.join(f'<rect x="{B[h][0]}" y="{B[h][1]}" width="{B[h][2] - B[h][0]}" height="{B[h][3] - B[h][1]}" rx="24" style="fill:var(--bad);fill-opacity:.12;stroke:var(--bad);stroke-width:5"/>'
                if h != 'anus' else '<circle cx="1200" cy="1240" r="30" style="fill:none;stroke:var(--bad);stroke-width:5"/>' for h in hits), when=O(k))
    a, b = TAG[k]
    text(a, 1150, 1530, 'nf-l1 dyn-tag', 'middle', when=O(k)); text('treat: ' + b, 1150, 1560, 'nf-l2', 'middle', when=O(k))
# malaria extras
add(f'<circle cx="{C["rbc"][0]}" cy="{C["rbc"][1]}" r="110" style="fill:none;stroke:var(--nf-blood);stroke-width:4;stroke-dasharray:8 8"/>', when=O('falc', 'vivax'))
for (dx, dy) in ((-30, 46), (0, 52), (30, 46)):
    add(f'<circle cx="{C["liver"][0] + dx}" cy="{C["liver"][1] + dy}" r="10" style="fill:var(--dk7)"/>', when=O('vivax'))
text('hypnozoites', C['liver'][0] - 140, C['liver'][1] + 40, 'nf-l2', 'end', when=O('vivax'))

# ════════ motion ════════
def path(keys):
    pts = [C[k] for k in keys]
    d = f'M{pts[0][0]} {pts[0][1]} ' + ' '.join(f'L{x} {y}' for x, y in pts[1:])
    L = sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
    return d, round(L)
flows = []
for k, keys in ROUTE.items():
    d, L = path(keys)
    flows.append(dict(d=d, len=L, speed=160, r=10, base=dict(par=4), when=O(k)))
    shapes.insert(0, dict(svg=f'<path d="{d}" style="fill:none;stroke:var(--dk7);stroke-width:4;stroke-dasharray:10 10;opacity:.5"/>', when=O(k)))
cx, cy = C['rbc']
flows.append(dict(d=f'M{cx + 110} {cy} A110 110 0 1 1 {cx + 109.9} {cy - 1}', len=690, speed=140, r=9, base=dict(par=4), when=O('falc', 'vivax')))
sx, sy = C['sb']
flows.append(dict(d=f'M{sx} {sy} C{sx - 500} {sy + 300} 700 1420 820 1420 L{C["lung"][0]} {C["lung"][1]} L{sx} {sy}', len=2400, speed=200, r=8,
                  base=dict(par=3), when=O('strong')))
sites = [dict(x=C['rbc'][0], y=B['rbc'][3], n=[0, 1], w=10, t='rec', l='', aria='Malaria', c='malaria', ions=[]),
         dict(x=C['sb'][0] + 150, y=B['sb'][3], n=[0, 1], w=10, t='rec', l='', aria='Giardia', c='giardia', ions=[])]

readouts = [
  dict(l='Anemia', mods=[dict(when=O('falc', 'vivax', 'hook'), d=1)]),
  dict(l='Diarrhea', mods=[dict(when=O('giar', 'ent', 'cryp'), d=1)]),
  dict(l='Lungs on the route', mods=[dict(when=O('hook', 'strong', 'asc'), d=1)]),
  dict(l='Liver involved', mods=[dict(when=O('vivax', 'ent', 'schm', 'falc'), d=1)]),
  dict(l='CNS involved', mods=[dict(when=O('falc', 'toxo', 'cyst'), d=1)]),
]

notes = {
  '': 'Parasites get in by a mosquito bite, by mouth (food, water, fingers) or straight through the skin (soil, fresh water). Where they '
      'travel decides the disease: through the lungs, into red cells, encysted in muscle or brain, or trapped as eggs in liver and bladder.',
  'p:falc': 'Malaria: sporozoites infect hepatocytes, then merozoites invade red cells and burst out in synchronized cycles — cyclic fever, '
            'anemia, splenomegaly. P. falciparum makes infected cells stick to capillaries of brain, kidney and lung.',
  'p:vivax': 'P. vivax and ovale: 48-hour (tertian) fevers and dormant liver hypnozoites that relapse — add primaquine.',
  'p:hook': 'Hookworm: larvae enter bare feet (cutaneous larva migrans), pass through the lungs and attach to the small bowel to feed on '
            'blood — microcytic iron-deficiency anemia.',
  'p:strong': 'Strongyloides: skin → lungs → duodenum; it can finish its cycle inside one host (autoinfection), which runs away into '
              'hyperinfection with glucocorticoids, transplant, lymphoma or HTLV-1 — often with gram-negative sepsis.',
  'p:asc': 'Ascaris: swallowed eggs hatch, larvae migrate through blood to the lungs (Löffler syndrome), are coughed up and swallowed and '
           'mature in the gut — obstruction at the ileocecal valve or biliary tree.',
  'p:pin': 'Pinworm: the female lays eggs on the perianal skin at night; scratching carries them back to the mouth — anal pruritus in '
           'children 5–10.',
  'p:giar': 'Giardia: cysts in untreated water become trophozoites on the duodenal mucosa that block fat absorption — bloating, foul '
            'fatty nonbloody diarrhea. IgA deficiency raises the risk.',
  'p:ent': 'Entamoeba histolytica: trophozoites invade the colon (flask-shaped ulcers, dysentery) and can reach the liver by the portal '
           'vein — anchovy-paste abscess.',
  'p:cryp': 'Cryptosporidium: acid-fast, chlorine-resistant oocysts in water — mild watery diarrhea, severe chronic diarrhea in AIDS.',
  'p:toxo': 'Toxoplasma: tissue cysts in undercooked meat or oocysts from cat litter; latent in brain and muscle, reactivates when CD4 falls '
            '(ring-enhancing lesions); crosses the placenta (chorioretinitis, hydrocephalus, calcifications).',
  'p:trich': 'Trichinella: larvae from undercooked pork enter the blood and encyst in striated muscle — fever, periorbital edema, myositis.',
  'p:taen': 'Taenia solium, larvae in undercooked pork: an intestinal tapeworm, usually mild.',
  'p:cyst': 'Taenia solium, eggs from a human carrier: larvae hatch and encyst throughout the body — neurocysticercosis, seizures.',
  'p:schm': 'Schistosoma mansoni/japonicum: cercariae penetrate skin in fresh water (snails are the intermediate host); adults live in '
            'venous plexuses and eggs trapped in the liver cause granulomas, periportal fibrosis and portal hypertension.',
  'p:schh': 'Schistosoma haematobium: eggs lodge in the bladder wall — hematuria, chronic inflammation, squamous metaplasia and squamous '
            'cell carcinoma.',
}

dyn = dict(
  kinds=dict(par=['par', '--dk7']), groups=[['par', 'Parasite']],
  switches=[dict(id='p', label='Parasite', type='one', options=[
    ['falc', 'P. falciparum', 'malaria'], ['vivax', 'P. vivax / ovale', 'malaria'], ['hook', 'Hookworm', 'hookworm'],
    ['strong', 'Strongyloides', 'strongyloides'], ['asc', 'Ascaris', 'ascaris'], ['pin', 'Pinworm', 'pinworm'], ['giar', 'Giardia', 'giardia'],
    ['ent', 'Entamoeba', 'entamoeba'], ['cryp', 'Cryptosporidium', 'cryptosporidium'], ['toxo', 'Toxoplasma', 'toxo'],
    ['trich', 'Trichinella', 'trichinella'], ['taen', 'Taenia — tapeworm', 'taenia'], ['cyst', 'Taenia — cysticercosis', 'taenia'],
    ['schm', 'Schistosoma mansoni', 'schisto'], ['schh', 'Schistosoma haematobium', 'schisto']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='First Aid pp. 152–157 · Robbins ch 8 · Katzung ch 52–53')

MAP = dict(
  id='parasim', title='Parasite Life Cycles in Motion', topic='id', after='fungpar',
  sub='Follow each parasite in — by mosquito, mouth or skin — along its route through lungs, gut, liver, blood, muscle, brain or bladder, '
      'with what it damages and the drug: malaria, hookworm, Strongyloides, Ascaris, pinworm, Giardia, Entamoeba, Cryptosporidium, '
      'Toxoplasma, Trichinella, Taenia and Schistosoma',
  w=3600, h=1900,
  fa='152, 154, 156, 157',
  src=['Robbins ch 8 — Infectious diseases', 'Katzung ch 52 — Antiprotozoal Drugs', 'Katzung ch 53 — Pharmacology of the Antihelminthic Drugs'],
  lanes=[('paProt', 'Protozoa', 'glycolysis'), ('paNem', 'Nematodes', 'tca'), ('paFlat', 'Tapeworms & flukes', 'gluconeo')],
  nodes=[
    ('pa1', 'Malaria', 330, 1660, 'paProt', 'liver → red cells', ['malaria'], 'hub'),
    ('pa2', 'Giardia · Cryptosporidium', 760, 1660, 'paProt', 'water, small bowel', ['giardia', 'cryptosporidium']),
    ('pa3', 'Entamoeba', 1200, 1660, 'paProt', 'colon → liver', ['entamoeba']),
    ('pa4', 'Toxoplasma', 1640, 1660, 'paProt', 'brain in AIDS', ['toxo']),
    ('pa5', 'Hookworm · Strongyloides', 2080, 1660, 'paNem', 'through the feet', ['hookworm', 'strongyloides']),
    ('pa6', 'Ascaris · pinworm', 330, 1790, 'paNem', 'lungs · perianal', ['ascaris', 'pinworm']),
    ('pa7', 'Trichinella', 760, 1790, 'paNem', 'muscle cysts', ['trichinella']),
    ('pa8', 'Taenia', 1200, 1790, 'paFlat', 'tapeworm vs cysts', ['taenia']),
    ('pa9', 'Schistosoma', 1640, 1790, 'paFlat', 'liver vs bladder', ['schisto'])],
  panels=[
    (2500, PANY, 1000, 'The way in (First Aid pp. 152–157)', [
      ('Mosquito', 'malaria'),
      ('Through the skin', 'hookworm, Strongyloides, Schistosoma'),
      ('Water', 'Giardia, Entamoeba, Cryptosporidium'),
      ('Undercooked pork', 'Trichinella, Taenia tapeworm'),
      ('Eggs (fecal-oral)', 'Ascaris, pinworm, cysticercosis')])],
  dyn=dyn)
