#!/usr/bin/env python3
"""Regression test suite for the OCOM Question Hub (index.html, the 10 block pages, the Lesion Atlas, sw.js).

Usage (from the repo root; stdlib only + /Applications/Google Chrome.app, driven over the DevTools protocol by
tools/cdp_mini.py):

    python3 tools/test-site.py                 # everything (~1 min): data, hub, 10 blocks, all 370 maps, features, offline
    python3 tools/test-site.py --quick         # smoke subset (< 1 min): data, hub, 3 blocks, 12 maps, features, offline
    python3 tools/test-site.py --maps rtasim,core      # the atlas sweep on just these maps (other sections still run)
    python3 tools/test-site.py --only data,atlas       # sections: data, hub, blocks, atlas, features, offline
    python3 tools/test-site.py --shots [DIR]   # save screenshots (default $TMPDIR/qbank-test-shots)
    python3 tools/test-site.py --phone --dark  # phone viewport (390x844, touch) and/or dark colour scheme
    python3 tools/test-site.py --jobs 6 --headed -v

It serves the repo on a free local port (http.server in a thread), launches headless Chrome with a temp profile and checks:
  data      each <block>/data.js parses; every question has choices A-D or A-E, its correct letter among them and a non-empty
            explanation; ids unique per block; atlas-qlinks / atlas-qstates point at real cards, questions, moving maps,
            switches and options; resources/dyn/<map>.js exists for every moving map, matches its content hash and the
            page's switch list; the LES_BODY card-text file exists and matches its hash; sw.js CORE files exist
  hub       loads without console errors (favicon 404 ignored); New-in-the-atlas, Moving-map mix, systems, block links
  blocks    each block: exam list; one SDL practice answered right and wrong (explanation; "See it move" on the miss when
            atlas-qstates has a state for it); #sdlwrong, #examwrong and #spaced render; no console errors
  atlas     every map opens via #<id> and draws its SVG with no errors; every moving map loads its drawing, then every
            switch option (data-dyn="o:<sw>:<key>") and toggle is clicked: the state applies, the readouts row renders,
            no errors
  features  Name it and Predict on a moving map; #quiz/mix and #quiz/moving run a few items; a deep card link opens the
            full card once the card text loads; search; the note box saves (and survives a reload); print doesn't throw
  offline   the service worker registers and controls the page; with the network cut (server refuses + CDP offline) the
            hub and the atlas still render from the cache
  a11y      (inside hub / blocks / atlas, m56) no horizontal page scroll; every visible button, link and field has an
            accessible name; Tab gives the first controls a visible focus ring; question choices carry aria-pressed and the
            question a heading; the map <svg> is not role="img" (that hides its pins); --phone also flags controls under
            24 px (WARN). --dark now also saves the dark theme (the site's own toggle), so the pages really render dark
Exit status is 1 when any check FAILs (WARN does not fail the run). Chrome throttles more than 200 history/hash changes per
10 s in one tab, so the in-page helper paces itself (__T.budget) — that is the harness, not the site, being slow.
"""
import argparse, concurrent.futures as cf, functools, hashlib, http.server, json, os, re, socket, sys, tempfile, threading, time, traceback

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from cdp_mini import Browser, CDPError  # noqa: E402

# ─────────────────────────────────────────────────────────── results
RESULTS = []          # (section, check, status, detail, seconds)
RLOCK = threading.Lock()
VERBOSE = False


def record(section, check, ok, detail="", secs=0.0, warn=False):
    status = "PASS" if ok else ("WARN" if warn else "FAIL")
    with RLOCK:
        RESULTS.append((section, check, status, detail, secs))
        if VERBOSE or status != "PASS":
            print("  [%s] %-9s %s%s" % (status, section, check, (" — " + detail[:300]) if detail else ""), flush=True)


def fmt_errs(errs, n=3):
    errs = list(errs)
    return "; ".join(e[:220] for e in errs[:n]) + (" (+%d more)" % (len(errs) - n) if len(errs) > n else "")


