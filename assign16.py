#question 1: Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
from tkinter import *
from tkinter import ttk
import tkinter
tk=Tk()
label=Label(tk,text="Hello World!")
label.pack()
bt=tkinter.Button(tk,text='Exit',width=25,command=tk.destroy)
bt.pack()
tk.mainloop()

#question 2: Write a python program to in the same interface as above and create a action when the button is click it will display some text.
from tkinter import *
from tkinter import ttk
import tkinter
tk=Tk()
label=Label(tk,text="Hello World!")
label.pack()
def popuptext():
    popup=Tk()
    label=Label(popup,text="click to exit").pack()
    bb=tkinter.Button(popup,text="QUIT",command=popup.destroy)
    bb.pack()
bt=tkinter.Button(tk,text='Clickme',fg="black",bg="white",width=25,command=popuptext)
bt.pack()
tk.mainloop()

#question 3: Create a frame using tkinter with any label text and two buttons. One to exit and other to change the label to some other text.
from tkinter import *
import  tkinter
tk=Tk()
frame=Frame(tk)
frame.pack()
mylabel=Label(tk,text="have a nice day!")
def changelabel():
 mylabel.config(text="ok bye!")
bt1=tkinter.Button(tk,text='Exit',fg="Black",bg="white",width=25,command=tk.destroy)
bt1.pack()
bt2=tkinter.Button(tk,text='click to change label',bg="white",width=25,command=changelabel)
bt2.pack()
mylabel.pack()
tk.mainloop()

#question 4: Write a python program using tkinter interface to take an input in the GUI program and print it.
from tkinter import *
import  tkinter
tk=Tk()
def show_details():
    print("First name: %s \nLast name: %s" %(e1.get(),e2.get()))
Label(tk,text="First name").grid(row=0)
Label(tk,text="Last name").grid(row=1)
e1=Entry(tk)
e2=Entry(tk)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(tk,text="Quit",command=tk.quit).grid(row=3,column=0,sticky=W,pady=4)
Button(tk,text="show",command=show_details).grid(row=3,column=1,sticky=W,pady=4)
tk.mainloop()