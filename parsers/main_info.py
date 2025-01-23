from utils.request_utils import scraping_request
from bs4 import BeautifulSoup
from config.settings import HOSTS 
from models.song import Song

def parse_main_info():
    page = scraping_request(HOSTS["main"])
    soup = BeautifulSoup(page, 'html.parser')

    songs = soup.find_all("div", class_="item")
    for song in songs:
        title = get_title(song)
        artist = get_artist(song)
        url = HOSTS["main"] + song.find("a").get("href")
        lyrics = get_lyrics(url)


        yield Song(title, artist, lyrics)



def get_title(song):
    title = song.find("a").text
    if title == "":
        title = "Unknown"

    return title 

def get_artist(song):
    artist = song.find("div", class_="item__artist").text
    if artist == "":
        artist = "Unknown"

    return artist 

def get_lyrics(url_page):
    page = scraping_request(url_page)
    soup = BeautifulSoup(page, 'html.parser')

    lyrics_html = soup.find("div", class_="main_text-slova").prettify()
    lyrics = lyrics_html.replace("<p>", "").replace("</p>", "").replace('<div class="main_text-slova">', "").replace("</div>", "")

    lyrics = "\n".join(line for line in lyrics.splitlines() if line.strip())

    return lyrics 