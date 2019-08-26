# -*- coding: utf-8 -*-
'''
AB之間(包和各自) , 所有非七之倍數數字總合。
ver.9
'''

#結構主體 & 結果輸出
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    a=get_value()
    b=get_value()
    #a,b=sort_value(a,b)
    if a>b:
      a,b=b,a
    t=check_value(a,b)
    print()
    print(a,'跟',b,'之間非七之倍數數字總合為：',t)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！
(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  print('\nO~ K~ Bye~ _(:з」∠)_')

#加總
def check_value(x,y):  
  s=0
  for i in range(x,y+1) :
    if i % 7!= 0 :
      s += i
  return s

#我想排序
'''
def sort_value(x,y):
  l=[x,y]
  l.sort()
  x=l[0]
  y=l[1]
  return x,y
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
  ┌────────────────────┐
  │求 A~B 非 7 倍數總和♡│
  └─v──────────────────┘
  ก็ʕ•͡ᴥ•ʔ ก้
''')
  
#執行
if __name__ == '__main__':
  main()
