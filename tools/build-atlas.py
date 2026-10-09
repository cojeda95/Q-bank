#!/usr/bin/env python3
"""Wrap the standalone Lesion Atlas in the OCOM Question Hub shell.

The standalone atlas lives in the repo at tools/atlas-src.html — edit that,
never the built page. This adds the site head (meta/og/mobile reset), the blue
"All Blocks" topbar and the accent overrides that make it match the hub. Run it
after every atlas edit:

    python3 tools/build-atlas.py                      # builds tools/atlas-src.html
    python3 tools/build-atlas.py --accept-homes       # after deliberately moving a card's home

Counts in the meta and og tags are derived from the artifact, so they never
drift from what the page actually contains. It also writes
resources/atlas-terms.js, which the question bank uses to link each answered
question to the matching atlas card, and resources/atlas-practice.js, which
counts those questions per card and block for the cards' Practice buttons —
re-run it after syncing new questions so the counts stay current.
"""
import hashlib, json, re, shutil, subprocess, sys, tempfile, pathlib

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
ACCEPT_HOMES = "--accept-homes" in sys.argv
src = pathlib.Path(args[0]) if args else TOOLS / "atlas-src.html"
out = ROOT / "resources" / "metabolic-atlas.html"
TERMS_OUT = ROOT / "resources" / "atlas-terms.js"
PRACTICE_OUT = ROOT / "resources" / "atlas-practice.js"
QLINKS_OUT = ROOT / "resources" / "atlas-qlinks.js"
COUNTS_OUT = ROOT / "resources" / "qbank-counts.js"
HOME_OUT = ROOT / "resources" / "atlas-home.js"
CARDS_OUT = ROOT / "resources" / "atlas-cards.js"
HOMES = TOOLS / "atlas-homes.json"
art = src.read_text(encoding="utf-8")

# ── validation ────────────────────────────────────────────────────────────
# Two failure modes have shipped before. Both are silent at runtime, so the
# build refuses rather than warns.

ESCAPED_TAG = re.compile(r"</?(?:b|i|em|strong)>")
KNOWN_SRC = re.compile(r"(Robbins|Katzung|Guyton|Costanzo|Kaplan & Sadock|Marks|Langman|Moore|Pawlina|"
                       r"Fundamental Neuroscience|Foundations of Osteopathic Medicine|Atlas of Osteopathic Techniques|"
                       r"Somatic Dysfunction in Osteopathic Family Medicine|An Osteopathic Approach to Diagnosis and Treatment|DeGowin|"
                       r"OCOM OMM|OCOM Ortho|OCOM Psych|OCOM Rheum|OCOM Nephro|Osmosis|Bootcamp\.com) ")

def dyn_maps(text):
    """[(map id, its m.dyn data)] for every drawn, moving map (art:"kit") — the data is JSON on the map's dyn: line"""
    return [(m, d) for m, d, _, _ in dyn_spans(text)]

def dyn_spans(text):
    """like dyn_maps, with where each map's dyn JSON starts and ends in text"""
    dec = json.JSONDecoder(); out = []
    heads = list(re.finditer(r"^MAPS\.([a-z0-9_]+) = \{", text, re.M))
    for i, mm in enumerate(heads):
        stop = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        k = text.find("\n dyn:", mm.end(), stop)
        if k < 0:
            continue
        data, end = dec.raw_decode(text, k + len("\n dyn:"))
        out.append((mm.group(1), data, k + len("\n dyn:"), end))
    return out

