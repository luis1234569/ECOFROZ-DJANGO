# Generated by Django 3.0.8 on 2021-09-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0049_auto_20210823_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='descripcion',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), ('', 'Pendiente'), (2, 'Anulada'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(2, 'Reubicación'), (1, 'Dada de Baja'), (5, 'Venta'), (4, 'Reparación'), (3, 'Backup')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('dia', 'Dias'), ('anio', 'Años'), ('hora', 'Horas'), ('mes', 'Meses')], max_length=7),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), ('', 'Pendiente'), (2, 'Anulada'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(2, 'Reubicación'), (1, 'Dada de Baja'), (5, 'Venta'), (4, 'Reparación'), (3, 'Backup')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('dia', 'Dias'), ('anio', 'Años'), ('hora', 'Horas'), ('mes', 'Meses')], max_length=7),
        ),
    ]
