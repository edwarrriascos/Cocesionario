from django.conf.urls.defaults import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config 
dajaxice_autodiscover()
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concesionariom.views.home', name='home'),
    # url(r'^concesionariom/', include('concesionariom.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^',include('concesionariom.apps.home.urls')),
     url(r'^',include('concesionariom.apps.ventas.urls')),
     url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
     url(r'^',include('concesionariom.apps.webservices.ws_productos.urls')),
     
    )
    
