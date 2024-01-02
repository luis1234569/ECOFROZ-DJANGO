# Generated by Django 3.0.8 on 2022-01-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0107_auto_20220126_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='activo_estados_select',
            name='custodio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
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
            field=models.CharField(blank=True, choices=[('RE', 'REPARACIÓN EXTERNA'), ('DO', 'DONADO'), ('DB', 'DADO DE BAJA'), ('AC', 'ACTIVO'), ('VE', 'VENDIDO'), ('MN', 'MANTENIMIENTO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='grabado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('ETIQUETA', 'ETIQUETA'), ('GRABADO', 'GRABADO')], default='NO', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('4', 'SIN SEGURO'), ('6', 'EQUIPO ELECTRONICO'), ('3', 'INCENDIO'), ('2', 'EQUIPO Y MAQUINARIA'), ('1', 'ROTURA DE MAQUINARIA'), ('5', 'VEHICULOS')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_estado_identifica', 'Cambio de Estado Identificación Grabado/Etiquetado'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_estado', 'Cambio de Estado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(4, 'Cambio de Ubicación (Haciendas / Machachi)'), (1, 'Reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('DAVID  MENCIAS', 'DAVID MENCIAS'), ('PABLO BORJA', 'PABLO BORJA'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
