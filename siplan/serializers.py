from .models import UnidadOrganizativa
from rest_framework import serializers


class UnidadOrganizativaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadOrganizativa
        fields = [
            "id_unidad_organizativa",
            "nombre_unidad_organizativa",
            "id_organizacion",
            "id_unidad_superior",
        ]
