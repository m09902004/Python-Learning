# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:55:52 2019

@author: ASUS
"""

import xml.etree.cElementTree as ET

#建立classA標籤
classA = ET.Element("classA")

#建立學生資料
student = ET.SubElement(classA, "student")
ET.SubElement(student, "name").text = "Amy"
ET.SubElement(student, "address").text = "New Taipei City"

student = ET.SubElement(classA, "student")
ET.SubElement(student, "name").text = "Bob"
ET.SubElement(student, "address").text = "Taichung"

student = ET.SubElement(classA, "student")
ET.SubElement(student, "name").text = "Steven"
ET.SubElement(student, "address").text = "Hualin"

#將所有元素建立成元素樹
tree = ET.ElementTree(classA)

tree.write("classA.xml")

#將檔案內容轉換成元素樹
tree = ET.parse("classA.xml")

#取得樹根
root = tree.getroot()

#輸出每個部門的相關資料
for dept in root.findall("student"):
  print("student name:{}".format(dept.find("name").text))
  print("student address:{}".format(dept.find("address").text))
  print()
  
