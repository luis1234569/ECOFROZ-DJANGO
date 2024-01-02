# Generated by Django 3.0 on 2021-02-09 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0071_auto_20210209_1045'),
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
            field=models.CharField(blank=True, choices=[('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA'), ('DO', 'DONADO'), ('AC', 'ACTIVO'), ('MN', 'MANTENIMIENTO'), ('RE', 'REPARACIÓN EXTERNA')], default='ACTIVO', max_length=20, null=True),
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
            field=models.CharField(blank=True, choices=[('1', 'ROTURA DE MAQUINARIA'), ('6', 'EQUIPO ELECTRONICO'), ('3', 'INCENDIO'), ('4', 'SIN SEGURO'), ('2', 'EQUIPO Y MAQUINARIA'), ('5', 'VEHICULOS')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_fecha', 'Cambio de Fecha'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_estado', 'Cambio de Estado'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_custodio', 'Cambio de Custodio')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historial_movimientos_internos',
            name='ubicacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='activos.activo_ubica'),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(3, 'Venta'), (1, 'Reparación'), (4, 'Cambio de Ubicación Geográfica'), (2, 'Dado de Baja')], null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('PABLO BORJA', 'PABLO BORJA')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
