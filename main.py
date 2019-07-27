from tkinter import *
from back import *

class Window(Frame):

    def __init__(self, startingBalance, master=None):
        Frame.__init__(self, master)
        self.atm = ATM(startingBalance)
        self.master = master
        self.init_window()
        self.balance()
        self.entries()
        self.buttons()

    def init_window(self):    
        self.master.title("ATM Module")
        self.pack(fill=BOTH, expand=1)
        self.topFrame = Frame(self)
        self.mainLabel = Label(self, text="Welcome to Chase Banking ATM")
        self.mainLabel.pack()
        self.canvas = Canvas(self, width=300, height=100, bd=0, highlightthickness=0)
        self.canvas.create_text(145, 30, text='Please Select an Activity')
        self.canvas.pack()

    def buttons(self):
        buttonLabel = Label(self, text='Finished with your\n transaction?')
        buttonLabel.place(x=280, y=300)
        self.yesButton = Button(self, text="Yes", command= self.client_execute)
        self.yesButton.place(x=321, y=360)
        self.noButton = Button(self, text="EXIT", fg='red', command = self.destroy)
        self.noButton.place(x=318, y=400)

    def entries(self):
        self.depositLabel = Label(self, text='Deposit')
        self.depositLabel.pack()
        self.deposit = Entry(self)
        self.deposit.pack()
        self.withdrawLabel = Label(self, text='Withdraw')
        self.withdrawLabel.pack()
        self.withdraw = Entry(self)
        self.withdraw.pack()

    def balance(self):
        self.currentBalance = Message(self, text='Your starting balance is %s' %self.atm.display(), width=300)
        self.currentBalance.pack()
        
    def client_execute(self):
        if len(self.withdraw.get()) != 0:
            self.atm.withdraw(self.withdraw.get())
            self.withdraw.delete(0, 'end')
        if len(self.deposit.get()) != 0:
            self.atm.deposit(self.deposit.get())
            self.deposit.delete(0, 'end')
        self.msg = Message(self, text=self.atm.message(), width=300)
        self.msg.place(x=50, y=320)

        self.currentBalance = Message(self, text='Your current balance is %s' %self.atm.display(), width=300)
        self.currentBalance.pack()


        
            
starting_money = int(input('How much money would you like to start with?'))
root = Tk()
root.geometry("420x458")
GUI = Window(starting_money, root)
root.mainloop()  
