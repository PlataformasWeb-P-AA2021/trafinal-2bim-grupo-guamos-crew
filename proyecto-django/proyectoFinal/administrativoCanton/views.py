from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativoCanton.serializers import UserSerializer, GroupSerializer, \
BarrioSerializer, PersonaSerializer,CasaSerializer,DepartamentoSerializer

# importar las clases de models.py
from administrativoCanton.models import *

# importar los formularios de forms.py
from administrativoCanton.forms import *

def index(request):
    casas = Casa.objects.all()
    inf_template = {'casas':casas, 'num_casas':len(casas)}
    return render(request, 'index.html', inf_template)
