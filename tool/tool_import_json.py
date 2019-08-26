# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 14:40:36 2019

@author: ASUS
"""
#讀取json(ansi)
import json
file01=r'C:\Users\ASUS\Desktop\ansi.json'
with open(file01,'r',encoding='ansi') as file_obj:
  data_json=json.load(file_obj)
print(data_json)
print(type(data_json))

#讀取json(utf-8-sig)
import json
file01=r'C:\Users\ASUS\Desktop\utf-8.json'
with open(file01,'r',encoding='utf-8-sig') as file_obj:
  data_json=json.load(file_obj)
print(data_json)
print(type(data_json))

#讀取json(utf-8-sig)(轉list)
import json
file01=r'C:\Users\ASUS\Desktop\utf-8.json'
with open(file01,'r',encoding='utf-8-sig') as file_obj:
  data_json=json.load(file_obj)
  for item in data_json:
    print(item['name'],item['phone'],item['email'])
    
#讀取sample:NewBike.json(轉list)
import json
file_smaple=r'C:\Users\ASUS\Desktop\NewBike.json'
with open(file_smaple,'r',encoding='utf8') as file:
  data=json.load(file)
  for item in data:
    print([item['sno'],item['sna'],item['tot']])
