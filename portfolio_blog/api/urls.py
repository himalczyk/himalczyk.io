from django.urls import path, include
from . import views

urlpatterns = [
    path("api/", views.api_home, name="api_home"),
    path("rp_tutorial/", views.rp_article_index, name="rp_article_index"),
    path("yt_channel_tutorials/", views.yt_video_index, name="yt_video_index"),
]