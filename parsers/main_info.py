from utils.request_utils import scraping_request
from bs4 import BeautifulSoup
from config.settings import HOSTS 

def parse_main_info(song):
    title = get_title(song)
    artist = get_artist(song)
    url = HOSTS["main"] + song.find("a").get("href")
    lyrics = get_lyrics(url)

    return title, artist, lyrics


def get_title(song):
    title = song.find("a").text
    if title == "":
        title = "Unknown"

    print(f"get_title: title - {title}")
    return title 

def get_artist(song):
    artist = song.find("div", class_="item__artist").text
    if artist == "":
        artist = "Unknown"

    print(f"get_artist: artist - {artist}")
    return artist 

def get_lyrics(url_page):
    page = scraping_request(url_page)
    soup = BeautifulSoup(page, 'html.parser')

    lyrics_html = soup.find("div", class_="main_text-slova").prettify()
    lyrics = lyrics_html.replace("<p>", "").replace("</p>", "").replace('<div class="main_text-slova">', "").replace("</div>", "")


    print(f"get_lyrics: lyrics - {lyrics}")
    return lyrics 