from django.db import models
from django.conf.urls.defaults import url

# Create your models here.

class Color (models.Model):
	nombre      = models.CharField(max_length = 200)
	status      = models.BooleanField(default = True)

	def  __unicode__(self):
		return self.nombre



class Motor(models.Model):
	
	nombre =  models.CharField(max_length = 200)
	cuatro_TiemposDOHC  = models.CharField(max_length = 100)
	dos_TiemposSOHC  = models.CharField(max_length = 100) 
	status      = models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre

		

class Marca(models.Model):
	nombre       =  models.CharField(max_length = 100)
	status       =  models.BooleanField(default = True)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre        = models.CharField(max_length = 100)
	descripcion   = models.TextField(max_length = 500)

	def __unicode__(self):
		return self.nombre
			
									

class Moto(models.Model):

	def url(self, filename):
		ruta = "MultimediaData/Moto/%s/%s"%(self.nombre, str(filename))
		return ruta
		
	nombre        = models.CharField(max_length = 100)
	descripcion   = models.CharField(max_length = 500)
	status        = models.BooleanField(default = True)
	imagen        = models.ImageField(upload_to = url, null = True, blank =True)
	precio        = models.DecimalField(max_digits = 10, decimal_places = 2)
	stock         = models.IntegerField()
	categorias    = models.ManyToManyField(Categoria, null = True, blank = True)
	     

	def __unicode__(self):
		return self.nombre




	


