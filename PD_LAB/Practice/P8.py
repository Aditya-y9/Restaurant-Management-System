import os
print(os.getcwd())

path = "address" + "adoinis.txt"
with open(path, 'r') as f:
  cont = f.read()
print(cont)

path = os.getcwd() + '/'

cont = os.listdir(path)
print(type(cont), cont)

for i in cont:
  print(i)