"""Minimal stdlib Chrome DevTools Protocol client (used by tools/test-site.py).

Browser(port=None, prof=None, headless=True) launches /Applications/Google Chrome.app with a temp
profile and a remote-debugging port; browser.page(w, h, mobile, dark) opens a new tab and returns a
Page with .cmd(method, **params), .js(expr) (awaits promises, returns by value), .goto(url),
.shot(path), .errors (console errors / uncaught exceptions / failed loads seen so far).
"""
import base64, json, os, shutil, socket, struct, subprocess, tempfile, threading, time, urllib.request

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); p = s.getsockname()[1]; s.close(); return p


class WS:
    """Tiny RFC 6455 client: text frames, client masking, fragmentation, ping/pong."""
    def __init__(self, url):
        assert url.startswith("ws://")
        hostport, path = url[5:].split("/", 1)
        host, port = hostport.split(":")
        self.sock = socket.create_connection((host, int(port)), timeout=30)
        key = base64.b64encode(os.urandom(16)).decode()
        req = ("GET /%s HTTP/1.1\r\nHost: %s\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
               "Sec-WebSocket-Key: %s\r\nSec-WebSocket-Version: 13\r\n\r\n") % (path, hostport, key)
        self.sock.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            chunk = self.sock.recv(4096)
            if not chunk: raise ConnectionError("websocket handshake failed")
            buf += chunk
        head, self.rest = buf.split(b"\r\n\r\n", 1)
        if b" 101 " not in head.split(b"\r\n")[0]: raise ConnectionError(head.decode(errors="replace"))
        self.sock.settimeout(None)
        self.lock = threading.Lock()

    def _recvn(self, n):
        while len(self.rest) < n:
            chunk = self.sock.recv(max(65536, n - len(self.rest)))
            if not chunk: raise ConnectionError("websocket closed")
            self.rest += chunk
        out, self.rest = self.rest[:n], self.rest[n:]
        return out

    def send(self, text, opcode=1):
        data = text.encode() if isinstance(text, str) else text
        hdr = bytearray([0x80 | opcode])
        n = len(data)
        if n < 126: hdr.append(0x80 | n)
        elif n < 65536: hdr.append(0x80 | 126); hdr += struct.pack(">H", n)
        else: hdr.append(0x80 | 127); hdr += struct.pack(">Q", n)
        mask = os.urandom(4); hdr += mask
        masked = bytes(b ^ mask[i & 3] for i, b in enumerate(data)) if n < 4096 else _mask(data, mask)
        with self.lock: self.sock.sendall(bytes(hdr) + masked)

    def recv(self):
        msg, first_op = b"", None
        while True:
            b0, b1 = self._recvn(2)
            fin, op, n = b0 & 0x80, b0 & 0x0F, b1 & 0x7F
            if n == 126: n = struct.unpack(">H", self._recvn(2))[0]
            elif n == 127: n = struct.unpack(">Q", self._recvn(8))[0]
            if b1 & 0x80: mask = self._recvn(4); data = _mask(self._recvn(n), mask)
            else: data = self._recvn(n)
            if op == 8: raise ConnectionError("websocket closed by peer")
            if op == 9: self.send(data, 10); continue
            if op == 10: continue
            if first_op is None: first_op = op
            msg += data
            if fin: return msg.decode("utf-8", errors="replace")

    def close(self):
        try: self.sock.close()
        except Exception: pass


