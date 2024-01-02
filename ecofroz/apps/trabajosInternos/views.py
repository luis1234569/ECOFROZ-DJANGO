import logging
from rest_framework.generics import ListAPIView
from .serializers import SectoresSerializer
from django.shortcuts import render, redirect, get_object_or_404
from apps.activos.models import activo_depar, activo_areas
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404, FileResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse
from datetime import datetime, date, timedelta
from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils import timezone, formats
from django.db.models import Q
from .models import *
from .forms import *
from apps.ordenTrabajo.forms import TrabajoAutoriForm2, EditaDetTrForm2
from apps.ordenTrabajo.models import OrdenesTrabajos, DetalleTrabajo, TipoPedido
from apps.activos.models import activo_ubica
from django.template import context, loader
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from apps.usuarios.models import *
from apps.parametrosGlobales.models import tipo_notificacion, modelo_App, notificaciones_globales, proyectos_contabilidad

logger = logging.getLogger(__name__)


def envioMail(subject, email, template, queryset, queryset2):
    html_message = loader.render_to_string(
        'trabajosInternos/email/%s' %template,
            {
                'aprob':queryset,
                'aprob2':queryset2,
            }
        )
    email_subject = subject
    to_list = email.split(',')
    mail = EmailMultiAlternatives(
            email_subject, '', '', (to_list), bcc=['desarrolloecofroz@gmail.com'])
    mail.attach_alternative(html_message, "text/html")
    try:
        mail.send()
    except:
        logger.error("Unable to send mail.")

@login_required
def ingresoOrdenes(request):
    if request.method == "GET":
        # form = ingresoTrabajos(request.GET or None)
        
        form = cabIngresoTrabajos(request.GET or None)
        form2 = detIngresoTrabajos(request.GET or None)

        return render(request, 'trabajosInternos/ingreso.html', {'form':form, 'form2':form2})
    else:
        form = cabIngresoTrabajos(request.POST)
        form2 = detIngresoTrabajos(request.POST, request.FILES)
        sector = request.POST.get("nsector")
        print("nsector")

        if form.is_valid() and form2.is_valid():
            cab = form.save(commit=False)
            cab.area = sector
            cab.usuario_solicita_id = request.user.id
            cab.save()
            fecha = datetime.today()
            # fec = datetime.strftime(fecha, '%Y-%m-%d %H:%M:%S.%fZ') 
            
            actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=cab.numtrabajo).update(fchsolicita=fecha,estado1n=1)
            
            det = form2.save(commit=False)
            det.numtrabajo = cab
            
            form2.save()
            
            queryset = DetSolicitudTrabajoInterno.objects.filter(numtrabajo=cab.numtrabajo)
            emailaprob = User.objects.get(id=request.user.id)
            aut_oti = emailaprob.autoriza_oti.e_mail
            autoriza_instancia = Autorizador.objects.get(id=emailaprob.autoriza_oti_id)
            autoriza_user_id = autoriza_instancia.user_id.id
            autoriza_user = User.objects.get(id=autoriza_user_id)
            

            solicitud = DetSolicitudTrabajoInterno.objects.get(numtrabajo=cab.numtrabajo)
            ## SECCION DE NOTIFICACIONES GLOBALES

            ##Guarda cambio de estado en tabla de mensajeria
            noti = tipo_notificacion.objects.get(id=14) # 14. TRABAJOS INTERNOS SOLICITUD

            app_number = modelo_App.objects.get(id=3) # 3. trabajosInternos

            r = notificaciones_globales(
                app_origen = app_number,
                estado = True,
                identificador = solicitud.numtrabajo.numtrabajo,
                tipo = noti, 
                usuario_activa = emailaprob,
                autorizador_id = autoriza_user,
                )

            r.save()

            print("Helouuuu")
            envioMail('Solicitud Autorización de Orden de Trabajo Interna', aut_oti, 'email_aprobado_gerente.html', queryset, '')

            return redirect('trabajosinternos:listar_trabajos_internos')
        else:
            print(form.errors)
            print(form2.errors)
            return HttpResponse("errores")

@login_required
def verTrabajos(request,numtrabajo):
    if request.method == 'GET':
        identifica = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        detalle = DetSolicitudTrabajoInterno.objects.get(numtrabajo=identifica.numtrabajo)
        area = identifica.area
        print(area)

        form = cabVerTrabajos(instance=identifica)
        form2 = detVerTrabajos(instance=detalle)

        return render(request, 'trabajosInternos/ver_solamente_ingreso.html', {'form':form, 'form2':form2,'sectordj':area,'numtrabajo':identifica.numtrabajo })

