# Generated by Django 3.0.3 on 2022-04-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0038_auto_20220418_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'permissions': (('procesos', 'Procesos'), ('desecho', 'Desecho'), ('ingresa_solicitud_desecho', 'Ingresa Solicitudes Desecho'), ('autoriza_1n_desecho', 'Autoriza Solicitudes Desecho'), ('autoriza_1n_donacion', 'Autoriza Solicitudes Donaciones'), ('autoriza_2n_desecho', 'Autoriza Seguridad Solicitudes Desecho'), ('salida_desecho_guardias', 'Salida Desecho Guardias'), ('reporte_general_desecho', 'Reporte General Desecho'), ('materia_prima', 'Materia Prima'), ('inspeccion_materia_prima', 'Inspección Materia Prima'), ('ingreso_parametros_cl', 'Ingreso de Parametros CL'), ('ingreso_programacion_cl', 'Ingreso de Programación CL'), ('documento_cl', 'Control de Limpieza'))},
        ),
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(3, 'Salida Activos'), (2, 'Secundario'), (1, 'Principal')], null=True),
        ),
    ]
