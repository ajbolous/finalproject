(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MachinesService', MachinesService);

    function MachinesService($q, $http) {
        function getAll() {
            return $http.get(DJANGOURL + '/machines/get-all');
        }

        function addMachine(machine) {
            return $http.get(DJANGOURL + '/machines/add', { params: machine })

        }

        return {
            getAll: getAll,
            addMachine: addMachine
        }
    }
})();