# ─────────────────────────────────────────────────────────── local server
class Server:
    def __init__(self, root):
        self.offline = False
        srv = self

        class H(http.server.SimpleHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def __init__(self, *a, **k): super().__init__(*a, directory=root, **k)

            def log_message(self, *a): pass

            def handle_one_request(self):
                if srv.offline:      # "no signal": drop the connection without an answer
                    try: self.connection.shutdown(socket.SHUT_RDWR)
                    except Exception: pass
                    self.close_connection = True
                    return
                return super().handle_one_request()

            def end_headers(self):
                self.send_header("Cache-Control", "no-cache")
                super().end_headers()

        class S(http.server.ThreadingHTTPServer):
            request_queue_size = 512
            daemon_threads = True

        self.httpd = S(("127.0.0.1", 0), H)
        self.port = self.httpd.server_address[1]
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()
        self.base = "http://127.0.0.1:%d/" % self.port

    def close(self):
        self.httpd.shutdown()


# ─────────────────────────────────────────────────────────── data (no browser)
def js_json(path, start_marker=None):
    """Parse a built `window.X = {...};` file (or the JSON after start_marker)."""
    s = open(path, encoding="utf-8").read()
    if start_marker:
        i = s.index(start_marker) + len(start_marker)
    else:
        m = re.search(r"^\s*(?:/\*.*?\*/\s*)?(?:window\.)?[\w.\[\]\"()|{}=]+?\s*=\s*", s, re.S)
        i = m.end()
    body = s[i:].strip()
    if body.endswith(";"): body = body[:-1]
    return json.loads(body)


def block_dirs():
    out = []
    for d in sorted(os.listdir(ROOT)):
        if os.path.isfile(os.path.join(ROOT, d, "index.html")) and os.path.isfile(os.path.join(ROOT, d, "data.js")):
            out.append(d)
    # the hub's order (index.html #blocks) when it can be read
    try:
        hub = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
        order = re.findall(r'href="([\w-]+)/index\.html"', hub)
        out.sort(key=lambda d: order.index(d) if d in order else 99)
    except Exception:
        pass
    return out


def atlas_model():
    """Read MAPS ids, moving-map stubs, LES ids and LES_BODY from the built atlas page."""
    html = open(os.path.join(ROOT, "resources", "metabolic-atlas.html"), encoding="utf-8").read()
    ids = re.findall(r"^MAPS\.([A-Za-z0-9_]+) = \{", html, re.M)
    stubs = {}
    for m in re.finditer(r'^ dyn:(\{"lazy":)', html, re.M):
        start = m.start(1)
        # which map: the last MAPS.<id> = { before this point
        mid = re.findall(r"^MAPS\.([A-Za-z0-9_]+) = \{", html[:start][-400000:], re.M)[-1]
        stub, _ = json.JSONDecoder().raw_decode(html, start)
        stubs[mid] = stub
    les_line = re.search(r"^const LES = (\{.*\});$", html, re.M)
    les = json.loads(les_line.group(1)) if les_line else None
    lb = re.search(r'^const LES_BODY = "([^"]+)";', html, re.M)
    return {"html": html, "ids": ids, "stubs": stubs, "les": les, "les_body": lb.group(1) if lb else None}


def check_data(A):
    S = "data"
    blocks = block_dirs()
    record(S, "block folders found", len(blocks) >= 1, "%d: %s" % (len(blocks), ",".join(blocks)))
    BQ = {}      # block -> {qid: question}
    for b in blocks:
        t0 = time.time()
        try:
            d = js_json(os.path.join(ROOT, b, "data.js"), "window.QUIZ_DATA =")
        except Exception as e:
            record(S, b + "/data.js parses", False, str(e)[:200]); continue
        probs, ids, n = [], {}, 0
        for ex in d.get("exams", []):
            for sd in ex.get("sdls", []):
                for q in sd.get("questions", []):
                    n += 1
                    qid = q.get("id")
                    where = "%s (exam %s, SDL %s)" % (qid, ex.get("examNumber"), sd.get("sdlNumber"))
                    if not qid: probs.append("question without id in SDL %s" % sd.get("sdlNumber"))
                    elif qid in ids: probs.append("duplicate id " + where)
                    ids[qid] = q
                    ch = q.get("choices") or {}
                    if sorted(ch.keys()) not in (list("ABCD"), list("ABCDE")):   # 4-choice SDLs (pulm 32) are fine; the page draws only what exists
                        probs.append("choices %s not A-D/A-E: %s" % ("".join(sorted(ch.keys())), where))
                    if any((not v) or (isinstance(v, str) and not v.strip()) for v in ch.values()):
                        probs.append("empty choice text: " + where)
                    if q.get("correct") not in ch: probs.append("correct %r not among choices: %s" % (q.get("correct"), where))
                    if not str(q.get("explanation") or "").strip(): probs.append("empty explanation: " + where)
                    if not str(q.get("stem") or "").strip(): probs.append("empty stem: " + where)
        BQ[b] = ids
        # group repeated messages ("choices ABCD not A-E" x42) so the table stays readable
        grp = {}
        for p in probs:
            k = re.sub(r":.*", "", p); grp.setdefault(k, []).append(p)
        detail = "%d questions" % n if not probs else "; ".join(
            "%s ×%d (e.g. %s)" % (k, len(v), v[0].split(": ", 1)[-1]) if len(v) > 1 else v[0] for k, v in grp.items())
        record(S, b + "/data.js: questions well-formed", not probs, detail, time.time() - t0)

    les = A["les"] or {}
    record(S, "atlas: LES card list parses", bool(les), "%d cards" % len(les))
    record(S, "atlas: MAPS ids unique", len(A["ids"]) == len(set(A["ids"])), "%d maps" % len(A["ids"]))
    moving = A["stubs"]

    # dyn drawings
    probs = []
    dyn_dir = os.path.join(ROOT, "resources", "dyn")
    for mid, stub in moving.items():
        f = os.path.join(dyn_dir, mid + ".js")
        if not os.path.isfile(f): probs.append("missing dyn/%s.js" % mid); continue
        s = open(f, encoding="utf-8").read()
        m = re.search(r'\(window\.DYNDATA=window\.DYNDATA\|\|\{\}\)\[("[^"]+")\]=', s)
        if not m: probs.append("dyn/%s.js: unexpected format" % mid); continue
        body = s[m.end():].rstrip()
        if body.endswith(";"): body = body[:-1]
        if json.loads(m.group(1)) != mid: probs.append("dyn/%s.js registers %s" % (mid, m.group(1)))
        try: D = json.loads(body)
        except Exception as e: probs.append("dyn/%s.js does not parse: %s" % (mid, e)); continue
        if hashlib.sha1(body.encode("utf-8")).hexdigest()[:10] != stub.get("lazy"):
            probs.append("dyn/%s.js content hash != page's lazy %s (stale drawing?)" % (mid, stub.get("lazy")))
        if D.get("switches", []) != stub.get("switches", []):
            probs.append("dyn/%s.js switches differ from the page's stub" % mid)
    record(S, "dyn drawings: one per moving map, hash + switches match", not probs,
           ("%d moving maps" % len(moving)) if not probs else fmt_errs(probs, 6))
    orphans = sorted(set(x[:-3] for x in os.listdir(dyn_dir) if x.endswith(".js")) - set(moving)) if os.path.isdir(dyn_dir) else []
    record(S, "dyn drawings: no orphan files", not orphans, ",".join(orphans), warn=True)

    # LES_BODY
    lbn = A["les_body"]
    if lbn:
        f = os.path.join(ROOT, "resources", lbn)
        ok = os.path.isfile(f); det = lbn
        if ok:
            raw = open(f, "rb").read()
            if hashlib.sha1(raw).hexdigest()[:10] not in lbn: ok, det = False, lbn + ": content hash does not match its name"
            else:
                try:
                    B = js_json(f, "window.LESBODY=")
                    extra = [k for k in B if k not in les]
                    if extra: ok, det = False, "card text for unknown cards: " + ",".join(extra[:8])
                    else: det = "%s (%d cards)" % (lbn, len(B))
                except Exception as e: ok, det = False, "does not parse: %s" % e
        else: det = "missing resources/" + lbn
        record(S, "LES_BODY card text file", ok, det)
    else:
        record(S, "LES_BODY card text file", True, "LES_BODY null (card text inline)", warn=True)

    # qlinks
    probs = []
    try:
        QL = js_json(os.path.join(ROOT, "resources", "atlas-qlinks.js"), "window.ATLAS_QLINKS=")
        bl = [x[0] for x in QL["blocks"]]
        for b in bl:
            if b not in BQ: probs.append("unknown block " + b)
        for cid, rows in QL["cards"].items():
            if cid not in les: probs.append("unknown card " + cid)
            for bi, qids in rows:
                b = bl[bi] if 0 <= bi < len(bl) else None
                if b not in BQ: probs.append("card %s: bad block index %s" % (cid, bi)); continue
                for q in qids:
                    if q not in BQ[b]: probs.append("card %s: %s/%s not in data.js" % (cid, b, q))
        record(S, "atlas-qlinks: cards + questions exist", not probs,
               ("%d cards" % len(QL["cards"])) if not probs else "%d problems: %s" % (len(probs), fmt_errs(probs, 5)))
    except Exception as e:
        record(S, "atlas-qlinks: cards + questions exist", False, "parse: %s" % e)

    # answer-only link terms (m61): a q:["=…"] term counts only when it appears in a question's correct answer. Answers get
    # reworded (length parity, duplicate swaps), and then the term silently stops linking anything — list those (WARN)
    try:
        GREEK = {"α": " alpha ", "β": " beta ", "γ": " gamma ", "δ": " delta ", "κ": " kappa ", "ε": " epsilon ", "μ": " mu "}
        SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "01234567890123456789+-")
        def anorm(t):   # = atlas_norm in tools/build-atlas.py
            t = t.lower()
            for k, v in GREEK.items(): t = t.replace(k, v)
            t = t.translate(SUB); t = re.sub(r"<[^>]+>", " ", t); t = re.sub(r"['’‘`]", "", t)
            t = re.sub(r"[‐‑‒–—―\-/]", " ", t); t = re.sub(r"[^a-z0-9+ ]", " ", t)
            return re.sub(r"\s+", " ", t).strip()
        answers = []
        for b, qs in BQ.items():
            for q in qs.values():
                a = (q.get("choices") or {}).get(q.get("correct"))
                if isinstance(a, list): a = " / ".join(str(c) for c in a)
                answers.append(" " + anorm(str(a or "")) + " ")
        blob = "\n".join(answers)
        TT = js_json(os.path.join(ROOT, "resources", "atlas-terms.js"), "window.ATLAS_TERMS=")
        dead = [(c[0], t[1:]) for c in TT["cards"] for t in c[3] if t.startswith("=")
                and not any(f" {t[1:]}{s} " in blob for s in ("", "s", "es"))]
        nall = sum(1 for c in TT["cards"] for t in c[3] if t.startswith("="))
        record(S, "atlas-terms: every answer-only (=) term matches some correct answer", not dead,
               "%d answer-only terms" % nall if not dead else "%d of %d match no answer (reworded answers?): %s" % (
                   len(dead), nall, fmt_errs(["%s %r" % d for d in dead], 8)), warn=True)
    except Exception as e:
        record(S, "atlas-terms: every answer-only (=) term matches some correct answer", False, "parse: %s" % e, warn=True)

    # qstates
    probs, QS, n = [], None, 0
    try:
        QS = js_json(os.path.join(ROOT, "resources", "atlas-qstates.js"), "window.ATLAS_QSTATES=")
        bl = QS["blocks"]
        for bi, qmap in QS["q"].items():
            b = bl[int(bi)] if 0 <= int(bi) < len(bl) else None
            if b not in BQ: probs.append("bad block index %s" % bi); continue
            for qid, st in qmap.items():
                n += 1
                if qid not in BQ[b]: probs.append("%s/%s not in data.js" % (b, qid))
                mp, sw, opt = st
                if mp not in moving: probs.append("%s/%s → %s is not a moving map" % (b, qid, mp)); continue
                s = next((x for x in moving[mp].get("switches", []) if x.get("id") == sw), None)
                if not s: probs.append("%s/%s → %s has no switch %s" % (b, qid, mp, sw)); continue
                if opt not in [o[0] for o in s.get("options", [])]: probs.append("%s/%s → %s:%s has no option %s" % (b, qid, mp, sw, opt))
        record(S, "atlas-qstates: questions, maps, switches, options exist", not probs,
               ("%d states" % n) if not probs else "%d problems: %s" % (len(probs), fmt_errs(probs, 5)))
    except Exception as e:
        record(S, "atlas-qstates: questions, maps, switches, options exist", False, "parse: %s" % e)

    # other built resources parse
    for name, marker in (("atlas-practice.js", "window.ATLAS_PRACTICE="), ("atlas-home.js", "window.ATLAS_HOME="),
                         ("qbank-counts.js", "window.QBANK_COUNTS=")):
        try:
            js_json(os.path.join(ROOT, "resources", name), marker); record(S, "resources/%s parses" % name, True)
        except Exception as e:
            record(S, "resources/%s parses" % name, False, str(e)[:200])

    # sw.js CORE
    try:
        sw = open(os.path.join(ROOT, "sw.js"), encoding="utf-8").read()
        core = re.findall(r"'([^']+)'", re.search(r"const CORE = \[(.*?)\];", sw, re.S).group(1))
        miss = [c for c in core if c != "./" and not os.path.isfile(os.path.join(ROOT, c))]
        record(S, "sw.js CORE files exist", not miss, ("%d files" % len(core)) if not miss else ",".join(miss))
    except Exception as e:
        record(S, "sw.js CORE files exist", False, str(e))
    return BQ, QS


