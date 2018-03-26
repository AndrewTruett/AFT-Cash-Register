import tkinter as tk
from tkinter import *

import random
import time

LARGE_FONT = ("Verdana",24)
NORMAL_FONT = ("Verdana",14)

class CashRegister(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self,"Cash Register")  #title of the software
        
        self.state("zoomed")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        #test - need to update
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        '''self.frames = {}
        for F in (StartPage,PageOne,PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)'''

        #frame1 = StartPage(container, self)
        #frame2 = PageOne(container, self)
        #frame1.grid(row=0, column=0, sticky="nw")
        #frame2.grid(row=0, column=1, sticky="ne")

        #More frames go here
        scanFrame = ScanFrame(container, self)
        scanFrame.grid(row=0, column=0, sticky="NW")

        ##Numpad Frame
        numpadFrame = NumpadFrame(container,self)
        numpadFrame.grid(row=2,column=0, sticky="NW")
        
        purchaseInfoFrame = PurchaseInfoFrame(container, self)
        purchaseInfoFrame.grid(row=0, column=3, rowspan=4, sticky="NE")

        #buttonFrame = ButtonFrame(container, self)
        #buttonFrame.grid(row=1, column=0, sticky="NW")
        
        

        checkoutFrame = CheckoutFrame(container, self)
        checkoutFrame.grid(row=5, column=3, sticky="N")
        
        


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class ScanFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)

        #Label
        self.scanLabel = Label(self, text="UPC/PLU:", font=NORMAL_FONT)
        self.scanLabel.grid(row=0, column=0)

        #Entry
        self.scanEntry = Entry(self, font=NORMAL_FONT, width=100)
        self.scanEntry.grid(row=0, column=1)

        #Button
        self.scanButton = Button(self, text="Scan", font=NORMAL_FONT, bg="grey")#***Needs command***
        self.scanButton.grid(row=0, column=2, padx=5)

'''class ButtonFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)

        self.itemLookupButton = Button(self, text="Item Lookup", font=NORMAL_FONT)
        self.itemLookupButton.grid(row=0, column=0)

        self.custLookupButton = Button(self, text="Customer Lookup", font=NORMAL_FONT)
        self.custLookupButton.grid(row=0, column=1)'''

class NumpadFrame(tk.Frame):

    def button_press(self,value):  #needs update for "CLR" @frn-self
        # Get the current value in the entry
        entry = self.numpad_entry.get()
        # Put the new value to the right of it
        # If it was 1 and 2 is pressed it is now 12
        # Otherwise the new number goes on the left
        entry = entry+value

        # Clear the entry box
        self.numpad_entry.delete(0, END)

        # Insert the new value going from left to right
        if value is not "CLR":
            self.numpad_entry.insert(0, entry)


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)

        # Will hold the changing value stored in the entry
        self.entry = StringVar(parent, value="")

        # Create the text entry box
        self.numpad_entry = tk.Entry(self,
                                      textvariable=self.entry)
        self.numpad_entry.grid(row=0, columnspan=2)

        #Buttons
        #1st row
        self.seven = Button(self,text="7",font=NORMAL_FONT, bg="white",height=3,width=5, command=lambda: self.button_press('7'))\
            .grid(row=2,column=0,padx=3,pady=3)
        self.eight = Button(self,text="8",font=NORMAL_FONT, bg="white",height=3,width=5, command=lambda: self.button_press('8'))\
            .grid(row=2,column=1,padx=3,pady=3)
        self.nine = Button(self,text="9",font=NORMAL_FONT, bg="white",height=3,width=5, command=lambda: self.button_press('9')).\
            grid(row=2,column=2,padx=3,pady=3)

        # 2nd row
        self.four = Button(self, text="4", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('4')).\
            grid(row=3, column=0,padx=3,pady=3)
        self.five = Button(self, text="5", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('5')).\
            grid(row=3, column=1,padx=3,pady=3)
        self.six = Button(self, text="6", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('6')).\
            grid(row=3, column=2,padx=3,pady=3)

        # 3rd row
        self.one = Button(self, text="1", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('1')).\
            grid(row=4, column=0,padx=3,pady=3)
        self.two = Button(self, text="2", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('2')).\
            grid(row=4, column=1,padx=3,pady=3)
        self.three = Button(self, text="3", font=NORMAL_FONT, bg="white", height=3, width=5, command=lambda: self.button_press('3')).\
            grid(row=4, column=2,padx=3,pady=3)

        #4th row
        self.zero = Button(self, text="0", font=NORMAL_FONT, bg="white", height=3, width=5,
                          command=lambda: self.button_press('0')). \
            grid(row=5, column=0, padx=3, pady=3)
        self.zeroZero = Button(self, text="00", font=NORMAL_FONT, bg="white", height=3, width=5,
                           command=lambda: self.button_press('00')). \
            grid(row=5, column=1, padx=3, pady=3)
        self.decimal = Button(self, text=".", font=NORMAL_FONT, bg="white", height=3, width=5,
                               command=lambda: self.button_press('.')). \
            grid(row=5, column=2, padx=3, pady=3)

        #5th row           #command needs update @frn-self
        self.zero = Button(self, text="CLEAR", font=NORMAL_FONT, bg="white", height=3, width=10,
                           command=lambda: self.button_press('CLR')). \
            grid(row=6, columnspan=3, padx=3, pady=3)





class PurchaseInfoFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        container = tk.Frame(self)

        #Item Labels
        self.itemsLabel = Label(self, text="Items", font=LARGE_FONT)
        self.itemsLabel.grid(row=0, column=0, columnspan=2)

        #Scrollbar and Listbox
        self.lb = Listbox(self, height = 30, font=NORMAL_FONT, selectmode=SINGLE)
        self.lb.insert(0, "abc")#(index, "")
        self.lb.insert(1, "xyz")
   

        self.yscroll = Scrollbar(self, orient=VERTICAL)
        self.lb["yscrollcommand"] = self.yscroll.set
        self.yscroll["command"] = self.lb.yview

        self.lb.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="N")
        self.yscroll.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="NE")

        #Edit and Remove Buttons
        self.voidButton = Button(self, text="Clear Sale", font=NORMAL_FONT, bg="grey", command=lambda: self.clearSale())#***Needs command***
        self.voidButton.grid(row=3, column=0, pady=10)
        
        self.removeButton = Button(self, text="Remove", font=NORMAL_FONT, bg="grey", command=lambda: self.removeItem())
        self.removeButton.grid(row=3, column=1, pady=10)

    def removeItem(self):
        #get price of item, reduce the total cost
        #Reducing cost may involve generating an event that the frame that displays the current total would listen for.
        self.lb.delete(ANCHOR)

    def clearSale(self):
        #set total field to 0
        self.lb.delete(0, END)
        
        
        
        
        
