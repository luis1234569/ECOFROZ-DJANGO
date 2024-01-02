# Generated by Django 3.0.7 on 2021-03-12 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0078_auto_20210211_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activo_nomenclatura',
            name='nomenclatura_estado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='activos_temp_excel',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='activo_estado',
            field=models.CharField(blank=True, choices=[('RE', 'REPARACIÓN EXTERNA'), ('MN', 'MANTENIMIENTO'), ('DO', 'DONADO'), ('AC', 'ACTIVO'), ('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='grabado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], default='NO', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('1', 'ROTURA DE MAQUINARIA'), ('4', 'SIN SEGURO'), ('6', 'EQUIPO ELECTRONICO'), ('2', 'EQUIPO Y MAQUINARIA'), ('3', 'INCENDIO'), ('5', 'VEHICULOS')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_estado', 'Cambio de Estado'), ('cambio_ubicacion', 'Cambio de Ubicación')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(1, 'Reparación'), (4, 'Cambio de Ubicación Geográfica'), (2, 'Dado de Baja'), (3, 'Venta')], null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('PABLO BORJA', 'PABLO BORJA')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
