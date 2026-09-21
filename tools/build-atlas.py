#!/usr/bin/env python3
"""Wrap the standalone Lesion Atlas in the OCOM Question Hub shell.

The standalone artifact is authored on its own; this adds the site head
(meta/og/mobile reset), the blue "All Blocks" topbar and the accent overrides
that make it match the hub. Run it after every atlas edit:

    python3 tools/build-atlas.py <standalone.html>

Counts in the meta and og tags are derived from the artifact, so they never
drift from what the page actually contains.
"""
import re, sys, pathlib

src = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "atlas-src.html")
out = pathlib.Path(__file__).resolve().parent.parent / "resources" / "metabolic-atlas.html"
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

    return problems


problems = validate(art)
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
