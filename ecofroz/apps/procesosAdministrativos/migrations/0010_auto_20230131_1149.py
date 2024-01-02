# Generated by Django 3.0.8 on 2023-01-31 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0009_auto_20230131_1143'),
    ]

    operations = [
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
    ]
