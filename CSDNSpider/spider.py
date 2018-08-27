from lxml import etree

import requests

url = 'https://blog.csdn.net/qq_39687901/'

response = requests.get(url)

dom_tree = etree.HTML(response.text)

print(dom_tree.xpath('//div[@class="article-list"]'))