# serializers.py: Define los serializadores para convertir los objetos
# de Django en representaciones JSON y viceversa. Esto se utiliza para la serialización
# y deserialización de los datos cuando se realizan solicitudes HTTP a la API.



from django.contrib.auth.models import Group, User
from rest_framework import serializers

from vehicle_management.models import Vehiculo, Marca


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Vehiculo
        fields = ['url', 'tipo', 'chasis', 'marca', 'modelo', 'matricula', 'color', 'fecha_fabricacion', 'fecha_matriculacion',
                  'fecha_baja', 'suspendido']


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = ['url', 'nombre']
