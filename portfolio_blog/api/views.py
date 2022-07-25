from django.shortcuts import render
from api.youtube_api import YoutubeApi
from api.config import YT_BASE_URL, YOUTUBE_CHANNELS

# Create your views here.
def api_home(response):
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    yt_videos = yt_api.get_youtube_urls()
    video = {
        "yt_videos" : yt_videos
    }
    return render(response, 'api/api_home.html', video)