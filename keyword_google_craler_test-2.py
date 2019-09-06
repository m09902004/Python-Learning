# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:55:10 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.google.com.tw/search'

search = input("請輸入關鍵字：")

# 查詢參數
params = {'q': search}

# 下載 Google 搜尋結果
res = requests.get(url, params)
soup = bs(res.text, 'html.parser')

# 觀察 HTML 原始碼
print(soup.prettify())

# 以 CSS 的選擇器來抓取 Google 的搜尋結果
items = soup.select('div');items
for i in items:
  # 標題 網址
  print("標題：{}\n網址：{}".format(i.text,i.get('href')))

