import requests
from bs4    import BeautifulSoup
import json
import time 


HOST = "https://text-pesenok.ru/"
HEADERS = {
    {'user-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/62.0'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 OPR/70.0.3728.189'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 OPR/69.0.3686.77'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.3.234 Yowser/2.5 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 YaBrowser/21.5.2.638 Yowser/2.5 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'},
    {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36 Maxthon/5.1.5.3000 '}
}

PROXIES = [
"54.155.127.16:8888",
"111.1.61.49:3128",
"111.1.61.47:3128",
"62.201.229.66:8080",
"176.10.125.7:8118",
"52.67.117.187:3128",
"188.235.146.220:40754",
"185.10.129.14:3128",
"92.124.154.154:8080",
"62.33.53.248:3128",
]

class Song:
    def __init__(self, title="", artist="", lyrics="", album="", release_year=0, genre=""):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics
        self.album = album
        self.release_year = release_year
        self.genre = genre 
    
    def __str__(self):
        return f"Title - {self.title}\n Artist - {self.artist}\n Lyrics - \n {self.lyrics} Album - {self.album} \n Release Year - {self.release_year} \n"

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

def parsing_lyrics(url_page):
    resp = requests.get(url_page, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')

    lyrics_html = soup.find("div", class_="main_text-slova").prettify()
    lyrics = lyrics_html.replace("<p>", "").replace("</p>", "\n").strip()

    return lyrics 



if __name__ == "__main__":
    resp = requests.get(HOST, headers=HEADERS)
    soup = BeautifulSoup(resp.text, 'html.parser')

    songs = soup.find_all("div", class_="item")
    for song in songs:
        title = song.find("a").text 
        artist = song.find("div", class_="item__artist").text
        url = HOST + song.find("a").get("href")
        lyrics = parsing_lyrics(url)
        print(Song(title, artist, lyrics))
        time.sleep(10)





