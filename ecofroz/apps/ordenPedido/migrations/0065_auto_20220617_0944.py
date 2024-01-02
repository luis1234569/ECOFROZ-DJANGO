# Generated by Django 3.0.8 on 2022-06-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0064_auto_20220617_0907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultaexperto',
            name='experto',
        ),
        migrations.AlterField(
            model_name='ordenespago',
            name='origen',
            field=models.IntegerField(blank=True, choices=[(1, 'MBA'), (2, 'SIA'), (3, 'RESERVA')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(0, 'No Aprobado'), ('', 'Pendiente'), (1, 'Aprobado'), (2, 'Anulada')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo'), ('reemplazo_m', 'Reemplazo por Mejora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(3, 'Backup'), (1, 'Dada de Baja'), (2, 'Reubicación'), (5, 'Venta'), (4, 'Reparación')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_vida',
            field=models.IntegerField(choices=[(19, '19'), (18, '18'), (7, '7'), (10, '10'), (1, '1'), (9, '9'), (11, '11'), (20, '20'), (4, '4'), (8, '8'), (16, '16'), (14, '14'), (2, '2'), (15, '15'), (12, '12'), (13, '13'), (3, '3'), (6, '6'), (17, '17'), (5, '5')]),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(0, 'No Aprobado'), ('', 'Pendiente'), (1, 'Aprobado'), (2, 'Anulada')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo'), ('reemplazo_m', 'Reemplazo por Mejora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(3, 'Backup'), (1, 'Dada de Baja'), (2, 'Reubicación'), (5, 'Venta'), (4, 'Reparación')], null=True),
        ),
    ]
