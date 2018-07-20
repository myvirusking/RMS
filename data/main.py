from tkinter import*
import time
import random
from tkinter import messagebox
from data.payment import Payment


#create new class RMS
class Main:
    def __init__(self):
        #configuration of root window
        self.root = Tk()
        self.screen_width=(self.root.winfo_screenwidth())
        self.screen_height=(self.root.winfo_screenheight())
        #self.root.geometry('{0}x{1}+0+0'.format(self.screen_width,self.screen_height))

        self.root.attributes("-fullscreen",True)
        self.root.title("Restaurant Management System")
        #root.resizable(width='enable',height='enable')
        self.header()
        self.vcmd = (self.root.register(self.validate),'%P','%S')
        screen_width=self.root.winfo_screenwidth()-100
        f=Frame(self.root,height=5,width=screen_width,bg="green")
        f.pack()
        with open(r"data/price.txt",'w') as f:
            f.write('0')
            
        self.body()
        f=Frame(self.root,height=5,width=screen_width,bg="green")
        f.pack(side=TOP,pady=10)
        
        self.footer()
        #Label(self.root,text='© 2018 VINAY KUMAR AND ANIKET KARMAKAR ALL RIGHTS RESERVED').pack(pady=60)
        

#--------------------BACKEND------------------------

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

    
    def total(self):
  #-------Calculate Order No---------------
        self.orderno=random.randint(11111, 99999)
        self.v1.set(self.orderno)
        
        #-----------------ITEMS IN LEFT SIDE-------
        self.Fries_Meal = 30*(self.v2.get())
        self.Lunch_Meal = 40*(self.v3.get())
        self.Burger_Meal = 25*(self.v4.get())
        self.Pizza_Meal = 40*(self.v5.get())
        self.Cheese_Burger = 15*(self.v6.get())
        self.Drinks = 10*(self.v7.get())

        #--------------=---ITEMS IN MIDDLE SIDE------
        self.Fried_Rice = 70*(self.v12.get())
        self.Hot_Dog = 50*(self.v13.get())
        self.Momos = 30*(self.v14.get())
        self.Dosa = 40*(self.v15.get())
        self.Butter_Chicken = 140*(self.v16.get())
        self.Idli = 30*(self.v17.get())
        
        #-----------------ITEMS IN MIDDLE SIDE------
        self.Palak_Paneer = 45*(self.v18.get())
        self.Chinese = 60*(self.v19.get())
        self.Cheese_Sandwich = 35*(self.v20.get())
        self.Biryani = 180*(self.v21.get())
        self.Rajma_Chaval  = 60*(self.v22.get())
        self.Ice_Cream = 35*(self.v23.get())
       
	
        #-------Calculate Total Cost---------------
        items=[self.Fries_Meal,self.Lunch_Meal,self.Burger_Meal,self.Pizza_Meal,self.Cheese_Burger,self.Drinks,self.Fried_Rice,self.Hot_Dog,self.Momos,self.Dosa,self.Butter_Chicken,self.Idli,self.Palak_Paneer,self.Chinese,self.Cheese_Sandwich,self.Biryani,self.Rajma_Chaval,self.Ice_Cream]
        total=sum(items)
        self.v8.set('{0}₹'.format(total))
        
        #-------Calculate CGST AND SGST---------------
        self.cgst=(total*9)/100
        self.v9.set('{0}₹'.format(self.cgst))
        sgst=(total*9)/100
        self.v10.set('{0}₹'.format(sgst))

        #-------All Total Amt---------------
        all_total=total+self.cgst+sgst
        self.my=all_total
        self.v11.set('{0}₹  => {1}₹'.format(all_total,round(all_total)))

        with open(r"data/price.txt",'w') as f:
            content=str(round(all_total))
            f.write(content)


    def reset(self):
        self.v1.set('0')
        self.v2.set('0')
        self.v3.set('0')
        self.v4.set('0')
        self.v5.set('0')
        self.v6.set('0')
        self.v7.set('0')
        self.v8.set('0')
        self.v9.set('0')
        self.v10.set('0')
        self.v11.set('0')
        self.v12.set('0')
        self.v13.set('0')
        self.v14.set('0')
        self.v15.set('0')
        self.v16.set('0')
        self.v17.set('0')
        self.v18.set('0')
        self.v19.set('0')
        self.v20.set('0')
        self.v21.set('0')
        self.v22.set('0')
        self.v23.set('0')


    def payment(self):
        self.savebill()
        self.root.destroy()
        Payment()
        
