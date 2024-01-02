# Generated by Django 3.0.8 on 2023-05-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0015_auto_20230502_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='desc_evento',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='eventosclorol2',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eventospareceticol3',
            name='parametro',
            field=models.CharField(blank=True, choices=[('1', 'CORRECTO'), ('2', 'OBSERVACION')], max_length=20, null=True),
        ),
    ]
