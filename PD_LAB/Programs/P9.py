path = "address" + "adoinis.txt"
with open(path, 'r') as f:
  cont = f.read(10)
  cont1 = f.read(20)
  cont2 = f.read()

print(cont)
print(cont1)
print(cont2)