# ─────────────────────────────────────────────────────────── in-page helper
INIT_JS = r"""
(() => {
  const T = window.__navT = [];
  const wrap = f => function () { T.push(performance.now()); return f.apply(this, arguments); };
  try { history.replaceState = wrap(history.replaceState); history.pushState = wrap(history.pushState); } catch (e) {}
  const E = window.__errs = [];
  addEventListener('error', e => { if (e && e.message) E.push('error: ' + e.message + ' @' + (e.filename || '') + ':' + (e.lineno || '')); });
  addEventListener('unhandledrejection', e => E.push('unhandled rejection: ' + (e.reason && (e.reason.stack || e.reason.message) || e.reason)));
  const ce = console.error.bind(console);
  console.error = function () { try { E.push('console.error: ' + [...arguments].map(a => a && a.stack || String(a)).join(' ')); } catch (e) {} return ce.apply(console, arguments); };
  window.__printed = 0; window.print = () => { window.__printed++; };
  window.open = () => null;           // "Quiz me" and links that open new tabs: not under test here
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const frame = () => new Promise(r => requestAnimationFrame(() => setTimeout(r, 0)));
  window.__T = {
    sleep, frame,
    takeErrs() { return E.splice(0); },
    async budget(max) { max = max || 150;      // Chrome: <= 200 history changes / 10 s per tab
      for (;;) { const now = performance.now(); while (T.length && T[0] < now - 10500) T.shift();
        if (T.length < max) return T.length; await sleep(100); } },
    async until(fn, ms) { const t0 = performance.now();
      while (performance.now() - t0 < (ms || 8000)) { try { const v = fn(); if (v) return v; } catch (e) {} await sleep(25); }
      try { return fn(); } catch (e) { return null; } },
    click(sel) { const el = typeof sel === 'string' ? document.querySelector(sel) : sel; if (!el) return false;
      el.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, view: window })); return true; },
    q(sel) { return document.querySelector(sel); },
    dynChip(key) { return document.querySelector('[data-dyn="' + key.replace(/"/g, '\\"') + '"]'); },
    readoutsShown() { return document.querySelectorAll('.dyn-ro, .ds-r').length; },
    // a11y (m56): page overflow, unnamed controls, tiny tap targets (phone) — visible elements only
    a11y(scope) {
      const root = scope ? document.querySelector(scope) || document.body : document.body, W = innerWidth;
      const vis = e => { if (!e.getClientRects().length) return false; for (let x = e; x && x.nodeType === 1; x = x.parentElement) {
        const c = getComputedStyle(x); if (c.display === 'none' || c.visibility === 'hidden' || +c.opacity === 0 || x.hidden) return false;
        if (x.getAttribute('aria-hidden') === 'true') return false; } return true; };
      const nm = e => (e.getAttribute('aria-label') || '').trim() || (e.getAttribute('aria-labelledby') && (document.getElementById(e.getAttribute('aria-labelledby')) || {}).textContent || '').trim()
        || (e.labels && [...e.labels].map(l => l.textContent).join('').trim()) || (e.innerText || e.textContent || '').trim() || (e.title || '').trim() || (e.placeholder || '').trim()
        || (e.querySelector && ((e.querySelector('img[alt]') || {}).alt || '')).trim();
      const els = [...root.querySelectorAll('a[href],button,input:not([type=hidden]),select,textarea,[role=button],[role=tab],[role=menuitemradio]')].filter(vis);
      const sig = e => e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + ((e.getAttribute('class') || '').trim() ? '.' + e.getAttribute('class').trim().split(/\s+/)[0] : '');
      const tiny = els.filter(e => { if (e.closest('svg')) return false; const r = e.getBoundingClientRect(); const inl = e.tagName === 'A' && getComputedStyle(e).display === 'inline';
        return !inl && r.width > 0 && (r.width < 24 || r.height < 24); }).map(sig);
      return { docW: Math.max(document.documentElement.scrollWidth, document.body.scrollWidth), W,
               unnamed: [...new Set(els.filter(e => !nm(e)).map(sig))].slice(0, 8), tiny: [...new Set(tiny)].slice(0, 8) };
    },
  };
})();
"""

ATLAS_OPEN_JS = r"""
(async (v) => {
  await __T.budget(); __navT.push(performance.now());
  const t0 = performance.now(), kit = MAPS[v].art === 'kit';
  location.hash = v;
  const ok = await __T.until(() => state.view === v && (!kit || (window.DYNDATA && DYNDATA[v] && MAPS[v].dyn && !MAPS[v].dyn.lazy) || DYNFAIL[v]), 10000);
  await __T.frame();
  const d = kit ? MAPS[v].dyn : null;
  return { view: state.view, ok: !!ok, kit, ms: Math.round(performance.now() - t0), n: svg.querySelectorAll('*').length,
           fail: kit ? !!DYNFAIL[v] : false, lazy: kit ? !!(d && d.lazy) : false, readouts: d ? (d.readouts || []).length : 0,
           shown: __T.readoutsShown(), errs: __T.takeErrs() };
})(%s)
"""

ATLAS_SWITCHES_JS = r"""
(async (v) => {
  const d = MAPS[v].dyn, out = [], sws = d.switches || []; let clicks = 0;
  const want = (d.readouts || []).length;
  const tryKey = async (key, check) => {
    await __T.budget();
    const el = __T.dynChip(key);
    if (!el) { out.push([key, 'chip not on the page']); return; }
    __T.click(el); __navT.push(performance.now()); clicks++;
    await __T.frame();
    const e = __T.takeErrs(); if (e.length) out.push([key, 'errors: ' + e.slice(0, 2).join(' | ')]);
    const c = check(); if (c) out.push([key, c]);
    if (want && !__T.readoutsShown()) out.push([key, 'readouts row missing (' + want + ' readouts)']);
  };
  for (const s of sws) {
    if (!s.type || s.type === 'toggle') {
      const before = !!DYN[v].sw[s.id];
      await tryKey('t:' + s.id, () => !!DYN[v].sw[s.id] === before ? 'toggle did not flip' : '');
      await tryKey('t:' + s.id, () => !!DYN[v].sw[s.id] !== before ? 'toggle did not flip back' : '');
    } else {
      for (const o of s.options || []) {
        // a "one" switch: tapping the option that is already on (its default) turns it off; "steps" always selects
        const want = s.type === 'one' && DYN[v].sw[s.id] === o[0] ? '' : o[0];
        await tryKey('o:' + s.id + ':' + o[0], () => DYN[v].sw[s.id] !== want ? 'state is ' + JSON.stringify(DYN[v].sw[s.id]) + ', expected ' + JSON.stringify(want) : '');
      }
    }
  }
  return { clicks, problems: out };
})(%s)
"""


