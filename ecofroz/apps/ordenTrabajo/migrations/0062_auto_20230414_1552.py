# Generated by Django 3.0.8 on 2023-04-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenTrabajo', '0061_auto_20230413_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenestrabajos',
            name='usuario_precotiza',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), ('', 'Pendiente'), (2, 'Anulada'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='refer_orden',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='salida_activo',
            field=models.BooleanField(blank=True, choices=[(False, 'NO'), (True, 'SI')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trabajospago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA'), (1, 'MBA'), (3, 'RESERVA')], null=True),
        ),
    ]
