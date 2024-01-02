# Generated by Django 3.0.8 on 2023-09-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0054_auto_20230830_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudtransporte',
            name='fecha_gestiona_vale',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='solicitudtransporte',
            name='observaciones_anula_vale',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='solicitudtransporte',
            name='usu_gestiona_vale',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(5, 'Booked'), (4, 'Anulada'), (3, 'Rechazada'), (2, 'Aprobado'), (1, 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(4, 'Vale de Combustible'), (2, 'Nueva Solicitud Transporte'), (3, 'Encomienda'), (1, 'Booking Ruta Programada')], null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('HIDROCOOLER', 'HIDROCOOLER'), ('CUBA', 'CUBA')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='ubicacion',
            field=models.CharField(blank=True, choices=[('HIDROCOOLER', 'HIDROCOOLER'), ('CUBA', 'CUBA')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(5, 'Booked'), (4, 'Anulada'), (3, 'Rechazada'), (2, 'Aprobado'), (1, 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(2, 'En proceso'), (1, 'Pendiente'), (4, 'Confirmado'), (3, 'Devuelta')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte personas'), (2, 'Encomienda'), (3, 'Vale Combustible')], null=True),
        ),
    ]
