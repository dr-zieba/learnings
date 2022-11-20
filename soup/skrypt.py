import requests
from bs4 import BeautifulSoup

web = requests.get(r"https://webscraper.io/test-sites/e-commerce/static")

content = web.content

print(BeautifulSoup(content, "html.parser"))
