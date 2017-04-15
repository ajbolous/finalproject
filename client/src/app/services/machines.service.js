(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MachineService', MachineService);

    function MachineService($q, $http) {



        function getAll() {
            return $http.get(DJANGOURL + '/machines/getAll');
        }

        return {

            getAll: getAll
        }
    }
})();