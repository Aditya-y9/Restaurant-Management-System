from Programs.P9 import cont1
path = "C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB" + "aditya.txt"

with open(path, 'r') as f:
    
    cont = f.read(10)
    cont1 = f.read(20)
    cont2 = f.read()

print(cont)
print(cont1)
print(cont2)
