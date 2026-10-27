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
QSTATES_OUT = ROOT / "resources" / "atlas-qstates.js"
HOMES = TOOLS / "atlas-homes.json"
art = src.read_text(encoding="utf-8")

# ── validation ────────────────────────────────────────────────────────────
# Two failure modes have shipped before. Both are silent at runtime, so the
# build refuses rather than warns.

ESCAPED_TAG = re.compile(r"</?(?:b|i|em|strong)>")
KNOWN_SRC = re.compile(r"(Robbins|Katzung|Guyton|Costanzo|Kaplan & Sadock|Marks|Langman|Moore|Pawlina|"
                       r"Fundamental Neuroscience|Foundations of Osteopathic Medicine|Atlas of Osteopathic Techniques|"
                       r"Somatic Dysfunction in Osteopathic Family Medicine|An Osteopathic Approach to Diagnosis and Treatment|DeGowin|"
                       r"OCOM OMM|OCOM Ortho|OCOM Psych|OCOM Rheum|OCOM Nephro|OCOM Gastro|Osmosis|Bootcamp\.com) ")

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

# a kit with qlLoad (assemble.py #23) starts atlas-qlinks.js itself after the first map draws, and redraws what the
# practice counts touch once the deferred atlas-practice.js is in, so neither holds up the page; an older kit gets both up front
HEAD_SCRIPTS = ('<script src="atlas-practice.js" defer></script>\n' if "function qlLoad(" in art
                else '<script src="atlas-practice.js"></script>\n<script src="atlas-qlinks.js" defer></script>\n')
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
{HEAD_SCRIPTS}"""

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
# the Google Fonts stylesheet must not hold up the first paint (or the page's script, which waits for every stylesheet above
# it): load it as a preload that turns into a stylesheet when it arrives; the fonts swap in (display=swap), and the kit
# re-fits its labels on the FontFaceSet's loadingdone (assemble.py #23). Without JS, the plain stylesheet.
built, nf = re.subn(r'<link rel="stylesheet" href="(https://fonts\.googleapis\.com/[^"]+)">',
                    lambda m: (f'<link rel="preload" as="style" href="{m.group(1)}" onload="this.onload=null;this.rel=\'stylesheet\'">'
                               f'<noscript><link rel="stylesheet" href="{m.group(1)}"></noscript>'), built)
assert nf <= 1, nf

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

# ── card text: each card's text (LES_TEXT) goes to resources/atlas-les.<hash>.js, which the kit loads right after the first map
#    draws (lesLoad, assemble.py #23) — about 55 % of the page. The page keeps every other field (n, k, p, q, alias, hi, fa, enz):
#    the Index, the rail, search by name / alias / match term, #card links, homes and the quiz pickers work before it arrives;
#    opening a card waits for it ("Loading card…"). The name carries a hash of the content, so a page served from the offline
#    copy (sw.js) always asks for the card text of its own build; the previous file is deleted (a build artifact). LES is a JS
#    literal (unquoted keys), so JavaScriptCore evaluates it, as in the deep check. No jsc, or a kit without lesLoad → no split.
LES_TEXT = ("mech", "find", "labs", "buzz", "src", "tx", "inh", "gen", "ref")
les_name = None
_jsc = shutil.which("jsc") or next((p for p in JSC_PATHS if pathlib.Path(p).exists()), None)
if "function lesLoad(" in built and _jsc:
    la = built.index("const LES = {"); lb = built.index("\n};\n", la) + 4
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
        f.write(built[la:lb] + "\nprint(JSON.stringify(LES));\n")
    try:
        r = subprocess.run([_jsc, f.name], capture_output=True, text=True, timeout=120)
    finally:
        pathlib.Path(f.name).unlink(missing_ok=True)
    if r.returncode:
        sys.exit(f"card text split: LES does not evaluate — {(r.stderr or r.stdout).strip()[:400]}")
    les_all = json.loads(r.stdout)
    skel = {cid: {k: v for k, v in L.items() if k not in LES_TEXT} for cid, L in les_all.items()}
    les_text = {cid: {k: v for k, v in L.items() if k in LES_TEXT} for cid, L in les_all.items()}
    les_text = {cid: t for cid, t in les_text.items() if t}
    js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
    les_body = ("/* Built by tools/build-atlas.py — do not edit. The text of every Lesion Atlas card (" + ", ".join(LES_TEXT) +
            "), merged into the page's LES when it loads. */\nwindow.LESBODY=" + js(les_text) + ";\n")
    les_name = f"atlas-les.{hashlib.sha1(les_body.encode('utf-8')).hexdigest()[:10]}.js"
    (ROOT / "resources" / les_name).write_text(les_body, encoding="utf-8")
    built = (built[:la] + "const LES = " + js(skel).replace("</", "<\\/") + ";\n" +
             f"const LES_BODY = {json.dumps(les_name)};   /* the card text (tools/build-atlas.py) */\n" + built[lb:])
elif "function lesLoad(" in built:   # no jsc: the page keeps the whole LES, and LES_BODY = null tells the kit so (it still loads atlas-qlinks.js)
    print("  ! card text not split — JavaScriptCore (jsc) not found", file=sys.stderr)
    lb = built.index("\n};\n", built.index("const LES = {")) + 4
    built = built[:lb] + "const LES_BODY = null;   /* the card text is inline (tools/build-atlas.py) */\n" + built[lb:]
# keep the card text the last commit's page names too: a browser still holding that page (HTTP cache, no service worker)
# asks for it for a while after a deploy; anything older goes
try:
    _prev = subprocess.run(["git", "-C", str(ROOT), "show", "HEAD:resources/metabolic-atlas.html"], capture_output=True, text=True).stdout
    _m = re.search(r'const LES_BODY = "(atlas-les\.[0-9a-f]+\.js)"', _prev); _keep_prev = _m.group(1) if _m else None
except Exception:
    _keep_prev = None
for f in (ROOT / "resources").glob("atlas-les.*.js"):
    if f.name not in (les_name, _keep_prev):
        f.unlink()
out.write_text(built, encoding="utf-8")
print(f"built {out.relative_to(out.parents[1])}  —  {maps} maps, {cards} cards, {len(built):,} bytes")
print(f"built resources/dyn/  —  {len(keep)} moving-map drawings, {moved:,} bytes moved out of the page")
if les_name:
    print(f"built resources/{les_name}  —  the text of {len(les_text)} cards, {len(les_body.encode('utf-8')):,} bytes moved out of the page")

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
         "ortho": "Ortho", "rheum": "Rheum", "nephro": "Nephro", "gi": "GI", "gastro": "Gastro", "omm": "OMM"}
hub = (ROOT / "index.html").read_text(encoding="utf-8")
blocks = []
for b in re.findall(r'href="([a-z0-9_-]+)/index\.html"', hub):
    if b not in [x[0] for x in blocks] and (ROOT / b / "data.js").exists():
        blocks.append((b, SHORT.get(b, b.capitalize())))

by_first = {}
for ci, (cid, _, _, terms) in enumerate(rows):
    for t in terms:
        by_first.setdefault(t.lstrip("=").split(" ")[0], set()).add(ci)

# The explanation's first sentence: it ends at . ! or ? followed by a space or the end, but not
# after a lone capital ("H. pylori", "E. coli") — shared/app.js atlasLead() must match
LEAD_END = re.compile(r"(?<!\b[A-Z])[.!?]+(?=\s|$)")

def expl_lead(expl):
    m = LEAD_END.search(expl)
    return expl[:m.end()] if m else expl

# a term's s/es form that is an ordinary word is not its plural: LES + s = "less" (app.js atlasMatch must match)
NOT_PLURAL = {"less", "has", "was", "yes", "does", "goes", "lies", "dies", "bias", "gas", "bus", "its", "thus", "plus"}

def first_hit(terms, text, zone):
    for t in terms:
        if t.startswith("="):           # answer-only term
            if zone:
                continue
            t = t[1:]
        if f" {t} " in text or (f"{t}s" not in NOT_PLURAL and f" {t}s " in text) or (f"{t}es" not in NOT_PLURAL and f" {t}es " in text):
            return t
    return None

def links_for(q):
    expl = str(q.get("explanation") or "")
    lead = expl_lead(expl)
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
qrecs = []        # (block index, question, linked cards) — for the question states below
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
                qrecs.append((bi, q, qcards))
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


# ── question states: "See it move →" after a miss ─────────────────────────────
# For each question, the moving-map switch option that shows what the question is about, so the question bank can open
# that map with it already on (#<map>/~<switch>:<option>). Only confident matches are kept; any other question opens
# the map for its card as before (atlas-terms.js moves). resources/atlas-qstates.js: per block, question id ->
# [map, switch id, option key]. The rules, in order of strength (a tier is "where the match comes from"):
#   0-2  an option pinned to the question's linked card of that rank (links_for above). The option's label must be named
#        in the answer or as the subject of the explanation lead (its first words: a lead's examples and contrasts do not
#        count). Rank 0: the answer opens with it, or something else in the question is about the map (another linked card on it, its title words, another of its options); a drug's switch shows one of
#        its effects ("Glucocorticoids" on Bone Remodeling is not fat redistribution, "Beta-blockers" for akathisia not
#        the ECG), so a drug must be in the answer with two such things (one of them the map's title when the drug has states on
#        several maps: lithium's dose in CKD is not Calcium & PTH) — or one, opening the answer, on its only map.
#        Named only after a contrast ("unlike …", "rather than …") does not count.
#        Rank 1-2 (never a drug): the answer must open with it (its first four words), and the rank-0 card must have no state of its own on another map.
#   3    the answer opens (first four words) by naming an option whose card was not linked: a long several-word label on a
#        map one of the question's cards is on and whose title the question uses ("Beta-blockers" for akathisia is not
#        Poison & Antidote's β-blocker), or any label on a map whose title the question spells out ("Type 2 renal tubular
#        acidosis" → Renal Tubular Acidosis Simulator · Type 2 — proximal).
#   4    the stem's question asks about an option by a several-word name on a map whose title the stem spells out ("Which pairing … best
#        fits type 4 RTA?"); that map then goes first, though a card the answer names on it still wins there.
# Then: the best tier, the place it is named (answer < lead < stem), the most context, the atlas's own order; two options
# on that map that nothing tells apart → no state.
ROMAN = {"i": "1", "ii": "2", "iii": "3", "iv": "4", "v": "5", "vi": "6", "vii": "7", "viii": "8"}
def qs_canon(t):
    """atlas_norm text, with type/class/grade IV → 4, so "Type IV RTA" meets the label "Type 4 — hyperkalemic\""""
    return re.sub(r"\b(type|class|grade|stage|mobitz) (i|ii|iii|iv|v|vi|vii|viii)\b", lambda m: m.group(1) + " " + ROMAN[m.group(2)], t)
