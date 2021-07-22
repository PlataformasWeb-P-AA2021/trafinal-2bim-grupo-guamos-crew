"""
    Manejo de urls para la aplicación
    administrativoCanton
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Ruta Casa
    path('crear/casa', views.crear_casa, name = 'crear_casa'),
    path('editar/casa/<int:id>', views.editar_casa, name = 'editar_casa'),
    path('eliminar/casa/<int:id>', views.eliminar_casa,name='eliminar_casa'),
    path('mostrar/casas', views.ver_casas,name='ver_casas'),
    # Rutas Departamento
    path('crear/departamento', views.crear_departamento, name = 'crear_departamento'),
    path('editar/departamento/<int:id>', views.editar_departamento, name = 'editar_departamento'),
    path('eliminar/departamento/<int:id>', views.eliminar_departamento,name='eliminar_departamento'),
    path('mostrar/departamentos', views.ver_casas,name='ver_departamentos'),
    # Rutas Persona
    path('crear/persona', views.crear_persona, name = 'crear_persona'),
    path('editar/persona/<int:id>', views.editar_persona, name = 'editar_persona'),
    path('eliminar/persona/<int:id>', views.eliminar_persona,name='eliminar_persona'),
    # Rutas Barrio
    path('crear/barrio', views.crear_barrio, name = 'crear_barrio'),
    path('editar/barrio/<int:id>', views.editar_barrio, name = 'editar_barrio'),
    path('eliminar/barrio/<int:id>', views.eliminar_barrio,name='eliminar_barrio'),
    # Rutas de Autentificación
    path('saliendo/logout/', views.logout_view, name="logout_view"),
    path('entrando/login/', views.ingreso, name="login"),
]
