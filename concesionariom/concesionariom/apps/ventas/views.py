# vistas de la aplicacion ventas
from django.shortcuts import render_to_response
from django.template import RequestContext
from concesionariom.apps.ventas.forms import add_moto_form
from concesionariom.apps.ventas.forms import edit_moto_form
from concesionariom.apps.ventas.models import Moto
from django.http import HttpResponseRedirect

def add_motos_view(request):
	info = "inicializando" 
	save =""
	if request.method == "POST":
		formulario = add_moto_form(request.POST, request.FILES)
		if formulario.is_valid():
			m = formulario.save(commit = False)
			m.status = True
			m.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/moto/%s' %m.id)
	else:
		formulario = add_moto_form()
	ctx = {'form': formulario, 'info': info}
	return render_to_response('ventas/add_moto.html', ctx, context_instance = RequestContext(request))

	
def edit_motos_view(request, id_moto):
	info = "#" 
	save =""
	if request.method == "POST":
		formulario = add_moto_form(request.POST,request.FILES)
		informacion = "inicializando"
		if formulario.is_valid():
			p = formulario.save(commit = False)
			p.status = True
			p.save()
			formulario.save.m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/moto/%s' %p.id)
	else:
		
		formulario = add_moto_form()
	ctx = {'form': formulario, 'informacion': info}
	return render_to_response('ventas/edit_moto.html', ctx, context_instance = RequestContext(request))		

