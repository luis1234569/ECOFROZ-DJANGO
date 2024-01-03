# Generated by Django 5.0.1 on 2024-01-03 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activo_depar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_nombre', models.CharField(max_length=50, null=True)),
                ('dep_estado', models.IntegerField(blank=True)),
                ('autoriza_salida', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='activo_ubica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubica_nombre', models.CharField(max_length=50, null=True)),
                ('ubica_estado', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='activo_areas',
            fields=[
                ('area_codigo', models.AutoField(primary_key=True, serialize=False)),
                ('area_nombre', models.CharField(max_length=50, null=True)),
                ('area_estado', models.IntegerField(blank=True)),
                ('area_ubica', models.IntegerField(blank=True, null=True)),
                ('area_departamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='solicita_puestos.activo_depar')),
            ],
        ),
        migrations.CreateModel(
            name='solicita_puesto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(blank=True, max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('justificacion', models.CharField(blank=True, max_length=255)),
                ('solicitante', models.CharField(blank=True, max_length=255)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('estado_aprobacion', models.IntegerField(blank=True, choices=[(0, 'No Aprobado'), (1, 'Aprobado'), (2, 'Anulada'), ('', 'Pendiente')], null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='solicita_puestos.activo_areas')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='solicita_puestos.activo_depar')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='solicita_puestos.activo_ubica')),
            ],
        ),
    ]