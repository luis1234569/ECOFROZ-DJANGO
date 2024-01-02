from django.db import models

# Create your models here.

    
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
    
class motivo(models.Model):
    motivo= mo

class solicita_puesto(models.Model):
    ubicacion= models.ForeignKey(activo_ubica, on_delete=models.CASCADE)
    departamento= models.ForeignKey(activo_depar, on_delete=models.CASCADE)
    area= models.ForeignKey(activo_areas, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    justificacion = models.CharField(max_length=255)
    def __str__(self):
        return str(self.nombre)