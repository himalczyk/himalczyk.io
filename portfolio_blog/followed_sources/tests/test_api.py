import requests
from api.youtube_api import YoutubeApi
from api.config import YT_BASE_URL, YOUTUBE_CHANNELS, RP_PODCAST_BASE_URL
from api.web_scraper import scrape_rp_latest_tutorial, scrape_rp_podcast, scrape_latest_rp_podcast_episode

def test_scrape_rp_latest_tutorial():
    """Test fetching of latest tutorial works correctly and fetches all details"""
    rp_post_uri = scrape_rp_latest_tutorial()[1]
    rp_post_image = str(scrape_rp_latest_tutorial()[0])
    rp_post_image_alt = str(scrape_rp_latest_tutorial()[2])
    rp_post_description = str(scrape_rp_latest_tutorial()[3])
    
    assert rp_post_uri
    assert rp_post_image
    assert rp_post_image_alt
    assert rp_post_description
    
    
def test_scrape_rp_podcast():
    """Test fetching of the rp podcast image"""
    rp_podcast = scrape_rp_podcast()    
    
    assert rp_podcast
    
    
def test_rp_podcast_url_available():
    """Test if podcast path still available"""
    rp_podcast_page_response = requests.get(RP_PODCAST_BASE_URL)
    
    assert rp_podcast_page_response.status_code == 200
    
    
def test_scrape_latest_rp_podcast_episode():
    """Test fetching of latest rp podcast episode"""
    latest_episode_title = scrape_latest_rp_podcast_episode()[0]
    latest_episode_url = scrape_latest_rp_podcast_episode()[1]
    
    assert latest_episode_title
    assert latest_episode_url


def test_fetching_youtube_videos():
    """Test if youtube videos are still loading correctly"""
    yt_api = YoutubeApi(YT_BASE_URL, YOUTUBE_CHANNELS)
    yt_videos = yt_api.get_youtube_urls()
    
    assert yt_videos
    assert len(yt_videos) > 0