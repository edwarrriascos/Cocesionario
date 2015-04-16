from django.conf.urls.defaults import patterns, url

from django.conf.urls import include
from rest_framework import routers
from concesionariom.apps.webservices.ws_productos.views import  *
router =  routers.DefaultRouter()
router.register(r'motos', moto_viewset)
router.register(r'marcas', marca_viewset)
router.register(r'categorias', categoria_viewset)
router.register(r'color', color_viewset)
router.register(r'motor', motor_viewset)



urlpatterns = patterns('concesionariom.apps.webservices.ws_productos.views',
		url(r'^ws/motos/$','ws_productos_view',name = 'ws_productos_url'),
		url(r'^api/', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_frameworks')),
		
	)