@login_required
def verTrabajos1n(request,numtrabajo):
    if request.method == 'GET':
        identifica = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        detalle = DetSolicitudTrabajoInterno.objects.get(numtrabajo=identifica.numtrabajo)
        area = identifica.area
        print(area)

        form = cabVerTrabajos(instance=identifica)
        form2 = detVerTrabajos(instance=detalle)

        return render(request, 'trabajosInternos/ver_solamente_ingreso1n.html', {'form':form, 'form2':form2,'sectordj':area,'numtrabajo':identifica.numtrabajo,'observa':identifica.observaciones_rechazo1n })

@login_required
def verTrabajos2n(request,numtrabajo):
    if request.method == 'GET':
        identifica = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        detalle = DetSolicitudTrabajoInterno.objects.get(numtrabajo=identifica.numtrabajo)
        area = identifica.area
        print(area)


        form = cabVerTrabajos(instance=identifica)
        form2 = detVerTrabajos(instance=detalle)
        initial_data = RecibeEncargo.objects.filter(asignadoa__numtrabajo=numtrabajo).values_list(
                'responsable', flat=True
            )
        
        # print(initial_data)
        form3 = selectAsignadoa(initial={"asignacion":[cat for cat in initial_data]})

        return render(request, 'trabajosInternos/ver_solamente_ingreso2n.html', {'form':form, 'form2':form2,'form3':form3,'sectordj':area,'numtrabajo':identifica.numtrabajo,'observa':identifica.observaciones_rechazo1n })


