# Generated by Django 3.0.3 on 2022-05-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajosInternos', '0023_auto_20220510_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(3, 'Rechazada'), (4, 'Anulada'), (1, 'Pendiente'), (2, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(1, 'Pendiente'), (3, 'Devuelta'), (4, 'Finalizada'), (2, 'En proceso'), (5, 'Convertida')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtrabajointerno',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Obra Civil'), (3, 'Pintura'), (7, 'Mantenimiento Maquinaria'), (4, 'Eléctricos'), (5, 'Estructuras Metálicas'), (6, 'Adecuaciones'), (2, 'Cableado Estructurado')], null=True),
        ),
    ]
