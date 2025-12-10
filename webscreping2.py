import requests
from bs4 import BeautifulSoup
import csv 
with open("WebScreping_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["product_name","product_categry","product_price",'product_link','review_count',"description"])
    links=['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops','https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets','https://webscraper.io/test-sites/e-commerce/allinone/phones/touch']
    for link in links:
        if link==links[0]:
            categry="laptop"
        elif link ==links[1]:
            categry="tablets"
        else:
            categry="phone"
        data=requests.get(link)
        soup=BeautifulSoup(data.content,"html.parser")
        items=soup.find_all('div',class_='col-md-4 col-xl-4 col-lg-4')
  
        for item in items:
             name=item.find('a',class_='title').text.strip()
             price= item.find("h4").find('span').text
             product_Link="https://webscraper.io"+item.find('a',class_='title')['href']
             review_count=item.find("p",class_='review-count float-end').find("span").text
             description=item.find("p",class_="description card-text").text
             writer.writerow([name,categry,price,product_Link,review_count,description])
        