from config import YT_API_KEY

#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse
import scrapetube

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = YT_API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part='id,snippet',
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                    search_result['id']['playlistId']))

  print('Videos:\n', '\n'.join(videos), '\n')
  print('Channels:\n', '\n'.join(channels), '\n')
  print('Playlists:\n', '\n'.join(playlists), '\n')




if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--q', help='Search term', default='Freecodecamp')
  parser.add_argument('--max-results', help='Max results', default=25)
  args = parser.parse_args()

  try:
    youtube_search(args)
  except HttpError as e:
    print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    
    
    
# YOUTUBE_CHANNELS = ['UC8butISFwT-Wl7EV0hUK0BQ', 'UCVhQ2NnY5Rskt6UjCUkJ_DA', 'UC4JX40jDee_tINbkjycV4Sg', 'UCCezIgC97PvUuR4_gbFUs5g']

# https://www.googleapis.com/youtube/v3/search?key={your_key_here}&channelId={channel_id_here}&part=snippet,id&order=date&maxResults=20

# yt_channel_videos = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyC8ZB7s9cjNFT4zwUTSxvuulhwEZJPNuHI&channelId=UC8butISFwT-Wl7EV0hUK0BQ&part=snippet,id&order=date&maxResults=1')

# response = yt_channel_videos.json()
# video_urls = []
# for youtube_channel_id in YOUTUBE_CHANNELS:
#     yt_channel_video = requests.get(f'https://www.googleapis.com/youtube/v3/search?key=AIzaSyC8ZB7s9cjNFT4zwUTSxvuulhwEZJPNuHI&channelId={youtube_channel_id}&part=snippet,id&order=date&maxResults=1')
#     response = yt_channel_video.json()
#     for i in response['items']:
#         video_urls.append(i['id']['videoId'])
# print(video_urls)
# for i in response['items']:
#     video_urls.append(i['id']['videoId'])
# print(video_urls)
# for youtube_channel_id in YOUTUBE_CHANNELS:
#     channel_videos = scrapetube.get_channel(channel_id = youtube_channel_id)
#     print(next(channel_videos))

# WORKING    
# yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
# print(yt_api.get_youtube_urls())


#FreeCodeCamp
# video = scrapetube.get_channel("UC8butISFwT-Wl7EV0hUK0BQ")
# first_video = next(video)


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
