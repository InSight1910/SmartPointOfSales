from rest_framework import serializers
from .models import DetalleVenta, MedioPago, Venta


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ["id_venta", "monto", "medio_pago", "fecha", "cliente"]


class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVenta
        fields = ["id_detalle_venta", "producto", "venta"]


class MedioPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedioPago
        fields = ["id_medio_pago", "nombre"]
