# m39 — dynamic maps: the shared library for the map writers (check, screenshot) and the assembler.
# A writer's module defines MAP (see SPEC_DYN.md) and may define new cards with card() and nothing else.
import json, re, sys, pathlib, importlib, math, os, shutil, subprocess
HERE = pathlib.Path(__file__).resolve().parent          # <repo>/drafts/tools
ROOT = HERE.parents[1]                                   # <repo>
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(ROOT / 'drafts' / 'maps'))
from common import CARDS, card_js, T

# the atlas as it is on this branch: check and shot insert a module into it; assemble happens on the Mac
SRC = ROOT / 'tools' / 'atlas-src.html'
REAL = SRC
KIT = HERE / 'kit.js'   # the current kit, for reference; put_kit below leaves the page's own kit alone
J = lambda x: json.dumps(x, ensure_ascii=False)

DECKS = ('Biochemistry|Biostatistics|Cardiology|Dermatology|Endocrinology|Gastroenterology|Genetics|Hematology & Oncology|'
         'Immunology|MSK|Microbiology|Nephrology|Neurology|Pathology|Pharmacology|Psychiatry|Public Health Sciences|Pulmonology|Reproduction')
BOOT = re.compile(r'^Bootcamp\.com (' + DECKS + r') — \S.*$')

def titles(S):
    ex = set(re.findall(r'"((?:OCOM [A-Za-z]+|Foundations of Osteopathic Medicine|DeGowin|Atlas of Osteopathic Techniques|Osmosis)[^"]*)"', S))
    return ({f"{v['book']} ch {v['ch']} — {v['title']}" for v in T.values()} |
            {f"{v['book']} {v['ch']} — {v['title']}" for v in T.values()} | ex)

LANE_COLORS = ('glycolysis', 'tca', 'gluconeo', 'ppp', 'glycogen', 'sugars')

# ── the kit's drawing styles (added to the atlas once, with the kit) ──
KIT_CSS = '''
/* ── dynamic-maps kit: drawing (m39) ── */
.dyn-mem{fill:none;stroke:var(--dyn-mem);stroke-linecap:round}
.dyn-mem-in{fill:none;stroke:var(--dyn-mem-in);stroke-dasharray:2 6}
.dyn-cell{fill:var(--dyn-cell);stroke:var(--dyn-cell-line);stroke-width:3}
.dyn-soft{fill:var(--surface-2);stroke:var(--line-2);stroke-width:2}
.dyn-line{fill:none;stroke:var(--ink-3);stroke-width:2.5}
.dyn-dash{fill:none;stroke:var(--ink-3);stroke-width:2.5;stroke-dasharray:7 5}
.dyn-trace{fill:none;stroke:var(--ink-2);stroke-width:3;stroke-linejoin:round;stroke-linecap:round}
.dyn-hl{fill:none;stroke:var(--accent);stroke-width:7;stroke-linecap:round;stroke-linejoin:round;opacity:.85}
.dyn-lesion{fill:none;stroke:var(--bad);stroke-width:5;stroke-linecap:round}
.dyn-lost{fill:var(--dyn-lost)}
.dyn-field{fill:var(--dyn-field);stroke:var(--ink-2);stroke-width:2}
.dyn-big{font:700 15px var(--font-ui);fill:var(--ink)}
.dyn-cap{font:italic 12px var(--font-ui);fill:var(--ink-3)}
.dyn-dim{opacity:.35}
#artWrap .nf-l1,#artWrap .nf-l2,#artWrap .dyn-cap,#artWrap .dyn-big{paint-order:stroke;stroke:var(--map-bg);stroke-width:3.5px;stroke-linejoin:round;stroke-opacity:.9}
:root{--dyn-mem:#D9C7A5;--dyn-mem-in:#F6EEDD;--dyn-cell:#FCF8F1;--dyn-cell-line:#D6CBB8;--dyn-field:#FFFFFF;--dyn-lost:#33302C}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--dyn-mem:#6E5F45;--dyn-mem-in:#3B342A;--dyn-cell:#2A2723;--dyn-cell-line:#5A5246;--dyn-field:#4A4F48;--dyn-lost:#0B0C0B}}
:root[data-theme="dark"]{--dyn-mem:#6E5F45;--dyn-mem-in:#3B342A;--dyn-cell:#2A2723;--dyn-cell-line:#5A5246;--dyn-field:#4A4F48;--dyn-lost:#0B0C0B}
'''

