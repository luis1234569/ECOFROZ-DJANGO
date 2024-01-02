# Generated by Django 3.0.8 on 2023-05-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0021_auto_20230512_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventosclorol2',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('CUBA', 'CUBA'), ('HIDROCOOLER', 'HIDROCOOLER')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('CUBA', 'CUBA'), ('HIDROCOOLER', 'HIDROCOOLER')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='recgpt',
            name='pc',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(4, 'Anulada'), (3, 'Rechazada'), (1, 'Pendiente'), (2, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(2, 'En proceso'), (3, 'Devuelta'), (1, 'Pendiente'), (4, 'Confirmado')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte'), (2, 'Encomienda')], null=True),
        ),
    ]
