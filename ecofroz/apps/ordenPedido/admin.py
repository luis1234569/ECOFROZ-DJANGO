from django.contrib import admin
from .models import OrdenesPedidos, DetallePedido, CotizaPedido

# Register your models here.

admin.site.register (OrdenesPedidos)
admin.site.register (DetallePedido)
admin.site.register (CotizaPedido)
