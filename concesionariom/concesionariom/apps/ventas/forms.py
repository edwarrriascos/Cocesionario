from django import forms
from concesionariom.apps.ventas.models import Moto 



class add_moto_form(forms.ModelForm):
	class Meta:
		model   = Moto
		exclude = {'status',}
		

class edit_moto_form(forms.ModelForm):
	class Meta:
		model = Moto
		exclude = {'status',}

	

		
		