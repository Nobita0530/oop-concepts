from tkinter import *

master = Tk() 

var1 = IntVar() 

c1=Checkbutton(master, text='male', variable=var1)
c1.grid(row=0, sticky=W) 

var2 = IntVar() 

c2=Checkbutton(master, text='female', variable=var2)
c2.grid(row=1, sticky=W) 
mainloop()