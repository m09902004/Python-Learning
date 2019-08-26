# -*- coding: utf-8 -*-
'''
三個數字由小到大排序。
ver.5
'''

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    x=get_value()
    y=get_value()
    z=get_value()
    r=check_value(x,y,z)
    print()
    print(x,y,z,'由小到大排序為：',r)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！
(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  print('\nO~ K~ Bye~ _(:з」∠)_')

#判斷大小
def check_value(x,y,z):
  a=[0,0,0]
  if x >= y:
    if y>=z:
      a=[z,y,x]
    else:
      a=[y,z,x]
  else:
    if y<z:
      a=[x,y,z]
    else:
      a=[x,z,y]
  return a

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
  ┌───────────────┐
  │來比大小吧！騷年 │
  └─v─────────────┘
  (・∀・)つ
''')
  
#執行
if __name__ == '__main__':
  main()
