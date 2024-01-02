from django.db import models

from apps.usuarios.models import Autorizador
from apps.usuarios.models import User

valor_estado = {
    ('AC','ACTIVO'),
    ('DB','DADO DE BAJA'),
    ('MN','MANTENIMIENTO'),
    ('RE', 'REPARACIÓN EXTERNA'),
    ('VE', 'VENDIDO'),
    ('DO', 'DONADO'),
    
}
valor_incendios = {
    ('SI','SI'),
    ('NO','NO'),
}

valor_grabado = {
    ('NO','NO'),
    ('ETIQUETA','ETIQUETA'),
    ('GRABADO','GRABADO'),
    ('NO ES POSIBLE IDENTIFICAR','NO ES POSIBLE IDENTIFICAR'),

}

valor_poliza = {
    ('1','ROTURA DE MAQUINARIA'),
    ('2','EQUIPO Y MAQUINARIA'),
    ('3','INCENDIO'),
    ('4','SIN SEGURO'),
    ('5','VEHICULOS'),
    ('6','EQUIPO ELECTRONICO'),
}


# Create your models here.
class desc_activo(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    activo_codigo = models.CharField(max_length=20,blank=True, null=True)
    activo_grupo = models.ForeignKey('activo_grupo', models.DO_NOTHING,blank=True,null=True)
    activo_tipo = models.ForeignKey('activo_tipo', models.DO_NOTHING,blank=True,null=True)
    activo_descripcion = models.CharField(max_length=500, blank=True, null=True)
    activo_depar = models.ForeignKey('activo_depar', models.DO_NOTHING,blank=True,null=True)
    activo_ubica = models.ForeignKey('activo_ubica', models.DO_NOTHING,blank=True,null=True)
    activo_area = models.ForeignKey('activo_areas', models.DO_NOTHING,null=True,blank=True)
    activo_subsec = models.ForeignKey('activo_subsector', models.DO_NOTHING,null=True,blank=True)
    pestanias_seguros = models.ForeignKey('pestanias_seguros', models.DO_NOTHING,null=True,blank=True)
    activo_valor = models.FloatField(blank=True, null=True, default=None)
    activo_valor_compra = models.FloatField(blank=True, null=True, default=None)
    orden_de_pedido = models.IntegerField(unique=True,blank=True, null=True)
    numero_factura = models.CharField(max_length=20,blank=True, null=True)
    secuencia_codigo = models.IntegerField(blank=True, null=True)
    activo_index = models.IntegerField(blank=True, null=True)
    cod_activo_padre = models.ForeignKey('cod_activo_padres', models.DO_NOTHING, blank=True, null=True)
    activo_fecha_modifica = models.DateTimeField(auto_now=True)
    activo_nomenclatura = models.ForeignKey('activo_nomenclatura', models.DO_NOTHING,blank=True, null=True)
    activo_estado = models.CharField(max_length=20, blank=True, null=True,choices=valor_estado, default='ACTIVO')
    grabado = models.CharField(max_length=50, blank=True, null=True,choices=valor_grabado, default='NO')
    poliza_seguros = models.CharField(max_length=20, blank=True, null=True,choices=valor_poliza)
    incendios = models.CharField(max_length=4, blank=True, null=True,choices=valor_incendios)
    toma_fisica = models.DateTimeField(blank=True,null=True)
    usuario_modifica = models.CharField(max_length=50, blank=True, null=True)
    justificacion_modifica = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"desc_activo'

        permissions = (
            ('acceso_activos', 'Acceso Provicional'),
            ('modificaciones_activos', 'Modificaciones Activos'),
            ('genera_código', 'Generación de Activos'),
            ('consulta_edita', 'Consulta y Edita Activos'),
            ('mis_activos', 'Consulta Activos en Custodio Propio'),
            ('descargo_activos','Descargo de Activos Seguridad'),
            ('custom_rep1', 'Consulta Reportes Activos Custom1'),
            
        )

        ordering = ['-activo_fecha_modifica']

    def __str__(self):
        return str(self.activo_codigo)
    
    @property
    def order_by(self):
        return self.activo_codigo.order_by('activo_codigo')
    
    @property
    def get_activo_valor(self):
        if self.activo_valor:
              return self.activo_valor
        else:
              return ""
    
    @property
    def get_activo_valor_compra(self):
        if self.activo_valor_compra:
              return self.activo_valor_compra
        else:
              return ""
    

usuario_modifica = {
    ('dmencias','David Mencías'),
    ('eclavijo','Eduardo Clavijo'),
    ('jcvillamarin','Juan Carlos Villamrín'),
    ('pborja','Pablo Borja'),
}

valor_bool = {
    ('SI','SI'),
    ('NO','NO'),
}

motivo_modifica = {
    ('cambio_caracteristicas','Cambio de Caracteristicas'),
    ('cambio_ubicacion','Cambio de Ubicación'),
    ('actualiza_asegurado','Cambio valor Asegurado'),
    ('cambio_custodio','Cambio de Custodio'),
    ('cambio_estado','Cambio de Estado'),
    ('cambio_fecha', 'Cambio de Fecha'),
    ('cambio_estado_identifica', 'Cambio de Estado Identificación Grabado/Etiquetado'),
}


class detalle_desc_activo(models.Model):
    desc_activo_codigo = models.ForeignKey('desc_activo', on_delete = models.CASCADE, related_name='detalle')
    desc_activo_codigo_mba = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_fecha_ingre = models.DateField(blank=True,null=True)
    desc_activo_custodio = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_num_serie = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_modelo = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_marca = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_num_motor = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_num_placa_vehiculo = models.CharField(max_length=10, blank=True, null=True)
    desc_activo_anio_fabrica = models.CharField(max_length=4, blank=True, null=True)
    desc_activo_usuario_registra = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_usuario_modifica = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_usuario_registra_cambio_custodio = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_observaciones_seg_cambio_custodio = models.CharField(max_length=5000, blank=True, null=True)
    desc_activo_fecha_modifica = models.DateField(blank=False,null=True)
    desc_activo_motivo_modifica = models.CharField(max_length=50, blank=True,null=True,choices=motivo_modifica)
    desc_activo_pc_procesador = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_pc_memoria = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_pc_disco = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_asegurado = models.CharField(max_length=2, blank=True, null=True,choices=valor_bool)
    desc_activo_cod_responsable = models.CharField(max_length=10, blank=True, null=True)
    desc_activo_proveedor = models.CharField(max_length=200, blank=True, null=True)
    fecha_baja_dona_vende =  models.DateField(blank=True,null=True)
    fecha_cambia_custodio =  models.DateField(blank=True,null=True)
    usuario_realiza_baja_dona_vende = models.CharField(max_length=50, blank=True, null=True)
    notas_baja_dona_vende = models.CharField(max_length=2000, blank=True, null=True)
    observaciones_reporte_no_custodio = models.CharField(max_length=2500, blank=True, null=True)
    fecha_envia_reporte_no_custodio = models.DateField(blank=True,null=True)
    motivo_no_se_puede_identificar = models.CharField(max_length=2500, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'activos\".\"detalle_desc_activo'

        permissions = (
            ('acceso_activos', 'Acceso Provicional'),
        )

        ordering = ['-desc_activo_codigo__activo_fecha_modifica']
    
    def __str__(self):
        return str(self.desc_activo_codigo)


class pestanias_seguros(models.Model):
    pestania_nombre = models.CharField(max_length=50, blank=False, null=True)
    pestania_estado = models.IntegerField(blank=True, null=False)

    class Meta:     
        managed = True
        db_table = 'activos\".\"pestanias_seguros'

        ordering = ['pestania_nombre']

    def __str__(self):
        return self.pestania_nombre

class poliza_seguros(models.Model):
    poliza_nombre = models.CharField(max_length=50, blank=False, null=True)
    poliza_estado = models.IntegerField(blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'activos\".\"poliza_seguros'

        ordering = ['poliza_nombre']

    def __str__(self):
        return self.poliza_nombre


class activo_grupo(models.Model):
    grupo_nombre = models.CharField(max_length=50, blank=False, null=True)
    grupo_estado = models.IntegerField(blank=True, null=False)
    autoriza_salida = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'activos\".\"activo_grupo'

        ordering = ['grupo_nombre']

    def __str__(self):
        return str(self.grupo_nombre)

class activo_ubica(models.Model):
    ubica_nombre = models.CharField(max_length=50, blank=False, null=True)
    ubica_estado = models.IntegerField(blank=True, null=False)

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_ubica'

        ordering = ['ubica_nombre']


    def __str__(self):
        return str(self.ubica_nombre)

class activo_areas(models.Model):
    area_codigo = models.AutoField(primary_key=True)
    area_nombre = models.CharField(max_length=50, blank=False, null=True)
    area_estado = models.IntegerField(blank=True, null=False)
    area_departamento = models.ForeignKey('activo_depar', models.DO_NOTHING)
    area_ubica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_areas'

        ordering = ['area_nombre']

    def __str__(self):
        return str(self.area_nombre)

class activo_subsector(models.Model):
    subsector_codigo = models.AutoField(primary_key=True)
    subsector_nombre = models.CharField(max_length=200, blank=True, null=True)
    subsector_estado = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'activos\".\"activo_subsector'

        ordering = ['subsector_nombre']

    def __str__(self):
        return str(self.subsector_nombre)


class activo_tipo(models.Model):
    tipo_nombre = models.CharField(max_length=50, blank=False, null=True)
    tipo_estado = models.IntegerField(blank=True, null=False)
    tipo_nomenclatura = models.CharField(max_length=5, blank=False, null=True)
    tipo_grupo = models.ForeignKey('activo_grupo', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_tipo'

        ordering = ['tipo_nombre']

    def __str__(self):
        return str(self.tipo_nombre)


class cod_activo_padres(models.Model):
    cod_activo_padre = models.CharField(max_length=5,primary_key=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"cod_activo_padres'

        ordering = ['cod_activo_padre']

    def __str__(self):
        return str(self.cod_activo_padre)

class activos_temp_excel(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    activo_codigo = models.CharField(max_length=20,blank=True, null=True)
    activo_grupo = models.CharField(max_length=100,blank=True, null=True)
    activo_tipo = models.CharField(max_length=100,blank=True, null=True)
    activo_descripcion = models.CharField(max_length=500, blank=True, null=True)
    activo_depar = models.CharField(max_length=100,blank=True, null=True)
    activo_ubica = models.CharField(max_length=100,blank=True, null=True)
    activo_area = models.CharField(max_length=100,blank=True, null=True)
    activo_valor = models.FloatField(blank=True, null=True)
    orden_de_pedido = models.IntegerField(unique=True,blank=True, null=True)
    numero_factura = models.IntegerField(unique=True,blank=True, null=True)
    secuencia_codigo = models.IntegerField(blank=True, null=True)
    activo_index = models.IntegerField(blank=True, null=True)
    cod_activo_padre = models.CharField(max_length=20,blank=True, null=True)
    desc_activo_codigo = models.IntegerField(unique=True,blank=True, null=True)
    desc_activo_codigo_mba = models.CharField(max_length=20,blank=True, null=True)
    desc_activo_fecha_ingre = models.DateField(blank=True,null=True)
    desc_activo_custodio = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_num_serie = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_modelo = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_marca = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_num_motor = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_num_placa_vehiculo = models.CharField(max_length=10, blank=True, null=True)
    desc_activo_anio_fabrica = models.CharField(max_length=4, blank=True, null=True)
    desc_activo_usuario_registra = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_usuario_modifica = models.CharField(max_length=50, blank=True, null=True)
    desc_activo_fecha_modifica = models.DateField(blank=True,null=True)
    desc_activo_motivo_modifica = models.CharField(max_length=50, blank=True,null=True)
    desc_activo_pc_procesador = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_pc_memoria = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_pc_disco = models.CharField(max_length=100, blank=True, null=True)
    desc_activo_asegurado = models.CharField(max_length=2, blank=True, null=True,choices=valor_bool)
    desc_activo_cod_responsable = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"activos_temp_excel'

class activo_nomenclatura(models.Model):
    nomenclatura_codigo = models.CharField(max_length=4, blank=True, null=True)
    nomenclatura_nombre = models.CharField(max_length=50, blank=True, null=True)
    nomenclatura_estado = models.CharField(max_length=2, blank=True, null=True,choices=valor_bool)
    nomenclatura_mix = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_nomenclatura'

        ordering = ['nomenclatura_codigo']

    def __str__(self):
        return str(self.nomenclatura_nombre)

class activo_estados_select(models.Model):
    codigo = models.CharField(max_length=100, blank=True, null=True)
    tipo = models.ForeignKey('activo_tipo', models.DO_NOTHING,blank=True, null=True)
    grupo = models.ForeignKey('activo_grupo', models.DO_NOTHING,blank=True, null=True)
    ubicacion = models.ForeignKey('activo_ubica', models.DO_NOTHING,blank=True, null=True)
    departamento = models.ForeignKey('activo_depar', models.DO_NOTHING,blank=True, null=True)
    area = models.ForeignKey('activo_areas', models.DO_NOTHING,blank=True, null=True)
    seguros = models.ForeignKey('pestanias_seguros', models.DO_NOTHING,blank=True, null=True)
    poliza =  models.CharField(max_length=100, blank=True, null=True)
    custodio = models.CharField(max_length=200, blank=True, null=True)
    pclave = models.CharField(max_length=1000, blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_estados_select'

motivos_salida = {
    (1,'Reparación'),
    # (2,'Dado de Baja'),
    # (3,'Venta'),
    (4,'Movimiento entre ubicaciones Propias')
    }

estado_salida = {
    (1,'En Reparación Externa'),
    (2,'Retornó'),
    }

autoriza_seguridad = {
    ('Galo Jaramillo','Galo Jaramillo'),
    ('Fernando Ortiz','Fernando Ortiz'),
    }

class salida_activos(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_movimiento = models.DateTimeField(auto_now=True)
    fecha_efectiva_retorno = models.DateTimeField(blank=True,null=True)
    activo_tipo = models.CharField(max_length=100,blank=True, null=True)
    activo_codigo = models.ForeignKey('desc_activo', models.DO_NOTHING,blank=True,null=True)
    activo_num_serie = models.CharField(max_length=100,blank=True, null=True)
    marca = models.CharField(max_length=100,blank=True, null=True)
    retorno = models.CharField(max_length=2, blank=True, null=True,choices=valor_bool)
    detalle_activo = models.CharField(max_length=500, blank=True, null=True)
    sale_por = models.IntegerField(blank=True, null=True,choices=motivos_salida)
    num_orden_trabajo = models.IntegerField(blank=True, null=True)
    solicitado_por = models.CharField(max_length=200, blank=True, null=True)
    id_solicita = models.ForeignKey(User, models.DO_NOTHING, null=True, blank=True)
    motivo = models.CharField(max_length=500, blank=True, null=True)
    empresa_mantenimiento = models.CharField(max_length=500, blank=True, null=True)
    fecha_estimada_retorno = models.DateField(blank=True,null=True)
    hora_salida = models.CharField(max_length=20, blank=True, null=True)
    pers_gestiona_bodega = models.IntegerField(blank=True, null=True)
    pers_autoriza_seguridad = models.CharField(max_length=200, blank=True, null=True)
    persona_retira = models.CharField(max_length=200, blank=True, null=True)
    guardia_control = models.IntegerField(blank=True, null=True)
    estado_autoriza_dep = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=100, blank=True, null=True,default='PENDIENTE')
    estado_bodega  = models.BooleanField(blank=True,null=True)
    codigo = models.CharField(max_length=100, blank=True, null=True)
    orden_mantenimiento = models.IntegerField(blank=True, null=True)
    departamento = models.IntegerField(blank=True, null=True)
    grupo = models.IntegerField(blank=True, null=True)
    observa_autoriza = models.CharField(max_length=2000, null=True, blank=True)
    observa_recibe = models.CharField(max_length=2000, null=True, blank=True)
    persona_autoriza_dep = models.CharField(max_length=200, blank=True, null=True)
    ubica_depar = models.IntegerField(blank=True, null=True)
    ubica_area = models.IntegerField(blank=True, null=True)
    ubica_ubica = models.IntegerField(blank=True, null=True)
    persona_registra_en_proyecto = models.CharField(max_length=200, blank=True, null=True)
    anula  = models.BooleanField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"salida_activos'

        permissions = (
            ('acceso_activos', 'Acceso Provicional'),
            ('movimiento_activos', 'Acceso Movimiento de Activos'),
            ('consulta_activos_en_taller', 'Consulta Activos en Taller'),
            ('autorizacion_salida_activos', 'Autorización de Salida de Activos'),
            ('control_salida_activos', 'Control de Seguridad Salida de Activos'),
            ('movimiento_bodega_activos', 'Acceso Movimiento de Activos en Bodega'),
            ('rehistro_salida_activos', 'Registro de Salida de Activos'),
        )

usuario_toma_fisica = {
    ('EDUARDO CLAVIJO','EDUARDO CLAVIJO'),
    ('PABLO BORJA','PABLO BORJA'),
    ('JUAN VILLAMARIN','JUAN VILLAMARIN'),
    ('DAVID  MENCIAS','DAVID MENCIAS'),
}



class historial_movimientos_internos(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_movimientos = models.DateTimeField(auto_now=True)
    activo_codigo = models.ForeignKey('desc_activo', models.DO_NOTHING,blank=True,null=True)
    ubicacion = models.ForeignKey('activo_ubica', models.DO_NOTHING,blank=True, null=True)
    departamento = models.ForeignKey('activo_depar', models.DO_NOTHING,blank=True, null=True)
    sector = models.ForeignKey('activo_areas', models.DO_NOTHING,blank=True, null=True)
    subsector = models.CharField(max_length=300, blank=True, null=True)
    usuario_registra = models.CharField(max_length=50, blank=True, null=True)
    usuario_retira = models.CharField(max_length=50, blank=True, null=True)
    justificacion_movimiento = models.CharField(max_length=500, blank=True, null=True)
    nuevo_ubicacion = models.ForeignKey('activo_ubica', models.DO_NOTHING,blank=True, null=True, related_name='ubica_nueva')
    nuevo_departamento = models.ForeignKey('activo_depar', models.DO_NOTHING,blank=True, null=True, related_name='depar_nueva')
    nuevo_sector = models.ForeignKey('activo_areas', models.DO_NOTHING,blank=True, null=True, related_name='area_nueva')
    # nuevo_ubicacion = models.CharField(max_length=300, blank=True, null=True)
    # nuevo_departamento = models.CharField(max_length=300, blank=True, null=True)
    # nuevo_sector = models.CharField(max_length=300, blank=True, null=True)
    nuevo_subsector = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"historial_movimientos_internos'


class toma_fisica(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    codigo = models.CharField(max_length=20,blank=True, null=True)
    numero_toma = models.CharField(max_length=20,blank=True, null=True)
    fecha = models.DateTimeField(blank=True,null=True)
    fecha_txt = models.CharField(max_length=8,blank=True, null=True)
    usuario = models.CharField(max_length=50, blank=True, null=True,choices=usuario_toma_fisica, default='EDUARDO CLAVIJO')

    class Meta:
        managed = True
        db_table = 'activos\".\"toma_fisica'

        permissions = (
            ('acceso_activos', 'Acceso Provicional'),
        )

class no_encontrados(models.Model):
    codigo = models.ForeignKey('desc_activo', on_delete = models.DO_NOTHING, blank=True, null=True)
    descripcion = models.CharField(max_length=2000,blank=True,null=True)
    grabado = models.BooleanField(blank=True,null=True)
    usuario_registra = models.CharField(max_length=100,blank=True,null=True)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"no_encontrados'



def upload_gallery_image(instance, filename):
    return f"img_activos/{instance.activo_codigo}/gallery/{filename}"


class Imagenes(models.Model):
    imagen_activo = models.ImageField(upload_to=upload_gallery_image, blank=True)
    activo_codigo = models.ForeignKey('desc_activo', on_delete=models.CASCADE, related_name="img_activos")

    class Meta:
        managed = True
        db_table = 'activos\".\"imagenes'