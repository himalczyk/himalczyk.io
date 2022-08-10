"""This is a module having scraping data from real python blog"""

from bs4 import BeautifulSoup
import requests
from api.config import RP_BASE_URL
# testing
# from config import RP_BASE_URL

page = requests.get(RP_BASE_URL)
rp_podcast_page = requests.get(RP_BASE_URL + '/podcasts/rpp/')

# passing in page.content instead of page.text to avoid problem with character encoding.
def scrape_rp_latest_tutorial():
    """Scraping the latest episode image, uri, title and description"""
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="card border-0")
    image = results.find("img")["src"]
    uri = results.find("a")["href"]
    uri = RP_BASE_URL + uri
    # keep it as a placeholder
    # alt = results.find("img")["alt"]
    title = results.find("h2").text.strip()
    print(title)
    description = results.find("p").text.strip()
    return image, uri, title, description

def scrape_rp_podcast():
    """Scraping the main rp podcast webpage"""
    soup = BeautifulSoup(rp_podcast_page.content, "html.parser")
    podcast_image = soup.find("img", class_="card-img-top")
    image = podcast_image["src"]
    return image

def scrape_latest_rp_podcast_episode():
    """Scraping the latest rp podcast episode title and uri"""
    soup = BeautifulSoup(rp_podcast_page.content, "html.parser")
    last_ep = soup.find("div", class_="my-5")
    description = last_ep.find_all(["p"])[1].text.strip()
    uri = last_ep.find("a")["href"]
    uri = RP_BASE_URL + uri
    title = last_ep.find("a").text.strip()
    return title, uri, description