from tkinter import *

class Photo:
    def __init__(self,root):
        img = PhotoImage(file=r"data/paytmcode.png")
        img = img.subsample(4)
        Label(root,image=img).pack(padx=50,pady=20)
        root.mainloop()


class About:
    def __init__(self,root):
        img = PhotoImage(file=r"data/about.png")
        Label(root,image=img).pack()
        root.mainloop()
        
        
