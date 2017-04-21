(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MachinesService', MachinesService);

    function MachinesService($q, $http) {
        function getAll() {
            return $http.get(DJANGOURL + '/machines/getAll');
        }



        return {
            getAll: getAll
        }
    }
})();