QS_STOP = {"in", "motion", "the", "a", "an", "of", "and", "or", "to", "on", "map", "maps", "simulator", "work", "up", "flow", "with",
           "for", "how", "what", "it", "its", "at", "by", "from", "explorer", "lab", "labs", "cause", "causes", "type", "types",
           "drug", "drugs", "test", "tests", "function", "normal", "none", "baseline", "healthy", "control", "other", "left", "right",
           "blood", "body", "cell", "cells", "system", "systems", "human", "loss", "pain"}
# First Aid abbreviations with one several-word meaning ("di" → "diabetes insipidus"): the label "Nephrogenic DI" also
# matches the spelled-out name, and a question's "RTA" counts toward the title Renal Tubular Acidosis
_am = re.search(r"^const ABBR=(\{.*?\});$", art, re.M)
QS_ABBR = {k: qs_canon(atlas_norm(v[0])) for k, v in (json.loads(_am.group(1)).items() if _am else [])
           if len(v) == 1 and len(k) >= 2 and " " in v[0] and k not in {"as", "at", "if", "so", "top", "post", "ant", "max", "pat", "med", "pick"}}
def qs_expand(n):
    return " ".join(QS_ABBR.get(w, w) for w in n.split())
def qs_term(p):
    n = qs_canon(atlas_norm(p))
    return n if (len(n) >= 4 or re.fullmatch(r"[A-Z0-9]{3}", p.strip())) and n not in QS_STOP and not n.isdigit() else None