def add_init(p):
    p.cmd("Page.addScriptToEvaluateOnNewDocument", source=INIT_JS)


# ─────────────────────────────────────────────────────────── browser sections
class Ctx:
    def __init__(self, args, server, browser):
        self.args, self.server, self.browser = args, server, browser
        self.shots = args.shots

    def page(self):
        a = self.args
        w, h = (390, 844) if a.phone else (1366, 900)
        p = self.browser.page(w=w, h=h, mobile=a.phone, dark=a.dark)
        add_init(p)
        if a.dark:   # the site's own ◐ choice ('mla-theme'): prefers-color-scheme alone leaves the hub and the blocks light
            p.cmd("Page.addScriptToEvaluateOnNewDocument", source="try{localStorage.setItem('mla-theme','dark')}catch(e){}")
        return p

    def shot(self, p, name):
        if not self.shots: return
        try: p.shot(os.path.join(self.shots, re.sub(r"[^\w.-]+", "_", name) + ".png"))
        except Exception: pass


def test_hub(C):
    S, t0 = "hub", time.time()
    p = C.page()
    try:
        p.goto(C.server.base + "index.html")
        r = p.wait("""(()=>{ const s=document.querySelectorAll('#systems .sys').length; if(!s) return null;
          const tn=document.getElementById('tileNew'), tm=document.getElementById('tileMoving');
          return {sys:s, newHidden:tn?tn.hidden:null, newCount:(document.getElementById('newCount')||{}).textContent||'',
            moving:!!tm, movingStat:(document.getElementById('movingStat')||{}).textContent||'', movingHref:tm?tm.getAttribute('href'):'',
            blocks:[...document.querySelectorAll('#blocks a')].map(a=>a.getAttribute('href')).filter(h=>/\\/index\\.html$/.test(h||'')),
            lede:(document.getElementById('heroLede')||{}).textContent||''}; })()""", timeout=15)
        time.sleep(0.8)
        record(S, "loads, systems render", r["sys"] >= 5, "%d systems · %s" % (r["sys"], r["lede"][:80]), time.time() - t0)
        record(S, "New-in-the-atlas tile", r["newHidden"] is False and bool(r["newCount"].strip()), r["newCount"])
        record(S, "Moving-map mix tile", r["moving"] and "quiz/moving" in r["movingHref"] and bool(re.search(r"\d+ moving maps", r["movingStat"])),
               r["movingStat"][:100])
        exp = block_dirs()
        got = sorted(set(h.split("/")[0] for h in r["blocks"]))
        record(S, "block links", set(exp) <= set(got), "%d linked" % len(got) + ("" if set(exp) <= set(got) else "; missing " + ",".join(sorted(set(exp) - set(got)))))
        C.shot(p, "hub")
        a11y_checks(C, p, "hub", "hub")
        errs = p.take_errors()
        record(S, "no console errors", not errs, fmt_errs(errs))
    except Exception as e:
        record(S, "hub run", False, "%s" % e)
    finally:
        p.close()


def a11y_checks(C, p, S, label, ring=True):
    """m56: no sideways scroll, every control named, a visible focus ring on the first Tab stops; on --phone tiny targets WARN."""
    try:
        a = p.js("__T.a11y()")
        record(S, "a11y %s: no sideways scroll" % label, a["docW"] <= a["W"] + 1, "%d px wide at %d" % (a["docW"], a["W"]))
        record(S, "a11y %s: every control has a name" % label, not a["unnamed"], ", ".join(a["unnamed"]))
        if C.args.phone and a["tiny"]:
            record(S, "a11y %s: tap targets >= 24 px" % label, False, ", ".join(a["tiny"]), warn=True)
        if ring:
            p.js("document.activeElement && document.activeElement.blur && document.activeElement.blur()")
            bad = []
            for _ in range(6):
                p.cmd("Input.dispatchKeyEvent", type="keyDown", key="Tab", code="Tab", windowsVirtualKeyCode=9)
                p.cmd("Input.dispatchKeyEvent", type="keyUp", key="Tab", code="Tab", windowsVirtualKeyCode=9)
                r = p.js("""(()=>{ const e=document.activeElement; if(!e||e===document.body) return null; const c=getComputedStyle(e);
                  return {s:e.tagName.toLowerCase()+(e.id?'#'+e.id:''), ok:(c.outlineStyle!=='none'&&parseFloat(c.outlineWidth)>0)||c.boxShadow!=='none'}; })()""")
                if r and not r["ok"]: bad.append(r["s"])
            record(S, "a11y %s: Tab shows a focus ring" % label, not bad, ", ".join(bad))
    except Exception as e:
        record(S, "a11y %s" % label, False, "%s" % e)


def pick_targets(block, BQ, QS):
    """An SDL to practice in: prefer one holding a question with a See-it-move state."""
    bi = QS["blocks"].index(block) if QS and block in QS.get("blocks", []) else -1
    states = (QS or {}).get("q", {}).get(str(bi), {}) if bi >= 0 else {}
    return list(states.keys())


