from tkinter import*
import tkinter as tk
m=tk.Tk()
tk.Label(m,text="enter your name    :").grid(row=0)
tk.Label(m,text="enter your surname :").grid(row=1)
tk.Entry(m).grid(row=0,column=1)
tk.Entry(m).grid(row=1,column=1)
m.mainloop()