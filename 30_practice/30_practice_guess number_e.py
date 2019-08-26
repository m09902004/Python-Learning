def guessnumber():
  def main():
    choice = 'y'
    while choice.lower() == 'y':
      code = getcode()
      start_game(code)
      choice = input("再玩一次(Y/N) : ")
    print('感謝使用本程式')
  def getcode():
    import random
    code = random.randrange(1,100)
    return code
  def start_game(code):
    cmin,cmax = 1,100
    while True:
      v = int(input('密碼範圍'+str(cmin)+' - '+str(cmax)+' : '))
      if v == code:
        print('恭喜您!! 猜對了')
        break
      elif v > code:
        cmax = v
      elif v < code:
        cmin = v
  main()
