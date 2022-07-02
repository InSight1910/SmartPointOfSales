from django.shortcuts import render
from rest_framework.request import HttpRequest
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST"])
def login(request: HttpRequest):
    try:
        data = JSONParser().parse(request)
        username = data["username"]
        password = data["password"]
    except Exception as e:
        return Response(
            "Campos Username y Password requeridos", status=status.HTTP_400_BAD_REQUEST
        )
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario no existe", status=status.HTTP_404_NOT_FOUND)
    passValid = check_password(password, user.password)
    if not passValid:
        return Response("Password incorrecta", status=status.HTTP_401_UNAUTHORIZED)
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key, status=status.HTTP_200_OK)
