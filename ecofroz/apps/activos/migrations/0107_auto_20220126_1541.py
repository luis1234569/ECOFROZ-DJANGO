# Generated by Django 3.0.8 on 2022-01-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0106_auto_20220126_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='desc_activo',
            options={'managed': True, 'ordering': ['-activo_fecha_modifica'], 'permissions': (('acceso_activos', 'Acceso Provicional'), ('modificaciones_activos', 'Modificaciones Activos'), ('genera_código', 'Generación de Activos'), ('consulta_edita', 'Consulta y Edita Activos'), ('mis_activos', 'Consulta Activos en Custodio Propio'), ('descargo_activos', 'Descargo de Activos Seguridad'))},
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
            field=models.CharField(blank=True, choices=[('AC', 'ACTIVO'), ('DO', 'DONADO'), ('MN', 'MANTENIMIENTO'), ('RE', 'REPARACIÓN EXTERNA'), ('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('4', 'SIN SEGURO'), ('3', 'INCENDIO'), ('6', 'EQUIPO ELECTRONICO'), ('5', 'VEHICULOS'), ('2', 'EQUIPO Y MAQUINARIA'), ('1', 'ROTURA DE MAQUINARIA')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_custodio', 'Cambio de Custodio'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_estado', 'Cambio de Estado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_fecha', 'Cambio de Fecha'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_estado_identifica', 'Cambio de Estado Identificación Grabado/Etiquetado')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('DAVID  MENCIAS', 'DAVID MENCIAS'), ('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('PABLO BORJA', 'PABLO BORJA'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
