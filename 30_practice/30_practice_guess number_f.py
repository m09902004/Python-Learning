"""
終極密碼 - 猜數字遊戲
"""
import random


def game_menu():
  """
  遊戲選單
  -------------------------------------
    title   : 遊戲選單標題
    msg     : 選單內容
    diff    : 用於接收遊戲者所選擇的難易程度
  """
  title = '終極密碼 - 猜數字遊戲'
  print(title.center(50))
  print()
  msg = '''
  密碼難度：
    A -> 2位數密碼
    B -> 3位數密碼
    C -> 4位數密碼
    Z -> 離開
  '''
  print('=' * 50,msg,'=' * 50,sep = '\n')
  print()
  diff = input('請選擇遊戲難度 : ')
  return diff
  
def getcode(diff):
  """
  產生密碼
  -------------------------------------
    df   : 用於儲存 diff 參數轉換成小寫字母
    ran  : 用於記錄遊戲的範圍最大值
  """
  df = diff.lower()
  if df == 'a':
    ran = 100
  elif df == 'b': 
    ran = 1000
  elif df == 'c':
    ran = 10000
  
  code = random.randrange(1,ran)
  return code,ran


def start_game(code,ran):
  """
  開始進入遊戲
  -------------------------------------
    times   : 用於記錄猜數字的次數
    cmax    : 用於記錄密碼範圍的最大值
    cmin    : 用於記錄密碼範圍的最小值
    v       : 用於儲存遊戲者所猜測的密碼
  """
  times = 1
  cmax,cmin = ran,1
  print('密碼範圍 : '+str(cmin)+' - '+str(cmax))
  while True:
    v = int(input('第 '+str(times)+' 次猜 : '))
    if v == code:
      print('恭喜您!! 猜對了')
      break
    elif v > code:
      cmax = v
    elif v < code:
      cmin = v
    print(str(cmin)+' 到 '+str(cmax)+' 之間 ')
    times += 1
    
    
def guessnumber():
  """
  變數：
    choice : 用於 while 迴圈判斷
    diff   : 用於接收由 game_menu 函數所回傳的遊戲難易度
    code   : 用於儲存由 random.randrange 函數所產生的密碼
    ran    : 用於顯示密碼的最大值範圍
    
  函數：
    game_menu : 用於顯示遊戲選單，並接收遊戲者所輸入的難易度
    getcode   : 用於產生遊戲所需的密碼
    start_game: 用於開始遊戲
  """
  choice = 'y'
  while choice.lower() == 'y':
    diff = game_menu()
    if(diff.lower() in ['a','b','c']):
      code,ran = getcode(diff)
    elif diff.lower() == 'z':
      break
    else:
      print('輸入代碼錯誤，請重新輸入')
      continue
    
    start_game(code,ran)
    
    print()
    choice = input("再玩一次(Y/N) : ")
    print('-' * 50)
    print()
  print('感謝使用本程式')
