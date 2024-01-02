# Generated by Django 3.0.7 on 2021-01-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenTrabajo', '0033_auto_20210120_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalletrabajo',
            name='descripcion',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), (0, 'No Aprobado'), ('', 'Pendiente')], null=True),
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
            name='tipo_pedi',
            field=models.CharField(blank=True, choices=[('MP', 'Mantenimiento Preventivo'), ('OT', 'Otros Insumos'), ('OS', 'Orden de Servicio'), ('PR', 'Proyecto'), ('MC', 'Mantenimiento Correctivo')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='tipo_trabajo',
            field=models.IntegerField(blank=True, choices=[(1, 'Interno'), (2, 'Externo')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trabajospago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA'), (3, 'RESERVA'), (1, 'MBA')], null=True),
        ),
    ]
