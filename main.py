from tkinter import*
global enrty_1, entry_2, lscreen, mscreen, info_1, info_2, info_3, info_4
import time
from tkinter import messagebox
from tkinter import simpledialog

def checkpassword():
    global entry_1, entry_2, lscreen, mscreen
    username=entry_1.get()
    password=entry_2.get()
    if username=="slow boat":
        if password=="to china":
            messagebox.showinfo("Logged in")
            time.sleep(2)
            lscreen.destroy
            mscreen()  
        else:
            messagebox.showinfo("try again")
    else:
        messagebox.showinfo("try again")





def loginscreen():
    global entry_1, entry_2, lscreen
    lscreen = Tk()
    lscreen.title("login")
    lscreen.geometry("500x700")
    label_1 = Label(lscreen, text="enter name")
    label_2 = Label(lscreen, text="enter password")
    entry_1 = Entry(lscreen)
    entry_2 = Entry(lscreen)
    button_login = Button(lscreen, text="Login", command=checkpassword)
    label_1.grid(row=0)
    label_2.grid(row=1)
    entry_1.grid(row=0, column=1)
    entry_2.grid(row=1, column=1)
    button_login.grid(row=2, column=1)
    c = Checkbutton(lscreen, text="keep me logged in")
    c.grid(columnspan=2)
    lscreen.mainloop()

    
def mscreen():
    global mscreen, entry_1, entry_2
    mscreen = Tk()
    mscreen.title("main menu")
    mscreen.geometry("500x700")

    label_1 = Label(mscreen, text="new customer")
    button_login = Button(mscreen, text="Login", command=checkpassword)
    label_1.grid(row=0)
    button_login.grid(row=0, column=1)

    label_2 = Label(mscreen, text="exsisting customer")
    button_login_2 = Button(mscreen, text="Login", command=checkpassword)
    label_2.grid(row=1)
    button_login_2.grid(row=1, column=1)

    label_3 = Label(mscreen, text="menu")
    button_login_3 = Button(mscreen, text="Login", command=checkpassword)
    label_3.grid(row=2)
    button_login_3.grid(row=2, column=1)


# def button():
#     global button,button_1, button_2, button_3
#     button = TK()
#     button.title("new customer")
#     button.geometry("300x400")
#     button.entry_1()








loginscreen()
    
