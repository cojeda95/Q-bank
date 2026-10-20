/* OCOM Question Hub — offline support.
   Network first: online, every request goes to the network, so you always get
   the newest questions. Each file you open is saved as it arrives, so the hub,
   the Lesion Atlas and any block you have opened before keep working without
   signal. If the network is slow and a saved copy exists, the saved copy is
   shown when the whole file has not arrived after a few seconds, and the fresh
   one replaces it in the background.
   The Lesion Atlas is big (about 1 MB on the wire), so it is shown from the
   saved copy at once and refreshed in the background; when that refresh brings
   a new build, the open atlas is told (postMessage "atlas-updated") and offers
   a reload. Its card text (resources/atlas-les.<hash>.js) and the moving-map
   drawings (resources/dyn/<map>.js?v=<hash>) are named by their content, so a
   saved copy of the same name is served as is. Requests to other sites (the
   Firestore sync, CDNs) are left alone, so sync and Live Session still need a
   connection. */
const CACHE = 'qhub-v1';
const CORE = ['./', 'index.html', 'shared/theme.css', 'shared/theme.js', 'shared/style.css', 'shared/app.js',
  'announcements.js', 'sync.js', 'resources/metabolic-atlas.html', 'resources/atlas-terms.js', 'resources/atlas-practice.js', 'resources/atlas-qlinks.js',
  'resources/qbank-counts.js', 'resources/atlas-home.js', 'resources/atlas-cards.js', 'resources/atlas-qstates.js'];
// + the atlas's card text, resources/atlas-les.<hash>.js: its name changes with every build, so it is read from the saved atlas (pairLes)

const ATLAS = /\/resources\/metabolic-atlas\.html$/;
const LESF = /\/resources\/atlas-les\.[0-9a-f]+\.js$/;
const DYN = /\/resources\/dyn\/[^/]+\.js$/;
const SLOW = 4000;
const at = p => new URL(p, self.registration.scope).href;
const lesOf = html => (String(html).match(/\bconst LES_BODY = "(atlas-les\.[0-9a-f]+\.js)"/) || [])[1];

