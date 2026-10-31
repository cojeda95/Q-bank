#!/usr/bin/env python3
"""Build each block's split question files, <block>/q/ (m66) — the files the block page actually loads.

    python3 -I tools/build-split.py            # every block; also run at the end of tools/build-atlas.py
    python3 -I tools/build-split.py --check    # exit 1 (and say which) when any <block>/q/ is stale

<block>/data.js stays the one file every tool edits (qfix.py, build-atlas.py, build-search.py, the question pipeline).
This builder derives from it, so run it after ANY data.js change (tools/test-site.py fails while a block's q/ is stale):

  q/manifest.js   window.QUIZ_MANIFEST = { v: 1, src: first 10 hex of sha1(data.js), chunks: [file names],
                    exams: [{ examNumber, sdls: [{ sdlNumber, title, chunk: index into chunks (absent when the SDL has
                    no questions), objLabels: { objective: objectiveLabel } (m67, the hub's Weak spots),
                    questions: [{ id, batch, objective, isHighYield }] }] }] }
                  Everything the block home, the SDL lists, counts, progress and the exam / split / final builders need,
                  and nothing else (about 3-7 KB gzipped). Other exam and SDL fields are copied as they are.
  q/<part>.<hash>.js   the full questions, a few SDLs per file:
                  (window.QUIZ_CHUNKS = window.QUIZ_CHUNKS || {})["<file name>"] = { "<sdlNumber>": [question, …], … };
                  One exam per file, or an exam cut into SDL-aligned parts of about the same size when it is over
                  LIMIT bytes (neuro's Exam 4 → e4a, e4b, e4c). The name carries a hash of the content, so the service
                  worker can serve a saved copy of that name as is, and a changed SDL changes only its own file.

shared/app.js loads the manifest with the page, then the parts a screen needs, then the rest in the background (see
"Question data" there). Old part files left in q/ by an earlier build are deleted.
"""
import hashlib, json, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMIT = 450_000          # bytes of JSON per part file, at most (about 110 KB gzipped)
LIGHT = ("id", "batch", "objective", "isHighYield")   # per question, in the manifest
PART_RE = re.compile(r"^e\d+[a-z]?\.[0-9a-f]{10}\.js$")


def dumps(x):
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"))


def blocks():
    """every folder whose page runs shared/app.js on a data.js"""
    out = []
    for d in sorted(ROOT.iterdir()):
        page, data = d / "index.html", d / "data.js"
        if page.is_file() and data.is_file() and "shared/app.js" in page.read_text(encoding="utf-8"):
            out.append(d.name)
    return out


def load(block):
    raw = (ROOT / block / "data.js").read_bytes()
    s = raw.decode("utf-8")
    return raw, json.loads(s[s.index("=") + 1:].strip().rstrip(";"))


def cut(sizes, limit):
    """split a run of SDL sizes into k = ceil(total / limit) consecutive groups of about the same size"""
    total = sum(sizes)
    k = max(1, math.ceil(total / limit))
    groups, cur, acc, i = [], [], 0, 1
    for j, n in enumerate(sizes):
        # close the group when this SDL would end further past the i-th boundary than stopping here
        if cur and i < k and acc + n - i * total / k > i * total / k - acc:
            groups.append(cur); cur, i = [], i + 1
        cur.append(j); acc += n
    groups.append(cur)
    return groups


def plan(block):
    """-> {file name in q/: text} for one block"""
    raw, data = load(block)
    files, chunks, man_exams = {}, [], []
    for ex in data["exams"]:
        sdls = ex.get("sdls", [])
        bodies = [dumps(s.get("questions") or []) for s in sdls]
        with_q = [j for j, s in enumerate(sdls) if s.get("questions")]
        groups = cut([len(bodies[j]) for j in with_q], LIMIT) if with_q else []
        chunk_of = {}
        for gi, g in enumerate(groups):
            part = "e%s%s" % (ex["examNumber"], "abcdefghijklmnopqrstuvwxyz"[gi] if len(groups) > 1 else "")
            body = "{" + ",".join(dumps(str(sdls[with_q[x]]["sdlNumber"])) + ":" + bodies[with_q[x]] for x in g) + "}"
            name = "%s.%s.js" % (part, hashlib.sha1(body.encode("utf-8")).hexdigest()[:10])
            files[name] = ("/* Built by tools/build-split.py from data.js — do not edit. %s, SDLs %s */\n"
                           "(window.QUIZ_CHUNKS=window.QUIZ_CHUNKS||{})[%s]=%s;\n"
                           % (part, ", ".join(str(sdls[with_q[x]]["sdlNumber"]) for x in g), dumps(name), body))
            for x in g: chunk_of[with_q[x]] = len(chunks)
            chunks.append(name)
        m_sdls = []
        for j, s in enumerate(sdls):
            o = {k: v for k, v in s.items() if k != "questions"}
            if j in chunk_of: o["chunk"] = chunk_of[j]
            o["questions"] = [{k: q[k] for k in LIGHT if k in q} for q in s.get("questions") or []]
            # m67: each objective's label once per SDL, for the hub's "Weak spots" (it reads manifests, not data.js)
            labs = {}
            for q in s.get("questions") or []:
                if q.get("objective") is not None and q.get("objectiveLabel"): labs.setdefault(str(q["objective"]), q["objectiveLabel"])
            if labs: o["objLabels"] = labs
            m_sdls.append(o)
        e = {k: v for k, v in ex.items() if k != "sdls"}
        e["sdls"] = m_sdls
        man_exams.append(e)
    man = {"v": 1, "src": hashlib.sha1(raw).hexdigest()[:10], "chunks": chunks, "exams": man_exams}
    for k, v in data.items():
        if k != "exams": man[k] = v
    files["manifest.js"] = ("/* Built by tools/build-split.py from data.js — do not edit; run it after any data.js change. "
                            "Lists, counts and ids; the questions are in the files named in chunks. */\n"
                            "window.QUIZ_MANIFEST=" + dumps(man) + ";\n")
    return files


def stale(block, files):
    """what differs between q/ on disk and `files` (missing, changed, left over)"""
    d = ROOT / block / "q"
    have = {p.name for p in d.iterdir() if p.name == "manifest.js" or PART_RE.match(p.name)} if d.is_dir() else set()
    out = ["missing q/" + n for n in sorted(set(files) - have)]
    out += ["changed q/" + n for n in sorted(set(files) & have) if (d / n).read_text(encoding="utf-8") != files[n]]
    out += ["left over q/" + n for n in sorted(have - set(files))]
    return out


def main():
    check = "--check" in sys.argv[1:]
    bad = 0
    for b in blocks():
        files = plan(b)
        diff = stale(b, files)
        if check:
            if diff: bad += 1; print("%s: stale (%s) — run python3 -I tools/build-split.py" % (b, "; ".join(diff[:4])))
            continue
        d = ROOT / b / "q"
        d.mkdir(exist_ok=True)
        for n, text in files.items():
            p = d / n
            if not p.exists() or p.read_text(encoding="utf-8") != text: p.write_text(text, encoding="utf-8")
        for p in d.iterdir():
            if p.name not in files and PART_RE.match(p.name): p.unlink()
        parts = len(files) - 1
        print("built %s/q/  —  manifest %d KB + %d part%s (%s KB)%s" % (
            b, len(files["manifest.js"].encode()) // 1024, parts, "" if parts == 1 else "s",
            ", ".join(str(len(t.encode()) // 1024) for n, t in files.items() if n != "manifest.js"),
            "" if diff else ", unchanged"))
    if check:
        print("split files: %s" % ("all fresh" if not bad else "%d block(s) stale" % bad))
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
