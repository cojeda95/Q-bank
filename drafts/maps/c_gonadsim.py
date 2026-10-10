# Gonadal Tumors by Cell of Origin in Motion (dynamic map, kit data) — drafted on the drafts branch, off the Mac.
# An ovary and a testis side by side, each split into the cells tumors come from — surface epithelium (ovary only), germ
# cells, sex cord (granulosa/theca · Sertoli/Leydig) and stroma — with a blood-marker strip and target organs (endometrium,
# breast, skin and hair, pleura and peritoneum). A `dx` switch grows one tumor in its compartment and sends its marker or
# hormone where the card says: serous and mucinous carcinoma (CA 125, pseudomyxoma), mature teratoma (struma ovarii),
# dysgerminoma (hCG, LDH), yolk sac (AFP), granulosa cell (estrogen, inhibin), fibroma (Meigs), Sertoli-Leydig (androgens),
# seminoma, choriocarcinoma (hCG), Leydig cell tumor. Layout schematic. 5 readouts. Facts from the pinned cards; FA pages in
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

D = lambda *k: [f'dx:{x}' for x in k]
PANY = 1180
OV, TE = (620, 700), (1240, 700)
COMP = dict(epi=(OV[0], OV[1] - 210, 'surface epithelium', '--dk4'), ogerm=(OV[0] - 140, OV[1] + 40, 'germ cells', '--dk9'),
            ocord=(OV[0] + 120, OV[1] + 60, 'sex cord · stroma', '--dk10'),
            tgerm=(TE[0] - 90, TE[1] - 40, 'germ cells', '--dk9'), tcord=(TE[0] + 100, TE[1] + 90, 'Sertoli · Leydig', '--dk10'))
WHERE = dict(serous='epi', mucinous='epi', teratoma='ogerm', dysg='ogerm', yolk='ogerm', gran='ocord', fibroma='ocord', sl='ocord',
             semi='tgerm', chorio='tgerm', leydig='tcord')
MK = dict(ca125=(1700, 380, 'CA 125'), hcg=(1700, 500, 'hCG'), afp=(1700, 620, 'AFP'), ldh=(1700, 740, 'LDH'), inh=(1700, 860, 'inhibin'),
          estro=(2050, 380, 'estrogen'), andro=(2050, 500, 'androgens'), plap=(2050, 620, 'PLAP'))
TG = dict(endo=(2050, 800, 'endometrium'), breast=(2050, 940, 'breast'), skin=(2050, 1080, 'skin · hair'), pleura=(1700, 1080, 'pleura · peritoneum'),
          thy=(1700, 1220, 'thyroid hormone'))
SENDS = dict(serous=('ca125', 'pleura'), mucinous=('pleura',), teratoma=('thy',), dysg=('hcg', 'ldh'), yolk=('afp',), gran=('estro', 'inh', 'endo', 'breast'),
             fibroma=('pleura',), sl=('andro', 'skin'), semi=('plap',), chorio=('hcg',), leydig=('andro', 'estro', 'breast'))

text('Gonadal tumors — which cell they come from, and what they send out', 180, 150, 'dyn-big')
text('ovary left, testis right · markers and hormones in the middle · targets on the right · schematic', 180, 176, 'dyn-cap')

add(f'<ellipse cx="{OV[0]}" cy="{OV[1]}" rx="300" ry="260" style="fill:var(--dk10);fill-opacity:.06;stroke:var(--dk10);stroke-width:4"/>'); text('ovary', OV[0], OV[1] - 290, 'nf-l1', 'middle')
add(f'<ellipse cx="{OV[0]}" cy="{OV[1]}" rx="300" ry="260" style="fill:none;stroke:var(--dk4);stroke-width:14;stroke-opacity:.4"/>')
add(f'<ellipse cx="{TE[0]}" cy="{TE[1]}" rx="220" ry="270" style="fill:var(--dk9);fill-opacity:.06;stroke:var(--dk9);stroke-width:4"/>'); text('testis', TE[0], TE[1] - 300, 'nf-l1', 'middle')
for k, (x, y, l, c) in COMP.items():
    add(f'<circle cx="{x}" cy="{y}" r="44" style="fill:var({c});fill-opacity:.25;stroke:var({c});stroke-width:3"/>'); text(l, x, y + 74, 'nf-l2', 'middle')
for d, k in WHERE.items():
    x, y, _, _ = COMP[k]
    add(f'<circle cx="{x}" cy="{y}" r="90" style="fill:var(--bad);fill-opacity:.3;stroke:var(--bad);stroke-width:5"/>', when=D(d))
for k, (x, y, l) in {**MK, **TG}.items():
    add(f'<rect x="{x - 40}" y="{y - 30}" width="80" height="60" rx="16" style="fill:var(--dk3);fill-opacity:.1;stroke:var(--dk3);stroke-width:3"/>')
    text(l, x + 56, y + 6, 'nf-l1')
