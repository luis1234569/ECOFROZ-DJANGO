from django.contrib import admin
from .models import OrdenesTrabajos, DetalleTrabajo, CotizaTrabajo

# Register your models here.

admin.site.register (OrdenesTrabajos)
admin.site.register (DetalleTrabajo)
admin.site.register (CotizaTrabajo)