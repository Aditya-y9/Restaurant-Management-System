import tkinter as tk
import math


# to create a window
# root window
root = tk.Tk()

# to set the title of the window
root.title("PD LAB")

# to set the size of the window (fixed)

# geometry("width x height + X_POS + Y_POS")
root.geometry("900x600+200+25")

# resizable h?
root.resizable(False, False)

# to set the background color of the window
# .configure() method is used to configure the widget specific parameters
root.configure(bg="#2A2D36",border=10,borderwidth=10,relief="sunken")

# init screen empty
equation = ""

def sin():
    global equation
    # to update the equation in the string
    eq = equation
    clear()
    equation += "math.sin(" + str(float(eq)*math.pi/180) + ")"
    label_result.configure(text=equation.replace("math.",""))

def cos():
    global equation
    # to update the equation in the string
    eq = equation
    clear()
    equation += "math.cos(" + str(float(eq)*math.pi/180) + ")"
    label_result.configure(text=equation.replace("math.",""))

def tan():
    global equation
    # to update the equation in the string
    eq = equation
    clear()
    equation += "math.tan(" + str(float(eq)*math.pi/180) + ")"
    label_result.configure(text=equation.replace("math.",""))

def erase():
    global equation
    equation = equation[:-1]
    label_result.configure(text=equation)


def sqrt():
    global equation
    # to update the equation in the string
    equation += "math.sqrt("

    # to update the equation in the label
    label_result.configure(text=equation.replace("math.sqrt","√"))

def square():
    global equation
    # to update the equation in the string
    equation += "**2"

    # to update the equation in the label
    label_result.configure(text=equation.replace("**2","²"))


def power():
    global equation
    # to update the equation in the string
    equation += "**"

    # to update the equation in the label
    label_result.configure(text=equation.replace("**","^"))

def fact():
    # assign to global var
    global equation

    # to update the equation in the string
    equation += "math.factorial("

    # to update the equation in the label each time
    label_result.configure(text=equation.replace("math.factorial","!"))



def show(value):
    global equation
    # to update the equation in the string
    equation += value

    # to update the equation in the label
    label_result.configure(text=equation)

def clear():
    # assigin pointer to global var
    global equation

    # reset the equation string
    equation = ""

    # update the label
    label_result.configure(text=equation)

def calculate():
    # to perform the arithmetic operations
    global equation

    # try and except statement is used for handling the errors like zero division error etc.
    result = ""
    if equation != "":
        try:
            # evaluate the expression using the eval function
            result = eval(equation)
        except:
            result = "Error"

            equation = ""

            # update the result in the label
    label_result.configure(text=result)

# to create a label for the result of the calculation
label_result = tk.Label(root, width=40, height=2, font=("Arial", 20),fg="#47f507",bg="black",border=10,borderwidth=10,relief="sunken")
label_result.pack()

# to create Buttons
tk.Button(root,text="C",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:clear()).place(x=10,y=100)
tk.Button(root,text="[]",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("/")).place(x=150,y=100)
tk.Button(root,text="%",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("%")).place(x=290,y=100)
tk.Button(root,text="*",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("*")).place(x=430,y=100)

tk.Button(root,text="7",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("7")).place(x=10,y=200)
tk.Button(root,text="8",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("8")).place(x=150,y=200)
tk.Button(root,text="9",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("9")).place(x=290,y=200)
tk.Button(root,text="-",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("-")).place(x=430,y=200)

tk.Button(root,text="4",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("4")).place(x=10,y=300)
tk.Button(root,text="5",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("5")).place(x=150,y=300)
tk.Button(root,text="6",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("6")).place(x=290,y=300)
tk.Button(root,text="+",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("+")).place(x=430,y=300)

tk.Button(root,text="1",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("1")).place(x=10,y=400)
tk.Button(root,text="2",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("2")).place(x=150,y=400)
tk.Button(root,text="3",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("3")).place(x=290,y=400)
tk.Button(root,text="0",width=11,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show("0")).place(x=10,y=500)

tk.Button(root,text=".",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="#f80",command=lambda:show(".")).place(x=290,y=500)
tk.Button(root,text="=",width=5,height=3,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : calculate()).place(x=430,y=400)

tk.Button(root,text="(",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : show("(")).place(x=570,y=100)
tk.Button(root,text=")",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : show(")")).place(x=570,y=200)

tk.Button(root,text="sin",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : sin()).place(x=570,y=300)
tk.Button(root,text="cos",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : cos()).place(x=570,y=400)
tk.Button(root,text="tan",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : tan()).place(x=570,y=500)

tk.Button(root,text="DEL",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : erase()).place(x=710,y=100)
tk.Button(root,text="√",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : sqrt()).place(x=710,y=200)
tk.Button(root,text="²",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : square()).place(x=710,y=300)
tk.Button(root,text="^",width=5,height=1,font=("Arial",30,"bold"),bd=5,fg="#2A2D36",bg="blue",command=lambda : power()).place(x=710,y=400)

root.mainloop()