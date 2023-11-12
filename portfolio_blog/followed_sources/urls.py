from django.urls import include, path

from . import views

urlpatterns = [
    path("followed_sources/", views.rp_articles, name="rp_articles"),
    path("podcasts/", views.podcasts, name="podcasts"),
    path("articles/", views.rp_articles, name="rp_articles"),
    path("videos/", views.yt_video_index, name="yt_video_index"),
]
