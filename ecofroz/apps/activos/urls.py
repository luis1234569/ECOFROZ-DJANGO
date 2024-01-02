"""ecofroz01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import home,registro_nuevo,listar_activos, \
    eliminar_activos, ActivoList, ActivoUpdate, ActivoDelete, RegistroNuevo, \
    filtrar_activos, to_excel, to_excelclass, ultimos_movimientos, \
    ActivoMoverUbicacion, genera_nomenclatura, registro_nuevo, \
    registro_guardado, to_mba, ActivoCambiaEstado, salida_activos_func, \
    registro_guardado_salida, control_retorno_activos,registro_nuevov2, imprimeSalidaActivos, \
    cambiaEstadoRetorno, listarSalida, confirmaSalida, saleActivo, cambiaEstadoBajaActivos, identifica_valores, \
    SolicitudesSalidaActivos, verSolicitudesSalida, apruebaBodegaSalida,listar_bajas,to_ExcelAll,to_ExcelBajas, \
    registro_movimiento_interno_func, identifica_valores_mov_int, salida_activos_ind, busqueda_salida_activos, \
    busqueda_mov_int, AutorizaSalidasDep, depAutorizaSalida, autorizaSalidaAutorizador, registro_guardado_mov_int, \
    listarMovimientosInternos,listarSalidasAprobadas, busqueda_activo_bodega, registro_no_encontrados, \
    busqueda_movimientos_bodega,busqueda_activos_mantenimiento, movimiento_a_bodega, ver_autoriza_seguridad,autoriza_salida_seguridad, \
    recibeActivoBodega,movimiento_desde_bodega,mov_success_bodega,cambio_estado_grabado_bodega, \
     autMovimientosActivosExcel, add_activo_view, gallery_view, imprimeActaMovimientosInternos, ver_detalle_bajas, \
     listarRecepcionesforSeg, descargo_custodio, confirma_acta_recepcion_entregada, imprimeActaEntregaActivosCustodio, \
     descargo_custodio_activold, imprimeActaEntregaActivosCustodio2, descargo_custodio_activold_custom, listar_mis_activos_en_custodio, \
     reportar_no_custodio, gallery_mis_activos, imprimeActaEntregaActivosCustodioGlobal, filtrar_activos2, custom_to_excelclass, \
     CustomExcelAll, CustomExcelBajas, busqueda_salida_activos_agricola, listarSalidaAgri, imprimeSalidaActivosAgri, \
     salida_activos_agri, gallery_view_custom, mueve_bodega, movimiento_a_bodega2, registro_guardado_mov_int2


urlpatterns = [
    path('gallery/<int:pk>', add_activo_view, name="carga_imagenes"),
    path('gallery_view/<int:pk>', gallery_view, name="gallery_view"),
    path('gallery_view_custom/<int:pk>', gallery_view_custom, name="gallery_view_custom"),
    path('gallery_mis_activos/<int:pk>', gallery_mis_activos, name="gallery_mis_activos"),
    
    path('nuevo', registro_nuevov2 ,name='registro_nuevov2'),
    path('registro_observaciones/<int:pk>', registro_no_encontrados,name='registro_no_encontrados'),
    path('listar_salida', listarSalida, name='listar_salida'),
    path('listar_salida_agri', listarSalidaAgri, name='listar_salida_agri'),
    path('listar_mis_activos', listar_mis_activos_en_custodio, name='listar_mis_activos'),

    path('listar_salidas_aprobadas', listarSalidasAprobadas, name='listar_salidas_aprobadas'),
    path('aprueba_salida/<int:id>', confirmaSalida, name='aprueba_salida'),
    path('busqueda_salida/', busqueda_salida_activos, name='busqueda_salida'),
    path('busqueda_salida_agr/', busqueda_salida_activos_agricola, name='busqueda_salida_agr'),
    path('busqueda_movimientos_bodega/', busqueda_movimientos_bodega, name='busqueda_movimientos_bodega'),
    path('busqueda_activos_mantenimiento/', busqueda_activos_mantenimiento, name='busqueda_activos_mantenimiento'),
    path('mueve_bodega/', mueve_bodega, name='mueve_bodega'),
    
    path('autmovimientosactivos/', autMovimientosActivosExcel, name='aut_movimientos_activos_excel'),
    
    path('busqueda_mov_int/', busqueda_mov_int, name='busqueda_mov_int'),
    path('mov_success/<str:codigo>',registro_guardado_mov_int,name='mov_success'),
    path('mov_success2/<str:codigo>',registro_guardado_mov_int2,name='mov_success2'),
    
    path('mov_success_bodega/',mov_success_bodega,name='mov_success_bodega'),
    path('registrosalida/<int:numtrabajo>', salida_activos_func ,name='salida_activos_func'),
    path('registrosalidaind/<str:codigo>', salida_activos_ind ,name='registrosalidaind'),
    path('registrosalidaagri/<str:codigo>', salida_activos_agri ,name='registrosalidagri'),
    path('movimientointerno/<str:codigo>', registro_movimiento_interno_func ,name='registro_movimiento_interno'),
    path('verdetallebajas/<str:codigo>', ver_detalle_bajas ,name='ver_detalle_bajas'),
    
    path('movimientoabodega/<str:codigo>', movimiento_a_bodega ,name='movimiento_a_bodega'),
    path('movimientoabodega2/<str:codigo>', movimiento_a_bodega2 ,name='movimiento_a_bodega2'),
    
    path('movimientodesdebodega/<str:codigo>', movimiento_desde_bodega ,name='movimiento_desde_bodega'),
    path('cambio_estado_grabado_bodega/<str:codigo>', cambio_estado_grabado_bodega ,name='cambio_estado_grabado_bodega'),
    
    # path('movimiento_activos_bodega/<str:codigo>', movimiento_activos_bodega ,name='movimiento_activos_bodega'),
    path('histmovints/<int:codigo>', listarMovimientosInternos ,name='listar_historial_movimientos_internos'),
    path('lista_autoriza_dep', AutorizaSalidasDep, name='lista_autoriza_dep'),
    path('ver_autoriza/<int:numorden>', depAutorizaSalida, name='ver_autoriza'),
    path('ver_autoriza_seguridad/<int:numorden>', ver_autoriza_seguridad, name='ver_autoriza_seguridad'),
    path('salida_activo', saleActivo, name='salida_activo'),
    path('autoriza_salida/<int:numorden>', autorizaSalidaAutorizador, name='autoriza_salida'),
    path('autoriza_salida_seguridad/<int:numorden>', autoriza_salida_seguridad, name='autoriza_salida_seguridad'),
    path('autorizaseguridad', control_retorno_activos ,name='control_retorno_activos'),
    path('listar', listar_activos,name='listar_activos'),
    path('busqueda_activo_bodega', busqueda_activo_bodega,name='busqueda_activo_bodega'),
    path('listar_bajas', listar_bajas,name='listar_bajas'),
    path('listar_entregas_activos', listarRecepcionesforSeg ,name='listar_entregas_activos'),
    path('descargo_custodio/<int:numpedido>', descargo_custodio, name='descargo_custodio'),
    path('descargo_custodio_activold/<int:id>', descargo_custodio_activold, name='descargo_custodiold'),
    path('reportar_no_custodio/<int:id>', reportar_no_custodio, name='reportar_no_custodio'),
    
    
    path('descargo_custodio_activold_custom/<int:id>', descargo_custodio_activold_custom, name='descargo_custodiold_custom'),
    
    path('alertsave', registro_guardado ,name='registro_guardado'),
    path('alertsavesalida', registro_guardado_salida ,name='registro_guardado_salida'),
    path('filtrar', filtrar_activos,name='filtrar_activos'),
    path('customrep', filtrar_activos2,name='filtrar_activos2'),
    
    path('nomenclatura', genera_nomenclatura,name='genera_nomenclatura'),
    path('identifica', identifica_valores,name='identifica_valores'),
    path('identifica_activo', identifica_valores_mov_int,name='identifica_valores_mov_int'),
    path('bitacora', ultimos_movimientos,name='ultimos_movimientos'),
    path('toexcel', to_excelclass.as_view(),name='to_excelclass'),
    path('customtoexcel', custom_to_excelclass.as_view(),name='custom_to_excelclass'),

    path('tomba', to_mba.as_view(),name='to_mba'),
    path('to_excel_all', to_ExcelAll.as_view(),name='dall'),
    path('custom_excel_all', CustomExcelAll.as_view(),name='custom_all'),
    
    path('to_excel_bajas', to_ExcelBajas.as_view(),name='dbajas'),
    path('custom_excel_bajas', CustomExcelBajas.as_view(),name='custom_bajas'),
    
    
    path('mover/<int:pk>', ActivoMoverUbicacion.as_view(),name='mover_activos'),
    path('editar/<int:pk>', ActivoUpdate.as_view(),name='editar_activos'),
    #path('eliminar/<int:pk>', ActivoDelete.as_view(),name='eliminar_activos'),
    # path('cambia_estado/<int:pk>', ActivoCambiaEstado.as_view(),name='cambia_estado'),
    path('dar_baja/<int:id>/<str:estado>',cambiaEstadoBajaActivos,name='dar_baja'),
    path('printguia/<int:id>', imprimeSalidaActivos,name='imprime_guia_salida'),
    path('printguia_agri/<int:id>', imprimeSalidaActivosAgri,name='imprime_guia_salida_agri'),
    path('cambiaretornoestado/<int:id>/<str:estado>/<str:codigo>', cambiaEstadoRetorno,name='cambia_retorno_activo'),
    path('solicitud_salida/',SolicitudesSalidaActivos,name='solicitud_salida'),
    path('ver_salida/<int:numorden>',verSolicitudesSalida,name='ver_salida'),
    path('aprueba_bodega/<int:id>', apruebaBodegaSalida,name='aprueba_bodega'),
    path('recibe_activo_bodega/<str:codigo>', recibeActivoBodega, name='recibe_activo_bodega'),
    path('imprime_movimientos_internos/<str:codigo>', imprimeActaMovimientosInternos, name='imprime_movimientos_internos'),
    path('confirma_acta_recepcion_entregada/<int:numpedido>', confirma_acta_recepcion_entregada,name='confirma_acta_recepcion_entregada'),
    path('imprime_acta_custodio/<int:numpedido>', imprimeActaEntregaActivosCustodio, name='acta_de_entrega_custodio'),
    path('imprime_acta_custodio2/<int:id>', imprimeActaEntregaActivosCustodio2, name='acta_de_entrega_custodio2'),
    path('imprime_acta_custodiogl/<str:nombre>', imprimeActaEntregaActivosCustodioGlobal, name='acta_de_entrega_custodiogl'),
    path('entrega_activos_rep/<str:nombre>', imprimeActaEntregaActivosCustodioGlobal, name='entrega_activos_rep'),

]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)