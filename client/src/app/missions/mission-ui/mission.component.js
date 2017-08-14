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
                type: 'lineChart',
                height: 250,
                x: function(d) { return d.label; },
                y: function(d) { return d.value; },
                showValues: true,
                valueFormat: function(d) {
                    return d3.format(',.2f')(d);
                },
                transitionDuration: 500,
                xAxis: {
                    axisLabel: 'Machine id',
                },
                yAxis: {
                    axisLabel: 'Total Cost',
                    axisLabelDistance: 30,
                    tickFormat: function(d) {
                        return d3.format(',.2f')(d);
                    }
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

        $ctrl.greedyCosts = [{
            key: "Greedy Cost",
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
            $ctrl.allocatedSchedule.greedy.events = $ctrl.mission.getScheduleEvents(schedule.greedy.schedule);

            $ctrl.masCosts[0].values = [];
            Object.keys(schedule.mas.cost.machines).map(function(val) { return parseInt(val); }).sort(function(a, b) { return a - b }).forEach(function(mid) {
                $ctrl.masCosts[0].values.push({ 'label': parseInt(mid), 'value': schedule.mas.cost.machines[mid].total });
            });

            $ctrl.randCosts[0].values = [];
            Object.keys(schedule.rand.cost.machines).map(function(val) { return parseInt(val); }).sort(function(a, b) { return a - b }).forEach(function(mid) {
                $ctrl.randCosts[0].values.push({ 'label': parseInt(mid), 'value': schedule.rand.cost.machines[mid].total });
            });

            $ctrl.greedyCosts[0].values = [];
            Object.keys(schedule.greedy.cost.machines).map(function(val) { return parseInt(val); }).sort(function(a, b) { return a - b }).forEach(function(mid) {
                console.log(mid);
                $ctrl.greedyCosts[0].values.push({ 'label': parseInt(mid), 'value': schedule.greedy.cost.machines[mid].total });
            });
        }

        $ctrl.allocateSchedule = function() {
            $ctrl.mission.allocateSchedule($ctrl.schedule).then(function(schedule) {
                $ctrl.showAllocatedSchedule(schedule);
            });
        }

    }
})();