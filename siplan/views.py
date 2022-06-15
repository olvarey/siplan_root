from rest_framework import generics
from .models import UnidadOrganizativa, Organizacion
from .serializers import UnidadOrganizativaSerializer, OrganizacionSerializer


class OrganizacionList(generics.ListCreateAPIView):
    queryset = Organizacion.objects.all().order_by("id_organizacion")
    serializer_class = OrganizacionSerializer
    filterset_fields = ["id_organizacion", "nombre_organizacion"]


class OrganizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer


class UnidadOrganizativaList(generics.ListCreateAPIView):
    queryset = UnidadOrganizativa.objects.all().order_by("id_unidad_organizativa")
    serializer_class = UnidadOrganizativaSerializer


class UnidadOrganizativaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UnidadOrganizativa.objects.all()
    serializer_class = UnidadOrganizativaSerializer
