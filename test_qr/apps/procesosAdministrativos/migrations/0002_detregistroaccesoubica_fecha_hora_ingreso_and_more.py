# Generated by Django 5.0.1 on 2024-01-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procesosAdministrativos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detregistroaccesoubica',
            name='fecha_hora_ingreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cabregistroaccesoubica',
            name='completado',
            field=models.IntegerField(choices=[(3, 'Incompleto'), (1, 'Completo'), (2, 'No Registrado'), (0, 'Pendiente')], default=0),
        ),
        migrations.AlterField(
            model_name='detregistroaccesoubica',
            name='completado',
            field=models.IntegerField(choices=[(3, 'Incompleto'), (1, 'Completo'), (2, 'No Registrado'), (0, 'Pendiente')], default=0),
        ),
    ]
