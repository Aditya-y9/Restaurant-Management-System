from tkinter import *
from tkinter import ttk

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1100x600+100+15")
        self.win.title("Restaurant Management System")
        # self.bg = PhotoImage(file="images/bg.png")

#<-------------------Title------------------->
        self.title_label = Label(self.win,width=1,height=1,bd=0,text="Restaurant Management System",font=("times new roman",25,"bold"),compound=CENTER,fg="white",bg="black")
        self.title_label.pack(side=TOP,fill=X)
#<-------------------Login Frame------------------->


if __name__ == "__main__":
    main()