# Generated by Django 3.2.15 on 2023-10-20 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0051_auto_20221028_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='activo_estado_oc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='activo_only_control', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='empleado_cod',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Principal'), (2, 'Secundario'), (3, 'Salida Activos')], null=True),
        ),
        migrations.AlterField(
            model_name='roles',
            name='estado',
            field=models.IntegerField(blank=True, choices=[(0, 'Inactivo'), (1, 'Activo')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
