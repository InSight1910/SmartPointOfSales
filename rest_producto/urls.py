from django.urls import path, include
from .views import getAll, getById

urlpatterns = [
    path("", getAll),
    path("<id>", getById),
]
