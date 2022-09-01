"""Module that is scraping the latest videos from pre-defined followed channel ids"""

from bs4 import BeautifulSoup
import requests

class YoutubeApi():
    """A class to retrieve and create direct video urls from latest published videos for channels"""
    def __init__(self, yt_base_url: str, yt_channels: list):
        self.yt_base_url = yt_base_url
        self.yt_channels = yt_channels
        
    
