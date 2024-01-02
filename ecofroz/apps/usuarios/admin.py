from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Autorizador, Generador, Cotizador, Roles
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields':('username', 'password', 'first_name', 'last_name', 'email', 'autorizador', 'generador',
         'generador_int', 'autoriza_oti', 'cotizador', 'groups', 'soporte', 'mantenimiento', 'supervisor1', 'supervisor2',
          'is_staff', 'is_active', 'is_superuser','guardia', 'asignado_mantenimiento','consulta_experta',
          'genera_consultas_a_expertos', 'rol')}),
    )

admin.site.register (User, CustomUserAdmin)
admin.site.register (Autorizador)
admin.site.register (Generador)
admin.site.register (Cotizador)
admin.site.register (Roles)