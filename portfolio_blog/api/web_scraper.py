"""This is going to be a module having a class to scrape data from real python blog"""

from bs4 import BeautifulSoup
import requests
from api.config import RP_BASE_URL, DJANGO_CHAT_PODCAST_PAGE
# testing
# from config import RP_BASE_URL

page = requests.get(RP_BASE_URL)
rp_podcast_page = requests.get(RP_BASE_URL + '/podcasts/rpp/')
django_chat_podcast_page = requests.get(DJANGO_CHAT_PODCAST_PAGE)

# passing in page.content instead of page.text to avoid problem with character encoding.
def scrape_rp_image_uri():
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="card border-0")
    image = results.find("img")["src"]
    uri = results.find("a")["href"]
    uri = RP_BASE_URL + uri
    alt = results.find("img")["alt"]
    paragraph = results.find("p").text.strip()
    return image, uri, alt, paragraph

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="card border-0")

def scrape_rp_podcast():
    soup = BeautifulSoup(rp_podcast_page.content, "html.parser")
    podcast_image = soup.find("img", class_="card-img-top")
    image = podcast_image["src"]
    return image

def scrape_latest_rp_episode():
    soup = BeautifulSoup(rp_podcast_page.content, "html.parser")
    last_ep = soup.find("div", class_="my-5")
    uri = last_ep.find("a")["href"]
    uri = RP_BASE_URL + uri
    title = last_ep.find("a").text.strip()
    return title, uri

def scrape_django_podcast():
    soup = BeautifulSoup(django_chat_podcast_page.content, "html.parser")
