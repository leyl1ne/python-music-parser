import requests
from bs4    import BeautifulSoup


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