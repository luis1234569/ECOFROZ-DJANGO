# Generated by Django 3.0.8 on 2021-09-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0142_auto_20210924_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentos_prove',
            name='fecha_documento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='documentos_prove',
            name='marca_cal',
            field=models.CharField(blank=True, choices=[('CORRECTA', 'CORECTA'), ('DESACTUALIZADA', 'DESACTUALIZADA'), ('INCORRECTA', 'INCORRECTA')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (3, 'Análisis de metales pesados'), (7, 'No soy proveedor de fertilizantes')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de pesticidas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (3, 'Análisis de metales pesados'), (7, 'No soy proveedor de fertilizantes')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de pesticidas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_documentos',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(24, 'Transporte de contenedores'), (16, 'Catering'), (17, 'Laboratorios de Analisis'), (1, 'Fecha de elaboración'), (9, 'Información de la relacion comercial con Ecofroz'), (14, 'Quimicos de limpieza (Desinfectantes)'), (10, 'Fundas/Rollos'), (13, 'Quimicos de limpieza (Detergentes)'), (33, 'Buenas practicas con proveedores y clientes'), (5, 'Información General'), (12, 'Centros de acopio'), (26, 'Korex - Sleep Shipt'), (27, 'Transporte'), (20, 'Gestores ambientales de desechos'), (34, 'Retroalimentacion Ecofroz'), (31, 'Buenas prracticas de  responsabilidad social'), (22, 'Quimicos para el caldero'), (7, 'Requisitos persona Natural'), (32, 'Buenas practicas laborales'), (30, 'Buenas practicas ambientales'), (28, 'Buenas practicas de calidad'), (15, 'Cajas'), (18, 'Materiales de laboratorio (insumos)'), (8, 'Requisitos Persona Juridica'), (4, 'Veracidad de las respuestas'), (3, 'Licitud de Fondos'), (21, 'Materia Prima'), (25, 'Transporte maritimo (navieras)'), (19, 'Laboratorios de calibracion'), (6, 'Existencia y Legalidad'), (23, 'Grados de grado alimenticio'), (29, 'Buenas practicas de seguridad'), (11, 'Control de Plagas'), (2, 'Codigo de Etica')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_etiquetas_productos',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_fichas',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_hojas_msds',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=100, null=True),
        ),
    ]
