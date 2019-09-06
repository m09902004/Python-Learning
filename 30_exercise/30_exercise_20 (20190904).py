# -*- coding: utf-8 -*-
"""
讀讀寫寫
ver.0
"""

import pandas as pd
'''
#一般版
data = pd.read_html('read.html')[1]
data.to_csv('30_write.csv', index = False, float_format = '%.3f', encoding = 'utf-8')
'''
#超級精簡版
pd.read_html('read.html')[1].to_csv('30_write.csv', index = False, float_format = '%.3f', encoding = 'utf-8')
