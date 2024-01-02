# Generated by Django 3.0 on 2020-03-30 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0017_auto_20200330_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_encuesta',
            name='consulta',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (6, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (5, 'No soy proveedor de MATERIA ORGANICA')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (1, 'Registro de los productos en Agrocalidad o Magar'), (5, 'No soy proveedor de pesticidas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Trabaja en residencia', 'Trabaja en residencia'), ('Propias', 'Propias'), ('Compartida por varias empresas', 'Compartida por varias empresas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(23, 'Grados de grado alimenticio'), (27, 'Transporte'), (17, 'Laboratorios de Analisis'), (19, 'Laboratorios de calibracion'), (30, 'Buenas practicas ambientales'), (34, 'Retroalimentacion Ecofroz'), (2, 'Codigo de Etica'), (3, 'Licitud de Fondos'), (33, 'Buenas practicas con proveedores y clientes'), (28, 'Buenas practicas de calidad'), (6, 'Existencia y Legalidad'), (5, 'Información General'), (9, 'Información de la relacion comercial con Ecofroz'), (25, 'Transporte maritimo (navieras)'), (29, 'Buenas practicas de seguridad'), (12, 'Centros de acopio'), (22, 'Quimicos para el caldero'), (31, 'Buenas prracticas de  responsabilidad social'), (24, 'Transporte de contenedores'), (20, 'Gestores ambientales de desechos'), (14, 'Quimicos de limpieza (Desinfectantes)'), (13, 'Quimicos de limpieza (Detergentes)'), (10, 'Fundas/Rollos'), (18, 'Materiales de laboratorio (insumos)'), (8, 'Requisitos Persona Juridica'), (7, 'Requisitos persona Natural'), (4, 'Veracidad de las respuestas'), (26, 'Korex - Sleep Shipt'), (11, 'Control de Plagas'), (16, 'Catering'), (1, 'Fecha de elaboración'), (15, 'Cajas'), (21, 'Materia Prima'), (32, 'Buenas practicas laborales')], max_length=200, null=True),
        ),
    ]
