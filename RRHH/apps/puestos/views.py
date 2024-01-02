from django.views.generic import CreateView, ListView
from .models import *
from django.shortcuts import render
# Create your views here.
class ListarPedidosPuesto(ListView):
    model = solicita_puesto
    template_name = 'puestos/puestos-list.html'
