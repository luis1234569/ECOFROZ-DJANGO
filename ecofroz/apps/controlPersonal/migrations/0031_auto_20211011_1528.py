# Generated by Django 3.0.8 on 2021-10-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0030_auto_20210921_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='autorizado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='fch_ingreso',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
