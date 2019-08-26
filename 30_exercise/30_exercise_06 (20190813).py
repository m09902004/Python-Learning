# -*- coding: utf-8 -*-
"""
a符號 b欄數 c列數
ver.6
"""

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    a=input('請輸入任意符號 : ')
    b=get_value()
    c=get_value()
    print()
    show(a,b,c)
    choice = input('''(」・ω・)」超好看！(/・ω・)/再一次！(y/n) : ''')
  print('\nO~ K~ Bye~ _(:з」∠)_')

#show圖
def show(x,y,z):
  x=x+' '
  for i in range(z):
    print(x*y)

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
  ┌─────────────┐
  │親手畫圖給你♡ │
  └─v───────────┘
  ก็ʕ•͡ᴥ•ʔ ก้
''')
  
#執行
if __name__ == '__main__':
  main()
