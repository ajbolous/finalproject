(function () {
    'use strict';

    angular
        .module('opmopApp')
        .service('ExampleService', ExampleService);

    function ExampleService($q, $http ) {

        function addPerson(fname, lname) {
            return $http.get(DJANGOURL + '/persons/new', { params: { fname: fname, lname: lname } })
        }

        function getPerson(name) {
            return $http.get(DJANGOURL + '/persons/get', { params: { name: name } })
        }

        function getAll(){
            return $http.get(DJANGOURL + '/persons/all');
        }

        return {
            getPerson: getPerson,
            addPerson: addPerson,
            getAll: getAll
        }
    }
})();