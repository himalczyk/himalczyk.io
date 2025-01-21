"""Module that is fetching the latest videos from pre-defined followed channel ids"""

import asyncio
import platform

import aiohttp
import requests

if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import os

YT_API_KEY = os.getenv("YT_API_KEY")


class YoutubeApi:
    """A class to retrieve and create direct video urls from latest published videos for channels"""

    def __init__(self, yt_base_url: str, yt_channels: list):
        self.yt_base_url = yt_base_url
        self.yt_channels = yt_channels

    async def get_youtube_urls(self) -> list:
        """Handler function to provide the direct youtube urls list"""
        # video_ids = self.get_latest_youtube_channel_videos(self.yt_channels)
        video_ids = await self.get_latest_youtube_channel_videos(self.yt_channels)
        direct_video_urls = self.create_youtube_direct_video_url(video_ids)

        return direct_video_urls

    def create_youtube_direct_video_url(self, video_ids: list) -> list:
        """Create direct video urls list with base url and video id"""
        video_urls = []
        for video_id in video_ids:
            video_urls.append(f"{self.yt_base_url}{video_id}")
        return video_urls

    async def get_latest_youtube_channel_videos(self, YOUTUBE_CHANNELS: list) -> list:
        """Concurrent youtube api calls to get latest video'ids for the provided list of Youtube Channel ids"""
        async with aiohttp.ClientSession() as session:
            urls = [
                f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
                for youtube_channel_id in YOUTUBE_CHANNELS
            ]
            video_ids = await asyncio.gather(*[self.get(url, session) for url in urls])
            return video_ids

    async def get(self, url, session):
        """Getter function for the get_latest_youtube_channel_videos async"""
        async with session.get(url=url) as response:
            resp = await response.json()
            return resp["items"][0]["id"]["videoId"]

    def _backup_get_latest_youtube_channel_videos(
        self, youtube_channel_ids: list
    ) -> list:
        """Get latest two video identifiers from pre-defined youtube channel list"""
        video_ids = []
        for youtube_channel_id in youtube_channel_ids:
            yt_channel_video = requests.get(
                f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
            )
            response = yt_channel_video.json()
            for i in response["items"]:
                video_ids.append(i["id"]["videoId"])

        return video_ids

    def get_latest_youtube_channel_videos(self, youtube_channel_ids: list) -> list:
        """Get latest two video identifiers from pre-defined youtube channel list"""
        video_ids = []
        for youtube_channel_id in youtube_channel_ids:
            yt_channel_video = requests.get(
                f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1"
            )
            response = yt_channel_video.json()
            for i in response["items"]:
                video_ids.append(i["id"]["videoId"])

        return video_ids
