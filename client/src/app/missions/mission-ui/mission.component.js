(function() {
    'use strict';

    angular.module('opmopApp')
        .component('missionUi', {
            templateUrl: 'app/missions/mission-ui/mission.component.html',
            controller: MissionUI,
            bindings: {
                mission: "=",
                displayMode: "@"
            }
        });

    function MissionUI($log, $scope) {
        var $ctrl = this;
        $ctrl.mission = undefined;
        $ctrl.displayMode = undefined;

        $ctrl.schedule = undefined;

        $ctrl.taskTypes = {
            'dig': true,
            'haulage': true,
            'load': true
        }

        $ctrl.refresh = function() {
            var events = [];
            $ctrl.mission.getScheduleEvents($ctrl.schedule).forEach(function(event) {
                if ($ctrl.taskTypes[event.type] == true) {
                    events.push(event);
                }
            });

            $ctrl.schedule.events = events;
        }

        $ctrl.showSchedule = function(schedule) {
            var events = $ctrl.mission.getScheduleEvents(schedule);
            $ctrl.schedule = schedule;
            $ctrl.schedule.events = events;
        }

        $ctrl.allocateSchedule = function() {
            $ctrl.mission.allocateSchedule($ctrl.schedule).then(function(schedule) {
                $ctrl.showSchedule($ctrl.mission.getScheduleById($ctrl.schedule.id));
            });
        }

    }
})();