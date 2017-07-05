(function() {
    'use strict';

    angular.module('opmopApp').controller('MissionsController', MissionsController);

    /** @ngInject */
    function MissionsController(toastr, $scope, $log, MissionsService, ngProgressFactory, $uibModal) {
        var $ctrl = this;
        /* alert on eventClick */

        $ctrl.events = [{ title: 'All Day Event', startsAt: new Date(2017, 5, 1) }];

        $ctrl.calendarView = "day";
        $ctrl.viewDate = new Date(2017, 5, 1, 9);

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();
        $ctrl.missions = [];

        $ctrl.todayDate = new Date();

        $ctrl.todayMissions = [];

        $ctrl.fetchMissions = function() {
            return MissionsService.getMissions().then(function(missions) {
                $log.debug(missions);
                $ctrl.missions = missions;
                $ctrl.progressbar.complete();
                $ctrl.getTodaySchedules();
            });
        }

        $ctrl.showMission = function(mission) {
            $ctrl.selectedMission = mission;
        }


        $ctrl.getTodaySchedules = function() {
            var todayMissions = [];
            $ctrl.missions.forEach(function(miss) {
                miss.getSchedules().forEach(function(sched) {
                    if (sched.date.getDate() == $ctrl.todayDate.getDate()) {
                        var events = miss.getScheduleEvents(sched);
                        todayMissions.push({ mission: miss, schedule: sched, events: events });
                    }
                });
            });
            $ctrl.todayMissions = todayMissions;
        }

        $ctrl.addMission = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/missions/add-mission-modal/mission-modal.html',
                controller: 'AddMissionModalController',
                controllerAs: '$ctrl',
            });
            modalInstance.result.then(function(missionData) {
                MissionsService.addMachine(missionData).then(function(mission) {
                    $ctrl.fetchMissions();
                    $ctrl.showMission(mission)
                    toastr.success("Mission added successfully.");
                });
            });
        }
        $ctrl.fetchMissions();
    }

})();