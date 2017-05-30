(function() {
    'use strict';

    angular.module('opmopApp').controller('MainController', MainController);

    /** @ngInject */
    function MainController(toastr, $scope, $log, WebSocket) {
        var $ctrl = this;

        $ctrl.eventSources = [];

        WebSocket.listen("service_response", function(response) {
            $log.debug(response);
            $ctrl.data = [{ key: "Data", values: response.data }];
            $scope.$apply();
        });

        $ctrl.refresh = function() {
            WebSocket.send("service_pipe", { data: "hello" });
        }

        $ctrl.uiConfig = {
            calendar: {
                height: 450,
                editable: true,
                header: {
                    left: 'month basicWeek basicDay agendaWeek agendaDay',
                    center: 'title',
                    right: 'today prev,next'
                },
                eventClick: $scope.alertEventOnClick,
                eventDrop: $scope.alertOnDrop,
                eventResize: $scope.alertOnResize
            }
        };


        $ctrl.options = {
            chart: {
                type: 'discreteBarChart',
                height: 350,
                margin: {
                    top: 20,
                    right: 20,
                    bottom: 60,
                    left: 55
                },
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

        $ctrl.options2 = {
            chart: {
                type: 'scatterChart',
                height: 350,
                color: d3.scale.category10().range(),
                scatter: {
                    onlyCircles: false
                },
                showDistX: true,
                showDistY: true,
                //tooltipContent: function(d) {
                //    return d.series && '<h3>' + d.series[0].key + '</h3>';
                //},
                duration: 350,
                xAxis: {
                    axisLabel: 'X Axis',
                    tickFormat: function(d) {
                        return d3.format('.02f')(d);
                    }
                },
                yAxis: {
                    axisLabel: 'Y Axis',
                    tickFormat: function(d) {
                        return d3.format('.02f')(d);
                    },
                    axisLabelDistance: -5
                },
                zoom: {
                    //NOTE: All attributes below are optional
                    enabled: true,
                    scaleExtent: [1, 10],
                    useFixedDomain: false,
                    useNiceScale: false,
                    horizontalOff: false,
                    verticalOff: false,
                    unzoomEventType: 'dblclick.zoom'
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


        $ctrl.data3 = [{
                key: "One",
                y: 5
            },
            {
                key: "Two",
                y: 2
            },
            {
                key: "Three",
                y: 9
            },
            {
                key: "Four",
                y: 7
            },
            {
                key: "Five",
                y: 4
            },
            {
                key: "Six",
                y: 3
            },
            {
                key: "Seven",
                y: .5
            }
        ];


        /* Random Data Generator (took from nvd3.org) */
        function generateData(groups, points) {
            var data = [],
                shapes = ['circle', 'cross', 'triangle-up', 'triangle-down', 'diamond', 'square'],
                random = d3.random.normal();

            for (var i = 0; i < groups; i++) {
                data.push({
                    key: 'Group ' + i,
                    values: []
                });

                for (var j = 0; j < points; j++) {
                    data[i].values.push({
                        x: random(),
                        y: random(),
                        size: Math.random(),
                        shape: shapes[j % 6]
                    });
                }
            }
            return data;
        }


        $ctrl.data2 = generateData(4, 40);

    }

})();