"""
    Manejo de urls para la aplicación
    administrativoCanton
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
