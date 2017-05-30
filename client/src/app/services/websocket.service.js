(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('WebSocket', WebSocket);

    function WebSocket($q, $http) {
        var socket = undefined;
        var topics = {};

        function connect(ip, port, namespace) {
            socket = io.connect("http://" + ip + ":" + port + "/" + namespace);
            socket.on('connect', function(message) {
                $log.debug("WebSocket connected", message);
            });
        }

        function _send(topic, message) {

        }

        function _listen(topic) {
            if (topic in topics == false) {
                topics[topic] = [];
                var topicHandlers = topics[topic];
                socket.on(topic, function(message) {
                    for (var handler in topicHandlers) {
                        handler(message);
                        $log.debug(message, handler);
                    }
                });
            }

        }

        return {

            connect: _connect,
            send: _send,
            listen: _listen
        }
    }
})();