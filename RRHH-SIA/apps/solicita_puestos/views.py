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


def SolicitaPuestoList(request):
    queryset = request.GET.get("buscar")
    if queryset:
        solicitudes = SolicitaPuesto.objects.filter(
            Q(id__icontains=queryset) |
            # Q(numpedido__numproyecto__icontains = queryset) |
            Q(cargo__icontains=queryset)
        ).order_by('-fecha_solicitud')
    else:
        solicitudes2 = SolicitaPuesto.objects.all().order_by('-fecha_solicitud')
        paginator = Paginator(solicitudes2, 100)
        page = request.GET.get('page')
        solicitudes = paginator.get_page(page)

    context = {
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
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')  # Coloca la URL a la que deseas redirigir después de guardar la solicitud

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ubica = activo_ubica.objects.all()
        area = activo_areas.objects.none()
        context['ubica'] = ubica
        context['area'] = area
        return context

    def form_valid(self, form):
        # Aquí puedes realizar acciones adicionales si el formulario es válido
        # Antes de guardar el objeto
        return super().form_valid(form)


class SolicitaPuestoUpdateView(UpdateView):
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')  # Coloca la URL a la que deseas redirigir después de guardar la solicitud

    def form_valid(self, form):
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


class SolicitaPuestoDeleteView(DeleteView):
    model = SolicitaPuesto
    template_name = 'puestos/puestos-delete.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto')

class SolicitaPuestoApruebaUpdateView(UpdateView):
    model = SolicitaPuesto
    form_class = SolicitaPuestoForm
    template_name = 'puestos/puestos-form.html'
    success_url = reverse_lazy('solicita_puestos:listar_solicita_puesto_aprueba') 
    def form_valid(self, form):
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
    def form_valid(self, form):
        # Modifica un campo antes de guardar
        instancia = form.save(commit=False)
        user = self.request.user
        instancia.usuario_aprueba = f"{user.first_name} {user.last_name}"
        instancia.save()
        return super(SolicitaPuestoApruebaUpdateView, self).form_valid(form)



def SolicitaPuestoListAprueba(request):
    queryset = request.GET.get("buscar")
    if queryset:
        solicitudes = SolicitaPuesto.objects.filter(
            Q(id__icontains=queryset) |
            # Q(numpedido__numproyecto__icontains = queryset) |
            Q(puesto__icontains=queryset)
        ).order_by('-fecha_solicitud')
    else:
        solicitudes2 = SolicitaPuesto.objects.all().order_by('-fecha_solicitud')
        paginator = Paginator(solicitudes2, 100)
        page = request.GET.get('page')
        solicitudes = paginator.get_page(page)

    context = {
        'puestosSolicitados': solicitudes,
        'busqueda': queryset
    }
    return render(request, 'puestos/puestos-list-aprueba.html', context)


def SolicitaCargoList(request):
    queryset = request.GET.get("buscar")
    if queryset:
        solicitudes = SolicitaPuesto.objects.filter(
            Q(id__icontains=queryset) |
            # Q(numpedido__numproyecto__icontains = queryset) |
            Q(puesto__icontains=queryset).order_by('-fecha_solicitud')
        )
    else:
        solicitudes2 = SolicitaPuesto.objects.all().order_by('-fecha_solicitud')
        paginator = Paginator(solicitudes2, 100)
        page = request.GET.get('page')
        solicitudes = paginator.get_page(page)

    context = {
        'puestosSolicitados': solicitudes,
        'busqueda': queryset
    }
    return render(request, 'puestos/puestos-list-aprueba.html', context)


def SolicitaCargoNotasRRHH(request, pk):
    if request.method == 'GET':
        solicitud = SolicitaPuesto.objects.filter(id=pk)
        detail_solicitud = SolicitaPuesto.objects.get(id=pk)
        note = detail_solicitud.notasges
        context = {
            'solicitud': solicitud,
            'note': note
        }

    return render(request, 'puestos/puestos-form-rrhh.html', context)


def SolicitaPuestoListRRHH(request):
    queryset = request.GET.get("buscar")
    # area administracion
    # nuevas solicitudes aprobada
    generalQuery = SolicitaPuesto.objects.filter(departamento__id=108).filter(
        estado_aprobacion=1).order_by('fecha_aprueba')
    if queryset:

        q1 = generalQuery.exclude(estado_ingreso=1).exclude(estado_ingreso=0)
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
            estado_ingreso=None).exclude(estado_ingreso=2)

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
            estado_ingreso=1).exclude(estado_ingreso=0)

        query_proceso = generalQuery.exclude(
            estado_ingreso=None).exclude(estado_ingreso=2)

        query_confirmadas = generalQuery.exclude(
            estado_ingreso=None).exclude(estado_ingreso=2)

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


def none(request):
    none = SolicitaPuesto.objects.filter(departamento__id=108).filter(
        estado_aprobacion=1).order_by('fecha_aprueba')
    context = {
        'nonelist': none
    }
    return render(request, 'puestos/none.html', context)


def SolicitarPuestoAprobar(request, pk):
    SolicitaPuesto.objects.filter(id=pk).update(estado_aprobacion=1)
    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')


def rechazaDirect(request, pk):
    rechaza = SolicitaPuesto.objects.get(id=pk)
    if request.method == 'GET':
        rechaza.estado_aprobacion = 0
        rechaza.motRechaza = request.GET.get("text")
        rechaza.save()
    noend= SolicitaPuesto.objects.get(id=pk)
    print(noend,'dddddd')
    return redirect('solicita_puestos:listar_solicita_puesto_aprueba')


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


def ajax_save_status(request):
    idn = request.GET.get("id")
    notas = request.GET.get("notasg", 'No ingreso notas')
    confirma = request.GET.get("aprobar", None) or None
    SolicitaPuesto.objects.filter(id=idn).update(
        notasges=notas, estado_ingreso=confirma)
    msg = ""
    if confirma == '1':
        msg = "aprobado"
    elif confirma == '2':
        msg = "rechazado"
    return JsonResponse(msg, safe=False)


def ajax_save(request):
    idn = request.GET.get("id")
    notas = request.GET.get("notasg", 'Notas')
    SolicitaPuesto.objects.filter(id=idn).update(notasges=notas)
    return JsonResponse("Exito", safe=False)
