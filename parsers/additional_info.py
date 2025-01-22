from utils.request_utils import scraping_request
from bs4 import BeautifulSoup
from config.settings import HOSTS 

def parse_additional_info(url):
    page = scraping_request(url)
    soup = BeautifulSoup(page, "html.parser")

    song = soup.find_all("div", class_="ant-row pDoqI")[0]
    url = HOSTS["additional"] + song.find("a").get("href")
    page = scraping_request(url)

    song_additional_info = page.find("div", class_="_4aYzP")
    
    release_date = song_additional_info.find_all("span", class_="O7uCY")[0].text 
    print(f"release_date - {release_date}")

    album = song_additional_info.find_all("span", class_="O7uCY")[2].text
    print(f"album - {album}")

    # for song in songs:
    #     found_artist = song.find("div", class_="ant-typography ant-typography-ellipsis ant-typography-single-line ant-typography-ellipsis-single-line _2zAVA").text 
    #     found_title = song.find("div", class_="ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line aZDDf").text 

    #     if found_artist == artist and found_title == title:
            
    #         response = scraping_request(url)
            
    #         return release_date, album  