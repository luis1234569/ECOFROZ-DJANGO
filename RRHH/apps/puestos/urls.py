from django.urls import path
from .views import *
from django.http import HttpResponse

urlpatterns = [
    path('', ListarPedidosPuesto.as_view(), name = 'generar_vacante'),
]
