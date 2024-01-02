from django.db import models

from apps.activos.models import activo_depar, activo_areas, activo_tipo, activo_grupo, activo_ubica
from apps.usuarios.models import User
from apps.proveedores.models import proveedor
from apps.ordenPedido.models import OrdenesPedidos
from apps.parametrosGlobales.models import proyectos_contabilidad

# Create your models here.

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
    (0,'Pendiente'),
    (1,'Aprobado Ger'),
    (2,'Gestionado Conta'),
    (3,'Rechazada Ger'),
    (4,'Rechazada Conta')
}

tipo_tr={
    (1,'Interno'),
    (2,'Externo'),
}

tipo_ped={
    # ('PR', 'Proyecto'),
    ('MP', 'Mantenimiento Preventivo'),
    ('MC', 'Mantenimiento Correctivo'),
    ('OT', 'Otros Insumos'),
    ('OS', 'Orden de Servicio'), 
    ('AM', 'ANALISIS MICROBIOLOGICO'), 
    ('AP', 'ANALISIS DE PESTICIDAS'), 
    ('CA', 'SERVICIO DE CALIBRACIÓN'), 
    ('CP', 'CONTROL DE PLAGAS'), 
  # ('LC', 'Laboratorio Calidad'),  Este tipo si existe pero se escribe directamente a la base sin ser mostrado en el template de ingreso de ordenes
}

orden_ref={
    (True, 'SI'),
    (False, 'NO'),
}

origenes={
    (1,'MBA'),
    (2,'SIA/ACTIVOS'),
    (3,'SIA/TRABAJOS'),
}

