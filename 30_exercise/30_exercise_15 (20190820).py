# -*- coding: utf-8 -*-
"""
資料整理
ver.2
"""
#讀取sample(json)
import json
file_pop=r'C:\Users\ASUS\Desktop\各鄉鎮市區人口密度.json'
with open(file_pop,'r',encoding='utf-8-sig') as file_obj:
  data_pop=json.load(file_obj)
  '''
  print(data_pop)
  print(type(data_pop))
  print(data_pop['responseData'])
  print(type(data_pop['responseData']))
  print(data_pop['responseData'][0])
  print(type(data_pop['responseData'][0]))
  print(data_pop['responseData'][0]['site_id'])
  print(type(data_pop['responseData'][0]['site_id']))
  print(data_pop['responseData'][0]['population_density'])
  print(type(data_pop['responseData'][0]['population_density']))
  '''
  #取需要的部分做為新的dict
  dict_pop={}
  data_pop=data_pop['responseData']
  i=0
  for i in range(len(data_pop)):
    try:
      dict_pop[data_pop[i]['site_id']]=int(data_pop[i]['population_density'])
    except ValueError:
      dict_pop[data_pop[i]['site_id']]=0
  '''
  print(min(dict_pop, key=dict_pop.get),dict_pop[min(dict_pop, key=dict_pop.get)])
  print(max(dict_pop, key=dict_pop.get),dict_pop[max(dict_pop, key=dict_pop.get)])
  '''
  #把max10跟min10提出
  j=0
  print('人口密度最高前10名')
  for j in range(0,10):
    max_key=max(dict_pop, key=dict_pop.get)
    max_value=dict_pop[max(dict_pop, key=dict_pop.get)]
    print('第{:2d}名：{:6s}人口密度- {:d}'.format(j+1,max_key,max_value))
    del dict_pop[max(dict_pop, key=dict_pop.get)] 
  print('-'*40)
  j=0
  print('人口密度最低前10名')
  for j in range(0,10):
    min_key=min(dict_pop, key=dict_pop.get)
    min_value=dict_pop[min(dict_pop, key=dict_pop.get)]
    print('第{:2d}名：{:6s}人口密度- {:d}'.format(j+1,min_key,min_value))
    del dict_pop[min(dict_pop, key=dict_pop.get)] 

    