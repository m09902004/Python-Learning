# -*- coding: utf-8 -*-
'''
基本套版。
ver.0
'''

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    a=get_value()
    #b=get_value()
    #r=check_value(a,b)
    print()
    print('#結果輸出為：',a)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  print()
  good_bye()
  print('\014')

#倒數計時
def good_bye():
  import time
  for i in range(6):
      print("\r",end="")
      print("_(:з」∠)_ O~ K~ Bye{:s}" .format('~'*i),flush = True,end="")
      time.sleep(0.4)

#控制
'''
def check_value(x,y):  
  s=0
  if x > y:
    x,y=y,x
  for i in range(x,y+1) :
    if i % 7!= 0 :
      s += i
  return s
'''

#判斷輸入
def get_value():
  while True:
    try:
      n =eval(input('請輸入數字 : '))
      break
    except:
      print('\n就跟你說了要數字 ! (ﾟ皿ﾟﾒ)')
      continue
  return n

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌─────────┐
  │#起始頁面 │
  └─v───────┘
  ก็ʕ•͡ᴥ•ʔ ก้ ''')
  
#執行
if __name__ == '__main__':
  main()
