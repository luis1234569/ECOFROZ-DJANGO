# Generated by Django 3.0.7 on 2020-09-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0051_auto_20200825_1642'),
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
            field=models.CharField(blank=True, choices=[('RE', 'REPARACIÓN EXTERNA'), ('DO', 'DONADO'), ('MN', 'MANTENIMIENTO'), ('AC', 'ACTIVO'), ('VE', 'VENDIDO'), ('DB', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('6', 'EQUIPO ELECTRONICO'), ('5', 'VEHICULOS'), ('2', 'EQUIPO Y MAQUINARIA'), ('1', 'ROTURA DE MAQUINARIA'), ('4', 'SIN SEGURO')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('cambio_custodio', 'Cambio de Custodio'), ('actualiza_asegurado', 'Cambio valor Asegurado'), ('cambio_estado', 'Cambio de Estado'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_fecha', 'Cambio de Fecha')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='pers_autoriza_seguridad',
            field=models.CharField(blank=True, choices=[('Fernando Ortiz', 'Fernando Ortiz'), ('Galo Jaramillo', 'Galo Jaramillo')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='salida_activos',
            name='retorno',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='toma_fisica',
            name='usuario',
            field=models.CharField(blank=True, choices=[('EDUARDO CLAVIJO', 'EDUARDO CLAVIJO'), ('PABLO BORJA', 'PABLO BORJA'), ('DAVID  MENCIAS', 'DAVID MENCIAS'), ('JUAN VILLAMARIN', 'JUAN VILLAMARIN')], default='EDUARDO CLAVIJO', max_length=50, null=True),
        ),
    ]
