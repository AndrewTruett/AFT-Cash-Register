import tkinter as tk
from tkinter import *

LARGE_FONT = ("Verdana",24)
NORMAL_FONT = ("Verdana",14)

class CashRegister(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self,"Cash Register")  #title of the software
        
        self.state("zoomed")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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
        
        purchaseInfoFrame = PurchaseInfoFrame(container, self)
        purchaseInfoFrame.grid(row=0, column=1, sticky="NE")

        checkoutFrame = CheckoutFrame(container, self)
        checkoutFrame.grid(row=1, column=1, sticky="N")
        #More frames go here
        


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


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
        self.lb.insert(0, "xyz")
   

        self.yscroll = Scrollbar(self, orient=VERTICAL)
        self.lb["yscrollcommand"] = self.yscroll.set
        self.yscroll["command"] = self.lb.yview

        self.lb.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="N")
        self.yscroll.grid(row=1, column=0, rowspan=2, columnspan=2, sticky="NE")

        #Edit and Remove Buttons
        self.editButton = Button(self, text="Edit", font=NORMAL_FONT, bg="grey")#***Needs command***
        self.removeButton = Button(self, text="Remove", font=NORMAL_FONT, bg="grey", command=lambda: self.removeItem())

        self.editButton.grid(row=3, column=0, pady=10)
        self.removeButton.grid(row=3, column=1, pady=10)

    def removeItem(self):
        #get price of item, reduce the total cost
        #Reducing cost may involve generating an event that the frame that displays the current total would listen for.
        self.lb.delete(ANCHOR)
        
        
        
        
        
class CheckoutFrame(tk.Frame):  
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Total Label
        self.totalLabel = Label(self, text="Total:", font=NORMAL_FONT)
        self.totalLabel.grid(row=0, column=0)

        #Total Amt Label
        self.totalAmtLabel = Label(self, text="0", font=NORMAL_FONT)
        self.totalAmtLabel.grid(row=0, column=1)
        
        #Checkout Label
        self.checkoutLabel = Label(self, text="Checkout", font=NORMAL_FONT)
        self.checkoutLabel.grid(row=1, column=0, columnspan=2)

        #Checkout Buttons
        self.cashButton = Button(self, text="Cash", font=NORMAL_FONT, bg="grey")#***Needs command***
        self.cardButton = Button(self, text="Card", font=NORMAL_FONT, bg="grey")#***Needs command***

        self.cashButton.grid(row=2, column=0, pady=10)
        self.cardButton.grid(row=2, column=1)

    def getTotal(self):
        print(self.totalAmtLabel.cget("text"))

    def payCash(self):
        #Open a small window which just inputs the amnt of cash recieved
        pass
    def payCard(self):
        #Open small window which just has a button that says swipe card
        pass
    


app = CashRegister()
app.mainloop()
