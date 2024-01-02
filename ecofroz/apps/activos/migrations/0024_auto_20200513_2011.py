# Generated by Django 3.0 on 2020-05-14 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0023_auto_20200511_2307'),
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
            field=models.CharField(blank=True, choices=[('DADO DE BAJA', 'DADO DE BAJA'), ('ACTIVO', 'ACTIVO'), ('MANTENIMIENTO', 'MANTENIMIENTO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_estado', 'Cambio de Estado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_ubicacion', 'Cambio de Ubicación')], max_length=50, null=True),
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
