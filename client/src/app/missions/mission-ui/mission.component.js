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
        $ctrl.allocatedSchedule = undefined;

        $ctrl.taskTypes = {
            'dig': true,
            'haulage': true,
            'load': true
        }




        $ctrl.options = {
            chart: {
                type: 'discreteBarChart',
                height: 250,
                x: function(d) { return d.label; },
                y: function(d) { return d.value; },
                showValues: true,
                valueFormat: function(d) {
                    return d3.format(',.4f')(d);
                },
                transitionDuration: 500,
                xAxis: {
                    axisLabel: 'X Axis'
                },
                yAxis: {
                    axisLabel: 'Y Axis',
                    axisLabelDistance: 30
                }
            }
        };


        $ctrl.masCosts = [{
            key: "MAS Cost",
            values: []
        }]

        $ctrl.randCosts = [{
            key: "MAS Cost",
            values: []
        }]

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

            $ctrl.schedule = schedule;
            $ctrl.schedule.events = $ctrl.mission.getScheduleEvents(schedule);
        }

        $ctrl.showAllocatedSchedule = function(schedule) {
            $ctrl.allocatedSchedule = schedule;
            $ctrl.allocatedSchedule.mas.events = $ctrl.mission.getScheduleEvents(schedule.mas.schedule);
            $ctrl.allocatedSchedule.rand.events = $ctrl.mission.getScheduleEvents(schedule.rand.schedule);
            $log.debug(schedule);
            $ctrl.masCosts[0].values = [];
            for (var mid in schedule.mas.cost.machines) {
                $ctrl.masCosts[0].values.push({ 'label': '' + mid, 'value': schedule.mas.cost.machines[mid].total });
            }
            $ctrl.randCosts[0].values = [];
            for (var mid in schedule.rand.cost.machines) {
                $ctrl.randCosts[0].values.push({ 'label': '' + mid, 'value': schedule.rand.cost.machines[mid].total });
            }
        }

        $ctrl.allocateSchedule = function() {
            $ctrl.mission.allocateSchedule($ctrl.schedule).then(function(schedule) {
                $ctrl.showAllocatedSchedule(schedule);
            });
        }

    }
})();