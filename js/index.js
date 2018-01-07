// create the module and name it tvtcresultsApp
var app = angular.module('tvtcResultatsApp', [
  'ngRoute',
  'ui.bootstrap',
  'tvtcResultatsApp.escons',
  'tvtcResultatsApp.permesa',
  'tvtcResultatsApp.permunicipi',
]);

app.config(['$routeProvider', function($routeProvider) {

  // configure our routes
  $routeProvider

    // .when('/', {
    //   templateUrl: 'views/escons/index.html',
    //   controller: 'esconsController'
    // })
    .when('/', {
      templateUrl: 'views/permesa/index.html',
      controller: 'permesaController'
    })

}]);


// create the controller and inject Angular's $scope
app.controller('mainController', ["$scope", "$location", "$rootScope", "$http",
    function($scope, $location, $rootScope, $http) {
      $scope.alerts = [];
      $scope.closeAlert = function(index) {
        $scope.alerts.splice(index, 1);
      };
    }
  ])
  .filter('joinby', function() {
    return function(input, delimiter) {
      if(!input || !input.length)return '';
      return (input || []).join(delimiter || ',');
    };
  });