/* the card text the atlas page `html` (or the saved one) needs, saved next to it — fetched if it is not saved yet */
async function pairLes(c, html) {
  if (html == null) { const r = await c.match(at('resources/metabolic-atlas.html')); if (!r) return null; html = await r.text(); }
  const name = lesOf(html); if (!name) return null;
  const url = at('resources/' + name);
  if (!(await c.match(url))) {
    const res = await fetch(url);
    if (!res.ok) throw new Error('card text ' + res.status);
    await c.put(url, res);
  }
  return url;
}
/* keep the card text of the saved atlas and `keep` (the build before it, which an open page may still be loading); drop the rest */
async function pruneLes(c, keep) {
  const cur = await pairLes(c).catch(() => null), ok = new Set([cur, ...keep].filter(Boolean));
  for (const k of await c.keys()) if (LESF.test(new URL(k.url).pathname) && !ok.has(k.url)) await c.delete(k);
}

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE)
    .then(c => Promise.allSettled(CORE.map(u => c.add(u))).then(() => pairLes(c)).catch(() => {}))
    .then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(ks => Promise.all(ks.filter(k => k.startsWith('qhub-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

const offlinePage = () => `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Offline</title><body style="font:16px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:560px;margin:15vh auto;padding:0 20px;color:#22241F">
<h1 style="font-size:22px">You're offline</h1>
<p>This page hasn't been saved on this device yet. Open it once while you're online and it will work without signal after that.</p>
<p><a href="${self.registration.scope}" style="color:#1f4e79">Back to the hub</a> — the hub, the Lesion Atlas and any block you've opened before still work.</p></body>`;
function saved(req) {
  return caches.open(CACHE).then(c => c.match(req, { ignoreSearch: true }))
    .then(m => m || (req.mode === 'navigate'
      ? new Response(offlinePage(), { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8' } })
      : undefined));
}
// the hub's Save all / Update (cache: 'reload'): the network's copy or nothing. Not a page load: offline, a reload still shows the saved page
const fresh = req => req.mode !== 'navigate' && (req.cache === 'reload' || req.cache === 'no-store');

/* fetch req; a good same-site answer is saved under `key` (default: req). -> {net: the response, done: settles once it is saved} */
function fetchSave(e, req, key, before) {
  let done = Promise.resolve();
  const net = fetch(req).then(res => {
    if (res && res.ok && res.type === 'basic') {
      const copy = res.clone();
      done = caches.open(CACHE).then(async c => { if (before) await before(c); await c.put(key || req, copy); }).catch(() => {});
    }
    return res;
  });
  e.waitUntil(net.then(() => done, () => {}));
  return { net, done: net.then(() => done, () => {}) };
}

/* everything but the atlas: network first; with a saved copy, that copy if the WHOLE file has not arrived after SLOW ms
   (racing fetch() alone only waited for the headers, which come at once on a weak signal while the body trickles in) */
async function networkFirst(e) {
  const req = e.request, { net, done } = fetchSave(e, req);
  net.catch(() => {});
  const copy = await caches.match(req, { ignoreSearch: true });
  if (!copy || fresh(req)) {
    try { return await net; } catch (err) { return (!fresh(req) && (await saved(req))) || Response.error(); }
  }
  const whole = net.then(res => done.then(() => res));   // the saved copy is written once the whole body is in
  const slow = new Promise(r => setTimeout(() => r(null), SLOW));
  try { return (await Promise.race([whole, slow])) || copy; } catch (err) { return copy; }
}

/* the atlas page: the saved copy at once, the network's in the background (stale-while-revalidate) */
async function atlasPage(e) {
  const req = e.request, key = at('resources/metabolic-atlas.html');
  const c = await caches.open(CACHE);
  const copy = req.mode === 'navigate' && await c.match(key);
  if (!copy || req.cache === 'reload') {   // first visit, a hard reload or Save all: the network, saved as it arrives
    const { net } = fetchSave(e, req, key);
    try { return await net; } catch (err) { return copy || (!fresh(req) && (await saved(req))) || Response.error(); }
  }
  const old = copy.clone();
  e.waitUntil((async () => {
    const res = await fetch(key, { cache: 'no-cache' });   // revalidates: a 304 when nothing changed
    if (!res.ok || res.type !== 'basic') return;
    const html = await res.clone().text(), was = await old.text();
    if (html === was) return;
    // a new build: save its card text first, so the saved page and its card text always match (offline too)
    await pairLes(c, html);
    await c.put(key, res);
    await pruneLes(c, [lesOf(was) && at('resources/' + lesOf(was))]);
    const told = new Set();
    for (let i = 0; i < 20; i++) {   // every open atlas; the one that is opening may not be ready for messages yet
      (await self.clients.matchAll({ type: 'window' })).filter(w => ATLAS.test(new URL(w.url).pathname) && !told.has(w.id))
        .forEach(w => { told.add(w.id); w.postMessage({ type: 'atlas-updated' }); });
      if (!e.resultingClientId || told.has(e.resultingClientId)) return;
      await new Promise(r => setTimeout(r, 500));
    }
  })().catch(() => {}));
  return copy;
}

/* the card text: named by its content — a saved copy is the right one */
async function cardText(e) {
  const req = e.request, c = await caches.open(CACHE), copy = await c.match(req, { ignoreSearch: true });
  if (copy) return copy;
  const { net, done } = fetchSave(e, req);
  e.waitUntil(done.then(() => pruneLes(c, [new URL(req.url).origin + new URL(req.url).pathname])).catch(() => {}));
  try { return await net; } catch (err) { return Response.error(); }
}

/* a moving-map drawing, dyn/<map>.js?v=<content hash>: a saved copy of that version is served as is; any other version →
   the network (saved in place of the old one), and the old one only when offline */
async function drawing(e) {
  const req = e.request, c = await caches.open(CACHE), v = new URL(req.url).searchParams.get('v');
  const all = await c.matchAll(req, { ignoreSearch: true });
  const same = v && all.find(r => r.url && new URL(r.url).searchParams.get('v') === v);
  if (same && !fresh(req)) return same;
  const { net } = fetchSave(e, req, null, cc => cc.delete(req, { ignoreSearch: true }));
  try { return await net; } catch (err) {
    return (!fresh(req) && (all.find(r => r.url && !new URL(r.url).searchParams.get('v')) || all[0])) || Response.error();
  }
}

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  const p = url.pathname;
  e.respondWith(ATLAS.test(p) ? atlasPage(e) : LESF.test(p) ? cardText(e) : DYN.test(p) ? drawing(e) : networkFirst(e));
});
