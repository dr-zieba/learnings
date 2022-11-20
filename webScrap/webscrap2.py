import requests
import pandas as pd
from bs4 import BeautifulSoup

link = "https://webscraper.io/test-sites/e-commerce/static/computers/tablets?page="
product_list = []
name_list = []
link_list = []
    
for i in range(1,5):
    print(link + str(i))
    web_page = requests.get(link + str(i))
    content = web_page.content
    soup = BeautifulSoup(content, "html.parser")
    print("*************** Page number" + str(i) + "*******************")

    for i in soup.find_all(class_='col-sm-4 col-lg-4 col-md-4'):
        product = i.find(class_='pull-right price').text
        product_list.append(str(product))

        name_list.append(i.find(class_='title').string)

        link_product = i.a['href']
        link_list.append(str("https://webscraper.io" + link_product))
        print(str("https://webscraper.io" + link_product))

data = list(zip(product_list, name_list, link_list))
print(data)
d = pd.DataFrame(data, columns = ['Price', 'Name', 'Link'])
try:
    d.to_excel(r'C:\Users\zieba\Desktop\python\webScrap\file2.xlsx')
except:
    print("Something wen wrong!!")
else:
    print("Data written to file")
finally:
    print("Program finished")
        