def validate(art):
    """Return a list of problems that should block the build."""
    problems = []
    lines = art.split("\n")

    # 1. n / alias / enz / inh / gen / buzz are passed through esc() at render time,
    #    so any inline markup in them prints as literal "<b>" to the reader.
    #    mech / find / labs / tx ARE rendered as HTML and keep their emphasis.
    card = None
    for ln in lines:
        m = re.match(r"^([a-z0-9_]+):\{n:\"", ln)
        mp = re.match(r"^MAPS\.([a-z0-9_]+) = \{", ln)
        if mp:
            card = f"MAPS.{mp.group(1)}"   # maps carry src lines too
        elif m:
            card = m.group(1)
            if ESCAPED_TAG.search(ln):
                problems.append(
                    f"{card}: markup in an escaped header field "
                    f"(n/alias/enz/inh/gen) — it will print as literal tags")
        elif ln.lstrip().startswith("buzz:[") and ESCAPED_TAG.search(ln):
            problems.append(
                f"{card}: markup in buzz — buzz is escaped, so tags show "
                f"literally in the side rail")
        elif ln.lstrip().startswith("src:["):
            if ESCAPED_TAG.search(ln):
                problems.append(f"{card}: markup in src — sources are escaped")
            for entry in re.findall(r'"((?:[^"\\]|\\.)*)"', ln):
                if not KNOWN_SRC.match(entry):
                    problems.append(f"{card}: unknown source {entry[:60]!r} — "
                                    f"src entries must name a known textbook or course source")
        elif ln.lstrip().startswith("ref:["):
            if ESCAPED_TAG.search(ln):
                problems.append(f"{card}: markup in ref — references are escaped")
            for pm, doi in re.findall(r'pmid:"([^"]*)",doi:"([^"]*)"', ln):
                if not re.fullmatch(r"\d{6,9}", pm) or not doi.startswith("10."):
                    problems.append(f"{card}: malformed reference (pmid {pm!r}, doi {doi!r})")

    # 2. A lesion card is invisible unless some node or edge pins it, and a
    #    pin naming a card that does not exist is a dead click.
    cards = set(re.findall(r"^([a-z0-9_]+):\{n:\"", art, re.M))
    pinned = set()
    for arr in re.findall(r'm:\[([^\]]*)\]', art):
        pinned.update(re.findall(r'"([a-z0-9_]+)"', arr))
    for k in sorted(cards - pinned):
        problems.append(f"{k}: card is defined but pinned to no map — "
                        f"it will only appear in the Index")
    for k in sorted(pinned - cards):
        problems.append(f"{k}: pinned by a map but no such card exists")

    # 3. A JavaScript object literal keeps the LAST of two identical keys and
    #    says nothing, so a pasted-in duplicate silently replaces the original.
    def dupes(keys, what):
        seen = set()
        for k in keys:
            if k in seen:
                problems.append(f"{k}: {what} is defined twice — the later one silently wins")
            seen.add(k)
    # 4. A moving map's switch option may name the card it is about ([key, label, card]) — search and
    #    "See it move" follow it, so it must exist.
    for mid, d in dyn_maps(art):
        for sw in d.get("switches", []):
            for o in sw.get("options", []):
                if len(o) > 2 and o[2] and o[2] not in cards:
                    problems.append(f"MAPS.{mid}: switch {sw.get('id')} option {o[0]} names card {o[2]!r}, which does not exist")
    dupes(re.findall(r"^([a-z0-9_]+):\{n:\"", art, re.M), "card")
    dupes(re.findall(r"^MAPS\.([a-z0-9_]+) = \{", art, re.M), "map")
    paths_block = art[art.index("const PATHS = {"):art.index("\n};", art.index("const PATHS = {"))]
    dupes(re.findall(r"^\s+([a-z0-9_]+):\{n:", paths_block, re.M), "pathway")

    return problems


# ── deep check ────────────────────────────────────────────────────────────
# The regexes above cannot see inside the data. tools/atlas-check.js evaluates
# the real PATHS / LES / MAPS / VIEWS objects under JavaScriptCore (macOS ships
# it; this Mac has no Node) and checks the wiring: every edge ends on a real
# node, every pathway has a colour, ghost nodes point at real maps, card HTML
# is balanced, nothing sits off the canvas. See that file for the full list.

JSC_PATHS = ["/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc",
             "/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc"]

def deep_check(art):
    jsc = shutil.which("jsc") or next((p for p in JSC_PATHS if pathlib.Path(p).exists()), None)
    if not jsc:
        print("  ! deep check skipped — JavaScriptCore (jsc) not found", file=sys.stderr)
        return [], [], None
    start = art.index("<script>") + len("<script>")
    end = art.index("/* \u2550", art.index("const VIEWS"))   # the ENGINE banner after VIEWS
    code = art[start:end] + "\n" + (TOOLS / "atlas-check.js").read_text(encoding="utf-8")
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(code)
    try:
        r = subprocess.run([jsc, f.name], capture_output=True, text=True, timeout=120)
    finally:
        pathlib.Path(f.name).unlink(missing_ok=True)
    lines = [l for l in r.stdout.strip().splitlines() if l.startswith("{")]
    if r.returncode or not lines:
        return [f"deep check crashed — the atlas data does not evaluate: {(r.stderr or r.stdout).strip()[:400]}"], [], None
    res = json.loads(lines[-1])
    return res["errors"], res["warnings"], res["cards"]


problems = validate(art)
deep_errors, deep_warnings, card_info = ([], [], None) if problems else deep_check(art)
problems += deep_errors

# ── first homes ───────────────────────────────────────────────────────────
# A card pinned on several maps opens on its FIRST home (the earliest map in
# MAPS definition order) from the Index and from #card links — including the
# links the question bank makes. Defining a new map anywhere but last quietly
# moves cards; this snapshot turns that into a refusal.
homes_now = {c["id"]: c["home"] for c in card_info} if card_info else None
if homes_now is not None and HOMES.exists():
    homes_then = json.loads(HOMES.read_text(encoding="utf-8"))
    moved = sorted(k for k in homes_then if k in homes_now and homes_now[k] != homes_then[k])
    if moved and not ACCEPT_HOMES:
        for k in moved:
            problems.append(f"{k}: first home moved {homes_then[k]} → {homes_now[k]} — define new maps "
                            f"LAST (just before const VIEWS); if the move is intended, rebuild with --accept-homes")

