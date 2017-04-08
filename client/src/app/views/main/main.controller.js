(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, ExampleService) {
        var $ctrl = this;

        $ctrl.person = undefined

        ExampleService.getPerson('Bolous').then(function(person){
            $log.debug(person);
            $ctrl.person = person.data;
        })
    }

})();