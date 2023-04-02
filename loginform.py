import tkinter as tk
def process():
    u = t1.get()
    p = t2.get()
    if u == "prasad" and p == "bhavsar":
        l3.config(text="Welcome")
    else:
        l3.config(text="Invalid logins")
    
m=tk.Tk()
l1=tk.Label(m,text="Username :")
l1.grid(row=0)
l2=tk.Label(m,text="Password :")
l2.grid(row=1)

t1=tk.Entry(m)
t1.grid(row=0,column=1)
t2=tk.Entry(m)
t2.grid(row=1,column=1)

b1=tk.Button(m,text="login",command=process)
b1.grid(row=2)
b2=tk.Button(m,text="cancle")
b2.grid(row=2,column=1)

l3=tk.Label(m,text="")
l3.grid(row=3)
m.mainloop()