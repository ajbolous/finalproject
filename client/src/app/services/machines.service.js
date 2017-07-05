(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MachinesService', MachinesService);

    function MachinesService($q, $http) {
        function _getAll() {
            return $http.get(DJANGOURL + '/machines/get-all').then(function(response) {
                return response.data
            });
        }

        function _addMachine(machine) {
            return $http.get(DJANGOURL + '/machines/add', { params: machine })
        }

        function _editMachine(machine) {
            return $http.get(DJANGOURL + '/machines/edit', { params: machine })

        }

        function _deleteMachine(machine) {
            return $http.get(DJANGOURL + '/machines/delete', { params: machine })
        }

        function _getMachineRoute(machine) {
            var today = new Date();

            var todayStr = today.getDate() + "/" + (today.getMonth() + 1) + "/" + today.getFullYear();
            return $http.get(DJANGOURL + '/tasks/machine-tasks', { params: { mid: machine.id, date: todayStr } }).then(function(response) {
                return response.data;
            });
        }

        return {
            getAll: _getAll,
            addMachine: _addMachine,
            editMachine: _editMachine,
            deleteMachine: _deleteMachine,
            getMachineRoute: _getMachineRoute
        }
    }
})();