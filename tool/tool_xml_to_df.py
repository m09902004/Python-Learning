# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 21:58:10 2019

@author: DioChen
"""

#匯入套件
import xml.etree.cElementTree as ET
import pandas as pd

#讀取來源(xml)
file_xml = r'file_name.xml'
tree = ET.ElementTree(file=file_xml)
root = tree.getroot()
root.tag, root.attrib

#先將資料轉為 dict
xml_dict = {}
# root 為根目錄
# child_of_root 為 root 的子目錄
# gchild_of_root 為 child_of_root 的子目錄
for child_of_root in root:
  for gchild_of_root in child_of_root:
    if gchild_of_root.tag not in xml_dict:
      xml_dict[gchild_of_root.tag] = list()
    else:
      xml_dict[gchild_of_root.tag].append(gchild_of_root.text)
      
#先將 dict 轉為 DataFrame
xml_df = pd.DataFrame.from_dict(xml_dict)  