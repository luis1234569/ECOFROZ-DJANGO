from django.shortcuts import render
from django.http import HttpResponse
from apps.procesosAdministrativos.models import *
import datetime

# Create your views here.
def listarInformacion(request):
    return render()

def registerIngresoSalida(request, code_qr):
    user = request.user
    # Aquí va el código para registrar la entrada o salida de un usuario
    validate_qr = CodigoQrAreas.objects.get(codigo_qr =code_qr)
    ingreso_salida = CabRegistroAccesoUbica.objects.get(usuario=user)
    if validate_qr is None:
        return HttpResponse("El codigo QR no es válido", status=403)
    else:
        if ingreso_salida:
            if ingreso_salida.fecha_hora_salida:
                CabRegistroAccesoUbica.objects.create(
                usuario= user,
                username= user.username,
                fecha_hora_ingreso= datetime.datetime.now()
                )
            else:
                ingreso_salida.fecha_hora_salida= datetime.datetime.now()
                ingreso_salida.completado= 1
        else:
            CabRegistroAccesoUbica.objects.create(
                usuario= user,
                username= user.username,
                fecha_hora_ingreso= datetime.datetime.now()
            )
            
    
    return render()

def registerCodeQR(request, code_qr):
    return render()


def generateCodigoQR(request, code_qr):
    return render()