def qs_label_terms(label):
    """(names, qualifiers) of an option label. Names: the whole label, and each alternative before any dash or
    parenthesis ("Sjögren · SLE" → sjogren, sle; "Hemiballismus (STN lesion)" → hemiballismus), and qualifiers of two or
    more words ("Type 2 — proximal" is named by "type 2", never by "proximal" alone; "Locked-in (basilar)" never by
    "basilar"). Qualifiers: every part after a dash or in parentheses, used only to tell apart options that share a name."""
    head = re.split(r" — | – ", label)[0]
    quals = re.findall(r"\(([^)]*)\)", label) + re.split(r" — | – ", label)[1:]
    names = [label] + re.split(r" · |/|, ", re.sub(r"\s*\([^)]*\)", "", head))
    quals = [q for p in quals for q in re.split(r" · |/|, ", re.sub(r"\s*\([^)]*\)", "", p))]
    names = [qs_term(p) for p in names] + [qs_term(q) for q in quals if qs_term(q) and " " in qs_term(q)]
    out = []
    for n in names:
        if n:
            out += [v for v in dict.fromkeys([n, qs_expand(n)]) if v not in out]
    return out, [q for q in map(qs_term, quals) if q]
# A label term inside the longer name of a card from another map is not the label: "type 2" in "type 2 diabetes" is not
# the RTA simulator's Type 2 (but "type 1" in "type 1 renal tubular acidosis", a card on that map, still is)
QS_CARDTERMS = {}
for _r in rows:
    for _t in _r[3]:
        QS_CARDTERMS.setdefault(_t.lstrip("=").split(" ")[0], set()).add((_t.lstrip("="), _r[0]))
