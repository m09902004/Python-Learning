'''
movie menu
'''
def display_menu():
  print('''
movie menu:
(A)Show Movie List
(B)Add Movie
(C)Edit Movie List
(D)Delet Movie
(E)Exit
        ''')

def show_list(ml):
  i = 1
  print('Movie List: \n')
  for m in ml:
    print(str(i)+' '+m+'\n')
    i += 1
  
def add_movie(ml):
  m=input('New Movie Name:')
  ml.append(m)
  print(m+' added\n')

def edit_list(ml):
    m=int(input('Choose a Movie:'))
    n=str(input('Replace a Movie:'))
    if m < 1 or m > len(ml):
      print('Invaild movie number')
    else:
      ml[m-1]=n
  
def del_movie(ml):
  m=int(input('Movie Number:'))
  if m < 1 or m > len(ml):
    print('Invaild movie number')
  else:
    m = ml.pop(m-1)
    print(m + ' was delete\n')
  
def movie_menu():
  movie_list = ["Lion King","Toy Story","Iron Man","Spider Man"]
  display_menu()
  while True:  
    mf = str(input('Commmand : '))
    if mf.lower() == 'a':
      show_list(movie_list)
    elif mf.lower() == 'b':
      add_movie(movie_list)
    elif mf.lower() == 'c':
      edit_list(movie_list)
    elif mf.lower() == 'd':
      del_movie(movie_list)
    elif mf.lower() == 'e':
      break
    else :
      print('Please try again')
  print('bye!')      
