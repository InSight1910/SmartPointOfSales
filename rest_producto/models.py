from pydoc import describe
from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(
        verbose_name="Identificador del producto", primary_key=True
    )
    nombre = models.CharField("Nombre del producto", max_length=100, null=True)
    descripcion = models.CharField("Descripcion del producto", max_length=250)
    precio = models.IntegerField("Precio del producto")

    def __str__(self) -> str:
        return self.nombre
