# Generated by Django 3.0 on 2020-10-19 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0017_auto_20201019_1509'),
        ('controlPersonal', '0022_auto_20200901_0902'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaregistro',
            options={'managed': True, 'ordering': ['-ord'], 'permissions': (('registro_personal', 'Registros de Personal'), ('reporte_ingresos', 'Reporte de Ingresos'), ('registro_ac', 'Registros de Personal Agua Clara'), ('registro_ll', 'Registros de Personal La Laurita'), ('registro_la', 'Registros de Personal La Avelina')), 'verbose_name': 'Registro Persona', 'verbose_name_plural': 'Registros Personas'},
        ),
        migrations.AlterField(
            model_name='persona',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.Areas'),
        ),
    ]
