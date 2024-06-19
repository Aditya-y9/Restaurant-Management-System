import tkinter as tk
import Calculator.Calc as Calc
from tkinter import ttk
from tkinter import messagebox as mb
import webbrowser
from playsound import playsound


root = tk.Tk()


root.geometry("1025x600+150+10")

root.title("Aditya Yedurkar's Calculator")

root.resizable(False,False)



root.configure(bg="#2B2D60",border=20,bd=20,relief="sunken")

def callback(url):
    webbrowser.open_new_tab(url)

def clear():
    result_label.configure(text=Calc.clear())

def show(value):
    print("this value" + str(value))
    val = value
    if val == '13':
        print("Playing music")
        playsound('tera.wav')
    result_label.configure(text=Calc.show(value))

def calculate():
    val = Calc.calculate()
    print("this val" + str(val))
    if val == 13:
        print("Playing music")
        playsound('tera.wav')
    result_label.configure(text=val)

def sin():
    result_label.configure(text=Calc.sin())

def cos():
    result_label.configure(text=Calc.cos())

def tan():
    result_label.configure(text=Calc.tan())

def sqrt():
    result_label.configure(text=Calc.sqrt())

def modulo():
    result_label.configure(text=Calc.mod())


def mod():
    result_label.configure(text=Calc.mod())

def exp():
    result_label.configure(text=Calc.exp())

def power():
    result_label.configure(text=Calc.power())

def inverse():
    result_label.configure(text=Calc.inverse())

def log10():
    result_label.configure(text=Calc.log10())

def loge():
    result_label.configure(text=Calc.log())

def fact():
    result_label.configure(text=Calc.fact())

def power10():
    result_label.configure(text=Calc.power10())

try:

    result_label = tk.Label(root,fg="green",bg="black",width=120,height=2,border=8,bd=8,relief="sunken",font=("Ariel",25,"bold"))
    result_label.pack()


            
    tk.Button(fg="black",bg="yellow",width=5,height=2,border=4,bd=4,command=lambda:clear(),text="C",font=("Ariel",20,"bold")).place(x=10,y=120)

    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("1"),text="1",font=("Ariel",20,"bold")).place(x=120,y=120)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("2"),text="2",font=("Ariel",20,"bold")).place(x=230,y=120)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("3"),text="3",font=("Ariel",20,"bold")).place(x=10,y=220)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("4"),text="4",font=("Ariel",20,"bold")).place(x=120,y=220)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("5"),text="5",font=("Ariel",20,"bold")).place(x=230,y=220)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("6"),text="6",font=("Ariel",20,"bold")).place(x=10,y=320)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("7"),text="7",font=("Ariel",20,"bold")).place(x=120,y=320)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("8"),text="8",font=("Ariel",20,"bold")).place(x=230,y=320)
    tk.Button(fg="black",bg="#94eaf2",width=5,height=2,border=4,bd=4,command=lambda:show("."),text=".",font=("Ariel",20,"bold")).place(x=340,y=320)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("9"),text="9",font=("Ariel",20,"bold")).place(x=10,y=420)
    tk.Button(fg="black",bg="#dae8f7",width=5,height=2,border=4,bd=4,command=lambda:show("0"),text="0",font=("Ariel",20,"bold")).place(x=120,y=420)



    tk.Button(fg="black",bg="#12fac8",width=18,height=2,border=4,bd=4,command=lambda:calculate(),text="=",font=("Ariel",20,"bold")).place(x=230,y=420)



    tk.Button(fg="black",bg="#94eaf2",width=5,height=2,border=4,bd=4,command=lambda:show("+"),text="+",font=("Ariel",20,"bold")).place(x=340,y=120)
    tk.Button(fg="black",bg="#94eaf2",width=5,height=2,border=4,bd=4,command=lambda:show("-"),text="-",font=("Ariel",20,"bold")).place(x=450,y=120)
    tk.Button(fg="black",bg="#94eaf2",width=5,height=2,border=4,bd=4,command=lambda:show("/"),text="/",font=("Ariel",20,"bold")).place(x=560,y=120)
    tk.Button(fg="black",bg="#94eaf2",width=5,height=2,border=4,bd=4,command=lambda:show("*"),text="*",font=("Ariel",20,"bold")).place(x=670,y=120)

    sin_button=tk.Button(fg="black",bg="#facd05",width=5,height=2,border=4,bd=4,command=lambda:sin(),text="sin",font=("Ariel",20,"bold"))
    sin_button.place(x=340,y=220)
    cos_button = tk.Button(fg="black",bg="#facd05",width=5,height=2,border=4,bd=4,command=lambda:cos(),text="cos",font=("Ariel",20,"bold"))
    cos_button.place(x=450,y=220)
    tan_button = tk.Button(fg="black",bg="#facd05",width=5,height=2,border=4,bd=4,command=lambda:tan(),text="tan",font=("Ariel",20,"bold"))
    tan_button.place(x=560,y=220)



    
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:show("*"),text="*",font=("Ariel",20,"bold")).place(x=670,y=220)

    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:sqrt(),text="√",font=("Ariel",20,"bold")).place(x=450,y=320)

    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:show("("),text="(",font=("Ariel",20,"bold")).place(x=560,y=420)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:show(")"),text=")",font=("Ariel",20,"bold")).place(x=670,y=420)

    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:modulo(),text="mod",font=("Ariel",20,"bold")).place(x=560,y=320)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:mod(),text="|x|",font=("Ariel",20,"bold")).place(x=670,y=320)


    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:exp(),text="exp",font=("Ariel",20,"bold")).place(x=780,y=120)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:power(),text="^",font=("Ariel",20,"bold")).place(x=890,y=120)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:inverse(),text="1/x",font=("Ariel",20,"bold")).place(x=780,y=220)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:log10(),text="log10",font=("Ariel",20,"bold")).place(x=890,y=220)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:loge(),text="ln",font=("Ariel",20,"bold")).place(x=780,y=320)
    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:fact(),text="!",font=("Ariel",20,"bold")).place(x=890,y=320)

    
    tk.Button(fg="black",bg="#e83f71",width=10,height=1,border=4,bd=4,text="Made by AY",font=("Ariel",10,"bold"),command=lambda:callback("https://github.com/Aditya-y9")).place(x=780,y=440)

    tk.Button(fg="black",bg="#f80",width=5,height=2,border=4,bd=4,command=lambda:power10(),text="10^",font=("Ariel",20,"bold")).place(x=890,y=420)
except:
    equation="error"
    result_label.configure(text=equation)
    print(Exception.with_traceback())



root.mainloop()