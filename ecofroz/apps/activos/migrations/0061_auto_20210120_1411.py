# Generated by Django 3.0.7 on 2021-01-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0060_auto_20210120_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='desc_activo',
            options={'managed': True, 'ordering': ['-activo_fecha_modifica'], 'permissions': (('acceso_activos', 'Acceso Provicional'), ('modificaciones_activos', 'Modificaciones Activos'), ('genera_código', 'Generación de Activos'))},
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('MN', 'MANTENIMIENTO'), ('DO', 'DONADO'), ('AC', 'ACTIVO'), ('RE', 'REPARACIÓN EXTERNA'), ('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('1', 'ROTURA DE MAQUINARIA'), ('2', 'EQUIPO Y MAQUINARIA'), ('4', 'SIN SEGURO'), ('5', 'VEHICULOS'), ('3', 'INCENDIO'), ('6', 'EQUIPO ELECTRONICO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_estado', 'Cambio de Estado'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='pers_autoriza_seguridad',
            field=models.CharField(blank=True, choices=[('Fernando Ortiz', 'Fernando Ortiz'), ('Galo Jaramillo', 'Galo Jaramillo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('PABLO BORJA', 'PABLO BORJA'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
