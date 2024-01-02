from django.db import models
from apps.activos.models import activo_depar, activo_areas, activo_ubica
from apps.usuarios.models import User
from apps.proveedores.models import proveedor

# Create your models here.

class EventosRaytec(models.Model):
    counter = models.IntegerField(blank=True, null=True)
    defect_key = models.CharField(max_length=300, null=True, blank=True)
    pixels = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    way = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    fecha_txt = models.CharField(max_length=50, null=True, blank=True)
    receta = models.CharField(max_length=200, null=True, blank=True)
    linea = models.CharField(max_length=5, null=True, blank=True)
    origen = models.CharField(max_length=40, null=True, blank=True)
    proceso = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    usuini = models.CharField(max_length=60, null=True, blank=True)
    usufin = models.CharField(max_length=60, null=True, blank=True)
    defecto = models.CharField(max_length=200, null=True, blank=True)
    fecha_evento = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_raytec'

        permissions = (
    
            ('reportes_planta', 'Reportes Planta'),
            ('reporte_parecetico_l3', 'Reporte Dosificación APA L3'),
            ('reporte_raytec', 'Reporte Diario de Eventos Raytec'),

        )
valor_ubicacion = {
    ('CUBA','CUBA'),
    ('HIDROCOOLER','HIDROCOOLER'),
}

valor_parametro = {
    ('1','CORRECTO'),
    ('2','OBSERVACION'),
}

tipo_medicion = {
    ('APA','APA'),
    ('PH','PH'),
}

tipo_medicion_l2 = {
    ('CI','CI'),
    ('PH','PH'),
}


class EventosPareceticoL3(models.Model):
    index = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=200, null=True, blank=True,choices=tipo_medicion)
    valor = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200, null=True, blank=True,choices=valor_ubicacion)
    linea = models.CharField(max_length=5, null=True, blank=True)
    proceso = models.IntegerField(blank=True, null=True)
    parametro = models.CharField(max_length=20, null=True, blank=True,choices=valor_parametro)
    usuini = models.CharField(max_length=60, null=True, blank=True)
    usufin = models.CharField(max_length=60, null=True, blank=True)
    aiEstado = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_parecetico_l3'

        permissions = (
    
            ('reporte_parecetico', 'Reporte de Mediciones Parecetico'),

        )