def put_kit(S):
    """drafts branch: the page already carries the current kit (edit it in tools/atlas-src.html); only the styles are ensured"""
    if '/* ── dynamic-maps kit: drawing (m39) ── */' not in S:
        i = S.index('</style>')
        S = S[:i] + KIT_CSS + S[i:]
    return S

# ── text sizes (px per character), as the atlas draws them ──
CW = {'nf-l1': 7.4, 'nf-l2': 6.4, 'dyn-big': 8.6, 'dyn-cap': 6.4, 'nf-h': 8.0, 'nf-nt': 7.0}
def tw(text, cls='nf-l2', size=None):
    if size: return len(text) * size * 0.56
    return len(text) * CW.get(cls, 7.0)

def text_box(x, y, text, cls='nf-l2', anchor='start', size=None):
    w = tw(text, cls, size); h = (size or (15 if cls == 'dyn-big' else 13 if cls == 'nf-l1' else 12)) + 4
    x0 = x if anchor == 'start' else x - w / 2 if anchor == 'middle' else x - w
    return (x0, y - h + 4, x0 + w, y + 4)

TXT = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
def svg_texts(svg):
    out = []
    for attrs, body in TXT.findall(svg):
        g = lambda k: (re.search(r'\b' + k + r'="([^"]*)"', attrs) or [None, None])[1]
        x, y = g('x'), g('y')
        if x is None or y is None: continue
        try: x, y = float(x), float(y)
        except ValueError: continue
        cls = (g('class') or 'nf-l2').split()[0]
        fs = g('font-size')
        body = re.sub(r'<[^>]+>', '', body)
        out.append((body, text_box(x, y, body, cls, g('text-anchor') or 'start', float(fs) if fs else None)))
    return out

def load(modname):
    """import a writer's module; returns (MAP, its new cards)"""
    before = len(CARDS)
    if modname in sys.modules: del sys.modules[modname]
    mod = importlib.import_module(modname)
    return mod.MAP, CARDS[before:], mod

# ── conditions ──
def conds_of(dyn):
    sws = {s['id']: s for s in dyn.get('switches', [])}
    def ok(c):
        if '&' in c: return all(ok(q) for q in c.split('&'))
        c = c.lstrip('!')
        a, _, b = c.partition(':')
        if a not in sws: return False
        s = sws[a]
        if not b: return s.get('type', 'toggle') == 'toggle'
        if b == '*': return s.get('type') in ('one', 'steps')
        return b in [o[0] for o in s.get('options', [])]
    return ok

def states(dyn):
    """the states worth checking: the default, each toggle flipped, each option of each group"""
    base = {}
    for s in dyn.get('switches', []):
        t = s.get('type', 'toggle')
        base[s['id']] = (s.get('def') or '') if t == 'one' else (s.get('def') or s['options'][0][0]) if t == 'steps' else (s.get('def', True) is not False)
    out = [('default', dict(base))]
    for s in dyn.get('switches', []):
        t = s.get('type', 'toggle')
        if t == 'toggle':
            st = dict(base); st[s['id']] = not st[s['id']]; out.append((f"{s['id']} flipped", st))
        else:
            for k, *_ in s['options']:
                st = dict(base); st[s['id']] = k; out.append((f"{s['id']}:{k}", st))
    return out

def has(st, c):
    if not c: return False
    if '&' in c: return all(has(st, q) for q in c.split('&'))
    if c[0] == '!': return not has(st, c[1:])
    a, sep, b = c.partition(':')
    v = st.get(a)
    if not sep: return v is True
    if b == '*': return bool(v) and v is not True
    return v == b
anyc = lambda st, l: any(has(st, c) for c in (l or []))
allc = lambda st, l: all(has(st, c) for c in (l or []))

