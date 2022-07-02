from django.shortcuts import render
from rest_framework.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_venta.serializer import DetalleVentaSerializer, MedioPagoSerializer, VentaSerializer
from .models import Venta, DetalleVenta, MedioPago

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def homeVenta(request: HttpRequest):
    if request.method == 'GET':
        venta = Venta.objects.all()
        serializer = VentaSerializer(venta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser(request)
        serializer = VentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.id_venta, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def getVentaById(request: HttpRequest, id_venta):
    try:
        venta = Venta.objects.get(id_venta=id_venta)
    except Venta.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = VentaSerializer(venta)
    return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET', 'POST'])
def homeDetalleVenta(request: HttpRequest):
    if request.method == 'GET':
        detalleVenta = DetalleVenta.objects.all()
        serializer = DetalleVentaSerializer(detalleVenta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser(request)
        serializer = DetalleVentaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.id_detalle_venta, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def getDetalleVentaById(request: HttpRequest, id_detalle_venta):
    try:
        detalleVenta = DetalleVenta.objects.get(id_venta=id_detalle_venta)
    except DetalleVenta.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = VentaSerializer(detalleVenta)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
def homeMedioPago(request: HttpRequest):
    if request.method == 'GET':
        medioPago = MedioPago.objects.all()
        serializer = MedioPagoSerializer(medioPago, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser(request)
        serializer = MedioPagoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data.id_medio_pago, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def getMedioPagoById(request: HttpRequest, id_medio_pago):
    try:
        medioPago = MedioPago.objects.get(id_medio_pago=id_medio_pago)
    except MedioPago.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    serializer = MedioPagoSerializer(medioPago)
    return Response(serializer.data, status=status.HTTP_200_OK)