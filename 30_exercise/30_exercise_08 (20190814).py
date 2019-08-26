# -*- coding: utf-8 -*-
'''
猜撲克牌。
ver.87
'''
#結構主體
def main():
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    point=get_goal()
    check_value(point)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  input('\nO~ K~ Bye~ _(:з」∠)_')
  print('\014')
  
#判斷大小
def check_value(c):
  cmin,cmax = 1,13
  sum_c=1
  while True:
    g_raw = get_value(cmin,cmax)
    g = sort_value(g_raw)
    if g == c:
      print('阿不就好棒棒猜到了')
      print('總共猜了',str(sum_c),'次')
      break
    elif g > c:
      cmax = g 
      sum_c+=1
    elif g < c:
      cmin = g
      sum_c+=1
    
#整理輸入值(數字)
def sort_value(raw):
  num=['1','2','3','4','5','6','7','8','9','10','11','12','13']
  cka=['K','KING','Q','QUEEN','J','JACK','A','ACE']
  raw=str(raw)
  new=1
  if raw.upper() in cka:
    raw=raw.upper()
    new=alph_tran(raw) 
  elif raw in num :
    new = eval(raw) 
  else:
    print('認真點好嗎？')
  return new

#整理輸入值(字串)
def alph_tran(rawd):
  now = 1  
  if rawd == 'K' or rawd =='KING':
    now = 13
  elif rawd == 'Q' or rawd =='QUEEN':
    now = 12
  elif rawd == 'J' or rawd =='JACK':
    now = 11
  elif rawd == 'A' or rawd =='ACE':
    now = 1
  else:
    print('特殊異常，請找作者本人回報')
  return now

#求取輸入值
def get_value(cmin,cmax):
  ck=['1','11','12','13']
  if str(cmin) in ck :
    if str(cmin) == '1':
      cmin = 'Ace'
    elif str(cmin) == '11':
      cmin = 'J'
    elif str(cmin) == '12':
      cmin = 'Q'
    elif str(cmin) == '13':
      cmin = 'K'
  if str(cmax) in ck :
    if str(cmax) == '1':
      cmax = 'Ace'
    elif str(cmax) == '11':
      cmax = 'J'
    elif str(cmax) == '12':
      cmax = 'Q'
    elif str(cmax) == '13':
      cmax = 'K' 
  cmin=str(cmin)
  cmax=str(cmax)
  r=input('請猜'+cmin+'-'+cmax+'之間的撲克牌 : ')
  return r

#隨機指定正確答案
def get_goal():
  import random
  goal = random.randint(1,13)
  return goal

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌─────────────────────┐
  │烹油我們來玩猜撲克牌吧！│
  └─v───────────────────┘
  ก็ʕ•͡ᴥ•ʔ ก้
''')

#執行
if __name__ == '__main__':
  main()
