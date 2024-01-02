from django.db import models
from apps.activos.models import activo_depar, activo_areas, activo_ubica
from apps.usuarios.models import User

estado={
    (1,'Pendiente'),
    (2,'Aprobado'),
    (3,'Rechazada'),
    (4,'Anulada')
}

estado2={
    (1,'Pendiente'),
    (2,'En proceso'),
    (3,'Devuelta'),
    (4,'Finalizada'),
    (5,'Convertida')
}

tipo_orden={
    (1,'Obra Civil'),
    (2,'Cableado Estructurado'),
    (3,'Pintura'),
    (4,'Eléctricos'),
    (5,'Estructuras Metálicas'),
    (6,'Adecuaciones'),
    (7,'Mantenimiento Maquinaria'),
    (8,'Mantenimiento Otros'),
}


class SolicitudTrabajoInterno(models.Model):
    numtrabajo = models.AutoField(primary_key=True)
    tipo = models.IntegerField(blank=True, null=True, choices=tipo_orden)
    ubica = models.ForeignKey(activo_ubica, models.DO_NOTHING)
    departamento = models.ForeignKey(activo_depar, models.DO_NOTHING)
    area = models.CharField(max_length=301, blank=True, null=True)
    usuario_solicita = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    usuario_aprueba1n = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='aprueba1n')
    estado1n = models.IntegerField(blank=True, null=True, choices=estado)
    fchsolicita = models.DateTimeField(blank=True, null=True)
    fchaprueba1n = models.DateTimeField(blank=True, null=True)
    fecha_en_proceso = models.DateTimeField(blank=True, null=True)
    fecha_finaliza_rechaza_convierte = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=10000, blank=True, null=True)
    justificacion = models.CharField(max_length=10000, blank=True, null=True)
    estado2n = models.IntegerField(blank=True, null=True, choices=estado2)
    fecha_aprox_entrega = models.DateTimeField(blank=True, null=True)
    usuario_aprueba_mantenimiento = models.CharField(max_length=10000, blank=True, null=True)
    entregado = models.BooleanField(blank=True, null=True)
    fecha_real_entrega = models.DateTimeField(blank=True, null=True)
    observaciones_devuelve_mantenimiento = models.CharField(max_length=10000, blank=True, null=True)
    observaciones_internas_mantenimiento = models.CharField(max_length=10000, blank=True, null=True)
    observaciones_rechazo1n = models.CharField(max_length=10000, blank=True, null=True)
    anula = models.BooleanField(blank=True, null=True)
    num_req_sia = models.IntegerField(blank=True, null=True)
    estado_mant = models.IntegerField(blank=True, null=True, choices=estado2)
    fecha_en_proceso_mant = models.DateTimeField(blank=True, null=True)
    fecha_finaliza_mant = models.DateTimeField(blank=True, null=True)
    
    
    
    class Meta:
        managed = True
        db_table = 'trabajosinternos\".\"solicitud'

        permissions = (
            ('acceso_trabajos_internos', 'Acceso a Trabajos Internos'),
            ('ingresa_trabajos_internos', 'Ingresa Trabajos Internos'),
            ('autoriza_solicitudes_trabajos_internos', 'Autoriza Solicitudes Trabajos Internos'),
            ('gestiona_solicitudes_trabajos_internos', 'Gestor de Solicitudes Trabajos Internos'),
            ('asignaciones_mantenimiento_trabajos_internos', 'Asignaciones de Solicitudes Trabajos Internos'),

        )
    

class DetSolicitudTrabajoInterno(models.Model):
    numtrabajo = models.ForeignKey('SolicitudTrabajoInterno', related_name = 'camello', on_delete=models.CASCADE)
    img_1 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 1')
    img_2 = models.ImageField(upload_to='img_pedidos/', blank=True, null=True, verbose_name='Imagen 2')
    
    class Meta:
        managed = True
        db_table = 'trabajosinternos\".\"detsolicitud'

class RecibeEncargo(models.Model):
    responsable = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    asignadoa = models.ManyToManyField(SolicitudTrabajoInterno, blank=True, related_name='responsables')

    class Meta:
        managed = True
        db_table = 'trabajosinternos\".\"asignados'


