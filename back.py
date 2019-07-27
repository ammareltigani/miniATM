class ATM:
    def __init__(self, userBalance):
        self.currentBalance = userBalance
        
    def deposit(self, amount):
        self.amount = amount
        self.currentBalance += int(self.amount)

    def withdraw(self, amount):
        self.amount = amount
        self.currentBalance -= int(self.amount)

    def display(self):
        return self.currentBalance

    def message(self):
        if self.currentBalance < 0:
            self.currentBalance += int(self.amount)
            return 'You do not have sufficient funds'
        else:
            return 'Success!'
       

