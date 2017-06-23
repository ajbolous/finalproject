(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('MissionsService', MissionsService);

    function MissionsService($q, $log, $http, toastr) {

        function fixDate(date) {
            var fixedDate = new Date(date)
            return new Date(fixedDate.getFullYear(), fixedDate.getMonth() + 1, fixedDate.getDate(), fixedDate.getHours(), fixedDate.getMinutes());
        }

        function _buildTaskEvents(mission, filter) {
            var i = 0;
            var events = [];
            mission.schedules.forEach(function(sched) {
                //var sortedTasks = sortByKey(sched.tasks, 'machine', 'id');
                sched.tasks.forEach(function(task) {

                    if (filter[task.type] == false)
                        return;

                    var color = 'aliceblue';
                    if (task.type == 'haulage')
                        color = 'lightyellow'
                    else if (task.type == 'load')
                        color = 'lightgreen'

                    var t = {
                        title: ' Task ' + i++ + " (" + task.type + ")\n Machine: (" + task.machine.id + " - " + task.machine.model + ")",
                        startsAt: task.startTime,
                        endsAt: task.endTime,
                        color: {
                            primary: '#0071c5',
                            secondary: color
                        },
                        draggable: true, //Allow an event to be dragged and dropped
                        resizable: true
                    }
                    events.push(t);
                });
            });

            return events
        }

        function _getTasksEvents(filter) {
            return _getMissions().then(function(missions) {
                var mission = missions[0]
                return { mission: mission, events: _buildTaskEvents(mission, filter) }
            });
        }



        function _buildMissionEvent(mission) {
            return {
                title: 'Mission ' + " (" + mission.id + ")\n Target: (" + mission.target + ")",
                startsAt: mission.startTime,
                endsAt: mission.endTime,
                color: {
                    primary: '#0071c5',
                    secondary: 'aliceblue'
                },
                draggable: true, //Allow an event to be dragged and dropped
                resizable: true
            };
        }

        function _getMissionsEvents() {

            return _getMissions().then(function(missions) {
                var missionsEvents = []
                missions.forEach(function(m) {
                    missionsEvents.push({ mission: m, events: _buildMissionEvent(m) })
                });
                return missionsEvents;
            });
        }

        function _getMissionCosts() {
            var machines = [];
            var totalCost = 0;
            return $http.get(DJANGOURL + '/tasks/get-costs').then(function(response) {
                for (var key in response.data) {
                    totalCost += response.data[key]['total'];
                    machines.push({
                        "label": key,
                        "value": response.data[key]['total']
                    });
                }
                return machines;
            });
        }

        function _getMissions(date) {
            return $http.get(DJANGOURL + '/tasks/get-missions').then(function(response) {
                $log.debug(response);
                return response.data;
            });
        }


        function _getTaskAllocation(mission, date) {
            return $http.get(DJANGOURL + '/tasks/alloc-sched').then(function(response) {
                $log.debug(response);
            });
        }

        return {
            getMissionsEvents: _getMissionsEvents,
            getMissions: _getMissions,
            getTasksEvents: _getTasksEvents,
            getMissionCosts: _getMissionCosts,
        }
    }
})();