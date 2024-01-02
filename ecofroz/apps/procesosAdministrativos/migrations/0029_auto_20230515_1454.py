# Generated by Django 3.0.8 on 2023-05-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0028_auto_20230515_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutatransporte',
            name='comentarios',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('HIDROCOOLER', 'HIDROCOOLER'), ('CUBA', 'CUBA')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='tipo',
            field=models.CharField(blank=True, choices=[('PH', 'PH'), ('APA', 'APA')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('HIDROCOOLER', 'HIDROCOOLER'), ('CUBA', 'CUBA')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(3, 'Rechazada'), (2, 'Aprobado'), (4, 'Anulada'), (1, 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(4, 'Confirmado'), (3, 'Devuelta'), (2, 'En proceso'), (1, 'Pendiente')], null=True),
        ),
    ]
