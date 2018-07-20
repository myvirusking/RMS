from tkinter import *

class Bill:
    def __init__(self,frame):
        self.frame=frame

        
    def main(self):
        file=open(r'data/bill.txt')
        content=file.read()
        Label(self.frame,text=content,font=('times',8,'bold')).pack(padx=30)
