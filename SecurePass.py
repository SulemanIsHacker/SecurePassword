from tkinter import *
from tkinter.messagebox import showinfo as tsmg
SECURE = (('s', '$'), ('and', '&'),
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))
def SecurePassowrd():
    password = passentry.get()
    for a,b in SECURE:
        password = password.replace(a,b)
    show = tsmg("SecurePassword",f"You Secure Password is {password}")
    print(f"Your Secure Password is {password}")
    return show


root = Tk()
root.geometry("650x450")
root.title("Suleman Password Secure App")

Password = Label(root,text="Password:",font='lucida 16 bold')
Password.grid(row=1,column=1)

passvalue = StringVar()
passentry = Entry(root,textvariable=passvalue,font="lucida 10 bold")
passentry.grid(row=1,column=2)

Button(text="Get Secure Password",command=SecurePassowrd).grid(row=3, column=2)
getValue = StringVar()
passentry = Entry(root,textvariable=passvalue,font="lucida 10 bold")
passentry.grid(row=1,column=2)
root.mainloop()