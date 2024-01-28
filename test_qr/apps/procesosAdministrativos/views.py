from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.procesosAdministrativos.models import *
import datetime
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
# def listarInformacion(request):
#     cabeceras = CabRegistroAccesoUbica.objects.all()
#     detalles = DetRegistroAccesoUbica.objects.all()

#     return render(request, 'listar_lugares.html', {'cabeceras': cabeceras, 'detalles': detalles})

def lista(request):
    user= request.user
    cabeceras = CabRegistroAccesoUbica.objects.filter(usuario= user).prefetch_related('detregistroaccesoubica_set')
    # 'detregistroaccesoubica_set' es el nombre por defecto de la relación inversa en el modelo CabRegistroAccesoUbica

    return render(request, 'listar_lugares.html', {'cabeceras': cabeceras})

def registerIngresoSalida(request, code_qr):
    user = request.user
    print(user)
    # Aquí va el código para registrar la entrada o salida de un usuario
    validate_qr = CodigoQrAreas.objects.get(codigo_qr =code_qr)
    try:
        ingreso_salida = CabRegistroAccesoUbica.objects.get(usuario=user)
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
    # Aquí va el código para registrar la entrada o salida de un usuario
    validate_qr = CodigoQrAreas.objects.get(codigo_qr =code_qr)
    cabecera = CabRegistroAccesoUbica.objects.get(usuario=user)
    if validate_qr is None:
        return HttpResponse("El codigo QR no es válido", status=403)
    else:
        if cabecera.fecha_hora_salida:
            return HttpResponse("Usted no ha ingresado correctamente", status=403)
        else:
            detalle = DetRegistroAccesoUbica.objects.get(cab_registro_id=cabecera.id, area=validate_qr.area)
            detalle.completado = 1
            detalle.save()
    return redirect('procesosAdministrativos:accesos')


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