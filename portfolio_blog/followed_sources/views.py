import logging
import time

from asgiref.sync import sync_to_async
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import sync_and_async_middleware
from django.views.decorators.cache import cache_page
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
    cache_key = "youtube_latest_videos"
    yt_videos = cache.get(cache_key)

    if yt_videos is None:
        logger.info("Cache miss - fetching fresh data from YouTube API")
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

        # Cache the data for 1 hour
        cache.set(cache_key, yt_videos, 60 * 60)
    else:
        logger.info("Cache hit - using cached YouTube data")

    logger.debug(f"Final video count: {len(yt_videos)}")
    return await sync_to_async(render)(
        response, "followed_sources/videos.html", {"yt_videos": yt_videos}
    )


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
