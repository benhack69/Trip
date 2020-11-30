var CACHE_NAME = 'cache';

var urlsToCache = [
    '/',
    '/static/Tripeando/css/main.css',
    '/static/Tripeando/css/registromain.css',
    '/static/Tripeando/img/'
];

self.addEventListener('install', function(event){
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache){
            console.log('Se ha generado el cache');
            return cache.addAll(urlsToCache);
        })
    )
});

self.addEventListener('fetch',function(event){
    event.respondWith(
        caches.match(event.request).then(function(response){
            return fetch(event.request)
            .catch(function(rsp){
                return response;
            });
        })

    );

});