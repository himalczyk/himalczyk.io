from django.urls import path
from . import views

urlpatterns = [
    path("tutorial/", views.tutorial, name="tutorial")
]