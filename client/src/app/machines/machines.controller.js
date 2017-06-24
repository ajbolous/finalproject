(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesController', MachinesController);

    /** @ngInject */
    function MachinesController(toastr, $scope, $log, $uibModal, MachinesService, ngProgressFactory) {
        var $ctrl = this;
        $ctrl.selectedMachine;
        $ctrl.machines = []

        $ctrl.filteredMachines = [];

        $ctrl.machinesGroup = [];
        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();

        $ctrl.searchCallBack = function(searchObj) {
            var filteredMachines = [];

            if (searchObj == undefined) {
                $ctrl.filteredMachines = $ctrl.machines;
                return;
            }

            $ctrl.machines.forEach(function(machine) {
                for (var field in searchObj) {
                    if (searchObj[field] != "" && machine[field].indexOf(searchObj[field]) == -1) {
                        return;
                    }
                }
                filteredMachines.push(machine);
            });
            $ctrl.filteredMachines = filteredMachines;
        }

        $ctrl.getFilteredTrucks = function() {
            var trucks = [];
            $ctrl.filteredMachines.forEach(function(machine) {
                if (machine.type == "truck")
                    trucks.push(machine);
            })
            return trucks;
        }

        $ctrl.getFilteredLoaders = function() {
            var trucks = [];
            $ctrl.filteredMachines.forEach(function(machine) {
                if (machine.type == "loader")
                    trucks.push(machine);
            })
            return trucks;
        }


        $ctrl.getFilteredShovels = function() {
            var trucks = [];
            $ctrl.filteredMachines.forEach(function(machine) {
                if (machine.type == "shovel")
                    trucks.push(machine);
            })
            return trucks;
        }
        $ctrl.refreshMachines = function() {
            MachinesService.getAll().then(function(machines) {
                $ctrl.machines = machines;
                $ctrl.filteredMachines = machines;
                $ctrl.progressbar.complete();
            });
        }

        $ctrl.refreshMachines();

        $ctrl.addMachine = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/views/machines/machines-modal/machines-modal.html',
                controller: 'MachinesModalController',
                controllerAs: '$ctrl',
                resolve: {
                    options: function() {
                        return {
                            isEdit: false,
                            machine: undefined
                        }
                    }
                }
            });
            modalInstance.result.then(function(machine) {
                var promise = MachinesService.addMachine(machine);

                promise.then(function(response) {
                    $ctrl.refreshMachines();
                    toastr.success(response.data);
                });
            });

        }

        $ctrl.editMachine = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/views/machines/machines-modal/machines-modal.html',
                controller: 'MachinesModalController',
                controllerAs: '$ctrl',
                resolve: {
                    options: function() {
                        return {
                            isEdit: true,
                            machine: $ctrl.selectedMachine
                        }
                    }
                }
            });
            modalInstance.result.then(function(machine) {
                var promise = MachinesService.editMachine(machine);

                promise.then(function(response) {
                    $ctrl.refreshMachines();
                    toastr.success(response.data);
                });
            });

        }

        $ctrl.deleteMachine = function() {
            var modalInstance = $uibModal.open({
                animation: true,
                templateUrl: 'app/components/confirm-modal/confirm-modal.html',
                controller: 'ConfirmModalController',
                controllerAs: '$ctrl',

            });

            modalInstance.result.then(function(result) {
                $log.debug(result);
                if (result == true) {
                    var promise = MachinesService.deleteMachine($ctrl.selectedMachine);
                    promise.then(function(response) {
                        $log.debug(response);
                        toastr.success(response.data);
                        $ctrl.refreshMachines();
                    });
                }
            });
        }


    }

})();