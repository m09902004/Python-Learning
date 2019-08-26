# -*- coding: utf-8 -*-
"""
前5筆作物代號，作物名稱，平均價，交易量
ver.3
"""
#匯入套件
import xml.etree.ElementTree as et
import csv

#匯入原始資料(xml)為(tree)
file_xml=r'C:\Users\ASUS\Desktop\FarmTransData.xml'
tree = et.ElementTree(file=file_xml)
root=tree.getroot()

#寫入檔案(csv)
file_csv=r'C:\Users\ASUS\Desktop\30_write.csv'

#定義輸出用變數
print_var='作物代號：{}\n作物名稱：{}\n平均價：{}\n交易量：{}\n'
i=0

#取出需要的檔案並逐筆寫入
with open(file_csv,'w',newline='',encoding='utf-8') as csvfile:
  csv_writer=csv.writer(csvfile)
  csv_writer.writerow(['作物代號','作物名稱','平均價','交易量'])
  for row in root.findall('row'):
    a=row.find('作物代號').text
    b=row.find('作物名稱').text
    c=row.find('平均價').text
    d=row.find('交易量').text
    csv_writer.writerow([a,b,c,d])
    if i<5:
      #只輸出前5筆資料
      print(print_var.format(a,b,c,d))
    i+=1
      