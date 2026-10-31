#!/usr/bin/env python3
"""Build resources/qsearch.js — the hub's question search index (m66).

    python3 tools/build-search.py          # also run at the end of tools/build-atlas.py

Run it after any <block>/data.js change (tools/test-site.py fails when the index is stale: each block's data.js hash and
question ids are written into the index and compared).

The hub (index.html) loads the index lazily, the first time the search box is focused, so the ~20 MB of data.js files are
never loaded on the hub. Per question the index holds its block, id, SDL and the opening of its stem (the result's snippet).
What is searchable: the stem, the keyed answer and the explanation's first sentence, normalized like the hub's atlas search
(norm() in index.html = atlas_norm in build-atlas.py) and split into words. Two inverted lists per word:
  P  the questions whose stem or keyed answer has the word   (ranked higher)
  S  the questions that have it only in the explanation's first sentence
Each list is the ascending question numbers, delta-encoded in base 45 with a terminal/continuation alphabet (see enc()),
so no separators and most gaps are one character. Stop words, the question template's words ("best", "explains") and words
in more than DROP_DF of all questions are left out (listed in `stop`, so the hub ignores them in a query instead of finding
nothing).

Format: window.QSEARCH = {
  v: 1, n: number of questions,
  blocks: [[folder, short name, hub tile title]], src: {folder: first 10 hex of sha1(data.js)} (freshness, test-site.py),
  sdls: [[block index, sdlNumber, title, number of questions]] — questions are numbered in this order, SDL by SDL,
  ids: the ids in question number order, front-coded like words (not sorted), snip: ["the stem's first SNIP characters…", …],
  words: front-coded sorted words (front_code()), post: "P!S P!S …" one entry per word ("!S" left off when S is empty),
  stop: "words not indexed" }
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "resources" / "qsearch.js"
SNIP = 72           # snippet length (characters of the stem)
DROP_DF = 0.25      # words in more than this share of questions are not indexed

SHORT = {"psych": "Psych", "neuro": "Neuro", "endocrine": "Endocrine", "eent": "EENT", "pulm": "Pulm",
         "ortho": "Ortho", "rheum": "Rheum", "nephro": "Nephro", "gastro": "Gastro", "omm": "OMM", "research": "Research"}
STOP = set("""a an the and or nor but of to in on at by for with from into onto over under as is are was were be been being
am it its this that these those which who whom whose what when where why how than then so such not no do does did has have
had having he she his her him they them their there here we our you your i me my can could would should will shall may might
must also both either neither each any all most more very just only other others own same s t
best following explains describes shows likely according rather directly which""".split())   # + the question template

GREEK = {"α": " alpha ", "β": " beta ", "γ": " gamma ", "δ": " delta ", "κ": " kappa ", "ε": " epsilon ", "μ": " mu "}
SUBSUP = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "01234567890123456789+-")


def norm(t):
    """= atlas_norm (tools/build-atlas.py) and norm() in index.html, plus accents dropped (index.html does that too)"""
    import unicodedata
    t = str(t).lower()
    for k, v in GREEK.items():
        t = t.replace(k, v)
    t = t.translate(SUBSUP)
    t = "".join(c for c in unicodedata.normalize("NFD", t) if not unicodedata.combining(c))
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"['’‘`]", "", t)
    t = re.sub(r"[‐‑‒–—―\-/]", " ", t)
    t = re.sub(r"[^a-z0-9+ ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# the explanation's first sentence — the same rule as expl_lead in build-atlas.py / atlasLead in shared/app.js
LEAD_END = re.compile(r"(?<!\b[A-Z])[.!?]+(?=\s|$)")


def expl_lead(expl):
    m = LEAD_END.search(expl or "")
    return expl[:m.end()] if m else (expl or "")


def answer_text(q):
    a = (q.get("choices") or {}).get(q.get("correct"), "")
    if isinstance(a, list):          # grid questions: a row of cells
        a = " ".join(str(x) for x in a)
    elif isinstance(a, dict):
        a = " ".join(str(x) for x in a.values())
    return str(a)


def snippet(stem):
    s = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", stem or "")).strip()
    if len(s) <= SNIP:
        return s
    return s[:SNIP].rsplit(" ", 1)[0].rstrip(",;:") + "…"


# base-45 varint: digits 0-44 as continuation chars C, the last digit as a terminal char T (both avoid " and \)
ALPHA = "".join(chr(c) for c in range(0x23, 0x7F) if chr(c) != "\\")   # 91 printable chars
T, C = ALPHA[:45], ALPHA[45:90]


def enc(nums):
    out, prev = [], -1
    for n in nums:
        d = n - prev - 1          # gaps start at 0
        prev = n
        digs = []
        while True:
            digs.append(d % 45)
            d //= 45
            if not d:
                break
        digs.reverse()
        out.append("".join(C[x] for x in digs[:-1]) + T[digs[-1]])
    return "".join(out)


def dec(s):
    """the reverse of enc (the hub's decoder is the same loop in JS) — used by the self-check below"""
    out, prev, v = [], -1, 0
    for ch in s:
        i = C.find(ch)
        if i >= 0:
            v = v * 45 + i
            continue
        v = v * 45 + T.index(ch)
        prev = prev + 1 + v
        out.append(prev)
        v = 0
    return out


def front_code(words):
    """words (sorted, or ids in order), each written as one capital letter (A + how many leading characters it shares with the word before,
    at most 25) and the rest of it: "pheochromocytoma" after "pheochromocytes" → "Noma" (words and ids have no capitals, so the
    capital marks where each word starts)"""
    out, prev = [], ""
    for w in words:
        k = 0
        while k < min(len(w), len(prev), 25) and w[k] == prev[k]:
            k += 1
        out.append(chr(65 + k) + w[k:])
        prev = w
    return "".join(out)


def unfront(s):
    out, prev = [], ""
    for m in re.finditer(r"[A-Z][^A-Z]*", s):
        w = prev[:ord(m.group(0)[0]) - 65] + m.group(0)[1:]
        out.append(w)
        prev = w
    return out


def blocks_in_hub():
    hub = (ROOT / "index.html").read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<a class="block-card[^"]*" href="([a-z0-9_-]+)/index\.html">\s*<div class="block-title">([^<]*)</div>', hub):
        b, title = m.group(1), m.group(2).strip()
        if b not in [x[0] for x in out] and (ROOT / b / "data.js").exists():
            out.append((b, SHORT.get(b, b.capitalize()), title))
    for b in re.findall(r'href="([a-z0-9_-]+)/index\.html"', hub):   # any other block link (no tile title)
        if b not in [x[0] for x in out] and (ROOT / b / "data.js").exists():
            out.append((b, SHORT.get(b, b.capitalize()), SHORT.get(b, b.capitalize()) + " block"))
    return out