def test_block(C, block, BQ, QS):
    S, t0 = "block:" + block, time.time()
    p = C.page()
    stepname = "load"
    try:
        p.goto(C.server.base + block + "/index.html")
        r = p.wait("""(()=>{ if(typeof DATA==='undefined'||!DATA) return null; const n=document.querySelectorAll('.exam-card').length;
          return n?{cards:n, exams:DATA.exams.length, withQ:DATA.exams.filter(e=>e.sdls.some(s=>s.questions.length)).length}:null; })()""", timeout=20)
        record(S, "exam list renders", r["cards"] >= max(1, r["withQ"]), "%d exam cards (%d exams, %d with questions)" % (r["cards"], r["exams"], r["withQ"]))
        errs = p.take_errors(); record(S, "home: no console errors", not errs, fmt_errs(errs))
        a11y_checks(C, p, S, "home")

        # the page's own card links (shared/app.js atlasLinksFor) agree with the built atlas-qlinks.js (build-atlas.py)
        stepname = "links"
        QL = js_json(os.path.join(ROOT, "resources", "atlas-qlinks.js"), "window.ATLAS_QLINKS=")
        bi = [b[0] for b in QL["blocks"]].index(block) if block in [b[0] for b in QL["blocks"]] else -1
        exp = {}
        for cid, v in QL["cards"].items():
            for b, ids in v:
                if b == bi:
                    for q in ids: exp.setdefault(q, []).append(cid)
        p.wait("typeof ATLAS_INDEX!=='undefined' && ATLAS_INDEX && ATLAS_INDEX.length", timeout=20)
        got = p.js("""(()=>{ const o={}; for(const e of DATA.exams) for(const s of e.sdls) for(const q of s.questions){
            const c=atlasLinksFor(q).map(c=>c.id); if(c.length) o[q.id]=c; } return o; })()""")
        bad = sorted(q for q in set(exp) | set(got) if sorted(exp.get(q, [])) != sorted(got.get(q, [])))
        record(S, "card links: page = build", not bad, "%d questions linked" % len(got) if not bad else
               "%d differ, e.g. %s" % (len(bad), "; ".join("%s page %s build %s" % (q, got.get(q), exp.get(q)) for q in bad[:3])))

        # SDL to practice: one holding a question with a state (See it move), else the first with questions
        state_ids = pick_targets(block, BQ, QS)
        pick = p.js("""((ids)=>{ const set=new Set(ids);
          for(const e of DATA.exams) for(const s of e.sdls){ const q=s.questions.find(q=>set.has(q.id)&&!q.batch||set.has(q.id)&&q.batch<=2);
            if(q) return {sdl:s.sdlNumber, exam:e.examNumber, target:q.id}; }
          for(const e of DATA.exams) for(const s of e.sdls) if(s.questions.length) return {sdl:s.sdlNumber, exam:e.examNumber, target:null};
          return null; })(%s)""" % json.dumps(state_ids))
        if not pick:
            record(S, "practice", False, "no SDL with questions"); return
        sdl, exam, target = pick["sdl"], pick["exam"], pick["target"]

        stepname = "practice"
        p.js("location.hash='practice/%d/all'" % sdl)
        p.wait("typeof session!=='undefined' && session && session.mode==='practice' && document.querySelectorAll('.choice[data-letter]').length", timeout=15)
        info = p.js("""(()=>{ const t=%s; const i=t?session.questions.findIndex(q=>q.id===t):-1;
            return {n:session.questions.length, ti:i, first:session.questions[0].id}; })()""" % json.dumps(target))
        # right answer on a question that isn't the target
        right_i = 0 if info["ti"] != 0 else (1 if info["n"] > 1 else 0)
        wrong_i = info["ti"] if info["ti"] >= 0 else (1 if info["n"] > 1 else 0)

        ANSWER = """(async (idx, right) => {
          if (session.index !== idx) { session.index = idx; session.pendingLetter = null; renderPracticeQuestion(); }
          const q = session.questions[idx];
          const letter = right ? q.correct : ['A','B','C','D','E'].find(l => l !== q.correct && q.choices[l]);
          if (!__T.click('.choice[data-letter="' + letter + '"]')) return {err: 'choice ' + letter + ' not clickable'};
          const conf = await __T.until(() => document.getElementById('confConfident'), 3000);
          if (!conf) return {err: 'confidence prompt missing'};
          __T.click(conf);
          const fb = await __T.until(() => document.querySelector('.feedback-banner'), 3000);
          const ex = document.querySelector('.info-block.explanation');
          return {id: q.id, banner: fb ? fb.className : '', bannerText: fb ? fb.textContent.trim() : '',
                  expl: ex ? ex.textContent.replace(/^Explanation/, '').trim().length : 0,
                  rendered: [...document.querySelectorAll('.choice[data-letter]')].map(b => b.dataset.letter + ':' + b.textContent.replace(/^\\s*[A-E]/, '').trim().length)};
        })(%d, %s)"""
        a = p.js(ANSWER % (right_i, "true"), timeout=30)
        ok = not a.get("err") and "correct" in a["banner"].split() and a["expl"] > 0
        record(S, "SDL %d: right answer + explanation" % sdl, ok, a.get("err") or "%s · %s · explanation %d chars" % (a["id"], a["bannerText"][:30], a["expl"]))
        a2 = p.js(ANSWER % (wrong_i, "false"), timeout=30)
        ok = not a2.get("err") and "incorrect" in a2["banner"].split() and a2["expl"] > 0
        record(S, "SDL %d: wrong answer + explanation" % sdl, ok, a2.get("err") or "%s · %s" % (a2["id"], a2["bannerText"][:50]))
        empty = [x for x in (a2.get("rendered") or []) if x.endswith(":0")]
        record(S, "SDL %d: no blank choice buttons" % sdl, not empty, ",".join(empty))
        if target and a2.get("id") == target:
            st = QS["q"][str(QS["blocks"].index(block))][target]
            try:
                href = p.wait("""(()=>{ const a=document.querySelector('.atlas-move-cta.has-state'); return a&&a.getAttribute('href'); })()""", timeout=12)
                want = "#%s/~%s:%s" % (st[0], st[1], st[2])
                record(S, "See it move on the miss", want in href, href[-80:])
            except CDPError as e:
                have = p.js("(()=>{const a=document.querySelector('.atlas-move-cta');return a?a.outerHTML.slice(0,200):(document.querySelector('.amc-slot')?'empty .amc-slot':'no .amc-slot')})()")
                record(S, "See it move on the miss", False, "no state CTA for %s → %s after 12 s (%s)" % (target, st, have))
        else:
            record(S, "See it move on the miss", True, "no question with a state in this block — skipped", warn=not state_ids)
        C.shot(p, "%s-practice-miss" % block)
        q11 = p.js("""(()=>{ const c=[...document.querySelectorAll('.choice[data-letter]')]; return {h:!!document.querySelector('.a11y-qh'),
          live:!!document.getElementById('a11yLive'), st:document.querySelectorAll('.a11y-st').length,
          pressed:c.filter(b=>!b.disabled).every(b=>b.hasAttribute('aria-pressed'))}; })()""")
        record(S, "a11y: question heading, live region, answer status for screen readers", q11["h"] and q11["live"] and q11["st"] >= 1 and q11["pressed"], json.dumps(q11))
        a11y_checks(C, p, S, "practice", ring=False)
        errs = p.take_errors(); record(S, "practice: no console errors", not errs, fmt_errs(errs))

        for route, sel, need in (("sdlwrong/%d" % sdl, ".info-block.explanation", 1), ("examwrong/%d" % exam, ".info-block.explanation", 1),
                                 ("spaced", "h1, h2", 1)):
            stepname = route
            p.js("location.hash=%s" % json.dumps(route))
            try:
                n = p.wait("""(()=>{ if(!main||!main.innerHTML||main.querySelector('.loading')) return 0; const n=main.querySelectorAll(%s).length; return n>=%d?n:0; })()""" % (json.dumps(sel), need), timeout=12)
                head = p.js("(()=>{const h=main.querySelector('h1,h2,.subtitle');return h?h.textContent.trim().slice(0,70):''})()")
                time.sleep(0.3)
                errs = p.take_errors()
                record(S, "#%s renders" % route, not errs, ("%d × %s · %s" % (n, sel, head)) if not errs else fmt_errs(errs))
            except CDPError as e:
                txt = p.js("main.innerText.slice(0,160)")
                record(S, "#%s renders" % route, False, "expected %s: %s" % (sel, txt.replace("\n", " ")))
            C.shot(p, "%s-%s" % (block, route.replace("/", "-")))
            a11y_checks(C, p, S, "#" + route, ring=False)
    except Exception as e:
        record(S, "run (%s)" % stepname, False, "%s" % e)
        if VERBOSE: traceback.print_exc()
    finally:
        p.close()
    record(S, "total", True, "", time.time() - t0)


def atlas_page(C, hash_=""):
    p = C.page()
    p.goto(C.server.base + "resources/metabolic-atlas.html" + (("#" + hash_) if hash_ else ""))
    p.wait("typeof MAPS==='object' && typeof state==='object' && typeof __T==='object' && booted", timeout=30)
    return p


def test_map_chunk(C, ids, label):
    """Open each map in `ids` in one atlas tab; for moving maps click every switch option."""
    S = "atlas"
    p = atlas_page(C)
    stats = {"maps": 0, "moving": 0, "clicks": 0}
    try:
        time.sleep(0.3); p.take_errors(); p.js("__T.takeErrs()")
        for v in ids:
            t0 = time.time()
            try:
                r = p.js(ATLAS_OPEN_JS % json.dumps(v), timeout=40)
            except CDPError as e:
                record(S, "map " + v, False, "open: %s" % e); continue
            stats["maps"] += 1
            probs = []
            if r["view"] != v: probs.append("did not open (state.view=%s)" % r["view"])
            elif not r["ok"] and not r["fail"]: probs.append("drawing still loading after 10 s")
            if r["n"] < 40: probs.append("SVG nearly empty (%d elements)" % r["n"])
            if r["kit"]:
                stats["moving"] += 1
                if r["fail"] or r["lazy"]: probs.append("drawing did not load (dyn/%s.js)" % v)
                elif r["readouts"] and not r["shown"]: probs.append("readouts row missing on open")
            if r["errs"]: probs.append("errors: " + fmt_errs(r["errs"], 2))
            if r["kit"] and not (r["fail"] or r["lazy"]):
                try:
                    s = p.js(ATLAS_SWITCHES_JS % json.dumps(v), timeout=300)
                    stats["clicks"] += s["clicks"]
                    for key, why in s["problems"][:6]: probs.append("%s: %s" % (key, why))
                    if len(s["problems"]) > 6: probs.append("+%d more switch problems" % (len(s["problems"]) - 6))
                except CDPError as e:
                    probs.append("switch sweep: %s" % e)
            cerr = p.take_errors()
            if cerr: probs.append("console: " + fmt_errs(cerr, 2))
            if C.shots: C.shot(p, "map-" + v)
            try:
                a = p.js("__T.a11y()")
                if a["docW"] > a["W"] + 1: probs.append("a11y: page scrolls sideways (%d px wide at %d)" % (a["docW"], a["W"]))
                if a["unnamed"]: probs.append("a11y: controls without a name: " + ", ".join(a["unnamed"][:4]))
            except CDPError as e:
                probs.append("a11y: %s" % e)
            if probs or VERBOSE:
                record(S, "map " + v, not probs, "; ".join(probs) if probs else "%d svg els%s" % (r["n"], " · moving" if r["kit"] else ""), time.time() - t0)
    finally:
        p.close()
    return stats


