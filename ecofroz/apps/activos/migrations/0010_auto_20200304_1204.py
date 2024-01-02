# Generated by Django 3.0 on 2020-03-04 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0009_auto_20200303_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo_tipo',
            name='tipo_grupo',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.DO_NOTHING, to='activos.activo_grupo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('DADO DE BAJA', 'DADO DE BAJA'), ('ACTIVO', 'ACTIVO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_estado', 'Cambio de Estado'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_ubicacion', 'Cambio de Ubicación')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_usuario_registra',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.CharField(blank=True, choices=[('Préstamo entre ubicaciones propias', 'Préstamo entre ubicaciones propias'), ('Salida por Reparacion', 'Salida por Reparacion')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='solicitado_por',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
