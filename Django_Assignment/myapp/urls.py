from django.urls import path, include
from .import views

urlpatterns = [
    path("", views.task_list, name="tasklist"),
]