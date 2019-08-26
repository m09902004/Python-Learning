# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:59:07 2019

@author: ASUS
"""

import xml.etree.ElementTree as et
proj_xml=r'C:\Users\ASUS\Desktop\108070130\open data\A17030000J-000049-BWn.xml'
tree = et.ElementTree(file=proj_xml)
root=tree.getroot()
print(root.tag)
for main_branch in root:
  print('tag:',main_branch.tag,'attributes:',main_branch.attrib)
  for sec_branch in main_branch:
    print('\ttag:',sec_branch.tag,'attributes:',sec_branch.attrib)
print(len(root))
print(len(root[0]))

import xml.etree.ElementTree as et
file_xml=r'C:\Users\ASUS\Desktop\menu.xml'
tree = et.ElementTree(file=file_xml)
root=tree.getroot()
print(root.tag)
for main_branch in root:
  print('tag:',main_branch.tag,'attributes:',main_branch.attrib)
  for sec_branch in main_branch:
    print('\ttag:',sec_branch.tag,'attributes:',sec_branch.attrib)
print(len(root))
print(len(root[0]))

