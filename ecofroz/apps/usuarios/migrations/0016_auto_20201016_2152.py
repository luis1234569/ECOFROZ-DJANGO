# Generated by Django 3.0.7 on 2020-10-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0015_auto_20201012_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(2, 'Secundario'), (1, 'Principal')], null=True),
        ),
    ]