@login_required
def convierteSia(request,numtrabajo):
    if request.method == 'GET':
        
        form = TrabajoAutoriForm2
        form2 = EditaDetTrForm2
        # ubica = activo_ubica.objects.all()
        # ubi_selected = activo_ubica.objects.get(id=ubicacion)
        # depar = activo_depar.objects.all()
        # depar_selected = activo_depar.objects.get(id=departamento)
        # area_id_selected = activo_areas.objects.get(area_nombre=area) 
        # tipo_trab = TipoTrab
        proy = proyectos_contabilidad.objects.filter(activo=True)
        
        
        queryset = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo)
        
        for i in queryset:
            ubi = i.ubica.id
            ubi_selected = activo_ubica.objects.get(id=ubi)

            depart = i.departamento.id
            depar_selected = activo_depar.objects.get(id=depart)

            area = str(i.area)
            print(area)
            area_selected = activo_areas.objects.get(area_nombre=area) 
            print(area_selected)

            descripcion = i.descripcion
            justificacion = i.justificacion
        
        ubicacion = activo_ubica.objects.all()
        departamento = activo_depar.objects.all()
        tipo_all = TipoPedido.objects.all().exclude(cod__in=['PR','AM','AP','CA','CP','LC','CD'])


        return render(request, 'trabajosInternos/convierte_sia.html', {'form':form, 'form2':form2,
        'ubi':ubi_selected,'depar':departamento,'ubica':ubicacion, 'dep':depar_selected,'area_s':area_selected,
        'tipo_all':tipo_all,'descripcion':descripcion,'justificacion':justificacion,'form4':proy})

    if request.method == 'POST':
        form = TrabajoAutoriForm2(request.POST)
        form2 = EditaDetTrForm2(request.POST, request.FILES)
        
        ubi = request.POST.get('ubicacion')
        depart = request.POST.get('depar')
        sec = request.POST.get('nsector')
        tip = request.POST.get('tipo')
        sectorantiguo = request.POST.get('area_s')
        proyecto = request.POST.get('numproyecto')
        fecha = datetime.today()

        justificacion = request.POST.get('justifica')
        descrip = request.POST.get('describe')

        try:
            proye = proyectos_contabilidad.objects.get(id=proyecto)
        except:
            proye = None

        if sec:
            print(sec)
            area_num = activo_areas.objects.get(area_nombre=sec)
            tiptr = TipoPedido.objects.get(cod=tip)
            ubicate = activo_ubica.objects.get(id=ubi)
            dept = activo_depar.objects.get(id=depart)
            if form.is_valid() and form2.is_valid():
                cab = form.save(commit=False)
                cab.fchaprueba = fecha
                cab.fchsolicita = fecha
                cab.aprobado = 1
                cab.usuario_aprueba = request.user.id
                # cab.usuario_aprueba = 16 #NICOLAS VERA. TEMPORAL HASTA ENTRAR EN PRODUCCION
                cab.ubica = ubicate.id
                cab.departamento_id = dept.id
                cab.area_id = area_num.area_codigo
                cab.numproyecto = proye
                cab.justificacion_compra = justificacion
                cab.usuario_solicita_id = 16 #NICOLAS VERA. TEMPORAL HASTA ENTRAR EN PRODUCCION
                cab.tipo_pedi_id = tiptr.cod
                det = form2.save(commit=False)
                det.descripcion = descrip
                cab.save()
                det.numtrabajo = form.save()
                det.save()
            
                consulta_numtra = OrdenesTrabajos.objects.all().last()  
                print(numtrabajo)
                
                actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(num_req_sia=consulta_numtra.numtrabajo,estado2n=5,fecha_finaliza_rechaza_convierte=fecha)  

                print(consulta_numtra.numtrabajo)

                queryset = DetalleTrabajo.objects.all().select_related('numtrabajo').filter(numtrabajo=consulta_numtra.numtrabajo)

                envioMail('Aprobación de Orden de Trabajo Gerente de Area', 'adquisiciones@ecofroz.com, dmencias@ecofroz.com', 'email_aprobado_gerente_sia.html', queryset, '')      
            else:
                return HttpResponse(form.errors,form2.errors)
            
        else:
            print("Sector Nulo")
            if form.is_valid() and form2.is_valid():
                fecha = datetime.today()
                print(sectorantiguo, type(sectorantiguo))
                ubicate = activo_ubica.objects.get(id=ubi)
                dept = activo_depar.objects.get(id=depart)
                sec_antiguo =  activo_areas.objects.get(area_nombre=sectorantiguo)
                tiptr = TipoPedido.objects.get(cod=tip)
                print(tiptr)

                cab = form.save(commit=False)
                cab.fchaprueba = fecha
                cab.fchsolicita = fecha
                cab.aprobado = 1
                cab.usuario_aprueba = request.user.id
                #cab.usuario_aprueba = 16 #NICOLAS VERA. TEMPORAL HASTA ENTRAR EN PRODUCCION
                cab.ubica = ubicate.id
                cab.departamento_id = dept.id
                cab.area_id = sec_antiguo.area_codigo
                cab.numproyecto = proye
                cab.justificacion_compra = justificacion
                #cab.usuario_solicita_id = 16 #NICOLAS VERA. TEMPORAL HASTA ENTRAR EN PRODUCCION
                cab.usuario_solicita_id = request.user.id
                cab.tipo_pedi_id = tiptr.cod
                det = form2.save(commit=False)
                det.descripcion = descrip
                cab.save()
                det.numtrabajo = form.save()
                det.save()
                # cab.save()

                print(tiptr.cod,type(tiptr.cod))

                consulta_numtra = OrdenesTrabajos.objects.all().last()  
                print(numtrabajo)
                
                actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(num_req_sia=consulta_numtra.numtrabajo,estado2n=5,fecha_finaliza_rechaza_convierte=fecha)  

                print(consulta_numtra.numtrabajo)

                queryset = DetalleTrabajo.objects.all().select_related('numtrabajo').filter(numtrabajo=consulta_numtra.numtrabajo)

                envioMail('Aprobación de Orden de Trabajo Gerente de Area', 'adquisiciones@ecofroz.com, dmencias@ecofroz.com', 'email_aprobado_gerente_sia.html', queryset, '')
            else:
                return HttpResponse(form.errors, form2.errors)


        return redirect('trabajosinternos:listar2n')

