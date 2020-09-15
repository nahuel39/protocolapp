from django.contrib import admin
from proapp.models import Visitas,Positivo, Negocio
# Register your models here.


class VisitasAdmin(admin.ModelAdmin):
    pass

admin.site.register(Visitas,VisitasAdmin)