(function() {
    'use strict';

    angular.module('opmopApp').controller('MissionsController', MissionsController);

    /** @ngInject */
    function MissionsController(toastr, $scope, $log, MissionsService, ngProgressFactory) {
        var $ctrl = this;
        /* alert on eventClick */

        $ctrl.events = [{ title: 'All Day Event', startsAt: new Date(2017, 5, 1) }];

        $ctrl.calendarView = "day";
        $ctrl.viewDate = new Date(2017, 5, 1, 9);

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();


        $ctrl.taskTypes = {
            'dig': true,
            'haulage': true,
            'load': true
        }

        $ctrl.refresh = function() {
            MissionsService.getTasksEvents($ctrl.taskTypes).then(function(data) {
                $ctrl.events = data.events;
                $ctrl.mission = data.mission;
                $ctrl.progressbar.complete();
            });
        }
        $ctrl.refresh();
    }

})();