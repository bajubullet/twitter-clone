var app = angular.module('project', []).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
}).config(function($routeProvider) {
  $routeProvider.when('/', {controller: MainCtrl,
      templateUrl:'/static/ng-templates/list.html'}).
  otherwise({redirectTo: '/'})
});


function MainCtrl($scope, $http) {
  $scope.posts = [];

  $scope.init = function() {
    $http.get('/posts/posts/.json').success(function(data) {
      $scope.posts = data;
    }).error(function(error) {
      console.log(error);
    })
  };
};

