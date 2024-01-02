from django.db import models

from apps.activos.models import activo_depar, activo_areas, activo_tipo
from apps.usuarios.models import User
from apps.proveedores.models import proveedor

# Create your models here.

tiempos={
    ('hora','Horas'),
    ('dia','Dias'),
    ('semana','Semanas'),
    ('mes','Meses'),
    ('anio','Años'),
}

medidas={
    ('unidad','U'),
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
    (0,'No Aprobado')
}

motivos={
    ('nuevo','Nuevo'),
    ('reemplazo_m','Reemplazo por Mejora'),
    ('reemplazo_o','Reemplazo por Obsolescencia'),
}

reemplazos={
    (1,'Dada de Baja'),
    (2,'Reubicación'),
    (3,'Backup'),
    (4,'Reparación'),
}

class OrdenesPedidosMulti(models.Model):
    numpedido = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.ForeignKey(activo_areas, models.DO_NOTHING)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING)
    usuario_aprueba = models.CharField(max_length=100, blank=True, null=True)
    aprobado = models.IntegerField(blank=True, null=True, choices=estado)
    fchsolicita = models.DateField(auto_now_add=True)
    fchsolicitatxt = models.CharField(max_length=8, blank=True, null=True)
    numproyecto = models.CharField(max_length=70, blank=True, null=True)
    regimenespecial = models.BooleanField(blank=True, null=True, default=False)
    fchaprueba = models.DateField(auto_now=True, blank=True, null=True)
    fchapruebatxt = models.CharField(max_length=8, blank=True, null=True)
    motRechaza = models.CharField(max_length=250, blank=True, null=True)
    estado_cotiza = models.BooleanField(null=True, blank=True)
    cotiza_observa = models.CharField(max_length=250, blank=True, null=True)
    genera_compra = models.IntegerField(blank=True, null=True)
    observa_compra = models.CharField(max_length=250, blank=True, null=True)
    motivo_compra = models.CharField(max_length=50, blank=True, null=True, choices=motivos)
    justificacion_compra = models.CharField(max_length=250, blank=True, null=True)
    reemplazo_accion = models.IntegerField(choices=reemplazos, blank=True, null=True)
    reemplazo_observa = models.CharField(max_length=250, blank=True, null=True)
    entregado_bodega =  models.BooleanField(blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    entrega_observa = models.CharField(max_length=250, blank=True, null=True)
    cotiza_ref = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización Referencial')
    
    class Meta:
        managed = True
        db_table = 'pedidos\".\"ordenespedidosmulti'

        verbose_name = 'Orden Pedido Multiple'
        verbose_name_plural = 'Ordenes Pedidos Multiples'
        permissions = (
            ('menu_pedidos_multi', 'Acceso al Menu de Pedidos'),
            ('aprueba_pedidos_multi', 'Aprueba Pedidos Multiples'),
            ('genera_pedidos_multi', 'Generar Pedidos Multiples'),
        )
        ordering = ['-numpedido']

class DetallePedidoMulti(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidosMulti', on_delete=models.CASCADE)
    tipoactivo = models.ForeignKey(activo_tipo, models.DO_NOTHING)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    cantidad = models.FloatField(blank=True, null=True)
    unimedida = models.CharField(max_length=15, blank=True, null=True, choices=medidas, default='unidad')
    tiempo_vida = models.IntegerField(blank=True, null=True)
    tiempo_tipo = models.CharField(max_length=7, choices=tiempos)
    proveedor = models.CharField(max_length=150, blank=True, null=True)
    activado_activo = models.BooleanField(blank=True, null=True)
    fchactivacion = models.DateField(blank=True, null=True)
    fchactivaciontxt = models.CharField(max_length=8, blank=True, null=True)
    recibido_bodega = models.BooleanField(blank=True, null=True)
    fchrecepcion = models.DateField(blank=True, null=True)
    fchrecepciontxt = models.CharField(max_length=8, blank=True, null=True)
    codigo_genera = models.BooleanField(blank=True, null=True)
    img_1 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 2')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"detallepedidomulti'

        verbose_name = 'Detalle Pedido Multiple'
        verbose_name_plural = 'Detalles Pedidos Multiples'
        permissions = (
            ('menu_bodega_multi', 'Acceso al Menu de Bodega'),
            ('activa_pedidos_multi', 'Activación de Pedidos'),
            ('recibe_bodega_multi', 'Recepción de Producto Bodega'),
            ('genera_bodega_multi', 'Genera Codigo Activo'),
            ('entrega_bodega_multi', 'Entrega de Pedidos'),
        )

class CotizaPedidoMulti(models.Model):
    numpedido = models.ForeignKey('OrdenesPedidosMulti', null=True, blank=True, on_delete=models.CASCADE)
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor')
    empresa_cotiza = models.ForeignKey(proveedor, models.DO_NOTHING, null=True, blank=True, verbose_name='Proveedor')
    pdf_cotiza = models.FileField(upload_to='cotizaciones/', blank=True, null=True, verbose_name='Cotización')
    cotiza_seleccion = models.BooleanField(null=True, blank=True, verbose_name='Selección')

    class Meta:
        managed = True
        db_table = 'pedidos\".\"cotizapedidomulti'

        verbose_name = 'Cotización Multiple'
        verbose_name_plural = 'Cotizaciones Multiples'
        permissions = (
            ('menu_cotiza_multi', 'Acceso al Menu de Cotizaciones'),
            ('selecciona_cotizapedido_multi', 'Seleccionar Cotizaciones Multiples'),
        )