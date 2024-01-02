from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('listarreqsarchivo/', listarSolicitudes, name = 'listar_requerimientos_archivo'),
    path('ingreso/',ingresoSolicitudes, name = 'ingreso_solicitudes'),
    # path('editar/<int:numpedido>', editaSolicitudes, name='edita_solicitudes'),
    path('reporte_raytec', reporteRaytec, name='reporte_raytec'),
    path('export_excel/<str:inicio>/<str:fin>', exportExcelEventosRaytec,name='export_excel'),
    path('reporte_parecetico_l3', reportePareceticoL3, name='reporte_parecetico_l3'),
     path('export_excel_parecetico_l3/<str:inicio>/<str:fin>', exportExcelEventosPeraceticoL3,name='export_excel_parecetico_l3'),

    path('reporte_cloro_l2', reporteCloroL2, name='reporte_cloro_l2'),

    path('reporte_pesos_ishida_r1', reporteIshidaR1, name='reporte_ishida_r1'),
    path('reporte_pesos_ishida_r2', reporteIshidaR2, name='reporte_ishida_r2'),
    path('reporte_pesos_ishida_r3', reporteIshidaR3, name='reporte_ishida_r3'),
    
    path('export_excel_cloro_l2/<str:inicio>/<str:fin>', exportExcelCloroL2,name='export_excel_cloro_l2'),

    path('api/ry_linea1/', consultaEventosL1, name = 'consulta_eventos_l1'),
    path('api/ry_linea2/', consultaEventosL2, name = 'consulta_eventos_l2'),
    
    path('administra_transporte', administra_eventos, name = 'administra_eventos'),
    path('all_events/', all_events, name = 'all_events'),
    path('all_events_wchis/', all_events_wchis, name = 'all_events_wchis'),
    path('add_event/', add_event, name = 'add_event'),
    path('update_event/', update_event, name = 'update_event'),
    path('update_event_tarjeta/', update_event_tarjeta, name = 'update_event_tarjeta'),
    path('remove_event/', remove_event, name = 'remove_event'),

    path('listarsolicitudestransporte/', listarSolicitudesTransporte, name = 'listar_solicitudes_transporte'),
    path('listarapruebatransporte1n/', listarParaAprobarTransporte, name = 'listar_aprueba_1n'),
    path('autorizatransporte1n/<int:numpedido>', autorizaTransporte1n, name = 'autoriza_transporte_1n'),
    
    path('gestionatransporte2n/', gestionaTransporte2n, name = 'listar_gestiona_2n'),
    path('gestionavales/', gestionaVales, name = 'gestiona_vales'),
    path('autorizavales/<int:numpedido>', autorizaVales, name = 'autoriza_vales'),
    
    path('ver_calendario_rutas_fijas', ver_rutas_fijas, name = 'ver_rutas_fijas'),

    path('nueva_solicitud', nuevaSolicitud, name = 'nueva_solicitud'),
    path('admin_rutas', nuevaRuta, name = 'registra_nueva_ruta'),
    path('updateestadoruta/', actualizaEstadoRuta, name='actualiza_estado_ruta'),
    path('ajaxcallruta/', ajax_call_ruta, name='ajax_call_ruta'),
    path('ajaxcallnombreruta/', ajax_call_nombreruta, name='ajaxcallnombreruta'),
    path('ajaxcalldepar/', ajax_call_depar, name='ajaxcalldepar'),
    path('ajaxcallpasajero/', ajax_call_pasajero, name='ajaxcallpasajero'),
    path('ajaxcallnombretransportista/', ajax_call_nombretransportista, name='ajaxcallnombretransportista'),
    path('ajaxcallnombrepasajero/', ajax_call_nombrepasajero, name='ajaxcallnombrepasajero'),
    path('ajax_save_booking/', ajax_save_booking, name='ajax_save_booking'),
    path('ajax_query_passengers/', ajax_query_passengers, name='ajax_query_passengers'),
    path('gestionasolicitudestransporte/ajax_cambia_enproceso/', ajax_cambia_enproceso, name='ajax_cambia_enproceso'),
    path('gestionasolicitudestransporte/ajax_cambia_confirma/', ajax_cambia_confirma, name='ajax_cambia_confirma'),
    path('gestionasolicitudestransporte/ajax_save/', ajax_save, name='ajax_save'),

    path('editarsolicitudes/<int:numpedido>', editaSolicitudes, name='edita_solicitudes'),
    path('versolicitudes/<int:numpedido>', verSolicitudes, name='ver_solicitudes'),
    path('anula/<int:numpedido>', anulaSolicitudes, name='anula'),

    path('gestionasolicitudestransporte/<int:numpedido>', gestionaSolicitudesTransporte, name='gestiona_solicitudes_transporte'),
    path('printpermiso/<int:numpedido>', imprimeAutorizacionSalida,name='imprime_autoriza_salida'),
    path('reporte_transporte', reporteTransporte, name='reporte_transporte'),
    path('devuelve2n/<int:numpedido>', devuelve2n, name='devuelve2nx'),
    path('export_excel_transporte/<str:inicio>/<str:fin>', exportExcelTransporte,name='export_excel_transporte'),
    path('verifica_salida', verificaSalidaAutotizada,name='verifica_salida_autorizada'),

    path('cargaplanagri', cargaPlanAgri,name='carga_plan_agri'),
    path('gestionainventario', gestionaInventarioAgri,name='gestiona_inventario_agri'),
    path('registraegreso', registraEgreso,name='registra_egreso'),
    path('nomina', NominaList.as_view(), name='nomina'),
   
    # path('chat/', chat, name='chat'),
]
