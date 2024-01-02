# Generated by Django 3.0 on 2020-08-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0058_auto_20200824_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='control',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='antecedentes_verificados_rep_legal',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='capacita_usuarios_prevencion_accidentes',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='conoce_proceso_pago',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='conoce_proceso_recepcion',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='contrato_vigente_ecofroz',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='cumple_procedimiento_compra',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='cumple_procedimiento_entrega',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='cumple_procedimiento_facturacion',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='cumplimiento_proceso_pago',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='ecofroz_explico_proceso_compra',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_atendido_bien',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='especificaciones_oportunas_claras',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='giro_negocio_igual',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='hace_mantenimiento_preventivo',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='hace_respaldos_periodicos_informacion_empresa',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='optimiza_uso_recursos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='prioriza_contratacion_personal_zona',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proceso_compra_agil',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (6, 'Conocer el orígen de las materias primas'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (3, 'Análisis de metales pesados'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (5, 'No soy proveedor de pesticidas'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='realiza_simulacro_emergencia',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='requiere_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='subcontrata',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_activos_asegurados',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_afiliacion_empleados_iess',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_analisis_composicion_concentraciones',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_analisis_cumplimiento_fda_173310',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_aprobaciones_contacto_alimentos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_carta_garantia',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificacion_basc',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificacion_gfsi_o_bpm',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_aecpu',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_arcsa',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_auditoria_ecofroz_por_no_gfsi',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_buenas_practicas_manufactura',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_calidad_por_lote',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_calidad_producto',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_destruccion_material_x_carga',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_fabricacion_libre_alergenicos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_insumos_aoac',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_iso_17025',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_iso_21469',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_logistica_producto',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_migracion_fundas',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_mip_personal',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_nfs_h1_h2',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_npma',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_patrones_trazables_baja_incertidumbre',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_tiempo_analisis',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_transporte_exclusivo',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_transporte_sellado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_validaciones_reduccion_logaritmica',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_cobertura_seguro_ocupantes_vehiculos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_cobertura_seguro_vehiculos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_codigo_conducta',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_documento_aceptacion_especificaciones_ecofroz',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_documentos_habilitantes_vehiculos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_especificacion_material_empaque',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_especificaciones_fichas_tecnicas',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ficha_tecnica_hoja_seguridad_registro_sanitario',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_seleccion_materia_prima',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_homologacion_auditoria_basc_ecofroz',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_homologacion_gfsi',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_licencia_unica_funcionamiento_luae',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_lista_choferes_autorizados',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_matricula_vehiculo_actualizada',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_mecanismo_discrimen',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_mecanismo_satisfaccion_cliente',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_permiso_funcionamiento',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_permiso_operacion_transporte',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_plan_continuidad_negocio',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_plan_respuesta_riesgos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_politica_inclusion_social',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_politica_prevencion_actos_acoso',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_politica_prevencion_actos_corrupcion',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_politica_proteccion_ambiente',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_politica_responsabilidad_social',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_poliza_responsabilidad_civil',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_practicas_no_discriminacion_laboral',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_procedimientos_ventas_no_conformes',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_procesos_mejora_continua',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_programa_auditoria_interna',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_programa_manejo_desechos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_reglamento_interno_seguridad_salud_laboral',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_reglamento_interno_trabajo',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_reporte_inspeccion_permiso_funcionamiento',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_seguimiento_medico_trabajadores',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_seguro_ocupantes_vehiculo',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_sistema_calidad_iso9001',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_sistema_comunicacion_transmision_datos',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_sistema_evaluacion_seleccion_proveedores',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_sistema_seguridad_logistica_transporte',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tieneweb',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='trabajadores_menores_16anios',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='utiliza_transporte_propio',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='vehiculos_estan_asegurados',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(14, 'Quimicos de limpieza (Desinfectantes)'), (27, 'Transporte'), (30, 'Buenas practicas ambientales'), (8, 'Requisitos Persona Juridica'), (5, 'Información General'), (10, 'Fundas/Rollos'), (29, 'Buenas practicas de seguridad'), (2, 'Codigo de Etica'), (32, 'Buenas practicas laborales'), (16, 'Catering'), (26, 'Korex - Sleep Shipt'), (31, 'Buenas prracticas de  responsabilidad social'), (7, 'Requisitos persona Natural'), (25, 'Transporte maritimo (navieras)'), (1, 'Fecha de elaboración'), (4, 'Veracidad de las respuestas'), (11, 'Control de Plagas'), (34, 'Retroalimentacion Ecofroz'), (17, 'Laboratorios de Analisis'), (28, 'Buenas practicas de calidad'), (13, 'Quimicos de limpieza (Detergentes)'), (20, 'Gestores ambientales de desechos'), (33, 'Buenas practicas con proveedores y clientes'), (12, 'Centros de acopio'), (9, 'Información de la relacion comercial con Ecofroz'), (18, 'Materiales de laboratorio (insumos)'), (23, 'Grados de grado alimenticio'), (21, 'Materia Prima'), (24, 'Transporte de contenedores'), (19, 'Laboratorios de calibracion'), (6, 'Existencia y Legalidad'), (22, 'Quimicos para el caldero'), (3, 'Licitud de Fondos'), (15, 'Cajas')], max_length=200, null=True),
        ),
    ]
