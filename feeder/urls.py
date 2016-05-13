from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feeder.views.home', name='home'),
    # url(r'^feeder/', include('feeder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^', include('reader.urls')),
    url(r'^reader/', include('reader.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
