# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:33:58 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs

search = input("請輸入要查詢的關鍵字(wiki) :")
url = "https://zh.wikipedia.org/wiki/"+search
res = requests.get(url) 

soup = bs(res.text,"lxml")
a = soup.select("p")
content = []
for i in range(len(a)):
  content.append(a[i].text.replace("\n","").replace("\xa0",""))
print(content)

