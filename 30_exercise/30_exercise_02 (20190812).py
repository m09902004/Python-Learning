# -*- coding: utf-8 -*-
'''
找出閏年, 4年閏, 100年平, 400年閏。
ver.5
'''

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    y=get_value()
    r=check_value(y)
    print()
    if r == True:
      print(y,'年是"閏年"')
    else:
      print(y,'年是"平年"')
    choice = input('''(」・ω・)」再一年！(/・ω・)/再一年！
(」・ω・)」再一年！(/・ω・)/再一年！(y/n) : ''')
  print('\nO~ K~ Bye~ _(:з」∠)_')

#判斷閏年
def check_value(y):
  if y % 400 == 0:
    return True
  elif y % 100 != 0 and y % 4 == 0:
    return True
  else:
    return False 

#判斷輸入
def get_value():
  while True:
    try:
      n =int(input('請輸入西元年 : '))
      break
    except:
      print('就跟你說了要年分 ! (ﾟ皿ﾟﾒ)')
      continue
  return n

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌───────────────┐
  │輸入年分吧！騷年 │
  └─v─────────────┘
  (・∀・)つ
''')

#執行
if __name__ == '__main__':
  main()
