# Generated by Django 3.0.7 on 2020-07-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenPedido', '0032_auto_20200708_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecuencialCodifica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=1)),
                ('numeracion', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Codificación Secuencial',
                'verbose_name_plural': 'Codificaciones Secuenciales',
                'db_table': 'activos"."secuencialcodifica',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (1, 'Aprobado'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(4, 'Reparación'), (1, 'Dada de Baja'), (2, 'Reubicación'), (3, 'Backup')], null=True),
        ),
        migrations.AlterField(
            model_name='ordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('anio', 'Años'), ('hora', 'Horas'), ('semana', 'Semanas'), ('mes', 'Meses'), ('dia', 'Dias')], max_length=7),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='aprobado',
            field=models.IntegerField(blank=True, choices=[('', 'Pendiente'), (1, 'Aprobado'), (0, 'No Aprobado')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='motivo_compra',
            field=models.CharField(choices=[('reemplazo_m', 'Reemplazo por Mejora'), ('reemplazo_r', 'Reemplazo por Reparación'), ('reemplazo_o', 'Reemplazo por Obsolescencia'), ('nuevo', 'Nuevo')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='reemplazo_accion',
            field=models.IntegerField(blank=True, choices=[(4, 'Reparación'), (1, 'Dada de Baja'), (2, 'Reubicación'), (3, 'Backup')], null=True),
        ),
        migrations.AlterField(
            model_name='rechazaordenespedidos',
            name='tiempo_tipo',
            field=models.CharField(choices=[('anio', 'Años'), ('hora', 'Horas'), ('semana', 'Semanas'), ('mes', 'Meses'), ('dia', 'Dias')], max_length=7),
        ),
    ]
