import tkinter as tk
from tkinter import ttk
import requests

class Downloaader:
    def __init__(self):
        self.window=tk.Tk()
        self.window.title("GUI Downloader")
        self.url_label=tk.Label(text="Enter URL: ")
def downloadFile():
    pass

root=Tk()
frm=ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm,text="display").grid(column=1,row=0)
ttk.Button(frm,text="exit",command=root.destroy).grid(column=2,row=0)
root.mainloop()