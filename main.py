from tkinter import *
from tkinter import ttk
import requests
import 
root=Tk()
frm=ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text="display").grid(column=1,row=0)
ttk.Button(frm,text="exit",command=root.destroy).grid(column=2,row=0)
root.mainloop()