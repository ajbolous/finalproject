(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('WebSocket', WebSocket);

    function WebSocket($q, $http, $log) {
        var socket = undefined;
        var topics = {};

        function _connect(ip, port, namespace) {
            socket = io.connect("http://" + ip + ":" + port + namespace);
            $log.debug("trying to connect to", ip);
            socket.on('connect', function() {
                $log.debug("WebSocket connected");
            });
        }

        function _send(topic, message) {
            socket.emit(topic, message);
        }

        function _listen(topic, handler) {
            if ((topic in topics) == false) {
                topics[topic] = [];
                var topicHandlers = topics[topic];
                socket.on(topic, function(message) {
                    topicHandlers.forEach(function(h) {
                        h(message);
                    });
                });
            }
            $log.debug(handler);
            topics[topic].push(handler)
        }

        _connect(SERVERIP, 5000, '/');

        return {
            send: _send,
            listen: _listen
        }
    }
})();