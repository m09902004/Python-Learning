# -*- coding: utf-8 -*-
'''
猜數字-終極密碼
ver.20
'''

#結構主體
def main():
  # goal = 正確答案
  choice = 'y'
  while choice.lower() == 'y':
    display_menu()
    goal = get_goal()
    check_value(goal)
    choice = input('''(」・ω・)」再一次！(/・ω・)/再一次！(y/n) : ''')
  print()
  good_bye()
  print('\014')

#判斷大小
def check_value(goal):
  # goal=正確答案
  # range_min = 最小值, range_max = 最大值
  # good_count = 範圍內猜測次數 , bad_count = 範圍外猜測次數
  # guess = 符合格式的猜測值
  range_min,range_max = -37,73
  good_count = 1
  bad_count = 0
  while True:
    guess = get_value(range_min,range_max)  
    if guess != 'quit':
      if guess == goal:
        print('\n猜到了，阿不就好棒棒ლ（╹ε╹ლ）'.format(good_count))
        print('總共猜了{:d}次'.format(good_count))
        break
      elif guess > range_max:
        print('數字太大，已超出範圍，請重新輸入')
        bad_count += 1
      elif guess < range_min:
        print('數字太小，已超出範圍，請重新輸入')
        bad_count += 1
      elif guess > goal:
        range_max = guess 
        print('答錯，目前猜了{:d}次'.format(good_count))
        good_count += 1
      elif guess < goal:
        range_min = guess
        print('答錯，目前猜了{:d}次'.format(good_count))
        good_count += 1
      if good_count > 5 or bad_count > 2:
          print('累了吧？想放棄就 quit 吧ʅ（´◔౪◔）ʃ')
    #傳說中的中途放棄機制
    elif guess == 'quit':
      print('\n放棄遊戲')
      break

#求取輸入值
def get_value(range_min,range_max):
  # range_min = 最小值 , range_max = 最大值
  # raw_guess = 原始猜測值 , guess = 符合格式的猜測值
  while True:
    raw_guess = input('請猜{:d}到{:d}之間的撲克牌 : '.format(range_min,range_max))
    #傳說中的中途放棄機制
    if raw_guess.strip().lower() == 'quit':
      guess = 'quit'
      break
    elif raw_guess.strip().lower() != 'quit':
      try:
        guess = int(str(eval(raw_guess)))
        break
      except NameError:
        print('\n你當這是簽名版呀！(ﾟ皿ﾟﾒ)')
      except SyntaxError:
        print('\n至少也來個數字吧！(ﾟ皿ﾟﾒ)')
      except ValueError:
        print('\n大哥請給我整數呀！(ﾟ皿ﾟﾒ)')
      except UnboundLocalError:
        print('\n保安！這個人來亂的 (ﾟ皿ﾟﾒ)')
      except Exception as ex :
        print(ex.args)
      #else:
      #finally:
  return guess

#隨機指定正確答案
def get_goal():
  #goal=正確答案
  import random
  goal = random.randint(-37,73)
  return goal 

#倒數計時
def good_bye():
  import time
  for i in range(6):
      print("\r",end="")
      print("_(:з」∠)_ O~ K~ Bye{:s}" .format('~'*i),flush = True,end="")
      time.sleep(0.4)

#讓人尷尬又不失禮貌的起始頁面
def display_menu():
  print('''
  ┌───────────────┐
  │來猜數字吧！騷年│
  └─v─────────────┘
  ก็ʕ•͡ᴥ•ʔ ก้
''')

#執行
if __name__ == '__main__':
  main()
  