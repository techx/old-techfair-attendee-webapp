from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mobileapp.views.home', name='home'),
    # url(r'^mobileapp/', include('mobileapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/$', 'map.views.index'),
    url(r'^company/$', 'company.views.index'),
    url(r'^map/search/$', 'map.views.search'),
    url(r'^company/(\d+)/$', 'company.views.view'), 
    url(r'^$', 'mobileapp.views.home', name='home'),

)
urlpatterns += staticfiles_urlpatterns()
