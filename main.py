
from parsers.main_info import parse_main_info
from parsers.additional_info import parse_additional_info

def main():
    for song_main_info in parse_main_info():
        song = parse_additional_info(song_main_info)
        song.send_to_api("http://localhost:8080/save")

if __name__ == "__main__":
    main()