# ── the control block's size (mirrors kitArt) ──
def ctl_layout(dyn, w_map):
    P = dyn.get('panel') or {'x': w_map - 1080, 'y': 110, 'w': 1000}
    X0, W = P['x'], P['w']; y = P['y'] + 16; x = X0
    def chip(label, dot=False):
        nonlocal x, y
        w = round(len(label) * 7.1 + (40 if dot else 26))
        if x + w > X0 + W: x = X0; y += 44
        x += w + 8
    def head():
        nonlocal x, y
        x = X0; y += 30
    if dyn.get('groups'):
        head(); [chip(l, True) for _, l in dyn['groups']]; y += 50
    tg = [s for s in dyn.get('switches', []) if s.get('type', 'toggle') == 'toggle']
    if tg:
        head(); [chip(max(s.get('on') or s['label'], s.get('off') or 'No ' + s['label'], key=len)) for s in tg]; y += 50
    for s in dyn.get('switches', []):
        if s.get('type') in ('one', 'steps'):
            head()
            for i, (_, l, *_x) in enumerate(s['options']): chip((f'{i+1} · ' if s['type'] == 'steps' and not re.match(r'(Phase|\d)', l) else '') + l)
            if s['type'] == 'steps':
                chip('Next ›')
                if s.get('auto'): chip('Stepping through')
            y += 50
    x = X0; chip('Pause the motion'); chip('Reset')
    if dyn.get('readouts'): chip('Predict the arrows')
    chip('Tour'); chip('Name it · 99/99'); chip('Side by side'); chip('Unpin'); chip('✓ Link copied')   # m42: the widest last row (a state pinned to compare)
    if dyn.get('readouts'): y += 46
    y += 34
    # the longest set of notes that can show at once: each toggle's off-note, the longest note of each group
    per = math.floor(W / 7.3)
    def nlines(t):
        lines, cur = 0, ''
        for wd in t.split(' '):
            if len((cur + ' ' + wd).strip()) > per: lines += 1; cur = wd
            else: cur += ' ' + wd
        return lines + 1
    notes = dyn.get('notes', {})
    tot = 0
    groups = {}
    for k, t in notes.items():
        if not k: continue
        g = k.lstrip('!').split('&')[0].split(':')[0]
        groups[g] = max(groups.get(g, 0), nlines(t))
    tot = sum(groups.values()) + max(0, len(groups) - 1)
    tot = max(tot, nlines(notes.get('', '')) if notes.get('') else 1)
    tot += 2   # m42: the tour's 'Tour 3 of 14 — …' line, or the pinned-state line
    bottom = y + tot * 19 + 56
    return (X0, P['y'], X0 + W, bottom)

