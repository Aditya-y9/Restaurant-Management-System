import tkinter as tk
from tkinter import *
import math
from functions import click



def getValues(event):
    screen.configure(text=click(event))
  


root=Tk()
root.title("Aditi's scientific calculator")
root.geometry("480x490")
root.resizable(0,0)
screen = Label(root, font="Veranda 20 bold", fg="#F896DF", bg="#690751", justify=RIGHT,bd=5,relief=SUNKEN)
screen.pack(fill=X)
row1 = Frame(root)
buttonList = ['sinθ', 'cosθ', 'tanθ', 'sinhθ', 'coshθ', 'rad', 'π', 'e', 'AC', 'DEL', 'x^2', '1/x', '|x|', 'exp', '%', '√x', '(', ')', 'x!', '/', 'x^y', '7', '8', '9', '*', '10^x', '4', '5', '6', '-', 'log10', '1', '2', '3', '+', 'ln', '+/-', '0', '.', '=']
text_input = StringVar()
rowvalue = 1
colvalue = 0
text = ''
answer = ''

ifrow1 = Frame(root)  # Create the ifrow1 variable as an instance of the Frame class

buttonrow1 = Frame(root)  # Create the buttonrow1 variable as an instance of the Frame class

for i in buttonList:
  if i in "1234567890DEL":
    button = Button(row1, text=i, fg="#BE1E78", bg="#FAA9CF", font="Veranda 20 bold", relief=SUNKEN, bd=1, padx=4, pady=2, command=lambda i=i:getValues(i))
    button.grid(row=rowvalue, column=colvalue, sticky='nsew')
  else:
    button = Button(row1, text=i, fg="#F896DF", bg="#BE1E78", font="Veranda 20 bold", relief=SUNKEN, bd=1, padx=4, pady=2, command = lambda i=i:getValues(i))
    button.grid(row=rowvalue, column=colvalue, sticky='nsew')

  colvalue = colvalue + 1
  if colvalue > 4:
    rowvalue = rowvalue + 1
    colvalue = 0
row1.pack()

root.mainloop()