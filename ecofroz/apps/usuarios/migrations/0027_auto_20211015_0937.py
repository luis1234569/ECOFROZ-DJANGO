# Generated by Django 3.0.8 on 2021-10-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0026_auto_20210528_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Principal'), (2, 'Secundario'), (3, 'Salida Activos')], null=True),
        ),
    ]
