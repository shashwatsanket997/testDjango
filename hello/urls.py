from django.urls import path, include
from . import views

urlpatterns = [
    path("hello", views.helloWorld),
    path("hello2", views.helloWorldHTML),
]
