from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.indexpage, name="frontpage"),
    path("insert/", views.inserdata, name="insert"),
]