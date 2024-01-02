# Generated by Django 3.2.15 on 2023-10-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0123_auto_20230817_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('DO', 'DONADO'), ('AC', 'ACTIVO'), ('RE', 'REPARACIÓN EXTERNA'), ('DB', 'DADO DE BAJA'), ('VE', 'VENDIDO'), ('MN', 'MANTENIMIENTO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='grabado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('GRABADO', 'GRABADO'), ('NO ES POSIBLE IDENTIFICAR', 'NO ES POSIBLE IDENTIFICAR'), ('ETIQUETA', 'ETIQUETA')], default='NO', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('1', 'ROTURA DE MAQUINARIA'), ('3', 'INCENDIO'), ('6', 'EQUIPO ELECTRONICO'), ('4', 'SIN SEGURO'), ('5', 'VEHICULOS'), ('2', 'EQUIPO Y MAQUINARIA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_fecha', 'Cambio de Fecha'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_estado_identifica', 'Cambio de Estado Identificación Grabado/Etiquetado'), ('cambio_estado', 'Cambio de Estado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_custodio', 'Cambio de Custodio')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('PABLO BORJA', 'PABLO BORJA'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('DAVID  MENCIAS', 'DAVID MENCIAS')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
