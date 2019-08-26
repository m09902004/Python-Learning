# -*- coding: utf-8 -*-
"""
column 國語 數學 英文 自然 社會
row 小林 小黃 小陳 小美
ver.1
"""
#匯入 pandas
import pandas as pd

#建立資料
grade = {'':['小林','小黃','小陳','小美'],
'國語':[75,91,71,69],
'數學':[62,53,88,53],
'英文':[85,56,51,87],
'自然':[73,63,69,74],
'社會':[60,65,87,70]}

#將各df建立為變數
grade_data = pd.DataFrame(grade)
last_2 = grade_data.iloc[-2:,:]
grade_sort = grade_data.sort_values('自然',ascending=False)
grade_sort = grade_sort.iloc[:,[0,-2]]
math_Science = grade_sort.iloc[[0,2],[0,2,4]]

#輸出
print_form=('''全部學生成績：
{}\n
後兩位學生成績：
{}\n
依'自然'做排序：
{}\n
第一、三位學生的數學與自然成績：
{}
''')

print(print_form.format(grade_data,last_2,grade_sort,math_Science))
