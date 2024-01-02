# Generated by Django 3.0.8 on 2023-01-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0002_auto_20221219_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventosPareceticoL3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(blank=True, null=True)),
                ('ppms', models.FloatField(blank=True, null=True)),
                ('ph', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('ubicacion', models.IntegerField(blank=True, choices=[('2', 'HIDROCOOLER'), ('1', 'CUBA')], null=True)),
                ('linea', models.CharField(blank=True, max_length=5, null=True)),
                ('proceso', models.IntegerField(blank=True, null=True)),
                ('parametro', models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True)),
                ('usuini', models.CharField(blank=True, max_length=60, null=True)),
                ('usufin', models.CharField(blank=True, max_length=60, null=True)),
                ('fecha', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'public"."eventos_parecetico_l3',
                'permissions': (('reporte_parecetico', 'Reporte de Mediciones Parecetico'),),
                'managed': True,
            },
        ),
    ]