#==========Bill save in file==========================
    def savebill(self):
        #----------------Starting-------------------------------------------------------
        
        file = open(r'data/bill.txt','w')
        file.write("-----------------------------------------\n*** WELCOME ***\nBill No : {0}\nBill Dt : {1}".format(self.orderno,time.strftime('%Y-%m-%d %H:%M:%S')))
        file.write("\nRestaurant Nm : {0}".format("AV VAG/NON VEG"))
        content1 = ("\n-----------------------------------------\n|------------------|------|-------|------|\n| Items       |  Qty  |  Rate  | Total Price  |\n|------------------|------|-------|------|\n")
        file.write(content1)
        
        #----------------Left Side Items Bill-------------------------------------------------------
        items_values = [self.Fries_Meal,self.Lunch_Meal,self.Burger_Meal,self.Pizza_Meal,self.Cheese_Burger,self.Drinks]
        items_name = ["Fries Meal    ","Lunch Meal     ","Burger Meal    ","Pizza Meal    ","Cheese Burger  ","Drinks         "]
        rate = [30,40,25,40,15,10]
        
        i=0
        for item in items_values:                   
            if item>0:
                content2 = ("| {0} \t|    {1}   |     {2}   |    {3}  |\n".format(items_name[i],round(item/rate[i]),round(rate[i]),item))
                file.write(content2)
            i+=1
            
        #---------------- Middle Items Bill-------------------------------------------------------
        items_values = [self.Fried_Rice,self.Hot_Dog,self.Momos,self.Dosa,self.Butter_Chicken,self.Idli]
        items_name = ["Fried Rice     ","Hot Dog       ","Momos          ","Dosa           ","Butter Chicken","Idli           "]
        rate = [70,50,30,40,140,30]
        
        i=0
        for item in items_values:                   
            if item>0:
                content2 = ("| {0} \t|    {1}   |     {2}   |    {3}  |\n".format(items_name[i],round(item/rate[i]),round(rate[i]),item))
                file.write(content2)
            i+=1


        #---------------- Right Items Bill-------------------------------------------------------
        items_values = [self.Palak_Paneer,self.Chinese,self.Cheese_Sandwich,self.Biryani,self.Rajma_Chaval,self.Ice_Cream]
        items_name = ["Palak Paneer   ","Chinese        ","Cheese Sandwich","Biryani    ","Rajma Chaval","Ice Cream"]
        rate = [45,60,35,180,60,35]
        
        i=0
        for item in items_values:                   
            if item>0:
                content2 = ("| {0} \t|    {1}   |     {2}   |    {3}  |\n".format(items_name[i],round(item/rate[i]),round(rate[i]),item))
                file.write(content2)
            i+=1

            

        #---------------Ending-------------------------------------
        file.write(" |--------------------------------|--------|\n |        CGST @9% \t\t       |    {0}  |".format(self.cgst))
        file.write("\n |        SGST @9% \t\t       |    {0}  |\n|--------------------------------|-------|".format(self.cgst))
        file.write("\n |       TOTAL AMT >>\t        |   {0}  |\n |--------------------------------|-------|".format(round(self.my)))
        
        
