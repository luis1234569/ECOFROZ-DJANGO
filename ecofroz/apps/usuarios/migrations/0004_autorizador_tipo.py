# Generated by Django 3.0 on 2020-02-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20200221_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(2, 'Secundario'), (1, 'Principal')], null=True),
        ),
    ]
