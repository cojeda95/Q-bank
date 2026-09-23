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
question to the matching atlas card.
"""
import json, re, shutil, subprocess, sys, tempfile, pathlib

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
args = [a for a in sys.argv[1:] if not a.startswith("--")]
ACCEPT_HOMES = "--accept-homes" in sys.argv
src = pathlib.Path(args[0]) if args else TOOLS / "atlas-src.html"
out = ROOT / "resources" / "metabolic-atlas.html"
TERMS_OUT = ROOT / "resources" / "atlas-terms.js"
HOMES = TOOLS / "atlas-homes.json"
art = src.read_text(encoding="utf-8")

# ── validation ────────────────────────────────────────────────────────────
# Two failure modes have shipped before. Both are silent at runtime, so the
# build refuses rather than warns.

ESCAPED_TAG = re.compile(r"</?(?:b|i|em|strong)>")

def validate(art):
    """Return a list of problems that should block the build."""
    problems = []
    lines = art.split("\n")

    # 1. n / alias / enz / inh / buzz are passed through esc() at render time,
    #    so any inline markup in them prints as literal "<b>" to the reader.
    #    mech / find / labs / tx ARE rendered as HTML and keep their emphasis.
    card = None
    for ln in lines:
        m = re.match(r"^([a-z0-9_]+):\{n:\"", ln)
        if m:
            card = m.group(1)
            if ESCAPED_TAG.search(ln):
                problems.append(
                    f"{card}: markup in an escaped header field "
                    f"(n/alias/enz/inh) — it will print as literal tags")
        elif ln.lstrip().startswith("buzz:[") and ESCAPED_TAG.search(ln):
            problems.append(
                f"{card}: markup in buzz — buzz is escaped, so tags show "
                f"literally in the side rail")

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
.ocom-topbar{background:#1f4e79;color:#fff;padding:14px 16px;flex:none;
  padding-top:calc(14px + env(safe-area-inset-top,0px))}
.ocom-topbar-inner{max-width:1100px;margin:0 auto;font-weight:700;font-size:1.1rem;
  display:flex;align-items:center;gap:14px;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.ocom-topbar-inner a{color:#fff;text-decoration:none;opacity:.85;font-weight:500;font-size:.95rem}
.ocom-topbar-inner a:hover{opacity:1;text-decoration:underline}
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
"""

TOPBAR = ('<div class="ocom-topbar"><div class="ocom-topbar-inner">'
          '<a href="../index.html">&larr; All Blocks</a>'
          '<span>Lesion Atlas</span></div></div>\n')

styled = artifact[:last_style_close] + OCOM_CSS + artifact[last_style_close:]
# the artifact's markup starts right after its stylesheet block
marker = '<div class="app">'
i = styled.index(marker)
built = head + styled[:i] + "\n</head>\n<body>\n" + TOPBAR + styled[i:] + "\n</body>\n</html>\n"

out.write_text(built, encoding="utf-8")
print(f"built {out.relative_to(out.parents[1])}  —  {maps} maps, {cards} cards, {len(built):,} bytes")

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
    out += q
    seen = []
    for t in out:
        t = atlas_norm(t)
        if len(t) >= 3 and t not in seen:
            seen.append(t)
    return seen

rows = []
heads = list(re.finditer(r'^([a-z0-9_]+):\{n:"([^"]*)",(?:alias:"([^"]*)",)?k:"([a-z]+)"', art, re.M))
for i, m in enumerate(heads):
    block = art[m.start():heads[i + 1].start() if i + 1 < len(heads) else art.index("const MAPS")]
    qm = re.search(r"\bq:(\[[^\]]*\])", block)
    q = json.loads(qm.group(1)) if qm else []
    rows.append([m.group(1), m.group(2), m.group(4), link_terms(m.group(2), m.group(3), q)])
TERMS_OUT.write_text("/* Built by tools/build-atlas.py — do not edit. [id, name, kind, normalized terms] */\n"
                     "window.ATLAS_TERMS=" + json.dumps({"atlas": "metabolic-atlas.html", "cards": rows},
                                                        ensure_ascii=False, separators=(",", ":")) + ";\n",
                     encoding="utf-8")
print(f"built {TERMS_OUT.relative_to(ROOT)}  —  {sum(len(r[3]) for r in rows)} link terms for {len(rows)} cards")
