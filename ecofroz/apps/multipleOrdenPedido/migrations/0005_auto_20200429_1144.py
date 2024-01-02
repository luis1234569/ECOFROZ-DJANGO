# Generated by Django 3.0 on 2020-04-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipleOrdenPedido', '0004_auto_20200429_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedidomulti',
            name='tiempo_tipo',
            field=models.CharField(choices=[('semana', 'Semanas'), ('anio', 'Años'), ('hora', 'Horas'), ('mes', 'Meses'), ('dia', 'Dias')], max_length=7),
        ),
        migrations.AlterField(
            model_name='detallepedidomulti',
            name='unimedida',
            field=models.CharField(blank=True, choices=[('unidad', 'U')], default='unidad', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (0, 'No Aprobado'), (1, 'Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='motivo_compra',
            field=models.CharField(blank=True, choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('nuevo', 'Nuevo'), ('reemplazo_o', 'Reemplazo por Obsolescencia')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(4, 'Reparación'), (2, 'Reubicación'), (3, 'Backup'), (1, 'Dada de Baja')], null=True),
        ),
    ]
