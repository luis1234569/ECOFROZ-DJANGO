from django.db import models

from apps.activos.models import activo_depar, activo_areas, activo_tipo, activo_ubica, activo_grupo
from apps.usuarios.models import User
from apps.proveedores.models import proveedor
from apps.parametrosGlobales.models import proyectos_contabilidad

# Create your models here.

tiempos={
    # ('hora','Horas'),
    # ('dia','Dias'),
    # ('semana','Semanas'),
    # ('mes','Meses'),
    ('anio','Años'),
}

medidas={
    ('unidad','Unidad'),
    # ('m','Metro'),
    # ('cm','Centimetro'),
    # ('mm','Milimetro'),
    # ('lt','Litros'),
    # ('gl','Galones'),
    # ('gr','Gramos'),
    # ('kg','Kilos'),
    # ('lb','Libras'),
}


estado={
    ('','Pendiente'),
    (1,'Aprobado'),
    (0,'No Aprobado'),
    (2,'Anulada')
}

proveedores={
    (1,'COREPTEC'),
    (2,'DELCORP S.A.'),
    (3,'IDC'),
    (4,'GRUPASA'),
    (5,'ELECTROLEG'),
    (6,'GRUENTEC'),
}

motivos={
    ('nuevo','Nuevo'),
    ('reemplazo_m','Reemplazo por Mejora'),
    ('reemplazo_o','Reemplazo por Obsolescencia'),
    ('reemplazo_r','Reemplazo por Reparación'),
}

reemplazos={
    (1,'Dar de Baja'),
    (2,'Reubicación'),
    (3,'Backup'),
    (4,'Reparación'),
    (5,'Venta'),
}

origenes={
    (1,'MBA'),
    (2,'SIA'),
    (3,'RESERVA'),
}

vida={
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
    (13, '13'),
    (14, '14'),
    (15, '15'),
    (16, '16'),
    (17, '17'),
    (18, '18'),
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
    (24, '24'),
    (25, '25'),
}