for d, ks in SENDS.items():
    for k in ks:
        x, y, _ = {**MK, **TG}[k]
        add(f'<rect x="{x - 40}" y="{y - 30}" width="80" height="60" rx="16" style="fill:var(--bad);fill-opacity:.35"/>', when=D(d))
text('blood markers', 1700, 320, 'nf-l1', 'middle'); text('hormones · targets', 2050, 320, 'nf-l1', 'middle')
TAG = dict(serous='serous carcinoma — tube-like epithelium, often bilateral, psammoma bodies · most common malignant; CA 125 for monitoring',
           mucinous='mucinous — large, multiloculated; carcinoma rare, may be GI metastasis → pseudomyxoma peritonei',
           teratoma='mature cystic teratoma (dermoid) — teeth, hair, sebum; torsion; struma ovarii → hyperthyroidism',
           dysg='dysgerminoma — the ovary’s seminoma: fried-egg cells · hCG, LDH', yolk='yolk sac tumor — Schiller-Duval bodies · AFP',
           gran='granulosa cell — estrogen: postmenopausal bleeding, endometrial hyperplasia · Call-Exner bodies, inhibin',
           fibroma='fibroma — Meigs: fibroma + ascites + pleural effusion', sl='Sertoli-Leydig — androgens: hirsutism, virilization',
           semi='seminoma — fried-egg cells, PLAP, radiosensitive', chorio='choriocarcinoma — hCG → gynecomastia, hyperthyroid symptoms; to lung and brain',
           leydig='Leydig cell tumor — Reinke crystals; androgens or estrogens: precocious puberty, gynecomastia')
for k, s in TAG.items(): text(s, 1150, 1480, 'nf-l1 dyn-tag', 'middle', when=D(k))

flows = []
for d, ks in SENDS.items():
    x0, y0, _, _ = COMP[WHERE[d]]
    for k in ks:
        x1, y1, _ = {**MK, **TG}[k]
        flows.append(dict(d=f'M{x0} {y0} C{(x0 + x1) / 2:.0f} {y0} {(x0 + x1) / 2:.0f} {y1} {x1 - 40} {y1}', len=1100, speed=140, r=9,
                          base=dict(sig=3), when=D(d)))
flows.append(dict(d=f'M{OV[0] - 280} {OV[1] - 100} C{OV[0] - 200} {OV[1] - 260} {OV[0] + 200} {OV[1] - 260} {OV[0] + 280} {OV[1] - 100}',
                  len=700, speed=50, r=7, base=dict(cell=3), when=D('serous', 'mucinous')))
sites = [dict(x=OV[0] + 80, y=OV[1] - 260, n=[1, -1], w=10, t='rec', l='', aria='Epithelial ovarian tumors', c='ovepi', ions=[]),
         dict(x=OV[0] - 220, y=OV[1] + 120, n=[-1, 1], w=10, t='rec', l='', aria='Ovarian germ cell tumors', c='ovgerm', ions=[]),
         dict(x=OV[0] + 220, y=OV[1] + 150, n=[1, 1], w=10, t='rec', l='', aria='Ovarian sex cord-stromal tumors', c='ovstromal', ions=[]),
         dict(x=TE[0] - 160, y=TE[1] - 130, n=[-1, -1], w=10, t='rec', l='', aria='Testicular germ cell tumors', c='testisgct', ions=[]),
         dict(x=TE[0] + 170, y=TE[1] + 190, n=[1, 1], w=10, t='rec', l='', aria='Leydig and Sertoli tumors', c='testisstromal', ions=[])]

readouts = [
  dict(l='hCG', mods=[dict(when=D('dysg', 'chorio'), d=1)]),
  dict(l='AFP', mods=[dict(when=D('yolk'), d=1)]),
  dict(l='Estrogen', mods=[dict(when=D('gran'), d=1)]),
  dict(l='Androgens', mods=[dict(when=D('sl'), d=1)]),
  dict(l='Fluid in pleura · peritoneum', mods=[dict(when=D('fibroma', 'mucinous', 'serous'), d=1)]),
]