class OrdenesTrabajos(models.Model):
    numtrabajo = models.AutoField(primary_key=True)
    tipo_trabajo = models.IntegerField(choices=tipo_tr, default=None, blank=True, null=True)
    tipo_pedi = models.ForeignKey('TipoPedido', models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.ForeignKey(activo_areas, models.DO_NOTHING, null=True, blank=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING)
    usuario_aprueba = models.IntegerField(blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True, choices=estado)
    observa_selec_cot = models.CharField(max_length=2500, null=True, blank=True)
    fchsolicita = models.DateField(auto_now_add=True)
    fchsolicitatxt = models.CharField(max_length=8, blank=True, null=True)
    numproyecto = models.ForeignKey(proyectos_contabilidad, models.DO_NOTHING, null=True, blank=True)
    proveedor = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    fchaprueba = models.DateField(blank=True, null=True)
    fchapruebatxt = models.CharField(max_length=8, blank=True, null=True)
    motRechaza = models.CharField(max_length=2000, blank=True, null=True)
    usuario_cotiza = models.CharField(max_length=100, blank=True, null=True)
    estado_cotiza = models.BooleanField(null=True, blank=True)
    cotiza_observa = models.CharField(max_length=2500, blank=True, null=True)
    fchcotiza = models.DateField(blank=True, null=True)
    fchcotizatxt = models.CharField(max_length=8, blank=True, null=True)
    select_cotiza = models.BooleanField(max_length=250, blank=True, null=True)
    fchselectcotiza = models.DateField(auto_now=False, blank=True, null=True)
    fchselectcotizatxt = models.CharField(max_length=8, blank=True, null=True)
    usuario_genera = models.IntegerField(blank=True, null=True)
    genera_compra = models.IntegerField(blank=True, null=True)
    observa_compra = models.CharField(max_length=2500, blank=True, null=True)
    fchgenerac = models.DateField(blank=True, null=True)
    fchgeneractxt = models.CharField(max_length=8, blank=True, null=True)
    justificacion_compra = models.CharField(max_length=2000, blank=True, null=True)
    activado_activo = models.BooleanField(blank=True, null=True)
    activado_observa = models.CharField(max_length=2500, blank=True, null=True)
    fecha_activacion = models.DateField(blank=True, null=True)
    fchactivatxt = models.CharField(max_length=8, blank=True, null=True)
    usuario_recibe = models.IntegerField(null=True, blank=True)
    recibido_bodega = models.BooleanField(blank=True, null=True)
    fecha_recepcion = models.DateField(blank=True, null=True)
    fchrecibetxt = models.CharField(max_length=8, blank=True, null=True)
    codigo_genera = models.BooleanField(blank=True, null=True)
    entregado_bodega =  models.BooleanField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    fchengtregatxt = models.CharField(max_length=8, blank=True, null=True)
    entrega_observa = models.CharField(max_length=2500, blank=True, null=True)
    compra_directa = models.BooleanField(blank=True, null=True)
    tipo_liquida= models.IntegerField(blank=True, null=True)
    total_observa = models.CharField(max_length=2500, blank=True, null=True)
    refer_orden = models.BooleanField(blank=True, null=True, choices=orden_ref, default=None)
    orden_referencial = models.IntegerField(blank=True, null=True)
    salida_activo = models.BooleanField(blank=True, null=True, choices=orden_ref, default=None)
    salida_genera = models.BooleanField(blank=True, null=True)
    ord = models.DateTimeField(auto_now=True)
    entrega_solicita = models.BooleanField(blank=True, null=True)
    ubica = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    aceptacion_factura = models.BooleanField(blank=True, null=True)
    valor_factura = models.FloatField(blank=True, null=True)
    numero_factura = models.CharField(max_length=50, blank=True, null=True)
    usuario_factura = models.CharField(max_length=100, blank=True, null=True)
    fch_factura = models.DateField(blank=True, null=True)
    fch_factura_txt = models.CharField(max_length=8, blank=True, null=True)
    pago_mba = models.BooleanField(blank=True, null=True)
    estado_consulta_experto = models.IntegerField(blank=True, null=True)
    fchprecotiza = models.DateTimeField(null=True, blank=True)
    fchpreresponde = models.DateTimeField(null=True, blank=True)
    estado_precotiza = models.BooleanField(blank=True, null=True)
    estado_responde_precotiza = models.BooleanField(blank=True, null=True)
    usuario_precotiza = models.CharField(max_length=100, blank=True, null=True)
    usuario_anula = models.CharField(max_length=50, blank=True, null=True)
    insumos = models.BooleanField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'pedidos\".\"ordenestrabajos'

        verbose_name = 'Orden Trabajo'
        verbose_name_plural = 'Ordenes Trabajos'
        permissions = (
            ('acceso_ordenes', 'Acceso a Ordenes'),
            ('supervisa_ordenes', 'Supervisión de Ordenes'),
            ('supervisa_ordenes_ga', 'Supervisión de Ordenes GA'),
            ('supervisa_ordenes2', 'Supervisión de Ordenes 2'),
            ('reporte_ga', 'Reporte GA'),
            ('reporte_requisiciones_por_proyecto', 'Reporte Proyectos'),

        )

class DetalleTrabajo(models.Model):
    numtrabajo = models.ForeignKey('OrdenesTrabajos', related_name = 'camello', on_delete=models.CASCADE)
    cantidad = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=5000, blank=True, null=True)
    unimedida = models.CharField(max_length=15, blank=True, null=True, choices=medidas)
    img_1 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 2')
    cotiza_Ref = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización Referencial', max_length=500)
    otros_doc = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Otros Documentos', max_length=500)
    otros_doc_adqui = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Documentos Adquisiciones', max_length=500)
    observa_envia_precotiza = models.CharField(max_length=5000, blank=True, null=True)
    observa_responde_precotiza = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"detalletrabajo'

        verbose_name = 'Detalle Trabajo'
        verbose_name_plural = 'Detalles Trabajos'

class CotizaTrabajo(models.Model):
    numtrabajo = models.ForeignKey('OrdenesTrabajos', on_delete=models.CASCADE)
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor')
    empresa_cotiza = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    pdf_cotiza = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización')
    cotiza_seleccion = models.BooleanField(null=True, blank=True, verbose_name='Selección')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"cotizatrabajo'

        verbose_name = 'Cotización Trabajo'
        verbose_name_plural = 'Cotizaciones Trabajos'
        permissions = (
            ('selecciona_cotizatrabajo', 'Seleccionar Cotizaciones Trabajos'),
        )

class PedidosMba(models.Model):
    documentos = models.FileField(upload_to='documentos_mba/', blank=True, null=True, verbose_name='Documentos MBA', max_length=500)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    fch_carga = models.DateField(blank=True, null=True)
    fch_carga_txt = models.CharField(max_length=8, blank=True, null=True)
    estado_gestion = models.BooleanField(null=True, blank=True)
    ordenar = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"pedidos_mba'

        verbose_name = 'Pedido MBA'
        verbose_name_plural = 'Pedidos MBA'
        permissions = (
            ('ingreso_pedidos_mba', 'Ingreso de Pedidos MBA'),
        )

class TrabajosPago(models.Model):
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
        db_table = 'pedidos\".\"trabajospago'

        verbose_name = 'Orden de Pago de Trabajo'
        verbose_name_plural = 'Ordenes de Pagos de Trabajos'

