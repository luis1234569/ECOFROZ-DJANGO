# Generated by Django 3.0 on 2021-05-14 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0100_auto_20210514_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_fichas',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='fichas_proveedores/'),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='proveedor_critico',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='proveedor_revisado',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (7, 'No soy proveedor de fertilizantes'), (6, 'Conocer el orígen de las materias primas'), (3, 'Análisis de metales pesados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de FOLIARES'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (1, 'Registro de los productos en Agrocalidad o Magar'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor_critico',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor_revisado',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (7, 'No soy proveedor de fertilizantes'), (6, 'Conocer el orígen de las materias primas'), (3, 'Análisis de metales pesados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de FOLIARES'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (1, 'Registro de los productos en Agrocalidad o Magar'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo tengo', 'No lo tengo'), ('Documento Físico', 'Documento Físico'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(7, 'Requisitos persona Natural'), (30, 'Buenas practicas ambientales'), (26, 'Korex - Sleep Shipt'), (29, 'Buenas practicas de seguridad'), (1, 'Fecha de elaboración'), (20, 'Gestores ambientales de desechos'), (25, 'Transporte maritimo (navieras)'), (3, 'Licitud de Fondos'), (28, 'Buenas practicas de calidad'), (22, 'Quimicos para el caldero'), (8, 'Requisitos Persona Juridica'), (34, 'Retroalimentacion Ecofroz'), (15, 'Cajas'), (5, 'Información General'), (32, 'Buenas practicas laborales'), (16, 'Catering'), (11, 'Control de Plagas'), (12, 'Centros de acopio'), (21, 'Materia Prima'), (10, 'Fundas/Rollos'), (31, 'Buenas prracticas de  responsabilidad social'), (33, 'Buenas practicas con proveedores y clientes'), (4, 'Veracidad de las respuestas'), (6, 'Existencia y Legalidad'), (2, 'Codigo de Etica'), (18, 'Materiales de laboratorio (insumos)'), (23, 'Grados de grado alimenticio'), (27, 'Transporte'), (24, 'Transporte de contenedores'), (13, 'Quimicos de limpieza (Detergentes)'), (9, 'Información de la relacion comercial con Ecofroz'), (17, 'Laboratorios de Analisis'), (19, 'Laboratorios de calibracion'), (14, 'Quimicos de limpieza (Desinfectantes)')], max_length=200, null=True),
        ),
    ]
