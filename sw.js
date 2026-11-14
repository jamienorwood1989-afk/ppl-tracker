/* PPL+ Tracker — service worker (v3.6)
   App-shell caching: the whole app is one HTML file, so caching it +
   manifest + icons gives full offline use. Data lives in localStorage +
   an IndexedDB mirror, both unaffected by the cache. */
const CACHE='ppl-v3.6';
const SHELL = [
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/apple-touch-icon.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(ks =>
      Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return; // let video embeds etc. go to network

  // Navigations: cache-first with network fallback + offline shell
  if (req.mode === 'navigate') {
    e.respondWith(
      caches.match('./index.html').then(cached =>
        cached ||
        fetch(req).then(res => {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put('./index.html', copy));
          return res;
        }).catch(() => caches.match('./index.html'))
      )
    );
    return;
  }

  // Static assets: cache-first, network-fill
  e.respondWith(
    caches.match(req).then(cached =>
      cached ||
      fetch(req).then(res => {
        if (res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(req, copy));
        }
        return res;
      })
    )
  );
});