# ── checks ──
def check(modname, S=None):
    S = S or SRC.read_text(encoding='utf-8')
    M, NEW, mod = load(modname)
    P = []   # problems
    W = []   # warnings (layout)
    TI = titles(S)
    ids = set(re.findall(r'^([a-z0-9_]+):\{n:"', S, re.M))
    ok_src = lambda s: s in TI or bool(BOOT.match(s))
    newids = {c['id'] for c in NEW}
    allids = ids | newids
    for key in ('id', 'title', 'topic', 'after', 'sub', 'w', 'h', 'fa', 'src', 'lanes', 'nodes', 'dyn'):
        if key not in M: P.append(f'MAP has no {key}')
    if P: return P, W, M, NEW
    if re.search(r'MAPS\.' + M['id'] + r'\s*=', S): P.append(f"map id {M['id']} exists")
    if not re.fullmatch(r'[a-z0-9]+', M['id']): P.append('map id: lowercase letters/digits only')
    if M['id'] in ids: P.append(f"map id {M['id']} is also a card id — #{M['id']} links would open the map, pick another")
    tseg = S[S.index('const TOPICS'):S.index(']];', S.index('const TOPICS'))]
    tm = re.search(r'\["' + M['topic'] + r'","[^"]+",\[([^\]]*)\]\]', tseg)
    if not tm: P.append(f"topic {M['topic']} unknown")
    elif M['after'] not in re.findall(r'"([a-z0-9_]+)"', tm.group(1)): P.append(f"after: {M['after']} is not in topic {M['topic']}")
    for s in M['src']:
        if not ok_src(s): P.append(f'map src not a known title: {s}')
    if not M['src'] and not M['fa']: P.append('the map lists no sources: give it fa and src')
    existing_paths = set(re.findall(r'^  ([A-Za-z0-9_]+):\{n:"[^"]*",v:"--p-', S, re.M))
    lanes = {}
    for k, n, c in M['lanes']:
        if k in existing_paths: P.append(f'lane key {k} exists already — pick another')
        if c not in LANE_COLORS: P.append(f'lane {k}: colour {c} not one of {LANE_COLORS}')
        lanes[k] = n
    # new cards
    for c in NEW:
        if c['id'] in ids: P.append(f"card {c['id']} exists")
        if not re.fullmatch(r'[a-z0-9]+', c['id']): P.append(f"card id {c['id']}")
        for s in c['src']:
            if not ok_src(s): P.append(f"card {c['id']}: src not known: {s}")
        for f in ('n', 'alias', 'enz'):
            if re.search(r'</?(b|i|em|strong)>', c[f]): P.append(f"card {c['id']}: html in {f}")
        for b in c['buzz']:
            if re.search(r'<', b): P.append(f"card {c['id']}: html in buzz")
        if c['k'] not in ('dz', 'drug', 'reg'): P.append(f"card {c['id']}: k")
        if c['p'] not in lanes and c['p'] not in existing_paths: P.append(f"card {c['id']}: p {c['p']} not a lane")
    # nodes
    pinned = set(); nids = set(); boxes = []
    for nd in M['nodes']:
        nid, lab, x, y, lane, sub, pins = nd[:7]
        if nid in nids: P.append(f'node id {nid} twice')
        nids.add(nid)
        if lane not in lanes: P.append(f'node {nid}: lane {lane} unknown')
        if not pins: P.append(f'node {nid} pins nothing')
        for cid in pins:
            if cid not in allids: P.append(f'node {nid}: card {cid} does not exist')
            pinned.add(cid)
        if len(lab) > 30: W.append(f'node {nid}: label over 30 characters')
        w = max(82, len(lab) * 7.45 + 26, len(sub) * 5.9 + 26 if sub else 0); h = 46 if sub else 34
        boxes.append((f'node {nid} “{lab}”', (x - w / 2, y - h / 2, x + w / 2 + len(pins) * 23 + 4, y + h / 2)))
    for c in NEW:
        if c['id'] not in pinned: P.append(f"new card {c['id']} is not pinned on a node")
    for i, (x, y, w, t, rows) in enumerate(M.get('panels', [])):
        kw = max(120, min(400, round(8.6 * max(len(a) for a, _ in rows) + 24)))
        need = 15 + kw + max(len(b) for _, b in rows) * 7.0 + 15
        h = 50 + 22 * len(rows)
        boxes.append((f'panel “{t[:30]}”', (x, y, x + max(w, need), y + h)))
        if need > w: W.append(f'panel “{t[:30]}” text needs ~{round(need)} px wide, you gave {w} (it will widen)')
    for (x, y, w, h, l) in M.get('comps', []):
        boxes.append((f'compartment badge “{l}”', (x + 26, y - 12, x + 166, y + 12)))
    d = M['dyn']
    ok = conds_of(d)
    def cc(where, lst):
        for c in lst or []:
            if not ok(c): P.append(f'{where}: condition {c!r} does not match a switch/option')
    kinds = d.get('kinds', {})
    groups = {g for g, _ in d.get('groups', [])}
    for k, (g, col) in kinds.items():
        if groups and g not in groups: P.append(f'kind {k}: group {g} not in groups')
        if not re.fullmatch(r'--[a-z0-9-]+', col): P.append(f'kind {k}: colour {col}')
    for s in d.get('switches', []):
        if s.get('type', 'toggle') not in ('toggle', 'one', 'steps'): P.append(f"switch {s['id']}: type")
        if ':' in s['id'] or '&' in s['id']: P.append(f"switch id {s['id']}")
        for o in s.get('options', []):
            if len(o) > 2 and o[2] not in allids: P.append(f"switch {s['id']} option {o[0]}: card {o[2]} does not exist")
    for k in d.get('notes', {}):
        if k: cc('notes key', [k])
        if len(d['notes'][k]) > 460: W.append(f'note {k!r} is long ({len(d["notes"][k])} chars) — keep notes under ~400')
    for i, s in enumerate(d.get('shapes', [])):
        if isinstance(s, dict): cc(f'shape {i}', (s.get('when') or []) + (s.get('unless') or []) + [c for md in s.get('mods', []) for c in md['when']])
    for i, f in enumerate(d.get('flows', [])):
        cc(f'flow {i}', (f.get('when') or []) + (f.get('unless') or []) + [c for md in f.get('mods', []) for c in md['when']])
        for k in list(f.get('base', {})) + [k for md in f.get('mods', []) for k in list(md.get('add', {})) + list(md.get('set', {}))]:
            if k not in kinds: P.append(f'flow {i}: kind {k} not in kinds')
        if 'len' not in f: P.append(f'flow {i}: no len (path length in px)')
    for i, s in enumerate(d.get('sites', [])):
        nm = s.get('l') or s.get('aria') or f'site {i}'
        for key in ('block', 'stop', 'low', 'boost', 'need', 'when', 'unless'): cc(f'site {nm} {key}', s.get(key))
        for k, dr, n in s.get('ions', []):
            if k not in kinds: P.append(f'site {nm}: kind {k} not in kinds')
            if dr not in ('in', 'out'): P.append(f'site {nm}: direction {dr}')
        if s.get('c') and s['c'] not in allids: P.append(f"site {nm}: card {s['c']} does not exist")
        if s.get('c') and s['c'] not in pinned: W.append(f"site {nm}: its card {s['c']} is not pinned on any node (pin it so the map lists it)")
        if s.get('t') not in ('co', 'ex', 'ch', 'aqp', 'pump', 'para', 'wall', 'md', 'rec'): P.append(f"site {nm}: icon type {s.get('t')}")
    for r in d.get('readouts', []):
        cc(f"readout {r['l']}", [c for md in r.get('mods', []) for c in md['when']])
    # bounds
    for name, (x0, y0, x1, y1) in boxes:
        if x0 < 0 or y0 < 0 or x1 > M['w'] or y1 > M['h']: P.append(f'{name} is outside the map ({M["w"]}×{M["h"]})')
    ctl = ctl_layout(d, M['w'])
    if ctl[3] > M['h']: P.append(f'the switches + notes run to y≈{round(ctl[3])}, past the map height {M["h"]}')
    # overlaps, state by state
    seen = set()
    for sname, st in states(d):
        bx = list(boxes) + [('the switches and notes', ctl)]
        for i, s in enumerate(d.get('shapes', [])):
            if isinstance(s, str): svg = s
            else:
                if s.get('when') and not anyc(st, s['when']): continue
                if s.get('unless') and anyc(st, s['unless']): continue
                if 'text' in s:
                    bx.append((f'text “{s["text"][:24]}”', text_box(s['x'], s['y'], s['text'], (s.get('cls') or 'nf-l2').split()[0], s.get('anchor') or 'start')))
                    continue
                svg = s.get('svg', '')
            for body, b in svg_texts(svg):
                bx.append((f'text “{body[:24]}”', b))
        for i, s in enumerate(d.get('sites', [])):
            if s.get('when') and not anyc(st, s['when']): continue
            if s.get('unless') and anyc(st, s['unless']): continue
            nx, ny = s.get('n', [0, 1]); h = s['w'] / 2
            wx, wy = s['x'] + nx * (h + 3), s['y'] + ny * (h + 3)
            bx.append((f'site icon {s.get("l") or i}', (wx - 15, wy - 15, wx + 15, wy + 15)))
            if not s.get('l'): continue
            blocked = anyc(st, s.get('block')); stopped = not blocked and anyc(st, s.get('stop'))
            closed = bool(s.get('need')) and not allc(st, s['need'])
            low = not (blocked or stopped or closed) and anyc(st, s.get('low')); boost = not (blocked or stopped or closed) and anyc(st, s.get('boost'))
            sx = dict(block=' — blocked', stop=' — idle', low=' — less active', boost=' — more active'); sx.update(s.get('sfx') or {})
            suf = sx['block'] if blocked else sx['stop'] if stopped else (' — ' + (s.get('closed') or 'closed')) if closed else sx['low'] if low else sx['boost'] if boost else ''
            l1, l2 = s['l'] + suf, s.get('s', '')
            if 'lx' in s:
                an = s.get('la', 'middle'); bb = [text_box(s['lx'], s['ly'], l1, 'nf-l1', an)]
                if l2: bb.append(text_box(s['lx'], s['ly'] + 16, l2, 'nf-l2', an))
            elif nx:
                lx = s['x'] + nx * (h + 46); an = 'end' if nx < 0 else 'start'
                bb = [text_box(lx, s['y'] - 3, l1, 'nf-l1', an), text_box(lx, s['y'] + 13, l2, 'nf-l2', an)]
            else:
                ly = s['y'] + ny * (h + (50 if ny > 0 else 36))
                bb = [text_box(s['x'], ly if ny > 0 else ly - 16, l1, 'nf-l1', 'middle'), text_box(s['x'], ly + 16 if ny > 0 else ly, l2, 'nf-l2', 'middle')]
            x0 = min(b[0] for b in bb); y0 = min(b[1] for b in bb); x1 = max(b[2] for b in bb); y1 = max(b[3] for b in bb)
            bx.append((f'site label “{l1[:30]}”', (x0, y0, x1, y1)))
        for i in range(len(bx)):
            for j in range(i + 1, len(bx)):
                (na, a), (nb, b) = bx[i], bx[j]
                if a[0] < b[2] - 2 and b[0] < a[2] - 2 and a[1] < b[3] - 2 and b[1] < a[3] - 2:
                    if na.startswith('site icon') and nb.startswith('site icon'): continue
                    key = (na, nb)
                    if key in seen: continue
                    seen.add(key)
                    W.append(f'overlap [{sname}]: {na} × {nb}')
        for name, (x0, y0, x1, y1) in bx:
            if x0 < 0 or y0 < 0 or x1 > M['w'] or y1 > M['h']:
                key = ('out', name)
                if key not in seen: seen.add(key); W.append(f'[{sname}] {name} runs outside the map')
    return P, W, M, NEW

