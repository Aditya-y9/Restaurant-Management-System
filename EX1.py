# very basic python revision.
# string methods

# match case is very similar to switch case.

s = "A"
match s:
    case "A":
        print("Aditya revised!")
# range(start, end, step)
for i in range(0, 10, 2):
    print(i)







# pip to install libraries(eg pygame,tensorflow,scilearn)
# modules are code written by else which we can use

# comment / uncomment with (Ctrl + /)

# \n new line
# \" double quote escape

print("Not all \"Adityas\" are Adityas")


print("Aditya",7,6)
# by default separator is sep = " ".
# end = "" to escapenew line.

print("Aditya",7,6,sep="%")

print("Aditya",7,6,end="")
print("Aditya")

# dictionaries
# oops
 
class Aditya:
    name=""
    age=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
    


obj = Aditya("aditya", 19)
print(obj.name)