QS_LONGER = {}
def qs_mask(t, text, mid):
    if t not in QS_LONGER:
        QS_LONGER[t] = sorted(((ct, c) for ct, c in QS_CARDTERMS.get(t.split(" ")[0], ()) if ct.startswith(t + " ")), key=lambda x: -len(x[0]))
    on = qs_mapcards.get(mid, ())
    for ct, c in QS_LONGER[t]:
        if c not in on:
            text = text.replace(" " + ct + " ", " # ").replace(" " + ct + "s ", " # ")
    return text
def qs_hit(terms, text, mid=None):
    for t in terms:
        if f" {t} " in text or f" {t}s " in text:
            if mid is None:
                return True
            text2 = qs_mask(t, text, mid)
            if f" {t} " in text2 or f" {t}s " in text2:
                return True
    return False
QS_NOT = {"unlike", "not", "no", "non", "without", "than", "versus", "vs", "excluding", "except", "nor"}
def qs_early(terms, head, mid=None, within=5):
    """a term named in the first words of the answer's headline, and not as what it is NOT ("Unlike S. pneumoniae")"""
    words = head.split()
    while words and words[0] in ("the", "a", "an"):
        words = words[1:]
    text = " " + " ".join(words) + " "
    for t in terms:
        for m in re.finditer(re.escape(" " + t) + r"s? ", qs_mask(t, text, mid) if mid else text):
            i = text[:m.start()].count(" ")
            if i <= within and not (i and words[i - 1] in QS_NOT):
                return True
    return False
