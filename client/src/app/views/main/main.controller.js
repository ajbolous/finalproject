(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, ExampleService) {
        var $ctrl = this;

        $ctrl.person = undefined;
        $ctrl.persons = [];


        ExampleService.getPerson('Bolous').then(function(person){
            $log.debug(person);
            $ctrl.person = person.data;
        });

        ExampleService.getAll().then(function(response){
            $log.debug(response);
            $ctrl.persons = response.data;
        });
    }

})();