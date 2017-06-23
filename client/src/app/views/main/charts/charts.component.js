(function() {
    'use strict';

    angular.module('opmopApp')
        .component('chartsUi', {
            templateUrl: 'app/views/main/charts/charts.component.html',
            controller: ChartsUiController,
            bindings: {}
        });

    function ChartsUiController(toastr, $scope, $log, ngProgressFactory, MissionsService) {
        var $ctrl = this;

        $ctrl.eventSources = [];

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();

        //$ctrl.player = new jsmpeg(new WebSocket('ws://' + SERVERIP + ':8084/'), { canvas: document.getElementById('videoCanvas') });
        $ctrl.events = [];

        $ctrl.calendarView = "week";
        $ctrl.viewDate = new Date(2017, 5, 1, 9);

        $ctrl.refresh = function() {
            MissionsService.getMissionsEvents().then(function(missionEvents) {

                missionEvents.forEach(function(mission) {
                    $log.debug(mission);
                    $ctrl.events.push(mission.events);
                });
                $ctrl.progressbar.complete();
            });
        }

        $ctrl.refresh();

        $ctrl.options = {
            chart: {
                type: 'discreteBarChart',
                height: 350,
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


        $ctrl.options3 = {
            chart: {
                type: 'pieChart',
                height: 350,
                x: function(d) { return d.key; },
                y: function(d) { return d.y; },
                showLabels: true,
                duration: 500,
                labelThreshold: 0.01,
                labelSunbeamLayout: true,
                legend: {
                    margin: {
                        top: 5,
                        right: 35,
                        bottom: 5,
                        left: 0
                    }
                }
            }
        };

        $ctrl.data = [{
            key: "Cumulative Return",
            values: [
                { "label": "A", "value": -29.765957771107 },
                { "label": "B", "value": 0 },
                { "label": "C", "value": 32.807804682612 },
                { "label": "D", "value": 196.45946739256 },
                { "label": "E", "value": 0.19434030906893 },
                { "label": "F", "value": -98.079782601442 },
                { "label": "G", "value": -13.925743130903 },
                { "label": "H", "value": -5.1387322875705 }
            ]
        }]

        // MissionsService.getMissionCosts().then(function(mission) {
        //     $log.debug(mission);
        //     $ctrl.data = [{
        //         key: "Costs",
        //         values: mission
        //     }]
        // });

    }
})();