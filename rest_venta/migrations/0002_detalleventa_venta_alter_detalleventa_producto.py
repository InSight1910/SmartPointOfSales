# Generated by Django 4.0.5 on 2022-06-30 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_producto', '0001_initial'),
        ('rest_venta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rest_venta.venta', verbose_name='Identificador de la venta'),
        ),
        migrations.AlterField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_producto.producto', verbose_name='Identificador del producto'),
        ),
    ]