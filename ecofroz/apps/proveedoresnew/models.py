from django.db import models

proveedor_estado = {
    ('ACTIVO','ACTIVO'),
    ('INACTIVO','INACTIVO'),
}

categorizacion = {
    ('ACTIVO','ACTIVO'),
    ('INACTIVO','INACTIVO'),
}

class proveedor(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    categoria = models.ForeignKey('proveedor_categoria', models.DO_NOTHING,blank=True,null=True)
    nombre_empresa = models.CharField(max_length=200,blank=True, null=True)
    direccion_matriz = models.CharField(max_length=200,blank=True, null=True)
    horario_trabajo = models.CharField(max_length=200,blank=True, null=True)
    representante_legal = models.CharField(max_length=100,blank=True, null=True)
    ruc = models.CharField(max_length=13,blank=True, null=True)
    nombre_contacto_ecofroz =  models.CharField(max_length=100,blank=True, null=True)
    telefono =  models.CharField(max_length=15,blank=True, null=True)
    celular =  models.CharField(max_length=15,blank=True, null=True)
    calificacion = models.CharField(max_length=15,blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True,null=True,choices=proveedor_estado)
    categorizacion = models.CharField(max_length=20, blank=True,null=True,choices=categorizacion)
    fecha_modifica = models.DateTimeField(auto_now=True)
    fecha_modifica_txt =  models.CharField(max_length=8,blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_registro_txt =  models.CharField(max_length=8,blank=True, null=True)
    observaciones = models.CharField(max_length=2000,blank=True, null=True) 
 
    class Meta:
        managed = True
        db_table = 'proveedoresnew\".\"proveedor'
        
      
        ordering = ['-fecha_modifica']
    
    def __str__(self):
        return str(self.nombre_empresa)

class proveedor_encuesta(models.Model):
    pregunta = models.CharField(max_length=2000,blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'proveedoresnew\".\"proveedor_encuesta'

    def __str__(self):
       return str(self.pregunta)

class proveedor_categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100,blank=True, null=True)
    encuesta = models.ManyToManyField('proveedor_encuesta')
    
    class Meta:
        managed = True
        db_table = 'proveedoresnew\".\"proveedor_categoria'

    def __str__(self):
       return str(self.nombre_categoria)



class proveedor_respuestas(models.Model):
    respuesta = models.CharField(max_length=2000,blank=True, null=True)
    proveedor = models.ForeignKey('proveedor', models.DO_NOTHING,blank=True,null=True)
    encuesta = models.ForeignKey('proveedor_encuesta', models.DO_NOTHING,blank=True,null=True)
   
    class Meta:
        managed = True
        db_table = 'proveedoresnew\".\"proveedor_respuestas'

    def __str__(self):
       return str(self.pregunta)