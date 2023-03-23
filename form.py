# from tkinter import*
# import tkinter as tk
# m=tk.Tk()
# tk.Label(m,text="Username : ").grid(row=0)
# tk.Label(m,text="Password : ").grid(row=1)
# tk.Entry(m).grid(row=0,column=1)
# tk.Entry(m,text="enter").grid(row=1,column=1)
# tk.Button(m).grid(row=3)
# tk.Button(m,text="Cancle").grid(row=3,column=1)
# m.mainloop()


import tkinter as tk
def disp():
    l1.config(text="change")
m=tk.Tk()
l1=tk.Label(m,text="hello").grid(row=0)
tk.Button(m,text="login",command=disp).grid(row=1)
m.mainloop()

import tkinter as tk

def disp():
    l1.config(text="change")
m = tk.Tk()
l1 = tk.Label(m, text="hello")
l1.grid(row=0)
tk.Button(m, text="login", command=disp).grid(row=1)
m.mainloop()
