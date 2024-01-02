from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.

valor_bool = {
    ('SI','SI'),
    ('NO','NO'),
}

valor_bool2 = {
    (True,'SI'),
    (False,'NO'),
}

valor_unico = {
    ('SI','SI'),
    
}


proveedor_estado = {
    ('ACTIVO','ACTIVO'),
    ('INACTIVO','INACTIVO'),
}

empresa_tipo = {
    ('Persona Natural','Persona Natural'),
    ('Persona Jurídica','Persona Jurídica'),
}

tipo_prov = {
    (0, 'VARIOS'),
    (1, 'EMPAQUE'),
}

class proveedor(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    nombre_empresa = models.CharField(max_length=200,blank=True, null=True)
    nombre_comercial = models.CharField(max_length=200,blank=True, null=True)
    direccion_matriz = models.CharField(max_length=200,blank=True, null=True)
    horario_trabajo = models.CharField(max_length=200,blank=True, null=True)
    representante_legal = models.CharField(max_length=100,blank=True, null=True)
    ruc = models.CharField(max_length=13,blank=True, null=True, unique=True)
    nombre_contacto_ecofroz =  models.CharField(max_length=100,blank=True, null=True)
    telefono =  models.CharField(max_length=15,blank=True, null=True)
    celular =  models.CharField(max_length=15,blank=True, null=True)
    calificacion = models.IntegerField(blank=True, null=True,default=0)
    estado = models.CharField(max_length=20, blank=True,null=True,choices=proveedor_estado)
    fecha_modifica = models.DateTimeField(auto_now=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_eleboracion = models.DateTimeField(blank=True,null=True)
    tipo_empresa = models.CharField(max_length=500, blank=True,null=True,choices=empresa_tipo)
    categoria = models.ForeignKey('proveedor_categoria', models.DO_NOTHING,blank=False,null=True)
    respondio_encuesta = models.BooleanField(default=False,blank=True,null=True,choices=valor_bool2)
    proveedor_critico = models.BooleanField(default=False,blank=True,null=True,choices=valor_bool2)
    proveedor_revisado = models.BooleanField(default=False,blank=True,null=True,choices=valor_bool2)
    grade = models.CharField(max_length=2, blank=True,null=True)
    control = models.IntegerField(blank=True, null=True,default=0)
    usuario_modifica = models.CharField(max_length=50, blank=True, null=True)
    history = HistoricalRecords()
    tipo_provee = models.IntegerField(blank=True, null=True, choices=tipo_prov)

    @property
    def _history_user(self):
        return self.changed_by
 
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor'
        
        permissions = (
            ('acceso_proveedores', 'Acceso Menu Proveedores'),
            ('acceso_provisional', 'Acceso Provicional Proveedores'),
            ('acceso_rev_calidad', 'Acceso Revisión Proveedores Calidad'),
            ('acceso_auditorias', 'Acceso Auditorias'),
        )

        ordering = ['-fecha_modifica']
    
    def __str__(self):
        return str(self.nombre_empresa)


    
anios = {
    ('UNO',1),
    ('DOS',2),
    ('TRES',3),
    ('CUATRO',4),
    ('CINCO',5),
    ('SEIS',6),
    ('SIETE',7),
    ('OCHO',8),
    ('NUEVE',9),
    ('DIEZ',10),
    ('MAS DE DIEZ','Más de 10'),
    
}



opciones_instalaciones = {
    ('Propias','Propias'),
    ('Compartida por varias empresas','Compartida por varias empresas'),
    ('Trabaja en residencia','Trabaja en residencia'),
    
}

valor_bool_extendido = {
    ('Adjunto a este formulario','Adjunto a este formulario'),
    ('Por correo electrónico','Por correo electrónico'),
    ('Documento Físico','Documento Físico'),
    ('No lo requiero','No lo requiero'),
    ('No lo tengo','No lo tengo'),
    
}

valor_bool_maquinaria = {
    ('Maquinaria y/o equipos','Maquinaria y/o equipos'),
    ('Repuestos de maquinaria y/o equipos','Repuestos de maquinaria y/o equipos'),
    ('Servicio de mantenimiento de maquinaria y/o equipos','Servicio de mantenimiento de maquinaria y/o equipos'),
    ('No','No'),
}

valor_pesticidas = {
    (1,'Registro de los productos en Agrocalidad o Magar'),
    (2,'Fichas técnicas y hojas de seguridad de los productos empleado'),
    (3,'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'),
    (4,'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'),
    (5,'No soy proveedor de pesticidas'),
}

valor_fertilizantes = {
    (1,'Registro de los productos en Agrocalidad o MAGAP'),
    (2,'Fichas técnicas y hojas de seguridad de los productos empleados'),
    (3,'Análisis de metales pesados'),
    (4,'Certificado de que esta libre de noni fenol y cloruro de benzalconio'),
    (5,'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'),
    (6,'Conocer el orígen de las materias primas'),
    (7,'No soy proveedor de fertilizantes'),
}

valor_foliares = {
    (1,'Registro de los productos en Agrocalidad o MAGAP'),
    (2,'Fichas técnicas y hojas de seguridad de los productos empleados'),
    (3,'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'),
    (4,'Conocer el orígen de las materias primas'),
    (5,'No soy proveedor de FOLIARES'),
}

valor_materia_organica = {
    (1,'Registro de los productos en Agrocalidad o MAGAP'),
    (2,'Fichas técnicas y hojas de seguridad de los productos empleados'),
    (3,'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'),
    (4,'Conocer el orígen de las materias primas'),
    (5,'No soy proveedor de MATERIA ORGANICA'),
}

valor_marca_ficha_cal = {
    ('DESACTUALIZADA','DESACTUALIZADA'),
    ('INCORRECTA','INCORRECTA'),
    ('CORRECTA','CORECTA'),
    
}


class documentos_prove(models.Model):
    proveedor = models.ForeignKey('proveedor', models.DO_NOTHING,blank=True,null=True)
    archivos = models.FileField(upload_to='info_proveedores/',blank=True, null=True)
    nombre_corto = models.CharField(max_length=1000, blank=True, null=True)
    es_ficha = models.BooleanField(blank=True,null=True)
    es_hoja_msds = models.BooleanField(blank=True,null=True)
    es_etiqueta_producto = models.BooleanField(blank=True,null=True)
    es_doc_categoria = models.BooleanField(blank=True,null=True)
    es_ficha_pes = models.BooleanField(blank=True,null=True)
    es_ficha_fol = models.BooleanField(blank=True,null=True)
    es_ficha_fer = models.BooleanField(blank=True,null=True)
    es_ficha_mao = models.BooleanField(blank=True,null=True)
    es_ficha_sem = models.BooleanField(blank=True,null=True)
    es_agro_pes = models.BooleanField(blank=True,null=True)
    es_agro_fol = models.BooleanField(blank=True,null=True)
    es_agro_fer = models.BooleanField(blank=True,null=True)
    es_agro_mao = models.BooleanField(blank=True,null=True)
    es_agro_sem = models.BooleanField(blank=True,null=True)
    es_msds_pes = models.BooleanField(blank=True,null=True)
    es_msds_fol = models.BooleanField(blank=True,null=True)
    es_msds_fer = models.BooleanField(blank=True,null=True)
    es_msds_mao = models.BooleanField(blank=True,null=True)
    es_msds_sem = models.BooleanField(blank=True,null=True)
    es_etiqueta_pes = models.BooleanField(blank=True,null=True)
    es_etiqueta_fer = models.BooleanField(blank=True,null=True)
    es_etiqueta_mao = models.BooleanField(blank=True,null=True)
    es_etiqueta_sem = models.BooleanField(blank=True,null=True)
    es_analisis_pes = models.BooleanField(blank=True,null=True)
    es_analisis_fol = models.BooleanField(blank=True,null=True)
    es_analisis_fer = models.BooleanField(blank=True,null=True)
    es_analisis_mao = models.BooleanField(blank=True,null=True)
    es_analisis_sem = models.BooleanField(blank=True,null=True)
    es_certificado_pes = models.BooleanField(blank=True,null=True)
    es_certificado_fol = models.BooleanField(blank=True,null=True)
    es_certificado_fer = models.BooleanField(blank=True,null=True)
    es_certificado_mao = models.BooleanField(blank=True,null=True)
    es_certificado_sem = models.BooleanField(blank=True,null=True)
    es_etiqueta_foliar = models.BooleanField(blank=True,null=True)
    observaciones_docs_agrocalidad = models.CharField(max_length=3000, blank=True, null=True)
    revisado_cal = models.BooleanField(blank=True,null=True,default=False)
    marca_cal = models.CharField(max_length=15, blank=True, null=True,choices=valor_marca_ficha_cal)
    observaciones_cal = models.CharField(max_length=3000, blank=True, null=True)
    observaciones_msds_cal = models.CharField(max_length=3000, blank=True, null=True)
    observaciones_eti_cal = models.CharField(max_length=3000, blank=True, null=True)
    subcategoria =  models.IntegerField(blank=True, null=True)
    fecha_documento = models.DateField(blank=True,null=True)
    observaciones_admin = models.CharField(max_length=3000, blank=True, null=True)
    actualiza = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedores\".\"documentos_prove'


valor_1_20 = {
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15),
    (16,16),
    (17,17),
    (18,18),
    (19,19),
    (20,20),
}

class proveedor_det(models.Model):
    codigo_id = models.ForeignKey('proveedor', on_delete = models.CASCADE,blank=True)
    carta_presentacion = models.FileField(upload_to='info_proveedores/',blank=True, null=True)
    giro_negocio = models.CharField(max_length=500,blank=True, null=True)
    monto_ventas_2018 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2019 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2020 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2021 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2022 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2023 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2024 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    monto_ventas_2025 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    antiguedad =  models.IntegerField(blank=True, null=True)
    num_trabajadores_fijos = models.IntegerField(blank=True, null=True)
    num_clientes = models.IntegerField(blank=True, null=True)
    num_proveedores = models.IntegerField(blank=True, null=True)
    valores_empresa = models.CharField(max_length=5000, blank=True, null=True)
    tieneweb = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    web = models.CharField(max_length=100, blank=True,null=True)
    actividad = models.ForeignKey('proveedor_actividad', models.DO_NOTHING,blank=False, null=True)
    otra_actividad = models.CharField(max_length=100, blank=True,null=True)
    empresa_tipo = models.CharField(max_length=500, blank=True,null=True,choices=empresa_tipo)
    ultima_actualizacion_estatutos = models.CharField(max_length=100, blank=True,null=True)
    ruc_adjunto = models.FileField('info_proveedores',blank=True, null=True)
    referencia_bancaria = models.FileField('info_proveedores',blank=True, null=True)
    certificado_iess = models.FileField('info_proveedores',blank=True, null=True)
    servicio_basico = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_prove1 = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_prove2 = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_prove3 = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_cliente1 = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_cliente2 = models.FileField('info_proveedores',blank=True, null=True)
    ref_comercial_cliente3 = models.FileField('info_proveedores',blank=True, null=True)
    rep_legal = models.FileField('info_proveedores',blank=True, null=True)
    accionistas = models.FileField('info_proveedores',blank=True, null=True)
    anios_como_proveedor = models.IntegerField(blank=True, null=True)
    ventas_ecofroz_2018 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2019 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2020 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2021 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2022 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2023 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2024 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    ventas_ecofroz_2025 = models.CharField(max_length=100,blank=True, null=True,default='0.00')
    subcontrata = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    actividades_subcontratadas = models.CharField(max_length=500, blank=True, null=True)
    confirmacion_canal_comunicacion = models.CharField(max_length=5, blank=True,null=True,choices=valor_unico,default='SI')
    categoria_proveedor = models.ForeignKey('proveedor_categoria', models.DO_NOTHING,blank=True,null=True)
    otra_categoria = models.CharField(max_length=100, blank=True,null=True)
    tiene_certificado_migracion_fundas = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_migracion_fundas = models.FileField('info_proveedores',blank=True, null=True)
    tiene_documento_aceptacion_especificaciones_ecofroz = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    documento_aceptacion_especificaciones_ecofroz = models.FileField('info_proveedores',blank=True, null=True)
    tiene_especificacion_material_empaque = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    especificacion_material_empaque = models.FileField('info_proveedores',blank=True, null=True)
    tiene_aprobaciones_contacto_alimentos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    aprobaciones_contacto_alimentos = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificacion_basc = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_basc = models.FileField('info_proveedores',blank=True, null=True)
    tiene_homologacion_auditoria_basc_ecofroz = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_homologacion_ecofroz = models.FileField('info_proveedores',blank=True, null=True)
    tiene_homologacion_gfsi = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_hologacion_gfsi = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_auditoria_ecofroz_por_no_gfsi = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_auditoria_ecofroz_por_no_gfsi = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_calidad_por_lote = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_calidad_por_lote = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_transporte_exclusivo = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_transporte_exclusivo = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_transporte_sellado = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_transporte_sellado = models.FileField('info_proveedores',blank=True, null=True)
    tiene_formato_informacion_contacto_emergencia = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    formato_informacion_contacto_emergencia = models.FileField('info_proveedores',blank=True, null=True)
    contrato_vigente_ecofroz = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_sistema_calidad_iso9001 = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    otro_sistema_calidad = models.CharField(max_length=100,blank=True, null=True)
    tiene_procedimientos_ventas_no_conformes = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_procesos_mejora_continua = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_plan_respuesta_riesgos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_programa_auditoria_interna = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_sistema_seguridad_logistica_transporte = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    utiliza_transporte_propio = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_documentos_habilitantes_vehiculos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_cobertura_seguro_vehiculos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_cobertura_seguro_ocupantes_vehiculos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_sistema_comunicacion_transmision_datos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    hace_respaldos_periodicos_informacion_empresa = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_activos_asegurados = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    hace_mantenimiento_preventivo = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tipo_instalaciones = models.CharField(max_length=50, blank=True,null=True,choices=opciones_instalaciones)
    giro_negocio_igual = models.CharField(max_length=50, blank=True,null=True,choices=valor_bool)
    descripcion_giro_negocio_otras_empresas = models.CharField(max_length=500,blank=True, null=True)
    requiere_certificado_ambiental = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_certificado_ambiental = models.CharField(max_length=50, blank=True,null=True,choices=valor_bool_extendido)
    certificado_ambiental = models.FileField('info_proveedores',blank=True, null=True)
    tiene_politica_proteccion_ambiente = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    describa_politica_ambiente = models.CharField(max_length=500,blank=True, null=True)
    optimiza_uso_recursos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_programa_manejo_desechos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_politica_responsabilidad_social = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    descripcion_politica_responsabilidad_social = models.CharField(max_length=500,blank=True, null=True)
    tiene_politica_prevencion_actos_corrupcion = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_politica_prevencion_actos_acoso = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_mecanismo_discrimen = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_codigo_conducta = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_plan_continuidad_negocio = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_reglamento_interno_trabajo = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_reglamento_interno_seguridad_salud_laboral = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_politica_inclusion_social = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_practicas_no_discriminacion_laboral = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    capacita_usuarios_prevencion_accidentes = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    prioriza_contratacion_personal_zona = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    realiza_simulacro_emergencia = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    trabajadores_menores_16anios = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_sistema_evaluacion_seleccion_proveedores = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_mecanismo_satisfaccion_cliente = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    mecanismo_satisfaccion_cliente = models.CharField(max_length=500, blank=True,null=True)
    ecofroz_explico_proceso_compra = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    especificaciones_oportunas_claras = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    proceso_compra_agil = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    sugerencia_proceso_compra = models.CharField(max_length=500,blank=True, null=True)
    conoce_proceso_pago = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumplimiento_proceso_pago = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    sugerencia_proceso_pago = models.CharField(max_length=500, blank=True,null=True)
    conoce_proceso_recepcion = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    sugerencia_proceso_recepcion = models.CharField(max_length=500, blank=True,null=True)
    es_atendido_bien = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    sugerencia_relacion_comercial = models.CharField(max_length=500,blank=True, null=True)
    es_proveedor_maquinaria_o_equipo = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_maquinaria)
    tipo_maquinaria_equipo_que_provee = models.CharField(max_length=500,blank=True, null=True)
    tipo_producto_servicio_provee = models.CharField(max_length=500,blank=True, null=True)
    proveedor_pesticidas_requisitos_indispensables = models.CharField(max_length=300, blank=True,null=True,choices=valor_pesticidas)
    proveedor_fertilizantes_requisitos_indispensables = models.CharField(max_length=300, blank=True,null=True,choices=valor_fertilizantes)
    proveedor_foliares_requisitos_indispensables = models.CharField(max_length=300, blank=True,null=True,choices=valor_foliares)
    proveedor_materia_organica_requisitos_indispensables = models.CharField(max_length=300, blank=True,null=True,choices=valor_materia_organica)
    cumple_procedimiento_facturacion = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumple_procedimiento_entrega = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumple_procedimiento_compra = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    antecedentes_verificados_rep_legal = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    tiene_certificado_npma = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_npma = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_aecpu = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_aecpu = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_mip_personal = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_mip_personal = models.FileField('info_proveedores',blank=True, null=True)
    tiene_fichas_tecnicas_y_registros_sanitarios = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    fichas_tecnicas_y_registros_sanitarios = models.FileField('info_proveedores',blank=True, null=True)
    tiene_poliza_responsabilidad_civil = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    poliza_responsabilidad_civil = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_arcsa = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_arcsa = models.FileField('info_proveedores',blank=True, null=True)
    tiene_permiso_funcionamiento = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    permiso_funcionamiento = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificacion_gfsi_o_bpm = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificacion_gfsi_o_bpm = models.FileField('info_proveedores',blank=True, null=True)
    tiene_copia_hoja_seguridad_datos_msds = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    copia_hoja_seguridad_datos_msds = models.FileField('info_proveedores',blank=True, null=True)
    tiene_ingredientes_activos_aprobados = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    ingredientes_activos_aprobados = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_determinar_concentracion_quimico = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    certificado_determinar_concentracion_quimico = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_biodegradabilidad = models.CharField(max_length=100, blank=True,null=True,choices=valor_bool_extendido)
    certificado_biodegradabilidad = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_validaciones_reduccion_logaritmica = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_validaciones_reduccion_logaritmica = models.FileField('info_proveedores',blank=True, null=True)
    tiene_analisis_composicion_concentraciones = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    analisis_composicion_concentraciones = models.FileField('info_proveedores',blank=True, null=True)
    tiene_especificaciones_fichas_tecnicas = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    especificaciones_fichas_tecnicas = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_buenas_practicas_manufactura = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_buenas_practicas_manufactura = models.FileField('info_proveedores',blank=True, null=True)
    tiene_seguimiento_medico_trabajadores = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    seguimiento_medico_trabajadores = models.FileField('info_proveedores',blank=True, null=True)
    tiene_reporte_inspeccion_permiso_funcionamiento = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    reporte_inspeccion_permiso_funcionamiento = models.FileField('info_proveedores',blank=True, null=True)
    tiene_afiliacion_empleados_iess = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    afiliacion_empleados_iess = models.FileField('info_proveedores',blank=True, null=True) 
    tiene_certificado_iso_17025 =  models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_iso_17025 = models.FileField('info_proveedores',blank=True, null=True)
    tiene_carta_garantia = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    carta_garantia = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_tiempo_analisis = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_tiempo_analisis = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_logistica_producto = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_logistica_producto = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_calidad_producto = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_calidad_producto = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_insumos_aoac = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_insumos_aoac = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_patrones_trazables_baja_incertidumbre = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_patrones_trazables_baja_incertidumbre = models.FileField('info_proveedores',blank=True, null=True)
    tiene_licencia_unica_funcionamiento_luae = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    licencia_unica_funcionamiento_luae = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_destruccion_material_x_carga = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_destruccion_material_x_carga = models.FileField('info_proveedores',blank=True, null=True)
    tiene_formato_seleccion_materia_prima = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    formato_seleccion_materia_prima = models.FileField('info_proveedores',blank=True, null=True)
    certificado_de_manejo_otros_productos = models.FileField('info_proveedores',blank=True, null=True)
    tiene_analisis_cumplimiento_fda_173310 = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    analisis_cumplimiento_fda_173310 = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_fabricacion_libre_alergenicos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_fabricacion_libre_alergenicos = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_nfs_h1_h2 = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_nfs_h1_h2 = models.FileField('info_proveedores',blank=True, null=True)
    tiene_ficha_tecnica_hoja_seguridad_registro_sanitario = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    ficha_tecnica_hoja_seguridad_registro_sanitario = models.FileField('info_proveedores',blank=True, null=True)
    tiene_certificado_iso_21469 = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    certificado_iso_21469 = models.FileField('info_proveedores',blank=True, null=True)
    tiene_lista_choferes_autorizados = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    lista_choferes_autorizados = models.FileField('info_proveedores',blank=True, null=True)
    nombre_cooperativa_y_o_compania_pertenecen_vehiculos = models.CharField(max_length=100, blank=True,null=True)
    tiene_permiso_operacion_transporte = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    permiso_operacion_transporte = models.FileField('info_proveedores',blank=True, null=True)
    tiene_matricula_vehiculo_actualizada = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    matricula_vehiculo_actualizada = models.FileField('info_proveedores',blank=True, null=True)
    vehiculos_estan_asegurados = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    poliza_seguro_vehiculos = models.FileField('info_proveedores',blank=True, null=True)
    tiene_seguro_ocupantes_vehiculo = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    poliza_seguro_ocupantes_vehiculo = models.FileField('info_proveedores',blank=True, null=True)
    otros_documentos_enviados1 = models.FileField('info_proveedores',blank=True, null=True)
    otros_documentos_enviados2 = models.FileField('info_proveedores',blank=True, null=True)
    otros_documentos_enviados3 = models.FileField('info_proveedores',blank=True, null=True)
    otros_documentos_enviados4 = models.FileField('info_proveedores',blank=True, null=True)
    otros_documentos_enviados5 = models.FileField('info_proveedores',blank=True, null=True)
    num_documentos_solicitados_categoria = models.IntegerField(blank=True,null=True)
    num_documentos_solicitados_personalizado = models.IntegerField(blank=True,null=True)
    num_documentos_cargados = models.IntegerField(blank=True,null=True)
    tiene_fichas = models.BooleanField(blank=True,null=True,choices=valor_bool2,default=False)
    numero_de_fichas = models.IntegerField(blank=True,null=True,default=0)
    cumple_entrega_docs = models.CharField(max_length=2, blank=True,null=True,default='NO')
    cumple_entrega_docs_esenciales = models.CharField(max_length=2, blank=True,null=True,default='NO')
    proveedor_mant_externo = models.BooleanField(blank=True,null=True,default=False)
    proveedor_ruta_fija = models.BooleanField(blank=True,null=True,default=False)
    asientos = models.IntegerField(blank=True,null=True, default=0)
    enviado_a_calidad = models.BooleanField(blank=True,null=True,default=False)
    fecha_enviado_a_calidad = models.DateTimeField(blank=True,null=True)
    revisado_por_calidad = models.BooleanField(blank=True,null=True,default=False)
    fecha_revisado_por_calidad = models.DateTimeField(blank=True,null=True)
    observaciones_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_fichas_single_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_msds_single_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_etiquetas_single_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_agrocalidad_single_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_fichas_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_fichas_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_fichas_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_fichas_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_fichas_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_agro_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_agro_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_agro_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_agro_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_agro_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_msds_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_msds_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_msds_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_msds_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_msds_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_etiquetas_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_etiquetas_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_etiquetas_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_etiquetas_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_etiquetas_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_analisis_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_analisis_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_analisis_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_analisis_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_analisis_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)

    observaciones_certificados_pes_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_certificados_fol_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_certificados_fer_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_certificados_mao_calidad = models.CharField(max_length=3000, blank=True,null=True)
    observaciones_certificados_sem_calidad = models.CharField(max_length=3000, blank=True,null=True)
    
    observaciones_administrativas = models.CharField(max_length=3000, blank=True,null=True)
    contesta_reclamos_administrativos = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    contesta_reclamos_calidad = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumple_procedimiento_facturacion_calidad = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumple_procedimiento_entrega_calidad = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    cumple_procedimiento_compra_calidad = models.CharField(max_length=5, blank=True,null=True,choices=valor_bool)
    color = models.CharField(max_length=20, blank=True,null=True)
    
    history = HistoricalRecords()


    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_det'

        permissions = (
            ('lista_adqui', 'Acceso Lista Adquisiciones'),
        )


