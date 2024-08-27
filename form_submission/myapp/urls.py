from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.showindex, name="indexpage"),
    path("insert/", views.InserData, name="insert"),
]