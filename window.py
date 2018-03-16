from tkinter import *
import os

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title('Login')

        #Labels
        welcome = Label(master, text='Welcome to AFT Cash Register!')
        welcome.grid(columnspan=2, row=0, column=0) 
        
        intruction = Label(master, text='Please log in') 
        intruction.grid(row=1, column=0, sticky=E) 
 
        nameL = Label(master, text='Username: ') 
        pwordL = Label(master, text='Pin number: ') 
        nameL.grid(row=2, column=0, sticky=W) 
        pwordL.grid(row=3, column=0, sticky=W) 

        #Entries
        nameE = Entry(master) 
        pwordE = Entry(master, show='*')
        nameE.grid(row=2, column=1) 
        pwordE.grid(row=3, column=1)

        #Buttons
        loginB = Button(master, text='Log in')
        createAccountB = Button(master, text="Create an Account!")
        loginB.grid(row=4, column=0)
        createAccountB.grid(row=4, column=1)
        
        master.mainloop()

    def checkLogin():
        #Check the values of the login fields in the database
        pass
    def signup():
        #open a new screen that allows user to create account
        pass
        

root = Tk() 
LoginWindow(root)