for w in deep_warnings:
    print(f"  ! {w}", file=sys.stderr)
if problems:
    print(f"\n  BUILD REFUSED — {len(problems)} problem(s):\n", file=sys.stderr)
    for pr in problems:
        print(f"    • {pr}", file=sys.stderr)
    print("", file=sys.stderr)
    sys.exit(1)


# derive the counts from the artifact itself
maps  = len(re.findall(r"^MAPS\.", art, re.M))
cards = len(re.findall(r'^[a-z0-9_]+:\{n:"', art, re.M))

# the artifact contributes everything from its font <link> to the end of its script
body_start = art.index('<link rel="preconnect"')
artifact = art[body_start:].rstrip()
assert artifact.endswith("</script>"), "artifact should end at </script>"

# split the artifact's own <style> so we can append the hub overrides inside it
last_style_close = artifact.rindex("</style>")

OCOM_CSS = """
/* ── OCOM Question Hub integration ─────────────────── */
:root{--accent:#1f4e79;--accent-soft:#E3ECF5}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--accent:#7FB3DE;--accent-soft:#16293A}}
:root[data-theme="dark"]{--accent:#7FB3DE;--accent-soft:#16293A}
body{display:flex;flex-direction:column}
.app{flex:1;min-height:0;height:auto}
.hdr{padding-top:12px}
/* the hub's own header, as on every page of the hub: brand on the left, the main links on the right */
.ocom-topbar{background:var(--bg);color:var(--ink);padding:10px 20px;flex:none;border-bottom:1px solid var(--line-2);
  padding-top:calc(10px + env(safe-area-inset-top,0px))}
.ocom-topbar-inner{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:6px 18px;
  font-family:"IBM Plex Sans",system-ui,sans-serif}
.ocom-brand{font-family:"IBM Plex Serif",Georgia,serif;font-weight:600;font-size:18px;color:var(--ink);text-decoration:none}
.ocom-nav{display:flex;flex-wrap:wrap;gap:2px 18px;font-size:14.5px;font-weight:500}
.ocom-nav a{color:var(--ink);text-decoration:none;padding:4px 0}
.ocom-nav a:hover{color:var(--accent);text-decoration:underline;text-underline-offset:5px}
.ocom-nav a[aria-current="page"]{color:var(--accent);font-weight:600}
@media (max-width:640px){.ocom-topbar{padding:8px 14px}.ocom-nav{flex:1 1 100%;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;gap:16px;font-size:13.5px}
  .ocom-nav::-webkit-scrollbar{display:none}.ocom-nav a{white-space:nowrap}}
/* the header row: the open map's name, then search and the buttons; the systems and the maps below it */
.hdr .brand h1{max-width:min(46vw,560px);overflow:hidden;text-overflow:ellipsis}
.hdr .topics{order:3;flex-basis:100%}
/* the map tabs: the open map in the atlas's teal */
.subtabs .tab[aria-selected="true"]{background:var(--p-ppp);color:#fff;border-color:transparent}
"""

