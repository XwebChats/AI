
def Add():
  n1 = float(input('n1: '))
  n2 = float(input('n2:'))
  print(f"{n1} + {n2} = {n1+n2}")
def Minus():
  n1 = float(input('n1: '))
  n2 = float(input('n2: '))
  print(f'{n1} - {n2} = {n1 - n1}')
def Pip3():
  import os
  lib = input('library name: ')
  os.system(f'pip3 install {lib}')
def Terminal():
  import os
  commandl = input('command: ')
  os.system(commandl)
def Python3():
  import os
  path = input('file path:')
  os.system(f'python3 {path}')
def Update():
  import os
  os.system('python3 upat.py')
  exit(0)
