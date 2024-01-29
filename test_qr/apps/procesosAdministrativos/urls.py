from django.urls import path
from .views import *

urlpatterns = [
    path('registro_ingreso_salida/<str:code_qr>', registerIngresoSalida, name="registro_ingreso_salida"),
    path('accesos/', accesos, name="accesos"),
    path('registro_qr/<str:code_qr>',registerCodeQR, name="register_qr")
]