def balanced_chunks(ids, moving, n):
    """Split maps into n chunks of similar cost (a moving map costs ~ its option count)."""
    cost = {v: (3 + sum(len(s.get("options", [])) or 2 for s in moving[v].get("switches", []))) if v in moving else 1 for v in ids}
    chunks = [[] for _ in range(n)]; load = [0] * n
    for v in sorted(ids, key=lambda v: -cost[v]):
        i = load.index(min(load)); chunks[i].append(v); load[i] += cost[v]
    return [c for c in chunks if c]


def test_features(C, A):
    S = "features"
    moving = A["stubs"]
    # a moving map with a quizzable "one" switch (>= 3 options) and readouts — aasim when present
    pick = "aasim" if "aasim" in moving else next(v for v, s in moving.items() if any(x.get("type") == "one" and len(x.get("options", [])) >= 3 for x in s.get("switches", [])))
    p = atlas_page(C, pick)
    try:
        p.wait("window.DYNDATA&&DYNDATA[%s]&&!MAPS[%s].dyn.lazy&&state.view===%s" % ((json.dumps(pick),) * 3), timeout=15)
        p.take_errors()
        # ── Name it
        t0 = time.time()
        r = p.js("""(async v => {
          await __T.budget(); if (!__T.click(__T.dynChip('quiz:new'))) return {err: 'no Name it chip (quiz:new)'};
          const qz = await __T.until(() => DYN[v].quiz, 3000); if (!qz) return {err: 'no question after Name it'};
          const chips = [...document.querySelectorAll('[data-dyn^="q:"]')].map(e => e.dataset.dyn);
          if (!chips.includes('q:' + qz.k)) return {err: 'answer chip missing', chips};
          __T.click(__T.dynChip('q:' + qz.k)); await __T.frame();
          return {k: qz.k, chips: chips.length, ans: DYN[v].quiz && DYN[v].quiz.ans, n: DYN[v].qz && DYN[v].qz.n, ok: DYN[v].qz && DYN[v].qz.ok};
        })(%s)""" % json.dumps(pick))
        errs = p.take_errors()
        record(S, "Name it on %s" % pick, not r.get("err") and r.get("ans") == r.get("k") and r.get("ok") == 1 and not errs,
               r.get("err") or ("%d choices, named %s right" % (r["chips"], r["k"]) if not errs else fmt_errs(errs)), time.time() - t0)
        p.js("__T.click(__T.dynChip('quiz:end'))||__T.click(__T.dynChip('reset'))")
        # ── Predict
        t0 = time.time()
        r = p.js("""(async v => {
          const d = MAPS[v].dyn; if (!(d.readouts||[]).length) return {err: 'map has no readouts'};
          // a state that moves at least one readout
          let key = null;
          for (const s of d.switches || []) for (const o of (s.options || [])) {
            const st = {on: {}, sw: {}}; (d.switches||[]).forEach(x => st.sw[x.id] = x.type === 'one' ? '' : x.type === 'steps' ? x.options[0][0] : x.def !== false);
            st.sw[s.id] = o[0]; if (!key && dynReadouts(d, st).some(r => r.dir)) key = 'o:' + s.id + ':' + o[0]; }
          if (!key) return {err: 'no state moves a readout'};
          await __T.budget(); __T.click(__T.dynChip(key)); await __T.frame();
          if (!__T.click(__T.dynChip('p:on'))) return {err: 'no Predict chip (p:on)'};
          await __T.frame(); if (!DYN[v].pred) return {err: 'predict did not start'};
          const g = document.querySelector('[data-dyn^="p:g:"]'); if (!g) return {err: 'no guess chips'};
          __T.click(g); await __T.frame();
          if (!__T.click(__T.dynChip('p:chk'))) return {err: 'no Check chip'};
          await __T.frame();
          return {key, chk: !!(DYN[v].pred && DYN[v].pred.chk), marks: document.querySelectorAll('.ds-ok,.ds-bad,.dyn-ok,.dyn-bad,[class*="dyn-ok"],[class*="dyn-bad"]').length};
        })(%s)""" % json.dumps(pick))
        errs = p.take_errors()
        record(S, "Predict on %s" % pick, not r.get("err") and r.get("chk") and not errs,
               r.get("err") or ("%s → checked" % r["key"] if not errs else fmt_errs(errs)), time.time() - t0)

        # ── print
        t0 = time.time()
        r = p.js("""(async () => { __T.takeErrs(); const b = document.getElementById('zprint'); if (!b) return {err: 'no Print button'};
          __T.click(b); await __T.sleep(250);
          const ps = document.getElementById('printsheet');
          const res = {printed: window.__printed, svg: !!(ps && ps.querySelector('.ps-map svg')), cards: ps ? ps.querySelectorAll('.ps-card').length : 0, errs: __T.takeErrs()};
          dispatchEvent(new Event('afterprint')); return res; })()""")
        errs = p.take_errors() + (r.get("errs") or [])
        record(S, "print a map", not r.get("err") and r.get("printed") == 1 and r.get("svg") and not errs,
               r.get("err") or ("print sheet: map + %d cards" % r["cards"] if not errs else fmt_errs(errs)), time.time() - t0)

        # ── search
        t0 = time.time()
        bad = []
        for q in ("hemophilia", "PKU", "nephrotic", "insulin", "asthma", "lithium"):
            n = p.js("""(async q => { const el = document.getElementById('q'); el.value = q; el.dispatchEvent(new Event('input', {bubbles: true}));
              await __T.until(() => /SEARCH RESULTS\\s*·\\s*\\d+/i.test(document.getElementById('rail').innerText), 3000);
              const m = document.getElementById('rail').innerText.match(/SEARCH RESULTS\\s*·\\s*(\\d+)/i); return m ? +m[1] : 0; })(%s)""" % json.dumps(q))
            if not n: bad.append(q)
            else: bad_n = n
        p.js("(()=>{const el=document.getElementById('q'); el.value=''; el.dispatchEvent(new Event('input',{bubbles:true}));})()")
        errs = p.take_errors()
        record(S, "search returns results", not bad and not errs, ("no results for: " + ",".join(bad)) if bad else fmt_errs(errs), time.time() - t0)

        # ── notes
        t0 = time.time()
        card = p.js("""(()=>{ const ids = Object.keys(LES).filter(id => (LOC[id]||[]).length); return ids.includes('vongierke') ? 'vongierke' : ids[0]; })()""")
        text = "test note %d" % int(time.time())
        r = p.js("""(async (id, text) => {
          await __T.budget(); location.hash = id;
          if (!await __T.until(() => state.sel === id && !drawer.hidden && drawer.querySelector('.mynote') && !drawer.querySelector('.lesload'), 10000)) return {err: 'card did not open'};
          const add = drawer.querySelector('[data-noteadd]'); if (add) __T.click(add);
          const ta = await __T.until(() => document.getElementById('mynoteTa'), 2000); if (!ta) return {err: 'no note textarea'};
          ta.value = text; ta.dispatchEvent(new Event('input', {bubbles: true}));
          const saved = await __T.until(() => (drawer.querySelector('.mynote-s') || {}).textContent === 'Saved', 4000);
          let ls = ''; try { ls = localStorage.getItem('mla-notes') || ''; } catch (e) {}
          return {saved: !!saved, prog: (PROG.note[id] || {}).text, ls: ls.includes(text)};
        })(%s, %s)""" % (json.dumps(card), json.dumps(text)), timeout=30)
        ok = not r.get("err") and r.get("saved") and r.get("prog") == text and r.get("ls")
        if ok:   # and it is there after a reload
            p.reload()
            p.wait("typeof __T==='object' && typeof state==='object' && booted", timeout=30)
            back = p.js("""(async (id) => { await __T.until(() => state.sel === id && !drawer.hidden && !drawer.querySelector('.lesload'), 10000);
              const ta = document.getElementById('mynoteTa'); return ta ? ta.value : null; })(%s)""" % json.dumps(card))
            ok = back == text
            if not ok: r["err"] = "after reload the note box shows %r" % back
        errs = p.take_errors()
        record(S, "note box saves (and survives reload)", ok and not errs, r.get("err") or ("card %s" % card if not errs else fmt_errs(errs)), time.time() - t0)
    except Exception as e:
        record(S, "run", False, "%s" % e)
        if VERBOSE: traceback.print_exc()
    finally:
        p.close()

    # ── deep card link on a fresh page: the full card once the card text loads
    t0 = time.time()
    p = C.page()
    try:
        les = A["les"] or {}
        card = "vongierke" if "vongierke" in les else next(iter(les))
        p.goto(C.server.base + "resources/metabolic-atlas.html#" + card)
        r = p.wait("""(()=>{ if(typeof LESFULL==='undefined'||!LESFULL||drawer.hidden||drawer.querySelector('.lesload')||state.sel!==%s) return null;
          const L=LES[%s], f=[].concat(L.find||[],L.mech||[],L.labs||[]).map(String)[0]||'';
          const probe=f.replace(/<[^>]+>/g,'').replace(/[^A-Za-z0-9 ]/g,' ').trim().split(/\\s+/).slice(0,2).join(' ');
          const txt=drawer.innerText.replace(/[^A-Za-z0-9 ]/g,' ').replace(/\\s+/g,' ');
          return {len: drawer.innerText.length, probe, hit: !probe || txt.includes(probe), title:(drawer.querySelector('.dtitle')||{}).textContent}; })()""" % (json.dumps(card), json.dumps(card)), timeout=20)
        time.sleep(0.3)
        errs = p.take_errors()
        record(S, "deep card link #%s opens the full card" % card, r["hit"] and r["len"] > 300 and not errs,
               ("%s · %d chars" % (r["title"], r["len"])) if not errs else fmt_errs(errs), time.time() - t0)
        C.shot(p, "atlas-card-" + card)
    except Exception as e:
        record(S, "deep card link", False, "%s" % e)
    finally:
        p.close()

    # ── mixes
    t0 = time.time()
    p = C.page()
    try:
        p.goto(C.server.base + "resources/metabolic-atlas.html#quiz/mix")
        p.wait("typeof state==='object' && booted && state.quiz==='mix' && drawer.querySelector('.pqopt')", timeout=20)
        r = p.js("""(async () => { const seen = [];
          for (let i = 0; i < 4; i++) {
            const opt = await __T.until(() => drawer.querySelector('.pqopt'), 4000); if (!opt) return {err: 'item ' + (i+1) + ': no answer choices', seen};
            seen.push(state.view); __T.click(opt);
            const nx = await __T.until(() => drawer.querySelector('[data-next]'), 4000); if (!nx) return {err: 'item ' + (i+1) + ': no Next card button', seen};
            await __T.budget(); __T.click(nx); await __T.frame(); }
          return {seen, errs: __T.takeErrs()}; })()""", timeout=60)
        errs = p.take_errors()
        record(S, "#quiz/mix runs 4 items", not r.get("err") and not errs, r.get("err") or ("maps: " + ",".join(r["seen"]) if not errs else fmt_errs(errs)), time.time() - t0)
        C.shot(p, "atlas-mix")
    except Exception as e:
        record(S, "#quiz/mix runs 4 items", False, "%s" % e)
    finally:
        p.close()
    t0 = time.time()
    p = C.page()
    try:
        p.goto(C.server.base + "resources/metabolic-atlas.html#quiz/moving")
        p.wait("typeof state==='object' && booted && typeof NMIX!=='undefined' && !!NMIX", timeout=20)
        r = p.js("""(async () => { const seen = [];
          // an item is Name it (st.quiz: name what is on) or Predict (st.mp + st.pred: guess the readout arrows)
          const live = () => { const st = DYN[state.view]; if (!st) return null;
            if (st.quiz && !st.quiz.ans && document.querySelector('[data-dyn^="q:"]')) return 'name';
            if (st.mp && st.pred && !st.pred.chk && document.querySelector('[data-dyn^="p:g:"]')) return 'predict';
            return null; };
          for (let i = 0; i < 4; i++) {
            const kind = await __T.until(live, 8000);
            if (!kind) return {err: 'item ' + (i+1) + ': no Name-it or Predict question on ' + state.view, seen};
            const v = state.view, st = DYN[v]; seen.push(v + '(' + kind + ')');
            await __T.budget();
            if (kind === 'name') {
              const k = st.quiz.k;
              const pick = i % 2 ? document.querySelector('[data-dyn^="q:"]:not([data-dyn="q:' + k + '"])') || __T.dynChip('q:' + k) : __T.dynChip('q:' + k);
              __T.click(pick); await __T.frame();
              if (!DYN[v].quiz || !DYN[v].quiz.ans) return {err: 'item ' + (i+1) + ': answer not taken on ' + v, seen};
            } else {
              const rows = [...new Set([...document.querySelectorAll('[data-dyn^="p:g:"]')].map(e => e.dataset.dyn.split(':')[2]))];
              for (const r of rows) { __T.click(__T.dynChip('p:g:' + r + ':' + (i % 2 ? 'd' : 'u'))); await __T.frame(); }
              if (!__T.click(__T.dynChip('p:chk'))) return {err: 'item ' + (i+1) + ': no Check chip on ' + v, seen};
              await __T.frame();
              if (!DYN[v].pred || !DYN[v].pred.chk) return {err: 'item ' + (i+1) + ': Check not taken on ' + v, seen};
            }
            if (i < 3) { const nx = await __T.until(() => __T.dynChip('quiz:mix'), 3000); if (!nx) return {err: 'item ' + (i+1) + ': no Next chip (quiz:mix)', seen};
              __T.click(nx); await __T.sleep(50); }
          }
          return {seen, k: NMIX && NMIX.k, ok: NMIX && NMIX.ok, errs: __T.takeErrs()}; })()""", timeout=90)
        errs = p.take_errors() + (r.get("errs") or [])
        record(S, "#quiz/moving runs 4 items", not r.get("err") and r.get("k") == 4 and not errs,
               r.get("err") or ("%s · score %s/%s" % (", ".join(r["seen"]), r["ok"], r["k"]) if not errs else fmt_errs(errs)), time.time() - t0)
        C.shot(p, "atlas-moving-mix")
    except Exception as e:
        record(S, "#quiz/moving runs 4 items", False, "%s" % e)
    finally:
        p.close()


