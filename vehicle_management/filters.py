# filters.py: Define un filtro para los vehículos basado en el nombre de la marca.
# Esto permite filtrar los vehículos por el nombre de la marca de forma que si se
# proporciona un parámetro de consulta "nombre_marca" en la solicitud, se devolverán solo los
# vehículos cuya marca contenga la cadena especificada.


from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from vehicle_management.models import Vehiculo


class VehiculoFilter(FilterSet):
    nombre_marca = CharFilter(field_name="marca__nombre", lookup_expr='icontains')

    class Meta:
        model = Vehiculo
        fields = ['modelo', 'color']