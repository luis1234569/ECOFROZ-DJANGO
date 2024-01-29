from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.procesosAdministrativos.models import *
import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def accesos(request):
    user= request.user
    cabeceras = CabRegistroAccesoUbica.objects.filter(usuario= user).order_by('-fecha_hora_ingreso').prefetch_related('detregistroaccesoubica_set')

    return render(request, 'listar_lugares.html', {'cabeceras': cabeceras})

def registerIngresoSalida(request, code_qr):
    user = request.user
    validate_qr = CodigoQrAreas.objects.get(codigo_qr =code_qr)
    try:
        ingreso_salida = CabRegistroAccesoUbica.objects.filter(usuario=user).order_by('-fecha_hora_ingreso').first()
    except ObjectDoesNotExist:
        ingreso_salida = None
        
    if validate_qr is None:
        return HttpResponse("El codigo QR no es válido", status=403)
    else:
        if ingreso_salida:
            if ingreso_salida.fecha_hora_salida:
                cab=CabRegistroAccesoUbica.objects.create(
                usuario= user,
                username= user.username,
                fecha_hora_ingreso= datetime.datetime.now()
                )
                addDetalle(cab)
            else:
                ingreso_salida.fecha_hora_salida= datetime.datetime.now()
                ingreso_salida.completado= 1
                ingreso_salida.save()
        else:
            cabnew=CabRegistroAccesoUbica.objects.create(
                usuario= user,
                username= user.username,
                fecha_hora_ingreso= datetime.datetime.now()
            )
            addDetalle(cabnew)
            
    return render(request,'hello.html')

def registerCodeQR(request, code_qr):
    user = request.user
    validate_qr = CodigoQrAreas.objects.get(codigo_qr =code_qr)
    cabecera = CabRegistroAccesoUbica.objects.filter(usuario=user).order_by('-fecha_hora_ingreso').first()
    if validate_qr is None:
        return HttpResponse("El codigo QR no es válido", status=403)
    else:
        if cabecera.fecha_hora_salida:
            return HttpResponse("Usted no ha ingresado correctamente", status=403)
        else:
            print(cabecera.id)
            print(validate_qr.area.area_codigo)
            detalle = DetRegistroAccesoUbica.objects.filter(cab_registro=cabecera.id, area=validate_qr.id).first()
            print(detalle.id)
            detalle.completado = 1
            detalle.save()
    return redirect('procesosadministrativos:accesos')


def generateCodigoQR(request, code_qr):
    return render()


def addDetalle(cabecera):
    lugares_visita= [13,14,15,16,17,18,19]
    for i in lugares_visita:
        area_local= CodigoQrAreas.objects.get(area = i)
        DetRegistroAccesoUbica.objects.create(
            cab_registro= cabecera,
            area = area_local
        )