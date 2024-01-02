from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail

from .views import IngresoPedido, ordenesPedido, EliminaPedido, EditaPedido, ordenesAprueba, apruebaDirect,\
                    rechazaDirect, cotizaPedidos, IngresoCotizaciones, pedidosCotizados, \
                    ApruebaCotiza, ordenesCompra, generaCompra, apruebaCompra, EditaPedidoAutoriza, \
                    listarActivaciones, activaActivo, activacionNo, activacionSi, listarRecepciones, \
                    recibidoProd, CodificaIngreso, entregaPedido, cancelaCompra, pdfCodigo, muestra, \
                    DuplicaPedido, editaCodifica, compraPedidos, observaReferencial, recibeProducto, \
                    listarComprasConta, datosCompraConta, apruebaFactura, autComprasExcel, actualizaObserva, \
                    muestraOrdenes, GeneraPagos, muestraOrdenesGa, detallePagos, apruebaPagos, rechazaPagos, \
                    muestraOrdenesConta, grabadoAct, AnularOrdenes, AnulaOrdenesConfirma, confirma_anulacion, \
                    entrega_de_activos, imprimeActaEntregaActivos, confirma_custodio, DevuelveCotiza, activacionesExcel, \
                    ubicaAreaAjax, consulta_expertos, listarPreguntasExperto, verPreguntasExperto, recuperaPreguntas, \
                    validaCotizacion, save_record_pre_cotiza, revisaCotizacion, save_estado_precotiza, eliminar_documentos, lookCotiza