# ── the map as atlas JS ──
def map_js(M):
    nodes = []
    for nd in M['nodes']:
        nid, lab, x, y, lane, sub, pins = nd[:7]; hub = len(nd) > 7 and nd[7] == 'hub'
        o = f'  {{id:"{nid}",l:{J(lab)},x:{x},y:{y},p:"{lane}"' + (',k:"hub"' if hub else '') + (f',s:{J(sub)}' if sub else '') + ',m:[' + ','.join(f'"{p}"' for p in pins) + ']}'
        nodes.append(o)
    panels = []
    for (x, y, w, t, rows) in M.get('panels', []):
        kw = max(120, min(400, round(8.6 * max(len(a) for a, _ in rows) + 24)))
        panels.append(f'  {{x:{x},y:{y},w:{w},h:{50 + 22 * len(rows)},kw:{kw},t:{J(t)},rows:[\n' + ',\n'.join(f'   [{J(a)},{J(b)}]' for a, b in rows) + ']}')
    comps = [f'  {{x:{x},y:{y},w:{w},h:{h},l:{J(l)}}}' for (x, y, w, h, l) in M.get('comps', [])]
    return (f'MAPS.{M["id"]} = {{\n t:{J(M["title"])}, sub:{J(M["sub"])},\n w:{M["w"]}, h:{M["h"]},\n fa:{J(M["fa"])},\n src:{J(M["src"])},\n art:"kit",\n dyn:{J(M["dyn"])},\n'
            f' comps:[\n' + ',\n'.join(comps) + '],\n panels:[\n' + ',\n'.join(panels) + '],\n nodes:[\n' + ',\n'.join(nodes) + '],\n edges:[]\n};')

