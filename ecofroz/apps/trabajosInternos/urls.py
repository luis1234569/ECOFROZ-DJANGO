from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('listartrabajosinternos/', listarSolicitudes, name = 'listar_trabajos_internos'),
    path('ingreso/',ingresoOrdenes, name = 'ingreso_ordenes'),
    path('editar/<int:numtrabajo>', editaTrabajos, name='edita_trabajos'),
    #path('conviertesia/<int:numtrabajo>/<int:ubicacion>/<int:departamento>/<str:area>/<str:descripcion>/<str:justificacion>', convierteSia, name='convierte_sia'),
    path('conviertesia/<int:numtrabajo>', convierteSia, name='convierte_sia'),
    path('ver/<int:numtrabajo>', verTrabajos, name='ver_solamente'),
    path('ver1n/<int:numtrabajo>', verTrabajos1n, name='ver_solamente1n'),
    path('ver2n/<int:numtrabajo>', verTrabajos2n, name='ver_solamente2n'),

    #URLS de los Servicios
    path('api/consultasector/',SectoresListApiView.as_view(), name = 'consulta_sector'),
    path('listar1n/', listarSolicitudes1n, name='listar1n'),
    path('listar2n/', Autoriza2n, name='listar2n'),
    path('listarmantenimiento/', listarMantenimiento, name='listar_mantenimiento'),
    
    path('gestionasolicitudes/<int:numtrabajo>', gestiona_solicitudes, name='gestiona_solicitudes'),
    path('gestionasolicitudesmant/<int:numtrabajo>', gestiona_solicitudes_mant, name='gestiona_solicitudes_mant'),
    path('editagestiona/<int:numtrabajo>', editaGestiona, name='edita_gestiona'),
    path('asignacion/<int:numtrabajo>', asignacionMantenimiento, name='asignacion_mantenimiento'),
    path('cambia_estado_mant/<int:numtrabajo>', cambiaEstadoMant, name='cambia_estado_mant'),
   
    path('marca_finalizadas/<int:numtrabajo>', marcaFinalizadas, name='marca_finalizadas'),
    path('marca_finalizadas_mantenimiento/<int:numtrabajo>', marcaFinalizadasMantenimiento, name='marca_finalizadas_mantenimiento'),
    path('autoriza1n/<int:numtrabajo>', autoriza1n, name='autoriza1n'),
    path('devuelve2n/<int:numtrabajo>', devuelve2n, name='devuelve2n'),
    path('anula/<int:numtrabajo>', anulaSolicitudes, name='anula'),

]