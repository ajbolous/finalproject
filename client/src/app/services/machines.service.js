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

        function editMachine(machine) {
            return $http.get(DJANGOURL + '/machines/edit', { params: machine })

        }

        function deleteMachine(machine) {
            return $http.get(DJANGOURL + '/machines/delete', { params: machine })
        }

        return {
            getAll: getAll,
            addMachine: addMachine,
            editMachine: editMachine,
            deleteMachine: deleteMachine

        }
    }
})();