class CheckoutFrame(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Total Label
        self.totalLabel = Label(self, text="Total:", font=NORMAL_FONT)
        self.totalLabel.grid(row=0, column=0)

        #Total Amt Entry
        self.totalAmtEntry = Entry(self, font=NORMAL_FONT, width=10)
        self.totalAmtEntry.insert(END, "0")
        self.totalAmtEntry.configure(state="readonly")#this may possibly be a problem. not sure if we can programmatically change the text in this field if its read only
        self.totalAmtEntry.grid(row=0, column=1)
        
        #Checkout Label
        self.checkoutLabel = Label(self, text="Checkout", font=NORMAL_FONT)
        self.checkoutLabel.grid(row=1, column=0, columnspan=2)

        #Checkout Buttons
        self.cashButton = Button(self, text="Cash", font=NORMAL_FONT, bg="grey", command=lambda: self.payCash())
        self.cardButton = Button(self, text="Card", font=NORMAL_FONT, bg="grey", command=lambda: self.payCard())

        self.cashButton.grid(row=2, column=0, pady=10)
        self.cardButton.grid(row=2, column=1)

    def getTotal(self):
        return self.totalAmtEntry.get()

    def payCash(self):
        #Open a small window which just inputs the amnt of cash recieved
        cashWindow = CashPayment(Tk(), self.getTotal())
        self.completeOrder()
    def payCard(self):
        #Open small window which just has a button that says swipe card
        cardWindow = CardPayment(Tk())
        self.completeOrder()
       
    def completeOrder(self):
        #clear the items, set total to 0 since order is complete
        pass

    

########################################
class LoginWindow(Tk):
    
    def checkLogin(self):
        #Check the values of the login fields in the database
        #If login is correct, open cash register screen

        self.master.destroy()
        app = CashRegister()#for testing just open the cash register
        app.mainloop()
        
        pass

    
    def __init__(self, master):#Constructor
        self.master = master
        master.title('Login')

        #Labels
        welcome = Label(master, text='Welcome to AFT Cash Register!')
        welcome.grid(columnspan=2, row=0, column=0) 
        
        intruction = Label(master, text='Please login') 
        intruction.grid(row=1, column=0, sticky=W) 
 
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
        loginB = Button(master, text='Log in', command=self.checkLogin)
        loginB.grid(row=4, column=0, columnspan=2, pady=5)
        
        master.mainloop()


class CashPayment(Tk):
    
    def __init__(self, master, totalAmount):#Constructor
        self.master = master
        master.title('Cash Payment')

        self.totalAmount = totalAmount

        #Label
        self.totalLabel = Label(master, text="Total:", font=NORMAL_FONT)
        self.totalLabel.grid(row=0, column=0, sticky="W")

        self.paymentLabel = Label(master, text="Amount Payed:", font=NORMAL_FONT)
        self.paymentLabel.grid(row=1, column=0, sticky="W")

        self.changeLabel = Label(master, text="Change:", font=NORMAL_FONT)
        self.changeLabel.grid(row=2, column=0, sticky="W")

        #Entries
        self.totalEntry = Entry(master, font=NORMAL_FONT)
        self.totalEntry.insert(0, str(self.totalAmount))
        self.totalEntry.configure(state="readonly")#this may possibly be a problem. not sure if we can programmatically change the text in this field if its read only
        self.totalEntry.grid(row=0, column=1)

        self.paymentEntry = Entry(master, font=NORMAL_FONT)
        self.paymentEntry.grid(row=1, column=1, pady=5)

        self.changeEntry = Entry(master, font=NORMAL_FONT)
        self.changeEntry.configure(state="readonly")#this may possibly be a problem. not sure if we can programmatically change the text in this field if its read only
        #changeEntry.insert(0, the amount of change)
        self.changeEntry.grid(row=2, column=1)

        #Button
        self.makeChangeButton = Button(master, text="Make Change")#***Needs command***
        self.makeChangeButton.grid(row=3, column=0, rowspan=2, pady=5)

        master.mainloop()

class CardPayment(Tk):
    
    def __init__(self, master):#Constructor
        self.master = master
        master.title('Card Payment')

        self.numDigits = 0

        #Labels
        self.swipeCardLabel = Label(master, text="Swipe Card", font=NORMAL_FONT)
        self.swipeCardLabel.grid(row=0, column=0, columnspan=3)
        
        self.cardNumLabel = Label(master, text="Card Number:", font=NORMAL_FONT)
        self.cardNumLabel.grid(row=1, column=0, padx=5, pady=5)

        #Entry
        self.cardNumEntry = Entry(master, font=NORMAL_FONT)
        self.cardNumEntry.grid(row=1, column=1)

        #Button
        self.swipeButton = Button(master, text="Swipe", font=NORMAL_FONT, command=lambda: self.cardSwipe())
        self.swipeButton.grid(row=1, column=2, padx=5)

        self.completeButton = Button(master, text="Complete", font=NORMAL_FONT, command=lambda: self.master.destroy())
        self.completeButton.grid(row=2, column=0, columnspan=3, pady=5)

    def cardSwipe(self):
        self.cardNumEntry.delete(0, END)
        self.numDigits = 0
        self.addDigit()

    def addDigit(self):
        if self.numDigits > 16:
            return
        else:
            self.cardNumEntry.insert(END, random.randint(0,9))
            self.numDigits += 1
            self.master.after(10, self.addDigit)
        
        
            
        
        
        
LoginWindow(Tk())
