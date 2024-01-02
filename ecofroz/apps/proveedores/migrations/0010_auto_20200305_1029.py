# Generated by Django 3.0 on 2020-03-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0009_auto_20200304_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor_det',
            name='otros_documentos_enviados1',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='info_proveedores'),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='otros_documentos_enviados2',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='info_proveedores'),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='otros_documentos_enviados3',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='info_proveedores'),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='otros_documentos_enviados4',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='info_proveedores'),
        ),
        migrations.AddField(
            model_name='proveedor_det',
            name='otros_documentos_enviados5',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='info_proveedores'),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='empresa_tipo',
            field=models.CharField(blank=True, choices=[('Persona Natural', 'Persona Natural'), ('Persona Jurídica', 'Persona Jurídica')], max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='es_proveedor_maquinaria_o_equipo',
            field=models.CharField(blank=True, choices=[('No', 'No'), ('Maquinaria y/o equipos', 'Maquinaria y/o equipos'), ('Servicio de mantenimiento de maquinaria y/o equipos', 'Servicio de mantenimiento de maquinaria y/o equipos'), ('Repuestos de maquinaria y/o equipos', 'Repuestos de maquinaria y/o equipos')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_fertilizantes_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(6, 'Conocer el orígen de las materias primas'), (7, 'No soy proveedor de fertilizantes'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (3, 'Análisis de metales pesados'), (4, 'Certificado de que esta libre de noni fenol y cloruro de benzalconio'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'Los ingredientes activos vigentes en las legislaciones de USA, Japón, Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_foliares_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(5, 'No soy proveedor de FOLIARES'), (1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_materia_organica_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(1, 'Registro de los productos en Agrocalidad o MAGAP'), (4, 'Conocer el orígen de las materias primas'), (2, 'Fichas técnicas y hojas de seguridad de los productos empleados'), (5, 'No soy proveedor de MATERIA ORGANICA'), (3, 'Análisis físico-químico y microbiológico de la M.O. (vigencia 1 año)')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='proveedor_pesticidas_requisitos_indispensables',
            field=models.CharField(blank=True, choices=[(2, 'Fichas técnicas y hojas de seguridad de los productos empleado'), (5, 'No soy proveedor de pesticidas'), (3, 'Análisis producto libre de noni fenol y cloruro de banzalconio con límite de 0.01 ppm de c/compuesto'), (1, 'Registro de los productos en Agrocalidad o Magar'), (4, 'Los ingredientes activos deben estar vigentes en las legislaciones de USA,Japón y Europa')], max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tiene_certificado_ambiental',
            field=models.CharField(blank=True, choices=[('Documento Físico', 'Documento Físico'), ('Adjunto a este formulario', 'Adjunto a este formulario'), ('Por correo electrónico', 'Por correo electrónico'), ('No lo tengo', 'No lo tengo'), ('No lo requiero', 'No lo requiero')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='proveedor_det',
            name='tipo_instalaciones',
            field=models.CharField(blank=True, choices=[('Compartida por varias empresas', 'Compartida por varias empresas'), ('Trabaja en residencia', 'Trabaja en residencia'), ('Propias', 'Propias')], max_length=50, null=True),
        ),
    ]
