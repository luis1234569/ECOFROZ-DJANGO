# Generated by Django 3.0.7 on 2020-08-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0018_persona_estado_al'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaregistro',
            name='ubica',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='vehiculoregistro',
            name='ubica',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
