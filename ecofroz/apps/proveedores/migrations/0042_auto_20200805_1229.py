# Generated by Django 3.0 on 2020-08-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0041_auto_20200803_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='carga_respuestas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p001', models.CharField(blank=True, max_length=100, null=True)),
                ('p002', models.CharField(blank=True, max_length=20, null=True)),
                ('p003', models.DateTimeField(blank=True, null=True)),
                ('p004', models.CharField(blank=True, max_length=100, null=True)),
                ('p005', models.CharField(blank=True, max_length=2, null=True)),
                ('p006', models.CharField(blank=True, max_length=2, null=True)),
                ('p007', models.CharField(blank=True, max_length=100, null=True)),
                ('p008', models.CharField(blank=True, max_length=300, null=True)),
                ('p009', models.CharField(blank=True, max_length=200, null=True)),
                ('p010', models.CharField(blank=True, max_length=200, null=True)),
                ('p011', models.CharField(blank=True, max_length=13, null=True)),
                ('p012', models.CharField(blank=True, max_length=100, null=True)),
                ('p013', models.CharField(blank=True, max_length=20, null=True)),
                ('p014', models.CharField(blank=True, max_length=20, null=True)),
                ('p015', models.CharField(blank=True, max_length=200, null=True)),
                ('p016', models.CharField(blank=True, max_length=500, null=True)),
                ('p017', models.CharField(blank=True, max_length=100, null=True)),
                ('p018', models.CharField(blank=True, max_length=100, null=True)),
                ('p019', models.IntegerField(blank=True, null=True)),
                ('p020', models.IntegerField(blank=True, null=True)),
                ('p021', models.IntegerField(blank=True, null=True)),
                ('p022', models.IntegerField(blank=True, null=True)),
                ('p023', models.CharField(blank=True, max_length=500, null=True)),
                ('p024', models.CharField(blank=True, max_length=5, null=True)),
                ('p025', models.CharField(blank=True, max_length=100, null=True)),
                ('p026', models.CharField(blank=True, max_length=100, null=True)),
                ('p027', models.CharField(blank=True, max_length=50, null=True)),
                ('p028', models.CharField(blank=True, max_length=50, null=True)),
                ('p029', models.CharField(blank=True, max_length=50, null=True)),
                ('p030', models.CharField(blank=True, max_length=50, null=True)),
                ('p031', models.CharField(blank=True, max_length=50, null=True)),
                ('p032', models.CharField(blank=True, max_length=50, null=True)),
                ('p033', models.CharField(blank=True, max_length=50, null=True)),
                ('p034', models.CharField(blank=True, max_length=50, null=True)),
                ('p035', models.CharField(blank=True, max_length=50, null=True)),
                ('p036', models.CharField(blank=True, max_length=50, null=True)),
                ('p037', models.DateTimeField(blank=True, null=True)),
                ('p038', models.CharField(blank=True, max_length=50, null=True)),
                ('p039', models.CharField(blank=True, max_length=50, null=True)),
                ('p040', models.CharField(blank=True, max_length=50, null=True)),
                ('p041', models.CharField(blank=True, max_length=20, null=True)),
                ('p042', models.CharField(blank=True, max_length=50, null=True)),
                ('p043', models.CharField(blank=True, max_length=50, null=True)),
                ('p044', models.CharField(blank=True, max_length=50, null=True)),
                ('p045', models.CharField(blank=True, max_length=2, null=True)),
                ('p046', models.CharField(blank=True, max_length=50, null=True)),
                ('p047', models.CharField(blank=True, max_length=2, null=True)),
                ('p048', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'proveedores"."carga_respuestas',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (7, 'No soy proveedor de fertilizantes'), (6, 'Conocer el orígen de las materias primas'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de FOLIARES'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (5, 'No soy proveedor de pesticidas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(9, 'Información de la relacion comercial con Ecofroz'), (24, 'Transporte de contenedores'), (10, 'Fundas/Rollos'), (2, 'Codigo de Etica'), (29, 'Buenas practicas de seguridad'), (3, 'Licitud de Fondos'), (23, 'Grados de grado alimenticio'), (7, 'Requisitos persona Natural'), (12, 'Centros de acopio'), (30, 'Buenas practicas ambientales'), (20, 'Gestores ambientales de desechos'), (11, 'Control de Plagas'), (4, 'Veracidad de las respuestas'), (31, 'Buenas prracticas de  responsabilidad social'), (8, 'Requisitos Persona Juridica'), (1, 'Fecha de elaboración'), (34, 'Retroalimentacion Ecofroz'), (25, 'Transporte maritimo (navieras)'), (5, 'Información General'), (14, 'Quimicos de limpieza (Desinfectantes)'), (6, 'Existencia y Legalidad'), (17, 'Laboratorios de Analisis'), (33, 'Buenas practicas con proveedores y clientes'), (21, 'Materia Prima'), (22, 'Quimicos para el caldero'), (13, 'Quimicos de limpieza (Detergentes)'), (28, 'Buenas practicas de calidad'), (32, 'Buenas practicas laborales'), (26, 'Korex - Sleep Shipt'), (27, 'Transporte'), (18, 'Materiales de laboratorio (insumos)'), (16, 'Catering'), (19, 'Laboratorios de calibracion'), (15, 'Cajas')], max_length=200, null=True),
        ),
    ]
