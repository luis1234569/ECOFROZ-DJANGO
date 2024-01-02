from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail

from .views import IngresoTrabajo, ordenesTrabajo, DuplicaTrabajo, EditaTrabajo, EditaTrabajoAutoriza, EliminaTrabajo, \
    trabajosAprueba, apruebaDirect, rechazaDirect, cotizaTrabajos, IngresoCotizaciones, trabajosCotizados, \
    ApruebaCotiza, ordenesCompra, generaCompra, apruebaCompra, cancelaCompra, ordenesBodega, recepParcial, \
    recepTotal, recibePedido, detalleEntrega, compraTrabajos, recibeServicio, observaReferencial, listarComprasConta, \
    datosCompraConta, ordenesCompraDirecta, apruebaFactura, creaTrabajo, autComprasExcel, autCompraDirectaExcel, \
    actualizaObserva, CargaMbaPedidos, listarMba, gestionaMba, actualizaMbaPedidos, GeneraPagos, muestraOrdenesGa, detallePagos, apruebaPagos, rechazaPagos, \
    muestraOrdenesConta, muestraOrdenes, listar_pedidos_laboratorio, generar_ingreso_laboratorio, supervisaPedidos, supervisaPedidos1, \
    supervisaPedidos2, gaComprasExcel,AnularOrdenes,AnulaOrdenesConfirma, confirma_anulacion, DevuelveCotiza, regresaCDCotizacion, \
    ubicaAreaAjax, recuperaPreguntas, consulta_expertos, listarPreguntasExperto, verPreguntasExperto, reporteProyectos, \
    comprasPorProyectoExcel, RevisaTrabajoAutoriza, validaCotizacion, revisaCotizacion, save_record_pre_cotiza, save_estado_precotiza, eliminar_documentos, \
    lookCotiza, listarSolicitudesAnticipos,ajax_call_proveedor,ajax_call_trabajos, ajax_call_activos, add_solic, anulaSolicitudesAnticipos, listarApruebaAnticipos, \
    ajax_consulta_solic, ajax_aprueba_1n, ajax_rechaza_1n, listarGestionaAnticipos, ajax_aprueba_2n, ajax_rechaza_2n, revisaConta, saveComprobante

from .ajax import get_areas

