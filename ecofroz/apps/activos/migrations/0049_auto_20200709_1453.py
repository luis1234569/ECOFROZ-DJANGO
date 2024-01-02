# Generated by Django 3.0 on 2020-07-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0048_auto_20200709_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA'), ('MN', 'MANTENIMIENTO'), ('DO', 'DONADO'), ('RE', 'REPARACIÓN EXTERNA'), ('AC', 'ACTIVO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('1', 'ROTURA DE MAQUINARIA'), ('2', 'EQUIPO Y MAQUINARIA'), ('4', 'SIN SEGURO'), ('5', 'VEHICULOS'), ('6', 'EQUIPO ELECTRONICO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_estado', 'Cambio de Estado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_custodio', 'Cambio de Custodio')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.CharField(blank=True, choices=[('Préstamo entre ubicaciones propias', 'Préstamo entre ubicaciones propias'), ('Salida por Reparacion', 'Salida por Reparacion')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('PABLO BORJA', 'PABLO BORJA'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
