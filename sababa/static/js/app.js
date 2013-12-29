var app = angular.module('app', ['ngRoute','ngResource','ui.bootstrap','ui.router'], function($interpolateProvider, $locationProvider, $stateProvider, $urlRouterProvider, $routeProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

    $locationProvider.html5Mode(true);

    $urlRouterProvider.otherwise("/home");

    $stateProvider
        .state('home', {
          url: "/home",
          templateUrl: "/static/html/browse/home.html",
            controller: 'HomeCtrl'
        });
});

app.controller('HomeCtrl', function($scope, OfferFactory){
    $scope.test = 0;
});