QS_NUMBERED = re.compile(r"(?:type|class|grade|stage|zone|phase) \d")
QS_CONTRAST = re.compile(r" (unlike|rather than|in contrast|instead of|whereas|versus|vs|compared with|as opposed to|not|no|without|negative|"
                         r"absent|absence of|excluded?|exclusion|rules? out|distinguished from|differs? from) ")
QS_UP = {"increased", "increase", "increases", "raised", "raises", "high", "higher", "elevated", "rise", "rises", "rising", "greater"}
QS_DOWN = {"decreased", "decrease", "decreases", "reduced", "reduces", "low", "lower", "lowers", "fall", "falls", "falling", "less", "diminished"}

QS_OPT = {}      # (map, switch, option) -> {"names", "quals", "card", "dir", "sib"}
qs_opts = {}     # card id -> [(map, switch, option, order)]
qs_bylabel = []  # every option: (map, switch, option, order, card)
qs_mapcards, qs_mapwords, qs_maplabels = {}, {}, {}
qs_workup = set()   # the symptom work-ups (Weight Loss Work-Up …): every disease is an option there, so the question must be about the symptom
order = 0
for mid, d in dyn_maps(art):
    tm = re.search(r"^MAPS\." + mid + r" = \{\s*t:\"([^\"]*)\"", art, re.M)
    if re.search(r"work-?up", tm.group(1) if tm else "", re.I):
        qs_workup.add(mid)
    qs_mapwords[mid] = {re.sub(r"(?<=[^s])s$", "", w) for w in qs_canon(atlas_norm(tm.group(1) if tm else "")).split() if len(w) >= 4 and w not in QS_STOP}
    on = set(map_cards.get(mid, [None, []])[1]) | {x.get("c") for x in d.get("sites", []) if x.get("c")}
    labs = []
    for sw in d.get("switches", []):
        first = {}
        for o in sw.get("options", []):
            order += 1
            names, quals = qs_label_terms(o[1])
            card = o[2] if len(o) > 2 and o[2] in card_ids else None
            key = (mid, sw["id"], o[0])
            QS_OPT[key] = {"names": names, "quals": quals, "card": card, "sib": False,
                           "dir": 1 if "↑" in o[1] else -1 if "↓" in o[1] else 0}
            labs.append((card, names))
            first.setdefault(names[1] if len(names) > 1 else names[0] if names else "", []).append(key)
            if card:
                on.add(card)
                qs_opts.setdefault(card, []).append((mid, sw["id"], o[0], order))
            qs_bylabel.append((mid, sw["id"], o[0], order, card))
        for keys in first.values():        # options on one switch that share a name ("Median — supracondylar", "Median — carpal tunnel")
            if len(keys) > 1:
                for k in keys:
                    QS_OPT[k]["sib"] = True
    qs_mapcards[mid], qs_maplabels[mid] = on, labs
qs_first = {}    # first word of a name -> options, so tiers 3 and 4 only try options the text could name
for li, x in enumerate(qs_bylabel):
    for term in QS_OPT[x[:3]]["names"]:
        qs_first.setdefault(term.split(" ")[0], set()).add(li)
qs_drugs = {r[0] for r in rows if r[2] == "drug"}
qs_drugmaps = {c: {x[0] for x in v} for c, v in qs_opts.items()}
qs_cardterms = {r[0]: [t.lstrip("=") for t in r[3]] for r in rows}

def qs_titled(t, text, mid):
    """t followed by one of the map's title words: "type 4 renal tubular acidosis" (text with abbreviations spelled out)"""
    return bool(qs_mapwords[mid]) and bool(re.search(re.escape(" " + t) + r"s? (?:" + "|".join(map(re.escape, qs_mapwords[mid])) + r")s? ",
                                                     qs_mask(t, text, mid)))
def zx(z):
    return " " + " ".join(QS_ABBR.get(w, w) for w in z.split()) + " "

