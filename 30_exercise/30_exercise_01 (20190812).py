# -*- coding: utf-8 -*-
'''
五個數字 & 總合 & 平均。
ver.7
'''

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    a=get_list()
    sum_a=round(sum(a),1)
    avg_a=round(sum_a/len(a),1)
    print()
    print(a,'\n總合 = ',sum_a,'\n平均 = ',avg_a)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！
(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  print('\nO~ K~ Bye~ _(:з」∠)_)')

#
def get_list():
  l=[]
  for i in range(0,5,1):
    n=eval(get_value())
    l.append(n)
  return l

#判斷輸入 & 取值
def get_value():
  while True:
    try:
      n =input('請輸入數字 :')
      break
    except:
      print('就跟你說了要數字 ! (ﾟ皿ﾟﾒ)')
      continue
  return n

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌───────────────┐
  │輸入數字吧！騷年 │
  └─v─────────────┘
  (・∀・)つ
''')
  
#執行
if __name__ == '__main__':
  main()
