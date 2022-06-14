from django.contrib import admin
from .models import Organizacion, UnidadOrganizativa

# Register your models here.


@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    pass


@admin.register(UnidadOrganizativa)
class UnidadOrganizativaAdmin(admin.ModelAdmin):
    pass
