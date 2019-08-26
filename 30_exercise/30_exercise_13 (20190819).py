# -*- coding: utf-8 -*-
"""
讀取input.csv
寫入30_output.csv
ver.2
"""
#結構主體 & 結果輸出
def main():
  import csv
  #設路徑為變數
  infile01=r'input.csv'
  outfile02=r'30_output.csv'
  #讀取CSV(為list)
  with open(infile01,'r',encoding='ansi') as csv_rfile:
    csv_reader=csv.reader(csv_rfile)
    list_report=list(csv_reader)
    #print(list_report)
  #寫入CSV(以list)
  with open(outfile02,'w',newline='',encoding='ansi') as csv_wfile:
    csv_writer=csv.writer(csv_wfile) 
    for row in list_report :
      csv_writer.writerow(row)
    csv_writer.writerow(['-'*10])
    for row in list_report :
      csv_writer.writerow(row)
    csv_writer.writerow(['花茶','15'])
    csv_writer.writerow(['蜜茶','10'])
  with open(outfile02,'r',encoding='ansi') as csv_rfile:
    csv_reader=csv.reader(csv_rfile)
    for row in csv_reader:
      print(row)

#執行
if __name__ == '__main__':
  main()