# Generated by Django 3.0.8 on 2021-05-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0102_auto_20210514_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor_fichas',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='proveedor_fichas',
            name='es_ficha',
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='proveedor_critico',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='proveedor_revisado',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de MATERIA ORGANICA'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (1, 'Registro de los productos en Agrocalidad o Magar'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor_critico',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor_revisado',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de MATERIA ORGANICA'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (1, 'Registro de los productos en Agrocalidad o Magar'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(12, 'Centros de acopio'), (15, 'Cajas'), (10, 'Fundas/Rollos'), (18, 'Materiales de laboratorio (insumos)'), (25, 'Transporte maritimo (navieras)'), (29, 'Buenas practicas de seguridad'), (28, 'Buenas practicas de calidad'), (8, 'Requisitos Persona Juridica'), (26, 'Korex - Sleep Shipt'), (4, 'Veracidad de las respuestas'), (33, 'Buenas practicas con proveedores y clientes'), (24, 'Transporte de contenedores'), (17, 'Laboratorios de Analisis'), (5, 'Información General'), (31, 'Buenas prracticas de  responsabilidad social'), (23, 'Grados de grado alimenticio'), (2, 'Codigo de Etica'), (3, 'Licitud de Fondos'), (7, 'Requisitos persona Natural'), (14, 'Quimicos de limpieza (Desinfectantes)'), (13, 'Quimicos de limpieza (Detergentes)'), (27, 'Transporte'), (21, 'Materia Prima'), (32, 'Buenas practicas laborales'), (16, 'Catering'), (9, 'Información de la relacion comercial con Ecofroz'), (1, 'Fecha de elaboración'), (30, 'Buenas practicas ambientales'), (34, 'Retroalimentacion Ecofroz'), (20, 'Gestores ambientales de desechos'), (22, 'Quimicos para el caldero'), (6, 'Existencia y Legalidad'), (11, 'Control de Plagas'), (19, 'Laboratorios de calibracion')], max_length=200, null=True),
        ),
    ]
