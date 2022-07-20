from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("about/", views.about, name="about"),
]