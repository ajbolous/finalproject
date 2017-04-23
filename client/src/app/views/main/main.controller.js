(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log) {
        var $ctrl = this;

        $ctrl.dateOptions = {
            minDate: new Date(),
            showWeeks: true
        };

        $ctrl.myDate = new Date();

    }

})();