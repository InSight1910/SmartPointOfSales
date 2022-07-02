from django.urls import path, include
from .views import (
    getDetalleVentaById,
    getMedioPagoById,
    getVentaById,
    homeDetalleVenta,
    homeMedioPago,
    homeVenta,
)

urlpatterns = [
    path("venta", homeVenta),
    path("venta/<id>", getVentaById),
    path("detalleVenta", homeDetalleVenta),
    path("detalleVenta/<id>", getDetalleVentaById),
    path("medioPago", homeMedioPago),
    path("medioPago/<id>", getMedioPagoById),
]
