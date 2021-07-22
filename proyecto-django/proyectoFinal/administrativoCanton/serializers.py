from django.contrib.auth.models import User, Group
from administrativoCanton.models import Barrio, Casa, Departamento, Persona

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BarrioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Barrio
        fields = '__all__'


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Persona
        fields = '__all__'


class CasaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Casa
        fields = '__all__'


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        id = serializers.IntegerField(read_only=True)
        model = Departamento
        fields = '__all__'
