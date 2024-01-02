from django.db import models

from apps.usuarios.models import Ubicacion, Departamento, Areas
from apps.usuarios.models import User

# Create your models here.

tipo={
    (1,'Soporte'),
}

class Estados(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField()
    tipo = models.IntegerField(choices=tipo)

    class Meta:
        managed = True
        db_table = 'soporte\".\"estados'

        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return str(self.nombre)

class Asignaciones(models.Model):
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    correo = models.EmailField()
    estado = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'soporte\".\"asignaciones'

        verbose_name = 'Asignación'
        verbose_name_plural = 'Asignaciones'

    def __str__(self):
        return str(self.area)

class Problemas(models.Model):
    nombre = models.CharField(max_length=100)
    asignacion = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)
    tipo = models.IntegerField(choices=tipo)
    asignacion = models.ForeignKey('Asignaciones', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'soporte\".\"problemas'

        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'

    def __str__(self):
        return str(self.nombre)

class TicketsIt(models.Model):
    numticket = models.AutoField(primary_key=True)
    solicita_nombre = models.CharField(max_length=250, blank=True, null=True)
    solicita_apellido = models.CharField(max_length=250, blank=True, null=True)
    solicita_codigo = models.IntegerField(blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, blank=True, null=True)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Areas, models.DO_NOTHING, blank=True, null=True)
    estado_solicitud = models.ForeignKey('Estados', models.DO_NOTHING, blank=True, null=True)
    tipo_problema = models.ForeignKey('Problemas', models.DO_NOTHING, blank=True, null=True)
    descripcion_problema = models.CharField(max_length=1000, blank=True, null=True)
    # fch_solicita = models.DateTimeField(auto_now_add=True)
    fch_solicita = models.DateTimeField(blank=True, null=True)
    fch_solicita_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_solicita = models.CharField(max_length=5, blank=True, null=True)
    fch_soluciona = models.DateTimeField(blank=True, null=True)
    fch_soluciona_txt = models.CharField(max_length=8, blank=True, null=True)
    hr_soluciona_txt = models.CharField(max_length=5, blank=True, null=True)
    observa_solucion = models.CharField(max_length=1000, blank=True, null=True)
    area_responsable = models.ForeignKey('Asignaciones', models.DO_NOTHING, blank=True, null=True)
    usuario_responsabe = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='responsable')
    reasignado = models.BooleanField(blank=True, null=True)
    observa_reasignacion = models.CharField(max_length=1000, blank=True, null=True)
    usuario = models.IntegerField(blank=True, null=True)
    delta_solucion = models.IntegerField(blank=True, null=True)
    reasignado_a = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='reasignado')


    class Meta:
        managed = True
        db_table = 'soporte\".\"ticketsti'

        verbose_name = 'Tickets TI'
        verbose_name_plural = 'Tickets TI'

        permissions = (
            ('soporte_interno', 'Acceso a Soporte Interno'),
        )
