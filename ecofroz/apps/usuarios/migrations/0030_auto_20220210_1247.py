# Generated by Django 3.0.8 on 2022-02-10 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0029_auto_20220210_1236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'permissions': (('procesos', 'Procesos'), ('desecho', 'Desecho'), ('autoriza_1n_desecho', 'Autoriza Solicitudes Desecho'), ('autoriza_2n_desecho', 'Autoriza Seguridad Solicitudes Desecho'), ('salida_desecho_guardias', 'Salida Desecho Guardias'))},
        ),
    ]
