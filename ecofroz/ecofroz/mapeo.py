#URLS APP ACTIVOS

urlpatterns = [
    path('nuevo', registro_nuevov2 ,name='registro_nuevov2'),
    # path('nuevov2', registro_nuevov2,name='registro_nuevov2'),
    path('listar_salida', listarSalida, name='listar_salida'),
    path('aprueba_salida/<int:id>', confirmaSalida, name='aprueba_salida'),
    path('registrosalida', salida_activos_func ,name='salida_activos_func'),
    path('salida_activo', saleActivo, name='salida_activo'),
    path('controlretorno', control_retorno_activos ,name='control_retorno_activos'),
    path('listar', listar_activos,name='listar_activos'),
    path('alertsave', registro_guardado ,name='registro_guardado'),
    path('alertsavesalida', registro_guardado_salida ,name='registro_guardado_salida'),
    path('filtrar', filtrar_activos,name='filtrar_activos'),
    path('nomenclatura', genera_nomenclatura,name='genera_nomenclatura'),
    path('identifica', identifica_valores,name='identifica_valores'),
    path('bitacora', ultimos_movimientos,name='ultimos_movimientos'),
    path('toexcel', to_excelclass.as_view(),name='to_excelclass'),
    path('tomba', to_mba.as_view(),name='to_mba'),
    path('mover/<int:pk>', ActivoMoverUbicacion.as_view(),name='mover_activos'),
    path('editar/<int:pk>', ActivoUpdate.as_view(),name='editar_activos'),
    path('eliminar/<int:pk>', ActivoDelete.as_view(),name='eliminar_activos'),
    # path('cambia_estado/<int:pk>', ActivoCambiaEstado.as_view(),name='cambia_estado'),
    path('dar_baja/<int:id>/<str:estado>',cambiaEstadoBajaActivos,name='dar_baja'),
    path('printguia/<int:id>', imprimeSalidaActivos,name='imprime_guia_salida'),
    path('cambiaretornoestado/<int:id>/<str:estado>', cambiaEstadoRetorno,name='cambia_retorno_activo'),
    path('solicitud_salida/',SolicitudesSalidaActivos,name='solicitud_salida'),
]

#URLS APP PROVEEDORES

urlpatterns = [
    path('nuevo', nuevo_registro ,name='nuevo_registro'),
    path('nuevorolfun', render_template_x_tipo_proveedor ,name='render_template_x_tipo_proveedor'),
    path('listar', listar_proveedores,name='listar_proveedores'),
    #path('filtrar', filtrar_proveedores,name='filtrar_proveedores'),
    #path('filtrar', ver_preguntas,name='ver_preguntas'),
    path('preguntas', ver_preguntas,name='ver_preguntas'),
    path('eliminar/<int:pk>', ProveedorDelete.as_view(),name='eliminar_proveedor'),
    path('editar/<int:pk>', ProveedorUpdate.as_view(),name='editar_proveedor'),
    path('verdocumentos/<int:pk>', VerDocumentos.as_view(),name='ver_documentos'),
    path('toexcel/<int:pk>', exportExcelEncuesta,name='to_excel'),

]

#URLS APP ORDENPEDIDO

