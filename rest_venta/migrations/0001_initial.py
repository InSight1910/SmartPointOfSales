# Generated by Django 4.0.5 on 2022-06-30 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rest_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedioPago',
            fields=[
                ('id_medio_pago', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del medio de pago')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre del medio de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador de la venta')),
                ('monto', models.IntegerField(verbose_name='Monto total')),
                ('fecha', models.CharField(max_length=10, verbose_name='Fecha de la venta')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_cliente.cliente', verbose_name='Identificador del cliente')),
                ('medio_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_venta.mediopago', verbose_name='Fecha de la venta')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle_venta', models.AutoField(primary_key=True, serialize=False, verbose_name='Identificador del detalle de venta')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_venta.venta', verbose_name='Identificador de la venta')),
            ],
        ),
    ]
