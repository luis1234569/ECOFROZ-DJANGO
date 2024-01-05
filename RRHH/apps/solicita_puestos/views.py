from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import solicita_puesto, activo_areas, activo_ubica
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitaPuestoForm
from django.core.paginator import Paginator
from django.http import JsonResponse
    
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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ubica = activo_ubica.objects.all()
        area = activo_areas.objects.none()
        context['ubica'] =  ubica
        context['area'] =  area
        return context

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        solicitud = self.model.objects.get(id=pk) 
        ubicacion_solicitud = solicitud.ubicacion.id
        area_solicitud= solicitud.area.area_codigo
        ubica = activo_ubica.objects.all()
        areas = activo_areas.objects.all()
        print(ubicacion_solicitud)
        context['ubicacion_solicitud']= ubicacion_solicitud
        context['area_solicitud']= area_solicitud
        context['ubica'] =  ubica
        context['areas'] =  areas
        
        context['editar'] = True
        return context
    
    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(solicita_puesto, id=id_)
    
class SolicitaPuestoDeleteView(DeleteView):
    model = solicita_puesto
    template_name= 'puestos/puestos-delete.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')
    
def SolicitaPuestoListAprueba(request):
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
    return render(request, 'puestos/puestos-list-aprueba.html', context)

def SolicitaPuestoListRRHH(request):
    queryset = request.GET.get("buscar")
    if queryset:
        solicitudes = solicita_puesto.objects.filter(
            Q(id__icontains = queryset) |
            Q(puesto__icontains = queryset)
        ).filter(estado_aprobacion=1)
    else:
        solicitudes2 = solicita_puesto.objects.filter(estado_aprobacion=1)
        paginator = Paginator(solicitudes2, 100)
        page = request.GET.get('page')
        solicitudes = paginator.get_page(page)
        
    context={
        'puestosSolicitados': solicitudes,
        'busqueda': queryset
    }
    return render(request, 'puestos/puestos-list-rrhh.html', context)

def SolicitaCargoList(request):
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
    return render(request, 'puestos/puestos-list-aprueba.html', context)
    
def SolicitarPuestoAprobar(request, pk):
    solicita_puesto.objects.filter(id=pk).update(estado_aprobacion=1)
    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')

def rechazaDirect(request, numpedido):
    pedido = request.GET.get("pedido")
    rechaza = solicita_puesto.objects.get(numpedido=pedido)
    if request.method == 'GET':
        rechaza.aprobado = 0
        rechaza.motRechaza = request.GET.get("text")
        rechaza.save()

    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')

def ubicaAreaAjax(request):
    data = []
    # action = request.GET['action']
    area = request.GET['id']
    print('hola' + ' ' + area)
    try:
        for i in activo_areas.objects.filter(area_ubica=area):
            data.append({
                'area_codigo': i.area_codigo,
                'area_nombre': i.area_nombre,
            })

        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)
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