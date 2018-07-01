#ASSIGNMENT ON GUI 2:
#question 1: Create a dictionary with name and mobile number. Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *
tk=Tk()
tk.title("GUI")
data={'simran':'7895875778','shreya':'8126642305','sonali':'6758945325','himadri':'9126675432'}
Label(tk,text="Enter your name").pack()
e1=Entry(tk)
e1.pack()
scrollbar=Scrollbar(tk)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(tk,yscrollcommand=scrollbar.set)
for key in data.keys():
    mylist.insert(END,key)
mylist.pack(side=LEFT)
scrollbar.config(command=mylist.yview)
Button(tk,text="Exit",fg="red",bg="white",command=tk.destroy).pack()
tk.mainloop()

#question 2: In the same tkinter file as above,create a function to insert items into the dictionary.
import tkinter
from tkinter import *
tk=tkinter.Tk()
tk.title("details")
label1=Label(tk,text="Enter your name").grid(row=0)
label2=Label(tk,text="Enter your phone number").grid(row=1)
x=StringVar()
y=IntVar()
e1=Entry(tk,textvariable=x)
e2=Entry(tk,textvariable=y)
a={'simran':7895875778,'shreya':8126642305,'sonali':6758945325,'himadri':9126675432}
def insert_items(x,y):
    a.update({x:int(y)})
    print(a)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(tk,text="Execute",fg="green",bg="white",command=lambda :insert_items(x.get(),y.get())).grid(row=3,column=0,sticky=W,pady=4)
Button(tk,text="Exit",fg="red",bg="white",command=tk.destroy).grid(row=3,column=1,sticky=W,pady=4)
tk.mainloop()