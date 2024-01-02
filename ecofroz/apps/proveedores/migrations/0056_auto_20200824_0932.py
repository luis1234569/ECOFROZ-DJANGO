# Generated by Django 3.0.7 on 2020-08-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0055_auto_20200824_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('INACTIVO', 'INACTIVO'), ('ACTIVO', 'ACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis de metales pesados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de MATERIA ORGANICA'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (5, 'No soy proveedor de pesticidas'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(15, 'Cajas'), (33, 'Buenas practicas con proveedores y clientes'), (7, 'Requisitos persona Natural'), (8, 'Requisitos Persona Juridica'), (3, 'Licitud de Fondos'), (28, 'Buenas practicas de calidad'), (12, 'Centros de acopio'), (9, 'Información de la relacion comercial con Ecofroz'), (21, 'Materia Prima'), (22, 'Quimicos para el caldero'), (16, 'Catering'), (23, 'Grados de grado alimenticio'), (24, 'Transporte de contenedores'), (27, 'Transporte'), (6, 'Existencia y Legalidad'), (2, 'Codigo de Etica'), (5, 'Información General'), (14, 'Quimicos de limpieza (Desinfectantes)'), (30, 'Buenas practicas ambientales'), (4, 'Veracidad de las respuestas'), (25, 'Transporte maritimo (navieras)'), (18, 'Materiales de laboratorio (insumos)'), (32, 'Buenas practicas laborales'), (20, 'Gestores ambientales de desechos'), (11, 'Control de Plagas'), (10, 'Fundas/Rollos'), (1, 'Fecha de elaboración'), (29, 'Buenas practicas de seguridad'), (13, 'Quimicos de limpieza (Detergentes)'), (26, 'Korex - Sleep Shipt'), (17, 'Laboratorios de Analisis'), (34, 'Retroalimentacion Ecofroz'), (31, 'Buenas prracticas de  responsabilidad social'), (19, 'Laboratorios de calibracion')], max_length=200, null=True),
        ),
    ]
