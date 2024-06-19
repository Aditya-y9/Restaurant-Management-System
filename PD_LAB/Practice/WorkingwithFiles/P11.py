path = "C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB" + "aditya.txt"
f = open(path, 'a')
f.write("Fourth Line")
f.close()

f = open(path, 'r')
print(f.read())
f.close()

path = "C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB" + "aditya.txt"
f = open(path, 'w')
f.write("Fourth Line")
f.close()

f = open(path, 'r')
print(f.read())
f.close()