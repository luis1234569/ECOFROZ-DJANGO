# Generated by Django 3.0.8 on 2021-08-12 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0094_auto_20210513_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='desc_activo',
            options={'managed': True, 'ordering': ['-activo_fecha_modifica'], 'permissions': (('acceso_activos', 'Acceso Provicional'), ('modificaciones_activos', 'Modificaciones Activos'), ('genera_código', 'Generación de Activos'), ('consulta_edita', 'Consulta y Edita Activos'))},
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
            field=models.CharField(blank=True, choices=[('RE', 'REPARACIÓN EXTERNA'), ('DO', 'DONADO'), ('MN', 'MANTENIMIENTO'), ('DB', 'DADO DE BAJA'), ('VE', 'VENDIDO'), ('AC', 'ACTIVO')], default='ACTIVO', max_length=20, null=True),
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
            field=models.CharField(blank=True, choices=[('2', 'EQUIPO Y MAQUINARIA'), ('3', 'INCENDIO'), ('5', 'VEHICULOS'), ('6', 'EQUIPO ELECTRONICO'), ('1', 'ROTURA DE MAQUINARIA'), ('4', 'SIN SEGURO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_fecha', 'Cambio de Fecha'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_estado', 'Cambio de Estado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='sale_por',
            field=models.IntegerField(blank=True, choices=[(4, 'Cambio de Ubicación (Haciendas / Machachi)'), (3, 'Venta'), (2, 'Dado de Baja'), (1, 'Reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('DAVID  MENCIAS', 'DAVID MENCIAS'), ('PABLO BORJA', 'PABLO BORJA'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
