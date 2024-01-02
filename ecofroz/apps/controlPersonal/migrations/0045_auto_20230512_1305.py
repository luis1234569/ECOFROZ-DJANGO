# Generated by Django 3.0.8 on 2023-05-12 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0044_auto_20221024_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'managed': True, 'permissions': (('menu_ecofroz', 'Acceso Menu Ecofroz'), ('persona_directorio', 'Directorio de Personal'), ('capacitacion', 'Capacitacion'), ('capacitacion_guardias', 'Capacitación Guardianía'), ('gpt', 'Chat GPT')), 'verbose_name': 'Persona', 'verbose_name_plural': 'Personas'},
        ),
    ]
