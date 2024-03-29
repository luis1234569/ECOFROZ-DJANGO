# Generated by Django 3.0.8 on 2023-08-08 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0042_auto_20230807_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(2, 'Aprobado'), (3, 'Rechazada'), (1, 'Pendiente'), (4, 'Anulada'), (5, 'Booked')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Booking Ruta Programada'), (3, 'Encomienda'), (2, 'Nueva Solicitud Transporte'), (4, 'Vale de Combustible')], null=True),
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
            field=models.IntegerField(blank=True, choices=[(2, 'Aprobado'), (3, 'Rechazada'), (1, 'Pendiente'), (4, 'Anulada'), (5, 'Booked')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(3, 'Devuelta'), (2, 'En proceso'), (1, 'Pendiente'), (4, 'Confirmado')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='ruta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='laruta', to='procesosAdministrativos.RutaTransporte'),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte personas'), (3, 'Vale Combustible'), (2, 'Encomienda')], null=True),
        ),
    ]
