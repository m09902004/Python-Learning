# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:59:46 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs
url = "https://tw.bid.yahoo.com/search/auction/product?kw=%E9%9B%BB%E8%85%A6&p=%E9%9B%BB%E8%85%A6"
res = requests.get(url)
soup = bs(res.text)
#print(soup.prettify)

data = soup.select('ul.gridList li a img')

for i in range(len(data)):
    print(data[i].get('alt'))
