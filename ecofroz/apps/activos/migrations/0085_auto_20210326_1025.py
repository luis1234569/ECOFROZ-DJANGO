# Generated by Django 3.0.7 on 2021-03-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0084_auto_20210322_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salida_activos',
            options={'managed': True, 'permissions': (('acceso_activos', 'Acceso Provicional'), ('movimiento_activos', 'Acceso Movimiento de Activos'), ('autorizacion_salida_activos', 'Autorización de Salida de Activos'), ('control_salida_activos', 'Control de Seguridad Salida de Activos'), ('movimiento_bodega_activos', 'Acceso Movimiento de Activos en Bodega'), ('rehistro_salida_activos', 'Registro de Salida de Activos'))},
        ),
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
            field=models.CharField(blank=True, choices=[('RE', 'REPARACIÓN EXTERNA'), ('AC', 'ACTIVO'), ('MN', 'MANTENIMIENTO'), ('DO', 'DONADO'), ('DB', 'DADO DE BAJA'), ('VE', 'VENDIDO')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='grabado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('4', 'SIN SEGURO'), ('1', 'ROTURA DE MAQUINARIA'), ('5', 'VEHICULOS'), ('2', 'EQUIPO Y MAQUINARIA'), ('3', 'INCENDIO'), ('6', 'EQUIPO ELECTRONICO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_ubicacion', 'Cambio de Ubicación'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_estado', 'Cambio de Estado'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_custodio', 'Cambio de Custodio')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(4, 'Cambio de Ubicación Geográfica'), (3, 'Venta'), (1, 'Reparación'), (2, 'Dado de Baja')], null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('PABLO BORJA', 'PABLO BORJA'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
