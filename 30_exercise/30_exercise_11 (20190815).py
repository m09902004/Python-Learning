# -*- coding: utf-8 -*-
"""
建檔&修改內文
ver.6
"""
#結構主體 & 結果輸出
def main():
    
  #開啟檔案
  n =input("請輸入檔名(預設路徑:桌面)： ")
  n='30_ex11_'+n+'.txt'
  text='''My doctor says I'm lacking vitamin U.
Your hand looks heavy, let me hold it for you.
Did the sun just rise or did you just smile at me?'''
  print(text,file=open(r'C:\Users\ASUS\Desktop\{:s}'.format(n),'w'))
  
  #輸出
  with open(r'C:\Users\ASUS\Desktop\{:s}'.format(n),'r') as fileWork:
    show1=fileWork.read()
    print('\n===更改前===\n'+show1)
    #取值欲更改字串 
    n1 =input("請輸入欲更改字串 : ")
    #取值更改後字串
    n2 =input("請輸入更改後字串 : ")
    show2=show1.replace(n1,n2)
    print('\n===更改後===\n'+show2)
   
  #覆蓋
  with open(r'C:\Users\ASUS\Desktop\{:s}'.format(n),'w') as fileWork:
    fileWork.write(show2)

#執行
if __name__ == '__main__':
  main()