from django.urls import path, include
from . import views

urlpatterns = [
    path("followed_sources/", views.followed_sources_home, name="followed_sources_home"),
    path("podcasts/", views.podcasts, name="podcasts"),
    path("articles/", views.rp_articles, name="rp_articles"),
    path("videos/", views.yt_video_index, name="yt_video_index"),
]