def insert(S, mods, date='2026-10-09'):
    """put the kit and every module's map, lanes and cards into atlas source S"""
    S = put_kit(S)
    def rep(a, b):
        nonlocal S
        assert S.count(a) == 1, (S.count(a), a[:80])
        S = S.replace(a, b)
    loaded = [load(m) for m in mods]
    cards = [c for _, NEW, _ in loaded for c in NEW]
    if cards:
        rep('/* ── seizures, anticonvulsants & headache (m14)', '/* ── cards for the dynamic maps (m39) ─── */\n' + '\n\n'.join(card_js(c) for c in cards) + '\n\n/* ── seizures, anticonvulsants & headache (m14)')
    lanes = [l for M, _, _ in loaded for l in M['lanes']]
    rep('  neutral:{n:"Transport / shuttle",v:"--p-etc"}', ''.join(f'  {k}:{{n:{J(n)},v:"--p-{v}"}},\n' for k, n, v in lanes) + '  neutral:{n:"Transport / shuttle",v:"--p-etc"}')
    S = S.replace('const VIEWS = [', '\n\n'.join(map_js(M) for M, _, _ in loaded) + '\n\n' + 'const VIEWS = [', 1)
    rep(',["index","Index"]]', ',' + ','.join(f'[{J(M["id"])},{J(M["title"])}]' for M, _, _ in loaded) + ',["index","Index"]]')
    for M, _, _ in loaded:
        i = S.index('const TOPICS'); j = S.index(']];', i); seg = S[i:j]
        m = re.search(r'\["' + M['topic'] + r'","[^"]+",\[([^\]]*)\]\]', seg)
        lst = re.findall(r'"([a-z0-9_]+)"', m.group(1))
        at = lst.index(M['after']) + 1
        while at < len(lst) and lst[at] in [x[0]['id'] for x in loaded]: at += 1   # several new maps after one map: keep their order
        lst.insert(at, M['id'])
        seg = seg[:m.start(1)] + ','.join(f'"{x}"' for x in lst) + seg[m.end(1):]
        S = S[:i] + seg + S[j:]
    i = S.index('const NEW_MAPS={'); j = S.index('};', i)
    S = S[:j] + ',\n  ' + ','.join(f'{M["id"]}:"{date}"' for M, _, _ in loaded) + S[j:]
    return S, loaded

