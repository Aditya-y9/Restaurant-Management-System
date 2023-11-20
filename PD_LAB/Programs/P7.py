f = open('aditya.txt', 'r') 
'''
r: read, a: append, w: write, x: create the file
'''
cont = f.read()
print(type(cont), cont)
f.close()

with open('adoinis.txt', 'r') as f:
  cont = f.read()
print(cont)