class preguntas_categoria_calidad(models.Model):
    codigo_id = models.ForeignKey('proveedor', on_delete = models.CASCADE,blank=True)


class carga_respuestas_prod_serv_varios(models.Model):
    marca_temporal = models.CharField(max_length=100,primary_key=True)
    p001 = models.CharField(max_length=50, blank=True,null=True) 
    p002 = models.CharField(max_length=2, blank=True,null=True)
    p003 = models.CharField(max_length=2, blank=True,null=True)
    p004 = models.CharField(max_length=2, blank=True,null=True)
    p005 = models.CharField(max_length=2, blank=True,null=True)
    p006 = models.CharField(max_length=300, blank=True,null=True)
    p007 = models.CharField(max_length=2000, blank=True,null=True) 
    p008 = models.CharField(max_length=300, blank=True,null=True)
    p009 = models.CharField(max_length=100, blank=True,null=True)
    p010 = models.CharField(max_length=13, blank=True,null=True) # N° Cedula o RUC
    p011 = models.CharField(max_length=100, blank=True,null=True) #Nombre persona se contacta con Ecofroz
    p012 = models.CharField(max_length=20, blank=True,null=True) #Teléfono fijo
    p013 = models.CharField(max_length=20, blank=True,null=True) #Celular Contacto
    p014 = models.CharField(max_length=200, blank=True,null=True) #Carta de presentación
    p015 = models.CharField(max_length=500,blank=True, null=True) #Giro de negocio
    
    p016 = models.CharField(max_length=100,blank=True, null=True) 
    p017 = models.CharField(max_length=100,blank=True, null=True) 
    p018 = models.CharField(max_length=100,blank=True, null=True) 
    p019 = models.CharField(max_length=100,blank=True, null=True) 
    p020 = models.CharField(max_length=100,blank=True, null=True) 
    p021 = models.CharField(max_length=100,blank=True, null=True) 
    
    p022 = models.CharField(max_length=2000, blank=True, null=True) #3 Valores
    p023 = models.CharField(max_length=2000, blank=True,null=True) #Tiene pagina Web
    p024 = models.CharField(max_length=2000, blank=True,null=True) #Direccion Web
    p025 = models.CharField(max_length=2000, blank=True,null=True) #Actividad
    p026 = models.CharField(max_length=2000, blank=True,null=True) #Persona natural o juridica
    p027 = models.CharField(max_length=2000, blank=True,null=True) #Fecha de aprobación de estatutos
    p028 = models.CharField(max_length=2000, blank=True,null=True) #cambio accionario mayor al 50%
    p029 = models.CharField(max_length=2000, blank=True,null=True) #N° de años que ha sido proveedor de Ecofroz
    p030 = models.CharField(max_length=2000, blank=True,null=True) #Monto (USD) de ventas totales de productos y/o servicios a ECOFROZ S.A en el 2019
    p031 = models.CharField(max_length=2000, blank=True,null=True) #Monto (USD) de ventas de productos y/o servicios a ECOFROZ S.A. en el 2020
    p032 = models.CharField(max_length=2000, blank=True,null=True) #¿Subcontrata alguna actividad importante para el producto/servicio que ofrece?
    p033 = models.CharField(max_length=2000, blank=True,null=True) #En caso de que la respuesta a la pregunta anterior sea "SI", indique la/s actividades sub contratadas, y si es "NO" escriba NO APLICA
    p034 = models.CharField(max_length=2000, blank=True,null=True) #Usted es proveedor de maquinaria o equipos?
    p035 = models.CharField(max_length=2000, blank=True,null=True) #Usted es proveedor de repuestos de maquinaria o equipos?
    p036 = models.CharField(max_length=2000, blank=True,null=True) #Usted es proveedor de servicios de maquinaria o equipos?
    p037 = models.CharField(max_length=2000, blank=True,null=True) #ISO 9001
    p038 = models.CharField(max_length=2000, blank=True,null=True) # Otro diferente a ISO 9001
    p039 = models.CharField(max_length=2000, blank=True,null=True) #Procedimientos de no conformidades
    p040 = models.CharField(max_length=200, blank=True,null=True) #¿Tiene procesos establecidos para desarrollo y mejora continua de sus productos y/o servicios?
    p041 = models.CharField(max_length=200, blank=True,null=True) #¿Cuenta con un plan de respuesta para los riesgos que puedan afectar su operación?
    p042 = models.CharField(max_length=200, blank=True,null=True)
    p043 = models.CharField(max_length=200, blank=True,null=True)
    p044 = models.CharField(max_length=200, blank=True,null=True)
    p045 = models.CharField(max_length=200, blank=True,null=True)
    p046 = models.CharField(max_length=200, blank=True,null=True)
    p047 = models.CharField(max_length=200, blank=True,null=True)
    p048 = models.CharField(max_length=200, blank=True,null=True)
    p049 = models.CharField(max_length=200, blank=True,null=True)
    p050 = models.CharField(max_length=200, blank=True,null=True)
    p051 = models.CharField(max_length=200, blank=True,null=True)
    p052 = models.CharField(max_length=200, blank=True,null=True)
    p053 = models.CharField(max_length=200, blank=True,null=True)
    p054 = models.CharField(max_length=500, blank=True,null=True)
    p055 = models.CharField(max_length=500, blank=True,null=True)
    p056 = models.CharField(max_length=500, blank=True,null=True)
    p057 = models.CharField(max_length=500, blank=True,null=True)
    p058 = models.CharField(max_length=500, blank=True,null=True)
    p059 = models.CharField(max_length=5000, blank=True,null=True)
    p060 = models.CharField(max_length=500, blank=True,null=True)
    p061 = models.CharField(max_length=2000, blank=True,null=True)
    p062 = models.CharField(max_length=500, blank=True,null=True)
    p063 = models.CharField(max_length=5000, blank=True,null=True)
    p064 = models.CharField(max_length=500, blank=True,null=True)
    p065 = models.CharField(max_length=5000, blank=True,null=True)
    p066 = models.CharField(max_length=500, blank=True,null=True)
    p067 = models.CharField(max_length=500, blank=True,null=True)
    p068 = models.CharField(max_length=500, blank=True,null=True)
    p069 = models.CharField(max_length=500, blank=True,null=True)
    p070 = models.CharField(max_length=500, blank=True,null=True)
    p071 = models.CharField(max_length=500, blank=True,null=True)
    p072 = models.CharField(max_length=500, blank=True,null=True)
    p073 = models.CharField(max_length=500, blank=True,null=True)
    p074 = models.CharField(max_length=500, blank=True,null=True)
    p075 = models.CharField(max_length=500, blank=True,null=True)
    p076 = models.CharField(max_length=2000, blank=True,null=True)
    p077 = models.CharField(max_length=500, blank=True,null=True)
    p078 = models.CharField(max_length=500, blank=True,null=True)
    p079 = models.CharField(max_length=500, blank=True,null=True)
    p080 = models.CharField(max_length=2000, blank=True,null=True)
    p081 = models.CharField(max_length=500, blank=True,null=True)
    p082 = models.CharField(max_length=500, blank=True,null=True)
    p083 = models.CharField(max_length=2000, blank=True,null=True)
    p084 = models.CharField(max_length=500, blank=True,null=True)
    p085 = models.CharField(max_length=2000, blank=True,null=True)
    p086 = models.CharField(max_length=500, blank=True,null=True)
    p087 = models.CharField(max_length=2000, blank=True,null=True)
    p088 = models.CharField(max_length=2000, blank=True,null=True)
    p089 = models.CharField(max_length=2000, blank=True,null=True)
    p090 = models.CharField(max_length=2000, blank=True,null=True)
    p091 = models.CharField(max_length=2000, blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'proveedores\".\"carga_respuestas_prod_serv_varios'





class carga_respuestas(models.Model):
    #codigo_id = models.ForeignKey('proveedor', on_delete = models.DO_NOTHING,blank=True)
    p001 = models.CharField(max_length=100, blank=True,null=True) # Marca Temporal
    p002 = models.CharField(max_length=20, blank=True,null=True) # Puntuación
    p003 = models.CharField(max_length=20, blank=True,null=True) #Fecha Elaborción cuestionario
    p004 = models.CharField(max_length=100, blank=True,null=True) #Declaración haber recibido Código de Etica
    p005 = models.CharField(max_length=2, blank=True,null=True) # Licitud de Fondos
    p006 = models.CharField(max_length=2, blank=True,null=True) #Certificación información veridica
    p007 = models.CharField(max_length=100, blank=True,null=True) #Nombre Empresa
    p008 = models.CharField(max_length=300, blank=True,null=True) #Direccion Oficina
    p009 = models.CharField(max_length=200, blank=True,null=True) #Horario Trabajo
    p010 = models.CharField(max_length=200, blank=True,null=True) #Rep. Legal
    p011 = models.CharField(max_length=13, blank=True,null=True) # N° Cedula o RUC
    p012 = models.CharField(max_length=100, blank=True,null=True) #Nombre persona se contacta con Ecofroz
    p013 = models.CharField(max_length=20, blank=True,null=True) #Teléfono fijo
    p014 = models.CharField(max_length=20, blank=True,null=True) #Celular Contacto
    p015 = models.CharField(max_length=200, blank=True,null=True) #Carta de presentación
    p016 = models.CharField(max_length=500,blank=True, null=True) #Giro de negocio
    p017 = models.CharField(max_length=100,blank=True, null=True) #Monto Ventas 2018
    p018 = models.CharField(max_length=100,blank=True, null=True) #Monto Ventas 2019
    p019 =  models.IntegerField(blank=True, null=True) #Años en el mercado antiguedad
    p020 = models.IntegerField(blank=True, null=True) #N° trabajadores Fijos
    p021 = models.IntegerField(blank=True, null=True) #N° de clientes
    p022 = models.IntegerField(blank=True, null=True) #N° de proveedores
    p023 = models.CharField(max_length=1000, blank=True, null=True) #3 Valores
    p024 = models.CharField(max_length=5, blank=True,null=True) #Tiene pagina Web
    p025 = models.CharField(max_length=100, blank=True,null=True) #Direccion Web
    p026 = models.CharField(max_length=100, blank=True,null=True) #Actividad
    p027 = models.CharField(max_length=50, blank=True,null=True) #Persona natural o juridica
    p028 = models.CharField(max_length=100, blank=True,null=True) #Tiene RUC actualizado
    p029 = models.CharField(max_length=100, blank=True,null=True) #Referencia Bancaria
    p030 = models.CharField(max_length=100, blank=True,null=True) #Certificado cumplimiento obligaciones IESS
    p031 = models.CharField(max_length=100, blank=True,null=True) #Envie la factura de servicio basico
    p032 = models.CharField(max_length=100, blank=True,null=True) #Envie las referencias de proveedores y clientes
    p033 = models.CharField(max_length=100, blank=True,null=True) #tiene RUC actualizado
    p034 = models.CharField(max_length=100, blank=True,null=True) #tiene el nombramiento de representante legal
    p035 = models.CharField(max_length=100, blank=True,null=True) #tiene referencia bancaria actualizada
    p036 = models.CharField(max_length=100, blank=True,null=True) #envió el certificado de cumplimiento de obligaciones con el IESS
    p037 = models.CharField(max_length=20, blank=True,null=True) #Fecha de aprobación de estatutos
    p038 = models.CharField(max_length=100, blank=True,null=True) #envie la copia de factura de servicios basicos
    p039 = models.CharField(max_length=100, blank=True,null=True) #envió las referencias de proveedores y clientes
    p040 = models.CharField(max_length=100, blank=True,null=True) #nomina de accionistas
    p041 = models.CharField(max_length=20, blank=True,null=True) #cambio accionario mayor al 50%
    p042 = models.CharField(max_length=100, blank=True,null=True) #N° de años que ha sido proveedor de Ecofroz
    p043 = models.CharField(max_length=100, blank=True,null=True) #Monto (USD) de ventas totales de productos y/o servicios a ECOFROZ S.A en el 2018
    p044 = models.CharField(max_length=100, blank=True,null=True) #Monto (USD) de ventas de productos y/o servicios a ECOFROZ S.A. en el 2019
    p045 = models.CharField(max_length=2, blank=True,null=True) #¿Subcontrata alguna actividad importante para el producto/servicio que ofrece?
    p046 = models.CharField(max_length=100, blank=True,null=True) #En caso de que la respuesta a la pregunta anterior sea "SI", indique la/s actividades sub contratadas, y si es "NO" escriba NO APLICA
    p047 = models.CharField(max_length=2, blank=True,null=True) #El canal de consulta y/o ayuda y/o denuncia que usted tuviere en cualquier instancia de su relación con Ecofroz S.A., es vía correo electrónico a la siguiente dirección: gerencia.administrativa@ecofroz.com o pborja@ecofroz.com.  Confirma usted que esta informado de como canalizar sus consultas quejas y/ denuncias ?
    p048 = models.CharField(max_length=100, blank=True,null=True) #¿De las siguientes categorías de producto/servicio,  a cuál corresponde su empresa? 
    p049 = models.CharField(max_length=40, blank=True,null=True) # ¿ Tiene el certificado de migración ? Envíe una copia 
    p050 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene la aceptación de las especificaciones de Ecofroz S.A? Envíe una copia 
    p051 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene las especificación del material de empaque (vigencia 1 año)? Envíe una copia 
    p052 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene las aprobaciones de contacto con los alimentos (materia prima)? Envíe una copia 
    p053 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene certificación de seguridad BASC? Envíe una copia 
    p054 = models.CharField(max_length=40, blank=True,null=True) #En caso de que NO tenga certificación BASC. ¿Tiene homologación y/o Ecofroz ha realizado una auditoria a su empresa? 
    p055 = models.CharField(max_length=40, blank=True,null=True) #Confirmo envío de certificación BASC u homologación o Auditoria de Ecofroz por:
    p056 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene certificado de homologación GFSI?
    p057 = models.CharField(max_length=40, blank=True,null=True) #En caso de no tener certificado de homologación GFSI, tiene certificado de auditoria actualizada de Ecofroz? 
    p058 = models.CharField(max_length=40, blank=True,null=True) #En caso de tener certificado GFSI o de auditoria Ecofroz confirmo envío por:
    p059 = models.CharField(max_length=40, blank=True,null=True) #¿Entrega certificado de calidad por lote?
    p060 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene el certificado de que el transporte es exclusivo para este material? Envíe una copia 
    p061 = models.CharField(max_length=40, blank=True,null=True) #¿ Tiene el certificado de que el transporte debe llegar sellado a Ecofroz S.A? Envíe una copia 
    p062 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene el formato de información del contacto de emergencia debidamente completado? Envíe una copia 
    p063 = models.CharField(max_length=40, blank=True,null=True) #¿Tiene el contrato vigente firmado con Ecofroz S.A?
    p064 = models.CharField(max_length=40, blank=True,null=True)
    p065 = models.CharField(max_length=40, blank=True,null=True)
    p066 = models.CharField(max_length=40, blank=True,null=True)
    p067 = models.CharField(max_length=40, blank=True,null=True)
    p068 = models.CharField(max_length=40, blank=True,null=True)
    p069 = models.CharField(max_length=40, blank=True,null=True)
    p070 = models.CharField(max_length=40, blank=True,null=True)
    p071 = models.CharField(max_length=40, blank=True,null=True)
    p072 = models.CharField(max_length=40, blank=True,null=True)
    p073 = models.CharField(max_length=40, blank=True,null=True)
    p074 = models.CharField(max_length=40, blank=True,null=True)
    p075 = models.CharField(max_length=40, blank=True,null=True)
    p076 = models.CharField(max_length=40, blank=True,null=True)
    p077 = models.CharField(max_length=40, blank=True,null=True)
    p078 = models.CharField(max_length=40, blank=True,null=True)
    p079 = models.CharField(max_length=40, blank=True,null=True)
    p080 = models.CharField(max_length=40, blank=True,null=True)
    p081 = models.CharField(max_length=40, blank=True,null=True)
    p082 = models.CharField(max_length=40, blank=True,null=True)
    p083 = models.CharField(max_length=40, blank=True,null=True)
    p084 = models.CharField(max_length=40, blank=True,null=True)
    p085 = models.CharField(max_length=40, blank=True,null=True)
    p086 = models.CharField(max_length=40, blank=True,null=True)
    p087 = models.CharField(max_length=40, blank=True,null=True)
    p088 = models.CharField(max_length=40, blank=True,null=True)
    p089 = models.CharField(max_length=40, blank=True,null=True)
    p090 = models.CharField(max_length=40, blank=True,null=True)
    p091 = models.CharField(max_length=40, blank=True,null=True)
    p092 = models.CharField(max_length=40, blank=True,null=True)
    p093 = models.CharField(max_length=40, blank=True,null=True)
    p094 = models.CharField(max_length=40, blank=True,null=True)
    p095 = models.CharField(max_length=40, blank=True,null=True)
    p096 = models.CharField(max_length=40, blank=True,null=True)
    p097 = models.CharField(max_length=40, blank=True,null=True)
    p098 = models.CharField(max_length=40, blank=True,null=True)
    p099 = models.CharField(max_length=40, blank=True,null=True)
    p100 = models.CharField(max_length=40, blank=True,null=True)
    p101 = models.CharField(max_length=40, blank=True,null=True)
    p102 = models.CharField(max_length=40, blank=True,null=True)
    p103 = models.CharField(max_length=40, blank=True,null=True)
    p104 = models.CharField(max_length=40, blank=True,null=True)
    p105 = models.CharField(max_length=40, blank=True,null=True)
    p106 = models.CharField(max_length=40, blank=True,null=True)
    p107 = models.CharField(max_length=40, blank=True,null=True)
    p108 = models.CharField(max_length=40, blank=True,null=True)
    p109 = models.CharField(max_length=40, blank=True,null=True)
    p110 = models.CharField(max_length=40, blank=True,null=True)
    p111 = models.CharField(max_length=40, blank=True,null=True)
    p112 = models.CharField(max_length=40, blank=True,null=True)
    p113 = models.CharField(max_length=40, blank=True,null=True)
    p114 = models.CharField(max_length=40, blank=True,null=True)
    p115 = models.CharField(max_length=40, blank=True,null=True)
    p116 = models.CharField(max_length=40, blank=True,null=True)
    p117 = models.CharField(max_length=40, blank=True,null=True)
    p118 = models.CharField(max_length=40, blank=True,null=True)
    p119 = models.CharField(max_length=40, blank=True,null=True)
    p120 = models.CharField(max_length=40, blank=True,null=True)
    p121 = models.CharField(max_length=40, blank=True,null=True)
    p122 = models.CharField(max_length=40, blank=True,null=True)
    p123 = models.CharField(max_length=40, blank=True,null=True)
    p124 = models.CharField(max_length=40, blank=True,null=True)
    p125 = models.CharField(max_length=40, blank=True,null=True)
    p126 = models.CharField(max_length=40, blank=True,null=True)
    p127 = models.CharField(max_length=40, blank=True,null=True)
    p128 = models.CharField(max_length=40, blank=True,null=True)
    p129 = models.CharField(max_length=40, blank=True,null=True)
    p130 = models.CharField(max_length=40, blank=True,null=True)
    p131 = models.CharField(max_length=40, blank=True,null=True)
    p132 = models.CharField(max_length=40, blank=True,null=True)
    p133 = models.CharField(max_length=40, blank=True,null=True)
    p134 = models.CharField(max_length=40, blank=True,null=True)
    p135 = models.CharField(max_length=40, blank=True,null=True)
    p136 = models.CharField(max_length=40, blank=True,null=True)
    p137 = models.CharField(max_length=40, blank=True,null=True)
    p138 = models.CharField(max_length=40, blank=True,null=True)
    p139 = models.CharField(max_length=40, blank=True,null=True)
    p140 = models.CharField(max_length=40, blank=True,null=True)
    p141 = models.CharField(max_length=40, blank=True,null=True)
    p142 = models.CharField(max_length=40, blank=True,null=True)
    p143 = models.CharField(max_length=40, blank=True,null=True)
    p144 = models.CharField(max_length=40, blank=True,null=True)
    p145 = models.CharField(max_length=40, blank=True,null=True)
    p146 = models.CharField(max_length=40, blank=True,null=True)
    p147 = models.CharField(max_length=40, blank=True,null=True)
    p148 = models.CharField(max_length=40, blank=True,null=True)
    p149 = models.CharField(max_length=500, blank=True,null=True)
    p150 = models.CharField(max_length=40, blank=True,null=True)
    p151 = models.CharField(max_length=40, blank=True,null=True)
    p152 = models.CharField(max_length=40, blank=True,null=True)
    p153 = models.CharField(max_length=40, blank=True,null=True)
    p154 = models.CharField(max_length=40, blank=True,null=True)
    p155 = models.CharField(max_length=200, blank=True,null=True)
    p156 = models.CharField(max_length=40, blank=True,null=True)
    p157 = models.CharField(max_length=40, blank=True,null=True)
    p158 = models.CharField(max_length=40, blank=True,null=True)
    p159 = models.CharField(max_length=40, blank=True,null=True)
    p160 = models.CharField(max_length=40, blank=True,null=True)
    p161 = models.CharField(max_length=40, blank=True,null=True)
    p162 = models.CharField(max_length=40, blank=True,null=True)
    p163 = models.CharField(max_length=40, blank=True,null=True)
    p164 = models.CharField(max_length=40, blank=True,null=True)
    p165 = models.CharField(max_length=40, blank=True,null=True)
    p166 = models.CharField(max_length=40, blank=True,null=True)
    p167 = models.CharField(max_length=40, blank=True,null=True)
    p168 = models.CharField(max_length=40, blank=True,null=True)
    p169 = models.CharField(max_length=400, blank=True,null=True)
    p170 = models.CharField(max_length=40, blank=True,null=True)
    p171 = models.CharField(max_length=400, blank=True,null=True)
    p172 = models.CharField(max_length=40, blank=True,null=True)
    p173 = models.CharField(max_length=40, blank=True,null=True)
    p174 = models.CharField(max_length=400, blank=True,null=True)
    p175 = models.CharField(max_length=40, blank=True,null=True)
    p176 = models.CharField(max_length=40, blank=True,null=True)
    p177 = models.CharField(max_length=40, blank=True,null=True)
    p178 = models.CharField(max_length=500, blank=True,null=True)
    p179 = models.CharField(max_length=40, blank=True,null=True)
    p180 = models.CharField(max_length=40, blank=True,null=True)
    p181 = models.CharField(max_length=40, blank=True,null=True)
    p182 = models.CharField(max_length=40, blank=True,null=True)
    p183 = models.CharField(max_length=40, blank=True,null=True)
    p184 = models.CharField(max_length=40, blank=True,null=True)
    p185 = models.CharField(max_length=40, blank=True,null=True)
    p186 = models.CharField(max_length=40, blank=True,null=True)
    p187 = models.CharField(max_length=40, blank=True,null=True)
    p188 = models.CharField(max_length=40, blank=True,null=True)
    p189 = models.CharField(max_length=40, blank=True,null=True)
    p190 = models.CharField(max_length=40, blank=True,null=True)
    p191 = models.CharField(max_length=40, blank=True,null=True)
    p192 = models.CharField(max_length=40, blank=True,null=True)
    p193 = models.CharField(max_length=40, blank=True,null=True)
    p194 = models.CharField(max_length=400, blank=True,null=True)
    p195 = models.CharField(max_length=40, blank=True,null=True)
    p196 = models.CharField(max_length=40, blank=True,null=True)
    p197 = models.CharField(max_length=40, blank=True,null=True)
    p198 = models.CharField(max_length=1000, blank=True,null=True)
    p199 = models.CharField(max_length=40, blank=True,null=True)
    p200 = models.CharField(max_length=40, blank=True,null=True)
    p201 = models.CharField(max_length=1000, blank=True,null=True)
    p202 = models.CharField(max_length=40, blank=True,null=True)
    p203 = models.CharField(max_length=1000, blank=True,null=True)
    p204 = models.CharField(max_length=40, blank=True,null=True)
    p205 = models.CharField(max_length=1000, blank=True,null=True)
    p206 = models.CharField(max_length=2000, blank=True,null=True)
    p207 = models.CharField(max_length=2000, blank=True,null=True)
    p208 = models.CharField(max_length=2000, blank=True,null=True)
    p209 = models.CharField(max_length=2000, blank=True,null=True)
    p210 = models.CharField(max_length=2000, blank=True,null=True)
    p211 = models.CharField(max_length=2000, blank=True,null=True)
    p212 = models.CharField(max_length=2000, blank=True,null=True)
    p213 = models.CharField(max_length=2000, blank=True,null=True)
    p214 = models.CharField(max_length=2000, blank=True,null=True)
    p215 = models.CharField(max_length=2000, blank=True,null=True)
    p216 = models.CharField(max_length=2000, blank=True,null=True)
    p217 = models.CharField(max_length=40, blank=True,null=True)
    p218 = models.CharField(max_length=40, blank=True,null=True)
    p219 = models.CharField(max_length=40, blank=True,null=True)



    class Meta:
        managed = True
        db_table = 'proveedores\".\"carga_respuestas'
    


class proveedor_actividad(models.Model):
    nombre_actividad = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_actividad'

    def __str__(self):
       return str(self.nombre_actividad)

class proveedor_categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100,blank=True, null=True)
    nombre_plantilla_detalle = models.CharField(max_length=500,blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_categoria'

    def __str__(self):
       return str(self.nombre_categoria)

class proveedor_segmento(models.Model):
    nombre_segmento = models.CharField(max_length=100,blank=True, null=True)
  
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_segmento'

    def __str__(self):
       return str(self.nombre_segmento)



seccion = {
    (1,'Fecha de elaboración'),
    (2,'Codigo de Etica'),
    (3,'Licitud de Fondos'),
    (4,'Veracidad de las respuestas'),
    (5,'Información General'),
    (6,'Existencia y Legalidad'),
    (7,'Requisitos persona Natural'),
    (8,'Requisitos Persona Juridica'),
    (9,'Información de la relacion comercial con Ecofroz'),
    (10,'Fundas/Rollos'),
    (11,'Control de Plagas'),
    (12,'Centros de acopio'),
    (13,'Quimicos de limpieza (Detergentes)'),
    (14,'Quimicos de limpieza (Desinfectantes)'),
    (15,'Cajas'),
    (16,'Catering'),
    (17,'Laboratorios de Analisis'),
    (18,'Materiales de laboratorio (insumos)'),
    (19,'Laboratorios de calibracion'),
    (20,'Gestores ambientales de desechos'),
    (21,'Materia Prima'),
    (22,'Quimicos para el caldero'),
    (23,'Grados de grado alimenticio'),
    (24,'Transporte de contenedores'),
    (25,'Transporte maritimo (navieras)'),
    (26,'Korex - Sleep Shipt'),
    (27,'Transporte'),
    (28,'Buenas practicas de calidad'),
    (29,'Buenas practicas de seguridad'),
    (30,'Buenas practicas ambientales'),
    (31,'Buenas prracticas de  responsabilidad social'),
    (32,'Buenas practicas laborales'),
    (33,'Buenas practicas con proveedores y clientes'),
    (34,'Retroalimentacion Ecofroz'),
}

class proveedor_encuesta(models.Model):
    pregunta = models.CharField(max_length=2000,blank=True, null=True)
    pregunta_nombre_corto = models.CharField(max_length=2000,blank=True, null=True)
    seccion = models.CharField(max_length=200, blank=True,null=True,choices=seccion)
    segmento = models.ForeignKey('proveedor_segmento', models.DO_NOTHING,blank=True,null=True)
    pregunta_campo_modelo_id = models.CharField(max_length=1000, blank=True,null=True)
    categoria_proveedor = models.ForeignKey('proveedor_categoria', models.DO_NOTHING,blank=True,null=True)
    codigo_id = models.ForeignKey('proveedor', on_delete = models.CASCADE, blank=True,null=True)
    segundo_ordenamiento =  models.CharField(max_length=10, blank=True,null=True)
    puntaje_pregunta_especifica = models.IntegerField(blank=True,null=True)
    puntaje_pregunta_especifica_constructores = models.IntegerField(blank=True,null=True)


    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta'

    def __str__(self):
       return str(self.pregunta)

#NO UTILIZAR ###################
class proveedor_encuesta_prod_serv_agricola(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_prod_serv_agricola'
###############################

class proveedor_encuesta_prod_serv_varios(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_prod_serv_varios'

class proveedor_encuesta_control_plagas(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_control_plagas'

class proveedor_encuesta_fundas_rollos(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_fundas_rollos'


class proveedor_encuesta_quimicos_caldero(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_quimicos_caldero'

class proveedor_encuesta_transporte_otros(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_transporte_otros'

class proveedor_encuesta_prod_agricolas(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_prod_agricolas'

class proveedor_encuesta_laboratorio_insumos(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_laboratorio_insumos'

class proveedor_encuesta_constructores(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_constructores'

class proveedor_encuesta_laboratorio_analisis(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_laboratorio_analisis'

class proveedor_encuesta_gestores_desechos(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_gestores_desechos'

class proveedor_encuesta_quimicos_desinfectantes(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_quimicos_desinfectantes'

class proveedor_encuesta_cajas(models.Model):
    pregunta_id = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    ordenamiento = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True  
        db_table = 'proveedores\".\"proveedor_encuesta_cajas'


class proveedor_respuestas(models.Model):
    respuesta = models.CharField(max_length=5000,blank=True, null=True)
    pregunta = models.ForeignKey('proveedor_encuesta', on_delete = models.DO_NOTHING, blank=True,null=True)
    proveedor_id = models.ForeignKey('proveedor', on_delete = models.CASCADE, blank=True,null=True)
    categoria = models.ForeignKey('proveedor_categoria', on_delete = models.DO_NOTHING, blank=True,null=True)
    calificacion = models.IntegerField(blank=True, null=True,default=0)
    documento = models.ForeignKey('proveedor_documentos', on_delete = models.DO_NOTHING, blank=True,null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_respuestas'

    def __str__(self):
       return str(self.respuesta)


class proveedor_documentos(models.Model):
    proveedor = models.ForeignKey('proveedor', on_delete = models.DO_NOTHING, blank=True,null=True)
    categoria = models.ForeignKey('proveedor_categoria', on_delete = models.DO_NOTHING, blank=True,null=True)
    sub_categoria = models.IntegerField(blank=True, null=True)
    nombre_documento = models.CharField(max_length=300,blank=True, null=True)
    empresa_tipo = models.CharField(max_length=100, blank=True,null=True,choices=empresa_tipo)
    completo = models.BooleanField(blank=True,null=True)
    
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_documentos'

    def __str__(self):
       return str(self.nombre_documento)




class proveedor_fichas(models.Model):
    proveedor = models.ForeignKey('proveedor', on_delete = models.DO_NOTHING, blank=True,null=True)
    categoria = models.ForeignKey('proveedor_categoria', on_delete = models.DO_NOTHING, blank=True,null=True)
    nombre_ficha = models.CharField(max_length=300,blank=True, null=True)
    empresa_tipo = models.CharField(max_length=100, blank=True,null=True,choices=empresa_tipo)
    revisado = models.BooleanField(blank=True,null=True)
    persona_revisa = models.CharField(max_length=50,blank=True, null=True)
    observaciones = models.CharField(max_length=3000,blank=True, null=True)
    subcategoria =  models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_fichas'

    def __str__(self):
       return str(self.nombre_ficha)

class proveedor_hojas_msds(models.Model):
    proveedor = models.ForeignKey('proveedor', on_delete = models.DO_NOTHING, blank=True,null=True)
    categoria = models.ForeignKey('proveedor_categoria', on_delete = models.DO_NOTHING, blank=True,null=True)
    nombre_hoja_msds = models.CharField(max_length=300,blank=True, null=True)
    empresa_tipo = models.CharField(max_length=100, blank=True,null=True,choices=empresa_tipo)
    revisado = models.BooleanField(blank=True,null=True)
    persona_revisa = models.CharField(max_length=50,blank=True, null=True)
    observaciones = models.CharField(max_length=3000,blank=True, null=True)
    subcategoria =  models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_hojas_msds'

    def __str__(self):
       return str(self.nombre_hoja_msds)

class proveedor_etiquetas_productos(models.Model):
    proveedor = models.ForeignKey('proveedor', on_delete = models.DO_NOTHING, blank=True,null=True)
    categoria = models.ForeignKey('proveedor_categoria', on_delete = models.DO_NOTHING, blank=True,null=True)
    nombre_etiqueta_producto = models.CharField(max_length=300,blank=True, null=True)
    empresa_tipo = models.CharField(max_length=100, blank=True,null=True,choices=empresa_tipo)
    revisado = models.BooleanField(blank=True,null=True)
    persona_revisa = models.CharField(max_length=50,blank=True, null=True)
    observaciones = models.CharField(max_length=3000,blank=True, null=True)
    subcategoria =  models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_etiquetas_productos'

    def __str__(self):
       return str(self.nombre_etiqueta_producto)

class proveedor_estados_select(models.Model):
    codigo  = models.ForeignKey('proveedor', models.DO_NOTHING,blank=True, null=True)
    docu =  models.CharField(max_length=300, blank=True, null=True)
    tdocu = models.BooleanField(blank=True,null=True)
    fecini = models.DateField(blank=True,null=True)
    fecfin = models.DateField(blank=True,null=True)
    
    class Meta:
        managed = True
        db_table = 'proveedores\".\"proveedor_estados_select'