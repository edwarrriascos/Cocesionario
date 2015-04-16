from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('concesionariom.apps.ventas.views',
		url(r'^add/moto/$','add_motos_view', name = 'vista_agregar_motos'), 
		url(r'^edit/motos(?P<id_moto>.*)/$', 'edit_motos_view', name = 'vista_editar_motos'),
		

	)