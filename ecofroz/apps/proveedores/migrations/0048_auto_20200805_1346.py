# Generated by Django 3.0 on 2020-08-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0047_auto_20200805_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga_respuestas',
            name='p023',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('INACTIVO', 'INACTIVO'), ('ACTIVO', 'ACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('No', 'No'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (6, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis de metales pesados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de MATERIA ORGANICA'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (1, 'Registro de los productos en Agrocalidad o Magar'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Por correo electrónico', 'Por correo electrónico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(13, 'Quimicos de limpieza (Detergentes)'), (8, 'Requisitos Persona Juridica'), (34, 'Retroalimentacion Ecofroz'), (21, 'Materia Prima'), (28, 'Buenas practicas de calidad'), (25, 'Transporte maritimo (navieras)'), (23, 'Grados de grado alimenticio'), (33, 'Buenas practicas con proveedores y clientes'), (12, 'Centros de acopio'), (30, 'Buenas practicas ambientales'), (26, 'Korex - Sleep Shipt'), (29, 'Buenas practicas de seguridad'), (22, 'Quimicos para el caldero'), (1, 'Fecha de elaboración'), (27, 'Transporte'), (32, 'Buenas practicas laborales'), (14, 'Quimicos de limpieza (Desinfectantes)'), (3, 'Licitud de Fondos'), (24, 'Transporte de contenedores'), (9, 'Información de la relacion comercial con Ecofroz'), (11, 'Control de Plagas'), (19, 'Laboratorios de calibracion'), (20, 'Gestores ambientales de desechos'), (16, 'Catering'), (18, 'Materiales de laboratorio (insumos)'), (4, 'Veracidad de las respuestas'), (6, 'Existencia y Legalidad'), (10, 'Fundas/Rollos'), (31, 'Buenas prracticas de  responsabilidad social'), (5, 'Información General'), (7, 'Requisitos persona Natural'), (17, 'Laboratorios de Analisis'), (15, 'Cajas'), (2, 'Codigo de Etica')], max_length=200, null=True),
        ),
    ]