urlpatterns = [

    #Anulacion de Ordenes
    path('anular_orden/', AnularOrdenes, name = 'anular_ordenes'),
    path('anular_orden_confirma/<int:numpedido>', AnulaOrdenesConfirma, name='anula_ordenes_confirma'),
    path('confirma_anulacion/<int:numpedido>', confirma_anulacion, name='confirma_anulacion'),

    # Generacion de ordenes
    path('generar_trabajo/', IngresoTrabajo.as_view(), name = 'generar_trabajo'),
    path('ingreso_laboratorio/', generar_ingreso_laboratorio.as_view(), name = 'generar_ingreso_laboratorio'),
    
    path('duplicar_trabajo/<int:pk>', DuplicaTrabajo.as_view(), name = 'duplicar_trabajo'),
    path('trabajos/', ordenesTrabajo, name = 'listar_trabajos'),
    path('laboratorio/', listar_pedidos_laboratorio, name = 'listar_pedidos_laboratorio'),
    
    path('recibe_servicio/<int:numtrabajo>', recibeServicio, name='recibe_servicio'),
    path('editar_trabajo/<int:pk>', EditaTrabajo.as_view(), name='editar_trabajo'),
    path('eliminar_trabajo/<int:pk>', EliminaTrabajo.as_view(), name='eliminar_trabajo'),
    # Aprobacion de ordenes
    path('supervisa_pedido/', supervisaPedidos, name='supervisa_pedido'),
    path('supervisa_pedido1/', supervisaPedidos1, name='supervisa_pedido1'),
    path('supervisa_pedido2/', supervisaPedidos2, name='supervisa_pedido2'),
    path('trabajosaprueba/', trabajosAprueba, name = 'aprueba_trabajos'),
    path('editar_trabajo_aut/<int:pk>', EditaTrabajoAutoriza.as_view(), name='editar_trabajo_aut'),
    path('revisa_trabajo_aut/<int:pk>', RevisaTrabajoAutoriza.as_view(), name='revisar_trabajo_aut'),
    
    path('aprobado/<int:numpedido>', apruebaDirect, name='aprobado'),
    path('rechazado/<int:numpedido>', rechazaDirect, name='rechazado'),
    path('reporte_comprasga/', gaComprasExcel, name='reporte_comprasga'),
    # Cotizacion de pedidos
    path('trabajoscotizar/', cotizaTrabajos, name='cotiza_trabajos'),
    path('cotizar_trabajo/<int:pk>', IngresoCotizaciones.as_view(), name='cotizar_trabajo'),
    path('observa_refer/<int:numtrabajo>', observaReferencial, name='observa_refer'),
    path('look_cotiza/<int:numtrabajo>', lookCotiza, name='look_cotiza'),
    path('ingreso_pagos', muestraOrdenes, name='ingreso_pagos'),
    path('genera_pagos', GeneraPagos.as_view(), name='genera_pagos'),
    path('orden_pago/<int:orden>', detallePagos, name='orden_pago'),
    # Seleccion de cotizacion
    path('seleccionar_cotizacion/', trabajosCotizados, name='selec_cotiza'),
    path('aprueba_cotizacion/<int:pk>', ApruebaCotiza.as_view(), name='aprueba_cotiza'),
    path('devuelve_cotizacion/<int:pk>', DevuelveCotiza.as_view(), name='devuelve_cotiza'),
    path('ver_compras', compraTrabajos, name='ver_compras'),
    path('retornacd_cotizacion/<int:numtrabajo>', regresaCDCotizacion, name='regresacd_cotizacion'),
    
    
    path('aprobacion_factura', apruebaFactura, name='aprobacion_factura'),
    # Genera ordenes compra
    path('ordenescompra/', ordenesCompra, name='ordenescompra'),
    path('comprasdirectas/', ordenesCompraDirecta, name='comprasdirectas'),
    path('generarcompra/<int:numpedido>', generaCompra, name='generarcompra'),
    path('apruebacompra/<int:numpedido>', apruebaCompra, name='apruebacompra'),
    path('actualizaobserva/<int:numpedido>', actualizaObserva, name='actualizaobserva'),
    path('cancelacompra/<int:numpedido>', cancelaCompra, name='cancelacompra'),
    path('reporte_compras/', autComprasExcel, name='reporte_compras'),
    path('reporte_directas/', autCompraDirectaExcel, name='reporte_directas'),
    path('aprueba_pagos', muestraOrdenesGa, name='aprueba_pagos'),
    path('aprobado_pago/<int:orden>', apruebaPagos, name='aprobado_pago'),
    path('rechazado_pago/<int:orden>', rechazaPagos, name='rechazado_pago'),
    # # Activación de Activos
    path('compras_conta/', listarComprasConta, name='compras_conta'),
    path('compras_conta_det/<int:numpedido>', datosCompraConta, name='compras_conta_det'),
    # path('activaciones/', listarActivaciones, name='activaciones'),
    # path('activa/<int:pk>', CodificaIngreso.as_view(), name='activa'),
    # path('activa_si/<int:numpedido>', activacionSi, name='activa_si'),
    # path('activa_no/<int:numpedido>', activacionNo, name='activa_no'),
    path('pagos_ordenes', muestraOrdenesConta, name='pagos_ordenes'),
    # # Recepcion Bodega
    path('recepcion', ordenesBodega, name='recepcion'),
    path('recibido/<int:numtrabajo>', recibePedido, name='recibido'),
    path('recepcion_parcial/<int:numtrabajo>', recepParcial, name='recepcion_parcial'),
    path('recepcion_total/<int:numtrabajo>', recepTotal, name='recepcion_total'),
    path('detalle_entrega/<int:numtrabajo>', detalleEntrega, name='detalle_entrega'),
    # path('codificacion/<int:numpedido>', editaCodifica, name='codificacion'),
    # path('crea_pdf/<str:nomen>', pdfCodigo, name='crea_pdf'),
    # # Pruebas para nuevo ingreso
    # path('ingreso_multi/', muestra, name='ingreso_multi'),
    path('crea_trabajo/', creaTrabajo, name = 'crea_trabajo'),
    # url(r'^ajax/get_areas/', get_areas, name = 'get_areas'),
    path('ajax/get_areas/', get_areas, name = 'get_areas'),
    url(r'^(?P<pk>\d+)/carga-mba/$', CargaMbaPedidos.as_view(), name='carga-mba'),
    path('pedidos_mba/', listarMba, name='pedidos_mba'),
    path('gestionamba/<int:id>', gestionaMba, name='gestionamba'),
    path('actualiza-mba/', actualizaMbaPedidos, name='actualiza-mba'),
    # url(r'^(?P<pk>\d+)/actualiza-mba/$', ActualizaMbaPedidos.as_view(), name='actualiza-mba'),
    # Select dependiente ajax
    path('ubica_area_ajax', ubicaAreaAjax, name='ubica_area_ajax'),

    path('consultaexpertos/', consulta_expertos, name='consulta_expertos'),
    path('listarpreguntasexperto/', listarPreguntasExperto, name='listar_preguntas_experto'),
    path('verpreguntasexperto/<int:id>', verPreguntasExperto, name='ver_preguntas_rol_experto'),
    path('recuperapreguntas/', recuperaPreguntas, name='recupera_preguntas'),
    path('reporteproyectos/', reporteProyectos, name='reporte_proyectos'),
    path('reporte_compras_por_proyecto/', comprasPorProyectoExcel, name='reporte_compras_por_proyecto'),

    url(r'^(?P<pk>\d+)/valida-cotiza/$', validaCotizacion.as_view(), name='valida_cotizacion'),
    url(r'^(?P<pk>\d+)/revisa-cotiza/$', revisaCotizacion.as_view(), name='revisa_cotizacion'),
    path('saveprecotiza/<int:pk>', save_record_pre_cotiza,name='save_record_precotiza'),
    # path('saverevprecotiza/<int:pk>', save_rev_precotiza,name='save_rev_precotiza'),
    path('saveestadoprecotiza/', save_estado_precotiza,name='save_estado_precotiza'),
    path('eliminadocu/<int:pk>/<int:trabajo>', eliminar_documentos,name='eliminar_documentos'),

    path('listarsolicanticip/', listarSolicitudesAnticipos, name='listar_solicitudes_anticipos'),
    path('ajaxcallproveedor/', ajax_call_proveedor, name='ajaxcallproveedor'),
    path('ajaxcalltrabajos/', ajax_call_trabajos, name='ajaxcalltrabajos'),
    path('ajaxcallactivos/', ajax_call_activos, name='ajaxcallactivos'),
    path('listarsolicanticip/add_solic/', add_solic, name = 'add_solic'),
    path('listarapruebaanticipos1n/ajaxconsultasolic/', ajax_consulta_solic, name='ajaxconsultasolic'),
    path('listargestionaanticipos2n/ajaxconsultasolic/', ajax_consulta_solic, name='ajaxconsultasolic'),
    path('listarapruebaanticipos1n/ajax_save_autoriza/', ajax_aprueba_1n, name='ajax_save_autoriza'),
    path('listargestionaanticipos2n/ajax_save_autoriza_conta/', ajax_aprueba_2n, name='ajax_save_autoriza_conta'),
    path('listarapruebaanticipos1n/ajax_save_rechaza/', ajax_rechaza_1n, name='ajax_save_rechaza'),
    path('listargestionaanticipos2n/ajax_save_rechaza_conta/', ajax_rechaza_2n, name='ajax_save_rechaza_conta'),
    
    path('anulasolicanticip/<int:numsolic>', anulaSolicitudesAnticipos, name='anula_solic_anticipos'),

    path('listarapruebaanticipos1n/', listarApruebaAnticipos, name = 'listar_aprueba_anticipos_1n'),
    path('listargestionaanticipos2n/', listarGestionaAnticipos, name = 'listar_gestiona_anticipos_2n'),
   
    path('revisaconta/<int:numsolic>', revisaConta, name = 'revisa_conta'),
    path('savecomprobante/<int:pk>', saveComprobante, name='save_comprobante'),

]