def _mask(data, mask):
    n = len(data)
    k = (mask * (n // 4 + 1))[:n]
    return (int.from_bytes(data, "little") ^ int.from_bytes(k, "little")).to_bytes(n, "little")


class CDPError(Exception):
    pass


class Page:
    def __init__(self, browser, target_id, ws_url, w=1280, h=900, mobile=False, dark=False):
        self.browser, self.target_id = browser, target_id
        self.ws = WS(ws_url)
        self.next_id = 0
        self.pending = {}
        self.cv = threading.Condition()
        self.errors = []          # [str]
        self.events = []          # selected raw events (for waits)
        self.ignore = ["favicon.ico"]
        self.alive = True
        self.reader = threading.Thread(target=self._read, daemon=True); self.reader.start()
        for d in ("Page", "Runtime", "Log", "Network"):
            self.cmd(d + ".enable")
        self.cmd("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1 if not mobile else 2,
                 mobile=bool(mobile))
        if mobile: self.cmd("Emulation.setTouchEmulationEnabled", enabled=True, maxTouchPoints=5)
        self.cmd("Emulation.setEmulatedMedia", features=[{"name": "prefers-color-scheme", "value": "dark" if dark else "light"}])
        self.cmd("Page.setLifecycleEventsEnabled", enabled=True)

    def _read(self):
        try:
            while True:
                m = json.loads(self.ws.recv())
                if "id" in m:
                    with self.cv:
                        self.pending[m["id"]] = m; self.cv.notify_all()
                else:
                    self._event(m)
        except Exception:
            self.alive = False
            with self.cv: self.cv.notify_all()

    def _ign(self, s):
        return any(x in s for x in self.ignore)

    def _event(self, m):
        meth, p = m.get("method"), m.get("params", {})
        if meth == "Runtime.exceptionThrown":
            d = p.get("exceptionDetails", {})
            ex = d.get("exception", {}) or {}
            s = "exception: %s (%s:%s)" % (ex.get("description") or d.get("text"), d.get("url", ""), d.get("lineNumber", ""))
            if not self._ign(s): self.errors.append(s[:600])
        elif meth == "Runtime.consoleAPICalled" and p.get("type") in ("error", "assert"):
            args = " ".join(str(a.get("value", a.get("description", ""))) for a in p.get("args", []))
            s = "console.%s: %s" % (p.get("type"), args)
            if not self._ign(s): self.errors.append(s[:600])
        elif meth == "Log.entryAdded":
            e = p.get("entry", {})
            if e.get("level") == "error":
                s = "log: %s %s" % (e.get("text", ""), e.get("url", ""))
                if not self._ign(s): self.errors.append(s[:600])
        elif meth == "Network.loadingFailed":
            if p.get("canceled") or p.get("blockedReason"): return
            self.events.append(m)
        elif meth in ("Page.loadEventFired", "Page.lifecycleEvent", "Page.javascriptDialogOpening"):
            if meth == "Page.javascriptDialogOpening":
                threading.Thread(target=lambda: self.cmd("Page.handleJavaScriptDialog", accept=True), daemon=True).start()
            self.events.append(m)

    def cmd(self, method, timeout=60, **params):
        with self.cv:
            self.next_id += 1; i = self.next_id
        self.ws.send(json.dumps({"id": i, "method": method, "params": params}))
        end = time.time() + timeout
        with self.cv:
            while i not in self.pending:
                if not self.alive: raise CDPError("connection lost during " + method)
                left = end - time.time()
                if left <= 0: raise CDPError("timeout: " + method)
                self.cv.wait(left)
            m = self.pending.pop(i)
        if "error" in m: raise CDPError("%s: %s" % (method, m["error"].get("message")))
        return m.get("result", {})

    def js(self, expr, timeout=60):
        r = self.cmd("Runtime.evaluate", timeout=timeout, expression=expr, awaitPromise=True, returnByValue=True,
                     userGesture=True)
        if "exceptionDetails" in r:
            d = r["exceptionDetails"]
            raise CDPError("js error: %s" % ((d.get("exception") or {}).get("description") or d.get("text")))
        return r.get("result", {}).get("value")

    def goto(self, url, wait=True, timeout=60):
        self.events = [e for e in self.events if e.get("method") != "Page.loadEventFired"]
        self.cmd("Page.navigate", url=url)
        if wait: self.wait_load(timeout)

    def reload(self, timeout=60):
        self.events = [e for e in self.events if e.get("method") != "Page.loadEventFired"]
        self.cmd("Page.reload", ignoreCache=False)
        self.wait_load(timeout)

    def wait_load(self, timeout=60):
        end = time.time() + timeout
        while time.time() < end:
            if any(e.get("method") == "Page.loadEventFired" for e in self.events): return True
            time.sleep(0.05)
        raise CDPError("page load timeout")

    def wait(self, expr, timeout=20, interval=0.1):
        """Poll a JS expression until truthy; returns its value (raises on timeout)."""
        end = time.time() + timeout; last = None
        while time.time() < end:
            try:
                last = self.js(expr)
                if last or last == {}: return last if last != {} else True   # {} = a DOM node / object (truthy in JS)
            except CDPError as e:
                last = str(e)
            time.sleep(interval)
        raise CDPError("wait timeout: %s (last=%r)" % (expr[:120], last))

    def shot(self, path):
        r = self.cmd("Page.captureScreenshot", format="png")
        with open(path, "wb") as f: f.write(base64.b64decode(r["data"]))

    def take_errors(self):
        e, self.errors = self.errors, []
        return e

    def close(self):
        try: self.browser._http("/json/close/" + self.target_id)
        except Exception: pass
        self.ws.close()


class Browser:
    def __init__(self, headless=True, extra=()):
        self.port = free_port()
        self.prof = tempfile.mkdtemp(prefix="qbank-test-chrome-")
        args = [CHROME, "--remote-debugging-port=%d" % self.port, "--user-data-dir=" + self.prof,
                "--no-first-run", "--no-default-browser-check", "--disable-extensions", "--disable-sync",
                "--disable-background-networking", "--disable-component-update", "--mute-audio",
                "--disable-background-timer-throttling", "--disable-renderer-backgrounding",
                "--disable-backgrounding-occluded-windows", "--disable-features=Translate,MediaRouter",
                "--remote-allow-origins=*", "about:blank"] + list(extra)
        if headless: args.insert(1, "--headless=new")
        self.blk, self.bid = threading.Lock(), 0
        self.proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end = time.time() + 30
        while time.time() < end:
            try: self._http("/json/version"); break
            except Exception: time.sleep(0.1)
        else:
            raise CDPError("Chrome did not start")

    def _http(self, path, method="GET"):
        req = urllib.request.Request("http://127.0.0.1:%d%s" % (self.port, path), method=method)
        with urllib.request.urlopen(req, timeout=10) as r: return json.loads(r.read() or b"null") if "close" not in path else None

    def _browser_cmd(self, method, **params):
        """One command on the browser-level endpoint (a short-lived websocket; Target.* calls)."""
        with self.blk:
            ws = WS(self._http("/json/version")["webSocketDebuggerUrl"])
            try:
                self.bid += 1
                ws.send(json.dumps({"id": self.bid, "method": method, "params": params}))
                while True:
                    m = json.loads(ws.recv())
                    if m.get("id") == self.bid:
                        if "error" in m: raise CDPError("%s: %s" % (method, m["error"].get("message")))
                        return m.get("result", {})
            finally:
                ws.close()

    def page(self, w=1280, h=900, mobile=False, dark=False):
        """A new tab in its OWN window: a background tab in a shared window is 'hidden' (no requestAnimationFrame)."""
        tid = self._browser_cmd("Target.createTarget", url="about:blank", newWindow=True, width=w, height=h)["targetId"]
        return Page(self, tid, "ws://127.0.0.1:%d/devtools/page/%s" % (self.port, tid), w, h, mobile, dark)

    def close(self):
        try: self.proc.terminate(); self.proc.wait(10)
        except Exception:
            try: self.proc.kill()
            except Exception: pass
        shutil.rmtree(self.prof, ignore_errors=True)
