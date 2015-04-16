# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from concesionariom.apps.home.forms import contact_form, Login_form
from concesionariom.apps.ventas.models import Moto
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.mail import EmailMultiAlternatives 



def index_view(request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

def about_view(request):
	mensaje = "este es un mensaje desde mi vista"
	ctx = {'msg': mensaje}  
	return render_to_response('home/about.html', context_instance = RequestContext(request))


def motos_view(request,pagina):
	p = Moto.objects.filter(status = True)	
	paginator = Paginator(p, 3) 
	
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		motos = paginator.page(page)	
	except (EmptyPage, InvalidPage):
		motos = paginator.page(paginator.rum_pages)
		
	ctx ={'motos':motos}
	return render_to_response ('home/motos.html', ctx, context_instance = RequestContext(request))


	

def contacto_view(request):
	info_enviado = ""
	email = ""
	title = ""
	text  = ""
	if request.method == "POST":
		formulario = contact_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text  = formulario.cleaned_data['texto']
			''' Bloque conficugraion de envio por GMAIL'''
			to_admin = 'edwarr941@gmail.com'
			html_content = "Informacio recibida de %s <br>---Mensaje---<br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
			''' Fin del Bloque '''
	else:
		formulario = contact_form()
	ctx = {'form': formulario, 'email':email, "title":title, "text":text, "info_enviado":info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))	

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje ="usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form':formulario, 'mensaje':mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))	

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def single_moto_view(request, id_moto):
	mot = Moto.objects.get(id = id_moto)
	cat = mot.categorias.all()
	ctx = {'moto':mot, 'categorias': cat}
	return render_to_response('home/single_moto.html', ctx,context_instance = RequestContext(request))	




def administrador_view(request):
	return render_to_response('ventas/administrador.html', context_instance = RequestContext(request))

def color_view(request):
	return render_to_response('ventas/color.html', context_instance = RequestContext(request))
