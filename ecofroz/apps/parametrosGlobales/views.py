from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from django.db.models import Q, Count
from .models import *
from apps.procesosAdministrativos.models import RutaTransporte
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect, HttpResponse, FileResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.template import defaultfilters
# from apps.ordenTrabajo import models
# from apps.ordenPedido import models

# Create your views here.


@login_required
def parametrosRutas(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        queryset = RutaTransporte.objects.filter(Q(codigo_ruta__icontains=busqueda) | 
        Q(origen__icontains=busqueda)| Q(destino__icontains=busqueda))
    
    else:
        query = RutaTransporte.objects.all().order_by('-id')

        paginator = Paginator(query, 4)
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

    return render(request, 'parametrosGlobales/administracion/listar_rutas.html',{'queryset':queryset,'busqueda':busqueda})






@login_required
def updateEstadoProyectos(request):
    return redirect('parametrosglobales:parametros_proyectos')

@login_required
def parametrosProyectos(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        queryset = proyectos_contabilidad.objects.filter(Q(nombre_proyecto__icontains=busqueda) | 
        Q(codigo_proyecto__icontains=busqueda))
    
    else:
        query = proyectos_contabilidad.objects.all().order_by('-id')

        paginator = Paginator(query, 5)
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

    return render(request, 'parametrosGlobales/contabilidad/listar_proyectos.html',{'queryset':queryset,'busqueda':busqueda})

@login_required
def registraNuevo(request):
    proyecto = request.GET.get("registro_proyecto")
    codigo = request.GET.get("codigo_proyecto")

    print(proyecto)

    for i in range(1):
        r = proyectos_contabilidad(
            nombre_proyecto = proyecto,
            codigo_proyecto = codigo,
            activo = True,
            fecha_creacion = datetime.today(),
            fecha_modifica = datetime.today(),
            persona_edita = request.user.username,
            )
        r.save()
 
    
    return redirect ('parametrosglobales:parametros_rutas')

@login_required
def actualizaEstadoProyectos(request):
    if request.method == 'POST':
        valor_radio = request.POST.get("radio")
        id = request.POST.get("proyec")
        fecha = datetime.today()
        nombre = request.POST.get("registro_proyecto")
        codigo = request.POST.get("codigo_proye")

        if valor_radio == "SI":
            actualiza = proyectos_contabilidad.objects.filter(id=id).update(activo=True,fecha_modifica=fecha,persona_edita=request.user.username,
            nombre_proyecto=nombre,codigo_proyecto=codigo)
        else:
            actualiza = proyectos_contabilidad.objects.filter(id=id).update(activo=False,fecha_modifica=fecha,persona_edita=request.user.username,
            nombre_proyecto=nombre,codigo_proyecto=codigo)
        
    return redirect ('parametrosglobales:parametros_proyectos')


def ajax_call(request):
    id = request.GET["id"]
    proyecto = proyectos_contabilidad.objects.filter(id=id) 
    
    context = []
    for i in proyecto:
        d = {
            'proyecto':i.nombre_proyecto,
            'codigo_proye':i.codigo_proyecto,
            'estado':i.activo,
            'id':i.id,
        }
        context.append(d)

    return JsonResponse (context, safe=False)

### FUNCIONES PARA NOTIFICACIONES GLOBALES ###
def notifica(request):
    usu = request.user.id
    data = []
    queryset = notificaciones_globales.objects.filter(autorizador_id=usu).order_by('-fecha_registro')[:5]
    
    for i in queryset:
        modelo = i.app_origen.model
        
        if i.app_origen.id == 1:
            from apps.ordenTrabajo import models
            print('Aqui el error' + str(i.identificador))
            noti = getattr(models, modelo).objects.get(numtrabajo=i.identificador)
        elif i.app_origen.id == 2:
            from apps.ordenPedido import models
            noti = getattr(models, modelo).objects.get(numpedido=i.identificador) 
        elif i.app_origen.id == 3:
            from apps.trabajosInternos import models
            noti = getattr(models, modelo).objects.get(numtrabajo=i.identificador)
        elif i.app_origen.id == 4:
            from apps.ordenPedido import models
            print(i.identificador)
            noti = getattr(models, modelo).objects.filter(numpedido=i.identificador).last()
        elif i.app_origen.id == 5:
            from apps.ordenTrabajo import models
            noti = getattr(models, modelo).objects.filter(numtrabajo=i.identificador).last()
        
        if i.app_origen.id == 1  or i.app_origen.id == 2 or i.app_origen.id == 3:

            d={
                'id':i.identificador,
                'desc':noti.descripcion[:80],
                'estado':i.estado,
                'nid':i.id,
                'url_1':i.tipo.url_tipo,
                'url_2':i.tipo.url_lista,
                'abrev':i.tipo.nombre_abreviado,
                'fec':datetime.strftime((i.fecha_registro - timedelta(hours=5)), '%d %b %H:%M'),
                'solic':i.usuario_activa.username,
            }
            data.append(d)
            
        
        elif i.app_origen.id == 4 or i.app_origen.id == 5: # CONSULTA A ROL EXPERTO

            d={
                'id':i.identificador,
                'desc':noti.pregunta[:80],
                'estado':i.estado,
                'nid':i.id,
                'url_1':i.tipo.url_tipo,
                'url_2':i.tipo.url_lista,
                'abrev':i.tipo.nombre_abreviado,
                'fec':datetime.strftime((i.fecha_registro - timedelta(hours=5)), '%d %b %H:%M'),
                'solic':i.usuario_activa.username,
            }
            data.append(d)

    return JsonResponse(data, safe=False)

def desactivanotifica(request):
    id = request.GET['id']
    data = []
    queryset = notificaciones_globales.objects.get(id=id)
    queryset.estado = False
    queryset.save()

    d={
        'id':queryset.identificador,
        'url_1':queryset.tipo.url_tipo,
        'url_2':queryset.tipo.url_lista,
    }
    data.append(d)
    
    return JsonResponse(data, safe=False)




