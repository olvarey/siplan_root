from .models import UnidadOrganizativa, Organizacion
from rest_framework import serializers


class OrganizacionSerializer(serializers.ModelSerializer):
    # unidades_organizativas = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Organizacion
        fields = [
            "id_organizacion",
            "nombre_organizacion",
            # @olvarey This is related with Unidad Organizativa model foreign key
            # "unidades_organizativas",
        ]


class UnidadOrganizativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadOrganizativa
        fields = [
            "id_unidad_organizativa",
            "nombre_unidad_organizativa",
            "unidad_superior",
            "organizacion",
        ]
        depth = 1
