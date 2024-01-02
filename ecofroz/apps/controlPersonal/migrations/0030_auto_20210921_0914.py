# Generated by Django 3.0.8 on 2021-09-21 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controlPersonal', '0029_auto_20201203_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaregistro',
            options={'managed': True, 'ordering': ['-ord'], 'permissions': (('registro_personal', 'Registros de Personal'), ('reporte_ingresos', 'Reporte de Ingresos'), ('busqueda_rapida', 'Busqueda Rapida'), ('registro_ac', 'Registros de Personal Agua Clara'), ('registro_ll', 'Registros de Personal La Laurita'), ('registro_la', 'Registros de Personal La Avelina'), ('registro_lm', 'Registros de Personal La Merced')), 'verbose_name': 'Registro Persona', 'verbose_name_plural': 'Registros Personas'},
        ),
    ]
