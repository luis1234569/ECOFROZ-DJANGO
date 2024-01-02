# Generated by Django 3.0 on 2020-12-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0069_auto_20201215_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproveedor_det',
            name='cumple_entrega_docs',
            field=models.CharField(blank=True, default='NO', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='cumple_entrega_docs',
            field=models.CharField(blank=True, default='NO', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('INACTIVO', 'INACTIVO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='respondio_encuesta',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('No', 'No'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(6, 'Conocer el orígen de las materias primas'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis de metales pesados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (7, 'No soy proveedor de fertilizantes'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de MATERIA ORGANICA'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias')], max_length=50, null=True),
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
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('No', 'No'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(6, 'Conocer el orígen de las materias primas'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis de metales pesados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (7, 'No soy proveedor de fertilizantes'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de MATERIA ORGANICA'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de pesticidas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('Adjunto a este formulario', 'Adjunto a este formulario'), ('No lo requiero', 'No lo requiero'), ('Documento Físico', 'Documento Físico'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Trabaja en residencia', 'Trabaja en residencia'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(6, 'Existencia y Legalidad'), (31, 'Buenas prracticas de  responsabilidad social'), (9, 'Información de la relacion comercial con Ecofroz'), (27, 'Transporte'), (4, 'Veracidad de las respuestas'), (10, 'Fundas/Rollos'), (25, 'Transporte maritimo (navieras)'), (32, 'Buenas practicas laborales'), (13, 'Quimicos de limpieza (Detergentes)'), (34, 'Retroalimentacion Ecofroz'), (17, 'Laboratorios de Analisis'), (20, 'Gestores ambientales de desechos'), (23, 'Grados de grado alimenticio'), (11, 'Control de Plagas'), (28, 'Buenas practicas de calidad'), (33, 'Buenas practicas con proveedores y clientes'), (16, 'Catering'), (5, 'Información General'), (1, 'Fecha de elaboración'), (7, 'Requisitos persona Natural'), (14, 'Quimicos de limpieza (Desinfectantes)'), (30, 'Buenas practicas ambientales'), (29, 'Buenas practicas de seguridad'), (8, 'Requisitos Persona Juridica'), (18, 'Materiales de laboratorio (insumos)'), (3, 'Licitud de Fondos'), (26, 'Korex - Sleep Shipt'), (19, 'Laboratorios de calibracion'), (2, 'Codigo de Etica'), (22, 'Quimicos para el caldero'), (24, 'Transporte de contenedores'), (15, 'Cajas'), (21, 'Materia Prima'), (12, 'Centros de acopio')], max_length=200, null=True),
        ),
    ]
