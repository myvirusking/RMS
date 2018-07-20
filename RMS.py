from tkinter import *
import time
from tkinter import messagebox
from data.main import Main


#-------------root configuration------------
root = Tk()
screen_width=(root.winfo_screenwidth())-10
screen_height=(root.winfo_screenheight())-10
root.geometry('{0}x{1}+{2}+{3}'.format(screen_width//2,screen_height//2,screen_width//4,screen_height//4))
#root.attributes("-fullscreen",True)
root.title('RMS')
root.iconbitmap(r"data/icon.ico")
root.resizable(width=False, height=False)



class auth:
    def __init__(self,root):
        self.root=root
        screen_width=(root.winfo_screenwidth())-10
        screen_height=(root.winfo_screenheight())-10
#-----------------bg handler with canvas-----------------------
        self.canvas = Canvas(self.root,width=screen_width//2, height=screen_height//2, bg='black')
        self.canvas.pack(fill=BOTH,expand=True)
        img = PhotoImage(file=r'data/bg.png')
        self.canvas.create_image(0, 0, image=img, anchor=NW)
        self.failure_max = 3
        self.passwords = [('Aniket_Vinay_RMS', 'DEADPOOL'),('av','av'),('AV','av')]
        self.header()
        screen_width=self.canvas.winfo_screenwidth()-100
        self.main()
        Label(self.root,text='© 2018 VINAY KUMAR AND ANIKET KARMAKAR ALL RIGHTS RESERVED',bg='light blue').pack(side=BOTTOM,fill=BOTH)
        self.canvas.mainloop()

    def header(self):
        #-----RMS name with datetime-----
        top = Frame(self.canvas)
        top.pack(side=TOP,pady=20)

        
        rms_label=Label(top,bg='#1E2BAA',font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg='powder blue')
        rms_label.grid()

    def check_password(self,failures=[]):
        #print(self.username.get(), self.password.get())
        if (self.username.get(), self.password.get()) in self.passwords:
            self.root.destroy()
            Main()
            return 1
        failures.append(1)
        if sum(failures)<3:
            result=sum(failures)
            messagebox.showinfo("Unauthorized Access",'Try again. Attempt %s/%s' % (result, self.failure_max))
            result=result+1
            self.username.delete(0, END)
            self.username.insert(0, 'Enter Username')
            self.password.delete(0, END)
            self.password.insert(0, 'Password')
        else:
            messagebox.showinfo("Access Denied","Unauthorized Login Attempt")
            self.canvas.destroy()

    def clear_letter(self,event):
        # will clear out any entry boxes defined below when the user shifts
        if self.username == self.username.focus_get() and self.username.get() == 'Enter Username':
            self.username.delete(0, END)
        elif self.password == self.password.focus_get() and self.password.get() == 'Password':
            self.password.delete(0, END)
 
    def default_letter(self,event):
        # will repopulate the default text previously inside the entry boxes defined below if
        if self.username != self.username.focus_get() and self.username.get() == '':
            self.username.insert(0, 'Enter Username')
        elif self.password != self.password .focus_get() and self.password.get() == '':
            self.password.insert(0, 'Password')
    
    
    def main(self):
        self.right = Frame(self.canvas,relief=RAISED,bg='light blue',bd=3)
        self.right.pack(padx=30,ipadx=20,ipady=10,pady=40)
        #=============USERNAME AND PASSWORD===================================
        Label(self.right, text="ADMIN LOGIN",bg='light blue',font=('times',18,'underline'),fg='green').pack(pady=3)
        self.username=Entry(self.right,width=50,bg='powder blue')
        self.username.insert(0, 'Enter Username')
        self.username.bind("<FocusIn>", self.clear_letter)
        self.username.bind('<FocusOut>', self.default_letter)
        self.username.pack(pady=20)
        
        #=============LOGIN BUTTON=============================================
        #Label(self.right, text="Enter Password:").pack(pady=3)
        self.password=Entry(self.right,show="*",width=50,bg='powder blue')
        self.password.insert(0, 'Password')
        self.password.bind("<FocusIn>", self.clear_letter)
        self.password.bind('<FocusOut>', self.default_letter)
        self.password.pack(pady=10)
        
        #=============LOGIN BUTTON=============================================
        self.btn = Button(self.right,text='Log In',bg='lightgreen',fg='Green',width=15,command=self.check_password)
        self.btn.pack(pady=10)

obj=auth(root)
