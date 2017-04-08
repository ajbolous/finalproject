(function () {
    'use strict';

    angular
        .module('opmopApp')
        .service('ExampleService', ExampleService);

    function ExampleService($q, $http) {

        function addPerson(fname, lname) {
            return $http.get('http://localhost:8000/persons/new', { params: { fname: fname, lname: lname } })
        }

        function getPerson(name) {
            return $http.get('http://localhost:8000/persons/get', { params: { name: name } })
        }
        return {
            getPerson: getPerson,
            addPerson: addPerson
        }
    }
})();