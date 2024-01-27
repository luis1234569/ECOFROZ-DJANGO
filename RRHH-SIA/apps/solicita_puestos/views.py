from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import SolicitaPuesto, activo_areas, activo_ubica
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SolicitaPuestoForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.timezone import now


# listado de las solicitudes para ocupar un cargo (solicitante)
def SolicitaPuestoList(request):
    queryset = request.GET.get("buscar")
    solicitudes = SolicitaPuesto.objects.filter(solicitante_id=request.user.id)

    if queryset:
        solicitudes = solicitudes.filter(
            Q(id__icontains=queryset) |
            # Q(numpedido__numproyecto__icontains=queryset) |
            Q(cargo__icontains=queryset)
        )
    solicitudes = solicitudes.order_by('-fecha_solicitud')

    # Mueve la paginación fuera del condicional
    paginator = Paginator(solicitudes, 100)
    page = request.GET.get('page')
    puestos_paginados = paginator.get_page(page)

    context = {
        'puestosSolicitados': puestos_paginados,
        'busqueda': queryset
    }

    return render(request, 'puestos/puestos-list.html', context)
# formulario de ingreso de solicitud (solicitante)
class SolicitaPuestoCreateView(CreateView):
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ubica = activo_ubica.objects.all()
        area = activo_areas.objects.none()
        context['ubica'] = ubica
        context['area'] = area
        return context

    def form_valid(self, form):
        return super().form_valid(form)
# actualizar una solicitud (solicitante)
class SolicitaPuestoUpdateView(UpdateView):
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')

    def form_valid(self, form):
        instancia = form.save(commit=False)
        # user = self.request.user
        # instancia.solicitante = user
        instancia.estado_aprobacion = None
        instancia.estado_ingreso = None
        instancia.notasges=''
        instancia.observacion_aprueba=''
        instancia.motRechaza=''
        instancia.save()
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('erroroororor',form.errors)
        return response
            # if self.request.is_ajax:
            #     return JsonResponse(form.errors, status=400)
            # else:
            #     return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        ubicacion_solicitud = solicitud.ubicacion.id
        area_solicitud = solicitud.area.area_codigo
        ubica = activo_ubica.objects.all()
        areas = activo_areas.objects.all()
        context['ubicacion_solicitud'] = ubicacion_solicitud
        context['area_solicitud'] = area_solicitud
        context['ubica'] = ubica
        context['areas'] = areas

        context['editar'] = True
        context['motivoRechaza']= solicitud.motRechaza
        context['observacionRRHH']= solicitud.notasges
        
        return context

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(SolicitaPuesto, id=id_)
# elimina una solicitud (solicitante )
class SolicitaPuestoDeleteView(DeleteView):
    model = SolicitaPuesto
    template_name = 'puestos/puestos-delete.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')
# aprueba solicitud (gerencia)
class SolicitaPuestoApruebaUpdateView(UpdateView):
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form-aprueba.html'
    success_url = reverse_lazy(
        'solicita_puestos:listar_solicita_puesto_aprueba')

    def form_valid(self, form):
        instancia = form.save(commit=False)
        user = self.request.user
        instancia.usuario_aprueba = f"{user.first_name} {user.last_name}"
        instancia.estado_aprobacion = 1
        instancia.fecha_aprueba = now()
        instancia.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        ubicacion_solicitud = solicitud.ubicacion.id
        area_solicitud = solicitud.area.area_codigo
        ubica = activo_ubica.objects.all()
        areas = activo_areas.objects.all()
        context['ubicacion_solicitud'] = ubicacion_solicitud
        context['area_solicitud'] = area_solicitud
        context['ubica'] = ubica
        context['areas'] = areas

        context['editar'] = True
        return context

    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(SolicitaPuesto, id=id_)
# lista las solicitudes para ser aprobadas
def SolicitaPuestoListAprueba(request):
    queryset = request.GET.get("buscar")
    solicitudes_base = SolicitaPuesto.objects.exclude(estado_aprobacion=0)
    # filter(estado_aprobacion= 0 )

    if queryset:
        solicitudes_base = solicitudes_base.filter(
            Q(id__icontains=queryset) |
            Q(puesto__icontains=queryset)
        )

    solicitudes_base = solicitudes_base.order_by('-fecha_solicitud')

    paginator = Paginator(solicitudes_base, 100)
    page = request.GET.get('page')
    puestos_paginados = paginator.get_page(page)

    context = {
        'puestosSolicitados': puestos_paginados,
        'busqueda': queryset
    }

    return render(request, 'puestos/puestos-list-aprueba.html', context)
