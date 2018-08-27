import requests
from bs4 import BeautifulSoup

url = 'https://blog.csdn.net/qq_39687901/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

article_list=soup.find(class_='article-list')

print(len(article_list.contents))

