# Generated by Django 3.0.8 on 2022-06-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parametrosGlobales', '0011_auto_20220601_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_notificacion',
            name='nombre_abreviado',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
