# Generated by Django 3.0 on 2020-06-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0031_auto_20200611_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo_nomenclatura',
            name='nomenclatura_estado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='activos_temp_excel',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('ACTIVO', 'ACTIVO'), ('MANTENIMIENTO', 'MANTENIMIENTO'), ('DADO DE BAJA', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('4', 'SIN SEGURO'), ('2', 'EQUIPO Y MAQUINARIA'), ('3', 'INCENDIO'), ('6', 'EQUIPO ELECTRONICO'), ('5', 'VEHICULOS'), ('1', 'ROTURA DE MAQUINARIA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_ubicacion', 'Cambio de Ubicación'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_estado', 'Cambio de Estado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='pers_autoriza_seguridad',
            field=models.CharField(blank=True, choices=[('Galo Jaramillo', 'Galo Jaramillo'), ('Fernando Ortiz', 'Fernando Ortiz')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.CharField(blank=True, choices=[('Salida por Reparacion', 'Salida por Reparacion'), ('Préstamo entre ubicaciones propias', 'Préstamo entre ubicaciones propias')], max_length=200, null=True),
        ),
    ]
