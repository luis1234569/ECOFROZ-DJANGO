from django.urls import path, include, re_path
# from django.conf import settings
from django.conf.urls.static import static
# from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail

from .views import ingresoPedidoMulti, ordenesPedidoMulti

urlpatterns = [
    # Generacion de ordenes
    path('generar_multi_orden/', ingresoPedidoMulti, name = 'generar_multi_orden'),
    path('multi_ordenes/', ordenesPedidoMulti, name = 'listar_multi_ordenes'),
    # path('editar_orden/<int:pk>', EditaPedido.as_view(), name='editar_orden'),
    # path('eliminar_pedido/<int:pk>', EliminaPedido.as_view(), name='eliminar_pedido'),
    # # Aprobacion de ordenes
    # path('ordenesaprueba/', ordenesAprueba, name = 'aprueba_ordenes'),
    # path('editar_pedido/<int:pk>', EditaPedidoAutoriza.as_view(), name='editar_pedido'),
    # path('aprobado/<int:numpedido>', apruebaDirect, name='aprobado'),
    # path('rechazado/<int:numpedido>', rechazaDirect, name='rechazado'),
    # # Cotizacion de pedidos
    # path('ordenescotizar/', cotizaPedidos, name='cotiza_pedidos'),
    # path('cotizar_orden/<int:pk>', IngresoCotizaciones.as_view(), name='cotizar_orden'),
    # # Seleccion de cotizacion
    # path('seleccionar_cotizacion/', pedidosCotizados, name='selec_cotiza'),
    # path('aprueba_cotizacion/<int:pk>', ApruebaCotiza.as_view(), name='aprueba_cotiza'),
    # # Genera ordenes compra
    # path('ordenescompra/', ordenesCompra, name='ordenescompra'),
    # path('generarcompra/<int:numpedido>', generaCompra, name='generarcompra'),
    # path('apruebacompra/<int:numpedido>', apruebaCompra, name='apruebacompra'),
    # path('cancelacompra/<int:numpedido>', cancelaCompra, name='cancelacompra'),
    # # Activación de Activos
    # path('activaciones/', listarActivaciones, name='activaciones'),
    # path('activa/<int:numpedido>', activaActivo, name='activa'),
    # path('activa_si/<int:numpedido>', activacionSi, name='activa_si'),
    # path('activa_no/<int:numpedido>', activacionNo, name='activa_no'),
    # # Recepcion Bodega
    # path('recepcion', listarRecepciones, name='recepcion'),
    # path('recibido/<int:numpedido>', recibidoProd, name='recibido'),
    # path('codificacion/<int:pk>', CodificaIngreso.as_view(), name='codificacion'),
    # path('entrega/<int:numpedido>', entregaPedido, name='entrega'),
    # path('crea_pdf/<str:nomen>', pdfCodigo, name='crea_pdf'),
    # # Pruebas para nuevo ingreso
    # path('ingreso_multi/', muestra, name='ingreso_multi'),
]
