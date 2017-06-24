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
        $ctrl.missions = [];


        $ctrl.fetchMissions = function() {
            MissionsService.getMissions().then(function(missions) {
                $log.debug(missions);
                $ctrl.missions = missions;
                $ctrl.progressbar.complete();
            });
        }

        $ctrl.showMission = function(mission) {
            $ctrl.selectedMission = mission;
        }

        $ctrl.fetchMissions();
    }

})();