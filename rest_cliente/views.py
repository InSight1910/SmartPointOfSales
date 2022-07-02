import re
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.request import HttpRequest
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from .serializer import ClienteSerializer
from .models import Cliente

# Create your views here.
@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def getAll(request: HttpRequest):
    if request.method == "GET":
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = JSONParser().parse(request)
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(
                serializer.data.get("id_cliente"), status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(["GET"])
def getById(request: HttpRequest, id):
    try:
        cliente = Cliente.objects.get(id_cliente=id)
    except Cliente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClienteSerializer(cliente)
    return Response(serializer.data, status=status.HTTP_200_OK)
