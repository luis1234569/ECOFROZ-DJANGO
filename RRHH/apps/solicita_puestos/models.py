from django.db import models
import datetime

# Create your models here.
estado = {
    ('', 'Pendiente'),
    (1, 'Aprobado'),
    (0, 'No Aprobado'),
    (2, 'Anulada')
}


motivo = {
    ('nuevo', 'Nuevo'),
    ('reemplazo', 'Reemplazo'),
}


class activo_ubica(models.Model):
    ubica_nombre = models.CharField(max_length=50, blank=False, null=True)
    ubica_estado = models.IntegerField(blank=True, null=False)

    def __str__(self):
        return str(self.ubica_nombre)


class activo_depar(models.Model):
    dep_nombre = models.CharField(max_length=50, blank=False, null=True)
    dep_estado = models.IntegerField(blank=True, null=False)
    autoriza_salida = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.dep_nombre


class activo_areas(models.Model):
    area_codigo = models.AutoField(primary_key=True)
    area_nombre = models.CharField(max_length=50, blank=False, null=True)
    area_estado = models.IntegerField(blank=True, null=False)
    area_departamento = models.ForeignKey('activo_depar', models.DO_NOTHING)
    area_ubica = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.area_nombre)


class solicita_puesto(models.Model):
    ubicacion = models.ForeignKey(activo_ubica, models.DO_NOTHING)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.ForeignKey(activo_areas, models.DO_NOTHING)
    puesto = models.CharField(blank=True, null=False, max_length=20)
    descripcion = models.CharField(blank=True, null=True, max_length=255)
    justificacion = models.CharField(blank=True, null=False, max_length=255)
    solicitante = models.CharField(blank=True, null=False, max_length=255)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    estado_aprobacion = models.IntegerField(
        blank=True, null=True, choices=estado)
    motivo = models.CharField(
        blank=True, null=True, choices=motivo, default='nuevo')

    def __str__(self):
        return str(self.puesto)