class OrdenesPedidos(models.Model):
    numpedido = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.ForeignKey(activo_areas, models.DO_NOTHING, null=True, blank=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING)
    usuario_aprueba = models.CharField(max_length=100, blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True, choices=estado)
    observa_selec_cot = models.CharField(max_length=2500, null=True, blank=True)
    fchsolicita = models.DateField(auto_now_add=True)
    fchsolicitatxt = models.CharField(max_length=8, blank=True, null=True)
    tipoactivo = models.ForeignKey(activo_tipo, models.DO_NOTHING)
    tiempo_vida = models.IntegerField(choices=vida)
    tiempo_tipo = models.CharField(max_length=7, choices=tiempos, default='anio')
    numproyecto = models.ForeignKey(proyectos_contabilidad, models.DO_NOTHING, null=True, blank=True)
    regimenespecial = models.BooleanField(blank=True, null=True, default=False)
    proveedor = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    fchaprueba = models.DateField(auto_now=False, blank=True, null=True)
    fchapruebatxt = models.CharField(max_length=8, blank=True, null=True)
    motRechaza = models.CharField(max_length=250, blank=True, null=True)
    usuario_cotiza = models.CharField(max_length=100, blank=True, null=True)
    estado_cotiza = models.BooleanField(null=True, blank=True)
    cotiza_observa = models.CharField(max_length=2500, blank=True, null=True)
    fchcotiza = models.DateField(auto_now=False, blank=True, null=True)
    fchcotizatxt = models.CharField(max_length=8, blank=True, null=True)
    select_cotiza = models.BooleanField(max_length=250, blank=True, null=True)
    fchselectcotiza = models.DateField(auto_now=False, blank=True, null=True)
    fchselectcotizatxt = models.CharField(max_length=8, blank=True, null=True)
    usuario_genera = models.CharField(max_length=100, blank=True, null=True)
    genera_compra = models.IntegerField(blank=True, null=True)
    observa_compra = models.CharField(max_length=2500, blank=True, null=True)
    fchgenerac = models.DateField(auto_now=False, blank=True, null=True)
    fchgeneractxt = models.CharField(max_length=8, blank=True, null=True)
    motivo_compra = models.CharField(max_length=50, blank=False, null=True, choices=motivos)
    justificacion_compra = models.CharField(max_length=5000, blank=True, null=True)
    reemplazo_accion = models.IntegerField(choices=reemplazos, blank=True, null=True)
    reemplazo_observa = models.CharField(max_length=2500, blank=True, null=True)
    activado_activo = models.BooleanField(blank=True, null=True) 
    activado_observa = models.CharField(max_length=250, blank=True, null=True)
    fecha_activacion = models.DateField(blank=True, null=True)
    fchactivatxt = models.CharField(max_length=8, blank=True, null=True)
    usuario_recibe = models.BooleanField(null=True, blank=True)
    recibido_bodega = models.BooleanField(blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fchrecibetxt = models.CharField(max_length=8, blank=True, null=True)
    codigo_genera = models.BooleanField(blank=True, null=True)
    entregado_bodega =  models.BooleanField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fchengtregatxt = models.CharField(max_length=8, blank=True, null=True)
    entrega_observa = models.CharField(max_length=2500, blank=True, null=True)
    ord = models.DateTimeField(auto_now=True)
    cod_activo = models.CharField(max_length=10, blank=True, null=True)
    entrega_solicita = models.BooleanField(blank=True, null=True)
    ubica = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    parte_activo = models.BooleanField(blank=True, null=True)
    compra_directa = models.BooleanField(blank=True, null=True)
    aceptacion_factura = models.BooleanField(blank=True, null=True)
    valor_factura = models.FloatField(blank=True, null=True)
    numero_factura = models.CharField(max_length=50, blank=True, null=True)
    usuario_factura = models.CharField(max_length=100, blank=True, null=True)
    fch_factura = models.DateField(blank=True, null=True)
    fch_factura_txt = models.CharField(max_length=8, blank=True, null=True)
    codigo_mba = models.CharField(max_length=250, blank=True, null=True)
    grabado_activo = models.BooleanField(blank=True, null=True)
    persona_retira_de_bodega = models.CharField(max_length=250, blank=True, null=True)
    persona_entrega_en_bodega = models.CharField(max_length=250, blank=True, null=True)
    custodio_sugerido = models.CharField(max_length=250, blank=True, null=True)
    descargo_custodio = models.BooleanField(blank=True, null=True)
    descargo_custodio_observa = models.CharField(max_length=2500, blank=True, null=True)
    fecha_descargo_custodio = models.DateField(blank=True, null=True)
    persona_confirma_descargo = models.CharField(max_length=250, blank=True, null=True)
    acta_entregada = models.BooleanField(blank=True, null=True)
    estado_consulta_experto = models.IntegerField(blank=True, null=True) 
    codigo_activo_reemplazado =  models.CharField(max_length=10, blank=True, null=True)
    fchprecotiza = models.DateTimeField(null=True, blank=True)
    fchpreresponde = models.DateTimeField(null=True, blank=True)
    estado_precotiza = models.BooleanField(blank=True, null=True)
    estado_responde_precotiza = models.BooleanField(blank=True, null=True)
    usuario_precotiza = models.CharField(max_length=100, blank=True, null=True)
    no_codificable = models.BooleanField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'pedidos\".\"ordenespedidos'

        verbose_name = 'Orden Pedido'
        verbose_name_plural = 'Ordenes Pedidos'
        permissions = (
            ('aprueba_ordenespedidos', 'Aprueba Ordenes de Pedidos'),
            ('genera_ordenescompra', 'Genera Ordenes de Conpra'),
            ('activa_activos', 'Activación de Activos'),
            ('acceso_pedidos', 'Acceso a Pedidos'),
            ('facturacion', 'Revisión de Facturación'),
            ('facturas_laboratorio', 'Ingreso de Facturas Laboratorio'),
            ('preguntas_experto', 'Preguntas Rol Experto'),

        
        )
        ordering = ['-numpedido']

class DetallePedido(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidos', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=5000, blank=True, null=True)
    unimedida = models.CharField(max_length=15, blank=True, null=True, choices=medidas)
    img_1 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 2')
    cotiza_Ref = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización Referencial')
    otros_doc = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Otros Documentos', max_length=500)
    otros_doc_adqui = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Documentos Adquisiciones', max_length=500)
    observa_envia_precotiza = models.CharField(max_length=5000, blank=True, null=True)
    observa_responde_precotiza = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"detallepedido'

        verbose_name = 'Detalle Pedido'
        verbose_name_plural = 'Detalles Pedidos'
        permissions = (
            ('menu_bodega', 'Acceso al menu de bodega'),
        )


class CotizaPedido(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidos', null=True, blank=True, on_delete=models.CASCADE)
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor')
    empresa_cotiza = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    pdf_cotiza = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización')
    cotiza_seleccion = models.BooleanField(null=True, blank=True, verbose_name='Selección')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"cotizapedido'

        verbose_name = 'Cotización'
        verbose_name_plural = 'Cotizaciones'
        permissions = (
            ('selecciona_cotizapedido', 'Seleccionar Cotizaciones'),
        )

class ConsultaExperto(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidos', null=True, blank=True, on_delete=models.CASCADE)
    fecha_pregunta = models.DateTimeField(null=True, blank=True)
    pregunta = models.CharField(max_length=5000, blank=True, null=True)
    respuesta = models.CharField(max_length=5000, blank=True, null=True)
    persona_pregunta = models.ForeignKey(User, models.DO_NOTHING, related_name='realiza_pregunta')
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
   
    class Meta:
        managed = True
        db_table = 'pedidos\".\"consulta_experto'


class Consultados(models.Model):
    responsable = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    consultadoa = models.ManyToManyField(ConsultaExperto, blank=True, related_name='consul')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"consultados'      



################TABLAS HISTORICAS###################E

class RechazaOrdenesPedidos(models.Model):
    numpedido = models.IntegerField(primary_key=True)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.ForeignKey(activo_areas, models.DO_NOTHING, null=True, blank=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING)
    usuario_aprueba = models.CharField(max_length=100, blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True, choices=estado)
    observa_selec_cot = models.CharField(max_length=250, null=True, blank=True)
    fchsolicita = models.DateField(auto_now_add=True)
    fchsolicitatxt = models.CharField(max_length=8, blank=True, null=True)
    tipoactivo = models.ForeignKey(activo_tipo, models.DO_NOTHING)
    tiempo_vida = models.IntegerField()
    tiempo_tipo = models.CharField(max_length=7, choices=tiempos)
    numproyecto = models.CharField(max_length=70, blank=True, null=True)
    regimenespecial = models.BooleanField(blank=True, null=True, default=False)
    proveedor = models.CharField(max_length=150, blank=True, null=True)
    files = models.CharField(max_length=1000, blank=True, null=True)
    fchaprueba = models.DateField(auto_now=False, blank=True, null=True)
    fchapruebatxt = models.CharField(max_length=8, blank=True, null=True)
    motRechaza = models.CharField(max_length=250, blank=True, null=True)
    estado_cotiza = models.BooleanField(null=True, blank=True)
    cotiza_observa = models.CharField(max_length=250, blank=True, null=True)
    select_cotiza = models.BooleanField(max_length=250, blank=True, null=True)
    genera_compra = models.IntegerField(blank=True, null=True)
    observa_compra = models.CharField(max_length=250, blank=True, null=True)
    motivo_compra = models.CharField(max_length=50, blank=False, null=True, choices=motivos)
    justificacion_compra = models.CharField(max_length=250, blank=True, null=True)
    reemplazo_accion = models.IntegerField(choices=reemplazos, blank=True, null=True)
    reemplazo_observa = models.CharField(max_length=250, blank=True, null=True)
    activado_activo = models.BooleanField(blank=True, null=True)
    fecha_activacion = models.DateField(blank=True, null=True)
    recibido_bodega = models.BooleanField(blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    codigo_genera = models.BooleanField(blank=True, null=True)
    entregado_bodega =  models.BooleanField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    entrega_observa = models.CharField(max_length=250, blank=True, null=True)
    ord = models.DateTimeField(auto_now=True)
    cod_activo = models.CharField(max_length=10, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'pedidos\".\"ordenespedidosrechaza'

        verbose_name = 'Orden Pedido Rechazada'
        verbose_name_plural = 'Ordenes Pedidos Rechazadas'

class RechazaDetallePedido(models.Model):
    numpedido = models.ForeignKey('RechazaOrdenesPedidos', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    unimedida = models.CharField(max_length=15, blank=True, null=True, choices=medidas)
    img_1 = models.CharField(max_length=250, blank=True, null=True)
    img_2 = models.CharField(max_length=250, blank=True, null=True)
    cotiza_Ref = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"detallepedidorechaza'

        verbose_name = 'Detalle Pedido Rechazada'
        verbose_name_plural = 'Detalles Pedidos Rechazadas'

class RechazaCotizaPedido(models.Model):
    numpedido = models.ForeignKey('RechazaOrdenesPedidos', null=True, blank=True, on_delete=models.CASCADE)
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor')
    empresa_cotiza = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    pdf_cotiza = models.CharField(max_length=250, blank=True, null=True)
    cotiza_seleccion = models.BooleanField(null=True, blank=True, verbose_name='Selección')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"cotizapedidorechaza'

        verbose_name = 'Cotización Rechazada'
        verbose_name_plural = 'Cotizaciones Rechazadas'

class SecuencialCodifica(models.Model):
    codigo = models.CharField(max_length=1)
    numeracion = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'activos\".\"secuencialcodifica'

        verbose_name = 'Codificación Secuencial'
        verbose_name_plural = 'Codificaciones Secuenciales'

class OrdenesPago(models.Model):
    fch_genera = models.DateField(blank=True, null=True)
    fch_genera_txt = models.CharField(max_length=8, blank=True, null=True)
    origen = models.IntegerField(blank=True, null=True, choices=origenes)
    numero = models.CharField(max_length=25, blank=True,null=True)
    documento = models.FileField(upload_to='pagos/', blank=True, null=True, verbose_name='Pagos')
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING)
    estado = models.BooleanField(null=True, blank=True)
    observaciones_adqui = models.CharField(max_length=2500, blank=True, null=True)
    observaciones_ga = models.CharField(max_length=2500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"ordenespago'

        verbose_name = 'Orden de Pago'
        verbose_name_plural = 'Ordenes de Pagos'
        permissions = (
            ('menu_ingreso_pagos', 'Acceso al menu de Ingreso Pagos'),
            ('menu_autoriza_pagos', 'Acceso al menu de Autrización Pagos'),
            ('menu_consulta_pagos', 'Acceso al menu de Consulta Pagos'),
        )

class PreCotiza(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidos', models.DO_NOTHING,blank=True,null=True)
    archivos = models.FileField(upload_to='cotizaciones/',blank=True, null=True)
    nombre_corto = models.CharField(max_length=1000, blank=True, null=True)
    seleccion = models.BooleanField(null=True, blank=True)
    fecha_pre_cotiza = models.DateField(auto_now_add=True)
    escrito = models.BooleanField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"pre_cotiza_activos' 