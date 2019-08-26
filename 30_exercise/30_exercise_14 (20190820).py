# -*- coding: utf-8 -*-
"""
json 寫+讀+輸出
ver.3
"""

import json
file_meal=r'C:\Users\ASUS\Desktop\30_output.json'
dict_meal={"breakfast":50,"lunch":80,"dinner":100}
with open(file_meal,'w',encoding='ansi') as file_obj:
  data_meal=json.dump(dict_meal,file_obj)
with open(file_meal,'r',encoding='ansi') as file_obj:
  data_meal=json.load(file_obj)
  form_meal='早餐費用：{:d}元\n午餐費用：{:d}元\n晚餐費用：{:d}元'
print(form_meal.format(data_meal['breakfast'],data_meal['lunch'],data_meal['dinner']))

