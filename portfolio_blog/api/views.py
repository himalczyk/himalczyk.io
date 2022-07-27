from django.shortcuts import render
from api.youtube_api import YoutubeApi
from api.config import YT_BASE_URL, YOUTUBE_CHANNELS
from api.web_scraper import scrape_rp_image_uri

# Create your views here.
def api_home(response):
    return render(response, 'api/api_home.html', {})

def yt_video_index(response):
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    yt_videos = yt_api.get_youtube_urls()
    video = {
        "yt_videos" : yt_videos,
    }
    return render(response, "api/yt_video_index.html", video)

def rp_article_index(response):
    rp_post_uri = scrape_rp_image_uri()[1]
    rp_post_image = str(scrape_rp_image_uri()[0])
    rp_post_image_alt = str(scrape_rp_image_uri()[2])
    blog_post = {
        "image" : rp_post_image,
        "uri" : rp_post_uri,
        "alt" : rp_post_image_alt,
    }
    return render(response, "api/rp_article_index.html", blog_post)