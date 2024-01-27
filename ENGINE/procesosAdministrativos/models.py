from django.db import models
from django.contrib.auth.models import User
# Create your models here.
codigo_qr_tipo={
    (0, 'Secundario'),
    (1, 'Principal')
}
class activo_areas(models.Model):
    area_codigo = models.AutoField(primary_key=True)
    area_nombre = models.CharField(max_length=50, blank=True, null=True)
    area_estado = models.IntegerField(blank=True, null=True)
    area_departamento = models.IntegerField(blank=True, null=True)
    area_ubica = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activos\".\"activo_areas'

        ordering = ['area_nombre']

    def __str__(self):
        return str(self.area_nombre)

class CodigoQrAreas(models.Model):
    area = models.ForeignKey(activo_areas, models.DO_NOTHING)
    codigo_qr = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.IntegerField(null=True, blank=True, choices=codigo_qr_tipo, default = 0)
    alterar = models.BooleanField(default= False)
    activo = models.BooleanField()
    
    class Meta:
        managed = True
        db_table = 'procesos\".\"area_codigo_qr'
       
    def __str__(self):
        return self.id

estado_acceso_ubica = {
    (0, 'Incompleto'),
    (1, 'Completo'),
    (2, 'No Registrado')
}

class CabRegistroAccesoUbica(models.Model):
    usuario = models.ForeignKey(User, models.DO_NOTHING)
    area = models.ForeignKey(CodigoQrAreas, models.DO_NOTHING)
    fecha_hora_ingreso = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)
    completado = models.IntegerField(blank=False, null=False, choices=estado_acceso_ubica, default = 0)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    nombre_usuario = models.CharField(max_length=255, null=False, blank=False) 
    
    class Meta:
        managed = True 
        db_table = 'procesos\".\"registro_acceso_ubicacion_cab'
        
    def __str__(self):
        return self.id
    
class DetRegistroAccesoUbica(models.Model):
    cab_registro = models.ForeignKey(CabRegistroAccesoUbica, models.DO_NOTHING)
    completado = models.IntegerField(blank=False, null=False, choices=estado_acceso_ubica, default = 0)
    observacion = models.CharField(max_length=255, null=True, blank=True)
    codigo_area = models.ForeignKey(CodigoQrAreas, models.DO_NOTHING)
    
    class Meta:
        managed = True 
        db_table = 'procesos\".\"registro_acceso_ubicacion_det'
        
    def __str__(self):
        return self.id


        

    