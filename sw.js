/* OCOM Question Hub — offline support.
   Network first: online, every request goes to the network, so you always get
   the newest questions and atlas. Each file you open is saved as it arrives,
   so the hub, the Lesion Atlas and any block you have opened before keep
   working without signal. If the network is slow and a saved copy exists, the
   saved copy is shown after a few seconds and the fresh one replaces it in the
   background. Requests to other sites (the Firestore sync, CDNs) are left
   alone, so sync and Live Session still need a connection. */
const CACHE = 'qhub-v1';
const CORE = ['./', 'index.html', 'shared/theme.css', 'shared/theme.js', 'shared/style.css', 'shared/app.js',
  'announcements.js', 'sync.js', 'resources/metabolic-atlas.html', 'resources/atlas-terms.js', 'resources/atlas-practice.js', 'resources/atlas-qlinks.js', 'resources/qbank-counts.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE)
    .then(c => Promise.allSettled(CORE.map(u => c.add(u))))
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

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  if (new URL(req.url).origin !== self.location.origin) return;
  e.respondWith((async () => {
    const net = fetch(req).then(res => {
      if (res && res.ok && res.type === 'basic') {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy));
      }
      return res;
    });
    net.catch(() => {});
    const copy = await caches.match(req, { ignoreSearch: true });
    if (!copy) {
      try { return await net; } catch (err) { return (await saved(req)) || Response.error(); }
    }
    const slow = new Promise(r => setTimeout(() => r(null), 4000));
    try { return (await Promise.race([net, slow])) || copy; } catch (err) { return copy; }
  })());
});
