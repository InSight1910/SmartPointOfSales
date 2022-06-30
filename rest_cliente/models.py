from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(
        verbose_name="Identificador del cliente", primary_key=True
    )
    nombre = models.CharField("Nombre del cliente", max_length=100, null=True)
    apellido = models.CharField("Apellido del cliente", max_length=150, null=True)
    correo = models.CharField("Correo del cliente", max_length=200, null=True)
    direccion = models.CharField("Direccion del cliente", max_length=200)

    def __str__(self) -> str:
        return self.nombre
