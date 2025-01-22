from utils.request_utils import scraping_request
from bs4    import BeautifulSoup
from config.settings import HOSTS
from parsers.main_info import parse_main_info
from parsers.additional_info import parse_additional_info

def main():
    page = scraping_request(HOSTS["main"])
    soup = BeautifulSoup(page, 'html.parser')

    print("get main page")

    songs = soup.find_all("div", class_="item")
    for song in songs:
        title, artist, lyrics = parse_main_info(song)

        url = HOSTS["additional"] + f"Search?q={artist} - {title}"

        print(f"additional_info: url - {url}")
        parse_additional_info(url)
        break

if __name__ == "__main__":
    main()