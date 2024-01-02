# Generated by Django 3.0 on 2020-04-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0012_auto_20200403_0803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallepedido',
            options={'managed': True, 'permissions': (('menu_bodega', 'Acceso al menu de bodega'),), 'verbose_name': 'Detalle Pedido', 'verbose_name_plural': 'Detalles Pedidos'},
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (0, 'No Aprobado'), (1, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(blank=True, choices=[('reemplazo_o', 'Reemplazo por Obsolescencia'), ('reemplazo_m', 'Reemplazo por Mejora'), ('nuevo', 'Nuevo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(3, 'Backup'), (2, 'Reubicación'), (4, 'Reparación'), (1, 'Dada de Baja')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('hora', 'Horas'), ('dia', 'Dias'), ('semana', 'Semanas'), ('mes', 'Meses'), ('anio', 'Años')], max_length=7),
        ),
    ]
