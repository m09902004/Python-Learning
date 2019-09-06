# -*- coding: utf-8 -*-
"""
爬爬練習
ver.1
"""

import requests

url = 'http://tqc.codejudger.com:3000/target/5205.json'
data = requests.get(url).json()
print('Content-Length : {}\n\n新北市PM2.5相關資料 :'.format(requests.get(url).headers['Content-Length']))
print_form = '{} :\n\tAQI : {}\n\tPM2.5 : {}\n\tPM10 : {}\n\t資料更新時間 : {} '
for i in range(len(data)):
    if data[i]['SiteName']=='汐止':
        print(print_form.format(data[i]['SiteName'],data[i]['AQI'],data[i]['PM2.5'],data[i]['PM10'],data[i]['PublishTime']))
    elif data[i]['SiteName']=='萬里':
        print(print_form.format(data[i]['SiteName'],data[i]['AQI'],data[i]['PM2.5'],data[i]['PM10'],data[i]['PublishTime']))