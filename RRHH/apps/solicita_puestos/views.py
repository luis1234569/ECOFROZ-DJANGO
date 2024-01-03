from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import solicita_puesto
from django.shortcuts import render, get_object_or_404
from .forms import SolicitaPuestoForm
from django.core.paginator import Paginator
    
def SolicitaPuestoList(request):
    queryset = request.GET.get("buscar")
    if queryset:
        solicitudes = solicita_puesto.objects.filter(
            Q(id__icontains = queryset) |
            # Q(numpedido__numproyecto__icontains = queryset) |
            Q(puesto__icontains = queryset)
        )
    else:
        solicitudes2 = solicita_puesto.objects.all()
        paginator = Paginator(solicitudes2, 100)
        page = request.GET.get('page')
        solicitudes = paginator.get_page(page)
    
    
    
    context={
        'puestosSolicitados': solicitudes,
        'busqueda': queryset
    }
    
    return render(request, 'puestos/puestos-list.html', context)

    # queryset = request.GET.get("buscar")
    # if queryset:
    #     orden = DetallePedido.objects.filter(
    #         Q(numpedido__numpedido__icontains = queryset) |
    #         # Q(numpedido__numproyecto__icontains = queryset) |
    #         Q(descripcion__icontains = queryset)
    #     ).filter(numpedido__usuario_solicita_id = request.user.id)
    # else:
    #     orden2 = DetallePedido.objects.filter(numpedido__usuario_solicita_id = request.user.id).order_by('-numpedido__numpedido')
    
    #     paginator = Paginator(orden2, 100)
    #     page = request.GET.get('page')
    #     orden = paginator.get_page(page)
    
    # return render(request, 'ordenPedido/pedidotmp/listar_ordenes.html', {'form':orden, 'busqueda':queryset})


class SolicitaPuestoCreateView(CreateView):
    model = solicita_puesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = '/'  # Coloca la URL a la que deseas redirigir después de guardar la solicitud

    def form_valid(self, form):
        # Aquí puedes realizar acciones adicionales si el formulario es válido
        # Antes de guardar el objeto
        return super().form_valid(form)
    
class SolicitaPuestoUpdateView(UpdateView):
    model = solicita_puesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = '/'  # Coloca la URL a la que deseas redirigir después de guardar la solicitud

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(solicita_puesto, id=id_)
    
class SolicitaPuestoDeleteView(DeleteView):
    model = solicita_puesto
    template_name= 'puestos/puestos-delete.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')
    
# class SolicitaPuestoListView(ListView):
#     model= solicita_puesto
#     template_name = 'puestos/puestos-list.html'
#     context_object_name= 'puestosSolicitados'
#     # paginate_by= 27
    
#     def get_queryset(self):
#         queryset = self.request.GET.get("buscar")
#         if queryset:
#             return solicita_puesto.objects.filter(
#             Q(id__icontains= queryset) |
#             Q(puesto__icontains= queryset) 
#         )
#         else:
#             return solicita_puesto
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['busqueda'] = self.request.GET.get("buscar","")   
#         return context