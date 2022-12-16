from django.contrib import admin
from appPrueba.models import Inscripcion
# Register your models here.

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut']

admin.site.register(Inscripcion, InscripcionAdmin)
