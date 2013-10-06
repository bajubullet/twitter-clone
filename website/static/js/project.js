var app = angular.module('project', []).config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
}).config(function($routeProvider) {
  $routeProvider.when('/', {controller: MainCtrl,
      templateUrl:'/static/ng-templates/list.html'}).
  when('/user/:username', {controller: MainCtrl,
      templateUrl: '/static/ng-templates/list.html'}).
  otherwise({redirectTo: '/'})
}).config(function($httpProvider) {
  $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
}).service('postService', function() {
  var posts = [];
  return {
    getPosts: function() {
      return posts;
    },
    append: function(post) {
      posts.push(post);
    },
    extend: function(postList) {
      posts = posts.concat(postList);
    },
    set: function(postList) {
      posts = postList;
    }
  }
});


function MainCtrl($scope, $http, $routeParams, postService) {
  $scope.username = $routeParams.username;
  $scope.posts = [];

  $scope.init = function() {
    $http.get('/posts/posts/.json', {params: {'username': $scope.username}}).
    success(function(data) {
      postService.set(data);
      $scope.posts = postService.getPosts();
    }).error(function(error) {
      console.log(error);
    })
  };
};


function CreateCtrl($scope, $http, postService) {
  $scope.savePost = function() {
    var data = {'content': $scope.postContent}
    $http.post('posts/posts/', data).success(function(data) {
      postService.append(data);
      $('#id-preparePost').modal('hide');
    }).error(function(error) {
      console.log(error);
    })
  };

  $scope.remaining = function() {
    if ($scope.postContent) {
      return 140 - $scope.postContent.length;
    }
    return 140;
  };

  $scope.validPostLength = function() {
    return $scope.remaining() < 0;
  }
}