# The lead rule: a question that links a single card may take a state from the explanation's opening words alone (cx 0),
# but only on a map of the block's own system — elsewhere the same lead lands on look-alike maps (biliary atresia on edema).
LEAD_SYS = {"gastro": {"gi"}, "gi": {"gi"}, "nephro": {"renal"}, "pulm": {"pulmo"}, "endocrine": {"endo"}, "neuro": {"neuro"},
            "psych": {"behav"}, "eent": {"eent"}, "rheum": {"msk", "immuno"}, "ortho": {"msk"}, "omm": {"omm"}}
_tseg = art[art.index("const TOPICS"):]
MAP_SYS = {v: t for t, vs in re.findall(r'\["([a-z0-9_]+)","[^"]+",\[([^\]]*)\]\]', _tseg[:_tseg.index("]];") + 3])
           for v in re.findall(r'"([a-z0-9_]+)"', vs)}
# hand-checked (m60): the lead names the map's option but the question is about something the map does not show
LEAD_NO = {"gastro": {"sdl11_q20"}, "neuro": {"sdl09_q05", "sdl38_q24"}, "psych": {"sdl25_q04", "sdl32_q01", "sdl16_q19"},
           "pulm": {"sdl18_ex1_q02_b1", "sdl18_ex1_q15_b1", "sdl22_ex1_q15_b1", "sdl23_ex1_q04_b1", "sdl23_ex1_q05_b1",
                    "sdl23_ex1_q08_b1", "sdl23_ex1_q14_b1"}}
QS_BLOCK = [None, None]   # block, question id
def lead_ok(mid, qcards):
    return (len(qcards) == 1 and MAP_SYS.get(mid) in LEAD_SYS.get(QS_BLOCK[0], ())
            and QS_BLOCK[1] not in LEAD_NO.get(QS_BLOCK[0], ()))