urlpatterns = [
    #Anulación de Ordenes
    path('anular_orden/', AnularOrdenes, name = 'anular_orden'),
    path('anular_orden_confirma/<int:numpedido>', AnulaOrdenesConfirma, name='anula_ordenes_confirma'),
    path('confirma_anulacion/<int:numpedido>', confirma_anulacion, name='confirma_anulacion'),

    # Generacion de ordenes
    path('generar_orden/', IngresoPedido.as_view(), name = 'generar_orden'),
    path('duplicar_orden/<int:pk>', DuplicaPedido.as_view(), name = 'duplicar_orden'),
    path('ordenes/', ordenesPedido, name = 'listar_ordenes'),
    path('editar_orden/<int:pk>', EditaPedido.as_view(), name='editar_orden'),
    path('eliminar_pedido/<int:pk>', EliminaPedido.as_view(), name='eliminar_pedido'),
    path('recibe_producto/<int:numpedido>', recibeProducto, name='recibe_producto'),
    # Aprobacion de ordenes
    path('ordenesaprueba/', ordenesAprueba, name = 'aprueba_ordenes'),
    path('editar_pedido/<int:pk>', EditaPedidoAutoriza.as_view(), name='editar_pedido'),
    path('aprobado/<int:numpedido>', apruebaDirect, name='aprobado'),
    path('rechazado/<int:numpedido>', rechazaDirect, name='rechazado'),
    # Cotizacion de pedidos
    path('ordenescotizar/', cotizaPedidos, name='cotiza_pedidos'),
    path('cotizar_orden/<int:pk>', IngresoCotizaciones.as_view(), name='cotizar_orden'),
    path('observa_refer/<int:numpedido>', observaReferencial, name='observa_refer'),
    path('look_cotiza/<int:numpedido>', lookCotiza, name='look_cotiza'),
    path('ingreso_pagos', muestraOrdenes, name='ingreso_pagos'),
    path('genera_pagos', GeneraPagos.as_view(), name='genera_pagos'),
    path('orden_pago/<int:orden>', detallePagos, name='orden_pago'),
    # Seleccion de cotizacion
    path('seleccionar_cotizacion/', pedidosCotizados, name='selec_cotiza'),
    path('aprueba_cotizacion/<int:pk>', ApruebaCotiza.as_view(), name='aprueba_cotiza'),
    path('devuelve_cotizacion/<int:pk>', DevuelveCotiza.as_view(), name='devuelve_cotiza'),
    
    path('ver_compras/', compraPedidos, name='ver_compras'),
    # Genera ordenes compra
    path('ordenescompra/', ordenesCompra, name='ordenescompra'),
    path('generarcompra/<int:numpedido>', generaCompra, name='generarcompra'),
    path('apruebacompra/<int:numpedido>', apruebaCompra, name='apruebacompra'),
    path('actualizaobserva/<int:numpedido>', actualizaObserva, name='actualizaobserva'),
    path('cancelacompra/<int:numpedido>', cancelaCompra, name='cancelacompra'),
    path('reporte_compras/', autComprasExcel, name='reporte_compras'),
    path('reporte_activaciones/', activacionesExcel, name='reporte_activaciones'),
    path('aprueba_pagos', muestraOrdenesGa, name='aprueba_pagos'),
    path('aprobado_pago/<int:orden>', apruebaPagos, name='aprobado_pago'),
    path('rechazado_pago/<int:orden>', rechazaPagos, name='rechazado_pago'),
    # Activación de Activos
    path('activaciones/', listarActivaciones, name='activaciones'),
    path('activa/<int:numpedido>', activaActivo, name='activa'),
    path('activa_si/<int:numpedido>', activacionSi, name='activa_si'),
    path('activa_no/<int:numpedido>', activacionNo, name='activa_no'),
    path('compras_conta/', listarComprasConta, name='compras_conta'),
    path('compras_conta_det/<int:numpedido>', datosCompraConta, name='compras_conta_det'),
    path('aprobacion_factura/', apruebaFactura, name='aprobacion_factura'),
    path('pagos_ordenes', muestraOrdenesConta, name='pagos_ordenes'),
    # Recepcion Bodega
    path('recepcion', listarRecepciones, name='recepcion'),
    path('recibido/<int:numpedido>', recibidoProd, name='recibido'),
    path('grabado/<int:numpedido>', grabadoAct, name='grabado'),
    path('codificacion/<int:pk>', CodificaIngreso.as_view(), name='codificacion'),
    path('entrega/<int:numpedido>', entregaPedido, name='entrega'),
    path('crea_pdf/<str:nomen>', pdfCodigo, name='crea_pdf'),
    # Pruebas para nuevo ingreso
    path('ingreso_multi/', muestra, name='ingreso_multi'),
    path('entrega_de_activos/<int:numpedido>', entrega_de_activos, name='entrega_de_activos'),
    path('imprime_acta/<int:numpedido>', imprimeActaEntregaActivos, name='acta_de_entrega'),
    path('confirma_custodio/<int:numpedido>', confirma_custodio, name='confirma_custodio'),
    # Select dependiente ajax
    path('ubica_area_ajax', ubicaAreaAjax, name='ubica_area_ajax'),
    # Consulta a personas técnicas desde pantalla de aprobación de compras
    path('consultaexpertos/', consulta_expertos, name='consulta_expertos'),
    path('listarpreguntasexperto/', listarPreguntasExperto, name='listar_preguntas_experto'),
    path('verpreguntasexperto/<int:id>', verPreguntasExperto, name='ver_preguntas_rol_experto'),
    path('recuperapreguntas/', recuperaPreguntas, name='recupera_preguntas'),

    url(r'^(?P<pk>\d+)/valida-cotiza/$', validaCotizacion.as_view(), name='valida_cotizacion'),
    url(r'^(?P<pk>\d+)/revisa-cotiza/$', revisaCotizacion.as_view(), name='revisa_cotizacion'),
    path('saveprecotiza/<int:pk>', save_record_pre_cotiza,name='save_record_precotiza'),
    path('saveestadoprecotiza/', save_estado_precotiza,name='save_estado_precotiza'),
    path('eliminadocu/<int:pk>/<int:pedido>', eliminar_documentos,name='eliminar_documentos'),

]