def test_offline(C):
    S, t0 = "offline", time.time()
    p = C.page()
    try:
        p.goto(C.server.base + "index.html")
        r = p.wait("""(async()=>{ if(!navigator.serviceWorker) return 'no serviceWorker API';
          const reg = await navigator.serviceWorker.ready; return reg && reg.active ? {scope: reg.scope, ctl: !!navigator.serviceWorker.controller} : null; })()""", timeout=20)
        if not navigator_ok(r):
            record(S, "service worker registers", False, str(r)); return
        p.wait("!!navigator.serviceWorker.controller", timeout=10)
        record(S, "service worker registers + controls the hub", True, r["scope"])
        # visit the atlas once online, with its card text, so it is saved
        p.goto(C.server.base + "resources/metabolic-atlas.html")
        p.wait("typeof LESFULL!=='undefined' && LESFULL && booted", timeout=30)
        p.wait("""(async()=>{ const c = await caches.open('qhub-v1'); const k = (await c.keys()).map(r => new URL(r.url).pathname);
          return k.some(x => /metabolic-atlas\\.html$/.test(x)) && k.some(x => /atlas-les\\.[0-9a-f]+\\.js$/.test(x)) && k.some(x => /\\/index\\.html$|\\/$/.test(x)); })()""", timeout=20)
        # cut the network: the server drops every connection and the tab is emulated offline
        C.server.offline = True
        p.cmd("Network.emulateNetworkConditions", offline=True, latency=0, downloadThroughput=-1, uploadThroughput=-1)
        p.take_errors()
        p.goto(C.server.base + "index.html")
        n = p.wait("document.querySelectorAll('#systems .sys').length", timeout=20)
        record(S, "offline: hub renders from the cache", n >= 5, "%d systems" % n)
        C.shot(p, "offline-hub")
        p.goto(C.server.base + "resources/metabolic-atlas.html#core")
        v = p.wait("typeof MAPS==='object' && booted && state.view==='core' && svg.querySelectorAll('*').length>40 && svg.querySelectorAll('*').length", timeout=20)
        record(S, "offline: atlas renders from the cache", v > 40, "%d svg elements" % v)
        lf = p.wait("""(async()=>{ await __T.until(()=>LESFULL,8000); return LESFULL?'yes':'no'; })()""", timeout=15)
        record(S, "offline: atlas card text loads from the cache", lf == "yes", lf)
        C.shot(p, "offline-atlas")
        errs = [e for e in p.take_errors() if "ERR_INTERNET_DISCONNECTED" not in e and "ERR_FAILED" not in e and "ERR_EMPTY_RESPONSE" not in e]
        record(S, "offline: no script errors", not errs, fmt_errs(errs))
    except Exception as e:
        record(S, "run", False, "%s" % e)
        if VERBOSE: traceback.print_exc()
    finally:
        C.server.offline = False
        p.close()
    record(S, "total", True, "", time.time() - t0)