# aprobacion directa de gerencia
def SolicitarPuestoAprobar(request, pk):
    # Obtener el objeto y manejar el caso de que no exista
    solicita_puesto = get_object_or_404(SolicitaPuesto, id=pk)

    # Actualizar los campos necesarios en una sola llamada
    solicita_puesto.estado_aprobacion = 1
    solicita_puesto.fecha_aprueba = now()
    solicita_puesto.save()

    # Redirigir al usuario
    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')
# rechazo directo por gerencia
def rechazaDirect(request, pk):
    rechaza = SolicitaPuesto.objects.get(id=pk)
    if request.method == 'GET':
        rechaza.estado_aprobacion = 0
        rechaza.motRechaza = request.GET.get("text")
        rechaza.save()
    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')
# formulario (rrhh)
def SolicitaCargoNotasRRHH(request, pk):
    if request.method == 'POST':
        id = request.POST.get("pkSolicita", '')
        estado = request.POST.get("estado_ingreso", None) or None
        notas = request.POST.get("notasges", '')
        fecha = request.POST.get("fecha_inicio_proceso", '')
        querySet = SolicitaPuesto.objects.get(id=id)
        querySet.notasges = notas
        if estado:
            querySet.estado_ingreso = estado
        if estado == 1 and fecha:
            querySet.fecha_inicio_proceso = fecha
        if estado == 2  :
            querySet.estado_aprobacion = 0
        querySet.save()
        return redirect('solicita_puestos:listar_solicita_puesto_rrhh')
    solicitud = SolicitaPuesto.objects.filter(id=pk)
    context = {
        'solicitud': solicitud,
    }
    return render(request, 'puestos/puestos-form-rrhh.html', context)
# lista las solicitudes rrhh
def SolicitaPuestoListRRHH(request):
    queryset = request.GET.get("buscar")
    # area administracion
    # nuevas solicitudes aprobada
    generalQuery = SolicitaPuesto.objects.filter(
        estado_aprobacion=1).order_by('fecha_aprueba')
    if queryset:

        q1 = generalQuery.exclude(estado_ingreso=1).exclude(
            estado_ingreso=0).exclude(estado_ingreso=2)
        # q1 = SolicitaPuesto.objects.filter(activo_depar__id=108).filter(estado_aprobacion=1).order_by('fecha_aprueba')
        query_nuevas = q1.filter(
            Q(id__icontains=queryset) |
            Q(cargo__icontains=queryset) |
            Q(motivo__icontains=queryset)
        )

        q2 = generalQuery.exclude(
            estado_ingreso=None).exclude(estado_ingreso=2)

        query_proceso = q2.filter(
            Q(id__icontains=queryset) |
            Q(cargo__icontains=queryset) |
            Q(motivo__icontains=queryset))

        q3 = generalQuery.exclude(
            estado_ingreso=None)

        query_confirmadas = q3.filter(
            Q(id__icontains=queryset) |
            Q(cargo__icontains=queryset) |
            Q(motivo__icontains=queryset))

        countn = q1.count()
        countp = q2.count()
        countc = q3.count()

    else:

        queryset = None
        query_nuevas = generalQuery.exclude(
            estado_ingreso=1).exclude(estado_ingreso=0).exclude(estado_ingreso=2)

        query_proceso = generalQuery.exclude(
            estado_ingreso=None).exclude(estado_ingreso=2)

        query_confirmadas = generalQuery.exclude(
            estado_ingreso=None)

        countn = query_nuevas.count()
        countp = query_proceso.count()
        countc = query_confirmadas.count()

    context = {'form2': query_nuevas,
               'form3': query_proceso,
               'form4': query_confirmadas,
               'busqueda': queryset,
               'countn': countn,
               'countp': countp,
               'countc': countc}
    return render(request, 'puestos/puestos-list-rrhh.html', context)
# componente formulario solicita puesto
def ubicaAreaAjax(request):
    data = []
    # action = request.GET['action']
    area = request.GET['id']
    try:
        for i in activo_areas.objects.filter(area_ubica=area):
            data.append({
                'area_codigo': i.area_codigo,
                'area_nombre': i.area_nombre,
            })

        return JsonResponse(data, safe=False)
    except Exception as e:
        print(e)




def none(request):

    none = SolicitaPuesto.objects.filter(departamento__id=108).filter(
        estado_aprobacion=1).order_by('fecha_aprueba')
    context = {
        'nonelist': none
    }
    return render(request, 'puestos/none.html', context)


# def ajax_save_status(request):
#     idn = request.GET.get("id")
#     notas = request.GET.get("notasg", '')
#     confirma = request.GET.get("aprobar", None) or None
#     SolicitaPuesto.objects.filter(id=idn).update(
#         notasges=notas, estado_ingreso=confirma)
#     return redirect('solicita_puestos:listar_solicita_puesto_rrhh')