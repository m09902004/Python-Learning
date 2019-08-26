# -*- coding: utf-8 -*-
"""
A字串中B出現幾次
ver.3
"""

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    compute() 
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  input('\nO~ K~ Bye~ _(:з」∠)_')
  print('\014')

def compute():
  a=input('請輸入A : ')
  b=input('請輸入B : ')
  print()
  print(b,'occurs',a.count(b),'time(s)')

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌────────────────────┐
  │A字串中B出現幾次呢？  │
  └─v──────────────────┘
  ก็ʕ•͡ᴥ•ʔ ก้
''')
  
#執行
if __name__ == '__main__':
  main()
