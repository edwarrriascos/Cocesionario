# Create your views here.
from django.http import HttpResponse
from concesionariom.apps.ventas.models import *
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("json",Moto.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/json')


from .serializers import *
from rest_framework import viewsets


class moto_viewset(viewsets.ModelViewSet):
	queryset= Moto.objects.all()
	serializer_class = moto_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer


class color_viewset(viewsets.ModelViewSet):
	queryset = Color.objects.all()
	serializer_class = color_serializer


class motor_viewset(viewsets.ModelViewSet):
	queryset = Motor.objects.all()
	serializer_class = motor_serializer





 	 