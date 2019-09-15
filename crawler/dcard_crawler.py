# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:31:42 2019

@author: DioChen
"""

import requests
from bs4 import BeautifulSoup

topic = input('請輸入子版代號 :')

url = 'https://www.dcard.tw'+'/f/'+topic

res = requests.get(url)

soup = BeautifulSoup(res.text,'html.parser')

print(soup.prettify())

a = soup.select('a.PostEntry_root_V6g0rd')

for i in range(len(a)):
  print('\n',soup.select('a.PostEntry_root_V6g0rd')[i].text)
