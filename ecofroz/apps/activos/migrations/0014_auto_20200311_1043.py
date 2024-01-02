# Generated by Django 3.0 on 2020-03-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0013_auto_20200306_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='salida_activos',
            name='estado',
            field=models.CharField(blank=True, choices=[(1, 'En Reparación Externa'), (2, 'Retornó')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_valor',
            field=models.FloatField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_estado', 'Cambio de Estado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='pers_autoriza_seguridad',
            field=models.CharField(blank=True, choices=[('Galo Jaramillo', 'Galo Jaramillo'), ('Fernando Ortiz', 'Fernando Ortiz')], max_length=200, null=True),
        ),
    ]
