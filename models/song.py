import requests
import json 

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
