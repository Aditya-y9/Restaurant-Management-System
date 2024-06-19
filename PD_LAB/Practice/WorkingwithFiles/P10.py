path = "C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB" + "aditya.txt"

with open(path, 'r') as f:
    cont = f.readlines()

print(type(cont), cont)

for i in cont:
    print(i)
    
# Counting the number of lines in a file
path = "C:\Users\MSHOME\Desktop\Newfolder\Python\PD_LAB" + "aditya.txt"
with open(path, "r") as f:
    for i in f:
        print(len(i),len(i.strip()))