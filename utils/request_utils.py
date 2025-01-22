import random 
from config.settings import PROXIES, HEADERS
import requests
import time 

def scraping_request(url):
    while True:
        time.sleep(random.randrange(4, 8))
        ip = random.choice(PROXIES)
        headers = random.choice(HEADERS)
        try: 
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"Proxy currently being used: {ip}")
                return response.text 
            
            elif response.status_code == 403:
                print("Forbidden client")
                continue

            elif response.status_code == 429:
                print("Too many requests")
                continue
        
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}. Changing proxy and header.")
            continue 