def load_block(b):
    raw = (ROOT / b / "data.js").read_text(encoding="utf-8")
    data = json.loads(raw[raw.index("=") + 1:].strip().rstrip(";"))
    return raw, data


def build():
    blocks = blocks_in_hub()
    sdls, qs, src = [], [], {}
    texts = []      # (primary words, secondary words) per question
    for bi, (b, _, _) in enumerate(blocks):
        raw, data = load_block(b)
        src[b] = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
        for ex in data["exams"]:
            for sdl in ex["sdls"]:
                si = len(sdls)
                sdls.append([bi, sdl.get("sdlNumber"), sdl.get("title") or "", len(sdl["questions"])])
                for q in sdl["questions"]:
                    qs.append([si, q["id"], snippet(q.get("stem"))])
                    prim = set(norm(q.get("stem", "") + " " + answer_text(q)).split())
                    sec = set(norm(expl_lead(q.get("explanation", ""))).split()) - prim
                    texts.append((prim, sec))
    n = len(qs)
    df = {}
    for p, s in texts:
        for w in p | s:
            df[w] = df.get(w, 0) + 1
    drop = {w for w, c in df.items() if c > DROP_DF * n} | (STOP & set(df))
    P, S = {}, {}
    for i, (p, s) in enumerate(texts):
        for w in p:
            if w not in drop:
                P.setdefault(w, []).append(i)
        for w in s:
            if w not in drop:
                S.setdefault(w, []).append(i)
    words = sorted(set(P) | set(S))
    post = []
    for w in words:
        a, b2 = enc(P.get(w, [])), enc(S.get(w, []))
        post.append(a + ("!" + b2 if b2 else ""))
    # self-check: the encodings round-trip
    fc = front_code(words)
    assert unfront(fc) == words
    for w, x in list(zip(words, post))[::97]:
        a, _, b2 = x.partition("!")
        assert dec(a) == P.get(w, []) and dec(b2) == S.get(w, []), w
    out = {"v": 1, "n": n, "blocks": [list(x) for x in blocks], "src": src, "sdls": sdls,
           "ids": front_code([q[1] for q in qs]), "snip": [q[2] for q in qs],
           "words": fc, "post": " ".join(post), "stop": " ".join(sorted(drop))}
    assert unfront(out["ids"]) == [q[1] for q in qs]
    js = ("/* Built by tools/build-search.py — do not edit. The hub's question search index (stem + keyed answer + the "
          "explanation's first sentence of every question); run the builder after any data.js change. */\n"
          "window.QSEARCH=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
    return out, js


def main():
    out, js = build()
    OUT.write_text(js, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)}  —  {out['n']} questions in {len(out['blocks'])} blocks, "
          f"{len(out['post'].split(' '))} words ({len(js.encode('utf-8')) // 1024} KB)")


if __name__ == "__main__":
    sys.exit(main())