urlpatterns = [
    # Generacion de ordenes
    path('generar_orden/', IngresoPedido.as_view(), name = 'generar_orden'),
    path('duplicar_orden/<int:pk>', DuplicaPedido.as_view(), name = 'duplicar_orden'),
    path('ordenes/', ordenesPedido, name = 'listar_ordenes'),
    path('editar_orden/<int:pk>', EditaPedido.as_view(), name='editar_orden'),
    path('eliminar_pedido/<int:pk>', EliminaPedido.as_view(), name='eliminar_pedido'),
    # Aprobacion de ordenes
    path('ordenesaprueba/', ordenesAprueba, name = 'aprueba_ordenes'),
    path('editar_pedido/<int:pk>', EditaPedidoAutoriza.as_view(), name='editar_pedido'),
    path('aprobado/<int:numpedido>', apruebaDirect, name='aprobado'),
    path('rechazado/<int:numpedido>', rechazaDirect, name='rechazado'),
    # Cotizacion de pedidos
    path('ordenescotizar/', cotizaPedidos, name='cotiza_pedidos'),
    path('cotizar_orden/<int:pk>', IngresoCotizaciones.as_view(), name='cotizar_orden'),
    path('observa_refer/<int:numpedido>', observaReferencial, name='observa_refer'),
    # Seleccion de cotizacion
    path('seleccionar_cotizacion/', pedidosCotizados, name='selec_cotiza'),
    path('aprueba_cotizacion/<int:pk>', ApruebaCotiza.as_view(), name='aprueba_cotiza'),
    path('ver_compras/', compraPedidos, name='ver_compras'),
    # Genera ordenes compra
    path('ordenescompra/', ordenesCompra, name='ordenescompra'),
    path('generarcompra/<int:numpedido>', generaCompra, name='generarcompra'),
    path('apruebacompra/<int:numpedido>', apruebaCompra, name='apruebacompra'),
    path('cancelacompra/<int:numpedido>', cancelaCompra, name='cancelacompra'),
    # Activación de Activos
    path('activaciones/', listarActivaciones, name='activaciones'),
    path('activa/<int:pk>', CodificaIngreso.as_view(), name='activa'),
    path('activa_si/<int:numpedido>', activacionSi, name='activa_si'),
    path('activa_no/<int:numpedido>', activacionNo, name='activa_no'),
    # Recepcion Bodega
    path('recepcion', listarRecepciones, name='recepcion'),
    path('recibido/<int:numpedido>', recibidoProd, name='recibido'),
    path('codificacion/<int:numpedido>', editaCodifica, name='codificacion'),
    path('entrega/<int:numpedido>', entregaPedido, name='entrega'),
    path('crea_pdf/<str:nomen>', pdfCodigo, name='crea_pdf'),
    # Pruebas para nuevo ingreso
    path('ingreso_multi/', muestra, name='ingreso_multi'),
]

#URLS ORDENTRABAJO

urlpatterns = [
    # Generacion de ordenes
    path('generar_trabajo/', IngresoTrabajo.as_view(), name = 'generar_trabajo'),
    path('duplicar_trabajo/<int:pk>', DuplicaTrabajo.as_view(), name = 'duplicar_trabajo'),
    path('trabajos/', ordenesTrabajo, name = 'listar_trabajos'),
    path('recibe_servicio/<int:numtrabajo>', recibeServicio, name='recibe_servicio'),
    path('editar_trabajo/<int:pk>', EditaTrabajo.as_view(), name='editar_trabajo'),
    path('eliminar_trabajo/<int:pk>', EliminaTrabajo.as_view(), name='eliminar_trabajo'),
    # Aprobacion de ordenes
    path('trabajosaprueba/', trabajosAprueba, name = 'aprueba_trabajos'),
    path('editar_trabajo_aut/<int:pk>', EditaTrabajoAutoriza.as_view(), name='editar_trabajo_aut'),
    path('aprobado/<int:numpedido>', apruebaDirect, name='aprobado'),
    path('rechazado/<int:numpedido>', rechazaDirect, name='rechazado'),
    # Cotizacion de pedidos
    path('trabajoscotizar/', cotizaTrabajos, name='cotiza_trabajos'),
    path('cotizar_trabajo/<int:pk>', IngresoCotizaciones.as_view(), name='cotizar_trabajo'),
    path('observa_refer/<int:numtrabajo>', observaReferencial, name='observa_refer'),
    path('seleccionar_cotizacion/', trabajosCotizados, name='selec_cotiza'),
    path('aprueba_cotizacion/<int:pk>', ApruebaCotiza.as_view(), name='aprueba_cotiza'),
    path('ver_compras', compraTrabajos, name='ver_compras'),

    path('ordenescompra/', ordenesCompra, name='ordenescompra'),
    path('generarcompra/<int:numpedido>', generaCompra, name='generarcompra'),
    path('apruebacompra/<int:numpedido>', apruebaCompra, name='apruebacompra'),
    path('cancelacompra/<int:numpedido>', cancelaCompra, name='cancelacompra'),
  
    path('recepcion', ordenesBodega, name='recepcion'),
    path('recibido/<int:numtrabajo>', recibePedido, name='recibido'),
    path('recepcion_parcial/<int:numtrabajo>', recepParcial, name='recepcion_parcial'),
    path('recepcion_total/<int:numtrabajo>', recepTotal, name='recepcion_total'),
    path('detalle_entrega/<int:numtrabajo>', detalleEntrega, name='detalle_entrega'),
  
]






