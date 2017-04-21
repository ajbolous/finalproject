(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('TasksService', TasksService);

    function TasksService($q, $http) {



        function getAll() {
            return $http.get(DJANGOURL + '/tasks/getAll');
        }

        return {

            getAll: getAll
        }
    }
})();