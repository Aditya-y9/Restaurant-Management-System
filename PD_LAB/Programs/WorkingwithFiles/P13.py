import tkinter
window = tkinter.Tk()

data = tkinter.StringVar()
data.set("Aditya Yedurkar")

label = tkinter.Label(window, textvariable=data)

label.pack()

window.mainloop()
