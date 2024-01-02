from django.db import models

from apps.usuarios.models import User, Areas
from apps.activos.models import activo_areas

# Create your models here.

class Cargos(models.Model):
    nombre_cargo = models.CharField(max_length=500,blank=True, null=True)
    fch_modifica = models.DateTimeField(blank=True, null=True)
    usu_modifica = models.CharField(max_length=50,blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'personal\".\"cargos'



class Persona(models.Model):
    cedula = models.CharField(primary_key=True, unique=True, max_length=13)
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    cod_empleado = models.IntegerField(null=True, blank=True)
    estado = models.IntegerField(null=True, blank=True)
    bandera = models.IntegerField(null=False, blank=False)
    estado_pl = models.BooleanField(blank=True, null=True, default=False)
    estado_al = models.BooleanField(blank=True, null=True, default=False)
    area = models.ForeignKey(Areas, models.DO_NOTHING, related_name="areas")
    extension = models.CharField(max_length=10,null=True,blank=True)
    fch_ingreso = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    autorizado = models.BooleanField(blank=True, null=True)
    nom_empresa = models.CharField(max_length=250, blank=True, null=True)
    username_sia = models.CharField(max_length=50, blank=True, null=True)

    
    class Meta:
        managed = True
        db_table = 'personal\".\"persona'

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

        permissions = (
            ('menu_ecofroz', 'Acceso Menu Ecofroz'),
            ('persona_directorio', 'Directorio de Personal'),
            ('capacitacion', 'Capacitacion'),
            ('capacitacion_guardias', 'Capacitación Guardianía'),
            ('gpt', 'Chat GPT'),
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class PersonaDet(models.Model):
    persona = models.ForeignKey(Persona, models.DO_NOTHING)  
    fch_modifica = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"persona_det'

    

class Vehiculos(models.Model):
    placa = models.CharField(primary_key=True, max_length=7)
    persona = models.ForeignKey(Persona, models.DO_NOTHING)
    matricula = models.CharField(max_length=250, null=True, blank=True)
    estado = models.IntegerField(null=True, blank=True)
    random = models.IntegerField(null=True, blank=True)
    bandera = models.IntegerField(null=False, blank=False)
    estado_pl = models.BooleanField(blank=True, null=True, default=False)
    maximo = models.IntegerField(null=True, blank=True, default=0)
    referencia = models.CharField(max_length=500, null=True, blank=True)
    fecha_modifica = models.DateTimeField(blank=True, null=True)
    persona_edita = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"vehiculos'

        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return self.placa

class PersonaRegistro(models.Model):
    persona = models.ForeignKey(Persona, models.DO_NOTHING)
    fch_ingreso = models.DateField(blank=True, null=True)
    fch_ingreso_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_ingreso = models.DateTimeField(blank=True, null=True)
    hr_ingreso_txt = models.CharField(max_length=5, blank=True, null=True)
    hr_salida_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_salida_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    hr_entrada_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_entrada_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    fch_salida =models.DateField(blank=True, null=True)
    fch_salida_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_salida = models.DateTimeField(blank=True, null=True)
    hr_salida_txt = models.CharField(max_length=5, blank=True, null=True)
    carnet = models.BooleanField(blank=False, null=False, default=True)
    usuario_registra = models.ForeignKey(User, models.DO_NOTHING)
    ubica = models.CharField(max_length=3)
    ord = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"persona_registro'

        verbose_name = 'Registro Persona'
        verbose_name_plural = 'Registros Personas'

        permissions = (
            ('registro_personal', 'Registros de Personal'),
            ('reporte_ingresos', 'Reporte de Ingresos'),
            ('busqueda_rapida', 'Busqueda Rapida'),
            ('registro_ac', 'Registros de Personal Agua Clara'),
            ('registro_ll', 'Registros de Personal La Laurita'),
            ('registro_la', 'Registros de Personal La Avelina'),
            ('registro_lm', 'Registros de Personal La Merced'),
        )

        ordering = ['-ord']

class AlmuerzoRegistro(models.Model):
    persona = models.ForeignKey(Persona, models.DO_NOTHING)
    fecha = models.DateField(blank=True, null=True)
    fecha_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_salida_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_salida_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    hr_entrada_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_entrada_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    usuario_registra = models.ForeignKey(User, models.DO_NOTHING)
    ord = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"almuerzo_registro'

        verbose_name = 'Registro Almuerzo'
        verbose_name_plural = 'Registros Almuerzos'

        permissions = (
            ('registro_almuerzos', 'Registros de Almuerzos'),
            ('reporte_almuerzos', 'Reporte de Almuerzos'),
        )

        ordering = ['-ord']

class VehiculoRegistro(models.Model):
    vehiculo = models.ForeignKey(Vehiculos, models.DO_NOTHING, related_name='detalle_reg')
    fch_ingreso = models.DateField(blank=True, null=True)
    fch_ingreso_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_ingreso = models.DateTimeField(blank=True, null=True)
    hr_ingreso_txt = models.CharField(max_length=5, blank=True, null=True)
    hr_salida_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_salida_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    hr_entrada_almuerzo = models.DateTimeField(blank=True, null=True)
    hr_entrada_almuerzo_txt = models.CharField(max_length=5, blank=True, null=True)
    fch_salida =models.DateField(blank=True, null=True)
    fch_salida_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_salida = models.DateTimeField(blank=True, null=True)
    hr_salida_txt = models.CharField(max_length=5, blank=True, null=True)
    revision_vehiculo = models.BooleanField(null=True, blank=True)
    usuario_registra = models.ForeignKey(User, models.DO_NOTHING)
    ubica = models.CharField(max_length=3)
    ord = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"vehiculo_registro'

        verbose_name = 'Registro Vehículo'
        verbose_name_plural = 'Registros Vehículos'

        permissions = (
            ('registro_vehiculo', 'Registros de Vehículos'),
            ('reporte_vehiculos', 'Reporte de ingreso de Vehículos'),
            ('registro_reporte_diario', 'Registro Diario de Novedades Seguridad'),
            ('supervisa_reporte_diario', 'Supervisa Reporte Diario de Novedades Seguridad'),

        )

class Transportista(models.Model):
    ruc = models.CharField(max_length=13, unique=True)
    transportista = models.CharField(max_length=150, blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'personal\".\"transportista'

        verbose_name = 'Transportista'
        verbose_name_plural = 'Transportistas'

        permissions = (
            ('registro_transporte', 'Registro de Transportistas'),
        )

        ordering = ['transportista']
    
    def __str__(self):
        return self.transportista

class Cabezales(models.Model):
    transportista = models.ForeignKey(Transportista, models.DO_NOTHING)
    placa = models.CharField(max_length=7, unique=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    estado = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = 'personal\".\"cabezales'

        verbose_name = 'Cabezal'
        verbose_name_plural = 'Cabezales'

        permissions = (
            ('registro_cabezal', 'Registro de Cabezales'),
        )
    
        ordering = ['placa']

    def __str__(self):
        return self.placa
    

class Chofer(models.Model):
    cedula = models.CharField(primary_key=True, max_length=13)
    nombres = models.CharField(max_length=250, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    estado = models.IntegerField(default=1)
    transportista = models.ForeignKey(Transportista, models.DO_NOTHING,blank=True)
    placa = models.ForeignKey(Cabezales, models.DO_NOTHING,blank=True)
    observaciones = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"chofer'

        verbose_name = 'Chofer'
        verbose_name_plural = 'Choferes'

        permissions = (
            ('registro_chofer', 'Registro de Choferes'),
        )

dest={
    ('GY','GUAYAQUIL'),
    ('PS','POSORJA'),
}

class ContenedorRegistro(models.Model):
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING)
    placa = models.CharField(max_length=7, blank=False)
    num_contenedor_ingreso = models.CharField(max_length=12)
    fch_ingreso = models.DateField(blank=True, null=True)
    fch_ingreso_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_ingreso = models.DateTimeField(blank=True, null=True)
    hr_ingreso_txt = models.CharField(max_length=5, blank=True, null=True)
    num_contenedor_salida = models.CharField(max_length=12)
    fch_salida =models.DateField(blank=True, null=True)
    fch_salida_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_salida = models.DateTimeField(blank=True, null=True)
    hr_salida_txt = models.CharField(max_length=5, blank=True, null=True)
    sello_1 = models.CharField(max_length=100, blank=True, null=True)
    sello_2 = models.CharField(max_length=100, blank=True, null=True)
    sello_3 = models.CharField(max_length=100, blank=True, null=True)
    sello_basc_1 = models.CharField(max_length=100, blank=True, null=True)
    sello_basc_2 = models.CharField(max_length=100, blank=True, null=True)
    sello_basc_3 = models.CharField(max_length=100, blank=True, null=True)
    sello_eco_1 = models.CharField(max_length=100, blank=True, null=True)
    sello_eco_2 = models.CharField(max_length=100, blank=True, null=True)
    sello_eco_3 = models.CharField(max_length=100, blank=True, null=True)
    sello_naviera = models.CharField(max_length=100, blank=True, null=True)
    ord = models.DateTimeField(auto_now=True)
    solo_cabezal = models.BooleanField(blank=True,null=True)
    destino = models.CharField(max_length=2, blank=True, null=True, choices=dest)
    tmaxgye = models.DateTimeField(blank=True, null=True)
    tmaxpsj = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"contenedor_registro'

        verbose_name = 'Registro Contenedor'
        verbose_name_plural = 'Registro Contenedores'

        permissions = (
            ('registro_contenedor', 'Registro de Contenedores'),
            ('reporte_contenedor', 'Reporte de Contenedores'),
        )

estado_reporte={
    (1,'Enviado'),
    (2,'Recibido'),
    (3,'Recibido con Observaciones'),
    
}

guardias={
    (1,'Chiliquinga Carlos'),
    (2,'FAJARDO MOSQUERA FABIAN'),
    (3,'Arguero Hector'),
    (4,'CHANGOLUISA ZAMBRANO FREDDY'),
    (5,'FLORES MARTINEZ VICENTE'),
    (6,'LEON VARGAS WILMER'),
    (7,'OCAÑA HERMOSA EDISON'),
    (8,'ORTIZ REMACHE MARCO'),
    
}


class ReporteNovedades(models.Model):
    numreporte = models.AutoField(primary_key=True)
    guardia1 = models.CharField(max_length=200, blank=True, null=True)
    guardia2 = models.CharField(max_length=200, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True, choices=estado_reporte)
    fchregistro = models.DateTimeField(blank=True, null=True)
    fchrecibido = models.DateTimeField(blank=True, null=True)
    asunto = models.CharField(max_length=1000, blank=True, null=True) 
    observaciones_guardias = models.CharField(max_length=50000, blank=True, null=True)
    observaciones_seg = models.CharField(max_length=20000, blank=True, null=True)
    estado_observaciones_seg = models.BooleanField(blank=True, null=True)
        
    class Meta:
        managed = True
        db_table = 'personal\".\"reportenovedades'
    

class DetReporteNovedades(models.Model):
    numreporte = models.ForeignKey('ReporteNovedades', related_name = 'detnovedades', on_delete=models.CASCADE)
    img_1 = models.ImageField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='otros_doc/', blank=True, null=True, verbose_name='Imagen 2')
    
    class Meta:
        managed = True
        db_table = 'personal\".\"detreportenovedades'

class TrackBusqueda(models.Model):
    personabb = models.CharField(max_length=300, blank=True, null=True)
    personab = models.CharField(max_length=40, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'personal\".\"busquedas'