class EventosCloroL2(models.Model):
    index = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=200, null=True, blank=True,choices=tipo_medicion_l2)
    valor = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200, null=True, blank=True,choices=valor_ubicacion)
    linea = models.CharField(max_length=5, null=True, blank=True)
    proceso = models.IntegerField(blank=True, null=True)
    parametro = models.CharField(max_length=20, null=True, blank=True,choices=valor_parametro)
    usuini = models.CharField(max_length=60, null=True, blank=True)
    usufin = models.CharField(max_length=60, null=True, blank=True)
    aiEstado = models.CharField(max_length=60, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_cloro_l2'

        permissions = (
    
            ('reporte_parecetico', 'Reporte de Mediciones Parecetico'),

        )


class EventosIshidaR2(models.Model):
    num_remepaque = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    num_reempacadora = models.CharField(max_length=5, null=True, blank=True)
    receta = models.CharField(max_length=500, null=True, blank=True)
    peso = models.FloatField(blank=True, null=True)
    peso_objetivo = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    usu = models.CharField(max_length=60, null=True, blank=True)
    motivo_para = models.CharField(max_length=500, null=True, blank=True)
    speed = models.FloatField(blank=True, null=True)
    speedw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_ishida_r2'

        permissions = (
    
            ('reporte_ishida_r2', 'Reporte de Pesos Rempacadora Ishida R2'),

        )

class EventosIshidaR3(models.Model):
    num_remepaque = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    num_reempacadora = models.CharField(max_length=5, null=True, blank=True)
    receta = models.CharField(max_length=500, null=True, blank=True)
    peso = models.FloatField(blank=True, null=True)
    peso_objetivo = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    usu = models.CharField(max_length=60, null=True, blank=True)
    motivo_para = models.CharField(max_length=500, null=True, blank=True)
    speed = models.FloatField(blank=True, null=True)
    speedw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_ishida_r3'

        permissions = (
    
            ('reporte_ishida_r3', 'Reporte de Pesos Rempacadora Ishida R3'),

        )

class EventosIshidaR1(models.Model):
    num_remepaque = models.IntegerField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    num_reempacadora = models.CharField(max_length=5, null=True, blank=True)
    receta = models.CharField(max_length=500, null=True, blank=True)
    peso = models.FloatField(blank=True, null=True)
    peso_objetivo = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    usu = models.CharField(max_length=60, null=True, blank=True)
    motivo_para = models.CharField(max_length=500, null=True, blank=True)
    speed = models.FloatField(blank=True, null=True)
    speedw = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'public\".\"eventos_ishida_r1'

        permissions = (
    
            ('reporte_ishida_r1', 'Reporte de Pesos Rempacadora Ishida R1'),

        )


tipo_solicitud={
    (1,'Transporte personas'),
    (2,'Encomienda'),
    (3,'Vale Combustible'),
}

estado={
    (1,'Pendiente'),
    (2,'Aprobado'),
    (3,'Rechazada'),
    (4,'Anulada'),
    (5,'Booked'),

}

estado2={
    (1,'Pendiente'),
    (2,'En proceso'),
    (3,'Devuelta'),
    (4,'Confirmado')
}

tipo_s={
    (1,'Booking Ruta Programada'),
    (2,'Nueva Solicitud Transporte'),
    (3,'Encomienda'),
    (4,'Vale de Combustible')
}



class RutaTransporte(models.Model):
    codigo_ruta = models.CharField(max_length=50, blank=True, null=True, unique=True)
    origen = models.CharField(max_length=500, blank=True, null=True)
    destino = models.CharField(max_length=500, blank=True, null=True)
    tarifa = models.FloatField(blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    fecha_modifica = models.DateField(blank=True,null=True)
    persona_edita = models.CharField(max_length=50, blank=True, null=True)
    comentarios = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return str(self.codigo_ruta)

    class Meta:
        managed = True
        db_table = 'procesos\".\"ruta_transporte'
    
        permissions = (
                ('edicion_rutas_transporte', 'Edicion Rutas Transporte'),
            )

class Eventos(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    desc_evento = models.CharField(max_length=10000,null=True,blank=True)
    color = models.CharField(max_length=255,null=True,blank=True)
    allday = models.BooleanField(default=False,blank=True,null=True)
    ruta = models.ForeignKey(RutaTransporte, models.DO_NOTHING, blank=True, null=False, default=34, related_name='laruta_ev')
    transportista = models.CharField(max_length=10000,null=True,blank=True)
    conteo_disponible = models.IntegerField(blank=True, null=True)
    docs = models.FileField(upload_to='transporte/', blank=True, null=True, verbose_name='Documentos Transpote')
    tarifa_evento = models.FloatField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'procesos\".\"eventos_transporte'

        permissions = (
    
            ('calendario_transporte', 'Administracion Transporte'),
            ('solicitudes_transporte', 'Solicitud Transporte'),
            ('autorizaciones_transporte', 'Autorizacion Transporte'),
            ('vales_combustible', 'Admini Vales Combustible'),
            ('reporte_transporte', 'Acceso a Reporte de Transporte'),

        )

#SI SE AUMENTAN CAMPOS EN ESTE MODELO, INCLUIRLOS TAMBIEN EN LA TABLA BookingReporte
class SolicitudTransporte(models.Model):   
    numpedido = models.AutoField(primary_key=True)
    tipo = models.IntegerField(blank=True, null=True, choices=tipo_solicitud)
    ubica = models.ForeignKey(activo_ubica, models.DO_NOTHING)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.CharField(max_length=301, blank=True, null=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    usuario_aprueba1n = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='aprobador')
    estado1n = models.IntegerField(blank=True, null=True, choices=estado)
    fchsolicita = models.DateTimeField(blank=True, null=True)
    fchaprueba1n = models.DateTimeField(blank=True, null=True)
    fecha_en_proceso = models.DateTimeField(blank=True, null=True)
    fecha_confirma = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=10000, blank=True, null=True)
    justificacion = models.CharField(max_length=10000, blank=True, null=True)
    estado2n = models.IntegerField(blank=True, null=True, choices=estado2)
    confirmacion = models.BooleanField(blank=True, null=True)
    observaciones_rechazo1n = models.CharField(max_length=10000, blank=True, null=True)
    observaciones_rechazo2n = models.CharField(max_length=10000, blank=True, null=True)
    anula = models.BooleanField(blank=True, null=True)
    num_requisicion = models.IntegerField(blank=True, null=True)
    ruta = models.ForeignKey(RutaTransporte, models.DO_NOTHING, blank=True, null=True, related_name='laruta')
    otra_ruta = models.CharField(max_length=2000, blank=True, null=True)
    pasajero = models.CharField(max_length=500, blank=True, null=True)
    fchevento = models.DateTimeField(blank=True, null=True)
    otros_pasajeros = models.CharField(max_length=500, blank=True, null=True)
    notas_del_gestor = models.CharField(max_length=10000, blank=True, null=True)
    notas_de_confirmacion = models.CharField(max_length=10000, blank=True, null=True)
    retorno = models.BooleanField(blank=True, null=True)
    usu_gestiona_vale = models.CharField(max_length=200, blank=True, null=True)
    fecha_gestiona_vale = models.DateTimeField(blank=True, null=True)
    observaciones_vale = models.CharField(max_length=10000, blank=True, null=True)
    num_vale = models.IntegerField(blank=True, null=True)
    valor_vale = models.FloatField(blank=True, null=True)
    estado_vale = models.IntegerField(blank=True, null=True)
    beneficiario_vale = models.CharField(max_length=500, blank=True, null=True)
    evento_de_calendario = models.BooleanField(blank=True, null=True)
    evento = models.ForeignKey('Eventos',models.DO_NOTHING,default=None,blank=True,null=True)
    transportista = models.CharField(max_length=10000,null=True,blank=True)
    tarifa_real = models.FloatField(blank=True,null=True)
    num_factura = models.IntegerField(blank=True, null=True)
    fecha_factura = models.DateField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'procesos\".\"solicitud_transporte'


class BookingReporte(models.Model):
    numpedido = models.AutoField(primary_key=True)
    tipo = models.IntegerField(blank=True, null=True, choices=tipo_solicitud)
    ubica = models.ForeignKey(activo_ubica, models.DO_NOTHING)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.CharField(max_length=301, blank=True, null=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    usuario_aprueba1n = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='aprobadorbr')
    estado1n = models.IntegerField(blank=True, null=True, choices=estado)
    fchsolicita = models.DateTimeField(blank=True, null=True)
    fchaprueba1n = models.DateTimeField(blank=True, null=True)
    fecha_en_proceso = models.DateTimeField(blank=True, null=True)
    fecha_confirma = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=10000, blank=True, null=True)
    justificacion = models.CharField(max_length=10000, blank=True, null=True)
    estado2n = models.IntegerField(blank=True, null=True, choices=estado2)
    confirmacion = models.BooleanField(blank=True, null=True)
    observaciones_rechazo1n = models.CharField(max_length=10000, blank=True, null=True)
    observaciones_rechazo2n = models.CharField(max_length=10000, blank=True, null=True)
    anula = models.BooleanField(blank=True, null=True)
    num_requisicion = models.IntegerField(blank=True, null=True)
    ruta = models.ForeignKey(RutaTransporte, models.DO_NOTHING, blank=True, null=True, related_name='larutabr')
    otra_ruta = models.CharField(max_length=2000, blank=True, null=True)
    pasajero = models.CharField(max_length=500, blank=True, null=True)
    fchevento = models.DateTimeField(blank=True, null=True)
    otros_pasajeros = models.CharField(max_length=500, blank=True, null=True)
    notas_del_gestor = models.CharField(max_length=10000, blank=True, null=True)
    notas_de_confirmacion = models.CharField(max_length=10000, blank=True, null=True)
    retorno = models.BooleanField(blank=True, null=True)
    usu_gestiona_vale = models.CharField(max_length=200, blank=True, null=True)
    fecha_gestiona_vale = models.DateTimeField(blank=True, null=True)
    observaciones_vale = models.CharField(max_length=10000, blank=True, null=True)
    num_vale = models.IntegerField(blank=True, null=True)
    valor_vale = models.FloatField(blank=True, null=True)
    estado_vale = models.IntegerField(blank=True, null=True)
    beneficiario_vale = models.CharField(max_length=500, blank=True, null=True)
    evento_de_calendario = models.BooleanField(blank=True, null=True)
    evento = models.ForeignKey('Eventos',models.DO_NOTHING,default=None,blank=True,null=True)
    transportista = models.CharField(max_length=10000,null=True,blank=True)
    tarifa_real = models.FloatField(blank=True,null=True)
    num_factura = models.IntegerField(blank=True, null=True)
    fecha_factura = models.DateField(blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'procesos\".\"booking_reporte'

        

class DetSolicitudTransporte(models.Model):
    numpedido = models.ForeignKey('SolicitudTransporte', related_name = 'carrera', on_delete=models.CASCADE)
    img_1 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 2')
    
    class Meta:
        managed = True
        db_table = 'procesos\".\"det_solicitud_transporte'

class Booking(models.Model):
    evento = models.ForeignKey('Eventos', related_name = 'book', on_delete=models.CASCADE)
    departamento = models.CharField(max_length=500, blank=True, null=True)
    nombre_pasajero = models.CharField(max_length=10000, blank=True, null=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    usuario_aprueba1n = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='apruebaasist')
    estado1n = models.IntegerField(blank=True, null=True, choices=estado)
    fchsolicita = models.DateTimeField(blank=True, null=True)
    fchaprueba1n = models.DateTimeField(blank=True, null=True)
    justificacion = models.CharField(max_length=10000, blank=True, null=True)
    observaciones_rechazo1n = models.CharField(max_length=10000, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, choices=tipo_s)
    
    class Meta:
        managed = True
        db_table = 'procesos\".\"booking'


class RecGPT(models.Model):
    pc = models.CharField(max_length=100000, blank=True, null=True)
    pr = models.CharField(max_length=100000, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'procesos\".\"rec_gpt'
    

valmed={
    ('ml','Mililitros'),
    ('gr','Gramos'),
    ('Kg','Kilogramos'),
    ('LT','Litros'),
    ('GAL','Galones'),
}

bode={
    ('AC','Agua Clara'),
    ('LM','La Merced'),
}

proye={
    ('AC','Agua Clara'),
    ('LM','La Merced'),
    ('AV','La Avelina'),
    ('ML','Los Molles'),
    ('KO','Kosher'),
}

uni={
    ('gr','Gramos'),
    ('Kg','Kilogramos'),
    ('LT','Litros'),
    ('ml','Mililitros'),
    ('GAL','Galón'),
}



class InventarioSemanal(models.Model):
    producto = models.CharField(primary_key=True, max_length=500)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    unimed = models.CharField(max_length=3,blank=False, null=False,choices=valmed)
   
    class Meta:
        managed = True
        db_table = 'procesos\".\"inventario_semanal_agri'

class InventarioConsolidado(models.Model):
    producto = models.CharField(blank=True, null=True, max_length=500)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    unimed = models.CharField(max_length=3,blank=False, null=False,choices=valmed)
    anio = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    semana = models.IntegerField(blank=True, null=True)
    proyecto = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'procesos\".\"inventario_consolidado_agri'

class Egresos(models.Model):
    bodega = models.CharField(max_length=3,blank=False, null=False,choices=bode)
    proyecto = models.CharField(max_length=3,blank=False, null=False,choices=proye) 
    producto = models.ForeignKey(InventarioConsolidado, models.DO_NOTHING, blank=True, null=True, related_name='egreso')
    fecha = models.DateTimeField(blank=True, null=True)
    lote = models.CharField(max_length=300,blank=True, null=True)
    unimed =  models.CharField(max_length=3,blank=True, null=True, choices=uni) 
    cantidad = models.FloatField(blank=True, null=True)
    registra = models.CharField(max_length=20,blank=True, null=True)
    fecha_registra = models.DateTimeField(blank=True, null=True)
    usuario_registra = models.CharField(max_length=20,blank=True, null=True)
    observaciones = models.CharField(max_length=2000,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'procesos\".\"egresos_agri'
      
class Califica(models.Model):
    cali_id = models.AutoField(db_column='CALI_ID', primary_key=True)  # Field name made lowercase.
    cali_nom = models.CharField(db_column='CALI_NOM', unique=True, max_length=100)  # Field name made lowercase.
    cali_des = models.CharField(db_column='CALI_DES', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALIFICA'
        unique_together = (('cali_id', 'cali_nom'),)
        app_label = 'ONLYCONTROL'

class Area(models.Model):
    area_id = models.AutoField(db_column='AREA_ID', primary_key=True)  # Field name made lowercase.
    area_nom = models.CharField(db_column='AREA_NOM', unique=True, max_length=100)  # Field name made lowercase.
    area_des = models.CharField(db_column='AREA_DES', max_length=40, blank=True, null=True)  # Field name made lowercase.
    area_obs = models.CharField(db_column='AREA_OBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_em = models.CharField(db_column='AREA_EM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    area_sel = models.CharField(db_column='AREA_SEL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREA'
        unique_together = (('area_id', 'area_nom'),)
        app_label = 'ONLYCONTROL'

class Dpto(models.Model):
    dep_id = models.AutoField(db_column='DEP_ID', primary_key=True)  # Field name made lowercase.
    dep_are = models.DecimalField(db_column='DEP_ARE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dep_nom = models.CharField(db_column='DEP_NOM', max_length=100)  # Field name made lowercase.
    dep_desc = models.CharField(db_column='DEP_DESC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dep_obs = models.CharField(db_column='DEP_OBS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dep_em = models.CharField(db_column='DEP_EM', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DPTO'
        unique_together = (('dep_id', 'dep_nom'),)
        app_label = 'ONLYCONTROL'
        
class Nomina(models.Model):
    nomina_id = models.CharField(db_column='NOMINA_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    nomina_ape = models.CharField(db_column='NOMINA_APE', max_length=100)  # Field name made lowercase.
    nomina_nom = models.CharField(db_column='NOMINA_NOM', max_length=50)  # Field name made lowercase.
    nomina_clave = models.CharField(db_column='NOMINA_CLAVE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    nomina_cod = models.CharField(db_column='NOMINA_COD', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nomina_tipo = models.CharField(db_column='NOMINA_TIPO', max_length=30)  # Field name made lowercase.
    nomina_cal = models.ForeignKey(Califica, models.DO_NOTHING, db_column='NOMINA_CAL', related_name='califica1')  # Field name made lowercase.
    nomina_area = models.ForeignKey(Area, models.DO_NOTHING, db_column='NOMINA_AREA', related_name='area1')  # Field name made lowercase.
    nomina_dep = models.ForeignKey(Dpto, models.DO_NOTHING, db_column='NOMINA_DEP', related_name='dep1')  # Field name made lowercase.
    nomina_cal1 = models.ForeignKey(Califica, models.DO_NOTHING, db_column='NOMINA_CAL1', blank=True, null=True, related_name='califica2')  # Field name made lowercase.
    nomina_area1 = models.ForeignKey(Area, models.DO_NOTHING, db_column='NOMINA_AREA1', blank=True, null=True, related_name='area2')  # Field name made lowercase.
    nomina_dep1 = models.ForeignKey(Dpto, models.DO_NOTHING, db_column='NOMINA_DEP1', blank=True, null=True, related_name='dep2')  # Field name made lowercase.
    nomina_fing = models.DateTimeField(db_column='NOMINA_FING', blank=True, null=True)  # Field name made lowercase.
    nomina_fsal = models.DateTimeField(db_column='NOMINA_FSAL', blank=True, null=True)  # Field name made lowercase.
    nomina_suel = models.DecimalField(db_column='NOMINA_SUEL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomina_com = models.DecimalField(db_column='NOMINA_COM', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    nomina_auti = models.IntegerField(db_column='NOMINA_AUTI', blank=True, null=True)  # Field name made lowercase.
    nomina_es = models.IntegerField(db_column='NOMINA_ES', blank=True, null=True)  # Field name made lowercase.
    nomina_obs = models.CharField(db_column='NOMINA_OBS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_emp = models.DecimalField(db_column='NOMINA_EMP', max_digits=10, decimal_places=0)  # Field name made lowercase.
    nomina_finger = models.CharField(db_column='NOMINA_FINGER', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nomina_f1 = models.BinaryField(db_column='NOMINA_F1', blank=True, null=True)  # Field name made lowercase.
    nomina_ced = models.BinaryField(db_column='NOMINA_CED', blank=True, null=True)  # Field name made lowercase.
    nomina_fir = models.BinaryField(db_column='NOMINA_FIR', blank=True, null=True)  # Field name made lowercase.
    nomina_hd1 = models.CharField(db_column='NOMINA_HD1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_hf1 = models.BinaryField(db_column='NOMINA_HF1', blank=True, null=True)  # Field name made lowercase.
    nomina_hi1 = models.BinaryField(db_column='NOMINA_HI1', blank=True, null=True)  # Field name made lowercase.
    nomina_hd2 = models.CharField(db_column='NOMINA_HD2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_hf2 = models.BinaryField(db_column='NOMINA_HF2', blank=True, null=True)  # Field name made lowercase.
    nomina_hi2 = models.BinaryField(db_column='NOMINA_HI2', blank=True, null=True)  # Field name made lowercase.
    nomina_sel = models.IntegerField(db_column='NOMINA_SEL', blank=True, null=True)  # Field name made lowercase.
    nomina_empc = models.CharField(db_column='NOMINA_EMPC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nomina_empe = models.CharField(db_column='NOMINA_EMPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nomina_p1 = models.BooleanField(db_column='NOMINA_P1', blank=True, null=True)  # Field name made lowercase.
    nomina_p2 = models.BooleanField(db_column='NOMINA_P2', blank=True, null=True)  # Field name made lowercase.
    nomina_p3 = models.BooleanField(db_column='NOMINA_P3', blank=True, null=True)  # Field name made lowercase.
    nomina_p4 = models.BooleanField(db_column='NOMINA_P4', blank=True, null=True)  # Field name made lowercase.
    nomina_p5 = models.BooleanField(db_column='NOMINA_P5', blank=True, null=True)  # Field name made lowercase.
    nomina_p6 = models.BooleanField(db_column='NOMINA_P6', blank=True, null=True)  # Field name made lowercase.
    nomina_p7 = models.BooleanField(db_column='NOMINA_P7', blank=True, null=True)  # Field name made lowercase.
    nomina_p8 = models.BooleanField(db_column='NOMINA_P8', blank=True, null=True)  # Field name made lowercase.
    nomina_p9 = models.BooleanField(db_column='NOMINA_P9', blank=True, null=True)  # Field name made lowercase.
    nomina_p10 = models.BooleanField(db_column='NOMINA_P10', blank=True, null=True)  # Field name made lowercase.
    nomina_p11 = models.BooleanField(db_column='NOMINA_P11', blank=True, null=True)  # Field name made lowercase.
    nomina_p12 = models.BooleanField(db_column='NOMINA_P12', blank=True, null=True)  # Field name made lowercase.
    nomina_p13 = models.BooleanField(db_column='NOMINA_P13', blank=True, null=True)  # Field name made lowercase.
    nomina_p14 = models.BooleanField(db_column='NOMINA_P14', blank=True, null=True)  # Field name made lowercase.
    nomina_p15 = models.BooleanField(db_column='NOMINA_P15', blank=True, null=True)  # Field name made lowercase.
    nomina_p16 = models.BooleanField(db_column='NOMINA_P16', blank=True, null=True)  # Field name made lowercase.
    nomina_p17 = models.BooleanField(db_column='NOMINA_P17', blank=True, null=True)  # Field name made lowercase.
    nomina_p18 = models.BooleanField(db_column='NOMINA_P18', blank=True, null=True)  # Field name made lowercase.
    nomina_p19 = models.BooleanField(db_column='NOMINA_P19', blank=True, null=True)  # Field name made lowercase.
    nomina_p20 = models.BooleanField(db_column='NOMINA_P20', blank=True, null=True)  # Field name made lowercase.
    nomina_doc = models.BinaryField(db_column='NOMINA_DOC', blank=True, null=True)  # Field name made lowercase.
    nomina_pla = models.BinaryField(db_column='NOMINA_PLA', blank=True, null=True)  # Field name made lowercase.
    nomina_f = models.IntegerField(db_column='NOMINA_F', blank=True, null=True)  # Field name made lowercase.
    nomina_card = models.CharField(db_column='NOMINA_CARD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_fcard = models.DateTimeField(db_column='NOMINA_FCARD', blank=True, null=True)  # Field name made lowercase.
    nomina_obs1 = models.CharField(db_column='NOMINA_OBS1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomina_now = models.DateTimeField(db_column='NOMINA_NOW', blank=True, null=True)  # Field name made lowercase.
    nomina_cafe = models.BooleanField(db_column='NOMINA_CAFE', blank=True, null=True)  # Field name made lowercase.
    nomina_auto = models.CharField(db_column='NOMINA_AUTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomina_p21 = models.BooleanField(db_column='NOMINA_P21', blank=True, null=True)  # Field name made lowercase.
    nomina_p22 = models.BooleanField(db_column='NOMINA_P22', blank=True, null=True)  # Field name made lowercase.
    nomina_p23 = models.BooleanField(db_column='NOMINA_P23', blank=True, null=True)  # Field name made lowercase.
    nomina_p24 = models.BooleanField(db_column='NOMINA_P24', blank=True, null=True)  # Field name made lowercase.
    nomina_p25 = models.BooleanField(db_column='NOMINA_P25', blank=True, null=True)  # Field name made lowercase.
    nomina_controlapb = models.BooleanField(db_column='NOMINA_CONTROLAPB', blank=True, null=True)  # Field name made lowercase.
    nomina_statusapb = models.IntegerField(db_column='NOMINA_STATUSAPB', blank=True, null=True)  # Field name made lowercase.
    nomina_cafemenu = models.BooleanField(db_column='NOMINA_CAFEMENU', blank=True, null=True)  # Field name made lowercase.
    nomina_level = models.IntegerField(db_column='NOMINA_LEVEL', blank=True, null=True)  # Field name made lowercase.
    nomina_tipoid = models.CharField(db_column='NOMINA_TIPOID', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nomina_tiponom = models.CharField(db_column='NOMINA_TIPONOM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    nomina_hs1 = models.CharField(db_column='NOMINA_HS1', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    nomina_hs2 = models.CharField(db_column='NOMINA_HS2', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    nomina_cafecontrol = models.DecimalField(db_column='NOMINA_CAFECONTROL', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    nomina_serv1 = models.FloatField(db_column='NOMINA_SERV1')  # Field name made lowercase.
    nomina_serv2 = models.FloatField(db_column='NOMINA_SERV2')  # Field name made lowercase.
    nomina_serv3 = models.FloatField(db_column='NOMINA_SERV3')  # Field name made lowercase.
    nomina_serv4 = models.FloatField(db_column='NOMINA_SERV4')  # Field name made lowercase.
    nomina_serv5 = models.FloatField(db_column='NOMINA_SERV5')  # Field name made lowercase.
    nomina_serv6 = models.FloatField(db_column='NOMINA_SERV6')  # Field name made lowercase.
    nomina_serv7 = models.FloatField(db_column='NOMINA_SERV7')  # Field name made lowercase.
    nomina_serv8 = models.FloatField(db_column='NOMINA_SERV8')  # Field name made lowercase.
    nomina_serv9 = models.FloatField(db_column='NOMINA_SERV9')  # Field name made lowercase.
    nomina_cardkey = models.CharField(db_column='NOMINA_CARDKEY', max_length=6)  # Field name made lowercase.
    nomina_tipo_registro = models.IntegerField(db_column='NOMINA_TIPO_REGISTRO')  # Field name made lowercase.
    nomina_hwsq1 = models.BinaryField(db_column='NOMINA_HWSQ1', blank=True, null=True)  # Field name made lowercase.
    nomina_hwsq2 = models.BinaryField(db_column='NOMINA_HWSQ2', blank=True, null=True)  # Field name made lowercase.
    nomina_face = models.CharField(db_column='NOMINA_FACE', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    nomina_face_len = models.IntegerField(db_column='NOMINA_FACE_LEN', blank=True, null=True)  # Field name made lowercase.
    b_matcher_flag = models.CharField(db_column='B_MATCHER_FLAG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nomina_p26 = models.BooleanField(db_column='NOMINA_P26', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOMINA'
        app_label = 'ONLYCONTROL'