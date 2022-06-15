import django


from django.urls import path
from .views import (
    OrganizacionDetail,
    OrganizacionList,
    UnidadOrganizativaList,
    UnidadOrganizativaDetail,
)

urlpatterns = [
    path("organizaciones/", OrganizacionList.as_view()),
    path("organizaciones/<int:pk>/", OrganizacionDetail.as_view()),
    path("unidades-organizativas/", UnidadOrganizativaList.as_view()),
    path("unidades-organizativas/<int:pk>/", UnidadOrganizativaDetail.as_view()),
]
