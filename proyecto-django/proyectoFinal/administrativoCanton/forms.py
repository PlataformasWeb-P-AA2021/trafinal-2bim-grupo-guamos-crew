from django.db.models import fields
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativoCanton.models import Departamento,Casa,Persona,Barrio

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre_barrio','siglas']

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['prop_dept', 'direccion_dept', 'valor_dept', 'cuartos_dept', 'mensualidad', 'barrio']

class CasaForm(ModelForm):
    class Meta: 
        model = Casa
        fields = ['prop_casa', 'direccion_casa', 'valor_casa', 'color', 'cuartos_casa', 'pisos', 'barrio']