from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('concesionariom.apps.home.views',
		url(r'^$', 'index_view', name = 'vista_principal'),
		url(r'^about/$', 'about_view', name = 'vista_about'),
		url(r'^motos/page/(?P<pagina>.*)/$', 'motos_view', name = 'vista_motos'),
		url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
		url(r'^administrador/$', 'administrador_view', name = 'vista_administrador'),
		url(r'^color/$', 'color_view', name = 'vista_color'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^motos/(?P<id_moto>.*)/$', 'single_moto_view', name = 'vista_single_moto'),
		
		)