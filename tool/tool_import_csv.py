# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 09:57:33 2019

@author: ASUS
"""
#讀取CSV(為list)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf-8') as csv_file:
  csv_reader=csv.reader(csv_file)
  list_report=list(csv_reader)
print(list_report)

#讀取CSV(為list)(for)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf8') as csv_file:
  csv_reader=csv.reader(csv_file)
  for row in csv_reader:
    print("Row {:d} = ".format(csv_reader.line_num),row)
    
#讀取CSV(為list)(指定索引)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf-8') as csv_file:
  csv_reader=csv.reader(csv_file)
  list_report=list(csv_reader)
print(list_report[0][0],list_report[0][1],list_report[0][2])
print(list_report[1][0],list_report[1][1],list_report[1][2])
print(list_report[-1][0],list_report[-1][1],list_report[-1][2])

#讀取CSV(為dict)(for)(row)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf-8') as csv_file:
  csv_dictreader=csv.DictReader(csv_file)
  for row in csv_dictreader:
    print(row)

#讀取CSV(為dict)(for)(key)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf-8') as csv_file:
  csv_dictreader=csv.DictReader(csv_file)
  for row in csv_dictreader:
    print(row['name'],row['phone'],row['email'])

#讀取CSV(為dict)(做成list)
import csv
file01=r'C:\Users\ASUS\Desktop\ansi.csv'
with open(file01,encoding='utf-8') as csv_file:
  csv_dictreader=csv.DictReader(csv_file)
  dict_report=list(csv_dictreader)
print(dict_report)

#寫入CSV(以list)
import csv
file01=r'C:\Users\ASUS\Desktop\csv_output.csv'
with open(file01,'w',newline='',encoding='utf-8') as csv_file:
  csv_writer=csv.writer(csv_file,delimiter='\t')#delimiter預設為逗點
  csv_writer.writerow(['name','phone','email'])
  csv_writer.writerow(['alex','0987','a@gmail.com'])
  csv_writer.writerow(['くまモン','0944','f@gamil.com'])

#寫入CSV(以dict)
import csv
file01=r'C:\Users\ASUS\Desktop\csv_dictoutput.csv'
with open(file01,'w',newline='',encoding='utf-8') as csv_file:
  fields=['name','phone','email']
  csv_dictwriter=csv.DictWriter(csv_file,fieldnames=fields)
  csv_dictwriter.writeheader()
  csv_dictwriter.writerow({'name':'alex','phone':'0987','email':'a@gmail.com'})
  csv_dictwriter.writerow({'name':'くまモン','phone':'0944','email':'f@gamil.com'})

#寫入CSV(以dict)(for)
import csv
dictlist=[{'name':'alex','phone':'0987','email':'a@gmail.com'},{'name':'くまモン','phone':'0944','email':'f@gamil.com'}]
file01=r'C:\Users\ASUS\Desktop\csv_dictoutput.csv'
with open(file01,'w',newline='',encoding='utf-8') as csv_file:
  fields=['name','phone','email']
  csv_dictwriter=csv.DictWriter(csv_file,fieldnames=fields)
  csv_dictwriter.writeheader()
  for row in dictlist:
    csv_dictwriter.writerow(row)

#讀取 & 寫入CSV
import csv
infile01=r'C:\Users\ASUS\Desktop\ansi.csv'
outfile02=r'C:\Users\ASUS\Desktop\csv_output.csv'
with open(infile01,encoding='utf-8') as csv_rfile:
  csv_reader=csv.reader(csv_rfile)
  list_report=list(csv_reader)
with open(outfile02,'w',newline='',encoding='utf-8') as csv_wfile:
  csv_writer=csv.writer(csv_wfile)
  for row in list_report :
    csv_writer.writerow(row)
