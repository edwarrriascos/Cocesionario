from rest_framework import serializers
from concesionariom.apps.ventas.models import Moto, Marca, Categoria, Color, Motor

class moto_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Moto
		fields = ('url',  'nombre', 'descripcion', 'status',  'imagen', 'precio', 'stock', 'categorias')

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url',  'nombre', 'status')
	
class categoria_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Categoria
		fields = ('url','nombre', 'descripcion')


class color_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Color
		fields = ('url','nombre', 'status')


class motor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Motor
		fields = ('url','nombre', 'cuatro_TiemposDOHC', 'dos_TiemposSOHC', 'status')				
	


	
		