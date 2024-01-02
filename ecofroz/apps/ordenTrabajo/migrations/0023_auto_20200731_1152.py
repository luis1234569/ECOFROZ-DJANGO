# Generated by Django 3.0.7 on 2020-07-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenTrabajo', '0022_auto_20200729_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenestrabajos',
            name='fch_factura',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordenestrabajos',
            name='fch_factura_txt',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='ordenestrabajos',
            name='usuario_factura',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='tipo_pedi',
            field=models.CharField(blank=True, choices=[('OT', 'Otros Insumos'), ('PR', 'Proyecto'), ('MP', 'Mantenimiento Preventivo'), ('OS', 'Orden de Servicio'), ('MC', 'Mantenimiento Correctivo')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='ordenestrabajos',
            name='tipo_trabajo',
            field=models.IntegerField(blank=True, choices=[(2, 'Externo'), (1, 'Interno')], default=None, null=True),
        ),
    ]
