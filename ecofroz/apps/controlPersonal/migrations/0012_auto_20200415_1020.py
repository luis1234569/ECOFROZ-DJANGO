# Generated by Django 3.0 on 2020-04-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0011_auto_20200413_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenedorregistro',
            name='sello_1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contenedorregistro',
            name='sello_2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
