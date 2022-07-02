from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializer import ProductSerializer
from .models import Producto
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def getAll(request: HttpRequest):
    if request.method == "GET":
        producto = Producto.objects.all()
        serializer = ProductSerializer(producto, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        producto = ProductSerializer(data=data)
        if producto.is_valid():
            producto.save()
            print(producto.data)
            return Response(
                producto.data.get("id_producto"), status=status.HTTP_201_CREATED
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def getById(request: HttpRequest, id):
    try:
        producto = Producto.objects.get(id_producto=id)
        JSONParser()
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(producto)
    return Response(serializer.data, status=status.HTTP_200_OK)
