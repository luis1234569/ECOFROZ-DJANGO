# Generated by Django 3.0.8 on 2022-08-09 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0157_auto_20220622_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos_prove',
            name='marca_cal',
            field=models.CharField(blank=True, choices=[('INCORRECTA', 'INCORRECTA'), ('DESACTUALIZADA', 'DESACTUALIZADA'), ('CORRECTA', 'CORECTA')], max_length=15, null=True),
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
            model_name='historicalproveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor',
            name='tipo_provee',
            field=models.IntegerField(blank=True, choices=[(0, 'VARIOS'), (1, 'EMPAQUE')], null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (6, 'Conocer el orígen de las materias primas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (5, 'No soy proveedor de pesticidas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o Magar')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='historicalproveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
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
            model_name='proveedor',
            name='tipo_empresa',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='tipo_provee',
            field=models.IntegerField(blank=True, choices=[(0, 'VARIOS'), (1, 'EMPAQUE')], null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(7, 'No soy proveedor de fertilizantes'), (3, 'Análisis de metales pesados'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa'), (6, 'Conocer el orígen de las materias primas')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (5, 'No soy proveedor de FOLIARES'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(4, 'Conocer el orígen de las materias primas'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (5, 'No soy proveedor de MATERIA ORGANICA')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa'), (5, 'No soy proveedor de pesticidas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o Magar')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_biodegradabilidad',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_determinar_concentracion_quimico',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_copia_hoja_seguridad_datos_msds',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=False, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_fichas_tecnicas_y_registros_sanitarios',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_formato_informacion_contacto_emergencia',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_ingredientes_activos_aprobados',
            field=models.CharField(blank=True, choices=[('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('Documento Físico', 'Documento Físico')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Compartida por varias empresas', 'Compartida por varias empresas'), ('Propias', 'Propias'), ('Trabaja en residencia', 'Trabaja en residencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_documentos',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Jurídica', 'Persona Jurídica'), ('Persona Natural', 'Persona Natural')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_encuesta',
            name='seccion',
            field=models.CharField(blank=True, choices=[(3, 'Licitud de Fondos'), (15, 'Cajas'), (34, 'Retroalimentacion Ecofroz'), (20, 'Gestores ambientales de desechos'), (25, 'Transporte maritimo (navieras)'), (29, 'Buenas practicas de seguridad'), (7, 'Requisitos persona Natural'), (23, 'Grados de grado alimenticio'), (16, 'Catering'), (30, 'Buenas practicas ambientales'), (21, 'Materia Prima'), (2, 'Codigo de Etica'), (8, 'Requisitos Persona Juridica'), (5, 'Información General'), (10, 'Fundas/Rollos'), (6, 'Existencia y Legalidad'), (14, 'Quimicos de limpieza (Desinfectantes)'), (28, 'Buenas practicas de calidad'), (11, 'Control de Plagas'), (27, 'Transporte'), (13, 'Quimicos de limpieza (Detergentes)'), (32, 'Buenas practicas laborales'), (1, 'Fecha de elaboración'), (12, 'Centros de acopio'), (9, 'Información de la relacion comercial con Ecofroz'), (33, 'Buenas practicas con proveedores y clientes'), (22, 'Quimicos para el caldero'), (31, 'Buenas prracticas de  responsabilidad social'), (19, 'Laboratorios de calibracion'), (17, 'Laboratorios de Analisis'), (4, 'Veracidad de las respuestas'), (24, 'Transporte de contenedores'), (26, 'Korex - Sleep Shipt'), (18, 'Materiales de laboratorio (insumos)')], max_length=200, null=True),
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
        migrations.CreateModel(
            name='proveedor_estados_select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docu', models.CharField(blank=True, max_length=300, null=True)),
                ('tdocu', models.BooleanField(blank=True, null=True)),
                ('fecini', models.DateField(blank=True, null=True)),
                ('fecfin', models.DateField(blank=True, null=True)),
                ('codigo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='proveedores.proveedor')),
            ],
            options={
                'db_table': 'proveedores"."proveedor_estados_select',
                'managed': True,
            },
        ),
    ]