def qs_state(q, qcards):
    expl = str(q.get("explanation") or "")
    lead = expl_lead(expl)
    ans = (q.get("choices") or {}).get(q.get("correct"))
    if isinstance(ans, list):
        ans = " / ".join(str(c) for c in ans)
    zones = [" " + qs_canon(atlas_norm(z or "")) + " " for z in (ans, lead, q.get("stem"))]
    alltext = "".join(zones)
    alltext += " " + " ".join(QS_ABBR[w] for w in set(alltext.split()) if w in QS_ABBR) + " "
    # the answer's headline: what it names before the reasoning that follows (as atlasOptionCard in shared/app.js)
    head = " " + qs_canon(atlas_norm(re.split(r"[,;:(]| [—–-] | (?:which|because|since|due to|caused by|as|so|while|whereas|that) ",
                                              str(ans or ""), flags=re.I)[0])) + " "
    hwords = set(head.split())
    def named(names, z, mid):   # named in z, and not only after a contrast ("…, unlike the receptor antibodies of myasthenia gravis")
        for t in names:
            if QS_NUMBERED.fullmatch(t) and not ((z is zones[0] and qs_early([t], head, mid) and title(mid, alltext))
                                                 or (z is not zones[2] and qs_titled(t, zx(z), mid))):
                continue   # a bare "Type II" / "Zone 1" only followed by the map's title ("type 1 RTA"), or opening the
                           # answer to a question that uses the title ("Salter-Harris Type II" on Fractures); never the stem
            z2 = qs_mask(t, z, mid)
            m = re.search(re.escape(" " + t) + r"s? ", z2)
            if m and not QS_CONTRAST.search(z2[:m.start() + 1]):
                return True
        return False
    def lab(names, mid):   # where the question names the option: 0 answer, 1 explanation lead, 2 stem, 3 nowhere
        return next((zi for zi, z in enumerate(zones) if named(names, z, mid)), 3)
    def title(mid, text):
        return sum(f" {w} " in text or f" {w}s " in text for w in qs_mapwords[mid])
    def ctx(mid, card):    # what ELSE in the question is about this map: its other linked cards, its title words, its other options
        return (sum(c in qs_mapcards[mid] for c in qcards if c != card) + title(mid, alltext)
                + sum(qs_hit(t, alltext, mid) for c, t in qs_maplabels[mid] if t and (c != card or not c)))
    cands = []   # (tier, where named, context, order, map, switch, option)
    for r, c in enumerate(qcards):                                                 # tiers 0-2
        for mid, sw, key, o in qs_opts.get(c, []):
            names = QS_OPT[(mid, sw, key)]["names"]
            lb, cx, early = lab(names, mid), ctx(mid, c), qs_early(names, head, mid)
            if r == 0:
                good = (lb == 0 and (cx >= 1 or early)
                        or lb == 1 and (cx >= 1 or lead_ok(mid, qcards)) and qs_early(names, zones[1], mid, 7)) if c not in qs_drugs else lb == 0 and (
                    (cx >= 2 and (len(qs_drugmaps[c]) == 1 or title(mid, alltext))) or (cx >= 1 and early and len(qs_drugmaps[c]) == 1))
            else:
                good = lb < 2 and qs_early(names, head, mid, 3) and c not in qs_drugs
            if good:
                cands.append((r, lb, cx, o, mid, sw, key))
    first_maps = {x[4] for x in cands if x[0] == 0}
    cands = [x for x in cands if x[0] == 0 or not (first_maps - {x[4]})]
    two = re.search(r" (combined|mixed|both|concomitant|superimposed|concurrent|coexisting) ", head)
    if not two:                                                                    # tier 3 — not "Combined respiratory and metabolic acidosis"
        words = hwords | {w[:-1] for w in hwords if w.endswith("s")}
        for li in sorted({li for w in words for li in qs_first.get(w, ())}):
            mid, sw, key, o, card = qs_bylabel[li]
            # a bare "Zone 1" or "Type 2" only when followed by the map's title ("Zone 1, creating dead space" is not
            # the liver's zone 1)
            names = [n for n in QS_OPT[(mid, sw, key)]["names"] if not QS_NUMBERED.fullmatch(n) or qs_titled(n, zx(head), mid)]
            tw = title(mid, alltext)
            quals = QS_OPT[(mid, sw, key)]["quals"]
            if quals and not qs_hit(quals, alltext, mid):    # "Compression atelectasis" is not "Atelectasis (suction)"
                names = [n for n in names if " " in n]
            if card not in qcards and ((qs_early([t for t in names if len(t) >= 8 and " " in t], head, mid, 3) and tw and any(c in qs_mapcards[mid] for c in qcards))
                                       or (qs_early(names, head, mid, 3) and tw >= 2)):
                cands.append((3, 0, ctx(mid, card), o, mid, sw, key))
    # tier 4: in the stem's question itself (its last sentence), not the history before it, and named as the map's subject —
    # followed by a title word ("type 4 RTA" = "type 4 renal tubular acidosis"; not "just after the optic chiasm, …")
    ask = " " + qs_canon(atlas_norm((re.findall(r"[^.!?\n]+[.!?]*\s*$", str(q.get("stem") or "")) or [""])[0])) + " "
    swords = set(ask.split())
    ask = " " + " ".join(QS_ABBR.get(w, w) for w in ask.split()) + " "
    stemx = zones[2] + " ".join(QS_ABBR[w] for w in set(zones[2].split()) if w in QS_ABBR) + " "
    for li in sorted({li for w in swords for li in qs_first.get(w, ())}):
        mid, sw, key, o, card = qs_bylabel[li]
        if title(mid, stemx) >= 2 and any(qs_titled(t, ask, mid) for t in QS_OPT[(mid, sw, key)]["names"] if " " in t):
            cands.append((4, 2, ctx(mid, card), o, mid, sw, key))
    # vetoes: an answer naming two states at once ("Metabolic acidosis with concomitant respiratory acidosis") unless the
    # option is the mixed one; a work-up whose symptom the question does not ask about; a numbered class or type the answer names and the label does not
    # ("Class VI with …" is not "Lupus nephritis (DPGN)"); options sharing a name where the question gives none of this
    # one's qualifiers; the opposite direction ("Reduced venous return and lower preload" is not "↑ Preload"); and an
    # answer that opens by naming another linked card ("Bulimia nervosa; distinguished from anorexia nervosa…")
    num = re.findall(r" ((?:class|type|grade|stage) \d) ", head)
    head_cards = {c for c in qcards if qs_early(qs_cardterms.get(c, []), head)}
    def veto(x):
        op = QS_OPT[(x[4], x[5], x[6])]
        if two and not any(re.search(r"\bmixed\b|\bcombined\b|\+", n) for n in op["names"]):   # two states, one option
            return True
        if x[4] in qs_workup and not title(x[4], zones[0] + zones[1] + ask):   # the symptom in what is asked, not the history
            return True
        if num and not all(n in " ".join(op["names"] + op["quals"]) + " " for n in num):
            return True
        if op["sib"] and not qs_hit(op["quals"], alltext, x[4]):
            return True
        if op["dir"] and (hwords & (QS_DOWN if op["dir"] > 0 else QS_UP)) and not (hwords & (QS_UP if op["dir"] > 0 else QS_DOWN)):
            return True
        if x[0] < 3 and head_cards and qcards[x[0]] not in head_cards and not qs_early(op["names"], head, x[4]):
            return True
        return False
    cands = [x for x in cands if not veto(x)]
    if not cands:
        return None
    stem_maps = {x[4] for x in cands if x[0] == 4}
    cands.sort(key=lambda x: (x[4] not in stem_maps, x[0], x[1], -x[2], x[3]))
    best = cands[0]
    for x in cands[1:]:                    # two options on the best map that nothing tells apart
        if x[4] == best[4] and (x[5], x[6]) != (best[5], best[6]) and x[:3] == best[:3]:
            return None
    return [best[4], best[5], best[6]]

