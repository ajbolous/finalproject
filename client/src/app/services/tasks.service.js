(function() {
    'use strict';

    angular
        .module('opmopApp')
        .service('TasksService', TasksService);

    function TasksService($q, $http) {

        var _mission = undefined;

        function getAll() {
            return $http.get(DJANGOURL + '/tasks/get-all');
        }

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
                        startsAt: fixDate(task.startTime),
                        endsAt: fixDate(task.endTime),
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
            console.log(events);
            return events
        }

        function _buildMissionEvents(mission) {
            return [{
                title: 'Mission ' + " (" + mission.digLocation.nid + ")\n Target: (" + mission.target + ")",
                startsAt: fixDate(mission.startTime),
                endsAt: fixDate(mission.endTime),
                color: {
                    primary: '#0071c5',
                    secondary: 'aliceblue'
                },
                draggable: true, //Allow an event to be dragged and dropped
                resizable: true
            }];
        }



        function _getEvents(filter) {
            var d = $q.defer();
            if (angular.isDefined(_mission))
                d.resolve({ mission: _mission, events: _buildTaskEvents(_mission, filter) })
            else
                getAll().then(function(response) {
                    _mission = response.data[0]
                    d.resolve({ mission: _mission, events: _buildTaskEvents(_mission, filter) })
                });
            return d.promise;
        }

        function _getMissionsEvents(filter) {
            var d = $q.defer();
            if (angular.isDefined(_mission))
                d.resolve({ mission: _mission, events: _buildMissionEvents(_mission, filter) })
            else
                getAll().then(function(response) {
                    _mission = response.data[0]
                    d.resolve({ mission: _mission, events: _buildMissionEvents(_mission, filter) })
                });
            return d.promise;
        }
        return {
            getMissionEvents: _getMissionsEvents,
            getEvents: _getEvents,
            getAll: getAll
        }
    }
})();