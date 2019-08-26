'''
Calculater
'''


def num_check1():
  try:
    n=float(input('請輸入第1個數字：'))
    return n
  except ValueError:
    return False

def num_check2():
  try:
    n=float(input('請輸入第2個數字：'))
    return n
  except ValueError:
    return False

def cal_check():
  print('''
        (1)加法
        (2)減法
        (3)乘法
        (4)除法(商數)
        ''')
  try:
    c=int(input('請輸入功能: '))
    return c
  except:
    return False

def run_check():
  while True:
    x=num_check1()
    if x== False:
      print('請重新輸入')
    else:
      return x
      break
  while True:
    z=cal_check()
    if z== False or z not in [1, 2, 3, 4]:
      print('請重新輸入')
    else:
      return z
      break
  while True:
    y=num_check2()
    if y== False:
      print('請重新輸入')
    elif z==4 and y==0:
      print('請重新輸入')
    else:
      return y
      break

def run_cal():
  x,y,z=run_check()
  if z == 1:
    st=x+y
  elif z== 2:
    st=x-y
  elif z== 3:
    st=x*y
  else:
    st=x/y
  return st

def calculate():
  cal=run_cal()
  print(cal)






