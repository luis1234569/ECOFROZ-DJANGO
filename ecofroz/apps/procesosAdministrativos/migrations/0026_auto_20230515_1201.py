# Generated by Django 3.0.8 on 2023-05-15 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0025_auto_20230515_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutatransporte',
            name='fecha_creacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rutatransporte',
            name='fecha_modifica',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rutatransporte',
            name='persona_edita',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('CUBA', 'CUBA'), ('HIDROCOOLER', 'HIDROCOOLER')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='tipo',
            field=models.CharField(blank=True, choices=[('APA', 'APA'), ('PH', 'PH')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('CUBA', 'CUBA'), ('HIDROCOOLER', 'HIDROCOOLER')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(1, 'Pendiente'), (2, 'Aprobado'), (3, 'Rechazada'), (4, 'Anulada')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(2, 'En proceso'), (1, 'Pendiente'), (4, 'Confirmado'), (3, 'Devuelta')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte'), (2, 'Encomienda')], null=True),
        ),
    ]
