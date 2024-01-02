# Generated by Django 3.0.8 on 2022-03-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0033_auto_20220222_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='guardia',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(2, 'Secundario'), (1, 'Principal'), (3, 'Salida Activos')], null=True),
        ),
    ]