head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Interactive pathway and physiology atlas for COMLEX Level 1 and USMLE Step 1 — {maps} pan/zoom maps with {cards} diseases, drug targets and toxicities pinned to the exact step they break.">
<meta name="color-scheme" content="light dark">
<meta property="og:title" content="Lesion Atlas">
<meta property="og:description" content="{maps} interactive maps. {cards} lesions pinned to the step they break.">
<meta property="og:type" content="website">
<style>
:root{{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;font:14px/1.5 system-ui,-apple-system,sans-serif;background:#EFEFEB}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
<title>Lesion Atlas — COMLEX 1 / Step 1</title>
<script src="atlas-practice.js"></script>
<script src="atlas-qlinks.js" defer></script>
"""

TOPBAR = ('<header class="ocom-topbar"><div class="ocom-topbar-inner">'
          '<a class="ocom-brand" href="../index.html">OCOM Question Hub</a>'
          '<nav class="ocom-nav" aria-label="Main">'
          '<a href="metabolic-atlas.html" aria-current="page">Lesion Atlas</a>'
          '<a href="../index.html#blocks">Blocks</a>'
          '<a href="../live.html">Live Session</a>'
          '<a href="../index.html#sync">Sync</a>'
          '<a href="../index.html#offline">Offline</a>'
          '</nav></div></header>\n')

styled = artifact[:last_style_close] + OCOM_CSS + artifact[last_style_close:]
# the artifact's markup starts right after its stylesheet block
marker = '<div class="app">'
i = styled.index(marker)
built = head + styled[:i] + "\n</head>\n<body>\n" + TOPBAR + styled[i:] + "\n</body>\n</html>\n"

# ── moving maps: each drawing goes to resources/dyn/<map>.js and loads when its map opens (the kit's dynLoad);
#    the page keeps {lazy: content hash, switches, panel} so search, links and the switch state work before it arrives
DYN_DIR = ROOT / "resources" / "dyn"
DYN_DIR.mkdir(exist_ok=True)
parts, pos, keep, moved = [], 0, set(), 0
for mid, data, a, b in (dyn_spans(built) if "function dynLoad(" in built else []):   # only a kit that can load them
    body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    h = hashlib.sha1(body.encode("utf-8")).hexdigest()[:10]
    (DYN_DIR / f"{mid}.js").write_text(f"/* Built by tools/build-atlas.py — do not edit. The drawing of MAPS.{mid} (Lesion Atlas). */\n"
                                       f"(window.DYNDATA=window.DYNDATA||{{}})[{json.dumps(mid)}]={body};\n", encoding="utf-8")
    stub = {"lazy": h, "switches": data.get("switches", []), "panel": data.get("panel")}
    parts += [built[pos:a], json.dumps(stub, ensure_ascii=False, separators=(",", ":"))]; pos = b
    keep.add(f"{mid}.js"); moved += b - a
parts.append(built[pos:]); built = "".join(parts)
for f in DYN_DIR.glob("*.js"):
    if f.name not in keep:
        f.unlink()
if not keep:
    DYN_DIR.rmdir() if not any(DYN_DIR.iterdir()) else None
out.write_text(built, encoding="utf-8")
print(f"built {out.relative_to(out.parents[1])}  —  {maps} maps, {cards} cards, {len(built):,} bytes")
print(f"built resources/dyn/  —  {len(keep)} moving-map drawings, {moved:,} bytes moved out of the page")

if homes_now is not None:
    snap = json.dumps(dict(sorted(homes_now.items())), indent=0, ensure_ascii=False) + "\n"
    if not HOMES.exists() or HOMES.read_text(encoding="utf-8") != snap:
        HOMES.write_text(snap, encoding="utf-8")
        print(f"updated {HOMES.relative_to(ROOT)}  —  first home of {len(homes_now)} cards")


# ── question-bank link terms ──────────────────────────────────────────────
# Each card's own name, its alias parts that read like names, and its curated
# q:[...] list, normalized exactly as shared/app.js normalizes question text
# (atlasNorm). A question links to a card only when one of these appears as a
# whole phrase in its correct answer, the opening of its explanation, or its
# board-prep note.

GREEK = {"α": " alpha ", "β": " beta ", "γ": " gamma ", "δ": " delta ", "κ": " kappa ",
         "ε": " epsilon ", "μ": " mu "}
SUBSUP = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "01234567890123456789+-")

def atlas_norm(t):
    t = t.lower()
    for k, v in GREEK.items():
        t = t.replace(k, v)
    t = t.translate(SUBSUP)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"['’‘`]", "", t)
    t = re.sub(r"[‐‑‒–—―\-/]", " ", t)
    t = re.sub(r"[^a-z0-9+ ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def link_terms(n, alias, q):
    out = []
    base = n.split(" — ")[0]
    paren = re.findall(r"\(([^)]*)\)", base)
    out.append(re.sub(r"\s*\([^)]*\)", "", base))
    out += [p for p in paren if re.search(r"[A-Z]{3,}|syndrome|disease", p) and not p.lower().startswith("type ")]
    for a in re.split(r" · |, ", alias or ""):
        a = re.sub(r"\s*\([^)]*\)", "", a).split(" — ")[0].strip()
        if a and (" " in a or re.fullmatch(r"[A-Z0-9]{3,}", a)):
            out.append(a)
    # A q entry written "=term" counts only in the correct answer, never in the
    # explanation: for findings and anatomy that explanations mention in passing.
    # It also overrides the same term coming from the name or alias.
    answer_only = {atlas_norm(x[1:]) for x in q if x.startswith("=")}
    out += [x.lstrip("=") for x in q]
    seen = []
    for t in out:
        t = atlas_norm(t)
        if len(t) >= 3 and t not in seen:
            seen.append(t)
    return ["=" + t if t in answer_only else t for t in seen]

rows = []
heads = list(re.finditer(r'^([a-z0-9_]+):\{n:"([^"]*)",(?:alias:"([^"]*)",)?k:"([a-z]+)"', art, re.M))
for i, m in enumerate(heads):
    block = art[m.start():heads[i + 1].start() if i + 1 < len(heads) else art.index("const MAPS")]
    qm = re.search(r"\bq:(\[[^\]]*\])", block)
    q = json.loads(qm.group(1)) if qm else []
    rows.append([m.group(1), m.group(2), m.group(4), link_terms(m.group(2), m.group(3), q)])
# map id -> [title, card ids pinned anywhere on it], for "Practice this map" (#atlasmap/<id>)
map_cards = {}
for mm in re.finditer(r"^MAPS\.([a-z0-9_]+) = \{\s*t:\"([^\"]*)\"(.*?)\n\};", art, re.M | re.S):
    ids = []
    for lst in re.findall(r"\bm:\[([^\]]*)\]", mm.group(3)):
        for cid in re.findall(r'"([a-z0-9_]+)"', lst):
            if cid not in ids:
                ids.append(cid)
    if ids:
        map_cards[mm.group(1)] = [mm.group(2), ids]
# graphs: [map id, plot index, title, card ids] — PLOTCARDS lists the cards each graph kind illustrates; the question
# bank uses these for "See it on a graph" under a question and "Graphs for this block" (#graph/<map>/<plot> in the atlas)
plotcards = {}
pc = re.search(r"const PLOTCARDS=\{(.*?)\};", art, re.S)
if pc:
    for kind, lst in re.findall(r"([a-z0-9]+):\[([^\]]*)\]", pc.group(1)):
        plotcards[kind] = re.findall(r'"([a-z0-9_]+)"', lst)
card_ids = {r[0] for r in rows}
graphs = []
all_plots = []   # every graph, with or without cards — the hub's "Graph of the day"
for mm in re.finditer(r"^MAPS\.([a-z0-9_]+) = \{(.*?)\n\};", art, re.M | re.S):
    body = mm.group(2); k = body.find("\n plots:[")
    if k < 0:
        continue
    seg = body[k:body.find("\n edges:", k) if "\n edges:" in body[k:] else len(body)]
    for i, obj in enumerate(re.findall(r"\{[^{}]*kind:\"[a-z0-9]+\"[^{}]*\}", seg)):
        kind = re.search(r'kind:"([a-z0-9]+)"', obj).group(1); t = re.search(r't:"([^"]*)"', obj)
        ids = [c for c in plotcards.get(kind, []) if c in card_ids]
        if t:
            all_plots.append([mm.group(1), i, t.group(1)])
        if ids and t:
            graphs.append([mm.group(1), i, t.group(1), ids])
# moves: [map, "switch:option" ("" = the map as it opens), option label, map title, card ids] — "See it move" under a
# question opens a moving map with the switch for its card already on (#<map>/~<switch:option>), else just the map
moves = []
for mid, d in dyn_maps(art):
    tm = re.search(r"^MAPS\." + mid + r" = \{\s*t:\"([^\"]*)\"", art, re.M)
    title = tm.group(1) if tm else mid
    for sw in d.get("switches", []):
        for o in sw.get("options", []):
            if len(o) > 2 and o[2] in card_ids:
                moves.append([mid, f"{sw['id']}:{o[0]}", o[1], title, [o[2]]])
    on_map = {x["c"] for x in d.get("sites", []) if x.get("c") in card_ids} | set(map_cards.get(mid, [None, []])[1])
    moves.append([mid, "", "", title, sorted(on_map)])
TERMS_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. [id, name, kind, normalized terms]; maps: id -> [title, card ids]; graphs: [map, plot, title, card ids]; moves: [map, switch:option, label, map title, card ids] */\n"
                     "window.ATLAS_TERMS=" + json.dumps({"atlas": "metabolic-atlas.html", "cards": rows, "maps": map_cards, "graphs": graphs, "moves": moves},
                                                        ensure_ascii=False, separators=(",", ":")) + ";\n",
                     encoding="utf-8")
print(f"built {TERMS_OUT.relative_to(ROOT)}  —  {sum(len(r[3]) for r in rows)} link terms for {len(rows)} cards, {len(graphs)} graphs, "
      f"{sum(1 for x in moves if x[1])} moving-map switches")


# ── practice index: how many Q-bank questions link to each card ─────────────
# The same rule as atlasLinksFor() in shared/app.js — a term as a whole phrase
# (or with -s/-es) in the correct answer or the first explanation sentence
# ("=" terms in the answer only),
# earlier zone first, then longer term, top 3 cards per question — so the count
# on a card's button matches what #atlas/<id> finds when it runs in the block.

SHORT = {"psych": "Psych", "neuro": "Neuro", "endocrine": "Endocrine", "eent": "EENT", "pulm": "Pulm",
         "ortho": "Ortho", "rheum": "Rheum", "nephro": "Nephro", "gi": "GI", "omm": "OMM"}
hub = (ROOT / "index.html").read_text(encoding="utf-8")
blocks = []
for b in re.findall(r'href="([a-z0-9_-]+)/index\.html"', hub):
    if b not in [x[0] for x in blocks] and (ROOT / b / "data.js").exists():
        blocks.append((b, SHORT.get(b, b.capitalize())))

by_first = {}
for ci, (cid, _, _, terms) in enumerate(rows):
    for t in terms:
        by_first.setdefault(t.lstrip("=").split(" ")[0], set()).add(ci)

def first_hit(terms, text, zone):
    for t in terms:
        if t.startswith("="):           # answer-only term
            if zone:
                continue
            t = t[1:]
        if f" {t} " in text or f" {t}s " in text or f" {t}es " in text:
            return t
    return None

def links_for(q):
    expl = str(q.get("explanation") or "")
    lead = (re.findall(r"[^.!?]+[.!?]+", expl) or [expl])[0]
    ans = (q.get("choices") or {}).get(q.get("correct"))
    if isinstance(ans, list):   # grid ("matrix") choice, PROTOTYPE: cells joined, as choiceText() in app.js
        ans = " / ".join(str(c) for c in ans)
    zones = [ans, lead]
    found = {}
    for zone, z in enumerate(zones):
        if not z:
            continue
        text = " " + atlas_norm(z) + " "
        words = set(text.split())
        cand = set()
        for w in words:
            for key in (w, w[:-1] if w.endswith("s") else None, w[:-2] if w.endswith("es") else None):
                if key and key in by_first:
                    cand |= by_first[key]
        for ci in sorted(cand):
            cid = rows[ci][0]
            if cid in found:
                continue
            hit = first_hit(rows[ci][3], text, zone)
            if hit:
                found[cid] = (zone, len(hit), ci)
    return [cid for cid, _ in sorted(found.items(), key=lambda kv: (kv[1][0], -kv[1][1], kv[1][2]))[:3]]

counts = {}
qlinks = {}       # card id -> block index -> question ids linked to it (the atlas card's "Your record")
map_counts = {}   # map id -> block index -> questions linked to any card on that map (each question once)
graph_counts = {} # graph index -> block index -> questions linked to any card the graph illustrates (each question once)
graphs_of = {}
for gi, g in enumerate(graphs):
    for cid in g[3]:
        graphs_of.setdefault(cid, set()).add(gi)
maps_of = {}
for mid, (_, ids) in map_cards.items():
    for cid in ids:
        maps_of.setdefault(cid, set()).add(mid)
nq = 0
nlinked = 0       # questions linked to at least one card
sdl_list = []     # [block index, SDL number, title] for the hub's search
exam_counts = {}  # block folder -> {trial: [batches], exams: [[exam number, regular questions]]} for the hub's exam readiness
for bi, (b, _) in enumerate(blocks):
    raw = (ROOT / b / "data.js").read_text(encoding="utf-8")
    data = json.loads(raw[raw.index("=") + 1:].strip().rstrip(";"))
    # trial batches are opt-in and left out of exam totals, as in shared/app.js (isTrialQ):
    # batch 3 always, batch 4 only where the block's QUIZ_CONFIG defines batch4
    trial = [3] + ([4] if "batch4" in (ROOT / b / "index.html").read_text(encoding="utf-8") else [])
    exam_counts[b] = {"trial": trial, "exams": [[ex.get("examNumber"), sum(1 for sdl in ex["sdls"] for q in sdl["questions"] if q.get("batch") not in trial)]
                                                for ex in data["exams"]]}
    for ex in data["exams"]:
        for sdl in ex["sdls"]:
            sdl_list.append([bi, sdl.get("sdlNumber"), sdl.get("title") or ""])
            for q in sdl["questions"]:
                nq += 1
                hit_maps = set(); hit_graphs = set()
                qcards = links_for(q)
                nlinked += bool(qcards)
                for cid in qcards:
                    hit_graphs |= graphs_of.get(cid, set())
                    counts.setdefault(cid, {}).setdefault(bi, 0)
                    counts[cid][bi] += 1
                    if q.get("id"):
                        qlinks.setdefault(cid, {}).setdefault(bi, []).append(q["id"])
                    hit_maps |= maps_of.get(cid, set())
                for mid in hit_maps:
                    map_counts.setdefault(mid, {}).setdefault(bi, 0)
                    map_counts[mid][bi] += 1
                for gi in hit_graphs:
                    graph_counts.setdefault(gi, {}).setdefault(bi, 0)
                    graph_counts[gi][bi] += 1
PRACTICE_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. cards (and maps): id -> [[block index, questions]] */\n"
                        "window.ATLAS_PRACTICE=" + json.dumps(
                            {"blocks": [list(b) for b in blocks],
                             "cards": {cid: sorted(v.items(), key=lambda kv: -kv[1]) for cid, v in sorted(counts.items())},
                             "maps": {mid: sorted(v.items(), key=lambda kv: -kv[1]) for mid, v in sorted(map_counts.items())},
                             "graphs": {str(gi): sorted(v.items(), key=lambda kv: -kv[1]) for gi, v in sorted(graph_counts.items())}},
                            ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
QLINKS_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. card id -> [[block index, [question ids]]]: the atlas card's 'Your record' reads each block's attempt log for these */\n"
                      "window.ATLAS_QLINKS=" + json.dumps(
                          {"blocks": [list(b) for b in blocks],
                           "cards": {cid: sorted(v.items()) for cid, v in sorted(qlinks.items())}},
                          ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
COUNTS_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. Per block: trial batches and regular questions per exam, for the hub's exam readiness */\n"
                      "window.QBANK_COUNTS=" + json.dumps(exam_counts, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"built {COUNTS_OUT.relative_to(ROOT)}  —  exam totals for {len(exam_counts)} blocks")
print(f"built {QLINKS_OUT.relative_to(ROOT)}  —  question ids for {len(qlinks)} cards ({QLINKS_OUT.stat().st_size // 1024} KB)")
print(f"built {PRACTICE_OUT.relative_to(ROOT)}  —  {len(counts)} cards and {len(map_counts)} maps with practice questions from {nq} questions in {len(blocks)} blocks")


# ── the hub's home page (index.html): the atlas at a glance ─────────────────
# Systems and map titles for "Browse by system" and the search, a small schematic
# of each map (its first two lanes and their first steps, from the map's own
# compartments, or its pathways where it has none) for "Pick up where you left
# off", the newest batch of maps (the last line of NEW_MAPS), every graph for
# "Graph of the day", and each block's SDL titles for the search.
vseg = art[art.index("const VIEWS"):]
views = re.findall(r'\["([a-z0-9_]+)","([^"]*)"\]', vseg[:vseg.index("];")])
tseg = art[art.index("const TOPICS"):]
topics = [[t, n, re.findall(r'"([a-z0-9_]+)"', vs)] for t, n, vs in
          re.findall(r'\["([a-z0-9_]+)","([^"]+)",\[([^\]]*)\]\]', tseg[:tseg.index("]];") + 3]) if t != "idx"]
topic_of = {v: t for t, _, vs in topics for v in vs}
pseg = art[art.index("const PATHS"):]
paths = {k: (n, c) for k, n, c in re.findall(r'([A-Za-z0-9_]+):\{n:"([^"]*)",v:"--p-([a-z]+)"\}', pseg[:pseg.index("\n};")])}
nseg = art[art.index("const NEW_MAPS="):]
new_lines = [l for l in nseg[:nseg.index("};")].split("\n") if re.search(r'[a-z0-9_]+:"\d{4}-\d\d-\d\d"', l)]
latest = re.findall(r'([a-z0-9_]+):"\d{4}-\d\d-\d\d"', new_lines[-1]) if new_lines else []

def num(s, k):
    m = re.search(r"\b" + k + r":(-?[\d.]+)", s)
    return float(m.group(1)) if m else None

def preview(body):
    def seg(name):
        k = body.find("\n " + name + ":[")
        if k < 0:
            return ""
        nxt = [body.find("\n " + x + ":", k + 3) for x in ("comps", "mem", "panels", "nodes", "edges", "plots", "notes")]
        nxt = [x for x in nxt if x > k]
        return body[k:min(nxt) if nxt else len(body)]
    comps = []
    for o in re.findall(r"\{[^{}]*\}", seg("comps")):
        l = re.search(r'\bl:"([^"]*)"', o)
        if l and None not in (num(o, "x"), num(o, "y"), num(o, "w"), num(o, "h")):
            comps.append((num(o, "x"), num(o, "y"), num(o, "w"), num(o, "h"), l.group(1)))
    nodes = []
    for o in re.findall(r'\{id:"[^"]+"[^{}]*\}', seg("nodes")):
        nid = re.search(r'id:"([^"]+)"', o).group(1); l = re.search(r'\bl:"([^"]*)"', o)
        p = re.search(r'\bp:"([^"]*)"', o); k = re.search(r'\bk:"([^"]*)"', o)
        if l and l.group(1) and not (k and k.group(1) == "ghost") and num(o, "x") is not None and num(o, "y") is not None:
            nodes.append({"id": nid, "l": l.group(1), "x": num(o, "x"), "y": num(o, "y"), "p": p.group(1) if p else "neutral"})
    linked = set()
    for a, b in re.findall(r'\{a:"([^"]+)",b:"([^"]+)"', body):
        linked |= {(a, b), (b, a)}
    lanes, used = [], set()
    for x, y, w, h, l in comps:
        inside = [n for n in nodes if x <= n["x"] <= x + w and y <= n["y"] <= y + h and n["id"] not in used]
        if len(inside) >= 2:
            top = min(n["y"] for n in inside)
            row = sorted([n for n in inside if n["y"] - top < 40], key=lambda n: n["x"])
            if len(row) < 2:
                row = sorted(inside, key=lambda n: (n["y"], n["x"]))
            lanes.append((top, l, row[:5])); used |= {n["id"] for n in inside}
    if len(lanes) < 2:
        groups = {}
        for n in nodes:
            if n["id"] not in used:
                groups.setdefault(n["p"], []).append(n)
        for p, ns in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            if len(ns) >= 2 and len(lanes) < 2:
                ns = sorted(ns, key=lambda n: (n["y"], n["x"]))
                lanes.append((ns[0]["y"], paths.get(p, (p, ""))[0], ns[:5]))
    out = []
    for _, l, row in sorted(lanes, key=lambda t: t[0])[:2]:
        out.append([l, [[n["l"], paths.get(n["p"], ("", "neutral"))[1], int((n["id"], row[i + 1]["id"]) in linked) if i + 1 < len(row) else 0]
                        for i, n in enumerate(row)]])
    return out

home_maps = {}
for mm in re.finditer(r"^MAPS\.([a-z0-9_]+) = \{\s*t:\"([^\"]*)\"(.*?)\n\};", art, re.M | re.S):
    vid = mm.group(1)
    home_maps[vid] = [mm.group(2), topic_of.get(vid, ""), len(map_cards.get(vid, ["", []])[1]), preview(mm.group(3))]
# First Aid's abbreviation list from the atlas (ABBR), for the hub's search — minus everyday words
# ("as", "at", "if", "top"…) and the entries whose meaning is only a fragment of the term
ABBR_SKIP = {"as", "at", "if", "so", "top", "post", "ant", "asc", "max", "pat", "tib", "fem", "liv", "kid", "sp", "st", "ca", "cl",
             "vh", "vl", "fab", "fc", "ev", "nu", "pick", "szalus", "r3", "med", "cmc", "cmr", "vpl", "vpm", "tnm", "crest", "pap",
             "vpn", "col1a1", "col1a2", "mdma"}
am = re.search(r"^const ABBR=(\{.*?\});$", art, re.M)
abbr = {}
for k, ms in (json.loads(am.group(1)).items() if am else []):
    ms = [m for m in ms if len(m) >= 4 and "&" not in m and not m.endswith(".")]
    if k not in ABBR_SKIP and len(k) >= 2 and ms:
        abbr[k] = ms
home = {"stats": {"maps": len(home_maps), "cards": len(rows), "graphs": len(all_plots), "linked": nlinked}, "abbr": abbr,
        "topics": topics, "maps": home_maps, "latest": [v for v in latest if v in home_maps],
        "graphs": all_plots, "blocks": [list(b) for b in blocks], "sdls": sdl_list,
        "moves": [x[:4] for x in moves if x[1]],
        "dyn": sorted(keep)}   # the moving-map drawings (resources/dyn/), so the hub's "Save all" saves them too
HOME_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. The hub home page: atlas stats, systems, map titles and "
                    "schematics, the newest maps, every graph, and each block's SDLs for the search */\n"
                    "window.ATLAS_HOME=" + json.dumps(home, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"built {HOME_OUT.relative_to(ROOT)}  —  {len(home_maps)} maps in {len(topics)} systems, {len(all_plots)} graphs, "
      f"{nlinked} linked questions, {len(sdl_list)} SDLs, {len(abbr)} abbreviations ({HOME_OUT.stat().st_size // 1024} KB)")


# ── card summaries: the question bank's "On the Lesion Atlas" panel ───────────
# For every card a question links to: its one-line subtitle (enz), the opening of its
# mechanism, its first buzzword, its First Aid pages and its first two sources, short
# ("Costanzo ch 6"). shared/app.js loads this after the first answer, so the panel can
# show the card itself next to the explanation.
def js_str(block, key):
    m = re.search(r"\b" + key + r':"((?:[^"\\]|\\.)*)"', block)
    return re.sub(r"<[^>]+>", "", m.group(1).replace('\\"', '"').replace("\\\\", "\\")).strip() if m else ""

def js_list(block, key):
    m = re.search(r"\b" + key + r":\[(.*?)\]\s*[,}]", block, re.S)
    if not m:
        return []
    return [re.sub(r"<[^>]+>", "", s.replace('\\"', '"')).strip() for s in re.findall(r'"((?:[^"\\]|\\.)*)"', m.group(1))]

def lead(text, cap=260):
    out = ""
    for s in re.findall(r"[^.!?]+[.!?]+(?:\s|$)|[^.!?]+$", text):
        if out and len(out) + len(s) > cap:
            break
        out += s
        if len(out) >= 140:
            break
    out = out.strip()
    return out if len(out) <= cap else out[:cap - 1].rsplit(" ", 1)[0] + "…"

card_out = {}
for i, m in enumerate(heads):
    cid = m.group(1)
    if cid not in counts:
        continue
    block = art[m.start():heads[i + 1].start() if i + 1 < len(heads) else art.index("const MAPS")]
    enz = js_str(block, "enz")
    card_out[cid] = [enz if enz not in ("—", "-") else "", lead(js_str(block, "mech")),
                     next((b for b in js_list(block, "buzz") if b not in ("—", "-")), ""), js_str(block, "fa"),
                     [s.split(" — ")[0] for s in js_list(block, "src")[:2]]]
CARDS_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. card id -> [subtitle, mechanism lead, buzzword, FA pages, "
                     "[short sources]] for every card a question links to: the question bank's On the Lesion Atlas panel */\n"
                     "window.ATLAS_CARDS=" + json.dumps(card_out, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"built {CARDS_OUT.relative_to(ROOT)}  —  summaries of {len(card_out)} linked cards ({CARDS_OUT.stat().st_size // 1024} KB)")
