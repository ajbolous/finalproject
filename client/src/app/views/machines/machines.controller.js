(function() {
    'use strict';

    angular.module('opmopApp').controller('MachinesController', MachinesController);

    /** @ngInject */
    function MachinesController(toastr, $scope, $log, $uibModal, MachinesService, ngProgressFactory) {
        var $ctrl = this;
        $ctrl.selectedMachine;
        $ctrl.machines = []

        $ctrl.progressbar = ngProgressFactory.createInstance();
        $ctrl.progressbar.start();


        $ctrl.gridOptions = {
            enableFiltering: true,
            enableRowSelection: true,
            enableSelectAll: true,
            selectionRowHeaderWidth: 35,
            rowHeight: 35,
            showGridFooter: true,
            multiSelect: false,

            onRegisterApi: function(gridApi) {
                $ctrl.gridApi = gridApi;
                $ctrl.gridApi.selection.on.rowSelectionChanged($scope, function(row) {
                    $ctrl.selectedMachine = row.entity;
                });
            }
        };

        $ctrl.refreshMachines = function() {
            MachinesService.getAll().then(function(response) {
                $ctrl.machines = response.data;
                $ctrl.gridOptions.data = $ctrl.machines;
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