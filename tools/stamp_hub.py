#!/usr/bin/env python3
"""Write the hub hero and block-card counts into index.html.

Reads the same numbers tools/build-atlas.py stores in resources/qbank-counts.js
(regular questions per exam) and resources/atlas-home.js (map/card stats and SDL
lists). The HTML is what shows with JavaScript off; the hub script sets the
same sentences once those files load. Run automatically at the end of the
atlas build, or alone after those two files change:

    python3 tools/stamp_hub.py
"""
import json
import pathlib
import re
import sys

TOOLS = pathlib.Path(__file__).resolve().parent
ROOT = TOOLS.parent
HUB = ROOT / "index.html"
COUNTS = ROOT / "resources" / "qbank-counts.js"
HOME = ROOT / "resources" / "atlas-home.js"


def _fmt(n):
    return f"{int(n):,}"


def hero_text(stats):
    return (f"{_fmt(stats['maps'])} maps and {_fmt(stats['cards'])} cards, every one sourced, "
            f"and linked to {_fmt(stats['linked'])} of your practice questions.")


def card_text(n_exams, n_sdls, n_questions):
    exams = f"{n_exams} exam" + ("" if n_exams == 1 else "s")
    sdls = f"{n_sdls} SDL" + ("" if n_sdls == 1 else "s")
    if n_questions <= 0:
        return f"{exams} · {sdls} · coming soon"
    return f"{exams} · {sdls} · {_fmt(n_questions)} questions"


def load_js_json(path, marker):
    text = path.read_text(encoding="utf-8")
    i = text.index(marker)
    return json.loads(text[i + len(marker):].strip().rstrip(";"))


def stamp_from_objects(exam_counts, home, path=HUB):
    """Replace the hero line and each block card's count from the in-memory build data."""
    html = path.read_text(encoding="utf-8")
    hero = hero_text(home["stats"])
    html2, n = re.subn(
        r'(<p class="lede" id="heroLede">)(.*?)(</p>)',
        lambda m: m.group(1) + hero + m.group(3),
        html, count=1, flags=re.S)
    if n != 1:
        raise SystemExit("stamp_hub: hero line not found in index.html")
    sdl_n = {}
    for bi, _num, _title in home.get("sdls") or []:
        sdl_n[bi] = sdl_n.get(bi, 0) + 1
    for i, block in enumerate(home["blocks"]):
        folder = block[0]
        info = exam_counts.get(folder)
        if not info:
            continue
        desc = card_text(len(info["exams"]), sdl_n.get(i, 0), sum(e[1] for e in info["exams"]))
        pat = (rf'(<a class="block-card" href="{re.escape(folder)}/index\.html">'
               rf'\s*<div class="block-title">.*?</div>\s*<div class="block-desc">)(.*?)(</div>)')
        html2, n = re.subn(pat, lambda m, desc=desc: m.group(1) + desc + m.group(3), html2, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f"stamp_hub: block card for {folder} not found in index.html")
    if html2 != html:
        path.write_text(html2, encoding="utf-8")
    return hero


def main():
    counts = load_js_json(COUNTS, "window.QBANK_COUNTS=")
    home = load_js_json(HOME, "window.ATLAS_HOME=")
    hero = stamp_from_objects(counts, home)
    print(f"stamped hub counts — {hero}")


if __name__ == "__main__":
    sys.exit(main())