@login_required
def editaTrabajos(request,numtrabajo):
    if request.method == 'GET':
        instancia = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        detalle = DetSolicitudTrabajoInterno.objects.get(numtrabajo=instancia.numtrabajo)
        sectordj = instancia.area
        form = cabIngresoTrabajos(instance=instancia)
        form2 = detIngresoTrab(instance=detalle, files=request.FILES )
        return render(request, 'trabajosInternos/edita_solicitudes.html', {'form':form, 'form2':form2,'sectordj':sectordj,'observa':instancia.observaciones_rechazo1n})

    
    if request.method == 'POST':
        instancia = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        detalle = DetSolicitudTrabajoInterno.objects.get(numtrabajo=instancia.numtrabajo)
    
        form = cabIngresoTrabajos(request.POST, instance=instancia)
        form2 = detIngresoTrab(request.POST, request.FILES, instance=detalle)

        sectorantiguo = instancia.area
        fecha = datetime.today()
        
        if request.POST.get('nsector'):
            print(request.POST.get('nsector'))
            if form.is_valid() and form2.is_valid():
                cab = form.save(commit=False)
                cab.fchsolicita = fecha
                cab.area = str(request.POST.get('nsector'))
                cab.estado1n = 1
                cab.observaciones_rechazo1n = None
                det = form2.save(commit=False)
                det.numtrabajo = cab
                det.save()
                cab.save()
                
            else:
                return HttpResponse(form.errors,form2.errors)
                
        else:
            print("Sector Nulo")
            if form2.is_valid():
                print("Llega")
                cab = form.save(commit=False)
                cab.area = sectorantiguo
                cab.fchsolicita = fecha
                cab.estado1n = 1
                cab.observaciones_rechazo1n = None
                det = form2.save(commit=False)
                det.numtrabajo = cab
                det.save()
                cab.save()
            else:
                return HttpResponse(form.errors, form2.errors)


        return redirect('trabajosinternos:listar_trabajos_internos')

@login_required
def autoriza1n(request,numtrabajo):
    if request.method == 'GET':
        trabajo = DetSolicitudTrabajoInterno.objects.select_related('numtrabajo').get(numtrabajo__numtrabajo=numtrabajo)

        return render(request, 'trabajosInternos/ver_solicitudes1n.html', {'solic':trabajo})
    else:
        fecha = datetime.today()
        if request.POST.get('notas_rechazo'):
            actualiza_rechazo = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(
                estado1n=3,fchaprueba1n=fecha, observaciones_rechazo1n=str(request.POST.get('notas_rechazo')))
        else:
            actualiza_campo = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(
                estado1n=2,estado2n=1,fchaprueba1n=fecha, usuario_aprueba1n_id=request.user.id)

            queryset = DetSolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
            emailaprob = queryset.numtrabajo.usuario_solicita.generador_int.e_mail
            copia = 'mantenimiento@ecofroz.com'

            ## Sección para Notificaciones Globales
            query = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)

            id_usuario = query.usuario_solicita_id
                

            id_genera = User.objects.get(id=id_usuario)
            emailgenera =  Generador.objects.get(id=id_genera.generador_id)
            id_aprueba = User.objects.get(id=emailgenera.user_id.id)

            ##Guarda cambio de estado en tabla de mensajeria
            noti = tipo_notificacion.objects.get(id=15) # 15. TRABAJOS INTERNOS AUTORIZACION GERENTE AREA

            app_number = modelo_App.objects.get(id=3) # 3. TRABAJOS INTERNOS

            r = notificaciones_globales(
                app_origen = app_number,
                estado = True,
                identificador = query.numtrabajo,
                tipo = noti, 
                usuario_activa = id_genera,
                autorizador_id = id_aprueba,
                )

            r.save()


            #envioMail('Solicitud Autorizada de Orden de Trabajo Interna', emailaprob, 'email_generado.html', queryset, '')
            #envioMail('Solicitud Autorizada de Orden de Trabajo Interna', copia, 'email_generado.html', queryset, '')

        return redirect('trabajosinternos:listar1n')

@login_required        
def gestiona_solicitudes(request, numtrabajo):
    if request.method == 'GET':
        
        solicitud = DetSolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).select_related('numtrabajo')
        solic = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        asignacion = selectAsignadoa()
        num = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        numt = num.numtrabajo

        return render(request, 'trabajosInternos/gestiona_solicitudes.html', { 'cot': solicitud,'solic':solic, 'asignado':asignacion,'numt':numt})

def gestiona_solicitudes_mant(request, numtrabajo):
    if request.method == 'GET':
        
        solicitud = DetSolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).select_related('numtrabajo')
        solic = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        asignacion = selectAsignadoa()
        num = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        numt = num.numtrabajo

        return render(request, 'trabajosInternos/gestiona_solicitudes_mant.html', { 'cot': solicitud,'solic':solic, 'asignado':asignacion,'numt':numt})


def cambiaEstadoMant(request, numtrabajo):
    if request.method == 'GET':
        fecha=datetime.today()
        #Marca con 2 en estado_mant para indicar que la orden està en proceso
        solic = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(estado_mant=2,fecha_en_proceso_mant=fecha,fecha_finaliza_mant=None)

        return redirect('trabajosinternos:listar_mantenimiento')


