from django.db import models
from django.contrib.auth.models import AbstractUser

# from apps.activos.models import activo_tipo

# Create your models here.

tipo = {
    (1, 'Principal'),
    (2, 'Secundario'),
    (3, 'Salida Activos'),
}

estado = {
    (0, 'Inactivo'),
    (1, 'Activo'),
}

class Autorizador(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    e_mail = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True, choices=tipo)
    user_id = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='usuario')
    status = models.BooleanField(blank=True, null=True, default=1)

    class Meta:
       verbose_name = 'Autorizador'
       verbose_name_plural = 'Autorizadores'

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Cotizador(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    e_mail = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='usuarioseleccionacotiza')
    status = models.BooleanField(blank=True, null=True, default=1)
    # tipo = models.ForeignKey(activo_tipo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
       verbose_name = 'Cotizador'
       verbose_name_plural = 'Cotizadores'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Generador(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    e_mail = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE, related_name='usuariogenera')

    class Meta:
       verbose_name = 'Generador'
       verbose_name_plural = 'Generadores'
    
    def __str__(self):
        return self.first_name

class User(AbstractUser):
    autorizador = models.ManyToManyField(Autorizador, blank=True)
    cotizador = models.ForeignKey(Cotizador, models.DO_NOTHING, blank=True, null=True)
    generador = models.ForeignKey(Generador, models.DO_NOTHING, blank=True, null=True)
    soporte = models.BooleanField(null=True, blank=True)
    guardia = models.BooleanField(null=True, blank=True)
    asignado_mantenimiento = models.BooleanField(null=True, blank=True)
    mantenimiento = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='revisa_mantenimiento')
    supervisor1 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='revisa_supervisor1')
    supervisor2 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='revisa_supervisor2')
    generador_int = models.ForeignKey(Generador, models.DO_NOTHING, blank=True, null=True, related_name='generador_int')
    autoriza_oti = models.ForeignKey(Autorizador, models.DO_NOTHING, blank=True, null=True, related_name='aoti')
    consulta_experta = models.BooleanField(null=True, blank=True)
    genera_consultas_a_expertos = models.BooleanField(null=True, blank=True)
    rol = models.ForeignKey('Roles', on_delete=models.DO_NOTHING, blank=True, null=True)
    activo_estado_oc = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='activo_only_control')
    empleado_cod = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['username']

        permissions = (
            ('procesos', 'Procesos'),

            ## Desecho
            ('desecho', 'Desecho'),
            ('ingresa_solicitud_desecho', 'Ingresa Solicitudes Desecho'),
            ('autoriza_1n_desecho', 'Autoriza Solicitudes Desecho'),
            ('autoriza_1n_donacion', 'Autoriza Solicitudes Donaciones'),
            ('autoriza_2n_desecho', 'Autoriza Seguridad Solicitudes Desecho'),
            ('salida_desecho_guardias', 'Salida Desecho Guardias'),
            ('reporte_general_desecho', 'Reporte General Desecho'),

            ## Recepción Materia Prima
            ('materia_prima', 'Materia Prima'),
            ('inspeccion_materia_prima', 'Inspección Materia Prima'),

            ## Control Limpieza
            ('control_limpieza', 'Control Limpieza'),
            ('ingreso_parametros_cl', 'Ingreso de Parametros CL'),
            ('ingreso_programacion_cl', 'Ingreso de Programación CL'),
            ('documento_cl', 'Control de Limpieza'),
            ('apr_psqi', 'Aprobador PSQI'),

            ## Material Empaque
            ('material_empaque', 'Material de Empaque'),
            ('lista_me', 'Material de Empaque'),
            ('ingreso_me', 'Ingreso de Material de Empaque'),
            ('ingreso_po', 'Ingreso de Polizas'),
            ('productos_me', 'Activación de Productos'),
        )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Email(models.Model):
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    e_mail = models.CharField(max_length=250, blank=True, null=True)
    op_codifica_activo = models.BooleanField(blank=True, null=True)
    op_activa_activo = models.BooleanField(blank=True, null=True)
    op_1 = models.BooleanField(blank=True, null=True)
    op_2 = models.BooleanField(blank=True, null=True)
    op_3 = models.BooleanField(blank=True, null=True)
    op_4 = models.BooleanField(blank=True, null=True)
    op_5 = models.BooleanField(blank=True, null=True)
    op_6 = models.BooleanField(blank=True, null=True)
    op_7 = models.BooleanField(blank=True, null=True)
    op_8 = models.BooleanField(blank=True, null=True)
    op_9 = models.BooleanField(blank=True, null=True)
    op_10 = models.BooleanField(blank=True, null=True)

class Ubicacion(models.Model):
    ubica_nombre = models.CharField(max_length=50, blank=False, null=True)
    ubica_estado = models.IntegerField(blank=True, null=False)

    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = 'Ubicaciones'

        ordering = ['ubica_nombre']


    def __str__(self):
        return str(self.ubica_nombre)

class Departamento(models.Model):
    dep_nombre = models.CharField(max_length=50, blank=False, null=True)
    dep_estado = models.IntegerField(blank=True, null=False)
    dep_ubica = models.ForeignKey('Ubicacion', models.DO_NOTHING)
    autoriza_salida = models.ForeignKey('Autorizador', models.DO_NOTHING)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

        ordering = ['dep_nombre']

    def __str__(self):
        return self.dep_nombre

class Areas(models.Model):
    area_nombre = models.CharField(max_length=50, blank=False, null=True)
    area_estado = models.IntegerField(blank=True, null=False)
    area_departamento = models.ForeignKey('Departamento', models.DO_NOTHING)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'

        ordering = ['area_nombre']

    def __str__(self):
        return str(self.area_nombre)

class Roles(models.Model):
    cod = models.CharField(max_length=3, primary_key=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    estado = models.IntegerField(blank=True, null=True, choices=estado)

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        managed = True

        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'