from tkinter import *
from tkinter import messagebox

import time
from data.photo import Photo
from data.bill import Bill
from data.photo import About



class Payment:
    def __init__(self):
        self.root = Tk()
        self.screen_width=(self.root.winfo_screenwidth())
        self.screen_height=(self.root.winfo_screenheight())
        self.root.attributes("-fullscreen",True)
        #self.root.geometry('{0}x{1}+0+0'.format(self.screen_width,self.screen_height))
        self.frame1=Frame(self.root,bd=5,relief=SUNKEN)
        self.frame1.pack(side=RIGHT)
        self.header()
        screen_width=self.root.winfo_screenwidth()-100
        f=Frame(self.root,height=5,width=screen_width,bg="green")
        f.pack()
        self.customer()
        self.main()
        self.page3()
        self.root.mainloop()
        

    def header(self):
        #-----RMS name with datetime-----
        top = Frame(self.root)
        top.pack(side=TOP)
        
        rms_label=Label(top,fg='green', font=( 'aria' ,30, 'bold' ),text="Restaurant Management System")
        rms_label.grid(pady=10)
        clock = Label(self.root, font=('times', 20, 'bold'), fg='dark green')
        clock.pack()
        def curr_time():
            time1 = ''
            time2 = time.strftime('%Y-%m-%d %H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
            clock.after(200, curr_time)
        curr_time()

#--------validation-----------------------------------------

    def validate(self, value_if_allowed, text):
        if text in '0123456789':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return False


#--------------Customer--------------------------------------
    def customer(self):
        def caps1(event):
            v1.set(v1.get().upper())
            
        def caps2(event):
            v2.set(v2.get().upper())

        
        self.cus_frame=Frame(self.root)
        self.cus_frame.pack()
        Label(self.cus_frame,text='----------------------------------------Customer Details---------------------------------------', font=('times', 20, 'bold'),fg='orange').grid(row=0,columnspan=7)

        vcmd = (self.cus_frame.register(self.validate),'%P','%S')
    
        v1 = StringVar()
        Label(self.cus_frame,text="NAME:",font=('times',20,"italic")).grid(row=1,column=0,pady=10)
        self.e1=Entry(self.cus_frame,relief=RIDGE,bd=4,width=30,font=('times',12),textvariable=v1,justify='center')
        self.e1.grid(row=1,column=1,padx=10,pady=10)
        self.e1.bind("<KeyRelease>", caps1)

         
        Label(self.cus_frame,text="PHONE NO:",font=('times',20,"italic")).grid(row=1,column=2,pady=10)
        Entry(self.cus_frame,relief=RIDGE,bd=4,width=30,font=('times',12),justify='center',validate = 'key', validatecommand = vcmd).grid(row=1,column=3,padx=10,pady=10)
        

        v2 = StringVar()
        Label(self.cus_frame,text="ADDRESS:",font=('times',20,"italic")).grid(row=1,column=4,pady=10)
        e2=Entry(self.cus_frame,relief=RIDGE,bd=4,width=50,font=('times',12),textvariable=v2,justify='center')
        e2.grid(row=1,column=5,padx=10,pady=10)
        e2.bind("<KeyRelease>", caps2)

      

        
        
#--------------Paytm----------------------------------    
    def page1(self):
        self.frame1.destroy()
        self.frame1=Frame(self.root,bd=5,relief=GROOVE)
        #self.frame1=Frame(self.root)
        self.frame1.pack(pady=30)
        
        
        self.paytm=Frame(self.frame1,bd=2,relief=SUNKEN,bg='light grey')
        self.paytm.pack(pady=10,padx=100)

        #file=open(r'data/price.txt','r')
        file=open(r'data/price.txt','r')
        price=file.read()
        file.close()
        
        txt="Total Amount = {} Rs\n You Can Pay For Scan Above Paytm Code".format(price)
        Label(self.paytm,text=txt,font=('times',20,'bold italic'),fg='Green',bg='light grey').pack()

        Button(self.frame1,text='BILL >>',font=('times',16),bg='light green',width=25,command=lambda : self.bill(1)).pack(pady=20)

        Photo(self.paytm)

    
#--------------Cardpay----------------------------------   
    def page2(self):
        self.frame1.destroy()
        self.frame1=Frame(self.root,bd=5,relief=GROOVE)
        self.frame1.pack(pady=30)
        
        #self.cardpay=Frame(self.frame1,bd=2,relief=SUNKEN)
        self.cardpay=Frame(self.frame1)
        self.cardpay.pack(pady=10,padx=50)
       
        #file=open(r'data/price.txt','r')
        file=open(r'data/price.txt','r')
        price=file.read()
        file.close()

        Label(self.cardpay,text="Complete Your Payment...",font=('times',15,'bold italic'),).pack(pady=10)
        
        v=StringVar(self.cardpay)
        Radiobutton(self.cardpay,text='SBI BANK',font=('times',16),variable=v,value=1).pack(anchor=W)
        Radiobutton(self.cardpay,text='HDFC BANK',font=('times',16),variable=v,value=2).pack(anchor=W)
        Radiobutton(self.cardpay,text='ICICI BANK',font=('times',16),variable=v,value=3).pack(anchor=W)
        Radiobutton(self.cardpay,text='UNION BANK OF INDIA',font=('times',16),variable=v,value=4).pack(anchor=W)
        Radiobutton(self.cardpay,text='BANK OF INDIA',font=('times',16),variable=v,value=5).pack(anchor=W)
        Radiobutton(self.cardpay,text='AXIS BANK',font=('times',16),variable=v,value=6).pack(anchor=W)
        Radiobutton(self.cardpay,text='PUNJAB NATIONAL BANK',font=('times',16),variable=v,value=7).pack(anchor=W)
        Radiobutton(self.cardpay,text='KOTAK BANK',font=('times',16),variable=v,value=8).pack(anchor=W)
        Radiobutton(self.cardpay,text='CENTRAL BANK OF INDIA',font=('times',16),variable=v,value=9).pack(anchor=W)

        Button(self.frame1,text='Pay Now >>',font=('times',16),bg='light green',width=25,command=self.construction).pack(pady=10)

        
#--------------Cash---------------------------------- 
    def page3(self):
        self.frame1.destroy()
        #self.frame1=Frame(self.root,bd=5,relief=SUNKEN)
        self.frame1=Frame(self.root)
        self.frame1.pack(pady=30)

        self.cash=Frame(self.frame1,bd=5,relief=GROOVE,width=400,height=400)
        self.cash.pack(pady=80)

        cash1=Frame(self.cash)
        cash1.pack(side=TOP)
        
        cash2=Frame(self.cash)
        cash2.pack(side=BOTTOM)
       
        #file=open(r'data/price.txt','r')
        file=open(r'data/price.txt','r')
        price=file.read()
        file.close()
       
        txt="Total Amount = {} Rs".format(price)
        Label(cash1,text=txt,font=('times',40,'bold italic')).pack(pady=40,padx=150)
        Button(cash2,text='BILL >>',font=('times',20,),bg='light green',width=20,command=lambda : self.bill(2)).pack(pady=40)

#-------------main-----------------------------
    def main(self):
        self.buttonframe = Frame(self.root,bd=5,relief=GROOVE)
        self.buttonframe.pack(side="left",padx=50)
        
        b1 = Button(self.buttonframe,width=30,height=2, text="PAYTM",font=('Helvetica',10,'bold italic'),bg='powder blue',relief=RAISED,bd=5,command=self.page1)
        b2 = Button(self.buttonframe,width=30,height=2,text="CARD PAY",font=('Helvetica',10,'bold italic'),bg='powder blue',relief=RAISED,bd=5,command=self.page2)
        b3 = Button(self.buttonframe, width=30,height=2,text="CASH",font=('Helvetica',10,'bold italic'),bg='powder blue',relief=RAISED,bd=5,command=self.page3)

        b1.pack(side="top",pady=30,padx=15)
        b2.pack(pady=15,padx=20)
        b3.pack(side="top",pady=30,padx=15)


#-------------Button commands---------------------------
    def construction(self):
        messagebox.showinfo('Pro Pack','Buy Pro Version Only For >> 199$ << \n--Contact With Admin...')


    def about(self):
        self.f1.destroy()
        self.f2.destroy()

        about_frame=Frame(self.root)
        about_frame.pack()
        l=Label(about_frame,text='ABOUT US',font=('times',25,'bold italic underline'),fg='blue')
        l.pack(pady=20)
        l.bind("<Button-1>",lambda e : self.root.destroy())

        
        icon_frame=Frame(self.root)
        icon_frame.pack(pady=20)

        text_frame=Frame(self.root)
        text_frame.pack(pady=20)

        txt = """ RESTAURANT MANAGEMENT SYSTEM IS CREATED USING HIGH LEVEL POWERFUL SECURED,PROGRAMMING LANGUAGE i.e "PYTHON".

RMS IS DEMO APPLICATION FOR TRIAL USE IN RESTAURANT AND IT'S PRO VERSION ARE AVAILABLE IN $199,

IF YOU WANT TO BUY PRO VERSION PLEASE CONTACT TO THE DEVELOPERS.


THIS PROJECT i.e (RESTAURANT MANAGEMENT SYSTEM) IS DEVELOPED UNDER THE GUIDANCE OF Mrs KAJAL JAISINGHANI FROM BIRLA COLLEGE CS DEPT.

WE ARE THANKFUL TO KAJAL MADAM FOR GIVING US AN OPPORTUNITY TO WORK ON THIS PROJECT. 

CREATED BY ANIKET KARMAKAR AND VINAY KUMAR IN 2018 (FROM BIRLA COLLEGE COMPUTER SCIENCE DEPARTMENT)
"""
        
        Label(text_frame,text=txt ,font=('Helvetica ',12,'italic')).pack()

        Label(self.root,text='© 2018 VINAY KUMAR AND ANIKET KARMAKAR ALL RIGHTS RESERVED').pack(side=BOTTOM,fill=X
                                                                                                )
        
        About(icon_frame)
        

        
##    def back1(self):
##        self.f1.destroy()
##        self.f2.destroy()
##        self.f3.destroy()
##
##        self.customer()
##        self.main()
##        self.page3()
        
        

#-------------------Bill Page---------------
    def bill(self,x):
        file=open(r'data/bill.txt','a+')
        if x==1:
            file.write("\nCustomer Name : {}\n Paid Via : PAYTM".format(self.e1.get()))
            file.write("\n-----------------------------------------\n*** THANK YOU ***\n***PLEASE COME AGAIN***\n-----------------------------------------")
        elif x==2:
            file.write("\nCustomer Name : {}\n Paid Via : CASH".format(self.e1.get()))
            file.write("\n-----------------------------------------\n*** THANK YOU ***\n***PLEASE COME AGAIN***\n-----------------------------------------")
        file.close()

        self.buttonframe.destroy()
        self.frame1.destroy()
        self.cus_frame.destroy()
        
        self.f1=Frame(self.root,bd=5,relief=GROOVE)
        self.f1.pack(pady=20,side=TOP)
        
        obj=Bill(self.f1)
        obj.main()

        self.f2=Frame(self.root)
        self.f2.pack(pady=10)
        
        b4 = Button(self.f2,text="EXIT!",font=('times',15,),bg='light green',width=15,relief=RAISED,bd=5,command=self.root.destroy)
        b4.grid(row=0,column=0,padx=100)

        b6 = Button(self.f2,text="<< ABOUT US >>",font=('times',15,),bg='light green',width=20,relief=RAISED,bd=5,command=self.about)
        b6.grid(row=0,column=1,padx=100)
        
        b5 = Button(self.f2,text="PRINT>>",font=('times',15,),bg='light green',width=15,relief=RAISED,bd=5,command=self.construction)
        b5.grid(row=0,column=2,padx=100)

#Payment()
