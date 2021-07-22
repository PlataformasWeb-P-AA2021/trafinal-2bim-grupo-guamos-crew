from django.contrib import admin

# Register your models here.
from administrativoCanton.models import Barrio, Casa, Departamento, Persona


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('nombre_barrio', 'siglas')
    search_fields = ('nombre_barrio', 'siglas')


admin.site.register(Barrio, BarrioAdmin)


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'cedula', 'correo')
    search_fields = ('nombres', 'apellidos')


admin.site.register(Persona, PersonaAdmin)


class CasaAdmin(admin.ModelAdmin):
    list_display = ('prop_casa', 'direccion_casa', 'valor_casa', 'color', 'cuartos_casa', 'pisos', 'barrio')
    search_fields = ('barrio', 'prop_casa', 'direccion_casa')


admin.site.register(Casa, CasaAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('prop_dept', 'direccion_dept', 'valor_dept', 'cuartos_dept', 'mensualidad', 'barrio')
    search_fields = ('barrio', 'prop_dept', 'direccion_dept')


admin.site.register(Departamento, DepartamentoAdmin)
