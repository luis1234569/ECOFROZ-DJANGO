# Generated by Django 3.0 on 2020-05-19 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0013_persona_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='chofer',
            name='observaciones',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
