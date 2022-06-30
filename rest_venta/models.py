from django.db import models

from rest_cliente.models import Cliente
from rest_producto.models import Producto

# Create your models here.
class MedioPago(models.Model):
    id_medio_pago = models.AutoField(
        "Identificador del medio de pago", primary_key=True
    )
    nombre = models.CharField("Nombre del medio de pago", max_length=25, null=False)

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    id_venta = models.AutoField(
        verbose_name="Identificador de la venta", primary_key=True, null=False
    )
    monto = models.IntegerField("Monto total", null=False)
    medio_pago = models.ForeignKey(
        MedioPago, on_delete=models.CASCADE, verbose_name="Fecha de la venta"
    )
    fecha = models.CharField("Fecha de la venta", max_length=10, null=False)
    cliente = models.ForeignKey(
        Cliente, verbose_name="Identificador del cliente", on_delete=models.CASCADE
    )


class DetalleVenta(models.Model):
    id_detalle_venta = models.AutoField(
        "Identificador del detalle de venta", primary_key=True
    )
    producto = models.ForeignKey(
        Producto, verbose_name="Identificador del producto", on_delete=models.CASCADE
    )
    venta = models.ForeignKey(
        Venta,
        verbose_name="Identificador de la venta",
        on_delete=models.CASCADE,
        null=True,
    )
