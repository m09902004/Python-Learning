# -*- coding: utf-8 -*-
"""
輸入數字(1~10)決定層數 , 依序輸入(1~10)各層星數
ver.7
"""

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    n=get_value1()
    for i in range(n):
      m=get_value2()
      for j in range(m):
        print('*',end='')
    choice = input('''\n再看一次星星吧｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡！(y/n) : ''')
  print('\n星星討厭你 _(:з」∠)_')

#判斷輸入
def get_value1():
  while True:
    try:
      n =eval(input('請輸入數字(1~10)決定層數 : '))
      break
    except:
      print('\n就跟你說了要數字 ! (ﾟ皿ﾟﾒ)')
      continue
  return n

#判斷輸入
def get_value2():
  while True:
    try:
      n =eval(input('請輸入數字(1~10)決定星數 : '))
      break
    except:
      print('\n就跟你說了要數字 ! (ﾟ皿ﾟﾒ)')
      continue
  return n

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌───────────────┐
  │來看星星吧！騷年 │
  └─v─────────────┘
  （<ゝω・）ノ☆
''')
  
#執行
if __name__ == '__main__':
  main()