@login_required
def editaGestiona(request, numtrabajo):
    if request.method == 'GET':
        
        solicitud = DetSolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).select_related('numtrabajo')
        initial_data = RecibeEncargo.objects.filter(asignadoa__numtrabajo=numtrabajo).values_list(
                'responsable', flat=True
            )
        
        print(initial_data)
        
        asignacion = selectAsignadoa(initial={"asignacion":[cat for cat in initial_data]})
        solic = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        numt = solic.numtrabajo
        
        return render(request, 'trabajosInternos/edita_gestiona.html', { 'cot': solicitud, 'asignado':asignacion, 'solic':solic, 'numt':numt,'control':True})

@login_required
def asignacionMantenimiento(request,numtrabajo):
    
    # valor_destino = request.GET.get("destino")
    notas = request.GET.get("notas")
    # print(valor_destino)
    # print(notas)

    # print(request.user.username)
    form = selectAsignadoa(request.GET or None)
    
    
    if request.method == 'GET':
        control = request.GET.get('control')
        print(numtrabajo)
        fec = datetime.today()
        form = selectAsignadoa(request.GET or None)

        if control:
            print("Si llega control")
            borra_asignados = RecibeEncargo.objects.filter(asignadoa__numtrabajo=numtrabajo).delete()


        if form.is_valid():
            data = form.cleaned_data['asignacion']
            
            ids = []
            for i in data:
                id = i.id
                ids.append(id)
            
            
            fecha=datetime.today()
            asignaciones = SolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)   
            actualiza_observa =  SolicitudTrabajoInterno.objects.filter(
                numtrabajo=numtrabajo).update(observaciones_internas_mantenimiento=notas, estado2n=2,fecha_en_proceso=fecha)
            usuarios = User.objects.filter(id__in=ids)

            for i in usuarios:
                responsable = RecibeEncargo(responsable=i)
                responsable.save()
                responsable.asignadoa.add(asignaciones)

            queryset = DetSolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
            queryset2 = RecibeEncargo.objects.filter(asignadoa=numtrabajo)
            emailaprob = 'mantenimiento@ecofroz.com'

        
            id_usuario = asignaciones.usuario_solicita.id   

            id_solicita = User.objects.get(id=id_usuario)
            
            id_mant1 = User.objects.get(id=42) # OSCAR MACHUCA
            id_mant2 = User.objects.get(id=14) # ROLANDO MOLINA
            


            ##Guarda cambio de estado en tabla de mensajeria
            noti = tipo_notificacion.objects.get(id=16) # 16. TRABAJOS INTERNOS ASIGNACION GER TECNICA

            app_number = modelo_App.objects.get(id=3) # 3. TRABAJOS INTERNOS

            r = notificaciones_globales(
                app_origen = app_number,
                estado = True,
                identificador = asignaciones.numtrabajo,
                tipo = noti, 
                usuario_activa = id_solicita,
                autorizador_id = id_mant1,
                )
            r.save()

            r = notificaciones_globales(
                app_origen = app_number,
                estado = True,
                identificador = asignaciones.numtrabajo,
                tipo = noti, 
                usuario_activa = id_solicita,
                autorizador_id = id_mant2,
                )
            r.save()


            envioMail('Asignación de Orden de Trabajo', emailaprob, 'email_asignacion.html', queryset, queryset2)
            
        else:
            return HttpResponse("Errores")
        
        return redirect('trabajosinternos:listar2n')


@login_required
def listarSolicitudes(request):
    queryset = request.GET.get("buscar")
    if queryset:
        query = DetSolicitudTrabajoInterno.objects.filter(
            Q(numtrabajo__numtrabajo = queryset) |
            Q(numtrabajo__descripcion__icontains = queryset)).filter(numtrabajo__usuario_solicita = request.user.id).exclude(numtrabajo__anula=True)
    else:
        query = DetSolicitudTrabajoInterno.objects.select_related('numtrabajo').filter(numtrabajo__usuario_solicita = request.user.id).exclude(
            numtrabajo__anula=True).order_by('-numtrabajo__fchsolicita')
    

    paginator = Paginator(query, 50)
    page = request.GET.get('page')
    solic = paginator.get_page(page)

    return render(request, 'trabajosInternos/listar_solicitudes.html', {'form':solic,'busqueda':queryset})

