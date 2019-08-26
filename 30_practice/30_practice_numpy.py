# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:03:58 2019

@author: ASUS
"""

import numpy as np

x=np.random.randn(5,5)
x1=np.round(x,2);x1

#start(2_sx,1_sy),end(5_ex,4_ey)
#第2(sy+1)筆到第4(ey)筆 的 第3(sx+1)項到第5(ex)項
slice = x1[1:4,2:5]
print(x1)
print(slice)
