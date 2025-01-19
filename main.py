import requests
from bs4    import BeautifulSoup
import json


HOST = "https://text-pesenok.ru/"
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
}

resp = requests.get(HOST, headers=HEADERS)
soup = BeautifulSoup(resp.text, 'html.parser')

songs = soup.find_all("div", class_="item")

for song in songs:
    print(song.find("a").get("href"))

class Song:
    def __init__(self, title="", artist="", lyrics="", album="", release_year=0, genre=""):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.album = album
        self.release_year = release_year
        self.genre = genre 

    def to_dict(self):
        return{
            'title' : self.title,
            'artist' : self.artist,
            'album' : self.album,
            'release_year' : self.release_year,
            'genre' : self.genre,
            'lyrics' : self.lyrics
        }
    
    def send_to_api(self, api_url):
        data = self.to_dict()
        headers = {'Content-Type': 'application/json'}

        response = requests.post(api_url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print(f"Song '{self.title}' successfully send to API.")
        else:
            print(f"Failed to send song: {response.status_code} - {response.text}")