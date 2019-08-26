# -*- coding: utf-8 -*-
"""
20 int => array，and so on
ver.2
"""
#匯入 numpy
import numpy as np
#隨機產生 20 個數字組為 array
a=np.random.randint(1,21,20)
x=a.reshape(5,4)
#取 x 邊角的四個值為 array y
y=x[np.ix_([0,4],[0,3])];y
#輸出
print_form='''隨機正整數：
{}
---
X矩陣內容：
{}
---
最大：{}
最小：{}
平均：{}
總合：{}
標準差：{}
---
四個角落元素：
{}'''
print(print_form.format(a,x,np.max(x),np.min(x),np.mean(x),np.sum(x),np.std(x),y))
