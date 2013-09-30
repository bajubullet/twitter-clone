from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = format_suffix_patterns(patterns('posts.views',
    url(r'^$', 'api_root', name='list-posts'),
    url(r'^posts/$', views.PostViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostViewSet.as_view(
        {
          'get': 'retrieve',
          'put': 'update',
          'patch': 'partial_update',
          'delete': 'destroy'
        }), name='post-detail'),
))
