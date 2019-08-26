# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 10:01:14 2019

@author: ASUS
"""

import pandas as pd
file_csv=r'C:\Users\ASUS\Desktop\108070130\open data\A17030000J-000049-9k0.csv'
df=pd.read_csv(file_csv,header=0) #0首列為欄名 -1首列保留
print(type(df))
print(df.info())
print(df.shape)
print(df)
print(df.iloc[0:12,[1,2,4]])
df.head()
filt01=df["月別"]<="2018-12"
filt02=df["月別"]>"2018-12"
df01=df[filt01]
df02=df[filt02]