@login_required
def listarSolicitudes1n(request):
    queryset = request.GET.get("buscar")
    usu_depend = Autorizador.objects.get(user_id=request.user.id)
    usu_depend2 = User.objects.filter(autorizador=usu_depend.id)
    id_usu = []
    for i in usu_depend2:
        d = i.id
        id_usu.append(d)

    if queryset:
        query_procesadas = DetSolicitudTrabajoInterno.objects.filter(
            Q(numtrabajo__numtrabajo__iexact = queryset)).filter(Q(numtrabajo__usuario_solicita__in=id_usu))
    else:
        startdate = date.today() + timedelta(days=1) 
        enddate = startdate - timedelta(days=90)

        solic = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(
            numtrabajo__estado1n=1
            ).filter(Q(numtrabajo__usuario_solicita__in=id_usu)).order_by('-numtrabajo__fchsolicita')
        
        procesadas = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(Q(
            numtrabajo__estado1n=2) | Q(numtrabajo__estado1n=3)).filter(numtrabajo__fchsolicita__range=[enddate,startdate]
            ).filter(Q(numtrabajo__usuario_solicita__in=id_usu)).order_by('-numtrabajo__fchsolicita')
    

    # paginator = Paginator(query_procesadas, 6)
    # page = request.GET.get('page')
    # procesadas = paginator.get_page(page)

    return render(request, 'trabajosInternos/listar_solicitudes_1n.html', {'form':solic,'busqueda':queryset,'procesadas':procesadas})

@login_required
def anulaSolicitudes(request, numtrabajo):
    if request.method == 'GET':
        anular = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(anula=True)

        return redirect('trabajosinternos:listar_trabajos_internos')


@login_required
def Autoriza2n(request):
    usu_depend = Generador.objects.get(user_id=request.user.id)
    usu_depend2 = User.objects.filter(generador_int=usu_depend.id)
    id_usu = []
    for i in usu_depend2:
        d = i.id
        id_usu.append(d)

    if request.method == 'GET':
        
        finalizadas1 = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(Q(numtrabajo__estado2n=5) | Q(numtrabajo__estado2n=4) | Q(numtrabajo__estado2n=3)).order_by("-numtrabajo__fecha_finaliza_rechaza_convierte")
       
        paginator_recep = Paginator(finalizadas1, 25) # Show 25 contacts per page.
        page_number_fin = request.GET.get('page_finalin')
        finalizadas = paginator_recep.get_page(page_number_fin)

        pendientes = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado1n=2,numtrabajo__estado2n=1).order_by("-numtrabajo__fchaprueba1n")
       
        enproceso1 = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado2n=2).order_by("-numtrabajo__fecha_en_proceso")

        paginator_recep = Paginator(enproceso1, 25) # Show 25 contacts per page.
        page_number_proc = request.GET.get('page_enproc')
        enproceso = paginator_recep.get_page(page_number_proc)

        if page_number_proc:
            activate = 'enproceso'
        elif page_number_fin:
            activate = 'finalizadas'
        else:
            activate = 0

        try:
            cfin = finalizadas1.count()
        except:
            # countfin = 0
            cfin = 0
        
        try:
            cpend = pendientes.count()
        except:
            # countpend = 0
            cpend = 0
        
        try:
            cproc = enproceso1.count()
        except: 
            # countproc = 0
            cproc = 0

        return render(request, 'trabajosInternos/listar_solicitudes_2n.html', {'form':pendientes, 'finalizadas':finalizadas, 'enproceso':enproceso,'cfin':cfin,'cpend':cpend,'cproc':cproc,'activate':activate})

    else:

        buscar = request.POST.get("buscar")
        print(buscar)
        finalizadas1 = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(Q(numtrabajo__estado2n=5) | Q(numtrabajo__estado2n=4) | Q(numtrabajo__estado2n=3)).filter(
            Q(numtrabajo__descripcion__icontains=buscar) |
              Q(numtrabajo__numtrabajo__icontains=buscar) |
                Q(numtrabajo__departamento__dep_nombre__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__first_name__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__last_name__icontains=buscar)).order_by("-numtrabajo__fecha_finaliza_rechaza_convierte")

        paginator_recep = Paginator(finalizadas1, 25) # Show 25 contacts per page.
        page_number_fin = request.GET.get('page_finalin')
        finalizadas = paginator_recep.get_page(page_number_fin)

        pendientes = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado1n=2,numtrabajo__estado2n=1).filter(
            Q(numtrabajo__descripcion__icontains=buscar) |
              Q(numtrabajo__numtrabajo__icontains=buscar) |
                Q(numtrabajo__departamento__dep_nombre__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__first_name__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__last_name__icontains=buscar)).order_by("-numtrabajo__fchaprueba1n")
       
        enproceso1 = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado2n=2).filter(
            Q(numtrabajo__descripcion__icontains=buscar) |
              Q(numtrabajo__numtrabajo__icontains=buscar) |
                Q(numtrabajo__departamento__dep_nombre__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__first_name__icontains=buscar) |
                Q(numtrabajo__usuario_solicita__last_name__icontains=buscar)).order_by("-numtrabajo__fecha_en_proceso")

        paginator_recep = Paginator(enproceso1, 25) # Show 25 contacts per page.
        page_number_proc = request.GET.get('page_enproc')
        enproceso = paginator_recep.get_page(page_number_proc)

        if page_number_proc:
            activate = 'enproceso'
        elif page_number_fin:
            activate = 'finalizadas'
        else:
            activate = 0

        try:
            cfin = finalizadas1.count()
        except:
            # countfin = 0
            cfin = 0
        
        try:
            cpend = pendientes.count()
        except:
            # countpend = 0
            cpend = 0
        
        try:
            cproc = enproceso1.count()
        except: 
            # countproc = 0
            cproc = 0

        return render(request, 'trabajosInternos/listar_solicitudes_2n.html', {'form':pendientes, 'finalizadas':finalizadas, 'enproceso':enproceso,'cfin':cfin,'cpend':cpend,'cproc':cproc,'activate':activate,'buscar':buscar})



