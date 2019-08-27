# -*- coding: utf-8 -*-
"""
CPI_AnnualGrowthRate_Total
CPI_AnnualGrowthRate_Energy
CPI_AnnualGrowthRate_Food
CPI_AnnualGrowthRate_TotalLess
---
CPI_Total
CPI_Energy
CPI_Food
CPI_TotalLess
---
@author: AlexChen
"""

#匯入套件
import pandas as pd
import matplotlib.pyplot as plt

#讀取來源(json)
file_json01 = r'CPI_AnnualGrowthRate_Total.json'
file_json02 = r'CPI_AnnualGrowthRate_Energy.json'
file_json03 = r'CPI_AnnualGrowthRate_Food.json'
file_json04 = r'CPI_AnnualGrowthRate_TotalLess.json'
file_json05 = r'CPI_Total.json'
file_json06 = r'CPI_Energy.json'
file_json07 = r'CPI_Food.json'
file_json08 = r'CPI_TotalLess.json'

data_cat = pd.read_json(file_json01)
data_cae = pd.read_json(file_json02)
data_caf = pd.read_json(file_json03)
data_catl = pd.read_json(file_json04)
data_ct = pd.read_json(file_json05)
data_ce = pd.read_json(file_json06)
data_cf = pd.read_json(file_json07)
data_ctl = pd.read_json(file_json08)

#將資料存為 DataFrame (USA)
time_usa = list(data_cat[190:208]['TIME'])
cat_usa = pd.Series(list(data_cat[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_GR_T_USA')
cae_usa = pd.Series(list(data_cae[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_GR_E_USA')
caf_usa = pd.Series(list(data_caf[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_GR_F_USA')
catl_usa = pd.Series(list(data_catl[111:129]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_GR_Tl_USA')
ct_usa = pd.Series(list(data_ct[111:129]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_T_USA')
ce_usa = pd.Series(list(data_ce[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_E_USA')
cf_usa = pd.Series(list(data_cf[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_F_USA')
ctl_usa = pd.Series(list(data_ctl[190:208]['Value']),index = list(data_cat[190:208]['TIME']),name = 'CPI_Tl_USA')
df_new_usa = pd.DataFrame()
data_usa = [cat_usa,cae_usa,caf_usa,catl_usa,ct_usa,ce_usa,cf_usa,ctl_usa]
for i in data_usa:
  df_new_usa = df_new_usa.append(i)
df_new_usa = df_new_usa.transpose()

#將資料存為 DataFrame (Korea)
time_kor = list(data_cat[114:132]['TIME'])
cat_kor = pd.Series(list(data_cat[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_GR_T_Kor')
cae_kor = pd.Series(list(data_cae[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_GR_E_Kor')
caf_kor = pd.Series(list(data_caf[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_GR_F_Kor')
catl_kor = pd.Series(list(data_catl[168:186]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_GR_Tl_Kor')
ct_kor = pd.Series(list(data_ct[168:186]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_T_Kor')
ce_kor = pd.Series(list(data_ce[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_E_Kor')
cf_kor = pd.Series(list(data_cf[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_F_Kor')
ctl_kor = pd.Series(list(data_ctl[114:132]['Value']),index = list(data_cat[114:132]['TIME']),name = 'CPI_Tl_Kor')
df_new_kor = pd.DataFrame()
data_kor = [cat_kor,cae_kor,caf_kor,catl_kor,ct_kor,ce_kor,cf_kor,ctl_kor]
for i in data_kor:
  df_new_kor = df_new_kor.append(i)
df_new_kor = df_new_kor.transpose()

#畫圖
#設定圖示大小
plt.figure(figsize=(20, 12)) 

#圖1
plt.subplot(2,2,1)
plt.plot([0,1],[0,1])
plt.plot(time_usa,ct_usa,color='green',label='Total')
plt.plot(time_usa,ce_usa,color='blue',label='Energy')
plt.plot(time_usa,cf_usa,color='red',label='Food')
plt.plot(time_usa,ctl_usa,color='black',label='TotalLess')
plt.xlabel('year')
#plt.ylabel('%')
plt.title(r'USA_CPI',loc='left')
plt.xlim(1999,2019)
plt.ylim(50,150)
plt.xticks(rotation=30)
plt.legend()
plt.grid()

#圖2
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
plt.plot(time_usa,cat_usa,color='green',label='Rate_Total')
plt.plot(time_usa,cae_usa,color='blue',label='Rate_Energy')
plt.plot(time_usa,caf_usa,color='red',label='Rate_Food')
plt.plot(time_usa,catl_usa,color='black',label='Rate_TotalLess')
plt.xlabel('year')
#plt.ylabel('%')
plt.title(r'USA_GrowthRate',loc='right')
#plt.title(r'r/e',loc='right')
plt.xlim(1999,2019)
plt.ylim(-20,20)
plt.xticks(rotation=30)
#plt.yticks(new_ticks)
plt.legend()
plt.grid()

#圖3
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])
plt.plot(time_kor,ct_kor,color='green',label='Total')
plt.plot(time_kor,ce_kor,color='blue',label='Energy')
plt.plot(time_kor,cf_kor,color='red',label='Food')
plt.plot(time_kor,ctl_kor,color='black',label='TotalLess')
plt.xlabel('year')
#plt.ylabel('%')
plt.title(r'KOR_CPI',loc='left')
plt.xlim(1999,2019)
plt.ylim(50,150)
plt.xticks(rotation=30)
plt.legend()
plt.grid()

#圖4
plt.subplot(2,2,4)
plt.plot([0,1],[0,4])
plt.plot(time_kor,cat_kor,color='green',label='Rate_Total')
plt.plot(time_kor,cae_kor,color='blue',label='Rate_Energy')
plt.plot(time_kor,caf_kor,color='red',label='Rate_Food')
plt.plot(time_kor,catl_kor,color='black',label='Rate_TotalLess')
plt.xlabel('year')
#plt.ylabel('%')
plt.title(r'KOR_GrowthRate',loc='right')
plt.xlim(1999,2019)
plt.ylim(-20,20)
plt.xticks(rotation=30)
plt.legend()
plt.grid()

plt.show()   
