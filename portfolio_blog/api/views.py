from django.shortcuts import render
from api.youtube_api import YoutubeApi
from api.config import YT_BASE_URL, YOUTUBE_CHANNELS, RP_PODCAST_BASE_URL
from api.web_scraper import scrape_rp_latest_tutorial, scrape_rp_podcast, scrape_latest_rp_podcast_episode


def api_home(response):
    """Followed sources content main page -> Real Python Article sub view"""
    rp_post_uri = scrape_rp_latest_tutorial()[1]
    rp_post_image = str(scrape_rp_latest_tutorial()[0])
    rp_post_image_alt = str(scrape_rp_latest_tutorial()[2])
    rp_post_description = str(scrape_rp_latest_tutorial()[3])
    blog_post = {
        "image" : rp_post_image,
        "uri" : rp_post_uri,
        "alt" : rp_post_image_alt,
        "description" : rp_post_description,
    }
    return render(response, "api/api_home.html", blog_post)


def yt_video_index(response):
    """Videos sub-page in followed sources content page"""
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    yt_videos = yt_api.get_youtube_urls()
    video = {
        "yt_videos" : yt_videos,
    }
    return render(response, "api/yt_video_index.html", video)


def podcasts(response):
    """Podcasts sub page in followed sources content page"""
    rp_podcast = scrape_rp_podcast()
    latest_episode_title = scrape_latest_rp_podcast_episode()[0]
    latest_episode_url = scrape_latest_rp_podcast_episode()[1]
    # not used right now
    latest_episode_description = scrape_latest_rp_podcast_episode()[2]
    podcast = {
        "rp_podcast" : rp_podcast,
        "rp_podcast_base_url" : RP_PODCAST_BASE_URL,
        "uri" : latest_episode_url,
        "alt" : latest_episode_title,
        "description" : latest_episode_description,
    }
    return render(response, "api/podcasts.html", podcast)