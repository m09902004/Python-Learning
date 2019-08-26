# -*- coding: utf-8 -*-
"""
前5筆作物代號，作物名稱，平均價，交易量
ver.1
"""
#匯入套件
import xml.etree.ElementTree as et
import csv

#匯入原始資料(xml)
file_xml=r'FarmTransData.xml'
tree = et.ElementTree(file=file_xml)
root=tree.getroot()

#取出需要的欄位內容(for)
all_crop=[]
i=0
print_var='作物代號：{}\n作物名稱：{}\n平均價：{}\n交易量：{}\n'
for row in root.findall('row'):
  crop=[]
  a=row.find('作物代號').text
  b=row.find('作物名稱').text
  c=row.find('平均價').text
  d=row.find('交易量').text
  crop=[a,b,c,d]
  all_crop.append(crop)
  if i<5:
    print(print_var.format(a,b,c,d))
  i+=1

#寫入新的檔案(for)
file_csv=r'30_write.csv'
with open(file_csv,'w',newline='',encoding='utf-8') as csvfile:
  csv_writer=csv.writer(csvfile)
  csv_writer.writerow(['作物代號','作物名稱','平均價','交易量'])
  for i in range(len(all_crop)):
    csv_writer.writerow([all_crop[i][0],all_crop[i][1],all_crop[i][2],all_crop[i][3]])
