# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:24:59 2019

@author: ASUS
"""

import requests
import json
url = 'https://ecapi.pchome.com.tw/mall/cateapi/v1/sign&tag=newarrival&fields=Id,Name,Sort,Nodes&_callback=jsonpcb_newarrival&1566877216068'
user_agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' #偽裝使用者
headers = {'User-Agent':user_agent,
          'server': 'PChome/1.0.4',
          'Referer': 'https://mall.pchome.com.tw/newarrival/'}
res = requests.get(url=url,headers=headers)#分析得出的網址
res_text = res.text
res_text_format = res_text.replace('try{jsonpcb_newarrival(','').replace(');}catch(e){if(window.console){console.log(e);}}','')
jd = json.loads(res_text_format)
print(jd)