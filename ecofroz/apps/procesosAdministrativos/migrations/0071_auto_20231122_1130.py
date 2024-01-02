# Generated by Django 3.2.15 on 2023-11-22 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0070_auto_20231121_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventarioconsolidado',
            name='anio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='inventarioconsolidado',
            name='proyecto',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(4, 'Anulada'), (3, 'Rechazada'), (2, 'Aprobado'), (1, 'Pendiente'), (5, 'Booked')], null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(2, 'Nueva Solicitud Transporte'), (3, 'Encomienda'), (1, 'Booking Ruta Programada'), (4, 'Vale de Combustible')], null=True),
        ),
        migrations.AlterField(
            model_name='bookingreporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(4, 'Anulada'), (3, 'Rechazada'), (2, 'Aprobado'), (1, 'Pendiente'), (5, 'Booked')], null=True),
        ),
        migrations.AlterField(
            model_name='bookingreporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(3, 'Devuelta'), (4, 'Confirmado'), (1, 'Pendiente'), (2, 'En proceso')], null=True),
        ),
        migrations.AlterField(
            model_name='bookingreporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte personas'), (3, 'Vale Combustible'), (2, 'Encomienda')], null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='tipo',
            field=models.CharField(blank=True, choices=[('PH', 'PH'), ('CI', 'CI')], max_length=200, null=True),
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
            model_name='inventarioconsolidado',
            name='unimed',
            field=models.CharField(choices=[('ml', 'Mililitros'), ('Kg', 'Kilogramos'), ('gr', 'Gramos'), ('LT', 'Litros'), ('GAL', 'Galones')], max_length=3),
        ),
        migrations.AlterField(
            model_name='inventariosemanal',
            name='unimed',
            field=models.CharField(choices=[('ml', 'Mililitros'), ('Kg', 'Kilogramos'), ('gr', 'Gramos'), ('LT', 'Litros'), ('GAL', 'Galones')], max_length=3),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado1n',
            field=models.IntegerField(blank=True, choices=[(4, 'Anulada'), (3, 'Rechazada'), (2, 'Aprobado'), (1, 'Pendiente'), (5, 'Booked')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='estado2n',
            field=models.IntegerField(blank=True, choices=[(3, 'Devuelta'), (4, 'Confirmado'), (1, 'Pendiente'), (2, 'En proceso')], null=True),
        ),
        migrations.AlterField(
            model_name='solicitudtransporte',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Transporte personas'), (3, 'Vale Combustible'), (2, 'Encomienda')], null=True),
        ),
        migrations.CreateModel(
            name='Egresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodega', models.CharField(choices=[('LM', 'La Merced'), ('AC', 'Agua Clara')], max_length=3)),
                ('proyecto', models.CharField(choices=[('ML', 'Los Molles'), ('AC', 'Agua Clara'), ('LM', 'La Merced'), ('KO', 'Kosher'), ('AV', 'La Avelina')], max_length=3)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('lote', models.CharField(blank=True, max_length=300, null=True)),
                ('unimed', models.CharField(blank=True, choices=[('ml', 'Mililitros'), ('Kg', 'Kilogramos'), ('GAL', 'Galón'), ('gr', 'Gramos'), ('LT', 'Litros')], max_length=3, null=True)),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('registra', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_registra', models.DateTimeField(blank=True, null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='egreso', to='procesosAdministrativos.inventarioconsolidado')),
            ],
            options={
                'db_table': 'procesos"."egresos_agri',
                'managed': True,
            },
        ),
    ]
