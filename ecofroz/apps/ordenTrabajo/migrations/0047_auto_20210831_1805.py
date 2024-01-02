# Generated by Django 3.0.8 on 2021-08-31 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenTrabajo', '0046_auto_20210528_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(0, 'No Aprobado'), (2, 'Anulada'), (1, 'Aprobado'), ('', 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='refer_orden',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='salida_activo',
            field=models.BooleanField(blank=True, choices=[(True, 'SI'), (False, 'NO')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='tipo_trabajo',
            field=models.IntegerField(blank=True, choices=[(2, 'Externo'), (1, 'Interno')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trabajospago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA'), (3, 'RESERVA'), (1, 'MBA')], null=True),
        ),
    ]
