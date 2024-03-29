# Generated by Django 3.0 on 2020-06-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipleOrdenPedido', '0005_auto_20200429_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedidomulti',
            name='tiempo_tipo',
            field=models.CharField(choices=[('anio', 'Años'), ('hora', 'Horas'), ('dia', 'Dias'), ('semana', 'Semanas'), ('mes', 'Meses')], max_length=7),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), (0, 'No Aprobado'), ('', 'Pendiente')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(2, 'Reubicación'), (4, 'Reparación'), (1, 'Dada de Baja'), (3, 'Backup')], null=True),
        ),
    ]
