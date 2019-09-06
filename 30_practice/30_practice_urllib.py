# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:35:05 2019

@author: ASUS
"""

import urllib.request as ur

url = "https://data.gov.tw"
res = ur.urlopen(url)

print('1.網址：',res.geturl(),type(res.geturl()))
print()
print('2.讀取狀態：',res.status,type(res.status))
print()
print('3.表頭資訊：',res.getheaders(),type(res.getheaders()))
print()
print('4.網頁資料(Byte)：',res.read(),type(res.read()))
print()
content = res.read()
print('5.網頁資料(string)：',content.decode(),type(content.decode()))
