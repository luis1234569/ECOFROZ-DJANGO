# Generated by Django 3.0 on 2021-02-11 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0077_auto_20210209_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('DO', 'DONADO'), ('RE', 'REPARACIÓN EXTERNA'), ('AC', 'ACTIVO'), ('VE', 'VENDIDO'), ('MN', 'MANTENIMIENTO'), ('DB', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('2', 'EQUIPO Y MAQUINARIA'), ('5', 'VEHICULOS'), ('3', 'INCENDIO'), ('4', 'SIN SEGURO'), ('6', 'EQUIPO ELECTRONICO'), ('1', 'ROTURA DE MAQUINARIA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_custodio', 'Cambio de Custodio'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_estado', 'Cambio de Estado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='num_orden_trabajo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(4, 'Cambio de Ubicación Geográfica'), (3, 'Venta'), (1, 'Reparación'), (2, 'Dado de Baja')], null=True),
        ),
    ]
