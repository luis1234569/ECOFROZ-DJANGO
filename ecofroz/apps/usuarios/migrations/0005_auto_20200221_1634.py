# Generated by Django 3.0 on 2020-02-21 21:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_autorizador_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='generador',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuariogenera', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='autorizador',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, 'Principal'), (2, 'Secundario')], null=True),
        ),
    ]
