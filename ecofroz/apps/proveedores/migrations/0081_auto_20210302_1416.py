# Generated by Django 3.0 on 2021-03-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0080_auto_20210302_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_documentos',
            name='ficha',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(6, 'Conocer el orígen de las materias primas'), (7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(6, 'Conocer el orígen de las materias primas'), (7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_documentos',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(25, 'Transporte maritimo (navieras)'), (5, 'Información General'), (3, 'Licitud de Fondos'), (4, 'Veracidad de las respuestas'), (9, 'Información de la relacion comercial con Ecofroz'), (32, 'Buenas practicas laborales'), (17, 'Laboratorios de Analisis'), (14, 'Quimicos de limpieza (Desinfectantes)'), (26, 'Korex - Sleep Shipt'), (34, 'Retroalimentacion Ecofroz'), (8, 'Requisitos Persona Juridica'), (13, 'Quimicos de limpieza (Detergentes)'), (19, 'Laboratorios de calibracion'), (12, 'Centros de acopio'), (29, 'Buenas practicas de seguridad'), (21, 'Materia Prima'), (22, 'Quimicos para el caldero'), (6, 'Existencia y Legalidad'), (24, 'Transporte de contenedores'), (20, 'Gestores ambientales de desechos'), (1, 'Fecha de elaboración'), (30, 'Buenas practicas ambientales'), (16, 'Catering'), (23, 'Grados de grado alimenticio'), (2, 'Codigo de Etica'), (33, 'Buenas practicas con proveedores y clientes'), (7, 'Requisitos persona Natural'), (27, 'Transporte'), (15, 'Cajas'), (28, 'Buenas practicas de calidad'), (10, 'Fundas/Rollos'), (31, 'Buenas prracticas de  responsabilidad social'), (11, 'Control de Plagas'), (18, 'Materiales de laboratorio (insumos)')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_fichas',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=100, null=True),
        ),
    ]