class TipoPedido(models.Model):
    cod = models.CharField(max_length=25, primary_key=True)
    nombre = models.CharField(max_length=150, blank=True,null=True)
    tipo = models.CharField(max_length=25, blank=True,null=True)
    estado = models.BooleanField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"tipopedido'

        verbose_name = 'Tipo Pedido'
        verbose_name_plural = 'Tipos Pedidos'
    
    def __str__(self):
        return self.nombre

class ConsultaExpertoTrab(models.Model):
    numtrabajo = models.ForeignKey('OrdenesTrabajos', null=True, blank=True, on_delete=models.CASCADE)
    fecha_pregunta = models.DateTimeField(null=True, blank=True)
    pregunta = models.CharField(max_length=5000, blank=True, null=True)
    respuesta = models.CharField(max_length=5000, blank=True, null=True)
    persona_pregunta = models.ForeignKey(User, models.DO_NOTHING, related_name='realiza_pregunta_trab')
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
   
    class Meta:
        managed = True
        db_table = 'pedidos\".\"consulta_experto_trab'


class ConsultadosTrab(models.Model):
    responsable = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    consultadoa = models.ManyToManyField(ConsultaExpertoTrab, blank=True, related_name='consul_trab')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"consultados_trab'  

class PreCotiza(models.Model):
    numtrabajo = models.ForeignKey('OrdenesTrabajos', models.DO_NOTHING,blank=True,null=True)
    archivos = models.FileField(upload_to='cotizaciones/',blank=True, null=True)
    nombre_corto = models.CharField(max_length=1000, blank=True, null=True)
    seleccion = models.BooleanField(null=True, blank=True)
    fecha_pre_cotiza = models.DateField(auto_now_add=True)
    escrito = models.BooleanField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"pre_cotiza_trab' 

class PreCotizaDet(models.Model):
    numtrabajo = models.ForeignKey('PreCotiza', models.DO_NOTHING,blank=True,null=True)
    archivos = models.FileField(upload_to='pre_cotiza/',blank=True, null=True)
    nombre_corto = models.CharField(max_length=1000, blank=True, null=True)
    observa_adqui = models.CharField(max_length=20000, blank=True, null=True)
    observa_solicita = models.CharField(max_length=20000, blank=True, null=True)
    fecha_pre_cotiza = models.DateTimeField(null=True, blank=True)
    fecha_pre_responde = models.DateTimeField(null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'pedidos\".\"pre_cotiza_trab_det' 

class SolicitudesAdqui(models.Model):
    numsolic = models.AutoField(primary_key=True)
    psolicita = models.CharField(max_length=100, blank=True, null=True)
    observa_solicita = models.CharField(max_length=2500, blank=True, null=True)
    fch_solicita = models.DateTimeField(null=True, blank=True)
    origen = models.IntegerField(blank=True, null=True, choices=origenes)
    usuario_aprueba = models.ForeignKey(User, models.DO_NOTHING, related_name='paprueba', blank=True,null=True)
    aprobado_ger = models.BooleanField(null=True, blank=True)
    aceptado_conta = models.BooleanField(null=True, blank=True)
    enviada = models.BooleanField(null=True, blank=True)
    observa_autoriza = models.CharField(max_length=2500, blank=True, null=True)
    fch_aprueba = models.DateTimeField(null=True, blank=True)
    numtrabajo = models.ForeignKey(OrdenesTrabajos, blank=True, related_name='trabajo', null=True, on_delete=models.DO_NOTHING)
    numpedido = models.ForeignKey(OrdenesPedidos, blank=True, null=True, related_name='activo', on_delete=models.DO_NOTHING)
    num_mba = models.IntegerField(blank=True, null=True)
    prove = models.ForeignKey(proveedor, blank=True, null=True, related_name='proveedor', on_delete=models.DO_NOTHING)
    pgestiona_cont = models.ForeignKey(User, models.DO_NOTHING, related_name='pgestiona', blank=True, null=True)
    observa_cont = models.CharField(max_length=2500, blank=True, null=True)
    fch_gestiona_cont = models.DateTimeField(null=True, blank=True)
    aprobado_cont = models.IntegerField(blank=True, null=True, choices=estado)
    anula = models.BooleanField(null=True, blank=True)
    valor = models.FloatField(blank=True, null=True)
    docs = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Anticipos')
    comprobante = models.FileField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Comprobante')
   
    class Meta:
        managed = True
        db_table = 'pedidos\".\"solicitudes_adqui' 
