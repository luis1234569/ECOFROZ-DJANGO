# Generated by Django 3.0.8 on 2022-03-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosInternos', '0007_auto_20220317_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitudtrabajointerno',
            options={'managed': True, 'permissions': (('acceso_trabajos_internos', 'Acceso a Trabajos Internos'),)},
        ),
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(4, 'Anulada'), (2, 'Aprobado'), (3, 'Rechazada'), (1, 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(1, 'Pendiente'), (2, 'En proceso'), (5, 'Convertida'), (4, 'Finalizada'), (3, 'Anulada')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(3, 'Pintura'), (1, 'Obra Civil'), (6, 'Adecuaciones'), (2, 'Cableado Estructurado'), (4, 'Eléctricos'), (5, 'Estructuras Metálicas')], null=True),
        ),
    ]