notes = {
  '': 'Tumors of the ovary and testis come from the surface epithelium (ovary), the germ cells, or the sex cord–stroma — and the '
      'cell of origin predicts the marker or hormone. Pick one.',
  'dx:serous': 'Serous: fallopian tube-like epithelium, often bilateral; serous carcinoma is the most common malignant ovarian tumor, '
               'with psammoma bodies. BRCA1/2, Lynch; CA 125 monitors therapy, not screening. Surgery, chemotherapy, PARP inhibitors.',
  'dx:mucinous': 'Mucinous: large, multiloculated; carcinoma is rare and may be metastatic from the appendix or GI tract → '
                 'pseudomyxoma peritonei.',
  'dx:teratoma': 'Mature cystic teratoma (dermoid): commonest ovarian tumor in young women — all three germ layers (teeth, hair, '
                 'sebum); torsion; struma ovarii → hyperthyroidism. Immature teratoma (neural tissue) is malignant.',
  'dx:dysg': 'Dysgerminoma: the ovarian seminoma — adolescents, sheets of fried-egg cells; hCG and LDH.',
  'dx:yolk': 'Yolk sac tumor: children and young women; yellow, friable, Schiller-Duval bodies; AFP.',
  'dx:gran': 'Granulosa cell tumor: the commonest malignant sex cord-stromal tumor, women in their 50s; estrogen → postmenopausal '
             'bleeding, endometrial hyperplasia, precocious puberty; Call-Exner bodies; inhibin.',
  'dx:fibroma': 'Fibroma: spindle fibroblasts; Meigs syndrome = fibroma + ascites + pleural effusion.',
  'dx:sl': 'Sertoli-Leydig cell tumor: androgens → hirsutism, virilization.',
  'dx:semi': 'Seminoma: commonest testicular germ cell tumor — painless, homogeneous; fried-egg cells; PLAP; radiosensitive.',
  'dx:chorio': 'Choriocarcinoma: syncytio- and cytotrophoblast; hCG → gynecomastia, hyperthyroid symptoms; spreads by blood to lung, brain.',
  'dx:leydig': 'Leydig cell tumor: golden-brown, Reinke crystals; androgens or estrogens → precocious puberty, gynecomastia. Over 60, '
               'the commonest testicular cancer is lymphoma.',
}

dyn = dict(
  kinds=dict(sig=['mov', '--bad'], cell=['mov', '--dk4']), groups=[['mov', 'Markers & hormones']],
  switches=[dict(id='dx', label='Tumor', type='one', options=[
              ['serous', 'Serous (ovary)', 'ovepi'], ['mucinous', 'Mucinous (ovary)', 'ovepi'], ['teratoma', 'Mature teratoma', 'ovgerm'],
              ['dysg', 'Dysgerminoma', 'ovgerm'], ['yolk', 'Yolk sac tumor', 'ovgerm'], ['gran', 'Granulosa cell', 'ovstromal'],
              ['fibroma', 'Fibroma (Meigs)', 'ovstromal'], ['sl', 'Sertoli-Leydig', 'ovstromal'], ['semi', 'Seminoma', 'testisgct'],
              ['chorio', 'Choriocarcinoma', 'testisgct'], ['leydig', 'Leydig cell tumor', 'testisstromal']])],
  notes=notes, shapes=shapes, flows=flows, sites=sites, readouts=readouts,
  panel=dict(x=2500, y=110, w=1000),
  src='Robbins ch 22')

MAP = dict(
  id='gonadsim', title='Gonadal Tumors in Motion', topic='devrepro', after='malerepro',
  sub='Grow an ovarian or testicular tumor in the cell it comes from — epithelium, germ cell or sex cord-stroma — and follow its '
      'marker or hormone: CA 125, hCG, AFP, LDH, inhibin, estrogen, androgens',
  w=3600, h=1900,
  fa='664, 665, 670, 671',
  src=['Robbins ch 22 — The female genital tract', 'Robbins ch 21 — The lower urinary tract and male genital system'],
  lanes=[('gnOv', 'Ovary', 'tca'), ('gnTe', 'Testis', 'glycolysis')],
  nodes=[
    ('gn1', 'Epithelial ovarian tumors', 330, 1720, 'gnOv', 'serous · CA 125', ['ovepi'], 'hub'),
    ('gn2', 'Ovarian germ cell tumors', 760, 1720, 'gnOv', 'teratoma · AFP · hCG', ['ovgerm']),
    ('gn3', 'Ovarian sex cord-stromal', 1200, 1720, 'gnOv', 'estrogen · Meigs', ['ovstromal']),
    ('gn4', 'Testicular germ cell tumors', 1640, 1720, 'gnTe', 'PLAP · AFP · hCG', ['testisgct']),
    ('gn5', 'Leydig & Sertoli tumors', 2080, 1720, 'gnTe', 'Reinke crystals', ['testisstromal'])],
  panels=[
    (2500, PANY, 1000, 'Marker → tumor (Robbins ch 22)', [
      ('CA 125', 'epithelial (monitor)'), ('AFP', 'yolk sac'), ('hCG', 'choriocarcinoma, dysgerminoma'), ('LDH', 'dysgerminoma'),
      ('Inhibin', 'granulosa cell'), ('PLAP', 'seminoma')])],
  dyn=dyn)
