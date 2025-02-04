"""Module that is fetching the latest videos from pre-defined followed channel ids"""

import asyncio
import logging
import platform

import aiohttp
import requests

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os

YT_API_KEY = os.getenv("YT_API_KEY")

logger = logging.getLogger(__name__)


class YoutubeApi:
    """A class to retrieve and create direct video urls from latest published videos for channels"""

    def __init__(self, yt_base_url: str, yt_channels: list):
        self.yt_base_url = yt_base_url
        self.yt_channels = yt_channels

    async def get_youtube_urls(self) -> list:
        """Handler function to provide the direct youtube urls list"""
        videos = await self.get_latest_youtube_channel_videos(self.yt_channels)
        return videos  # Now returning the full video data list, not just URLs

    def create_youtube_direct_video_url(self, video_ids: list) -> list:
        """Create direct video urls list with base url and video id"""
        video_urls = []
        for video_id in video_ids:
            video_urls.append(f"{self.yt_base_url}{video_id}")
        return video_urls

    async def get_latest_youtube_channel_videos(self, YOUTUBE_CHANNELS: list) -> list:
        """Concurrent youtube api calls to get latest video data for the provided list of Youtube Channel ids"""
        async with aiohttp.ClientSession() as session:
            urls = [
                f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
                for youtube_channel_id in YOUTUBE_CHANNELS
            ]
            videos = await asyncio.gather(*[self.get(url, session) for url in urls])
            return videos

    async def get(self, url, session):
        """Getter function for the get_latest_youtube_channel_videos async"""
        try:
            async with session.get(url=url) as response:
                resp = await response.json()
                logger.debug(f"Response: {resp}")
                if "items" not in resp or not resp["items"]:
                    return None

                video = resp["items"][0]
                channel_id = video["snippet"]["channelId"]
                video_id = video["id"]["videoId"]

                return {
                    "url": f"{self.yt_base_url}{video_id}",
                    "youtube_url": f"https://youtube.com/watch?v={video_id}",
                    "title": video["snippet"]["title"],
                    "description": video["snippet"]["description"][:100] + "...",
                    "channel_name": video["snippet"]["channelTitle"],
                    "channel_url": f"https://youtube.com/channel/{channel_id}",
                    "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
                }
        except Exception as e:
            logger.debug(f"Error fetching video data: {e}")
            return None

    # def _backup_get_latest_youtube_channel_videos(
    #     self, youtube_channel_ids: list
    # ) -> list:
    #     """Get latest two video identifiers from pre-defined youtube channel list"""
    #     video_ids = []
    #     for youtube_channel_id in youtube_channel_ids:
    #         yt_channel_video = requests.get(
    #             f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
    #         )
    #         response = yt_channel_video.json()
    #         for i in response["items"]:
    #             video_ids.append(i["id"]["videoId"])

    #     return video_ids

    # def get_latest_youtube_channel_videos(self, youtube_channel_ids: list) -> list:
    #     """Get latest two video identifiers from pre-defined youtube channel list"""
    #     video_ids = []
    #     for youtube_channel_id in youtube_channel_ids:
    #         yt_channel_video = requests.get(
    #             f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
    #         )
    #         response = yt_channel_video.json()
    #         for i in response["items"]:
    #             video_ids.append(i["id"]["videoId"])

    #     return video_ids
