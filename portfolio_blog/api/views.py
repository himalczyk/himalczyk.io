from django.shortcuts import render
from api.youtube_api import YoutubeApi
from api.config import YT_BASE_URL, YOUTUBE_CHANNELS
from api.web_scraper import scrape_rp_image_uri

# Create your views here.
def api_home(response):
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    yt_videos = yt_api.get_youtube_urls()
    rp_post_uri = scrape_rp_image_uri()[1]
    print(rp_post_uri)
    rp_post_image = str(scrape_rp_image_uri()[0])
    print(rp_post_image)
    video = {
        "yt_videos" : yt_videos,
        "image" : rp_post_image,
        "uri" : rp_post_uri,
    }
    return render(response, 'api/api_home.html', video)