#--------------------FRONTEND------------------------
    def header(self):
        #-----RMS name with datetime-----
        top = Frame(self.root,width = self.screen_width,height=self.screen_height,relief=SUNKEN)
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
        

    def body(self):
        self.bottom = Frame(self.root,width = self.screen_width,height=(self.screen_height)-(self.screen_height//6),relief=SUNKEN)
        self.bottom.pack(pady=25,anchor=W,padx=10)
        #---------Order No--------------
        l1=Label(self.bottom, font=( 'arial' ,16, 'bold' ),text="Order No :",fg="#08CA60",bd=10,anchor='w')
        l1.grid(row=0,column=2)
        self.v1=IntVar()
        self.e1 = Entry(self.bottom,width=20,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg='#92E1B1' ,justify='right',textvariable=self.v1,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e1.grid(row=0,column=3)
#-----------------ITEMS IN LEFT SIDE---------------------------------------------------------
        #---------Fries Meal--------------
        l2=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Fries  (₹30) :",fg="#08CA60",bd=10,anchor='w')
        l2.grid(row=2,column=0,sticky=E)
        self.v2=IntVar()
        self.e2 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v2,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e2.grid(row=2,column=1)
        #---------Lunch Meal--------------
        l3=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Lunch Meal (₹40) :",fg="#08CA60",bd=10,anchor='w')
        l3.grid(row=3,column=0,sticky=E)
        self.v3=IntVar()
        self.e3 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v3,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e3.grid(row=3,column=1)
        #---------Burger Meal--------------
        l4=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Burger (₹25) :",fg="#08CA60",bd=10,anchor='w')
        l4.grid(row=4,column=0,sticky=E)
        self.v4=IntVar()
        self.e4 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v4,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e4.grid(row=4,column=1)
        #---------Pizza Meal--------------
        l5=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Pizza (₹40) :",fg="#08CA60",bd=10,anchor='w')
        l5.grid(row=5,column=0,sticky=E)
        self.v5=IntVar()
        self.e5 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v5,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e5.grid(row=5,column=1)
        #---------Cheese Burger--------------
        l6=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Cheese Burger (₹15) :",fg="#08CA60",bd=10,anchor='w')
        l6.grid(row=6,column=0,sticky=E)
        self.v6=IntVar()
        self.e6 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v6,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e6.grid(row=6,column=1)
        #---------Drinks--------------
        l7=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Drinks (₹10) :",fg="#08CA60",bd=10,anchor='w')
        l7.grid(row=7,column=0,sticky=E)
        self.v7=IntVar()
        self.e7 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v7,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e7.grid(row=7,column=1)
        #-----------Calculate---------
        b1=Button(self.bottom,font=( 'arial' ,16, 'bold' ),text="CALCULATE",bg="#92E1B1",bd=10,width=15,command=self.total)
        b1.grid(row=8,column=3,pady=10)
        #-----------Reset---------
        b2=Button(self.bottom, font=( 'arial' ,16, 'bold' ),text="RESET",bg="#92E1B1",bd=10,width=15,command=self.reset)
        b2.grid(row=8,column=2)



#-----------------ITEMS IN MIDDLE SIDE---------------------------------------------------------
        #---------Fried Rice--------------
        l12=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Fried Rice (₹70) :",fg="#08CA60",bd=10,anchor='w')
        l12.grid(row=2,column=2)
        self.v12=IntVar()
        self.e12 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v12,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e12.grid(row=2,column=3)
        #---------Hot Dog --------------
        l13=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Hot Dog (₹50) :",fg="#08CA60",bd=10,anchor='w')
        l13.grid(row=3,column=2)
        self.v13=IntVar()
        self.e13 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v13,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e13.grid(row=3,column=3)
        #==========Momos==================================
        l14=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Momos (₹30) :",fg="#08CA60",bd=10,anchor='w')
        l14.grid(row=4,column=2)
        self.v14=IntVar()
        self.e14 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v14,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e14.grid(row=4,column=3)
        #============Dosa=====================================================
        l15=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Dosa (₹40) :",fg="#08CA60",bd=10,anchor='w')
        l15.grid(row=5,column=2)
        self.v15=IntVar()
        self.e15 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v15,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e15.grid(row=5,column=3)
        #==========Butter Chicken ======================================================
        l16=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Butter Chicken (₹140) :",fg="#08CA60",bd=10,anchor='w')
        l16.grid(row=6,column=2)
        self.v16=IntVar()
        self.e16 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v16,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e16.grid(row=6,column=3)
        #=============Idli=========================================================
        l17=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Idli (₹30) :",fg="#08CA60",bd=10,anchor='w')
        l17.grid(row=7,column=2)
        self.v17=IntVar()
        self.e17 = Entry(self.bottom,width=18,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v17,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e17.grid(row=7,column=3)

#-----------------ITEMS IN RIGHT SIDE---------------------------------------------------------
        #---------Palak Paneer--------------
        l18=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Palak Paneer(₹45) :",fg="#08CA60",bd=10,anchor='w')
        l18.grid(row=2,column=4)
        self.v18=IntVar()
        self.e18 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v18,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e18.grid(row=2,column=5)
        #---------Chinese--------------
        l19=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Chinese (₹60) :",fg="#08CA60",bd=10,anchor='w')
        l19.grid(row=3,column=4)
        self.v19=IntVar()
        self.e19 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v19,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e19.grid(row=3,column=5)
        #---------Cheese Sandwich--------------
        l20=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Cheese Sandwich (₹35) :",fg="#08CA60",bd=10,anchor='w')
        l20.grid(row=4,column=4)
        self.v20=IntVar()
        self.e20 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v20,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e20.grid(row=4,column=5)
        #---------Biryani-------------
        l21=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Biryani (₹180) :",fg="#08CA60",bd=10,anchor='w')
        l21.grid(row=5,column=4)
        self.v21=IntVar()
        self.e21 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v21,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e21.grid(row=5,column=5)
        #---------Rajma chaval--------------
        l22=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Rajma chaval (₹60) :",fg="#08CA60",bd=10,anchor='w')
        l22.grid(row=6,column=4)
        self.v22=IntVar()
        self.e22 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v22,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e22.grid(row=6,column=5)
        #---------Ice Cream--------------
        l23=Label(self.bottom, font=( 'arial' ,14, 'bold' ),text="Ice Cream (₹35) :",fg="#08CA60",bd=10,anchor='w')
        l23.grid(row=7,column=4)
        self.v23=IntVar()
        self.e23 = Entry(self.bottom,width=15,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v23,relief=RIDGE,selectbackground='red',validate = 'key', validatecommand = self.vcmd)
        self.e23.grid(row=7,column=5)

        
#-----------------------------------------------------------------------------------------------------------------------------------------------------------         

    def footer(self):
        self.bottom2= Frame(self.root,width = self.screen_width,height=self.screen_height-((self.screen_height)-(self.screen_height//6)),relief=SUNKEN)
        self.bottom2.pack(pady=15)
        #-----------Total Cost-------
        l8=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="TOTAL COST :",fg="#08CA60",bd=10,anchor='w')
        l8.grid(row=0,column=0,sticky=E)
        self.v8=IntVar()
        self.e8 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v8,relief=RIDGE)
        self.e8.grid(row=0,column=1)
        #-----------CGST-------------
        l9=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="CGST (9%) :",fg="#08CA60",bd=10,anchor='w')
        l9.grid(row=0,column=2,sticky=E)
        self.v9=IntVar()

        self.e9 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v9,relief=RIDGE)
        self.e9.grid(row=0,column=3)

        #-----------SGST-------------
        l10=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="SGST (9%) :",fg="#08CA60",bd=10,anchor='w')
        l10.grid(row=0,column=4,sticky=E)
        self.v10=IntVar()
        self.e10 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',textvariable=self.v10,relief=RIDGE)
        self.e10.grid(row=0,column=5)
        #-----------All Total Amt-----
        l11=Label(self.bottom2, font=( 'arial' ,16, 'bold' ),text="ALL TOTAL AMT :",fg="#08CA60",bd=10,anchor='w')
        l11.grid(row=1,columnspan=4)
        self.v11=IntVar()
        self.e11 = Entry(self.bottom2,font=('ariel' ,16,'bold'),bd=6,insertwidth=4,bg="#92E1B1" ,justify='right',width=30,textvariable=self.v11,relief=RIDGE)
        self.e11.grid(row=1,columnspan=5,sticky=E,pady=15)
        #-----------Payment-------------
        self.b3=Button(self.bottom2, font=( 'arial' ,16, 'bold' ),text="PAYMENT",bg="#08CA60",bd=10,command=self.payment)
        self.b3.grid(row=9,column=6,sticky=E)
        #-----------Exit-------------
        self.b3=Button(self.bottom2, font=( 'arial' ,16, 'bold' ),text="Exit",bg="#08CA60",bd=10,command=self.root.destroy,width=10)
        self.b3.grid(row=9,column=0,sticky=SE)


#call the class RMS
##app=RMS(root)
##root.mainloop()
#Main()
