import tkinter as tk
def add():
    a=float(t1.get())
    b=float(t2.get())
    c=a+b
    t3.config(text=c)
def subtract():
    a=float(t1.get())
    b=float(t2.get())
    c=a-b
    t3.config(text=c)
def multi():
    a=float(t1.get())
    b=float(t2.get())
    c=a*b
    t3.config(text=c)
def div():
    a=float(t1.get())
    b=float(t2.get())
    c=a/b
    t3.config(text=c)
    
m=tk.Tk()
l1=tk.Label(m,text="Enter first number :")
l1.grid(row=0)
l2=tk.Label(m,text="enter second number :")
l2.grid(row=1)
l3=tk.Label(m,text="your Answer is :")
l3.grid(row=2)

t1=tk.Entry(m)
t1.grid(row=0,column=1)
t2=tk.Entry(m)
t2.grid(row=1,column=1)
t3=tk.Label(m,text="") #highlight this point 
t3.grid(row=2,column=1)

tk.Button(m,text="ADD",command=add).grid(row=3)
tk.Button(m,text="Substract",command=subtract).grid(row=3,column=1)
tk.Button(m,text="Multiplication",command=multi).grid(row=4)
tk.Button(m,text="Division",command=div).grid(row=4,column=1)

m.mainloop()