# Generated by Django 3.0 on 2020-07-21 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0039_auto_20200721_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_encuesta',
            name='segmento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='proveedores.proveedor_segmento'),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (6, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis de metales pesados')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (4, 'Conocer el orígen de las materias primas'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (5, 'No soy proveedor de FOLIARES')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA'), (4, 'Conocer el orígen de las materias primas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o Magar'), (5, 'No soy proveedor de pesticidas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo requiero', 'No lo requiero'), ('No lo tengo', 'No lo tengo'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Propias', 'Propias'), ('Compartida por varias empresas', 'Compartida por varias empresas'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(11, 'Control de Plagas'), (12, 'Centros de acopio'), (3, 'Licitud de Fondos'), (22, 'Quimicos para el caldero'), (10, 'Fundas/Rollos'), (20, 'Gestores ambientales de desechos'), (23, 'Grados de grado alimenticio'), (14, 'Quimicos de limpieza (Desinfectantes)'), (18, 'Materiales de laboratorio (insumos)'), (34, 'Retroalimentacion Ecofroz'), (1, 'Fecha de elaboración'), (8, 'Requisitos Persona Juridica'), (19, 'Laboratorios de calibracion'), (4, 'Veracidad de las respuestas'), (15, 'Cajas'), (26, 'Korex - Sleep Shipt'), (33, 'Buenas practicas con proveedores y clientes'), (24, 'Transporte de contenedores'), (13, 'Quimicos de limpieza (Detergentes)'), (9, 'Información de la relacion comercial con Ecofroz'), (2, 'Codigo de Etica'), (6, 'Existencia y Legalidad'), (21, 'Materia Prima'), (28, 'Buenas practicas de calidad'), (30, 'Buenas practicas ambientales'), (25, 'Transporte maritimo (navieras)'), (31, 'Buenas prracticas de  responsabilidad social'), (27, 'Transporte'), (32, 'Buenas practicas laborales'), (7, 'Requisitos persona Natural'), (17, 'Laboratorios de Analisis'), (29, 'Buenas practicas de seguridad'), (5, 'Información General'), (16, 'Catering')], max_length=200, null=True),
        ),
    ]
