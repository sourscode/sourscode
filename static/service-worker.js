importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');

// cache name
workbox.core.setCacheNameDetails({
    prefix: 'cache',
    precache: 'precache',
    runtime: 'runtime',
  });
  
// runtime cache

workbox.routing.registerRoute(
    new RegExp('/static/.*'),
    new workbox.strategies.CacheFirst({
			cacheName: 'cache-Static'
		})
);

// 1. stylesheet
workbox.routing.registerRoute(
    new RegExp('\.css$'),
    new workbox.strategies.CacheFirst({
        cacheName: 'cache-Stylesheets'
    })
);
// 2. images
workbox.routing.registerRoute(
    new RegExp('\.(png|svg|jpg|jpeg)$'),
    new workbox.strategies.CacheFirst({
        cacheName: 'cache-Images'
    })
);

// 3. Everything
workbox.routing.registerRoute(
    new RegExp('/.*'),
    new workbox.strategies.CacheFirst()
);


workbox.precaching.precacheAndRoute([]);