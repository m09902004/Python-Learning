# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 13:32:15 2019

@author: ASUS
"""

import pymysql

db = pymysql.connect('127.0.0.1','root','','mybooks',charset='utf8')
cursor = db.cursor()

cursor.execute('select * from books')
data = cursor.fetchall()
print(type(data))
'''
for row in data:
    print(row[0],row[1])
'''
db.close()




