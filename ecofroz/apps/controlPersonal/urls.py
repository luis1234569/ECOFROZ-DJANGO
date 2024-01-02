from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url

from .views import ingresoPersonal, ingresoVehiculo, salidaPersona, salidaVehiculo, \
registroEmpleados, reporteIngresos, exportExcel, contenedorRegistro, \
reporteContenedor, exportExcelConte, reporteTablet, registroChofer, registroGuardado, \
listarChoferes, choferDelete, ingresoNuevaPlaca,editaChofer, editaRegConte, \
registroAlmuerzos, registroAguaClara, registroLaLaurita, registroLaAvelina, nuevaPantallaReportesPersonal, \
reporteIngresosVehiculos, exportExcelVehiculos, personalDirectorio, registroLaMerced, ingresoNovedades, \
listarNovedades, gallery_view, verReporte, editarReporte, capacitacionSegu, uploadFotosView, cerrarEdicion, \
activaChofer, listarVadministrativos, ajax_call_placa, actualizaEstadoVehiAdministrativo

urlpatterns = [
    path('ingreso_personal/', ingresoPersonal, name = 'ingreso_personal'),
    path('ingreso_vehiculo/', ingresoVehiculo, name = 'ingreso_vehiculo'),
    path('salida_persona/', salidaPersona, name = 'salida_persona'),
    path('salida_vehiculo/', salidaVehiculo, name = 'salida_vehiculo'),
    path('registros/', registroEmpleados, name='registros'),
    path('registros_ac/', registroAguaClara, name='registros_ac'),
    path('registros_lm/', registroLaMerced, name='registros_lm'),
    path('registros_ll/', registroLaLaurita, name='registros_ll'),
    path('registros_la/', registroLaAvelina, name='registros_la'),
    path('almuerzo/', registroAlmuerzos, name='almuerzo'),
    path('reporte_tablet/', reporteTablet, name = 'reporte_tablet'),
    path('reporte_ingresos', reporteIngresos, name='reporte_ingresos'),
    path('reporte_vehiculos', reporteIngresosVehiculos, name='reporte_vehiculos'),
    path('reporte_excel_veh/<str:inicio>/<str:fin>', exportExcelVehiculos, name='reporte_excel_veh'),
    path('export_excel/<str:inicio>/<str:fin>', exportExcel,name='export_excel'),
    path('registro_contenedor', contenedorRegistro, name='registro_contenedor'),
    path('reporte_contenedor', reporteContenedor, name='reporte_contenedor'),
    path('export_excel_conte/<str:inicio>/<str:fin>', exportExcelConte, name='export_excel_conte'),
    path('registro_chofer', registroChofer, name='registro_chofer'),
    path('alertsavesalida', registroGuardado ,name='registro_guardado_salida_chofer'),
    path('listar_chofer', listarChoferes ,name='listar_chofer'),
    path('listar_vadministrativos', listarVadministrativos ,name='listar_vadministrativos'),
    path('estado_chofer/<str:cedula>', activaChofer, name='estado_chofer'),
    path('eliminarchofer/<str:pk>', choferDelete.as_view(),name='eliminar_chofer'),
    path('edita_chofer/<str:pk>', editaChofer.as_view(),name='edita_chofer'),
    path('guarda_newplaca', ingresoNuevaPlaca,name='ingreso_placa'),
    path('edita_conte/<int:reg>', editaRegConte, name='edita_conte'),
    path('reportespersonal_new',nuevaPantallaReportesPersonal,name='reportespersonal_new'),
    path('directorio',personalDirectorio,name='directorio'),
    path('ingresonovedades',ingresoNovedades,name='ingreso_novedades'),
    path('listarnovedades',listarNovedades,name='listar_novedades'),
    path('gallery_view/<int:pk>', gallery_view, name='gallery_view'),
    path('ver_novedades/<int:pk>', verReporte, name='ver_novedades'),
    path('close_edit/<int:pk>', cerrarEdicion, name='close_edit'),
    path('editar_reporte/<int:pk>', editarReporte, name='editar_reporte'),
    path('capacitacion',capacitacionSegu,name='capacitacion_seguridad'),
    #AJAX para cargar fotos
    url(r'^upload-fotos/$', uploadFotosView.as_view(), name='upload_fotos'),
    path('ajaxcallplaca/', ajax_call_placa, name='ajax_call_placa'),
    path('updatevehiadmin/', actualizaEstadoVehiAdministrativo, name='actualiza_estado_vehiculo_administrativo'),
]
