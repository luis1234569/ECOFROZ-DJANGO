# Generated by Django 3.0 on 2020-06-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0030_auto_20200601_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='desc_activo',
            name='incendios',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='desc_activo',
            name='poliza_seguros',
            field=models.CharField(blank=True, choices=[('5', 'VEHICULOS'), ('1', 'ROTURA DE MAQUINARIA'), ('3', 'INCENDIO'), ('4', 'SIN SEGURO'), ('2', 'EQUIPO Y MAQUINARIA'), ('6', 'EQUIPO ELECTRONICO')], max_length=20, null=True),
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
            field=models.CharField(blank=True, choices=[('MANTENIMIENTO', 'MANTENIMIENTO'), ('ACTIVO', 'ACTIVO'), ('DADO DE BAJA', 'DADO DE BAJA')], default='ACTIVO', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_asegurado',
            field=models.CharField(blank=True, choices=[('NO', 'NO'), ('SI', 'SI')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='detalle_desc_activo',
            name='desc_activo_motivo_modifica',
            field=models.CharField(blank=True, choices=[('cambio_estado', 'Cambio de Estado'), ('cambio_custodio', 'Cambio de Custodio'), ('cambio_ubicacion', 'Cambio de Ubicación'), ('cambio_caracteristicas', 'Cambio de Caracteristicas'), ('actualiza_asegurado', 'Cambio valor Asegurado')], max_length=50, null=True),
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
            model_name='salida_activos',
            name='sale_por',
            field=models.CharField(blank=True, choices=[('Préstamo entre ubicaciones propias', 'Préstamo entre ubicaciones propias'), ('Salida por Reparacion', 'Salida por Reparacion')], max_length=200, null=True),
        ),
    ]
