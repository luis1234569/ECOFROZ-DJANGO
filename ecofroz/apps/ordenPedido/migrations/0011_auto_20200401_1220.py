# Generated by Django 3.0 on 2020-04-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0010_auto_20200311_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenespedidos',
            name='observa_compra',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(0, 'No Aprobado'), (1, 'Aprobado'), ('', 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(blank=True, choices=[('nuevo', 'Nuevo'), ('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_o', 'Reemplazo por Obsolescencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('anio', 'Años'), ('dia', 'Dias'), ('mes', 'Meses'), ('hora', 'Horas'), ('semana', 'Semanas')], max_length=7),
        ),
    ]