qstates = {}
for bi, q, qcards in qrecs:
    if q.get("id"):
        QS_BLOCK[:] = [blocks[bi][0], q["id"]]
        st = qs_state(q, qcards)
        if st:
            qstates.setdefault(str(bi), {})[q["id"]] = st
nqs = sum(len(v) for v in qstates.values())
QSTATES_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. per block index: question id -> [moving map, switch id, option key] — "
                       "the question bank's \"See it move →\" after a miss opens #<map>/~<switch>:<option> */\n"
                       "window.ATLAS_QSTATES=" + json.dumps({"blocks": [b for b, _ in blocks], "q": qstates},
                                                          ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print(f"built {QSTATES_OUT.relative_to(ROOT)}  —  moving-map states for {nqs} of {nq} questions "
      f"({len({s[0] for v in qstates.values() for s in v.values()})} maps, {QSTATES_OUT.stat().st_size // 1024} KB)")


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
latest_date = (re.search(r'"(\d{4}-\d\d-\d\d)"', new_lines[-1]).group(1) if new_lines else "")   # the batch's go-live date, for the hub tile
# the atlas's What's-new lines from that same date (simple <b> markup only), shown on the hub tile
wseg = art[art.index("const WHATSNEW=["):]
latest_news = [json.loads(t) for d, t in re.findall(r'\[\s*"(\d{4}-\d\d-\d\d)",\s*("(?:[^"\\]|\\.)*")\s*\]', wseg[:wseg.index("];")]) if d == latest_date]

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
        "topics": topics, "maps": home_maps, "latest": [v for v in latest if v in home_maps], "latestDate": latest_date, "latestNews": latest_news,
        "graphs": all_plots, "blocks": [list(b) for b in blocks], "sdls": sdl_list,
        "moves": [x[:4] for x in moves if x[1]],
        "dyn": sorted(keep),   # the moving-map drawings (resources/dyn/), so the hub's "Save all" saves them too
        "les": les_name}       # the card text file (resources/atlas-les.<hash>.js) — Save all saves it too
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
