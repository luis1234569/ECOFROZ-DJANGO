# Generated by Django 3.0.7 on 2021-02-05 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_auto_20210201_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizador',
            name='status',
            field=models.BooleanField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='cotizador',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarioseleccionacotiza', to=settings.AUTH_USER_MODEL),
        ),
    ]
