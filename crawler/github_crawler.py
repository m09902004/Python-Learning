# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:37:39 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup as bs

user_name = input("請輸入User Name :")

repositories = input("請輸入Repositories :")

url = "https://github.com/" + user_name + "/" + repositories

res = requests.get(url)

soup = bs(res.text,"lxml")

#print(soup.prettify())

a = soup.find_all("a",{"link-gray"});a
b = {}
for i in range(len(a)):
  b[a[i].text] = a[i]["href"] 
print(b)