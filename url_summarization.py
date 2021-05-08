from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    fetched_text = ' '.join(map(lambda p:p.text,soup.find_all('p')))
    return fetched_text

