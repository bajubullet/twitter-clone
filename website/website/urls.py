from django.conf import settings
from django.conf.urls import patterns, include, url
from profiles import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT.replace('\\','/')}, name='media'),
    url(r'^$', views.landing, name='landing'),
    url(r'^login/$', views.login_user, name='login-user'),
    url(r'^logout/$', views.logout_user, name='logout-user'),
    url(r'^signup/$', views.signup, name='signup-user'),
    url(r'^profile/$', views.profile, name='user-profile'),
    url(r'^search-user/$', views.search_user, name='search-user'),
    url(r'^posts/', include('posts.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
