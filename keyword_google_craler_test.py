# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:46:01 2019

@author: ASUS
"""

import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 宣告
ckeck_list = []
a_list_of_dictionaries = []

# 作假的開頭請求 因為fake_useragent 我用他抓不知WHY有點問題所以自己做的header
ua = UserAgent()

#一般的桌面板瀏覽器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

#假iPhone瀏覽器
mobile_headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'}

# 關鍵字
input_keyword = input("關鍵字查詢(例：電商平台) : ")

#如果要換頁面抓的話
page_number = 1
page = 0 + (10*(page_number - 1))

# 網址製作區
url = "https://www.google.com.tw/search?q=" + input_keyword + "&start=" + str(page)

# 抓取網頁資料
response = requests.get(url, headers=headers)

input_html = response.text

# 下面是整理成要用的資料
soup = BeautifulSoup(input_html,"html.parser")

x = 1
for item in soup.select('.ads-ad'):
    result = {}
    ad_text = ""
    ad_ext_link = ""
    ad_tilte =  item.select('a')[1].text.replace("\u200e", "")  #消除最後會有多個u200e
    ad_resource = "google"
    ad_link =  item.select('a')[1].get('href')
    if  len(item.select('ul li a')) > 0:
        for ext_link in item.select('ul li a'):
            if  ext_link.text != "":
                ad_ext_link += ext_link.text +"->"+ext_link.get('href') + "\n"

    for info in item.select('.ellip '):
        ad_text +=  info.text +"\n"

    ad_sort = x
    x += 1

    if ad_tilte not  in ckeck_list:
        ckeck_list.append(ad_tilte)
        result['01廣告內文'] = ad_text
        result['02廣告主連結'] = ad_link
        result['03廣告副文'] = ad_ext_link
        result['04廣告來源'] = ad_resource
        result['05順位'] = ad_sort
        a_list_of_dictionaries.append(result)
    else:
        print ('已存在的廣告')

print (a_list_of_dictionaries)