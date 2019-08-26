'''
上課練習的玩意兒
str_practice()    字串實驗
lagh()            嘲笑你~
grade()           考試分數
rw()              零售批發折扣
stars()           新星星知我心
fund_easy()       低能版基金投報
fund()            高能版基金投報
getprime()        查找質數
temperature()     攝氏華氏溫度轉換
to be contitue... 待續
'''

def str_practice():
  strA='Office 2019 Professional'
  print(strA)
  strB='Adobe CC 2018'
  print(strB)
  strA1=strA.split()
  print(strA1)
  strB1=strB.split()
  print(strB1)
  strC=int(strA1[1])+int(strB1[2])
  print(strC)
  print('strA.find(空集合)',strA.find('ia'))

def lagh():
  strX='''
  ┌───────────────┐
  │哈哈！你不會拍森 │
  └─v─────────────┘
  (☞ﾟ∀ﾟ)ﾟ∀ﾟ)☞
  '''
  print(strX)
  
def grade():
  x=0
  while True:
    x = int(input('國文:'))
    if x>=0 and x<=100:
     print('輸入正確')
     break
    else :
     print('到底是在輸入什麼東西！ ლ(´•д• ̀ლ)')
  while True:
    y=int(input('英文:'))
    if y>=0 and y<=100:
      print('輸入正確')
      break
    else :
      print('到底是在輸入什麼東西！ ლ(´•д• ̀ლ)')
  while True:
    z=int(input('數學:'))
    if z>=0 and z<=100:
      print('輸入正確')
      break
    else :
      print('到底是在輸入什麼東西！ ლ(´•д• ̀ლ)')     
  g=x+y+z
  print('\n總分:',g)
  if g<180:
    print('這什麼狗淦分數？我阿罵都考比你好 (ಠ益ಠ)')
  else:
    print('阿不就好棒棒 (´_ゝ`)')


def rw():
  choice = 'y'
  while choice.lower() == 'y':
    rw=input('請輸入會員類別(R/W):')
    if rw.lower()== 'r':
      mt=str('零售商')
      paid=int(input('請輸入購買金額(買不到1000吼林周罵給你好看):'))
      if paid>10000:
        dc=0.8
        dcc = str('8折')
      elif paid>5000:
        dc=0.9
        dcc = str('9折')
      elif paid>1000:
        dc=0.95
        dcc = str('95折')
      else:
        dc=1
        dcc = str('沒折扣啦，小窮逼！ (ﾟ皿ﾟﾒ)') 
      print('本次交易\n會員類別:',mt,'\n原價:',paid,'\n折扣:',dcc,'\n實收:',round(paid*dc,0))
    elif rw.lower()== 'w':
      mt=str('批發商')
      paid=int(input('請輸入購買金額(買不到1000吼林周罵給你好看):'))
      if paid>10000:
        dc=0.6
        dcc = str('6折')
      elif paid>5000:
        dc=0.7
        dcc = str('7折')
      elif paid>1000:
        dc=0.75
        dcc = str('75折')
      else:
        dc=1
        dcc = str('還想要折扣，當林周罵慈善事業膩？ (╯#`Д´)╯︵┴─┴')
      print('本次交易\n會員類別:',mt,'\n原價:',paid,'\n折扣:',dcc,'\n實收:',round(paid*dc,0))
    else :
      print('到底是在輸入什麼東西！ (╬☉д⊙)')
    choice = input("是否繼續試算 (Y/N) ？: ")

def stars():
  import math
  choice = 'y'
  while choice.lower() == 'y':
    lb=int(input('請輸入層數:'))
    i=0
    if lb%2 !=0:
      i=0
      while True:
        lb2=lb/2
        lb3=math.floor(lb2)
        lb4=math.ceil(lb2)
        if i == lb+1:
          break
        elif  i > lb2:
          print(' '*(i-lb3),'* '*(lb+1-i))
          i=i+1
        else :
          print(' '*(lb4+1-i),'* '*i)
          i=i+1  
    elif  lb%2 ==0:
      i=0
      while True:
        lb2=int(lb/2)
        if i == lb+1:
          break
        elif  i > lb2:
          print(' '*(i-(lb2)),'* '*(lb+1-i))
          i=i+1
        else:
          print(' '*(lb2+1-i),'* '*i)
          i=i+1
    else:
      print('不要鬧了好嗎？')
    choice = input("是否繼續試算 (Y/N) ？: ")    

def fund():
  def main():
    display_menu()
    choice = 'y'
    while choice.lower() == 'y':
      import math
      x,y,z = get_value()
      g = calculate(x,y,z)
      print('\n預估獲利:',math.ceil(g))
      choice = input("是否繼續試算 (Y/N) ？: ")
  def display_menu():
    print('基金投報評估')
  def get_value():
    x=float(input('每月投資額:'))
    y=float(input('年利率(%):'))
    z=float(input('投資年數:'))
    return x,y,z
  def calculate(x,y,z):
    x1=x*12
    y1=(y/100)+1
    g=(x1*(y1**z))-x1*y1
    return g 
  main()

def getprime():
  def main():  
    choice = 'y'
    while choice.lower() == 'y':
      n = int(input('請輸入最大值:'))
      prime(n)
      for i in range(2,n):
          temp = prime(i)
          if temp == True:
              print(i)
      choice = input('Try again(Y/N)?:')    
  def prime(n):
    for i in range(2,n):
      if n % i == 0:
        return False
      return True
  main()

def temperature(): 
  def main():
    choice = 'y'
    while choice.lower() == 'y':
      check()
      choice = input('Try again(Y/N)?:')
  def check():
    t=input('請選擇轉換方式\n(A)攝氏轉華氏\n(B)華氏轉攝氏\n請選擇(A/B):')
    import math
    if t.lower() == 'a' :
      o=calculate1()
      print('轉換後華氏溫度:',math.ceil(o))
    elif t.lower() == 'b':
      o=calculate2()
      print('轉換後攝氏溫度:',math.ceil(o))
    else:
      print('不要鬧好嗎？')
  def calculate1():
    i=float(input('攝氏溫度:'))
    o=((i+40)/1.8)-40
    return o
  def calculate2():
    i=float(input('華氏溫度:'))
    o=((i+40)*1.8)-40
    return o
  main()
  
def fund_easy():
  print('基金投報評估')
  x=float(input('每月投資額:'))
  y=float(input('年利率(%):'))
  z=float(input('投資年數:'))
  print('\n預估獲利:',x*y*z*0.12)

#if __name__ == '__main__':
#  main()  可以植入任何希望直接執行的函數or程序
