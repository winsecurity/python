import tkinter
from tkinter import *
import tkinter.messagebox

def dialog():
    temp=Tk()
    temp.title("Notification")
    x=e.get()
    var=StringVar()
    lbl=Label(temp,textvariable=var,relief=RAISED)

    var.set("hello")
    lbl.pack()
    temp.mainloop()


def setlabel():
    choice="You selected "+ str(r1.getvar(str(var1)))
    l.config(text=choice)



root=Tk()
b1=Button(root,text="click here",command=dialog)
b1.pack()
root.title("SuperMarket Management System")
root.geometry("1080x720")


e=Entry(root)
e.pack(side=LEFT)
#print(e.get(
var1=StringVar()
r1=Radiobutton(root,text="Vanilla",value=1,variable=var1,command=setlabel)
r1.pack()

var2=StringVar()
r2=Radiobutton(root,text="Strawberry",value=2,variable=var1,command=setlabel)
r2.pack()

l=Label(root)
l.pack()
root.mainloop()