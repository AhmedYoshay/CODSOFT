import tkinter
from tkinter import *

root=Tk()
root.title("Yoshay's TO-DO-LIST")
root.geometry("400x650+450+100")
root.resizable(False,False)

toDO_list= []

def Add_task():
    task = To_do_entry.get()
    To_do_entry.delete(0,END) 

    if task:
        with open('task.txt','a') as tf:
            tf.write(f"\n{task}")
        toDO_list.append(task)
        lb.insert(END,task)  

def Delete_task():
    global toDO_list
    task= str(lb.get(ANCHOR))
    if task in toDO_list:
        toDO_list.remove(task)
        with open("task.txt",'w') as tf:
            for task in toDO_list:
                tf.write(task+"\n")
        lb.delete(ANCHOR)

def OpenFile():

    try:
        global toDO_list
        with open("task.txt","r") as tf:
            tasks= tf.readlines()
        for task in tasks:
            if task !='\n':
                toDO_list.append(task)
                lb.insert(END,task)    
    except:
        f=open('task.txt','w')
        f.close()
 
#Logos for App

icon = PhotoImage(file="Bar.png")
Label(root,image=icon).pack()

Menu_icon=PhotoImage(file="Menu.png")
Label(root,image=Menu_icon,bg="#32405b").place(x=30,y=25)

title=Label(root,text="MY TASKS",font="Nexa 20 bold",fg="White",bg="#32405b")
title.place(x=155,y=20)


#Working
layout= Frame(root,width=450,height=50,bg="white")
layout.place(x=0,y=180)

To_do=StringVar()
To_do_entry=Entry(layout,width=18,font="Nexa 20",bd=0)
To_do_entry.place(x=15,y=7)

button=Button(layout,text="ADD",font="Nexa 20 bold",width=6,bg="#800080",fg="#fff",bd=0,command=Add_task)
button.place (x=300,y=0)

#Box
b1=Frame(root,width=700,height=280,bg="#32405b")
b1.pack(pady=(160,0))

lb=Listbox(b1,font=('arial',12),width=41,height=16,bg="#87CEEB",fg="black",cursor="hand2",selectbackground="#5a9")
lb.pack(side=LEFT,fill=BOTH,padx=2,pady=2)
sc=Scrollbar(b1)
sc.pack(side=RIGHT, fill= BOTH,padx=2,pady=3)


lb.config(yscrollcommand=sc.set)
sc.config(command=lb.yview)

OpenFile()

delete_icon= PhotoImage(file="Delete.png")
delete= Button(root,image=delete_icon,bg="#800080",fg="#fff",command=Delete_task)
delete.pack(side=BOTTOM,pady=13,padx=13)


root.mainloop()