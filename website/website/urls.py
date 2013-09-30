from django.conf.urls import patterns, include, url
from profiles.views import signup, login_user, landing
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', landing, name='landing'),
    url(r'^login/$', login_user, name='login-user'),
    url(r'^signup/$', signup, name='signup-user'),
    url(r'^posts/', include('posts.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
