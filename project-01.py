# -*- coding: utf-8 -*-
"""
匯率變動 from 政府公開資料
ExchangeRates
---
@author: AlexChen
"""

#匯入套件
import xml.etree.cElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

#讀取來源(xml)
file_xml = r'ExchangeRates.xml'
tree = ET.ElementTree(file=file_xml)
root = tree.getroot()
root.tag, root.attrib

#將資料轉為 DataFrame
ex_rate = {}
for child_of_root in root:
  for gchild_of_root in child_of_root:
    if gchild_of_root.tag not in ex_rate:
      ex_rate[gchild_of_root.tag] = list()
    else:
      if gchild_of_root.tag == '月別':
        ex_rate[gchild_of_root.tag].append(gchild_of_root.text)
      else:
        ex_rate[gchild_of_root.tag].append(eval(gchild_of_root.text))  
ex_rate_df = pd.DataFrame.from_dict(ex_rate)  

#將資料內容轉為同單位(USD)
ex_rate_df['人民幣'] = ex_rate_df['人民幣']*0.14110
ex_rate_df['新加坡元'] = ex_rate_df['新加坡元']*0.72
ex_rate_df['新台幣'] = ex_rate_df['新台幣']*0.03187
ex_rate_df['日圓'] = ex_rate_df['日圓']*0.009399
ex_rate_df['歐元'] = ex_rate_df['歐元']*1.1100
ex_rate_df['澳幣'] = ex_rate_df['澳幣']*0.6823
ex_rate_df['英鎊'] = ex_rate_df['英鎊']*1.2145
ex_rate_df['韓元'] = ex_rate_df['韓元']*0.0008279

#將各國數據定義為變數
year_month = ex_rate_df['月別']
cny = ex_rate_df['人民幣']
sgd = ex_rate_df['新加坡元']
ntd = ex_rate_df['新台幣']
jpy = ex_rate_df['日圓']
eur = ex_rate_df['歐元']
aud = ex_rate_df['澳幣']
gbp = ex_rate_df['英鎊']
krw = ex_rate_df['韓元']

#輸出各國數據統計值
countries = [cny,sgd,ntd,jpy,eur,aud,gbp,krw]
er_an_df = pd.DataFrame()
for x in countries:
  ss = pd.Series({'平均值':x.mean(),'最大值':x.max(),'最小值':x.min(),'變異數':x.var(),'標準差':x.std(),'偏度':x.skew(),'峰度':x.kurt()},name=x.name)
  er_an_df = er_an_df.append(ss)
print(er_an_df)

#畫圖
#設定圖示大小
plt.figure(figsize=(12,8)) 
plt.plot(year_month,ntd,color='green',label='NTD')
plt.plot(year_month,cny,color='black',label='CNY')
plt.plot(year_month,jpy,color='red',label='JPY')
plt.plot(year_month,krw,color='magenta',label='KRW')
plt.plot(year_month,eur,color='blue',label='EUR')
plt.plot(year_month,gbp,color='cyan',label='GBP')
plt.plot(year_month,sgd,color='chocolate',label='SGD')
plt.plot(year_month,aud,color='grey',label='AUD')
plt.title(r'r/e',loc='right')
#plt.xlim(2018,2020)
#plt.ylim(0.75,1.75)
plt.xlabel('year-month')
plt.ylabel('USD')
plt.xticks(rotation=30)
#plt.yticks(new_ticks)
plt.legend()
plt.grid()
plt.show() 
