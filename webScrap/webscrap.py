import requests
import pandas as pd
from bs4 import BeautifulSoup

web_request = requests.get("https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page=1")
content = web_request.content
soup = BeautifulSoup(content, "html.parser")

product_l = []
name = []
link_l = []

for i in soup.find_all(class_='caption'):
    product = i.find(class_='pull-right price').text
    product_l.append(str(product))
    
    name.append(i.find(class_='title').string)
    
    link = i.a['href']
    link_l.append(str("https://webscraper.io" + link))

data = list(zip(name, product_l, link_l))
d = pd.DataFrame(data, columns=['Name', 'Price', 'Link'])
d.to_excel(r'C:\Users\zieba\Desktop\python\webScrap\file.xlsx')



print(product_l)
print(name)
print(link_l)





