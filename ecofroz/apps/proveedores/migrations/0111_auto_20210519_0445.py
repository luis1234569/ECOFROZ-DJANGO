# Generated by Django 3.0.8 on 2021-05-19 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0110_auto_20210518_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproveedor_det',
            name='observaciones_administrativas',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='observaciones_administrativas',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (6, 'Conocer el orígen de las materias primas'), (3, 'Análisis de metales pesados'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (7, 'No soy proveedor de fertilizantes'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de MATERIA ORGANICA'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de pesticidas'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (6, 'Conocer el orígen de las materias primas'), (3, 'Análisis de metales pesados'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (7, 'No soy proveedor de fertilizantes'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de MATERIA ORGANICA'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de pesticidas'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(5, 'Información General'), (3, 'Licitud de Fondos'), (12, 'Centros de acopio'), (17, 'Laboratorios de Analisis'), (6, 'Existencia y Legalidad'), (25, 'Transporte maritimo (navieras)'), (13, 'Quimicos de limpieza (Detergentes)'), (31, 'Buenas prracticas de  responsabilidad social'), (34, 'Retroalimentacion Ecofroz'), (4, 'Veracidad de las respuestas'), (28, 'Buenas practicas de calidad'), (26, 'Korex - Sleep Shipt'), (32, 'Buenas practicas laborales'), (24, 'Transporte de contenedores'), (9, 'Información de la relacion comercial con Ecofroz'), (30, 'Buenas practicas ambientales'), (16, 'Catering'), (33, 'Buenas practicas con proveedores y clientes'), (19, 'Laboratorios de calibracion'), (1, 'Fecha de elaboración'), (27, 'Transporte'), (15, 'Cajas'), (22, 'Quimicos para el caldero'), (11, 'Control de Plagas'), (21, 'Materia Prima'), (8, 'Requisitos Persona Juridica'), (2, 'Codigo de Etica'), (10, 'Fundas/Rollos'), (23, 'Grados de grado alimenticio'), (29, 'Buenas practicas de seguridad'), (20, 'Gestores ambientales de desechos'), (7, 'Requisitos persona Natural'), (14, 'Quimicos de limpieza (Desinfectantes)'), (18, 'Materiales de laboratorio (insumos)')], max_length=200, null=True),
        ),
    ]
