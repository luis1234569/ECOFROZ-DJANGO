# Generated by Django 3.0 on 2020-04-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multipleOrdenPedido', '0003_auto_20200428_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenespedidosmulti',
            name='cotiza_ref',
            field=models.FileField(blank=True, null=True, upload_to='cotizaciones/', verbose_name='Cotización Referencial'),
        ),
        migrations.AlterField(
            model_name='detallepedidomulti',
            name='tiempo_tipo',
            field=models.CharField(choices=[('mes', 'Meses'), ('dia', 'Dias'), ('anio', 'Años'), ('semana', 'Semanas'), ('hora', 'Horas')], max_length=7),
        ),
        migrations.AlterField(
            model_name='detallepedidomulti',
            name='unimedida',
            field=models.CharField(blank=True, choices=[('unidad', 'U')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[(1, 'Aprobado'), ('', 'Pendiente'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='motivo_compra',
            field=models.CharField(blank=True, choices=[('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo'), ('reemplazo_m', 'Reemplazo por Mejora')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidosmulti',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(1, 'Dada de Baja'), (3, 'Backup'), (4, 'Reparación'), (2, 'Reubicación')], null=True),
        ),
    ]
