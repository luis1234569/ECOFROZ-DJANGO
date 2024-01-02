from django.views.generic import CreateView, ListView
from .models import solicita_puesto
from django.shortcuts import render
    
def ListarPedidosPuesto(request):

    puestosSolicitados= solicita_puesto.objects.all()
    context={
        'puestosSolicitados': puestosSolicitados
    }
    
    return render(request, 'puestos/puestos-list.html', context)
