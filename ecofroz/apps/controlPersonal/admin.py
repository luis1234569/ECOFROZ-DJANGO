from django.contrib import admin
from .models import Persona, Vehiculos, PersonaRegistro, VehiculoRegistro

# Register your models here.

admin.site.register (Persona)
admin.site.register (Vehiculos)
admin.site.register (PersonaRegistro)
admin.site.register (VehiculoRegistro)
