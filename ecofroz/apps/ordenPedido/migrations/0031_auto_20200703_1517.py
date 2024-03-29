# Generated by Django 3.0.7 on 2020-07-03 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0030_auto_20200702_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenespedidos',
            name='grupo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordenespedidos',
            name='ubica',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('nuevo', 'Nuevo'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('reemplazo_m', 'Reemplazo por Mejora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(1, 'Dada de Baja'), (2, 'Reubicación'), (3, 'Backup'), (4, 'Reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('anio', 'Años'), ('mes', 'Meses'), ('dia', 'Dias'), ('hora', 'Horas')], max_length=7),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('nuevo', 'Nuevo'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('reemplazo_m', 'Reemplazo por Mejora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(1, 'Dada de Baja'), (2, 'Reubicación'), (3, 'Backup'), (4, 'Reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('anio', 'Años'), ('mes', 'Meses'), ('dia', 'Dias'), ('hora', 'Horas')], max_length=7),
        ),
    ]
