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
import json
file_json01=r'project-03\CPI_AnnualGrowthRate_Total.json'
with open(file_json01,'r',encoding='ansi') as f01:
  dict_data = json.load(f01)
print(dict_data)