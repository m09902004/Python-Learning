# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:16:39 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs

url = "https://news.google.com/?tab=rn1&hl=zh-TW&gl=TW&ceid=TW:zh-Hant"

res = requests.get(url)

soup = bs(res.text,"lxml")

#span = soup.select("span")
a = soup.select("a.DY5T1d")
for i in range(len(a)):
  href = "https://news.google.com/" + a[i]["href"]
  print("{}\n{}".format(a[i].text,href))


