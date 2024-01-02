# Generated by Django 3.0.8 on 2022-01-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0054_auto_20211216_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenespedidos',
            name='custodio_sugerido',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='ordenespedidos',
            name='descargo_custodio',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(2, 'SIA'), (1, 'MBA'), (3, 'RESERVA')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (2, 'Anulada'), (0, 'No Aprobado'), (1, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo'), ('reemplazo_r', 'Reemplazo por Reparación')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(1, 'Dada de Baja'), (4, 'Reparación'), (2, 'Reubicación'), (3, 'Backup'), (5, 'Venta')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('hora', 'Horas'), ('mes', 'Meses'), ('anio', 'Años'), ('dia', 'Dias')], max_length=7),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (2, 'Anulada'), (0, 'No Aprobado'), (1, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo'), ('reemplazo_r', 'Reemplazo por Reparación')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(1, 'Dada de Baja'), (4, 'Reparación'), (2, 'Reubicación'), (3, 'Backup'), (5, 'Venta')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('hora', 'Horas'), ('mes', 'Meses'), ('anio', 'Años'), ('dia', 'Dias')], max_length=7),
        ),
    ]
