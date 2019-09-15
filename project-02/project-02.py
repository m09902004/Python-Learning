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
儲蓄率比GDP百分比
SavingRate_PercentageOfGDP
---
@author: AlexChen
"""

import pandas as pd
import matplotlib.pyplot as plt

file_csv01 = r'NetNationalIncome_PerCapita_USD.csv'
file_csv02 = r'GDP_PerCapita_USD.csv'
file_csv03 = r'HousingPrice_PriceToIncomeRatio.csv'
file_csv04 = r'HousingPrice_PriceToRentRatio.csv'
file_csv05 = r'SavingRate_PercentageOfGDP.csv'

nni_raw = pd.read_csv(file_csv01)
gdp_raw = pd.read_csv(file_csv02)
pir_raw = pd.read_csv(file_csv03)
prr_raw = pd.read_csv(file_csv04)
sr_raw = pd.read_csv(file_csv05)

nni = nni_raw.iloc[164:182]
time = list(nni['TIME'])
nni = pd.Series(list(nni['Value']),index = list(nni['TIME']),name = 'NNI')
gdp = gdp_raw.iloc[190:208]
gdp = pd.Series(list(gdp['Value']),index = list(gdp['TIME']),name = 'GDP')
pir = pir_raw.iloc[152:170]
pir = pd.Series(list(pir['Value']),index = list(pir['TIME']),name = 'PIR')
prr = prr_raw.iloc[175:193]
prr = pd.Series(list(prr['Value']),index=list(prr['TIME']),name = 'PRR')
sr = sr_raw.iloc[18:36]
sr = pd.Series(list(sr['Value']),index = list(sr['TIME']),name = 'SR')
df_new = pd.DataFrame()
data = [nni,gdp,pir,prr,sr]
for i in data:
  df_new = df_new.append(i)
df_new = df_new.transpose()

#比較各國匯率走勢
#設定圖示大小
plt.figure(figsize=(12, 8)) 

plt.subplot(3,1,1)
plt.plot(time,nni,color='green',label='NNI')
plt.plot(time,gdp,color='black',label='GDP')
plt.xlabel('year')
plt.ylabel('USD')
plt.xticks(rotation=40)
plt.legend()
plt.grid()

plt.subplot(3,1,2)
plt.plot(time,pir,color='red',label='PIR')
plt.plot(time,prr,color='magenta',label='PRR')
#plt.title(r'r/e',loc='right')
#plt.xlim(low,up)
#plt.ylim(0.75,1.75)
plt.xlabel('year')
plt.ylabel('%')
plt.xticks(rotation=40)
#plt.yticks(new_ticks)
plt.legend()
plt.grid()

plt.subplot(3,1,3)
plt.plot(time,sr,color='blue',label='SR')
plt.xlabel('year')
plt.ylabel('%')
plt.xticks(rotation=40)
plt.legend()
plt.grid()

plt.show()    







