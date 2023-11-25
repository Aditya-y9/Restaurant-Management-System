import tkinter as tk
from fontTools.cffLib import width


# to create a window
root = tk.Tk()

# to set the title of the window
root.title("PD LAB")

# to set the size of the window (fixed)
root.geometry("570x600+100+200")

# resizable h?
root.resizable(False, False)

# to set the background color of the window
root.configure(bg="#2A2D36")


equation = ""

def show(value):
    global equation
    # to update the equation in the string
    equation += value

    # to update the equation in the label
    label_result.configure(text=equation)

def clear():
    global equation
    # reset the equation string
    equation = ""

    # empty the label
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
label_result = tk.Label(root, width=40, height=2, font=("Arial", 20))
label_result.pack()

# to create Buttons
tk.Button(root,text="C",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:clear()).place(x=10,y=100)
tk.Button(root,text="[]",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("/")).place(x=150,y=100)
tk.Button(root,text="%",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("%")).place(x=290,y=100)
tk.Button(root,text="*",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("*")).place(x=430,y=100)

tk.Button(root,text="7",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("7")).place(x=10,y=200)
tk.Button(root,text="8",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("8")).place(x=150,y=200)
tk.Button(root,text="9",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("9")).place(x=290,y=200)
tk.Button(root,text="-",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("-")).place(x=430,y=200)

tk.Button(root,text="4",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("4")).place(x=10,y=300)
tk.Button(root,text="5",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("5")).place(x=150,y=300)
tk.Button(root,text="6",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("6")).place(x=290,y=300)
tk.Button(root,text="+",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("+")).place(x=430,y=300)

tk.Button(root,text="1",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("1")).place(x=10,y=400)
tk.Button(root,text="2",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("2")).place(x=150,y=400)
tk.Button(root,text="3",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("3")).place(x=290,y=400)
tk.Button(root,text="0",width=11,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show("0")).place(x=10,y=500)

tk.Button(root,text=".",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="#f80",command=lambda:show(".")).place(x=290,y=500)
tk.Button(root,text="=",width=5,height=3,font=("Arial",30,"bold"),bd=1,fg="#2A2D36",bg="blue",command=lambda : calculate()).place(x=430,y=400)

root.mainloop()