# ── screenshots, for writers: a scratch copy of the site with this map in it ──
HOOK = '''<script>/* m39 screenshot hook — scratch copies only */
(function(){ const q=new URLSearchParams(location.search);
 const ready=f=>{ const m=MAPS[state.view]; if(m&&m.dyn&&m.dyn.lazy) return setTimeout(()=>ready(f),100); setTimeout(f,300); };   // wait for a lazy drawing
 window.addEventListener("load",()=>ready(()=>{ try{
  if(q.get("dark")) document.documentElement.setAttribute("data-theme","dark");
  (q.get("dyn")||"").split(",").filter(Boolean).forEach(k=>dynSet(k));
  if(q.get("still")){ const s=dynSt(state.view); s.paused=true; s.auto=null; dynMotion(); const w=svg.querySelector("#artWrap"); if(w) w.innerHTML=kitArt(MAPS[state.view]); }
  const lk=q.get("look"); if(lk){ const [x0,y0,x1,y1]=lk.split(",").map(Number), m=MAPS[state.view], r=svg.getBoundingClientRect(), s0=Math.min(r.width/m.w,r.height/m.h), z=Math.min(r.width/(s0*(x1-x0)),r.height/(s0*(y1-y0)));
   state.z=z; state.tx=-(r.width-s0*m.w)/(2*s0)-z*x0; state.ty=-(r.height-s0*m.h)/(2*s0)-z*y0; applyCam(); }
 }catch(e){ document.body.insertAdjacentHTML("afterbegin","<pre style='color:red;font-size:30px'>"+e+"</pre>"); } })); })();
</script>'''
CHROME = next((c for c in ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chromium-browser'), shutil.which('chrome')] if c and os.path.exists(c)), None)
SCRATCH = ROOT / 'drafts' / '.scratch'   # git-ignored

def site_for(modname, theme=None):
    site = SCRATCH / modname
    if not site.exists():
        site.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(['rsync', '-a', '--exclude', '.git', '--exclude', 'drafts', str(ROOT) + '/', str(site) + '/'], check=True)
    S = SRC.read_text(encoding='utf-8')
    S, loaded = insert(S, [modname])
    S = S.rstrip() + '\n' + HOOK + '\n'
    if theme == 'dark': S = S.replace('<html', '<html data-theme="dark"', 1)
    (site / 'tools' / 'atlas-src.html').write_text(S, encoding='utf-8')
    r = subprocess.run([sys.executable, '-I', str(site / 'tools' / 'build-atlas.py')], capture_output=True, text=True)
    if r.returncode: raise SystemExit('build failed:\n' + r.stdout[-3000:] + r.stderr[-3000:])
    return site, loaded[0][0]

def shoot(site, mid, out, dyn='', look='', still=True, size=(2400, 1500), dark=False):
    q = ['dark=1'] if dark else []
    if dyn: q.append('dyn=' + dyn)
    if look: q.append('look=' + look)
    if still: q.append('still=1')
    url = (site / 'resources' / 'metabolic-atlas.html').as_uri() + ('?' + '&'.join(q) if q else '') + '#' + mid
    r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run', '--no-default-browser-check',
                        f'--user-data-dir={SCRATCH}/chrome-{mid}', f'--window-size={size[0]},{size[1]}', '--virtual-time-budget=6000',
                        f'--screenshot={out}', url], capture_output=True, text=True, timeout=90)
    return out
