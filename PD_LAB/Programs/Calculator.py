import tkinter as tk
from fontTools.cffLib import width


# to create a window
root = tk.Tk()

# to set the title of the window
root.title("PD LAB")

# to set the size of the window (fixed)
root.geometry("570x600+100+200")

# resizable h?
root.resizable(True, True)

# to set the background color of the window
root.configure(bg="black")

# to create a label for the result of the calculation
label_result = tk.Label(root, width=40, height=2, font=("Arial", 20))
label_result.pack()

# to create Reset button
tk.Button(root,text="C",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="black",bg="#f80").place(x=10,y=100)
tk.Button(root,text="/",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="black",bg="#f80").place(x=150,y=100)
tk.Button(root,text="%",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="black",bg="#f80").place(x=290,y=100)
tk.Button(root,text="*",width=5,height=1,font=("Arial",30,"bold"),bd=1,fg="black",bg="#f80").place(x=430,y=100)







root.mainloop()