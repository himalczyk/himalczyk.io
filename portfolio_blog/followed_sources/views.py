import logging

from django.shortcuts import render
from followed_sources.config import (
    RP_PODCAST_BASE_URL,
    YOUTUBE_CHANNELS,
    YT_BASE_URL,
    YT_VIDEOS_API_LIMIT_REACHED,
)
from followed_sources.utils import current_year
from followed_sources.web_scraper import (
    scrape_latest_rp_podcast_episode,
    scrape_rp_latest_tutorial,
    scrape_rp_podcast,
)
from followed_sources.youtube_api import YoutubeApi

logger = logging.getLogger(__name__)


def rp_articles(response):
    """Real Python videos fetching sub-page re-direction"""
    rp_post_data = scrape_rp_latest_tutorial()
    blog_post = {
        "image": rp_post_data["image"],
        "uri": rp_post_data["uri"],
        "title": rp_post_data["title"],
        "description": rp_post_data["description"],
        "current_year": current_year,
    }
    return render(response, "followed_sources/articles_and_home.html", blog_post)


async def yt_video_index(response):
    """Videos sub-page in followed sources content page"""
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    try:
        logger.info("Fetching YouTube videos")
        yt_videos = await yt_api.get_youtube_urls()
        logger.debug(f"yt_videos: {yt_videos}")

        if not yt_videos or all(video is None for video in yt_videos):
            logger.warning("No valid videos returned from API, using fallback data")
            yt_videos = YT_VIDEOS_API_LIMIT_REACHED
    except Exception as e:
        logger.warning(f"YouTube API error, using fallback data. Error: {e}")
        yt_videos = YT_VIDEOS_API_LIMIT_REACHED

    logger.debug(f"Final video count: {len(yt_videos)}")
    return render(response, "followed_sources/videos.html", {"yt_videos": yt_videos})


def podcasts(response):
    """Podcasts sub page in followed sources content page"""
    rp_podcast = scrape_rp_podcast()
    rp_latest_episode_data = scrape_latest_rp_podcast_episode()
    podcast = {
        "rp_podcast": rp_podcast,
        "rp_podcast_base_url": RP_PODCAST_BASE_URL,
        "uri": rp_latest_episode_data["uri"],
        "alt": rp_latest_episode_data["title"],
        "description": rp_latest_episode_data["description"],
        "current_year": current_year,
    }
    return render(response, "followed_sources/podcasts.html", podcast)
