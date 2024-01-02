from django.db import models
from apps.usuarios.models import User, Generador


class proyectos_contabilidad(models.Model):
    nombre_proyecto = models.CharField(max_length=1000, blank=True, null=True)
    codigo_proyecto = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    fecha_creacion = models.DateField(blank=True,null=True)
    fecha_modifica = models.DateField(blank=True,null=True)
    persona_edita = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'parametros\".\"proyectos_contabilidad'

        permissions = (
            ('edicion_proyectos_conta', 'Edicion Proyectos Contabilidad'),
        )

    def __str__(self):
        return self.nombre_proyecto

class tipo_notificacion(models.Model):
    nombre_notificacion = models.CharField(max_length=500, blank=True, null=True)
    nombre_abreviado = models.CharField(max_length=80, blank=True, null=True)
    url_tipo = models.CharField(max_length=500, blank=True, null=True)
    url_lista = models.CharField(max_length=500, blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'parametros\".\"tipo_notificacion'

class modelo_App(models.Model):
    app_origen = models.CharField(max_length=150, null=True, blank=True)
    model = models.CharField(max_length=150, null=True, blank=True)

    class Meta:
        managed = True
        db_table = 'parametros\".\"modelo_app'

class notificaciones_globales(models.Model):
    usuario_activa = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    autorizador_id = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='autorizadorid')
    tipo = models.ForeignKey('tipo_notificacion', models.DO_NOTHING, blank=True, null=True)
    app_origen = models.ForeignKey(modelo_App, models.DO_NOTHING, blank=True, null=True)
    estado = models.BooleanField(blank=True, null=True)
    identificador = models.IntegerField(blank=True,null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'parametros\".\"notificaciones_globales'

app_origen={
    ('1','ACTIVOS'),
    ('2','INSUMOS/TRAB.'),
}

class consolida_ordenes_proyectos(models.Model):
    orden = models.IntegerField(blank=True,null=True)
    fecha_aprueba_compra = models.DateTimeField(blank=True,null=True)
    app_origen = models.CharField(choices=app_origen,max_length=60, null=True, blank=True)
    solicita = models.CharField(max_length=100, null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    tipo = models.CharField(max_length=200, null=True, blank=True)
    proyecto = models.CharField(max_length=1000, null=True, blank=True)
    descripcion = models.CharField(max_length=10000, null=True, blank=True)
    proveedor = models.CharField(max_length=300, null=True, blank=True)
    valor = models.FloatField(blank=True, null=True)
    analista = models.CharField(max_length=50, null=True, blank=True)


    class Meta:
        managed = True
        db_table = 'parametros\".\"consolida_ordenes_proyectos' 