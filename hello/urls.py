from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.helloWorldHTML),
    path("contact", views.contactUs)
]
