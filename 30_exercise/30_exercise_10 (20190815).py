# -*- coding: utf-8 -*-
"""
建立通訊錄
ver.10
"""

#結構主體
def main(con_inf):
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()   
    r=get_value()
    print()
    if r == 1:
      add_inf(con_inf)
    elif r == 2:
      check_inf(con_inf) 
    elif r == 3:
      del_inf(con_inf)
    elif r == 4:
      break
    else:
      print('快叫作者來 debug')
    choice = input('''請問要繼續使用嗎 ? (y/n) : ''')
  print()
  good_bye()
  print('\014')
  return con_inf
  
#新增
def add_inf(con_inf):
  print('新增聯絡人')
  name=input('請輸入姓名： ')
  name=name.strip()
  name=name.lower()
  if name != 'finish':
    phone=input('請輸入電話號碼： ')
    phone=phone.strip()
    if phone.lower() == 'finish':      
      phone='未輸入聯絡方式'
      print('聯絡方式未確認')
    con_inf[name]=phone
    nums=str(len(con_inf))
    print("已加入第{:s}筆資料進通訊錄".format(nums))
    print('\t停止新增請輸入 finish\n')
    add_inf(con_inf)  
  else:
    print('取消新增')
  
#查詢
def check_inf(con_inf):
  print('查詢聯絡方式')
  name=input('請輸入姓名： ')
  name=name.strip()
  name=name.lower()
  if name in con_inf:
    print(con_inf[name])
  else:
    print('不在通訊錄中')

#刪除
def del_inf(con_inf):
  print('刪除聯絡資訊')
  name=input('請輸入姓名： ')
  name=name.strip()
  name=name.lower()
  if name in con_inf:
    del con_inf[name]
    print('已刪除')
  else:
    print('不在通訊錄中')
   
#判斷輸入
def get_value():
  while True:
    n_list=[1,2,3,4]
    i=str(n_list[0])
    j=str(n_list[-1])
    try:
      n =int(input("請輸入功能鍵({:s}~{:s}) : ".format(i,j)))
      if n not in n_list:
        print('\n你是來亂的是不是 ! (ﾟ皿ﾟﾒ)')
        continue
      else:
        break
    except:
      print('\n到底是在輸入什麼東西 ! (ﾟ皿ﾟﾒ)')
      continue   
  return n

#關閉程式倒數計時
def good_bye():
  import time
  for i in range(6):
      print("\r",end="")
      print("_(:з」∠)_ O~ K~ Bye{:s}" .format('~'*i),flush = True,end="")
      time.sleep(0.4)
      
#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌──────────────┐
  │1)新增聯絡資訊 │
  │2)查詢聯絡方式 │
  │3)刪除聯絡資訊 │
  │4)關閉通訊錄   │  
  └─v────────────┘
  ก็ʕ•͡ᴥ•ʔ ก้ ''')

#執行 & 建立通訊錄
if __name__ == '__main__':
  if 'con_inf' not in dir():
      con_inf=dict()
  con_inf=main(con_inf)