import time
import random 
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
    root = Tk() 
    app1  = windows1(root)
    app2  = windows1(root)
    app3  = windows1(root)     
    app4  = windows1(root)
    app5  = windows1(root)
    root.mainloop()


class windows1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy Management System ")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitle = Label(self.frame,text = "Pharmacy Management System" ,
        font = ("arial",40,"bold"), bd =10 ,relief="sunken")

        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        
        self.Loginframe1= Frame(self.frame,width = 1000, height=300, bd=10, relief="groove")
        self.Loginframe1.grid(row=0,column=0) 

        self.Loginframe2= Frame(self.frame,width = 1000, height=100, bd=10, relief="groove")
        self.Loginframe2.grid(row=2,column=0,pady=15) 

        self.Loginframe3= Frame(self.frame,width = 1000, height=200, bd=10, relief="groove")
        self.Loginframe3.grid(row=6,column=0,pady=5) 

        self.button_reg = Button(self.Loginframe3,text="Patient Registration Window",font=("arial",15,"bold"),command=self.Registration_window)
        self.button_reg.grid(row=0,column=0,padx=10,pady=10)
        
        self.button_Dr_app = Button(self.Loginframe3,text="Patient Registration Window",font=("arial",15,"bold"),command=self.Dr_Appointment_window)
        self.button_Dr_app.grid(row=0,column=1,padx=10,pady=10)
        
        self.button_med_stock = Button(self.Loginframe3,text="Patient Registration Window",font=("arial",15,"bold"),command=self.Medicine_stock)
        self.button_med_stock.grid(row=1,column=0,padx=10,pady=10)
        
        self.button_Hos = Button(self.Loginframe3,text="Patient Registration Window",font=("arial",15,"bold"),command=self.Hospital_window)
        self.button_Hos.grid(row=1,column=1,padx=10,pady=10)

    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)

    def Dr_Appointment_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)

    def Medicine_stock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)  

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)
      
    




class windows2:
    def __init__(self,master):
        self.master=master
        self.master.title("Patient Management System ")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()


class windows3:
    def __init__(self,master):
        self.master=master
        self.master.title("Doctor Management System ")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()



class windows4:
    def __init__(self,master):
        self.master=master
        self.master.title("Medicine Management System ")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()                



class windows5:
    def __init__(self,master):
        self.master=master
        self.master.title("Hospital Management System ")
        self.master.geometry("1350x750+0+0")
        self.frame = Frame(self.master)
        self.frame.pack()



if __name__=="__main__":
    main()