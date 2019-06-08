import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()
s = requests.Session()
headers = {'User-Agent': ua.random}

while True:
    response = s.get("https://www.ecosia.org/search?q=free hotels", headers=headers).text
