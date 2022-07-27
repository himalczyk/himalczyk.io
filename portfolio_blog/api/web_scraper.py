"""This is going to be a module having a class to scrape data from real python blog"""

from bs4 import BeautifulSoup
import requests
from api.config import RP_BASE_URL

page = requests.get(RP_BASE_URL)

# passing in page.content instead of page.text to avoid problem with character encoding.
def scrape_rp_image_uri():
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("div", class_="card border-0")
    image = results.find("img")["src"]
    uri = results.find("a")['href']
    alt = results.find("img")["alt"]
    uri = RP_BASE_URL + uri
    return image, uri, alt