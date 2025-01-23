from utils.request_utils import scraping_request
from bs4 import BeautifulSoup
from config.settings import HOSTS
from models.song import Song  

def parse_additional_info(song):
    title = song.title 
    artist = song.artist

    search_url = HOSTS["additional"] + f"/Search?q={artist} - {title}"

    search_page = scraping_request(search_url)
    soup = BeautifulSoup(search_page, "html.parser")

    searched_song = soup.find_all("div", class_="ant-row pDoqI")[0]
    url_page_info = HOSTS["additional"] + searched_song.find("a").get("href")
    
    page_additional_info = scraping_request(url_page_info)
    soup = BeautifulSoup(page_additional_info, "html.parser")

    song_additional_info = soup.find("div", class_="_4aYzP")
    fields = song_additional_info.find_all("span", class_="ant-typography")

    release_date = "Unknown"
    album = "Unknown"
    for field in fields:
        if field.text[:13] == "Release Date:":
            release_date = field.find("span", class_="O7uCY").text 

        if field.text[:6] == "Album:":
            album = field.find("span", class_="O7uCY").text 

    song.release_year = int(release_date[-4:])
    song.album = album 

    return song

   