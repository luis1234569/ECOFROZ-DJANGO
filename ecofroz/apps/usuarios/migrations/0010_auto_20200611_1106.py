# Generated by Django 3.0 on 2020-06-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_auto_20200318_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Principal'), (2, 'Secundario')], null=True),
        ),
    ]
