# Generated by Django 3.2.15 on 2023-12-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenTrabajo', '0076_auto_20231220_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudesadqui',
            name='aceptado_conta',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudesadqui',
            name='aprobado_ger',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudesadqui',
            name='enviada',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(3, 'Rechazada Ger'), (1, 'Aprobado Ger'), (0, 'Pendiente'), (4, 'Rechazada Conta'), (2, 'Gestionado Conta')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='tipo_trabajo',
            field=models.IntegerField(blank=True, choices=[(2, 'Externo'), (1, 'Interno')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudesadqui',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(3, 'Rechazada Ger'), (1, 'Aprobado Ger'), (0, 'Pendiente'), (4, 'Rechazada Conta'), (2, 'Gestionado Conta')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudesadqui',
            name='aprobado_cont',
            field=models.IntegerField(blank=True, choices=[(3, 'Rechazada Ger'), (1, 'Aprobado Ger'), (0, 'Pendiente'), (4, 'Rechazada Conta'), (2, 'Gestionado Conta')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudesadqui',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA/ACTIVOS'), (1, 'MBA'), (3, 'SIA/TRABAJOS')], null=True),
        ),
        migrations.AlterField(
            model_name='trabajospago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA/ACTIVOS'), (1, 'MBA'), (3, 'SIA/TRABAJOS')], null=True),
        ),
    ]
