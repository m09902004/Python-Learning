# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:39:24 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs

url = "https://tw.yahoo.com/"
res = requests.get("https://tw.yahoo.com/")

soup = bs(res.text, "html.parser")

news = soup.select("a.story-title")
for i in range(len(news)):
  print("標題：{}\n網址：{}".format(news[i].text,news[i]['href']))