def navigator_ok(r):
    return isinstance(r, dict) and r.get("scope")


# ─────────────────────────────────────────────────────────── main
def main():
    global VERBOSE
    ap = argparse.ArgumentParser(description="OCOM Question Hub regression tests (see the docstring at the top of this file)")
    ap.add_argument("--quick", action="store_true", help="smoke subset (< 1 min)")
    ap.add_argument("--maps", default="", help="comma-separated atlas map ids for the map sweep")
    ap.add_argument("--blocks", default="", help="comma-separated block folders (default: all)")
    ap.add_argument("--only", default="", help="sections to run: data,hub,blocks,atlas,features,offline")
    ap.add_argument("--shots", nargs="?", const=os.path.join(tempfile.gettempdir(), "qbank-test-shots"), default=None, help="save screenshots here")
    ap.add_argument("--phone", action="store_true", help="phone viewport (390x844, touch)")
    ap.add_argument("--dark", action="store_true", help="dark colour scheme")
    ap.add_argument("--jobs", type=int, default=6, help="parallel browser tabs (default 6)")
    ap.add_argument("--headed", action="store_true", help="show the Chrome window")
    ap.add_argument("--root", default=None, help="serve and check this copy of the site instead of the repo")
    ap.add_argument("-v", "--verbose", action="store_true", help="print every check as it runs")
    args = ap.parse_args()
    VERBOSE = args.verbose
    global ROOT
    if args.root: ROOT = os.path.abspath(args.root)
    only = set(x.strip() for x in args.only.split(",") if x.strip()) or {"data", "hub", "blocks", "atlas", "features", "offline"}
    if args.shots: os.makedirs(args.shots, exist_ok=True)

    T0 = time.time()
    print("OCOM Question Hub tests — %s%s%s" % ("quick" if args.quick else "full", " · phone" if args.phone else "", " · dark" if args.dark else ""), flush=True)
    A = atlas_model()
    BQ, QS = {}, None
    if "data" in only or "blocks" in only:
        t = time.time()
        if "data" in only:
            print("· data checks", flush=True)
            BQ, QS = check_data(A)
        else:
            QS = js_json(os.path.join(ROOT, "resources", "atlas-qstates.js"), "window.ATLAS_QSTATES=")
        print("  data: %.1fs" % (time.time() - t), flush=True)

    browser_secs = only - {"data"}
    if browser_secs:
        server = Server(ROOT)
        browser = Browser(headless=not args.headed)
        C = Ctx(args, server, browser)
        print("· serving %s on %s · Chrome on port %d" % (ROOT, server.base, browser.port), flush=True)
        try:
            jobs = []
            blocks = [b for b in (args.blocks.split(",") if args.blocks else block_dirs()) if b]
            if args.quick and not args.blocks: blocks = blocks[:3]
            ids = A["ids"]
            if args.maps:
                want = [x.strip() for x in args.maps.split(",") if x.strip()]
                unknown = [x for x in want if x not in ids]
                if unknown: record("atlas", "--maps ids exist", False, ",".join(unknown))
                ids = [x for x in want if x in ids]
            elif args.quick:
                mv = [v for v in ids if v in A["stubs"]]; st = [v for v in ids if v not in A["stubs"]]
                ids = st[:6] + [x for x in ("rtasim", "aasim", "nephflow", "coagflow", "pthsim", "tftsim") if x in A["stubs"]][:6]
                if len(ids) < 12: ids += mv[:12 - len(ids)]
            ex = cf.ThreadPoolExecutor(max_workers=max(1, args.jobs))
            futs = {}
            chunks = []
            if "atlas" in only:
                nch = max(1, min(len(ids), args.jobs * 2 if not args.quick else args.jobs))
                chunks = balanced_chunks(ids, A["stubs"], nch)
                for i, ch in enumerate(chunks):
                    futs[ex.submit(test_map_chunk, C, ch, "chunk%d" % i)] = ("atlas", ch)
            if "hub" in only: futs[ex.submit(test_hub, C)] = ("hub", None)
            if "features" in only: futs[ex.submit(test_features, C, A)] = ("features", None)
            if "blocks" in only:
                for b in blocks: futs[ex.submit(test_block, C, b, BQ, QS)] = ("block", b)
            stats = {"maps": 0, "moving": 0, "clicks": 0}
            for f in cf.as_completed(futs):
                kind, what = futs[f]
                try:
                    r = f.result()
                    if kind == "atlas" and r:
                        for k in stats: stats[k] += r[k]
                except Exception as e:
                    record(kind, "task %s" % (what if isinstance(what, str) else (what[0] + "…" if what else "")), False, "%s" % e)
            ex.shutdown()
            if "atlas" in only:
                failed = [r for r in RESULTS if r[0] == "atlas" and r[1].startswith("map ") and r[2] == "FAIL"]
                record("atlas", "every map opens + renders; moving maps: every switch", not failed and stats["maps"] == len(ids),
                       "%d/%d maps opened, %d moving, %d switch clicks, %d maps with problems" % (stats["maps"], len(ids), stats["moving"], stats["clicks"], len(failed)))
            if "offline" in only:
                print("· offline checks", flush=True)
                test_offline(C)
        finally:
            browser.close()
            server.close()

    # ── table
    total = time.time() - T0
    rows = [r for r in RESULTS if not (r[1] == "total")]
    w1 = max([len(r[0]) for r in rows] + [7]); w2 = min(70, max([len(r[1]) for r in rows] + [5]))
    print("\n%-*s  %-*s  %-6s %s" % (w1, "SECTION", w2, "CHECK", "RESULT", "DETAIL"))
    print("-" * (w1 + w2 + 40))
    for s, c, st, d, secs in rows:
        print("%-*s  %-*s  %-6s %s" % (w1, s, w2, c[:w2], st, (d[:160] + ("  (%.1fs)" % secs if secs >= 1 else ""))))
    nf = sum(1 for r in rows if r[2] == "FAIL"); nw = sum(1 for r in rows if r[2] == "WARN"); npass = sum(1 for r in rows if r[2] == "PASS")
    print("-" * (w1 + w2 + 40))
    print("%d passed, %d failed, %d warnings in %.1fs%s" % (npass, nf, nw, total, (" · screenshots: " + args.shots) if args.shots else ""))
    sys.exit(1 if nf else 0)


if __name__ == "__main__":
    main()