def listarMantenimiento(request):
    # usu_depend = Generador.objects.get(user_id=request.user.id)
    # usu_depend2 = User.objects.filter(generador_int=usu_depend.id)
    # id_usu = []
    # for i in usu_depend2:m
    #     d = i.id
    #     id_usu.append(d)

    if request.method == 'GET':
        
        finalizadas = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado_mant=4).order_by("-numtrabajo__fecha_finaliza_mant")
        en_proceso = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado_mant=2).order_by("-numtrabajo__fecha_en_proceso_mant")
        nuevas = DetSolicitudTrabajoInterno.objects.all().select_related('numtrabajo').filter(numtrabajo__estado2n=2).filter(~Q(numtrabajo__estado_mant__in=[2,4])).order_by("-numtrabajo__fecha_en_proceso")

        return render(request, 'trabajosInternos/listar_solicitudes_mantenimiento.html', {'en_proceso':en_proceso, 'finalizadas':finalizadas, 'nuevas':nuevas})



@login_required
def devuelve2n(request, numtrabajo):
    if request.method == 'GET':
        observa = request.GET.get('notas')
        fecha = datetime.today()

        actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(
            estado2n=3, fecha_finaliza_rechaza_convierte=fecha, observaciones_devuelve_mantenimiento=observa)

        queryset = DetSolicitudTrabajoInterno.objects.get(numtrabajo=numtrabajo)
        emailaprob = queryset.numtrabajo.usuario_solicita.email

        envioMail('Devolución de Orden de Trabajo', emailaprob, 'email_devolucion.html', queryset, '')
        
        return redirect('trabajosinternos:listar2n')

@login_required
def marcaFinalizadas(request,numtrabajo):
    if request.method== 'GET':

        fecha = datetime.today()
        actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(estado2n=4,fecha_finaliza_rechaza_convierte=fecha)

        return redirect('trabajosinternos:listar2n')

def marcaFinalizadasMantenimiento(request,numtrabajo):
    if request.method== 'GET':

        fecha = datetime.today()
        actualiza = SolicitudTrabajoInterno.objects.filter(numtrabajo=numtrabajo).update(estado_mant=4,fecha_finaliza_mant=fecha)

        return redirect('trabajosinternos:listar_mantenimiento')


####### AQUI VAN LOS SERVICIOS #########

class SectoresListApiView(ListAPIView):
    serializer_class = SectoresSerializer

    def get_queryset(self):
        kword = self.request.query_params.get('kword','')
        if kword == '':
            return activo_areas.objects.none()

        return activo_areas.objects.filter(area_nombre__icontains=kword)[:8]