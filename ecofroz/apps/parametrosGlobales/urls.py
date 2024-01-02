from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import parametrosProyectos, registraNuevo, actualizaEstadoProyectos, \
ajax_call, notifica, desactivanotifica, parametrosRutas

urlpatterns = [

    path('paramproyectos/', parametrosProyectos, name = 'parametros_proyectos'),
    path('registranuevo/', registraNuevo, name='registra_nuevo'),
    path('updateestado/', actualizaEstadoProyectos, name='actualiza_estado_proyectos'),
    path('ajaxcall/', ajax_call, name='ajax_call'),
    path('notificaciones', notifica, name='notificaciones'),
    path('desactivanotif', desactivanotifica, name='desactivanotif'),
    #URLs Transporte
    path('paramrutas/', parametrosRutas, name = 'parametros_rutas'),
]