from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

import views

urlpatterns = format_suffix_patterns(patterns('posts.views',
    url(r'^$', 'api_root', name='list-posts'),
    url(r'^posts/$', views.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(),
        name='post-detail'),
))
