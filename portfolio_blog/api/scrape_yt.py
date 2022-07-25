import argparse

import scrapetube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import YT_API_KEY, YOUTUBE_CHANNELS, YT_BASE_URL


class YoutubeApi():
    """A class to retrieve and create direct video urls from latest published videos for channels"""
    def __init__(self, yt_base_url):
        self.yt_base_url = yt_base_url
        
        
    def get_youtube_urls(self) -> list:
        """Handler function to provide the direct youtube urls list"""
        video_ids = self.get_latest_youtube_channel_videos(YOUTUBE_CHANNELS)
        direct_video_urls = self.create_youtube_direct_video_url(video_ids)
        
        return direct_video_urls


    def get_latest_youtube_channel_videos(self, youtube_channel_ids: list) -> list:
        """Get latest two video identifiers from pre-defined youtube channel list"""
        video_ids = []
        for youtube_channel_id in youtube_channel_ids:
            channel_videos = scrapetube.get_channel(youtube_channel_id)
            for video in list(channel_videos)[:1]:
                video_ids.append(video['videoId'])
            
        return video_ids


    def create_youtube_direct_video_url(self, video_ids: list) -> list:
        """Create direct video urls list with base url and video id"""
        video_urls = []
        for video_id in video_ids:
            video_urls.append(f'{self.yt_base_url}{video_id}')
        return video_urls
        
yt_api = YoutubeApi(YT_BASE_URL)
print(yt_api.get_youtube_urls())



#FreeCodeCamp
# videos = scrapetube.get_channel("UC8butISFwT-Wl7EV0hUK0BQ")
# for video in list(videos)[:10]:
#     print(video['videoId'])

#ArjanCodes
# UCVhQ2NnY5Rskt6UjCUkJ_DA
# videos = scrapetube.get_channel("UCVhQ2NnY5Rskt6UjCUkJ_DA")

#TechWithTim
# UC4JX40jDee_tINbkjycV4Sg
# videos = scrapetube.get_channel("UC4JX40jDee_tINbkjycV4Sg")

#Corey Schafer
# UCCezIgC97PvUuR4_gbFUs5g
# videos = scrapetube.get_channel("UCCezIgC97PvUuR4_gbFUs5g")
# for video in list(videos)[:10]:
#     print(video['videoId'])
    

# VIDEO_URL = ''
# YT_BASE_URL = 'https://www.youtube.com/watch?v='
# YT_VIDEO_URL = f'{YT_BASE_URL}{VIDEO_URL}'

# DEVELOPER_KEY = YT_API_KEY
# YOUTUBE_API_SERVICE_NAME = 'youtube'
# YOUTUBE_API_VERSION = 'v3'


# def youtube_search_channel_details(channel_name):
#     youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
#                     developerKey=DEVELOPER_KEY)

#     # Call the search.list method to retrieve results matching the specified
#     # query term.
#     search_response = youtube.search().list(
#         q=channel_name,
#         part='id,snippet',
#     ).execute()

#     channel = {}

#     # Add each result to the appropriate list, and then display the lists of
#     # matching videos, channels, and playlists.
#     for search_result in search_response.get('items', []):
#         if search_result['id']['kind'] == 'youtube#channel':
#             channel['title'] = search_result['snippet']['title']
#             channel['channel_id'] = search_result['id']['channelId']
                                         
#     return channel


# if __name__ == '__main__':

#     try:
#         print(youtube_search_channel_details('Corey Schafer'))
#     except HttpError as e:
#         print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
