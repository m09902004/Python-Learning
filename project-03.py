# -*- coding: utf-8 -*-
"""
人均淨收入 
NetNationalIncome_PerCapita_USD
人均GDP       
GDP_PerCapita_USD
---
房價比收入
HousingPrice_PriceToIncomeRatio
房價比租金
HousingPrice_PriceToRentRatio
---
@author: AlexChen
"""

#匯入套件
import pandas as pd
import matplotlib.pyplot as plt

#讀取來源(csv)
file_csv01 = r'NetNationalIncome_PerCapita_USD.csv'
file_csv02 = r'GDP_PerCapita_USD.csv'
file_csv03 = r'HousingPrice_PriceToIncomeRatio.csv'
file_csv04 = r'HousingPrice_PriceToRentRatio.csv'

nni_raw = pd.read_csv(file_csv01)
gdp_raw = pd.read_csv(file_csv02)
pir_raw = pd.read_csv(file_csv03)
prr_raw = pd.read_csv(file_csv04)

#將資料存為 DataFrame (USA)
nni_usa = nni_raw.iloc[164:182]
time_usa = list(nni_usa['TIME'])
nni_usa = pd.Series(list(nni_usa['Value']),index = list(nni_usa['TIME']),name = 'NNI')
gdp_usa = gdp_raw.iloc[190:208]
gdp_usa = pd.Series(list(gdp_usa['Value']),index = list(gdp_usa['TIME']),name = 'GDP')
pir_usa = pir_raw.iloc[152:170]
pir_usa = pd.Series(list(pir_usa['Value']),index = list(pir_usa['TIME']),name = 'PIR')
prr_usa = prr_raw.iloc[175:193]
prr_usa = pd.Series(list(prr_usa['Value']),index=list(prr_usa['TIME']),name = 'PRR')
df_new_usa = pd.DataFrame()
data_usa = [nni_usa,gdp_usa,pir_usa,prr_usa]
for i in data_usa:
  df_new_usa = df_new_usa.append(i)
df_new_usa = df_new_usa.transpose()

#將資料存為 DataFrame (Korea)
nni_kor = nni_raw.iloc[110:128]
time_kor = list(nni_kor['TIME'])
nni_kor = pd.Series(list(nni_kor['Value']),index = list(nni_kor['TIME']),name = 'NNI')
gdp_kor = gdp_raw.iloc[114:132]
gdp_kor = pd.Series(list(gdp_kor['Value']),index = list(gdp_kor['TIME']),name = 'GDP')
pir_kor = pir_raw.iloc[114:132]
pir_kor = pd.Series(list(pir_kor['Value']),index = list(pir_kor['TIME']),name = 'PIR')
prr_kor = prr_raw.iloc[114:132]
prr_kor = pd.Series(list(prr_kor['Value']),index=list(prr_kor['TIME']),name = 'PRR')
df_new_kor = pd.DataFrame()
data_kor = [nni_kor,gdp_kor,pir_kor,prr_kor]
for i in data_kor:
  df_new_kor = df_new_kor.append(i)
df_new_kor = df_new_kor.transpose()

#畫圖
#設定圖示大小
plt.figure(figsize = (20,12)) 

#圖1
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])
plt.plot(time_usa,nni_usa,color='green',label='USA_NNI')
plt.plot(time_usa,gdp_usa,color='black',label='USA_GDP')
plt.xlim(1999,2019)
plt.ylim(10000,70000)
plt.xlabel('year')
plt.ylabel('USD')
plt.xticks(rotation=30)
plt.legend()
plt.grid()

#圖2
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
plt.plot(time_usa,pir_usa,color='red',label='USA_PIR')
plt.plot(time_usa,prr_usa,color='magenta',label='USA_PRR')
#plt.title(r'r/e',loc='right')
plt.xlim(1999,2019)
plt.ylim(50,150)
plt.xlabel('year')
plt.ylabel('%')
plt.xticks(rotation=30)
#plt.yticks(new_ticks)
plt.legend()
plt.grid()

#圖3
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])
plt.plot(time_kor,nni_kor,color='green',label='KOR_NNI')
plt.plot(time_kor,gdp_kor,color='black',label='KOR_GDP')
plt.xlim(1999,2019)
plt.ylim(10000,70000)
plt.xlabel('year')
plt.ylabel('USD')
plt.xticks(rotation=30)
plt.legend()
plt.grid()

#圖4
plt.subplot(2,2,4)
plt.plot([0,1],[0,4])
plt.plot(time_kor,pir_kor,color='red',label='KOR_PIR')
plt.plot(time_kor,prr_kor,color='magenta',label='KOR_PRR')
plt.xlim(1999,2019)
plt.ylim(50,150)
plt.xlabel('year')
plt.ylabel('%')
plt.xticks(rotation=30)
plt.legend()
plt.grid()

plt.show()    
